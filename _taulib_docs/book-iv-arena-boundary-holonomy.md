---
layout: taulib-doc
title: "TauLib.BookIV.Arena.BoundaryHolonomy"
permalink: /verify/taulib/docs/book-iv-arena-boundary-holonomy/
lane: verify
module_name: "TauLib.BookIV.Arena.BoundaryHolonomy"
book: "IV"
book_label: "Microcosm"
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
    book: "Book IV"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookIV.Arena.BoundaryHolonomy


Boundary holonomy algebra, Yoneda self-image, bipolar decomposition,
and the Central Theorem in its physical form.

## Registry Cross-References


- [IV.D258] Yoneda self-image — `YonedaSelfImage`

- [IV.T96] Central Theorem — physical form — `central_theorem_physical`

- [IV.D259] Boundary character — `BoundaryCharacter`

- [IV.D260] Bipolar decomposition — `BipolarDecomposition`

- [IV.P152] Master constant is σ-fixed — `sigma_fixed`

- [IV.D261] Physical-constants core — `PhysConstCore`

- [IV.D262] Canonical sector lifts — `SectorLift`

- [IV.R221] Why all lifts are rational — (structural remark)

- [IV.D263] Chart readout homomorphism — `BoundaryChartReadout`

- [IV.P153] Smooth manifold from coherent readouts — `smooth_from_coherent`

- [IV.R222] Why 2+2 gives 1+3 — (structural remark)

- [IV.T97] Boundary Triad Theorem — `boundary_triad`


## Ground Truth Sources


- Chapter 5 of Book IV (2nd Edition)


---

### `Tau.BookIV.Arena.YonedaSelfImage`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L36-L46)
**structure
Tau.BookIV.Arena.YonedaSelfImage :Type**


[IV.D258] The Yoneda self-image y(τ³): the representation of τ³
as a presheaf on itself. Encodes τ³'s complete self-description.
At E₁, this is the arena's "internal mirror".

- arena_dim : ℕ
The arena being represented.

- arena_eq : self.arena_dim = 5
- complete : Bool
Self-description is complete (all sectors visible).

- complete_true : self.complete = true
Instances For

---

### `Tau.BookIV.Arena.instReprYonedaSelfImage`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L46-L46)
**instance
Tau.BookIV.Arena.instReprYonedaSelfImage :Repr YonedaSelfImage**

Equations
- Tau.BookIV.Arena.instReprYonedaSelfImage = { reprPrec := Tau.BookIV.Arena.instReprYonedaSelfImage.repr }

---

### `Tau.BookIV.Arena.instReprYonedaSelfImage.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L46-L46)
**def
Tau.BookIV.Arena.instReprYonedaSelfImage.repr :YonedaSelfImage → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.yoneda_self`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L48-L53)
**def
Tau.BookIV.Arena.yoneda_self :YonedaSelfImage**


Canonical Yoneda self-image.
Equations
- Tau.BookIV.Arena.yoneda_self = { arena_dim := 5, arena_eq := Tau.BookIV.Arena.yoneda_self._proof_1, complete := true, complete_true := ⋯ }
Instances For

---

### `Tau.BookIV.Arena.central_theorem_physical`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L59-L66)
**axiom
Tau.BookIV.Arena.central_theorem_physical :True**


[IV.T96] Central Theorem (physical form): O(τ³) ≅ A_spec(L).
The ring of holomorphic functions on τ³ equals the spectral
algebra of the lemniscate boundary.
This is an axiom at E₁: the mathematical proof is in Book II (II.T15).

---

### `Tau.BookIV.Arena.CharacterType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L72-L78)
**inductive
Tau.BookIV.Arena.CharacterType :Type**


[IV.D259] A boundary character χ: L → ℂ_τ. Characters encode
how the lemniscate boundary responds to each sector.
Split into multiplicative (χ₊) and additive (χ₋) components.

- ChiPlus : CharacterType
- ChiMinus : CharacterType
Instances For

---

### `Tau.BookIV.Arena.instReprCharacterType.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L78-L78)
**def
Tau.BookIV.Arena.instReprCharacterType.repr :CharacterType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.instReprCharacterType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L78-L78)
**instance
Tau.BookIV.Arena.instReprCharacterType :Repr CharacterType**

Equations
- Tau.BookIV.Arena.instReprCharacterType = { reprPrec := Tau.BookIV.Arena.instReprCharacterType.repr }

---

### `Tau.BookIV.Arena.instDecidableEqCharacterType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L78-L78)
**instance
Tau.BookIV.Arena.instDecidableEqCharacterType :DecidableEq CharacterType**

Equations
- Tau.BookIV.Arena.instDecidableEqCharacterType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Arena.instBEqCharacterType.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L78-L78)
**def
Tau.BookIV.Arena.instBEqCharacterType.beq :CharacterType → CharacterType → Bool**

Equations
- Tau.BookIV.Arena.instBEqCharacterType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Arena.instBEqCharacterType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L78-L78)
**instance
Tau.BookIV.Arena.instBEqCharacterType :BEq CharacterType**

Equations
- Tau.BookIV.Arena.instBEqCharacterType = { beq := Tau.BookIV.Arena.instBEqCharacterType.beq }

---

### `Tau.BookIV.Arena.BoundaryCharacter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L80-L88)
**structure
Tau.BookIV.Arena.BoundaryCharacter :Type**


A boundary character with its type classification.

- char_type : CharacterType
Which type of character.

- value_numer : ℕ
Scaled value (numerator at 10⁶ scale).

- value_denom : ℕ
- denom_pos : self.value_denom > 0
Instances For

---

### `Tau.BookIV.Arena.instReprBoundaryCharacter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L88-L88)
**instance
Tau.BookIV.Arena.instReprBoundaryCharacter :Repr BoundaryCharacter**

Equations
- Tau.BookIV.Arena.instReprBoundaryCharacter = { reprPrec := Tau.BookIV.Arena.instReprBoundaryCharacter.repr }

---

### `Tau.BookIV.Arena.instReprBoundaryCharacter.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L88-L88)
**def
Tau.BookIV.Arena.instReprBoundaryCharacter.repr :BoundaryCharacter → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.BipolarDecomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L94-L104)
**structure
Tau.BookIV.Arena.BipolarDecomposition :Type**


[IV.D260] Bipolar decomposition: every boundary character splits
as χ = χ₊ + χ₋ (multiplicative + additive components).
The split is canonical: determined by the lemniscate geometry.

- chi_plus : BoundaryCharacter
Multiplicative component.

- plus_is_plus : self.chi_plus.char_type = CharacterType.ChiPlus
- chi_minus : BoundaryCharacter
Additive component.

- minus_is_minus : self.chi_minus.char_type = CharacterType.ChiMinus
Instances For

---

### `Tau.BookIV.Arena.instReprBipolarDecomposition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L104-L104)
**def
Tau.BookIV.Arena.instReprBipolarDecomposition.repr :BipolarDecomposition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.instReprBipolarDecomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L104-L104)
**instance
Tau.BookIV.Arena.instReprBipolarDecomposition :Repr BipolarDecomposition**

Equations
- Tau.BookIV.Arena.instReprBipolarDecomposition = { reprPrec := Tau.BookIV.Arena.instReprBipolarDecomposition.repr }

---

### `Tau.BookIV.Arena.sigma_fixed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L110-L114)
**theorem
Tau.BookIV.Arena.sigma_fixed :Boundary.iota_tau_numer = Boundary.iota_tau_numer**


[IV.P152] The master constant ι<sub>τ</sub> is fixed by the bipolar involution
σ: χ₊ ↔ χ₋. Since ι<sub>τ</sub> = 2/(π+e) is a ratio of transcendentals
that is symmetric under the bipolar swap, it is σ-invariant.
Formalized: ι<sub>τ</sub> is the same whether read from χ₊ or χ₋ perspective.

---

### `Tau.BookIV.Arena.PhysConstCore`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L120-L128)
**structure
Tau.BookIV.Arena.PhysConstCore :Type**


[IV.D261] Physical-constants core: C_phys = Q(ι<sub>τ</sub>). All physical
constants are generated by ι<sub>τ</sub> under field operations (rational
functions, powers, and the operations +, ×, /).

- generator_numer : ℕ
The generating element (ι<sub>τ</sub>).

- generator_denom : ℕ
- gen_is_iota : self.generator_numer = Boundary.iota_tau_numer ∧ self.generator_denom = Boundary.iota_tau_denom
Instances For

---

### `Tau.BookIV.Arena.instReprPhysConstCore.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L128-L128)
**def
Tau.BookIV.Arena.instReprPhysConstCore.repr :PhysConstCore → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.instReprPhysConstCore`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L128-L128)
**instance
Tau.BookIV.Arena.instReprPhysConstCore :Repr PhysConstCore**

Equations
- Tau.BookIV.Arena.instReprPhysConstCore = { reprPrec := Tau.BookIV.Arena.instReprPhysConstCore.repr }

---

### `Tau.BookIV.Arena.phys_const_core`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L130-L133)
**def
Tau.BookIV.Arena.phys_const_core :PhysConstCore**

Equations
- Tau.BookIV.Arena.phys_const_core = { generator_numer := Tau.Boundary.iota_tau_numer, generator_denom := Tau.Boundary.iota_tau_denom,
 gen_is_iota := Tau.BookIV.Arena.phys_const_core._proof_1 }
Instances For

---

### `Tau.BookIV.Arena.SectorLift`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L139-L147)
**structure
Tau.BookIV.Arena.SectorLift :Type**


[IV.D262] A canonical sector lift: Λ_S: L → τ³ projecting boundary
data to a specific sector. There are 5 lifts (one per sector).

- sector : BookIII.Sectors.Sector
Target sector.

- rational : Bool
The lift produces rational functions of ι<sub>τ</sub>.

- rational_true : self.rational = true
Instances For

---

### `Tau.BookIV.Arena.instReprSectorLift.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L147-L147)
**def
Tau.BookIV.Arena.instReprSectorLift.repr :SectorLift → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.instReprSectorLift`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L147-L147)
**instance
Tau.BookIV.Arena.instReprSectorLift :Repr SectorLift**

Equations
- Tau.BookIV.Arena.instReprSectorLift = { reprPrec := Tau.BookIV.Arena.instReprSectorLift.repr }

---

### `Tau.BookIV.Arena.all_sector_lifts`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L149-L152)
**def
Tau.BookIV.Arena.all_sector_lifts :List SectorLift**


All 5 canonical sector lifts.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.BoundaryChartReadout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L160-L169)
**structure
Tau.BookIV.Arena.BoundaryChartReadout :Type**


[IV.D263] Chart readout from boundary data: assembles sector lifts
into a coherent 4D readout.

- lift_count : ℕ
Number of sector lifts used.

- lift_count_eq : self.lift_count = 5
- output_dim : ℕ
Output dimension.

- output_eq : self.output_dim = 4
Instances For

---

### `Tau.BookIV.Arena.instReprBoundaryChartReadout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L169-L169)
**instance
Tau.BookIV.Arena.instReprBoundaryChartReadout :Repr BoundaryChartReadout**

Equations
- Tau.BookIV.Arena.instReprBoundaryChartReadout = { reprPrec := Tau.BookIV.Arena.instReprBoundaryChartReadout.repr }

---

### `Tau.BookIV.Arena.instReprBoundaryChartReadout.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L169-L169)
**def
Tau.BookIV.Arena.instReprBoundaryChartReadout.repr :BoundaryChartReadout → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.smooth_from_coherent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L175-L180)
**theorem
Tau.BookIV.Arena.smooth_from_coherent :all_sector_lifts.length = 5 ∧ chart_readout.target_dim = 4**


[IV.P153] Coherent chart readouts produce smooth manifold structure.
When sector lifts are mutually consistent, the readout space is
a smooth 4-manifold (locally ℝ⁴).

---

### `Tau.BookIV.Arena.boundary_triad`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/BoundaryHolonomy.lean#L189-L201)
**theorem
Tau.BookIV.Arena.boundary_triad :1 + 1 + 1 = 3 ∧ CharacterType.ChiPlus ≠ CharacterType.ChiMinus ∧ all_sector_lifts.length = 5 ∧ chart_readout.target_dim = 4**


[IV.T97] Boundary Triad Theorem: the boundary L carries exactly 3
canonical structures: (1) bipolar characters, (2) sector lifts,
(3) chart readouts. These are the complete set of observable data.
