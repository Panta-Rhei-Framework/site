---
layout: "program-doc"
lane: "publications"
v2_lane: "publications"
status: "Active"
last_updated: 2026-04-30
updated: "April 2026"
title: "Research Papers"
permalink: "/publications/research-papers/"
type: "Publication Category"
summary_short: "Standalone scholarly papers carrying primary technical research contributions."
---

## Research Papers

Research Papers are standalone scholarly papers carrying primary technical research contributions.

They are intended to state, prove, derive, or argue for original research claims in a paper-like scholarly format.

<div class="notice note"><strong>Current status.</strong> The first Research Papers batch is published with public PDF artifacts and final Zenodo DOI links.</div>

## First batch

<ul class="pub-card-grid">
{% for paper in site.data.publications.research_papers %}
  {% assign cover = "/assets/thumbnails/papers/" | append: paper.slug | append: "-cover.png" %}
  {% assign landing = "/publications/research-papers/" | append: paper.slug | append: "/" %}
  <li>
    <article class="pub-card">
      <a href="{{ landing | relative_url }}" aria-hidden="true" tabindex="-1">
        <img src="{{ cover | relative_url }}" alt="" class="pub-card__cover" loading="lazy" width="96" height="128" />
      </a>
      <div class="pub-card__body">
        <h3 class="pub-card__title"><a href="{{ landing | relative_url }}">{{ paper.title }}</a></h3>
        <p class="pub-card__summary">{{ paper.summary_short }}</p>
        <p class="pub-card__meta"><span>{{ paper.role }}</span><span>{{ paper.date }}</span></p>
        <div class="pub-card__actions">
          <a href="{{ paper.pdf_path | relative_url }}" class="chip chip-small">PDF</a>
          <a href="https://doi.org/{{ paper.doi }}" class="chip chip-small" rel="noopener">DOI</a>
        </div>
      </div>
    </article>
  </li>
{% endfor %}
</ul>

## Citation status

Cite each paper by title, authors, version, date, URL, and DOI. The detail pages above include the preferred citation sentence for each artifact.
