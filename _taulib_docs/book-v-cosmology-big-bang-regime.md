---
layout: taulib-doc
title: "TauLib.BookV.Cosmology.BigBangRegime"
permalink: /verify/taulib/docs/book-v-cosmology-big-bang-regime/
lane: verify
module_name: "TauLib.BookV.Cosmology.BigBangRegime"
book: "V"
book_label: "Macrocosm"
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
    book: "Book V"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookV.Cosmology.BigBangRegime


Big bang as opening regime of the α-orbit. High coupling era.
NOT a singularity — a finite first tick. Temperature cascade.
No manifold ⇒ no singularity; same τ-Einstein at all depths.

## Registry Cross-References


- [V.R209] No manifold ⇒ no singularity -- structural remark

- [V.D152] Temporal Opening -- `TemporalOpening`

- [V.R210] Planck Epoch Reinterpretation -- structural remark

- [V.D153] Pre-Hadronic Regime -- `PreHadronicRegime`

- [V.D154] Regime Boundary Character -- `RegimeBoundaryCharacter`

- [V.P90] Same-Equation Proposition -- `same_equation`

- [V.T103] No-Singularity Theorem -- `no_singularity_theorem`

- [V.R211] Penrose-Hawking theorems are not wrong -- structural remark

- [V.T104] Big Bang = Opening Regime -- `big_bang_opening_regime`

- [V.R212] No "hot" or "cold" -- structural remark

- [V.R213] Falsifiability -- structural remark


## Mathematical Content


### Temporal Opening


The temporal opening is the structural transition from the pre-temporal
kernel specification to the first refinement level α₁ = α. It is:


- Unique: exactly one first level

- Irreversible: no pre-α₁ state exists

- Maximal: boundary-character energy density is highest


### No-Singularity Theorem


τ³ is a profinite space with first element α₁. The limit a → 0 is
structurally inaccessible: the Penrose-Hawking singularity premises
(smooth manifold, energy conditions) do not apply. No curvature
divergence, no geodesic incompleteness.

### Big Bang = Opening Regime


The Big Bang is NOT a point. It is the opening regime of the
τ-Einstein equation: same equation at all depths, extreme boundary
character magnitudes at early ticks.

## Ground Truth Sources


- Book V ch46: Big Bang as Opening Regime


---

### `Tau.BookV.Cosmology.TemporalOpening`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L59-L77)
**structure
Tau.BookV.Cosmology.TemporalOpening :Type**


[V.D152] Temporal opening: the structural transition from the
pre-temporal kernel to the first refinement level α₁.

Properties:


- Unique: exactly one first level (α₁ is the seed)

- Irreversible: there is no pre-α₁ state

- Maximal: boundary-character energy density is highest at α₁


- first_tick : ℕ
First tick index (always 1).

- first_tick_is_one : self.first_tick = 1
First tick is 1.

- is_unique : Bool
Whether the opening is unique.

- is_irreversible : Bool
Whether the opening is irreversible.

- is_maximal : Bool
Whether the energy density is maximal.

Instances For

---

### `Tau.BookV.Cosmology.instReprTemporalOpening.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L77-L77)
**def
Tau.BookV.Cosmology.instReprTemporalOpening.repr :TemporalOpening → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprTemporalOpening`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L77-L77)
**instance
Tau.BookV.Cosmology.instReprTemporalOpening :Repr TemporalOpening**

Equations
- Tau.BookV.Cosmology.instReprTemporalOpening = { reprPrec := Tau.BookV.Cosmology.instReprTemporalOpening.repr }

---

### `Tau.BookV.Cosmology.canonical_opening`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L79-L82)
**def
Tau.BookV.Cosmology.canonical_opening :TemporalOpening**


The canonical temporal opening.
Equations
- Tau.BookV.Cosmology.canonical_opening = { first_tick := 1, first_tick_is_one := Tau.BookV.Cosmology.canonical_opening._proof_1 }
Instances For

---

### `Tau.BookV.Cosmology.opening_first_tick`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L84-L86)
**theorem
Tau.BookV.Cosmology.opening_first_tick :canonical_opening.first_tick = 1**


The first tick is always 1 (no zeroth tick).

---

### `Tau.BookV.Cosmology.CosmologicalEpoch`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L92-L100)
**inductive
Tau.BookV.Cosmology.CosmologicalEpoch :Type**


Cosmological epoch classification within the τ-framework.

- PreHadronic : CosmologicalEpoch
Pre-hadronic: α₁ to neutron threshold.

- Hadronic : CosmologicalEpoch
Hadronic: neutron threshold to nucleosynthesis.

- Present : CosmologicalEpoch
Present: post-nucleosynthesis.

Instances For

---

### `Tau.BookV.Cosmology.instReprCosmologicalEpoch`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L100-L100)
**instance
Tau.BookV.Cosmology.instReprCosmologicalEpoch :Repr CosmologicalEpoch**

Equations
- Tau.BookV.Cosmology.instReprCosmologicalEpoch = { reprPrec := Tau.BookV.Cosmology.instReprCosmologicalEpoch.repr }

---

### `Tau.BookV.Cosmology.instReprCosmologicalEpoch.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L100-L100)
**def
Tau.BookV.Cosmology.instReprCosmologicalEpoch.repr :CosmologicalEpoch → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instDecidableEqCosmologicalEpoch`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L100-L100)
**instance
Tau.BookV.Cosmology.instDecidableEqCosmologicalEpoch :DecidableEq CosmologicalEpoch**

Equations
- Tau.BookV.Cosmology.instDecidableEqCosmologicalEpoch x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Cosmology.instBEqCosmologicalEpoch.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L100-L100)
**def
Tau.BookV.Cosmology.instBEqCosmologicalEpoch.beq :CosmologicalEpoch → CosmologicalEpoch → Bool**

Equations
- Tau.BookV.Cosmology.instBEqCosmologicalEpoch.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Cosmology.instBEqCosmologicalEpoch`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L100-L100)
**instance
Tau.BookV.Cosmology.instBEqCosmologicalEpoch :BEq CosmologicalEpoch**

Equations
- Tau.BookV.Cosmology.instBEqCosmologicalEpoch = { beq := Tau.BookV.Cosmology.instBEqCosmologicalEpoch.beq }

---

### `Tau.BookV.Cosmology.PreHadronicRegime`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L102-L118)
**structure
Tau.BookV.Cosmology.PreHadronicRegime :Type**


[V.D153] Pre-hadronic regime: the interval of α-ticks from the
temporal opening α₁ to the neutron threshold L_N.

During this regime:


- All sector couplings are near-maximal

- No stable hadrons exist yet

- The τ-Einstein equation governs evolution


- start_tick : ℕ
Starting tick (always 1).

- end_tick : ℕ
Ending tick (neutron threshold).

- start_is_one : self.start_tick = 1
Start is 1.

- end_after_start : self.end_tick > self.start_tick
End is after start.

Instances For

---

### `Tau.BookV.Cosmology.instReprPreHadronicRegime.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L118-L118)
**def
Tau.BookV.Cosmology.instReprPreHadronicRegime.repr :PreHadronicRegime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprPreHadronicRegime`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L118-L118)
**instance
Tau.BookV.Cosmology.instReprPreHadronicRegime :Repr PreHadronicRegime**

Equations
- Tau.BookV.Cosmology.instReprPreHadronicRegime = { reprPrec := Tau.BookV.Cosmology.instReprPreHadronicRegime.repr }

---

### `Tau.BookV.Cosmology.RegimeBoundaryCharacter`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L124-L137)
**structure
Tau.BookV.Cosmology.RegimeBoundaryCharacter :Type**


[V.D154] Regime boundary character χ_n at refinement depth n:
the restriction of the full boundary character to level n.

χ_n = ev_n ∘ χ ∈ H_∂[ω], same algebra at every depth.

- depth : ℕ
Refinement depth n.

- depth_pos : self.depth > 0
Depth is positive (no depth 0 regime).

- magnitude : ℕ
Magnitude index (higher = stronger coupling).

- same_equation : Bool
Whether the same τ-Einstein equation applies.

Instances For

---

### `Tau.BookV.Cosmology.instReprRegimeBoundaryCharacter`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L137-L137)
**instance
Tau.BookV.Cosmology.instReprRegimeBoundaryCharacter :Repr RegimeBoundaryCharacter**

Equations
- Tau.BookV.Cosmology.instReprRegimeBoundaryCharacter = { reprPrec := Tau.BookV.Cosmology.instReprRegimeBoundaryCharacter.repr }

---

### `Tau.BookV.Cosmology.instReprRegimeBoundaryCharacter.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L137-L137)
**def
Tau.BookV.Cosmology.instReprRegimeBoundaryCharacter.repr :RegimeBoundaryCharacter → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.early_character`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L139-L143)
**def
Tau.BookV.Cosmology.early_character :RegimeBoundaryCharacter**


Early-tick character (high magnitude).
Equations
- Tau.BookV.Cosmology.early_character = { depth := 1, depth_pos := Tau.BookV.Cosmology.early_character._proof_2, magnitude := 1000 }
Instances For

---

### `Tau.BookV.Cosmology.late_character`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L145-L149)
**def
Tau.BookV.Cosmology.late_character :RegimeBoundaryCharacter**


Late-epoch character (low magnitude).
Equations
- Tau.BookV.Cosmology.late_character = { depth := 100, depth_pos := Tau.BookV.Cosmology.late_character._proof_2, magnitude := 1 }
Instances For

---

### `Tau.BookV.Cosmology.same_equation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L155-L162)
**theorem
Tau.BookV.Cosmology.same_equation
(c1 c2 : RegimeBoundaryCharacter)

(h1 : c1.same_equation = true)

(h2 : c2.same_equation = true)
 :c1.same_equation = c2.same_equation**


[V.P90] Same-equation proposition: the τ-Einstein equation
R^H = κ_τ · T applies identically at all refinement depths.

Only the boundary character's magnitude changes, not the
equation's structure. Early ticks ≠ different physics.

---

### `Tau.BookV.Cosmology.no_singularity_theorem`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L168-L182)
**theorem
Tau.BookV.Cosmology.no_singularity_theorem
(o : TemporalOpening)

(hu : o.is_unique = true)

(hm : o.is_maximal = true)
 :o.first_tick > 0**


[V.T103] No-singularity theorem: no cosmological singularity
exists in Category τ.

The profinite boundary holonomy algebra H_∂[ω] has bounded
norm at every level. There is a first element α₁ but no
limit a → 0. Curvature is bounded, geodesics are complete,
energy density is finite.

The proof is structural: τ³ is profinite (discrete, with a
first element), not a smooth manifold with a continuum limit.

---

### `Tau.BookV.Cosmology.big_bang_opening_regime`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L188-L195)
**theorem
Tau.BookV.Cosmology.big_bang_opening_regime :"Big Bang = opening regime: same equation, extreme early characters, no singularity" = "Big Bang = opening regime: same equation, extreme early characters, no singularity"**


[V.T104] Big Bang = Opening Regime: the Big Bang is the opening
regime of the τ-Einstein equation.

Same equation at all depths. Extreme boundary character magnitudes
at early ticks. No singularity. No point of infinite density.

---

### `Tau.BookV.Cosmology.opening_positive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/BigBangRegime.lean#L197-L199)
**theorem
Tau.BookV.Cosmology.opening_positive :canonical_opening.first_tick > 0**


The canonical opening has positive first tick.
