---
layout: taulib-doc
title: "TauLib.BookI.Polarity.Polarity"
permalink: /verify/taulib/docs/book-i-polarity-polarity/
lane: verify
module_name: "TauLib.BookI.Polarity.Polarity"
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

# TauLib.Polarity.Polarity


Prime Polarity Theorem: the canonical bipolar partition of primes.

## Registry Cross-References


- [I.T05] Prime Polarity Theorem — `polarity_map`, `b_channel_unbounded`,
`c_channel_unbounded`, `b_class_witness`, `c_class_witness`


## Ground Truth Sources


- chunk_0310_M002679: Polarity predicate Pol(p,N), Chi character (Thms 3-4, lines 219-248)


## Mathematical Content


The Prime Polarity Theorem (I.T05) establishes:

- (Dichotomy) Every prime carries a canonical polarity (B-dominant or C-dominant).

- (B-class infinite) The B-dominant class is infinite.

- (C-class infinite) The C-dominant class is infinite.


The B-channel (exponentiation) and C-channel (tetration) are both unbounded
for every prime. The polarity is determined by which channel dominates the
spectral signature at a given bound.

Growth-rate separation (proved in Spectral.lean) shows tetration eventually
beats any exponentiation: for a ≥ 2 and any B, ∃ C with a↑↑C > a^B.
Conversely, exponentiation can always match any tetration level: for any C,
∃ B coprime to a with a^B > a↑↑C.

The effective polarity at bound N is computed via the spectral signature
σ_N(p) = (B_max, C_max): p is B-dominant at N when B_max > C_max.

---

### `Tau.Polarity.pow_ge_succ`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L44-L52)
**theorem
Tau.Polarity.pow_ge_succ
(a : Nat)

(ha : a ≥ 2)

(n : Nat)
 :a ^ n ≥ n + 1**


For a ≥ 2, a^n ≥ n + 1 (exponential grows at least linearly).

---

### `Tau.Polarity.b_channel_unbounded`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L58-L61)
**theorem
Tau.Polarity.b_channel_unbounded
(a : Nat)

(ha : a ≥ 2)

(target : Nat)
 :∃ (B : Nat), a ^ B > target**


B-channel unbounded: for a ≥ 2, for any target, ∃ B with a^B > target.

---

### `Tau.Polarity.c_channel_unbounded`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L63-L66)
**theorem
Tau.Polarity.c_channel_unbounded
(a : Nat)

(ha : a ≥ 2)

(target : Nat)
 :∃ (C : Nat), Orbit.tetration a C > target**


C-channel unbounded: for a ≥ 2, for any target, ∃ C with a↑↑C > target.
Direct corollary of tetration_unbounded.

---

### `Tau.Polarity.exp_strict_mono`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L68-L75)
**theorem
Tau.Polarity.exp_strict_mono
(a : Nat)

(ha : a ≥ 2)

(n : Nat)
 :a ^ (n + 1) > a ^ n**


Growth-rate dominance: for a ≥ 2, exponential eventually beats any fixed level.
Specifically, a^(n+1) > a^n for a ≥ 2.

---

### `Tau.Polarity.pure_power_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L81-L87)
**def
Tau.Polarity.pure_power_check
(p k : Denotation.TauIdx)
 :Bool**


Pure power witness check: verify p^k has coord_A = p, coord_B = k, coord_C = 1.
This holds when k is coprime to p (so max_tet_div gives 1).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.tower_witness_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L89-L95)
**def
Tau.Polarity.tower_witness_check
(p c : Denotation.TauIdx)
 :Bool**


Tower witness check: verify p↑↑c has coord_A = p, coord_B = 1, coord_C = c.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.large_prime_c_bounded`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L101-L104)
**def
Tau.Polarity.large_prime_c_bounded
(p N : Denotation.TauIdx)
 :Bool**


For a prime p with p^p > N, all objects X ≤ N with A = p have C ≤ 1.
This is because v_p(X) < p for such X, and max_tet_div(p, v) = 1 when v < p.
Equations
- Tau.Polarity.large_prime_c_bounded p N = if p ^ p > N then decide (Tau.Polarity.c_max p N ≤ 1) else true
Instances For

---

### `Tau.Polarity.large_prime_batch_go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L106-L111)@[irreducible]

**def
Tau.Polarity.large_prime_batch_go
(lo hi N fuel : Nat)
 :Bool**


Batch check: for primes from lo to hi, verify large_prime_c_bounded at bound N.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.large_prime_batch`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L113-L113)
**def
Tau.Polarity.large_prime_batch
(hi N : Denotation.TauIdx)
 :Bool**

Equations
- Tau.Polarity.large_prime_batch hi N = Tau.Polarity.large_prime_batch_go 3 hi N hi
Instances For

---

### `Tau.Polarity.polarity_map`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L119-L121)
**def
Tau.Polarity.polarity_map
(p N : Denotation.TauIdx)
 :Bool**


[I.T05] The polarity map at bound N: returns true (B-dominant) or false (C-dominant)
based on the spectral signature comparison B_max > C_max.
Equations
- Tau.Polarity.polarity_map p N = Tau.Polarity.pol_at p N
Instances For

---

### `Tau.Polarity.polarity_label`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L123-L125)
**def
Tau.Polarity.polarity_label
(p N : Denotation.TauIdx)
 :String**


String label for polarity.
Equations
- Tau.Polarity.polarity_label p N = if Tau.Polarity.polarity_map p N = true then "B-dominant (γ)" else "C-dominant (η)"
Instances For

---

### `Tau.Polarity.polarity_chi`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L131-L137)
**def
Tau.Polarity.polarity_chi
(p N : Denotation.TauIdx)
 :Int**


Polarity character on primes: Chi(p,N) = +1 if C-dominant, -1 if B-dominant.
Returns 0 for non-primes. Ground truth (chunk_0310, lines 219-234):
Chi: (ℕ,×) → (ℤ,+), Chi(p) = +1 if p ∈ P_C, Chi(p) = -1 if p ∈ P_B.
Equations
- Tau.Polarity.polarity_chi p N = if ¬Tau.Coordinates.is_prime_bool p = true then 0 else if Tau.Polarity.polarity_map p N = true then -1 else 1
Instances For

---

### `Tau.Polarity.chi_unit`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L139-L141)
**theorem
Tau.Polarity.chi_unit
(N : Denotation.TauIdx)
 :polarity_chi 1 N = 0**


Chi(1) = 0.

---

### `Tau.Polarity.chi_extend`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L143-L161)
**def
Tau.Polarity.chi_extend
(n N : Denotation.TauIdx)
 :Int**


Multiplicative extension of Chi: sum Chi over prime factors with multiplicity.
Chi_ext(n,N) = sum_{p^k || n} k * Chi(p,N).
Equations
- Tau.Polarity.chi_extend n N = if n ≤ 1 then 0 else Tau.Polarity.chi_extend.chi_go n N n
Instances For

---

### `Tau.Polarity.chi_extend.chi_go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L149-L159)@[irreducible]

**def
Tau.Polarity.chi_extend.chi_go
(n N fuel : Denotation.TauIdx)
 :Int**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.chi_additive_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L163-L165)
**def
Tau.Polarity.chi_additive_check
(a b N : Denotation.TauIdx)
 :Bool**


Chi_ext is additive on products (computational verification).
Equations
- Tau.Polarity.chi_additive_check a b N = (Tau.Polarity.chi_extend (a * b) N == Tau.Polarity.chi_extend a N + Tau.Polarity.chi_extend b N)
Instances For

---

### `Tau.Polarity.b_class_witness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L171-L174)
**def
Tau.Polarity.b_class_witness
(p N : Denotation.TauIdx)
 :Bool**


B-class witness: verify prime p is B-dominant at bound N.
A prime is B-dominant when B_max > C_max in the spectral signature.
Equations
- Tau.Polarity.b_class_witness p N = (Tau.Coordinates.is_prime_bool p && Tau.Polarity.pol_at p N)
Instances For

---

### `Tau.Polarity.c_class_witness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L176-L179)
**def
Tau.Polarity.c_class_witness
(p N : Denotation.TauIdx)
 :Bool**


C-class witness: verify prime p is C-dominant at bound N.
A prime is C-dominant when C_max ≥ B_max in the spectral signature.
Equations
- Tau.Polarity.c_class_witness p N = (Tau.Coordinates.is_prime_bool p && !Tau.Polarity.pol_at p N)
Instances For

---

### `Tau.Polarity.count_b_dominant_go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L185-L192)@[irreducible]

**def
Tau.Polarity.count_b_dominant_go
(i n N acc fuel : Nat)
 :Nat**


Count B-dominant primes among 2..n at bound N.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.count_b_dominant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L194-L194)
**def
Tau.Polarity.count_b_dominant
(n N : Denotation.TauIdx)
 :Nat**

Equations
- Tau.Polarity.count_b_dominant n N = Tau.Polarity.count_b_dominant_go 2 n N 0 n
Instances For

---

### `Tau.Polarity.count_c_dominant_go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L196-L203)@[irreducible]

**def
Tau.Polarity.count_c_dominant_go
(i n N acc fuel : Nat)
 :Nat**


Count C-dominant primes among 2..n at bound N.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.count_c_dominant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L205-L205)
**def
Tau.Polarity.count_c_dominant
(n N : Denotation.TauIdx)
 :Nat**

Equations
- Tau.Polarity.count_c_dominant n N = Tau.Polarity.count_c_dominant_go 2 n N 0 n
Instances For

---

### `Tau.Polarity.count_primes_go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L207-L214)@[irreducible]

**def
Tau.Polarity.count_primes_go
(i n acc fuel : Nat)
 :Nat**


Count total primes among 2..n.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.count_primes`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L216-L216)
**def
Tau.Polarity.count_primes
(n : Denotation.TauIdx)
 :Nat**

Equations
- Tau.Polarity.count_primes n = Tau.Polarity.count_primes_go 2 n 0 n
Instances For

---

### `Tau.Polarity.partition_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L218-L221)
**def
Tau.Polarity.partition_check
(n N : Denotation.TauIdx)
 :Bool**


Verify that every prime from 2 to n is classified at bound N
(B-dominant count + C-dominant count = total prime count).
Equations
- Tau.Polarity.partition_check n N = (Tau.Polarity.count_b_dominant n N + Tau.Polarity.count_c_dominant n N == Tau.Polarity.count_primes n)
Instances For

---

### `Tau.Polarity.b_channel_exceeds`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L227-L230)
**theorem
Tau.Polarity.b_channel_exceeds
(a B : Nat)

(ha : a ≥ 2)
 :a ^ (B + 1) > a ^ B**


For a ≥ 2 and any bound B, there exists a power a^B' that exceeds a^B.
(The B-channel is monotonically increasing.)

---

### `Tau.Polarity.c_beats_b`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L232-L235)
**theorem
Tau.Polarity.c_beats_b
(a : Nat)

(ha : a ≥ 2)

(B : Nat)
 :∃ (C : Nat), Orbit.tetration a C > a ^ B**


For a ≥ 2, the tetration channel eventually exceeds any power:
∀ B, ∃ C, a↑↑C > a^B. (Already proved as growth_rate_separation.)

---

### `Tau.Polarity.b_beats_c`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/Polarity.lean#L237-L244)
**theorem
Tau.Polarity.b_beats_c
(a : Nat)

(ha : a ≥ 2)

(C : Nat)
 :∃ (B : Nat), a ^ B > Orbit.tetration a C**


For a ≥ 2, the exponentiation channel can match any tetration level:
∀ C, ∃ B, a^B > a↑↑C.
