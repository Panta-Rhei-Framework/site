#!/usr/bin/env node

import { chromium } from "@playwright/test";
import { createServer } from "node:http";
import { mkdir, readFile, stat } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const rootDir = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const siteDir = path.resolve(rootDir, process.env.VISUAL_QA_SITE_DIR || "_site");
const outputDir = path.resolve(rootDir, process.env.VISUAL_QA_OUTPUT_DIR || ".visual-qa");
const explicitBaseUrl = process.env.VISUAL_QA_BASE_URL;

const viewports = [
  { name: "desktop", width: 1440, height: 1000 },
  { name: "mobile", width: 390, height: 844 },
];

const pages = [
  { name: "home", url: "/", expect: ["Panta Rhei Research"] },
  { name: "discover", url: "/discover/", expect: ["Discover"] },
  { name: "program", url: "/program/", expect: ["Program"] },
  { name: "corpus", url: "/corpus/", expect: ["Corpus"] },
  { name: "registry", url: "/corpus/registry/", expect: ["Registry"] },
  { name: "results", url: "/results/", expect: ["Results"] },
  { name: "results-progress", url: "/results/progress-against-agenda/", expect: ["Progress Against Agenda"] },
  { name: "verify", url: "/verify/", expect: ["Verify"] },
  { name: "verify-spine", url: "/verify/construction-spine-verification/", expect: ["Verify the Construction Spine"] },
  { name: "publications", url: "/publications/", expect: ["Publications"] },
  { name: "research-notes", url: "/publications/research-notes/", expect: ["Research Notes", "Browse Research Notes"] },
  {
    name: "research-note-chirality",
    url: "/publications/research-notes/structural-prior-dynamic-chirality-induced-spin-selectivity/",
    expect: ["A Structural Prior", "Claim Boundary", "Download PDF"],
  },
  {
    name: "research-note-inflation",
    url: "/publications/research-notes/inflationary-observables-without-an-inflaton/",
    expect: ["Inflationary Observables", "Verification Surface", "Download PDF"],
  },
  { name: "impact", url: "/impact/", expect: ["Impact"] },
  { name: "impact-framework", url: "/impact/impact-framework/", expect: ["Verification survival", "Translation layer", "Domain uptake"] },
  { name: "impact-foundational-science", url: "/impact/foundational-science/", expect: ["Foundational Science", "Reading discipline"] },
  { name: "impact-applied-science", url: "/impact/applied-science-and-research/", expect: ["Applied Science", "Reading discipline"] },
  { name: "impact-global-education", url: "/impact/global-education/", expect: ["Global Education", "Reading discipline"] },
  { name: "impact-existential-orientation", url: "/impact/existential-orientation/", expect: ["Existential Orientation", "Reading discipline"] },
  { name: "impact-societal-coherence", url: "/impact/societal-coherence/", expect: ["Societal Coherence", "Reading discipline"] },
  { name: "impact-global-public-good", url: "/impact/global-public-good/", expect: ["Global Public Good", "conditional public-good portfolio"] },
  { name: "impact-portfolio-agriculture", url: "/impact/portfolio/agriculture/", expect: ["Agriculture", "Portfolio status", "Public-Good Briefings"] },
  { name: "engage", url: "/engage/", expect: ["Engagement without endorsement", "structured open-research engagement"] },
  { name: "engage-discussions", url: "/engage/discussions/", expect: ["Public Discussions", "GitHub Discussions", "Participation does not imply endorsement"] },
  { name: "engage-how-to-engage", url: "/engage/how-to-engage/", expect: ["How to Engage", "Discussions, Issues, Pull Requests, Email"] },
  { name: "engage-review-the-work", url: "/engage/review-the-work/", expect: ["Review the Work", "Review modes", "What to include"] },
  { name: "engage-contact", url: "/engage/contact/", expect: ["Contact", "Before contacting us", "Use public GitHub Discussions"] },
  { name: "engage-engineering-contributors", url: "/engage/for-engineering-contributors/", expect: ["For Engineering Contributors", "GitHub workflow"] },
  { name: "engage-support", url: "/engage/support-the-research/", expect: ["Support without endorsement", "Participation does not imply endorsement"] },
  { name: "engage-media", url: "/engage/media/", expect: ["Responsible communication", "externally accepted scientific conclusions"] },
  { name: "result-hubble", url: "/results/problem/hubble-tension/", expect: ["Hubble"] },
  { name: "registry-object", url: "/registry/object/VII.T16/", expect: ["VII.T16"] },
  { name: "publication-ledger", url: "/publications/monograph-supplements/numerical-physics-ledger/", expect: ["Numerical Physics Ledger", "Monograph Supplement"] },
  { name: "publications-monograph-supplements", url: "/publications/monograph-supplements/", expect: ["Monograph Supplements", "Categorical Genesis"] },
  { name: "publications-research-briefings", url: "/publications/research-briefings/", expect: ["Research Briefings", "Public-Good Briefings"] },
  { name: "publications-public-good-briefings", url: "/publications/research-briefings/public-good/", expect: ["Public-Good Briefings", "Reading discipline"] },
  {
    name: "public-good-briefing-fission",
    url: "/publications/research-briefings/public-good/advanced-fission-safety-operations-licensing-fleet-modernization/",
    expect: ["Abstract", "Key Takeaways", "Read full text as HTML"],
  },
];

const mimeTypes = new Map([
  [".css", "text/css; charset=utf-8"],
  [".html", "text/html; charset=utf-8"],
  [".js", "text/javascript; charset=utf-8"],
  [".json", "application/json; charset=utf-8"],
  [".svg", "image/svg+xml"],
  [".png", "image/png"],
  [".jpg", "image/jpeg"],
  [".jpeg", "image/jpeg"],
  [".webp", "image/webp"],
  [".woff2", "font/woff2"],
  [".xml", "application/xml; charset=utf-8"],
  [".txt", "text/plain; charset=utf-8"],
]);

async function fileExists(filePath) {
  try {
    await stat(filePath);
    return true;
  } catch {
    return false;
  }
}

function screenshotName(viewportName, pageName, suffix = "page") {
  return `${viewportName}-${pageName}-${suffix}.png`.replace(/[^a-z0-9_.-]+/gi, "-");
}

async function resolveStaticPath(requestUrl) {
  const parsed = new URL(requestUrl, "http://127.0.0.1");
  const decodedPath = decodeURIComponent(parsed.pathname);
  let candidate = path.resolve(siteDir, `.${decodedPath}`);

  if (!candidate.startsWith(siteDir)) {
    return null;
  }

  try {
    const info = await stat(candidate);
    if (info.isDirectory()) {
      candidate = path.join(candidate, "index.html");
    }
  } catch {
    if (!path.extname(candidate)) {
      candidate = path.join(candidate, "index.html");
    }
  }

  return candidate;
}

async function startStaticServer() {
  if (!(await fileExists(path.join(siteDir, "index.html")))) {
    throw new Error(`Missing ${path.join(siteDir, "index.html")}. Run the Jekyll build before visual QA.`);
  }

  const server = createServer(async (req, res) => {
    try {
      const filePath = await resolveStaticPath(req.url || "/");
      if (!filePath) {
        res.writeHead(403);
        res.end("Forbidden");
        return;
      }

      const body = await readFile(filePath);
      const type = mimeTypes.get(path.extname(filePath)) || "application/octet-stream";
      res.writeHead(200, { "Content-Type": type });
      res.end(body);
    } catch {
      res.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
      res.end("Not found");
    }
  });

  await new Promise((resolve, reject) => {
    server.once("error", reject);
    server.listen(0, "127.0.0.1", () => {
      server.off("error", reject);
      resolve();
    });
  });
  const address = server.address();
  return {
    baseUrl: `http://127.0.0.1:${address.port}`,
    close: () => new Promise((resolve) => server.close(resolve)),
  };
}

function pageUrl(baseUrl, pagePath) {
  return new URL(pagePath, `${baseUrl}/`).toString();
}

async function inspectPage(page) {
  return page.evaluate(() => {
    const main = document.querySelector("main");
    const header = document.querySelector(".site-header");
    const footer = document.querySelector(".site-footer");
    const h1 = document.querySelector("h1");
    const mainRect = main ? main.getBoundingClientRect() : null;

    return {
      title: document.title,
      h1: h1 ? h1.textContent.trim() : "",
      mainTextLength: main ? main.innerText.trim().length : 0,
      mainHeight: mainRect ? mainRect.height : 0,
      mainWidth: mainRect ? mainRect.width : 0,
      headerHeight: header ? header.getBoundingClientRect().height : 0,
      footerHeight: footer ? footer.getBoundingClientRect().height : 0,
      scrollWidth: document.documentElement.scrollWidth,
      viewportWidth: window.innerWidth,
      bodyText: document.body.innerText,
    };
  });
}

async function runVisualQa() {
  await mkdir(outputDir, { recursive: true });

  const server = explicitBaseUrl ? null : await startStaticServer();
  const baseUrl = explicitBaseUrl || server.baseUrl;
  const failures = [];
  const screenshots = [];

  const browser = await chromium.launch();
  try {
    for (const viewport of viewports) {
      const context = await browser.newContext({
        viewport: { width: viewport.width, height: viewport.height },
        deviceScaleFactor: 1,
      });

      for (const spec of pages) {
        const page = await context.newPage();
        const consoleErrors = [];
        const pageErrors = [];

        page.on("console", (message) => {
          if (message.type() === "error") {
            consoleErrors.push(message.text());
          }
        });
        page.on("pageerror", (error) => pageErrors.push(error.message));

        const response = await page.goto(pageUrl(baseUrl, spec.url), {
          waitUntil: "networkidle",
          timeout: 30000,
        });

        const inspection = await inspectPage(page);
        const shotPath = path.join(outputDir, screenshotName(viewport.name, spec.name));
        await page.screenshot({ path: shotPath, fullPage: true, timeout: 90000 });
        screenshots.push(shotPath);

        if (!response || response.status() >= 400) {
          failures.push(`${viewport.name}/${spec.name}: HTTP ${response ? response.status() : "no response"}`);
        }
        if (!inspection.h1) {
          failures.push(`${viewport.name}/${spec.name}: missing h1`);
        }
        if (inspection.mainTextLength < 120 || inspection.mainHeight < 160) {
          failures.push(`${viewport.name}/${spec.name}: main content looks too small or blank`);
        }
        if (inspection.headerHeight < 40 || inspection.footerHeight < 40) {
          failures.push(`${viewport.name}/${spec.name}: header or footer did not render`);
        }
        if (inspection.scrollWidth > inspection.viewportWidth + 8) {
          failures.push(`${viewport.name}/${spec.name}: horizontal overflow ${inspection.scrollWidth}px > ${inspection.viewportWidth}px`);
        }
        for (const expected of spec.expect) {
          if (!inspection.bodyText.includes(expected)) {
            failures.push(`${viewport.name}/${spec.name}: missing expected text "${expected}"`);
          }
        }
        if (pageErrors.length) {
          failures.push(`${viewport.name}/${spec.name}: page errors: ${pageErrors.join(" | ")}`);
        }
        if (consoleErrors.length) {
          failures.push(`${viewport.name}/${spec.name}: console errors: ${consoleErrors.join(" | ")}`);
        }

        await page.close();
      }

      const searchPage = await context.newPage();
      await searchPage.goto(pageUrl(baseUrl, "/"), { waitUntil: "networkidle", timeout: 30000 });
      await searchPage.locator(".header-search").click();
      await searchPage.locator("#search-overlay:not([hidden])").waitFor({ timeout: 5000 });
      await searchPage.locator("#search-container input").fill("Hubble");
      await searchPage.waitForTimeout(600);

      const searchState = await searchPage.evaluate(() => {
        const link = document.querySelector("#search-google-link");
        const input = document.querySelector("#search-container input");
        const overlay = document.querySelector("#search-overlay");
        return {
          title: document.querySelector(".search-overlay-title")?.textContent.trim() || "",
          inputValue: input ? input.value : "",
          googleHref: link ? link.href : "",
          overlayVisible: overlay ? !overlay.hidden : false,
          scrollWidth: document.documentElement.scrollWidth,
          viewportWidth: window.innerWidth,
        };
      });

      const searchShot = path.join(outputDir, screenshotName(viewport.name, "search", "overlay"));
      await searchPage.screenshot({ path: searchShot, fullPage: true });
      screenshots.push(searchShot);

      if (searchState.title !== "Search the Site") {
        failures.push(`${viewport.name}/search: unexpected overlay title "${searchState.title}"`);
      }
      if (searchState.inputValue !== "Hubble") {
        failures.push(`${viewport.name}/search: Pagefind input did not accept query`);
      }
      if (!searchState.googleHref.includes("Hubble")) {
        failures.push(`${viewport.name}/search: Google fallback did not sync query`);
      }
      if (!searchState.overlayVisible) {
        failures.push(`${viewport.name}/search: overlay is not visible`);
      }
      if (searchState.scrollWidth > searchState.viewportWidth + 8) {
        failures.push(`${viewport.name}/search: horizontal overflow ${searchState.scrollWidth}px > ${searchState.viewportWidth}px`);
      }

      await searchPage.close();

      const agendaPage = await context.newPage();
      await agendaPage.goto(pageUrl(baseUrl, "/results/progress-against-agenda/"), {
        waitUntil: "networkidle",
        timeout: 30000,
      });

      const filter = (selector) => agendaPage.locator(selector);
      const countValue = async () => {
        const value = await agendaPage.locator("#agenda-progress-count").textContent();
        return Number((value || "").trim());
      };
      const state = async () =>
        agendaPage.evaluate(() => ({
          query: window.location.search,
          emptyVisible: !document.getElementById("agenda-progress-empty")?.hidden,
          activeFilters: Array.from(document.querySelectorAll("#agenda-progress-controls .filter-chip.is-active")).map(
            (el) => `${el.getAttribute("data-filter")}:${el.getAttribute("data-value")}`,
          ),
        }));

      const initialCount = await countValue();
      if (initialCount < 50) {
        failures.push(`${viewport.name}/agenda-progress: unexpected initial count ${initialCount}`);
      }

      await filter('[data-filter="domain"][data-value="physics"]').click();
      await filter('[data-filter="verification_status"][data-value="pending_physics_verification"]').click();
      await agendaPage.waitForTimeout(250);

      const filteredCount = await countValue();
      const filteredState = await state();
      if (!(filteredCount > 0 && filteredCount < initialCount)) {
        failures.push(`${viewport.name}/agenda-progress: physics/pending-physics filter count ${filteredCount} did not narrow from ${initialCount}`);
      }
      if (!filteredState.query.includes("domain=physics") || !filteredState.query.includes("verification_status=pending_physics_verification")) {
        failures.push(`${viewport.name}/agenda-progress: filter query string did not persist expected params`);
      }

      await agendaPage.reload({ waitUntil: "networkidle", timeout: 30000 });
      const reloadedCount = await countValue();
      const reloadedState = await state();
      if (reloadedCount !== filteredCount) {
        failures.push(`${viewport.name}/agenda-progress: reload changed filtered count from ${filteredCount} to ${reloadedCount}`);
      }
      if (
        !reloadedState.activeFilters.includes("domain:physics") ||
        !reloadedState.activeFilters.includes("verification_status:pending_physics_verification")
      ) {
        failures.push(`${viewport.name}/agenda-progress: active filters were not restored after reload`);
      }

      await filter('[data-filter="construction_step"][data-value="build-the-kernel"]').click();
      await agendaPage.waitForTimeout(250);
      const emptyCount = await countValue();
      const emptyState = await state();
      if (emptyCount !== 0 || !emptyState.emptyVisible) {
        failures.push(`${viewport.name}/agenda-progress: empty-state check failed (count ${emptyCount}, emptyVisible ${emptyState.emptyVisible})`);
      }

      await agendaPage.locator("#agenda-progress-clear-filters").click();
      await agendaPage.waitForTimeout(250);
      const resetCount = await countValue();
      const resetState = await state();
      if (resetCount !== initialCount || resetState.query !== "" || resetState.emptyVisible) {
        failures.push(`${viewport.name}/agenda-progress: clear filters did not restore initial state`);
      }

      const agendaShot = path.join(outputDir, screenshotName(viewport.name, "agenda-progress", "page"));
      await agendaPage.screenshot({ path: agendaShot, fullPage: true });
      screenshots.push(agendaShot);
      await agendaPage.close();

      const notesPage = await context.newPage();
      await notesPage.goto(pageUrl(baseUrl, "/publications/research-notes/"), {
        waitUntil: "networkidle",
        timeout: 30000,
      });

      const noteCountValue = async () => {
        const value = await notesPage.locator("#research-notes-count").textContent();
        return Number((value || "").trim());
      };
      const notesState = async () =>
        notesPage.evaluate(() => ({
          query: window.location.search,
          emptyVisible: !document.getElementById("research-notes-empty")?.hidden,
          activeFilters: Array.from(document.querySelectorAll("#research-notes-controls .filter-chip.is-active")).map(
            (el) => `${el.getAttribute("data-filter")}:${el.getAttribute("data-value")}`,
          ),
        }));

      const initialNotesCount = await noteCountValue();
      if (initialNotesCount < 8) {
        failures.push(`${viewport.name}/research-notes: unexpected initial count ${initialNotesCount}`);
      }

      await notesPage.locator('[data-filter="note_type"][data-value="pre-registration-note"]').click();
      await notesPage.locator('[data-filter="domain"][data-value="physics"]').click();
      await notesPage.waitForTimeout(250);

      const filteredNotesCount = await noteCountValue();
      const filteredNotesState = await notesState();
      if (!(filteredNotesCount > 0 && filteredNotesCount < initialNotesCount)) {
        failures.push(`${viewport.name}/research-notes: pre-registration/physics filter count ${filteredNotesCount} did not narrow from ${initialNotesCount}`);
      }
      if (!filteredNotesState.query.includes("note_type=pre-registration-note") || !filteredNotesState.query.includes("domain=physics")) {
        failures.push(`${viewport.name}/research-notes: filter query string did not persist expected params`);
      }

      await notesPage.reload({ waitUntil: "networkidle", timeout: 30000 });
      const reloadedNotesCount = await noteCountValue();
      const reloadedNotesState = await notesState();
      if (reloadedNotesCount !== filteredNotesCount) {
        failures.push(`${viewport.name}/research-notes: reload changed filtered count from ${filteredNotesCount} to ${reloadedNotesCount}`);
      }
      if (
        !reloadedNotesState.activeFilters.includes("note_type:pre-registration-note") ||
        !reloadedNotesState.activeFilters.includes("domain:physics")
      ) {
        failures.push(`${viewport.name}/research-notes: active filters were not restored after reload`);
      }

      await notesPage.locator("#research-notes-clear-filters").click();
      await notesPage.waitForTimeout(250);
      const resetNotesCount = await noteCountValue();
      const resetNotesState = await notesState();
      if (resetNotesCount !== initialNotesCount || resetNotesState.query !== "" || resetNotesState.emptyVisible) {
        failures.push(`${viewport.name}/research-notes: clear filters did not restore initial state`);
      }

      const notesShot = path.join(outputDir, screenshotName(viewport.name, "research-notes", "filters"));
      await notesPage.screenshot({ path: notesShot, fullPage: true });
      screenshots.push(notesShot);
      await notesPage.close();
      await context.close();
    }
  } finally {
    await browser.close();
    if (server) {
      await server.close();
    }
  }

  console.log(`Visual QA checked ${pages.length} pages at ${viewports.length} viewports.`);
  console.log(`Screenshots written to ${path.relative(rootDir, outputDir)}/ (${screenshots.length} files).`);

  if (failures.length) {
    console.error("\nFailures:");
    for (const failure of failures) {
      console.error(`- ${failure}`);
    }
    process.exitCode = 1;
    return;
  }

  console.log("All visual QA checks passed.");
}

runVisualQa().catch((error) => {
  console.error(error.stack || error.message);
  process.exitCode = 1;
});
