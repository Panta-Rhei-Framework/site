---
layout: "prediction-page"
title: "CKM Parameter η̄"
title_plain: "CKM Parameter η̄"
permalink: "/predictions/bar-14/"
lane: "results"
prediction_id: "pred-014"
domain: "particle-physics"
domain_display: "Particle Physics"
observable: "barη"
observable_mathml: "<math><mi>ι<sub>τ</sub>⁻¹/⁴ κD⁵/⁴/sqrt5</mi></math>"
formula_plain: "ι<sub>τ</sub>⁻¹/⁴ κD⁵/⁴/sqrt5"
formula_mathml: "<math><mi>ι<sub>τ</sub>⁻¹/⁴ κD⁵/⁴/sqrt5</mi></math>"
formula_display: "η̄ = ι<sub>τ</sub>⁻¹ᐟ⁴ · κ_D⁵ᐟ⁴ / √5 ≈ 0.345"
tau_value: "0.345"
observed: "0.348"
observed_value: "0.348"
deviation: "-2285~ppm"
precision_tier: "1-5-percent"
cascade_tier: "A"
precision_display: "1–5%"
registry_id: "IV.T167"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "IV"
summary_short: "CKM Parameter η̄: τ-value 0.345, observed 0.348, deviation -2285~ppm."
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
    precision: "1–5%"
    scope: "τ-Effective"
    updated: "April 2026"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.1"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**η̄ = ι<sub>τ</sub>⁻¹ᐟ⁴ · κ_D⁵ᐟ⁴ / √5 ≈ 0.345**

## Derivation

where $κ_D = 1 - ι<sub>τ</sub>$.
The PDG 2024 value is
$η = 0.349^+0.012_-0.011$,
giving a deviation of $-2\,285$ ppm ($-0.23%$, $0.7σ$).

The exponents in (eq:ch61-etabar)
are not numerological accidents.
They have a topological reading
(IV.D363/IV.T173):

-14
&= -12 · |lobes|
= -12 × 2
(holonomy factor),
+54
&= |gen|2 · |lobes|
+ 1|lobes|
= 34 + 12
(coupling factor),
-12
&= -1|lobes|
= |gen|^-1/2|_|gen|=4
(normalization factor).

η
= ι<sub>τ</sub>^-1/(2·lobes)_holonomy
\;·\;
κ_D^|gen|/(2·lobes)+1/lobes_coupling
\;·\;
|generators|^-1/lobes_normalization.

## Source

This prediction is derived in the Numerical Physics Ledger (Chapter 61 — mixing-baryogenesis), Books IV–V of *Panta Rhei*.
