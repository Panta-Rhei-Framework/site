---
layout: bibliography-browse
title: Browse Bibliography
permalink: /bibliography/browse/
lane: support
type: support_page
support_type: bibliography
status: canonical
last_updated: 2026-04-30
updated: "April 2026"
section: "Bibliography · Browse"
summary: "Interactive browse and filter surface for the public bibliography."
summary_short: "All manifest-pinned references in the research corpus — filter by domain, role, type, citation status, book, and decade."
right_rail:
  related:
  - title: Bibliography Overview
    url: /bibliography/
  - title: Results Browse
    url: /results/browse/
  - title: Corpus
    url: /corpus/
  artifacts:
  - title: "Download references.bib"
    url: /assets/bibliography/references.bib
  meta:
    type: Support page
    scope: Bibliography browse
    status: Canonical
    updated: April 2026
---

The Bibliography & Prior-Art Catalog contains **{% include release-metric.html id="bibliography.references" %} references** spanning mathematics, physics, biology, philosophy, and computation. Every reference has been reviewed and classified, and directly cited entries are linked to the seven-book series by chapter metadata. Every entry is pre-rendered below as a card — the page is fully crawlable and readable without JavaScript. With JavaScript enabled, the six filter groups and three sort modes narrow and reorder the view interactively, and the active filter state is shared via the URL.

Use the controls below to narrow down, or open a reference directly to see its detail page with the full citation, the "Cited in" section for cited entries, and the editorial prose explaining why the reference is included. Construction-step and prior-art filters arrive in a follow-up pass; until then, browse by domain, role, type, citation status, book, and decade.

## Quick prior-art clusters

The bibliography supports prior-art positioning across these scholarly horizons. Each cluster maps to one or more Construction Spine steps; the clusters themselves will become dedicated landing pages in a follow-up pass.

- **Wolfram / computational universe** — ruliad, observer theory, hypergraph rewriting (CS-04, CS-10).
- **Penrose / twistor / conformal geometry** — twistor theory, conformal cyclic cosmology (CS-04).
- **Wheeler / absorber / it-from-bit** — relational physics, observer participation (CS-04, CS-10).
- **HoTT / type theory / internal logic** — homotopy type theory, univalent foundations, internal language (CS-01, CS-03).
- **Gödel / foundations / formal limits** — incompleteness, reflection principles, self-reference (CS-01, CS-09).
- **GR / QFT / quantum gravity** — emergent spacetime, categorical physics, causal sets (CS-04, CS-05).
- **Cosmology / Hubble / CMB** — Hubble tension, CMB-S4, dark sector (CS-06).
- **Ultrametric / solenoidal / continuum recovery** — p-adic physics, continuum-from-discrete (CS-02, CS-05).
- **Life / autopoiesis / FEP / IIT** — definitions of life, predictive processing, integrated information (CS-07, CS-08).
- **Open science / inspection architecture** — public-research observatory practices (cross-cutting).
- **Impact / public good / RRI** — responsible research and innovation (Impact lane).

Cluster pages with curated reference lists, related construction steps, and external review status arrive at `/bibliography/clusters/<slug>/` in a follow-up pass.
