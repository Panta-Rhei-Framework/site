---
layout: "program-doc"
lane: "publications"
v2_lane: "publications"
status: "Canonical"
updated: "April 2026"
title: "Public-Good Briefings"
permalink: "/publications/research-briefings/public-good/"
type: "Publication Family"
summary_short: "44 conditional scenario briefings across 11 public-good portfolios."
publication_category: "research_briefing"
publication_subcategory: "public_good_briefing"
artifact_status: "html_available"
primary_or_secondary: "translation"
claim_role: "translation_briefing"
search_keywords:
  - "Public-Good Briefings"
  - "public good papers"
  - "scenario briefings"
---

## What Public-Good Briefings are

Public-Good Briefings are Research Briefings: framework-grounded translation artifacts that explore what could become valuable in public-good domains if the relevant Results survive verification, translation, domain review, and uptake.

They are not validation claims, policy commitments, implementation plans, or deployment-ready proposals. They are downstream conditional scenario analyses.

## Current portfolios

<ul class="portfolio-grid portfolio-card-list">
{% for p in site.data.impact.portfolios %}
  {% assign portfolio_title = p.title | replace: "/", " / " %}
  <li>
    <article>
      <a href="{{ p.url | relative_url }}" class="portfolio-card">
        <h3 class="portfolio-card-title">{{ portfolio_title }}</h3>
        <p class="portfolio-card-summary">{{ p.summary_short }}</p>
        <span class="chip chip-small">{{ p.briefing_count }} {% if p.briefing_count == 1 %}briefing{% else %}briefings{% endif %}</span>
      </a>
    </article>
  </li>
{% endfor %}
</ul>

## Reading discipline

Read every Public-Good Briefing through the Impact chain:

Result → Verification survival → Translation layer → Domain uptake → Consequence.

If any upstream link weakens, the public-good claim weakens with it.

## Browse briefings

{% for portfolio in site.data.impact.portfolios %}
{% assign portfolio_briefings = site.data.impact["public-good-briefings"] | where: "portfolio_id", portfolio.id %}
{% assign briefing_count = portfolio_briefings | size %}
{% assign portfolio_title = portfolio.title | replace: "/", " / " %}
<section class="briefing-portfolio-group" aria-labelledby="briefings-{{ portfolio.slug }}">
  <h3 id="briefings-{{ portfolio.slug }}">{{ portfolio_title }} — {{ briefing_count }} {% if briefing_count == 1 %}briefing{% else %}briefings{% endif %}</h3>
  <div class="dep-list">
  {% for briefing in portfolio_briefings %}
    <a class="dep-link" href="{{ briefing.landing_url | relative_url }}">
      <span class="dep-title">{{ briefing.title }}</span>
      <span class="dep-meta">{{ briefing.summary_short }}</span>
    </a>
  {% endfor %}
  </div>
</section>
{% endfor %}
