---
layout: taulib-doc
title: "TauLib.BookII.Closure.GeometricBiSquare"
permalink: /verify/taulib/docs/book-ii-closure-geometric-bi-square/
lane: verify
module_name: "TauLib.BookII.Closure.GeometricBiSquare"
book: "II"
book_label: "Holomorphy"
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
    book: "Book II"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookII.Closure.GeometricBiSquare


The Geometric Bi-Square: Book I's algebraic bi-square (I.T41)
filled with the geometric objects earned in Book II Parts I-IX.

## Registry Cross-References


- [II.D77] Geometric Bi-Square -- `GeometricBiSquareData`, `compute_geometric_bisquare`

- [II.T49] Geometric Bi-Square Theorem -- `geometric_bisquare_check`

- [II.R33] Algebraic-to-Geometric Audit -- `algebraic_geometric_audit`

- [II.R34] Scaling Chain Forward -- `ScalingLevel`, `scaling_chain_check`


## Mathematical Content


The algebraic bi-square (I.T41) is a pasted commuting diagram
on finite cyclic groups Z/M_kZ:


- Left square: tower coherence (reduce(f_l(n), k) = f_k(n))

- Right square: spectral naturality (chi_+/chi_- decomposition)

- Limit principle: agreement at one depth implies agreement below


Book II fills this algebraic skeleton with geometric content:


- Domain L becomes S^1 v S^1 via torus degeneration (II.T13)

- Interior tau^3 becomes Stone space (II.T07)

- Codomain becomes calibrated H_tau (II.D35)

- Spectral algebra becomes A_spec(L) (II.D60)

- Limit principle becomes Central Theorem (II.T40)


The Geometric Bi-Square Theorem (II.T49) asserts all eight components
are earned, all commuting squares are continuous, and the limit row
is precisely the Central Theorem.

---

### `Tau.BookII.Closure.GeometricBiSquareData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L52-L82)
**structure
Tau.BookII.Closure.GeometricBiSquareData :Type**


[II.D77] The Geometric Bi-Square: Book I's algebraic bi-square (I.T41)
annotated with boolean witnesses recording that each geometric
component has been earned in Book II.

Eight witnesses correspond to eight geometric "earnings":

- topology_earned: Stone space structure on tau^3 (II.T07)

- continuity_earned: Hol implies Continuous (II.T06)

- geometry_earned: Tarski axioms verified (II.T16-T20)

- torus_degeneration_earned: T^2 -> S^1 v S^1 (II.T13)

- calibration_earned: H_tau calibrated with pi, e, j (II.D35)

- spectral_algebra_earned: A_spec(L) ring structure (II.D60)

- central_theorem_earned: O(tau^3) = A_spec(L) (II.T40)

- hartogs_earned: Mutual determination (II.T27)


- topology_earned : Bool
Stone space structure on tau^3 (II.T07).

- continuity_earned : Bool
Hol implies Continuous (II.T06).

- geometry_earned : Bool
Tarski axioms verified (II.T16-T20).

- torus_degeneration_earned : Bool
T^2 -> S^1 v S^1 via pinch map (II.T13).

- calibration_earned : Bool
H_tau calibrated with pi, e, j (II.D35).

- spectral_algebra_earned : Bool
A_spec(L) ring/tower structure (II.D60).

- central_theorem_earned : Bool
Central Theorem O(tau^3) = A_spec(L) (II.T40).

- hartogs_earned : Bool
Mutual determination / Hartogs (II.T27).

Instances For

---

### `Tau.BookII.Closure.instReprGeometricBiSquareData.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L82-L82)
**def
Tau.BookII.Closure.instReprGeometricBiSquareData.repr :GeometricBiSquareData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.instReprGeometricBiSquareData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L82-L82)
**instance
Tau.BookII.Closure.instReprGeometricBiSquareData :Repr GeometricBiSquareData**

Equations
- Tau.BookII.Closure.instReprGeometricBiSquareData = { reprPrec := Tau.BookII.Closure.instReprGeometricBiSquareData.repr }

---

### `Tau.BookII.Closure.instDecidableEqGeometricBiSquareData.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L82-L82)
**def
Tau.BookII.Closure.instDecidableEqGeometricBiSquareData.decEq
(x✝ x✝¹ : GeometricBiSquareData)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.instDecidableEqGeometricBiSquareData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L82-L82)
**instance
Tau.BookII.Closure.instDecidableEqGeometricBiSquareData :DecidableEq GeometricBiSquareData**

Equations
- Tau.BookII.Closure.instDecidableEqGeometricBiSquareData = Tau.BookII.Closure.instDecidableEqGeometricBiSquareData.decEq

---

### `Tau.BookII.Closure.compute_geometric_bisquare`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L88-L101)
**def
Tau.BookII.Closure.compute_geometric_bisquare
(db bound : Denotation.TauIdx)
 :GeometricBiSquareData**


[II.D77] Compute the Geometric Bi-Square by evaluating all
eight geometric check functions from Book II.
Parameters db, bound control verification depth.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.geometric_bisquare_complete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L103-L112)
**def
Tau.BookII.Closure.geometric_bisquare_complete
(gbs : GeometricBiSquareData)
 :Bool**


[II.D77] Check that all eight components are earned.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.geometric_bisquare_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L118-L121)
**def
Tau.BookII.Closure.geometric_bisquare_check
(db bound : Denotation.TauIdx)
 :Bool**


[II.T49] The Geometric Bi-Square Theorem: compute and verify
that all eight geometric components are earned.
Equations
- Tau.BookII.Closure.geometric_bisquare_check db bound = Tau.BookII.Closure.geometric_bisquare_complete (Tau.BookII.Closure.compute_geometric_bisquare db bound)
Instances For

---

### `Tau.BookII.Closure.geometric_component_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L123-L132)
**def
Tau.BookII.Closure.geometric_component_count
(gbs : GeometricBiSquareData)
 :ℕ**


[II.T49] Count how many geometric components are verified (out of 8).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.algebraic_geometric_audit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L138-L144)
**def
Tau.BookII.Closure.algebraic_geometric_audit
(db bound k_max : Denotation.TauIdx)
 :Bool**


[II.R33] Algebraic-to-Geometric Audit: record which Book I
algebraic components have received geometric content in Book II.
The audit passes when all eight components are earned AND
the E1 export package is complete.
Equations
- Tau.BookII.Closure.algebraic_geometric_audit db bound k_max = (Tau.BookII.Closure.geometric_bisquare_check db bound && Tau.BookII.Closure.full_export_check db bound k_max)
Instances For

---

### `Tau.BookII.Closure.algebraic_core`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L150-L154)
**def
Tau.BookII.Closure.algebraic_core :Holomorphy.BookICrownJewel**


The algebraic core: the Book I crown jewel is always available
regardless of the geometric witnesses.
This is a definitional identity: the algebraic bi-square (I.T41)
exists independently of whether Book II's geometry is earned.
Equations
- Tau.BookII.Closure.algebraic_core = Tau.Holomorphy.book_i_crown_jewel
Instances For

---

### `Tau.BookII.Closure.compatibility_with_algebraic`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L156-L162)
**theorem
Tau.BookII.Closure.compatibility_with_algebraic
(f : Holomorphy.StageFun)
 :Holomorphy.TowerCoherent f ↔ (∀ (n k l : Denotation.TauIdx), k ≤ l → Polarity.reduce (f.b_fun n l) k = f.b_fun n k) ∧ ∀ (n k l : Denotation.TauIdx), k ≤ l → Polarity.reduce (f.c_fun n l) k = f.c_fun n k**


Compatibility: the algebraic bi-square characterization is
preserved. Forgetting geometry recovers I.T41.

---

### `Tau.BookII.Closure.geometric_preserves_limit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L164-L169)
**theorem
Tau.BookII.Closure.geometric_preserves_limit
(f₁ f₂ : Holomorphy.StageFun)

(h₁ : Holomorphy.TowerCoherent f₁)

(h₂ : Holomorphy.TowerCoherent f₂)

(d₀ : Denotation.TauIdx)

(h : ∀ (n : Denotation.TauIdx), Holomorphy.agree_at f₁ f₂ n d₀)

(n k : Denotation.TauIdx)
 :k ≤ d₀ → Holomorphy.agree_at f₁ f₂ n k**


Compatibility: the limit principle survives geometrization.

---

### `Tau.BookII.Closure.geometric_preserves_right_auto`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L171-L177)
**theorem
Tau.BookII.Closure.geometric_preserves_right_auto
(f : Holomorphy.StageFun)

(htc : Holomorphy.TowerCoherent f)

(n k l : Denotation.TauIdx)

(hkl : k ≤ l)
 :Holomorphy.spectral_of f n k = { b_coeff := Polarity.reduce (Holomorphy.spectral_of f n l).b_coeff k,
 c_coeff := Polarity.reduce (Holomorphy.spectral_of f n l).c_coeff k }**


Compatibility: right-square automaticity survives geometrization.

---

### `Tau.BookII.Closure.ScalingLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L183-L191)
**inductive
Tau.BookII.Closure.ScalingLevel :Type**


[II.R34] The three enrichment levels at which the bi-square lives.


- E0_algebraic: Book I (finite cyclic groups, no topology)

- E1_geometric: Book II (Stone space, continuity, torus degeneration)

- E2_enriched: Book III (spectral forces, preview only)


- E0_algebraic : ScalingLevel
- E1_geometric : ScalingLevel
- E2_enriched : ScalingLevel
Instances For

---

### `Tau.BookII.Closure.instReprScalingLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L191-L191)
**instance
Tau.BookII.Closure.instReprScalingLevel :Repr ScalingLevel**

Equations
- Tau.BookII.Closure.instReprScalingLevel = { reprPrec := Tau.BookII.Closure.instReprScalingLevel.repr }

---

### `Tau.BookII.Closure.instReprScalingLevel.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L191-L191)
**def
Tau.BookII.Closure.instReprScalingLevel.repr :ScalingLevel → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.instDecidableEqScalingLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L191-L191)
**instance
Tau.BookII.Closure.instDecidableEqScalingLevel :DecidableEq ScalingLevel**

Equations
- Tau.BookII.Closure.instDecidableEqScalingLevel x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookII.Closure.scaling_level_index`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L193-L198)
**def
Tau.BookII.Closure.scaling_level_index :ScalingLevel → ℕ**


[II.R34] The scaling chain: algebraic < geometric < enriched.
Each level adds geometric content to the bi-square.
Equations
- Tau.BookII.Closure.scaling_level_index Tau.BookII.Closure.ScalingLevel.E0_algebraic = 0
- Tau.BookII.Closure.scaling_level_index Tau.BookII.Closure.ScalingLevel.E1_geometric = 1
- Tau.BookII.Closure.scaling_level_index Tau.BookII.Closure.ScalingLevel.E2_enriched = 2
Instances For

---

### `Tau.BookII.Closure.scaling_chain_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L200-L203)
**def
Tau.BookII.Closure.scaling_chain_check :Bool**


[II.R34] Scaling chain monotonicity: E0 < E1 < E2.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.book2_scaling_level`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L205-L206)
**def
Tau.BookII.Closure.book2_scaling_level :ScalingLevel**


[II.R34] Book II lives at E1_geometric.
Equations
- Tau.BookII.Closure.book2_scaling_level = Tau.BookII.Closure.ScalingLevel.E1_geometric
Instances For

---

### `Tau.BookII.Closure.e2_not_yet_earned`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L208-L211)
**def
Tau.BookII.Closure.e2_not_yet_earned :Bool**


[II.R34] The geometric bi-square is the E1 avatar of the algebraic
bi-square. The E2 avatar (enriched bi-square) will be earned in Book III.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.geometric_bisquare_3_15`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L254-L255)
**theorem
Tau.BookII.Closure.geometric_bisquare_3_15 :geometric_bisquare_check 3 15 = true**


---

### `Tau.BookII.Closure.geometric_all_eight`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L258-L259)
**theorem
Tau.BookII.Closure.geometric_all_eight :geometric_component_count (compute_geometric_bisquare 3 15) = 8**


---

### `Tau.BookII.Closure.geo_topology`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L262-L263)
**theorem
Tau.BookII.Closure.geo_topology :(compute_geometric_bisquare 3 15).topology_earned = true**


---

### `Tau.BookII.Closure.geo_continuity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L265-L266)
**theorem
Tau.BookII.Closure.geo_continuity :(compute_geometric_bisquare 3 15).continuity_earned = true**


---

### `Tau.BookII.Closure.geo_geometry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L268-L269)
**theorem
Tau.BookII.Closure.geo_geometry :(compute_geometric_bisquare 3 15).geometry_earned = true**


---

### `Tau.BookII.Closure.geo_torus_degeneration`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L271-L272)
**theorem
Tau.BookII.Closure.geo_torus_degeneration :(compute_geometric_bisquare 3 15).torus_degeneration_earned = true**


---

### `Tau.BookII.Closure.geo_calibration`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L274-L275)
**theorem
Tau.BookII.Closure.geo_calibration :(compute_geometric_bisquare 3 15).calibration_earned = true**


---

### `Tau.BookII.Closure.geo_spectral_algebra`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L277-L278)
**theorem
Tau.BookII.Closure.geo_spectral_algebra :(compute_geometric_bisquare 3 15).spectral_algebra_earned = true**


---

### `Tau.BookII.Closure.geo_central_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L280-L281)
**theorem
Tau.BookII.Closure.geo_central_theorem :(compute_geometric_bisquare 3 15).central_theorem_earned = true**


---

### `Tau.BookII.Closure.geo_hartogs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L283-L284)
**theorem
Tau.BookII.Closure.geo_hartogs :(compute_geometric_bisquare 3 15).hartogs_earned = true**


---

### `Tau.BookII.Closure.audit_3_15_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L287-L288)
**theorem
Tau.BookII.Closure.audit_3_15_3 :algebraic_geometric_audit 3 15 3 = true**


---

### `Tau.BookII.Closure.scaling_chain_valid`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L291-L292)
**theorem
Tau.BookII.Closure.scaling_chain_valid :scaling_chain_check = true**


---

### `Tau.BookII.Closure.e2_not_earned`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L294-L295)
**theorem
Tau.BookII.Closure.e2_not_earned :e2_not_yet_earned = true**


---

### `Tau.BookII.Closure.complete_means_eight`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L301-L318)
**theorem
Tau.BookII.Closure.complete_means_eight
(gbs : GeometricBiSquareData)
 :geometric_bisquare_complete gbs = true → geometric_component_count gbs = 8**


[II.T49] A complete geometric bi-square has all 8 components.
This is the structural statement that completeness implies count = 8.

---

### `Tau.BookII.Closure.geometric_implies_central`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L320-L329)
**theorem
Tau.BookII.Closure.geometric_implies_central
(db bound : Denotation.TauIdx)
 :geometric_bisquare_check db bound = true → CentralTheorem.central_theorem_check db bound = true**


[II.T49] The geometric bi-square implies the Central Theorem is earned.
If the full check passes, the central_theorem_earned field is true.

---

### `Tau.BookII.Closure.e0_ne_e1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L331-L333)
**theorem
Tau.BookII.Closure.e0_ne_e1 :ScalingLevel.E0_algebraic ≠ ScalingLevel.E1_geometric**


[II.R34] E0 and E1 are distinct scaling levels.

---

### `Tau.BookII.Closure.e1_ne_e2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/GeometricBiSquare.lean#L335-L337)
**theorem
Tau.BookII.Closure.e1_ne_e2 :ScalingLevel.E1_geometric ≠ ScalingLevel.E2_enriched**


[II.R34] E1 and E2 are distinct scaling levels.
