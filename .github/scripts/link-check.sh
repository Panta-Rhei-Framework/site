#!/usr/bin/env bash
# ============================================================
# Dead-link audit for panta-rhei.site
# ============================================================
# Runs html-proofer against the built _site/ tree. Internal-only
# (external link validation is a separate, slower check).
#
# Runs AFTER Jekyll build + Pagefind, BEFORE Pages artifact upload.
# Fails the build visibly if any broken internal link appears.
#
# Usage:
#   ./link-check.sh [path/to/_site]
#
# Exit codes:
#   0 — all checks passed
#   1 — at least one broken link found
# ============================================================

set -u

SITE="${1:-_site}"
if [ ! -d "$SITE" ]; then
  echo "ERROR: $SITE is not a directory"
  echo "Usage: $0 <path-to-_site>"
  exit 2
fi

export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

# Only persistent false-positive: Pagefind URLs carry `?v=<epoch>` cache-bust
# that html-proofer doesn't strip before the file-exists check. The rest of
# the historical ignore-list (25 items tracked in
# atlas/audits/site/2026-04-19-dead-link-audit.md) has been resolved at source
# in a follow-up sprint — Book IV YAML fixes, registry-drift cleanup,
# Results slug rewrites, asset generation, stale-ref removal.
IGNORE_URLS='/\/pagefind\//'

echo "═══════════════════════════════════════════════════════════"
echo " Dead-link audit against ${SITE}/"
echo "═══════════════════════════════════════════════════════════"
echo ""

bundle exec htmlproofer "$SITE" \
  --disable-external \
  --checks Links,Images,Scripts \
  --ignore-missing-alt \
  --no-check-internal-hash \
  --ignore-urls "$IGNORE_URLS"
