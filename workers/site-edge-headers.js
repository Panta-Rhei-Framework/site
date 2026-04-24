const SECURITY_HEADERS = {
  "X-Content-Type-Options": "nosniff",
  "X-Frame-Options": "DENY",
  "Referrer-Policy": "strict-origin-when-cross-origin",
  "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
  "Link": [
    '</sitemap.xml>; rel="sitemap"; type="application/xml"',
    '<https://creativecommons.org/licenses/by/4.0/>; rel="license"; title="CC BY 4.0"',
    '</verify/taulib/docs/>; rel="service-doc"; type="text/html"; title="TauLib API reference"',
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
    test: (url) => url.pathname.startsWith("/assets/") || url.pathname.startsWith("/pagefind/"),
    value: "public, max-age=31536000, immutable"
  },
  {
    test: (url, response) => isHtmlRequest(url, response),
    value: "public, max-age=3600, must-revalidate"
  }
];

function isHtmlRequest(url, response) {
  const contentType = response.headers.get("Content-Type") || "";
  return contentType.includes("text/html") || url.pathname.endsWith(".html") || url.pathname.endsWith("/");
}

function cachePolicyFor(url, response) {
  const policy = CACHE_POLICIES.find((candidate) => candidate.test(url, response));
  return policy?.value;
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

  return new Response(response.body, {
    status: response.status,
    statusText: response.statusText,
    headers
  });
}

export default {
  async fetch(request) {
    const originResponse = await fetch(request);
    return applyEdgeHeaders(request, originResponse);
  }
};

