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
    - title: "Construction Roadmap"
      url: /program/research-agenda/construction-roadmap/
    - title: "Corpus Construction Spine"
      url: /corpus/construction-spine/
    - title: "Verify the Construction Spine"
      url: /verify/construction-spine-verification/
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
  <a class="v2-tile" href="{{ '/program/research-agenda/' | relative_url }}">
    <strong>Start from the Research Agenda</strong>
    <span>Check the Problem Ledger, Recovery Requirements, Kernel/Model/Reality burden, and Construction Roadmap.</span>
  </a>
  <a class="v2-tile" href="{{ '/corpus/construction-spine/' | relative_url }}">
    <strong>Start from the Construction Spine</strong>
    <span>Choose one of the ten construction steps and inspect Registry items, TauLib modules, book locations, related Results, and Verify surfaces.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/browse/' | relative_url }}">
    <strong>Start from a Result</strong>
    <span>Choose a result page, follow its agenda mapping, Corpus support, recovery target status, and verification route.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/taulib/' | relative_url }}">
    <strong>Start from TauLib</strong>
    <span>Inspect Lean formalization and map declarations back to Corpus items and construction steps.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/predictions-and-falsification/' | relative_url }}">
    <strong>Start from Predictions / Falsification</strong>
    <span>Follow the Numerical Physics Ledger, prediction timing, falsification paths, and falsification packs.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/assessment-protocols/' | relative_url }}">
    <strong>Start from Assessment Protocols</strong>
    <span>Use manual or LLM-assisted review routes.</span>
  </a>
</div>

## Practical First Pass

1. Read [Scientific Rigor]({{ '/verify/scientific-rigor/' | relative_url }}) to understand the program's self-binding standards.
2. Use the [Verification Framework]({{ '/verify/verification-framework/' | relative_url }}) to identify the kind of verification your question needs.
3. If the question is construction-facing, use [Verify the Construction Spine]({{ '/verify/construction-spine-verification/' | relative_url }}) to map the relevant step to its inspection modes.
4. Inspect the operational surface: [TauLib]({{ '/verify/taulib/' | relative_url }}), [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}), [Predictions & Falsification]({{ '/verify/predictions-and-falsification/' | relative_url }}), or [Assessment Protocols]({{ '/verify/assessment-protocols/' | relative_url }}).
