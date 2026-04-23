---
layout: taulib-doc
title: "TauLib.BookV.Astrophysics.CompactObjects"
permalink: /verify/taulib/docs/book-v-astrophysics-compact-objects/
lane: verify
module_name: "TauLib.BookV.Astrophysics.CompactObjects"
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

# TauLib.BookV.Astrophysics.CompactObjects


Neutron stars and white dwarfs from defect-bundle topology. TOV
solutions, maximum mass limits, and the connection to the coherence
horizon from the GravityField module.

## Registry Cross-References


- [V.D124] Compact Object Classification -- `CompactObjectType`

- [V.T86] White Dwarf Mass Limit -- `wd_mass_limit`

- [V.R177] Chandrasekhar from Electron Degeneracy -- structural remark

- [V.P71] Neutron Star EOS from Defect Bundle -- `ns_eos_from_defect`

- [V.T87] TOV Maximum Mass -- `tov_maximum_mass`

- [V.R178] Maximum Mass Observational Constraint -- structural remark

- [V.D125] Pulsar Data -- `PulsarData`

- [V.R179] Pulsar Timing as Precision Test -- structural remark

- [V.T88] Mass Gap Prediction -- `mass_gap_prediction`

- [V.P72] Magnetar from Defect Vortex -- `magnetar_from_vortex`

- [V.R180] No Naked Singularities -- structural remark


## Mathematical Content


### Compact Object Classification


Compact objects in the τ-framework are high-density defect bundles
with boundary topology constrained by:

- White dwarfs: electron degeneracy boundary (S² topology)

- Neutron stars: neutron degeneracy boundary (S² topology)

- Black holes: torus vacuum (T² topology, above coherence horizon)


### Mass Limits


- Chandrasekhar limit: M_Ch ≈ 1.4 M_☉ (white dwarf maximum)

- TOV maximum mass: M_TOV ≈ 2.1-2.5 M_☉ (neutron star maximum)

- Above M_TOV: topology crossing to T² (black hole formation)


### Mass Gap


The τ-framework predicts a mass gap between NS maximum (~2.5 M_☉)
and the lightest BH (~5 M_☉) because the topology crossing has a
finite defect cost barrier.

### Pulsars


Pulsars are rotating neutron stars whose beam emission is a
readout of the defect-bundle's rotational asymmetry. Millisecond
pulsars provide the most precise tests of τ-gravitational predictions.

## Ground Truth Sources


- Book V ch38: Compact Objects


---

### `Tau.BookV.Astrophysics.CompactObjectType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L64-L75)
**inductive
Tau.BookV.Astrophysics.CompactObjectType :Type**


[V.D124] Compact object type classification by defect-bundle
topology and degeneracy boundary.

- WhiteDwarf : CompactObjectType
White dwarf: electron degeneracy, S² topology.

- NeutronStar : CompactObjectType
Neutron star: neutron degeneracy, S² topology.

- BlackHole : CompactObjectType
Black hole: torus vacuum, T² topology.

- QuarkStar : CompactObjectType
Hypothetical quark star (not yet confirmed).

Instances For

---

### `Tau.BookV.Astrophysics.instReprCompactObjectType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L75-L75)
**instance
Tau.BookV.Astrophysics.instReprCompactObjectType :Repr CompactObjectType**

Equations
- Tau.BookV.Astrophysics.instReprCompactObjectType = { reprPrec := Tau.BookV.Astrophysics.instReprCompactObjectType.repr }

---

### `Tau.BookV.Astrophysics.instReprCompactObjectType.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L75-L75)
**def
Tau.BookV.Astrophysics.instReprCompactObjectType.repr :CompactObjectType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instDecidableEqCompactObjectType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L75-L75)
**instance
Tau.BookV.Astrophysics.instDecidableEqCompactObjectType :DecidableEq CompactObjectType**

Equations
- Tau.BookV.Astrophysics.instDecidableEqCompactObjectType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqCompactObjectType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L75-L75)
**instance
Tau.BookV.Astrophysics.instBEqCompactObjectType :BEq CompactObjectType**

Equations
- Tau.BookV.Astrophysics.instBEqCompactObjectType = { beq := Tau.BookV.Astrophysics.instBEqCompactObjectType.beq }

---

### `Tau.BookV.Astrophysics.instBEqCompactObjectType.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L75-L75)
**def
Tau.BookV.Astrophysics.instBEqCompactObjectType.beq :CompactObjectType → CompactObjectType → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqCompactObjectType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.CompactObjectData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L77-L91)
**structure
Tau.BookV.Astrophysics.CompactObjectData :Type**


Compact object data.

- obj_type : CompactObjectType
Object type.

- mass_tenth_solar : ℕ
Mass (scaled, 0.1 solar masses).

- mass_pos : self.mass_tenth_solar > 0
Mass is positive.

- radius_km : ℕ
Radius (scaled, km).

- radius_pos : self.radius_km > 0
Radius positive.

- log_B_gauss : ℕ
Surface magnetic field (scaled, log10 in Gauss).

Instances For

---

### `Tau.BookV.Astrophysics.instReprCompactObjectData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L91-L91)
**instance
Tau.BookV.Astrophysics.instReprCompactObjectData :Repr CompactObjectData**

Equations
- Tau.BookV.Astrophysics.instReprCompactObjectData = { reprPrec := Tau.BookV.Astrophysics.instReprCompactObjectData.repr }

---

### `Tau.BookV.Astrophysics.instReprCompactObjectData.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L91-L91)
**def
Tau.BookV.Astrophysics.instReprCompactObjectData.repr :CompactObjectData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.chandrasekhar_mass_limit`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L97-L98)
**def
Tau.BookV.Astrophysics.chandrasekhar_mass_limit :ℕ**


Chandrasekhar mass limit (14 = 1.4 solar masses in tenths).
Equations
- Tau.BookV.Astrophysics.chandrasekhar_mass_limit = 14
Instances For

---

### `Tau.BookV.Astrophysics.wd_mass_limit`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L100-L112)
**theorem
Tau.BookV.Astrophysics.wd_mass_limit :"WD mass limited by electron degeneracy at M_Ch ~ 1.4 M_sun" = "WD mass limited by electron degeneracy at M_Ch ~ 1.4 M_sun"**


[V.T86] White dwarf mass limit: no white dwarf can exceed the
Chandrasekhar mass M_Ch ≈ 1.4 M_☉.

In the τ-framework, this is the maximum mass at which electron
degeneracy can sustain the S² boundary topology against the
D-sector coupling.

Above M_Ch, the defect cost of maintaining electron-degeneracy
boundary exceeds the energy budget, forcing a transition to
neutron degeneracy (neutron star) or direct collapse.

---

### `Tau.BookV.Astrophysics.ns_eos_from_defect`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L118-L127)
**theorem
Tau.BookV.Astrophysics.ns_eos_from_defect :"NS EOS = defect-bundle compression component at nuclear density" = "NS EOS = defect-bundle compression component at nuclear density"**


[V.P71] Neutron star EOS from defect bundle: the equation of
state of neutron-star matter is determined by the defect-bundle
structure at nuclear densities.

At density ρ > ρ_nuclear, the defect tuple's compression
component dominates, stiffening the EOS and setting the
TOV maximum mass.

---

### `Tau.BookV.Astrophysics.tov_mass_lower`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L133-L134)
**def
Tau.BookV.Astrophysics.tov_mass_lower :ℕ**


TOV maximum mass range (in tenths of solar mass).
Equations
- Tau.BookV.Astrophysics.tov_mass_lower = 21
Instances For

---

### `Tau.BookV.Astrophysics.tov_mass_upper`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L135-L135)
**def
Tau.BookV.Astrophysics.tov_mass_upper :ℕ**

Equations
- Tau.BookV.Astrophysics.tov_mass_upper = 25
Instances For

---

### `Tau.BookV.Astrophysics.tov_maximum_mass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L137-L145)
**theorem
Tau.BookV.Astrophysics.tov_maximum_mass :tov_mass_lower < tov_mass_upper**


[V.T87] TOV maximum mass: neutron stars have a maximum mass
M_TOV ≈ 2.1-2.5 M_☉ above which the S² topology is
unsustainable and the coherence horizon crossing occurs.

The exact value depends on the nuclear EOS, which the
τ-framework constrains but does not uniquely determine
from first principles alone.

---

### `Tau.BookV.Astrophysics.PulsarType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L151-L159)
**inductive
Tau.BookV.Astrophysics.PulsarType :Type**


Pulsar type.

- Normal : PulsarType
Normal pulsar (period 0.1-10 seconds).

- Millisecond : PulsarType
Millisecond pulsar (period < 30 ms).

- Magnetar : PulsarType
Magnetar (B > 10^14 Gauss).

Instances For

---

### `Tau.BookV.Astrophysics.instReprPulsarType.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L159-L159)
**def
Tau.BookV.Astrophysics.instReprPulsarType.repr :PulsarType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprPulsarType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L159-L159)
**instance
Tau.BookV.Astrophysics.instReprPulsarType :Repr PulsarType**

Equations
- Tau.BookV.Astrophysics.instReprPulsarType = { reprPrec := Tau.BookV.Astrophysics.instReprPulsarType.repr }

---

### `Tau.BookV.Astrophysics.instDecidableEqPulsarType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L159-L159)
**instance
Tau.BookV.Astrophysics.instDecidableEqPulsarType :DecidableEq PulsarType**

Equations
- Tau.BookV.Astrophysics.instDecidableEqPulsarType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqPulsarType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L159-L159)
**instance
Tau.BookV.Astrophysics.instBEqPulsarType :BEq PulsarType**

Equations
- Tau.BookV.Astrophysics.instBEqPulsarType = { beq := Tau.BookV.Astrophysics.instBEqPulsarType.beq }

---

### `Tau.BookV.Astrophysics.instBEqPulsarType.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L159-L159)
**def
Tau.BookV.Astrophysics.instBEqPulsarType.beq :PulsarType → PulsarType → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqPulsarType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.PulsarData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L161-L179)
**structure
Tau.BookV.Astrophysics.PulsarData :Type**


[V.D125] Pulsar data: a rotating neutron star emitting beamed
radiation from its magnetic poles.

The timing stability of millisecond pulsars (Δt/t ~ 10⁻²¹)
makes them the most precise gravitational clocks.

- star : CompactObjectData
Underlying compact object.

- pulsar_type : PulsarType
Pulsar type.

- period_microseconds : ℕ
Period (scaled, microseconds).

- period_pos : self.period_microseconds > 0
Period positive.

- period_dot_scaled : ℕ
Period derivative (dimensionless, scaled × 10^20).

- is_ns : self.star.obj_type = CompactObjectType.NeutronStar
Must be a neutron star.

Instances For

---

### `Tau.BookV.Astrophysics.instReprPulsarData.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L179-L179)
**def
Tau.BookV.Astrophysics.instReprPulsarData.repr :PulsarData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprPulsarData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L179-L179)
**instance
Tau.BookV.Astrophysics.instReprPulsarData :Repr PulsarData**

Equations
- Tau.BookV.Astrophysics.instReprPulsarData = { reprPrec := Tau.BookV.Astrophysics.instReprPulsarData.repr }

---

### `Tau.BookV.Astrophysics.mass_gap_lower`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L185-L186)
**def
Tau.BookV.Astrophysics.mass_gap_lower :ℕ**


Lower edge of mass gap (tenths of solar mass).
Equations
- Tau.BookV.Astrophysics.mass_gap_lower = 25
Instances For

---

### `Tau.BookV.Astrophysics.mass_gap_upper`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L187-L188)
**def
Tau.BookV.Astrophysics.mass_gap_upper :ℕ**


Upper edge of mass gap (tenths of solar mass).
Equations
- Tau.BookV.Astrophysics.mass_gap_upper = 50
Instances For

---

### `Tau.BookV.Astrophysics.mass_gap_prediction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L190-L202)
**theorem
Tau.BookV.Astrophysics.mass_gap_prediction :mass_gap_lower < mass_gap_upper**


[V.T88] Mass gap prediction: the τ-framework predicts a mass gap
between the maximum NS mass (~2.5 M_☉) and the minimum BH mass
(~5 M_☉).

The gap arises because the topology crossing (S² → T²) has a
finite defect cost barrier. The system cannot continuously
transition but must jump, creating a gap in the compact-object
mass spectrum.

This prediction is testable via gravitational wave observations
of merger remnants.

---

### `Tau.BookV.Astrophysics.magnetar_from_vortex`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L208-L216)
**theorem
Tau.BookV.Astrophysics.magnetar_from_vortex :"Magnetar = NS with large vorticity defect component, topologically stabilized" = "Magnetar = NS with large vorticity defect component, topologically stabilized"**


[V.P72] Magnetar from defect vortex: magnetars (B ~ 10^15 G)
are neutron stars whose defect bundle contains a large-amplitude
vorticity component, read out as an ultra-strong magnetic field.

The vortex is topologically stabilized by the S² boundary,
preventing field decay on dynamical timescales.

---

### `Tau.BookV.Astrophysics.crab_pulsar`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/CompactObjects.lean#L246-L260)
**def
Tau.BookV.Astrophysics.crab_pulsar :PulsarData**


Example: Crab pulsar.
Equations
- One or more equations did not get rendered due to their size.
Instances For
