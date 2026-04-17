---

layout: result-page
title: 'Glass Transition: Regime from Defect-Tuple Phase Space'
permalink: /results/problem/glass-transition/
result_id: result-250
topic: physics
layer: physics
result_type: structural_readout
bridge_status: internal
result_kind: frontier-problem
importance_class: domain-level-open-problem
status_code: R
domain_group: "Physics"
summary_short: 'The glass transition is a rigorous τ-regime (Book IV ch62): glass lives where d₁ ≈ 0 and d₄ ≈ 0 in the defect-tuple phase space. The Glass Threshold K_glass demarcates the regime; the CheckGlass procedure decidably tests membership (IV.P288). First-principles, not phenomenological.'
canonical_books: ["IV"]
right_rail:
  meta:
    type: Structural Readout
    layer: Physics
    topic: Physics
    status: Internal
    updated: April 2026
---

## Overview

The glass transition is one of the most controversial unsolved problems in condensed matter physics: Phil Anderson called it "the deepest and most interesting unsolved problem in solid state theory". There is no universally accepted order parameter, no rigorous definition distinguishing a glass from a supercooled liquid, and no first-principles derivation of the transition temperature. Book IV ch62 ("Crystals, Glass, and Phase Transitions") provides one. In τ, glass is a rigorous regime: it lives where d₁ ≈ 0 and d₄ ≈ 0 in the defect-tuple phase space (d₁, d₂, d₃, d₄). The Glass Threshold K_glass demarcates the regime; the CheckGlass procedure decidably tests whether a configuration belongs (IV.P288, glass transition as kinetic crossover). The treatment is first-principles — no fitted correlation lengths, no phenomenological relaxation times.

## Detail

Orthodox glass-transition theories fall into two broad classes: kinetic theories (mode-coupling, Adam-Gibbs) that describe dynamic arrest without resolving the thermodynamic ontology, and thermodynamic theories (Kauzmann entropy crisis, random first-order transition) that posit an ideal glass transition at an inaccessibly slow cooling rate. Neither program has converged on a rigorous definition, and experimental work cannot distinguish between them definitively. Book IV (`books/IV-CategoricalMicrocosm/latex/sections/part07/ch62-crystals-glass-phases.tex`) recasts the problem in the defect-tuple phase space (d₁, d₂, d₃, d₄) — the four dimensional coordinates that characterize τ-regimes. The Glass Regime (def:iv-glass-regime-detail, line 204) is defined by d₁ = 0, d₄ ≈ 0: glass has vanishing long-range order in two of the four directions while retaining short-range structure in the others. The Glass Threshold K_glass (def:iv-kglass, line 223) is an explicit numerical threshold on the tuple coordinates. The EM-Glass subtype (def:iv-em-glass, line 238) handles electromagnetic glass variants. Critically, CheckCrystal and CheckGlass (def:iv-check-crystal, def:iv-check-glass) are decidable procedures: given a configuration, one can algorithmically test whether it is crystal, glass, or neither. IV.P288 (prop:iv-glass-transition, line 252) treats the glass transition as a kinetic crossover between these rigorously defined regimes; prop:iv-decidable-phases (line 317) proves decidability of the classification. The result is a rigorous, algorithmic, first-principles treatment of a problem that has resisted such treatment for forty years.

## Result Statement

IV.P288 + ch62 definitions: Glass is a rigorous τ-regime (d₁≈0, d₄≈0) demarcated by the Glass Threshold K_glass; CheckGlass decidably tests membership. The glass transition is a kinetic crossover between first-principles-defined regimes.
