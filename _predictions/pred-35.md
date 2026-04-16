---
layout: prediction-page
title: "First CMB Acoustic Peak ℓ₁"
title_plain: "First CMB Acoustic Peak ℓ₁"
permalink: /predictions/pred-35/
lane: results
prediction_id: "pred-035"
domain: "cosmology"
domain_display: "Cosmology"
observable: "ℓ₁"
observable_mathml: "M3h holonomy"
formula_plain: "M3h holonomy"
formula_mathml: "M3h holonomy"
formula_display: "ℓ₁ = ℓ_A · (1 − φ₁) ≈ 220.6"
tau_value: "220.6"
observed_value: "220.0"
deviation: "+2840~ppm"
precision_tier: "1-5-percent"
precision_display: "1–5%"
registry_id: "V.T190"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "V"
summary_short: "First CMB Acoustic Peak ℓ₁: τ-value 220.6, observed 220.0, deviation +2840~ppm."
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
    domain: "Cosmology"
    precision: "1–5%"
    scope: "τ-Effective"
    updated: "April 2026"
---

## τ-Formula

**ℓ₁ = ℓ_A · (1 − φ₁) ≈ 220.6**

## Derivation

The first acoustic peak multipole
is determined by the Friedmann pipeline
with $τ$-native inputs:

where $_A = π d_A(z_rec) / r_s(z_rec)$
is the acoustic scale,
$d_A$ is the angular diameter distance,
$r_s$ is the sound horizon at recombination,
and $_1$ is the phase shift
from the neutrino and gravitational driving.
All quantities are computed
from $ι_τ$ with zero free parameters.
The Planck measurement gives
$_1 = 220.0 ± 0.5$.
The deviation is $+0.28%$ ($+2840$ ppm).
*(Registry: V.T190, $τ$-effective, Wave 8A.)*

The computation of $_1$
requires three $τ$-native inputs,
each derived from $ι_τ$:

- **Baryon density:**
$ω_b = 0.02209$,
derived from
$η_B = (121/270)\,ι_τ^19$
(Section (sec:ch62-baryon-density)).

## Source

This prediction is derived in the Physics Ledger (Chapter 62 — inflation-cmb-bbn), Books IV–V of *Panta Rhei*.

