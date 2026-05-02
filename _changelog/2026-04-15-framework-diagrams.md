---
title: "Legacy diagram projection — TikZ→SVG pipeline + Books I–VII (60 modules, 58 diagrams)"
date: 2026-04-15
change_type: "content"
summary_short: "TikZ→SVG diagram pipeline infrastructure shipped, followed by 58 hand-reviewed diagrams covering the legacy module projection across 7 books. Each diagram has a dedicated figcaption citing its source Book + Chapter."
affected_lanes:
  - corpus
right_rail:
  toc: false
  related:
    - title: "Changelog"
      url: /changelog/
    - title: "Corpus"
      url: /corpus/
  meta:
    type: "Changelog Entry"
    status: "Published"
    updated: "April 2026"
---

The legacy module projection received a complete diagram build:

- **Infrastructure**: a TikZ→SVG pipeline that compiles standalone TikZ sources to optimized SVG files, committed to the archived diagram asset tree.
- **Phase 2 review mapping**: all 60 legacy modules mapped to their canonical diagram targets.
- **Books I–VII**: 58 diagrams shipped in seven successive commits, one per book — 4 diagrams for Book I (Foundations), 5 for Book II (Holomorphy), 6 for Book III (Spectrum), 9 for Book IV (Microcosm), 8 for Book V (Macrocosm), 7 for Book VI (Life), 7 for Book VII (Metaphysics).

Every diagram has a `<figcaption>` citing its source Book + Chapter, and the archived module layout renders them with alt text for accessibility.
