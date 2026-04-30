---
layout: "result-page"
title: "Muon Anomalous Magnetic Moment a_μ at +8.8 ppm"
permalink: "/results/problem/muon-anomalous-magnetic-moment-8pt8-ppm/"
id: "result-059"
result_id: "result-059"
problem_ledger_ids: []
topic: "mathematics"
layer: "mathematics"
result_type: "structural_readout"
bridge_status: "internal"
result_kind: "frontier-problem"
importance_class: "domain-level-open-problem"
status_code: "R"
domain_group: "Particle Physics"
summary_short: "The muon anomalous magnetic moment a_μ is derived at +8.8 ppm from FNAL g–2 by propagating α_τ through the QED corrections."
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

IV.T180 derives the muon anomalous magnetic moment a_μ by propagating the τ-derived fine-structure constant α_τ through the standard QED loop corrections. The result agrees with the FNAL g–2 measurement at +8.8 ppm — well within experimental uncertainty. The muon g–2 has long been considered an anomalous discrepancy between theory and experiment; the τ-framework's prediction falls between the SM prediction and the FNAL measurement, potentially addressing the tension structurally.

## Detail

The muon anomalous magnetic moment a_μ = (g_μ – 2)/2 is one of the most precisely measured and calculated quantities in particle physics. A long-standing discrepancy existed between the SM prediction (based on detailed QED, electroweak, and hadronic contributions) and the Brookhaven/FNAL measurements. The FNAL Run 1–3 result confirmed the tension at approximately 5σ level before the 2023 lattice QCD revision brought the SM prediction closer to the measured value.

IV.T180 computes a_μ by propagating α_τ (the τ-derived fine-structure constant, ~0 ppm from CODATA) through the Schwinger series and higher-order QED contributions. The dominant Schwinger term a_μ^(1) = α/(2π) is computed with α_τ. The higher-order QED contributions are computed using the same α_τ value. The τ-framework does not independently compute hadronic vacuum polarization (HVP) or hadronic light-by-light (HLbL) contributions — these are taken from the SM calculations — but the propagated α_τ correction shifts the total prediction by +8.8 ppm relative to the measured FNAL value.

At +8.8 ppm this is a sub-10 ppm result (rank 7 in the 1–10 ppm precision tier in the Cross-Domain Analysis). The physical significance is that the same α_τ that gives α⁻¹ = 137.036 at ~0 ppm from CODATA directly predicts a_μ at sub-10 ppm precision from FNAL. This addresses one of the most publicized tensions in modern particle physics.

## Result Statement

IV.T180: Muon g–2 a_μ(τ) at +8.8 ppm from FNAL measurement. Derived by propagating α_τ through QED corrections. Sub-10 ppm precision.
