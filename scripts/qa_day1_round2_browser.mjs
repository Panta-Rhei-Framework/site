import { chromium, devices } from "playwright";

const baseUrl = process.argv[2] || "http://127.0.0.1:4178";
const queries = [
  "Hubble",
  "prime polarity",
  "Book V",
  "ring axioms",
  "consciousness",
  "climate",
  "TauLib",
  "falsification",
  "research notes",
  "Corpus",
  "Bibliography",
];

async function waitForSearchInput(page) {
  const input = page.locator("#search-container .pagefind-ui__search-input").first();
  await input.waitFor({ state: "visible", timeout: 10000 });
  return input;
}

async function openFromTrigger(page, trigger) {
  await trigger.click();
  await page.locator("#search-overlay:not([hidden])").waitFor({ timeout: 5000 });
  const input = await waitForSearchInput(page);
  await input.evaluate((el) => document.activeElement === el || Promise.reject(new Error("search input did not receive focus")));
  return input;
}

async function closeWithEscape(page, trigger) {
  await page.keyboard.press("Escape");
  await page.waitForFunction(() => document.querySelector("#search-overlay")?.hidden === true, null, { timeout: 5000 });
  await trigger.evaluate((el) => document.activeElement === el || Promise.reject(new Error("focus did not return to search trigger")));
}

async function closeWithBackdrop(page) {
  const point = await page.evaluate(() => {
    const candidates = [
      [8, 8],
      [window.innerWidth - 8, 8],
      [8, window.innerHeight - 8],
      [window.innerWidth - 8, window.innerHeight - 8],
      [Math.floor(window.innerWidth / 2), window.innerHeight - 8],
    ];
    for (const [x, y] of candidates) {
      if (document.elementFromPoint(x, y)?.classList.contains("search-overlay-backdrop")) return { x, y };
    }
    return null;
  });
  if (!point) {
    console.log("  Backdrop click skipped: no exposed backdrop point in this viewport.");
    await closeWithButton(page);
    return;
  }
  await page.mouse.click(point.x, point.y);
  await page.waitForFunction(() => document.querySelector("#search-overlay")?.hidden === true, null, { timeout: 5000 });
}

async function closeWithButton(page) {
  await page.locator(".search-overlay-close").click();
  await page.waitForFunction(() => document.querySelector("#search-overlay")?.hidden === true, null, { timeout: 5000 });
}

async function testFocusTrap(page) {
  const closeButton = page.locator(".search-overlay-close");
  const googleLink = page.locator("#search-google-link");
  await closeButton.focus();
  await page.keyboard.press("Shift+Tab");
  await googleLink.evaluate((el) => document.activeElement === el || Promise.reject(new Error("Shift+Tab did not wrap to last modal control")));
  await page.keyboard.press("Tab");
  await closeButton.evaluate((el) => document.activeElement === el || Promise.reject(new Error("Tab did not wrap to first modal control")));
}

async function runQuery(page, query) {
  const input = await waitForSearchInput(page);
  await input.fill(query);
  await page.waitForTimeout(450);
  const googleHref = await page.locator("#search-google-link").getAttribute("href");
  const expected = encodeURIComponent(`site:panta-rhei.site ${query}`);
  if (!googleHref || !googleHref.includes(expected)) {
    throw new Error(`Google fallback did not encode query "${query}": ${googleHref}`);
  }
  const results = page.locator(".pagefind-ui__result-link");
  await results.first().waitFor({ state: "visible", timeout: 10000 });
  const count = await results.count();
  if (count < 1) throw new Error(`No Pagefind results for query "${query}"`);
  const first = (await results.first().innerText()).trim();
  return { query, count, first };
}

async function verifySocialLinks(page) {
  const expectedLabels = [
    "GitHub organization",
    "LinkedIn profile",
    "Bluesky profile",
    "Mastodon profile",
    "Amazon author page and books",
    "Zenodo records",
  ];
  for (const label of expectedLabels) {
    const links = page.locator(`a.social-icon[aria-label="${label}"][title="${label}"]`);
    const count = await links.count();
    if (!count) throw new Error(`Social link "${label}" was not rendered`);
    let focusedVisible = false;
    for (let index = 0; index < count; index += 1) {
      const link = links.nth(index);
      const href = await link.getAttribute("href");
      if (!href) throw new Error(`Social link "${label}" has no href`);
      if (await link.isVisible()) {
        await link.focus();
        await link.evaluate((el) => document.activeElement === el || Promise.reject(new Error(`Social link "${label}" cannot receive focus`)));
        focusedVisible = true;
      }
    }
    if (!focusedVisible) throw new Error(`No visible focusable instance for social link "${label}"`);
  }
}

async function runViewport(browser, name, contextOptions) {
  const context = await browser.newContext(contextOptions);
  const page = await context.newPage();
  const consoleErrors = [];
  const pageErrors = [];
  page.on("console", (msg) => {
    if (msg.type() === "error") consoleErrors.push(msg.text());
  });
  page.on("pageerror", (err) => pageErrors.push(err.message));

  await page.goto(`${baseUrl}/`, { waitUntil: "networkidle" });
  await verifySocialLinks(page);

  const headerTrigger = page.locator(".header-search").first();
  let input = await openFromTrigger(page, headerTrigger);
  await closeWithEscape(page, headerTrigger);

  input = await openFromTrigger(page, headerTrigger);
  await testFocusTrap(page);
  await closeWithButton(page);

  const footerTrigger = page.locator(".footer-link-button", { hasText: "Search" }).first();
  input = await openFromTrigger(page, footerTrigger);
  await closeWithBackdrop(page);

  input = await openFromTrigger(page, headerTrigger);
  const results = [];
  for (const query of queries) results.push(await runQuery(page, query));

  await input.fill("TauLib");
  await page.waitForTimeout(450);
  await page.keyboard.press("ArrowDown");
  await page.keyboard.press("Enter");
  await page.waitForLoadState("networkidle").catch(() => {});

  if (consoleErrors.length || pageErrors.length) {
    throw new Error(`${name} browser errors:\n${[...consoleErrors, ...pageErrors].join("\n")}`);
  }

  await context.close();
  return { name, results };
}

const browser = await chromium.launch();
try {
  const desktop = await runViewport(browser, "desktop", { viewport: { width: 1440, height: 1000 } });
  const mobile = await runViewport(browser, "mobile", { ...devices["iPhone 14"], isMobile: true });
  for (const report of [desktop, mobile]) {
    console.log(`${report.name}: search modal, focus, fallback, social links, and ${queries.length} queries passed`);
    for (const result of report.results) {
      console.log(`  ${result.query}: ${result.count} results; first "${result.first}"`);
    }
  }
} finally {
  await browser.close();
}
