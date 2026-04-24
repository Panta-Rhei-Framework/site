---
layout: program-doc
title: "Verify"
lane: verify
permalink: /verify/
summary_short: "How to inspect, verify, and challenge the claims of the Panta Rhei Research Program — what can be checked, and what verification does not settle."
hero_ctas:
  - label: "Scientific Rigor"
    url: /verify/scientific-rigor/
    primary: true
  - label: "Formal Verification Stack"
    url: /verify/formal-verification-stack/
  - label: "How to Verify"
    url: /verify/how-to-verify/
hero_supporting_line: "445 Lean 4 modules · 127,440 lines · 4,332 machine-checked theorems · 0 sorry across all 7 books (TauLib Lean corpus; scope tiered — see [filter rules](/verify/filter-rules/)) · 3 conjectural axioms · Mathlib for tactics only."
summary_cards:
  - title: "What can be checked"
    body: "Every theorem in TauLib compiles in Lean 4. Every quantitative prediction has an explicit formula. Every scope claim carries its epistemic label."
  - title: "What verification does not settle"
    body: "Compilation proves internal consistency, not truth about the physical world. Bridge claims remain conjectural until independently validated."
  - title: "How to start"
    body: "Clone TauLib, run lake build, and step through the guided tours. Or read the falsification pack for the decisive empirical tests."
right_rail:
  related:
    - title: "Verification Framework"
      url: /verify/verification-framework/
    - title: "Domain Verification"
      url: /verify/domain-verification/
    - title: "Results"
      url: /results/
    - title: "Corpus Registry"
      url: /corpus/registry/
  artifacts:
    - title: "TauLib Docs"
      url: "https://taulib.site/"
      external: true
    - title: "TauLib Source (Apache-2.0)"
      url: "https://github.com/Panta-Rhei-Research/taulib"
      external: true
    - title: "License (Apache-2.0)"
      url: "https://github.com/Panta-Rhei-Research/taulib/blob/main/LICENSE"
      external: true
    - title: "TauLib (frozen)"
      url: "https://github.com/Panta-Rhei-Research/formalization"
      external: true
  meta:
    type: "Lane Root"
    scope: "All verification"
    status: "Canonical"
    updated: "April 2026"
---

## What Verify Means Here

Verification in this program is not one thing. It includes research-form legitimacy, formal proof checking, bridge adequacy, domain-specific validation, prediction and falsification surfaces, and structured external assessment.

<div class="v2-system-strip" aria-label="Verify lane model">
  <a href="{{ '/verify/scientific-rigor/' | relative_url }}">Scientific Rigor</a>
  <span>-></span>
  <a href="{{ '/verify/verification-framework/' | relative_url }}">Verification Framework</a>
  <span>-></span>
  <a href="{{ '/verify/formal-verification-stack/' | relative_url }}">Formal Stack</a>
  <span>-></span>
  <a href="{{ '/verify/domain-verification/' | relative_url }}">Domain Verification</a>
  <span>-></span>
  <a href="{{ '/verify/how-to-verify/' | relative_url }}">Operational Routes</a>
</div>

## Core Routes

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/verify/scientific-rigor/' | relative_url }}">
    <strong>Scientific Rigor</strong>
    <span>Whether the program operates as a serious, inspectable research artifact.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/verification-framework/' | relative_url }}">
    <strong>Verification Framework</strong>
    <span>The shared standards: explicitness, traceability, derivability, and domain-appropriate validation.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/formal-verification-stack/' | relative_url }}">
    <strong>Formal Verification Stack</strong>
    <span>Kernel integrity, standard-foundation checks, bridge verification, and current boundaries.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/domain-verification/' | relative_url }}">
    <strong>Domain Verification</strong>
    <span>How verification differs across mathematics, physics, life, and metaphysics.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/predictions-and-falsification/' | relative_url }}">
    <strong>Predictions & Falsification</strong>
    <span>Where results become accountable to computation, measurement, contradiction, or failure.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/assessment-protocols/' | relative_url }}">
    <strong>Assessment Protocols</strong>
    <span>Manual and LLM-assisted review pathways for structured external scrutiny.</span>
  </a>
</div>

## Operational Surfaces

- [TauLib]({{ '/verify/taulib/' | relative_url }}) is the Lean 4 formalization surface.
- [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}) pins the current public release state.
- [Filter Rules]({{ '/verify/filter-rules/' | relative_url }}) explain which count means what across site surfaces.
- [Custom Axiom Inventory]({{ '/verify/custom-axioms/' | relative_url }}) and [TCB Disclosure]({{ '/verify/tcb/' | relative_url }}) name the trust budget.
- [How to Verify]({{ '/verify/how-to-verify/' | relative_url }}) gives practical entry points for different reviewers.

## The Right First Question

The right first question is not "should I already believe this?" The right first question is: **is this a serious research program that has earned structured engagement?**

Start by checking the research form, then choose a result, trace its Corpus support, inspect the available formalization, and test its domain-specific accountability route.

## Report Corrections

Found an error, a broken proof, a mis-stated numerical value, or a scope-label issue? We take corrections seriously and credit corrigendum contributors in the changelog.

**Email**: [errata@panta-rhei.site](mailto:errata@panta-rhei.site)

For formal peer-review coordination or institutional review inquiries: [review@panta-rhei.site](mailto:review@panta-rhei.site)
