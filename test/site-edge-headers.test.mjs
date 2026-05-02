import assert from "node:assert/strict";
import { applyEdgeHeaders, corsPreflightResponse, edgeRedirectFor } from "../workers/site-edge-headers.js";

const SECURITY_EXPECTATIONS = {
  "X-Content-Type-Options": "nosniff",
  "X-Frame-Options": "DENY",
  "Referrer-Policy": "strict-origin-when-cross-origin",
  "Permissions-Policy": "camera=(), microphone=(), geolocation=()"
};

function originResponse(contentType = "text/html; charset=utf-8") {
  return new Response("ok", {
    status: 200,
    headers: {
      "Content-Type": contentType,
      "Cache-Control": "max-age=600"
    }
  });
}

function apply(path, contentType) {
  return applyEdgeHeaders(`https://panta-rhei.site${path}`, originResponse(contentType));
}

function assertSecurityHeaders(response) {
  for (const [name, value] of Object.entries(SECURITY_EXPECTATIONS)) {
    assert.equal(response.headers.get(name), value, `${name} should be enforced`);
  }

  assert.match(response.headers.get("Link"), /rel="sitemap"/);
  assert.match(response.headers.get("Link"), /rel="license"/);
  assert.match(response.headers.get("Link"), /rel="service-doc"/);
}

const cases = [
  ["/", "text/html; charset=utf-8", "public, max-age=3600, must-revalidate"],
  ["/program/", "text/html; charset=utf-8", "public, max-age=3600, must-revalidate"],
  ["/research-program/index.html", "text/html; charset=utf-8", "public, max-age=3600, must-revalidate"],
  ["/assets/css/site.css", "text/css", "public, max-age=31536000, immutable"],
  ["/assets/site.webmanifest", "application/manifest+json", "public, max-age=604800"],
  ["/pagefind/pagefind.js", "text/javascript", "public, max-age=31536000, immutable"],
  ["/sitemap.xml", "application/xml", "public, max-age=86400"],
  ["/robots.txt", "text/plain", "public, max-age=86400"],
  ["/api/plates.json", "text/plain", "public, max-age=3600, stale-while-revalidate=86400"]
];

for (const [path, contentType, expectedCacheControl] of cases) {
  const response = apply(path, contentType);
  assert.equal(response.headers.get("Cache-Control"), expectedCacheControl, `${path} cache policy`);
  assertSecurityHeaders(response);
}

// CORS endpoints: /api/* should be cross-site-fetchable with CC BY 4.0 content
{
  const apiResponse = apply("/api/plates.json", "text/plain");
  assert.equal(apiResponse.headers.get("Access-Control-Allow-Origin"), "*", "/api/* should allow cross-origin GET");
  assert.equal(apiResponse.headers.get("Access-Control-Allow-Methods"), "GET, HEAD, OPTIONS", "/api/* should advertise simple methods");
  assert.equal(apiResponse.headers.get("Access-Control-Allow-Headers"), "Content-Type", "/api/* should allow Content-Type header");
  assert.equal(apiResponse.headers.get("Access-Control-Max-Age"), "86400", "/api/* preflight should cache for 24h");
  assert.equal(apiResponse.headers.get("Content-Type"), "application/json; charset=utf-8", "/api/*.json should override Content-Type to JSON");
}

// Negative CORS cases — non-/api/ paths must NOT receive CORS headers
for (const negativePath of ["/", "/results/", "/assets/css/site.css", "/sitemap.xml"]) {
  const negResponse = apply(negativePath, "text/html");
  assert.equal(negResponse.headers.get("Access-Control-Allow-Origin"), null, `${negativePath} must not be CORS-permissive`);
}

// CORS preflight: OPTIONS /api/* must short-circuit with 204 + full CORS contract
{
  const preflight = corsPreflightResponse(new URL("https://panta-rhei.site/api/plates.json"));
  assert.ok(preflight, "OPTIONS /api/plates.json should short-circuit with a Response");
  assert.equal(preflight.status, 204, "preflight should be 204 No Content");
  const decorated = applyEdgeHeaders("https://panta-rhei.site/api/plates.json", preflight);
  assert.equal(decorated.headers.get("Access-Control-Allow-Origin"), "*", "preflight must carry Allow-Origin: *");
  assert.equal(decorated.headers.get("Access-Control-Allow-Methods"), "GET, HEAD, OPTIONS", "preflight must advertise simple methods");
  assert.equal(decorated.headers.get("Access-Control-Max-Age"), "86400", "preflight must cache for 24h");
}

// Negative preflight: OPTIONS / must NOT short-circuit (falls through to origin → 405)
assert.equal(corsPreflightResponse(new URL("https://panta-rhei.site/")), null, "OPTIONS / must not short-circuit (no broad preflight)");

for (const path of ["/publications/physics-ledger", "/publications/physics-ledger/", "/publications/numerical-physics-ledger/"]) {
  const redirect = edgeRedirectFor(`https://panta-rhei.site${path}`);
  assert.ok(redirect, `${path} should redirect at the edge`);
  assert.equal(redirect.status, 301, `${path} should be permanent`);
  assert.equal(
    redirect.headers.get("Location"),
    "https://panta-rhei.site/publications/monograph-supplements/numerical-physics-ledger/",
    `${path} redirect target`
  );
}

for (const [path, target] of [
  ["/publications/categorical-genesis", "/publications/monograph-supplements/categorical-genesis/"],
  ["/publications/categorical-genesis/", "/publications/monograph-supplements/categorical-genesis/"],
  ["/publications/companion-papers", "/publications/research-briefings/public-good/"],
  ["/publications/companion-papers/", "/publications/research-briefings/public-good/"],
  [
    "/publications/books/book-i/part-01-the-coherence-kernel/",
    "/corpus/monographs/book-i/part-01-the-coherence-kernel/"
  ],
  [
    "/publications/books/book-i/part-01-the-coherence-kernel/chapter-02-the-five-generators/",
    "/corpus/monographs/book-i/part-01-the-coherence-kernel/chapter-02-the-five-generators/"
  ],
  ["/verify/taulib/docs/book-i/", "/corpus/taulib/docs/book-i/"],
  [
    "/verify/taulib/docs/book-iii-arithmetic-abcconjecture/",
    "/corpus/taulib/docs/book-iii-arithmetic-abcconjecture/"
  ],
  ["/framework", "/corpus/"],
  ["/framework/about/", "/corpus/"],
  ["/framework/mathematics-coherence-kernel/", "/corpus/"],
  [
    "/framework/prior-art/wolfram/",
    "/program/research-agenda/kernel-model-reality/related-approaches/deep-comparison/"
  ]
]) {
  const redirect = edgeRedirectFor(`https://panta-rhei.site${path}`);
  assert.ok(redirect, `${path} should redirect at the edge`);
  assert.equal(redirect.status, 301, `${path} should be permanent`);
  assert.equal(redirect.headers.get("Location"), `https://panta-rhei.site${target}`, `${path} redirect target`);
}

assert.equal(edgeRedirectFor("https://panta-rhei.site/publications/monograph-supplements/numerical-physics-ledger/"), null);
assert.equal(edgeRedirectFor("https://panta-rhei.site/publications/books/book-i/"), null);
assert.equal(edgeRedirectFor("https://panta-rhei.site/verify/taulib/docs/"), null);

console.log(`site-edge-headers: ${cases.length} header cases, 5 CORS assertions, 4 CORS-negative cases, 4 preflight assertions, and 15 redirect cases passed`);
