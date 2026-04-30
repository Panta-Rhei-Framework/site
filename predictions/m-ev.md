---
layout: "prediction-page"
title: "Sum of Neutrino Masses"
title_plain: "Sum of Neutrino Masses"
permalink: "/predictions/m-ev/"
lane: "results"
prediction_id: "pred-007"
domain: "particle-physics"
domain_display: "Particle Physics"
observable: "Σ m_ν (eV)"
observable_mathml: "CF-asymm grid"
formula_plain: "CF-asymm grid"
formula_mathml: "CF-asymm grid"
formula_display: "Σmν = 0.089 eV (CF-asymmetry grid)"
tau_value: "0.089"
observed: "< 0.12"
observed_value: "< 0.12"
deviation: "+7~ppm"
precision_tier: "sub-10-ppm"
cascade_tier: "A"
precision_display: "Sub-10 ppm"
registry_id: "V.T175"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "V"
summary_short: "Sum of Neutrino Masses: τ-value 0.089, observed < 0.12, deviation +7~ppm."
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
    domain: "Particle Physics"
    precision: "Sub-10 ppm"
    scope: "τ-Effective"
    updated: "April 2026"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.1"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**Σmν = 0.089 eV (CF-asymmetry grid)**

## Derivation

The NuFIT 5.3 value is
$^2θ_23 = 0.572 ± 0.018$
(normal ordering),
giving a deviation of $+8\,604$ ppm ($+0.86%$, $0.9σ$).

The formula has a structural reading:
$θ_23$
is the probability amplitude
for a neutrino to traverse
one lobe of $$
through the $ι<sub>τ</sub>$-coupling gate.
The factor $(1+ι<sub>τ</sub>)^-1$
is the inverse of the effective junction width.

The atmospheric angle is *near-maximal*
but not exactly maximal:
$^2θ_23 ≠ 1/2$.
In $τ$,
exact maximality
would require $ι<sub>τ</sub> = 0$,
which is excluded by the Central Theorem.
The deviation from maximality
is a direct measure of $ι<sub>τ</sub>$:

This is a genuine prediction:
if future experiments determine
$^2θ_23 = 0.500\,0 ± $
with $ < 0.01$,
the formula (eq:ch61-theta23)
would be falsified.

## Source

This prediction is derived in the Numerical Physics Ledger (Chapter 61 — mixing-baryogenesis), Books IV–V of *Panta Rhei*.
