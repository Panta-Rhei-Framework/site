---
layout: "recovery-requirement-item"
title: "Physical Quantity Types"
permalink: "/agenda/recovery-requirements/physics/physical-quantity-types/"
lane: "program"
v2_lane: "program"
section: "research-agenda"
type: "Recovery Requirement"
status: "canonical"
summary_short: "Physics recovery ledger entry: Physical Quantity Types."
generated_from: "corpus/recovery-requirements"
projection_version: "v0.1"
canonical_source: "corpus/recovery-requirements"
do_not_edit: true
canonical_recovery_id: "PREC-P0"
id: "PREC-P0"
short_title: "Physical Quantity Types"
slug: "physical-quantity-types"
domain: "physics"
domain_slug: "physics"
display_domain: "Physics"
item_type: "recovery_requirement"
visibility: "public"
program_role: "physical_measurement_recovery_target"
priority: "high"
recovery_status: "partial"
verification_status: "pending_physics_verification"
related:
  problem_ledger_items: []
  corpus_items: []
  results: []
  verify:
    - "verify-predictions-and-falsification"
  publications: []
refusal_type: ""
not_refused: []
related_recovery_targets: []
version:
  item_version: "0.1.0"
  introduced_in: "recovery-ledger-v1"
  last_modified: "2026-04-25"
  change_summary: "Initial Recovery Requirements v0.1 item."
tags:
  - "physics"
  - "recovery-requirements"
  - "prec-p0"
url: "/agenda/recovery-requirements/physics/physical-quantity-types/"
verification:
  status: "pending_physics_verification"
  mode: "quantity_type_recovery"
  related_results:
    - "/results/world-readout/physics/"
  related_corpus_steps:
    - "/corpus/construction-spine/identify-physical-carrier/"
    - "/corpus/construction-spine/recover-internal-physical-grammar/"
  related_verify_pages:
    - "/verify/domain-verification/physics/"
    - "/verify/construction-spine-verification/"
expanded_rationale: "A physics-facing kernel must explain why physical quantities have stable roles before it can claim to recover laws, constants, or measurements. This item therefore tests whether the framework carries a typed measurement grammar rather than an untyped numerical fit."
public_summary: "Physical recovery begins with typed quantities: time, length, energy, charge, temperature, count, and luminosity cannot be treated as interchangeable labels."
what_this_requires:
  - "Stable semantic roles for time, length, mass/energy, charge/current, temperature, amount/count, and luminosity where required."
  - "A bridge from internal invariants to public measurement units without treating units as primitive ontology."
  - "Enough type discipline to prevent category mistakes between formal parameters, empirical observables, and calibration conventions."
what_this_does_not_claim:
  - "It does not claim that every conventional unit is ontically primitive."
  - "It does not claim that public measurement practice is already fully derived."
  - "It does not replace empirical calibration with formal notation."
related_examples:
  - "Time, length, and mass/energy roles in physics recovery."
  - "SI calibration as a bridge rather than a primitive substrate."
  - "Dimension and quantity checks for later Results claims."
---

# Physical Quantity Types

## Requirement

The kernel must recover meaningful physical quantity types rather than treating physics as dimensionless bookkeeping.

## What This Target Requires

- Stable semantic roles for time, length, mass/energy, charge/current, temperature, amount/count, and luminosity where required.

## Current Status

This v0.1 item fixes the public burden of proof. Detailed formal, empirical, or bridge verification remains routed through the Verify and Results lanes.
