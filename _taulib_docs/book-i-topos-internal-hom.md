---
layout: taulib-doc
title: "TauLib.BookI.Topos.InternalHom"
permalink: /verify/taulib/docs/book-i-topos-internal-hom/
lane: verify
module_name: "TauLib.BookI.Topos.InternalHom"
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

# TauLib.Topos.InternalHom


Internal hom (exponentials) and the cartesian closed structure of E_τ.

## Registry Cross-References


- [I.D64] Internal Hom — `internal_hom`

- [I.T28] Cartesian Closed — `cartesian_closed_adj`

- [I.P28] Self-Enrichment — `self_enrichment`


## Mathematical Content


The internal hom Q^P in E_τ assigns to each object X the set of
"morphisms P → Q over X". In our Boolean-presheaf model, this simplifies:
Q^P(X) = true iff P(X) = true implies Q(X) = true.

This gives E_τ a cartesian closed structure:
Hom(A × B, C) ≅ Hom(A, C^B).

---

### `Tau.Topos.internal_hom`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/InternalHom.lean#L32-L35)
**def
Tau.Topos.internal_hom
(P Q : Presheaf)
 :Presheaf**


[I.D64] The internal hom Q^P: pointwise implication.
(Q^P)(X) = true iff P(X) implies Q(X).
Equations
- Tau.Topos.internal_hom P Q = { support := fun (x : Tau.Denotation.TauIdx) => !P.support x || Q.support x }
Instances For

---

### `Tau.Topos.ihom_both_true`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/InternalHom.lean#L37-L41)
**theorem
Tau.Topos.ihom_both_true
(P Q : Presheaf)

(x : Denotation.TauIdx)

(hp : P.support x = true)

(hq : Q.support x = true)
 :(internal_hom P Q).support x = true**


Internal hom evaluates correctly when P holds and Q holds.

---

### `Tau.Topos.ihom_p_false`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/InternalHom.lean#L43-L47)
**theorem
Tau.Topos.ihom_p_false
(P Q : Presheaf)

(x : Denotation.TauIdx)

(hp : P.support x = false)
 :(internal_hom P Q).support x = true**


Internal hom evaluates correctly when P fails.

---

### `Tau.Topos.ihom_p_true_q_false`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/InternalHom.lean#L49-L53)
**theorem
Tau.Topos.ihom_p_true_q_false
(P Q : Presheaf)

(x : Denotation.TauIdx)

(hp : P.support x = true)

(hq : Q.support x = false)
 :(internal_hom P Q).support x = false**


Internal hom evaluates correctly when P holds but Q fails.

---

### `Tau.Topos.cartesian_closed_adj`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/InternalHom.lean#L59-L73)
**theorem
Tau.Topos.cartesian_closed_adj
(A B C : Presheaf)

(x : Denotation.TauIdx)
 :(cat_product A B).support x = true → C.support x = true ↔ A.support x = true → (internal_hom B C).support x = true**


[I.T28] Cartesian closed adjunction:
(A × B)(x) = true → C(x) = true
iff
A(x) = true → (C^B)(x) = true

This is the pointwise version of Hom(A × B, C) ≅ Hom(A, C^B).

---

### `Tau.Topos.eval_morphism`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/InternalHom.lean#L75-L80)
**theorem
Tau.Topos.eval_morphism
(P Q : Presheaf)

(x : Denotation.TauIdx)
 :(cat_product (internal_hom P Q) P).support x = true → Q.support x = true**


Evaluation morphism: (Q^P × P) → Q.

---

### `Tau.Topos.self_enrichment`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/InternalHom.lean#L86-L91)
**theorem
Tau.Topos.self_enrichment
(P Q : Presheaf)
 :∃ (R : Presheaf), R = internal_hom P Q**


[I.P28] E_τ is self-enriched: internal hom gives an
internal presheaf of morphisms.
Witness: internal_hom P Q is itself a Presheaf.

---

### `Tau.Topos.ihom_terminal`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/InternalHom.lean#L93-L96)
**theorem
Tau.Topos.ihom_terminal
(Q : Presheaf)
 :(internal_hom { support := fun (x : Denotation.TauIdx) => true } Q).support = Q.support**


Internal hom with terminal: Q^1 = Q (everything implies Q iff Q).

---

### `Tau.Topos.ihom_initial`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/InternalHom.lean#L98-L101)
**theorem
Tau.Topos.ihom_initial
(Q : Presheaf)
 :(internal_hom { support := fun (x : Denotation.TauIdx) => false } Q).support = { support := fun (x : Denotation.TauIdx) => true }.support**


Internal hom from initial: Q^0 = 1 (false implies anything).

---

### `Tau.Topos.ihom_to_terminal`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Topos/InternalHom.lean#L103-L106)
**theorem
Tau.Topos.ihom_to_terminal
(P : Presheaf)
 :(internal_hom P { support := fun (x : Denotation.TauIdx) => true }).support = { support := fun (x : Denotation.TauIdx) => true }.support**


Internal hom to terminal: 1^P = 1 (everything implies true).
