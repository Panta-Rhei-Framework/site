---
layout: program-doc
title: "First Edition Archive"
lane: publications
permalink: /publications/archived/first-edition/
section: "archived releases"
type: "Publication Archive"
publication_type: "First Edition"
status: "Archived"
summary_short: "The First Edition is preserved as an archived historical release of the Panta Rhei Research Program. It documents an earlier public state of the work before the current canonical Second Edition."
summary_cards:
  - title: "Edition"
    body: "First Edition — December 2025"
  - title: "Status"
    body: "Archived — superseded by 2nd Edition (March 2026)"
  - title: "Structure"
    body: "7 books, 71 parts, 532 chapters"
right_rail:
  related:
    - title: "Archived Releases"
      url: /publications/archived/
    - title: "Publications"
      url: /publications/
    - title: "The Seven Books (2nd Edition)"
      url: /publications/books/
    - title: "About the Research"
      url: /program/about/
  meta:
    type: "Archive Root"
    scope: "First Edition"
    status: "Archived"
    updated: "April 2026"
---

## Archival Status

The First Edition is preserved as an archived historical release of the Panta Rhei Research Program. It documents an earlier public state of the work before the current canonical Second Edition. It remains available for reference and comparison, but it is no longer the active research canon.

The Second Edition (March 2026) substantially rewrites all seven volumes, consolidating the foundation into the Coherence Kernel (7 axioms, 5 generators, 1 operator), correcting the master constant, and adding full Lean 4 machine-checked verification.

For a compact account of the transition, read [From First to Second Edition: What Changed and Why]({{ '/publications/research-notes/from-first-to-second-edition/' | relative_url }}).

## Archived Volumes

{% for book in site.data.publications.first_edition %}
### [Book {{ book.book_id }}: {{ book.title }}]({{ '/publications/archived/first-edition/' | append: book.slug | append: '/' | relative_url }})

*{{ book.subtitle }}* — {{ book.parts }} parts, {{ book.chapters }} chapters

{{ book.archival_note }}

**Current canonical edition:** [Book {{ book.book_id }}: {{ book.title }} (2nd Edition)]({{ book.superseded_by | relative_url }})

---

{% endfor %}

## Availability

The First Edition volumes are currently available as archived retail artifacts via Amazon. Open archival downloads may follow once current distribution constraints end.

## Historical Context

The First Edition was the first public release of the Panta Rhei Research Program. It already contained major lines of thought and many substantial results, but it predated the full Coherence Kernel consolidation and the current level of formalization. The Second Edition is substantially rewritten, carries the stronger formalization and verification posture, and is the current active release for reading, citation, and scrutiny.

The First Edition remains historically important as a record of the program's development, but the Second Edition should be used for all active engagement.
