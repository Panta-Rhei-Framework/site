---
layout: taulib-doc
title: "TauLib.BookIII.Doors.MutualDetermination"
permalink: /verify/taulib/docs/book-iii-doors-mutual-determination/
lane: verify
module_name: "TauLib.BookIII.Doors.MutualDetermination"
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

# TauLib.BookIII.Doors.MutualDetermination


Mutual Determination Schema: B ↔ I ↔ S at spectral level.

## Registry Cross-References


- [III.D25] Mutual Determination Schema -- `MDDescription`, `mutual_det_check`


## Mathematical Content


**III.D25 (Mutual Determination Schema):** The Master Schema formalized:
B (boundary) ↔ I (interior) ↔ S (spectral invariants). Three equivalences:
boundary→interior (Global Hartogs), interior→spectral (spectral decomposition),
closure B↔S (dual perspectives). Uniform template for all millennium problems.

---

### `Tau.BookIII.Doors.MDDescription`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/MutualDetermination.lean#L31-L38)
**inductive
Tau.BookIII.Doors.MDDescription :Type**


[III.D25] The three descriptions in the Mutual Determination Schema.
B = Boundary data (CRT residues), I = Interior data (reconstruction),
S = Spectral data (bipolar B/C/X decomposition).

- Boundary : MDDescription
- Interior : MDDescription
- Spectral : MDDescription
Instances For

---

### `Tau.BookIII.Doors.instReprMDDescription.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/MutualDetermination.lean#L38-L38)
**def
Tau.BookIII.Doors.instReprMDDescription.repr :MDDescription → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.instReprMDDescription`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/MutualDetermination.lean#L38-L38)
**instance
Tau.BookIII.Doors.instReprMDDescription :Repr MDDescription**

Equations
- Tau.BookIII.Doors.instReprMDDescription = { reprPrec := Tau.BookIII.Doors.instReprMDDescription.repr }

---

### `Tau.BookIII.Doors.instDecidableEqMDDescription`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/MutualDetermination.lean#L38-L38)
**instance
Tau.BookIII.Doors.instDecidableEqMDDescription :DecidableEq MDDescription**

Equations
- Tau.BookIII.Doors.instDecidableEqMDDescription x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIII.Doors.instBEqMDDescription.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/MutualDetermination.lean#L38-L38)
**def
Tau.BookIII.Doors.instBEqMDDescription.beq :MDDescription → MDDescription → Bool**

Equations
- Tau.BookIII.Doors.instBEqMDDescription.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIII.Doors.instBEqMDDescription`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/MutualDetermination.lean#L38-L38)
**instance
Tau.BookIII.Doors.instBEqMDDescription :BEq MDDescription**

Equations
- Tau.BookIII.Doors.instBEqMDDescription = { beq := Tau.BookIII.Doors.instBEqMDDescription.beq }

---

### `Tau.BookIII.Doors.boundary_to_interior_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/MutualDetermination.lean#L40-L56)
**def
Tau.BookIII.Doors.boundary_to_interior_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D25] Boundary → Interior: reconstruction from CRT residues
agrees with direct computation.
Equations
- Tau.BookIII.Doors.boundary_to_interior_check bound db = Tau.BookIII.Doors.boundary_to_interior_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Doors.boundary_to_interior_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/MutualDetermination.lean#L45-L55)@[irreducible]

**def
Tau.BookIII.Doors.boundary_to_interior_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.interior_to_spectral_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/MutualDetermination.lean#L58-L75)
**def
Tau.BookIII.Doors.interior_to_spectral_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D25] Interior → Spectral: the bipolar decomposition of the
reconstructed value is exact (sums back).
Equations
- Tau.BookIII.Doors.interior_to_spectral_check bound db = Tau.BookIII.Doors.interior_to_spectral_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Doors.interior_to_spectral_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/MutualDetermination.lean#L63-L74)@[irreducible]

**def
Tau.BookIII.Doors.interior_to_spectral_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.spectral_to_boundary_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/MutualDetermination.lean#L77-L100)
**def
Tau.BookIII.Doors.spectral_to_boundary_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D25] Spectral → Boundary: the spectral decomposition uniquely
determines the boundary data (injectivity).
Equations
- Tau.BookIII.Doors.spectral_to_boundary_check bound db = Tau.BookIII.Doors.spectral_to_boundary_check.go bound db 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Doors.spectral_to_boundary_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/MutualDetermination.lean#L82-L99)@[irreducible]

**def
Tau.BookIII.Doors.spectral_to_boundary_check.go
(bound db : Denotation.TauIdx)

(x y k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.mutual_det_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/MutualDetermination.lean#L102-L106)
**def
Tau.BookIII.Doors.mutual_det_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D25] Full mutual determination: all three descriptions equivalent.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.b_to_i_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/MutualDetermination.lean#L121-L122)
**theorem
Tau.BookIII.Doors.b_to_i_15_4 :boundary_to_interior_check 15 4 = true**


---

### `Tau.BookIII.Doors.i_to_s_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/MutualDetermination.lean#L124-L125)
**theorem
Tau.BookIII.Doors.i_to_s_15_4 :interior_to_spectral_check 15 4 = true**


---

### `Tau.BookIII.Doors.s_to_b_10_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/MutualDetermination.lean#L127-L128)
**theorem
Tau.BookIII.Doors.s_to_b_10_3 :spectral_to_boundary_check 10 3 = true**


---

### `Tau.BookIII.Doors.mutual_det_10_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/MutualDetermination.lean#L130-L131)
**theorem
Tau.BookIII.Doors.mutual_det_10_3 :mutual_det_check 10 3 = true**


---

### `Tau.BookIII.Doors.b_to_i_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/MutualDetermination.lean#L137-L139)
**theorem
Tau.BookIII.Doors.b_to_i_zero :Polarity.crt_reconstruct (Polarity.crt_decompose 0 3) 3 = 0**


[III.D25] Structural: boundary→interior is exact for 0.

---

### `Tau.BookIII.Doors.md_cycle_42_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Doors/MutualDetermination.lean#L141-L147)
**theorem
Tau.BookIII.Doors.md_cycle_42_3 :have residues := Polarity.crt_decompose 42 3;
have reconstructed := Polarity.crt_reconstruct residues 3;
have nf := Spectral.boundary_normal_form reconstructed 3;
(nf.b_part + nf.c_part + nf.x_part) % Polarity.primorial 3 = 42 % Polarity.primorial 3**


[III.D25] Structural: mutual determination cycle for 42 at depth 3.
