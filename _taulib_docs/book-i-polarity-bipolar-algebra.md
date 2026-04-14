---
layout: taulib-doc
title: "TauLib.BookI.Polarity.BipolarAlgebra"
permalink: /verify/taulib/docs/book-i-polarity-bipolar-algebra/
lane: verify
module_name: "TauLib.BookI.Polarity.BipolarAlgebra"
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

# TauLib.Polarity.BipolarAlgebra


The bipolar spectral algebra H_τ with split-complex scalars.

## Registry Cross-References


- [I.D28] Boundary Local Ring — `BdryRing`

- [I.T10] Split-Complex Forced — `split_complex_forced`, `no_elliptic_idempotent`

- [I.D27] Bipolar Spectral Algebra — `SplitComplex`, `e_plus`, `e_minus`


## Ground Truth Sources


- chunk_0228_M002194: Split-complex algebra, bipolar balance, τ-RH scalar structure

- chunk_0310_M002679: Bipolar partition lifts to split-complex via Chi character


## Mathematical Content


The boundary local ring ℤ̂_τ = lim Z/M_k Z inherits componentwise ring structure.
Extending by the split-complex unit j (with j² = +1) gives the bipolar spectral
algebra H_τ = ℤ̂_τ[j].

The key theorem (I.T10): split-complex scalars (j² = +1) are FORCED by the bipolar
prime partition. The elliptic alternative (i² = -1) admits no nontrivial idempotents
over Z, so it cannot encode the bipolar structure.

The canonical idempotents e± = (1±j)/2 decompose H_τ into B-sector and C-sector,
mirroring the polarity partition of the primes.

---

### `Tau.Polarity.bdry_add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L42-L43)
**def
Tau.Polarity.bdry_add
(x y k : Denotation.TauIdx)
 :Denotation.TauIdx**


Boundary ring element at stage k: a pair of Z/M_kZ values (for add/mul).
Equations
- Tau.Polarity.bdry_add x y k = (x + y) % Tau.Polarity.primorial k
Instances For

---

### `Tau.Polarity.bdry_mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L44-L44)
**def
Tau.Polarity.bdry_mul
(x y k : Denotation.TauIdx)
 :Denotation.TauIdx**

Equations
- Tau.Polarity.bdry_mul x y k = x * y % Tau.Polarity.primorial k
Instances For

---

### `Tau.Polarity.bdry_neg`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L45-L45)
**def
Tau.Polarity.bdry_neg
(x k : Denotation.TauIdx)
 :Denotation.TauIdx**

Equations
- Tau.Polarity.bdry_neg x k = (Tau.Polarity.primorial k - x % Tau.Polarity.primorial k) % Tau.Polarity.primorial k
Instances For

---

### `Tau.Polarity.SplitComplex`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L51-L56)
**structure
Tau.Polarity.SplitComplex :Type**


[I.D27] Split-complex number: a + bj where j² = +1.
Represented as a pair of integers.

- re : ℤ
- im : ℤ
Instances For

---

### `Tau.Polarity.instDecidableEqSplitComplex`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L56-L56)
**instance
Tau.Polarity.instDecidableEqSplitComplex :DecidableEq SplitComplex**

Equations
- Tau.Polarity.instDecidableEqSplitComplex = Tau.Polarity.instDecidableEqSplitComplex.decEq

---

### `Tau.Polarity.instDecidableEqSplitComplex.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L56-L56)
**def
Tau.Polarity.instDecidableEqSplitComplex.decEq
(x✝ x✝¹ : SplitComplex)
 :Decidable (x✝ = x✝¹)**

Equations
- Tau.Polarity.instDecidableEqSplitComplex.decEq { re := a, im := a_1 } { re := b, im := b_1 } = if h : a = b then h ▸ if h : a_1 = b_1 then h ▸ isTrue ⋯ else isFalse ⋯ else isFalse ⋯
Instances For

---

### `Tau.Polarity.instReprSplitComplex`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L56-L56)
**instance
Tau.Polarity.instReprSplitComplex :Repr SplitComplex**

Equations
- Tau.Polarity.instReprSplitComplex = { reprPrec := Tau.Polarity.instReprSplitComplex.repr }

---

### `Tau.Polarity.instReprSplitComplex.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L56-L56)
**def
Tau.Polarity.instReprSplitComplex.repr :SplitComplex → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.instInhabitedSplitComplex`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L58-L58)
**instance
Tau.Polarity.instInhabitedSplitComplex :Inhabited SplitComplex**

Equations
- Tau.Polarity.instInhabitedSplitComplex = { default := { re := 0, im := 0 } }

---

### `Tau.Polarity.SplitComplex.zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L60-L61)
**def
Tau.Polarity.SplitComplex.zero :SplitComplex**


Split-complex zero.
Equations
- Tau.Polarity.SplitComplex.zero = { re := 0, im := 0 }
Instances For

---

### `Tau.Polarity.SplitComplex.one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L63-L64)
**def
Tau.Polarity.SplitComplex.one :SplitComplex**


Split-complex one.
Equations
- Tau.Polarity.SplitComplex.one = { re := 1, im := 0 }
Instances For

---

### `Tau.Polarity.SplitComplex.j`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L66-L67)
**def
Tau.Polarity.SplitComplex.j :SplitComplex**


The split-complex unit j.
Equations
- Tau.Polarity.SplitComplex.j = { re := 0, im := 1 }
Instances For

---

### `Tau.Polarity.SplitComplex.add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L69-L71)
**def
Tau.Polarity.SplitComplex.add
(a b : SplitComplex)
 :SplitComplex**


Split-complex addition.
Equations
- a.add b = { re := a.re + b.re, im := a.im + b.im }
Instances For

---

### `Tau.Polarity.SplitComplex.neg`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L73-L75)
**def
Tau.Polarity.SplitComplex.neg
(a : SplitComplex)
 :SplitComplex**


Split-complex negation.
Equations
- a.neg = { re := -a.re, im := -a.im }
Instances For

---

### `Tau.Polarity.SplitComplex.mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L77-L80)
**def
Tau.Polarity.SplitComplex.mul
(a b : SplitComplex)
 :SplitComplex**


Split-complex multiplication: (a + bj)(c + dj) = (ac + bd) + (ad + bc)j.
Uses j² = +1.
Equations
- a.mul b = { re := a.re * b.re + a.im * b.im, im := a.re * b.im + a.im * b.re }
Instances For

---

### `Tau.Polarity.SplitComplex.sub`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L82-L84)
**def
Tau.Polarity.SplitComplex.sub
(a b : SplitComplex)
 :SplitComplex**


Split-complex subtraction.
Equations
- a.sub b = a.add b.neg
Instances For

---

### `Tau.Polarity.j_squared`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L90-L92)
**theorem
Tau.Polarity.j_squared :SplitComplex.j.mul SplitComplex.j = SplitComplex.one**


j² = 1: the defining property of split-complex numbers.

---

### `Tau.Polarity.SectorPair`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L98-L103)
**structure
Tau.Polarity.SectorPair :Type**


[I.D27] Sector pair: the isomorphic representation (u, v) = (re + im, re - im).
In sector coordinates, multiplication is componentwise.

- b_sector : ℤ
- c_sector : ℤ
Instances For

---

### `Tau.Polarity.instDecidableEqSectorPair`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L103-L103)
**instance
Tau.Polarity.instDecidableEqSectorPair :DecidableEq SectorPair**

Equations
- Tau.Polarity.instDecidableEqSectorPair = Tau.Polarity.instDecidableEqSectorPair.decEq

---

### `Tau.Polarity.instDecidableEqSectorPair.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L103-L103)
**def
Tau.Polarity.instDecidableEqSectorPair.decEq
(x✝ x✝¹ : SectorPair)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.instReprSectorPair.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L103-L103)
**def
Tau.Polarity.instReprSectorPair.repr :SectorPair → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.instReprSectorPair`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L103-L103)
**instance
Tau.Polarity.instReprSectorPair :Repr SectorPair**

Equations
- Tau.Polarity.instReprSectorPair = { reprPrec := Tau.Polarity.instReprSectorPair.repr }

---

### `Tau.Polarity.to_sectors`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L105-L107)
**def
Tau.Polarity.to_sectors
(z : SplitComplex)
 :SectorPair**


Convert split-complex to sector representation.
Equations
- Tau.Polarity.to_sectors z = { b_sector := z.re + z.im, c_sector := z.re - z.im }
Instances For

---

### `Tau.Polarity.SectorPair.add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L109-L111)
**def
Tau.Polarity.SectorPair.add
(a b : SectorPair)
 :SectorPair**


Sector addition (componentwise).
Equations
- a.add b = { b_sector := a.b_sector + b.b_sector, c_sector := a.c_sector + b.c_sector }
Instances For

---

### `Tau.Polarity.SectorPair.mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L113-L115)
**def
Tau.Polarity.SectorPair.mul
(a b : SectorPair)
 :SectorPair**


Sector multiplication (componentwise).
Equations
- a.mul b = { b_sector := a.b_sector * b.b_sector, c_sector := a.c_sector * b.c_sector }
Instances For

---

### `Tau.Polarity.sectors_add`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L117-L122)
**theorem
Tau.Polarity.sectors_add
(a b : SplitComplex)
 :to_sectors (a.add b) = (to_sectors a).add (to_sectors b)**


Homomorphism check: to_sectors preserves addition.

---

### `Tau.Polarity.sectors_mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L124-L129)
**theorem
Tau.Polarity.sectors_mul
(a b : SplitComplex)
 :to_sectors (a.mul b) = (to_sectors a).mul (to_sectors b)**


Homomorphism check: to_sectors preserves multiplication.

---

### `Tau.Polarity.e_plus_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L135-L137)
**def
Tau.Polarity.e_plus_sector :SectorPair**


The B-sector idempotent e+ in sector coordinates: (1, 0).
In split-complex coordinates: e+ = (1+j)/2 (defined over Z[1/2]).
Equations
- Tau.Polarity.e_plus_sector = { b_sector := 1, c_sector := 0 }
Instances For

---

### `Tau.Polarity.e_minus_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L139-L140)
**def
Tau.Polarity.e_minus_sector :SectorPair**


The C-sector idempotent e- in sector coordinates: (0, 1).
Equations
- Tau.Polarity.e_minus_sector = { b_sector := 0, c_sector := 1 }
Instances For

---

### `Tau.Polarity.e_plus_idem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L142-L144)
**theorem
Tau.Polarity.e_plus_idem :e_plus_sector.mul e_plus_sector = e_plus_sector**


e+² = e+ (idempotent).

---

### `Tau.Polarity.e_minus_idem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L146-L148)
**theorem
Tau.Polarity.e_minus_idem :e_minus_sector.mul e_minus_sector = e_minus_sector**


e-² = e- (idempotent).

---

### `Tau.Polarity.e_orthogonal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L150-L153)
**theorem
Tau.Polarity.e_orthogonal :e_plus_sector.mul e_minus_sector = { b_sector := 0, c_sector := 0 }**


e+ · e- = 0 (orthogonal).

---

### `Tau.Polarity.e_partition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L155-L158)
**theorem
Tau.Polarity.e_partition :e_plus_sector.add e_minus_sector = { b_sector := 1, c_sector := 1 }**


e+ + e- = 1 (partition of unity).

---

### `Tau.Polarity.GaussInt`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L164-L169)
**structure
Tau.Polarity.GaussInt :Type**


An "elliptic" number: a + bi where i² = -1.
We represent as integer pairs (Gaussian integers).

- re : ℤ
- im : ℤ
Instances For

---

### `Tau.Polarity.instDecidableEqGaussInt.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L169-L169)
**def
Tau.Polarity.instDecidableEqGaussInt.decEq
(x✝ x✝¹ : GaussInt)
 :Decidable (x✝ = x✝¹)**

Equations
- Tau.Polarity.instDecidableEqGaussInt.decEq { re := a, im := a_1 } { re := b, im := b_1 } = if h : a = b then h ▸ if h : a_1 = b_1 then h ▸ isTrue ⋯ else isFalse ⋯ else isFalse ⋯
Instances For

---

### `Tau.Polarity.instDecidableEqGaussInt`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L169-L169)
**instance
Tau.Polarity.instDecidableEqGaussInt :DecidableEq GaussInt**

Equations
- Tau.Polarity.instDecidableEqGaussInt = Tau.Polarity.instDecidableEqGaussInt.decEq

---

### `Tau.Polarity.instReprGaussInt.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L169-L169)
**def
Tau.Polarity.instReprGaussInt.repr :GaussInt → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.instReprGaussInt`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L169-L169)
**instance
Tau.Polarity.instReprGaussInt :Repr GaussInt**

Equations
- Tau.Polarity.instReprGaussInt = { reprPrec := Tau.Polarity.instReprGaussInt.repr }

---

### `Tau.Polarity.GaussInt.mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L171-L174)
**def
Tau.Polarity.GaussInt.mul
(a b : GaussInt)
 :GaussInt**


Gaussian integer multiplication: (a+bi)(c+di) = (ac-bd) + (ad+bc)i.
Uses i² = -1.
Equations
- a.mul b = { re := a.re * b.re - a.im * b.im, im := a.re * b.im + a.im * b.re }
Instances For

---

### `Tau.Polarity.GaussInt.ext`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L176-L178)
**theorem
Tau.Polarity.GaussInt.ext
{a b : GaussInt}

(hre : a.re = b.re)

(him : a.im = b.im)
 :a = b**


---

### `Tau.Polarity.GaussInt.ext_iff`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L176-L176)
**theorem
Tau.Polarity.GaussInt.ext_iff
{a b : GaussInt}
 :a = b ↔ a.re = b.re ∧ a.im = b.im**


---

### `Tau.Polarity.no_elliptic_idempotent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L193-L224)
**theorem
Tau.Polarity.no_elliptic_idempotent
(z : GaussInt)

(h : z.mul z = z)
 :z = { re := 0, im := 0 } ∨ z = { re := 1, im := 0 }**


[I.T10] No nontrivial idempotent in the Gaussian integers:
if (a+bi)² = (a+bi) over Z, then (a,b) = (0,0) or (a,b) = (1,0).

Proof: From (a+bi)² = a+bi:


- Real part: a² - b² = a

- Imaginary part: 2ab = b
From 2ab = b: either b = 0 or 2a = 1 (impossible in Z).
If b = 0: a² = a, so a(a-1) = 0, hence a = 0 or a = 1.


---

### `Tau.Polarity.split_complex_forced`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L226-L237)
**theorem
Tau.Polarity.split_complex_forced :(∃ (e : SectorPair), e.mul e = e ∧ e ≠ { b_sector := 0, c_sector := 0 } ∧ e ≠ { b_sector := 1, c_sector := 1 }) ∧ ∀ (z : GaussInt), z.mul z = z → z = { re := 0, im := 0 } ∨ z = { re := 1, im := 0 }**


[I.T10] Split-complex forced: the split-complex algebra (j² = +1) admits
nontrivial idempotents (e+, e-), while the elliptic algebra (i² = -1) does not.
Therefore, encoding a bipolar partition requires j² = +1.

---

### `Tau.Polarity.polarity_inv`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L243-L244)
**def
Tau.Polarity.polarity_inv
(z : SplitComplex)
 :SplitComplex**


The polarity involution σ: j ↦ -j, i.e., (a, b) ↦ (a, -b).
Equations
- Tau.Polarity.polarity_inv z = { re := z.re, im := -z.im }
Instances For

---

### `Tau.Polarity.polarity_inv_squared`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L246-L249)
**theorem
Tau.Polarity.polarity_inv_squared
(z : SplitComplex)
 :polarity_inv (polarity_inv z) = z**


σ² = id.

---

### `Tau.Polarity.polarity_inv_fixes_real`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L251-L254)
**theorem
Tau.Polarity.polarity_inv_fixes_real
(a : ℤ)
 :polarity_inv { re := a, im := 0 } = { re := a, im := 0 }**


σ fixes the real part.

---

### `Tau.Polarity.polarity_inv_j`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L256-L259)
**theorem
Tau.Polarity.polarity_inv_j :polarity_inv SplitComplex.j = SplitComplex.j.neg**


σ(j) = -j.

---

### `Tau.Polarity.polarity_inv_swaps_sectors`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L261-L266)
**theorem
Tau.Polarity.polarity_inv_swaps_sectors
(z : SplitComplex)
 :to_sectors (polarity_inv z) = { b_sector := (to_sectors z).c_sector, c_sector := (to_sectors z).b_sector }**


σ swaps sectors: σ maps (u, v) to (v, u) in sector coordinates.

---

### `Tau.Polarity.chi_split`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L272-L281)
**def
Tau.Polarity.chi_split
(p N : Denotation.TauIdx)
 :SectorPair**


[chunk_0228] Split-complex lift of the polarity character.
Maps the Int-valued polarity_chi to sector idempotents:


- B-dominant (chi = -1) → e_plus_sector = (1, 0)

- C-dominant (chi = +1) → e_minus_sector = (0, 1)

- non-prime (chi = 0) → (0, 0)
Ground truth: chunk_0228_M002194 — χ̃(p) ∈ {e⁻, e⁺}.

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.chi_split_idempotent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L283-L291)
**theorem
Tau.Polarity.chi_split_idempotent
(p N : Denotation.TauIdx)
 :(chi_split p N).mul (chi_split p N) = chi_split p N**


chi_split is idempotent-valued: the output squares to itself.

---

### `Tau.Polarity.chi_split_of_b`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L293-L296)
**theorem
Tau.Polarity.chi_split_of_b
(p N : Denotation.TauIdx)

(h : polarity_chi p N = -1)
 :chi_split p N = e_plus_sector**


Bridge theorem: polarity_chi = -1 implies chi_split = e_plus_sector.

---

### `Tau.Polarity.chi_split_of_c`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L298-L301)
**theorem
Tau.Polarity.chi_split_of_c
(p N : Denotation.TauIdx)

(h : polarity_chi p N = 1)
 :chi_split p N = e_minus_sector**


Bridge theorem: polarity_chi = +1 implies chi_split = e_minus_sector.

---

### `Tau.Polarity.chi_split_orthogonal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/BipolarAlgebra.lean#L303-L309)
**theorem
Tau.Polarity.chi_split_orthogonal
(p q N : Denotation.TauIdx)

(hp : polarity_chi p N = -1)

(hq : polarity_chi q N = 1)
 :(chi_split p N).mul (chi_split q N) = { b_sector := 0, c_sector := 0 }**


The two character representations are orthogonal:
chi_split for B-dominant and C-dominant primes give orthogonal sectors.
