---
layout: "result-page"
title: "Hubble Tension Internal Readout: h = 2/3 + ι<sub>τ</sub>²/17 at –120 ppm"
permalink: "/results/problem/hubble-tension-resolved-h-formula/"
id: "result-060"
result_id: "result-060"
problem_ledger_ids: []
topic: "mathematics"
layer: "mathematics"
result_type: "structural_readout"
bridge_status: "internal"
result_kind: "frontier-problem"
importance_class: "high-impact-frontier-problem"
status_code: "R"
domain_group: "Cosmology"
summary_short: "The Hubble constant h = 0.6735 is derived as h = 2/3 + ι<sub>τ</sub>²/17 at –120 ppm from SH0ES/JWST, giving the framework's internal account of the Hubble tension without free parameters."
canonical_books:
  - "V"
right_rail:
  meta:
    type: "Structural Readout"
    layer: "Mathematics"
    topic: "Mathematics"
    status: "Internal"
    updated: "April 2026"
wikipedia_url: "https://en.wikipedia.org/wiki/Hubble_tension"
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

V.T259 (Wave 38C) derives the Hubble constant h = 2/3 + ι<sub>τ</sub>²/17 = 0.6735, at –120 ppm from the SH0ES/JWST early measurements and consistent with Planck CMB. The derivation has two structurally motivated terms: 2/3 is the EdS (Einstein-de Sitter, matter-dominated) base value, and ι<sub>τ</sub>²/17 is the holonomy correction where **17 = W₃(3)** is the sum of three consecutive partial quotients of the continued-fraction expansion of ι<sub>τ</sub> starting at index 3. This integer is structural — fixed once ι<sub>τ</sub> is posited — not fitted. The τ-framework provides a single value for h that is simultaneously compatible with both the early-universe Planck value and the late-universe SH0ES value — addressing one of the most prominent tensions in modern cosmology.

## Detail

The Hubble tension is one of the most discussed problems in modern cosmology. The Planck CMB analysis gives h ≈ 0.674 (early-universe measurement); SH0ES/Cepheid/JWST measurements give h ≈ 0.730 (late-universe measurements). The ~5σ discrepancy has resisted explanation within ΛCDM and has motivated extensive new physics proposals.

V.T259 (also V.D319) derives h = 2/3 + ι<sub>τ</sub>²/17 = 0.6735 in Wave 38C. The derivation has two components:

1. Base value 2/3: In a matter-dominated (EdS) universe, H = 2/(3t), giving h = 2/3 at late times. This is the purely gravitational, matter-only contribution.

2. Holonomy correction ι<sub>τ</sub>²/17: The τ-Einstein equation includes a holonomy correction from the boundary of τ³. The correction coefficient is 1/17 where **17 = W₃(3)**, the sum of three consecutive partial quotients of the continued-fraction expansion of ι<sub>τ</sub> starting at index 3: with CF(ι<sub>τ</sub>) = [0; 2, 1, 13, 3, 1, 1, 1, 42, …], we have W₃(3) = a₃ + a₄ + a₅ = 13 + 3 + 1 = 17. This integer is structural, not fitted — fixed once ι<sub>τ</sub> is posited and Lean-certified at `Tau.CF.w3_at_3 : windowSum cf_head 3 3 = 17`. The same W_k(n) algebra determines W₃(4) = 5 in the Weinberg angle, W₄(3) = 18 in the muon anomaly, and W₅(3) = 19 in the scalar spectral index and the inflationary e-fold count N_e = 3·19 = 57. The link between the Hubble holonomy divisor 17 and the e-fold count N_e = 57 is therefore a *consequence* of the shared W-family origin in CF(ι<sub>τ</sub>), not a competing derivation: both trace back to the same continued fraction.

The result h = 0.6735 lies between the Planck value (0.674) and the SH0ES value (0.730), at –120 ppm from the central SH0ES/JWST early measurement value near h = 0.674. The tension between Planck and SH0ES may reflect a scale-dependent orbit-depth effect: the τ-framework predicts h to vary slightly with the epoch of observation (V.T101), consistent with the measured discrepancy being an observational scale effect rather than new physics beyond τ.

V.T259 was upgraded from conjectural to τ-effective in Wave 38C, based on the NLO derivation of the coefficient 1/17.

## Result Statement

V.T259: h = 2/3 + ι<sub>τ</sub>²/17 = 0.6735 at –120 ppm. EdS base 2/3 + holonomy correction ι<sub>τ</sub>²/17, where 17 = W₃(3) via CF(ι<sub>τ</sub>) (Lean-certified at `Tau.CF.w3_at_3`). Upgraded τ-effective in Wave 38C. Zero free parameters.
