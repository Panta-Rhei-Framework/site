---
layout: "result-page"
title: "Helium-4 Primordial Abundance Y_p = 20/81 at 0.43σ from Planck"
permalink: "/results/problem/helium-4-abundance-y-p-20-over-81/"
id: "result-064"
result_id: "result-064"
problem_ledger_ids: []
topic: "mathematics"
layer: "mathematics"
result_type: "structural_readout"
bridge_status: "internal"
result_kind: "foundational-math"
importance_class: "structural-support-result"
status_code: "R"
domain_group: "Mathematics"
summary_short: "The primordial helium-4 mass fraction Y_p = 20/81 ≈ 0.24691 is derived at 0.43σ from the Planck+BBN value 0.2449 ± 0.0040."
canonical_books:
  - "V"
right_rail:
  meta:
    type: "Structural Readout"
    layer: "Mathematics"
    topic: "Mathematics"
    status: "Internal"
    updated: "April 2026"
visibility: "public"
provenance_source: "manuscript"
lean_formalization_status: "none"
cascade_layer: "kernel"
foundational_hinge_ids: []
glossary_term_ids: []
recovery_requirement_ids: []
generated_from: "corpus/results"
projection_version: "v0.2"
canonical_source: "corpus/results"
do_not_edit: true
---

## Overview

V.P112 predicts the primordial helium-4 mass fraction Y_p = 20/81 ≈ 0.24691 at 0.43σ from the Planck 2018 value 0.2449 ± 0.0040. The rational fraction 20/81 factors as (8/27) · (5/6), where 8/27 = 2³/3³ is the He-4 packing maximum in the stride-3 BBN voxel macrocell (V.T146) and 5/6 = 1 − (1/2)(1/3) is the domain-wall correction (V.D194). The denominator 81 = 27 · 6/2 = 3⁴ is therefore a consequence of stride-3 lattice packing, not a free integer; no fitting is required.

## Detail

Big Bang Nucleosynthesis (BBN) predicts the primordial abundances of light elements. The helium-4 mass fraction Y_p is the most precisely measured BBN prediction, with the observational value from Planck 2018 combining CMB constraints: Y_p = 0.2449 ± 0.0040.

V.P112 derives Y_p = 20/81 = 0.24691 in the τ-BBN framework. The derivation chain is: ι<sub>τ</sub> → κ_D → η_B (baryon asymmetry, V.T188) → n/p freeze-out ratio → helium synthesis → Y_p. The key structural result is that Y_p = 4n_He / (4n_He + n_H) where the neutron-to-proton ratio at nucleosynthesis is determined by the τ-weak coupling and ι<sub>τ</sub>. The exact fraction 20/81 arises because the He-4 packing maximum in the stride-3 BBN voxel macrocell is 8/27 = 2³/3³ (V.T146, Lean-certified at `packing_is_8_27`), and the domain-wall correction multiplies by 5/6 = 1 − (1/2)(1/3) (V.D194), giving (8/27)(5/6) = 20/81 (V.T149). The denominator 81 = 27 · 6/2 = 3⁴ inherits its structure from the stride-3 voxel geometry, not from a free parameter.

The 0.43σ agreement is notable because it is the second-best agreement with Planck in terms of σ-units (after the structural predictions like Ω_k = 0 which are exact), and it is achieved with a pure rational number — no irrational constants enter the final answer. The entry V.P112 is the only BBN prediction in the Crown Jewels (rank 28, score 29) and the first non-obvious rational BBN prediction in the framework.

## Result Statement

V.P112: Y_p = 20/81 = 0.24691 at 0.43σ from Planck 0.2449 ± 0.0040. Derived from τ-BBN chain: ι<sub>τ</sub> → η_B → n/p freeze-out → helium synthesis. Exact rational fraction.
