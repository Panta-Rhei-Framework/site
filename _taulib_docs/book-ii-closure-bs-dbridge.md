---
layout: taulib-doc
title: "TauLib.BookII.Closure.BSDbridge"
permalink: /verify/taulib/docs/book-ii-closure-bs-dbridge/
lane: verify
module_name: "TauLib.BookII.Closure.BSDbridge"
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

# TauLib.BookII.Closure.BSDbridge


Proto-rationality: the finite-stage-determined points of the primorial tower.

## Registry Cross-References


- [II.D65] Proto-Rationality -- `is_proto_rational`, `proto_rational_check`,
`proto_rational_examples_check`


## Mathematical Content


**II.D65 (Proto-Rationality):** A point x is proto-rational if:

- x > 1 (nontrivial), and

- There exists a stage k such that reduce(x, k) = x (the point is
determined at a finite stage -- it lives entirely within Z/P_kZ).


The proto-rational points are the "algebraic" points of the primorial
tower: they are determined by finitely many prime residues. Points that
are NOT proto-rational would require the full inverse limit (infinitely
many prime residues) to specify -- these are the "transcendental" points
in the tower's number-theoretic sense.

Proto-rationality connects to BSD because:


- Rational points on an elliptic curve are finitely determined

- Proto-rational points in the primorial tower are finitely determined

- The rank of the Mordell-Weil group measures how many independent
rational points exist -- analogously, the count of proto-rational
points at each stage measures the arithmetic complexity


**Examples:**


- x = 2 is proto-rational: reduce(2, 2) = 2 (since P_2 = 6 > 2)

- x = 5 is proto-rational: reduce(5, 3) = 5 (since P_3 = 30 > 5)

- x = 0 is NOT proto-rational: x > 1 required

- x = 1 is NOT proto-rational: x > 1 required


---

### `Tau.BookII.Closure.is_proto_rational`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L51-L62)
**def
Tau.BookII.Closure.is_proto_rational
(x max_k : Denotation.TauIdx)
 :Bool**


[II.D65] Check if a point x is proto-rational: x > 1 and there exists
a stage k (searched up to max_k) such that reduce(x, k) = x.
Equations
- Tau.BookII.Closure.is_proto_rational x max_k = if x ≤ 1 then false else Tau.BookII.Closure.is_proto_rational.find_stage max_k x 1 (max_k + 1)
Instances For

---

### `Tau.BookII.Closure.is_proto_rational.find_stage`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L57-L61)@[irreducible]

**def
Tau.BookII.Closure.is_proto_rational.find_stage
(max_k : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.proto_rational_stage`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L64-L75)
**def
Tau.BookII.Closure.proto_rational_stage
(x max_k : Denotation.TauIdx)
 :Denotation.TauIdx**


[II.D65] Find the smallest stage k at which x is determined.
Returns 0 if x is not proto-rational within max_k stages.
Equations
- Tau.BookII.Closure.proto_rational_stage x max_k = if x ≤ 1 then 0 else Tau.BookII.Closure.proto_rational_stage.find_min_stage max_k x 1 (max_k + 1)
Instances For

---

### `Tau.BookII.Closure.proto_rational_stage.find_min_stage`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L70-L74)@[irreducible]

**def
Tau.BookII.Closure.proto_rational_stage.find_min_stage
(max_k : Denotation.TauIdx)

(x k fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.proto_rational_abcd`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L77-L81)
**def
Tau.BookII.Closure.proto_rational_abcd
(x : Denotation.TauIdx)
 :Interior.TauAdmissiblePoint**


[II.D65] ABCD structure of a proto-rational point.
For proto-rational x, from_tau_idx(x) gives the ABCD coordinates,
and the A-coordinate indicates the prime direction.
Equations
- Tau.BookII.Closure.proto_rational_abcd x = Tau.BookII.Interior.from_tau_idx x
Instances For

---

### `Tau.BookII.Closure.proto_rational_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L83-L94)
**def
Tau.BookII.Closure.proto_rational_check
(bound max_k : Denotation.TauIdx)
 :Bool**


[II.D65] Proto-rationality verification for a range [2, bound].
Check that every x in the range is proto-rational (which is true
for all finite x, since reduce(x, k) = x whenever P_k > x).
Equations
- Tau.BookII.Closure.proto_rational_check bound max_k = Tau.BookII.Closure.proto_rational_check.go bound max_k 2 (bound + 1)
Instances For

---

### `Tau.BookII.Closure.proto_rational_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L89-L93)@[irreducible]

**def
Tau.BookII.Closure.proto_rational_check.go
(bound max_k : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.proto_rational_examples_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L96-L110)
**def
Tau.BookII.Closure.proto_rational_examples_check :Bool**


[II.D65] Proto-rational examples check: verify specific examples.


- x = 2 is proto-rational at stage 2 (P_2 = 6 > 2)

- x = 5 is proto-rational at stage 2 (P_2 = 6 > 5)

- x = 7 is proto-rational at stage 3 (P_3 = 30 > 7)

- x = 12 is proto-rational at stage 3 (P_3 = 30 > 12)

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.proto_rational_count_at_stage`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L112-L132)
**def
Tau.BookII.Closure.proto_rational_count_at_stage
(k : Denotation.TauIdx)
 :Denotation.TauIdx**


[II.D65] Proto-rational count at stage k: the number of proto-rational
points determined at exactly stage k (i.e., reduce(x, k) = x but
reduce(x, k-1) != x, for x > 1).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.proto_rational_count_at_stage.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L122-L131)@[irreducible]

**def
Tau.BookII.Closure.proto_rational_count_at_stage.go
(k : Denotation.TauIdx)

(pk pk_prev x count fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Closure.proto_rational_count_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L134-L143)
**def
Tau.BookII.Closure.proto_rational_count_check :Bool**


Proto-rational count check: at stage 1 (P_1 = 2), no points are
newly determined (x=0 and x=1 are excluded by x > 1 condition,
but reduce(0, 0) = 0 and reduce(1, 0) = 0, so stage 0 already
captures them). Actually at stage 1, x = 0 has reduce(0, 0) = 0 = x
but x <= 1, so not counted. x = 1 is also <= 1.
At stage 2 (P_2 = 6): points 2, 3, 4, 5 are new (reduce(x, 1) != x
for x >= 2 since P_1 = 2).
Equations
- Tau.BookII.Closure.proto_rational_count_check = (Tau.BookII.Closure.proto_rational_count_at_stage 2 == 4 && decide (Tau.BookII.Closure.proto_rational_count_at_stage 3 ≥ 10))
Instances For

---

### `Tau.BookII.Closure.proto_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L185-L186)
**theorem
Tau.BookII.Closure.proto_2 :is_proto_rational 2 5 = true**


---

### `Tau.BookII.Closure.proto_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L188-L189)
**theorem
Tau.BookII.Closure.proto_5 :is_proto_rational 5 5 = true**


---

### `Tau.BookII.Closure.proto_7`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L191-L192)
**theorem
Tau.BookII.Closure.proto_7 :is_proto_rational 7 5 = true**


---

### `Tau.BookII.Closure.proto_12`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L194-L195)
**theorem
Tau.BookII.Closure.proto_12 :is_proto_rational 12 5 = true**


---

### `Tau.BookII.Closure.not_proto_0`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L198-L199)
**theorem
Tau.BookII.Closure.not_proto_0 :is_proto_rational 0 5 = false**


---

### `Tau.BookII.Closure.not_proto_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L201-L202)
**theorem
Tau.BookII.Closure.not_proto_1 :is_proto_rational 1 5 = false**


---

### `Tau.BookII.Closure.stage_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L205-L206)
**theorem
Tau.BookII.Closure.stage_2 :proto_rational_stage 2 5 = 2**


---

### `Tau.BookII.Closure.stage_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L208-L209)
**theorem
Tau.BookII.Closure.stage_5 :proto_rational_stage 5 5 = 2**


---

### `Tau.BookII.Closure.stage_7`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L211-L212)
**theorem
Tau.BookII.Closure.stage_7 :proto_rational_stage 7 5 = 3**


---

### `Tau.BookII.Closure.proto_examples`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L215-L216)
**theorem
Tau.BookII.Closure.proto_examples :proto_rational_examples_check = true**


---

### `Tau.BookII.Closure.proto_range_30`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L219-L220)
**theorem
Tau.BookII.Closure.proto_range_30 :proto_rational_check 30 5 = true**


---

### `Tau.BookII.Closure.proto_count_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L223-L224)
**theorem
Tau.BookII.Closure.proto_count_check :proto_rational_count_check = true**


---

### `Tau.BookII.Closure.finite_is_proto_rational_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L230-L233)
**theorem
Tau.BookII.Closure.finite_is_proto_rational_2 :is_proto_rational 2 5 = true**


[II.D65] Every finite x > 1 is proto-rational at a sufficiently large stage.
If P_k > x, then reduce(x, k) = x % P_k = x. Verified for x = 2.

---

### `Tau.BookII.Closure.proto_at_stage`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L235-L240)
**theorem
Tau.BookII.Closure.proto_at_stage
(x k : Denotation.TauIdx)

(h : x < Polarity.primorial k)
 :Polarity.reduce x k = x**


[II.D65] Proto-rationality is stable: if x < P_k, then reduce(x, k) = x.
This follows from x % P_k = x when x < P_k.

---

### `Tau.BookII.Closure.proto_abcd_roundtrip_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L242-L245)
**theorem
Tau.BookII.Closure.proto_abcd_roundtrip_2 :Interior.to_tau_idx (proto_rational_abcd 2) = 2**


[II.D65] The ABCD chart of a proto-rational point round-trips.
to_tau_idx(proto_rational_abcd(x)) = x.

---

### `Tau.BookII.Closure.proto_abcd_roundtrip_12`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Closure/BSDbridge.lean#L247-L248)
**theorem
Tau.BookII.Closure.proto_abcd_roundtrip_12 :Interior.to_tau_idx (proto_rational_abcd 12) = 12**
