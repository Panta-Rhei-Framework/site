---
layout: taulib-doc
title: "TauLib.BookI.Boundary.Iota"
permalink: /verify/taulib/docs/book-i-boundary-iota/
lane: verify
module_name: "TauLib.BookI.Boundary.Iota"
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

# TauLib.Boundary.Iota


The master constant iota_tau and the B/C ratio convergence framework.

## Registry Cross-References


- [I.D01] Master Constant — `iota_tau_numer`, `iota_tau_denom`, `iota_tau_float`

- [I.D28] Boundary Local Ring — B/C ratio, `bc_ratio`


## Ground Truth Sources


- chunk_0015_M000074: iota_tau = 2/(pi + e), foundational constant

- chunk_0310_M002679: Polarity counting, B/C ratio convergence


## Mathematical Content


The master constant iota_tau = 2/(pi + e) ~ 0.341304 governs the asymptotic
ratio of B-dominant to C-dominant primes. This module provides:

- **Rational approximation**: iota_tau ~ 341304/1000000 (6 decimal places)

- **B/C ratio**: count_b / count_c computed at various bounds

- **Convergence axiom stub**: the B/C ratio converges to iota_tau
(the formal proof requires analytic number theory beyond current scope)


The constant iota_tau is NOT defined as a real number (TauReal is deferred to
Book II). Instead we work with the rational approximation and Float evaluation.

---

### `Tau.Boundary.iota_tau_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Iota.lean#L40-L41)
**def
Tau.Boundary.iota_tau_numer :ℕ**


Numerator of iota_tau rational approximation (6 decimal places).
Equations
- Tau.Boundary.iota_tau_numer = 341304
Instances For

---

### `Tau.Boundary.iota_tau_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Iota.lean#L43-L44)
**def
Tau.Boundary.iota_tau_denom :ℕ**


Denominator of iota_tau rational approximation.
Equations
- Tau.Boundary.iota_tau_denom = 1000000
Instances For

---

### `Tau.Boundary.iota_tau_denom_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Iota.lean#L46-L48)
**theorem
Tau.Boundary.iota_tau_denom_pos :iota_tau_denom > 0**


iota_tau denominator is positive.

---

### `Tau.Boundary.iota_tau_float`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Iota.lean#L50-L53)
**def
Tau.Boundary.iota_tau_float :Float**


Float approximation of iota_tau = 2/(pi + e) ~ 0.341304.
Since Lean 4 Float does not have a built-in pi constant,
we use the known decimal approximation.
Equations
- Tau.Boundary.iota_tau_float = 0.341304
Instances For

---

### `Tau.Boundary.iota_tau_rat_float`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Iota.lean#L55-L57)
**def
Tau.Boundary.iota_tau_rat_float :Float**


Float approximation from the rational approximation.
Equations
- Tau.Boundary.iota_tau_rat_float = Float.ofNat Tau.Boundary.iota_tau_numer / Float.ofNat Tau.Boundary.iota_tau_denom
Instances For

---

### `Tau.Boundary.bc_ratio_pair`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Iota.lean#L63-L66)
**def
Tau.Boundary.bc_ratio_pair
(n N : Denotation.TauIdx)
 :ℕ × ℕ**


B/C count ratio as a pair (numerator, denominator).
Returns (count_b, count_c) where the ratio is count_b / count_c.
Equations
- Tau.Boundary.bc_ratio_pair n N = (Tau.Polarity.count_b_dominant n N, Tau.Polarity.count_c_dominant n N)
Instances For

---

### `Tau.Boundary.bc_ratio_float`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Iota.lean#L68-L72)
**def
Tau.Boundary.bc_ratio_float
(n N : Denotation.TauIdx)
 :Float**


B/C ratio as a Float. Returns 0.0 if there are no C-dominant primes.
Equations
- Tau.Boundary.bc_ratio_float n N = match Tau.Boundary.bc_ratio_pair n N with
 | (b, c) => if c = 0 then 0.0 else Float.ofNat b / Float.ofNat c
Instances For

---

### `Tau.Boundary.bc_ratio_scaled`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Iota.lean#L74-L78)
**def
Tau.Boundary.bc_ratio_scaled
(n N : Denotation.TauIdx)
 :ℕ**


Scaled B/C ratio: (count_b * 1000000) / count_c, for integer comparison.
Equations
- Tau.Boundary.bc_ratio_scaled n N = match Tau.Boundary.bc_ratio_pair n N with
 | (b, c) => if c = 0 then 0 else b * 1000000 / c
Instances For

---

### `Tau.Boundary.ConvergenceClaimFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Iota.lean#L84-L92)
**def
Tau.Boundary.ConvergenceClaimFloat
(N : Denotation.TauIdx)
 :Prop**


The convergence claim: for all epsilon > 0, there exists N₀ such that
for all n ≥ N₀, |bc_ratio(n, N) - iota_tau| < epsilon.
This is an axiom stub — the proof requires analytic number theory
(effective prime number theorem + polarity equidistribution)
which is beyond the current mechanization scope.
Equations
- Tau.Boundary.ConvergenceClaimFloat N = ∀ (eps : Float),
 eps > 0.0 →
 ∃ (n0 : ℕ), ∀ (n : ℕ), n ≥ n0 → (Tau.Boundary.bc_ratio_float n N - Tau.Boundary.iota_tau_float).abs < eps
Instances For

---

### `Tau.Boundary.ConvergenceClaimRat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Iota.lean#L94-L106)
**def
Tau.Boundary.ConvergenceClaimRat
(N : Denotation.TauIdx)

(k : ℕ)
 :Prop**


Convergence claim in rational form: for all k (precision level),
there exists n0 such that for n ≥ n0,
|count_b(n,N) * denom - numer * count_c(n,N)| < count_c(n,N) * (denom / 10^k).
This is the pure Nat formulation avoiding Float.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.both_channels_active`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Iota.lean#L112-L115)
**def
Tau.Boundary.both_channels_active
(n N : Denotation.TauIdx)
 :Bool**


Check that both B and C counts are positive at bound n, N.
Equations
- Tau.Boundary.both_channels_active n N = match Tau.Boundary.bc_ratio_pair n N with
 | (b, c) => decide (b > 0) && decide (c > 0)
Instances For

---

### `Tau.Boundary.b_minority_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Iota.lean#L117-L120)
**def
Tau.Boundary.b_minority_check
(n N : Denotation.TauIdx)
 :Bool**


Check that B-count < C-count (since iota_tau < 1, B should be minority).
Equations
- Tau.Boundary.b_minority_check n N = match Tau.Boundary.bc_ratio_pair n N with
 | (b, c) => decide (b < c)
Instances For
