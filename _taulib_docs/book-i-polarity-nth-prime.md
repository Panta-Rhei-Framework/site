---
layout: taulib-doc
title: "TauLib.BookI.Polarity.NthPrime"
permalink: /verify/taulib/docs/book-i-polarity-nth-prime/
lane: verify
module_name: "TauLib.BookI.Polarity.NthPrime"
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

# TauLib.Polarity.NthPrime


Formal properties of `nth_prime`: primality, primorial divisibility,
coprimality, and CRT hypothesis bundles.

## Main Results


- `nth_prime_go_is_prime`: Algorithmic invariant — nth_prime_go returns a prime
when fuel contains enough primes (proved by induction on fuel)

- `nth_prime_prime_of_fuel`: Assembly — nth_prime k is prime when fuel suffices

- `nth_prime_dvd_primorial`: nth_prime(i+1) divides primorial(k) for i < k

- `nth_prime_coprime_primorial`: nth_prime(k+1) coprime to primorial(k)

- `nth_prime_pairwise_coprime`: Pairwise coprimality for CRT

- `CRTHyp`: Bundle of CRT hypotheses at depth k


---

### `Tau.Polarity.count_primes_in`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/NthPrime.lean#L29-L34)@[irreducible]

**def
Tau.Polarity.count_primes_in
(lo hi : Nat)
 :Nat**


Count primes in the half-open interval (lo, hi].
Non-accumulator definition for clean inductive proofs.
Equations
- Tau.Polarity.count_primes_in lo hi = if lo ≥ hi then 0
 else (if Tau.Coordinates.is_prime_bool (lo + 1) = true then 1 else 0) + Tau.Polarity.count_primes_in (lo + 1) hi
Instances For

---

### `Tau.Polarity.count_primes_in_empty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/NthPrime.lean#L42-L43)
**theorem
Tau.Polarity.count_primes_in_empty
(lo : Nat)
 :count_primes_in lo lo = 0**


---

### `Tau.Polarity.count_primes_in_step_prime`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/NthPrime.lean#L45-L49)
**theorem
Tau.Polarity.count_primes_in_step_prime
(lo hi : Nat)

(hlt : lo < hi)

(hp : Coordinates.is_prime_bool (lo + 1) = true)
 :count_primes_in lo hi = 1 + count_primes_in (lo + 1) hi**


---

### `Tau.Polarity.count_primes_in_step_not`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/NthPrime.lean#L51-L55)
**theorem
Tau.Polarity.count_primes_in_step_not
(lo hi : Nat)

(hlt : lo < hi)

(hnp : Coordinates.is_prime_bool (lo + 1) = false)
 :count_primes_in lo hi = count_primes_in (lo + 1) hi**


---

### `Tau.Polarity.nth_prime_go_is_prime`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/NthPrime.lean#L65-L114)
**theorem
Tau.Polarity.nth_prime_go_is_prime
(target count cur fuel : Nat)

(h_target : target ≥ 1)

(h_le : count ≤ target)

(h_inv : count = target → Coordinates.is_prime_bool cur = true)

(h_fuel : count_primes_in cur (cur + fuel) ≥ target - count)
 :Coordinates.is_prime_bool (nth_prime_go target count cur fuel) = true**


If fuel contains enough primes, nth_prime_go returns a value that
passes is_prime_bool.

Invariant: count = target → is_prime_bool cur = true.
This propagates cleanly:


- When count < target and next is prime: count+1 = target → is_prime_bool next (trivially true)

- When count < target and next is NOT prime: count = target → ... (vacuously true since count < target)

- When count = target: function returns cur, and invariant gives primality.


---

### `Tau.Polarity.nth_prime_fuel_ok`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/NthPrime.lean#L120-L122)
**def
Tau.Polarity.nth_prime_fuel_ok
(k : Nat)
 :Bool**


Boolean fuel-sufficiency check for nth_prime.
Equations
- Tau.Polarity.nth_prime_fuel_ok k = (k == 0 || decide (Tau.Polarity.count_primes_in 1 (1 + (k * k * 10 + 10)) ≥ k))
Instances For

---

### `Tau.Polarity.nth_prime_prime_of_fuel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/NthPrime.lean#L124-L134)
**theorem
Tau.Polarity.nth_prime_prime_of_fuel
{k : Denotation.TauIdx}

(hk : k ≥ 1)

(hfuel : count_primes_in 1 (1 + (k * k * 10 + 10)) ≥ k)
 :Coordinates.idx_prime (nth_prime k)**


When fuel suffices, nth_prime k is prime.

---

### `Tau.Polarity.nth_prime_dvd_primorial`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/NthPrime.lean#L152-L170)
**theorem
Tau.Polarity.nth_prime_dvd_primorial
{i k : Denotation.TauIdx}

(h : i + 1 ≤ k)
 :nth_prime (i + 1) ∣ primorial k**


nth_prime(i+1) divides primorial(k) for i + 1 ≤ k. Structural induction.

---

### `Tau.Polarity.nth_prime_coprime_primorial`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/NthPrime.lean#L180-L185)
**theorem
Tau.Polarity.nth_prime_coprime_primorial
{k : Denotation.TauIdx}

(hprime : Coordinates.idx_prime (nth_prime (k + 1)))

(hfresh : primorial k % nth_prime (k + 1) ≠ 0)
 :Nat.Coprime (nth_prime (k + 1)) (primorial k)**


nth_prime(k+1) is coprime to primorial(k), given primality and freshness.

---

### `Tau.Polarity.nth_prime_pairwise_coprime`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/NthPrime.lean#L187-L194)
**theorem
Tau.Polarity.nth_prime_pairwise_coprime
{k : Denotation.TauIdx}

(hprimes : ∀ (i : Denotation.TauIdx), i < k → Coordinates.idx_prime (nth_prime (i + 1)))

(hdistinct : ∀ (i j : Denotation.TauIdx), i < k → j < k → i ≠ j → nth_prime (i + 1) ≠ nth_prime (j + 1))

(i j : Denotation.TauIdx)
 :i < k → j < k → i ≠ j → Nat.Coprime (nth_prime (i + 1)) (nth_prime (j + 1))**


Pairwise coprimality from primality and distinctness.

---

### `Tau.Polarity.CRTHyp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/NthPrime.lean#L196-L200)
**structure
Tau.Polarity.CRTHyp
(k : Denotation.TauIdx)
 :Prop**


CRT hypotheses at depth k: all primes are prime and pairwise coprime.

- all_prime
(i : Denotation.TauIdx)
 : i < k → Coordinates.idx_prime (nth_prime (i + 1))
- pairwise_coprime
(i j : Denotation.TauIdx)
 : i < k → j < k → i ≠ j → Nat.Coprime (nth_prime (i + 1)) (nth_prime (j + 1))
Instances For

---

### `Tau.Polarity.crt_hyp_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/NthPrime.lean#L209-L221)
**theorem
Tau.Polarity.crt_hyp_5 :CRTHyp 5**
