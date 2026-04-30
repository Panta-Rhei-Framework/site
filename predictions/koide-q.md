---
layout: "prediction-page"
title: "Koide Relation Q"
title_plain: "Koide Relation Q"
permalink: "/predictions/koide-q/"
lane: "results"
prediction_id: "pred-004"
domain: "particle-physics"
domain_display: "Particle Physics"
observable: "Koide Q"
observable_mathml: "<math><mi>2/3</mi></math>"
formula_plain: "2/3"
formula_mathml: "<math><mi>2/3</mi></math>"
formula_display: "Q = lobes / dim(τ³) = 2/3"
tau_value: "2/3"
observed: "0.66661"
observed_value: "0.66661"
deviation: "-9~ppm"
precision_tier: "sub-10-ppm"
cascade_tier: "A"
precision_display: "Sub-10 ppm"
registry_id: "IV.T143"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "IV"
summary_short: "Koide Relation Q: τ-value 2/3, observed 0.66661, deviation -9~ppm."
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

**Q = lobes / dim(τ³) = 2/3**

## Derivation

in agreement with the experimental value
$Q^(exp) = 0.666\,661 ± 0.000\,007$
at $-9$ ppm.
The rational value $2/3$
arises from the lemniscate structure:
$2/3 = lobes / (τ^3)$.
The derivation follows four steps:

- Three generations correspond
to three winding classes
in $π_1(τ^3) ≅ ℤ^3$
(Theorem (thm:ch60-three-gen-rank)).
- Each class has a mass eigenvalue
from the $T^2$ mode spectrum.
- The constraint
$χ_+ + χ_- = 1$
on the two lobes of $$
forces a democratic matrix structure.
- The democratic matrix
has eigenvalue ratio $2:(-1):(-1)$,
giving $Q = 2/3$.

The structurally significant parameter
controlling the departure of the lepton mass spectrum
from the democratic configuration
$m_e = m_μ = m_τ$ is

where lobes $= 2$
(the two lobes of $ = S^1 S^1$)
and $(τ^3)^2 = 9$.
This ratio controls the Koide phase,
setting the angular separation
of the three mass eigenvalues
on the unit circle
of the democratic mass matrix.

## Source

This prediction is derived in the Numerical Physics Ledger (Chapter 60 — mass-spectrum), Books IV–V of *Panta Rhei*.
