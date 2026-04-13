---
layout: program-doc
title: "Publications"
lane: publications
permalink: /publications/
summary_short: "The canonical publication surfaces of the Panta Rhei Research Program — books, guided tours, white papers, protocols, and companion papers."
summary_cards:
  - title: "Seven books"
    body: "The canonical monograph series (2nd Edition, 2026) — 79 parts, 535 chapters, ~3,430 pages across mathematics, physics, life, and metaphysics."
  - title: "Guided tours & companions"
    body: "56-page falsification whitepapers, 7 Lean companions with 49 hinges, 8 interactive TauLib tours, and 44 companion papers."
  - title: "White papers & protocols"
    body: "Falsification pack, Lean verification report, reviewer's dossier, reader's guide, prospectus, seminar abstracts, and assessment protocols."
right_rail:
  related:
    - title: "About the Research"
      url: /research-program/about/
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

The Panta Rhei Research Program publishes through complementary surfaces. Each serves a different purpose in the program's commitment to public inspectability. Publications are not marketing — they are the canonical articulation of the research.

## Publication Families

### [The Seven Books](/publications/books/)

The canonical monograph series — organized in proof-order, 79 parts, 535 chapters, ~3,430 pages. Each book earns its content from what came before.

{% for book in site.data.publications.books %}
- **Book {{ book.roman }}**: [{{ book.title }}]({{ book.url | relative_url }}) — *{{ book.subtitle }}* ({{ book.pages }} pages)
{% endfor %}

### [Guided Tours](/publications/guided-tours/)

Structural falsification whitepapers (56 pages, 49 hinges), Lean verification companions, and 8 interactive TauLib tours for different audiences.

### [White Papers](/publications/white-papers/)

Technical documents: falsification pack (220+ predictions), Lean verification report, reviewer's dossier, reader's guide, series prospectus, and seminar abstracts.

### [Companion Papers](/publications/companion-papers/)

44 public-good deployment papers across 11 impact portfolios — conditional scenario analyses. Full text available in the [Impact lane](/impact/).

### [Assessment Protocols](/publications/protocols/)

Structured guides helping domain experts evaluate specific claims. Currently in development.

## How Publications Relate to the Site

The books carry the canonical argument in proof-order. The Atlas (this site) provides navigable access in understanding-order. TauLib provides machine-checked verification. The guided tours and companion papers lower the threshold for structured engagement.

These are not separate projects. They are different public surfaces of the same research program.
