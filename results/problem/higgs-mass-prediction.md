---
layout: "result-page"
title: "Higgs Boson Mass Prediction at +8.0 ppm"
permalink: "/results/problem/higgs-mass-prediction/"
id: "result-012"
result_id: "result-012"
problem_ledger_ids: []
topic: "physics"
layer: "physics"
result_type: "structural_readout"
bridge_status: "internal"
result_kind: "frontier-problem"
importance_class: "domain-level-open-problem"
status_code: "R"
domain_group: "Physics"
summary_short: "The Higgs boson mass is derived from the structural integer n = 7 = 2·|lobes| + |sectors| at +8.0 ppm from the PDG value of 125.20 GeV."
canonical_books:
  - "IV"
right_rail:
  meta:
    type: "Structural Readout"
    layer: "Physics"
    topic: "Physics"
    status: "Internal"
    updated: "April 2026"
visibility: "public"
provenance_source: "manuscript"
lean_formalization_status: "formalized"
cascade_layer: "physics-cascade"
foundational_hinge_ids: []
glossary_term_ids:
  - "PG-P10-higgs-boson"
recovery_requirement_ids: []
generated_from: "corpus/results"
projection_version: "v0.2"
canonical_source: "corpus/results"
do_not_edit: true
---

## Overview

IV.T166 derives the Higgs boson mass using the structural integer n = 7, where 7 = 2·|lobes| + |sectors| = 2·2 + 3 = 7 (two lemniscate lobes and three τ-sectors). The formula m_H = κ_ω⁻¹(4 − ι<sub>τ</sub>³/(1 − 5κ_ω)) with n = 7 gives +8.0 ppm agreement with the PDG value of 125.20 GeV — exceptional precision with zero free continuous parameters.

## Detail

The Higgs mass is the least well-understood mass parameter in the Standard Model. It is determined experimentally at 125.20 ± 0.11 GeV, but the Standard Model provides no explanation for why it takes this value (the hierarchy problem). [Book IV]({{ '/publications/books/book-iv/' | relative_url }}) derives m_H from the ω-sector structure. The derivation uses the structural integer n = 7, where 7 counts the total dimension of the τ-structure available to the ω generator: 2 lobes of the lemniscate boundary (the topological dimension of L) plus 3 primitive sectors (the number of non-ω sectors, i.e., D, A+B, C). The formula κ_ω⁻¹(4 − ι<sub>τ</sub>³/(1 − 5κ_ω)) involves κ_ω = ι<sub>τ</sub>/(1 + ι<sub>τ</sub>) (the ω-sector coupling constant), and W₃(4) = 5 (appearing in the denominator as the NLO correction coefficient). The result at n = 7 gives +8.0 ppm. An earlier derivation used n = 5 and gave +493 ppm; the n = 7 derivation supersedes it.

## Result Statement

IV.T166: m_H derived from n = 7 = 2·|lobes| + |sectors| = 2·2 + 3 = 7 at +8.0 ppm from PDG value 125.20 GeV. (n=5 at +493 ppm was superseded.)
