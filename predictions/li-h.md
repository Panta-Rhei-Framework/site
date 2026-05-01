---
layout: "prediction-page"
title: "Lithium-7 Abundance (Framework Account)"
title_plain: "Lithium-7 Abundance (Framework Account)"
permalink: "/predictions/li-h/"
lane: "results"
prediction_id: "pred-045"
domain: "cosmology"
domain_display: "Cosmology"
observable: "⁷Li/H"
observable_mathml: "<math><mi>S = 1/3</mi></math> suppression"
formula_plain: "S = 1/3 suppression"
formula_mathml: "<math><mi>S = 1/3</mi></math> suppression"
formula_display: "⁷Li/H = S × standard BBN, S = 1/3 → 1.6 × 10⁻¹⁰"
tau_value: "1.6!×!10⁻¹⁰"
observed: "1.6!×!10⁻¹⁰"
observed_value: "1.6!×!10⁻¹⁰"
deviation: "∼ 0%"
precision_tier: "1-5-percent"
cascade_tier: "A"
precision_display: "1–5%"
registry_id: "V.T244"
scope: "conjectural"
scope_display: "Conjectural"
canonical_books:
  - "V"
summary_short: "Lithium-7 Abundance (Framework Account): τ-value 1.6!×!10⁻¹⁰, observed 1.6!×!10⁻¹⁰, deviation ∼ 0%."
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
    precision: "1–5%"
    scope: "Conjectural"
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
    module: "TauLib.BookI.Coordinates.Hyperfact"
    formalization: "formalized"
    registry_id_origin: "I.T04"
  -
    module: "TauLib.BookI.Denotation.TauIdx"
    formalization: "formalized"
    registry_id_origin: "I.D07"
  -
    module: "TauLib.BookI.Orbit.Ladder"
    formalization: "formalized"
    registry_id_origin: "I.D06"
  -
    module: "TauLib.BookI.Polarity.BipolarAlgebra"
    formalization: "formalized"
    registry_id_origin: "I.D28"
  -
    module: "TauLib.BookI.Polarity.Lemniscate"
    formalization: "formalized"
    registry_id_origin: "I.D18"
  -
    module: "TauLib.BookI.Polarity.Polarity"
    formalization: "formalized"
    registry_id_origin: "I.T05"
  -
    module: "TauLib.BookI.Polarity.Spectral"
    formalization: "formalized"
    registry_id_origin: "I.D19e"
  -
    module: "TauLib.BookIII.Enrichment.LayerTemplate"
    formalization: "formalized"
    registry_id_origin: "III.D08"
  -
    module: "TauLib.BookIII.Sectors.Decomposition"
    formalization: "formalized"
    registry_id_origin: "III.D13"
  -
    module: "TauLib.BookIII.Sectors.LanglandsReflection"
    formalization: "formalized"
    registry_id_origin: "III.D17"
  -
    module: "TauLib.BookIII.Sectors.ParityBridge"
    formalization: "formalized"
    registry_id_origin: "III.T07"
  -
    module: "TauLib.BookIV.Sectors.SectorParameters"
    formalization: "formalized"
    registry_id_origin: "IV.D05"
  -
    module: "TauLib.BookV.Cosmology.BBNBaryogenesis"
    formalization: "formalized"
    registry_id_origin: "V.D198"
  -
    module: "TauLib.BookV.Cosmology.BBNNuclearNetwork"
    formalization: "formalized"
    registry_id_origin: "V.T244"
  -
    module: "TauLib.BookV.Cosmology.BaryogenesisAsymmetry"
    formalization: "formalized"
    registry_id_origin: "V.T172"
  -
    module: "TauLib.BookV.Cosmology.HeliumFraction"
    formalization: "formalized"
    registry_id_origin: "V.T149"
  -
    module: "TauLib.BookV.Cosmology.ThresholdLadder"
    formalization: "formalized"
    registry_id_origin: "V.D159"
  -
    module: "TauLib.BookV.GravityField.LinearEinstein"
    formalization: "formalized"
    registry_id_origin: "V.D52"
  -
    module: "TauLib.BookV.GravityField.NonlinearEinstein"
    formalization: "formalized"
    registry_id_origin: "V.D56"
lean_linkage_status: "derived"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.2"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**⁷Li/H = S × standard BBN, S = 1/3 → 1.6 × 10⁻¹⁰**

## Derivation

With the suppression factor $S = 1/3$
applied to the $^7Be$ production channel:

^7Li/H(τ)
\;=\;
S_^7Be
× ^7Li/H(SBBN)
\;=\;
13 × 5.62 × 10^-10
\;≈\;
1.87 × 10^-10,

in comparison with the Spite plateau observation
$^7Li/H_obs
= (1.6 ± 0.3) × 10^-10$.
The deviation is $+0.9σ$—well
within observational uncertainty.
Including the standard
$∼ 15%$ stellar depletion correction:

^7Li/H(surface)
\;=\;
1.87 × 10^-10 × 0.85
\;≈\;
1.59 × 10^-10,

## Source

This prediction is derived in the Numerical Physics Ledger (Chapter 62 — inflation-cmb-bbn), Books IV–V of *Panta Rhei*.
