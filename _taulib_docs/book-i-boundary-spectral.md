---
layout: taulib-doc
title: "TauLib.BookI.Boundary.Spectral"
permalink: /verify/taulib/docs/book-i-boundary-spectral/
lane: verify
module_name: "TauLib.BookI.Boundary.Spectral"
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

# TauLib.Boundary.Spectral


The spectral decomposition theorem for the bipolar spectral algebra.

## Registry Cross-References


- [I.T12] Spectral Decomposition — `spectral_decomposition`, `spectral_unique`


## Ground Truth Sources


- chunk_0228_M002194: Sector decomposition = spectral decomposition

- chunk_0310_M002679: Bipolar spectral analysis, character-based decomposition


## Mathematical Content


The spectral decomposition theorem gives a canonical decomposition of every
element z ∈ H_τ into B-sector and C-sector components via the fundamental
characters:

to_sectors(z) = χ₊(z) + χ₋(z)

This is equivalent to the sector decomposition already proved in BipolarAlgebra.lean,
but repackaged in the language of characters and spectral theory.

Key results:


- Decomposition: every z decomposes uniquely as B-part + C-part

- Uniqueness: the decomposition is unique

- Multiplicativity: the spectral transform is a ring isomorphism

- Ring isomorphism: H_τ ≅ Z × Z via to_sectors


---

### `Tau.Boundary.spectral`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L42-L44)
**def
Tau.Boundary.spectral
(z : Polarity.SplitComplex)
 :Polarity.SectorPair**


[I.T12] The spectral transform: maps z to its (B-sector, C-sector) pair.
This is to_sectors repackaged in spectral/character language.
Equations
- Tau.Boundary.spectral z = Tau.Polarity.to_sectors z
Instances For

---

### `Tau.Boundary.spectral_eq_chi`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L46-L49)
**theorem
Tau.Boundary.spectral_eq_chi
(z : Polarity.SplitComplex)
 :spectral z = { b_sector := chi_plus_val z, c_sector := chi_minus_val z }**


Spectral transform equals character decomposition.

---

### `Tau.Boundary.spectral_decomposition`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L55-L60)
**theorem
Tau.Boundary.spectral_decomposition
(z : Polarity.SplitComplex)
 :spectral z = (chi_plus z).add (chi_minus z)**


[I.T12] Spectral decomposition: every element decomposes as the sum of its
B-sector projection and C-sector projection.
to_sectors(z) = χ₊(z) + χ₋(z)

---

### `Tau.Boundary.spectral_b`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L62-L63)
**def
Tau.Boundary.spectral_b
(z : Polarity.SplitComplex)
 :Polarity.SectorPair**


The B-component of the spectral decomposition.
Equations
- Tau.Boundary.spectral_b z = Tau.Boundary.chi_plus z
Instances For

---

### `Tau.Boundary.spectral_c`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L65-L66)
**def
Tau.Boundary.spectral_c
(z : Polarity.SplitComplex)
 :Polarity.SectorPair**


The C-component of the spectral decomposition.
Equations
- Tau.Boundary.spectral_c z = Tau.Boundary.chi_minus z
Instances For

---

### `Tau.Boundary.spectral_orthogonal`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L68-L71)
**theorem
Tau.Boundary.spectral_orthogonal
(z : Polarity.SplitComplex)
 :(spectral_b z).mul (spectral_c z) = SectorPair.zero**


The B and C components are orthogonal.

---

### `Tau.Boundary.spectral_reconstruct`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L73-L76)
**theorem
Tau.Boundary.spectral_reconstruct
(z : Polarity.SplitComplex)
 :(spectral_b z).add (spectral_c z) = spectral z**


The B and C components together reconstruct the spectral transform.

---

### `Tau.Boundary.spectral_unique`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L82-L86)
**theorem
Tau.Boundary.spectral_unique
(a b : Polarity.SplitComplex)

(h : spectral a = spectral b)
 :a = b**


[I.T12] Spectral uniqueness: if an element has the same spectral transform
as another, they are equal. This is to_sectors injectivity in spectral language.

---

### `Tau.Boundary.spectral_eq_iff`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L88-L91)
**theorem
Tau.Boundary.spectral_eq_iff
(a b : Polarity.SplitComplex)
 :spectral a = spectral b ↔ a = b**


Two elements have equal B-sectors and C-sectors iff they are equal.

---

### `Tau.Boundary.spectral_mul`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L97-L101)
**theorem
Tau.Boundary.spectral_mul
(a b : Polarity.SplitComplex)
 :spectral (a.mul b) = (spectral a).mul (spectral b)**


The spectral transform preserves multiplication (componentwise in sectors).

---

### `Tau.Boundary.spectral_add`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L103-L107)
**theorem
Tau.Boundary.spectral_add
(a b : Polarity.SplitComplex)
 :spectral (a.add b) = (spectral a).add (spectral b)**


The spectral transform preserves addition.

---

### `Tau.Boundary.spectral_one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L109-L111)
**theorem
Tau.Boundary.spectral_one :spectral Polarity.SplitComplex.one = SectorPair.one**


The spectral transform preserves one.

---

### `Tau.Boundary.spectral_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L113-L115)
**theorem
Tau.Boundary.spectral_zero :spectral Polarity.SplitComplex.zero = SectorPair.zero**


The spectral transform preserves zero.

---

### `Tau.Boundary.spectral_neg`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L117-L120)
**theorem
Tau.Boundary.spectral_neg
(z : Polarity.SplitComplex)
 :spectral z.neg = SectorPair.neg (spectral z)**


The spectral transform preserves negation.

---

### `Tau.Boundary.spectral_ring_iso`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L122-L134)
**theorem
Tau.Boundary.spectral_ring_iso :(∀ (a b : Polarity.SplitComplex), spectral (a.add b) = (spectral a).add (spectral b)) ∧ (∀ (a b : Polarity.SplitComplex), spectral (a.mul b) = (spectral a).mul (spectral b)) ∧ spectral Polarity.SplitComplex.one = SectorPair.one ∧ ∀ (a b : Polarity.SplitComplex), spectral a = spectral b → a = b**


Full ring isomorphism: spectral is a ring homomorphism that is also injective.

---

### `Tau.Boundary.spectral_j`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L140-L142)
**theorem
Tau.Boundary.spectral_j :spectral Polarity.SplitComplex.j = { b_sector := 1, c_sector := -1 }**


The spectral transform of j: B-sector = 1, C-sector = -1.

---

### `Tau.Boundary.spectral_one_val`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L144-L146)
**theorem
Tau.Boundary.spectral_one_val :spectral Polarity.SplitComplex.one = { b_sector := 1, c_sector := 1 }**


The spectral transform of 1: both sectors equal 1.

---

### `Tau.Boundary.spectral_real`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L148-L151)
**theorem
Tau.Boundary.spectral_real
(a : ℤ)
 :spectral { re := a, im := 0 } = { b_sector := a, c_sector := a }**


A real element (im = 0) has equal sector values.

---

### `Tau.Boundary.spectral_imaginary`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L153-L156)
**theorem
Tau.Boundary.spectral_imaginary
(b : ℤ)
 :spectral { re := 0, im := b } = { b_sector := b, c_sector := -b }**


A purely imaginary element (re = 0) has opposite sector values.

---

### `Tau.Boundary.spectral_sigma`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L162-L167)
**theorem
Tau.Boundary.spectral_sigma
(z : Polarity.SplitComplex)
 :spectral (Polarity.polarity_inv z) = { b_sector := (spectral z).c_sector, c_sector := (spectral z).b_sector }**


The polarity involution σ swaps the spectral components.

---

### `Tau.Boundary.spectral_sigma_involutive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L169-L172)
**theorem
Tau.Boundary.spectral_sigma_involutive
(z : Polarity.SplitComplex)
 :spectral (Polarity.polarity_inv (Polarity.polarity_inv z)) = spectral z**


σ is a spectral reflection: it exchanges B and C sectors.

---

### `Tau.Boundary.spectral_norm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L178-L181)
**def
Tau.Boundary.spectral_norm
(z : Polarity.SplitComplex)
 :ℤ**


The spectral norm: product of B-sector and C-sector values.
This is the norm form N(a+bj) = a² - b² = (a+b)(a-b).
Equations
- Tau.Boundary.spectral_norm z = (Tau.Boundary.spectral z).b_sector * (Tau.Boundary.spectral z).c_sector
Instances For

---

### `Tau.Boundary.spectral_norm_eq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L183-L187)
**theorem
Tau.Boundary.spectral_norm_eq
(z : Polarity.SplitComplex)
 :spectral_norm z = z.re * z.re - z.im * z.im**


The spectral norm equals a² - b² (the split-complex norm).

---

### `Tau.Boundary.spectral_norm_mul`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L189-L196)
**theorem
Tau.Boundary.spectral_norm_mul
(z w : Polarity.SplitComplex)
 :spectral_norm (z.mul w) = spectral_norm z * spectral_norm w**


The spectral norm is multiplicative: N(zw) = N(z)N(w).

---

### `Tau.Boundary.zero_div_iff_norm_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Spectral.lean#L198-L202)
**theorem
Tau.Boundary.zero_div_iff_norm_zero
(z : Polarity.SplitComplex)
 :spectral_norm z = 0 ↔ z.re + z.im = 0 ∨ z.re - z.im = 0**


Zero divisors have zero spectral norm.
