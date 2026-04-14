---
layout: taulib-doc
title: "TauLib.BookIII.Spectral.SieveInfrastructure"
permalink: /verify/taulib/docs/book-iii-spectral-sieve-infrastructure/
lane: verify
module_name: "TauLib.BookIII.Spectral.SieveInfrastructure"
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

# TauLib.BookIII.Spectral.SieveInfrastructure


Sieve infrastructure for the primorial tower: Eratosthenes sieve,
Brun combinatorial sieve, and compatibility with CRT decomposition.

## Registry Cross-References


- [III.D99] Eratosthenes Sieve — `eratosthenes_sieve`, `sieve_primes`

- [III.D100] Sieve Prime Count — `sieve_prime_count`

- [III.D101] Brun Sieve Count — `brun_sieve_count`

- [III.T66] Sieve Correctness — `sieve_correct_50`

- [III.T67] Sieve-Tower Compatibility — `sieve_tower_compat_3`

- [III.P42] Sieve-CRT Compatibility — `sieve_crt_compat_3`


## Mathematical Content


**III.D99 (Eratosthenes Sieve):** Classical sieve of Eratosthenes implemented
as a computable function. Given bound n, returns a Boolean predicate on
[0..n] where `true` indicates primality. This is the fundamental sieve
used by all three conjecture tracks.

**III.D100 (Sieve Prime Count):** π(n) computed via sieve: the number of
primes ≤ n. Agreement with trial division is verified at moderate bounds.

**III.D101 (Brun Sieve Count):** Combinatorial (inclusion-exclusion) sieve
at depth d. Counts integers in [1..n] coprime to the first d primes.
This is the starting point for Brun's theorem on twin primes.

**III.T66 (Sieve Correctness):** The Eratosthenes sieve agrees with trial
division primality testing for all n ≤ 50. Extended to 200 via native_decide.

**III.T67 (Sieve-Tower Compatibility):** The sieve output is stable under
primorial tower projection: primes at level k remain prime at level k+1.
The sieve respects the inverse system structure.

**III.P42 (Sieve-CRT Compatibility):** The sieve decomposes compatibly with
CRT: a number n is sieved out at depth k iff at least one CRT component
r_i = 0 (mod p_i) for i ≤ k. The multiplicative sieve = product of local
sieves via CRT.

---

### `Tau.BookIII.Spectral.eratosthenes_sieve`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L73-L75)
**def
Tau.BookIII.Spectral.eratosthenes_sieve
(n : ℕ)
 :Bool**


[III.D99] Sieve of Eratosthenes: primality test via trial division.
Equations
- Tau.BookIII.Spectral.eratosthenes_sieve n = Tau.BookIII.Spectral.is_prime_sieve✝ n
Instances For

---

### `Tau.BookIII.Spectral.sieve_primes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L77-L87)
**def
Tau.BookIII.Spectral.sieve_primes
(bound : ℕ)
 :List ℕ**


[III.D99] Collect all primes up to bound via sieve.
Equations
- Tau.BookIII.Spectral.sieve_primes bound = Tau.BookIII.Spectral.sieve_primes.go bound 2 [] (bound + 1)
Instances For

---

### `Tau.BookIII.Spectral.sieve_primes.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L81-L86)@[irreducible]

**def
Tau.BookIII.Spectral.sieve_primes.go
(bound k : ℕ)

(acc : List ℕ)

(fuel : ℕ)
 :List ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.sieve_prime_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L93-L103)
**def
Tau.BookIII.Spectral.sieve_prime_count
(n : ℕ)
 :ℕ**


[III.D100] π(n): count of primes ≤ n via sieve.
Equations
- Tau.BookIII.Spectral.sieve_prime_count n = Tau.BookIII.Spectral.sieve_prime_count.go n 2 0 (n + 1)
Instances For

---

### `Tau.BookIII.Spectral.sieve_prime_count.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L97-L102)@[irreducible]

**def
Tau.BookIII.Spectral.sieve_prime_count.go
(n k acc fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.is_coprime_to_small_primes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L109-L121)
**def
Tau.BookIII.Spectral.is_coprime_to_small_primes
(k d : ℕ)
 :Bool**


Helper: check if k is coprime to the first d primes.
Equations
- Tau.BookIII.Spectral.is_coprime_to_small_primes k d = Tau.BookIII.Spectral.is_coprime_to_small_primes.go k d 1 (d + 1)
Instances For

---

### `Tau.BookIII.Spectral.is_coprime_to_small_primes.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L113-L120)@[irreducible]

**def
Tau.BookIII.Spectral.is_coprime_to_small_primes.go
(k d i fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.divisible_by_small_prime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L123-L134)
**def
Tau.BookIII.Spectral.divisible_by_small_prime
(n d : ℕ)
 :Bool**


Helper: check if n is divisible by any of the first d primes.
Equations
- Tau.BookIII.Spectral.divisible_by_small_prime n d = Tau.BookIII.Spectral.divisible_by_small_prime.go n d 1 (d + 1)
Instances For

---

### `Tau.BookIII.Spectral.divisible_by_small_prime.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L127-L133)@[irreducible]

**def
Tau.BookIII.Spectral.divisible_by_small_prime.go
(n d i fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.brun_sieve_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L136-L149)
**def
Tau.BookIII.Spectral.brun_sieve_count
(n d : ℕ)
 :ℕ**


[III.D101] Brun sieve: count integers in [1..n] coprime to the
first d primes (i.e., not divisible by any of p₁, ..., p_d).
This is the inclusion-exclusion sieve at depth d.
Equations
- Tau.BookIII.Spectral.brun_sieve_count n d = Tau.BookIII.Spectral.brun_sieve_count.go n d 1 0 (n + 1)
Instances For

---

### `Tau.BookIII.Spectral.brun_sieve_count.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L142-L148)@[irreducible]

**def
Tau.BookIII.Spectral.brun_sieve_count.go
(n d k acc fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.brun_sieve_density`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L151-L154)
**def
Tau.BookIII.Spectral.brun_sieve_density
(n d : ℕ)
 :ℕ × ℕ**


[III.D101] Brun sieve density: fraction coprime to first d primes.
Returns (count, total) as a pair.
Equations
- Tau.BookIII.Spectral.brun_sieve_density n d = (Tau.BookIII.Spectral.brun_sieve_count n d, n)
Instances For

---

### `Tau.BookIII.Spectral.sieve_agrees_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L160-L170)
**def
Tau.BookIII.Spectral.sieve_agrees_check
(bound : ℕ)
 :Bool**


[III.T66] Sieve agrees with trial division: for all n in [0..bound],
eratosthenes_sieve n = is_prime_nat n.
Equations
- Tau.BookIII.Spectral.sieve_agrees_check bound = Tau.BookIII.Spectral.sieve_agrees_check.go bound 0 (bound + 1)
Instances For

---

### `Tau.BookIII.Spectral.sieve_agrees_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L165-L169)@[irreducible]

**def
Tau.BookIII.Spectral.sieve_agrees_check.go
(bound n fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.sieve_count_known_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L172-L178)
**def
Tau.BookIII.Spectral.sieve_count_known_check :Bool**


[III.T66] Sieve count matches known values at key points.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.check_prime_factors_of_primorial`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L184-L195)
**def
Tau.BookIII.Spectral.check_prime_factors_of_primorial
(k : ℕ)
 :Bool**


Helper: check that each p_i (i ≤ k) divides M_k.
Equations
- Tau.BookIII.Spectral.check_prime_factors_of_primorial k = Tau.BookIII.Spectral.check_prime_factors_of_primorial.go k 1 (k + 1)
Instances For

---

### `Tau.BookIII.Spectral.check_prime_factors_of_primorial.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L188-L194)@[irreducible]

**def
Tau.BookIII.Spectral.check_prime_factors_of_primorial.go
(k i fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.sieve_tower_compat_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L197-L213)
**def
Tau.BookIII.Spectral.sieve_tower_compat_check
(db : ℕ)
 :Bool**


[III.T67] Sieve-tower compatibility: the prime factors of M_k are
exactly {p_1,...,p_k}, and these all divide M_{k+1}. The sieve is
tower-stable: once a prime enters the factorization at level k, it
remains at all deeper levels. Checked via M_k | M_{k+1}.
Equations
- Tau.BookIII.Spectral.sieve_tower_compat_check db = Tau.BookIII.Spectral.sieve_tower_compat_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Spectral.sieve_tower_compat_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L204-L212)@[irreducible]

**def
Tau.BookIII.Spectral.sieve_tower_compat_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.euler_phi_primorial`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L215-L225)
**def
Tau.BookIII.Spectral.euler_phi_primorial
(k : ℕ)
 :ℕ**


[III.T67] Euler phi at primorial level: φ(M_k) = ∏(p_i - 1).
Equations
- Tau.BookIII.Spectral.euler_phi_primorial k = Tau.BookIII.Spectral.euler_phi_primorial.go k 1 1 (k + 1)
Instances For

---

### `Tau.BookIII.Spectral.euler_phi_primorial.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L219-L224)@[irreducible]

**def
Tau.BookIII.Spectral.euler_phi_primorial.go
(k i acc fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.brun_euler_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L227-L239)
**def
Tau.BookIII.Spectral.brun_euler_check
(db : ℕ)
 :Bool**


[III.T67] Brun sieve matches Euler phi at primorial levels.
Equations
- Tau.BookIII.Spectral.brun_euler_check db = Tau.BookIII.Spectral.brun_euler_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Spectral.brun_euler_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L231-L238)@[irreducible]

**def
Tau.BookIII.Spectral.brun_euler_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.sieve_crt_compat_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L245-L259)
**def
Tau.BookIII.Spectral.sieve_crt_compat_check
(bound db : ℕ)
 :Bool**


[III.P42] Sieve-CRT compatibility: n is divisible by p_i (i ≤ k)
iff the i-th CRT residue (n mod p_i) equals 0.
Equations
- Tau.BookIII.Spectral.sieve_crt_compat_check bound db = Tau.BookIII.Spectral.sieve_crt_compat_check.go bound db 1 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Spectral.sieve_crt_compat_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L250-L258)@[irreducible]

**def
Tau.BookIII.Spectral.sieve_crt_compat_check.go
(bound db n k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.sieve_correct_50`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L265-L267)
**theorem
Tau.BookIII.Spectral.sieve_correct_50 :sieve_agrees_check 50 = true**


[III.T66] Sieve agrees with trial division up to 50.

---

### `Tau.BookIII.Spectral.sieve_correct_200`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L269-L271)
**theorem
Tau.BookIII.Spectral.sieve_correct_200 :sieve_agrees_check 200 = true**


[III.T66] Sieve agrees with trial division up to 200.

---

### `Tau.BookIII.Spectral.sieve_count_known`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L273-L275)
**theorem
Tau.BookIII.Spectral.sieve_count_known :sieve_count_known_check = true**


[III.T66] Sieve count matches known prime-counting values.

---

### `Tau.BookIII.Spectral.sieve_tower_compat_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L277-L279)
**theorem
Tau.BookIII.Spectral.sieve_tower_compat_3 :sieve_tower_compat_check 3 = true**


[III.T67] Sieve-tower compatibility at depth 3.

---

### `Tau.BookIII.Spectral.brun_euler_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L281-L283)
**theorem
Tau.BookIII.Spectral.brun_euler_4 :brun_euler_check 4 = true**


[III.T67] Brun sieve matches Euler phi at primorial depths 1..4.

---

### `Tau.BookIII.Spectral.sieve_crt_compat_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L285-L287)
**theorem
Tau.BookIII.Spectral.sieve_crt_compat_3 :sieve_crt_compat_check 30 3 = true**


[III.P42] Sieve-CRT compatibility for values ≤ 30 at depth 3.

---

### `Tau.BookIII.Spectral.pi_10`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L293-L294)
**theorem
Tau.BookIII.Spectral.pi_10 :sieve_prime_count 10 = 4**


[III.D100] π(10) = 4 (primes: 2, 3, 5, 7).

---

### `Tau.BookIII.Spectral.pi_30`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L296-L297)
**theorem
Tau.BookIII.Spectral.pi_30 :sieve_prime_count 30 = 10**


[III.D100] π(30) = 10.

---

### `Tau.BookIII.Spectral.pi_100`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L299-L300)
**theorem
Tau.BookIII.Spectral.pi_100 :sieve_prime_count 100 = 25**


[III.D100] π(100) = 25.

---

### `Tau.BookIII.Spectral.brun_30_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L302-L304)
**theorem
Tau.BookIII.Spectral.brun_30_3 :brun_sieve_count 30 3 = 8**


[III.D101] Brun sieve at (30, 3): 8 integers in [1..30] coprime
to {2,3,5}. These are: 1, 7, 11, 13, 17, 19, 23, 29.

---

### `Tau.BookIII.Spectral.euler_phi_primorial_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L306-L308)
**theorem
Tau.BookIII.Spectral.euler_phi_primorial_3 :euler_phi_primorial 3 = 8**


[III.T67] Euler phi at primorial 3 = φ(30) = (2-1)(3-1)(5-1) = 8.

---

### `Tau.BookIII.Spectral.euler_phi_primorial_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L310-L312)
**theorem
Tau.BookIII.Spectral.euler_phi_primorial_4 :euler_phi_primorial 4 = 48**


[III.T67] Euler phi at primorial 4 = φ(210) = 1·2·4·6 = 48.
