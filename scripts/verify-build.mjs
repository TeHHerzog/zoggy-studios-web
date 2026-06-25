import { access, readFile, stat } from "node:fs/promises";
import path from "node:path";

const root = process.cwd();

const requiredSites = [
  {
    name: "studio",
    dir: path.join(root, "dist", "studio"),
    routes: [
      "index.html",
      "404.html",
      path.join("projects", "index.html"),
      path.join("about", "index.html"),
      path.join("updates", "index.html"),
      path.join("contact", "index.html"),
      path.join("privacy", "index.html"),
      path.join("terms", "index.html")
    ]
  },
  {
    name: "darkfantasy",
    dir: path.join(root, "dist", "darkfantasy"),
    routes: ["index.html", "404.html"]
  }
];

const requiredFiles = ["robots.txt", ".htaccess"];
const expectedRobots = "User-agent: *\nDisallow: /";
const expectedHtaccess = ["Options -Indexes", "DirectoryIndex index.html"];

async function assertExists(filePath) {
  await access(filePath);
}

async function assertDirectory(dirPath) {
  const info = await stat(dirPath);
  if (!info.isDirectory()) {
    throw new Error(`${dirPath} exists but is not a directory`);
  }
}

async function verifySite(site) {
  await assertDirectory(site.dir);

  for (const fileName of [...site.routes, ...requiredFiles]) {
    await assertExists(path.join(site.dir, fileName));
  }

  const robots = (await readFile(path.join(site.dir, "robots.txt"), "utf8")).trim();
  if (robots !== expectedRobots) {
    throw new Error(`${site.name} robots.txt does not block indexing during construction`);
  }

  const htaccess = await readFile(path.join(site.dir, ".htaccess"), "utf8");
  for (const line of expectedHtaccess) {
    if (!htaccess.includes(line)) {
      throw new Error(`${site.name} .htaccess missing ${line}`);
    }
  }
}

for (const site of requiredSites) {
  await verifySite(site);
}

console.log("Build verification passed for dist/studio and dist/darkfantasy.");
