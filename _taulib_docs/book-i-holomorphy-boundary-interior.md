---
layout: taulib-doc
title: "TauLib.BookI.Holomorphy.BoundaryInterior"
permalink: /verify/taulib/docs/book-i-holomorphy-boundary-interior/
lane: verify
module_name: "TauLib.BookI.Holomorphy.BoundaryInterior"
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

# TauLib.Holomorphy.BoundaryInterior


The boundary-interior passage: boundary determines interior.

## Registry Cross-References


- [I.D68] Earned Interior Point — `EarnedInteriorPoint`

- [I.C02] Interior from Boundary — `interior_from_boundary`

- [I.P29] Passage to Book II — `passage_to_book_ii`


## Mathematical Content


The Global Hartogs Extension Theorem (I.T31) implies that
the boundary L = S¹ ∨ S¹ determines the interior of τ³.
Every interior point can be reconstructed from boundary data
via tower-coherent extension.

This chapter bridges Book I to Book II:
the Central Theorem O(τ³) ≅ A_spec(L) makes this determination precise.

## Book I Summary


Starting from:


- 5 generators: α, π, γ, η, ω

- 6+3 axioms: K1-K6 + diagonal discipline + solenoidality + finite saturation

- 1 operator: ρ (primorial reduction)


Through 60 chapters we earned:


- The τ-index set and program monoid (Part III-V)

- The ABCD chart and normal form (Part V)

- Prime polarity and the algebraic lemniscate (Part VI-VII)

- Internal set theory and boundary ring (Part VIII-IX)

- Characters and spectral decomposition (Part X)

- Four-valued logic (Part XI)

- Holomorphic transformers and the Identity Theorem (Part XII)

- The earned category and topos (Part XIII)

- Bi-monoidal structure (Part XIV)

- The Global Hartogs Extension Theorem (Part XV)


---

### `Tau.Holomorphy.EarnedInteriorPoint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L53-L63)
**structure
Tau.Holomorphy.EarnedInteriorPoint :Type**


[I.D68] An earned interior point: a value obtained by
extending boundary data via the Hartogs extension.
The extension is uniquely determined by tower coherence
and the Identity Theorem.

- boundary_fun : StageFun
- coherent : TowerCoherent self.boundary_fun
- value_at : Denotation.TauIdx → Denotation.TauIdx → Denotation.TauIdx
Instances For

---

### `Tau.Holomorphy.earned_id`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L65-L68)
**def
Tau.Holomorphy.earned_id :EarnedInteriorPoint**


An earned interior point from the identity StageFun.
Equations
- Tau.Holomorphy.earned_id = { boundary_fun := Tau.Holomorphy.id_stage, coherent := Tau.Holomorphy.id_coherent }
Instances For

---

### `Tau.Holomorphy.earned_interior_reduced`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L70-L73)
**theorem
Tau.Holomorphy.earned_interior_reduced
(p : EarnedInteriorPoint)

(n k : Denotation.TauIdx)
 :Polarity.reduce (p.boundary_fun.b_fun n k) k = p.boundary_fun.b_fun n k**


Interior values are self-consistent: output at stage k is reduced.

---

### `Tau.Holomorphy.interior_from_boundary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L79-L86)
**theorem
Tau.Holomorphy.interior_from_boundary
(f₁ f₂ : StageFun)

(hcoh1 : TowerCoherent f₁)

(hcoh2 : TowerCoherent f₂)

(d₀ : Denotation.TauIdx)

(hbdry : ∀ (n : Denotation.TauIdx), agree_at f₁ f₂ n d₀)

(n k : Denotation.TauIdx)
 :k ≤ d₀ → f₁.b_fun n k = f₂.b_fun n k**


[I.C02] Corollary: the interior is determined by the boundary.
Two tower-coherent functions with the same boundary data
(i.e., agreement at a reference depth) have the same interior values.

---

### `Tau.Holomorphy.interior_from_boundary_c`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L88-L93)
**theorem
Tau.Holomorphy.interior_from_boundary_c
(f₁ f₂ : StageFun)

(hcoh1 : TowerCoherent f₁)

(hcoh2 : TowerCoherent f₂)

(d₀ : Denotation.TauIdx)

(hbdry : ∀ (n : Denotation.TauIdx), agree_at f₁ f₂ n d₀)

(n k : Denotation.TauIdx)
 :k ≤ d₀ → f₁.c_fun n k = f₂.c_fun n k**


The interior-boundary principle for C-sector.

---

### `Tau.Holomorphy.BookIExport`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L99-L118)
**structure
Tau.Holomorphy.BookIExport :Type 1**


[I.P29] Passage to Book II: the earned import list.
Book I has earned all the tools needed for the Central Theorem.

The canonical data structure that Book II receives:

- category : Topos.CatTau
- topos : Topos.EarnedTopos
- hol_space : Type
- identity
(f₁ f₂ : StageFun)
 : TowerCoherent f₁ →
 TowerCoherent f₂ →
 ∀ (d₀ : Denotation.TauIdx),
 (∀ (n : Denotation.TauIdx), agree_at f₁ f₂ n d₀) → ∀ (n k : Denotation.TauIdx), k ≤ d₀ → agree_at f₁ f₂ n k
- classifier_four
(v : Logic.Omega_tau)
 : v = Logic.Truth4.T ∨ v = Logic.Truth4.F ∨ v = Logic.Truth4.B ∨ v = Logic.Truth4.N
Instances For

---

### `Tau.Holomorphy.book_i_export`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L120-L125)
**def
Tau.Holomorphy.book_i_export :BookIExport**


The canonical Book I export.
Equations
- Tau.Holomorphy.book_i_export = { category := Tau.Topos.cat_tau, topos := Tau.Topos.earned_topos, identity := Tau.Holomorphy.tau_identity_nat,
 classifier_four := Tau.Topos.omega_tau_classifier }
Instances For

---

### `Tau.Holomorphy.five_generators`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L131-L133)
**theorem
Tau.Holomorphy.five_generators :[Kernel.Generator.alpha, Kernel.Generator.pi, Kernel.Generator.gamma, Kernel.Generator.eta, Kernel.Generator.omega].length = 5**


Book I summary: 5 generators (α, π, γ, η, ω).

---

### `Tau.Holomorphy.monoid_assoc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L135-L140)
**theorem
Tau.Holomorphy.monoid_assoc
(f₁ f₂ f₃ : StageFun)
 :(f₁.comp f₂).comp f₃ = f₁.comp (f₂.comp f₃)**


Book I summary: the program monoid is associative.

---

### `Tau.Holomorphy.non_boolean`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L142-L144)
**theorem
Tau.Holomorphy.non_boolean :Logic.Truth4.B.impl Logic.Truth4.F ≠ Logic.Truth4.T**


Book I summary: the topos is non-Boolean.
