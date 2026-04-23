---
layout: taulib-doc
title: "TauLib.BookIII.Doors.LemniscateOperator"
permalink: /verify/taulib/docs/book-iii-doors-lemniscate-operator/
lane: verify
module_name: "TauLib.BookIII.Doors.LemniscateOperator"
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

# TauLib.BookIII.Doors.LemniscateOperator


Lemniscate Operator H_L, Self-Adjointness, and Discrete Spectrum.

## Registry Cross-References


- [III.D28] Lemniscate Operator H_L -- `lemniscate_eigenvalue`, `kirchhoff_check`

- [III.T17] Self-Adjointness of H_L -- `self_adjoint_check`

- [III.P09] Discrete Spectrum of H_L -- `discrete_spectrum_check`


## Mathematical Content


**III.D28 (Lemniscate Operator):** The Laplacian H_L = −d²/dx² on L = S¹ ∨ S¹
with Kirchhoff boundary conditions at the crossing point. Standard self-adjoint
operator on a compact metric graph.

**III.T17 (Self-Adjointness):** H_L is self-adjoint on L²(L). All eigenvalues
are real. The K5 diagonal discipline is the structural mechanism: off-diagonal
coupling is forbidden at the crossing point.

**III.P09 (Discrete Spectrum):** Spectrum is discrete: {λ_n} with λ_n → ∞.
Compact resolvent from L being a compact metric graph.

---

### `Tau.BookIII.Doors.lemniscate_eigenvalue`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L39-L43)
**def
Tau.BookIII.Doors.lemniscate_eigenvalue
(n : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D28] Lemniscate operator eigenvalue at mode n.
For L = S¹ ∨ S¹ with unit circumference lobes:
λ_n = n² (the key spectral property of −d²/dx²).
The τ-native finite model uses n² directly.
Equations
- Tau.BookIII.Doors.lemniscate_eigenvalue n = n * n
Instances For

---

### `Tau.BookIII.Doors.kirchhoff_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L45-L58)
**def
Tau.BookIII.Doors.kirchhoff_check
(bound : Denotation.TauIdx)
 :Bool**


[III.D28] Kirchhoff condition: at the crossing point, eigenvalues
of the full lemniscate operator equal the expected n² values.
Equations
- Tau.BookIII.Doors.kirchhoff_check bound = Tau.BookIII.Doors.kirchhoff_check.go bound 0 (bound + 1)
Instances For

---

### `Tau.BookIII.Doors.kirchhoff_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L50-L57)@[irreducible]

**def
Tau.BookIII.Doors.kirchhoff_check.go
(bound : Denotation.TauIdx)

(n fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.lobe_agreement_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L60-L75)
**def
Tau.BookIII.Doors.lobe_agreement_check
(bound : Denotation.TauIdx)
 :Bool**


[III.D28] B-lobe and C-lobe eigenvalue agreement: the two lobes
of L produce the same eigenvalue spectrum (K5 diagonal discipline).
Equations
- Tau.BookIII.Doors.lobe_agreement_check bound = Tau.BookIII.Doors.lobe_agreement_check.go bound 0 (bound + 1)
Instances For

---

### `Tau.BookIII.Doors.lobe_agreement_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L65-L74)@[irreducible]

**def
Tau.BookIII.Doors.lobe_agreement_check.go
(bound : Denotation.TauIdx)

(n fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.self_adjoint_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L81-L95)
**def
Tau.BookIII.Doors.self_adjoint_check
(bound : Denotation.TauIdx)
 :Bool**


[III.T17] Self-adjointness check: eigenvalues are real and strictly
ordered. In the finite τ-model, all eigenvalues are natural numbers.
Equations
- Tau.BookIII.Doors.self_adjoint_check bound = Tau.BookIII.Doors.self_adjoint_check.go bound 0 (bound + 1)
Instances For

---

### `Tau.BookIII.Doors.self_adjoint_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L86-L94)@[irreducible]

**def
Tau.BookIII.Doors.self_adjoint_check.go
(bound : Denotation.TauIdx)

(n fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.k5_diagonal_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L97-L113)
**def
Tau.BookIII.Doors.k5_diagonal_check
(bound : Denotation.TauIdx)
 :Bool**


[III.T17] K5 diagonal discipline: the off-diagonal coupling at the
crossing point vanishes. B-lobe and C-lobe eigenvalues are independent
(no imaginary mixing terms).
Equations
- Tau.BookIII.Doors.k5_diagonal_check bound = Tau.BookIII.Doors.k5_diagonal_check.go bound 1 (bound + 1)
Instances For

---

### `Tau.BookIII.Doors.k5_diagonal_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L103-L112)@[irreducible]

**def
Tau.BookIII.Doors.k5_diagonal_check.go
(bound : Denotation.TauIdx)

(n fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.discrete_spectrum_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L119-L131)
**def
Tau.BookIII.Doors.discrete_spectrum_check
(bound : Denotation.TauIdx)
 :Bool**


[III.P09] Discrete spectrum: eigenvalues form a strictly increasing
unbounded sequence.
Equations
- Tau.BookIII.Doors.discrete_spectrum_check bound = Tau.BookIII.Doors.discrete_spectrum_check.go bound 1 bound
Instances For

---

### `Tau.BookIII.Doors.discrete_spectrum_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L124-L130)@[irreducible]

**def
Tau.BookIII.Doors.discrete_spectrum_check.go
(bound : Denotation.TauIdx)

(n fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.spectral_gap_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L133-L135)
**def
Tau.BookIII.Doors.spectral_gap_check :Bool**


[III.P09] Spectral gap: λ₁ > 0 (first nonzero eigenvalue).
Equations
- Tau.BookIII.Doors.spectral_gap_check = decide (Tau.BookIII.Doors.lemniscate_eigenvalue 1 > Tau.BookIII.Doors.lemniscate_eigenvalue 0)
Instances For

---

### `Tau.BookIII.Doors.weyl_law_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L137-L149)
**def
Tau.BookIII.Doors.weyl_law_check
(bound : Denotation.TauIdx)
 :Bool**


[III.P09] Weyl law compatibility: N(λ_n) grows as √λ ∼ n.
Equations
- Tau.BookIII.Doors.weyl_law_check bound = Tau.BookIII.Doors.weyl_law_check.go bound 1 (bound + 1)
Instances For

---

### `Tau.BookIII.Doors.weyl_law_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L141-L148)@[irreducible]

**def
Tau.BookIII.Doors.weyl_law_check.go
(bound : Denotation.TauIdx)

(n fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.kirchhoff_20`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L170-L171)
**theorem
Tau.BookIII.Doors.kirchhoff_20 :kirchhoff_check 20 = true**


---

### `Tau.BookIII.Doors.lobe_agreement_20`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L173-L174)
**theorem
Tau.BookIII.Doors.lobe_agreement_20 :lobe_agreement_check 20 = true**


---

### `Tau.BookIII.Doors.self_adjoint_20`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L176-L177)
**theorem
Tau.BookIII.Doors.self_adjoint_20 :self_adjoint_check 20 = true**


---

### `Tau.BookIII.Doors.k5_diagonal_20`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L179-L180)
**theorem
Tau.BookIII.Doors.k5_diagonal_20 :k5_diagonal_check 20 = true**


---

### `Tau.BookIII.Doors.discrete_spectrum_20`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L182-L183)
**theorem
Tau.BookIII.Doors.discrete_spectrum_20 :discrete_spectrum_check 20 = true**


---

### `Tau.BookIII.Doors.spectral_gap`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L185-L186)
**theorem
Tau.BookIII.Doors.spectral_gap :spectral_gap_check = true**


---

### `Tau.BookIII.Doors.weyl_law_20`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L188-L189)
**theorem
Tau.BookIII.Doors.weyl_law_20 :weyl_law_check 20 = true**


---

### `Tau.BookIII.Doors.eigenvalue_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L195-L196)
**theorem
Tau.BookIII.Doors.eigenvalue_zero :lemniscate_eigenvalue 0 = 0**


[III.D28] Structural: ground state eigenvalue is 0.

---

### `Tau.BookIII.Doors.eigenvalue_formula`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L198-L200)
**theorem
Tau.BookIII.Doors.eigenvalue_formula
(n : ℕ)
 :lemniscate_eigenvalue n = n * n**


[III.D28] Structural: eigenvalue at mode n equals n².

---

### `Tau.BookIII.Doors.eigenvalue_nonneg`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L202-L204)
**theorem
Tau.BookIII.Doors.eigenvalue_nonneg
(n : ℕ)
 :lemniscate_eigenvalue n ≥ 0**


[III.T17] Structural: all eigenvalues are non-negative.

---

### `Tau.BookIII.Doors.spectral_gap_value`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/LemniscateOperator.lean#L206-L208)
**theorem
Tau.BookIII.Doors.spectral_gap_value :lemniscate_eigenvalue 1 = 1**


[III.P09] Structural: spectral gap value is 1.
