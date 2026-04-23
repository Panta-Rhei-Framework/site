---
layout: taulib-doc
title: "TauLib.BookI.Coordinates.TowerAtoms"
permalink: /verify/taulib/docs/book-i-coordinates-tower-atoms/
lane: verify
module_name: "TauLib.BookI.Coordinates.TowerAtoms"
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

# TauLib.Coordinates.TowerAtoms


Tower atoms T(a,b,c) = (a↑↑c)^b and computable peel-off tools.

## Registry Cross-References


- [I.D19c] Tower Atom — `tower_atom`

- [I.D19d] Greedy Peel Algorithm — `largest_prime_divisor`, `max_tet_height`, `max_exp_at`


## Ground Truth Sources


- chunk_0241_M002280: Tower atom definition T(A,B,C) = (A↑↑C)^B (Def 2.12), greedy peel algorithm


## Mathematical Content


A tower atom T(a,b,c) for prime a, b ≥ 1, c ≥ 1 is the canonical
multiplicative building block of τ-Idx. The nesting ((a↑↑c)^b) is the
unique binding from which all three parameters are recoverable.

Tower atoms are prime powers: T(a,b,c) = a^(b · a↑↑(c-1)), so the only
prime factor of T(a,b,c) is a.

---

### `Tau.Coordinates.tetration_pos`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L34-L38)
**theorem
Tau.Coordinates.tetration_pos
(a : Nat)

(ha : a ≥ 1)

(c : Nat)
 :Orbit.tetration a c ≥ 1**


a↑↑c ≥ 1 for a ≥ 1.

---

### `Tau.Coordinates.tetration_ge_base`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L40-L49)
**theorem
Tau.Coordinates.tetration_ge_base
(a : Nat)

(ha : a ≥ 2)

(c : Nat)

(hc : c ≥ 1)
 :Orbit.tetration a c ≥ a**


a↑↑c ≥ a for a ≥ 2, c ≥ 1.

---

### `Tau.Coordinates.tetration_strict_mono`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L51-L61)
**theorem
Tau.Coordinates.tetration_strict_mono
(a : Nat)

(ha : a ≥ 2)

(c : Nat)
 :Orbit.tetration a (c + 1) > Orbit.tetration a c**


a↑↑(c+1) > a↑↑c for a ≥ 2 (strict monotonicity).

---

### `Tau.Coordinates.tetration_unbounded`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L63-L72)
**theorem
Tau.Coordinates.tetration_unbounded
(a : Nat)

(ha : a ≥ 2)

(N : Nat)
 :∃ (c : Nat), Orbit.tetration a c > N**


Tetration is unbounded: for a ≥ 2 and any N, ∃ c, a↑↑c > N.

---

### `Tau.Coordinates.tower_atom`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L78-L79)
**def
Tau.Coordinates.tower_atom
(a b c : Denotation.TauIdx)
 :Denotation.TauIdx**


[I.D19c] Tower atom: T(a,b,c) = (a↑↑c)^b.
Equations
- Tau.Coordinates.tower_atom a b c = Tau.Orbit.tetration a c ^ b
Instances For

---

### `Tau.Coordinates.tower_atom_eq_nat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L81-L83)
**theorem
Tau.Coordinates.tower_atom_eq_nat
(a b c : Denotation.TauIdx)
 :tower_atom a b c = Orbit.tetration a c ^ b**


Bridge: tower_atom a b c = (tetration a c) ^ b (definitional).

---

### `Tau.Coordinates.tower_atom_via_fold`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L85-L91)
**theorem
Tau.Coordinates.tower_atom_via_fold
(a b c : Denotation.TauIdx)
 :tower_atom a b c = Denotation.idx_exp (Denotation.idx_tetration a c) b**


Tower atom factors through the earned fold chain:
T(a,b,c) = idx_exp (idx_tetration a c) b.
Ground truth: chunk_0241, chunk_0060 (UR-ITER).

---

### `Tau.Coordinates.tower_atom_ge_two`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L93-L101)
**theorem
Tau.Coordinates.tower_atom_ge_two
(a b c : Denotation.TauIdx)

(ha : a ≥ 2)

(hb : b ≥ 1)

(hc : c ≥ 1)
 :tower_atom a b c ≥ 2**


Tower atoms are at least 2 for prime base, b ≥ 1, c ≥ 1.

---

### `Tau.Coordinates.tower_atom_pos`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L103-L108)
**theorem
Tau.Coordinates.tower_atom_pos
(a b c : Denotation.TauIdx)

(ha : a ≥ 1)
 :tower_atom a b c > 0**


Tower atoms are positive for a ≥ 1.

---

### `Tau.Coordinates.tetration_as_pow`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L114-L120)
**theorem
Tau.Coordinates.tetration_as_pow
(a c : Nat)

(hc : c ≥ 1)
 :Orbit.tetration a c = a ^ Orbit.tetration a (c - 1)**


The A-adic valuation of a↑↑c equals a↑↑(c-1) for a ≥ 2, c ≥ 1.
That is, a↑↑c = a ^ (a↑↑(c-1)).

---

### `Tau.Coordinates.tower_atom_as_prime_power`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L122-L127)
**theorem
Tau.Coordinates.tower_atom_as_prime_power
(a b c : Denotation.TauIdx)

(hc : c ≥ 1)
 :tower_atom a b c = a ^ (b * Orbit.tetration a (c - 1))**


T(a,b,c) is a power of a: T(a,b,c) = a^(b * a↑↑(c-1)).

---

### `Tau.Coordinates.tower_atom_prime_factor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L145-L157)
**theorem
Tau.Coordinates.tower_atom_prime_factor
(a b c p : Denotation.TauIdx)

(ha : idx_prime a)

(hb : b ≥ 1)

(hc : c ≥ 1)

(hp : idx_prime p)

(hpT : p ∣ tower_atom a b c)
 :p = a**


All prime factors of T(a,b,c) equal a (when a is prime, b ≥ 1, c ≥ 1).

---

### `Tau.Coordinates.largest_prime_divisor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L163-L173)
**def
Tau.Coordinates.largest_prime_divisor
(n : Denotation.TauIdx)
 :Denotation.TauIdx**


[I.D19d] Largest prime divisor of n (0 for n ≤ 1).
Equations
- Tau.Coordinates.largest_prime_divisor n = if n ≤ 1 then 0 else Tau.Coordinates.largest_prime_divisor.go n n
Instances For

---

### `Tau.Coordinates.largest_prime_divisor.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L168-L171)@[irreducible]

**def
Tau.Coordinates.largest_prime_divisor.go
(n d : Denotation.TauIdx)
 :Denotation.TauIdx**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Coordinates.max_tet_height`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L175-L185)
**def
Tau.Coordinates.max_tet_height
(a n : Denotation.TauIdx)
 :Denotation.TauIdx**


Max tetration height: largest c such that a↑↑(c+1) divides n. Returns 0-indexed.
Equations
- Tau.Coordinates.max_tet_height a n = if a ≤ 1 then 0 else Tau.Coordinates.max_tet_height.go a n 0 n
Instances For

---

### `Tau.Coordinates.max_tet_height.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L180-L183)@[irreducible]

**def
Tau.Coordinates.max_tet_height.go
(a n c fuel : Denotation.TauIdx)
 :Denotation.TauIdx**

Equations
- Tau.Coordinates.max_tet_height.go a n c fuel = if fuel = 0 then c
 else if n % Tau.Orbit.tetration a (c + 1) ≠ 0 then c else Tau.Coordinates.max_tet_height.go a n (c + 1) (fuel - 1)
Instances For

---

### `Tau.Coordinates.max_exp_at`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L187-L197)
**def
Tau.Coordinates.max_exp_at
(base n : Denotation.TauIdx)
 :Denotation.TauIdx**


Max exponent: largest b such that base^(b+1) divides n. Returns 0-indexed.
Equations
- Tau.Coordinates.max_exp_at base n = if base ≤ 1 then 0 else Tau.Coordinates.max_exp_at.go base n 0 n
Instances For

---

### `Tau.Coordinates.max_exp_at.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L192-L195)@[irreducible]

**def
Tau.Coordinates.max_exp_at.go
(base n b fuel : Denotation.TauIdx)
 :Denotation.TauIdx**

Equations
- Tau.Coordinates.max_exp_at.go base n b fuel = if fuel = 0 then b else if n % base ^ (b + 1) ≠ 0 then b else Tau.Coordinates.max_exp_at.go base n (b + 1) (fuel - 1)
Instances For

---

### `Tau.Coordinates.max_tet_div`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L199-L209)
**def
Tau.Coordinates.max_tet_div
(a v : Denotation.TauIdx)
 :Denotation.TauIdx**


Max c such that a↑↑(c-1) divides v. Starts at c=1; increments while a↑↑c | v.
Equations
- Tau.Coordinates.max_tet_div a v = if a ≤ 1 then 1 else Tau.Coordinates.max_tet_div.go a v 1 v
Instances For

---

### `Tau.Coordinates.max_tet_div.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L204-L207)@[irreducible]

**def
Tau.Coordinates.max_tet_div.go
(a v c fuel : Denotation.TauIdx)
 :Denotation.TauIdx**

Equations
- Tau.Coordinates.max_tet_div.go a v c fuel = if fuel = 0 then c
 else if v % Tau.Orbit.tetration a c ≠ 0 then c else Tau.Coordinates.max_tet_div.go a v (c + 1) (fuel - 1)
Instances For

---

### `Tau.Coordinates.greedy_peel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/TowerAtoms.lean#L211-L227)
**def
Tau.Coordinates.greedy_peel
(x : Denotation.TauIdx)
 :Denotation.TauIdx × Denotation.TauIdx × Denotation.TauIdx × Denotation.TauIdx**


[I.D19d] One-step greedy peel: extract (A, B, C, D) from X ≥ 2.
Uses A-adic valuation:

- A = largest prime divisor of X

- v = v_A(X)

- C = max c such that A↑↑(c-1) divides v

- B = v / A↑↑(C-1)

- T = tower_atom(A, B, C), D = X / T

Equations
- One or more equations did not get rendered due to their size.
Instances For
