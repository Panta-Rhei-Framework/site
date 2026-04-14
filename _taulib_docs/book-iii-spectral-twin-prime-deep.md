---
layout: taulib-doc
title: "TauLib.BookIII.Spectral.TwinPrimeDeep"
permalink: /verify/taulib/docs/book-iii-spectral-twin-prime-deep/
lane: verify
module_name: "TauLib.BookIII.Spectral.TwinPrimeDeep"
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

# TauLib.BookIII.Spectral.TwinPrimeDeep


Deep analysis of the twin prime conjecture on the primorial tower:
extended counting, Hardy-Littlewood constant approximation,
CRT admissibility, and structural theorems.

## Registry Cross-References


- [III.D105] Twin Prime Sieve Count — `twin_prime_sieve_count`

- [III.D106] Hardy-Littlewood Constant — `hl_twin_constant_approx`

- [III.D107] CRT Twin Admissibility — `crt_twin_admissible`

- [III.T72] Twin Primes to 500 — `twin_primes_500`

- [III.T73] Twin Density Primorial — `twin_density_primorial_5`

- [III.T74] HL Constant Convergence — `hl_constant_decreasing_5`

- [III.T75] CRT Admissible Positive — `crt_admissible_positive_4`

- [III.P45] Twin Admissibility Fraction — `twin_admissibility_fraction_5`

- [III.P46] Twin Gap Characterization — (meta-theorem, see docstring)


## Mathematical Content


**III.D107 (CRT Twin Admissibility):** At primorial level k, count residue
classes r mod M_k such that for ALL primes p_i (i≤k), neither r nor r+2
is divisible by p_i. For p=2: r must be odd. For p≥3: r mod p ∉ {0, p-2}.

**III.P45 (Admissibility Fraction):** At each odd prime p ≥ 3, exactly
(p-2) out of p residue classes are twin-admissible. For p=2, exactly 1
out of 2 (the odd residue). Product gives the admissible fraction.

**III.P46 (Twin Gap):** Admissible classes are nonempty at every prime.
Infinitude requires equidistribution (Bombieri-Vinogradov or stronger).

---

### `Tau.BookIII.Spectral.twin_prime_sieve_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L49-L59)
**def
Tau.BookIII.Spectral.twin_prime_sieve_count
(bound : ℕ)
 :ℕ**


[III.D105] Count twin prime pairs (p, p+2) with p ≤ bound via sieve.
Equations
- Tau.BookIII.Spectral.twin_prime_sieve_count bound = Tau.BookIII.Spectral.twin_prime_sieve_count.go bound 2 0 (bound + 1)
Instances For

---

### `Tau.BookIII.Spectral.twin_prime_sieve_count.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L53-L58)@[irreducible]

**def
Tau.BookIII.Spectral.twin_prime_sieve_count.go
(bound p acc fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.hl_twin_constant_approx`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L65-L81)
**def
Tau.BookIII.Spectral.hl_twin_constant_approx
(k : ℕ)
 :ℕ × ℕ**


[III.D106] Hardy-Littlewood twin constant C₂(k) approximation.
C₂(k) = ∏_{i=2}^{k} p_i(p_i-2)/(p_i-1)² (starting from p₂=3).
Returns (numerator, denominator) as integers.
Equations
- Tau.BookIII.Spectral.hl_twin_constant_approx k = Tau.BookIII.Spectral.hl_twin_constant_approx.go k 2 1 1 (k + 1)
Instances For

---

### `Tau.BookIII.Spectral.hl_twin_constant_approx.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L71-L80)@[irreducible]

**def
Tau.BookIII.Spectral.hl_twin_constant_approx.go
(k i num den fuel : ℕ)
 :ℕ × ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.hl_constant_decreasing_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L83-L94)
**def
Tau.BookIII.Spectral.hl_constant_decreasing_check
(lo hi : ℕ)
 :Bool**


[III.T74] HL constant is decreasing: C₂(k+1) ≤ C₂(k).
Equations
- Tau.BookIII.Spectral.hl_constant_decreasing_check lo hi = Tau.BookIII.Spectral.hl_constant_decreasing_check.go hi lo (hi - lo + 1)
Instances For

---

### `Tau.BookIII.Spectral.hl_constant_decreasing_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L87-L93)@[irreducible]

**def
Tau.BookIII.Spectral.hl_constant_decreasing_check.go
(hi k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.is_twin_admissible`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L100-L117)
**def
Tau.BookIII.Spectral.is_twin_admissible
(r d : ℕ)
 :Bool**


Helper: check if residue r is twin-admissible at all primes up to depth d.
For each p_i (i=1..d): r mod p_i ≠ 0 AND (r+2) mod p_i ≠ 0.
This includes p=2: r must be odd.
Equations
- Tau.BookIII.Spectral.is_twin_admissible r d = Tau.BookIII.Spectral.is_twin_admissible.go r d 1 (d + 1)
Instances For

---

### `Tau.BookIII.Spectral.is_twin_admissible.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L106-L116)@[irreducible]

**def
Tau.BookIII.Spectral.is_twin_admissible.go
(r d i fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.crt_twin_admissible`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L119-L130)
**def
Tau.BookIII.Spectral.crt_twin_admissible
(k : ℕ)
 :ℕ**


[III.D107] Count twin-admissible residues mod M_k.
Equations
- Tau.BookIII.Spectral.crt_twin_admissible k = Tau.BookIII.Spectral.crt_twin_admissible.go k 0 0 (Tau.Polarity.primorial k + 1)
Instances For

---

### `Tau.BookIII.Spectral.crt_twin_admissible.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L124-L129)@[irreducible]

**def
Tau.BookIII.Spectral.crt_twin_admissible.go
(k r acc fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.crt_admissible_positive_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L132-L141)
**def
Tau.BookIII.Spectral.crt_admissible_positive_check
(db : ℕ)
 :Bool**


[III.T75] Twin-admissible residues are positive at each depth.
Equations
- Tau.BookIII.Spectral.crt_admissible_positive_check db = Tau.BookIII.Spectral.crt_admissible_positive_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Spectral.crt_admissible_positive_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L136-L140)@[irreducible]

**def
Tau.BookIII.Spectral.crt_admissible_positive_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.twin_density_primorial_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L147-L161)
**def
Tau.BookIII.Spectral.twin_density_primorial_check
(db : ℕ)
 :Bool**


[III.T73] Twin prime density: at least one twin pair exists at
each primorial level k ≥ 2 (M_1=2 is too small).
Uses min(M_k, 500) for computability.
Equations
- Tau.BookIII.Spectral.twin_density_primorial_check db = Tau.BookIII.Spectral.twin_density_primorial_check.go db 2 (db + 1)
Instances For

---

### `Tau.BookIII.Spectral.twin_density_primorial_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L153-L160)@[irreducible]

**def
Tau.BookIII.Spectral.twin_density_primorial_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.count_admissible_at_prime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L167-L177)
**def
Tau.BookIII.Spectral.count_admissible_at_prime
(p : ℕ)
 :ℕ**


Helper: count r in [0..p-1] with r%p ≠ 0 AND (r+2)%p ≠ 0.
Equations
- Tau.BookIII.Spectral.count_admissible_at_prime p = Tau.BookIII.Spectral.count_admissible_at_prime.go p 0 0 (p + 1)
Instances For

---

### `Tau.BookIII.Spectral.count_admissible_at_prime.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L171-L176)@[irreducible]

**def
Tau.BookIII.Spectral.count_admissible_at_prime.go
(p r acc fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.twin_admissibility_fraction_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L179-L196)
**def
Tau.BookIII.Spectral.twin_admissibility_fraction_check
(db : ℕ)
 :Bool**


[III.P45] At each odd prime p ≥ 3, exactly (p-2) out of p residue classes
are twin-admissible. For p=2, exactly 0 out of 2 (since both r=0 and
r=1 fail: r=0 has r%2=0, r=1 has (r+2)%2=1%2≠0 but r=1 has r%2=1≠0
and 3%2=1≠0... actually for p=2: r=1 gives r%2=1, (r+2)%2=1, so admissible.
r=0 gives r%2=0, blocked. So p=2 has 1 admissible. We check p ≥ 3 gives p-2.
Equations
- Tau.BookIII.Spectral.twin_admissibility_fraction_check db = Tau.BookIII.Spectral.twin_admissibility_fraction_check.go db 2 (db + 1)
Instances For

---

### `Tau.BookIII.Spectral.twin_admissibility_fraction_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L187-L195)@[irreducible]

**def
Tau.BookIII.Spectral.twin_admissibility_fraction_check.go
(db i fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.twin_primes_500`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L202-L204)
**theorem
Tau.BookIII.Spectral.twin_primes_500 :twin_prime_sieve_count 500 ≥ 20**


[III.T72] At least 20 twin prime pairs below 500.

---

### `Tau.BookIII.Spectral.twin_density_primorial_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L206-L208)
**theorem
Tau.BookIII.Spectral.twin_density_primorial_5 :twin_density_primorial_check 5 = true**


[III.T73] Twin prime density positive at primorial depths 1..5.

---

### `Tau.BookIII.Spectral.hl_constant_decreasing_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L210-L212)
**theorem
Tau.BookIII.Spectral.hl_constant_decreasing_5 :hl_constant_decreasing_check 2 5 = true**


[III.T74] HL constant decreasing for k = 2..5.

---

### `Tau.BookIII.Spectral.crt_admissible_positive_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L214-L216)
**theorem
Tau.BookIII.Spectral.crt_admissible_positive_4 :crt_admissible_positive_check 4 = true**


[III.T75] CRT-admissible residues positive at depths 1..4.

---

### `Tau.BookIII.Spectral.twin_admissibility_fraction_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L218-L220)
**theorem
Tau.BookIII.Spectral.twin_admissibility_fraction_5 :twin_admissibility_fraction_check 5 = true**


[III.P45] Admissibility fraction = (p-2)/p for primes 3,5,7,11.

---

### `Tau.BookIII.Spectral.twin_count_100`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L226-L228)
**theorem
Tau.BookIII.Spectral.twin_count_100 :twin_prime_sieve_count 100 ≥ 8**


[III.D105] Twin prime count at 100 ≥ 8.

---

### `Tau.BookIII.Spectral.hl_depth_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L230-L232)
**theorem
Tau.BookIII.Spectral.hl_depth_2 :hl_twin_constant_approx 2 = (3, 4)**


[III.D106] HL constant at depth 2: C₂(2) = 3·1/(2·2) = 3/4.

---

### `Tau.BookIII.Spectral.twin_admissible_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L234-L236)
**theorem
Tau.BookIII.Spectral.twin_admissible_1 :crt_twin_admissible 1 = 1**


[III.D107] Twin-admissible residues at depth 1 (mod 2): 1 (only odd).

---

### `Tau.BookIII.Spectral.twin_admissible_3_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L238-L240)
**theorem
Tau.BookIII.Spectral.twin_admissible_3_pos :crt_twin_admissible 3 > 0**


[III.D107] Twin-admissible residues at depth 3 (mod 30).

---

### `Tau.BookIII.Spectral.admissible_at_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L242-L244)
**theorem
Tau.BookIII.Spectral.admissible_at_3 :count_admissible_at_prime 3 = 1**


[III.P45] At prime 3: 1 out of 3 admissible (3-2=1).

---

### `Tau.BookIII.Spectral.admissible_at_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L246-L248)
**theorem
Tau.BookIII.Spectral.admissible_at_5 :count_admissible_at_prime 5 = 3**


[III.P45] At prime 5: 3 out of 5 admissible (5-2=3).

---

### `Tau.BookIII.Spectral.admissible_at_7`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L250-L252)
**theorem
Tau.BookIII.Spectral.admissible_at_7 :count_admissible_at_prime 7 = 5**


[III.P45] At prime 7: 5 out of 7 admissible (7-2=5).
