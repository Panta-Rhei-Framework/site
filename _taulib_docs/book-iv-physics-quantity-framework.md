---
layout: taulib-doc
title: "TauLib.BookIV.Physics.QuantityFramework"
permalink: /verify/taulib/docs/book-iv-physics-quantity-framework/
lane: verify
module_name: "TauLib.BookIV.Physics.QuantityFramework"
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

# TauLib.BookIV.Physics.QuantityFramework


Core structural types for τ-native physical quantities: the 5 primary
physical invariants, carrier types, and particle ontology.

## Registry Cross-References


- [IV.D09] Primary Invariant — `PrimaryInvariant`

- [IV.D10] Carrier Type — `CarrierType`

- [IV.D11] Physical Quantity Template — `PhysicalQuantity`

- [IV.D12] Particle Kind — `ParticleKind`


## Mathematical Content


The τ-framework replaces orthodox physics' independent postulated quantities
with **coherence invariants of defect dynamics** on τ¹ × T². Five primary
invariants exhaust the independent physical degrees of freedom:


Invariant
τ-Definition
Carrier


Entropy
Coherence defect novelty measure (S_def + S_ref)
Crossing


Time
Defect novelty event sequence parameter (ρ-iteration)
Base τ¹


Energy
Coherence cost of maintaining localized defect bundle
Fiber T²


Mass
Inertial invariant of persistent T² defect bundle
Fiber T²


Gravity
Frame holonomy sector coupling (GR sector)
Base τ¹


All five are determined by ι<sub>τ</sub> = 2/(π+e) via sector lift functors.

## Ground Truth Sources


- particle-physics-defects.json: five-physical-invariants

- quantum-mechanics.json: sector lift functors

- holonomy-sectors.json: sector-carrier correspondence


---

### `Tau.BookIV.Physics.PrimaryInvariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L47-L66)
**inductive
Tau.BookIV.Physics.PrimaryInvariant :Type**


[IV.D09] The 5 primary physical invariants of the τ-framework.
These exhaust the independent physical degrees of freedom;
all other physical quantities are derived from these five.

- Entropy : PrimaryInvariant
Coherence defect novelty measure: S = S_def + S_ref.
S_def → 0 at coherence horizon; S_ref unbounded.

- Time : PrimaryInvariant
Defect novelty event sequence parameter (ρ-iteration depth).
Time emerges from defect dynamics ordering, NOT from spacetime.

- Energy : PrimaryInvariant
Coherence cost of maintaining localized defect bundle structure.
Energy ∝ defect-tuple magnitude & stability degree.

- Mass : PrimaryInvariant
Inertial invariant of persistent T² defect bundle.
Mass = boundary-fixed-point of defect bundle's coherence functional.

- Gravity : PrimaryInvariant
Frame holonomy sector coupling (GR sector).
Curvature = holonomy defect on frame transport.

Instances For

---

### `Tau.BookIV.Physics.instReprPrimaryInvariant.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L66-L66)
**def
Tau.BookIV.Physics.instReprPrimaryInvariant.repr :PrimaryInvariant → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instReprPrimaryInvariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L66-L66)
**instance
Tau.BookIV.Physics.instReprPrimaryInvariant :Repr PrimaryInvariant**

Equations
- Tau.BookIV.Physics.instReprPrimaryInvariant = { reprPrec := Tau.BookIV.Physics.instReprPrimaryInvariant.repr }

---

### `Tau.BookIV.Physics.instDecidableEqPrimaryInvariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L66-L66)
**instance
Tau.BookIV.Physics.instDecidableEqPrimaryInvariant :DecidableEq PrimaryInvariant**

Equations
- Tau.BookIV.Physics.instDecidableEqPrimaryInvariant x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Physics.instBEqPrimaryInvariant.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L66-L66)
**def
Tau.BookIV.Physics.instBEqPrimaryInvariant.beq :PrimaryInvariant → PrimaryInvariant → Bool**

Equations
- Tau.BookIV.Physics.instBEqPrimaryInvariant.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Physics.instBEqPrimaryInvariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L66-L66)
**instance
Tau.BookIV.Physics.instBEqPrimaryInvariant :BEq PrimaryInvariant**

Equations
- Tau.BookIV.Physics.instBEqPrimaryInvariant = { beq := Tau.BookIV.Physics.instBEqPrimaryInvariant.beq }

---

### `Tau.BookIV.Physics.instInhabitedPrimaryInvariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L66-L66)
**instance
Tau.BookIV.Physics.instInhabitedPrimaryInvariant :Inhabited PrimaryInvariant**

Equations
- Tau.BookIV.Physics.instInhabitedPrimaryInvariant = { default := Tau.BookIV.Physics.instInhabitedPrimaryInvariant.default }

---

### `Tau.BookIV.Physics.instInhabitedPrimaryInvariant.default`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L66-L66)
**def
Tau.BookIV.Physics.instInhabitedPrimaryInvariant.default :PrimaryInvariant**

Equations
- Tau.BookIV.Physics.instInhabitedPrimaryInvariant.default = Tau.BookIV.Physics.PrimaryInvariant.Entropy
Instances For

---

### `Tau.BookIV.Physics.CarrierType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L72-L81)
**inductive
Tau.BookIV.Physics.CarrierType :Type**


[IV.D10] Carrier type for physical quantities in the τ³ = τ¹ ×_f T² fibration.
Every physical quantity lives on exactly one of three carriers.

- Fiber : CarrierType
Lives on the fiber T² (spatial/microcosm = Book IV).

- Base : CarrierType
Lives on the base τ¹ (temporal/macrocosm = Book V).

- Crossing : CarrierType
Lives at the lemniscate crossing point L = S¹ ∨ S¹ (unpolarized).

Instances For

---

### `Tau.BookIV.Physics.instReprCarrierType.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L81-L81)
**def
Tau.BookIV.Physics.instReprCarrierType.repr :CarrierType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instReprCarrierType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L81-L81)
**instance
Tau.BookIV.Physics.instReprCarrierType :Repr CarrierType**

Equations
- Tau.BookIV.Physics.instReprCarrierType = { reprPrec := Tau.BookIV.Physics.instReprCarrierType.repr }

---

### `Tau.BookIV.Physics.instDecidableEqCarrierType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L81-L81)
**instance
Tau.BookIV.Physics.instDecidableEqCarrierType :DecidableEq CarrierType**

Equations
- Tau.BookIV.Physics.instDecidableEqCarrierType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Physics.instBEqCarrierType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L81-L81)
**instance
Tau.BookIV.Physics.instBEqCarrierType :BEq CarrierType**

Equations
- Tau.BookIV.Physics.instBEqCarrierType = { beq := Tau.BookIV.Physics.instBEqCarrierType.beq }

---

### `Tau.BookIV.Physics.instBEqCarrierType.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L81-L81)
**def
Tau.BookIV.Physics.instBEqCarrierType.beq :CarrierType → CarrierType → Bool**

Equations
- Tau.BookIV.Physics.instBEqCarrierType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Physics.instInhabitedCarrierType.default`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L81-L81)
**def
Tau.BookIV.Physics.instInhabitedCarrierType.default :CarrierType**

Equations
- Tau.BookIV.Physics.instInhabitedCarrierType.default = Tau.BookIV.Physics.CarrierType.Fiber
Instances For

---

### `Tau.BookIV.Physics.instInhabitedCarrierType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L81-L81)
**instance
Tau.BookIV.Physics.instInhabitedCarrierType :Inhabited CarrierType**

Equations
- Tau.BookIV.Physics.instInhabitedCarrierType = { default := Tau.BookIV.Physics.instInhabitedCarrierType.default }

---

### `Tau.BookIV.Physics.PhysicalQuantity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L87-L103)
**structure
Tau.BookIV.Physics.PhysicalQuantity :Type**


[IV.D11] Physical quantity template: a τ-native physical observable
characterized by its primary invariant, carrier, governing sector,
and structural properties.

- name : String
Display name.

- invariant : PrimaryInvariant
Which primary invariant this quantity belongs to.

- carrier : CarrierType
Where the quantity lives in τ³.

- sector : BookIII.Sectors.Sector
Which holonomy sector governs this quantity.

- is_sigma_fixed : Bool
Whether the quantity is σ-fixed (unpolarized, at crossing point).

- is_conserved : Bool
Whether the quantity is conserved under τ-admissible evolution.

Instances For

---

### `Tau.BookIV.Physics.instReprPhysicalQuantity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L103-L103)
**instance
Tau.BookIV.Physics.instReprPhysicalQuantity :Repr PhysicalQuantity**

Equations
- Tau.BookIV.Physics.instReprPhysicalQuantity = { reprPrec := Tau.BookIV.Physics.instReprPhysicalQuantity.repr }

---

### `Tau.BookIV.Physics.instReprPhysicalQuantity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L103-L103)
**def
Tau.BookIV.Physics.instReprPhysicalQuantity.repr :PhysicalQuantity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.ParticleKind`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L109-L121)
**inductive
Tau.BookIV.Physics.ParticleKind :Type**


[IV.D12] Particle classification in the τ-framework.
The τ-kernel distinguishes three kinds of carriers.

- Ontic : ParticleKind
Persistent localized defect bundle with stable T² fiber.
Example: neutron (first ontic particle = minimal mass-bearing config).

- Radiation : ParticleKind
Null transport along τ¹ with degenerate S¹ fiber (not T²).
Example: photon (null transport with degenerate circular fiber).

- Virtual : ParticleKind
Intermediate exchange carrier (not persistent).
Example: virtual photon in Feynman diagrams.

Instances For

---

### `Tau.BookIV.Physics.instReprParticleKind`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L121-L121)
**instance
Tau.BookIV.Physics.instReprParticleKind :Repr ParticleKind**

Equations
- Tau.BookIV.Physics.instReprParticleKind = { reprPrec := Tau.BookIV.Physics.instReprParticleKind.repr }

---

### `Tau.BookIV.Physics.instReprParticleKind.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L121-L121)
**def
Tau.BookIV.Physics.instReprParticleKind.repr :ParticleKind → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instDecidableEqParticleKind`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L121-L121)
**instance
Tau.BookIV.Physics.instDecidableEqParticleKind :DecidableEq ParticleKind**

Equations
- Tau.BookIV.Physics.instDecidableEqParticleKind x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Physics.instBEqParticleKind.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L121-L121)
**def
Tau.BookIV.Physics.instBEqParticleKind.beq :ParticleKind → ParticleKind → Bool**

Equations
- Tau.BookIV.Physics.instBEqParticleKind.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Physics.instBEqParticleKind`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L121-L121)
**instance
Tau.BookIV.Physics.instBEqParticleKind :BEq ParticleKind**

Equations
- Tau.BookIV.Physics.instBEqParticleKind = { beq := Tau.BookIV.Physics.instBEqParticleKind.beq }

---

### `Tau.BookIV.Physics.instInhabitedParticleKind.default`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L121-L121)
**def
Tau.BookIV.Physics.instInhabitedParticleKind.default :ParticleKind**

Equations
- Tau.BookIV.Physics.instInhabitedParticleKind.default = Tau.BookIV.Physics.ParticleKind.Ontic
Instances For

---

### `Tau.BookIV.Physics.instInhabitedParticleKind`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L121-L121)
**instance
Tau.BookIV.Physics.instInhabitedParticleKind :Inhabited ParticleKind**

Equations
- Tau.BookIV.Physics.instInhabitedParticleKind = { default := Tau.BookIV.Physics.instInhabitedParticleKind.default }

---

### `Tau.BookIV.Physics.PrimaryInvariant.carrier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L127-L133)
**def
Tau.BookIV.Physics.PrimaryInvariant.carrier :PrimaryInvariant → CarrierType**


Canonical carrier assignment for each primary invariant.
Equations
- Tau.BookIV.Physics.PrimaryInvariant.Entropy.carrier = Tau.BookIV.Physics.CarrierType.Crossing
- Tau.BookIV.Physics.PrimaryInvariant.Time.carrier = Tau.BookIV.Physics.CarrierType.Base
- Tau.BookIV.Physics.PrimaryInvariant.Energy.carrier = Tau.BookIV.Physics.CarrierType.Fiber
- Tau.BookIV.Physics.PrimaryInvariant.Mass.carrier = Tau.BookIV.Physics.CarrierType.Fiber
- Tau.BookIV.Physics.PrimaryInvariant.Gravity.carrier = Tau.BookIV.Physics.CarrierType.Base
Instances For

---

### `Tau.BookIV.Physics.PrimaryInvariant.sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L135-L141)
**def
Tau.BookIV.Physics.PrimaryInvariant.sector :PrimaryInvariant → BookIII.Sectors.Sector**


Canonical sector assignment for each primary invariant.
Equations
- Tau.BookIV.Physics.PrimaryInvariant.Entropy.sector = Tau.BookIII.Sectors.Sector.Omega
- Tau.BookIV.Physics.PrimaryInvariant.Time.sector = Tau.BookIII.Sectors.Sector.A
- Tau.BookIV.Physics.PrimaryInvariant.Energy.sector = Tau.BookIII.Sectors.Sector.B
- Tau.BookIV.Physics.PrimaryInvariant.Mass.sector = Tau.BookIII.Sectors.Sector.C
- Tau.BookIV.Physics.PrimaryInvariant.Gravity.sector = Tau.BookIII.Sectors.Sector.D
Instances For

---

### `Tau.BookIV.Physics.entropy_quantity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L147-L154)
**def
Tau.BookIV.Physics.entropy_quantity :PhysicalQuantity**


Entropy as physical quantity.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.time_quantity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L156-L163)
**def
Tau.BookIV.Physics.time_quantity :PhysicalQuantity**


Time as physical quantity.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.energy_quantity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L165-L172)
**def
Tau.BookIV.Physics.energy_quantity :PhysicalQuantity**


Energy as physical quantity.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.mass_quantity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L174-L181)
**def
Tau.BookIV.Physics.mass_quantity :PhysicalQuantity**


Mass as physical quantity.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.gravity_quantity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L183-L190)
**def
Tau.BookIV.Physics.gravity_quantity :PhysicalQuantity**


Gravity as physical quantity.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.all_quantities`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L192-L194)
**def
Tau.BookIV.Physics.all_quantities :List PhysicalQuantity**


All 5 canonical physical quantities.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.five_invariants_exhaust`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L200-L203)
**theorem
Tau.BookIV.Physics.five_invariants_exhaust
(p : PrimaryInvariant)
 :p = PrimaryInvariant.Entropy ∨ p = PrimaryInvariant.Time ∨ p = PrimaryInvariant.Energy ∨ p = PrimaryInvariant.Mass ∨ p = PrimaryInvariant.Gravity**


Exactly 5 primary invariants.

---

### `Tau.BookIV.Physics.three_carriers_exhaust`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L205-L208)
**theorem
Tau.BookIV.Physics.three_carriers_exhaust
(c : CarrierType)
 :c = CarrierType.Fiber ∨ c = CarrierType.Base ∨ c = CarrierType.Crossing**


Exactly 3 carrier types.

---

### `Tau.BookIV.Physics.three_particle_kinds`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L210-L213)
**theorem
Tau.BookIV.Physics.three_particle_kinds
(k : ParticleKind)
 :k = ParticleKind.Ontic ∨ k = ParticleKind.Radiation ∨ k = ParticleKind.Virtual**


Exactly 3 particle kinds.

---

### `Tau.BookIV.Physics.gravity_unique_sigma_fixed_base`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L215-L221)
**theorem
Tau.BookIV.Physics.gravity_unique_sigma_fixed_base :gravity_quantity.carrier = CarrierType.Base ∧ gravity_quantity.is_sigma_fixed = true ∧ time_quantity.is_sigma_fixed = false**


Gravity is the unique base-carrier primary invariant
among those with σ-fixed property.

---

### `Tau.BookIV.Physics.energy_mass_fiber`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L223-L226)
**theorem
Tau.BookIV.Physics.energy_mass_fiber :energy_quantity.carrier = CarrierType.Fiber ∧ mass_quantity.carrier = CarrierType.Fiber**


Energy and Mass both live on the fiber T².

---

### `Tau.BookIV.Physics.all_quantities_distinct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L228-L240)
**theorem
Tau.BookIV.Physics.all_quantities_distinct :entropy_quantity.invariant ≠ time_quantity.invariant ∧ entropy_quantity.invariant ≠ energy_quantity.invariant ∧ entropy_quantity.invariant ≠ mass_quantity.invariant ∧ entropy_quantity.invariant ≠ gravity_quantity.invariant ∧ time_quantity.invariant ≠ energy_quantity.invariant ∧ time_quantity.invariant ≠ mass_quantity.invariant ∧ time_quantity.invariant ≠ gravity_quantity.invariant ∧ energy_quantity.invariant ≠ mass_quantity.invariant ∧ energy_quantity.invariant ≠ gravity_quantity.invariant ∧ mass_quantity.invariant ≠ gravity_quantity.invariant**


All 5 canonical quantities use distinct primary invariants.

---

### `Tau.BookIV.Physics.InternalQuantity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L256-L279)
**structure
Tau.BookIV.Physics.InternalQuantity :Type**


[IV.D321a] An internal quantity as a categorical object.
Each quantity IS its generator action — a functor from a sector
subcategory of τ³ to its internal hom. This replaces the metadata-level
PhysicalQuantity with a definitional categorical characterization.

The `generator` field names the τ-generator whose minimal endomorphism
defines this quantity. The `carrier_space` identifies whether the
endomorphism acts on base τ¹, fiber T², or the crossing L.

- invariant : PrimaryInvariant
The primary invariant this quantity instantiates.

- generator : String
The τ-generator whose action defines this quantity.
α=gravity, π=time, γ=energy, η=mass, ω=entropy.

- endomorphism_type : String
Where the generator acts: "End(τ¹)" for base, "End(T²)" for fiber,
"Aut(L)" for crossing.

- sector : BookIII.Sectors.Sector
Governing sector.

- carrier : CarrierType
Carrier type.

- is_conserved : Bool
Whether the quantity is conserved.

Instances For

---

### `Tau.BookIV.Physics.instReprInternalQuantity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L279-L279)
**def
Tau.BookIV.Physics.instReprInternalQuantity.repr :InternalQuantity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instReprInternalQuantity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L279-L279)
**instance
Tau.BookIV.Physics.instReprInternalQuantity :Repr InternalQuantity**

Equations
- Tau.BookIV.Physics.instReprInternalQuantity = { reprPrec := Tau.BookIV.Physics.instReprInternalQuantity.repr }

---

### `Tau.BookIV.Physics.time_internal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L281-L288)
**def
Tau.BookIV.Physics.time_internal :InternalQuantity**


Time as generator action: π-endomorphism of base τ¹.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.energy_internal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L290-L297)
**def
Tau.BookIV.Physics.energy_internal :InternalQuantity**


Energy as generator action: γ-endomorphism of fiber T².
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.mass_internal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L299-L306)
**def
Tau.BookIV.Physics.mass_internal :InternalQuantity**


Mass as generator action: η-fixed point on fiber T².
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.gravity_internal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L308-L315)
**def
Tau.BookIV.Physics.gravity_internal :InternalQuantity**


Gravity as generator action: α-endomorphism of base τ¹.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.entropy_internal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L317-L324)
**def
Tau.BookIV.Physics.entropy_internal :InternalQuantity**


Entropy as generator action: ω-crossing automorphism of L.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.all_internal_quantities`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L326-L328)
**def
Tau.BookIV.Physics.all_internal_quantities :List InternalQuantity**


All 5 internal quantities.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.categorical_consistent_with_metadata`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L330-L338)
**theorem
Tau.BookIV.Physics.categorical_consistent_with_metadata :time_internal.sector = time_quantity.sector ∧ energy_internal.sector = energy_quantity.sector ∧ mass_internal.sector = mass_quantity.sector ∧ gravity_internal.sector = gravity_quantity.sector ∧ entropy_internal.sector = entropy_quantity.sector**


The categorical layer is consistent with the metadata layer:
same sector assignment for each invariant.

---

### `Tau.BookIV.Physics.internal_generators_distinct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/QuantityFramework.lean#L340-L352)
**theorem
Tau.BookIV.Physics.internal_generators_distinct :time_internal.generator ≠ energy_internal.generator ∧ time_internal.generator ≠ mass_internal.generator ∧ time_internal.generator ≠ gravity_internal.generator ∧ time_internal.generator ≠ entropy_internal.generator ∧ energy_internal.generator ≠ mass_internal.generator ∧ energy_internal.generator ≠ gravity_internal.generator ∧ energy_internal.generator ≠ entropy_internal.generator ∧ mass_internal.generator ≠ gravity_internal.generator ∧ mass_internal.generator ≠ entropy_internal.generator ∧ gravity_internal.generator ≠ entropy_internal.generator**


Each internal quantity has a distinct generator.
