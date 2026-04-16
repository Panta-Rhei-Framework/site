---
layout: prediction-page
title: "Fine-Structure Constant α"
title_plain: "Fine-Structure Constant α"
permalink: /predictions/pred-23/
lane: results
prediction_id: "pred-023"
domain: "electroweak-qcd"
domain_display: "Electroweak & QCD"
observable: "α"
observable_mathml: "<math><mi>(11/15)²,ι_τ⁴</mi></math>"
formula_plain: "(11/15)²,ι_τ⁴"
formula_mathml: "<math><mi>(11/15)²,ι_τ⁴</mi></math>"
formula_display: "α = (11/15)² · ι_τ⁴ → α⁻¹ ≈ 137.035"
tau_value: "1/137.035"
observed_value: "1/137.036"
deviation: "9.8~ppm"
precision_tier: "sub-10-ppm"
precision_display: "Sub-10 ppm"
registry_id: "IV.T25"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "IV"
summary_short: "Fine-Structure Constant α: τ-value 1/137.035, observed 1/137.036, deviation 9.8~ppm."
right_rail:
  toc: false
  related:
    - title: "Predictions Browse"
      url: /results/predictions/browse/
    - title: "Falsification Pack"
      url: /results/falsifications/browse/
    - title: "Results Overview"
      url: /results/
  meta:
    type: "Physics Prediction"
    domain: "Electroweak & QCD"
    precision: "Sub-10 ppm"
    scope: "τ-Effective"
    updated: "April 2026"
---

## τ-Formula

**α = (11/15)² · ι_τ⁴ → α⁻¹ ≈ 137.035**

## Derivation

The fine-structure constant α ≈ 1/137.036 is derived in Book IV, Chapter 10 (*The Fine-Structure Constant*). Feynman called it "one of the greatest damn mysteries of physics" — a pure, dimensionless number that governs all electromagnetic phenomena, measured to ~10⁻¹⁰ relative accuracy, yet treated as a free parameter in the Standard Model. In Category τ, the mystery dissolves.

Three independent derivation routes converge to the same value:

**Route A** (sector coupling): α = (11/15)² · ι_τ⁴, where the rational prefactor 11/15 arises from the ratio of active sector modes to the total spectral dimension, and the exponent 4 = 2 × lobes counts the two lobes of the lemniscate boundary at quadratic order. This yields α⁻¹ ≈ 137.035, matching CODATA to 9.8 ppm.

**Route B** (calibration chain): The same value emerges from the 10-link spectral chain that derives the electron mass. The fine-structure constant and the electron mass are two readings of the same chain — one is a ratio (dimensionless), the other is a mass (dimensionful, set by the neutron anchor).

**Route C** (G–α Bridge): The closing identity α_G = α¹⁸ · √3 · (1 − 3α/π) (V.T20) connects α directly to the gravitational constant G, providing an independent cross-check that contains no free parameters.

That α is *computable at all* — rather than a free parameter — rests on the spectral purity guarantee (Book III, III.T19): the Riemann Hypothesis ensures that eigenvalues of the boundary operator are cleanly separated, which in turn fixes the B-sector coupling that becomes α at the physical readout level.

## Source

This prediction is derived in Book IV, Part 1, Chapter 10 (*The Fine-Structure Constant*). The three convergent routes are presented in Sections 10.2–10.4. The G–α Bridge is in Book V, Part 8, Chapter 70.
