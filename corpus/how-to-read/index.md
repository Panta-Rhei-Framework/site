---
layout: program-doc
title: "How to Read the Corpus"
lane: corpus
v2_lane: corpus
permalink: /corpus/how-to-read/
type: "Corpus Guide"
status: "Canonical"
summary_short: "A reader's guide to corpus objects, dependencies, status labels, and public projections."
right_rail:
  related:
    - title: "Registry"
      url: /corpus/registry/
    - title: "Types"
      url: /corpus/types/
    - title: "Versioning"
      url: /corpus/versioning/
  meta:
    type: "Corpus Guide"
    status: "Canonical"
    updated: "April 2026"
---

## Reading order

The corpus is not meant to be read like a book. It is meant to be inspected as a graph.

Start with an object ID, follow its dependencies, then check where it appears in Results, Publications, or Verify. When possible, compare the human-readable statement with the corresponding TauLib formalization.

## Practical route

1. Find a registry object or result that interests you.
2. Check its type and status.
3. Follow its dependencies backward.
4. Follow its uses forward.
5. Inspect related publications and verification surfaces.

## Three entry routes

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/results/' | relative_url }}">
    <strong>Start from a result</strong>
    <span>Use a public result page, then follow its registry anchors backward into the corpus.</span>
  </a>
  <a class="v2-tile" href="{{ '/corpus/registry/' | relative_url }}">
    <strong>Start from an object</strong>
    <span>Browse by book, type, dependency count, or formalization status.</span>
  </a>
  <a class="v2-tile" href="{{ '/publications/books/' | relative_url }}">
    <strong>Start from a book</strong>
    <span>Read the narrative release, then use registry links to locate the formal spine.</span>
  </a>
</div>

## Reading an item page

On a registry item page, read the page in this order:

1. **ID and type**: what kind of object is this?
2. **Summary**: what does it claim or introduce?
3. **Book location**: where does it sit in the canonical release?
4. **Dependencies**: what must already be accepted?
5. **Depended on by**: where does it later carry weight?
6. **Lean formalization**: is there a corresponding formal artifact?
