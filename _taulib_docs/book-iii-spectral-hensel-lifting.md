---
layout: taulib-doc
title: "TauLib.BookIII.Spectral.HenselLifting"
permalink: /verify/taulib/docs/book-iii-spectral-hensel-lifting/
lane: verify
module_name: "TauLib.BookIII.Spectral.HenselLifting"
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

# TauLib.BookIII.Spectral.HenselLifting


Constructive Hensel Lifting: modular Newton iteration without signed arithmetic.

## Registry Cross-References


- [III.T11] Constructive Hensel Lifting -- `hensel_lift`, `hensel_check`


## Mathematical Content


**III.T11 (Constructive Hensel Lifting):** Given a root r of f mod p,
lift to a root mod p^n by modular Newton iteration. No signed arithmetic:
correction via modular complement. Lifting is unique (p-adic contraction).

---

### `Tau.BookIII.Spectral.is_prime_naive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L29-L39)
**def
Tau.BookIII.Spectral.is_prime_naive
(n : ℕ)
 :Bool**


Simple primality check by trial division.
Equations
- Tau.BookIII.Spectral.is_prime_naive n = if n < 2 then false else Tau.BookIII.Spectral.is_prime_naive.go n 2 (n + 1)
Instances For

---

### `Tau.BookIII.Spectral.is_prime_naive.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L34-L38)@[irreducible]

**def
Tau.BookIII.Spectral.is_prime_naive.go
(n d fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.poly_eval`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L45-L49)
**def
Tau.BookIII.Spectral.poly_eval
(a x m : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.T11] Evaluate a polynomial f(x) = x² - a mod m.
This is the canonical test case: lifting square roots.
Equations
- Tau.BookIII.Spectral.poly_eval a x m = if (m == 0) = true then 0 else (x * x + m - a % m) % m
Instances For

---

### `Tau.BookIII.Spectral.poly_deriv`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L51-L54)
**def
Tau.BookIII.Spectral.poly_deriv
(x m : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.T11] Modular derivative of f(x) = x² - a: f'(x) = 2x mod m.
Equations
- Tau.BookIII.Spectral.poly_deriv x m = if (m == 0) = true then 0 else 2 * x % m
Instances For

---

### `Tau.BookIII.Spectral.hensel_step`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L56-L67)
**def
Tau.BookIII.Spectral.hensel_step
(a x _p _pk pk1 : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.T11] Hensel step: lift a root from mod p^k to mod p^(k+1).
Newton correction: x_{k+1} = x_k - f(x_k) · f'(x_k)⁻¹ mod p^(k+1).
Uses modular complement to avoid signed arithmetic:
x - t ≡ x + (m - t) mod m.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.hensel_lift`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L69-L82)
**def
Tau.BookIII.Spectral.hensel_lift
(a root p n : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.T11] Full Hensel lift: iterate from mod p to mod p^n.
Starts by reducing root mod p (ensures canonical starting point).
Equations
- Tau.BookIII.Spectral.hensel_lift a root p n = if p < 2 then root else Tau.BookIII.Spectral.hensel_lift.go a p n (root % p) p 1 n
Instances For

---

### `Tau.BookIII.Spectral.hensel_lift.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L75-L81)@[irreducible]

**def
Tau.BookIII.Spectral.hensel_lift.go
(a p n : Denotation.TauIdx)

(x pk exp fuel : ℕ)
 :Denotation.TauIdx**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.hensel_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L84-L102)
**def
Tau.BookIII.Spectral.hensel_check
(bound : Denotation.TauIdx)
 :Bool**


[III.T11] Hensel lifting check: verify that lifted root satisfies
f(x) ≡ 0 mod p^n for test cases.
Equations
- Tau.BookIII.Spectral.hensel_check bound = Tau.BookIII.Spectral.hensel_check.go bound 3 (bound + 1)
Instances For

---

### `Tau.BookIII.Spectral.hensel_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L89-L101)@[irreducible]

**def
Tau.BookIII.Spectral.hensel_check.go
(bound : Denotation.TauIdx)

(p fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.hensel_uniqueness_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L104-L123)
**def
Tau.BookIII.Spectral.hensel_uniqueness_check
(bound : Denotation.TauIdx)
 :Bool**


[III.T11] Hensel uniqueness: the lifted root is unique mod p^n.
Starting from any root r with r ≡ 1 mod p, the lift produces
the same result as starting from 1.
Equations
- Tau.BookIII.Spectral.hensel_uniqueness_check bound = Tau.BookIII.Spectral.hensel_uniqueness_check.go bound 3 (bound + 1)
Instances For

---

### `Tau.BookIII.Spectral.hensel_uniqueness_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L110-L122)@[irreducible]

**def
Tau.BookIII.Spectral.hensel_uniqueness_check.go
(bound : Denotation.TauIdx)

(p fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.hensel_tower_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L125-L142)
**def
Tau.BookIII.Spectral.hensel_tower_check
(bound : Denotation.TauIdx)
 :Bool**


[III.T11] Tower coherence of Hensel lifting:
lift_n(r) mod p^k = lift_k(r) for k < n.
Equations
- Tau.BookIII.Spectral.hensel_tower_check bound = Tau.BookIII.Spectral.hensel_tower_check.go bound 3 (bound + 1)
Instances For

---

### `Tau.BookIII.Spectral.hensel_tower_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L130-L141)@[irreducible]

**def
Tau.BookIII.Spectral.hensel_tower_check.go
(bound : Denotation.TauIdx)

(p fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.hensel_20`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L168-L169)
**theorem
Tau.BookIII.Spectral.hensel_20 :hensel_check 20 = true**


---

### `Tau.BookIII.Spectral.hensel_unique_11`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L172-L173)
**theorem
Tau.BookIII.Spectral.hensel_unique_11 :hensel_uniqueness_check 11 = true**


---

### `Tau.BookIII.Spectral.hensel_tower_11`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L176-L177)
**theorem
Tau.BookIII.Spectral.hensel_tower_11 :hensel_tower_check 11 = true**


---

### `Tau.BookIII.Spectral.one_is_root_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L183-L184)
**theorem
Tau.BookIII.Spectral.one_is_root_3 :poly_eval 1 1 3 = 0**


[III.T11] Structural: 1 is a root of x²-1 mod any p.

---

### `Tau.BookIII.Spectral.one_is_root_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L185-L185)
**theorem
Tau.BookIII.Spectral.one_is_root_5 :poly_eval 1 1 5 = 0**


---

### `Tau.BookIII.Spectral.one_is_root_7`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L186-L186)
**theorem
Tau.BookIII.Spectral.one_is_root_7 :poly_eval 1 1 7 = 0**


---

### `Tau.BookIII.Spectral.hensel_1_mod_9`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L188-L189)
**theorem
Tau.BookIII.Spectral.hensel_1_mod_9 :hensel_lift 1 1 3 2 = 1**


[III.T11] Structural: Hensel lift of 1 mod 3² = 1.

---

### `Tau.BookIII.Spectral.hensel_correct_3_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L191-L193)
**theorem
Tau.BookIII.Spectral.hensel_correct_3_2 :poly_eval 1 (hensel_lift 1 1 3 2) 9 = 0**


[III.T11] Structural: poly_eval is zero at the lifted root.

---

### `Tau.BookIII.Spectral.hensel_correct_5_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/HenselLifting.lean#L195-L196)
**theorem
Tau.BookIII.Spectral.hensel_correct_5_2 :poly_eval 1 (hensel_lift 1 1 5 2) 25 = 0**
