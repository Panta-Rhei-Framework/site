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
og_image: /assets/images/plates/plate-06-verification-matrix-og.jpg
twitter_image: /assets/images/plates/plate-06-verification-matrix-og.jpg
og_image_alt: "Scientific plate showing the Verify lane as a verification matrix with obligations, construction steps, results, formal proof checking, bridge adequacy, predictions, falsification, and external assessment."
right_rail:
  related:
    - title: "Construction Roadmap"
      url: /agenda/construction-roadmap/
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
    - title: "AI-Assisted Discovery"
      url: /discover/ai-assisted-discovery/
  meta:
    type: "How to Verify"
    status: "Canonical"
    updated: "April 2026"
---

## How the verification matrix becomes a route

{% capture how_to_verify_plate_caption %}How to Verify turns the verification matrix into reviewer entry routes: start from an obligation, construction step, result, TauLib surface, prediction, falsification path, or assessment protocol.{% endcapture %}
{% include scientific-plate.html id="plate-06-verification-matrix" variant="thumb" class="scientific-plate--compact" caption=how_to_verify_plate_caption loading="lazy" %}

The matrix is not a single checklist. It is a routing layer that helps a reader choose which inspection mode fits the claim under review.

## Review routes

The former standalone reviewer kit has been folded into Verify and Engage.

Use this page to choose an inspection route. Use [Assessment Protocols]({{ '/verify/assessment-protocols/' | relative_url }}) for structured workflows. Use [Engage → Review the Work]({{ '/engage/review-the-work/' | relative_url }}) to offer bounded review, critique, correction, or contribution.

Review is a routed activity, not a standalone kit. Panta Rhei is inspected through bounded routes across Verify and Engage.

## Start with the inspection architecture

Before inspecting any individual claim, start with the inspection architecture.

Panta Rhei is organized so that reviewers can move from:

Program -> Agenda -> Corpus -> Results -> Verify

This means:

- first inspect the identity, status, and doctrine;
- then inspect the obligations;
- then inspect the construction;
- then inspect the current result stance;
- then inspect the verification route.

This route does not replace expert review. It orients bounded inspection.

## Choose Your Entry Route

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/agenda/' | relative_url }}">
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

## First-pass inspection checklist

1. Is the scope and burden of proof explicit?
2. Are the Problem Ledger and source-policy rules visible?
3. Are Core Semantics and answer-shape obligations stated separately from open problems?
4. Is there a Construction Roadmap / Construction Spine?
5. Is there a Corpus with stable IDs and dependency routes?
6. Is there a formalization surface, and are its limits stated?
7. Are Results status-marked?
8. Are bridge claims explicit?
9. Are falsification or failure paths visible?
10. Are errata and correction routes public?
11. Are remaining externalities disclosed?
12. Is there a route to ask questions or report errors?

## Domain entry routes

- **Mathematics** — [Core Semantics]({{ '/agenda/kernel-model-reality/answer-shape-requirements/' | relative_url }}), [Foundational Hinges]({{ '/corpus/foundational-hinges/' | relative_url }}), [TauLib]({{ '/verify/taulib/' | relative_url }}), and [Mathematics results]({{ '/results/topic/mathematics/' | relative_url }}).
- **Physics** — [Kernel, Model & Reality]({{ '/agenda/kernel-model-reality/' | relative_url }}), [Recovery Requirements: Physics]({{ '/agenda/core-semantics/physics/' | relative_url }}), [Predictions & Falsification]({{ '/verify/predictions-and-falsification/' | relative_url }}), and [Physics results]({{ '/results/topic/physics/' | relative_url }}).
- **Life** — [Recovery Requirements: Life]({{ '/agenda/core-semantics/life/' | relative_url }}), [Life World Readout]({{ '/results/world-readout/life/' | relative_url }}), and [Life-facing results]({{ '/results/topic/biology/' | relative_url }}).
- **Metaphysics** — [Kernel, Model & Reality]({{ '/agenda/kernel-model-reality/' | relative_url }}), [Recovery Requirements: Metaphysics]({{ '/agenda/core-semantics/metaphysics/' | relative_url }}), [Metaphysics World Readout]({{ '/results/world-readout/metaphysics/' | relative_url }}), and [Metaphysics / Philosophy-facing results]({{ '/results/topic/philosophy/' | relative_url }}).
- **Formalization** — [TauLib]({{ '/verify/taulib/' | relative_url }}), [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}), and [Formal Verification Stack]({{ '/verify/formal-verification-stack/' | relative_url }}).
