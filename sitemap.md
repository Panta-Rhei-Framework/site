---
layout: program-doc
title: "Sitemap"
lane: support
shell: home
type: support_page
support_type: sitemap
status: canonical
updated: "May 2026"
permalink: /sitemap/
summary: "Human-readable map of the Panta Rhei public research observatory."
summary_short: "Human-readable map of the Panta Rhei public research observatory."
right_rail:
  related:
  - title: Discover
    url: /discover/
  - title: Agenda
    url: /program/research-agenda/
  - title: XML Sitemap
    url: /sitemap.xml
  meta:
    type: "Support page"
    scope: "Sitemap"
    status: "Canonical"
    updated: "May 2026"
---

{% assign sitemap_data = site.data.sitemap_v4 %}

<section class="sitemap-intro" aria-labelledby="sitemap-directory-heading">
  <h2 id="sitemap-directory-heading">Observatory directory</h2>
  <p>{{ sitemap_data.intro }}</p>
</section>

<section class="sitemap-section" aria-labelledby="sitemap-primary-lanes-heading">
  <h2 id="sitemap-primary-lanes-heading">Primary lanes</h2>
  <div class="sitemap-grid sitemap-grid-primary">
    {% for lane in sitemap_data.primary_lanes %}
    <article class="sitemap-card sitemap-card-primary" data-sitemap-lane="{{ lane.title | slugify }}">
      <div class="sitemap-card-header">
        <p class="sitemap-card-role">{{ lane.role }}</p>
        <h3>{{ lane.title }}</h3>
        <p>{{ lane.description }}</p>
      </div>
      <ul class="sitemap-chip-list" aria-label="{{ lane.title }} pages">
        {% for link in lane.links %}
        <li><a class="sitemap-chip" href="{{ link.url | relative_url }}">{{ link.title }}</a></li>
        {% endfor %}
      </ul>
      <a class="sitemap-card-cta" href="{{ lane.root_url | relative_url }}">{{ lane.root_label }}</a>
    </article>
    {% endfor %}
  </div>
</section>

<section class="sitemap-section" aria-labelledby="sitemap-support-heading">
  <h2 id="sitemap-support-heading">Artifacts, media, and infrastructure</h2>
  {% assign support = sitemap_data.support %}
  <article class="sitemap-card sitemap-card-support" data-sitemap-lane="support">
    <div class="sitemap-card-header">
      <p class="sitemap-card-role">{{ support.role }}</p>
      <h3>{{ support.title }}</h3>
      <p>{{ support.description }}</p>
    </div>
    <ul class="sitemap-chip-list" aria-label="{{ support.title }} pages">
      {% for link in support.links %}
      <li><a class="sitemap-chip" href="{{ link.url | relative_url }}">{{ link.title }}</a></li>
      {% endfor %}
    </ul>
    <a class="sitemap-card-cta" href="{{ support.root_url | relative_url }}">{{ support.root_label }}</a>
  </article>
</section>

<section class="sitemap-machine" aria-labelledby="sitemap-machine-heading">
  <h2 id="sitemap-machine-heading">Machine-readable sitemap</h2>
  <p>The machine-readable sitemap remains available at <a href="{{ '/sitemap.xml' | relative_url }}">sitemap.xml</a>.</p>
</section>
