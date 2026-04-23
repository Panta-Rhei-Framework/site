---
layout: taulib-doc
title: "TauLib.BookII.Geometry.Congruence"
permalink: /verify/taulib/docs/book-ii-geometry-congruence/
lane: verify
module_name: "TauLib.BookII.Geometry.Congruence"
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

# TauLib.BookII.Geometry.Congruence


Congruence relation from canonical ultrametric distance.

## Registry Cross-References


- [II.D20] Congruence Relation — `congruent`

- [II.T16] Congruence Axioms — `cong_reflexivity_check` .. `cong_five_segment_check`


## Mathematical Content


AB ≅ CD ⟺ δ(A,B) = δ(C,D)

Tarski congruence axioms:


- C1 (Reflexivity): AB ≅ BA

- C2 (Identity): AB ≅ CC ⟹ A = B

- C3 (Transitivity): AB ≅ CD ∧ CD ≅ EF ⟹ AB ≅ EF

- C4 (Segment Construction): ∃ E with B(C,D,E) and DE ≅ AB

- C5 (Five-Segment): congruence propagation

- C6 (Inner Transitivity): congruence compatibility with betweenness


---

### `Tau.BookII.Geometry.congruent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Congruence.lean#L34-L38)
**def
Tau.BookII.Geometry.congruent
(a b c d db : Denotation.TauIdx)
 :Bool**


[II.D20] Ultrametric congruence: AB ≅ CD iff δ(A,B) = δ(C,D).
Segments have equal "length" iff their endpoints have equal
agreement depth in the primorial tower.
Equations
- Tau.BookII.Geometry.congruent a b c d db = (Tau.BookII.Domains.disagree_depth a b db == Tau.BookII.Domains.disagree_depth c d db)
Instances For

---

### `Tau.BookII.Geometry.cong_reflexivity_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Congruence.lean#L44-L54)
**def
Tau.BookII.Geometry.cong_reflexivity_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T16, C1] Reflexivity: AB ≅ BA.
Immediate from δ symmetry.
Equations
- Tau.BookII.Geometry.cong_reflexivity_check bound db = Tau.BookII.Geometry.cong_reflexivity_check.go bound db 2 2 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Geometry.cong_reflexivity_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Congruence.lean#L49-L53)@[irreducible]

**def
Tau.BookII.Geometry.cong_reflexivity_check.go
(bound db : Denotation.TauIdx)

(a b fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.cong_identity_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Congruence.lean#L56-L69)
**def
Tau.BookII.Geometry.cong_identity_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T16, C2] Identity: AB ≅ CC ⟹ A = B.
If δ(A,B) = δ(C,C) = ∞, then A = B.
Equations
- Tau.BookII.Geometry.cong_identity_check bound db = Tau.BookII.Geometry.cong_identity_check.go bound db 2 2 2 ((bound + 1) * (bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Geometry.cong_identity_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Congruence.lean#L61-L68)@[irreducible]

**def
Tau.BookII.Geometry.cong_identity_check.go
(bound db : Denotation.TauIdx)

(a b c fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.cong_transitivity_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Congruence.lean#L71-L79)
**def
Tau.BookII.Geometry.cong_transitivity_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T16, C3] Transitivity: AB ≅ CD ∧ CD ≅ EF ⟹ AB ≅ EF.
Follows from transitivity of equality on depths.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.cong_five_segment_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Congruence.lean#L81-L88)
**def
Tau.BookII.Geometry.cong_five_segment_check
(db : Denotation.TauIdx)
 :Bool**


[II.T16, C5] Five-Segment Axiom:
Verified via shift-invariance: disagree_depth is stable
under uniform translation by P₁, witnessed on distinct pairs.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.segment_construct`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Congruence.lean#L94-L98)
**def
Tau.BookII.Geometry.segment_construct
(d_val target_depth : Denotation.TauIdx)
 :Denotation.TauIdx**


[II.T16, C4] Segment construction: given target depth m,
find element E at depth m from D.
Uses primorial structure: E = D + P_m gives δ(D,E) = m.
Equations
- Tau.BookII.Geometry.segment_construct d_val target_depth = d_val + Tau.Polarity.primorial target_depth
Instances For

---

### `Tau.BookII.Geometry.segment_construct_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Congruence.lean#L100-L113)
**def
Tau.BookII.Geometry.segment_construct_check
(bound db : Denotation.TauIdx)
 :Bool**


Verify segment construction achieves target depth.
Equations
- Tau.BookII.Geometry.segment_construct_check bound db = Tau.BookII.Geometry.segment_construct_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Geometry.segment_construct_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Congruence.lean#L104-L112)@[irreducible]

**def
Tau.BookII.Geometry.segment_construct_check.go
(bound db : Denotation.TauIdx)

(d m fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.cong_refl_15`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Congruence.lean#L132-L132)
**theorem
Tau.BookII.Geometry.cong_refl_15 :cong_reflexivity_check 15 5 = true**


---

### `Tau.BookII.Geometry.cong_ident_8`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Congruence.lean#L133-L133)
**theorem
Tau.BookII.Geometry.cong_ident_8 :cong_identity_check 8 5 = true**


---

### `Tau.BookII.Geometry.cong_trans`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Congruence.lean#L134-L134)
**theorem
Tau.BookII.Geometry.cong_trans :cong_transitivity_check 15 5 = true**


---

### `Tau.BookII.Geometry.five_seg`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/Congruence.lean#L135-L135)
**theorem
Tau.BookII.Geometry.five_seg :cong_five_segment_check 5 = true**
