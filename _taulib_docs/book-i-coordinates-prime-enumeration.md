---
layout: taulib-doc
title: "TauLib.BookI.Coordinates.PrimeEnumeration"
permalink: /verify/taulib/docs/book-i-coordinates-prime-enumeration/
lane: verify
module_name: "TauLib.BookI.Coordinates.PrimeEnumeration"
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

# TauLib.Coordinates.PrimeEnumeration


Prime enumeration, counting, and orbit value projection —
the semantic projection between solenoidal orbits and the α-orbit.

## Registry Cross-References


- [I.D19f] Prime Enumeration — `nthPrime`, `prime_count`, `prime_index`


## Ground Truth Sources


- chunk_0310_M002679: Prime enumeration as orbit channel projection

- chunk_0060_M000698: UR-ITER — all computation earned from ρ


## Mathematical Content


The prime enumeration function nthPrime(k) = p_k maps TauIdx to TauIdx:


- nthPrime(0) = 2, nthPrime(1) = 3, nthPrime(2) = 5, ...


It is the semantic projection from the π-orbit to the α-orbit: the
depth-k element of O_π "represents" the number nthPrime(k).

The inverse is the prime index function: for prime p,
prime_index(p) = k such that nthPrime(k) = p.

The prime counting function π(n) = prime_count(n) counts primes ≤ n.

All three are computable via finite scanning using `is_prime_bool`,
which itself uses only the earned arithmetic from ρ-folds.
This is the categorical τ version of the Sieve of Eratosthenes.

---

### `Tau.Coordinates.prime_count_go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L43-L49)@[irreducible]

**def
Tau.Coordinates.prime_count_go
(n i acc : Denotation.TauIdx)

(fuel : Nat)
 :Denotation.TauIdx**


Count primes in the range [2, n] by scanning.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Coordinates.prime_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L51-L54)
**def
Tau.Coordinates.prime_count
(n : Denotation.TauIdx)
 :Denotation.TauIdx**


[I.D19f] Prime counting function π(n): number of primes ≤ n.
Returns 0 for n < 2.
Equations
- Tau.Coordinates.prime_count n = if n < 2 then 0 else Tau.Coordinates.prime_count_go n 2 0 n
Instances For

---

### `Tau.Coordinates.nthPrime_go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L60-L67)@[irreducible]

**def
Tau.Coordinates.nthPrime_go
(target candidate count : Denotation.TauIdx)

(fuel : Nat)
 :Denotation.TauIdx**


Scan for the k-th prime (0-indexed) starting from candidate.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Coordinates.nthPrime`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L69-L74)
**def
Tau.Coordinates.nthPrime
(k : Denotation.TauIdx)
 :Denotation.TauIdx**


[I.D19f] The k-th prime number (0-indexed).
nthPrime 0 = 2, nthPrime 1 = 3, nthPrime 2 = 5, ...
Computed by finite scanning using is_prime_bool — a finite
sieve earned entirely from ρ-folds.
Equations
- Tau.Coordinates.nthPrime k = Tau.Coordinates.nthPrime_go k 2 0 ((k + 1) * (k + 1) + 10)
Instances For

---

### `Tau.Coordinates.prime_index`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L80-L84)
**def
Tau.Coordinates.prime_index
(p : Denotation.TauIdx)
 :Denotation.TauIdx**


[I.D19f] Prime index: the number of primes strictly less than p.
For prime p, this is the k such that nthPrime(k) = p.
Equations
- Tau.Coordinates.prime_index p = if p ≤ 2 then 0 else Tau.Coordinates.prime_count (p - 1)
Instances For

---

### `Tau.Coordinates.pi_orbit_value`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L90-L96)
**def
Tau.Coordinates.pi_orbit_value
(k : Denotation.TauIdx)
 :Denotation.TauIdx**


The semantic projection from π-orbit depth to α-orbit value:
the depth-k element of O_π represents the number nthPrime(k).

This is the key distinction between structural rank transfer
(RT_π maps k ↦ ⟨π, k⟩, preserving depth) and semantic projection
(pi_orbit_value maps k ↦ p_k, giving the denotational value).
Equations
- Tau.Coordinates.pi_orbit_value k = Tau.Coordinates.nthPrime k
Instances For

---

### `Tau.Coordinates.pi_projection_via_RT`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L98-L102)
**theorem
Tau.Coordinates.pi_projection_via_RT
(k : Denotation.TauIdx)
 :Denotation.RT Kernel.Generator.alpha (pi_orbit_value k) = Denotation.toAlphaOrbit (nthPrime k)**


The π-orbit projection via rank transfer:
RT_α(nthPrime(k)) is the α-orbit element corresponding to π_k.

---

### `Tau.Coordinates.alpha_to_pi_rank`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L104-L105)
**def
Tau.Coordinates.alpha_to_pi_rank
(p : Denotation.TauIdx)
 :Denotation.TauIdx**


The reverse projection: for prime p, its π-rank.
Equations
- Tau.Coordinates.alpha_to_pi_rank p = Tau.Coordinates.prime_index p
Instances For

---

### `Tau.Coordinates.sieve_earned_from_rho`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/PrimeEnumeration.lean#L131-L142)
**theorem
Tau.Coordinates.sieve_earned_from_rho :(∀ (k : Denotation.TauIdx), ∃ (p : Denotation.TauIdx), p = nthPrime k) ∧ (∀ (n : Denotation.TauIdx), ∃ (c : Denotation.TauIdx), c = prime_count n) ∧ ∀ (p : Denotation.TauIdx), ∃ (k : Denotation.TauIdx), k = prime_index p**


The Earned Sieve Principle: the prime enumeration is computable
using only the earned predicate is_prime_bool, which chains through
the fold hierarchy: is_prime_bool → idx_divides → idx_mul →
idx_add → iter_rho → ρ.
Ground truth: chunk_0060 (UR-ITER).
