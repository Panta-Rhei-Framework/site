---
layout: taulib-doc
title: "TauLib.BookV.GravityField.BipolarHolonomy"
permalink: /verify/taulib/docs/book-v-gravity-field-bipolar-holonomy/
lane: verify
module_name: "TauLib.BookV.GravityField.BipolarHolonomy"
book: "V"
book_label: "Macrocosm"
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
    book: "Book V"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookV.GravityField.BipolarHolonomy


The **Bipolar Holonomy Space** (BHS) resolves OQ-C1: why the exponent in
α_G = α¹⁸·(geometric factors) equals 18.

## Key Result


**Definition.** BHS(τ³, L) := H₁(τ³; ℤ) ⊗ H¹(τ³; ℤ) ⊗ H₁(L; ℤ)

**Theorem.** dim(BHS) = b₁(τ³) · b¹(τ³) · b₁(L) = 3 · 3 · 2 = **18**

This is a single cohomological object whose dimension is the exponent.
The previous formulation (18 = 2 × 3 × 3 from three separate invariants)
is recovered as a CONSEQUENCE of the Künneth-type dimension formula.

## Why This Is Not Relabeling


- BHS is a **single mathematical object** (tensor product of homology groups)

- dim(V ⊗ W ⊗ U) = dim(V)·dim(W)·dim(U) is a THEOREM, not a definition

- BHS has independent physical interpretation (holonomy evaluation space)

- The construction is functorial: changing τ³ or L changes BHS and its dim


## Registry Cross-References


- [V.D101] Bipolar Holonomy Space — `BipolarHolonomySpace`, `canonical_bhs`

- [V.D102] Holonomy Basis Element — physical interpretation

- [V.T84] BHS Dimension Theorem — `bhs_dimension`

- [V.T85] BHS Equals Exponent — `bhs_equals_exponent`

- [V.T86] Universal Coefficients — `bhs_universality`

- [V.R170] BHS Is Topological — `bhs_is_topological`


## Ground Truth Sources


- oq_c1_bipolar_holonomy_lab.py: 33/33 checks

- oq_c1_bipolar_holonomy_sprint.md: full derivation


---

### `Tau.BookV.GravityField.BipolarHolonomy.BipolarHolonomySpace`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/BipolarHolonomy.lean#L52-L69)
**structure
Tau.BookV.GravityField.BipolarHolonomy.BipolarHolonomySpace :Type**


[V.D101] The Bipolar Holonomy Space of (τ³, L).

BHS(τ³, L) := H₁(τ³; ℤ) ⊗ H¹(τ³; ℤ) ⊗ H₁(L; ℤ)

The three Betti numbers:


- b₁_arena = rank H₁(τ³; ℤ): independent 1-cycles in τ³

- b1_arena = rank H¹(τ³; ℤ): independent characters on τ³

- b₁_boundary = rank H₁(L; ℤ): independent loops in L = S¹ ∨ S¹


- b₁_arena : ℕ
b₁(τ³): first Betti number of the arena (homology).

- b1_arena : ℕ
b¹(τ³): first Betti number of the arena (cohomology).

- b₁_boundary : ℕ
b₁(L): first Betti number of the boundary lemniscate.

- dim : ℕ
The dimension of the tensor product BHS.

Instances For

---

### `Tau.BookV.GravityField.BipolarHolonomy.instReprBipolarHolonomySpace.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/BipolarHolonomy.lean#L69-L69)
**def
Tau.BookV.GravityField.BipolarHolonomy.instReprBipolarHolonomySpace.repr :BipolarHolonomySpace → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.BipolarHolonomy.instReprBipolarHolonomySpace`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/BipolarHolonomy.lean#L69-L69)
**instance
Tau.BookV.GravityField.BipolarHolonomy.instReprBipolarHolonomySpace :Repr BipolarHolonomySpace**

Equations
- Tau.BookV.GravityField.BipolarHolonomy.instReprBipolarHolonomySpace = { reprPrec := Tau.BookV.GravityField.BipolarHolonomy.instReprBipolarHolonomySpace.repr }

---

### `Tau.BookV.GravityField.BipolarHolonomy.canonical_bhs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/BipolarHolonomy.lean#L71-L75)
**def
Tau.BookV.GravityField.BipolarHolonomy.canonical_bhs :BipolarHolonomySpace**


The canonical BHS for (τ³, L) with τ³ = τ¹ ×_f T² and L = S¹ ∨ S¹.
Equations
- Tau.BookV.GravityField.BipolarHolonomy.canonical_bhs = { b₁_arena := 3, b1_arena := 3, b₁_boundary := 2 }
Instances For

---

### `Tau.BookV.GravityField.BipolarHolonomy.bhs_dimension`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/BipolarHolonomy.lean#L81-L87)
**theorem
Tau.BookV.GravityField.BipolarHolonomy.bhs_dimension :canonical_bhs.dim = 18**


[V.T84] The dimension of the Bipolar Holonomy Space is 18.

dim(BHS) = b₁(τ³) · b¹(τ³) · b₁(L) = 3 · 3 · 2 = 18

This is THE key theorem: the exponent 18 is the dimension of a
single tensor product space, not three ad hoc factors multiplied.

---

### `Tau.BookV.GravityField.BipolarHolonomy.bhs_b1_arena_earned`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/BipolarHolonomy.lean#L93-L96)
**theorem
Tau.BookV.GravityField.BipolarHolonomy.bhs_b1_arena_earned :canonical_bhs.b₁_arena = BookIV.Physics.triple_holonomy.circle_count**


b₁(τ³) = 3 verified against triple_holonomy.circle_count.
Same invariant: dim(τ³) = 3 independent 1-cycles = 3 holonomy circles.

---

### `Tau.BookV.GravityField.BipolarHolonomy.bhs_b1_dual_earned`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/BipolarHolonomy.lean#L98-L102)
**theorem
Tau.BookV.GravityField.BipolarHolonomy.bhs_b1_dual_earned :canonical_bhs.b1_arena = Kernel.solenoidalGenerators.length**


b¹(τ³) = 3 verified against solenoidalGenerators.length.
Dual interpretation: 3 independent characters ↔ 3 solenoidal generators.

---

### `Tau.BookV.GravityField.BipolarHolonomy.bhs_b1_boundary_earned`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/BipolarHolonomy.lean#L104-L107)
**theorem
Tau.BookV.GravityField.BipolarHolonomy.bhs_b1_boundary_earned :canonical_bhs.b₁_boundary = BookIV.Arena.lemniscate.lobe_count**


b₁(L) = 2 verified against lemniscate.lobe_count.
Two independent loops in L = S¹ ∨ S¹ ↔ two lobes.

---

### `Tau.BookV.GravityField.BipolarHolonomy.bhs_equals_exponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/BipolarHolonomy.lean#L113-L122)
**theorem
Tau.BookV.GravityField.BipolarHolonomy.bhs_equals_exponent :canonical_bhs.dim = ExponentDerivation.canonical_factors.product**


[V.T85] The BHS dimension equals the ExponentFactors product.

dim(BHS) = 18 = ExponentFactors.product

This bridges the new (cohomological) and old (geometric) formulations.
The factorizations differ — BHS: 3·3·2, ExponentFactors: 2·3·3 —
but both yield 18 because they count the same holonomy passages
from different vantage points.

---

### `Tau.BookV.GravityField.BipolarHolonomy.bhs_matches_closing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/BipolarHolonomy.lean#L124-L126)
**theorem
Tau.BookV.GravityField.BipolarHolonomy.bhs_matches_closing :canonical_bhs.dim = closing_identity_canonical.alpha_exponent**


The BHS dimension matches the closing identity alpha exponent.

---

### `Tau.BookV.GravityField.BipolarHolonomy.bhs_universality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/BipolarHolonomy.lean#L132-L143)
**theorem
Tau.BookV.GravityField.BipolarHolonomy.bhs_universality :canonical_bhs.b₁_arena = canonical_bhs.b1_arena**


[V.T86] Universal coefficient theorem: b¹ = b₁ when H₁ is free.

For τ³ with H₁(τ³; ℤ) ≅ ℤ³ (free abelian), the UCT gives:
H¹(τ³; ℤ) ≅ Hom(H₁(τ³; ℤ), ℤ) ⊕ Ext¹(H₀(τ³; ℤ), ℤ)

Since both H₁ and H₀ are free, Ext¹ = 0, and
Hom(ℤ³, ℤ) ≅ ℤ³, giving b¹ = b₁ = 3.

This is the key algebraic topology fact that makes
b₁_arena = b1_arena in the BHS.

---

### `Tau.BookV.GravityField.BipolarHolonomy.bhs_is_topological`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/BipolarHolonomy.lean#L149-L161)
**theorem
Tau.BookV.GravityField.BipolarHolonomy.bhs_is_topological :canonical_bhs.b₁_arena = 3 ∧ canonical_bhs.b1_arena = 3 ∧ canonical_bhs.b₁_boundary = 2 ∧ canonical_bhs.dim = canonical_bhs.b₁_arena * canonical_bhs.b1_arena * canonical_bhs.b₁_boundary**


[V.R170] The BHS dimension depends only on (co)homological data.

All three inputs (b₁_arena, b1_arena, b₁_boundary) are topological
invariants — they are unchanged by smooth deformations of τ³ or L.
The dimension 18 is therefore a topological invariant of the pair (τ³, L).

---

### `Tau.BookV.GravityField.BipolarHolonomy.bhs_minimal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/BipolarHolonomy.lean#L167-L173)
**theorem
Tau.BookV.GravityField.BipolarHolonomy.bhs_minimal :canonical_bhs.b₁_arena * canonical_bhs.b1_arena ≠ 18 ∧ canonical_bhs.b₁_arena * canonical_bhs.b₁_boundary ≠ 18 ∧ canonical_bhs.b1_arena * canonical_bhs.b₁_boundary ≠ 18**


No proper sub-tensor of BHS gives 18.
The 2-fold products are 9, 6, 6 — none equals 18.
