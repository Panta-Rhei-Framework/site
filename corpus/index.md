---
layout: program-doc
title: "Corpus"
lane: corpus
v2_lane: corpus
permalink: /corpus/
type: "Lane Root"
status: "Canonical"
summary_short: "The living, versioned research corpus of the program."
summary_cards:
  - title: "Research body"
    body: "Definitions, lemmas, theorems, structures, and dependency relations."
  - title: "Registry spine"
    body: "The current public registry exposes 4,547 objects across seven books."
  - title: "Public projections"
    body: "Results, publications, verification, and TauLib are projections of the corpus."
hero_ctas:
  - label: "Browse the Registry"
    url: /corpus/registry/
    primary: true
  - label: "How to Read"
    url: /corpus/how-to-read/
  - label: "Corpus Graph"
    url: /corpus/graph/
right_rail:
  related:
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

The corpus is the central research artifact of the program.

It is not a summary, not a set of claims, and not a collection of papers. It is the structured body of what has been built: definitions, lemmas, theorems, structures, derivations, and dependency relations.

## Current state

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/corpus/registry/' | relative_url }}">
    <strong>{{ registry_objects | size }} registry objects</strong>
    <span>The current public spine across all seven books.</span>
  </a>
  {% for group in type_groups %}
  <a class="v2-tile" href="{{ '/corpus/types/' | relative_url }}#{{ group.name | slugify }}">
    <strong>{{ group.size }} {{ group.name | capitalize }}</strong>
    <span>Registry objects currently typed as {{ group.name }}.</span>
  </a>
  {% endfor %}
</div>

## What the corpus is not

- not a narrative exposition; see [Publications]({{ '/publications/' | relative_url }})
- not a list of answer claims; see [Results]({{ '/results/' | relative_url }})
- not the proof assistant itself; see [Verify]({{ '/verify/' | relative_url }}) and TauLib
- not static

## Corpus projections

The corpus is expressed in multiple public forms:

- [Registry]({{ '/corpus/registry/' | relative_url }}) — human-readable formal spine
- [Publications]({{ '/publications/' | relative_url }}) — narrative crystallizations
- [Results]({{ '/results/' | relative_url }}) — answer surfaces
- [Verify]({{ '/verify/' | relative_url }}) — formal and empirical inspection paths

## Structure

<div class="v2-system-strip" aria-label="Corpus structure">
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
