---
layout: taulib-doc
title: "TauLib.BookV.Astrophysics.KeplerSolarSystem"
permalink: /verify/taulib/docs/book-v-astrophysics-kepler-solar-system/
lane: verify
module_name: "TauLib.BookV.Astrophysics.KeplerSolarSystem"
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

# TauLib.BookV.Astrophysics.KeplerSolarSystem


Kepler orbits from D-sector gravity. The solar system as a boundary
readout of the τ-arena. Planetary motion, tidal forces, and orbital
resonances emerge from the D-sector coupling at refinement depth 1.

## Registry Cross-References


- [V.D118] Kepler Orbit Data -- `KeplerOrbitData`

- [V.T81] Kepler First Law Recovery -- `kepler_first_law`

- [V.T82] Kepler Second Law Recovery -- `kepler_second_law`

- [V.T83] Kepler Third Law Recovery -- `kepler_third_law`

- [V.R165] Perihelion Precession as Post-Newtonian -- structural remark

- [V.T84] Tidal Force from Gradient Readout -- `tidal_force_gradient`

- [V.R166] Roche Limit as Defect Threshold -- structural remark

- [V.P59] Orbital Stability from Defect Minimum -- `orbital_stability`

- [V.P60] Resonance from Rational Readout -- `resonance_rational`

- [V.P61] Solar System as Single Readout -- `solar_system_single_readout`

- [V.R167] Bode's Law as Approximate Readout -- structural remark

- [V.D119] Tidal Force Structure -- `TidalForceStructure`

- [V.R168] Tidal Locking as Defect Equilibrium -- structural remark

- [V.P62] Planetary Classification from Defect Budget -- `planetary_classification`


## Mathematical Content


### Kepler Orbits


All three Kepler laws are readout-level consequences of the D-sector
coupling at refinement depth 1:

- Elliptical orbits: conic sections from 1/r potential readout

- Equal areas: angular momentum conservation from D-sector isotropy

- Period-semimajor axis relation: T² ∝ a³ from κ(D;1) = 1−ι<sub>τ</sub>


### Perihelion Precession


Mercury's perihelion precession (43"/century) is the first
post-Newtonian correction: depth-2 readout of the D-sector coupling.
This is NOT a separate effect but the next term in the refinement
tower expansion.

### Tidal Forces


Tidal forces are the gradient of the D-sector coupling across an
extended defect bundle. The Roche limit is the threshold where tidal
defect cost exceeds the object's internal cohesion budget.

## Ground Truth Sources


- Book V ch35: Kepler and the Solar System


---

### `Tau.BookV.Astrophysics.OrbitType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L62-L72)
**inductive
Tau.BookV.Astrophysics.OrbitType :Type**


Orbit type classification.

- Circular : OrbitType
Circular orbit (e = 0).

- Elliptical : OrbitType
Elliptical orbit (0 < e < 1).

- Parabolic : OrbitType
Parabolic orbit (e = 1).

- Hyperbolic : OrbitType
Hyperbolic orbit (e > 1).

Instances For

---

### `Tau.BookV.Astrophysics.instReprOrbitType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L72-L72)
**instance
Tau.BookV.Astrophysics.instReprOrbitType :Repr OrbitType**

Equations
- Tau.BookV.Astrophysics.instReprOrbitType = { reprPrec := Tau.BookV.Astrophysics.instReprOrbitType.repr }

---

### `Tau.BookV.Astrophysics.instReprOrbitType.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L72-L72)
**def
Tau.BookV.Astrophysics.instReprOrbitType.repr :OrbitType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instDecidableEqOrbitType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L72-L72)
**instance
Tau.BookV.Astrophysics.instDecidableEqOrbitType :DecidableEq OrbitType**

Equations
- Tau.BookV.Astrophysics.instDecidableEqOrbitType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqOrbitType.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L72-L72)
**def
Tau.BookV.Astrophysics.instBEqOrbitType.beq :OrbitType → OrbitType → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqOrbitType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.instBEqOrbitType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L72-L72)
**instance
Tau.BookV.Astrophysics.instBEqOrbitType :BEq OrbitType**

Equations
- Tau.BookV.Astrophysics.instBEqOrbitType = { beq := Tau.BookV.Astrophysics.instBEqOrbitType.beq }

---

### `Tau.BookV.Astrophysics.KeplerOrbitData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L74-L94)
**structure
Tau.BookV.Astrophysics.KeplerOrbitData :Type**


[V.D118] Kepler orbit data: parametrization of a two-body orbit
from the D-sector coupling readout.

All orbital elements are readouts of the boundary character
at a given refinement depth.

- semimajor_axis : ℕ
Semi-major axis (scaled, AU * 1000).

- eccentricity_numer : ℕ
Eccentricity numerator (e * 10000).

- eccentricity_denom : ℕ
Eccentricity denominator.

- ecc_denom_pos : self.eccentricity_denom > 0
Eccentricity denominator positive.

- orbit_type : OrbitType
Orbit type.

- period_days : ℕ
Orbital period (scaled, days).

- readout_depth : ℕ
Readout depth.

Instances For

---

### `Tau.BookV.Astrophysics.instReprKeplerOrbitData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L94-L94)
**instance
Tau.BookV.Astrophysics.instReprKeplerOrbitData :Repr KeplerOrbitData**

Equations
- Tau.BookV.Astrophysics.instReprKeplerOrbitData = { reprPrec := Tau.BookV.Astrophysics.instReprKeplerOrbitData.repr }

---

### `Tau.BookV.Astrophysics.instReprKeplerOrbitData.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L94-L94)
**def
Tau.BookV.Astrophysics.instReprKeplerOrbitData.repr :KeplerOrbitData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.earth_orbit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L96-L103)
**def
Tau.BookV.Astrophysics.earth_orbit :KeplerOrbitData**


Earth's orbit.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.mercury_orbit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L105-L112)
**def
Tau.BookV.Astrophysics.mercury_orbit :KeplerOrbitData**


Mercury's orbit.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.kepler_first_law`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L118-L123)
**theorem
Tau.BookV.Astrophysics.kepler_first_law
(k : KeplerOrbitData)

(hb : k.orbit_type = OrbitType.Elliptical)
 :k.orbit_type = OrbitType.Elliptical**


[V.T81] Kepler first law: orbits are conic sections.
This follows from the 1/r form of the D-sector coupling
readout in the Newtonian regime.

---

### `Tau.BookV.Astrophysics.kepler_second_law`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L125-L130)
**theorem
Tau.BookV.Astrophysics.kepler_second_law :"Equal areas in equal times = D-sector angular momentum conservation" = "Equal areas in equal times = D-sector angular momentum conservation"**


[V.T82] Kepler second law: equal areas in equal times.
This follows from angular momentum conservation, which is
a readout of D-sector isotropy (rotational symmetry).

---

### `Tau.BookV.Astrophysics.kepler_third_law`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L132-L137)
**theorem
Tau.BookV.Astrophysics.kepler_third_law :"T^2 / a^3 = 4pi^2 / (G*M) = readout of D-sector coupling" = "T^2 / a^3 = 4pi^2 / (G*M) = readout of D-sector coupling"**


[V.T83] Kepler third law: T^2 proportional to a^3.
This follows from the specific form of the D-sector coupling
κ(D;1) = 1−ι<sub>τ</sub> in the Newtonian readout.

---

### `Tau.BookV.Astrophysics.TidalForceStructure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L143-L158)
**structure
Tau.BookV.Astrophysics.TidalForceStructure :Type**


[V.D119] Tidal force structure: the gradient of the D-sector
coupling across an extended defect bundle.

Tidal acceleration ∝ M·d/r³ where d is the object size.

- source_mass : ℕ
Source mass index.

- object_size : ℕ
Object size index.

- orbital_distance : ℕ
Orbital distance index.

- distance_pos : self.orbital_distance > 0
Distance must be positive.

- tidally_locked : Bool
Whether tidal locking has occurred.

Instances For

---

### `Tau.BookV.Astrophysics.instReprTidalForceStructure.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L158-L158)
**def
Tau.BookV.Astrophysics.instReprTidalForceStructure.repr :TidalForceStructure → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprTidalForceStructure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L158-L158)
**instance
Tau.BookV.Astrophysics.instReprTidalForceStructure :Repr TidalForceStructure**

Equations
- Tau.BookV.Astrophysics.instReprTidalForceStructure = { reprPrec := Tau.BookV.Astrophysics.instReprTidalForceStructure.repr }

---

### `Tau.BookV.Astrophysics.tidal_force_gradient`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L160-L165)
**theorem
Tau.BookV.Astrophysics.tidal_force_gradient :"Tidal force = gradient of D-sector coupling across object extent" = "Tidal force = gradient of D-sector coupling across object extent"**


[V.T84] Tidal force from gradient readout: tidal forces are the
gradient of the D-sector coupling. Not a separate force, but the
spatial variation of the same D-sector coupling that produces gravity.

---

### `Tau.BookV.Astrophysics.orbital_stability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L171-L175)
**theorem
Tau.BookV.Astrophysics.orbital_stability :"Stable orbit = local minimum of effective defect potential" = "Stable orbit = local minimum of effective defect potential"**


[V.P59] Orbital stability from defect minimum: stable orbits
correspond to local minima of the effective defect potential.

---

### `Tau.BookV.Astrophysics.resonance_rational`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L177-L182)
**theorem
Tau.BookV.Astrophysics.resonance_rational :"Orbital resonance = rational period ratio in refinement tower" = "Orbital resonance = rational period ratio in refinement tower"**


[V.P60] Resonance from rational readout: orbital resonances
(e.g. Jupiter-Saturn 5:2) occur when the period ratio is a
rational number — a condition on the refinement tower levels.

---

### `Tau.BookV.Astrophysics.solar_system_single_readout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L184-L190)
**theorem
Tau.BookV.Astrophysics.solar_system_single_readout :"Solar system = one D-sector readout at depth 1" = "Solar system = one D-sector readout at depth 1"**


[V.P61] Solar system as single readout: the entire solar system
is a single coarse-grained readout of the D-sector coupling
at refinement depth 1. All planetary orbits, asteroid belts,
and comets emerge from ONE sector.

---

### `Tau.BookV.Astrophysics.PlanetaryType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L192-L202)
**inductive
Tau.BookV.Astrophysics.PlanetaryType :Type**


Planetary type classification.

- Rocky : PlanetaryType
Rocky planet (small defect bundle, high density).

- GasGiant : PlanetaryType
Gas giant (large defect bundle, low density).

- IceGiant : PlanetaryType
Ice giant (intermediate).

- DwarfPlanet : PlanetaryType
Dwarf planet (sub-threshold defect bundle).

Instances For

---

### `Tau.BookV.Astrophysics.instReprPlanetaryType.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L202-L202)
**def
Tau.BookV.Astrophysics.instReprPlanetaryType.repr :PlanetaryType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprPlanetaryType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L202-L202)
**instance
Tau.BookV.Astrophysics.instReprPlanetaryType :Repr PlanetaryType**

Equations
- Tau.BookV.Astrophysics.instReprPlanetaryType = { reprPrec := Tau.BookV.Astrophysics.instReprPlanetaryType.repr }

---

### `Tau.BookV.Astrophysics.instDecidableEqPlanetaryType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L202-L202)
**instance
Tau.BookV.Astrophysics.instDecidableEqPlanetaryType :DecidableEq PlanetaryType**

Equations
- Tau.BookV.Astrophysics.instDecidableEqPlanetaryType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqPlanetaryType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L202-L202)
**instance
Tau.BookV.Astrophysics.instBEqPlanetaryType :BEq PlanetaryType**

Equations
- Tau.BookV.Astrophysics.instBEqPlanetaryType = { beq := Tau.BookV.Astrophysics.instBEqPlanetaryType.beq }

---

### `Tau.BookV.Astrophysics.instBEqPlanetaryType.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L202-L202)
**def
Tau.BookV.Astrophysics.instBEqPlanetaryType.beq :PlanetaryType → PlanetaryType → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqPlanetaryType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.planetary_classification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L204-L210)
**theorem
Tau.BookV.Astrophysics.planetary_classification :[PlanetaryType.Rocky, PlanetaryType.GasGiant, PlanetaryType.IceGiant, PlanetaryType.DwarfPlanet].length = 4**


[V.P62] Planetary classification from defect budget: the four
planetary types correspond to distinct defect-budget regimes
in the D-sector readout.
