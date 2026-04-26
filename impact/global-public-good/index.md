---
layout: "program-doc"
title: "Global Public Good"
permalink: "/impact/global-public-good/"
lane: "impact"
type: "Impact Section"
status: "Conditional"
summary_short: "Conditional public-good portfolios for climate, energy, agriculture, health, water, weather, disaster resilience, biodiversity, pollution, solar, and ocean systems."
right_rail:
  related:
    -
      title: "Impact Framework"
      url: "/impact/impact-framework/"
    -
      title: "Public-Good Briefings"
      url: "/publications/research-briefings/public-good/"
    -
      title: "Results"
      url: "/results/"
    -
      title: "Verify"
      url: "/verify/"
  meta:
    type: "Impact Section"
    scope: "Conditional public-good portfolios"
    status: "Conditional"
    updated: "April 2026"
---

## What This Section Does

Global Public Good gathers conditional public-good portfolios.

These are not deployment claims. They are scenario maps: if the relevant Results hold, if they survive Verify, if they can be translated into domain-specific models, and if institutions can use them responsibly, what public-good pathways become worth investigating?

This stratum is the outermost Impact layer. It does not make the framework true. It does not make an application ready. It identifies where verified results could matter for planetary systems and public-good domains.

<div class="v2-grid">
  <div class="v2-tile">
    <strong>11 conditional public-good portfolios</strong>
    <span>Domain portfolios for agriculture, water, climate, health, energy, biodiversity, disaster resilience, pollution, solar, ocean systems, and weather-facing operations.</span>
  </div>
  <div class="v2-tile">
    <strong>44 Public-Good Briefings</strong>
    <span>Public-Good Briefings provide the deeper conditional scenario analyses behind the portfolio summaries.</span>
  </div>
</div>

## Deployment-status note

No portfolio on this page claims real-world adoption, policy implementation, external validation, or operational readiness. Every portfolio remains a scenario map until upstream Results survive verification, translation assumptions are tested, and domain uptake is possible.

## Relation to Public-Good Briefings

The portfolio pages organize public-good domains. [Public-Good Briefings]({{ '/publications/research-briefings/public-good/' | relative_url }}) are the publication artifacts attached to those domains.

## Reading discipline

Read this page through the [Impact Framework]({{ '/impact/impact-framework/' | relative_url }}): Result → Verification survival → Translation layer → Domain uptake → Consequence.

If any upstream link weakens, the public-good claim weakens with it.

## What this does not mean

This page does not claim adoption, deployment, policy implementation, external validation, operational readiness, or public-good delivery. It does not turn a portfolio into a program plan, institutional commitment, validated intervention, or field-ready proposal.

## Boundary condition

Public-good consequence remains conditional until upstream Results hold, verification surfaces survive scrutiny, translation assumptions are tested, domain review is possible, and domain uptake can actually occur.

## Portfolio Index

<div class="portfolio-grid">
{% for p in site.data.impact.portfolios %}
  <a href="{{ p.url | relative_url }}" class="portfolio-card">
    <h3 class="portfolio-card-title">{{ p.title }}</h3>
    <p class="portfolio-card-summary">{{ p.summary_short }}</p>
    <span class="chip chip-small">{{ p.briefing_count }} {% if p.briefing_count == 1 %}briefing{% else %}briefings{% endif %}</span>
  </a>
{% endfor %}
</div>
