---
layout: program-doc
title: "TauLib Docs"
permalink: /corpus/taulib/docs/
lane: corpus
v2_lane: corpus
type: "Corpus Projection Docs"
status: "Canonical"
summary_short: "Generated Corpus-owned module documentation for TauLib."
right_rail:
  related:
    - title: "TauLib"
      url: /corpus/taulib/
    - title: "Module Explorer"
      url: /corpus/taulib/modules/
---

{% assign modules = site.data.taulib_projections.modules %}

## Generated module docs

Each module page records source path, imports, Registry anchors, and upstream source link. These pages are documentation of the Corpus projection; semantic interpretation belongs in Verify.

<ul class="v2-grid v2-card-list">
{% for module in modules limit: 36 %}
  {% assign module_url = module["url"] | replace: "/corpus/taulib/docs/", "/corpus/taulib/docs/" %}
  {% assign module_page = site.pages | where: "url", module_url | first %}
  <li><article class="v2-tile"><p class="eyebrow">{{ module.book | default: "TauLib" }}{% if module.family %} · {{ module.family }}{% endif %}</p><h3>{% if module_page %}<a href="{{ module_url | relative_url }}">{{ module.module_name }}</a>{% else %}<code>{{ module.module_name }}</code>{% endif %}</h3><p>{{ module.line_count }} lines · {{ module.registry_ids | size }} registry anchors.</p>{% unless module_page %}<p class="muted">Corpus module page pending in the public projection.</p>{% endunless %}</article></li>
{% endfor %}
</ul>

<p class="muted">The first 36 module docs are listed here for scanability. Use the <a href="{{ '/corpus/taulib/modules/' | relative_url }}">module explorer</a> for the full inventory.</p>
