---
layout: taulib-doc
title: "TauLib.BookI.Coordinates.NoTie"
permalink: /verify/taulib/docs/book-i-coordinates-no-tie/
lane: verify
module_name: "TauLib.BookI.Coordinates.NoTie"
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

# TauLib.Coordinates.NoTie


No-Tie Lemma: uniqueness of canonical (B,C) decomposition of a valuation.

## Registry Cross-References


- [I.L03] No-Tie Lemma — `no_tie`


## Ground Truth Sources


- chunk_0241_M002280: No-tie property from maximality constraint

- chunk_0310_M002679: No-tie as Lemma 2.1, uniqueness of (B,C)


## Mathematical Content


Given a prime A ≥ 2 and a valuation v = b · A↑↑(c-1) with c maximal
(i.e., ¬(A↑↑c ∣ v)), the pair (b,c) is uniquely determined by v.

The proof uses three key facts:

- Tetration is weakly monotone (from strict monotonicity)

- Higher tetrations divide lower ones (both are powers of A)

- Maximality prevents "C-leaking": if c₁ < c₂, then A↑↑c₁ | v,
contradicting maximality of c₁.


Note: tower_atom is NOT injective in general (T(2,2,1) = T(2,1,2) = 4).
The No-Tie holds only with the maximality constraint.

---

### `Tau.Coordinates.tetration_mono`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/NoTie.lean#L39-L46)
**theorem
Tau.Coordinates.tetration_mono
(a : Nat)

(ha : a ≥ 2)

{c1 c2 : Nat}

(h : c1 ≤ c2)
 :Orbit.tetration a c1 ≤ Orbit.tetration a c2**


Tetration is weakly monotone: c₁ ≤ c₂ → a↑↑c₁ ≤ a↑↑c₂ for a ≥ 2.

---

### `Tau.Coordinates.pow_dvd_pow_of_le`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/NoTie.lean#L52-L54)
**theorem
Tau.Coordinates.pow_dvd_pow_of_le
(a : Nat)

{m n : Nat}

(h : m ≤ n)
 :a ^ m ∣ a ^ n**


a^m divides a^n when m ≤ n.

---

### `Tau.Coordinates.tetration_dvd_of_le`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/NoTie.lean#L56-L61)
**theorem
Tau.Coordinates.tetration_dvd_of_le
(a : Nat)

(ha : a ≥ 2)

{c1 c2 : Nat}

(hc1 : c1 ≥ 1)

(hc2 : c2 ≥ 1)

(h : c1 ≤ c2)
 :Orbit.tetration a c1 ∣ Orbit.tetration a c2**


Higher tetrations divide lower tetrations (for c ≥ 1, both are powers of A).

---

### `Tau.Coordinates.nat_mul_cancel_right`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/NoTie.lean#L79-L82)
**theorem
Tau.Coordinates.nat_mul_cancel_right
{a b d : Nat}

(h : a * d = b * d)

(hd : d ≥ 1)
 :a = b**


Right cancellation for multiplication: a * d = b * d → d ≥ 1 → a = b.

---

### `Tau.Coordinates.no_tie`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/NoTie.lean#L88-L132)
**theorem
Tau.Coordinates.no_tie
(a b1 c1 b2 c2 : Nat)

(ha : a ≥ 2)

(_hb1 : b1 ≥ 1)

(hc1 : c1 ≥ 1)

(_hb2 : b2 ≥ 1)

(hc2 : c2 ≥ 1)

(heq : b1 * Orbit.tetration a (c1 - 1) = b2 * Orbit.tetration a (c2 - 1))

(hmax1 : ¬Orbit.tetration a c1 ∣ b1 * Orbit.tetration a (c1 - 1))

(hmax2 : ¬Orbit.tetration a c2 ∣ b2 * Orbit.tetration a (c2 - 1))
 :c1 = c2 ∧ b1 = b2**


[I.L03] No-Tie Lemma: If b₁ · A↑↑(c₁-1) = b₂ · A↑↑(c₂-1) (=: v),
and both c₁, c₂ are maximal (¬(A↑↑cᵢ ∣ v)), then c₁ = c₂ and b₁ = b₂.

Proof: Suppose c₁ < c₂. Then A↑↑c₁ ∣ A↑↑(c₂-1) (since both are
powers of A and c₁ ≤ c₂-1). Hence A↑↑c₁ ∣ v = b₂ · A↑↑(c₂-1).
But ¬(A↑↑c₁ ∣ v), contradiction. So c₁ = c₂, then b₁ = b₂.
