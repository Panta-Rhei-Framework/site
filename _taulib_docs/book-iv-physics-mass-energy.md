---
layout: taulib-doc
title: "TauLib.BookIV.Physics.MassEnergy"
permalink: /verify/taulib/docs/book-iv-physics-mass-energy/
lane: verify
module_name: "TauLib.BookIV.Physics.MassEnergy"
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

# TauLib.BookIV.Physics.MassEnergy


Mass, energy, and the mass-energy structural relation in the τ-framework.

## Registry Cross-References


- [IV.D20] Mass Index — `MassIndex`

- [IV.D21] Energy Index — `EnergyIndex`

- [IV.D22] Speed Constant — `SpeedConstant`

- [IV.D23] Mass-Energy Relation — `MassEnergyRelation`

- [IV.R04] Neutron as first ontic particle — structural remark


## Mathematical Content


### Mass in the τ-Framework


Mass is the **inertial invariant of a persistent localized defect bundle**
with stable 2-torus T² fiber. It is NOT a postulated scalar but a
**boundary fixed-point** of the defect bundle's coherence functional:

```
M_n(x) := MassIdx(NF_ω(x))
```


= α-Idx readout from normal-form stabilized configuration.

The **neutron** is the first ontic particle (minimal mass-bearing
defect bundle in τ). Beta decay is the shedding of subsidiary defect modes.

### Energy in the τ-Framework


Energy is the **coherence cost of maintaining a localized defect bundle
structure**. It is proportional to the defect-tuple magnitude and
stability degree.

### Mass-Energy Relation


```
E = m_τ · c²_τ
```


where c_τ is the τ-derived speed-of-light constant. This relation
holds as a structural identity between the mass and energy indices.

### Particle Ontology


- **Ontic particles**: Persistent defect bundles with stable T² fiber (neutron, proton, ...)

- **Radiation**: Null transport with degenerate S¹ fiber (photon)

- **E = ℏω_τ**: Photon energy from transport frequency


## Ground Truth Sources


- particle-physics-defects.json: particle-ontology, mass definition

- quantum-mechanics.json: mass-energy equivalence

- gravity-einstein.json: BH mass index


---

### `Tau.BookIV.Physics.MassIndex`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L65-L86)
**structure
Tau.BookIV.Physics.MassIndex :Type**


[IV.D20] Mass index: the inertial invariant of a persistent
localized defect bundle.

Mass = boundary fixed-point of the defect bundle's coherence
functional = α-Idx readout from NF-stabilized configuration.

Properties:


- Not a primitive scalar but a resistance/scale index

- Comes with minimal carrier that can host it

- Monotone under admissible evolution (No-Shrink for BH)


- numer : ℕ
Mass value numerator (scaled).

- denom : ℕ
Mass value denominator.

- denom_pos : self.denom > 0
Denominator is positive.

- carrier : CarrierType
Carrier type (must be Fiber for ontic particles).

- is_persistent : Bool
Whether the defect bundle is persistent (stable T² fiber).

Instances For

---

### `Tau.BookIV.Physics.instReprMassIndex.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L86-L86)
**def
Tau.BookIV.Physics.instReprMassIndex.repr :MassIndex → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instReprMassIndex`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L86-L86)
**instance
Tau.BookIV.Physics.instReprMassIndex :Repr MassIndex**

Equations
- Tau.BookIV.Physics.instReprMassIndex = { reprPrec := Tau.BookIV.Physics.instReprMassIndex.repr }

---

### `Tau.BookIV.Physics.MassIndex.toFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L88-L90)
**def
Tau.BookIV.Physics.MassIndex.toFloat
(m : MassIndex)
 :Float**


Float display for mass index.
Equations
- m.toFloat = Float.ofNat m.numer / Float.ofNat m.denom
Instances For

---

### `Tau.BookIV.Physics.EnergyIndex`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L96-L110)
**structure
Tau.BookIV.Physics.EnergyIndex :Type**


[IV.D21] Energy index: the coherence cost of maintaining a
localized defect bundle structure.

Energy ∝ defect-tuple magnitude × stability degree.
Each sector provides its own excitation cost scale.

- numer : ℕ
Energy value numerator (scaled).

- denom : ℕ
Energy value denominator.

- denom_pos : self.denom > 0
Denominator is positive.

- sector : BookIII.Sectors.Sector
Which sector provides the excitation.

Instances For

---

### `Tau.BookIV.Physics.instReprEnergyIndex.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L110-L110)
**def
Tau.BookIV.Physics.instReprEnergyIndex.repr :EnergyIndex → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instReprEnergyIndex`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L110-L110)
**instance
Tau.BookIV.Physics.instReprEnergyIndex :Repr EnergyIndex**

Equations
- Tau.BookIV.Physics.instReprEnergyIndex = { reprPrec := Tau.BookIV.Physics.instReprEnergyIndex.repr }

---

### `Tau.BookIV.Physics.EnergyIndex.toFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L112-L114)
**def
Tau.BookIV.Physics.EnergyIndex.toFloat
(e : EnergyIndex)
 :Float**


Float display for energy index.
Equations
- e.toFloat = Float.ofNat e.numer / Float.ofNat e.denom
Instances For

---

### `Tau.BookIV.Physics.SpeedConstant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L120-L133)
**structure
Tau.BookIV.Physics.SpeedConstant :Type**


[IV.D22] Speed-of-light constant c²_τ: the τ-derived structural
constant relating mass and energy indices.

c²_τ is not postulated but earned from the τ-kernel as the
canonical conversion factor between defect-bundle mass indices
and coherence cost indices.

- c_sq_numer : ℕ
c² numerator (scaled).

- c_sq_denom : ℕ
c² denominator.

- denom_pos : self.c_sq_denom > 0
Denominator is positive.

Instances For

---

### `Tau.BookIV.Physics.instReprSpeedConstant.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L133-L133)
**def
Tau.BookIV.Physics.instReprSpeedConstant.repr :SpeedConstant → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instReprSpeedConstant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L133-L133)
**instance
Tau.BookIV.Physics.instReprSpeedConstant :Repr SpeedConstant**

Equations
- Tau.BookIV.Physics.instReprSpeedConstant = { reprPrec := Tau.BookIV.Physics.instReprSpeedConstant.repr }

---

### `Tau.BookIV.Physics.SpeedConstant.toFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L135-L137)
**def
Tau.BookIV.Physics.SpeedConstant.toFloat
(s : SpeedConstant)
 :Float**


Float display for speed constant.
Equations
- s.toFloat = Float.ofNat s.c_sq_numer / Float.ofNat s.c_sq_denom
Instances For

---

### `Tau.BookIV.Physics.MassEnergyRelation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L143-L162)
**structure
Tau.BookIV.Physics.MassEnergyRelation :Type**


[IV.D23] Mass-energy relation template: E = m · c²_τ.

This is a structural identity relating the mass index to the
energy index via the τ-derived speed constant. The relation
holds as a cross-multiplication equality on scaled rationals:

energy/1 = mass × c² means:
E_numer · m_denom · c_denom = m_numer · E_denom · c_numer

- mass : MassIndex
Mass index.

- energy : EnergyIndex
Energy index.

- speed : SpeedConstant
Speed constant c²_τ.

- relation : self.energy.numer * self.mass.denom * self.speed.c_sq_denom = self.mass.numer * self.energy.denom * self.speed.c_sq_numer
The structural identity: E = m · c².

Instances For

---

### `Tau.BookIV.Physics.instReprMassEnergyRelation.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L162-L162)
**def
Tau.BookIV.Physics.instReprMassEnergyRelation.repr :MassEnergyRelation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instReprMassEnergyRelation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L162-L162)
**instance
Tau.BookIV.Physics.instReprMassEnergyRelation :Repr MassEnergyRelation**

Equations
- Tau.BookIV.Physics.instReprMassEnergyRelation = { reprPrec := Tau.BookIV.Physics.instReprMassEnergyRelation.repr }

---

### `Tau.BookIV.Physics.OnticParticle`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L168-L176)
**structure
Tau.BookIV.Physics.OnticParticle :Type**


Ontic particles have fiber carrier (stable T² topology).

- mass : MassIndex
Mass of the particle.

- persistent_proof : self.mass.is_persistent = true
Ontic particles are persistent.

- fiber_proof : self.mass.carrier = CarrierType.Fiber
Ontic particles live on the fiber T².

Instances For

---

### `Tau.BookIV.Physics.instReprOnticParticle.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L176-L176)
**def
Tau.BookIV.Physics.instReprOnticParticle.repr :OnticParticle → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instReprOnticParticle`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L176-L176)
**instance
Tau.BookIV.Physics.instReprOnticParticle :Repr OnticParticle**

Equations
- Tau.BookIV.Physics.instReprOnticParticle = { reprPrec := Tau.BookIV.Physics.instReprOnticParticle.repr }

---

### `Tau.BookIV.Physics.RadiationCarrier`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L178-L184)
**structure
Tau.BookIV.Physics.RadiationCarrier :Type**


Radiation has degenerate fiber (S¹, not T²).

- energy : EnergyIndex
Energy of the radiation.

- sector_proof : self.energy.sector = BookIII.Sectors.Sector.B ∨ self.energy.sector = BookIII.Sectors.Sector.D
Which sector (typically EM for photon).

Instances For

---

### `Tau.BookIV.Physics.instReprRadiationCarrier.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L184-L184)
**def
Tau.BookIV.Physics.instReprRadiationCarrier.repr :RadiationCarrier → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instReprRadiationCarrier`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L184-L184)
**instance
Tau.BookIV.Physics.instReprRadiationCarrier :Repr RadiationCarrier**

Equations
- Tau.BookIV.Physics.instReprRadiationCarrier = { reprPrec := Tau.BookIV.Physics.instReprRadiationCarrier.repr }

---

### `Tau.BookIV.Physics.NeutronRole`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L190-L208)
**structure
Tau.BookIV.Physics.NeutronRole :Type**


[IV.R04] The neutron is the first ontic particle: the minimal
mass-bearing defect bundle in τ.

Properties:


- Toroidal defect bundle on τ¹ (the "micro-donut")

- Beta decay: neutron → proton + electron + ν_e
(shedding subsidiary defect modes)

- Stable in bound states; β-decay only when free


This structure records the neutron's structural role.
The numerical mass comes from the calibration cascade (Part VII).

- mass : MassIndex
Neutron mass index (first/minimal).

- is_ontic : self.mass.is_persistent = true ∧ self.mass.carrier = CarrierType.Fiber
The neutron is ontic (persistent T² fiber).

- mass_positive : self.mass.numer > 0
The neutron mass is positive.

Instances For

---

### `Tau.BookIV.Physics.instReprNeutronRole`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L208-L208)
**instance
Tau.BookIV.Physics.instReprNeutronRole :Repr NeutronRole**

Equations
- Tau.BookIV.Physics.instReprNeutronRole = { reprPrec := Tau.BookIV.Physics.instReprNeutronRole.repr }

---

### `Tau.BookIV.Physics.instReprNeutronRole.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L208-L208)
**def
Tau.BookIV.Physics.instReprNeutronRole.repr :NeutronRole → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.ontic_has_fiber`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L214-L216)
**theorem
Tau.BookIV.Physics.ontic_has_fiber
(p : OnticParticle)
 :p.mass.carrier = CarrierType.Fiber**


Ontic particles have Fiber carrier type.

---

### `Tau.BookIV.Physics.ontic_is_persistent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L218-L220)
**theorem
Tau.BookIV.Physics.ontic_is_persistent
(p : OnticParticle)
 :p.mass.is_persistent = true**


Ontic particles are persistent.

---

### `Tau.BookIV.Physics.mass_energy_positive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Physics/MassEnergy.lean#L222-L228)
**theorem
Tau.BookIV.Physics.mass_energy_positive
(r : MassEnergyRelation)

(hm : r.mass.numer > 0)

(hc : r.speed.c_sq_numer > 0)
 :r.energy.numer * r.mass.denom * r.speed.c_sq_denom > 0**


The mass-energy relation implies energy > 0 when mass > 0
and speed > 0 (structural).
