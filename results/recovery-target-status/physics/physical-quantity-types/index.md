---
layout: "program-doc"
title: "Physical Quantity Types"
permalink: "/results/recovery-target-status/physics/physical-quantity-types/"
lane: "results"
v2_lane: "results"
type: "Recovery Target Status"
status: "Canonical"
summary_short: "Current Results-side recovery status for Physical Quantity Types."
canonical_recovery_id: "PREC-P0"
---

<div class="notice note"><strong>Status note.</strong> This page reports current recovery status. It does not imply external acceptance unless explicitly stated.</div>

## Status Separation

- Internal status: **Partial**
- Verification state: **Pending physics verification**
- External status: **Not externally reviewed**

## Requirement

Physical recovery begins with typed quantities: time, length, energy, charge, temperature, count, and luminosity cannot be treated as interchangeable labels.

## Current Recovery Status

- Recovery status: **Partial**
- Verification status: **Pending physics verification**
- Program ledger item: [PREC-P0](/agenda/recovery-requirements/physics/physical-quantity-types/)
- Verification mode: `quantity_type_recovery`

## Result Summary

A physics-facing kernel must explain why physical quantities have stable roles before it can claim to recover laws, constants, or measurements. This item therefore tests whether the framework carries a typed measurement grammar rather than an untyped numerical fit.

## Related Result Items

- [World Readout: Physics](/results/world-readout/physics/)

## Related Corpus Construction Steps

- [Identify Physical Carrier](/corpus/construction-spine/identify-physical-carrier/)
- [Recover Internal Physical Grammar](/corpus/construction-spine/recover-internal-physical-grammar/)

## Related Verify Surfaces

- [Domain Verification: Physics](/verify/domain-verification/physics/)
- [Construction Spine Verification](/verify/construction-spine-verification/)

## What This Status Does Not Yet Establish

- It does not claim that every conventional unit is ontically primitive.
- It does not claim that public measurement practice is already fully derived.
- It does not replace empirical calibration with formal notation.

## Projection Metadata

- Generated from: `corpus/recovery-requirements`
- Projection version: `v0.1`
- Do not edit generated projection: `True`
