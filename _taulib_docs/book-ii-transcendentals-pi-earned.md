---
layout: taulib-doc
title: "TauLib.BookII.Transcendentals.PiEarned"
permalink: /verify/taulib/docs/book-ii-transcendentals-pi-earned/
lane: verify
module_name: "TauLib.BookII.Transcendentals.PiEarned"
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

# TauLib.BookII.Transcendentals.PiEarned


Pi earned from three perspectives: Leibniz series, spectral, topological.

## Registry Cross-References


- [II.D28] Geometric Pi -- `pi_scaled`

- [II.D29] Archimedes Polygon Sequence -- `leibniz_pi_scaled`

- [II.T22] Three Perspectives on Pi -- `pi_convergence_check`


## Mathematical Content


Pi is earned from within tau^3, NOT imported from external analysis.
Three convergent perspectives:

- 
**Leibniz series**: pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...
Computable via scaled integer arithmetic (avoids Float).


- 
**Spectral**: B-channel characters at stage k have period
related to pi (circle winding number).


- 
**Topological**: lemniscate half-period = pi * iota_tau.


Since Float.pi does not exist in Lean 4 and Float arithmetic
is unreliable, all computations use scaled integer arithmetic.
pi * 10^6 ~ 3141592.

---

### `Tau.BookII.Transcendentals.leibniz_pi_scaled`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/PiEarned.lean#L41-L58)
**def
Tau.BookII.Transcendentals.leibniz_pi_scaled
(terms scale : Nat)
 :Nat**


[II.D29] Leibniz series for pi: pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...
Returns pi * scale (approximately), computed as 4 * scale * sum.

Uses separate positive and negative accumulators to avoid Nat underflow.
Final result = 4 * (pos_sum - neg_sum) where each term = scale / (2k+1).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.leibniz_pi_scaled.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/PiEarned.lean#L50-L57)@[irreducible]

**def
Tau.BookII.Transcendentals.leibniz_pi_scaled.go
(terms scale k fuel pos neg : Nat)
 :Nat × Nat**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.pi_scaled`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/PiEarned.lean#L60-L62)
**def
Tau.BookII.Transcendentals.pi_scaled
(terms : Nat)
 :Nat**


pi approximation at various term counts.
More terms = better approximation of pi * 10^6.
Equations
- Tau.BookII.Transcendentals.pi_scaled terms = Tau.BookII.Transcendentals.leibniz_pi_scaled terms 1000000
Instances For

---

### `Tau.BookII.Transcendentals.pi_convergence_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/PiEarned.lean#L68-L76)
**def
Tau.BookII.Transcendentals.pi_convergence_check :Bool**


[II.T22, perspective 1] Leibniz convergence: with enough terms,
the scaled pi approximation falls within a reasonable range.

pi * 10^6 = 3141592. With 1000 terms, Leibniz gives 3140592
(Leibniz converges slowly: error 1/N).
We check it lands in [3100000, 3200000].
Equations
- Tau.BookII.Transcendentals.pi_convergence_check = (decide (Tau.BookII.Transcendentals.pi_scaled 1000 > 3100000) && decide (Tau.BookII.Transcendentals.pi_scaled 1000 < 3200000))
Instances For

---

### `Tau.BookII.Transcendentals.pi_improvement_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/PiEarned.lean#L78-L94)
**def
Tau.BookII.Transcendentals.pi_improvement_check :Bool**


Monotone improvement: more terms should bring the approximation
closer to the true value. Evidence: the difference between
successive approximations decreases.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.spectral_pi_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/PiEarned.lean#L100-L111)
**def
Tau.BookII.Transcendentals.spectral_pi_check
(bound : Denotation.TauIdx)
 :Bool**


[II.T22, perspective 2] Spectral evidence: the number of
B-residues mod p_k (complete residue system) witnesses the
winding number. At prime p_k, B cycles through p_k values,
contributing 2*pi/p_k angular width per residue.

The full circle 2*pi is partitioned into p_k arcs.
Evidence: residue count = p_k exactly.
Equations
- Tau.BookII.Transcendentals.spectral_pi_check bound = (Tau.BookII.Transcendentals.circle_profinite_b_check 1 bound && Tau.BookII.Transcendentals.circle_profinite_b_check 2 bound)
Instances For

---

### `Tau.BookII.Transcendentals.topological_pi_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/PiEarned.lean#L117-L132)
**def
Tau.BookII.Transcendentals.topological_pi_check :Bool**


[II.T22, perspective 3] Topological evidence: the lemniscate
half-period is pi * iota_tau. In scaled arithmetic:
half_period * 10^6 = pi * iota_tau * 10^6
 3141592 * 341304 / 10^6
 1072793

We verify the numerical relationship:
pi_scaled * iota_tau_numer / iota_tau_denom should give a
consistent half-period value.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.three_perspectives_pi_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/PiEarned.lean#L134-L138)
**def
Tau.BookII.Transcendentals.three_perspectives_pi_check
(bound : Denotation.TauIdx)
 :Bool**


[II.T22] Full three-perspective check.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.pi_conv`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/PiEarned.lean#L164-L164)
**theorem
Tau.BookII.Transcendentals.pi_conv :pi_convergence_check = true**


---

### `Tau.BookII.Transcendentals.pi_improve`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/PiEarned.lean#L165-L165)
**theorem
Tau.BookII.Transcendentals.pi_improve :pi_improvement_check = true**


---

### `Tau.BookII.Transcendentals.spectral_pi`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/PiEarned.lean#L166-L166)
**theorem
Tau.BookII.Transcendentals.spectral_pi :spectral_pi_check 200 = true**


---

### `Tau.BookII.Transcendentals.topo_pi`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/PiEarned.lean#L167-L167)
**theorem
Tau.BookII.Transcendentals.topo_pi :topological_pi_check = true**


---

### `Tau.BookII.Transcendentals.three_persp_pi`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/PiEarned.lean#L168-L168)
**theorem
Tau.BookII.Transcendentals.three_persp_pi :three_perspectives_pi_check 200 = true**
