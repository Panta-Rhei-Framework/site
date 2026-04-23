---
layout: program-doc
title: "Global Public Good"
lane: impact
permalink: /impact/global-public-good/
type: "Impact Section"
status: "Conditional"
summary_short: "Conditional public-good consequence portfolios for climate, energy, agriculture, health, water, weather, disaster resilience, biodiversity, pollution, solar, and ocean systems."
summary_cards:
  - title: "11 portfolios"
    body: "Each portfolio names a public-good domain and the assumptions required before consequences follow."
  - title: "44 papers"
    body: "Companion papers provide the deeper scenario analyses behind the portfolio summaries."
  - title: "Downstream"
    body: "Global Public Good remains downstream of Results, Verify, and the Impact Framework."
right_rail:
  related:
    - title: "Impact Framework"
      url: /impact/impact-framework/
    - title: "Companion Papers"
      url: /publications/companion-papers/
    - title: "Results"
      url: /results/
    - title: "Verify"
      url: /verify/
  meta:
    type: "Impact Section"
    scope: "Public-good portfolios"
    status: "Conditional"
    updated: "April 2026"
---

## What This Section Does

Global Public Good gathers the program's assumption-led deployment portfolios. These are not promises that the framework will transform a domain. They are conditional consequence maps: if the relevant results hold, and if they can be translated into domain-specific models, what public-good pathways become worth investigating?

## Portfolio Index

<div class="portfolio-grid">
{% for p in site.data.impact.portfolios %}
  <a href="{{ p.url | relative_url }}" class="portfolio-card">
    <h3 class="portfolio-card-title">{{ p.title }}</h3>
    <p class="portfolio-card-summary">{{ p.summary_short }}</p>
    <span class="chip chip-small">{{ p.paper_count }} {% if p.paper_count == 1 %}paper{% else %}papers{% endif %}</span>
  </a>
{% endfor %}
</div>

## Reading Discipline

Every portfolio should be read through the [Impact Framework]({{ '/impact/impact-framework/' | relative_url }}): result, verification survival, translation layer, domain uptake, consequence. The corresponding publication family is [Companion Papers]({{ '/publications/companion-papers/' | relative_url }}).
