---
layout: program-doc
title: "Corpus"
lane: corpus
v2_lane: corpus
permalink: /corpus/
type: "Lane Root"
status: "Canonical"
summary_short: "The living, versioned research corpus of the program."
og_image: /assets/images/plates/plate-04-construction-spine-og.jpg
twitter_image: /assets/images/plates/plate-04-construction-spine-og.jpg
og_image_alt: "Scientific plate showing the Corpus Construction Spine as a ten-step build sequence from Kernel to Ontic Closure."
summary_cards:
  - title: "Research body"
    body: "Definitions, lemmas, theorems, structures, and dependency relations."
  - title: "Construction spine"
    body: "The public build-order narrative traces the Corpus through ten canonical construction steps."
  - title: "Public projections"
    body: "Results, publications, verification, and TauLib are projections of the corpus."
hero_ctas:
  - label: "Follow the Construction Spine"
    url: /corpus/construction-spine/
    primary: true
  - label: "Open Monographs"
    url: /corpus/monographs/
  - label: "Bi-Square Spine"
    url: /corpus/bi-square/
  - label: "Foundational Hinges"
    url: /corpus/foundational-hinges/
  - label: "Browse the Registry"
    url: /corpus/registry/
  - label: "How to Read"
    url: /corpus/how-to-read/
right_rail:
  related:
    - title: "Construction Spine"
      url: /corpus/construction-spine/
    - title: "Bi-Square Spine"
      url: /corpus/bi-square/
    - title: "Foundational Hinges"
      url: /corpus/foundational-hinges/
    - title: "Monographs"
      url: /corpus/monographs/
    - title: "Registry"
      url: /corpus/registry/
    - title: "Types"
      url: /corpus/types/
    - title: "How to Read"
      url: /corpus/how-to-read/
    - title: "Corpus Graph"
      url: /corpus/graph/
  meta:
    type: "Lane Root"
    status: "Canonical"
    updated: "April 2026"
---

## What the corpus is

{% assign registry_objects = site.data.registry.objects %}
{% assign type_groups = registry_objects | group_by: "type" | sort: "name" %}

The corpus is the central research artifact of the program: the public body of what has been built.

It is not a summary, not a set of claims, and not a collection of papers. It is the structured body of what has been built: definitions, lemmas, theorems, structures, derivations, and dependency relations.

<p class="eyebrow">The build-order at a glance</p>

## The Construction Spine

{% include scientific-plate.html id="plate-04-construction-spine" class="scientific-plate--construction-spine" loading="lazy" %}

The Construction Spine is the primary human-readable route into the Corpus. It shows the build-order narrative from kernel definition through mathematics, physics, life, reflective structure, self-hosting, and ontic closure.

<div class="btn-group section-ctas">
  <a class="btn-secondary" href="{{ '/corpus/construction-spine/' | relative_url }}">Open the Construction Spine</a>
  <a class="btn-ghost" href="{{ '/corpus/registry/' | relative_url }}">Explore the Registry</a>
  <a class="btn-ghost" href="{{ '/verify/taulib/' | relative_url }}">Inspect TauLib</a>
  <a class="btn-ghost" href="{{ '/verify/construction-spine-verification/' | relative_url }}">Verify the Construction Spine</a>
</div>

## The τ-Kernel

{% include scientific-plate.html id="plate-10-tau-kernel" variant="thumb" class="scientific-plate--compact scientific-plate--tau-kernel" loading="lazy" %}

The τ-Kernel is the formal starting point of the construction. It is not a hidden physical substrate; it is the constrained formal core from which the Corpus begins.

## The Bi-Square Spine

{% capture bi_square_plate_caption %}The Bi-Square Spine shows the repeated categorical shape that carries the kernel through its main lifts: tower coherence on the left, spectral naturality on the right, and a pasted constraint that becomes richer at each layer.{% endcapture %}
{% include scientific-plate.html id="plate-15-bi-square-spine" variant="thumb" class="scientific-plate--compact scientific-plate--bi-square-spine" caption=bi_square_plate_caption loading="lazy" %}

The [Bi-Square Spine]({{ '/corpus/bi-square/' | relative_url }}) is the Corpus route for the repeated proof-organizing diagram behind the kernel buildup. The Construction Spine gives the build order; the bi-square gives a stable categorical shape that reappears as algebraic, geometric, enriched, and computational structure.

## Foundational hinge route

The first three construction steps now have a dedicated reviewer route: eight foundational hinge papers plus a bundle memo, surfaced through Corpus-native hinge pages. These pages explain how the kernel is built, how core mathematics is recovered, and how self-enrichment begins.

<div class="btn-group section-ctas">
  <a class="btn-secondary" href="{{ '/corpus/foundational-hinges/' | relative_url }}">Open the Foundational Hinges</a>
  <a class="btn-ghost" href="{{ '/publications/research-papers/' | relative_url }}">Research Papers</a>
  <a class="btn-ghost" href="{{ '/verify/how-to-audit/mathematician/' | relative_url }}">Mathematician Audit Route</a>
</div>

## Corpus projections

The same research body appears through several public projections. The [Construction Spine]({{ '/corpus/construction-spine/' | relative_url }}) gives the build order; the [Corpus Monographs]({{ '/corpus/monographs/' | relative_url }}) expose the seven books as Book → Part → Chapter reading editions; the [Registry]({{ '/corpus/registry/' | relative_url }}) exposes atomic objects; [TauLib]({{ '/verify/taulib/' | relative_url }}) exposes formal proof surfaces where available; and the [Graph]({{ '/corpus/graph/' | relative_url }}) exposes dependency structure.

<ul class="v2-grid v2-card-list">
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/construction-spine/' | relative_url }}">
        <h3>Construction Spine</h3>
        <p>The human-readable build-order route through the Corpus.</p>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/monographs/' | relative_url }}">
        <h3>Corpus Monographs</h3>
        <p>Open Book → Part → Chapter reading editions of the seven research monographs.</p>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/bi-square/' | relative_url }}">
        <h3>Bi-Square Spine</h3>
        <p>The repeated proof-organizing shape that links tower coherence, spectral naturality, and layer-specific pasting constraints.</p>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/registry/' | relative_url }}">
        <h3>Registry</h3>
        <p>The atomic projection of definitions, propositions, theorems, and dependency anchors.</p>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/graph/' | relative_url }}">
        <h3>Dependency Graph</h3>
        <p>The relation surface connecting objects, monograph exposition, results, and verification routes.</p>
      </a>
    </article>
  </li>
</ul>

## Current state

The current registry is the public atomic projection of the corpus. The primary human-readable route into the Corpus is the [Construction Spine]({{ '/corpus/construction-spine/' | relative_url }}): the build-order narrative from kernel definition through mathematics, physics, life, reflective structure, self-hosting, and ontic closure.

<ul class="v2-grid v2-card-list">
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/construction-spine/' | relative_url }}">
        <h3>10 construction steps</h3>
        <p>The public build narrative that aligns Agenda obligations, Corpus construction, and Results status.</p>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/foundational-hinges/' | relative_url }}">
        <h3>8 foundational hinges</h3>
        <p>The reviewer-facing stress-test route for the mathematical hinges behind Steps 1-3.</p>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/registry/' | relative_url }}">
        <h3>{{ registry_objects | size }} registry objects</h3>
        <p>The current public spine across all seven books.</p>
      </a>
    </article>
  </li>
  {% for group in type_groups %}
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/types/' | relative_url }}#{{ group.name | slugify }}">
        <h3>{{ group.size }} {{ group.name | capitalize }}</h3>
        <p>Registry objects currently typed as {{ group.name }}.</p>
      </a>
    </article>
  </li>
  {% endfor %}
</ul>

## What the corpus is not

- not a narrative exposition; see [Publications]({{ '/publications/' | relative_url }})
- not a list of answer claims; see [Results]({{ '/results/' | relative_url }})
- not the proof assistant itself; see [Verify]({{ '/verify/' | relative_url }}) and TauLib
- not static

## Structure

<div class="v2-system-strip" aria-label="Corpus structure">
  <a href="{{ '/corpus/construction-spine/' | relative_url }}">Construction steps</a>
  <span>-></span>
  <a href="{{ '/corpus/registry/' | relative_url }}">Atomic items</a>
  <span>-></span>
  <a href="{{ '/corpus/graph/' | relative_url }}">Dependencies</a>
  <span>-></span>
  <a href="{{ '/results/' | relative_url }}">Result projections</a>
  <span>-></span>
  <a href="{{ '/verify/' | relative_url }}">Verification</a>
  <span>-></span>
  <a href="{{ '/publications/' | relative_url }}">Release artifacts</a>
</div>

The Corpus lane is the place to ask: what has actually been built, how does one item depend on another, and where does a public result touch the underlying research body?
