---
layout: program-doc
title: "Construction Spine"
permalink: /corpus/construction-spine/
lane: corpus
v2_lane: corpus
section: construction-spine
type: "Corpus Index"
status: "Canonical"
summary_short: "The build-order narrative of the Panta Rhei Corpus."
hero_ctas:
  - label: "Step 1: Define the Kernel"
    url: /corpus/construction-spine/define-the-kernel/
    primary: true
  - label: "Construction Roadmap"
    url: /program/research-agenda/construction-roadmap/
  - label: "Progress Against Agenda"
    url: /results/progress-against-agenda/
right_rail:
  related:
    - title: "Registry"
      url: /corpus/registry/
    - title: "TauLib"
      url: /verify/taulib/
    - title: "Corpus Graph"
      url: /corpus/graph/
    - title: "Results"
      url: /results/
  meta:
    type: "Corpus Index"
    scope: "10 construction steps"
    status: "Canonical"
    updated: "April 2026"
---

{% assign steps = site.data.construction_spine["construction-spine"] %}

## What this spine is

The Construction Spine is the Corpus-side realization of the Research Agenda's Construction Roadmap. It shows how the Corpus is built step by step: from kernel definition through mathematics, physics, life, reflective structure, self-hosting, and ontic closure.

## One spine, several projections

- [Registry]({{ '/corpus/registry/' | relative_url }}) is the atomic item projection.
- [TauLib]({{ '/verify/taulib/' | relative_url }}) is the Lean formalization projection.
- [Publications]({{ '/publications/' | relative_url }}) are narrative proof-order projections.
- [Corpus Graph]({{ '/corpus/graph/' | relative_url }}) is the dependency projection.

## The ten construction steps

<div class="v2-grid">
{% for step in steps %}
  <a class="v2-tile" href="{{ step.corpus_path | relative_url }}">
    <strong>{{ step.sequence }}. {{ step.title }}</strong>
    <span>{{ step.summary }}</span>
    <span class="chip">{{ step.build_status | replace: "_", " " }}</span>
  </a>
{% endfor %}
</div>

## How to read this section

Each step page explains what the step builds, why it is required, the key constructions, related Registry items, TauLib modules, book locations, related Results, Verify surfaces, and what the step does not yet establish.

<div class="notice note"><strong>Status note.</strong> Build status reflects the current internal state of the Corpus. It does not imply external acceptance unless explicitly stated.</div>

