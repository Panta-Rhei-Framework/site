---
layout: program-doc
title: "Assessment Protocols"
permalink: /verify/assessment-protocols/
lane: verify
v2_lane: verify
type: "Verification Surface"
verify_type: assessment_protocol
status: "Canonical"
summary_short: "Structured pathways for holding the program accountable to its stated standards."
og_image: /assets/images/plates/plate-06-verification-matrix-og.jpg
twitter_image: /assets/images/plates/plate-06-verification-matrix-og.jpg
og_image_alt: "Scientific plate showing the Verify lane as a verification matrix with obligations, construction steps, results, formal proof checking, bridge adequacy, predictions, falsification, and external assessment."
summary_cards:
  - title: "Manual protocols"
    body: "Human-readable review procedures for inspecting the program."
  - title: "LLM-assisted protocols"
    body: "Structured prompts for generating first-pass audit dossiers from public materials."
  - title: "Protocol boundary"
    body: "Assessment protocols are triage and review tools, not substitutes for proof or peer review."
right_rail:
  related:
    - title: "Manual Protocols"
      url: /verify/assessment-protocols/manual/
    - title: "LLM-Assisted Protocols"
      url: /verify/assessment-protocols/llm-assisted/
    - title: "Existing Assessment Library"
      url: /verify/assessments/
    - title: "How to Verify"
      url: /verify/how-to-verify/
  meta:
    type: "Assessment Protocol"
    status: "Canonical"
    updated: "April 2026"
---

## What These Protocols Do

These protocols are designed for reviewers, readers, and external evaluators. They provide explicit checklists and prompts for structured scrutiny.

## Assessment inside the verification matrix

{% capture assessment_plate_caption %}Assessment Protocols are external-review routes inside the broader verification matrix. They help structure scrutiny, but they do not replace proof, empirical testing, or peer review.{% endcapture %}
{% include scientific-plate.html id="plate-06-verification-matrix" variant="thumb" class="scientific-plate--compact" caption=assessment_plate_caption loading="lazy" %}

Assessment begins after the relevant obligation, construction step, result, and verification mode have been identified.

Protocols help reviewers decide where to inspect next: Agenda obligations, Corpus construction, Results status, TauLib formalization, bridge assumptions, or falsification surfaces.

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/verify/assessment-protocols/manual/' | relative_url }}">
    <strong>Manual Protocols</strong>
    <span>Human review procedures for legitimacy, derivation tracing, bridge adequacy, prediction review, and Corpus/Result alignment.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/assessment-protocols/llm-assisted/' | relative_url }}">
    <strong>LLM-Assisted Protocols</strong>
    <span>Prompted first-pass assessment workflows that use only public materials and produce typed dossiers.</span>
  </a>
</div>

## Existing Detailed Library

The earlier detailed assessment library remains available at [AI-Assisted First-Pass Assessment]({{ '/verify/assessments/' | relative_url }}), including methodology, rubric, scorecard, dossier schema, reviewer workflow, and prompt templates.
