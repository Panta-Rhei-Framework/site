---
layout: program-doc
title: "Falsification Packs"
permalink: /verify/predictions-and-falsification/falsification-packs/
lane: verify
v2_lane: verify
type: "Verification Surface"
verify_type: falsification_pack
status: "Canonical"
summary_short: "Structured bundles for checking numeric, structural, or empirical accountability surfaces."
right_rail:
  related:
    - title: "Falsification Pack"
      url: /results/falsifications/browse/
    - title: "Assessment Protocols"
      url: /verify/assessment-protocols/
    - title: "Manual Protocols"
      url: /verify/assessment-protocols/manual/
  meta:
    type: "Falsification Pack Surface"
    status: "Canonical"
    updated: "May 2026"
---

## Pack Structure

Each falsification pack should include:

- target claim or result
- context
- inputs and reference links
- expected structure
- evaluation criteria
- failure condition
- pack status (draft / current / canonical / pending)
- related Results, Corpus, and Verify links

## Pack Status Vocabulary

- **draft** — the pack is being assembled; structure may change.
- **current** — the pack is the active production surface for its target.
- **canonical** — the pack has been frozen as the reference structure for its claim family.
- **pending** — the pack target is identified but the bundle is not yet assembled.

## Current State

The first production surface is the [{% include release-metric.html id="falsifications.records" %}-item physics falsification pack]({{ '/results/falsifications/browse/' | relative_url }}) (status: **current**). This Verify page defines the pack grammar so future numeric, structural, and domain-specific packs can be added consistently.

Packs may be executed manually, computationally, or through LLM-assisted review where appropriate. Packs are operational bundles for inspection, not claims of completed falsification.

## Related Verify Surfaces

- [Assessment Protocols]({{ '/verify/assessment-protocols/' | relative_url }}) — manual and LLM-assisted review routes.
- [Measurement Bridges]({{ '/corpus/construction-spine/measurement-empirical-bridges/' | relative_url }}) — the construction step where empirical accountability begins.
- [LLM-Assisted Protocols]({{ '/verify/assessment-protocols/llm-assisted/' | relative_url }}) — for assisted pack review.
