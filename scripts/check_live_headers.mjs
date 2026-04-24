import assert from "node:assert/strict";
import https from "node:https";

const origin = process.env.SITE_ORIGIN || "https://panta-rhei.site";

const securityExpectations = {
  "x-content-type-options": "nosniff",
  "x-frame-options": "DENY",
  "referrer-policy": "strict-origin-when-cross-origin",
  "permissions-policy": "camera=(), microphone=(), geolocation=()"
};

const checks = [
  ["/", "cache-control", /max-age=3600/],
  ["/registry/", "cache-control", /max-age=3600/],
  ["/verify/", "cache-control", /max-age=3600/],
  ["/assets/site.webmanifest", "cache-control", /max-age=604800/],
  ["/sitemap.xml", "cache-control", /max-age=86400/],
  ["/robots.txt", "cache-control", /max-age=86400/],
  ["/pagefind/pagefind.js", "cache-control", /max-age=31536000/]
];

function requestHeaders(path, method = "HEAD") {
  const url = new URL(path, origin);

  return new Promise((resolve, reject) => {
    const request = https.request(
      url,
      {
        method,
        family: 4,
        timeout: 30000,
        headers: {
          "User-Agent": "panta-rhei-site-header-check/1.0"
        }
      },
      (response) => {
        response.resume();
        response.on("end", () => {
          resolve({
            status: response.statusCode,
            headers: response.headers
          });
        });
      }
    );

    request.on("timeout", () => {
      request.destroy(new Error(`${method} ${url.href} timed out`));
    });
    request.on("error", reject);
    request.end();
  });
}

async function getHeaders(path) {
  const headResponse = await requestHeaders(path);
  if (headResponse.status === 405) {
    return requestHeaders(path, "GET");
  }
  return headResponse;
}

function headerValue(headers, name) {
  const value = headers[name.toLowerCase()];
  return Array.isArray(value) ? value.join(", ") : value || "";
}

for (const [path, headerName, expectedPattern] of checks) {
  const response = await getHeaders(path);
  assert(response.status < 400, `${path} returned HTTP ${response.status}`);

  for (const [name, expectedValue] of Object.entries(securityExpectations)) {
    assert.equal(headerValue(response.headers, name), expectedValue, `${path} ${name}`);
  }

  assert.match(headerValue(response.headers, headerName), expectedPattern, `${path} ${headerName}`);

  const link = headerValue(response.headers, "link");
  assert.match(link, /rel="sitemap"/, `${path} Link sitemap relation`);
  assert.match(link, /rel="license"/, `${path} Link license relation`);
}

console.log(`Live edge headers passed for ${checks.length} paths at ${origin}`);
