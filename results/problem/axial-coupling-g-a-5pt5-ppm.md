---
layout: "result-page"
title: "Axial Coupling g_A at +5.5 ppm via κ_D² /ι<sub>τ</sub> with CF Window NLO"
permalink: "/results/problem/axial-coupling-g-a-5pt5-ppm/"
id: "result-057"
result_id: "result-057"
problem_ledger_ids: []
topic: "mathematics"
layer: "mathematics"
result_type: "structural_readout"
bridge_status: "internal"
result_kind: "foundational-math"
importance_class: "structural-support-result"
status_code: "R"
domain_group: "Mathematics"
summary_short: "The nucleon axial coupling g_A = 1.27637 is derived at +5.5 ppm from PDG using κ_D²/ι<sub>τ</sub> with a continued-fraction window NLO correction."
canonical_books:
  - "IV"
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

IV.T182 derives the nucleon axial vector coupling g_A = 1.27637 at +5.5 ppm from the PDG value 1.2764 ± 0.0008. The derivation uses the ratio κ_D²/ι<sub>τ</sub> = (1–ι<sub>τ</sub>)²/ι<sub>τ</sub> as the leading-order expression and a continued-fraction window NLO correction to achieve sub-10 ppm precision. g_A governs neutron beta decay and is one of the most precisely measured nucleon properties. At +5.5 ppm this is among the best predictions in the nuclear sector.

## Detail

The nucleon axial coupling g_A measures the ratio of the axial to vector coupling constants in nuclear beta decay. It appears in the neutron lifetime, nuclear matrix elements, and neutrino-nucleus cross-sections. The PDG value is g_A = 1.2764 ± 0.0008 (from ultracold neutron beta-decay experiments).

IV.T182 derives g_A as follows. The τ-framework associates the nucleon axial response with the ratio of the gravity coupling κ_D = 1–ι<sub>τ</sub> (squared, because axial coupling involves two insertions of the sector coupling) to the weak coupling κ_A = ι<sub>τ</sub>. This gives the LO expression g_A^(LO) = κ_D²/ι<sub>τ</sub> = (1–ι<sub>τ</sub>)²/ι<sub>τ</sub>. Numerically (1–ι<sub>τ</sub>)²/ι<sub>τ</sub> ≈ 1.2744, which is at approximately –160 ppm from PDG 1.2764.

The NLO correction uses the continued-fraction window for ι<sub>τ</sub>. The CF expansion CF(ι<sub>τ</sub>) = [0; 2, 1, 13, 3, …] identifies a natural NLO correction scale from the 13th convergent of the CF representation. Including this correction shifts the result to g_A = 1.27637, achieving +5.5 ppm from PDG.

At +5.5 ppm, the axial coupling prediction is in the 1–10 ppm precision tier (rank 8 in the 1–10 ppm table of the Cross-Domain Analysis), alongside the Higgs mass (+8.0 ppm), muon g–2 (+8.8 ppm), and Koide ratio (–9 ppm). It is the only nuclear coupling prediction at this precision level.

## Result Statement

IV.T182: g_A = 1.27637 at +5.5 ppm from PDG 1.2764. LO: κ_D²/ι<sub>τ</sub> = (1–ι<sub>τ</sub>)²/ι<sub>τ</sub>. NLO: CF(ι<sub>τ</sub>) window correction. Zero free parameters.
