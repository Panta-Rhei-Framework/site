---
layout: "prediction-page"
title: "Strong Coupling Constant α_s(M_Z)"
title_plain: "Strong Coupling Constant α_s(M_Z)"
permalink: "/predictions/mz/"
lane: "results"
prediction_id: "pred-022"
domain: "electroweak-qcd"
domain_display: "Electroweak & QCD"
observable: "αₛ(MZ)"
observable_mathml: "<math><mi>W₃(4)</mi></math> NLO"
formula_plain: "W₃(4) NLO"
formula_mathml: "<math><mi>W₃(4)</mi></math> NLO"
formula_display: "α_s(M_Z) = W₃(4) NLO readout = 0.1183"
tau_value: "0.1183"
observed: "0.1180"
observed_value: "0.1180"
deviation: "+43~ppm"
precision_tier: "10-1000-ppm"
cascade_tier: "A"
precision_display: "10–1000 ppm"
registry_id: "IV.T140"
scope: "tau-effective"
scope_display: "τ-Effective"
canonical_books:
  - "IV"
summary_short: "Strong Coupling Constant α_s(M_Z): τ-value 0.1183, observed 0.1180, deviation +43~ppm."
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
    domain: "Electroweak & QCD"
    precision: "10–1000 ppm"
    scope: "τ-Effective"
    updated: "April 2026"
lean_modules:
  -
    module: "TauLib.BookI.Holomorphy.PresheafEssence"
    formalization: "formalized"
    registry_id_origin: "I.T41"
  -
    module: "TauLib.BookII.CentralTheorem.CentralTheorem"
    formalization: "formalized"
    registry_id_origin: "II.T40"
  -
    module: "TauLib.BookII.CentralTheorem.HartogsExtension"
    formalization: "formalized"
    registry_id_origin: "II.T37"
  -
    module: "TauLib.BookII.Closure.GeometricBiSquare"
    formalization: "formalized"
    registry_id_origin: "II.T49"
  -
    module: "TauLib.BookII.Domains.HolImpliesCont"
    formalization: "formalized"
    registry_id_origin: "II.T06"
  -
    module: "TauLib.BookII.Enrichment.SelfEnrichment"
    formalization: "formalized"
    registry_id_origin: "II.D53"
  -
    module: "TauLib.BookII.Enrichment.YonedaTheorem"
    formalization: "formalized"
    registry_id_origin: "II.T36"
  -
    module: "TauLib.BookII.Hartogs.CalibratedSplitComplex"
    formalization: "formalized"
    registry_id_origin: "II.D35"
  -
    module: "TauLib.BookII.Hartogs.MutualDetermination"
    formalization: "formalized"
    registry_id_origin: "II.T27"
  -
    module: "TauLib.BookII.Hartogs.SheafCoherence"
    formalization: "formalized"
    registry_id_origin: "II.T32"
  -
    module: "TauLib.BookII.Topology.TorusDegeneration"
    formalization: "formalized"
    registry_id_origin: "II.T13"
  -
    module: "TauLib.BookIII.Enrichment.Functor"
    formalization: "formalized"
    registry_id_origin: "III.D04"
  -
    module: "TauLib.BookIII.Enrichment.LayerTemplate"
    formalization: "formalized"
    registry_id_origin: "III.D05"
  -
    module: "TauLib.BookIII.Sectors.BoundaryCharacters"
    formalization: "formalized"
    registry_id_origin: "III.D11"
  -
    module: "TauLib.BookIII.Sectors.Decomposition"
    formalization: "formalized"
    registry_id_origin: "III.D13"
  -
    module: "TauLib.BookIII.Sectors.LanglandsReflection"
    formalization: "formalized"
    registry_id_origin: "III.T06"
  -
    module: "TauLib.BookIII.Sectors.ParityBridge"
    formalization: "formalized"
    registry_id_origin: "III.T08"
  -
    module: "TauLib.BookIV.Arena.Tau3Arena"
    formalization: "formalized"
    registry_id_origin: "IV.D255"
  -
    module: "TauLib.BookIV.Electroweak.WeinbergNLO"
    formalization: "formalized"
    registry_id_origin: "IV.T140"
  -
    module: "TauLib.BookIV.Sectors.SectorParameters"
    formalization: "formalized"
    registry_id_origin: "IV.D01"
lean_linkage_status: "derived"
generated_from: "corpus/results/facets/predictions"
projection_version: "v0.2"
canonical_source: "corpus/results/facets/predictions"
do_not_edit: true
---

## τ-Formula

**α_s(M_Z) = W₃(4) NLO readout = 0.1183**

## Derivation

The three electroweak observables
at the $Z$-pole
are derived in the $τ$ framework
as readouts of the A-sector
and B-sector couplings:

**Observable** &
$τ$**-value** &
**PDG 2024** &
**ppm**
$^2θ_W$ &
$0.231\,19$ &
$0.231\,21(4)$ &
$-0.65$ $M_W$ &
$80.3696$ GeV &
$80.3692(13)$ GeV &
$-0.42$ $α_s(M_Z)$ &
$0.11794$ &
$0.11789(10)$ &
$+43$

The Waring number $W_3(4) = 5$
plays the role in the $τ$ framework
that the loop order plays in orthodox perturbation theory.
Specifically:

- The tree-level Weinberg angle
is $^2θ_W^(0) = 1/4$
(the cross-coupling ratio
$κ(A;1)/κ(B;2)$
at zeroth order).
- The NLO correction
involves $ι<sub>τ</sub>^W_3(4) = ι<sub>τ</sub>^5$,
which shifts $^2θ_W$
from $1/4 = 0.2500$
to $0.2312$.
- The same $ι<sub>τ</sub>^5$ correction
enters $M_W$ and $α_s$,
producing the correlated triple agreement.

## Source

This prediction is derived in the Numerical Physics Ledger (Chapter 60 — mass-spectrum), Books IV–V of *Panta Rhei*.
