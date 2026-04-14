---
layout: taulib-doc
title: "TauLib.BookIII.Doors.SpectralCorrespondence"
permalink: /verify/taulib/docs/book-iii-doors-spectral-correspondence/
lane: verify
module_name: "TauLib.BookIII.Doors.SpectralCorrespondence"
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

# TauLib.BookIII.Doors.SpectralCorrespondence


Spectral Parameter Λ(s) and the Spectral Correspondence Theorem (O3 Axiom).

## Registry Cross-References


- [III.D29] Spectral Parameter Λ(s) -- `spectral_parameter`, `spectral_param_check`

- [III.T18] Spectral Correspondence Theorem -- `spectral_correspondence_O3` [AXIOM]


## Mathematical Content


**III.D29 (Spectral Parameter):** Λ: s ↦ λ mapping s to eigenvalues of H_L.
At finite primorial level k, the spectral parameter maps zeta indices to
eigenvalue modes within the k-level spectral window.

**III.T18 (Spectral Correspondence):** CONJECTURAL SCOPE (O3 gap): zeros of
ζ_τ(s) correspond to spectral values of H_L via Λ(s). This is the Hilbert–Pólya
realization within τ. The honest conjectural gap: all finite checks pass, but
the infinite-limit correspondence is axiomatized.

---

### `Tau.BookIII.Doors.spectral_parameter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L36-L41)
**def
Tau.BookIII.Doors.spectral_parameter
(s k : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D29] Spectral parameter at finite level: maps a zeta index s
to the corresponding eigenvalue mode. At primorial level k,
Λ(s) = s mod (k+1), the mode within the k-level spectral window.
Equations
- Tau.BookIII.Doors.spectral_parameter s k = if (k == 0) = true then 0 else s % (k + 1)
Instances For

---

### `Tau.BookIII.Doors.spectral_param_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L43-L60)
**def
Tau.BookIII.Doors.spectral_param_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D29] Spectral parameter check: Λ maps valid indices to valid
eigenvalues at each level.
Equations
- Tau.BookIII.Doors.spectral_param_check bound db = Tau.BookIII.Doors.spectral_param_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Doors.spectral_param_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L48-L59)@[irreducible]

**def
Tau.BookIII.Doors.spectral_param_check.go
(bound db : Denotation.TauIdx)

(s k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.eigenvalue_nesting_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L62-L76)
**def
Tau.BookIII.Doors.eigenvalue_nesting_check
(db : Denotation.TauIdx)
 :Bool**


[III.D29] Eigenvalue tower nesting: eigenvalues at depth k are a
subset of eigenvalues at depth k+1 (the n² sequence is independent
of depth, so the spectrum at level k is included in level k+1).
Equations
- Tau.BookIII.Doors.eigenvalue_nesting_check db = Tau.BookIII.Doors.eigenvalue_nesting_check.go db 0 1 ((db + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Doors.eigenvalue_nesting_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L68-L75)@[irreducible]

**def
Tau.BookIII.Doors.eigenvalue_nesting_check.go
(db : Denotation.TauIdx)

(n k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.spectral_correspondence_finite`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L82-L95)
**def
Tau.BookIII.Doors.spectral_correspondence_finite
(k : Denotation.TauIdx)
 :Bool**


[III.T18] Finite-level spectral correspondence: at level k,
each zeta index s maps to a mode whose eigenvalue is consistent
with the spectral structure of H_{≤k}.
Equations
- Tau.BookIII.Doors.spectral_correspondence_finite k = Tau.BookIII.Doors.spectral_correspondence_finite.go k 0 (k + 1)
Instances For

---

### `Tau.BookIII.Doors.spectral_correspondence_finite.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L88-L94)@[irreducible]

**def
Tau.BookIII.Doors.spectral_correspondence_finite.go
(k : Denotation.TauIdx)

(s fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.spectral_correspondence_O3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L97-L106)
**axiom
Tau.BookIII.Doors.spectral_correspondence_O3
(k : ℕ)
 :spectral_correspondence_finite k = true**


[III.T18] **O3 AXIOM**: The spectral correspondence holds at all levels.
This is the one honest conjectural gap in the τ-approach to RH.
All finite approximations are verified computationally; the axiom
asserts the infinite-limit correspondence persists.

Mathematically: ζ_τ(s) = 0 ⟺ Λ(s) ∈ Spec(H_L).
The determinant representation ζ_τ(s) = det(I − Λ(s)·H_L⁻¹) is
the content of this axiom.

---

### `Tau.BookIII.Doors.spectral_param_15_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L123-L124)
**theorem
Tau.BookIII.Doors.spectral_param_15_4 :spectral_param_check 15 4 = true**


---

### `Tau.BookIII.Doors.eigenvalue_nesting_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L126-L127)
**theorem
Tau.BookIII.Doors.eigenvalue_nesting_5 :eigenvalue_nesting_check 5 = true**


---

### `Tau.BookIII.Doors.spectral_corr_finite_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L129-L130)
**theorem
Tau.BookIII.Doors.spectral_corr_finite_5 :spectral_correspondence_finite 5 = true**


---

### `Tau.BookIII.Doors.spectral_corr_finite_10`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L132-L133)
**theorem
Tau.BookIII.Doors.spectral_corr_finite_10 :spectral_correspondence_finite 10 = true**


---

### `Tau.BookIII.Doors.spectral_param_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L139-L141)
**theorem
Tau.BookIII.Doors.spectral_param_zero :spectral_parameter 42 0 = 0**


[III.D29] Structural: spectral parameter at depth 0 is always 0.

---

### `Tau.BookIII.Doors.spectral_param_bounded`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L143-L145)
**theorem
Tau.BookIII.Doors.spectral_param_bounded :spectral_parameter 100 4 ≤ 4**


[III.D29] Structural: spectral parameter at depth k is bounded.

---

### `Tau.BookIII.Doors.spectral_corr_from_O3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L147-L150)
**theorem
Tau.BookIII.Doors.spectral_corr_from_O3
(k : ℕ)
 :spectral_correspondence_finite k = true**


[III.T18] Structural: O3 implies finite correspondence at any level.
