---
title: "Books Lane editorial sign-off — LaTeX→Unicode, glass parts cards, hero dedup"
date: 2026-04-15
change_type: "site-release"
summary_short: "Release-readiness pass across all 7 canonical books (622 files). 4,081 inline LaTeX expressions converted to Unicode, 7 display-math blocks styled, glassmorphic parts cards on all book index pages, hero/body duplication removed."
affected_lanes:
  - publications
right_rail:
  toc: false
  related:
    - title: "Changelog"
      url: /changelog/
    - title: "Publications"
      url: /publications/
  meta:
    type: "Changelog Entry"
    status: "Published"
    updated: "April 2026"
---

The Books Lane went through a comprehensive editorial sign-off sprint for release readiness:

- **LaTeX→Unicode**: 4,081 inline `$...$` wrappers stripped and normalized across 556 of 622 files. Greek letters, subscripts, superscripts, and project macros all resolved to clean Unicode. 7 display `$$...$$` blocks converted to styled `.math-display` blocks.
- **Glassmorphic parts cards**: the 7 book index pages now render their Parts list as a 2-column grid of glass cards (reusing the site's `.lane-card` primitives) instead of a plain Markdown bullet list.
- **Hero/body duplication**: part pages no longer show `summary_short` in both the hero and the body. The body paragraph is the sole source; `summary_short` still powers the SEO description meta tag.
- **Data files cleaned**: `_data/publications/parts.json` and `chapters.json` cleaned in place to match the stripped source markdown.

The conversion script `scripts/strip_books_latex.py` is committed for reference and reproducibility.
