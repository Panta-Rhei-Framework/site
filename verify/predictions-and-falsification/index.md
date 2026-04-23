---
layout: program-doc
title: "Predictions & Falsification"
permalink: /verify/predictions-and-falsification/
lane: verify
v2_lane: verify
type: "Verification Surface"
verify_type: falsification_path
status: "Canonical"
summary_short: "How the program exposes possible failure modes and testable consequences."
summary_cards:
  - title: "Predictions"
    body: "Derived consequences that can serve as accountability surfaces for the program."
  - title: "Falsification paths"
    body: "Explicit routes by which a result, bridge, or domain claim could fail."
  - title: "Falsification packs"
    body: "Structured bundles for checking numeric, structural, or empirical accountability surfaces."
right_rail:
  related:
    - title: "Physics Verification"
      url: /verify/domain-verification/physics/
    - title: "Results"
      url: /results/
    - title: "Assessment Protocols"
      url: /verify/assessment-protocols/
  meta:
    type: "Predictions & Falsification"
    status: "Canonical"
    updated: "April 2026"
---

## Accountability, Not Decoration

Predictions and falsification are not merely outputs of the program. They are accountability structures for Results.

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/verify/predictions-and-falsification/predictions/' | relative_url }}">
    <strong>Predictions</strong>
    <span>Derived consequences that can be inspected as verification targets.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/predictions-and-falsification/falsification-paths/' | relative_url }}">
    <strong>Falsification Paths</strong>
    <span>Ways current claims could be challenged, contradicted, or broken.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/predictions-and-falsification/falsification-packs/' | relative_url }}">
    <strong>Falsification Packs</strong>
    <span>Structured audit bundles for manual, computational, or assisted review.</span>
  </a>
</div>

## Cross-Lane Reading

The [Results lane]({{ '/results/' | relative_url }}) presents what the program currently derives. This Verify subtree asks how those results could be checked or defeated. For physics, the first concrete surfaces are the [Predictions browse]({{ '/results/predictions/browse/' | relative_url }}), the [Prediction Timing Ledger]({{ '/results/predictions/timing/' | relative_url }}), and the [Falsification Pack]({{ '/results/falsifications/browse/' | relative_url }}).
