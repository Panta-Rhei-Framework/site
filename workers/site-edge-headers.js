const SECURITY_HEADERS = {
  "X-Content-Type-Options": "nosniff",
  "X-Frame-Options": "DENY",
  "Referrer-Policy": "strict-origin-when-cross-origin",
  "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
  "Link": [
    '</sitemap.xml>; rel="sitemap"; type="application/xml"',
    '<https://creativecommons.org/licenses/by/4.0/>; rel="license"; title="CC BY 4.0"',
    '</corpus/taulib/docs/>; rel="service-doc"; type="text/html"; title="TauLib API reference"',
    '</verify/assessment-protocols/>; rel="help"; type="text/html"; title="Assessment protocols"',
    '</program/about/founders/>; rel="author"; type="text/html"; title="Founders"',
    '</program/about/>; rel="describedby"; type="text/html"; title="About the research program"'
  ].join(", ")
};

const CACHE_POLICIES = [
  {
    test: (url) => url.pathname === "/assets/site.webmanifest",
    value: "public, max-age=604800"
  },
  {
    test: (url) => url.pathname === "/sitemap.xml" || url.pathname === "/robots.txt",
    value: "public, max-age=86400"
  },
  {
    test: (url) => url.pathname.startsWith("/api/"),
    value: "public, max-age=3600, stale-while-revalidate=86400"
  },
  {
    test: (url) => url.pathname.startsWith("/assets/") || url.pathname.startsWith("/pagefind/"),
    value: "public, max-age=31536000, immutable"
  },
  {
    test: (url, response) => isHtmlRequest(url, response),
    value: "public, max-age=3600, must-revalidate"
  }
];

// CORS-permissive endpoints — machine-readable indexes meant to be embedded
// from sibling sites (taulib.site, future poster microsites, partner programs).
// Content remains CC BY 4.0; cross-site GET is explicitly allowed.
const CORS_PATH_PREFIXES = ["/api/"];

const PERMANENT_REDIRECTS = new Map([
  ["/publications/physics-ledger", "/publications/monograph-supplements/numerical-physics-ledger/"],
  ["/publications/physics-ledger/", "/publications/monograph-supplements/numerical-physics-ledger/"],
  ["/publications/numerical-physics-ledger", "/publications/monograph-supplements/numerical-physics-ledger/"],
  ["/publications/numerical-physics-ledger/", "/publications/monograph-supplements/numerical-physics-ledger/"],
  ["/publications/categorical-genesis", "/publications/monograph-supplements/categorical-genesis/"],
  ["/publications/categorical-genesis/", "/publications/monograph-supplements/categorical-genesis/"],
  ["/publications/companion-papers", "/publications/research-briefings/public-good/"],
  ["/publications/companion-papers/", "/publications/research-briefings/public-good/"]
]);

function isHtmlRequest(url, response) {
  const contentType = response.headers.get("Content-Type") || "";
  return contentType.includes("text/html") || url.pathname.endsWith(".html") || url.pathname.endsWith("/");
}

function cachePolicyFor(url, response) {
  const policy = CACHE_POLICIES.find((candidate) => candidate.test(url, response));
  return policy?.value;
}

function shouldEnableCors(url) {
  return CORS_PATH_PREFIXES.some((prefix) => url.pathname.startsWith(prefix));
}

function dynamicRedirectFor(pathname) {
  if (pathname.startsWith("/publications/books/book-") && pathname.includes("/part-")) {
    return pathname.replace("/publications/books/", "/corpus/monographs/");
  }

  if (pathname.startsWith("/verify/taulib/docs/") && pathname !== "/verify/taulib/docs/") {
    return pathname.replace("/verify/taulib/docs/", "/corpus/taulib/docs/");
  }

  if (pathname === "/framework" || pathname === "/framework/") {
    return "/corpus/";
  }

  if (pathname.startsWith("/framework/prior-art")) {
    return "/program/research-agenda/kernel-model-reality/related-approaches/deep-comparison/";
  }

  if (pathname.startsWith("/framework/")) {
    return "/corpus/";
  }

  return null;
}

// Short-circuit CORS preflight for /api/* paths. GitHub Pages (the proxied
// origin) doesn't support OPTIONS and returns 405, which silently breaks
// non-simple cross-site fetches (custom headers, non-default Content-Type).
// Returning null leaves non-/api/ paths to fall through to the normal flow.
export function corsPreflightResponse(url) {
  if (!shouldEnableCors(url)) return null;
  return new Response(null, { status: 204, statusText: "No Content" });
}

export function applyEdgeHeaders(request, response) {
  const url = new URL(typeof request === "string" ? request : request.url);
  const headers = new Headers(response.headers);
  const cachePolicy = cachePolicyFor(url, response);

  if (cachePolicy) {
    headers.set("Cache-Control", cachePolicy);
  }

  for (const [name, value] of Object.entries(SECURITY_HEADERS)) {
    headers.set(name, value);
  }

  if (shouldEnableCors(url)) {
    headers.set("Access-Control-Allow-Origin", "*");
    headers.set("Access-Control-Allow-Methods", "GET, HEAD, OPTIONS");
    headers.set("Access-Control-Allow-Headers", "Content-Type");
    headers.set("Access-Control-Max-Age", "86400");
    if (url.pathname.endsWith(".json")) {
      headers.set("Content-Type", "application/json; charset=utf-8");
    }
  }

  return new Response(response.body, {
    status: response.status,
    statusText: response.statusText,
    headers
  });
}

export function edgeRedirectFor(request) {
  const url = new URL(typeof request === "string" ? request : request.url);
  const targetPath = PERMANENT_REDIRECTS.get(url.pathname) || dynamicRedirectFor(url.pathname);

  if (!targetPath) {
    return null;
  }

  const targetUrl = new URL(targetPath, url.origin);
  return Response.redirect(targetUrl.toString(), 301);
}

export default {
  async fetch(request) {
    if (request.method === "OPTIONS") {
      const url = new URL(request.url);
      const preflight = corsPreflightResponse(url);
      if (preflight) {
        return applyEdgeHeaders(request, preflight);
      }
    }

    const redirect = edgeRedirectFor(request);
    if (redirect) {
      return applyEdgeHeaders(request, redirect);
    }

    const originResponse = await fetch(request);
    return applyEdgeHeaders(request, originResponse);
  }
};
