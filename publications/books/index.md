---
layout: program-doc
title: "The Seven Books"
lane: publications
permalink: /publications/books/
summary_short: "The canonical monograph series — seven books tracing the enrichment ladder from mathematical kernel to the terminal boundary."
summary_cards:
  - title: "Proof-order"
    body: "The books are organized sequentially, each earning its content from what came before. No hidden forward dependencies."
  - title: "3,430 pages"
    body: "79 parts, 535 chapters across 7 volumes — the complete canonical prose articulation of the framework."
  - title: "Available now"
    body: "Hardcover, paperback, and Kindle on Amazon KDP. 2nd Edition, April 2026."
right_rail:
  related:
    - title: "Publications Overview"
      url: /publications/
    - title: "Framework Overview"
      url: /framework/about/
    - title: "Verify"
      url: /verify/
  meta:
    type: "Family Root"
    scope: "All books"
    status: "Published"
    updated: "April 2026"
---

## The Canonical Monograph Series

{% for book in site.data.publications.books %}
### [Book {{ book.roman }}: {{ book.title }}]({{ book.url | relative_url }})

*{{ book.subtitle }}* — {{ book.layer }} {{ book.layer_name }}

{{ book.parts }} parts · {{ book.chapters }} chapters · {{ book.pages }} pages

{% endfor %}

## Series Spine

*How Mathematics Is Earned* → *Finite Readouts of Infinity* → *Where Physics Lives* → *The Self-Describing Universe* → *The Biography of the Universe* → *Life as Self-Decoding Distinctions* → *The Final Self-Enrichment*

**One coherence kernel. Four layers. Seven books.**
