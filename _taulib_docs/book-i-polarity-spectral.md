---
layout: taulib-doc
title: "TauLib.BookI.Polarity.Spectral"
permalink: /verify/taulib/docs/book-i-polarity-spectral/
lane: verify
module_name: "TauLib.BookI.Polarity.Spectral"
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

# TauLib.Polarity.Spectral


Spectral signatures and growth-rate separation.

## Registry Cross-References


- [I.D19e] Spectral Signature — `spectral_sig`, `pol_at`


## Ground Truth Sources


- chunk_0310_M002679: Spectral signature σ_N(p), growth-rate separation, polarity predicate


## Mathematical Content


For a prime p and bound N, the spectral signature σ_N(p) = (B_max, C_max)
records the highest B and C coordinates among objects X ≤ N with coord_A(X) = p.

The growth-rate separation theorem shows tetration eventually dominates
exponentiation: for every B, there exists C such that a↑↑C > a^B.
This is already proved as `tetration_unbounded` in TowerAtoms.

The polarity at bound N is: p is B-dominant if B_max > C_max.

---

### `Tau.Polarity.spectral_scan`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Spectral.lean#L35-L48)@[irreducible]

**def
Tau.Polarity.spectral_scan
(p i N bmax cmax : Denotation.TauIdx)

(fuel : Nat)
 :Denotation.TauIdx × Denotation.TauIdx**


Scan objects from i to N, tracking max B and C for objects with A = p.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.spectral_sig`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Spectral.lean#L50-L52)
**def
Tau.Polarity.spectral_sig
(p N : Denotation.TauIdx)
 :Denotation.TauIdx × Denotation.TauIdx**


[I.D19e] Spectral signature σ_N(p) = (B_max, C_max).
Equations
- Tau.Polarity.spectral_sig p N = Tau.Polarity.spectral_scan p 2 N 0 0 N
Instances For

---

### `Tau.Polarity.b_max`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Spectral.lean#L54-L55)
**def
Tau.Polarity.b_max
(p N : Denotation.TauIdx)
 :Denotation.TauIdx**


B_max component of the spectral signature.
Equations
- Tau.Polarity.b_max p N = (Tau.Polarity.spectral_sig p N).fst
Instances For

---

### `Tau.Polarity.c_max`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Spectral.lean#L57-L58)
**def
Tau.Polarity.c_max
(p N : Denotation.TauIdx)
 :Denotation.TauIdx**


C_max component of the spectral signature.
Equations
- Tau.Polarity.c_max p N = (Tau.Polarity.spectral_sig p N).snd
Instances For

---

### `Tau.Polarity.pol_at`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Spectral.lean#L64-L65)
**def
Tau.Polarity.pol_at
(p N : Denotation.TauIdx)
 :Bool**


Polarity at bound N: true = B-dominant, false = C-dominant.
Equations
- Tau.Polarity.pol_at p N = decide (Tau.Polarity.b_max p N > Tau.Polarity.c_max p N)
Instances For

---

### `Tau.Polarity.pol_label`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Spectral.lean#L67-L69)
**def
Tau.Polarity.pol_label
(p N : Denotation.TauIdx)
 :String**


String polarity label.
Equations
- Tau.Polarity.pol_label p N = if Tau.Polarity.pol_at p N = true then "B" else "C"
Instances For

---

### `Tau.Polarity.growth_rate_separation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Spectral.lean#L75-L78)
**theorem
Tau.Polarity.growth_rate_separation
(a : Nat)

(ha : a ≥ 2)

(B : Nat)
 :∃ (C : Nat), Orbit.tetration a C > a ^ B**


Growth-rate separation: for a ≥ 2 and any B, there exists C such that
a↑↑C > a^B. This is a direct corollary of tetration_unbounded.

---

### `Tau.Polarity.tetration_ge_arg`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Spectral.lean#L80-L87)
**theorem
Tau.Polarity.tetration_ge_arg
(a : Nat)

(ha : a ≥ 2)

(c : Nat)
 :Orbit.tetration a c ≥ c**


Tetration grows at least as fast as the argument: a↑↑c ≥ c for a ≥ 2.
