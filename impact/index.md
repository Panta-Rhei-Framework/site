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
  - title: Claims
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

<div class="portfolio-grid">
{% for p in site.data.impact.portfolios %}
  <a href="{{ p.url | relative_url }}" class="portfolio-card">
    <div class="portfolio-card-icon">
      {% case p.slug %}
      {% when 'agriculture' %}
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22V8"/><path d="M5 12s2.5-5 7-5 7 5 7 5"/><path d="M5 18s2.5-5 7-5 7 5 7 5"/></svg>
      {% when 'biodiversity-restoration' %}
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22V12"/><path d="M12 12c-3-4-8-3-8 2"/><path d="M12 12c3-4 8-3 8 2"/><path d="M12 8c-2-3-6-3-6 1"/><path d="M12 8c2-3 6-3 6 1"/><circle cx="12" cy="4" r="1.5"/></svg>
      {% when 'climate' %}
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><path d="M12 1v2"/><path d="M12 21v2"/><path d="M4.22 4.22l1.42 1.42"/><path d="M18.36 18.36l1.42 1.42"/><path d="M1 12h2"/><path d="M21 12h2"/><path d="M4.22 19.78l1.42-1.42"/><path d="M18.36 5.64l1.42-1.42"/></svg>
      {% when 'disaster' %}
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M12 8v4"/><circle cx="12" cy="16" r="0.5" fill="currentColor"/></svg>
      {% when 'energy' %}
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
      {% when 'ocean' %}
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12c2-2 4-2 6 0s4 2 6 0 4-2 6 0"/><path d="M2 17c2-2 4-2 6 0s4 2 6 0 4-2 6 0"/><path d="M2 7c2-2 4-2 6 0s4 2 6 0 4-2 6 0"/></svg>
      {% when 'one-health' %}
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/><path d="M8 12h8"/><path d="M12 8v8"/></svg>
      {% when 'pollution-circularity' %}
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7.5 7.5c3-5 9-3 9 2"/><path d="M16.5 16.5c-3 5-9 3-9-2"/><polyline points="16.5 4.5 16.5 9.5 11.5 9.5"/><polyline points="7.5 19.5 7.5 14.5 12.5 14.5"/></svg>
      {% when 'solar' %}
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="7" r="4"/><path d="M12 1v1"/><path d="M12 12v1"/><path d="M6.34 2.34l.7.7"/><path d="M16.96 3.04l.7-.7"/><path d="M4 7h1"/><path d="M19 7h1"/><rect x="4" y="16" width="16" height="6" rx="1"/><path d="M8 16v6"/><path d="M12 16v6"/><path d="M16 16v6"/></svg>
      {% when 'water-wash' %}
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>
      {% when 'weather' %}
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg>
      {% endcase %}
    </div>
    <h3 class="portfolio-card-title">{{ p.title }}</h3>
    <p class="portfolio-card-summary">{{ p.summary_short }}</p>
    <span class="chip chip-small">{{ p.paper_count }} {% if p.paper_count == 1 %}paper{% else %}papers{% endif %}</span>
  </a>
{% endfor %}
</div>
