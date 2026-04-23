---
layout: program-doc
title: "How to Verify"
permalink: /verify/how-to-verify/
lane: verify
v2_lane: verify
type: "Verification Surface"
verify_type: how_to_verify
status: "Canonical"
summary_short: "Practical entry points for inspecting the program from different directions."
right_rail:
  related:
    - title: "Scientific Rigor"
      url: /verify/scientific-rigor/
    - title: "Formal Verification Stack"
      url: /verify/formal-verification-stack/
    - title: "Domain Verification"
      url: /verify/domain-verification/
    - title: "Assessment Protocols"
      url: /verify/assessment-protocols/
  meta:
    type: "How to Verify"
    status: "Canonical"
    updated: "April 2026"
---

## Choose Your Entry Route

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/program/about/' | relative_url }}">
    <strong>Start from the Program</strong>
    <span>Check whether the program satisfies standards of serious research practice.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/browse/' | relative_url }}">
    <strong>Start from a Result</strong>
    <span>Choose a result page, follow supporting Corpus items, then inspect Verify links.</span>
  </a>
  <a class="v2-tile" href="{{ '/corpus/registry/' | relative_url }}">
    <strong>Start from the Corpus</strong>
    <span>Choose a registry item, trace dependencies, and inspect formalization status.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/taulib/' | relative_url }}">
    <strong>Start from TauLib</strong>
    <span>Inspect mechanized proofs and map them back to Corpus items.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/predictions-and-falsification/' | relative_url }}">
    <strong>Start from Predictions</strong>
    <span>Choose a prediction or falsification path and follow the accountability chain.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/assessment-protocols/' | relative_url }}">
    <strong>Start from Protocols</strong>
    <span>Use a ready-made manual or LLM-assisted protocol.</span>
  </a>
</div>

## Practical First Pass

1. Read [Scientific Rigor]({{ '/verify/scientific-rigor/' | relative_url }}) to understand the program's self-binding standards.
2. Use the [Verification Framework]({{ '/verify/verification-framework/' | relative_url }}) to identify the kind of verification your question needs.
3. Pick the domain-specific route under [Domain Verification]({{ '/verify/domain-verification/' | relative_url }}).
4. Inspect the operational surface: [TauLib]({{ '/verify/taulib/' | relative_url }}), [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}), [Predictions & Falsification]({{ '/verify/predictions-and-falsification/' | relative_url }}), or [Assessment Protocols]({{ '/verify/assessment-protocols/' | relative_url }}).
