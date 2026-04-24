---
layout: program-doc
title: "Registry"
lane: corpus
v2_lane: corpus
permalink: /corpus/registry/
type: "Registry Index"
status: "Canonical"
summary_short: "The canonical public index of corpus items: definitions, lemmas, theorems, structures, and dependencies."
summary_cards:
  - title: "4,547 objects"
    body: "The current registry spans the seven-book corpus and exposes IDs, types, locations, dependencies, and status."
  - title: "Book-indexed"
    body: "Browse by book and dashboard while the v2 item templates are normalized."
  - title: "Corpus-owned"
    body: "Registry pages are now owned by Corpus; Results, Verify, and Publications link back to them."
right_rail:
  related:
    - title: "Corpus"
      url: /corpus/
    - title: "Types"
      url: /corpus/types/
    - title: "Registry Dashboards"
      url: /registry/dashboards/book-i/
    - title: "How to Read"
      url: /corpus/how-to-read/
  meta:
    type: "Registry Index"
    status: "Canonical"
    updated: "April 2026"
---

{% assign registry_objects = site.data.registry.objects %}
{% assign type_groups = registry_objects | group_by: "type" | sort: "name" %}

## Overview

The registry is the canonical public index of the corpus. Each object has an ID, a type, a book location, a scope label, dependency counts, and, when available, a Lean formalization pointer.

## Type filters

<div class="chip-row">
  {% for group in type_groups %}
  <a class="chip chip-link" href="{{ '/corpus/types/' | relative_url }}#{{ group.name | slugify }}">{{ group.name | capitalize }} · {{ group.size }}</a>
  {% endfor %}
</div>

## Browse by book

- [Book I]({{ '/registry/books/book-i/' | relative_url }}) — Categorical Foundations
- [Book II]({{ '/registry/books/book-ii/' | relative_url }}) — Categorical Holomorphy
- [Book III]({{ '/registry/books/book-iii/' | relative_url }}) — Categorical Spectrum
- [Book IV]({{ '/registry/books/book-iv/' | relative_url }}) — Categorical Microcosm
- [Book V]({{ '/registry/books/book-v/' | relative_url }}) — Categorical Macrocosm
- [Book VI]({{ '/registry/books/book-vi/' | relative_url }}) — Categorical Life
- [Book VII]({{ '/registry/books/book-vii/' | relative_url }}) — Categorical Metaphysics

## Registry sample

The full book indexes remain the best way to browse the complete list. This sample shows the object grammar used across the registry:

<div class="dep-list">
  {% for obj in registry_objects limit: 24 %}
  <a href="{{ obj.url | relative_url }}" class="dep-link">
    <span class="dep-id">{{ obj.id }}</span>
    <span class="dep-title">{{ obj.name }}</span>
    <span class="chip" style="margin-left:auto">{{ obj.type }}</span>
  </a>
  {% endfor %}
</div>

## What each item page shows

Every registry item page should expose identity, location, dependencies, formalization status, summary, and related projections.

The existing object pages remain available at their registry URLs while the v2 registry item normalization proceeds. In v2 navigation and search, those pages are treated as Corpus-owned surfaces.
