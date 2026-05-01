---
layout: "prediction-page"
title: "Galaxy Rotation Curve (NGC 3198)"
title_plain: "Galaxy Rotation Curve (NGC 3198)"
permalink: "/predictions/ngc-3198-v-f/"
lane: "results"
prediction_id: "pred-051"
domain: "astrophysics"
domain_display: "Astrophysics"
observable: "NGC 3198 vᵣₘ fₗₐₜ"
observable_mathml: "<math><mi>v⁴ = GMb c²/(2ℓ_τ)</mi></math>"
formula_plain: "v⁴ = GMb c²/(2ℓ_τ)"
formula_mathml: "<math><mi>v⁴ = GMb c²/(2ℓ_τ)</mi></math>"
formula_display: "v∞⁴ = G·M_b·c² / (2ℓ_τ) → v = 149.1 km/s"
tau_value: "149.1~km/s"
observed: "≈!150~km/s"
observed_value: "≈!150~km/s"
deviation: "0.6%"
precision_tier: "1-5-percent"
cascade_tier: "A"
precision_display: "1–5%"
registry_id: "V.T163"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "V"
summary_short: "Galaxy Rotation Curve (NGC 3198): τ-value 149.1~km/s, observed ≈!150~km/s, deviation 0.6%."
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
    precision: "1–5%"
    scope: "τ-Effective"
    updated: "April 2026"
lean_modules:
  -
    module: "TauLib.BookI.Boundary.Iota"
    formalization: "formalized"
    registry_id_origin: "I.D34"
  -
    module: "TauLib.BookI.Boundary.Ring"
    formalization: "formalized"
    registry_id_origin: "I.D19"
  -
    module: "TauLib.BookI.Boundary.SplitComplex"
    formalization: "formalized"
    registry_id_origin: "I.D20"
  -
    module: "TauLib.BookI.Coordinates.ABCD"
    formalization: "formalized"
    registry_id_origin: "I.D17"
  -
    module: "TauLib.BookI.Coordinates.Descent"
    formalization: "formalized"
    registry_id_origin: "I.L04"
  -
    module: "TauLib.BookI.Coordinates.Hyperfact"
    formalization: "formalized"
    registry_id_origin: "I.T04"
  -
    module: "TauLib.BookI.Coordinates.NoTie"
    formalization: "formalized"
    registry_id_origin: "I.L03"
  -
    module: "TauLib.BookI.Denotation.Arithmetic"
    formalization: "formalized"
    registry_id_origin: "I.P05"
  -
    module: "TauLib.BookI.Denotation.TauIdx"
    formalization: "formalized"
    registry_id_origin: "I.D07"
  -
    module: "TauLib.BookI.Orbit.Closure"
    formalization: "formalized"
    registry_id_origin: "I.T01"
  -
    module: "TauLib.BookI.Orbit.Generation"
    formalization: "formalized"
    registry_id_origin: "I.D05"
  -
    module: "TauLib.BookI.Polarity.BipolarAlgebra"
    formalization: "formalized"
    registry_id_origin: "I.D27"
  -
    module: "TauLib.BookI.Polarity.Lemniscate"
    formalization: "formalized"
    registry_id_origin: "I.D18"
  -
    module: "TauLib.BookI.Polarity.OmegaGerms"
    formalization: "formalized"
    registry_id_origin: "I.D25"
  -
    module: "TauLib.BookI.Polarity.Polarity"
    formalization: "formalized"
    registry_id_origin: "I.T05"
  -
    module: "TauLib.BookI.Polarity.PolarizedGerms"
    formalization: "formalized"
    registry_id_origin: "I.D26"
  -
    module: "TauLib.BookIV.Sectors.SectorParameters"
    formalization: "formalized"
    registry_id_origin: "IV.D04"
  -
    module: "TauLib.BookV.Astrophysics.RotationCurves"
    formalization: "formalized"
    registry_id_origin: "V.T163"
  -
    module: "TauLib.BookV.GravityField.NonlinearEinstein"
    formalization: "formalized"
    registry_id_origin: "V.T37"
  -
    module: "TauLib.BookV.GravityField.TauSchwarzschild"
    formalization: "formalized"
    registry_id_origin: "V.D63"
  -
    module: "TauLib.BookV.Temporal.MacroReadout"
    formalization: "formalized"
    registry_id_origin: "V.D31"
lean_linkage_status: "derived"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.2"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**v∞⁴ = G·M_b·c² / (2ℓ_τ) → v = 149.1 km/s**

## Derivation

Systematic assessment of all predictions above $5000\,ppm$
after Wave 49 corrections:

**Observable** | **Before** | **After** | **Status**
$θ_23$ (IV.T206) | $+8604$ | $-494$ | NNLO, sub-1000 $δ_CP$ (IV.T207) | $+9365$ | $+5645$ | NLO, 40% improved $m_μ/m_e$ (IV.T176) | $+6156$ | $-8.2$ | NNLO done (Wave 6D) QLC $θ_12$ (IV.T163) | $-41965$ | $-41965$ | structural limit $η$ pentagon (IV.D359) | $+75275$ | $+75275$ | structural limit

The QLC $θ_12$ and $η$ pentagon entries represent
**structural limits**: they require qualitatively new mathematical
insight (exact $θ_C$ NLO coupling for $θ_12$; complex
geometry resolution for $η$), not incremental NLO engineering.

- $θ_13$: $+5000\,ppm$ (sub-$1%$, $1.6σ$),
- $θ_12$: $+3106\,ppm$ (approaching $τ$-effective),
- $θ_23$: $-494\,ppm$ (NNLO, sub-$1000$),
- $δ_CP$: $+5645\,ppm$ (NLO, improved $40%$).

## Source

This prediction is derived in the Numerical Physics Ledger (Chapter 35 — three-generations), Books IV–V of *Panta Rhei*.
