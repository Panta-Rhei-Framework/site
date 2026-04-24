---
layout: program-doc
title: "Companion Papers"
lane: publications
permalink: /publications/companion-papers/
type: "Publication Family"
publication_type: "Companion Papers"
status: "Published"
summary_short: "44 public-good deployment papers across 11 impact portfolios — conditional scenario analyses if the framework holds."
summary_cards:
  - title: "44 papers"
    body: "Full-text companion papers covering climate, energy, agriculture, ocean, health, water, weather, disaster, biodiversity, pollution, and solar."
  - title: "11 portfolios"
    body: "Each paper belongs to an impact portfolio exploring conditional public-good consequences."
  - title: "Assumption-led"
    body: "Every paper states explicitly what must hold before consequences follow."
right_rail:
  related:
    - title: "Impact Lane"
      url: /impact/
    - title: "Publications Overview"
      url: /publications/
  meta:
    type: "Family Root"
    status: "Published"
    updated: "April 2026"
---

## What This Family Does

Companion Papers are the publication index for conditional public-good deployment work. They ask a narrow question: if the framework's relevant results survive scrutiny, what would become possible for climate, energy, health, water, agriculture, disaster resilience, biodiversity, pollution, solar, ocean systems, and weather intelligence?

They are not validation claims. They are downstream scenario analyses. The [Impact lane]({{ '/impact/' | relative_url }}) carries the full portfolio surfaces; this page organizes them as publication artifacts.

## Portfolio Index

<div class="v2-grid">
{% for p in site.data.impact.portfolios %}
  <a class="v2-tile" href="{{ p.url | relative_url }}">
    <h3>{{ p.title }}</h3>
    <p>{{ p.paper_count }} papers. {{ p.summary_short }}</p>
  </a>
{% endfor %}
</div>

## Reading Discipline

Each Companion Paper should be read with three questions in view:

- Which framework result is being assumed?
- Which empirical or formal checks would change the conclusion?
- Which public-good pathway remains valuable even if a stronger claim is later weakened?

For the first question, move to [Results]({{ '/results/' | relative_url }}). For the second, move to [Verify]({{ '/verify/' | relative_url }}). For the third, stay in [Impact]({{ '/impact/' | relative_url }}).
