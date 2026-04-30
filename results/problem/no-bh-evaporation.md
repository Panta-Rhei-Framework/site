---
layout: "result-page"
title: "No Black Hole Evaporation: dM/dn ≥ 0 and Information Preserved"
permalink: "/results/problem/no-bh-evaporation/"
id: "result-031"
result_id: "result-031"
problem_ledger_ids: []
topic: "mathematics"
layer: "mathematics"
result_type: "structural_readout"
bridge_status: "internal"
result_kind: "consequence"
importance_class: "consequence-reframing"
status_code: "C"
domain_group: "Black Holes"
summary_short: "Black hole mass is non-decreasing in the τ-framework (dM/dn ≥ 0 exactly); Hawking evaporation does not occur and information is preserved."
canonical_books:
  - "V"
right_rail:
  meta:
    type: "Structural Readout"
    layer: "Mathematics"
    topic: "Mathematics"
    status: "Internal"
    updated: "April 2026"
visibility: "public"
provenance_source: "manuscript"
lean_formalization_status: "planned"
cascade_layer: "kernel"
foundational_hinge_ids: []
glossary_term_ids:
  - "PG-O11-black-hole"
recovery_requirement_ids: []
generated_from: "corpus/results"
projection_version: "v0.2"
canonical_source: "corpus/results"
do_not_edit: true
---

## Overview

V.C19 and V.T114 prove that in the τ-framework, the black hole mass satisfies dM/dn ≥ 0 exactly: BH mass is non-decreasing along the τ-evolution. Hawking evaporation — the quantum mechanical process by which black holes lose mass through thermal radiation — does not occur in Category τ. As a consequence, the black hole information paradox is dissolved: information is preserved because no evaporation takes place.

## Detail

Hawking radiation is a quantum field theory effect in curved spacetime that predicts black holes emit thermal radiation and eventually evaporate, leaving behind no information about the infalling matter. This creates the black hole information paradox: unitary quantum mechanics requires information to be preserved, but thermal Hawking radiation appears to destroy information. The paradox is one of the central unsolved problems in theoretical physics. Book V addresses it through the τ-Einstein structure. In the τ-framework, Hawking radiation arises from quantum vacuum fluctuations near the event horizon. But V.C19 (Corollary 19) proves that the τ-vacuum has zero energy density (consistent with V.T139): there are no vacuum fluctuations in the τ-sense that could generate Hawking radiation. Therefore dM/dn ≥ 0 — the BH mass cannot decrease. V.T114 gives the full theorem: BH mass is a non-decreasing function of the τ-evolution parameter n. The information paradox is dissolved: since BH never evaporates, the infalling information is preserved inside the BH event horizon indefinitely (consistent with the BH being alive, VI.T29–T32).

## Result Statement

V.C19, V.T114: dM/dn ≥ 0 exactly in the τ-framework — BH mass is non-decreasing. Hawking evaporation does not occur. Information is preserved.
