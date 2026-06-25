import { readFile } from "node:fs/promises";
import path from "node:path";

const root = process.cwd();
const localEnvPath = path.join(root, ".env.deploy.local");

async function loadLocalEnv() {
  const content = await readFile(localEnvPath, "utf8").catch(() => "");
  for (const line of content.split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#") || !trimmed.includes("=")) {
      continue;
    }
    const [key, ...valueParts] = trimmed.split("=");
    const value = valueParts.join("=").trim();
    if (key && value && !process.env[key]) {
      process.env[key] = value;
    }
  }
}

await loadLocalEnv();

const apiKey = process.env.IONOS_API_KEY;

if (!apiKey) {
  console.error("IONOS_API_KEY is not set. Add it to your shell environment or .env.deploy.local.");
  process.exit(1);
}

const response = await fetch("https://api.hosting.ionos.com/dns/v1/zones", {
  headers: {
    "X-API-Key": apiKey,
    Accept: "application/json"
  }
});

if (!response.ok) {
  const text = await response.text();
  console.error(`IONOS API check failed: ${response.status} ${response.statusText}`);
  console.error(text.slice(0, 600));
  process.exit(1);
}

const zones = await response.json();
const zoneCount = Array.isArray(zones) ? zones.length : 0;

console.log(`IONOS API check passed. DNS zones visible: ${zoneCount}.`);
console.log("Note: this API verifies IONOS API access; static webspace upload still uses SFTP/SSH.");
