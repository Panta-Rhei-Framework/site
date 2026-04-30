---
layout: "prediction-page"
title: "Jet Magnetic Field Ratio B_z/B_φ"
title_plain: "Jet Magnetic Field Ratio B_z/B_φ"
permalink: "/predictions/bz-b-jet/"
lane: "results"
prediction_id: "pred-059"
domain: "astrophysics"
domain_display: "Astrophysics"
observable: "Bz / B_φ (jet)"
observable_mathml: "fiber vs. base"
formula_plain: "fiber vs. base"
formula_mathml: "fiber vs. base"
formula_display: "B_z/B_φ = fiber/base ≈ ι<sub>τ</sub> ≈ 0.3"
tau_value: "ι<sub>τ</sub>"
observed: "≈!0.3"
observed_value: "≈!0.3"
deviation: "∼ 10%"
precision_tier: "structural"
cascade_tier: "A"
precision_display: "Structural"
registry_id: "V.P156"
scope: "conjectural"
scope_display: "Conjectural"
canonical_books:
  - "V"
summary_short: "Jet Magnetic Field Ratio B_z/B_φ: τ-value ι<sub>τ</sub>, observed ≈!0.3, deviation ∼ 10%."
right_rail:
  toc: false
  related:
    -
      title: "Predictions Browse"
      url: "/results/predictions/browse/"
    -
      title: "Falsification Pack"
      url: "/results/falsifications/browse/"
    -
      title: "Results Overview"
      url: "/results/"
  meta:
    type: "Physics Prediction"
    domain: "Astrophysics"
    precision: "Structural"
    scope: "Conjectural"
    updated: "April 2026"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.1"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**B_z/B_φ = fiber/base ≈ ι<sub>τ</sub> ≈ 0.3**

## Derivation

At the jet base ($∼ 10\,R_S$),
the axial-to-toroidal magnetic field ratio is

This follows from the torus hoop-stress collimation:
the toroidal component $B_$ provides
hoop stress $P = B_^2/(4π r)$
that collimates the jet,
while the axial component $B_z$
originates from the topologically protected $Φ_pol$.
The equilibrium condition
$θ_jet ≤ B_z/B_ = ι<sub>τ</sub>$
independently recovers the jet collimation angle
$θ_jet ≤ 20^$
(Theorem (thm:ch40-jet-hoop-stress)).

VLBI observations of AGN jets
at sub-parsec scales
measure $B_z/B_ ∼ 0.2$–$0.5$,
consistent with the $τ$-prediction
$ι<sub>τ</sub> ≈ 0.341$.
The ratio is a zero-parameter prediction,
testable with improved VLBI polarimetry.

## Source

This prediction is derived in the Numerical Physics Ledger (Chapter 64 — black-hole-topology), Books IV–V of *Panta Rhei*.
