---
layout: "prediction-page"
title: "Neutrino Majorana Signature"
title_plain: "Neutrino Majorana Signature"
permalink: "/predictions/c/"
lane: "results"
prediction_id: "pred-009"
domain: "particle-physics"
domain_display: "Particle Physics"
observable: "σ = C_τ"
observable_mathml: "zero holonomy"
formula_plain: "zero holonomy"
formula_mathml: "zero holonomy"
formula_display: "σ = C_τ (zero holonomy) → Majorana"
tau_value: "Majorana"
observed: "(pending)"
observed_value: "(pending)"
deviation: "–"
precision_tier: "structural"
cascade_tier: "binary"
precision_display: "Structural"
registry_id: "IV.T146"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "IV"
summary_short: "Neutrino Majorana Signature: τ-value Majorana, deviation –."
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
    precision: "Structural"
    scope: "τ-Effective"
    updated: "April 2026"
lean_modules:
  -
    module: "TauLib.BookI.Coordinates.Hyperfact"
    formalization: "formalized"
    registry_id_origin: "I.T04"
  -
    module: "TauLib.BookI.Orbit.Ladder"
    formalization: "formalized"
    registry_id_origin: "I.D06"
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
    module: "TauLib.BookI.Polarity.Spectral"
    formalization: "formalized"
    registry_id_origin: "I.D19e"
  -
    module: "TauLib.BookIV.Electroweak.MajoranaStructure"
    formalization: "formalized"
    registry_id_origin: "IV.T146"
lean_linkage_status: "derived"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.2"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**σ = C_τ (zero holonomy) → Majorana**

## Derivation

The $τ$-framework predicts the **normal hierarchy**
$m_1 < m_2 < m_3$
from the ordering $r < p$
of the winding exponents:

This is a falsifiable prediction:
if the inverted hierarchy is confirmed
by JUNO or DUNE,
the $τ$-framework's mass structure
would require revision.

All three neutrinos
are predicted to be Majorana particles.
The structural origin is the $σ = C_τ$ condition
(Book IV, IV.T146):
the zero-holonomy constraint
on the $σ$-matrix
requires the neutrino
to be its own antiparticle.
This is testable
by neutrinoless double-beta decay
($0νββ$) experiments.
With $Σ m_ν = 0.089$ eV in normal hierarchy,
the effective Majorana mass
$|m_ββ| ∼ 1$–$4$ meV
is within reach
of next-generation experiments
(LEGEND-1000, nEXO, CUPID)
by the early 2030s.

## Source

This prediction is derived in the Numerical Physics Ledger (Chapter 61 — mixing-baryogenesis), Books IV–V of *Panta Rhei*.
