---
layout: program-doc
title: Potential Impact
permalink: /impact/
lane: impact
summary_short: If the framework holds, what could change? 11 public-good portfolios
  with 44 companion papers.
summary_cards:
- title: Assumption-led
  body: Every portfolio states explicitly what must hold true before consequences
    follow.
- title: 11 portfolios
  body: Climate, energy, agriculture, ocean, one-health, water, weather, disaster,
    biodiversity, pollution, solar.
- title: Not triumphalist
  body: Conditional scenarios, not promises. Always downstream of framework validation.
right_rail:
  related:
  - title: Key Results
    url: /results/
  - title: Framework
    url: /framework/about/
  meta:
    type: Lane Root
    status: Conditional
    updated: April 2026
---

## Public-Good Deployment Portfolios

The Impact lane translates framework claims into conditional consequence portfolios. Each portfolio asks: **if the framework holds, what could change in this domain?**

Every portfolio is:
- **Assumption-led** — states what must hold before consequences follow
- **Downstream** — always traces back to Framework, Results, and Verify lanes
- **Public-good oriented** — framed around societal benefit, not commercial value
- **Conditional** — never triumphalist, always explicit about preconditions

## Portfolios

{% for p in site.data.impact.portfolios %}- **[{{ p.title }}]({{ p.url | relative_url }})** — {{ p.summary_short }} ({{ p.paper_count }} {% if p.paper_count == 1 %}paper{% else %}papers{% endif %})
{% endfor %}


## Browse

- [All portfolios]({{ '/impact/by-portfolio/' | relative_url }})
- [By domain]({{ '/impact/by-domain/' | relative_url }})
- [By horizon]({{ '/impact/by-horizon/' | relative_url }})
