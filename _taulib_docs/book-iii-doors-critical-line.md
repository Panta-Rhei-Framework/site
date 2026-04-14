---
layout: taulib-doc
title: "TauLib.BookIII.Doors.CriticalLine"
permalink: /verify/taulib/docs/book-iii-doors-critical-line/
lane: verify
module_name: "TauLib.BookIII.Doors.CriticalLine"
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

# TauLib.BookIII.Doors.CriticalLine


Critical Line Theorem, K5 Off-Diagonal Exclusion, τ-Effective RH Statement,
and Primorial RH Verification Protocol.

## Registry Cross-References


- [III.T19] Critical Line Theorem -- `critical_line_check`

- [III.P10] K5 Off-Diagonal Exclusion -- `k5_exclusion_check`

- [III.D30] τ-Effective RH Statement -- `tau_effective_rh_check`

- [III.P11] Primorial RH Verification Protocol -- `rh_protocol_check`


## Mathematical Content


**III.T19 (Critical Line):** CONDITIONAL on O3: self-adjointness of H_L
forces all eigenvalues real, which via the spectral correspondence forces
all non-trivial zeros of ζ_τ to lie on Re(s) = ½.

**III.P10 (K5 Off-Diagonal Exclusion):** K5 forbids off-diagonal coupling
at the lemniscate crossing point. Off-critical-line zeros would require
imaginary spectral coupling, which K5 forbids.

**III.D30 (τ-Effective RH):** Computable predicate: for each primorial
depth k, the finite-cutoff operator has only real eigenvalues.

**III.P11 (Primorial RH Verification Protocol):** Six-step verification
protocol at each primorial level.

---

### `Tau.BookIII.Doors.critical_line_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/CriticalLine.lean#L44-L61)
**def
Tau.BookIII.Doors.critical_line_check
(k : Denotation.TauIdx)
 :Bool**


[III.T19] Critical line check at level k: all spectral modes have
real eigenvalues (= natural numbers) and the spectral correspondence
maps them consistently. Combines self-adjointness + O3.
Equations
- Tau.BookIII.Doors.critical_line_check k = Tau.BookIII.Doors.critical_line_check.go k 0 (k + 1)
Instances For

---

### `Tau.BookIII.Doors.critical_line_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/CriticalLine.lean#L50-L60)@[irreducible]

**def
Tau.BookIII.Doors.critical_line_check.go
(k : Denotation.TauIdx)

(n fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.critical_line_multi_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/CriticalLine.lean#L63-L72)
**def
Tau.BookIII.Doors.critical_line_multi_check
(db : Denotation.TauIdx)
 :Bool**


[III.T19] Critical line at multiple depths.
Equations
- Tau.BookIII.Doors.critical_line_multi_check db = Tau.BookIII.Doors.critical_line_multi_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Doors.critical_line_multi_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/CriticalLine.lean#L67-L71)@[irreducible]

**def
Tau.BookIII.Doors.critical_line_multi_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.k5_exclusion_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/CriticalLine.lean#L78-L97)
**def
Tau.BookIII.Doors.k5_exclusion_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.P10] K5 off-diagonal exclusion: at each primorial level k,
the B-lobe and C-lobe eigenvalues have zero off-diagonal coupling.
The crossing-point boundary conditions enforce real spectral flow.
Equations
- Tau.BookIII.Doors.k5_exclusion_check bound db = Tau.BookIII.Doors.k5_exclusion_check.go bound db 1 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Doors.k5_exclusion_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/CriticalLine.lean#L84-L96)@[irreducible]

**def
Tau.BookIII.Doors.k5_exclusion_check.go
(bound db : Denotation.TauIdx)

(n k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.tau_effective_rh_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/CriticalLine.lean#L103-L120)
**def
Tau.BookIII.Doors.tau_effective_rh_check
(db : Denotation.TauIdx)
 :Bool**


[III.D30] τ-Effective RH: for each primorial depth k, the finite-cutoff
operator H_{≤k} has only real eigenvalues, and the finite zeta
has the correct zero structure. A computable predicate.
Equations
- Tau.BookIII.Doors.tau_effective_rh_check db = Tau.BookIII.Doors.tau_effective_rh_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Doors.tau_effective_rh_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/CriticalLine.lean#L109-L119)@[irreducible]

**def
Tau.BookIII.Doors.tau_effective_rh_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.rh_protocol_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/CriticalLine.lean#L126-L149)
**def
Tau.BookIII.Doors.rh_protocol_check
(db : Denotation.TauIdx)
 :Bool**


[III.P11] Primorial RH verification protocol at depth k.
Six steps: (i) compute Spec(H_{≤k}), (ii) verify eigenvalues real,
(iii) verify zero locations, (iv) tower coherence, (v) CRT consistency,
(vi) record certificate. Returns true if all steps pass.
Equations
- Tau.BookIII.Doors.rh_protocol_check db = Tau.BookIII.Doors.rh_protocol_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Doors.rh_protocol_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/CriticalLine.lean#L133-L148)@[irreducible]

**def
Tau.BookIII.Doors.rh_protocol_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.critical_line_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/CriticalLine.lean#L166-L167)
**theorem
Tau.BookIII.Doors.critical_line_5 :critical_line_check 5 = true**


---

### `Tau.BookIII.Doors.critical_line_10`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/CriticalLine.lean#L169-L170)
**theorem
Tau.BookIII.Doors.critical_line_10 :critical_line_check 10 = true**


---

### `Tau.BookIII.Doors.critical_line_multi_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/CriticalLine.lean#L172-L173)
**theorem
Tau.BookIII.Doors.critical_line_multi_5 :critical_line_multi_check 5 = true**


---

### `Tau.BookIII.Doors.k5_exclusion_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/CriticalLine.lean#L175-L176)
**theorem
Tau.BookIII.Doors.k5_exclusion_10_3 :k5_exclusion_check 10 3 = true**


---

### `Tau.BookIII.Doors.tau_effective_rh_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/CriticalLine.lean#L178-L179)
**theorem
Tau.BookIII.Doors.tau_effective_rh_5 :tau_effective_rh_check 5 = true**


---

### `Tau.BookIII.Doors.rh_protocol_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/CriticalLine.lean#L181-L182)
**theorem
Tau.BookIII.Doors.rh_protocol_4 :rh_protocol_check 4 = true**


---

### `Tau.BookIII.Doors.critical_line_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/CriticalLine.lean#L188-L190)
**theorem
Tau.BookIII.Doors.critical_line_1 :critical_line_check 1 = true**


[III.T19] Structural: critical line at depth 1 (only prime 2).

---

### `Tau.BookIII.Doors.k5_eigenvalue_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/CriticalLine.lean#L192-L194)
**theorem
Tau.BookIII.Doors.k5_eigenvalue_1 :lemniscate_eigenvalue 1 = 1**


[III.P10] Structural: eigenvalue of first mode equals 1.

---

### `Tau.BookIII.Doors.tau_rh_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/CriticalLine.lean#L196-L198)
**theorem
Tau.BookIII.Doors.tau_rh_1 :tau_effective_rh_check 1 = true**


[III.D30] Structural: τ-effective RH at depth 1.
