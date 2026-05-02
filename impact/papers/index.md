---
layout: program-doc
title: "Public-Good Briefing Full Texts"
permalink: /impact/papers/
lane: impact
v2_lane: impact
type: "Compatibility Index"
status: "Compatibility"
summary_short: "Compatibility index for full-text public-good briefing pages retained in the Impact lane."
right_rail:
  related:
    - title: "Public-Good Briefings"
      url: /publications/research-briefings/public-good/
    - title: "Impact"
      url: /impact/
    - title: "Impact Framework"
      url: /impact/impact-framework/
  meta:
    type: "Compatibility index"
    status: "Compatibility"
    updated: "May 2026"
---

## Public-Good Briefing Full Texts

These pages are retained as full-text Impact-lane reading surfaces for the Public-Good Briefings. The canonical publication landing pages live under [Public-Good Briefings]({{ '/publications/research-briefings/public-good/' | relative_url }}); the routes below preserve the longer HTML text for readers and reviewers.

<ul class="v2-grid v2-card-list">
{% assign briefing_pages = site.pages | where_exp: "item", "item.path contains 'impact/papers/'" | sort: "title" %}
{% for item in briefing_pages %}
  {% unless item.url == page.url %}
  <li>
    <article class="v2-tile">
      <p class="eyebrow">Public-Good Briefing · Full text</p>
      <h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
      {% if item.summary_short %}<p>{{ item.summary_short }}</p>{% endif %}
    </article>
  </li>
  {% endunless %}
{% endfor %}
</ul>

