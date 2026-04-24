import { readdir, readFile, stat } from "node:fs/promises";
import path from "node:path";

const siteRoot = process.argv[2] || "_site";
const supportPages = [
  "bibliography/index.html",
  "bibliography/browse/index.html",
  "cite/index.html",
  "media/index.html",
  "media/review-kit/index.html",
  "credits/index.html",
  "impressum/index.html",
  "datenschutz/index.html",
  "changelog/index.html",
  "sitemap/index.html",
];

const oldNavLabels = [
  "Research Program",
  "Framework",
  "Claims",
  "Publications",
  "Verify",
  "Impact",
  "Engage",
];

const v2NavLabels = [
  "Discover",
  "Program",
  "Corpus",
  "Results",
  "Verify",
  "Publications",
  "Impact",
  "Engage",
];

async function* walk(dir) {
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      yield* walk(full);
    } else if (entry.isFile() && entry.name.endsWith(".html")) {
      yield full;
    }
  }
}

function extractHeader(html) {
  const match = html.match(/<header\b[\s\S]*?<\/header>/i);
  return match ? match[0] : "";
}

function hasAllLabels(fragment, labels) {
  return labels.every((label) => new RegExp(`>${label}<`).test(fragment));
}

function hasRawMarkdownLink(html) {
  return /\[[^\]\n]{2,}\]\(\/[^)\n]+\)/.test(html);
}

const failures = [];
const rootInfo = await stat(siteRoot).catch(() => null);
if (!rootInfo || !rootInfo.isDirectory()) {
  throw new Error(`Rendered site directory not found: ${siteRoot}`);
}

for await (const file of walk(siteRoot)) {
  const html = await readFile(file, "utf8");
  const rel = path.relative(siteRoot, file);
  const header = extractHeader(html);
  if (header && hasAllLabels(header, oldNavLabels) && !hasAllLabels(header, v2NavLabels)) {
    failures.push(`${rel}: rendered header appears to use the old v1 navigation labels`);
  }
}

for (const rel of supportPages) {
  const file = path.join(siteRoot, rel);
  const html = await readFile(file, "utf8").catch(() => null);
  if (!html) {
    failures.push(`${rel}: expected support page was not rendered`);
    continue;
  }
  const header = extractHeader(html);
  if (!hasAllLabels(header, v2NavLabels)) {
    failures.push(`${rel}: v2 top navigation labels are incomplete`);
  }
  if (hasRawMarkdownLink(html)) {
    failures.push(`${rel}: raw Markdown link syntax is visible in rendered HTML`);
  }
}

if (failures.length) {
  console.error("v2 shell migration check failed:");
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log(`v2 shell migration check passed for ${supportPages.length} support pages.`);
