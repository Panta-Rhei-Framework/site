---
layout: program-doc
title: Impact
permalink: /impact/
lane: impact
type: "Lane Root"
status: "Conditional"
summary_short: "If the framework holds, what could change? Conditional consequence surfaces across foundational science, applied research, education, orientation, societal coherence, and public-good deployment."
summary_cards:
  - title: "Impact is conditional"
    body: "The word if is load-bearing. Impact claims remain downstream of Results, Verify, and explicit translation assumptions."
  - title: "Six strata"
    body: "Foundational science, applied research, global education, existential orientation, societal coherence, and global public-good deployment."
  - title: "11 portfolios"
    body: "Global Public Good gathers 11 public-good portfolios and 44 companion papers."
hero_ctas:
  - label: "Impact Framework"
    url: /impact/impact-framework/
    primary: true
  - label: "Global Public Good"
    url: /impact/global-public-good/
  - label: "Foundational Science"
    url: /impact/foundational-science/
right_rail:
  related:
  - title: "Results"
    url: /results/
  - title: "Verify"
    url: /verify/
  - title: "Companion Papers"
    url: /publications/companion-papers/
  meta:
    type: "Lane Root"
    scope: "Conditional consequences"
    status: "Conditional"
    updated: "April 2026"
---

## Core Statement

Impact is conditional. This lane does not present promises, triumphalist claims, or productized certainty. It presents consequence structures that become relevant **if** the framework's [Results]({{ '/results/' | relative_url }}) hold and survive [Verify]({{ '/verify/' | relative_url }}).

The impact discipline is simple: a result does not automatically become a social consequence. It must survive scrutiny, pass through an explicit translation layer, meet domain uptake conditions, and remain honest about what is assumed.

## Why This Lane Exists

A framework of this scope would not affect only one layer of discourse if it were valid. Its consequences would appear at several levels:

- foundational science
- applied research and scientific toolchains
- education and public understanding
- existential orientation
- societal coherence
- global public-good deployment

These are not equal-strength claims. They are impact strata, each with its own assumptions, traceability requirements, and limits.

## Impact Pipeline

<div class="v2-system-row" aria-label="Impact pipeline">
  <a class="v2-system-node" href="{{ '/results/' | relative_url }}"><strong>Results</strong>What the framework claims follows.</a>
  <span class="v2-system-arrow">→</span>
  <a class="v2-system-node" href="{{ '/verify/' | relative_url }}"><strong>Verify</strong>What survives formal, empirical, and review pressure.</a>
  <span class="v2-system-arrow">→</span>
  <a class="v2-system-node" href="{{ '/impact/impact-framework/' | relative_url }}"><strong>Impact Framework</strong>How surviving results become conditional consequences.</a>
  <span class="v2-system-arrow">→</span>
  <a class="v2-system-node" href="{{ '/impact/global-public-good/' | relative_url }}"><strong>Public Good</strong>Where domain-specific deployment scenarios are organized.</a>
</div>

## Impact Strata

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/impact/foundational-science/' | relative_url }}">
    <h3>Foundational Science</h3>
    <p>How the framework could alter foundations, unification standards, and the comparison of scientific world-pictures.</p>
  </a>
  <a class="v2-tile" href="{{ '/impact/applied-science-and-research/' | relative_url }}">
    <h3>Applied Science & Research</h3>
    <p>How surviving results could generate downstream research agendas, modeling pathways, and formal toolchains.</p>
  </a>
  <a class="v2-tile" href="{{ '/impact/global-education/' | relative_url }}">
    <h3>Global Education</h3>
    <p>How the program could make difficult cross-domain science more teachable if the core structure holds.</p>
  </a>
  <a class="v2-tile" href="{{ '/impact/existential-orientation/' | relative_url }}">
    <h3>Existential Orientation</h3>
    <p>How humans might orient themselves differently in relation to life, mind, meaning, and reality.</p>
  </a>
  <a class="v2-tile" href="{{ '/impact/societal-coherence/' | relative_url }}">
    <h3>Societal Coherence</h3>
    <p>How a coherent framework could affect public tensions across scientific, philosophical, and existential registers.</p>
  </a>
  <a class="v2-tile" href="{{ '/impact/global-public-good/' | relative_url }}">
    <h3>Global Public Good</h3>
    <p>11 assumption-led public-good portfolios with 44 companion papers.</p>
  </a>
</div>

## Global Public-Good Portfolios

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

## Important Note

The word **if** is load-bearing. Impact remains downstream of explicit assumptions, translation layers, and survival under scrutiny. For the publication index of these papers, see [Companion Papers]({{ '/publications/companion-papers/' | relative_url }}).
