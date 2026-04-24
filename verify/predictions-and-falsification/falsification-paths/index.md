---
layout: program-doc
title: "Falsification Paths"
permalink: /verify/predictions-and-falsification/falsification-paths/
lane: verify
v2_lane: verify
type: "Verification Surface"
verify_type: falsification_path
status: "Canonical"
summary_short: "Explicitly stated routes by which current claims could be challenged or broken."
right_rail:
  related:
    - title: "Falsification Pack"
      url: /results/falsifications/browse/
    - title: "Predictions"
      url: /verify/predictions-and-falsification/predictions/
    - title: "Physics Verification"
      url: /verify/domain-verification/physics/
  meta:
    type: "Falsification Surface"
    status: "Canonical"
    updated: "April 2026"
---

## What Counts as a Falsification Path

A falsification path names where and how the system could fail. It should say what evidence, contradiction, failed bridge, or failed derivation would count against the current claim.

## Required Metadata for a Path

- falsification ID
- target result or result family
- target domain
- possible failure
- what evidence or contradiction would count
- related Corpus or bridge surface
- related prediction if relevant

## Current Public Surfaces

- [Falsification Pack]({{ '/results/falsifications/browse/' | relative_url }})
- [Prediction Timing Ledger]({{ '/results/predictions/timing/' | relative_url }})
- [Physics World Readout]({{ '/results/world-readout/physics/' | relative_url }})
- [Status and Claim Typing]({{ '/results/status-and-claim-typing/' | relative_url }})
