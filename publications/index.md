---
layout: program-doc
title: "Publications"
lane: publications
permalink: /publications/
summary_short: "The canonical publication surfaces of the Panta Rhei Research Program — books, guided tours, white papers, protocols, and companion papers."
summary_cards:
  - title: "Conspectus (synoptic)"
    body: "A self-contained, single-sitting reading of the complete seven-book arc (~27 pp, 35–45 min). Kernel → cascade → commitments → Lean trust budget."
  - title: "Seven books (canonical)"
    body: "The canonical monograph series (2nd Edition, 2026) — 79 parts, 535 chapters, ~3,430 pages across mathematics, physics, life, and metaphysics."
  - title: "Ledger, tours, protocols"
    body: "209-page Physics Ledger (numerical audit trail), 7 guided-tour companions, falsification pack, reviewer's dossier, seminar abstracts, assessment protocols."
right_rail:
  related:
    - title: "About the Research"
      url: /program/about/
    - title: "Framework Overview"
      url: /framework/about/
    - title: "Verify"
      url: /verify/
  meta:
    type: "Lane Root"
    scope: "All publications"
    status: "Canonical"
    updated: "April 2026"
---

## Publication Ontology

The Panta Rhei Research Program publishes through complementary surfaces rather than a single monolithic release. This is deliberate: a research program that claims to bridge mathematics, physics, biology, and metaphysics needs multiple entry points — the canonical proof-order argument (the books), the structured falsification surface (the white papers), the machine-checked [verification layer]({{ '/verify/' | relative_url }}), and the domain-specific guided tours that lower the threshold for expert engagement. Each surface serves a different kind of reader and a different depth of scrutiny. Publications are not marketing — they are the canonical articulation of the research, designed so that the [framework's claims]({{ '/framework/about/' | relative_url }}) can be inspected from any angle.

## Publication Families

### [The Panta Rhei Conspectus]({{ '/publications/conspectus/' | relative_url }})

A self-contained, **single-sitting reading** of the complete seven-book programme — approximately **27 pages, 35–45 minutes**. Walks the full arc from the 7-axiom kernel and master constant ι<sub>τ</sub>, through the L0→L4 calibration cascade and 67 zero-parameter predictions, to the 30-entry Falsification Pack and the Lean trust budget. Designed to be read cover-to-cover on a single flight or afternoon; sits between the 23-page *Series Prospectus* and the 209-page *Physics Ledger*.

### [The Seven Books]({{ '/publications/books/' | relative_url }})

The canonical monograph series — organized in proof-order, 79 parts, 535 chapters, ~3,430 pages. Each book earns its content from what came before.

{% for book in site.data.publications.books %}
- **Book {{ book.roman }}**: [{{ book.title }}]({{ book.url | relative_url }}) — *{{ book.subtitle }}* ({{ book.pages }} pages)
{% endfor %}

### [Guided Tours]({{ '/publications/guided-tours/' | relative_url }})

Structural falsification whitepapers (56 pages, 49 hinges), Lean verification companions, and 8 interactive TauLib tours for different audiences.

### [White Papers]({{ '/publications/white-papers/' | relative_url }})

Technical documents: falsification pack (220+ predictions), Lean verification report, reviewer's dossier, reader's guide, series prospectus, and seminar abstracts.

### [Companion Papers]({{ '/publications/companion-papers/' | relative_url }})

44 public-good deployment papers across 11 impact portfolios — conditional scenario analyses. Full text available in the [Impact lane]({{ '/impact/' | relative_url }}).

### [Errata]({{ '/publications/errata/' | relative_url }})

Public changelog for substantial corrections to the 2nd Edition books, verification surfaces, registry entries, and associated publications. Errata are append-only and citeable by ID.

### [Assessment Protocols]({{ '/verify/assessment-protocols/' | relative_url }})

AI-assisted first-pass assessment protocol with three-gate rubric, prompt templates, and structured dossier output. Now part of the [Verify lane]({{ '/verify/' | relative_url }}).

### [Archived Releases — First Edition]({{ '/publications/archived/first-edition/' | relative_url }})

The First Edition (December 2025) is preserved as an archived historical release. It documents an earlier public state of the work before the current canonical Second Edition. It remains available for reference and comparison, but it is no longer the active research canon.

## How Publications Relate to the Site

The books carry the canonical argument in proof-order — each chapter depends on what came before, and the seven volumes form a single derivation chain from [kernel]({{ '/framework/about/what-the-tau-framework-is/' | relative_url }}) to [metaphysics]({{ '/publications/books/book-vii/' | relative_url }}). The Atlas (this site) provides navigable access in understanding-order — readers can enter through any lane and follow the path that matches their questions. [TauLib]({{ '/verify/taulib/' | relative_url }}) provides machine-checked verification. The guided tours and companion papers lower the threshold for structured engagement.

These are not separate projects. They are different public surfaces of the same research program. The [Results lane]({{ '/results/' | relative_url }}) provides the claims; the books provide the proofs; the [bibliography]({{ '/bibliography/' | relative_url }}) provides the scholarly context; and the [verification surfaces]({{ '/verify/' | relative_url }}) provide the routes for inspection.
