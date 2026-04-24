---
layout: program-doc
title: "Books"
lane: publications
permalink: /publications/books/
type: "Publication Family"
publication_type: "Books"
status: "Published"
summary_short: "The canonical monograph series: seven Second Edition books tracing the enrichment ladder from mathematical kernel to terminal reflective boundary."
summary_cards:
  - title: "Proof-order"
    body: "The books are organized sequentially, each earning its content from what came before. No hidden forward dependencies."
  - title: "3,431 pages"
    body: "79 parts, 535 chapters across 7 volumes — the complete canonical prose articulation of the framework."
  - title: "Available now"
    body: "Hardcover, paperback, and Kindle on Amazon KDP. 2nd Edition, April 2026."
right_rail:
  related:
    - title: "Publications Overview"
      url: /publications/
    - title: "Corpus Registry"
      url: /corpus/registry/
    - title: "Verify"
      url: /verify/
  meta:
    type: "Family Root"
    scope: "All books"
    status: "Published"
    updated: "April 2026"
---

## The Seven-Book Spine

The books are the citation-bearing spine of the program. Other publication families help readers inspect, test, summarize, or apply the work, but the seven books carry the canonical argument in order. Read them as one derivation chain:

**Book I-II** earn the mathematical substrate. **Book III** opens the self-enrichment ladder and the hinge into physics. **Book IV-V** develop microphysics and cosmology. **Book VI** gives the life layer. **Book VII** carries the terminal reflective and metaphysical layer.

## Current Edition

{% for book in site.data.publications.books %}
{%- assign amz = nil -%}
{%- for a in site.data.publications.first_edition_amazon -%}
  {%- if a.slug == book.id -%}{%- assign amz = a -%}{%- endif -%}
{%- endfor -%}
<div class="book-list-item">
  <img src="{{ '/assets/books/covers/' | append: book.id | append: '-cover-96.webp' | relative_url }}" alt="Cover of Book {{ book.roman }}" class="book-list-thumb" width="88" height="141" loading="lazy">
  <div class="book-list-info">
    <h3><a href="{{ book.url | relative_url }}">Book {{ book.roman }}: {{ book.title }}</a></h3>
    <p><em>{{ book.subtitle }}</em> — {{ book.layer }} {{ book.layer_name }}<br>
    {{ book.parts }} parts · {{ book.chapters }} chapters · {{ book.pages }} pages</p>
    {%- if amz -%}
    <div class="book-format-btns">
      <a href="{{ amz.ebook_url_amazon_de }}" target="_blank" rel="noopener" class="btn-ghost">Ebook</a>
      <a href="{{ amz.paperback_url_amazon_de }}" target="_blank" rel="noopener" class="btn-ghost">Paperback</a>
      <a href="{{ amz.hardcover_url_amazon_de }}" target="_blank" rel="noopener" class="btn-ghost">Hardcover</a>
    </div>
    {%- endif -%}
  </div>
</div>
{% endfor %}

## How to Use the Books

For orientation, start with the [Conspectus]({{ '/publications/conspectus/' | relative_url }}) or the [Discover reading routes]({{ '/discover/what-to-read-first/' | relative_url }}). For source-object inspection, move from a book chapter to the [Corpus registry]({{ '/corpus/registry/' | relative_url }}). For theorem and artifact checks, use [Verify]({{ '/verify/' | relative_url }}). For problem-oriented reading, enter through [Results]({{ '/results/' | relative_url }}) and follow the result back to its book context.

## Edition Status

The Second Edition is the active canon for reading, citation, and verification. The [First Edition archive]({{ '/publications/archived/first-edition/' | relative_url }}) is preserved for provenance and comparison.

**One coherence kernel. Four layers. Seven books.**
