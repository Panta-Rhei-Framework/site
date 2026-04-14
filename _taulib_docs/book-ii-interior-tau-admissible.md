---
layout: taulib-doc
title: "TauLib.BookII.Interior.TauAdmissible"
permalink: /verify/taulib/docs/book-ii-interior-tau-admissible/
lane: verify
module_name: "TauLib.BookII.Interior.TauAdmissible"
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

# TauLib.BookII.Interior.TauAdmissible


τ-admissible points: the coordinate space of τ³.

## Registry Cross-References


- [II.D02] τ-Admissible Point — `TauAdmissiblePoint`, `from_tau_idx`

- [II.D03] Constraint Lattice — `constraint_C1` .. `constraint_C5`

- [II.T01] Point Set Well-Defined — `round_trip_check`, `admissible_check`


## Mathematical Content


A τ-admissible point is a quadruple (A, B, C, D) ∈ τ-Idx⁴ satisfying:


- C1: A ∈ ℙ_τ ∪ {1} (prime or unity)

- C2: B, C, D ≥ 0 (non-negativity; automatic for ℕ)

- C3: every prime factor of D is strictly < A

- C4: if A = 1 then B = 0 and C = 0

- C5: normalization (greedy peel consistency)


The point set τ³ := τ³_fin ∪ τ³_lim is well-defined:


- τ³_fin bijects with Obj(τ) via the ABCD chart Φ

- τ³_lim is non-empty (primorial tower)

- τ³ is closed under CRT reduction


---

### `Tau.BookII.Interior.constraint_C1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L38-L40)
**def
Tau.BookII.Interior.constraint_C1
(a : Denotation.TauIdx)
 :Bool**


[II.D03/C1] Prime constraint: A is prime or 1.
Equations
- Tau.BookII.Interior.constraint_C1 a = (Tau.Coordinates.is_prime_bool a || a == 1)
Instances For

---

### `Tau.BookII.Interior.largest_prime_factor_aux`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L42-L52)@[irreducible]

**def
Tau.BookII.Interior.largest_prime_factor_aux
(n d best fuel : Nat)
 :Nat**


[II.D03/C3] Remainder constraint: largest prime factor of D < A.
Returns true if all prime factors of d are strictly less than bound.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.largest_prime_factor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L54-L57)
**def
Tau.BookII.Interior.largest_prime_factor
(n : Denotation.TauIdx)
 :Denotation.TauIdx**


Largest prime factor of n, or 0 if n ≤ 1.
Equations
- Tau.BookII.Interior.largest_prime_factor n = if n ≤ 1 then 0 else Tau.BookII.Interior.largest_prime_factor_aux n 2 0 n
Instances For

---

### `Tau.BookII.Interior.constraint_C3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L59-L61)
**def
Tau.BookII.Interior.constraint_C3
(d a : Denotation.TauIdx)
 :Bool**


[II.D03/C3] Every prime factor of D is strictly < A.
Equations
- Tau.BookII.Interior.constraint_C3 d a = (decide (d ≤ 1) || decide (Tau.BookII.Interior.largest_prime_factor d < a))
Instances For

---

### `Tau.BookII.Interior.constraint_C4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L63-L65)
**def
Tau.BookII.Interior.constraint_C4
(a b c : Denotation.TauIdx)
 :Bool**


[II.D03/C4] Tower constraint: if A = 1 then B = C = 0.
Equations
- Tau.BookII.Interior.constraint_C4 a b c = if (a == 1) = true then b == 0 && c == 0 else true
Instances For

---

### `Tau.BookII.Interior.constraint_C5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L67-L73)
**def
Tau.BookII.Interior.constraint_C5
(a b c d : Denotation.TauIdx)
 :Bool**


[II.D03/C5] Normalization: round-trip through abcd_chart is consistent.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.is_tau_admissible`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L75-L77)
**def
Tau.BookII.Interior.is_tau_admissible
(a b c d : Denotation.TauIdx)
 :Bool**


[II.D03] Full constraint lattice check for a candidate (A, B, C, D).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.TauAdmissiblePoint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L83-L91)
**structure
Tau.BookII.Interior.TauAdmissiblePoint :Type**


[II.D02] A τ-admissible point: ABCD quadruple from the greedy peel
decomposition. Every object X ∈ Obj(τ) has a unique such representation
via the Hyperfactorization Theorem (I.T04).

- a : Denotation.TauIdx
- b : Denotation.TauIdx
- c : Denotation.TauIdx
- d : Denotation.TauIdx
Instances For

---

### `Tau.BookII.Interior.instReprTauAdmissiblePoint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L91-L91)
**instance
Tau.BookII.Interior.instReprTauAdmissiblePoint :Repr TauAdmissiblePoint**

Equations
- Tau.BookII.Interior.instReprTauAdmissiblePoint = { reprPrec := Tau.BookII.Interior.instReprTauAdmissiblePoint.repr }

---

### `Tau.BookII.Interior.instReprTauAdmissiblePoint.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L91-L91)
**def
Tau.BookII.Interior.instReprTauAdmissiblePoint.repr :TauAdmissiblePoint → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.instDecidableEqTauAdmissiblePoint.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L91-L91)
**def
Tau.BookII.Interior.instDecidableEqTauAdmissiblePoint.decEq
(x✝ x✝¹ : TauAdmissiblePoint)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.instDecidableEqTauAdmissiblePoint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L91-L91)
**instance
Tau.BookII.Interior.instDecidableEqTauAdmissiblePoint :DecidableEq TauAdmissiblePoint**

Equations
- Tau.BookII.Interior.instDecidableEqTauAdmissiblePoint = Tau.BookII.Interior.instDecidableEqTauAdmissiblePoint.decEq

---

### `Tau.BookII.Interior.from_tau_idx`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L93-L96)
**def
Tau.BookII.Interior.from_tau_idx
(x : Denotation.TauIdx)
 :TauAdmissiblePoint**


Construct τ-admissible point from a τ-index via the ABCD chart.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.to_tau_idx`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L98-L100)
**def
Tau.BookII.Interior.to_tau_idx
(p : TauAdmissiblePoint)
 :Denotation.TauIdx**


Reconstruct τ-index from an admissible point: T(A,B,C) · D.
Equations
- Tau.BookII.Interior.to_tau_idx p = Tau.Coordinates.tower_atom p.a p.b p.c * p.d
Instances For

---

### `Tau.BookII.Interior.TauAdmissiblePoint.valid`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L102-L104)
**def
Tau.BookII.Interior.TauAdmissiblePoint.valid
(p : TauAdmissiblePoint)
 :Bool**


Check that a TauAdmissiblePoint satisfies all constraints.
Equations
- p.valid = Tau.BookII.Interior.is_tau_admissible p.a p.b p.c p.d
Instances For

---

### `Tau.BookII.Interior.round_trip_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L110-L113)
**def
Tau.BookII.Interior.round_trip_check
(x : Denotation.TauIdx)
 :Bool**


[II.T01, clause 1] Round-trip: from_tau_idx ∘ to_tau_idx is consistent
with chart_value.
Equations
- Tau.BookII.Interior.round_trip_check x = (Tau.BookII.Interior.to_tau_idx (Tau.BookII.Interior.from_tau_idx x) == x)
Instances For

---

### `Tau.BookII.Interior.admissible_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L115-L118)
**def
Tau.BookII.Interior.admissible_check
(x : Denotation.TauIdx)
 :Bool**


[II.T01, clause 1] Admissibility: ABCD chart always produces admissible
quadruples.
Equations
- Tau.BookII.Interior.admissible_check x = (Tau.BookII.Interior.from_tau_idx x).valid
Instances For

---

### `Tau.BookII.Interior.batch_verify`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L120-L128)
**def
Tau.BookII.Interior.batch_verify
(bound : Denotation.TauIdx)
 :Bool**


[II.T01, clause 1] Batch verification for X = 2..bound.
Equations
- Tau.BookII.Interior.batch_verify bound = Tau.BookII.Interior.batch_verify.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Interior.batch_verify.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L124-L127)@[irreducible]

**def
Tau.BookII.Interior.batch_verify.go
(bound : Denotation.TauIdx)

(start fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.primorial_witness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L134-L141)
**def
Tau.BookII.Interior.primorial_witness :List (Denotation.TauIdx × TauAdmissiblePoint)**


Primorial P_k = p₁ · p₂ · ... · p_k.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.primorial_b_eq_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L143-L145)
**def
Tau.BookII.Interior.primorial_b_eq_one :Bool**


Primorial readouts have A = p_k, B = 1, C = 1, D = P_{k-1}.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.primorial_c_eq_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L147-L148)
**def
Tau.BookII.Interior.primorial_c_eq_one :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.primorial_a_increasing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L150-L153)
**def
Tau.BookII.Interior.primorial_a_increasing :Bool**


Primorial A-values form an increasing sequence of primes.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.admissible_2_to_20`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/TauAdmissible.lean#L198-L198)
**theorem
Tau.BookII.Interior.admissible_2_to_20 :batch_verify 20 = true**
