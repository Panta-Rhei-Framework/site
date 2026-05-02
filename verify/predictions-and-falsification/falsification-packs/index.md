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
    updated: "April 2026"
---

## Pack Structure

Each falsification pack should include:

- target claim or result
- context
- inputs and reference links
- expected structure
- evaluation criteria
- failure condition
- related Results, Corpus, and Verify links

## Current State

The first production surface is the [{% include release-metric.html id="falsifications.records" %}-item physics falsification pack]({{ '/results/falsifications/browse/' | relative_url }}). This Verify page defines the pack grammar so future numeric, structural, and domain-specific packs can be added consistently.

Packs may be executed manually, computationally, or through LLM-assisted review where appropriate.
