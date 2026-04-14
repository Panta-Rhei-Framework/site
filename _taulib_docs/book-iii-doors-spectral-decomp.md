---
layout: taulib-doc
title: "TauLib.BookIII.Doors.SpectralDecomp"
permalink: /verify/taulib/docs/book-iii-doors-spectral-decomp/
lane: verify
module_name: "TauLib.BookIII.Doors.SpectralDecomp"
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

# TauLib.BookIII.Doors.SpectralDecomp


Spectral decomposition theory for the lemniscate operator H_L.

## Registry Cross-References


- [III.D80] Spectral Projector — `spectral_projector`, `projector_check`

- [III.D81] Spectral Measure — `spectral_measure`, `measure_total_check`

- [III.T56] Parseval Identity — `parseval_check`

- [III.P48] Spectral Resolution — `spectral_resolution_check`


## Mathematical Content


**III.D80 (Spectral Projector):** The projector P_n onto the n-th eigenspace
of H_L. For the lemniscate with eigenvalues λ_n = n², P_n projects onto
the mode with frequency n. At finite stage k, P_n is a rank-1 operator
on the M_k-dimensional space.

**III.D81 (Spectral Measure):** The spectral measure μ_spec assigns weight
1/N to each eigenvalue λ_n for n = 0, ..., N-1 (uniform on modes).
The total measure is 1. This is the counting measure on the spectrum.

**III.T56 (Parseval Identity):** For f ∈ L²(L), ‖f‖² = Σ_n |⟨f, e_n⟩|².
At finite stage, this is the Pythagorean theorem for orthogonal decomposition.

**III.P48 (Spectral Resolution):** H_L = Σ_n λ_n P_n. The operator is
recovered from its eigenvalues and projectors. Verified at finite stages.

---

### `Tau.BookIII.Doors.spectral_projector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L46-L60)
**def
Tau.BookIII.Doors.spectral_projector
(n : ℕ)

(f : ℕ → ℤ)

(N x : ℕ)
 :ℤ**


[III.D80] Spectral projector: P_n(f) = ⟨f, e_n⟩ · e_n.
For the discrete model with N points, e_n(x) = exp(2πinx/N).
We use the real part: cos(2πnx/N), approximated by the indicator
of the n-th frequency bin.

Simplified: at stage k with M_k points, the n-th mode projector
extracts the n-th Fourier coefficient. For computational verification,
we use the orthogonal basis of indicator functions.
Equations
- Tau.BookIII.Doors.spectral_projector n f N x = if (N == 0) = true then 0
 else have coeff := if n < N then f n else 0;
 if (x == n) = true then coeff else 0
Instances For

---

### `Tau.BookIII.Doors.projector_idempotent_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L62-L82)
**def
Tau.BookIII.Doors.projector_idempotent_check
(N : ℕ)
 :Bool**


[III.D80] Check projector is idempotent: P_n² = P_n.
Equations
- Tau.BookIII.Doors.projector_idempotent_check N = Tau.BookIII.Doors.projector_idempotent_check.go_n 0 N N
Instances For

---

### `Tau.BookIII.Doors.projector_idempotent_check.go_n`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L66-L73)@[irreducible]

**def
Tau.BookIII.Doors.projector_idempotent_check.go_n
(n bound fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.projector_idempotent_check.go_x`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L75-L81)@[irreducible]

**def
Tau.BookIII.Doors.projector_idempotent_check.go_x
(n x bound fuel : ℕ)

(pf f : ℕ → ℤ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.projector_orthogonal_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L84-L108)
**def
Tau.BookIII.Doors.projector_orthogonal_check
(N : ℕ)
 :Bool**


[III.D80] Check projectors are orthogonal: P_n · P_m = 0 for n ≠ m.
Equations
- Tau.BookIII.Doors.projector_orthogonal_check N = Tau.BookIII.Doors.projector_orthogonal_check.go_n 0 N N
Instances For

---

### `Tau.BookIII.Doors.projector_orthogonal_check.go_n`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L88-L91)@[irreducible]

**def
Tau.BookIII.Doors.projector_orthogonal_check.go_n
(n bound fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.projector_orthogonal_check.go_m`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L93-L102)@[irreducible]

**def
Tau.BookIII.Doors.projector_orthogonal_check.go_m
(n m bound fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.projector_orthogonal_check.go_x`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L104-L107)@[irreducible]

**def
Tau.BookIII.Doors.projector_orthogonal_check.go_x
(x bound fuel : ℕ)

(result : ℕ → ℤ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.projector_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L110-L112)
**def
Tau.BookIII.Doors.projector_check
(N : ℕ)
 :Bool**


[III.D80] Full projector check: idempotent + orthogonal.
Equations
- Tau.BookIII.Doors.projector_check N = (Tau.BookIII.Doors.projector_idempotent_check N && Tau.BookIII.Doors.projector_orthogonal_check N)
Instances For

---

### `Tau.BookIII.Doors.spectral_measure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L118-L122)
**def
Tau.BookIII.Doors.spectral_measure
(N n : ℕ)
 :Bool**


[III.D81] Spectral measure: weight of eigenvalue λ_n = n² is 1/N.
Total measure = N · (1/N) = 1.
Equations
- Tau.BookIII.Doors.spectral_measure N n = decide (n < N)
Instances For

---

### `Tau.BookIII.Doors.measure_total_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L124-L132)
**def
Tau.BookIII.Doors.measure_total_check
(N : ℕ)
 :Bool**


[III.D81] Check total spectral measure = 1 (all N modes counted).
Equations
- Tau.BookIII.Doors.measure_total_check N = (Tau.BookIII.Doors.measure_total_check.go 0 N 0 == N)
Instances For

---

### `Tau.BookIII.Doors.measure_total_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L129-L131)@[irreducible]

**def
Tau.BookIII.Doors.measure_total_check.go
(n bound acc : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.parseval_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L138-L165)
**def
Tau.BookIII.Doors.parseval_check
(N : ℕ)
 :Bool**


[III.T56] Parseval identity: ‖f‖² = Σ_n |c_n|² where c_n = f(n).
For the indicator basis, ‖f‖² = Σ_x f(x)² and Σ_n c_n² = Σ_n f(n)².
These are the same sum — Parseval is an identity.
Equations
- Tau.BookIII.Doors.parseval_check N = Tau.BookIII.Doors.parseval_check.go_f 0 N N
Instances For

---

### `Tau.BookIII.Doors.parseval_check.go_f`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L144-L154)@[irreducible]

**def
Tau.BookIII.Doors.parseval_check.go_f
(seed bound fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.parseval_check.sum_sq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L156-L158)@[irreducible]

**def
Tau.BookIII.Doors.parseval_check.sum_sq
(f : ℕ → ℤ)

(x bound : ℕ)

(acc : ℤ)
 :ℤ**

Equations
- Tau.BookIII.Doors.parseval_check.sum_sq f x bound acc = if x ≥ bound then acc else Tau.BookIII.Doors.parseval_check.sum_sq f (x + 1) bound (acc + f x * f x)
Instances For

---

### `Tau.BookIII.Doors.parseval_check.sum_coeff_sq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L160-L164)@[irreducible]

**def
Tau.BookIII.Doors.parseval_check.sum_coeff_sq
(f : ℕ → ℤ)

(n bound : ℕ)

(acc : ℤ)

(N : ℕ)
 :ℤ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.spectral_resolution_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L171-L201)
**def
Tau.BookIII.Doors.spectral_resolution_check
(N : ℕ)
 :Bool**


[III.P48] Spectral resolution: H_L = Σ_n λ_n P_n.
Check: (Σ_n λ_n P_n)(f)(x) = H_L(f)(x) for test functions.
For the discrete Laplacian, H_L(f)(x) = λ_x · f(x) in the eigenbasis.
In the indicator basis, this is just f(x) · x².
Equations
- Tau.BookIII.Doors.spectral_resolution_check N = Tau.BookIII.Doors.spectral_resolution_check.go_f 0 N N
Instances For

---

### `Tau.BookIII.Doors.spectral_resolution_check.go_f`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L178-L183)@[irreducible]

**def
Tau.BookIII.Doors.spectral_resolution_check.go_f
(seed bound fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.spectral_resolution_check.go_x`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L185-L193)@[irreducible]

**def
Tau.BookIII.Doors.spectral_resolution_check.go_x
(seed x bound fuel : ℕ)

(f : ℕ → ℤ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.spectral_resolution_check.sum_projectors`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L195-L200)@[irreducible]

**def
Tau.BookIII.Doors.spectral_resolution_check.sum_projectors
(f : ℕ → ℤ)

(x n bound : ℕ)

(acc : ℤ)

(N : ℕ)
 :ℤ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.projector_check_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L207-L209)
**theorem
Tau.BookIII.Doors.projector_check_2 :projector_check 2 = true**


[III.D80] Projectors correct at N = 2.

---

### `Tau.BookIII.Doors.projector_check_6`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L211-L213)
**theorem
Tau.BookIII.Doors.projector_check_6 :projector_check 6 = true**


[III.D80] Projectors correct at N = 6.

---

### `Tau.BookIII.Doors.measure_total_6`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L215-L217)
**theorem
Tau.BookIII.Doors.measure_total_6 :measure_total_check 6 = true**


[III.D81] Spectral measure total at N = 6.

---

### `Tau.BookIII.Doors.measure_total_30`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L219-L221)
**theorem
Tau.BookIII.Doors.measure_total_30 :measure_total_check 30 = true**


[III.D81] Spectral measure total at N = 30.

---

### `Tau.BookIII.Doors.parseval_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L223-L225)
**theorem
Tau.BookIII.Doors.parseval_2 :parseval_check 2 = true**


[III.T56] Parseval identity at N = 2.

---

### `Tau.BookIII.Doors.parseval_6`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L227-L229)
**theorem
Tau.BookIII.Doors.parseval_6 :parseval_check 6 = true**


[III.T56] Parseval identity at N = 6.

---

### `Tau.BookIII.Doors.spectral_resolution_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L231-L233)
**theorem
Tau.BookIII.Doors.spectral_resolution_2 :spectral_resolution_check 2 = true**


[III.P48] Spectral resolution at N = 2.

---

### `Tau.BookIII.Doors.spectral_resolution_6`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralDecomp.lean#L235-L237)
**theorem
Tau.BookIII.Doors.spectral_resolution_6 :spectral_resolution_check 6 = true**


[III.P48] Spectral resolution at N = 6.
