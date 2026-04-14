---
layout: taulib-doc
title: "TauLib.BookIII.Arithmetic.RationalPoints"
permalink: /verify/taulib/docs/book-iii-arithmetic-rational-points/
lane: verify
module_name: "TauLib.BookIII.Arithmetic.RationalPoints"
book: "III"
book_label: "Spectrum"
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
    book: "Book III"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookIII.Arithmetic.RationalPoints


τ-Rational Point, Rank as Tower Depth, and Mordell-Weil Analogue.

## Registry Cross-References


- [III.D59] τ-Rational Point -- `TauRationalPoint`, `rational_point_check`

- [III.D60] Rank as Tower Depth -- `rank_as_depth`, `rank_check`

- [III.P25] Mordell-Weil Analogue -- `mordell_weil_check`


## Mathematical Content


**III.D59 (τ-Rational Point):** Address in ℤ̂_τ that stabilizes at finite
primorial depth with rational ABCD coordinates. A τ-rational point is an
element x such that its BNF stabilizes: BNF(x, k) = BNF(x, k+1) projected
to level k, for all k ≥ k₀.

**III.D60 (Rank as Tower Depth):** Minimal primorial depth at which the
τ-rational point group stabilizes. τ-analogue of Mordell-Weil rank.

**III.P25 (Mordell-Weil Analogue):** Group of τ-rational points is finitely
generated at each primorial level; rank stabilizes at finite depth.

---

### `Tau.BookIII.Arithmetic.TauRationalPoint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L40-L44)
**structure
Tau.BookIII.Arithmetic.TauRationalPoint :Type**


[III.D59] τ-rational point: stabilizes at finite primorial depth.

- value : Denotation.TauIdx
- stable_depth : Denotation.TauIdx
Instances For

---

### `Tau.BookIII.Arithmetic.instReprTauRationalPoint.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L44-L44)
**def
Tau.BookIII.Arithmetic.instReprTauRationalPoint.repr :TauRationalPoint → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.instReprTauRationalPoint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L44-L44)
**instance
Tau.BookIII.Arithmetic.instReprTauRationalPoint :Repr TauRationalPoint**

Equations
- Tau.BookIII.Arithmetic.instReprTauRationalPoint = { reprPrec := Tau.BookIII.Arithmetic.instReprTauRationalPoint.repr }

---

### `Tau.BookIII.Arithmetic.instDecidableEqTauRationalPoint.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L44-L44)
**def
Tau.BookIII.Arithmetic.instDecidableEqTauRationalPoint.decEq
(x✝ x✝¹ : TauRationalPoint)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.instDecidableEqTauRationalPoint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L44-L44)
**instance
Tau.BookIII.Arithmetic.instDecidableEqTauRationalPoint :DecidableEq TauRationalPoint**

Equations
- Tau.BookIII.Arithmetic.instDecidableEqTauRationalPoint = Tau.BookIII.Arithmetic.instDecidableEqTauRationalPoint.decEq

---

### `Tau.BookIII.Arithmetic.instBEqTauRationalPoint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L44-L44)
**instance
Tau.BookIII.Arithmetic.instBEqTauRationalPoint :BEq TauRationalPoint**

Equations
- Tau.BookIII.Arithmetic.instBEqTauRationalPoint = { beq := Tau.BookIII.Arithmetic.instBEqTauRationalPoint.beq }

---

### `Tau.BookIII.Arithmetic.instBEqTauRationalPoint.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L44-L44)
**def
Tau.BookIII.Arithmetic.instBEqTauRationalPoint.beq :TauRationalPoint → TauRationalPoint → Bool**

Equations
- Tau.BookIII.Arithmetic.instBEqTauRationalPoint.beq { value := a, stable_depth := a_1 }
 { value := b, stable_depth := b_1 } = (a == b && a_1 == b_1)
- Tau.BookIII.Arithmetic.instBEqTauRationalPoint.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIII.Arithmetic.is_rational_at`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L46-L60)
**def
Tau.BookIII.Arithmetic.is_rational_at
(x k : Denotation.TauIdx)
 :Bool**


[III.D59] Check if x is τ-rational at depth k: BNF is tower-compatible
at levels k and k+1.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.rational_point_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L62-L72)
**def
Tau.BookIII.Arithmetic.rational_point_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D59] τ-rational point check: all elements in range are rational.
Equations
- Tau.BookIII.Arithmetic.rational_point_check bound db = Tau.BookIII.Arithmetic.rational_point_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Arithmetic.rational_point_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L66-L71)@[irreducible]

**def
Tau.BookIII.Arithmetic.rational_point_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.rank_as_depth`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L78-L89)
**def
Tau.BookIII.Arithmetic.rank_as_depth
(x db : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D60] Rank of a τ-rational point: the minimal depth at which
the group operation stabilizes.
Equations
- Tau.BookIII.Arithmetic.rank_as_depth x db = Tau.BookIII.Arithmetic.rank_as_depth.go db x 1 (db + 1)
Instances For

---

### `Tau.BookIII.Arithmetic.rank_as_depth.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L83-L88)@[irreducible]

**def
Tau.BookIII.Arithmetic.rank_as_depth.go
(db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Denotation.TauIdx**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.rank_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L91-L100)
**def
Tau.BookIII.Arithmetic.rank_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D60] Rank check: all points have finite rank ≤ db.
Equations
- Tau.BookIII.Arithmetic.rank_check bound db = Tau.BookIII.Arithmetic.rank_check.go bound db 0 (bound + 1)
Instances For

---

### `Tau.BookIII.Arithmetic.rank_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L95-L99)@[irreducible]

**def
Tau.BookIII.Arithmetic.rank_check.go
(bound db : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.mordell_weil_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L106-L128)
**def
Tau.BookIII.Arithmetic.mordell_weil_check
(db : Denotation.TauIdx)
 :Bool**


[III.P25] Mordell-Weil analogue: the rational point group at level k
is finitely generated. Count: the number of rational points at each
level equals Prim(k) (all elements are rational in the canonical tower).
Equations
- Tau.BookIII.Arithmetic.mordell_weil_check db = Tau.BookIII.Arithmetic.mordell_weil_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Arithmetic.mordell_weil_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L112-L122)@[irreducible]

**def
Tau.BookIII.Arithmetic.mordell_weil_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.mordell_weil_check.count_rational`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L124-L128)@[irreducible]

**def
Tau.BookIII.Arithmetic.mordell_weil_check.count_rational
(x pk k : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.rank_stabilization_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L130-L143)
**def
Tau.BookIII.Arithmetic.rank_stabilization_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.P25] Rank stabilization: rank is non-decreasing across depths.
Equations
- Tau.BookIII.Arithmetic.rank_stabilization_check bound db = Tau.BookIII.Arithmetic.rank_stabilization_check.go bound db 0 (bound + 1)
Instances For

---

### `Tau.BookIII.Arithmetic.rank_stabilization_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L134-L142)@[irreducible]

**def
Tau.BookIII.Arithmetic.rank_stabilization_check.go
(bound db : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Arithmetic.rational_point_15_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L159-L160)
**theorem
Tau.BookIII.Arithmetic.rational_point_15_4 :rational_point_check 15 4 = true**


---

### `Tau.BookIII.Arithmetic.rank_15_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L162-L163)
**theorem
Tau.BookIII.Arithmetic.rank_15_5 :rank_check 15 5 = true**


---

### `Tau.BookIII.Arithmetic.mordell_weil_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L165-L166)
**theorem
Tau.BookIII.Arithmetic.mordell_weil_4 :mordell_weil_check 4 = true**


---

### `Tau.BookIII.Arithmetic.rank_stab_15_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L168-L169)
**theorem
Tau.BookIII.Arithmetic.rank_stab_15_5 :rank_stabilization_check 15 5 = true**


---

### `Tau.BookIII.Arithmetic.zero_rational`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L175-L177)
**theorem
Tau.BookIII.Arithmetic.zero_rational :is_rational_at 0 3 = true**


[III.D59] Structural: 0 is rational at every depth.

---

### `Tau.BookIII.Arithmetic.rank_bounded`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L179-L181)
**theorem
Tau.BookIII.Arithmetic.rank_bounded :rank_as_depth 42 5 ≤ 5**


[III.D60] Structural: rank is bounded by db.

---

### `Tau.BookIII.Arithmetic.all_rational_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Arithmetic/RationalPoints.lean#L183-L185)
**theorem
Tau.BookIII.Arithmetic.all_rational_1 :rational_point_check 10 1 = true**


[III.P25] Structural: all points rational at depth 1.
