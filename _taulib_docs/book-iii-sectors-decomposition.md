---
layout: taulib-doc
title: "TauLib.BookIII.Sectors.Decomposition"
permalink: /verify/taulib/docs/book-iii-sectors-decomposition/
lane: verify
module_name: "TauLib.BookIII.Sectors.Decomposition"
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

# TauLib.BookIII.Sectors.Decomposition


Sector Preservation Theorem, 4+1 Sector Decomposition, and ω-Coupling Sector.

## Registry Cross-References


- [III.T05] Sector Preservation Theorem -- `sector_preservation_check`

- [III.D13] 4+1 Sector Decomposition -- `Sector`, `sector_of`, `sector_decomposition_check`

- [III.D14] ω-Coupling Sector -- `omega_coupling_check`


## Mathematical Content


**III.T05 (Sector Preservation):** The boundary-to-interior functor Φ preserves
the bipolar decomposition: χ₊-characters map to B-sector holomorphic functions,
χ₋-characters map to C-sector, mixed characters map to the ω-coupling sector.

**III.D13 (4+1 Sector Decomposition):** Five generators yield four primitive
sectors (α→D, π→A, γ→B, η→C) plus one coupling sector (ω).

**III.D14 (ω-Coupling Sector):** The fifth generator ω mediates coupling
between B and C lobes simultaneously. The structural reason for 4+1, not 5.

---

### `Tau.BookIII.Sectors.Sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L38-L46)
**inductive
Tau.BookIII.Sectors.Sector :Type**


[III.D13] The five sectors induced by the ABCD decomposition.
Four primitive sectors (one per generator) plus one coupling sector.

- D : Sector
- A : Sector
- B : Sector
- C : Sector
- Omega : Sector
Instances For

---

### `Tau.BookIII.Sectors.instReprSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L46-L46)
**instance
Tau.BookIII.Sectors.instReprSector :Repr Sector**

Equations
- Tau.BookIII.Sectors.instReprSector = { reprPrec := Tau.BookIII.Sectors.instReprSector.repr }

---

### `Tau.BookIII.Sectors.instReprSector.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L46-L46)
**def
Tau.BookIII.Sectors.instReprSector.repr :Sector → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.instDecidableEqSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L46-L46)
**instance
Tau.BookIII.Sectors.instDecidableEqSector :DecidableEq Sector**

Equations
- Tau.BookIII.Sectors.instDecidableEqSector x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIII.Sectors.instBEqSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L46-L46)
**instance
Tau.BookIII.Sectors.instBEqSector :BEq Sector**

Equations
- Tau.BookIII.Sectors.instBEqSector = { beq := Tau.BookIII.Sectors.instBEqSector.beq }

---

### `Tau.BookIII.Sectors.instBEqSector.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L46-L46)
**def
Tau.BookIII.Sectors.instBEqSector.beq :Sector → Sector → Bool**

Equations
- Tau.BookIII.Sectors.instBEqSector.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIII.Sectors.instInhabitedSector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L46-L46)
**instance
Tau.BookIII.Sectors.instInhabitedSector :Inhabited Sector**

Equations
- Tau.BookIII.Sectors.instInhabitedSector = { default := Tau.BookIII.Sectors.instInhabitedSector.default }

---

### `Tau.BookIII.Sectors.instInhabitedSector.default`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L46-L46)
**def
Tau.BookIII.Sectors.instInhabitedSector.default :Sector**

Equations
- Tau.BookIII.Sectors.instInhabitedSector.default = Tau.BookIII.Sectors.Sector.D
Instances For

---

### `Tau.BookIII.Sectors.sector_of`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L48-L63)
**def
Tau.BookIII.Sectors.sector_of
(χ : BoundaryCharacter)
 :Sector**


[III.D13] Sector assignment: classify a boundary character into its sector.
Based on the dominance pattern of the (m, n) indices:


- D: m = 0, n = 0 (trivial = radial)

- A: |m| = |n|, both nonzero (balanced = weak)

- B: |m| > |n| and n = 0 (pure B-lobe = electromagnetic)

- C: |n| > |m| and m = 0 (pure C-lobe = strong)

- Omega: both nonzero and |m| ≠ |n| (mixed coupling)

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.Sector.toNat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L65-L71)
**def
Tau.BookIII.Sectors.Sector.toNat :Sector → ℕ**


Numeric index of a sector (for ordering).
Equations
- Tau.BookIII.Sectors.Sector.D.toNat = 0
- Tau.BookIII.Sectors.Sector.A.toNat = 1
- Tau.BookIII.Sectors.Sector.B.toNat = 2
- Tau.BookIII.Sectors.Sector.C.toNat = 3
- Tau.BookIII.Sectors.Sector.Omega.toNat = 4
Instances For

---

### `Tau.BookIII.Sectors.sector_decomposition_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L73-L92)
**def
Tau.BookIII.Sectors.sector_decomposition_check
(bound : Denotation.TauIdx)
 :Bool**


[III.D13] Sector decomposition check: verify that the 5 sectors
are exhaustive over characters in range. Uses 5-bit accumulator.
Equations
- Tau.BookIII.Sectors.sector_decomposition_check bound = Tau.BookIII.Sectors.sector_decomposition_check.go bound 0 0 0 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookIII.Sectors.sector_decomposition_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L79-L91)@[irreducible]

**def
Tau.BookIII.Sectors.sector_decomposition_check.go
(bound : Denotation.TauIdx)

(m n seen fuel : ℕ)
 :Bool**


Accumulate which sectors are seen. Bits: D=1, A=2, B=4, C=8, Omega=16.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.omega_coupling_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L98-L116)
**def
Tau.BookIII.Sectors.omega_coupling_check
(bound : Denotation.TauIdx)
 :Bool**


[III.D14] ω-Coupling sector check: verify that ω-classified characters
have both m ≠ 0 and n ≠ 0 (dual-lobe active) and |m| ≠ |n|.
The ω-sector mediates coupling: it is the unique sector with
both lobes active simultaneously.
Equations
- Tau.BookIII.Sectors.omega_coupling_check bound = Tau.BookIII.Sectors.omega_coupling_check.go bound 0 0 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookIII.Sectors.omega_coupling_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L105-L115)@[irreducible]

**def
Tau.BookIII.Sectors.omega_coupling_check.go
(bound : Denotation.TauIdx)

(m n fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

**Scope limitation (E3 collapse):** At finite primorial level, the E3
predicate degenerates to E0 because `reduce` is idempotent. This check
is vacuous but correctly models the mathematical structure. The E3 layer
is correctly DEFINED but finite verification is vacuous.
See audit DASHBOARD.md §E3 Collapse.

---

### `Tau.BookIII.Sectors.sector_preservation_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L128-L154)
**def
Tau.BookIII.Sectors.sector_preservation_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T05] Sector preservation check: verify that the BTI functor Φ
preserves reduce-compatibility for each sector.
For each character, the interior extension is reduce-stable:
reduce(Φ(χ)(x, k), k) = Φ(χ)(x, k).
Equations
- Tau.BookIII.Sectors.sector_preservation_check bound db = Tau.BookIII.Sectors.sector_preservation_check.go bound db 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Sectors.sector_preservation_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L135-L153)@[irreducible]

**def
Tau.BookIII.Sectors.sector_preservation_check.go
(bound db : Denotation.TauIdx)

(m n k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.sector_decomp_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L182-L183)
**theorem
Tau.BookIII.Sectors.sector_decomp_5 :sector_decomposition_check 5 = true**


---

### `Tau.BookIII.Sectors.omega_coupling_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L186-L187)
**theorem
Tau.BookIII.Sectors.omega_coupling_5 :omega_coupling_check 5 = true**


---

### `Tau.BookIII.Sectors.sector_preservation_5_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L190-L191)
**theorem
Tau.BookIII.Sectors.sector_preservation_5_3 :sector_preservation_check 5 3 = true**


---

### `Tau.BookIII.Sectors.zero_in_D`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L197-L198)
**theorem
Tau.BookIII.Sectors.zero_in_D :sector_of BoundaryCharacter.zero = Sector.D**


[III.D13] Trivial character is in D-sector.

---

### `Tau.BookIII.Sectors.pure_m_in_B`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L200-L201)
**theorem
Tau.BookIII.Sectors.pure_m_in_B :sector_of { m_index := 2, n_index := 0 } = Sector.B**


[III.D13] Pure m-character is in B-sector.

---

### `Tau.BookIII.Sectors.pure_n_in_C`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L203-L204)
**theorem
Tau.BookIII.Sectors.pure_n_in_C :sector_of { m_index := 0, n_index := 2 } = Sector.C**


[III.D13] Pure n-character is in C-sector.

---

### `Tau.BookIII.Sectors.equal_mag_in_A`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L206-L207)
**theorem
Tau.BookIII.Sectors.equal_mag_in_A :sector_of { m_index := 3, n_index := 3 } = Sector.A**


[III.D13] Equal-magnitude character is in A-sector.

---

### `Tau.BookIII.Sectors.mixed_in_Omega`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L209-L210)
**theorem
Tau.BookIII.Sectors.mixed_in_Omega :sector_of { m_index := 2, n_index := 1 } = Sector.Omega**


[III.D13] Mixed unequal character is in Omega-sector.

---

### `Tau.BookIII.Sectors.sector_exhaustive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/Decomposition.lean#L212-L222)
**theorem
Tau.BookIII.Sectors.sector_exhaustive
(χ : BoundaryCharacter)
 :sector_of χ = Sector.D ∨ sector_of χ = Sector.A ∨ sector_of χ = Sector.B ∨ sector_of χ = Sector.C ∨ sector_of χ = Sector.Omega**


[III.D13] The five sectors partition the character space:
every character belongs to exactly one sector.
