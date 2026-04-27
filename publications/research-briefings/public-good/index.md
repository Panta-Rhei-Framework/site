---
layout: "program-doc"
lane: "publications"
v2_lane: "publications"
status: "Canonical"
updated: "April 2026"
title: "Public-Good Briefings"
permalink: "/publications/research-briefings/public-good/"
type: "Publication Family"
hero_eyebrow: "Publications · Research Briefings · Public-Good Briefings"
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
og_image: "/assets/images/plates/plate-07-stable-artifact-layer-og.jpg"
twitter_image: "/assets/images/plates/plate-07-stable-artifact-layer-og.jpg"
og_image_alt: "Scientific plate showing Public-Good Briefings as a family under Research Briefings inside the Publications taxonomy."
---

## What Public-Good Briefings are

Public-Good Briefings are Research Briefings: framework-grounded translation artifacts that explore what could become valuable in public-good domains if the relevant Results survive verification, translation, domain review, and uptake.

They are not validation claims, policy commitments, implementation plans, or deployment-ready proposals. They are downstream conditional scenario analyses.

## Public-Good Briefings as Research Briefings

{% capture public_good_plate_caption %}Public-Good Briefings are a family of Research Briefings: conditional scenario briefings, not validation claims or deployment plans.{% endcapture %}
{% include scientific-plate.html id="plate-07-stable-artifact-layer" variant="thumb" class="scientific-plate--compact" caption=public_good_plate_caption loading="lazy" %}

Public-Good Briefings sit inside the Research Briefings category. Their role is to organize conditional scenario reasoning for public-good contexts while keeping claim status, verification status, and domain uptake separate.

## Public-Good Briefings and conditional impact

{% capture public_good_impact_plate_caption %}Public-Good Briefings belong to the outermost Impact stratum. They are conditional scenario briefings, not validation claims, policy commitments, or deployment plans.{% endcapture %}
{% include scientific-plate.html id="plate-08-conditional-impact-strata" variant="thumb" class="scientific-plate--compact" caption=public_good_impact_plate_caption loading="lazy" %}

Public-Good Briefings are conditional scenario artifacts. They explore what could become valuable if upstream Results survive verification, translation, domain review, and uptake.

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
  <ul class="briefing-list">
  {% for briefing in portfolio_briefings %}
    <li>
      <article class="briefing-card">
        <h4><a href="{{ briefing.landing_url | relative_url }}">{{ briefing.title }}</a></h4>
        <p>{{ briefing.summary_short }}</p>
      </article>
    </li>
  {% endfor %}
  </ul>
</section>
{% endfor %}
