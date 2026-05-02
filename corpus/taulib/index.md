---
layout: program-doc
title: "TauLib"
permalink: /corpus/taulib/
lane: corpus
v2_lane: corpus
type: "Corpus Projection"
status: "Canonical"
summary_short: "The compiled Lean projection of the Corpus."
hero_ctas:
  - label: "Browse Modules"
    url: /corpus/taulib/modules/
    primary: true
  - label: "Module Docs"
    url: /corpus/taulib/docs/
  - label: "Status"
    url: /corpus/taulib/status/
  - label: "Verify Bridge"
    url: /verify/taulib/
right_rail:
  related:
    - title: "Corpus"
      url: /corpus/
    - title: "TauLib Modules"
      url: /corpus/taulib/modules/
    - title: "TauLib Docs"
      url: /corpus/taulib/docs/
    - title: "TauLib Status"
      url: /corpus/taulib/status/
    - title: "TauLib Inspection Bridge"
      url: /verify/taulib/
  meta:
    type: "Corpus Projection"
    status: "Canonical"
    updated: "April 2026"
---

## Compiled Lean projection

TauLib now belongs to the Corpus lane because it is one of the Corpus projections: a compiled Lean module inventory, source map, Registry-link map, import graph, and generated module documentation.

That ownership move does not weaken verification. It makes the boundary cleaner: the Corpus publishes the compiled projection; Verify asks what the projection covers, what its formal terms mean, where semantic bridges hold, and what remains externally assessable.

<ul class="v2-grid v2-card-list">
  <li><article class="v2-tile"><h3>{% include release-metric.html id="taulib.modules" unit=true %}</h3><p>Lean modules in the pinned TauLib source projection.</p></article></li>
  <li><article class="v2-tile"><h3>{% include release-metric.html id="taulib.lines" unit=true %}</h3><p>Source lines counted from the imported TauLib snapshot.</p></article></li>
  <li><article class="v2-tile"><h3>{% include release-metric.html id="taulib.declarations" unit=true %}</h3><p>Declarations and computational evaluations discovered by the projection scanner.</p></article></li>
  <li><article class="v2-tile"><h3>{% include release-metric.html id="taulib.registry_links" unit=true %}</h3><p>Registry-to-module anchors that connect the atomic Corpus to Lean source.</p></article></li>
</ul>

## Entry points

<ul class="v2-grid v2-card-list">
  <li><article class="v2-tile"><h3><a href="{{ '/corpus/taulib/modules/' | relative_url }}">Module explorer</a></h3><p>Filter TauLib modules by book, family, module name, and Registry ID.</p></article></li>
  <li><article class="v2-tile"><h3><a href="{{ '/corpus/taulib/docs/' | relative_url }}">Generated module docs</a></h3><p>One generated page per module with imports, source links, and Registry anchors.</p></article></li>
  <li><article class="v2-tile"><h3><a href="{{ '/corpus/taulib/status/' | relative_url }}">Projection status</a></h3><p>Counts, source pin, and projection boundaries.</p></article></li>
  <li><article class="v2-tile"><h3><a href="{{ '/corpus/taulib/architecture/' | relative_url }}">Architecture</a></h3><p>Book and family structure, import graph, and relation to the Construction Map.</p></article></li>
</ul>

## Verification boundary

Lean compilation is treated here as a published baseline artifact. The Verify lane is still the place to inspect semantic adequacy, bridge assumptions, empirical accountability, and external assessment.

<div class="btn-group section-ctas">
  <a class="btn-secondary" href="{{ '/verify/taulib/' | relative_url }}">Open the TauLib inspection bridge</a>
  <a class="btn-ghost" href="{{ '/verify/verification-framework/' | relative_url }}">Verification Framework</a>
  <a class="btn-ghost" href="{{ '/verify/release-manifest/' | relative_url }}">Release Manifest</a>
</div>
