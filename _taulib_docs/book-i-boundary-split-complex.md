---
layout: taulib-doc
title: "TauLib.BookI.Boundary.SplitComplex"
permalink: /verify/taulib/docs/book-i-boundary-split-complex/
lane: verify
module_name: "TauLib.BookI.Boundary.SplitComplex"
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

# TauLib.Boundary.SplitComplex


Full ring axioms for SplitComplex and SectorPair, plus to_sectors bijectivity
and zero divisor characterization.

## Registry Cross-References


- [I.D27] Bipolar Spectral Algebra — Ring axiom suite for `SplitComplex`, `SectorPair`

- [I.T10] Split-Complex Forced — Zero divisor characterization


## Ground Truth Sources


- chunk_0228_M002194: Split-complex ring, sector decomposition ring isomorphism

- chunk_0310_M002679: Bipolar partition, zero divisors from sector coordinates


## Mathematical Content


The split-complex algebra H = Z[j] with j^2 = +1 is a commutative ring with
zero divisors. The sector decomposition phi: H -> Z x Z via (a+bj) -> (a+b, a-b)
is a ring isomorphism. Zero divisors in H are exactly elements where one sector
coordinate vanishes: z is a zero divisor iff z.re + z.im = 0 or z.re - z.im = 0.

---

### `Tau.Boundary.SplitComplex.ext`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L36-L39)
**theorem
Tau.Boundary.SplitComplex.ext
{a b : Polarity.SplitComplex}

(hre : a.re = b.re)

(him : a.im = b.im)
 :a = b**


---

### `Tau.Boundary.SplitComplex.ext_iff`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L36-L36)
**theorem
Tau.Boundary.SplitComplex.ext_iff
{a b : Polarity.SplitComplex}
 :a = b ↔ a.re = b.re ∧ a.im = b.im**


---

### `Tau.Boundary.sc_add_comm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L45-L48)
**theorem
Tau.Boundary.sc_add_comm
(a b : Polarity.SplitComplex)
 :a.add b = b.add a**


Additive commutativity: a + b = b + a.

---

### `Tau.Boundary.sc_add_assoc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L50-L54)
**theorem
Tau.Boundary.sc_add_assoc
(a b c : Polarity.SplitComplex)
 :(a.add b).add c = a.add (b.add c)**


Additive associativity: (a + b) + c = a + (b + c).

---

### `Tau.Boundary.sc_add_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L56-L59)
**theorem
Tau.Boundary.sc_add_zero
(a : Polarity.SplitComplex)
 :a.add Polarity.SplitComplex.zero = a**


Additive identity: a + 0 = a.

---

### `Tau.Boundary.sc_add_neg`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L61-L64)
**theorem
Tau.Boundary.sc_add_neg
(a : Polarity.SplitComplex)
 :a.add a.neg = Polarity.SplitComplex.zero**


Additive inverse: a + (-a) = 0.

---

### `Tau.Boundary.sc_mul_comm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L66-L69)
**theorem
Tau.Boundary.sc_mul_comm
(a b : Polarity.SplitComplex)
 :a.mul b = b.mul a**


Multiplicative commutativity: a * b = b * a.

---

### `Tau.Boundary.sc_mul_assoc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L71-L75)
**theorem
Tau.Boundary.sc_mul_assoc
(a b c : Polarity.SplitComplex)
 :(a.mul b).mul c = a.mul (b.mul c)**


Multiplicative associativity: (a * b) * c = a * (b * c).

---

### `Tau.Boundary.sc_mul_one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L77-L80)
**theorem
Tau.Boundary.sc_mul_one
(a : Polarity.SplitComplex)
 :a.mul Polarity.SplitComplex.one = a**


Multiplicative identity: a * 1 = a.

---

### `Tau.Boundary.sc_left_distrib`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L82-L86)
**theorem
Tau.Boundary.sc_left_distrib
(a b c : Polarity.SplitComplex)
 :a.mul (b.add c) = (a.mul b).add (a.mul c)**


Left distributivity: a * (b + c) = a*b + a*c.

---

### `Tau.Boundary.sc_ring_axioms`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L88-L102)
**theorem
Tau.Boundary.sc_ring_axioms :(∀ (a b : Polarity.SplitComplex), a.add b = b.add a) ∧ (∀ (a b c : Polarity.SplitComplex), (a.add b).add c = a.add (b.add c)) ∧ (∀ (a : Polarity.SplitComplex), a.add Polarity.SplitComplex.zero = a) ∧ (∀ (a : Polarity.SplitComplex), a.add a.neg = Polarity.SplitComplex.zero) ∧ (∀ (a b : Polarity.SplitComplex), a.mul b = b.mul a) ∧ (∀ (a b c : Polarity.SplitComplex), (a.mul b).mul c = a.mul (b.mul c)) ∧ (∀ (a : Polarity.SplitComplex), a.mul Polarity.SplitComplex.one = a) ∧ ∀ (a b c : Polarity.SplitComplex), a.mul (b.add c) = (a.mul b).add (a.mul c)**


Full SplitComplex ring axiom collection.

---

### `Tau.Boundary.SectorPair.ext`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L108-L112)
**theorem
Tau.Boundary.SectorPair.ext
{a b : Polarity.SectorPair}

(hb : a.b_sector = b.b_sector)

(hc : a.c_sector = b.c_sector)
 :a = b**


---

### `Tau.Boundary.SectorPair.ext_iff`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L108-L108)
**theorem
Tau.Boundary.SectorPair.ext_iff
{a b : Polarity.SectorPair}
 :a = b ↔ a.b_sector = b.b_sector ∧ a.c_sector = b.c_sector**


---

### `Tau.Boundary.SectorPair.zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L118-L119)
**def
Tau.Boundary.SectorPair.zero :Polarity.SectorPair**


SectorPair zero.
Equations
- Tau.Boundary.SectorPair.zero = { b_sector := 0, c_sector := 0 }
Instances For

---

### `Tau.Boundary.SectorPair.one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L121-L122)
**def
Tau.Boundary.SectorPair.one :Polarity.SectorPair**


SectorPair one (the multiplicative identity).
Equations
- Tau.Boundary.SectorPair.one = { b_sector := 1, c_sector := 1 }
Instances For

---

### `Tau.Boundary.SectorPair.neg`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L124-L126)
**def
Tau.Boundary.SectorPair.neg
(a : Polarity.SectorPair)
 :Polarity.SectorPair**


SectorPair negation.
Equations
- Tau.Boundary.SectorPair.neg a = { b_sector := -a.b_sector, c_sector := -a.c_sector }
Instances For

---

### `Tau.Boundary.sp_add_comm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L128-L131)
**theorem
Tau.Boundary.sp_add_comm
(a b : Polarity.SectorPair)
 :a.add b = b.add a**


Additive commutativity.

---

### `Tau.Boundary.sp_add_assoc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L133-L137)
**theorem
Tau.Boundary.sp_add_assoc
(a b c : Polarity.SectorPair)
 :(a.add b).add c = a.add (b.add c)**


Additive associativity.

---

### `Tau.Boundary.sp_add_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L139-L142)
**theorem
Tau.Boundary.sp_add_zero
(a : Polarity.SectorPair)
 :a.add SectorPair.zero = a**


Additive identity.

---

### `Tau.Boundary.sp_add_neg`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L144-L147)
**theorem
Tau.Boundary.sp_add_neg
(a : Polarity.SectorPair)
 :a.add (SectorPair.neg a) = SectorPair.zero**


Additive inverse.

---

### `Tau.Boundary.sp_mul_comm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L149-L152)
**theorem
Tau.Boundary.sp_mul_comm
(a b : Polarity.SectorPair)
 :a.mul b = b.mul a**


Multiplicative commutativity.

---

### `Tau.Boundary.sp_mul_assoc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L154-L158)
**theorem
Tau.Boundary.sp_mul_assoc
(a b c : Polarity.SectorPair)
 :(a.mul b).mul c = a.mul (b.mul c)**


Multiplicative associativity.

---

### `Tau.Boundary.sp_mul_one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L160-L163)
**theorem
Tau.Boundary.sp_mul_one
(a : Polarity.SectorPair)
 :a.mul SectorPair.one = a**


Multiplicative identity.

---

### `Tau.Boundary.sp_left_distrib`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L165-L169)
**theorem
Tau.Boundary.sp_left_distrib
(a b c : Polarity.SectorPair)
 :a.mul (b.add c) = (a.mul b).add (a.mul c)**


Left distributivity: a * (b + c) = a*b + a*c.

---

### `Tau.Boundary.sp_ring_axioms`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L171-L185)
**theorem
Tau.Boundary.sp_ring_axioms :(∀ (a b : Polarity.SectorPair), a.add b = b.add a) ∧ (∀ (a b c : Polarity.SectorPair), (a.add b).add c = a.add (b.add c)) ∧ (∀ (a : Polarity.SectorPair), a.add SectorPair.zero = a) ∧ (∀ (a : Polarity.SectorPair), a.add (SectorPair.neg a) = SectorPair.zero) ∧ (∀ (a b : Polarity.SectorPair), a.mul b = b.mul a) ∧ (∀ (a b c : Polarity.SectorPair), (a.mul b).mul c = a.mul (b.mul c)) ∧ (∀ (a : Polarity.SectorPair), a.mul SectorPair.one = a) ∧ ∀ (a b c : Polarity.SectorPair), a.mul (b.add c) = (a.mul b).add (a.mul c)**


Full SectorPair ring axiom collection.

---

### `Tau.Boundary.from_sectors`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L191-L197)
**def
Tau.Boundary.from_sectors
(s : Polarity.SectorPair)
 :Polarity.SplitComplex**


Inverse of to_sectors: recover SplitComplex from SectorPair.
Given (u, v) = (a+b, a-b), recover a = (u+v)/2, b = (u-v)/2.
Over integers, this requires u+v and u-v to be even, which is
always the case since u and v have the same parity. We work
formally: from_sectors(to_sectors(z)) = z is proved directly.
Equations
- Tau.Boundary.from_sectors s = { re := (s.b_sector + s.c_sector) / 2, im := (s.b_sector - s.c_sector) / 2 }
Instances For

---

### `Tau.Boundary.to_sectors_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L199-L206)
**theorem
Tau.Boundary.to_sectors_injective
(a b : Polarity.SplitComplex)

(h : Polarity.to_sectors a = Polarity.to_sectors b)
 :a = b**


to_sectors is injective: to_sectors a = to_sectors b implies a = b.

---

### `Tau.Boundary.from_sectors_left_inv`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L208-L212)
**theorem
Tau.Boundary.from_sectors_left_inv
(z : Polarity.SplitComplex)
 :from_sectors (Polarity.to_sectors z) = z**


from_sectors is a left inverse of to_sectors (over SplitComplex).

---

### `Tau.Boundary.to_sectors_surj_on_image`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L214-L224)
**theorem
Tau.Boundary.to_sectors_surj_on_image
(s : Polarity.SectorPair)

(h : (s.b_sector + s.c_sector) % 2 = 0)
 :Polarity.to_sectors (from_sectors s) = s**


to_sectors composed with from_sectors is identity on even-parity sector pairs.
Note: over Z, to_sectors only reaches even-sum pairs (u+v always even).

---

### `Tau.Boundary.to_sectors_parity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L226-L233)
**theorem
Tau.Boundary.to_sectors_parity
(z : Polarity.SplitComplex)
 :((Polarity.to_sectors z).b_sector + (Polarity.to_sectors z).c_sector) % 2 = 0**


The image of to_sectors consists of pairs with equal parity.

---

### `Tau.Boundary.to_sectors_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L239-L242)
**theorem
Tau.Boundary.to_sectors_zero :Polarity.to_sectors Polarity.SplitComplex.zero = SectorPair.zero**


to_sectors preserves zero.

---

### `Tau.Boundary.to_sectors_one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L244-L247)
**theorem
Tau.Boundary.to_sectors_one :Polarity.to_sectors Polarity.SplitComplex.one = SectorPair.one**


to_sectors preserves one.

---

### `Tau.Boundary.to_sectors_neg`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L249-L253)
**theorem
Tau.Boundary.to_sectors_neg
(z : Polarity.SplitComplex)
 :Polarity.to_sectors z.neg = SectorPair.neg (Polarity.to_sectors z)**


to_sectors preserves negation.

---

### `Tau.Boundary.zero_divisor_sector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L261-L278)
**theorem
Tau.Boundary.zero_divisor_sector
(z w : Polarity.SplitComplex)

(h : z.mul w = Polarity.SplitComplex.zero)
 :(z.re + z.im) * (w.re + w.im) = 0 ∧ (z.re - z.im) * (w.re - w.im) = 0**


A split-complex number z is a zero divisor iff one sector coordinate vanishes.
Forward: if z * w = 0 with w nonzero, then one sector of z is zero.
We prove: z * w = 0 implies (z.re+z.im)*(w.re+w.im) = 0 AND
(z.re-z.im)*(w.re-w.im) = 0. So if w has both sectors nonzero,
both sectors of z must be zero (and z = 0). Nontrivial zero divisors
have exactly one sector vanishing.

---

### `Tau.Boundary.zero_divisor_witness_b`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L280-L286)
**theorem
Tau.Boundary.zero_divisor_witness_b
(z : Polarity.SplitComplex)

(h : z.re + z.im = 0)
 :z.mul { re := 1, im := 1 } = Polarity.SplitComplex.zero**


Converse: if one sector of z is zero, z is a zero divisor
(witness provided explicitly).

---

### `Tau.Boundary.zero_divisor_witness_c`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L288-L292)
**theorem
Tau.Boundary.zero_divisor_witness_c
(z : Polarity.SplitComplex)

(h : z.re - z.im = 0)
 :z.mul { re := 1, im := -1 } = Polarity.SplitComplex.zero**


---

### `Tau.Boundary.zero_divisors_iff`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/SplitComplex.lean#L294-L314)
**theorem
Tau.Boundary.zero_divisors_iff
(z : Polarity.SplitComplex)

(hz : z ≠ Polarity.SplitComplex.zero)
 :(∃ (w : Polarity.SplitComplex), w ≠ Polarity.SplitComplex.zero ∧ z.mul w = Polarity.SplitComplex.zero) ↔ z.re + z.im = 0 ∨ z.re - z.im = 0**


The zero divisors of SplitComplex are exactly the elements with a vanishing sector.
