---
layout: taulib-doc
title: "TauLib.BookII.Hartogs.CategoryStructure"
permalink: /verify/taulib/docs/book-ii-hartogs-category-structure/
lane: verify
module_name: "TauLib.BookII.Hartogs.CategoryStructure"
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

# TauLib.BookII.Hartogs.CategoryStructure


Category structure of holomorphic endomorphisms on the primorial tower.

## Registry Cross-References


- [II.D39] Holomorphic Composition -- `hol_comp`, `hol_comp_sf`

- [II.D40] Holomorphic Identity -- `hol_id`, `hol_id_sf`

- [II.T29] Associativity -- `hol_assoc_check`, `hol_assoc_thm`

- [II.D41] Endomorphism Category HolEnd_tau -- `HolEndCat`, `holend_axioms_check`


## Mathematical Content


The holomorphic endomorphisms on the primorial tower form a category HolEnd_tau:

**Objects:** Stages k in N (each stage is a finite cyclic group Z/M_k Z).

**Morphisms:** Tower-coherent maps f : Z/M_k Z -> Z/M_k Z satisfying
reduce(f(x), j) = f(reduce(x, j)) for all j <= k.
At the TauIdx level: f(n, k) = reduce(f(n, k), k).

**Composition (II.D39):** Given f, g : TauIdx -> TauIdx -> TauIdx,
(f . g)(n, k) = f(g(n, k), k).
This preserves tower coherence because both f and g are reduce-compatible.

**Identity (II.D40):** id(n, k) = reduce(n, k).
This is tower-coherent by reduction_compat.

**Associativity (II.T29):** (f . (g . h))(n, k) = ((f . g) . h)(n, k)
holds definitionally by function application associativity.

**Unit laws:** f . id = f and id . f = f
hold when f is reduce-normalized (f(n, k) = f(reduce(n, k), k)).

The category HolEnd_tau is the endomorphism category of the primorial
inverse system, capturing all holomorphic self-maps of the tower.

---

### `Tau.BookII.Hartogs.hol_comp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L51-L61)
**def
Tau.BookII.Hartogs.hol_comp
(f g : Denotation.TauIdx → Denotation.TauIdx → Denotation.TauIdx)

(n k : Denotation.TauIdx)
 :Denotation.TauIdx**


[II.D39] Holomorphic composition at the TauIdx level.
Given two tower-coherent endomorphisms f, g on the primorial tower,
their composition applies g first, then f, at each stage k.

(f . g)(n, k) = f(g(n, k), k)

This is the pointwise composition of stage-k maps, which preserves
tower coherence because both f and g are reduce-compatible.
Equations
- Tau.BookII.Hartogs.hol_comp f g n k = f (g n k) k
Instances For

---

### `Tau.BookII.Hartogs.hol_comp_sf`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L63-L68)
**def
Tau.BookII.Hartogs.hol_comp_sf
(f g : Holomorphy.StageFun)
 :Holomorphy.StageFun**


[II.D39] Composition for StageFun pairs (bipolar composition):
B-sector and C-sector compose independently.
(f . g).b_fun(n, k) = f.b_fun(g.b_fun(n, k), k)
(f . g).c_fun(n, k) = f.c_fun(g.c_fun(n, k), k)
Equations
- Tau.BookII.Hartogs.hol_comp_sf f g = f.comp g
Instances For

---

### `Tau.BookII.Hartogs.hol_id`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L74-L80)
**def
Tau.BookII.Hartogs.hol_id
(n k : Denotation.TauIdx)
 :Denotation.TauIdx**


[II.D40] The identity holomorphic endomorphism.
id(n, k) = reduce(n, k): the canonical projection to Z/M_k Z.

This is the identity morphism in HolEnd_tau. It is tower-coherent
by reduction_compat: reduce(reduce(n, l), k) = reduce(n, k).
Equations
- Tau.BookII.Hartogs.hol_id n k = Tau.Polarity.reduce n k
Instances For

---

### `Tau.BookII.Hartogs.hol_id_sf`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L82-L84)
**def
Tau.BookII.Hartogs.hol_id_sf :Holomorphy.StageFun**


[II.D40] The identity StageFun: both sectors use reduce.
Equations
- Tau.BookII.Hartogs.hol_id_sf = Tau.Holomorphy.id_stage
Instances For

---

### `Tau.BookII.Hartogs.hol_sq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L90-L94)
**def
Tau.BookII.Hartogs.hol_sq
(n k : Denotation.TauIdx)
 :Denotation.TauIdx**


The squaring endomorphism: sq(n, k) = (n * n) % M_k.
Tower-coherent because reduce((n*n) mod M_l, k)
= (n*n) mod M_k = reduce(n*n, k) by Nat.mod_mod.
Equations
- Tau.BookII.Hartogs.hol_sq n k = Tau.Polarity.reduce (n * n) k
Instances For

---

### `Tau.BookII.Hartogs.hol_dbl`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L96-L99)
**def
Tau.BookII.Hartogs.hol_dbl
(n k : Denotation.TauIdx)
 :Denotation.TauIdx**


The doubling endomorphism: dbl(n, k) = (2 * n) % M_k.
Tower-coherent similarly.
Equations
- Tau.BookII.Hartogs.hol_dbl n k = Tau.Polarity.reduce (2 * n) k
Instances For

---

### `Tau.BookII.Hartogs.hol_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L101-L103)
**def
Tau.BookII.Hartogs.hol_zero
(_n _k : Denotation.TauIdx)
 :Denotation.TauIdx**


The constant-zero endomorphism: zero(n, k) = 0.
Trivially tower-coherent.
Equations
- Tau.BookII.Hartogs.hol_zero _n _k = 0
Instances For

---

### `Tau.BookII.Hartogs.hol_assoc_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L109-L130)
**def
Tau.BookII.Hartogs.hol_assoc_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T29] Associativity check for holomorphic composition.
For sample endomorphisms f, g, h, verify:
hol_comp f (hol_comp g h) n k = hol_comp (hol_comp f g) h n k

This holds definitionally because:
LHS = f(g(h(n, k), k), k)
RHS = f(g(h(n, k), k), k)
which are identical by function application.
Equations
- Tau.BookII.Hartogs.hol_assoc_check bound db = Tau.BookII.Hartogs.hol_assoc_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.hol_assoc_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L120-L129)@[irreducible]

**def
Tau.BookII.Hartogs.hol_assoc_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.hol_assoc_triple_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L132-L146)
**def
Tau.BookII.Hartogs.hol_assoc_triple_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T29] Associativity for a triple of concrete endomorphisms:
(sq . dbl) . id = sq . (dbl . id)
Equations
- Tau.BookII.Hartogs.hol_assoc_triple_check bound db = Tau.BookII.Hartogs.hol_assoc_triple_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.hol_assoc_triple_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L137-L145)@[irreducible]

**def
Tau.BookII.Hartogs.hol_assoc_triple_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.hol_assoc_exhaustive_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L148-L199)
**def
Tau.BookII.Hartogs.hol_assoc_exhaustive_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T29] Associativity for ALL triples from {id, sq, dbl, zero}.
Tests all 4^3 = 64 triples on [2, bound] x [1, db].
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.hol_assoc_exhaustive_check.go_f`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L154-L163)@[irreducible]

**def
Tau.BookII.Hartogs.hol_assoc_exhaustive_check.go_f
(fs gs hs : List (Denotation.TauIdx → Denotation.TauIdx → Denotation.TauIdx))

(x k bound db fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
- Tau.BookII.Hartogs.hol_assoc_exhaustive_check.go_f [] gs hs x k bound db fuel = if fuel = 0 then true else true
Instances For

---

### `Tau.BookII.Hartogs.hol_assoc_exhaustive_check.go_g`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L165-L175)@[irreducible]

**def
Tau.BookII.Hartogs.hol_assoc_exhaustive_check.go_g
(f : Denotation.TauIdx → Denotation.TauIdx → Denotation.TauIdx)

(gs hs : List (Denotation.TauIdx → Denotation.TauIdx → Denotation.TauIdx))

(x k bound db fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
- Tau.BookII.Hartogs.hol_assoc_exhaustive_check.go_g f [] hs x k bound db fuel = if fuel = 0 then true else true
Instances For

---

### `Tau.BookII.Hartogs.hol_assoc_exhaustive_check.go_h`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L177-L187)@[irreducible]

**def
Tau.BookII.Hartogs.hol_assoc_exhaustive_check.go_h
(f g : Denotation.TauIdx → Denotation.TauIdx → Denotation.TauIdx)

(hs : List (Denotation.TauIdx → Denotation.TauIdx → Denotation.TauIdx))

(x k bound db fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
- Tau.BookII.Hartogs.hol_assoc_exhaustive_check.go_h f g [] x k bound db fuel = if fuel = 0 then true else true
Instances For

---

### `Tau.BookII.Hartogs.hol_assoc_exhaustive_check.verify`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L189-L198)@[irreducible]

**def
Tau.BookII.Hartogs.hol_assoc_exhaustive_check.verify
(f g h : Denotation.TauIdx → Denotation.TauIdx → Denotation.TauIdx)

(x k bound db fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.hol_assoc_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L205-L213)
**theorem
Tau.BookII.Hartogs.hol_assoc_thm
(f g h : Denotation.TauIdx → Denotation.TauIdx → Denotation.TauIdx)

(n k : Denotation.TauIdx)
 :hol_comp f (hol_comp g h) n k = hol_comp (hol_comp f g) h n k**


[II.T29] Associativity theorem (formal):
Holomorphic composition is associative by definition.
hol_comp f (hol_comp g h) n k = hol_comp (hol_comp f g) h n k

This is an immediate consequence of the definition:
both sides expand to f(g(h(n, k), k), k).

---

### `Tau.BookII.Hartogs.right_unit_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L219-L236)
**def
Tau.BookII.Hartogs.right_unit_check
(bound db : Denotation.TauIdx)
 :Bool**


Right unit check: for reduce-normalized f, f . id = f.
f(reduce(n, k), k) = f(n, k) when f depends only on n mod M_k.
Equations
- Tau.BookII.Hartogs.right_unit_check bound db = Tau.BookII.Hartogs.right_unit_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.right_unit_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L224-L235)@[irreducible]

**def
Tau.BookII.Hartogs.right_unit_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.left_unit_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L238-L254)
**def
Tau.BookII.Hartogs.left_unit_check
(bound db : Denotation.TauIdx)
 :Bool**


Left unit check: id . f = f for reduce-normalized f.
id(f(n, k), k) = reduce(f(n, k), k) = f(n, k)
when f(n, k) is already reduced at stage k.
Equations
- Tau.BookII.Hartogs.left_unit_check bound db = Tau.BookII.Hartogs.left_unit_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.left_unit_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L244-L253)@[irreducible]

**def
Tau.BookII.Hartogs.left_unit_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.left_unit_id_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L256-L262)
**theorem
Tau.BookII.Hartogs.left_unit_id_thm
(n k : Denotation.TauIdx)
 :hol_comp hol_id hol_id n k = hol_id n k**


Left unit theorem (formal): hol_id composed with any reduce-based
endomorphism is idempotent.
hol_comp hol_id hol_id n k = hol_id n k

---

### `Tau.BookII.Hartogs.stagefun_id_comp_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L264-L269)
**theorem
Tau.BookII.Hartogs.stagefun_id_comp_check
(n k : Denotation.TauIdx)
 :(Holomorphy.id_stage.comp Holomorphy.id_stage).b_fun n k = Holomorphy.id_stage.b_fun n k**


StageFun identity unit laws: id_stage composed with itself yields
tower-coherent result equal to id_stage evaluation.

---

### `Tau.BookII.Hartogs.tower_coherent_comp_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L275-L291)
**def
Tau.BookII.Hartogs.tower_coherent_comp_check
(bound db : Denotation.TauIdx)
 :Bool**


Tower coherence of composed reduce-based endomorphisms.
If f(n, k) = reduce(g(n), k) for some g, then f is tower-coherent.
Composing two such f's gives another tower-coherent endomorphism.
Equations
- Tau.BookII.Hartogs.tower_coherent_comp_check bound db = Tau.BookII.Hartogs.tower_coherent_comp_check.go bound db 2 1 1 ((bound + 1) * (db + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.tower_coherent_comp_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L281-L290)@[irreducible]

**def
Tau.BookII.Hartogs.tower_coherent_comp_check.go
(bound db : Denotation.TauIdx)

(x k l fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.HolEndCat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L297-L309)
**structure
Tau.BookII.Hartogs.HolEndCat :Type**


[II.D41] The endomorphism category HolEnd_tau.
Encapsulates: objects (stages), morphisms (tower-coherent maps),
composition, identity, and the category axioms.

In the Lean representation, we store:


- max_stage: the number of stages considered

- A verification that the axioms hold up to given bounds.


- max_stage : Denotation.TauIdx
Maximum stage depth.

- max_val : Denotation.TauIdx
Maximum input value for verification.

Instances For

---

### `Tau.BookII.Hartogs.instReprHolEndCat.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L309-L309)
**def
Tau.BookII.Hartogs.instReprHolEndCat.repr :HolEndCat → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.instReprHolEndCat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L309-L309)
**instance
Tau.BookII.Hartogs.instReprHolEndCat :Repr HolEndCat**

Equations
- Tau.BookII.Hartogs.instReprHolEndCat = { reprPrec := Tau.BookII.Hartogs.instReprHolEndCat.repr }

---

### `Tau.BookII.Hartogs.mk_holend`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L311-L315)
**def
Tau.BookII.Hartogs.mk_holend
(max_stage max_val : Denotation.TauIdx)
 :HolEndCat**


Construct a verified HolEndCat: checks all axioms computationally.
Equations
- Tau.BookII.Hartogs.mk_holend max_stage max_val = { max_stage := max_stage, max_val := max_val }
Instances For

---

### `Tau.BookII.Hartogs.holend_axioms_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L317-L327)
**def
Tau.BookII.Hartogs.holend_axioms_check
(cat : HolEndCat)
 :Bool**


[II.D41] Full category axiom check for HolEnd_tau:

- Associativity (II.T29)

- Left unit law

- Right unit law

- Tower coherence preservation under composition

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.holend_4_12`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L329-L330)
**def
Tau.BookII.Hartogs.holend_4_12 :HolEndCat**


The canonical HolEndCat with depth 4 and bound 12.
Equations
- Tau.BookII.Hartogs.holend_4_12 = Tau.BookII.Hartogs.mk_holend 4 12
Instances For

---

### `Tau.BookII.Hartogs.holend_3_10`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L332-L333)
**def
Tau.BookII.Hartogs.holend_3_10 :HolEndCat**


Smaller HolEndCat for faster native_decide proofs.
Equations
- Tau.BookII.Hartogs.holend_3_10 = Tau.BookII.Hartogs.mk_holend 3 10
Instances For

---

### `Tau.BookII.Hartogs.composition_closure_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L339-L353)
**def
Tau.BookII.Hartogs.composition_closure_check
(bound db : Denotation.TauIdx)
 :Bool**


Composition of reduce-based endomorphisms produces reduce-based results.
hol_comp hol_sq hol_dbl n k = reduce((2n)^2, k), which is itself reduced.
Equations
- Tau.BookII.Hartogs.composition_closure_check bound db = Tau.BookII.Hartogs.composition_closure_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.composition_closure_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L344-L352)@[irreducible]

**def
Tau.BookII.Hartogs.composition_closure_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.bipolar_comp_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L359-L380)
**def
Tau.BookII.Hartogs.bipolar_comp_check
(bound db : Denotation.TauIdx)
 :Bool**


Composition respects bipolar decomposition:
the B-sector and C-sector compose independently.
For StageFun composition: (f.g).b = f.b . g.b, (f.g).c = f.c . g.c.
This is structural from the definition of StageFun.comp.
Equations
- Tau.BookII.Hartogs.bipolar_comp_check bound db = Tau.BookII.Hartogs.bipolar_comp_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Hartogs.bipolar_comp_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L366-L379)@[irreducible]

**def
Tau.BookII.Hartogs.bipolar_comp_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.full_category_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L386-L391)
**def
Tau.BookII.Hartogs.full_category_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.D41] Complete category structure verification:
HolEnd_tau axioms + composition closure + bipolar structure.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.assoc_12_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L444-L445)
**theorem
Tau.BookII.Hartogs.assoc_12_4 :hol_assoc_check 12 4 = true**


---

### `Tau.BookII.Hartogs.assoc_triple_12_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L447-L448)
**theorem
Tau.BookII.Hartogs.assoc_triple_12_4 :hol_assoc_triple_check 12 4 = true**


---

### `Tau.BookII.Hartogs.assoc_exhaustive_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L450-L451)
**theorem
Tau.BookII.Hartogs.assoc_exhaustive_8_3 :hol_assoc_exhaustive_check 8 3 = true**


---

### `Tau.BookII.Hartogs.left_unit_12_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L454-L455)
**theorem
Tau.BookII.Hartogs.left_unit_12_4 :left_unit_check 12 4 = true**


---

### `Tau.BookII.Hartogs.right_unit_12_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L457-L458)
**theorem
Tau.BookII.Hartogs.right_unit_12_4 :right_unit_check 12 4 = true**


---

### `Tau.BookII.Hartogs.tower_comp_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L461-L462)
**theorem
Tau.BookII.Hartogs.tower_comp_10_3 :tower_coherent_comp_check 10 3 = true**


---

### `Tau.BookII.Hartogs.holend_3_10_ok`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L465-L466)
**theorem
Tau.BookII.Hartogs.holend_3_10_ok :holend_axioms_check holend_3_10 = true**


---

### `Tau.BookII.Hartogs.comp_closure_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L469-L470)
**theorem
Tau.BookII.Hartogs.comp_closure_10_3 :composition_closure_check 10 3 = true**


---

### `Tau.BookII.Hartogs.bipolar_comp_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L473-L474)
**theorem
Tau.BookII.Hartogs.bipolar_comp_10_3 :bipolar_comp_check 10 3 = true**


---

### `Tau.BookII.Hartogs.full_cat_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Hartogs/CategoryStructure.lean#L477-L478)
**theorem
Tau.BookII.Hartogs.full_cat_10_3 :full_category_check 10 3 = true**
