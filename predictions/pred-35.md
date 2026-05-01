---
layout: "prediction-page"
title: "First CMB Acoustic Peak ℓ₁"
title_plain: "First CMB Acoustic Peak ℓ₁"
permalink: "/predictions/pred-35/"
lane: "results"
prediction_id: "pred-035"
domain: "cosmology"
domain_display: "Cosmology"
observable: "ℓ₁"
observable_mathml: "M3h holonomy"
formula_plain: "M3h holonomy"
formula_mathml: "M3h holonomy"
formula_display: "ℓ₁ = ℓ_A · (1 − φ₁) ≈ 220.6"
tau_value: "220.6"
observed: "220.0"
observed_value: "220.0"
deviation: "+2840~ppm"
precision_tier: "1-5-percent"
cascade_tier: "A"
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
    module: "TauLib.BookV.Cosmology.BaryogenesisAsymmetry"
    formalization: "formalized"
    registry_id_origin: "V.T172"
  -
    module: "TauLib.BookV.Cosmology.CMBSpectrum"
    formalization: "formalized"
    registry_id_origin: "V.T190"
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
from $ι<sub>τ</sub>$ with zero free parameters.
The Planck measurement gives
$_1 = 220.0 ± 0.5$.
The deviation is $+0.28%$ ($+2840$ ppm).
*(Registry: V.T190, $τ$-effective, Wave 8A.)*

The computation of $_1$
requires three $τ$-native inputs,
each derived from $ι<sub>τ</sub>$:

- **Baryon density:**
$ω_b = 0.02209$,
derived from
$η_B = (121/270)\,ι<sub>τ</sub>^19$
(Section (sec:ch62-baryon-density)).

## Source

This prediction is derived in the Numerical Physics Ledger (Chapter 62 — inflation-cmb-bbn), Books IV–V of *Panta Rhei*.
