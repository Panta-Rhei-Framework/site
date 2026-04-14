---
layout: taulib-doc
title: "TauLib.BookIV.QuantumMechanics.QuantumCharacters"
permalink: /verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/
lane: verify
module_name: "TauLib.BookIV.QuantumMechanics.QuantumCharacters"
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

# TauLib.BookIV.QuantumMechanics.QuantumCharacters


Characters on T^2 as the "address book" for quantum states:
character variety, geometric charge, charge quantization,
energy duality, and the sharp/spread conjugate trade-off.

## Registry Cross-References


- [IV.D55] Character on a Space — `SpaceCharacter`

- [IV.P11] Characters on T^2 — `characters_determined_by_pair`

- [IV.D56] Character Variety of T^2 — `CharacterVariety`

- [IV.P12] Automatic Quantization — `automatic_quantization`

- [IV.D57] Address Precision (ch17) — `CharacterPrecision`

- [IV.D58] Geometric Charge — `GeometricCharge`

- [IV.P13] Charge Quantization from Winding — `charge_quantized`

- [IV.R14] Fractional Charges and Confinement — (structural remark)

- [IV.P14] Energy Duality — `energy_duality`

- [IV.D59] Sharp and Spread States — `StateSharpness`

- [IV.P15] Conjugate Precision Trade-off — `conjugate_tradeoff`

- [IV.R15] Quasi-Ergodic Coverage — (structural remark)


## Ground Truth Sources


- Chapter 17 of Book IV (2nd Edition)


---

### `Tau.BookIV.QuantumMechanics.SpaceCharacter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L39-L50)
**structure
Tau.BookIV.QuantumMechanics.SpaceCharacter :Type**


[IV.D55] Character on a path-connected space X: a group
homomorphism pi_1(X) -> U(1). For T^2, pi_1 = Z^2, so a
character is determined by an image pair (m, n) in Z^2.
This is the abstract definition.

- pi1_rank : ℕ
Dimension of the fundamental group (rank of pi_1).

- param_count : ℕ
The character is determined by this many integers.

- param_eq : self.param_count = self.pi1_rank
Number of parameters equals pi_1 rank.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprSpaceCharacter.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L50-L50)
**def
Tau.BookIV.QuantumMechanics.instReprSpaceCharacter.repr :SpaceCharacter → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprSpaceCharacter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L50-L50)
**instance
Tau.BookIV.QuantumMechanics.instReprSpaceCharacter :Repr SpaceCharacter**

Equations
- Tau.BookIV.QuantumMechanics.instReprSpaceCharacter = { reprPrec := Tau.BookIV.QuantumMechanics.instReprSpaceCharacter.repr }

---

### `Tau.BookIV.QuantumMechanics.characters_on_torus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L56-L61)
**def
Tau.BookIV.QuantumMechanics.characters_on_torus :SpaceCharacter**


[IV.P11] A character on T^2 is determined by a pair (m,n) in Z^2,
since pi_1(T^2) = Z^2 has rank 2.
Equations
- Tau.BookIV.QuantumMechanics.characters_on_torus = { pi1_rank := 2, param_count := 2, param_eq := Tau.BookIV.QuantumMechanics.characters_on_torus._proof_1 }
Instances For

---

### `Tau.BookIV.QuantumMechanics.characters_determined_by_pair`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L63-L65)
**theorem
Tau.BookIV.QuantumMechanics.characters_determined_by_pair :characters_on_torus.param_count = 2**


Characters on T^2 are determined by exactly 2 integers.

---

### `Tau.BookIV.QuantumMechanics.FiberCharacter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L71-L81)
**structure
Tau.BookIV.QuantumMechanics.FiberCharacter :Type**


[IV.D56] Character variety Char(T^2) = U(1) x U(1) = T^2.
The admissible quantum characters are those restricted to
the CR-admissible sublattice Lambda_CR.

A FiberCharacter is a character mode together with its
CR-admissibility proof.

- mode : CharacterMode
The underlying (m,n) address.

- admissible : cr_admissible self.mode
Must be CR-admissible: m + n even.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprFiberCharacter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L83-L84)
**instance
Tau.BookIV.QuantumMechanics.instReprFiberCharacter :Repr FiberCharacter**

Equations
- One or more equations did not get rendered due to their size.

---

### `Tau.BookIV.QuantumMechanics.CharacterVariety`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L86-L94)
**structure
Tau.BookIV.QuantumMechanics.CharacterVariety :Type**


[IV.D56] The character variety has dimension 2 (= rank of pi_1(T^2)).

- dim : ℕ
Dimension of Char(T^2).

- dim_eq : self.dim = 2
- is_compact : Bool
Char(T^2) is compact (T^2 is compact).

- compact_true : self.is_compact = true
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprCharacterVariety`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L94-L94)
**instance
Tau.BookIV.QuantumMechanics.instReprCharacterVariety :Repr CharacterVariety**

Equations
- Tau.BookIV.QuantumMechanics.instReprCharacterVariety = { reprPrec := Tau.BookIV.QuantumMechanics.instReprCharacterVariety.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprCharacterVariety.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L94-L94)
**def
Tau.BookIV.QuantumMechanics.instReprCharacterVariety.repr :CharacterVariety → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.char_variety`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L96-L101)
**def
Tau.BookIV.QuantumMechanics.char_variety :CharacterVariety**


The canonical character variety.
Equations
- Tau.BookIV.QuantumMechanics.char_variety = { dim := 2, dim_eq := Tau.BookIV.QuantumMechanics.characters_on_torus._proof_1, is_compact := true,
 compact_true := ⋯ }
Instances For

---

### `Tau.BookIV.QuantumMechanics.automatic_quantization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L107-L111)
**theorem
Tau.BookIV.QuantumMechanics.automatic_quantization
(fc : FiberCharacter)
 :cr_admissible fc.mode**


[IV.P12] Automatic quantization: the admissible quantum addresses
are automatically restricted to Lambda_CR. No quantization postulate
is needed — it follows from CR-admissibility.

---

### `Tau.BookIV.QuantumMechanics.CharacterPrecision`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L117-L131)
**structure
Tau.BookIV.QuantumMechanics.CharacterPrecision :Type**


[IV.D57] Address precision at a specific character: delta(psi, (m0,n0))
= |c_{m0,n0}|^2 in [0,1]. Same concept as IV.D53 but specifically
tied to a FiberCharacter.

- target : FiberCharacter
The target character.

- numer : ℕ
Precision numerator (|c|^2 scaled).

- denom : ℕ
Precision denominator.

- denom_pos : self.denom > 0
Denominator positive.

- numer_le : self.numer ≤ self.denom
Precision in [0,1]: numer <= denom.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprCharacterPrecision`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L131-L131)
**instance
Tau.BookIV.QuantumMechanics.instReprCharacterPrecision :Repr CharacterPrecision**

Equations
- Tau.BookIV.QuantumMechanics.instReprCharacterPrecision = { reprPrec := Tau.BookIV.QuantumMechanics.instReprCharacterPrecision.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprCharacterPrecision.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L131-L131)
**def
Tau.BookIV.QuantumMechanics.instReprCharacterPrecision.repr :CharacterPrecision → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.GeometricCharge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L137-L147)
**structure
Tau.BookIV.QuantumMechanics.GeometricCharge :Type**


[IV.D58] Geometric charge from relative orientation of the
gamma-tube and eta-tube on T^2. Charge is an integer multiple
of a minimal quantum e_tau. Represented as (charge, scale).

- charge : ℤ
Charge numerator (integer winding number).

- scale : ℕ
Scale denominator (for fractional display).

- scale_pos : self.scale > 0
Scale is positive.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprGeometricCharge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L147-L147)
**instance
Tau.BookIV.QuantumMechanics.instReprGeometricCharge :Repr GeometricCharge**

Equations
- Tau.BookIV.QuantumMechanics.instReprGeometricCharge = { reprPrec := Tau.BookIV.QuantumMechanics.instReprGeometricCharge.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprGeometricCharge.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L147-L147)
**def
Tau.BookIV.QuantumMechanics.instReprGeometricCharge.repr :GeometricCharge → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.unit_charge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L149-L153)
**def
Tau.BookIV.QuantumMechanics.unit_charge :GeometricCharge**


Unit geometric charge (e_tau = 1).
Equations
- Tau.BookIV.QuantumMechanics.unit_charge = { charge := 1, scale := 1, scale_pos := Tau.BookIV.QuantumMechanics.unit_charge._proof_2 }
Instances For

---

### `Tau.BookIV.QuantumMechanics.charge_quantized`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L159-L165)
**theorem
Tau.BookIV.QuantumMechanics.charge_quantized
(gc : GeometricCharge)
 :gc.scale = 1 → ∃ (k : ℤ), gc.charge = k * 1**


[IV.P13] Charge quantization from winding: electric charge is an
integer multiple of the minimal charge e_tau. The integer is the
winding number of the gamma-tube around the eta-tube.
Formalized: charge is always an integer multiple of unit.

---

### `Tau.BookIV.QuantumMechanics.EnergyDuality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L176-L194)
**structure
Tau.BookIV.QuantumMechanics.EnergyDuality :Type**


[IV.P14] Energy duality: E = mc^2 (fiber stiffness) and E = hbar*omega
(base frequency) read the same eigenvalue of the defect coherence
functional from two complementary perspectives.
Formalized: the two energy indices agree structurally.

- e_mass_numer : ℕ
Mass-derived energy numerator.

- e_mass_denom : ℕ
Mass-derived energy denominator.

- e_freq_numer : ℕ
Frequency-derived energy numerator.

- e_freq_denom : ℕ
Frequency-derived energy denominator.

- mass_denom_pos : self.e_mass_denom > 0
Both denominators positive.

- freq_denom_pos : self.e_freq_denom > 0
- duality : self.e_mass_numer * self.e_freq_denom = self.e_freq_numer * self.e_mass_denom
Duality: same eigenvalue (cross-multiplication).

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprEnergyDuality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L194-L194)
**instance
Tau.BookIV.QuantumMechanics.instReprEnergyDuality :Repr EnergyDuality**

Equations
- Tau.BookIV.QuantumMechanics.instReprEnergyDuality = { reprPrec := Tau.BookIV.QuantumMechanics.instReprEnergyDuality.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprEnergyDuality.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L194-L194)
**def
Tau.BookIV.QuantumMechanics.instReprEnergyDuality.repr :EnergyDuality → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.energy_duality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L196-L199)
**theorem
Tau.BookIV.QuantumMechanics.energy_duality
(ed : EnergyDuality)
 :ed.e_mass_numer * ed.e_freq_denom = ed.e_freq_numer * ed.e_mass_denom**


Energy duality holds as a structural identity.

---

### `Tau.BookIV.QuantumMechanics.StateSharpness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L205-L212)
**inductive
Tau.BookIV.QuantumMechanics.StateSharpness :Type**


[IV.D59] A state is sharp at address (m0,n0) if its precision is
close to 1, and spread if the precision is distributed across many modes.

- Sharp : StateSharpness
Precision concentrated at one address.

- Spread : StateSharpness
Precision distributed across many addresses.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprStateSharpness.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L212-L212)
**def
Tau.BookIV.QuantumMechanics.instReprStateSharpness.repr :StateSharpness → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprStateSharpness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L212-L212)
**instance
Tau.BookIV.QuantumMechanics.instReprStateSharpness :Repr StateSharpness**

Equations
- Tau.BookIV.QuantumMechanics.instReprStateSharpness = { reprPrec := Tau.BookIV.QuantumMechanics.instReprStateSharpness.repr }

---

### `Tau.BookIV.QuantumMechanics.instDecidableEqStateSharpness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L212-L212)
**instance
Tau.BookIV.QuantumMechanics.instDecidableEqStateSharpness :DecidableEq StateSharpness**

Equations
- Tau.BookIV.QuantumMechanics.instDecidableEqStateSharpness x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.QuantumMechanics.instBEqStateSharpness.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L212-L212)
**def
Tau.BookIV.QuantumMechanics.instBEqStateSharpness.beq :StateSharpness → StateSharpness → Bool**

Equations
- Tau.BookIV.QuantumMechanics.instBEqStateSharpness.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.QuantumMechanics.instBEqStateSharpness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L212-L212)
**instance
Tau.BookIV.QuantumMechanics.instBEqStateSharpness :BEq StateSharpness**

Equations
- Tau.BookIV.QuantumMechanics.instBEqStateSharpness = { beq := Tau.BookIV.QuantumMechanics.instBEqStateSharpness.beq }

---

### `Tau.BookIV.QuantumMechanics.conjugate_tradeoff`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean#L218-L228)
**theorem
Tau.BookIV.QuantumMechanics.conjugate_tradeoff
(p_gamma p_eta budget : ℕ)

(h_budget : p_gamma * p_eta ≤ budget)
 :p_gamma > 0 → ∀ (h_eta_pos : p_eta > 0), p_gamma ≤ budget / p_eta**


[IV.P15] Conjugate precision trade-off: sharpening in one direction
(gamma-tube) necessarily spreads in the conjugate direction (eta-tube).
This is the structural origin of the uncertainty principle.
Formalized: if gamma-precision * eta-precision <= total_budget,
increasing one decreases the other.
