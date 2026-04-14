---
layout: taulib-doc
title: "TauLib.BookII.Interior.ABCDRigidity"
permalink: /verify/taulib/docs/book-ii-interior-abcd-rigidity/
lane: verify
module_name: "TauLib.BookII.Interior.ABCDRigidity"
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

# TauLib.BookII.Interior.ABCDRigidity


ABCD four-ray rigidity: the four rays (A, B, C, D) provide complete
and rigid coordinate structure for holomorphic analysis on τ³.

## Registry Cross-References


- [II.R04] ABCD vs Quaternions — comparison (remarks only)

- [II.P03] Four-Ray Rigidity — `four_ray_complete`, `four_ray_bipolar`


## Mathematical Content


The ABCD chart replaces quaternionic structure:


Feature
Quaternionic (ℍ)
ABCD


Scalars
ℍ, dim 4, noncommutative
H_τ = Ẑ_τ[j], commutative


Imaginary
i²=j²=k²=-1
j²=+1 (split-complex)


Zero divisors
None (division algebra)
e₊·e₋ = 0 (bipolar)


Coordinates
ℝ⁴ (two-sided axes)
ℕ⁴ (one-sided rays)


Bipolarity
Not native
Native (e₊, e₋ sectors)


Status in τ
Not earned (imported)
Earned (from K0-K6)


Four-ray rigidity (II.P03):

- Completeness: every Obj(τ) gets a unique ABCD quadruple (I.T04)

- Bipolar compatibility: (B,C) carry sector assignment

- Coherence: fibered product interlocks four rays

- No imports: earned from kernel axioms


---

### `Tau.BookII.Interior.four_ray_complete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/ABCDRigidity.lean#L42-L46)
**def
Tau.BookII.Interior.four_ray_complete
(bound : Denotation.TauIdx)
 :Bool**


[II.P03, clause 1] Completeness:
The ABCD chart assigns a unique quadruple to every X ≥ 2.
Verified by injectivity (no collisions) for X = 2..bound.
Equations
- Tau.BookII.Interior.four_ray_complete bound = Tau.BookII.Interior.faithful_check bound
Instances For

---

### `Tau.BookII.Interior.four_ray_bipolar_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/ABCDRigidity.lean#L48-L67)
**def
Tau.BookII.Interior.four_ray_bipolar_check
(bound : Denotation.TauIdx)
 :Bool**


[II.P03, clause 2] Bipolar compatibility:
Fiber coordinates (B,C) carry sector assignment compatible with
the idempotent decomposition of H_τ.

For all X in range: interior_bipolar produces orthogonal projections.
Equations
- Tau.BookII.Interior.four_ray_bipolar_check bound = Tau.BookII.Interior.four_ray_bipolar_check.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Interior.four_ray_bipolar_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/ABCDRigidity.lean#L56-L66)@[irreducible]

**def
Tau.BookII.Interior.four_ray_bipolar_check.go
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.four_ray_coherent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/ABCDRigidity.lean#L69-L82)
**def
Tau.BookII.Interior.four_ray_coherent
(bound : Denotation.TauIdx)
 :Bool**


[II.P03, clause 3] Coherence:
The fibered product structure interlocks all four rays.
Verified: base validity (C1, C3) holds for all ABCD decompositions.
Equations
- Tau.BookII.Interior.four_ray_coherent bound = Tau.BookII.Interior.four_ray_coherent.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Interior.four_ray_coherent.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/ABCDRigidity.lean#L75-L81)@[irreducible]

**def
Tau.BookII.Interior.four_ray_coherent.go
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.four_starting_primes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/ABCDRigidity.lean#L88-L93)
**def
Tau.BookII.Interior.four_starting_primes :List Denotation.TauIdx**


[II.R04] Key structural difference: ABCD uses one-sided rays (ℕ),
not two-sided axes (ℝ). Rays have a starting prime but no origin.

The four starting primes are distinct:
α₁ = 2, π₁ = 3, γ₁ = 5, η₁ = 7.
Equations
- Tau.BookII.Interior.four_starting_primes = [2, 3, 5, 7]
Instances For

---

### `Tau.BookII.Interior.starting_primes_distinct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/ABCDRigidity.lean#L95-L98)
**def
Tau.BookII.Interior.starting_primes_distinct :Bool**


The four starting primes are all distinct.
Equations
- Tau.BookII.Interior.starting_primes_distinct = (Tau.BookII.Interior.four_starting_primes.length == 4 && Tau.BookII.Interior.four_starting_primes.eraseDups.length == 4)
Instances For

---

### `Tau.BookII.Interior.starting_primes_all_prime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/ABCDRigidity.lean#L100-L102)
**def
Tau.BookII.Interior.starting_primes_all_prime :Bool**


The four starting primes are all prime.
Equations
- Tau.BookII.Interior.starting_primes_all_prime = Tau.BookII.Interior.four_starting_primes.all Tau.Coordinates.is_prime_bool
Instances For

---

### `Tau.BookII.Interior.abcd_has_zero_divisors`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/ABCDRigidity.lean#L104-L114)
**theorem
Tau.BookII.Interior.abcd_has_zero_divisors :∃ (z : Polarity.SplitComplex), ∃ (w : Polarity.SplitComplex), z ≠ { re := 0, im := 0 } ∧ w ≠ { re := 0, im := 0 } ∧ z.mul w = { re := 0, im := 0 }**


[II.R04] Split-complex has zero divisors; quaternions don't.
This is the key algebraic difference: H_τ admits bipolar sectors
via e₊ · e₋ = 0, while ℍ is a division algebra.

---

### `Tau.BookII.Interior.para_complex_structure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/ABCDRigidity.lean#L120-L129)
**theorem
Tau.BookII.Interior.para_complex_structure :{ re := 0, im := 1 }.mul { re := 0, im := 1 } = { re := 1, im := 0 }**


The ABCD chart induces a para-complex structure (j² = +id),
not a complex structure (J² = -id).

Para-complex: decomposes into two REAL eigenspaces (e₊ ⊕ e₋).
Complex: rotates between two components (no real eigenspaces).

Verification: j² = +1 in split-complex arithmetic.

---

### `Tau.BookII.Interior.rigidity_2_to_30`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/ABCDRigidity.lean#L145-L145)
**theorem
Tau.BookII.Interior.rigidity_2_to_30 :four_ray_complete 30 = true**


---

### `Tau.BookII.Interior.bipolar_2_to_30`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/ABCDRigidity.lean#L146-L146)
**theorem
Tau.BookII.Interior.bipolar_2_to_30 :four_ray_bipolar_check 30 = true**


---

### `Tau.BookII.Interior.coherent_2_to_30`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/ABCDRigidity.lean#L147-L147)
**theorem
Tau.BookII.Interior.coherent_2_to_30 :four_ray_coherent 30 = true**


---

### `Tau.BookII.Interior.primes_distinct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/ABCDRigidity.lean#L148-L148)
**theorem
Tau.BookII.Interior.primes_distinct :starting_primes_distinct = true**


---

### `Tau.BookII.Interior.primes_all_prime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/ABCDRigidity.lean#L149-L149)
**theorem
Tau.BookII.Interior.primes_all_prime :starting_primes_all_prime = true**
