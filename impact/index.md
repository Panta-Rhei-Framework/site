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

The Impact lane translates [framework claims]({{ '/framework/about/' | relative_url }}) into conditional consequence portfolios. Each portfolio asks: **if the framework holds, what could change in this domain?**

The word *if* is load-bearing. The framework's [key results]({{ '/results/' | relative_url }}) carry explicit epistemic status labels — resolved, partial, qualitative, or contradicted — and only results that survive the [verification surfaces]({{ '/verify/' | relative_url }}) earn the right to generate downstream consequences. A conditional portfolio does not promise that a consequence will materialize. It maps what *would* follow if the underlying framework claims hold, so that domain experts can evaluate the conditional chain independently.

This is the structure of honest public-good reasoning from an independent research program: trace the chain from [kernel]({{ '/framework/about/what-the-tau-framework-is/' | relative_url }}) to consequence, type the assumptions at every step, and let the evidence decide.

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
