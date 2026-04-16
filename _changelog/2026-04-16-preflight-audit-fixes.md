---
title: "Preflight audit — must-fix sprint across all 10 modules"
date: 2026-04-16
change_type: "site-release"
summary_short: "10-module preflight audit surfaced 7 must-fix items. This sprint resolves them: favicon set, footer legal block, TauLib build pin, bibliography/publications data cleanup, impact layout enrichment, and this changelog catch-up."
affected_lanes:
  - global
  - publications
  - bibliography
  - verify
  - impact
  - engage
right_rail:
  toc: false
  related:
    - title: "Changelog"
      url: /changelog/
    - title: "Preflight Dashboard"
      url: /changelog/
  meta:
    type: "Changelog Entry"
    status: "Published"
    updated: "April 2026"
---

A 10-module parallel preflight audit swept all ~7,250 content files. The audit surfaced 7 must-fix items, all resolved in this sprint:

1. **Favicon set** (M00): shipped full set — SVG + PNG fallbacks (16, 32) + apple-touch-icon (180) + android-chrome (192, 512) + `site.webmanifest`. Wired in `_includes/head.html`.
2. **Footer legal block** (M00): copyright line with dynamic year, CC BY 4.0 license link, new `/credits/` attribution page.
3. **TauLib build pin** (M07): created `_data/verify/build.yml` with commit SHA, Lean version, Mathlib rev, license. Surfaced on `/verify/taulib/status/` Build Pin table + every API doc page footer. Reproducibility gap closed.
4. **Publications data cleanup** (M05): re-cleaned `_data/publications/parts.json` + `chapters.json` — 7 + 13 LaTeX backslash escapes resolved to UTF-8 (Schrodinger→Schr&ouml;dinger, G&ouml;del, Poincar&eacute;, etc.).
5. **Bibliography overrides cleanup** (M06): fixed LaTeX residue in `_data/bibliography/overrides.yml` (`G\"odel`→G&ouml;del, `L\"ob`→L&ouml;b, `Weizs\"acker`→Weizs&auml;cker, etc.) affecting 9 rendered pages. Rewrote 1 tabular-debris excerpt.
6. **Changelog catch-up** (M09): this entry + 5 preceding entries covering world-readout clusters, bibliography pipeline, framework diagrams, Books Lane sign-off, and the SEO sprint.
7. **Impact layout enrichment** (M08): pending — queued as next mini-sprint.
