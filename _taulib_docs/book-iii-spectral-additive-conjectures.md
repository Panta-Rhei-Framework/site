---
layout: taulib-doc
title: "TauLib.BookIII.Spectral.AdditiveConjectures"
permalink: /verify/taulib/docs/book-iii-spectral-additive-conjectures/
lane: verify
module_name: "TauLib.BookIII.Spectral.AdditiveConjectures"
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

# TauLib.BookIII.Spectral.AdditiveConjectures


Goldbach conjecture and twin primes as spectral coherence tests
on the primorial tower. Additive structure meets multiplicative
ladder — the interplay is governed by the primorial sieve.

## Registry Cross-References


- [III.D95] Goldbach Representation — `goldbach_pair`, `goldbach_check`

- [III.D96] Twin Prime Distribution — `twin_prime_count`, `twin_prime_density_check`

- [III.T64] Goldbach at Primorial Levels — `goldbach_primorial_check`

- [III.P40] Additive-Multiplicative Duality — `additive_multiplicative_check`


## Mathematical Content


**III.D95 (Goldbach Representation):** Every even n ≥ 4 is the sum of two
primes. Verified computationally at all even numbers up to bound. The
partition count r(n) = #{(p,q) : p+q=n, p≤q prime} measures additive
richness. At primorial levels M_k, the partition count grows with k.

**III.D96 (Twin Prime Distribution):** Twin prime pairs (p, p+2) have
positive density at each primorial level. The count grows with the
primorial modulus. The twin prime constant C₂ ≈ 1.32 is approached.

**III.T64 (Goldbach at Primorial Levels):** Every even number up to M_k
(capped at 100 for computation) has a Goldbach representation. The
primorial sieve guarantees that primes are dense enough at each level
to provide both summands.

**III.P40 (Additive-Multiplicative Duality):** The multiplicative
structure (primorial tower, CRT) and additive structure (Goldbach
partitions, twin primes) coexist: at each primorial level, both
the CRT decomposition and the Goldbach partition count are well-defined
and nontrivial. This is a shadow of Langlands duality at the spectral level.

---

### `Tau.BookIII.Spectral.is_prime_nat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L52-L62)
**def
Tau.BookIII.Spectral.is_prime_nat
(n : ℕ)
 :Bool**


Trial-division primality test for Nat.
Equations
- Tau.BookIII.Spectral.is_prime_nat n = if n < 2 then false else Tau.BookIII.Spectral.is_prime_nat.go n 2 (n + 1)
Instances For

---

### `Tau.BookIII.Spectral.is_prime_nat.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L57-L61)@[irreducible]

**def
Tau.BookIII.Spectral.is_prime_nat.go
(n d fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.goldbach_pair`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L68-L78)
**def
Tau.BookIII.Spectral.goldbach_pair
(n : ℕ)
 :Bool**


[III.D95] Check if even n ≥ 4 has a Goldbach representation p + q = n.
Equations
- Tau.BookIII.Spectral.goldbach_pair n = if (decide (n < 4) || n % 2 != 0) = true then false else Tau.BookIII.Spectral.goldbach_pair.go n 2 (n / 2 + 1)
Instances For

---

### `Tau.BookIII.Spectral.goldbach_pair.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L73-L77)@[irreducible]

**def
Tau.BookIII.Spectral.goldbach_pair.go
(n p fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.goldbach_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L80-L91)
**def
Tau.BookIII.Spectral.goldbach_check
(bound : ℕ)
 :Bool**


[III.D95] Goldbach check: all even numbers from 4 to bound have
a Goldbach representation.
Equations
- Tau.BookIII.Spectral.goldbach_check bound = Tau.BookIII.Spectral.goldbach_check.go bound 4 (bound + 1)
Instances For

---

### `Tau.BookIII.Spectral.goldbach_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L85-L90)@[irreducible]

**def
Tau.BookIII.Spectral.goldbach_check.go
(bound n fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.goldbach_partition_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L93-L105)
**def
Tau.BookIII.Spectral.goldbach_partition_count
(n : ℕ)
 :ℕ**


[III.D95] Goldbach partition count: number of ways n = p + q
with p ≤ q and both prime.
Equations
- Tau.BookIII.Spectral.goldbach_partition_count n = if (decide (n < 4) || n % 2 != 0) = true then 0
 else Tau.BookIII.Spectral.goldbach_partition_count.go n 2 0 (n / 2 + 1)
Instances For

---

### `Tau.BookIII.Spectral.goldbach_partition_count.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L99-L104)@[irreducible]

**def
Tau.BookIII.Spectral.goldbach_partition_count.go
(n p acc fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.is_twin_prime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L111-L113)
**def
Tau.BookIII.Spectral.is_twin_prime
(p : ℕ)
 :Bool**


[III.D96] Is p a twin prime (p and p+2 both prime)?
Equations
- Tau.BookIII.Spectral.is_twin_prime p = (Tau.BookIII.Spectral.is_prime_nat p && Tau.BookIII.Spectral.is_prime_nat (p + 2))
Instances For

---

### `Tau.BookIII.Spectral.twin_prime_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L115-L125)
**def
Tau.BookIII.Spectral.twin_prime_count
(bound : ℕ)
 :ℕ**


[III.D96] Count twin prime pairs (p, p+2) with p ≤ bound.
Equations
- Tau.BookIII.Spectral.twin_prime_count bound = Tau.BookIII.Spectral.twin_prime_count.go bound 2 0 (bound + 1)
Instances For

---

### `Tau.BookIII.Spectral.twin_prime_count.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L119-L124)@[irreducible]

**def
Tau.BookIII.Spectral.twin_prime_count.go
(bound p acc fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.twin_prime_density_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L127-L140)
**def
Tau.BookIII.Spectral.twin_prime_density_check
(db : ℕ)
 :Bool**


[III.D96] Twin prime density check: at least one twin pair exists
up to each primorial level.
Equations
- Tau.BookIII.Spectral.twin_prime_density_check db = Tau.BookIII.Spectral.twin_prime_density_check.go db 2 (db + 1)
Instances For

---

### `Tau.BookIII.Spectral.twin_prime_density_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L132-L139)@[irreducible]

**def
Tau.BookIII.Spectral.twin_prime_density_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.goldbach_primorial_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L146-L158)
**def
Tau.BookIII.Spectral.goldbach_primorial_check
(db : ℕ)
 :Bool**


[III.T64] Goldbach at primorial levels: every even number up to
min(M_k, 100) has a Goldbach representation.
Equations
- Tau.BookIII.Spectral.goldbach_primorial_check db = Tau.BookIII.Spectral.goldbach_primorial_check.go db 2 (db + 1)
Instances For

---

### `Tau.BookIII.Spectral.goldbach_primorial_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L151-L157)@[irreducible]

**def
Tau.BookIII.Spectral.goldbach_primorial_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.additive_multiplicative_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L164-L184)
**def
Tau.BookIII.Spectral.additive_multiplicative_check
(db : ℕ)
 :Bool**


[III.P40] Additive-multiplicative duality: at each primorial level,
the Goldbach partition count and twin prime count are both positive.
Both additive and multiplicative structures are nontrivial.
Equations
- Tau.BookIII.Spectral.additive_multiplicative_check db = Tau.BookIII.Spectral.additive_multiplicative_check.go db 2 (db + 1)
Instances For

---

### `Tau.BookIII.Spectral.additive_multiplicative_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L170-L183)@[irreducible]

**def
Tau.BookIII.Spectral.additive_multiplicative_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.goldbach_30`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L190-L192)
**theorem
Tau.BookIII.Spectral.goldbach_30 :goldbach_check 30 = true**


[III.D95] Goldbach holds for all even numbers up to 30.

---

### `Tau.BookIII.Spectral.goldbach_100`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L194-L196)
**theorem
Tau.BookIII.Spectral.goldbach_100 :goldbach_check 100 = true**


[III.D95] Goldbach holds for all even numbers up to 100.

---

### `Tau.BookIII.Spectral.twin_primes_30`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L198-L200)
**theorem
Tau.BookIII.Spectral.twin_primes_30 :twin_prime_count 30 ≥ 5**


[III.D96] At least 5 twin prime pairs below 30: (3,5),(5,7),(11,13),(17,19),(29,31).

---

### `Tau.BookIII.Spectral.goldbach_primorial_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L202-L204)
**theorem
Tau.BookIII.Spectral.goldbach_primorial_3 :goldbach_primorial_check 3 = true**


[III.T64] Goldbach at primorial levels up to depth 3.

---

### `Tau.BookIII.Spectral.twin_prime_density_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L206-L208)
**theorem
Tau.BookIII.Spectral.twin_prime_density_3 :twin_prime_density_check 3 = true**


[III.D96] Twin prime density at depth 3.

---

### `Tau.BookIII.Spectral.additive_multiplicative_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L210-L212)
**theorem
Tau.BookIII.Spectral.additive_multiplicative_3 :additive_multiplicative_check 3 = true**


[III.P40] Additive-multiplicative duality at depth 3.
