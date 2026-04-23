---
layout: taulib-doc
title: "TauLib.BookIV.Physics.DefectFunctional"
permalink: /verify/taulib/docs/book-iv-physics-defect-functional/
lane: verify
module_name: "TauLib.BookIV.Physics.DefectFunctional"
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

# TauLib.BookIV.Physics.DefectFunctional


The 4-component defect functional and fluid regime classification.

## Registry Cross-References


- [IV.D16] Defect Component — `DefectComponent`

- [IV.D17] Defect Tuple — `DefectTuple`

- [IV.D18] Fluid Regime — `FluidRegime`

- [IV.D19] Regime Signature — `RegimeSignature`


## Mathematical Content


### 4-Component Defect Functional


Every fluid state is classified by a 4-component defect tuple:


Component
Description
Computation


Mobility
Local transport capability
Adjacency-graph diffusion rate


Vorticity
Rotational signature (Kelvin)
∮ u·dl on boundary cycles


Compression
Volumetric density change
∇·u on clopen adjacency


Topological
Winding/defect count
Defects on clopen tower


All four are computed on **clopen adjacency graphs** WITHOUT importing the reals.

### 8 Fluid Regimes


The defect tuple's inequality pattern classifies 8 canonical fluid regimes:


Regime
Key Signature


Crystal
Periodic NF-code + arrested transport


Glass
Aperiodic + mobility < k_glass


Euler
Kelvin-invariant + defect-budget preserved (inviscid)


Navier-Stokes
Viscous shear-defect + dissipation normalizer


MHD
Coupled fluid+EM holonomy + frozen flux


Plasma
EM-active + boundary-obstruction transport


Superfluid
Quantized circulation (hard lattice)


Superconductor
EM-superfluid + quantized flux Φ_τ


## Ground Truth Sources


- fluid-condensed-matter.json: defect-functional-spectrum, defect-functionals

- fluid-condensed-matter.json: regime classification, tau-superfluidity


---

### `Tau.BookIV.Physics.DefectComponent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L56-L68)
**inductive
Tau.BookIV.Physics.DefectComponent :Type**


[IV.D16] The 4 canonical defect components.
These are the independent degrees of freedom in the defect functional,
computed on clopen adjacency graphs without importing the reals.

- Mobility : DefectComponent
Local transport capability (diffusion rate on adjacency graph).

- Vorticity : DefectComponent
Rotational motion signature (Kelvin-type circulation invariant).

- Compression : DefectComponent
Volumetric density change (∇·u incompressibility measure).

- Topological : DefectComponent
Winding/defect count on clopen tower (topological charge).

Instances For

---

### `Tau.BookIV.Physics.instReprDefectComponent.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L68-L68)
**def
Tau.BookIV.Physics.instReprDefectComponent.repr :DefectComponent → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instReprDefectComponent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L68-L68)
**instance
Tau.BookIV.Physics.instReprDefectComponent :Repr DefectComponent**

Equations
- Tau.BookIV.Physics.instReprDefectComponent = { reprPrec := Tau.BookIV.Physics.instReprDefectComponent.repr }

---

### `Tau.BookIV.Physics.instDecidableEqDefectComponent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L68-L68)
**instance
Tau.BookIV.Physics.instDecidableEqDefectComponent :DecidableEq DefectComponent**

Equations
- Tau.BookIV.Physics.instDecidableEqDefectComponent x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Physics.instBEqDefectComponent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L68-L68)
**instance
Tau.BookIV.Physics.instBEqDefectComponent :BEq DefectComponent**

Equations
- Tau.BookIV.Physics.instBEqDefectComponent = { beq := Tau.BookIV.Physics.instBEqDefectComponent.beq }

---

### `Tau.BookIV.Physics.instBEqDefectComponent.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L68-L68)
**def
Tau.BookIV.Physics.instBEqDefectComponent.beq :DefectComponent → DefectComponent → Bool**

Equations
- Tau.BookIV.Physics.instBEqDefectComponent.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Physics.instInhabitedDefectComponent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L68-L68)
**instance
Tau.BookIV.Physics.instInhabitedDefectComponent :Inhabited DefectComponent**

Equations
- Tau.BookIV.Physics.instInhabitedDefectComponent = { default := Tau.BookIV.Physics.instInhabitedDefectComponent.default }

---

### `Tau.BookIV.Physics.instInhabitedDefectComponent.default`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L68-L68)
**def
Tau.BookIV.Physics.instInhabitedDefectComponent.default :DefectComponent**

Equations
- Tau.BookIV.Physics.instInhabitedDefectComponent.default = Tau.BookIV.Physics.DefectComponent.Mobility
Instances For

---

### `Tau.BookIV.Physics.DefectTuple`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L74-L88)
**structure
Tau.BookIV.Physics.DefectTuple :Type**


[IV.D17] Defect tuple: the 4-component functional that classifies
fluid states and drives regularity.

All components are non-negative scaled integers (representing
defect magnitudes computed on finite clopen lattices).

- mobility : ℕ
Mobility defect value (scaled).

- vorticity : ℕ
Vorticity defect value (scaled).

- compression : ℕ
Compression defect value (scaled).

- topological : ℕ
Topological defect value (scaled).

Instances For

---

### `Tau.BookIV.Physics.instReprDefectTuple`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L88-L88)
**instance
Tau.BookIV.Physics.instReprDefectTuple :Repr DefectTuple**

Equations
- Tau.BookIV.Physics.instReprDefectTuple = { reprPrec := Tau.BookIV.Physics.instReprDefectTuple.repr }

---

### `Tau.BookIV.Physics.instReprDefectTuple.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L88-L88)
**def
Tau.BookIV.Physics.instReprDefectTuple.repr :DefectTuple → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instDecidableEqDefectTuple`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L88-L88)
**instance
Tau.BookIV.Physics.instDecidableEqDefectTuple :DecidableEq DefectTuple**

Equations
- Tau.BookIV.Physics.instDecidableEqDefectTuple = Tau.BookIV.Physics.instDecidableEqDefectTuple.decEq

---

### `Tau.BookIV.Physics.instDecidableEqDefectTuple.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L88-L88)
**def
Tau.BookIV.Physics.instDecidableEqDefectTuple.decEq
(x✝ x✝¹ : DefectTuple)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instBEqDefectTuple.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L88-L88)
**def
Tau.BookIV.Physics.instBEqDefectTuple.beq :DefectTuple → DefectTuple → Bool**

Equations
- One or more equations did not get rendered due to their size.
- Tau.BookIV.Physics.instBEqDefectTuple.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIV.Physics.instBEqDefectTuple`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L88-L88)
**instance
Tau.BookIV.Physics.instBEqDefectTuple :BEq DefectTuple**

Equations
- Tau.BookIV.Physics.instBEqDefectTuple = { beq := Tau.BookIV.Physics.instBEqDefectTuple.beq }

---

### `Tau.BookIV.Physics.DefectTuple.total`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L90-L92)
**def
Tau.BookIV.Physics.DefectTuple.total
(d : DefectTuple)
 :ℕ**


Total defect budget: sum of all 4 components.
Equations
- d.total = d.mobility + d.vorticity + d.compression + d.topological
Instances For

---

### `Tau.BookIV.Physics.FluidRegime`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L98-L128)
**inductive
Tau.BookIV.Physics.FluidRegime :Type**


[IV.D18] The 8 canonical fluid regimes, classified by
defect-tuple inequality patterns.

Each regime is a τ-native formulation of a classical fluid type,
defined WITHOUT importing the reals.

- Crystal : FluidRegime
Periodic NF-code + arrested transport.
Physical: crystalline solid with periodic lattice.

- Glass : FluidRegime
Aperiodic NF-code + mobility below glass threshold k_glass.
Physical: amorphous solid (thermal aging).

- Euler : FluidRegime
Kelvin-invariant + defect-budget preserved (inviscid).
Physical: ideal fluid with circulation conservation.

- NavierStokes : FluidRegime
Viscous shear-defect dominant + dissipation normalizer.
Physical: viscous fluid with energy dissipation.

- MHD : FluidRegime
Coupled fluid + EM holonomy with frozen-flux axiom.
Physical: magnetohydrodynamic flow (Alfvén modes).

- Plasma : FluidRegime
EM-active fluid with boundary-obstruction transport.
Physical: ionized gas with Debye screening.

- Superfluid : FluidRegime
Quantized circulation constraint (hard lattice on plaquettes).
Physical: superfluid with protected vortex defects.

- Superconductor : FluidRegime
EM-superfluid with quantized flux Φ_τ.
Physical: superconductor (Meissner effect, Abrikosov vortices).

Instances For

---

### `Tau.BookIV.Physics.instReprFluidRegime`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L128-L128)
**instance
Tau.BookIV.Physics.instReprFluidRegime :Repr FluidRegime**

Equations
- Tau.BookIV.Physics.instReprFluidRegime = { reprPrec := Tau.BookIV.Physics.instReprFluidRegime.repr }

---

### `Tau.BookIV.Physics.instReprFluidRegime.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L128-L128)
**def
Tau.BookIV.Physics.instReprFluidRegime.repr :FluidRegime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instDecidableEqFluidRegime`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L128-L128)
**instance
Tau.BookIV.Physics.instDecidableEqFluidRegime :DecidableEq FluidRegime**

Equations
- Tau.BookIV.Physics.instDecidableEqFluidRegime x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Physics.instBEqFluidRegime`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L128-L128)
**instance
Tau.BookIV.Physics.instBEqFluidRegime :BEq FluidRegime**

Equations
- Tau.BookIV.Physics.instBEqFluidRegime = { beq := Tau.BookIV.Physics.instBEqFluidRegime.beq }

---

### `Tau.BookIV.Physics.instBEqFluidRegime.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L128-L128)
**def
Tau.BookIV.Physics.instBEqFluidRegime.beq :FluidRegime → FluidRegime → Bool**

Equations
- Tau.BookIV.Physics.instBEqFluidRegime.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Physics.instInhabitedFluidRegime`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L128-L128)
**instance
Tau.BookIV.Physics.instInhabitedFluidRegime :Inhabited FluidRegime**

Equations
- Tau.BookIV.Physics.instInhabitedFluidRegime = { default := Tau.BookIV.Physics.instInhabitedFluidRegime.default }

---

### `Tau.BookIV.Physics.instInhabitedFluidRegime.default`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L128-L128)
**def
Tau.BookIV.Physics.instInhabitedFluidRegime.default :FluidRegime**

Equations
- Tau.BookIV.Physics.instInhabitedFluidRegime.default = Tau.BookIV.Physics.FluidRegime.Crystal
Instances For

---

### `Tau.BookIV.Physics.RegimeSignature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L134-L154)
**structure
Tau.BookIV.Physics.RegimeSignature :Type**


[IV.D19] Regime signature: the structural properties that
distinguish each fluid regime.

Each regime is characterized by a combination of boolean flags
and optional bounds on defect components.

- regime : FluidRegime
Which regime this signature describes.

- mobility_bound : Option ℕ
Upper bound on mobility (Some k = mobility ≤ k, None = no bound).

- kelvin_invariant : Bool
Whether Kelvin circulation invariant holds (∮ u·dl conserved).

- dissipation : Bool
Whether energy dissipation is present.

- em_coupled : Bool
Whether coupled to EM holonomy sector.

- quantized_circulation : Bool
Whether circulation is quantized (hard lattice constraint).

- incompressible : Bool
Whether compression defect must vanish (incompressibility).

Instances For

---

### `Tau.BookIV.Physics.instReprRegimeSignature.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L154-L154)
**def
Tau.BookIV.Physics.instReprRegimeSignature.repr :RegimeSignature → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instReprRegimeSignature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L154-L154)
**instance
Tau.BookIV.Physics.instReprRegimeSignature :Repr RegimeSignature**

Equations
- Tau.BookIV.Physics.instReprRegimeSignature = { reprPrec := Tau.BookIV.Physics.instReprRegimeSignature.repr }

---

### `Tau.BookIV.Physics.crystal_signature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L160-L168)
**def
Tau.BookIV.Physics.crystal_signature :RegimeSignature**


Crystal regime signature: arrested, no circulation, no dissipation.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.glass_signature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L170-L178)
**def
Tau.BookIV.Physics.glass_signature :RegimeSignature**


Glass regime signature: arrested below threshold, aperiodic.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.euler_signature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L180-L188)
**def
Tau.BookIV.Physics.euler_signature :RegimeSignature**


Euler regime: inviscid, Kelvin-invariant, budget-preserving.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.ns_signature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L190-L198)
**def
Tau.BookIV.Physics.ns_signature :RegimeSignature**


Navier-Stokes regime: viscous, dissipative.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.mhd_signature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L200-L208)
**def
Tau.BookIV.Physics.mhd_signature :RegimeSignature**


MHD regime: coupled fluid+EM, frozen flux.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.plasma_signature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L210-L218)
**def
Tau.BookIV.Physics.plasma_signature :RegimeSignature**


Plasma regime: EM-active, mobile charges.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.superfluid_signature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L220-L228)
**def
Tau.BookIV.Physics.superfluid_signature :RegimeSignature**


Superfluid regime: quantized circulation, dissipation gap.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.superconductor_signature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L230-L238)
**def
Tau.BookIV.Physics.superconductor_signature :RegimeSignature**


Superconductor regime: EM-superfluid, quantized flux.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.all_regime_signatures`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L240-L243)
**def
Tau.BookIV.Physics.all_regime_signatures :List RegimeSignature**


All 8 canonical regime signatures.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.regime_signature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L245-L255)
**def
Tau.BookIV.Physics.regime_signature
(r : FluidRegime)
 :RegimeSignature**


Regime signature lookup.
Equations
- Tau.BookIV.Physics.regime_signature Tau.BookIV.Physics.FluidRegime.Crystal = Tau.BookIV.Physics.crystal_signature
- Tau.BookIV.Physics.regime_signature Tau.BookIV.Physics.FluidRegime.Glass = Tau.BookIV.Physics.glass_signature
- Tau.BookIV.Physics.regime_signature Tau.BookIV.Physics.FluidRegime.Euler = Tau.BookIV.Physics.euler_signature
- Tau.BookIV.Physics.regime_signature Tau.BookIV.Physics.FluidRegime.NavierStokes = Tau.BookIV.Physics.ns_signature
- Tau.BookIV.Physics.regime_signature Tau.BookIV.Physics.FluidRegime.MHD = Tau.BookIV.Physics.mhd_signature
- Tau.BookIV.Physics.regime_signature Tau.BookIV.Physics.FluidRegime.Plasma = Tau.BookIV.Physics.plasma_signature
- Tau.BookIV.Physics.regime_signature Tau.BookIV.Physics.FluidRegime.Superfluid = Tau.BookIV.Physics.superfluid_signature
- Tau.BookIV.Physics.regime_signature Tau.BookIV.Physics.FluidRegime.Superconductor = Tau.BookIV.Physics.superconductor_signature
Instances For

---

### `Tau.BookIV.Physics.four_components_exhaust`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L261-L264)
**theorem
Tau.BookIV.Physics.four_components_exhaust
(c : DefectComponent)
 :c = DefectComponent.Mobility ∨ c = DefectComponent.Vorticity ∨ c = DefectComponent.Compression ∨ c = DefectComponent.Topological**


Exactly 4 defect components.

---

### `Tau.BookIV.Physics.eight_regimes_exhaust`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L266-L270)
**theorem
Tau.BookIV.Physics.eight_regimes_exhaust
(r : FluidRegime)
 :r = FluidRegime.Crystal ∨ r = FluidRegime.Glass ∨ r = FluidRegime.Euler ∨ r = FluidRegime.NavierStokes ∨ r = FluidRegime.MHD ∨ r = FluidRegime.Plasma ∨ r = FluidRegime.Superfluid ∨ r = FluidRegime.Superconductor**


Exactly 8 fluid regimes.

---

### `Tau.BookIV.Physics.euler_no_dissipation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L272-L274)
**theorem
Tau.BookIV.Physics.euler_no_dissipation :(regime_signature FluidRegime.Euler).dissipation = false**


Euler regime has no dissipation (inviscid).

---

### `Tau.BookIV.Physics.euler_kelvin_invariant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L276-L278)
**theorem
Tau.BookIV.Physics.euler_kelvin_invariant :(regime_signature FluidRegime.Euler).kelvin_invariant = true**


Euler regime preserves Kelvin circulation invariant.

---

### `Tau.BookIV.Physics.ns_has_dissipation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L280-L282)
**theorem
Tau.BookIV.Physics.ns_has_dissipation :(regime_signature FluidRegime.NavierStokes).dissipation = true**


Navier-Stokes regime has dissipation.

---

### `Tau.BookIV.Physics.superfluid_quantized`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L284-L286)
**theorem
Tau.BookIV.Physics.superfluid_quantized :(regime_signature FluidRegime.Superfluid).quantized_circulation = true**


Superfluid has quantized circulation.

---

### `Tau.BookIV.Physics.superfluid_no_dissipation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L288-L290)
**theorem
Tau.BookIV.Physics.superfluid_no_dissipation :(regime_signature FluidRegime.Superfluid).dissipation = false**


Superfluid has no dissipation (dissipation gap).

---

### `Tau.BookIV.Physics.superconductor_em_coupled`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L292-L294)
**theorem
Tau.BookIV.Physics.superconductor_em_coupled :(regime_signature FluidRegime.Superconductor).em_coupled = true**


Superconductor is EM-coupled (Meissner effect).

---

### `Tau.BookIV.Physics.crystal_arrested`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L296-L298)
**theorem
Tau.BookIV.Physics.crystal_arrested :(regime_signature FluidRegime.Crystal).mobility_bound = some 0**


Crystal regime has arrested transport (mobility bound = 0).

---

### `Tau.BookIV.Physics.mhd_em_coupled`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L300-L302)
**theorem
Tau.BookIV.Physics.mhd_em_coupled :(regime_signature FluidRegime.MHD).em_coupled = true**


MHD is EM-coupled (frozen flux).

---

### `Tau.BookIV.Physics.defect_total_sum`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L304-L306)
**theorem
Tau.BookIV.Physics.defect_total_sum
(d : DefectTuple)
 :d.total = d.mobility + d.vorticity + d.compression + d.topological**


Defect tuple total is sum of all components.

---

### `Tau.BookIV.Physics.all_signatures_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/DefectFunctional.lean#L308-L309)
**theorem
Tau.BookIV.Physics.all_signatures_count :all_regime_signatures.length = 8**


All 8 regime signatures are present.
