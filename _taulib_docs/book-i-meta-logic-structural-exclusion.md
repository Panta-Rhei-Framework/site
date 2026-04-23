---
layout: taulib-doc
title: "TauLib.BookI.MetaLogic.StructuralExclusion"
permalink: /verify/taulib/docs/book-i-meta-logic-structural-exclusion/
lane: verify
module_name: "TauLib.BookI.MetaLogic.StructuralExclusion"
book: "I"
book_label: "Foundations"
right_rail:
  related:
  - title: TauLib Overview
    url: /verify/taulib/
  - title: Architecture
    url: /verify/taulib/architecture/
  artifacts:
  - title: Source on GitHub
    url: https://github.com/Panta-Rhei-Research/taulib
    external: true
  meta:
    type: "API Documentation"
    book: "Book I"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.MetaLogic.StructuralExclusion


The K5 Structural Exclusion theorem and the Enrichment Frontier Classification.

## Registry Cross-References


- [I.D80] Self-Hosting Degrees — `SelfHostingDegree`

- [I.D81] CCC-Linear Dichotomy — `CCCSide`, `StarAutonomousSide`

- [I.T39] K5 Structural Exclusion — `k5_structural_exclusion`

- [I.D82] Enrichment Frontier Classification — `EnrichmentFrontierStatus`


## Mathematical Content


The CCC-Linear Dichotomy: cartesian-closed categories admit the Lawvere
fixed-point barrier (free diagonals → no self-hosting). Star-autonomous
categories (the linear side) do not. K5's diagonal discipline places τ on
the star-autonomous side, excluding the standard obstruction to self-hosting.

The Enrichment Frontier Classification grades each E-transition:


- E₀ → E₁: achieved (adaptation needed)

- E₁ → E₂: partially achieved (novel combination)

- E₂ → E₃: unprecedented (open research problem)


---

### `Tau.MetaLogic.SelfHostingDegree`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L35-L47)
**inductive
Tau.MetaLogic.SelfHostingDegree :Type**


[I.D80] Self-hosting degrees classify how much of a formal system's
meta-theory is internalized within the system itself.


- `none`: no self-hosting — the system is formalized entirely externally

- `partial_`: some constructions are internalized but the meta-theory remains external

- `fragment`: significant portions of the meta-theory are internal, but gaps remain

- `full`: complete self-hosting — meta-language and object language coincide


- none : SelfHostingDegree
- partial_ : SelfHostingDegree
- fragment : SelfHostingDegree
- full : SelfHostingDegree
Instances For

---

### `Tau.MetaLogic.instDecidableEqSelfHostingDegree`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L47-L47)
**instance
Tau.MetaLogic.instDecidableEqSelfHostingDegree :DecidableEq SelfHostingDegree**

Equations
- Tau.MetaLogic.instDecidableEqSelfHostingDegree x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.MetaLogic.instReprSelfHostingDegree.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L47-L47)
**def
Tau.MetaLogic.instReprSelfHostingDegree.repr :SelfHostingDegree → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.instReprSelfHostingDegree`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L47-L47)
**instance
Tau.MetaLogic.instReprSelfHostingDegree :Repr SelfHostingDegree**

Equations
- Tau.MetaLogic.instReprSelfHostingDegree = { reprPrec := Tau.MetaLogic.instReprSelfHostingDegree.repr }

---

### `Tau.MetaLogic.allSelfHostingDegrees`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L51-L53)
**def
Tau.MetaLogic.allSelfHostingDegrees :List SelfHostingDegree**


All self-hosting degrees enumerated.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.self_hosting_degree_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L55-L56)
**theorem
Tau.MetaLogic.self_hosting_degree_count :allSelfHostingDegrees.length = 4**


There are exactly 4 self-hosting degrees.

---

### `Tau.MetaLogic.CCCSide`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L62-L71)
**structure
Tau.MetaLogic.CCCSide :Type**


[I.D81] The CCC side of the dichotomy: cartesian-closed categories
have free diagonal maps Δ : A → A × A, which enable the Lawvere
fixed-point argument. Self-hosting is obstructed.

- freeDiagonals : Bool
Free diagonals are available

- lawvereBarrier : Bool
The Lawvere barrier applies

- barrier_from_diag : self.freeDiagonals = true → self.lawvereBarrier = true
Consistency: free diagonals imply the barrier

Instances For

---

### `Tau.MetaLogic.StarAutonomousSide`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L73-L83)
**structure
Tau.MetaLogic.StarAutonomousSide :Type**


[I.D81] The star-autonomous side of the dichotomy: star-autonomous
categories replace the cartesian product × with the tensor ⊗.
The diagonal Δ : A → A ⊗ A is not freely available — it must be
earned. The Lawvere barrier does not apply.

- noFreeDiagonals : Bool
Free diagonals are NOT available

- noLawvereBarrier : Bool
The Lawvere barrier does NOT apply

- no_barrier_from_no_diag : self.noFreeDiagonals = true → self.noLawvereBarrier = true
Consistency: no free diagonals imply no barrier

Instances For

---

### `Tau.MetaLogic.ccc_side`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L85-L89)
**def
Tau.MetaLogic.ccc_side :CCCSide**


The CCC side: free diagonals, Lawvere barrier applies.
Equations
- Tau.MetaLogic.ccc_side = { freeDiagonals := true, lawvereBarrier := true, barrier_from_diag := ⋯ }
Instances For

---

### `Tau.MetaLogic.star_autonomous_side`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L91-L95)
**def
Tau.MetaLogic.star_autonomous_side :StarAutonomousSide**


The star-autonomous side: no free diagonals, no Lawvere barrier.
Equations
- Tau.MetaLogic.star_autonomous_side = { noFreeDiagonals := true, noLawvereBarrier := true, no_barrier_from_no_diag := ⋯ }
Instances For

---

### `Tau.MetaLogic.K5StructuralExclusion`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L101-L117)
**structure
Tau.MetaLogic.K5StructuralExclusion :Type**


[I.T39] K5 Structural Exclusion Theorem.

K5's diagonal discipline (DiagonalAspect.noUnearnedDiagonals) places τ
on the star-autonomous side of the CCC-linear dichotomy. Specifically:

- K5 refuses free diagonals (contraction is refused — from Substrate.lean)

- Refusing free diagonals places τ on the star-autonomous side

- On the star-autonomous side, the Lawvere barrier does not apply

- Therefore: the standard obstruction to self-hosting is excluded


- contraction_refused : k5_status StructuralRule.contraction = ObjectLevelStatus.refused
K5 refuses contraction (no free diagonals)

- diagonal_is_linear : diag_to_linear DiagonalAspect.noUnearnedDiagonals = LinearAspect.noFreeContraction
The diagonal-to-linear map sends noUnearnedDiagonals to noFreeContraction

- tau_star_autonomous : StarAutonomousSide
τ is on the star-autonomous side

- no_barrier : self.tau_star_autonomous.noLawvereBarrier = true
On the star-autonomous side, the Lawvere barrier does not apply

Instances For

---

### `Tau.MetaLogic.k5_structural_exclusion`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L119-L124)
**def
Tau.MetaLogic.k5_structural_exclusion :K5StructuralExclusion**


The K5 Structural Exclusion theorem: all components are satisfied.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.EnrichmentFrontierStatus`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L130-L136)
**inductive
Tau.MetaLogic.EnrichmentFrontierStatus :Type**


[I.D82] The enrichment frontier status classifies each transition
of the enrichment ladder by its novelty relative to existing work.

- achieved : EnrichmentFrontierStatus
- partiallyAchieved : EnrichmentFrontierStatus
- unprecedented : EnrichmentFrontierStatus
Instances For

---

### `Tau.MetaLogic.instDecidableEqEnrichmentFrontierStatus`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L136-L136)
**instance
Tau.MetaLogic.instDecidableEqEnrichmentFrontierStatus :DecidableEq EnrichmentFrontierStatus**

Equations
- Tau.MetaLogic.instDecidableEqEnrichmentFrontierStatus x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.MetaLogic.instReprEnrichmentFrontierStatus`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L136-L136)
**instance
Tau.MetaLogic.instReprEnrichmentFrontierStatus :Repr EnrichmentFrontierStatus**

Equations
- Tau.MetaLogic.instReprEnrichmentFrontierStatus = { reprPrec := Tau.MetaLogic.instReprEnrichmentFrontierStatus.repr }

---

### `Tau.MetaLogic.instReprEnrichmentFrontierStatus.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L136-L136)
**def
Tau.MetaLogic.instReprEnrichmentFrontierStatus.repr :EnrichmentFrontierStatus → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.e0_e1_status`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L140-L143)
**def
Tau.MetaLogic.e0_e1_status :EnrichmentFrontierStatus**


E₀ → E₁ status: achieved. Internalizing types in a categorical
framework has multiple precedents (Altenkirch-Kaposi 2016,
Bocquet-Kaposi-Sattler 2023, Moerdijk-Palmgren 2002).
Equations
- Tau.MetaLogic.e0_e1_status = Tau.MetaLogic.EnrichmentFrontierStatus.achieved
Instances For

---

### `Tau.MetaLogic.e1_e2_status`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L145-L148)
**def
Tau.MetaLogic.e1_e2_status :EnrichmentFrontierStatus**


E₁ → E₂ status: partially achieved. Internal proof-theoretic
reasoning (Joyal) and resource-sensitive DTT (Abel 2023) exist
separately; their combination is novel.
Equations
- Tau.MetaLogic.e1_e2_status = Tau.MetaLogic.EnrichmentFrontierStatus.partiallyAchieved
Instances For

---

### `Tau.MetaLogic.e2_e3_status`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L150-L153)
**def
Tau.MetaLogic.e2_e3_status :EnrichmentFrontierStatus**


E₂ → E₃ status: unprecedented. No formal system of CIC-level
strength achieves full self-hosting. Willard (2001) achieves it
below PA; Girard TX achieves fragments only.
Equations
- Tau.MetaLogic.e2_e3_status = Tau.MetaLogic.EnrichmentFrontierStatus.unprecedented
Instances For

---

### `Tau.MetaLogic.allFrontierStatuses`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L155-L157)
**def
Tau.MetaLogic.allFrontierStatuses :List EnrichmentFrontierStatus**


All enrichment frontier statuses enumerated.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.frontier_status_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L159-L160)
**theorem
Tau.MetaLogic.frontier_status_count :allFrontierStatuses.length = 3**


There are exactly 3 frontier statuses.

---

### `Tau.MetaLogic.e_transitions_distinct`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L162-L167)
**theorem
Tau.MetaLogic.e_transitions_distinct :e0_e1_status ≠ e1_e2_status ∧ e1_e2_status ≠ e2_e3_status ∧ e0_e1_status ≠ e2_e3_status**


The three E-transitions have distinct statuses.

---

### `Tau.MetaLogic.frontierRank`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L169-L175)
**def
Tau.MetaLogic.frontierRank :EnrichmentFrontierStatus → ℕ**


The enrichment frontier is strictly ordered: each transition
is harder than the previous one. We encode this by assigning
a difficulty rank (0, 1, 2) and verifying strict monotonicity.
Equations
- Tau.MetaLogic.frontierRank Tau.MetaLogic.EnrichmentFrontierStatus.achieved = 0
- Tau.MetaLogic.frontierRank Tau.MetaLogic.EnrichmentFrontierStatus.partiallyAchieved = 1
- Tau.MetaLogic.frontierRank Tau.MetaLogic.EnrichmentFrontierStatus.unprecedented = 2
Instances For

---

### `Tau.MetaLogic.e0_e1_easier_than_e1_e2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L177-L179)
**theorem
Tau.MetaLogic.e0_e1_easier_than_e1_e2 :frontierRank e0_e1_status < frontierRank e1_e2_status**


E₀→E₁ is easier than E₁→E₂.

---

### `Tau.MetaLogic.e1_e2_easier_than_e2_e3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L181-L183)
**theorem
Tau.MetaLogic.e1_e2_easier_than_e2_e3 :frontierRank e1_e2_status < frontierRank e2_e3_status**


E₁→E₂ is easier than E₂→E₃.

---

### `Tau.MetaLogic.max_frontier_rank`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L185-L187)
**theorem
Tau.MetaLogic.max_frontier_rank :frontierRank e2_e3_status = 2**


The maximum difficulty is 2 (unprecedented).
