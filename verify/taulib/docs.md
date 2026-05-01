---
layout: program-doc
title: "TauLib Module and Declaration Browser"
permalink: /verify/taulib/docs/
lane: verify
v2_lane: verify
type: "TauLib Browser"
status: "Canonical"
summary_short: "Corpus-native browser for pinned TauLib modules and Lean declarations."
hero_ctas:
  - label: "Formalization Status"
    url: /verify/taulib/status/
    primary: true
  - label: "Release Manifest"
    url: /verify/release-manifest/
right_rail:
  related:
    - title: "TauLib Hub"
      url: /verify/taulib/
    - title: "Formalization Status"
      url: /verify/taulib/status/
    - title: "Release Manifest"
      url: /verify/release-manifest/
  meta:
    type: "TauLib Browser"
    status: "Canonical"
    updated: "April 2026"
---

{% assign summary = site.data.taulib_projections.summary %}
{% assign modules = site.data.taulib_projections.modules %}

## Corpus-Native Projection

This browser is generated directly from the pinned Corpus TauLib snapshot. It is not imported from generated HTML: the Corpus scanner reads the Lean source, extracts modules, imports, registry IDs, declarations, source spans, and stable Corpus documentation URLs, then projects those records into these public pages.

<div class="v2-grid">
  <article class="v2-tile"><strong>{{ summary.module_count | default: modules.size }} modules</strong><span>Pinned Lean modules with stable Corpus documentation URLs.</span></article>
  <article class="v2-tile"><strong>{{ summary.declaration_count }} declarations/evals</strong><span>Theorems, lemmas, definitions, structures, classes, inductives, axioms, examples, and evaluations.</span></article>
  <article class="v2-tile"><strong>{{ summary.registry_linked_module_count }} linked modules</strong><span>Modules with explicit Registry identifiers.</span></article>
  <article class="v2-tile"><strong>{{ summary.registry_linked_declaration_count }} linked declarations</strong><span>Declaration-level Registry evidence where the source exposes it.</span></article>
</div>

## Browse Modules

<div class="table-wrap">
<table>
  <thead>
    <tr>
      <th scope="col">Module</th>
      <th scope="col">Book</th>
      <th scope="col">Family</th>
      <th scope="col">Declarations</th>
      <th scope="col">Registry IDs</th>
    </tr>
  </thead>
  <tbody>
  {% for module in modules %}
    {% assign module_url = module["url"] | replace: "/verify/taulib/docs/", "/corpus/taulib/docs/" %}
    {% assign module_page = site.pages | where: "url", module_url | first %}
    <tr>
      <th scope="row">{% if module_page %}<a href="{{ module_url | relative_url }}"><code>{{ module.module_name }}</code></a>{% else %}<code>{{ module.module_name }}</code>{% endif %}</th>
      <td>{{ module.book | default: "Core" }}</td>
      <td>{{ module.family | default: "Root" }}</td>
      <td>{{ module.declarations | size }}</td>
      <td>{{ module.registry_ids | size }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>
</div>

## Projection Boundary

TauLib checks formal proof obligations where they are represented in Lean. It does not, by itself, settle bridge adequacy, empirical truth, semantic correspondence, or external acceptance. Those questions remain owned by the broader Verify lane.
