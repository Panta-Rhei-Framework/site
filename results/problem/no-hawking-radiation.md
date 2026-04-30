---
layout: "result-page"
title: "No Hawking Radiation"
permalink: "/results/problem/no-hawking-radiation/"
id: "result-114"
result_id: "result-114"
problem_ledger_ids: []
topic: "physics"
layer: "physics"
result_type: "consequence"
bridge_status: "contradicted"
result_kind: "consequence"
importance_class: "consequence-reframing"
status_code: "C"
domain_group: "BH"
summary_short: "The τ-framework predicts that black holes do not evaporate via Hawking radiation. The boundary structure of τ³ does not support the semi-classical pair-creation…"
canonical_books:
  - "V"
right_rail:
  meta:
    type: "Consequence"
    layer: "Physics"
    topic: "Physics"
    status: "Contradicted"
    updated: "April 2026"
visibility: "public"
provenance_source: "manuscript"
lean_formalization_status: "planned"
cascade_layer: "physics-cascade"
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

The τ-framework predicts that black holes do not evaporate via Hawking radiation. In mainstream physics, Hawking (1975) argued that quantum effects near the event horizon produce particle-antiparticle pairs, with one particle escaping to infinity and the other falling in, causing the black hole to slowly lose mass and eventually evaporate. This prediction has become one of the cornerstones of theoretical physics, despite never being experimentally confirmed.

Category τ reaches the opposite conclusion: the profinite boundary structure of τ³ does not support the semi-classical pair-creation mechanism that Hawking radiation requires.

## Detail

The argument rests on the framework's [black hole topology]({{ '/corpus/monographs/' | relative_url }}): in τ³, the event horizon is a T² surface — a torus, not a mathematical boundary of spacetime. The profinite structure of the [primorial tower]({{ '/corpus/monographs/' | relative_url }}) prevents the divergences that classical general relativity produces at the horizon.

Hawking's calculation relies on quantum field theory on a fixed curved background — the semi-classical approximation. In this approximation, the vacuum state near the horizon contains virtual particle pairs that can be separated by the gravitational field. The key assumption is that the background spacetime has a smooth event horizon where pair-creation can occur.

In Category τ, this assumption fails. The horizon is not a smooth surface in a continuum manifold — it is a discrete topological transition in the profinite structure. The **No-Shrink Theorem** (V.C19) proves that mature black holes cannot decrease in mass: the profinite tower structure ensures monotonic growth along the α-orbit. The **black hole merger normal form** (V.T114) classifies all black hole mass changes as merger events, not evaporative losses.

This is one of the framework's most exposed predictions. If Hawking radiation were experimentally detected — for example, through analogue black hole experiments or primordial black hole signatures — this prediction would be falsified. The framework carries this prediction with the scope label *conjectural* because it contradicts the mainstream theoretical expectation, though Hawking radiation has itself never been observed.

See also: [No BH Evaporation]({{ '/results/problem/no-bh-evaporation/' | relative_url }}) for the complementary result on evaporation, and the [Black Holes module]({{ '/corpus/monographs/' | relative_url }}) for the full topological treatment.

## Result Statement

No Hawking radiation: the profinite boundary structure of τ³ does not support semi-classical pair creation at the horizon. The No-Shrink Theorem (V.C19) proves monotonic mass growth. Contradicts mainstream theoretical expectation. Status: **Contradicted** *(conjectural — Hawking radiation has never been observed, but is widely expected)*.
