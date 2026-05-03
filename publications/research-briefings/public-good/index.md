---
layout: "program-doc"
lane: "publications"
v2_lane: "publications"
status: "Canonical"
last_updated: 2026-04-30
updated: "April 2026"
title: "Public-Good Briefings"
permalink: "/publications/research-briefings/public-good/"
type: "Publication Family"
hero_eyebrow: "Publications · Research Briefings · Public-Good Briefings"
summary_short: "44 conditional scenario briefings across 11 public-good portfolios."
publication_category: "research_briefing"
publication_subcategory: "public_good_briefing"
artifact_status: "html_pdf_available"
primary_or_secondary: "translation"
claim_role: "translation_briefing"
search_keywords:
  - "Public-Good Briefings"
  - "Public-Good Impact Dossiers"
  - "scenario briefings"
  - "PDF dossiers"
og_image: "/assets/images/plates/plate-07-stable-artifact-layer-og.jpg"
twitter_image: "/assets/images/plates/plate-07-stable-artifact-layer-og.jpg"
og_image_alt: "Scientific plate showing Public-Good Briefings as a family under Research Briefings inside the Publications taxonomy."
---

## What Public-Good Briefings are

Public-Good Briefings are Research Briefings: framework-grounded translation artifacts that explore what could become valuable in public-good domains if the relevant Results survive verification, translation, domain review, and uptake. All 44 briefings are now available as publication-ready PDF dossiers alongside their full HTML text.

They are not validation claims, policy commitments, implementation plans, or deployment-ready proposals. They are downstream conditional scenario analyses.

## Public-Good Briefings as Research Briefings

{% capture public_good_plate_caption %}Public-Good Briefings are a family of Research Briefings: conditional scenario briefings, not validation claims or deployment plans.{% endcapture %}
{% include scientific-plate.html id="plate-07-stable-artifact-layer" variant="thumb" class="scientific-plate--compact" caption=public_good_plate_caption loading="lazy" %}

Public-Good Briefings sit inside the Research Briefings category. Their role is to organize conditional scenario reasoning for public-good contexts while keeping claim status, verification status, and domain uptake separate.

## Public-Good Briefings and conditional impact

{% capture public_good_impact_plate_caption %}Public-Good Briefings belong to the outermost Impact stratum. They are conditional scenario briefings, not validation claims, policy commitments, or deployment plans.{% endcapture %}
{% include scientific-plate.html id="plate-08-conditional-impact-strata" variant="thumb" class="scientific-plate--compact" caption=public_good_impact_plate_caption loading="lazy" %}

Public-Good Briefings are conditional scenario artifacts. They explore what could become valuable if upstream Results survive verification, translation, domain review, and uptake. The PDF release does not change the claim status: domain review remains pending, and no deployment, product, validation, or policy-adoption claim is made.

## Current portfolios

<ul class="portfolio-grid portfolio-card-list">
{% for slug in site.data.impact.portfolio_order %}
  {% assign p = site.data.impact.portfolios[slug] %}
  <li>
    <article>
      <a href="{{ p.url | relative_url }}" class="portfolio-card impact-portfolio-card" style="{% include impact-portfolio-style.html portfolio=p %}">
        <span class="portfolio-card-icon">{% include icon.html name=p.icon class="impact-portfolio-card__icon" label=p.icon_alt %}</span>
        <span class="impact-portfolio-card__eyebrow">{{ p.family }}</span>
        <h3 class="portfolio-card-title">{{ p.title }}</h3>
        <p class="portfolio-card-summary">{{ p.summary_short }}</p>
        <span class="chip chip-small">{{ p.briefing_count }} {% if p.briefing_count == 1 %}briefing{% else %}briefings{% endif %}</span>
        <span class="chip chip-small">PDFs available</span>
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

{% for slug in site.data.impact.portfolio_order %}
{% assign portfolio = site.data.impact.portfolios[slug] %}
{% assign portfolio_briefings = site.data.impact["public-good-briefings"] | where: "portfolio_id", portfolio.id %}
{% assign briefing_count = portfolio_briefings | size %}
<section class="briefing-portfolio-group" aria-labelledby="briefings-{{ portfolio.slug }}">
  <h3 id="briefings-{{ portfolio.slug }}"><span class="impact-portfolio-pill" style="{% include impact-portfolio-style.html portfolio=portfolio %}">{% include icon.html name=portfolio.icon class="impact-portfolio-icon" label=portfolio.icon_alt %}<span>{{ portfolio.title }}</span></span> — {{ briefing_count }} {% if briefing_count == 1 %}briefing{% else %}briefings{% endif %}</h3>
  <ul class="pub-card-grid">
  {% for briefing in portfolio_briefings %}
  {% assign release = site.data.impact.public_good_dossier_release[briefing.slug] %}
  {% assign cover = "/assets/thumbnails/briefings/" | append: briefing.slug | append: "-cover.png" %}
    <li>
      <article class="pub-card">
        <a href="{{ briefing.landing_url | relative_url }}" aria-hidden="true" tabindex="-1">
          <img src="{{ cover | relative_url }}" alt="" class="pub-card__cover" loading="lazy" width="96" height="128" />
        </a>
        <div class="pub-card__body">
          <h4 class="pub-card__title"><a href="{{ briefing.landing_url | relative_url }}">{{ briefing.title }}</a></h4>
          <p class="pub-card__summary">{{ briefing.summary_short }}</p>
          {% if release %}
          <p class="pub-card__meta"><span>{{ release.release_date }}</span><span>{{ release.pdf_pages }} pages</span></p>
          {% endif %}
          <div class="pub-card__actions">
            {% if briefing.pdf_path %}<a href="{{ briefing.pdf_path | relative_url }}" class="chip chip-small">PDF</a>{% endif %}
            {% if briefing.full_html_path %}<a href="{{ briefing.full_html_path | relative_url }}" class="chip chip-small">Full HTML</a>{% endif %}
          </div>
        </div>
      </article>
    </li>
  {% endfor %}
  </ul>
</section>
{% endfor %}
