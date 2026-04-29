---
layout: "prediction-page"
title: "Hubble Constant h"
title_plain: "Hubble Constant h"
permalink: "/predictions/h/"
lane: "results"
prediction_id: "pred-048"
domain: "cosmology"
domain_display: "Cosmology"
observable: "h"
observable_mathml: "<math><mi>τ</mi></math>-native <math><msub><mi>H</mi><mn>0</mn></msub></math>"
formula_plain: "τ-native H₀"
formula_mathml: "<math><mi>τ</mi></math>-native <math><msub><mi>H</mi><mn>0</mn></msub></math>"
formula_display: "h = 2/3 + ι<sub>τ</sub>²/17 = 0.6735"
tau_value: "0.6735"
observed: "0.6736"
observed_value: "0.6736"
deviation: "-15~ppm"
precision_tier: "10-1000-ppm"
cascade_tier: "A"
precision_display: "10–1000 ppm"
registry_id: "V.T196"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "V"
summary_short: "Hubble Constant h: τ-value 0.6735, observed 0.6736, deviation -15~ppm."
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
    domain: "Cosmology"
    precision: "10–1000 ppm"
    scope: "τ-Effective"
    updated: "April 2026"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.1"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**h = 2/3 + ι<sub>τ</sub>²/17 = 0.6735**

The denominator $17 = W_3(3) = a_3 + a_4 + a_5 = 13 + 3 + 1$
is the sum of three consecutive partial quotients
of the continued-fraction expansion
$CF(ι_τ) = [0; 2, 1, 13, 3, 1, 1, 1, 42, …]$
starting at index 3
(Lean-certified at `Tau.CF.w3_at_3`);
the base value $2/3$ is the matter-dominated
Einstein-de Sitter late-time limit.
Both numbers are structural — fixed once
$ι_τ = 2/(π+e)$ is posited — not fitted.
See the
[result page]({{ '/results/problem/hubble-tension-resolved-h-formula/' | relative_url }})
for the full derivation.

## Derivation

tter particle has been found.
After two decades
of theoretical effort,
the cosmological constant problem—a
mismatch of $120$ orders of magnitude
between the quantum vacuum prediction
and the observed value—remains
the worst quantitative failure
in the history of science.

This chapter demonstrates
that the dark sector dissolves
within Category $τ$.
The dissolution is not speculative:
it rests on five quantitative results,
each derived from the master constant
$ι<sub>τ</sub> = 2/(π + e)$
with zero free parameters.

- **Flat rotation curves**:
the master formula
$v^4 = G M_b c^2/(2_τ)$
reproduces NGC 3198 at $0.6%$
and passes a 20-galaxy survey
at $0.067$ dex RMS
(V.T85, V.D258).

- **Dark energy density**:
$Ω_Λ = κ_D(1 + ι<sub>τ</sub>^3) = 0.6849$,
matching Planck at $+269$ ppm
(V.T234).

## Source

This prediction is derived in the Numerical Physics Ledger (Chapter 63 — dark-sector), Books IV–V of *Panta Rhei*.
