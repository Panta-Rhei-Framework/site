---
layout: program-doc
title: "Scientific Rigor"
lane: verify
v2_lane: verify
type: "Verification Surface"
status: "Canonical"
permalink: /verify/scientific-rigor/
summary_short: "A concise map of how the program separates formal proof, empirical prediction, scope labels, and public scrutiny."
summary_cards:
  - title: "Typed claims"
    body: "Mathematical, physical, life, and metaphysical claims are not granted the same epistemic status."
  - title: "Public burden"
    body: "Claims remain inspectable through the corpus, release manifest, formalization surfaces, and falsification routes."
  - title: "No shortcut"
    body: "Formal verification supports internal coherence; empirical and interpretive claims still require external scrutiny."
right_rail:
  related:
    - title: "Verify"
      url: /verify/
    - title: "Release Manifest"
      url: /verify/release-manifest/
    - title: "How to Audit"
      url: /verify/how-to-audit/
  meta:
    type: "Verification Surface"
    status: "Canonical"
    updated: "April 2026"
---

## What Rigor Means Here

The program treats rigor as a layered obligation. A proof assistant can check a formal derivation, but it cannot by itself establish that a bridge to physics, life, or metaphysics is true. The public website therefore separates several kinds of scrutiny instead of blending them into a single confidence signal.

## The Four Checks

<div class="v2-grid v2-grid-2">
  <a class="v2-tile" href="{{ '/corpus/registry/' | relative_url }}">
    <h3>Corpus traceability</h3>
    <p>Definitions, theorems, lemmas, and result claims are tied back to registry objects and dependency chains.</p>
  </a>
  <a class="v2-tile" href="{{ '/verify/taulib/' | relative_url }}">
    <h3>Formal verification</h3>
    <p>TauLib exposes the Lean 4 formalization surface, including build status, axiom inventory, and documentation.</p>
  </a>
  <a class="v2-tile" href="{{ '/results/problem-ledger/' | relative_url }}">
    <h3>Result status</h3>
    <p>Results are typed by their current strength: resolved, partial, qualitative, contradicted, open, or deferred.</p>
  </a>
  <a class="v2-tile" href="{{ '/verify/how-to-audit/' | relative_url }}">
    <h3>Independent audit</h3>
    <p>Reviewers can enter through domain-specific audit routes and assessment protocols instead of relying on summaries.</p>
  </a>
</div>

## Reader Stance

The intended reader stance is neither deference nor dismissal. It is inspection. Follow the chain from publication prose to corpus object, from corpus object to formalization where available, and from formalization to the remaining bridge assumptions.
