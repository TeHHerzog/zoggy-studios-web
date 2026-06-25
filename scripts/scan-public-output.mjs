import { readdir, readFile, stat } from "node:fs/promises";
import path from "node:path";

const root = process.cwd();
const distRoot = path.join(root, "dist");

const siteDirs = [
  path.join(distRoot, "studio"),
  path.join(distRoot, "darkfantasy")
];

const forbiddenPathSegments = [
  ".git",
  "node_modules",
  "src",
  "docs",
  "scripts",
  "config",
  "schemas",
  "packages",
  ".env",
  ".astro",
  ".codegraph"
];

const forbiddenFileNames = [
  ".env",
  "credentials.json",
  "id_rsa",
  "id_ed25519",
  "package-lock.json",
  "pnpm-lock.yaml",
  "yarn.lock"
];

const forbiddenContentPatterns = [
  { label: "private admin route", pattern: /\/admin\//i },
  { label: "private admin panel URL", pattern: /127\.0\.0\.1:9090/i },
  { label: "PostgreSQL reference", pattern: /postgresql/i },
  { label: "DATABASE_URL reference", pattern: /DATABASE_URL/i },
  { label: "private key reference", pattern: /private key/i },
  { label: "local Windows project path", pattern: /C:\\Antigravity\\/i },
  { label: "source map reference", pattern: /sourceMappingURL/i },
  { label: "goroutine reference", pattern: /goroutine/i },
  { label: "raw memory usage reference", pattern: /memory usage/i },
  { label: "process ID reference", pattern: /process ID/i }
];

const crossSitePatterns = [
  {
    dir: path.join(distRoot, "studio"),
    label: "Dark Fantasy route-only copy in studio output",
    pattern: /Lost beyond the veil|Ancient<\/h2>|Corrupted<\/h2>|Cosmic<\/h2>/i
  },
  {
    dir: path.join(distRoot, "darkfantasy"),
    label: "studio route-only copy in darkfantasy output",
    pattern: /Creative Projects|Umbrella studio/i
  }
];

async function walk(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  const files = [];

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...(await walk(fullPath)));
    } else {
      files.push(fullPath);
    }
  }

  return files;
}

function assertSafePath(filePath) {
  const relative = path.relative(distRoot, filePath);
  const parts = relative.split(path.sep);

  for (const part of parts) {
    if (forbiddenPathSegments.includes(part)) {
      throw new Error(`Forbidden path segment copied to dist: ${relative}`);
    }
  }

  if (forbiddenFileNames.includes(path.basename(filePath))) {
    throw new Error(`Forbidden file copied to dist: ${relative}`);
  }
}

async function scanFile(filePath) {
  assertSafePath(filePath);

  const info = await stat(filePath);
  if (info.size > 2_000_000) {
    return;
  }

  const content = await readFile(filePath, "utf8").catch(() => "");
  for (const { label, pattern } of forbiddenContentPatterns) {
    if (pattern.test(content)) {
      throw new Error(`${label} found in ${path.relative(root, filePath)}`);
    }
  }
}

for (const dir of siteDirs) {
  const files = await walk(dir);
  for (const file of files) {
    await scanFile(file);
  }
}

for (const { dir, label, pattern } of crossSitePatterns) {
  const files = await walk(dir);
  for (const file of files) {
    const content = await readFile(file, "utf8").catch(() => "");
    if (pattern.test(content)) {
      throw new Error(`${label} found in ${path.relative(root, file)}`);
    }
  }
}

console.log("Public output scan passed for dist/studio and dist/darkfantasy.");
