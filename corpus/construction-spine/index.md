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
og_image: /assets/images/plates/plate-04-construction-spine-og.jpg
twitter_image: /assets/images/plates/plate-04-construction-spine-og.jpg
og_image_alt: "Scientific plate showing the Corpus Construction Spine as a ten-step build sequence from Kernel to Ontic Closure."
hero_ctas:
  - label: "Step 1: Build the τ-Kernel"
    url: /corpus/construction-spine/build-the-kernel/
    primary: true
  - label: "Foundational Hinges"
    url: /corpus/foundational-hinges/
  - label: "Construction Roadmap"
    url: /program/research-agenda/construction-roadmap/
  - label: "Progress Against Agenda"
    url: /results/progress-against-agenda/
right_rail:
  related:
    - title: "Verify the Construction Spine"
      url: /verify/construction-spine-verification/
    - title: "Foundational Hinges"
      url: /corpus/foundational-hinges/
    - title: "Bi-Square Spine"
      url: /corpus/bi-square/
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

{% assign steps = site.data.construction_spine["construction-spine-data"] %}

## What this spine is

The Construction Spine is the Corpus-side realization of the Research Agenda's Construction Roadmap. It shows how the Corpus is built step by step: from kernel definition through mathematics, physics, life, reflective structure, self-hosting, and ontic closure.

## From kernel to ontic closure

{% capture construction_spine_plate_caption %}The Construction Spine gives the human-readable build order of the Corpus: from the formal kernel through mathematical recovery, physical grammar, empirical bridges, life, reflection, self-hosting, and ontic closure.{% endcapture %}
{% include scientific-plate.html id="plate-04-construction-spine" class="scientific-plate--construction-spine" caption=construction_spine_plate_caption loading="lazy" %}

The ten construction steps show how the Corpus is built: not as a timeline or sprint plan, but as a logical build order from the formal kernel to ontic-closure testing.

## One spine, several projections

- [Registry]({{ '/corpus/registry/' | relative_url }}) is the atomic item projection.
- [TauLib]({{ '/verify/taulib/' | relative_url }}) is the Lean formalization projection.
- [Publications]({{ '/publications/' | relative_url }}) are narrative proof-order projections.
- [Corpus Graph]({{ '/corpus/graph/' | relative_url }}) is the dependency projection.
- [Bi-Square Spine]({{ '/corpus/bi-square/' | relative_url }}) is the diagrammatic-shape route: tower coherence, spectral naturality, and pasting across the main algebraic, geometric, enriched, and computational lifts.

## Kernel starting point

{% capture tau_kernel_plate_caption %}The τ-Kernel is the constrained formal core from which the construction begins: five generators, one primitive iterator, K0–K6 axiomatic constraints, and constructive closure under a no-hidden-runtime / no-hidden-substrate discipline.{% endcapture %}
{% include scientific-plate.html id="plate-10-tau-kernel" variant="thumb" class="scientific-plate--compact scientific-plate--tau-kernel" caption=tau_kernel_plate_caption loading="lazy" %}

The first construction step defines the kernel before later mathematics, physics, life, reflection, self-hosting, and ontic-closure burdens can be read as generated structure.

### Foundational hinge route

The first three construction steps are supported by a foundational hinge route: eight standalone research papers plus a bundle memo. These papers isolate the make-or-break mathematical constructions behind the τ-Kernel, recovered mathematics, and self-enrichment. Use the hinge route when you want the stress-test packet rather than the full monograph or atomic registry.

<div class="btn-group section-ctas">
  <a class="btn-secondary" href="{{ '/corpus/foundational-hinges/' | relative_url }}">Open the Foundational Hinges</a>
  <a class="btn-ghost" href="{{ '/publications/research-papers/' | relative_url }}">Research Papers</a>
  <a class="btn-ghost" href="{{ '/registry/dashboards/book-i/' | relative_url }}">Book I Dashboard</a>
</div>

## The ten construction steps

<ol class="v2-grid v2-step-list">
{% for step in steps %}
  <li>
    <a class="v2-tile" href="{{ step.corpus_path | relative_url }}">
      <article>
        <h3>{{ step.sequence }}. {{ step.title }}</h3>
        <p>{{ step.summary }}</p>
        <span class="chip">{{ step.build_status | replace: "_", " " }}</span>
      </article>
    </a>
  </li>
{% endfor %}
</ol>

## How to read this section

Each step page explains what the step builds, why it is required, the key constructions, related Registry items, TauLib modules, book locations, related Results, Verify surfaces, and what the step does not yet establish.

Use [Verify the Construction Spine]({{ '/verify/construction-spine-verification/' | relative_url }}) when you want the inspection matrix rather than the build narrative.

<div class="notice note"><strong>Status note.</strong> Build status reflects the current internal state of the Corpus. It does not imply external acceptance unless explicitly stated.</div>

## Build status legend

- **Framed** — the step is defined as a required construction obligation.
- **Partially built** — relevant Corpus structures exist, but mappings or verification remain incomplete.
- **Internally addressed** — the Corpus contains a substantive internal construction for this step.
- **Bridge pending** — internal structures exist, but measurement, standard-domain, or external bridge verification remains open.

These labels describe the program's internal construction state. They do not indicate external verification or scientific acceptance.
