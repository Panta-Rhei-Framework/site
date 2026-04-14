---
layout: taulib-doc
title: "TauLib.BookI.Polarity.ModArith"
permalink: /verify/taulib/docs/book-i-polarity-mod-arith/
lane: verify
module_name: "TauLib.BookI.Polarity.ModArith"
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

# TauLib.Polarity.ModArith


Modular arithmetic infrastructure for the primorial ladder.

## Ground Truth Sources


- chunk_0120_M001406: Primorial ladder, local ring structure on ℤ_p^(τ)


## Mathematical Content


The k-th primorial M_k = p₁ · p₂ · ... · p_k is the product of the first k
internal primes. Reduction maps π_{ℓ→k} : Z/M_ℓZ → Z/M_kZ are given by
x ↦ x mod M_k. These form a compatible inverse system.

This module provides: nth_prime, primorial, reduction maps, and modular
arithmetic ring laws needed for omega-germ construction.

---

### `Tau.Polarity.nth_prime_go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ModArith.lean#L29-L39)@[irreducible]

**def
Tau.Polarity.nth_prime_go
(target count cur fuel : Nat)
 :Nat**


Find the k-th prime by trial (1-indexed: nth_prime 1 = 2).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.nth_prime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ModArith.lean#L41-L44)
**def
Tau.Polarity.nth_prime
(k : Denotation.TauIdx)
 :Denotation.TauIdx**


The k-th prime (1-indexed). nth_prime 0 = 0 by convention.
Equations
- Tau.Polarity.nth_prime k = if k = 0 then 0 else Tau.Polarity.nth_prime_go k 0 1 (k * k * 10 + 10)
Instances For

---

### `Tau.Polarity.primorial`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ModArith.lean#L50-L54)
**def
Tau.Polarity.primorial :Denotation.TauIdx → Denotation.TauIdx**


The k-th primorial: M_k = p₁ · p₂ · ... · p_k.
primorial 0 = 1, primorial k = nth_prime(k) · primorial(k-1).
Equations
- Tau.Polarity.primorial 0 = 1
- Tau.Polarity.primorial (Nat.succ k) = Tau.Polarity.nth_prime (k + 1) * Tau.Polarity.primorial k
Instances For

---

### `Tau.Polarity.reduce`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ModArith.lean#L60-L62)
**def
Tau.Polarity.reduce
(x k : Denotation.TauIdx)
 :Denotation.TauIdx**


Reduction map: x mod M_k. This is the canonical projection
π_k : Z → Z/M_kZ.
Equations
- Tau.Polarity.reduce x k = x % Tau.Polarity.primorial k
Instances For

---

### `Tau.Polarity.primorial_dvd_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ModArith.lean#L64-L67)
**def
Tau.Polarity.primorial_dvd_check
(k l : Denotation.TauIdx)
 :Bool**


Primorial divisibility: M_k divides M_ℓ when k ≤ ℓ.
Computable check.
Equations
- Tau.Polarity.primorial_dvd_check k l = (decide (k ≤ l) && Tau.Polarity.primorial l % Tau.Polarity.primorial k == 0)
Instances For

---

### `Tau.Polarity.reduction_compat_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ModArith.lean#L69-L72)
**def
Tau.Polarity.reduction_compat_check
(x k l : Denotation.TauIdx)
 :Bool**


Reduction compatibility check: x % M_ℓ % M_k = x % M_k when k ≤ ℓ.
Equations
- Tau.Polarity.reduction_compat_check x k l = if k ≤ l then Tau.Polarity.reduce (Tau.Polarity.reduce x l) k == Tau.Polarity.reduce x k else true
Instances For

---

### `Tau.Polarity.mod_add_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ModArith.lean#L78-L80)
**theorem
Tau.Polarity.mod_add_eq
(a b m : Nat)
 :(a + b) % m = (a % m + b % m) % m**


Modular addition: (a + b) % m = ((a % m) + (b % m)) % m.

---

### `Tau.Polarity.mod_mul_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ModArith.lean#L82-L84)
**theorem
Tau.Polarity.mod_mul_eq
(a b m : Nat)
 :a * b % m = a % m * (b % m) % m**


Modular multiplication: (a * b) % m = ((a % m) * (b % m)) % m.

---

### `Tau.Polarity.mod_lt_of_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ModArith.lean#L86-L88)
**theorem
Tau.Polarity.mod_lt_of_pos
(a m : Nat)

(hm : m > 0)
 :a % m < m**


a % m < m for m > 0.

---

### `Tau.Polarity.distinct_primes_coprime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ModArith.lean#L94-L107)
**theorem
Tau.Polarity.distinct_primes_coprime
{p q : Denotation.TauIdx}

(hp : Coordinates.idx_prime p)

(hq : Coordinates.idx_prime q)

(hne : p ≠ q)
 :Nat.gcd p q = 1**


If p and q are distinct primes, they are coprime.

---

### `Tau.Polarity.nth_prime_go_ge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ModArith.lean#L113-L131)
**theorem
Tau.Polarity.nth_prime_go_ge
(target count cur fuel : Nat)
 :nth_prime_go target count cur fuel ≥ cur**


nth_prime_go always returns a value ≥ cur.

---

### `Tau.Polarity.nth_prime_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ModArith.lean#L133-L138)
**theorem
Tau.Polarity.nth_prime_pos
{k : Denotation.TauIdx}

(hk : k ≥ 1)
 :nth_prime k ≥ 1**


nth_prime k ≥ 1 for k ≥ 1.

---

### `Tau.Polarity.primorial_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ModArith.lean#L140-L148)
**theorem
Tau.Polarity.primorial_pos
(k : Denotation.TauIdx)
 :primorial k > 0**


Every primorial is positive: M_k > 0.

---

### `Tau.Polarity.primorial_dvd`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ModArith.lean#L154-L169)
**theorem
Tau.Polarity.primorial_dvd
{k l : Denotation.TauIdx}

(h : k ≤ l)
 :primorial k ∣ primorial l**


Primorial divisibility: M_k ∣ M_l when k ≤ l.
This is the structural backbone of the inverse system.

---

### `Tau.Polarity.mod_mod_of_dvd`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ModArith.lean#L184-L197)
**theorem
Tau.Polarity.mod_mod_of_dvd
(x a b : Nat)

(h : a ∣ b)
 :x % b % a = x % a**


If a ∣ b then (x % b) % a = x % a.
Proved from first principles using Lean 4 core.

---

### `Tau.Polarity.reduction_compat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/ModArith.lean#L199-L204)
**theorem
Tau.Polarity.reduction_compat
(x : Denotation.TauIdx)

{k l : Denotation.TauIdx}

(h : k ≤ l)
 :reduce (reduce x l) k = reduce x k**


Reduction maps compose: (x % M_l) % M_k = x % M_k for k ≤ l.
This is the fundamental compatibility condition of the primorial inverse system.
