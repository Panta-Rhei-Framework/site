---
layout: taulib-doc
title: "TauLib.BookIV.Physics.TickUnits"
permalink: /verify/taulib/docs/book-iv-physics-tick-units/
lane: verify
module_name: "TauLib.BookIV.Physics.TickUnits"
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

# TauLib.BookIV.Physics.TickUnits


Tick units as categorical endomorphisms: the minimal generator steps that
define internal measurement within Layer 1 (internal physics).

## Registry Cross-References


- [IV.D321] Tick Morphism — `TickMorphism`

- [IV.D322] Tick Kind — `TickKind`

- [IV.T125] Tick-Sector Bijection — `tick_sector_bijection`

- [IV.T126] Tick Exhaustion — `tick_exhaustion`


## Mathematical Content


### Tick Units as Categorical Morphisms


Each tick is a **minimal non-identity endomorphism** in its sector subcategory
of the boundary holonomy algebra H_∂[ω]. Within Layer 1 (internal physics),
all "durations" are counted in α-ticks, all "energies" in γ-oscillations, etc.
No seconds, no joules, no kilograms — pure counting of generator actions.


Tick
Generator
Categorical type
Layer 2 readout


α-tick
α
End(τ¹)_D — minimal gravitational step
Planck time


π-step
π
End(τ¹)_A — minimal weak step
Weak decay quantum


γ-oscillation
γ
End(T²)_B — minimal EM cycle
Photon period


η-step
η
End(T²)_C — minimal strong step
Confinement scale


ω-crossing
ω
Aut(L)_{B∩C} — lobe crossing
Mass event


### Key Principle


Within Layer 1, quantities are **tick counts** (natural numbers), not reals
with SI dimensions. The passage to ℝ-valued measurements occurs only in
Layer 2 via the readout functor R_μ.

## Ground Truth Sources


- Book IV Part II ch08-ch10: Internal physics layer

- particle-physics-defects.json: five-physical-invariants


---

### `Tau.BookIV.Physics.TickKind`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L52-L70)
**inductive
Tau.BookIV.Physics.TickKind :Type**


[IV.D322] The 5 tick kinds, one per generator/sector.
Each tick is the minimal non-identity endomorphism in its sector.

- AlphaTick : TickKind
α-tick: minimal gravitational endomorphism of τ¹ in sector D.
The internal unit of temporal duration.

- PiStep : TickKind
π-step: minimal weak endomorphism of τ¹ in sector A.
The internal unit of weak process evolution.

- GammaOscillation : TickKind
γ-oscillation: minimal EM endomorphism of T² in sector B.
The internal unit of electromagnetic phase.

- EtaStep : TickKind
η-step: minimal strong endomorphism of T² in sector C.
The internal unit of confinement-scale process.

- OmegaCrossing : TickKind
ω-crossing: minimal lobe automorphism at B∩C in sector ω.
The internal unit of mass acquisition.

Instances For

---

### `Tau.BookIV.Physics.instReprTickKind`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L70-L70)
**instance
Tau.BookIV.Physics.instReprTickKind :Repr TickKind**

Equations
- Tau.BookIV.Physics.instReprTickKind = { reprPrec := Tau.BookIV.Physics.instReprTickKind.repr }

---

### `Tau.BookIV.Physics.instReprTickKind.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L70-L70)
**def
Tau.BookIV.Physics.instReprTickKind.repr :TickKind → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instDecidableEqTickKind`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L70-L70)
**instance
Tau.BookIV.Physics.instDecidableEqTickKind :DecidableEq TickKind**

Equations
- Tau.BookIV.Physics.instDecidableEqTickKind x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Physics.instBEqTickKind`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L70-L70)
**instance
Tau.BookIV.Physics.instBEqTickKind :BEq TickKind**

Equations
- Tau.BookIV.Physics.instBEqTickKind = { beq := Tau.BookIV.Physics.instBEqTickKind.beq }

---

### `Tau.BookIV.Physics.instBEqTickKind.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L70-L70)
**def
Tau.BookIV.Physics.instBEqTickKind.beq :TickKind → TickKind → Bool**

Equations
- Tau.BookIV.Physics.instBEqTickKind.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Physics.instInhabitedTickKind`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L70-L70)
**instance
Tau.BookIV.Physics.instInhabitedTickKind :Inhabited TickKind**

Equations
- Tau.BookIV.Physics.instInhabitedTickKind = { default := Tau.BookIV.Physics.instInhabitedTickKind.default }

---

### `Tau.BookIV.Physics.instInhabitedTickKind.default`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L70-L70)
**def
Tau.BookIV.Physics.instInhabitedTickKind.default :TickKind**

Equations
- Tau.BookIV.Physics.instInhabitedTickKind.default = Tau.BookIV.Physics.TickKind.AlphaTick
Instances For

---

### `Tau.BookIV.Physics.TickMorphism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L76-L88)
**structure
Tau.BookIV.Physics.TickMorphism :Type**


[IV.D321] A tick morphism: a counted number of minimal generator steps
in a specific sector. This is an internal Layer 1 object — no SI units.

Ontologically: a morphism `n : End(X)_S` where X is the appropriate
carrier (τ¹ or T²) and S is the sector. The `count` field is the
number of generator compositions.

- kind : TickKind
Which tick kind (= which generator/sector).

- count : ℕ
Number of generator applications (composition count).
0 = identity morphism.

Instances For

---

### `Tau.BookIV.Physics.instReprTickMorphism.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L88-L88)
**def
Tau.BookIV.Physics.instReprTickMorphism.repr :TickMorphism → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instReprTickMorphism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L88-L88)
**instance
Tau.BookIV.Physics.instReprTickMorphism :Repr TickMorphism**

Equations
- Tau.BookIV.Physics.instReprTickMorphism = { reprPrec := Tau.BookIV.Physics.instReprTickMorphism.repr }

---

### `Tau.BookIV.Physics.instDecidableEqTickMorphism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L88-L88)
**instance
Tau.BookIV.Physics.instDecidableEqTickMorphism :DecidableEq TickMorphism**

Equations
- Tau.BookIV.Physics.instDecidableEqTickMorphism = Tau.BookIV.Physics.instDecidableEqTickMorphism.decEq

---

### `Tau.BookIV.Physics.instDecidableEqTickMorphism.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L88-L88)
**def
Tau.BookIV.Physics.instDecidableEqTickMorphism.decEq
(x✝ x✝¹ : TickMorphism)
 :Decidable (x✝ = x✝¹)**

Equations
- Tau.BookIV.Physics.instDecidableEqTickMorphism.decEq { kind := a, count := a_1 } { kind := b, count := b_1 } = if h : a = b then h ▸ if h : a_1 = b_1 then h ▸ isTrue ⋯ else isFalse ⋯ else isFalse ⋯
Instances For

---

### `Tau.BookIV.Physics.instBEqTickMorphism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L88-L88)
**instance
Tau.BookIV.Physics.instBEqTickMorphism :BEq TickMorphism**

Equations
- Tau.BookIV.Physics.instBEqTickMorphism = { beq := Tau.BookIV.Physics.instBEqTickMorphism.beq }

---

### `Tau.BookIV.Physics.instBEqTickMorphism.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L88-L88)
**def
Tau.BookIV.Physics.instBEqTickMorphism.beq :TickMorphism → TickMorphism → Bool**

Equations
- Tau.BookIV.Physics.instBEqTickMorphism.beq { kind := a, count := a_1 } { kind := b, count := b_1 } = (a == b && a_1 == b_1)
- Tau.BookIV.Physics.instBEqTickMorphism.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIV.Physics.TickMorphism.identity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L90-L93)
**def
Tau.BookIV.Physics.TickMorphism.identity
(k : TickKind)
 :TickMorphism**


The identity tick (zero applications).
Equations
- Tau.BookIV.Physics.TickMorphism.identity k = { kind := k, count := 0 }
Instances For

---

### `Tau.BookIV.Physics.TickMorphism.compose`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L95-L99)
**def
Tau.BookIV.Physics.TickMorphism.compose
(a b : TickMorphism)

(h : a.kind = b.kind)
 :TickMorphism**


Compose two tick morphisms of the same kind.
Equations
- a.compose b h = { kind := a.kind, count := a.count + b.count }
Instances For

---

### `Tau.BookIV.Physics.TickKind.sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L105-L111)
**def
Tau.BookIV.Physics.TickKind.sector :TickKind → BookIII.Sectors.Sector**


The sector governing a given tick kind.
Equations
- Tau.BookIV.Physics.TickKind.AlphaTick.sector = Tau.BookIII.Sectors.Sector.D
- Tau.BookIV.Physics.TickKind.PiStep.sector = Tau.BookIII.Sectors.Sector.A
- Tau.BookIV.Physics.TickKind.GammaOscillation.sector = Tau.BookIII.Sectors.Sector.B
- Tau.BookIV.Physics.TickKind.EtaStep.sector = Tau.BookIII.Sectors.Sector.C
- Tau.BookIV.Physics.TickKind.OmegaCrossing.sector = Tau.BookIII.Sectors.Sector.Omega
Instances For

---

### `Tau.BookIV.Physics.TickKind.carrier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L113-L119)
**def
Tau.BookIV.Physics.TickKind.carrier :TickKind → CarrierType**


The carrier type for a given tick kind.
Equations
- Tau.BookIV.Physics.TickKind.AlphaTick.carrier = Tau.BookIV.Physics.CarrierType.Base
- Tau.BookIV.Physics.TickKind.PiStep.carrier = Tau.BookIV.Physics.CarrierType.Base
- Tau.BookIV.Physics.TickKind.GammaOscillation.carrier = Tau.BookIV.Physics.CarrierType.Fiber
- Tau.BookIV.Physics.TickKind.EtaStep.carrier = Tau.BookIV.Physics.CarrierType.Fiber
- Tau.BookIV.Physics.TickKind.OmegaCrossing.carrier = Tau.BookIV.Physics.CarrierType.Crossing
Instances For

---

### `Tau.BookIV.Physics.TickKind.measuredInvariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L121-L127)
**def
Tau.BookIV.Physics.TickKind.measuredInvariant :TickKind → PrimaryInvariant**


The primary invariant measured by counting a given tick kind.
Equations
- Tau.BookIV.Physics.TickKind.AlphaTick.measuredInvariant = Tau.BookIV.Physics.PrimaryInvariant.Gravity
- Tau.BookIV.Physics.TickKind.PiStep.measuredInvariant = Tau.BookIV.Physics.PrimaryInvariant.Time
- Tau.BookIV.Physics.TickKind.GammaOscillation.measuredInvariant = Tau.BookIV.Physics.PrimaryInvariant.Energy
- Tau.BookIV.Physics.TickKind.EtaStep.measuredInvariant = Tau.BookIV.Physics.PrimaryInvariant.Mass
- Tau.BookIV.Physics.TickKind.OmegaCrossing.measuredInvariant = Tau.BookIV.Physics.PrimaryInvariant.Entropy
Instances For

---

### `Tau.BookIV.Physics.tick_sector_bijection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L133-L146)
**theorem
Tau.BookIV.Physics.tick_sector_bijection :TickKind.AlphaTick.sector ≠ TickKind.PiStep.sector ∧ TickKind.AlphaTick.sector ≠ TickKind.GammaOscillation.sector ∧ TickKind.AlphaTick.sector ≠ TickKind.EtaStep.sector ∧ TickKind.AlphaTick.sector ≠ TickKind.OmegaCrossing.sector ∧ TickKind.PiStep.sector ≠ TickKind.GammaOscillation.sector ∧ TickKind.PiStep.sector ≠ TickKind.EtaStep.sector ∧ TickKind.PiStep.sector ≠ TickKind.OmegaCrossing.sector ∧ TickKind.GammaOscillation.sector ≠ TickKind.EtaStep.sector ∧ TickKind.GammaOscillation.sector ≠ TickKind.OmegaCrossing.sector ∧ TickKind.EtaStep.sector ≠ TickKind.OmegaCrossing.sector**


[IV.T125] Tick-Sector Bijection: each tick kind maps to a distinct sector,
and each sector has exactly one tick kind.

---

### `Tau.BookIV.Physics.tick_exhaustion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L148-L152)
**theorem
Tau.BookIV.Physics.tick_exhaustion
(t : TickKind)
 :t = TickKind.AlphaTick ∨ t = TickKind.PiStep ∨ t = TickKind.GammaOscillation ∨ t = TickKind.EtaStep ∨ t = TickKind.OmegaCrossing**


[IV.T126] Tick Exhaustion: every tick kind is one of the five.

---

### `Tau.BookIV.Physics.tick_sector_consistent_with_invariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L154-L157)
**theorem
Tau.BookIV.Physics.tick_sector_consistent_with_invariant
(t : TickKind)
 :t.measuredInvariant.sector = t.sector**


The tick-sector assignment is consistent with the invariant-sector assignment.

---

### `Tau.BookIV.Physics.identity_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L159-L161)
**theorem
Tau.BookIV.Physics.identity_count
(k : TickKind)
 :(TickMorphism.identity k).count = 0**


Identity ticks have count zero.

---

### `Tau.BookIV.Physics.compose_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L163-L165)
**theorem
Tau.BookIV.Physics.compose_count
(a b : TickMorphism)

(h : a.kind = b.kind)
 :(a.compose b h).count = a.count + b.count**


Composition is additive in tick count.

---

### `Tau.BookIV.Physics.InternalRatio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L171-L185)
**structure
Tau.BookIV.Physics.InternalRatio :Type**


An internal ratio between two tick counts of possibly different kinds.
This represents a dimensionless quantity within Layer 1.
Example: the mass ratio R₀ is an internal ratio between η-step counts.

- num_kind : TickKind
Numerator tick kind.

- num_count : ℕ
Numerator tick count.

- den_kind : TickKind
Denominator tick kind.

- den_count : ℕ
Denominator tick count.

- den_pos : self.den_count > 0
Denominator is positive.

Instances For

---

### `Tau.BookIV.Physics.instReprInternalRatio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L185-L185)
**instance
Tau.BookIV.Physics.instReprInternalRatio :Repr InternalRatio**

Equations
- Tau.BookIV.Physics.instReprInternalRatio = { reprPrec := Tau.BookIV.Physics.instReprInternalRatio.repr }

---

### `Tau.BookIV.Physics.instReprInternalRatio.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L185-L185)
**def
Tau.BookIV.Physics.instReprInternalRatio.repr :InternalRatio → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.InternalRatio.isDimensionless`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/TickUnits.lean#L187-L189)
**def
Tau.BookIV.Physics.InternalRatio.isDimensionless
(r : InternalRatio)
 :Prop**


An internal ratio is dimensionless when both ticks are of the same kind.
Equations
- r.isDimensionless = (r.num_kind = r.den_kind)
Instances For
