#!/usr/bin/env bash
# ============================================================
# Build-artifact smoke test for panta-rhei.site
# ============================================================
# Runs AFTER `bundle exec jekyll build` + Pagefind, BEFORE
# `upload-pages-artifact`. Validates the built `_site/` tree
# directly — no CDN, no network, no Cloudflare bot-protection
# false-positives.
#
# Catches:
#   · missing assets referenced from head.html
#   · missing core pages (v2 lane roots, publications)
#   · duplicate <title> / meta regressions
#   · accent-color drift, deprecated-org refs, local-path leaks
#   · empty / stubbed sitemap
#
# Usage:
#   ./smoke-test.sh path/to/_site
#
# Exit codes:
#   0 — all checks passed
#   1 — one or more checks failed
#   2 — usage error
# ============================================================

set -u

SITE="${1:-_site}"
if [ ! -d "$SITE" ]; then
  echo "ERROR: $SITE is not a directory"
  echo "Usage: $0 <path-to-_site>"
  exit 2
fi

FAILED=0
CHECK_COUNT=0

pass() { echo "  ✓ $*"; CHECK_COUNT=$((CHECK_COUNT+1)); }
fail() { echo "  ✗ $*"; CHECK_COUNT=$((CHECK_COUNT+1)); FAILED=$((FAILED+1)); }

check_file() {
  local rel="$1"
  if [ -f "$SITE$rel" ]; then
    pass "exists  $rel"
  else
    fail "MISSING $rel"
  fi
}

file_contains() {
  local rel="$1" needle="$2" label="$3"
  if [ ! -f "$SITE$rel" ]; then
    fail "$label  (target file $rel missing)"
    return
  fi
  if grep -qF -- "$needle" "$SITE$rel"; then
    pass "$label"
  else
    fail "$label  ($rel missing '$needle')"
  fi
}

file_count() {
  local rel="$1" needle="$2" expected="$3" label="$4"
  if [ ! -f "$SITE$rel" ]; then
    fail "$label  (target file $rel missing)"
    return
  fi
  local count
  count=$(grep -cF -- "$needle" "$SITE$rel")
  if [ "$count" = "$expected" ]; then
    pass "$label  (count=${expected})"
  else
    fail "$label  (expected ${expected}, got ${count})"
  fi
}

file_absent() {
  local rel="$1" needle="$2" label="$3"
  if [ ! -f "$SITE$rel" ]; then
    fail "$label  (target file $rel missing)"
    return
  fi
  local count
  count=$(grep -cF -- "$needle" "$SITE$rel")
  if [ "$count" = "0" ]; then
    pass "$label"
  else
    fail "$label  (found ${count} occurrence(s) — regression)"
  fi
}

echo "═══════════════════════════════════════════════════════════"
echo " Build-artifact smoke test against ${SITE}/"
echo "═══════════════════════════════════════════════════════════"
echo ""

echo "── Every expected file exists in _site/ ──────────────────"
for f in \
  "/index.html" \
  "/discover/index.html" \
  "/program/index.html" \
  "/corpus/index.html" \
  "/corpus/registry/index.html" \
  "/results/index.html" \
  "/verify/index.html" \
  "/publications/index.html" \
  "/impact/index.html" \
  "/engage/index.html" \
  "/research-program/index.html" \
  "/registry/index.html" \
  "/research-notes/index.html" \
  "/robots.txt" \
  "/sitemap.xml" \
  "/assets/og-image.png" \
  "/assets/favicon.svg" \
  "/assets/favicon-32x32.png" \
  "/assets/favicon-16x16.png" \
  "/assets/apple-touch-icon.png" \
  "/assets/site.webmanifest" \
  "/assets/css/main.css" \
  "/assets/fonts/InterVariable.woff2" \
  "/pagefind/pagefind.js" \
  "/pagefind/pagefind-ui.js" \
  "/pagefind/pagefind-ui.css"
do
  check_file "$f"
done

echo ""
echo "── Homepage integrity ────────────────────────────────────"
file_count    "/index.html" "<title>"                                         "1"  "single <title> tag"
file_contains "/index.html" 'name="theme-color"'                                   "theme-color meta present"
file_contains "/index.html" "#163e64"                                              "canonical navy #163e64 in head"
file_contains "/index.html" "orcid.org/0009-0007-0718-1042"                        "Thorsten ORCID in JSON-LD"
file_contains "/index.html" "orcid.org/0009-0007-3495-7416"                        "Anna-Sophie ORCID in JSON-LD"
file_contains "/index.html" "https://panta-rhei.site/assets/og-image.png"          "og:image absolute URL"
file_contains "/index.html" "Start with Discover"                                  "v2 Discover CTA present"
file_contains "/index.html" "Explore the Corpus"                                   "v2 Corpus CTA present"
file_contains "/index.html" "See the Results"                                      "v2 Results CTA present"
file_contains "/index.html" "Verify It Yourself"                                   "v2 Verify CTA present"
file_contains "/index.html" "taulib.site"                                          "reciprocal link to taulib.site"

echo ""
echo "── Anti-regression (zero-occurrence) ─────────────────────"
file_absent "/index.html" "Panta-Rhei-Framework"                   "no deprecated org references"
file_absent "/index.html" "/Users/thorfuchs"                       "no local filesystem paths leaked"
file_absent "/index.html" "#294b66"                                "no pre-migration accent color"

echo ""
echo "── robots.txt + sitemap.xml integrity ────────────────────"
file_contains "/robots.txt" "Content-Signal"                        "Content-Signal directive present"
file_contains "/robots.txt" "Sitemap: https://panta-rhei.site"      "sitemap reference present"

loc_count=$(grep -c '<loc>' "$SITE/sitemap.xml" 2>/dev/null || echo "0")
if [ "$loc_count" -ge 100 ]; then
  pass "sitemap has ${loc_count} URLs (expected ≥100)"
else
  fail "sitemap has only ${loc_count} URLs (expected ≥100)"
fi
CHECK_COUNT=$((CHECK_COUNT+1))

echo ""
echo "═══════════════════════════════════════════════════════════"
if [ "$FAILED" -eq 0 ]; then
  echo " ✓ ALL ${CHECK_COUNT} CHECKS PASSED"
  echo "═══════════════════════════════════════════════════════════"
  exit 0
else
  echo " ✗ ${FAILED} of ${CHECK_COUNT} checks FAILED"
  echo "═══════════════════════════════════════════════════════════"
  exit 1
fi
