---
layout: program-doc
title: "Scientific Rigor"
lane: verify
v2_lane: verify
type: "Verification Surface"
status: "Canonical"
permalink: /verify/scientific-rigor/
summary_short: "The standards by which the program holds itself accountable as a serious, inspectable research program."
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
    - title: "Verification Framework"
      url: /verify/verification-framework/
    - title: "Assessment Protocols"
      url: /verify/assessment-protocols/
  meta:
    type: "Verification Surface"
    status: "Canonical"
    updated: "April 2026"
---

## Core Question

Before asking whether a specific result is true, a reviewer can ask whether the program operates in a way that qualifies as serious, inspectable research. This page verifies the research form, not the truth of the framework.

## Rigor Criteria

- **Explicit scope:** the site distinguishes formal, empirical, bridge, and interpretive burdens.
- **Explicit burden of proof:** each result should make clear what would have to be checked.
- **Public inspectability:** release surfaces, registry pages, TauLib, and assessment routes are exposed.
- **Structured artifacts:** books, corpus objects, generated docs, manifests, and pages are versioned.
- **Stable release surfaces:** snapshots and manifests make drift visible.
- **Openness to scrutiny:** the site names how to challenge the work rather than asking for deference.
- **Explicit refusals and constraints:** the Program lane names what the research program refuses to do.
- **Failure modes:** predictions, falsification paths, contradicted statuses, and open bridge issues stay visible.

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
  <a class="v2-tile" href="{{ '/verify/how-to-verify/' | relative_url }}">
    <h3>Independent audit</h3>
    <p>Reviewers can enter through domain-specific audit routes and assessment protocols instead of relying on summaries.</p>
  </a>
</div>

## Reader Stance

The intended reader stance is neither deference nor dismissal. It is inspection. Follow the chain from publication prose to corpus object, from corpus object to formalization where available, and from formalization to the remaining bridge assumptions.
