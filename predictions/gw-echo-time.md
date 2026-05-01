---
layout: "prediction-page"
title: "Gravitational Wave Echo Time"
title_plain: "Gravitational Wave Echo Time"
permalink: "/predictions/gw-echo-time/"
lane: "results"
prediction_id: "pred-056"
domain: "astrophysics"
domain_display: "Astrophysics"
observable: "GW echo time"
observable_mathml: "<math><mi>t_± = 4GMι<sub>τ</sub>± ¹/c³</mi></math>"
formula_plain: "t_± = 4GMι<sub>τ</sub>± ¹/c³"
formula_mathml: "<math><mi>t_± = 4GMι<sub>τ</sub>± ¹/c³</mi></math>"
formula_display: "t± = 4GM·ι<sub>τ</sub>±¹/c³"
tau_value: "see text"
observed: "(pending)"
observed_value: "(pending)"
deviation: "–"
precision_tier: "structural"
cascade_tier: "binary"
precision_display: "Structural"
registry_id: "V.D283"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "V"
summary_short: "Gravitational Wave Echo Time: τ-value see text, deviation –."
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
    scope: "τ-Effective"
    updated: "April 2026"
lean_modules:
  -
    module: "TauLib.BookIII.Sectors.Decomposition"
    formalization: "formalized"
    registry_id_origin: "III.D13"
  -
    module: "TauLib.BookIV.Sectors.SectorParameters"
    formalization: "formalized"
    registry_id_origin: "IV.D06"
  -
    module: "TauLib.BookV.Astrophysics.BinaryMergersGW"
    formalization: "formalized"
    registry_id_origin: "V.T223"
  -
    module: "TauLib.BookV.Astrophysics.EHTReread"
    formalization: "formalized"
    registry_id_origin: "V.P83"
  -
    module: "TauLib.BookV.Gravity.BHTopoModes"
    formalization: "formalized"
    registry_id_origin: "V.D283"
  -
    module: "TauLib.BookV.GravityField.LinearEinstein"
    formalization: "formalized"
    registry_id_origin: "V.D52"
  -
    module: "TauLib.BookV.GravityField.NonlinearEinstein"
    formalization: "formalized"
    registry_id_origin: "V.D54"
  -
    module: "TauLib.BookV.GravityField.TOVStarBuilder"
    formalization: "formalized"
    registry_id_origin: "V.P20"
  -
    module: "TauLib.BookV.GravityField.TauEinsteinEq"
    formalization: "formalized"
    registry_id_origin: "V.D50"
  -
    module: "TauLib.BookV.GravityField.TauSchwarzschild"
    formalization: "formalized"
    registry_id_origin: "V.T40"
lean_linkage_status: "derived"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.2"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**t± = 4GM·ι<sub>τ</sub>±¹/c³**

## Derivation

The gravitational-wave echo time delays
for a $T^2$-topology black hole of mass $M$ are

The echo separation
$Δ t = t_- - t_+
= 4GM(ι<sub>τ</sub>^-1 - ι<sub>τ</sub>)/c^3$
places both echoes in the sensitive frequency band
of current and next-generation detectors:

**Source** &
$M\,(M_)$ &
$t_+\,(ms)$ &
$t_-\,(ms)$ &
$Δ t\,(ms)$
Stellar BH | 10 | 0.067 | 0.577 | 0.510 GW150914 remnant | 62 | 0.417 | 3.580 | 3.163 Intermediate | 150 | 1.009 | 8.660 | 7.651 Sgr A* | $4 × 10^6$ &
3cLISA band: $∼$4.3 mHz / $∼$37 mHz

## Source

This prediction is derived in the Numerical Physics Ledger (Chapter 64 — black-hole-topology), Books IV–V of *Panta Rhei*.
