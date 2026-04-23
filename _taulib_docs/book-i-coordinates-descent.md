---
layout: taulib-doc
title: "TauLib.BookI.Coordinates.Descent"
permalink: /verify/taulib/docs/book-i-coordinates-descent/
lane: verify
module_name: "TauLib.BookI.Coordinates.Descent"
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

# TauLib.Coordinates.Descent


Remainder descent and prime stratum descent for greedy peel.

## Registry Cross-References


- [I.L04] Remainder Descent — `div_lt_of_ge_two`, descent checks


## Ground Truth Sources


- chunk_0241_M002280: Remainder descent D < X, prime stratum descent


## Mathematical Content


When X ≥ 2, the greedy peel extracts T(A,B,C) with T ≥ 2. Since D = X / T
and T ∣ X, we have D < X (strict descent).

Additionally, the largest prime of D is strictly less than A (prime stratum
descent). This ensures the spine terminates with strictly decreasing primes.

---

### `Tau.Coordinates.div_lt_of_ge_two`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/Descent.lean#L32-L35)
**theorem
Tau.Coordinates.div_lt_of_ge_two
{x d : Nat}

(hx : x ≥ 1)

(hd : d ≥ 2)

(_hdvd : d ∣ x)
 :x / d < x**


If d ≥ 2 divides x and x ≥ 1, then x / d < x.

---

### `Tau.Coordinates.lt_mul_of_ge_two`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/Descent.lean#L37-L41)
**theorem
Tau.Coordinates.lt_mul_of_ge_two
{a b : Nat}

(ha : a ≥ 2)

(hb : b ≥ 1)
 :b < a * b**


A product a * b with a ≥ 2 is strictly larger than b (when b ≥ 1).

---

### `Tau.Coordinates.descent_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/Descent.lean#L47-L54)
**def
Tau.Coordinates.descent_check
(x : Denotation.TauIdx)
 :Bool**


[I.L04] Check that greedy_peel remainder D < X for X ≥ 2.
Also checks T(A,B,C) * D = X (reconstruction).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Coordinates.prime_stratum_descent_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/Descent.lean#L56-L62)
**def
Tau.Coordinates.prime_stratum_descent_check
(x : Denotation.TauIdx)
 :Bool**


Check that the largest prime of D is strictly less than A.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Coordinates.full_descent_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/Descent.lean#L64-L66)
**def
Tau.Coordinates.full_descent_check
(x : Denotation.TauIdx)
 :Bool**


Combined descent: remainder descent + prime stratum descent.
Equations
- Tau.Coordinates.full_descent_check x = (Tau.Coordinates.descent_check x && Tau.Coordinates.prime_stratum_descent_check x)
Instances For

---

### `Tau.Coordinates.verify_descent_up_to_go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/Descent.lean#L72-L77)@[irreducible]

**def
Tau.Coordinates.verify_descent_up_to_go
(i n fuel : Nat)
 :Bool**


Verify descent for all X from 2 to n.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Coordinates.verify_descent_up_to`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/Descent.lean#L79-L79)
**def
Tau.Coordinates.verify_descent_up_to
(n : Denotation.TauIdx)
 :Bool**

Equations
- Tau.Coordinates.verify_descent_up_to n = Tau.Coordinates.verify_descent_up_to_go 2 n n
Instances For
