---
layout: program-doc
title: "Companion Papers"
lane: publications
permalink: /publications/companion-papers/
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

## Companion Papers

The companion papers are detailed scenario analyses exploring public-good consequences of the framework — organized under 11 impact portfolios. Each paper is assumption-led, conditional, and explicitly downstream of the framework's validation status.

Browse the full papers in the [Impact lane]({{ '/impact/' | relative_url }}).

### By Portfolio

{% for p in site.data.impact.portfolios %}
- **[{{ p.title }}]({{ p.url | relative_url }})** — {{ p.paper_count }} papers
{% endfor %}
