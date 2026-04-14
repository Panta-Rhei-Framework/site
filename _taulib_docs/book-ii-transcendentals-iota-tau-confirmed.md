---
layout: taulib-doc
title: "TauLib.BookII.Transcendentals.IotaTauConfirmed"
permalink: /verify/taulib/docs/book-ii-transcendentals-iota-tau-confirmed/
lane: verify
module_name: "TauLib.BookII.Transcendentals.IotaTauConfirmed"
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

# TauLib.BookII.Transcendentals.IotaTauConfirmed


Master constant iota_tau = 2/(pi + e) confirmed with earned pi and e.

## Registry Cross-References


- [II.T25] Master Constant Confirmed -- `iota_tau_confirmed_check`

- [II.D34] Archimedean Bridge -- `archimedean_bridge_check`

- [II.P07] Refinement Resolution Bound -- `refinement_resolution_check`


## Mathematical Content


The master constant iota_tau = 2/(pi + e) ~ 0.341304 is now confirmed
using the pi and e earned in the previous modules. This closes the
circle: iota_tau was introduced axiomatically in Book I; now it is
derived from earned transcendentals.

The Archimedean bridge: iota_tau mediates between the Archimedean world
(pi, e from limits/series) and the profinite world (tau^3 from primorial
inverse system). The resolution crossover happens between stages k=1
and k=2: 1/P_1 = 0.5 > iota_tau > 1/P_2 ~ 0.167.

Refinement resolution bound: at stage k, the approximation error is
bounded by 1/P_k, which decreases monotonically.

---

### `Tau.BookII.Transcendentals.iota_tau_computed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L39-L49)
**def
Tau.BookII.Transcendentals.iota_tau_computed
(pi_terms e_terms scale : ℕ)
 :ℕ**


Compute iota_tau * scale using earned pi and e approximations.
iota_tau = 2 / (pi + e).
In scaled arithmetic: iota_tau * scale = 2 * scale^2 / (pi_scaled + e_scaled).

pi_scaled and e_scaled are both in units of 10^6.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.iota_tau_confirmed_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L51-L58)
**def
Tau.BookII.Transcendentals.iota_tau_confirmed_check :Bool**


[II.T25] Master constant confirmed: iota_tau 0.341304.
iota_tau * 10^6 341304.
With 2000 Leibniz terms and 12 factorial terms:
pi 3141092, e 2718281, sum 5859373
iota 2 * 10^12 / 5859373 ~ 341381 (within 1% of 341304).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.iota_tau_precision_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L60-L67)
**def
Tau.BookII.Transcendentals.iota_tau_precision_check :Bool**


Higher precision check: the computed iota_tau matches the
known rational approximation 341304/10^6 to within 2%.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.self_consistency_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L73-L89)
**def
Tau.BookII.Transcendentals.self_consistency_check :Bool**


Self-consistency: pi + e = 2 / iota_tau.
In scaled arithmetic: (pi + e) * iota = 2 * scale.
Check: pi_scaled + e_scaled ~ 2 * scale^2 / iota_scaled.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.archimedean_bridge_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L95-L112)
**def
Tau.BookII.Transcendentals.archimedean_bridge_check :Bool**


[II.D34] Archimedean bridge: iota_tau mediates between
the Archimedean world (pi, e from limits) and the profinite
world (tau^3 from primorial inverse system).

The resolution at stage k is 1/P_k. The scale where
resolution crosses iota_tau happens between k=1 and k=2:
1/P_1 = 1/2 = 0.5 > iota_tau 0.341 > 1/P_2 = 1/6 0.167.

In scaled integer arithmetic: scale/P_k vs iota_tau_scaled.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.bridge_interpolation_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L114-L125)
**def
Tau.BookII.Transcendentals.bridge_interpolation_check :Bool**


Bridge characterization: iota_tau as the stage-1/stage-2
interpolation constant. The fact that iota_tau falls between
1/P_1 and 1/P_2 means it governs the first refinement step
where the primorial ladder becomes finer than the master constant.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.refinement_resolution_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L131-L141)
**def
Tau.BookII.Transcendentals.refinement_resolution_check
(stages : Denotation.TauIdx)
 :Bool**


[II.P07] Refinement resolution bound: at stage k, the
resolution 1/P_k decreases monotonically.
P_{k+1} > P_k for all k >= 0.
Equations
- Tau.BookII.Transcendentals.refinement_resolution_check stages = Tau.BookII.Transcendentals.refinement_resolution_check.go stages 1 (stages + 1)
Instances For

---

### `Tau.BookII.Transcendentals.refinement_resolution_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L137-L140)@[irreducible]

**def
Tau.BookII.Transcendentals.refinement_resolution_check.go
(stages : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.resolution_halving_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L143-L154)
**def
Tau.BookII.Transcendentals.resolution_halving_check
(stages : Denotation.TauIdx)
 :Bool**


Resolution ratio: P_{k+1}/P_k = p_{k+1} >= 2.
Each refinement step at least halves the resolution.
Equations
- Tau.BookII.Transcendentals.resolution_halving_check stages = Tau.BookII.Transcendentals.resolution_halving_check.go stages 1 (stages + 1)
Instances For

---

### `Tau.BookII.Transcendentals.resolution_halving_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L148-L153)@[irreducible]

**def
Tau.BookII.Transcendentals.resolution_halving_check.go
(stages : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.full_confirmation_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L160-L168)
**def
Tau.BookII.Transcendentals.full_confirmation_check :Bool**


Full master constant confirmation: all pieces fit together.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Transcendentals.iota_confirmed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L202-L202)
**theorem
Tau.BookII.Transcendentals.iota_confirmed :iota_tau_confirmed_check = true**


---

### `Tau.BookII.Transcendentals.iota_precision`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L203-L203)
**theorem
Tau.BookII.Transcendentals.iota_precision :iota_tau_precision_check = true**


---

### `Tau.BookII.Transcendentals.self_consist`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L204-L204)
**theorem
Tau.BookII.Transcendentals.self_consist :self_consistency_check = true**


---

### `Tau.BookII.Transcendentals.arch_bridge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L205-L205)
**theorem
Tau.BookII.Transcendentals.arch_bridge :archimedean_bridge_check = true**


---

### `Tau.BookII.Transcendentals.bridge_interp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L206-L206)
**theorem
Tau.BookII.Transcendentals.bridge_interp :bridge_interpolation_check = true**


---

### `Tau.BookII.Transcendentals.refine_res_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L207-L207)
**theorem
Tau.BookII.Transcendentals.refine_res_5 :refinement_resolution_check 5 = true**


---

### `Tau.BookII.Transcendentals.res_halving_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L208-L208)
**theorem
Tau.BookII.Transcendentals.res_halving_5 :resolution_halving_check 5 = true**


---

### `Tau.BookII.Transcendentals.full_confirm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Transcendentals/IotaTauConfirmed.lean#L209-L209)
**theorem
Tau.BookII.Transcendentals.full_confirm :full_confirmation_check = true**
