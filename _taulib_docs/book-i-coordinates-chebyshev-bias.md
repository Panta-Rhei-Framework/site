---
layout: taulib-doc
title: "TauLib.BookI.Coordinates.ChebyshevBias"
permalink: /verify/taulib/docs/book-i-coordinates-chebyshev-bias/
lane: verify
module_name: "TauLib.BookI.Coordinates.ChebyshevBias"
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

# TauLib.Coordinates.ChebyshevBias


Chebyshev bias (prime races) on the primorial tower: primes in
arithmetic progressions, race tracking, and bias quantification.

## Registry Cross-References


- [I.D97] Prime Counting in Progressions — `prime_count_mod`, `prime_race_check`

- [I.D98] Chebyshev Bias Measure — `chebyshev_bias`, `bias_quantification_check`

- [I.T50] Bias at Primorial Levels — `bias_primorial_check`


## Mathematical Content


**I.D97 (Prime Counting in Progressions):** π(x; q, a) counts primes
p ≤ x with p ≡ a (mod q). For q = 4: π(x;4,3) typically exceeds
π(x;4,1) (Chebyshev's observation). For q = 3: π(x;3,2) typically
exceeds π(x;3,1). These biases reflect the quadratic residue structure.

**I.D98 (Chebyshev Bias Measure):** The bias B(x; q, a₁, a₂) counts
how often π(n; q, a₁) > π(n; q, a₂) for n ≤ x. The bias ratio
B/x → δ ∈ (0.5, 1) quantifies the strength of the race advantage.

**I.T50 (Bias at Primorial Levels):** At each primorial level M_k,
the Chebyshev bias for (q=4, a=3 vs a=1) is positive. The bias
connects to the B/C sector asymmetry in the spectral decomposition:
non-residues (3 mod 4) bias reflects the C-sector dominance at
small primorial levels.

---

### `Tau.Coordinates.prime_count_mod`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/ChebyshevBias.lean#L55-L66)
**def
Tau.Coordinates.prime_count_mod
(x q a : Nat)
 :Nat**


[I.D97] Count primes p ≤ x with p ≡ a (mod q).
Equations
- Tau.Coordinates.prime_count_mod x q a = if (q == 0) = true then 0 else Tau.Coordinates.prime_count_mod.go x q a 2 0 (x + 1)
Instances For

---

### `Tau.Coordinates.prime_count_mod.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/ChebyshevBias.lean#L60-L65)@[irreducible]

**def
Tau.Coordinates.prime_count_mod.go
(x q a p acc fuel : Nat)
 :Nat**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Coordinates.prime_race_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/ChebyshevBias.lean#L68-L81)
**def
Tau.Coordinates.prime_race_check
(bound q a1 a2 : Nat)
 :Bool**


[I.D97] Prime race: compare π(x; q, a₁) vs π(x; q, a₂).
Equations
- Tau.Coordinates.prime_race_check bound q a1 a2 = Tau.Coordinates.prime_race_check.go bound q a1 a2 2 (bound + 1)
Instances For

---

### `Tau.Coordinates.prime_race_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/ChebyshevBias.lean#L72-L80)@[irreducible]

**def
Tau.Coordinates.prime_race_check.go
(bound q a1 a2 x fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Coordinates.chebyshev_bias`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/ChebyshevBias.lean#L87-L101)
**def
Tau.Coordinates.chebyshev_bias
(x q a1 a2 : Nat)
 :Nat**


[I.D98] Chebyshev bias: count how often π(n;q,a₁) > π(n;q,a₂)
for n from 2 to x. Returns the count of "winning" values.
Equations
- Tau.Coordinates.chebyshev_bias x q a1 a2 = if (q == 0) = true then 0 else Tau.Coordinates.chebyshev_bias.go x 2 0 (x + 1) q a1 a2
Instances For

---

### `Tau.Coordinates.chebyshev_bias.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/ChebyshevBias.lean#L93-L100)@[irreducible]

**def
Tau.Coordinates.chebyshev_bias.go
(x n acc fuel q a1 a2 : Nat)
 :Nat**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Coordinates.bias_quantification_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/ChebyshevBias.lean#L103-L108)
**def
Tau.Coordinates.bias_quantification_check
(bound : Nat)
 :Bool**


[I.D98] Bias quantification: the bias for (q=4, a=3 vs a=1) is
positive up to x. That is, π(n;4,3) > π(n;4,1) more often than not.
Equations
- Tau.Coordinates.bias_quantification_check bound = decide (Tau.Coordinates.chebyshev_bias bound 4 3 1 > Tau.Coordinates.chebyshev_bias bound 4 1 3)
Instances For

---

### `Tau.Coordinates.bias_mod3_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/ChebyshevBias.lean#L110-L114)
**def
Tau.Coordinates.bias_mod3_check
(bound : Nat)
 :Bool**


[I.D98] Bias for q=3: π(x;3,2) vs π(x;3,1).
Equations
- Tau.Coordinates.bias_mod3_check bound = decide (Tau.Coordinates.chebyshev_bias bound 3 2 1 ≥ Tau.Coordinates.chebyshev_bias bound 3 1 2)
Instances For

---

### `Tau.Coordinates.bias_primorial_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/ChebyshevBias.lean#L120-L157)
**def
Tau.Coordinates.bias_primorial_check
(db : Nat)
 :Bool**


[I.T50] Bias at primorial levels: at each M_k (capped at 50),
the Chebyshev bias (q=4, 3 vs 1) is positive.
Equations
- Tau.Coordinates.bias_primorial_check db = Tau.Coordinates.bias_primorial_check.go db 2 (db + 1)
Instances For

---

### `Tau.Coordinates.bias_primorial_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/ChebyshevBias.lean#L125-L134)@[irreducible]

**def
Tau.Coordinates.bias_primorial_check.go
(db k fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Coordinates.bias_primorial_check.go_primorial`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/ChebyshevBias.lean#L137-L138)
**def
Tau.Coordinates.bias_primorial_check.go_primorial
(k : Nat)
 :Nat**

Equations
- Tau.Coordinates.bias_primorial_check.go_primorial k = Tau.Coordinates.bias_primorial_check.go_p 1 k 1 (k + 1)
Instances For

---

### `Tau.Coordinates.bias_primorial_check.go_p`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/ChebyshevBias.lean#L140-L145)@[irreducible]

**def
Tau.Coordinates.bias_primorial_check.go_p
(i bound acc fuel : Nat)
 :Nat**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Coordinates.bias_primorial_check.go_nth_prime`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/ChebyshevBias.lean#L147-L148)
**def
Tau.Coordinates.bias_primorial_check.go_nth_prime
(k : Nat)
 :Nat**

Equations
- Tau.Coordinates.bias_primorial_check.go_nth_prime k = Tau.Coordinates.bias_primorial_check.go_np 2 k (100 * (k + 1))
Instances For

---

### `Tau.Coordinates.bias_primorial_check.go_np`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/ChebyshevBias.lean#L150-L156)@[irreducible]

**def
Tau.Coordinates.bias_primorial_check.go_np
(n count fuel : Nat)
 :Nat**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Coordinates.prime_race_4_50`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/ChebyshevBias.lean#L163-L165)
**theorem
Tau.Coordinates.prime_race_4_50 :prime_race_check 50 4 3 1 = true**


[I.D97] Prime race (q=4) is well-defined up to 50.

---

### `Tau.Coordinates.bias_positive_50`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/ChebyshevBias.lean#L167-L169)
**theorem
Tau.Coordinates.bias_positive_50 :bias_quantification_check 50 = true**


[I.D98] Chebyshev bias (q=4, 3 vs 1) is positive up to 50.

---

### `Tau.Coordinates.bias_mod3_50`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/ChebyshevBias.lean#L171-L173)
**theorem
Tau.Coordinates.bias_mod3_50 :bias_mod3_check 50 = true**


[I.D98] Bias mod 3 check up to 50.

---

### `Tau.Coordinates.bias_primorial_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Coordinates/ChebyshevBias.lean#L175-L177)
**theorem
Tau.Coordinates.bias_primorial_3 :bias_primorial_check 3 = true**


[I.T50] Bias at primorial levels up to depth 3.
