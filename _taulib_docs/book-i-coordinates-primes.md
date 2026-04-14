---
layout: taulib-doc
title: "TauLib.BookI.Coordinates.Primes"
permalink: /verify/taulib/docs/book-i-coordinates-primes/
lane: verify
module_name: "TauLib.BookI.Coordinates.Primes"
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

# TauLib.Coordinates.Primes


Primes, divisibility, GCD, Euclid's Lemma, and FTA on τ-Idx.

## Registry Cross-References


- [I.D19a] Index Divisibility — `idx_divides`, `idx_divides_iff_nat_dvd`

- [I.D19b] Index Prime — `idx_prime`

- [I.T09] Fundamental Theorem of Arithmetic — `prime_product_exists`, `prime_product_unique`


## Ground Truth Sources


- chunk_0310_M002679: Primes as finite witnesses, FTA as prerequisite for polarity partition


---

### `Tau.Coordinates.idx_divides`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L42-L43)
**def
Tau.Coordinates.idx_divides
(a b : Denotation.TauIdx)
 :Prop**


[I.D19a] Index divisibility: a divides b in τ-Idx.
Equations
- Tau.Coordinates.idx_divides a b = ∃ (k : Tau.Denotation.TauIdx), b = Tau.Denotation.idx_mul a k
Instances For

---

### `Tau.Coordinates.idx_divides_iff_nat_dvd`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L45-L49)
**theorem
Tau.Coordinates.idx_divides_iff_nat_dvd
(a b : Denotation.TauIdx)
 :idx_divides a b ↔ a ∣ b**


Bridge: idx_divides ↔ Nat.dvd.

---

### `Tau.Coordinates.instDecidableIdxDivides`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L51-L52)
**instance
Tau.Coordinates.instDecidableIdxDivides
(a b : Denotation.TauIdx)
 :Decidable (idx_divides a b)**

Equations
- Tau.Coordinates.instDecidableIdxDivides a b = decidable_of_iff (a ∣ b) ⋯

---

### `Tau.Coordinates.idx_divides_refl`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L58-L59)
**theorem
Tau.Coordinates.idx_divides_refl
(a : Denotation.TauIdx)
 :idx_divides a a**


---

### `Tau.Coordinates.idx_divides_trans`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L61-L65)
**theorem
Tau.Coordinates.idx_divides_trans
{a b c : Denotation.TauIdx}

(hab : idx_divides a b)

(hbc : idx_divides b c)
 :idx_divides a c**


---

### `Tau.Coordinates.idx_one_divides`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L67-L68)
**theorem
Tau.Coordinates.idx_one_divides
(a : Denotation.TauIdx)
 :idx_divides 1 a**


---

### `Tau.Coordinates.idx_divides_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L70-L71)
**theorem
Tau.Coordinates.idx_divides_zero
(a : Denotation.TauIdx)
 :idx_divides a 0**


---

### `Tau.Coordinates.idx_divides_le`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L73-L74)
**theorem
Tau.Coordinates.idx_divides_le
{a b : Denotation.TauIdx}

(hab : idx_divides a b)

(hb : b ≠ 0)
 :a ≤ b**


---

### `Tau.Coordinates.idx_divides_antisymm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L76-L79)
**theorem
Tau.Coordinates.idx_divides_antisymm
{a b : Denotation.TauIdx}

(hab : idx_divides a b)

(hba : idx_divides b a)
 :a = b**


---

### `Tau.Coordinates.idx_prime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L85-L87)
**def
Tau.Coordinates.idx_prime
(p : Denotation.TauIdx)
 :Prop**


[I.D19b] Index prime: p ≥ 2 and only divisors are 1 and p.
Equations
- Tau.Coordinates.idx_prime p = (p ≥ 2 ∧ ∀ (d : Tau.Denotation.TauIdx), d ∣ p → d = 1 ∨ d = p)
Instances For

---

### `Tau.Coordinates.no_factor_below`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L89-L96)@[irreducible]

**def
Tau.Coordinates.no_factor_below
(n d : Denotation.TauIdx)
 :Bool**


Boolean primality check via trial division.
Equations
- Tau.Coordinates.no_factor_below n d = if d ≥ n then true
 else if d * d > n then true else if n % d = 0 then false else Tau.Coordinates.no_factor_below n (d + 1)
Instances For

---

### `Tau.Coordinates.is_prime_bool`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L98-L99)
**def
Tau.Coordinates.is_prime_bool
(p : Denotation.TauIdx)
 :Bool**


Boolean primality test.
Equations
- Tau.Coordinates.is_prime_bool p = (decide (p ≥ 2) && Tau.Coordinates.no_factor_below p 2)
Instances For

---

### `Tau.Coordinates.exists_prime_divisor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L105-L135)
**theorem
Tau.Coordinates.exists_prime_divisor
(n : Denotation.TauIdx)

(hn : n ≥ 2)
 :∃ (p : Denotation.TauIdx), idx_prime p ∧ p ∣ n**


Every n ≥ 2 has a prime divisor. Proved by strong induction.

---

### `Tau.Coordinates.idx_gcd`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L141-L141)
**def
Tau.Coordinates.idx_gcd
(a b : Denotation.TauIdx)
 :Denotation.TauIdx**

Equations
- Tau.Coordinates.idx_gcd a b = Nat.gcd a b
Instances For

---

### `Tau.Coordinates.idx_gcd_dvd_left`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L143-L143)
**theorem
Tau.Coordinates.idx_gcd_dvd_left
(a b : Denotation.TauIdx)
 :idx_gcd a b ∣ a**


---

### `Tau.Coordinates.idx_gcd_dvd_right`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L144-L144)
**theorem
Tau.Coordinates.idx_gcd_dvd_right
(a b : Denotation.TauIdx)
 :idx_gcd a b ∣ b**


---

### `Tau.Coordinates.idx_dvd_gcd`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L146-L147)
**theorem
Tau.Coordinates.idx_dvd_gcd
{c a b : Denotation.TauIdx}

(hca : c ∣ a)

(hcb : c ∣ b)
 :c ∣ idx_gcd a b**


---

### `Tau.Coordinates.idx_coprime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L153-L153)
**def
Tau.Coordinates.idx_coprime
(a b : Denotation.TauIdx)
 :Prop**

Equations
- Tau.Coordinates.idx_coprime a b = (Tau.Coordinates.idx_gcd a b = 1)
Instances For

---

### `Tau.Coordinates.prime_coprime_of_not_dvd`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L155-L161)
**theorem
Tau.Coordinates.prime_coprime_of_not_dvd
{p a : Denotation.TauIdx}

(hp : idx_prime p)

(hna : ¬p ∣ a)
 :idx_coprime p a**


---

### `Tau.Coordinates.coprime_dvd_of_dvd_mul`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L163-L167)
**theorem
Tau.Coordinates.coprime_dvd_of_dvd_mul
{a b c : Denotation.TauIdx}

(hcop : idx_coprime a b)

(h : a ∣ b * c)
 :a ∣ c**


Gauss's lemma via Nat.Coprime.

---

### `Tau.Coordinates.euclid_lemma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L169-L174)
**theorem
Tau.Coordinates.euclid_lemma
{p a b : Denotation.TauIdx}

(hp : idx_prime p)

(h : p ∣ a * b)
 :p ∣ a ∨ p ∣ b**


Euclid's Lemma: p prime, p ∣ a*b → p ∣ a ∨ p ∣ b.

---

### `Tau.Coordinates.idx_factorial`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L180-L182)
**def
Tau.Coordinates.idx_factorial :Denotation.TauIdx → Denotation.TauIdx**

Equations
- Tau.Coordinates.idx_factorial 0 = 1
- Tau.Coordinates.idx_factorial (Nat.succ n) = (n + 1) * Tau.Coordinates.idx_factorial n
Instances For

---

### `Tau.Coordinates.idx_factorial_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L184-L187)
**theorem
Tau.Coordinates.idx_factorial_pos
(n : Denotation.TauIdx)
 :idx_factorial n > 0**


---

### `Tau.Coordinates.prime_dvd_factorial`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L189-L204)
**theorem
Tau.Coordinates.prime_dvd_factorial
{p n : Denotation.TauIdx}

(hp : idx_prime p)

(hpn : p ≤ n)
 :p ∣ idx_factorial n**


Every prime p ≤ n divides n!.

---

### `Tau.Coordinates.primes_infinite`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L225-L232)
**theorem
Tau.Coordinates.primes_infinite
(n : Denotation.TauIdx)
 :∃ (p : Denotation.TauIdx), idx_prime p ∧ p > n**


For every n, there exists a prime p > n.

---

### `Tau.Coordinates.list_prod`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L238-L240)
**def
Tau.Coordinates.list_prod :List Denotation.TauIdx → Denotation.TauIdx**

Equations
- Tau.Coordinates.list_prod [] = 1
- Tau.Coordinates.list_prod (x_1 :: xs) = x_1 * Tau.Coordinates.list_prod xs
Instances For

---

### `Tau.Coordinates.prime_product_exists`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L242-L273)
**theorem
Tau.Coordinates.prime_product_exists
(n : Denotation.TauIdx)

(hn : n ≥ 2)
 :∃ (ps : List Denotation.TauIdx), (∀ (p : Denotation.TauIdx), p ∈ ps → idx_prime p) ∧ list_prod ps = n**


Every n ≥ 2 is a product of primes.

---

### `Tau.Coordinates.prime_mem_of_dvd_prod`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L304-L320)
**theorem
Tau.Coordinates.prime_mem_of_dvd_prod
{p : Denotation.TauIdx}

(hp : idx_prime p)

{ps : List Denotation.TauIdx}

(hps : ∀ (q : Denotation.TauIdx), q ∈ ps → idx_prime q)

(hdvd : p ∣ list_prod ps)
 :p ∈ ps**


If p is prime and p divides a product of primes, then p is in the list.

---

### `Tau.Coordinates.sorted_nd`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L352-L355)
**def
Tau.Coordinates.sorted_nd :List Denotation.TauIdx → Prop**


Non-decreasing list (each element ≤ all successors).
Equations
- Tau.Coordinates.sorted_nd [] = True
- Tau.Coordinates.sorted_nd (x_1 :: xs) = (Tau.Coordinates.all_ge✝ x_1 xs ∧ Tau.Coordinates.sorted_nd xs)
Instances For

---

### `Tau.Coordinates.prime_product_unique`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L357-L407)
**theorem
Tau.Coordinates.prime_product_unique
(ps qs : List Denotation.TauIdx)

(hps : ∀ (p : Denotation.TauIdx), p ∈ ps → idx_prime p)

(hqs : ∀ (q : Denotation.TauIdx), q ∈ qs → idx_prime q)

(hps_sorted : sorted_nd ps)

(hqs_sorted : sorted_nd qs)

(heq : list_prod ps = list_prod qs)
 :ps = qs**


[I.T09] FTA uniqueness: two sorted non-decreasing prime lists
with the same product are identical.

---

### `Tau.Coordinates.p_adic_val`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L413-L424)
**def
Tau.Coordinates.p_adic_val
(p n : Denotation.TauIdx)
 :Denotation.TauIdx**


p-adic valuation: how many times p divides n.
Equations
- Tau.Coordinates.p_adic_val p n = if p ≤ 1 then 0 else if n = 0 then 0 else Tau.Coordinates.p_adic_val.go p n n
Instances For

---

### `Tau.Coordinates.p_adic_val.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/Primes.lean#L419-L422)@[irreducible]

**def
Tau.Coordinates.p_adic_val.go
(p n fuel : Denotation.TauIdx)
 :Denotation.TauIdx**

Equations
- Tau.Coordinates.p_adic_val.go p n fuel = if fuel = 0 then 0 else if n % p = 0 then 1 + Tau.Coordinates.p_adic_val.go p (n / p) (fuel - 1) else 0
Instances For
