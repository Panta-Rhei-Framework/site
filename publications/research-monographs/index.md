---
layout: "program-doc"
lane: "publications"
v2_lane: "publications"
status: "Canonical"
last_updated: 2026-04-30
updated: "April 2026"
title: "Research Monographs"
permalink: "/publications/research-monographs/"
type: "Publication Category"
summary_short: "Full book-length canonical release artifacts of the Panta Rhei Research Program."
---

## Research Monographs

Research Monographs are the full book-length canonical release artifacts of the Panta Rhei Research Program. This Publications page is the citation, DOI, format, and artifact-status surface.

For the open Book → Part → Chapter reading projection, use [Monograph Corpus]({{ '/corpus/monograph-corpus/' | relative_url }}). Corpus is where the monograph exposition participates in the constructed research body; Publications is where the same books are stabilized as released artifacts.

<div class="notice note"><strong>Category boundary.</strong> Research Monographs are the main canonical volumes. Omitted chapters, ledgers, appendices, and book-style supporting parts released separately belong under Monograph Supplements.</div>

<ul class="v2-grid v2-card-list">
{% for book in site.data.publications.books %}
  <li>
    <article>
      <a class="v2-tile" href="{{ book.url | relative_url }}">
        <h3>Book {{ book.roman }}: {{ book.title }}</h3>
        <p><em>{{ book.subtitle }}</em> · {{ book.pages }} pages · artifact page with citation and format metadata.</p>
      </a>
      <p class="hero-meta"><a href="{{ book.corpus_url | relative_url }}">Open Corpus edition</a></p>
    </article>
  </li>
{% endfor %}
</ul>
