---
layout: taulib-doc
title: "TauLib.BookI.Boundary.Fourier"
permalink: /verify/taulib/docs/book-i-boundary-fourier/
lane: verify
module_name: "TauLib.BookI.Boundary.Fourier"
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

# TauLib.Boundary.Fourier


The crossing point, sector ideals, and bipolar Fourier analysis on the lemniscate.

## Registry Cross-References


- [I.D39] Crossing Point — `crossing_point`, `crossing_iff_equal_sectors`

- [I.D40] Bipolar Fourier Transform — `fourier`, `fourier_e_plus`, `fourier_e_minus`


## Ground Truth Sources


- chunk_0228_M002194: Sector decomposition, crossing locus

- chunk_0310_M002679: Bipolar Fourier, spectral harmonic analysis


## Mathematical Content


The crossing point of the lemniscate is the algebraic locus where the two
lobes (sectors) meet. In sector coordinates, the crossing point condition is
b_sector = c_sector, which for split-complex elements means im = 0 (real line).

The B-ideal and C-ideal are the kernel ideals of the characters χ₋ and χ₊
respectively. They correspond to the two lobes of the lemniscate.

The bipolar Fourier transform is the spectral decomposition viewed as
harmonic analysis on the lemniscate: every element of H_τ has a unique
expansion in terms of B-sector and C-sector harmonics.

---

### `Tau.Boundary.crossing_point`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L39-L41)
**def
Tau.Boundary.crossing_point :Polarity.SectorPair**


[I.D39] The crossing point in sector coordinates: both sectors equal.
This is the algebraic locus where the two lobes of the lemniscate meet.
Equations
- Tau.Boundary.crossing_point = { b_sector := 1, c_sector := 1 }
Instances For

---

### `Tau.Boundary.is_crossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L43-L44)
**def
Tau.Boundary.is_crossing
(s : Polarity.SectorPair)
 :Prop**


An element is at the crossing iff its sectors are equal.
Equations
- Tau.Boundary.is_crossing s = (s.b_sector = s.c_sector)
Instances For

---

### `Tau.Boundary.instDecidableIs_crossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L46-L47)
**instance
Tau.Boundary.instDecidableIs_crossing
(s : Polarity.SectorPair)
 :Decidable (is_crossing s)**

Equations
- Tau.Boundary.instDecidableIs_crossing s = inferInstanceAs (Decidable (s.b_sector = s.c_sector))

---

### `Tau.Boundary.crossing_iff_real`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L49-L56)
**theorem
Tau.Boundary.crossing_iff_real
(z : Polarity.SplitComplex)
 :is_crossing (spectral z) ↔ z.im = 0**


[I.D39] Crossing characterization: a split-complex element z is at the crossing
iff z is real (im = 0). Proof: b_sector = c_sector iff re+im = re-im iff im = 0.

---

### `Tau.Boundary.crossing_iff_chi_equal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L58-L63)
**theorem
Tau.Boundary.crossing_iff_chi_equal
(z : Polarity.SplitComplex)
 :is_crossing (spectral z) ↔ chi_plus_val z = chi_minus_val z**


The crossing point condition in character language:
z is at the crossing iff χ₊(z) = χ₋(z).

---

### `Tau.Boundary.one_is_crossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L65-L67)
**theorem
Tau.Boundary.one_is_crossing :is_crossing (spectral Polarity.SplitComplex.one)**


The multiplicative identity is at the crossing.

---

### `Tau.Boundary.j_not_crossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L69-L71)
**theorem
Tau.Boundary.j_not_crossing :¬is_crossing (spectral Polarity.SplitComplex.j)**


The split-complex unit j is NOT at the crossing (sectors differ).

---

### `Tau.Boundary.in_b_ideal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L77-L80)
**def
Tau.Boundary.in_b_ideal
(z : Polarity.SplitComplex)
 :Prop**


An element is in the B-ideal iff its C-sector vanishes.
The B-ideal = ker(χ₋) = {z : z.re = z.im}.
Equations
- Tau.Boundary.in_b_ideal z = ((Tau.Boundary.spectral z).c_sector = 0)
Instances For

---

### `Tau.Boundary.in_c_ideal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L82-L85)
**def
Tau.Boundary.in_c_ideal
(z : Polarity.SplitComplex)
 :Prop**


An element is in the C-ideal iff its B-sector vanishes.
The C-ideal = ker(χ₊) = {z : z.re + z.im = 0}.
Equations
- Tau.Boundary.in_c_ideal z = ((Tau.Boundary.spectral z).b_sector = 0)
Instances For

---

### `Tau.Boundary.instDecidableIn_b_ideal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L87-L88)
**instance
Tau.Boundary.instDecidableIn_b_ideal
(z : Polarity.SplitComplex)
 :Decidable (in_b_ideal z)**

Equations
- Tau.Boundary.instDecidableIn_b_ideal z = inferInstanceAs (Decidable ((Tau.Boundary.spectral z).c_sector = 0))

---

### `Tau.Boundary.instDecidableIn_c_ideal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L90-L91)
**instance
Tau.Boundary.instDecidableIn_c_ideal
(z : Polarity.SplitComplex)
 :Decidable (in_c_ideal z)**

Equations
- Tau.Boundary.instDecidableIn_c_ideal z = inferInstanceAs (Decidable ((Tau.Boundary.spectral z).b_sector = 0))

---

### `Tau.Boundary.b_ideal_iff`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L93-L97)
**theorem
Tau.Boundary.b_ideal_iff
(z : Polarity.SplitComplex)
 :in_b_ideal z ↔ z.re = z.im**


B-ideal characterization: z is in the B-ideal iff z.re = z.im.

---

### `Tau.Boundary.c_ideal_iff`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L99-L102)
**theorem
Tau.Boundary.c_ideal_iff
(z : Polarity.SplitComplex)
 :in_c_ideal z ↔ z.re + z.im = 0**


C-ideal characterization: z is in the C-ideal iff z.re + z.im = 0.

---

### `Tau.Boundary.b_times_c_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L104-L113)
**theorem
Tau.Boundary.b_times_c_zero
(z w : Polarity.SplitComplex)

(hz : in_b_ideal z)

(hw : in_c_ideal w)
 :spectral (z.mul w) = SectorPair.zero**


The B-ideal and C-ideal are orthogonal: their product is zero.
If z ∈ ker(χ₋) and w ∈ ker(χ₊), then z·w = 0 in sector coordinates.

---

### `Tau.Boundary.b_ideal_add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L115-L120)
**theorem
Tau.Boundary.b_ideal_add
(z w : Polarity.SplitComplex)

(hz : in_b_ideal z)

(hw : in_b_ideal w)
 :in_b_ideal (z.add w)**


The B-ideal is closed under addition.

---

### `Tau.Boundary.c_ideal_add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L122-L127)
**theorem
Tau.Boundary.c_ideal_add
(z w : Polarity.SplitComplex)

(hz : in_c_ideal z)

(hw : in_c_ideal w)
 :in_c_ideal (z.add w)**


The C-ideal is closed under addition.

---

### `Tau.Boundary.b_ideal_mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L129-L134)
**theorem
Tau.Boundary.b_ideal_mul
(z w : Polarity.SplitComplex)

(hz : in_b_ideal z)
 :in_b_ideal (z.mul w)**


The B-ideal is closed under multiplication.

---

### `Tau.Boundary.c_ideal_mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L136-L141)
**theorem
Tau.Boundary.c_ideal_mul
(z w : Polarity.SplitComplex)

(hz : in_c_ideal z)
 :in_c_ideal (z.mul w)**


The C-ideal is closed under multiplication.

---

### `Tau.Boundary.fourier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L147-L149)
**def
Tau.Boundary.fourier
(z : Polarity.SplitComplex)
 :Polarity.SectorPair**


[I.D40] The bipolar Fourier transform: maps z to its spectral decomposition.
This is the spectral transform repackaged as harmonic analysis.
Equations
- Tau.Boundary.fourier z = Tau.Boundary.spectral z
Instances For

---

### `Tau.Boundary.fourier_e_plus_sc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L151-L154)
**theorem
Tau.Boundary.fourier_e_plus_sc :fourier { re := 1, im := 1 } = { b_sector := 2, c_sector := 0 }**


Fourier transform of e₊ = (1,1) in split-complex: maps to pure B-sector.

---

### `Tau.Boundary.fourier_e_minus_sc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L156-L159)
**theorem
Tau.Boundary.fourier_e_minus_sc :fourier { re := 1, im := -1 } = { b_sector := 0, c_sector := 2 }**


Fourier transform of e₋ = (1,-1) in split-complex: maps to pure C-sector.

---

### `Tau.Boundary.fourier_e_plus_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L161-L164)
**theorem
Tau.Boundary.fourier_e_plus_sector
(z : Polarity.SplitComplex)
 :Polarity.e_plus_sector.mul (spectral z) = { b_sector := (spectral z).b_sector, c_sector := 0 }**


Fourier of the sector idempotent e₊: pure B-sector.

---

### `Tau.Boundary.fourier_e_minus_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L166-L169)
**theorem
Tau.Boundary.fourier_e_minus_sector
(z : Polarity.SplitComplex)
 :Polarity.e_minus_sector.mul (spectral z) = { b_sector := 0, c_sector := (spectral z).c_sector }**


Fourier of the sector idempotent e₋: pure C-sector.

---

### `Tau.Boundary.fourier_invertible`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L175-L178)
**theorem
Tau.Boundary.fourier_invertible
(z : Polarity.SplitComplex)
 :from_sectors (fourier z) = z**


Fourier inversion: the spectral transform can be inverted via from_sectors.

---

### `Tau.Boundary.fourier_injective`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L180-L183)
**theorem
Tau.Boundary.fourier_injective
(a b : Polarity.SplitComplex)

(h : fourier a = fourier b)
 :a = b**


The Fourier transform is injective.

---

### `Tau.Boundary.fourier_sigma_swap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L189-L193)
**theorem
Tau.Boundary.fourier_sigma_swap
(z : Polarity.SplitComplex)
 :fourier (Polarity.polarity_inv z) = { b_sector := (fourier z).c_sector, c_sector := (fourier z).b_sector }**


[I.D40] σ = component swap in Fourier coordinates: σ exchanges B ↔ C harmonics.

---

### `Tau.Boundary.sigma_fixed_iff_real`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L195-L206)
**theorem
Tau.Boundary.sigma_fixed_iff_real
(z : Polarity.SplitComplex)
 :Polarity.polarity_inv z = z ↔ z.im = 0**


Fourier-space characterization of fixed points of σ: z is σ-fixed iff z is real.

---

### `Tau.Boundary.sigma_anti_fixed_iff_imaginary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L208-L217)
**theorem
Tau.Boundary.sigma_anti_fixed_iff_imaginary
(z : Polarity.SplitComplex)
 :Polarity.polarity_inv z = z.neg ↔ z.re = 0**


Fourier-space characterization of anti-fixed points: polarity_inv z = -z iff z is pure imaginary.

---

### `Tau.Boundary.fourier_parseval`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Fourier.lean#L223-L226)
**theorem
Tau.Boundary.fourier_parseval
(z : Polarity.SplitComplex)
 :spectral_norm z = (fourier z).b_sector * (fourier z).c_sector**


A Parseval-type identity: the spectral norm equals the product of Fourier components.
N(z) = (Fourier B-component) · (Fourier C-component).
