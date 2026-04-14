---
layout: taulib-doc
title: "TauLib.BookII.Prologue.SplitComplexInterior"
permalink: /verify/taulib/docs/book-ii-prologue-split-complex-interior/
lane: verify
module_name: "TauLib.BookII.Prologue.SplitComplexInterior"
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

# TauLib.BookII.Prologue.SplitComplexInterior


Split-complex codomain H_τ for Book II's τ-holomorphic functions.

## Registry Cross-References


- [II.D01] Split-Complex Codomain H_τ — `HTau`, `h_tau_sectors`


## Mathematical Content


H_τ := { a + bj : a, b ∈ Ẑ_τ } with j² = +1 (I.T10).

Three reasons the elliptic algebra (i² = -1) fails for τ:

- Laplacian glue — symmetric diffusion erases boundary/interior asymmetry

- No canonical propagation — isotropic, no preferred direction

- Unipolar — single rotation phase, can't encode bipolar ℒ


Split-complex (j² = +1) is forced by prime polarity (I.T05):
bipolar partition ⇒ two orthogonal idempotents e₊, e₋ ⇒ j² = +1.
H_τ ≅ A_τ⁺ × A_τ⁻ via sector decomposition.

---

### `Tau.BookII.Prologue.HTau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Prologue/SplitComplexInterior.lean#L35-L46)@[reducible, inline]

**abbrev
Tau.BookII.Prologue.HTau :Type**


[II.D01] The split-complex codomain H_τ.
Algebraically identical to Book I's SplitComplex (I.D20),
interpreted as the codomain for τ-holomorphic functions.

H_τ = { a + bj : a, b ∈ Ẑ_τ }, j² = +1

Key properties:


- Commutative ring (unlike quaternions ℍ)

- Has zero divisors: e₊ · e₋ = 0 (unlike ℂ)

- Bipolar: decomposes into e₊-sector and e₋-sector

- Wave-type: split-CR equations give hyperbolic PDE

Equations
- Tau.BookII.Prologue.HTau = Tau.Polarity.SplitComplex
Instances For

---

### `Tau.BookII.Prologue.h_tau_sectors`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Prologue/SplitComplexInterior.lean#L48-L49)
**def
Tau.BookII.Prologue.h_tau_sectors
(z : HTau)
 :Polarity.SectorPair**


Sector form: z ↦ (z₊, z₋) where z = z₊ e₊ + z₋ e₋.
Equations
- Tau.BookII.Prologue.h_tau_sectors z = Tau.Polarity.to_sectors z
Instances For

---

### `Tau.BookII.Prologue.h_tau_b_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Prologue/SplitComplexInterior.lean#L51-L52)
**def
Tau.BookII.Prologue.h_tau_b_sector
(z : HTau)
 :ℤ**


B-sector projection (e₊ component): z ↦ re(z) + im(z).
Equations
- Tau.BookII.Prologue.h_tau_b_sector z = (Tau.Polarity.to_sectors z).b_sector
Instances For

---

### `Tau.BookII.Prologue.h_tau_c_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Prologue/SplitComplexInterior.lean#L54-L55)
**def
Tau.BookII.Prologue.h_tau_c_sector
(z : HTau)
 :ℤ**


C-sector projection (e₋ component): z ↦ re(z) - im(z).
Equations
- Tau.BookII.Prologue.h_tau_c_sector z = (Tau.Polarity.to_sectors z).c_sector
Instances For

---

### `Tau.BookII.Prologue.h_tau_mul_comm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Prologue/SplitComplexInterior.lean#L61-L64)
**theorem
Tau.BookII.Prologue.h_tau_mul_comm
(z w : HTau)
 :Polarity.SplitComplex.mul z w = Polarity.SplitComplex.mul w z**


H_τ multiplication is commutative (I.T10 consequence).

---

### `Tau.BookII.Prologue.h_tau_zero_divisors`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Prologue/SplitComplexInterior.lean#L66-L70)
**theorem
Tau.BookII.Prologue.h_tau_zero_divisors :{ re := 1, im := 1 }.mul { re := 1, im := -1 } = { re := 0, im := 0 }**


H_τ has zero divisors: (1+j)(1-j) = 0.
This encodes bipolar sector orthogonality, not a pathology.

---

### `Tau.BookII.Prologue.h_tau_sector_faithful`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Prologue/SplitComplexInterior.lean#L72-L75)
**theorem
Tau.BookII.Prologue.h_tau_sector_faithful
(z : HTau)
 :Boundary.from_sectors (Polarity.to_sectors z) = z**


Sector decomposition is faithful: z recoverable from sectors.

---

### `Tau.BookII.Prologue.h_tau_e_plus_idem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Prologue/SplitComplexInterior.lean#L81-L84)
**theorem
Tau.BookII.Prologue.h_tau_e_plus_idem :Polarity.e_plus_sector.mul Polarity.e_plus_sector = Polarity.e_plus_sector**


e₊ is idempotent in sector coordinates (I.D21).

---

### `Tau.BookII.Prologue.h_tau_e_minus_idem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Prologue/SplitComplexInterior.lean#L86-L89)
**theorem
Tau.BookII.Prologue.h_tau_e_minus_idem :Polarity.e_minus_sector.mul Polarity.e_minus_sector = Polarity.e_minus_sector**


e₋ is idempotent in sector coordinates (I.D21).

---

### `Tau.BookII.Prologue.h_tau_e_orthogonal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Prologue/SplitComplexInterior.lean#L91-L94)
**theorem
Tau.BookII.Prologue.h_tau_e_orthogonal :Polarity.e_plus_sector.mul Polarity.e_minus_sector = { b_sector := 0, c_sector := 0 }**


e₊ · e₋ = 0: sectors are orthogonal (I.D21).

---

### `Tau.BookII.Prologue.h_tau_e_partition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Prologue/SplitComplexInterior.lean#L96-L99)
**theorem
Tau.BookII.Prologue.h_tau_e_partition :Polarity.e_plus_sector.add Polarity.e_minus_sector = { b_sector := 1, c_sector := 1 }**


e₊ + e₋ = 1: sectors partition the whole algebra (I.D21).

---

### `Tau.BookII.Prologue.h_tau_nontrivial_idempotent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Prologue/SplitComplexInterior.lean#L105-L117)
**theorem
Tau.BookII.Prologue.h_tau_nontrivial_idempotent :Polarity.e_plus_sector.mul Polarity.e_plus_sector = Polarity.e_plus_sector ∧ Polarity.e_plus_sector ≠ { b_sector := 0, c_sector := 0 } ∧ Polarity.e_plus_sector ≠ { b_sector := 1, c_sector := 1 }**


Nontrivial idempotent exists in sector coordinates.
Witness: e₊ = ⟨1, 0⟩ is idempotent, nontrivial (≠ 0 and ≠ 1).

---

### `Tau.BookII.Prologue.h_tau_no_elliptic_idempotent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Prologue/SplitComplexInterior.lean#L119-L124)
**theorem
Tau.BookII.Prologue.h_tau_no_elliptic_idempotent
(z : Polarity.GaussInt)
 :z.mul z = z → z = { re := 0, im := 0 } ∨ z = { re := 1, im := 0 }**


Elliptic (Gaussian) integers have NO nontrivial idempotents.
This is why ℂ cannot serve as codomain for τ-holomorphic functions.
