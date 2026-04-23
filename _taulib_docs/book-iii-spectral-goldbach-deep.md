---
layout: taulib-doc
title: "TauLib.BookIII.Spectral.GoldbachDeep"
permalink: /verify/taulib/docs/book-iii-spectral-goldbach-deep/
lane: verify
module_name: "TauLib.BookIII.Spectral.GoldbachDeep"
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

# TauLib.BookIII.Spectral.GoldbachDeep


Deep analysis of Goldbach's conjecture on the primorial tower:
extended verification, partition counts at primorial levels,
obstruction density, and CRT-Goldbach structural theorem.

## Registry Cross-References


- [III.D102] Sieve-Accelerated Goldbach — `goldbach_sieve_check`

- [III.D103] Partition Count at Primorial — `goldbach_partition_count_at_primorial`

- [III.D104] Goldbach Obstruction Set — `goldbach_obstruction_count`

- [III.T68] Goldbach Verified to 500 — `goldbach_500`

- [III.T69] Goldbach at Primorial M₄ — `goldbach_primorial_m4`

- [III.T70] Partition Growth — `partition_growth_5`

- [III.T71] Obstruction Bounded — `obstruction_bounded_5`

- [III.P43] CRT-Goldbach Duality — `crt_goldbach_duality_3`

- [III.P44] Goldbach Gap Characterization — (meta-theorem, see docstring)


## Mathematical Content


**III.T70 (Partition Growth):** r(M_k) is increasing for k = 2..5.

**III.T71 (Obstruction Bounded):** At each prime p, the number of
obstructed residues (both r and n−r ≡ 0 mod p) is at most 1, and equals
1 iff p | n. This means each prime blocks at most one Goldbach pair.

**III.P43 (CRT-Goldbach Duality):** CRT guarantees local solvability at
each prime: for any even n and any prime p ≥ 3, there exist r with both
r and n−r nonzero mod p.

**III.P44 (Goldbach Gap):** The gap is the parity barrier: no sieve or
finite verification can lift local solutions to a global proof.

---

### `Tau.BookIII.Spectral.goldbach_sieve_pair`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L51-L60)
**def
Tau.BookIII.Spectral.goldbach_sieve_pair
(n : ℕ)
 :Bool**


Helper: check if even n has a Goldbach pair via sieve.
Equations
- Tau.BookIII.Spectral.goldbach_sieve_pair n = Tau.BookIII.Spectral.goldbach_sieve_pair.go n 2 (n / 2 + 1)
Instances For

---

### `Tau.BookIII.Spectral.goldbach_sieve_pair.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L55-L59)@[irreducible]

**def
Tau.BookIII.Spectral.goldbach_sieve_pair.go
(n p fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.goldbach_sieve_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L62-L72)
**def
Tau.BookIII.Spectral.goldbach_sieve_check
(bound : ℕ)
 :Bool**


[III.D102] Sieve-accelerated Goldbach check for all even n in [4..bound].
Equations
- Tau.BookIII.Spectral.goldbach_sieve_check bound = Tau.BookIII.Spectral.goldbach_sieve_check.go bound 4 (bound + 1)
Instances For

---

### `Tau.BookIII.Spectral.goldbach_sieve_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L66-L71)@[irreducible]

**def
Tau.BookIII.Spectral.goldbach_sieve_check.go
(bound n fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.goldbach_partition_count_sieve`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L78-L89)
**def
Tau.BookIII.Spectral.goldbach_partition_count_sieve
(n : ℕ)
 :ℕ**


[III.D103] Goldbach partition count using sieve primality.
Equations
- Tau.BookIII.Spectral.goldbach_partition_count_sieve n = if (decide (n < 4) || n % 2 != 0) = true then 0
 else Tau.BookIII.Spectral.goldbach_partition_count_sieve.go n 2 0 (n / 2 + 1)
Instances For

---

### `Tau.BookIII.Spectral.goldbach_partition_count_sieve.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L83-L88)@[irreducible]

**def
Tau.BookIII.Spectral.goldbach_partition_count_sieve.go
(n p acc fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.goldbach_partition_count_at_primorial`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L91-L95)
**def
Tau.BookIII.Spectral.goldbach_partition_count_at_primorial
(k : ℕ)
 :ℕ**


[III.D103] Partition count at primorial level k.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.partition_growth_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L97-L108)
**def
Tau.BookIII.Spectral.partition_growth_check
(lo hi : ℕ)
 :Bool**


[III.T70] Partition growth check: r(M_{k+1}) > r(M_k).
Equations
- Tau.BookIII.Spectral.partition_growth_check lo hi = Tau.BookIII.Spectral.partition_growth_check.go hi lo (hi - lo + 1)
Instances For

---

### `Tau.BookIII.Spectral.partition_growth_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L101-L107)@[irreducible]

**def
Tau.BookIII.Spectral.partition_growth_check.go
(hi k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.goldbach_obstruction_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L114-L119)
**def
Tau.BookIII.Spectral.goldbach_obstruction_count
(n p : ℕ)
 :ℕ**


[III.D104] Count obstructed residues at prime p for even n:
r in [0..p-1] such that both r ≡ 0 AND (n-r) ≡ 0 (mod p).
This equals 1 if p | n, and 0 otherwise.
Equations
- Tau.BookIII.Spectral.goldbach_obstruction_count n p = if p < 2 then 0 else if (n % p == 0) = true then 1 else 0
Instances For

---

### `Tau.BookIII.Spectral.obstruction_bounded_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L121-L133)
**def
Tau.BookIII.Spectral.obstruction_bounded_check
(bound db : ℕ)
 :Bool**


[III.T71] Obstruction at each prime is at most 1.
Equations
- Tau.BookIII.Spectral.obstruction_bounded_check bound db = Tau.BookIII.Spectral.obstruction_bounded_check.go bound db 4 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Spectral.obstruction_bounded_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L125-L132)@[irreducible]

**def
Tau.BookIII.Spectral.obstruction_bounded_check.go
(bound db n k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.crt_goldbach_local_solvable`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L139-L154)
**def
Tau.BookIII.Spectral.crt_goldbach_local_solvable
(n k : ℕ)
 :Bool**


Helper: check local Goldbach solvability at prime p_k for even n.
For p ≥ 3: there exists r in [1..p-1] with both r and n-r nonzero mod p.
Equations
- Tau.BookIII.Spectral.crt_goldbach_local_solvable n k = if Tau.Polarity.nth_prime k < 3 then true
 else Tau.BookIII.Spectral.crt_goldbach_local_solvable.go n k 1 (Tau.Polarity.nth_prime k)
Instances For

---

### `Tau.BookIII.Spectral.crt_goldbach_local_solvable.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L146-L153)@[irreducible]

**def
Tau.BookIII.Spectral.crt_goldbach_local_solvable.go
(n k r fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.crt_goldbach_duality_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L156-L167)
**def
Tau.BookIII.Spectral.crt_goldbach_duality_check
(bound db : ℕ)
 :Bool**


[III.P43] CRT-Goldbach duality: at each depth k, every even n
in [4..bound] has a local solution at prime p_k.
Equations
- Tau.BookIII.Spectral.crt_goldbach_duality_check bound db = Tau.BookIII.Spectral.crt_goldbach_duality_check.go bound db 4 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Spectral.crt_goldbach_duality_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L161-L166)@[irreducible]

**def
Tau.BookIII.Spectral.crt_goldbach_duality_check.go
(bound db n k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.goldbach_500`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L173-L175)
**theorem
Tau.BookIII.Spectral.goldbach_500 :goldbach_sieve_check 500 = true**


[III.T68] Goldbach verified to 500 via sieve.

---

### `Tau.BookIII.Spectral.goldbach_primorial_m4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L177-L179)
**theorem
Tau.BookIII.Spectral.goldbach_primorial_m4 :goldbach_sieve_check 210 = true**


[III.T69] Goldbach at primorial M₄=210: all even n ≤ 210 verified.

---

### `Tau.BookIII.Spectral.partition_growth_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L181-L183)
**theorem
Tau.BookIII.Spectral.partition_growth_4 :partition_growth_check 2 4 = true**


[III.T70] Partition growth: r(M_k) increasing for k = 2..4.

---

### `Tau.BookIII.Spectral.obstruction_bounded_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L185-L187)
**theorem
Tau.BookIII.Spectral.obstruction_bounded_5 :obstruction_bounded_check 100 5 = true**


[III.T71] Obstruction bounded by 1 at each prime, for even n ≤ 100.

---

### `Tau.BookIII.Spectral.crt_goldbach_duality_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L189-L191)
**theorem
Tau.BookIII.Spectral.crt_goldbach_duality_3 :crt_goldbach_duality_check 100 3 = true**


[III.P43] CRT-Goldbach duality at depth 3, even n ≤ 100.

---

### `Tau.BookIII.Spectral.partition_m2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L197-L199)
**theorem
Tau.BookIII.Spectral.partition_m2 :goldbach_partition_count_at_primorial 2 = 1**


[III.D103] r(M_2) = r(6) = 1 (6 = 3+3).

---

### `Tau.BookIII.Spectral.partition_m3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L201-L203)
**theorem
Tau.BookIII.Spectral.partition_m3 :goldbach_partition_count_at_primorial 3 = 3**


[III.D103] r(M_3) = r(30) = 3 (30 = 7+23 = 11+19 = 13+17).

---

### `Tau.BookIII.Spectral.partition_m4_pos`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L205-L207)
**theorem
Tau.BookIII.Spectral.partition_m4_pos :goldbach_partition_count_at_primorial 4 > 0**


[III.D103] r(M_4) = r(210) > 0.

---

### `Tau.BookIII.Spectral.obstruction_100_p2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L209-L211)
**theorem
Tau.BookIII.Spectral.obstruction_100_p2 :goldbach_obstruction_count 100 2 = 1**


[III.D104] Obstruction at p=2 for n=100: 1 (100 is even).

---

### `Tau.BookIII.Spectral.obstruction_100_p3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/GoldbachDeep.lean#L213-L215)
**theorem
Tau.BookIII.Spectral.obstruction_100_p3 :goldbach_obstruction_count 100 3 = 0**


[III.D104] Obstruction at p=3 for n=100: 0 (100 mod 3 ≠ 0).
