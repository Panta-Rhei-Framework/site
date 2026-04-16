---
title: "Bibliography pipeline — 1,124 entries with MathML, editorial overrides, and browse surface"
date: 2026-04-15
change_type: "content"
summary_short: "Three-commit bibliography build: citation index + LaTeX→MathML infrastructure, 210 editorial overrides grounded in book manuscripts, MathML rendering + Cited-in section + browse/filter surface at /bibliography/browse/."
affected_lanes:
  - bibliography
right_rail:
  toc: false
  related:
    - title: "Changelog"
      url: /changelog/
    - title: "Bibliography"
      url: /bibliography/
  meta:
    type: "Changelog Entry"
    status: "Published"
    updated: "April 2026"
---

The bibliography lane received a three-commit infrastructure build:

1. **Commit 1** — citation index and LaTeX→MathML infrastructure for 1,124 entries.
2. **Commit 2** — 210 hand-written editorial overrides (`why_included` prose) grounded in specific book manuscript passages.
3. **Commit 3** — MathML rendering of 31 math-in-title entries, "Cited in" sections linking every entry to its citing chapters, and a mass regeneration pass across all 1,124 entry pages.

A dedicated **browse and filter surface** shipped at `/bibliography/browse/` with 6 filter groups and 3 sort modes, making the full reference corpus navigable.
