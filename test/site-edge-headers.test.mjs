import assert from "node:assert/strict";
import { applyEdgeHeaders } from "../workers/site-edge-headers.js";

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
  ["/robots.txt", "text/plain", "public, max-age=86400"]
];

for (const [path, contentType, expectedCacheControl] of cases) {
  const response = apply(path, contentType);
  assert.equal(response.headers.get("Cache-Control"), expectedCacheControl, `${path} cache policy`);
  assertSecurityHeaders(response);
}

console.log(`site-edge-headers: ${cases.length} cases passed`);

