---
layout: taulib-doc
title: "TauLib.BookI.Boundary.Characters"
permalink: /verify/taulib/docs/book-i-boundary-characters/
lane: verify
module_name: "TauLib.BookI.Boundary.Characters"
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

# TauLib.Boundary.Characters


Lemniscate characters: ring homomorphisms from the bipolar spectral algebra
into the split-complex scalars.

## Registry Cross-References


- [I.D37] Fundamental Characters — `chi_plus`, `chi_minus`

- [I.D38] Character Group — completeness, orthogonality


## Ground Truth Sources


- chunk_0228_M002194: Split-complex algebra, sector decomposition

- chunk_0310_M002679: Bipolar partition, character theory of L


## Mathematical Content


The fundamental characters χ₊ and χ₋ are ring homomorphisms from H_τ = Z[j]
into Z (or equivalently, into the product ring Z×Z via sector embedding):


- χ₊(a + bj) = a + b (B-sector projection)

- χ₋(a + bj) = a - b (C-sector projection)


Viewed as SectorPair-valued maps:


- χ₊(z) = ⟨z.re + z.im, 0⟩ (pure B-sector element)

- χ₋(z) = ⟨0, z.re - z.im⟩ (pure C-sector element)


Key properties:


- Completeness: χ₊(z) + χ₋(z) = to_sectors(z) (the full sector decomposition)

- Orthogonality: χ₊(z) · χ₋(w) = 0 (sectors are mutually annihilating)

- σ swaps: χ₊(σz) = χ₋(z) and χ₋(σz) = χ₊(z)


---

### `Tau.Boundary.chi_plus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L46-L49)
**def
Tau.Boundary.chi_plus
(z : Polarity.SplitComplex)
 :Polarity.SectorPair**


[I.D37] The B-sector character χ₊: H_τ → Z, mapping a+bj ↦ a+b.
As a SectorPair-valued map: projects to pure B-sector.
Equations
- Tau.Boundary.chi_plus z = { b_sector := z.re + z.im, c_sector := 0 }
Instances For

---

### `Tau.Boundary.chi_minus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L51-L54)
**def
Tau.Boundary.chi_minus
(z : Polarity.SplitComplex)
 :Polarity.SectorPair**


[I.D37] The C-sector character χ₋: H_τ → Z, mapping a+bj ↦ a-b.
As a SectorPair-valued map: projects to pure C-sector.
Equations
- Tau.Boundary.chi_minus z = { b_sector := 0, c_sector := z.re - z.im }
Instances For

---

### `Tau.Boundary.chi_plus_val`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L56-L57)
**def
Tau.Boundary.chi_plus_val
(z : Polarity.SplitComplex)
 :ℤ**


The B-sector value as an integer.
Equations
- Tau.Boundary.chi_plus_val z = z.re + z.im
Instances For

---

### `Tau.Boundary.chi_minus_val`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L59-L60)
**def
Tau.Boundary.chi_minus_val
(z : Polarity.SplitComplex)
 :ℤ**


The C-sector value as an integer.
Equations
- Tau.Boundary.chi_minus_val z = z.re - z.im
Instances For

---

### `Tau.Boundary.chi_plus_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L62-L64)
**theorem
Tau.Boundary.chi_plus_eq
(z : Polarity.SplitComplex)
 :chi_plus z = { b_sector := chi_plus_val z, c_sector := 0 }**


Bridge: chi_plus decomposes as sector-embedded chi_plus_val.

---

### `Tau.Boundary.chi_minus_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L66-L68)
**theorem
Tau.Boundary.chi_minus_eq
(z : Polarity.SplitComplex)
 :chi_minus z = { b_sector := 0, c_sector := chi_minus_val z }**


Bridge: chi_minus decomposes as sector-embedded chi_minus_val.

---

### `Tau.Boundary.chi_plus_add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L74-L79)
**theorem
Tau.Boundary.chi_plus_add
(a b : Polarity.SplitComplex)
 :chi_plus (a.add b) = (chi_plus a).add (chi_plus b)**


χ₊ preserves addition.

---

### `Tau.Boundary.chi_plus_mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L81-L88)
**theorem
Tau.Boundary.chi_plus_mul
(a b : Polarity.SplitComplex)
 :chi_plus (a.mul b) = (chi_plus a).mul (chi_plus b)**


χ₊ preserves multiplication.

---

### `Tau.Boundary.chi_plus_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L90-L93)
**theorem
Tau.Boundary.chi_plus_one :chi_plus Polarity.SplitComplex.one = { b_sector := 1, c_sector := 0 }**


χ₊ maps the identity to ⟨1, 0⟩ (pure B-sector unit).

---

### `Tau.Boundary.chi_plus_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L95-L98)
**theorem
Tau.Boundary.chi_plus_zero :chi_plus Polarity.SplitComplex.zero = SectorPair.zero**


χ₊ preserves zero.

---

### `Tau.Boundary.chi_plus_neg`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L100-L104)
**theorem
Tau.Boundary.chi_plus_neg
(z : Polarity.SplitComplex)
 :chi_plus z.neg = SectorPair.neg (chi_plus z)**


χ₊ preserves negation.

---

### `Tau.Boundary.chi_minus_add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L110-L115)
**theorem
Tau.Boundary.chi_minus_add
(a b : Polarity.SplitComplex)
 :chi_minus (a.add b) = (chi_minus a).add (chi_minus b)**


χ₋ preserves addition.

---

### `Tau.Boundary.chi_minus_mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L117-L124)
**theorem
Tau.Boundary.chi_minus_mul
(a b : Polarity.SplitComplex)
 :chi_minus (a.mul b) = (chi_minus a).mul (chi_minus b)**


χ₋ preserves multiplication.

---

### `Tau.Boundary.chi_minus_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L126-L129)
**theorem
Tau.Boundary.chi_minus_one :chi_minus Polarity.SplitComplex.one = { b_sector := 0, c_sector := 1 }**


χ₋ maps the identity to ⟨0, 1⟩ (pure C-sector unit).

---

### `Tau.Boundary.chi_minus_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L131-L134)
**theorem
Tau.Boundary.chi_minus_zero :chi_minus Polarity.SplitComplex.zero = SectorPair.zero**


χ₋ preserves zero.

---

### `Tau.Boundary.chi_minus_neg`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L136-L140)
**theorem
Tau.Boundary.chi_minus_neg
(z : Polarity.SplitComplex)
 :chi_minus z.neg = SectorPair.neg (chi_minus z)**


χ₋ preserves negation.

---

### `Tau.Boundary.chi_complete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L146-L151)
**theorem
Tau.Boundary.chi_complete
(z : Polarity.SplitComplex)
 :(chi_plus z).add (chi_minus z) = Polarity.to_sectors z**


[I.D38] Completeness: χ₊(z) + χ₋(z) = to_sectors(z).
The two characters together reconstruct the full sector decomposition.

---

### `Tau.Boundary.to_sectors_eq_chi`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L153-L156)
**theorem
Tau.Boundary.to_sectors_eq_chi
(z : Polarity.SplitComplex)
 :Polarity.to_sectors z = { b_sector := chi_plus_val z, c_sector := chi_minus_val z }**


Completeness in terms of values: the sector pair equals (χ₊ val, χ₋ val).

---

### `Tau.Boundary.chi_orthogonal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L162-L166)
**theorem
Tau.Boundary.chi_orthogonal
(z w : Polarity.SplitComplex)
 :(chi_plus z).mul (chi_minus w) = SectorPair.zero**


[I.D38] Orthogonality: χ₊(z) · χ₋(w) = 0 for all z, w.
The B-sector and C-sector are mutually annihilating.

---

### `Tau.Boundary.chi_orthogonal'`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L168-L171)
**theorem
Tau.Boundary.chi_orthogonal'
(z w : Polarity.SplitComplex)
 :(chi_minus z).mul (chi_plus w) = SectorPair.zero**


Orthogonality in the other order.

---

### `Tau.Boundary.chi_plus_idempotent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L177-L181)
**theorem
Tau.Boundary.chi_plus_idempotent
(z : Polarity.SplitComplex)
 :(chi_plus z).mul (chi_plus z) = { b_sector := (z.re + z.im) * (z.re + z.im), c_sector := 0 }**


χ₊ is an idempotent projection: χ₊² = χ₊ (in the sector ring).

---

### `Tau.Boundary.chi_plus_of_e_plus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L183-L186)
**theorem
Tau.Boundary.chi_plus_of_e_plus :chi_plus { re := 1, im := 1 } = { b_sector := 2, c_sector := 0 }**


χ₊ of e₊ = e₊ (the character selects its own idempotent).

---

### `Tau.Boundary.chi_minus_of_e_minus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L188-L191)
**theorem
Tau.Boundary.chi_minus_of_e_minus :chi_minus { re := 1, im := -1 } = { b_sector := 0, c_sector := 2 }**


χ₋ of e₋ = e₋ (the character selects its own idempotent).

---

### `Tau.Boundary.chi_plus_of_e_minus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L193-L196)
**theorem
Tau.Boundary.chi_plus_of_e_minus :chi_plus { re := 1, im := -1 } = SectorPair.zero**


χ₊ of e₋ = 0 (the B-character annihilates the C-idempotent).

---

### `Tau.Boundary.chi_minus_of_e_plus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L198-L201)
**theorem
Tau.Boundary.chi_minus_of_e_plus :chi_minus { re := 1, im := 1 } = SectorPair.zero**


χ₋ of e₊ = 0 (the C-character annihilates the B-idempotent).

---

### `Tau.Boundary.sigma_swaps_chi_plus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L207-L210)
**theorem
Tau.Boundary.sigma_swaps_chi_plus
(z : Polarity.SplitComplex)
 :chi_plus_val (Polarity.polarity_inv z) = chi_minus_val z**


σ swaps characters: χ₊(σz) = χ₋(z) (as SectorPair values with sector swap).

---

### `Tau.Boundary.sigma_swaps_chi_minus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L212-L215)
**theorem
Tau.Boundary.sigma_swaps_chi_minus
(z : Polarity.SplitComplex)
 :chi_minus_val (Polarity.polarity_inv z) = chi_plus_val z**


σ swaps characters: χ₋(σz) = χ₊(z).

---

### `Tau.Boundary.sigma_swaps_chi`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L217-L223)
**theorem
Tau.Boundary.sigma_swaps_chi
(z : Polarity.SplitComplex)
 :chi_plus (Polarity.polarity_inv z) = { b_sector := chi_minus_val z, c_sector := 0 } ∧ chi_minus (Polarity.polarity_inv z) = { b_sector := 0, c_sector := chi_plus_val z }**


σ swaps the SectorPair-valued characters (with coordinate exchange).

---

### `Tau.Boundary.chi_split_b_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L229-L233)
**theorem
Tau.Boundary.chi_split_b_sector
(p N : Denotation.TauIdx)

(h : Polarity.polarity_chi p N = -1)
 :Polarity.chi_split p N = Polarity.e_plus_sector**


Bridge: for a B-dominant prime (polarity_chi = -1), chi_split maps to
e_plus_sector = (1,0), which is in the image of chi_plus (up to scaling).

---

### `Tau.Boundary.chi_split_c_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L235-L239)
**theorem
Tau.Boundary.chi_split_c_sector
(p N : Denotation.TauIdx)

(h : Polarity.polarity_chi p N = 1)
 :Polarity.chi_split p N = Polarity.e_minus_sector**


Bridge: for a C-dominant prime (polarity_chi = +1), chi_split maps to
e_minus_sector = (0,1), which is in the image of chi_minus (up to scaling).

---

### `Tau.Boundary.chi_plus_j`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L245-L247)
**theorem
Tau.Boundary.chi_plus_j :chi_plus_val Polarity.SplitComplex.j = 1**


χ₊(j) = 1: the split-complex unit j has B-sector value 1.

---

### `Tau.Boundary.chi_minus_j`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L249-L251)
**theorem
Tau.Boundary.chi_minus_j :chi_minus_val Polarity.SplitComplex.j = -1**


χ₋(j) = -1: the split-complex unit j has C-sector value -1.

---

### `Tau.Boundary.chi_vals_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Characters.lean#L253-L255)
**theorem
Tau.Boundary.chi_vals_one :chi_plus_val Polarity.SplitComplex.one = 1 ∧ chi_minus_val Polarity.SplitComplex.one = 1**


χ₊(1) = 1 and χ₋(1) = 1.
