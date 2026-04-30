---
layout: "result-page"
title: "Hyperfactorization"
permalink: "/results/problem/hyperfactorization/"
id: "result-086"
result_id: "result-086"
problem_ledger_ids: []
topic: "mathematics"
layer: "mathematics"
result_type: "foundational_math"
bridge_status: "resolved"
result_kind: "foundational-math"
importance_class: "core-foundational-problem"
status_code: "R"
domain_group: "COORD"
summary_short: "Hyperfactorization is a foundational math in the COORD domain."
canonical_books:
  - "I"
right_rail:
  meta:
    type: "Foundational Math"
    layer: "Mathematics"
    topic: "Mathematics"
    status: "Internally addressed"
    updated: "April 2026"
wikipedia_url: "https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic"
visibility: "public"
provenance_source: "manuscript"
lean_formalization_status: "none"
cascade_layer: "kernel"
foundational_hinge_ids: []
glossary_term_ids: []
recovery_requirement_ids: []
generated_from: "corpus/results"
projection_version: "v0.2"
canonical_source: "corpus/results"
do_not_edit: true
---

## Overview

The Hyperfactorization Theorem (I.T04) is the first hinge theorem of the entire series. It proves that the [ABCD Coordinate Chart]({{ '/corpus/monographs/' | relative_url }}) is injective: every object in Category <math><mi>&tau;</mi></math> has a *unique* four-dimensional address. Without this result, the coordinate system would be ambiguous and all subsequent structural claims would collapse.

## Detail

Three lemmas support the theorem: tetration injectivity, the No-Tie Lemma (I.L03, ensuring the greedy peel is deterministic), and Strict Remainder Descent (I.L04, ensuring termination). The consequence is that shadow equality collapses to ontic identity -- distinct objects always have distinct addresses. See the [full derivation]({{ '/results/problem/hyperfactorization-theorem/' | relative_url }}) and the [Hyperfactorization module]({{ '/corpus/monographs/' | relative_url }}) for the complete proof structure.

## Result Statement

Every object has a unique ABCD decomposition. Status: **Internally addressed** *(established, machine-checked in [TauLib]({{ '/verify/taulib/' | relative_url }}))*.
