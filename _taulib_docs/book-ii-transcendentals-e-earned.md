---
layout: taulib-doc
title: "TauLib.BookII.Transcendentals.EEarned"
permalink: /verify/taulib/docs/book-ii-transcendentals-e-earned/
lane: verify
module_name: "TauLib.BookII.Transcendentals.EEarned"
book: "II"
book_label: "Holomorphy"
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
    book: "Book II"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookII.Transcendentals.EEarned


Euler's number e earned from the factorial series and primorial growth.

## Registry Cross-References


- [II.D30] e as Iterator Eigenvalue -- `e_factorial_scaled`

- [II.D31] Growth Base -- `primorial_growth_check`

- [II.T23] e from Index Arithmetic -- `e_convergence_check`


## Mathematical Content


e is earned from the growth rate of the primorial tower and the factorial
series e = sum_{k=0}^{N} 1/k!.

Since Float arithmetic is unreliable in Lean 4, all computations use
scaled integer arithmetic: e * 10^6 ~ 2718281.

The primorial growth P_{k+1}/P_k = p_{k+1} is super-exponential.
By PNT, ln(P_k) = sum ln(p_i) ~ k*ln(k), so the growth base
e appears naturally as the base of natural logarithms.

---

### `Tau.BookII.Transcendentals.e_factorial_scaled`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/EEarned.lean#L36-L49)
**def
Tau.BookII.Transcendentals.e_factorial_scaled
(terms scale : Nat)
 :Nat**


[II.D30] e via factorial series: e = sum_{k=0}^{N} 1/k!
Returns e * scale (approximately).
Tracks the running factorial to avoid recomputation.
Equations
- Tau.BookII.Transcendentals.e_factorial_scaled terms scale = Tau.BookII.Transcendentals.e_factorial_scaled.go terms scale 0 (terms + 1) 1 0
Instances For

---

### `Tau.BookII.Transcendentals.e_factorial_scaled.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/EEarned.lean#L42-L48)@[irreducible]

**def
Tau.BookII.Transcendentals.e_factorial_scaled.go
(terms scale k fuel factorial acc : Nat)
 :Nat**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.e_scaled`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/EEarned.lean#L51-L52)
**def
Tau.BookII.Transcendentals.e_scaled
(terms : Nat)
 :Nat**


e approximation: e * 10^6 using N terms of the factorial series.
Equations
- Tau.BookII.Transcendentals.e_scaled terms = Tau.BookII.Transcendentals.e_factorial_scaled terms 1000000
Instances For

---

### `Tau.BookII.Transcendentals.e_convergence_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/EEarned.lean#L58-L64)
**def
Tau.BookII.Transcendentals.e_convergence_check :Bool**


[II.T23] e from index arithmetic: e * 10^6 ~ 2718281.
The factorial series converges MUCH faster than Leibniz:
10 terms gives 6+ digits of accuracy.
Check: result in [2700000, 2750000].
Equations
- Tau.BookII.Transcendentals.e_convergence_check = (decide (Tau.BookII.Transcendentals.e_scaled 10 > 2700000) && decide (Tau.BookII.Transcendentals.e_scaled 10 < 2750000))
Instances For

---

### `Tau.BookII.Transcendentals.e_rapid_convergence_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/EEarned.lean#L66-L79)
**def
Tau.BookII.Transcendentals.e_rapid_convergence_check :Bool**


Rapid convergence: fewer terms already give reasonable accuracy.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.primorial_growth_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/EEarned.lean#L85-L99)
**def
Tau.BookII.Transcendentals.primorial_growth_check
(stages : Denotation.TauIdx)
 :Bool**


[II.D31] Growth base: consecutive primorial ratios.
P_{k+1} / P_k = p_{k+1} >= 2 for all k >= 0.
The primorial sequence grows super-exponentially.
Equations
- Tau.BookII.Transcendentals.primorial_growth_check stages = Tau.BookII.Transcendentals.primorial_growth_check.go stages 1 (stages + 1)
Instances For

---

### `Tau.BookII.Transcendentals.primorial_growth_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/EEarned.lean#L91-L98)@[irreducible]

**def
Tau.BookII.Transcendentals.primorial_growth_check.go
(stages : Denotation.TauIdx)

(k fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.primorial_ratio_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/EEarned.lean#L101-L114)
**def
Tau.BookII.Transcendentals.primorial_ratio_check
(stages : Denotation.TauIdx)
 :Bool**


Primorial ratios match primes: P_{k+1}/P_k = p_{k+1} exactly.
Equations
- Tau.BookII.Transcendentals.primorial_ratio_check stages = Tau.BookII.Transcendentals.primorial_ratio_check.go stages 1 (stages + 1)
Instances For

---

### `Tau.BookII.Transcendentals.primorial_ratio_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/EEarned.lean#L105-L113)@[irreducible]

**def
Tau.BookII.Transcendentals.primorial_ratio_check.go
(stages : Denotation.TauIdx)

(k fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.nat_factorial`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/EEarned.lean#L120-L123)
**def
Tau.BookII.Transcendentals.nat_factorial :Nat → Nat**


Factorial function for comparison with primorial.
Equations
- Tau.BookII.Transcendentals.nat_factorial 0 = 1
- Tau.BookII.Transcendentals.nat_factorial n.succ = (n + 1) * Tau.BookII.Transcendentals.nat_factorial n
Instances For

---

### `Tau.BookII.Transcendentals.factorial_primorial_compare`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/EEarned.lean#L125-L129)
**def
Tau.BookII.Transcendentals.factorial_primorial_compare
(k : Denotation.TauIdx)
 :Nat × Nat**


Factorial vs primorial comparison: for small k, primorial(k) < k!
(since primes are sparse), but both grow super-exponentially.
The ratio n!/P_n provides an e-related growth constant.
Equations
- Tau.BookII.Transcendentals.factorial_primorial_compare k = (Tau.BookII.Transcendentals.nat_factorial k, Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookII.Transcendentals.e_conv`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/EEarned.lean#L156-L156)
**theorem
Tau.BookII.Transcendentals.e_conv :e_convergence_check = true**


---

### `Tau.BookII.Transcendentals.e_rapid`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/EEarned.lean#L157-L157)
**theorem
Tau.BookII.Transcendentals.e_rapid :e_rapid_convergence_check = true**


---

### `Tau.BookII.Transcendentals.prim_growth_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/EEarned.lean#L158-L158)
**theorem
Tau.BookII.Transcendentals.prim_growth_5 :primorial_growth_check 5 = true**


---

### `Tau.BookII.Transcendentals.prim_ratio_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/EEarned.lean#L159-L159)
**theorem
Tau.BookII.Transcendentals.prim_ratio_5 :primorial_ratio_check 5 = true**
