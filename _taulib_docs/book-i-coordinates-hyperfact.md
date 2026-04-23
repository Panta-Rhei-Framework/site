---
layout: taulib-doc
title: "TauLib.BookI.Coordinates.Hyperfact"
permalink: /verify/taulib/docs/book-i-coordinates-hyperfact/
lane: verify
module_name: "TauLib.BookI.Coordinates.Hyperfact"
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

# TauLib.Coordinates.Hyperfact


Hyperfactorization: existence and uniqueness of the ABCD decomposition.

## Registry Cross-References


- [I.T04] Hyperfactorization Theorem — `hyperfact_check`, No-Tie + Descent

- [I.C01] Constructive Encoding Corollary — `encoding_check`


## Ground Truth Sources


- chunk_0241_M002280: Existence-uniqueness (Thm 2.14), constructive encoding

- chunk_0310_M002679: No-tie (Lemma 2.1) as uniqueness ingredient


## Mathematical Content


The Hyperfactorization Theorem states: every X ≥ 2 has a unique decomposition
X = T(A,B,C) · D where A is the largest prime divisor, C is the maximal
tetration height for the A-adic valuation, B = v_A(X) / A↑↑(C-1), and
D = X / T(A,B,C).

Uniqueness follows from the No-Tie Lemma (I.L03): the pair (B,C) is forced
by the maximality of C. Descent (I.L04) ensures D < X, so iteration terminates.

The constructive encoding corollary (I.C01) states: Φ is an injection from
τ-Idx ≥ 2 to the set of quadruples satisfying the ABCD constraints.

---

### `Tau.Coordinates.ValidABCD`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/Hyperfact.lean#L41-L45)
**def
Tau.Coordinates.ValidABCD
(x a b c d : Denotation.TauIdx)
 :Prop**


Predicate: (A,B,C,D) is a valid ABCD decomposition of X.
Equations
- Tau.Coordinates.ValidABCD x a b c d = (a ≥ 2 ∧ b ≥ 1 ∧ c ≥ 1 ∧ Tau.Coordinates.tower_atom a b c * d = x ∧ (d = 0 ∨ ¬a ∣ d))
Instances For

---

### `Tau.Coordinates.valid_abcd_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/Hyperfact.lean#L47-L51)
**def
Tau.Coordinates.valid_abcd_check
(x a b c d : Denotation.TauIdx)
 :Bool**


Computable check for valid ABCD constraints.
Equations
- Tau.Coordinates.valid_abcd_check x a b c d = (decide (a ≥ 2) && decide (b ≥ 1) && decide (c ≥ 1) && Tau.Coordinates.tower_atom a b c * d == x && (decide (d ≤ 1) || d % a != 0))
Instances For

---

### `Tau.Coordinates.hyperfact_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/Hyperfact.lean#L57-L70)
**def
Tau.Coordinates.hyperfact_check
(x : Denotation.TauIdx)
 :Bool**


[I.T04] Verify hyperfactorization for a single X:


- Greedy peel produces valid ABCD

- Reconstruction is exact

- Descent holds

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Coordinates.tau_encode`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/Hyperfact.lean#L76-L79)
**def
Tau.Coordinates.tau_encode
(x : Denotation.TauIdx)
 :List (Denotation.TauIdx × Denotation.TauIdx × Denotation.TauIdx) × Denotation.TauIdx**


[I.C01] Encoding: map X to its (spine, final remainder) pair.
This is injective by the Hyperfactorization Theorem.
Equations
- Tau.Coordinates.tau_encode x = (Tau.Coordinates.spine x, if x ≤ 1 then x else 1)
Instances For

---

### `Tau.Coordinates.tau_decode`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/Hyperfact.lean#L81-L83)
**def
Tau.Coordinates.tau_decode
(enc : List (Denotation.TauIdx × Denotation.TauIdx × Denotation.TauIdx) × Denotation.TauIdx)
 :Denotation.TauIdx**


Decoding: reconstruct X from its spine encoding.
Equations
- Tau.Coordinates.tau_decode enc = Tau.Coordinates.list_tower_prod enc.fst * enc.snd
Instances For

---

### `Tau.Coordinates.encoding_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/Hyperfact.lean#L85-L87)
**def
Tau.Coordinates.encoding_check
(x : Denotation.TauIdx)
 :Bool**


Check that encoding is a left inverse of decoding.
Equations
- Tau.Coordinates.encoding_check x = (Tau.Coordinates.tau_decode (Tau.Coordinates.tau_encode x) == x)
Instances For

---

### `Tau.Coordinates.injectivity_check_go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/Hyperfact.lean#L93-L100)@[irreducible]

**def
Tau.Coordinates.injectivity_check_go
(i n fuel : Nat)
 :Bool**


Check Φ is injective on [2..n]: no two distinct X values share coordinates.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Coordinates.injectivity_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/Hyperfact.lean#L102-L102)
**def
Tau.Coordinates.injectivity_check
(n : Denotation.TauIdx)
 :Bool**

Equations
- Tau.Coordinates.injectivity_check n = Tau.Coordinates.injectivity_check_go 2 n n
Instances For
