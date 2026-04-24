---
layout: program-doc
title: "Corpus Graph"
lane: corpus
v2_lane: corpus
permalink: /corpus/graph/
type: "Corpus Guide"
status: "Draft"
summary_short: "A conceptual map of how registry objects, dependencies, results, publications, and verification surfaces relate."
summary_cards:
  - title: "Graph, not list"
    body: "The registry is most useful when read as dependencies and projections, not as a flat catalog."
  - title: "Bidirectional"
    body: "Each object can be read backward through prerequisites and forward through uses."
  - title: "Projection-aware"
    body: "Results, publications, and TauLib are public projections of the same corpus spine."
right_rail:
  related:
    - title: "Registry"
      url: /corpus/registry/
    - title: "How to Read"
      url: /corpus/how-to-read/
    - title: "Verify"
      url: /verify/
  meta:
    type: "Corpus Guide"
    status: "Draft"
    updated: "April 2026"
---

## Conceptual graph

<div class="v2-system-strip" aria-label="Corpus graph model">
  <a href="{{ '/corpus/registry/' | relative_url }}">Registry object</a>
  <span>-></span>
  <a href="{{ '/corpus/graph/' | relative_url }}">Dependencies</a>
  <span>-></span>
  <a href="{{ '/results/' | relative_url }}">Results</a>
  <span>-></span>
  <a href="{{ '/publications/' | relative_url }}">Publications</a>
  <span>-></span>
  <a href="{{ '/verify/' | relative_url }}">Verification</a>
</div>

## What the graph should answer

The graph exists to answer practical review questions:

- Which definitions does this theorem depend on?
- Which later results use this object?
- Which public result is anchored by this registry item?
- Which publication states the argument narratively?
- Which Lean module, if any, formalizes the relevant layer?
- Which version or release manifest fixes the current public state?

## Phase-2 implementation

The current page is a conceptual surface. A later implementation can render an interactive dependency explorer from `_data/registry/adjacency.json`, `_data/registry/reverse-adjacency.json`, and `_data/registry/objects.json`.
