---
layout: program-doc
title: "TauLib Module Explorer"
permalink: /corpus/taulib/modules/
lane: corpus
v2_lane: corpus
type: "Corpus Projection Explorer"
status: "Canonical"
summary_short: "Filterable module inventory for the compiled Lean projection of the Corpus."
right_rail:
  related:
    - title: "TauLib"
      url: /corpus/taulib/
    - title: "TauLib Docs"
      url: /corpus/taulib/docs/
    - title: "Registry Graph"
      url: /corpus/graph/
---

{% assign modules = site.data.taulib_projections.modules %}

## Browse Modules

The full module inventory is rendered below for crawlers and non-JavaScript readers. The controls progressively enhance the list in the browser.

<div class="content-browser" id="taulib-module-explorer" data-module-count="{{ modules.size }}">
  <div class="compact-toolbar" aria-label="Filter TauLib modules">
    <label>Book <select id="taulib-book-filter"><option value="">All</option><option>BookI</option><option>BookII</option><option>BookIII</option><option>BookIV</option><option>BookV</option><option>BookVI</option><option>BookVII</option><option>Tour</option></select></label>
    <label>Family <input id="taulib-family-filter" type="search" placeholder="Kernel, Boundary, Gravity..."></label>
    <label>Registry ID <input id="taulib-registry-filter" type="search" placeholder="I.D01"></label>
    <label>Search <input id="taulib-search-filter" type="search" placeholder="module name"></label>
    <button class="btn-secondary" id="taulib-clear-filters" type="button">Clear</button>
    <span class="filter-count" id="taulib-module-count">{{ modules.size }} modules</span>
  </div>

  <ol class="v2-grid v2-card-list module-explorer-grid" id="taulib-module-list">
  {% for module in modules %}
    {% assign module_url = module["url"] | replace: "/verify/taulib/docs/", "/corpus/taulib/docs/" %}
    {% assign module_page = site.pages | where: "url", module_url | first %}
    <li class="module-card"
        data-book="{{ module.book }}"
        data-family="{{ module.family }}"
        data-module="{{ module.module_name | downcase }}"
        data-registry="{{ module.registry_ids | join: ' ' }}">
      <article class="v2-tile">
        <p class="eyebrow">{{ module.book | default: "TauLib" }}{% if module.family %} · {{ module.family }}{% endif %}</p>
        <h3>{% if module_page %}<a href="{{ module_url | relative_url }}">{{ module.module_name }}</a>{% else %}<code>{{ module.module_name }}</code>{% endif %}</h3>
        <p>{{ module.line_count }} lines · {{ module.registry_ids | size }} registry anchors.</p>
        {% unless module_page %}<p class="muted">Corpus module page pending in the public projection.</p>{% endunless %}
        {% if module.registry_ids and module.registry_ids.size > 0 %}
        <p>{% for id in module.registry_ids limit: 6 %}<a class="chip" href="{{ '/registry/object/' | append: id | append: '/' | relative_url }}">{{ id }}</a>{% endfor %}</p>
        {% endif %}
      </article>
    </li>
  {% endfor %}
  </ol>
</div>

<script defer src="{{ '/assets/js/taulib-modules.js' | relative_url }}"></script>
