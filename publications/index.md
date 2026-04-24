---
layout: program-doc
title: "Publications"
lane: publications
permalink: /publications/
summary_short: "The public release catalogue of the Panta Rhei Research Program: books, white papers, guided tours, companion papers, Research Notes, archives, and special artifacts."
summary_cards:
  - title: "Canonical series"
    body: "The seven Second Edition books are the proof-order monograph series: 79 parts, 535 chapters, and about 3,430 pages."
  - title: "Open artifacts"
    body: "White papers, guided tours, companion papers, Research Notes, the Physics Ledger, Categorical Genesis, errata, and archives are freely browsable from this lane."
  - title: "Inspection routes"
    body: "Each publication family points outward to the Corpus, Results, Verify, and Impact lanes when readers need source objects, claims, checks, or applications."
right_rail:
  related:
    - title: "Books"
      url: /publications/books/
    - title: "Research Notes"
      url: /publications/research-notes/
    - title: "Verify"
      url: /verify/
  meta:
    type: "Lane Root"
    scope: "Released artifacts"
    status: "Canonical"
    updated: "April 2026"
---

## What Belongs Here

Publications is the public shelf of released research artifacts. It is not the whole site and not a marketing layer. It holds stable things readers can cite, inspect, download, read in order, or compare across editions.

The lane is deliberately plural. The books carry the canonical proof-order argument. The white papers isolate technical audit surfaces. The guided tours lower the entry cost for specific audiences. Companion papers explore conditional public-good consequences. Research Notes carry dated, article-like research writing as the program develops. The archive preserves superseded public releases without treating them as current canon.

## Canonical Reading Order

### [Books]({{ '/publications/books/' | relative_url }})

The seven Second Edition books are the canonical monograph series. They are organized in proof order from mathematical kernel to physics, life, and metaphysics.

### [Conspectus]({{ '/publications/conspectus/' | relative_url }})

A single-sitting synoptic reading of the full seven-book arc. Use it when you want the whole shape before opening individual volumes.

### [Research Notes]({{ '/publications/research-notes/' | relative_url }})

Dated, article-like research artifacts for substantial public-facing updates, explanatory essays, and bridge texts. Research Notes are publication objects, while [Engage]({{ '/engage/follow-the-research/' | relative_url }}) handles email delivery and following.

## Technical Surfaces

### [Guided Tours]({{ '/publications/guided-tours/' | relative_url }})

Audience-specific entry routes and Lean companions for readers who want to attack structural hinges directly.

### [White Papers]({{ '/publications/white-papers/' | relative_url }})

Technical audit documents including the falsification pack, Lean verification report, reviewer's dossier, reader's guide, series prospectus, seminar abstracts, and one-page orientation artifacts.

### [Companion Papers]({{ '/publications/companion-papers/' | relative_url }})

Conditional public-good deployment papers organized by impact portfolio. They do not replace the [Impact lane]({{ '/impact/' | relative_url }}); they are the publication index for those papers.

### [Errata]({{ '/publications/errata/' | relative_url }})

Append-only correction and clarification surface for substantial changes to released public artifacts.

## Special Artifacts

### [Physics Ledger]({{ '/publications/physics-ledger/' | relative_url }})

The 209-page numerical scorecard for the physics layer, including the calibration cascade, prediction inventory, and falsification targets.

### [Categorical Genesis]({{ '/publications/categorical-genesis/' | relative_url }})

A self-contained companion to Book VII that applies the framework's structural apparatus to Genesis 1-3 under explicit scope and override rules.

### [Bibliography]({{ '/publications/bibliography/' | relative_url }})

The publication-facing bibliography home. It routes to the searchable reference corpus, browse surface, and BibTeX artifact.

## Archived Releases

### [Archived Releases]({{ '/publications/archived/' | relative_url }})

Historical public releases remain available for provenance and comparison. They are not the active citation target unless a reader is explicitly studying the program's development history.

{% for book in site.data.publications.books %}
- **Book {{ book.roman }}**: [{{ book.title }}]({{ book.url | relative_url }}) - *{{ book.subtitle }}* ({{ book.pages }} pages)
{% endfor %}

## How Publications Connect

The books and publication artifacts give the stable prose. The [Corpus]({{ '/corpus/' | relative_url }}) gives the registered source objects. The [Results]({{ '/results/' | relative_url }}) lane gives the problem-and-result mirror. The [Verify]({{ '/verify/' | relative_url }}) lane gives machine-checking, empirical falsification routes, and assessment protocols. The [Impact]({{ '/impact/' | relative_url }}) lane gives public-good deployment scenarios.

These surfaces are different public projections of one research program. Publications is where the released artifacts live; the surrounding lanes make them inspectable.
