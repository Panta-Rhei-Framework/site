---
layout: taulib-doc
title: "TauLib.BookII.Interior.BipolarDecomposition"
permalink: /verify/taulib/docs/book-ii-interior-bipolar-decomposition/
lane: verify
module_name: "TauLib.BookII.Interior.BipolarDecomposition"
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

# TauLib.BookII.Interior.BipolarDecomposition


Interior bipolar decomposition: every τ-admissible point inherits
sector assignment from the boundary idempotents e₊, e₋.

## Registry Cross-References


- [II.D08] Interior Bipolar Decomposition — `interior_bipolar`

- [II.P02] Sector Inheritance — `sector_orthogonal`, `sector_complete`


## Mathematical Content


For (D, A, B, C) ∈ τ³:
Ψ_int = s₊ + s₋ = e₊ · Ψ(B,A,D) + e₋ · Ψ(C,A,D)

Two independent channels:


- B-channel (e₊): carries γ-orbit data (exponent structure)

- C-channel (e₋): carries η-orbit data (tetration height)


Orthogonality: e₊ · e₋ = 0 → channels carry independent information.

Degeneration to boundary at ω-limit:


- B-dominant → e₊-lobe of ℒ

- C-dominant → e₋-lobe of ℒ

- Balanced → crossing point


---

### `Tau.BookII.Interior.interior_bipolar`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/BipolarDecomposition.lean#L42-L49)
**def
Tau.BookII.Interior.interior_bipolar
(p : TauAdmissiblePoint)
 :Polarity.SectorPair**


[II.D08] Interior bipolar decomposition.
Maps a τ-admissible point to a sector pair (s₊, s₋).
B-coordinate → e₊-sector, C-coordinate → e₋-sector.

At finite stages, this is the integer-level shadow of the
profinite decomposition Ψ_int = e₊ · Ψ(B) + e₋ · Ψ(C).
Equations
- Tau.BookII.Interior.interior_bipolar p = { b_sector := ↑p.b, c_sector := ↑p.c }
Instances For

---

### `Tau.BookII.Interior.s_plus`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/BipolarDecomposition.lean#L51-L52)
**def
Tau.BookII.Interior.s_plus
(p : TauAdmissiblePoint)
 :ℤ**


B-sector component: carries exponent (γ-orbit) data.
Equations
- Tau.BookII.Interior.s_plus p = ↑p.b
Instances For

---

### `Tau.BookII.Interior.s_minus`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/BipolarDecomposition.lean#L54-L55)
**def
Tau.BookII.Interior.s_minus
(p : TauAdmissiblePoint)
 :ℤ**


C-sector component: carries tetration height (η-orbit) data.
Equations
- Tau.BookII.Interior.s_minus p = ↑p.c
Instances For

---

### `Tau.BookII.Interior.interior_split_complex`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/BipolarDecomposition.lean#L57-L59)
**def
Tau.BookII.Interior.interior_split_complex
(p : TauAdmissiblePoint)
 :Polarity.SplitComplex**


Full split-complex interior image via sector → split-complex conversion.
Equations
- Tau.BookII.Interior.interior_split_complex p = Tau.Boundary.from_sectors (Tau.BookII.Interior.interior_bipolar p)
Instances For

---

### `Tau.BookII.Interior.sector_orthogonal`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/BipolarDecomposition.lean#L65-L74)
**theorem
Tau.BookII.Interior.sector_orthogonal
(p : TauAdmissiblePoint)
 :Polarity.e_plus_sector.mul { b_sector := 0, c_sector := s_minus p } = { b_sector := 0, c_sector := 0 }**


[II.P02, clause 2] Idempotent compatibility:
The B-sector projection of the interior bipolar decomposition
is annihilated by e₋, and vice versa.

In sector coordinates: e₊ · s₋ = 0 and e₋ · s₊ = 0.
This follows because e₊ = ⟨1,0⟩ projects out the C-component,
and e₋ = ⟨0,1⟩ projects out the B-component.

---

### `Tau.BookII.Interior.sector_orthogonal'`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/BipolarDecomposition.lean#L76-L78)
**theorem
Tau.BookII.Interior.sector_orthogonal'
(p : TauAdmissiblePoint)
 :Polarity.e_minus_sector.mul { b_sector := s_plus p, c_sector := 0 } = { b_sector := 0, c_sector := 0 }**


---

### `Tau.BookII.Interior.sector_complete`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/BipolarDecomposition.lean#L80-L89)
**theorem
Tau.BookII.Interior.sector_complete
(p : TauAdmissiblePoint)
 :(Polarity.e_plus_sector.mul (interior_bipolar p)).add (Polarity.e_minus_sector.mul (interior_bipolar p)) = interior_bipolar p**


[II.P02, clause 2] Completeness:
The interior bipolar decomposition recovers the full point data.
s₊ + s₋ (in appropriate sense) gives back (B, C).

---

### `Tau.BookII.Interior.sector_lobe`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/BipolarDecomposition.lean#L91-L94)
**def
Tau.BookII.Interior.sector_lobe
(p : TauAdmissiblePoint)
 :FiberDominance**


[II.P02, clause 3] Fiber dominance recovery:
Sector assignment determines which lobe of ℒ the point approaches.
Equations
- Tau.BookII.Interior.sector_lobe p = p.fiber_dominance
Instances For

---

### `Tau.BookII.Interior.char_plus`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/BipolarDecomposition.lean#L100-L103)
**def
Tau.BookII.Interior.char_plus
(p : TauAdmissiblePoint)
 :ℤ**


Characteristic coordinates: ξ = B + C, η' = B - C.
Split-complex holomorphic functions decompose as f(ξ,η') = g(ξ) + h(η').
B and C channels are the two characteristic directions.
Equations
- Tau.BookII.Interior.char_plus p = ↑p.b + ↑p.c
Instances For

---

### `Tau.BookII.Interior.char_minus`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/BipolarDecomposition.lean#L104-L104)
**def
Tau.BookII.Interior.char_minus
(p : TauAdmissiblePoint)
 :ℤ**

Equations
- Tau.BookII.Interior.char_minus p = ↑p.b - ↑p.c
Instances For

---

### `Tau.BookII.Interior.char_to_sectors`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Interior/BipolarDecomposition.lean#L106-L114)
**def
Tau.BookII.Interior.char_to_sectors
(p : TauAdmissiblePoint)
 :Polarity.SectorPair**


Characteristic coordinates recover sector coordinates:
b_sector = ξ = B + C (= re + im in split-complex)
c_sector = η' = B - C (= re - im in split-complex)

Note: this is the TRANSPOSE of the usual convention because
interior_bipolar maps B → b_sector directly. The characteristic
coordinate interpretation involves the full split-complex embedding.
Equations
- Tau.BookII.Interior.char_to_sectors p = { b_sector := Tau.BookII.Interior.char_plus p, c_sector := Tau.BookII.Interior.char_minus p }
Instances For
