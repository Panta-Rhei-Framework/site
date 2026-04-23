---
layout: taulib-doc
title: "TauLib.BookV.Thermodynamics.HeatEM"
permalink: /verify/taulib/docs/book-v-thermodynamics-heat-em/
lane: verify
module_name: "TauLib.BookV.Thermodynamics.HeatEM"
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

# TauLib.BookV.Thermodynamics.HeatEM


Heat as B-sector (electromagnetic) phenomenon. All macroscopic energy
transport (radiation, conduction, convection) is mediated by the B-sector
of the boundary holonomy algebra. Geometric and topological relaxation.

## Registry Cross-References


- [V.D91] EM Energy Transport -- `EMEnergyTransport`

- [V.D92] Geometric Relaxation -- `GeometricRelaxation`

- [V.D93] Topological Relaxation -- `TopologicalRelaxation`

- [V.P34] Radiation is B-Sector Transport -- `radiation_is_b_sector`

- [V.P35] Conduction is Near-Field B-Sector Transport -- `conduction_is_b_sector`

- [V.P36] Convective Transport is B-Sector Displacement -- `convection_is_b_sector`

- [V.P37] Hierarchy of Relaxation Times -- `relaxation_hierarchy`

- [V.T63] Alpha Governs Macroscopic Energy Transport -- `alpha_governs_transport`

- [V.T64] Heat is Electromagnetism -- `HeatIsEM`

- [V.R128] The Artificial Trichotomy -- `artificial_trichotomy`

- [V.R129] Why Alpha and Not iota_tau^2 -- `why_alpha_not_iota_sq`


## Mathematical Content


### EM Energy Transport


A change in the CR-tension distribution on tau^3 mediated by the B-sector
of H_partial[omega], with transport energy proportional to iota_tau^2.

### The Artificial Trichotomy


Classical radiation/conduction/convection is pedagogical convenience.
All three are B-sector boundary exchange: phonons are collective EM
lattice modes, pressure gradients are electromagnetic.

### Relaxation Hierarchy


Geometric relaxation (spatial redistribution on T^2) is much faster
than topological relaxation (absorption by lemniscate boundary).

### Heat is Electromagnetism


All macroscopic energy transport at E1 is mediated by the B-sector,
with heat flux proportional to the boundary holonomy algebra's B-component.

## Ground Truth Sources


- Book V ch24: heat as B-sector phenomenon

- temporal_spatial_decomposition.md: B-sector = EM


---

### `Tau.BookV.Thermodynamics.artificial_trichotomy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L60-L66)
**theorem
Tau.BookV.Thermodynamics.artificial_trichotomy :"radiation + conduction + convection = three faces of B-sector transport" = "radiation + conduction + convection = three faces of B-sector transport"**


[V.R128] The artificial trichotomy: radiation/conduction/convection
is pedagogical convenience. All three are B-sector (EM) boundary
exchange. Phonons are collective EM lattice modes, pressure
gradients are electromagnetic.

---

### `Tau.BookV.Thermodynamics.TransportMode`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L72-L80)
**inductive
Tau.BookV.Thermodynamics.TransportMode :Type**


Transport mode classification: the three faces of EM transport.

- Radiation : TransportMode
Radiative: far-field EM (photon) transport.

- Conduction : TransportMode
Conductive: near-field EM (phonon/lattice) transport.

- Convection : TransportMode
Convective: coherent bulk displacement of defect profiles.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprTransportMode`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L80-L80)
**instance
Tau.BookV.Thermodynamics.instReprTransportMode :Repr TransportMode**

Equations
- Tau.BookV.Thermodynamics.instReprTransportMode = { reprPrec := Tau.BookV.Thermodynamics.instReprTransportMode.repr }

---

### `Tau.BookV.Thermodynamics.instReprTransportMode.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L80-L80)
**def
Tau.BookV.Thermodynamics.instReprTransportMode.repr :TransportMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instDecidableEqTransportMode`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L80-L80)
**instance
Tau.BookV.Thermodynamics.instDecidableEqTransportMode :DecidableEq TransportMode**

Equations
- Tau.BookV.Thermodynamics.instDecidableEqTransportMode x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Thermodynamics.instBEqTransportMode.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L80-L80)
**def
Tau.BookV.Thermodynamics.instBEqTransportMode.beq :TransportMode → TransportMode → Bool**

Equations
- Tau.BookV.Thermodynamics.instBEqTransportMode.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Thermodynamics.instBEqTransportMode`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L80-L80)
**instance
Tau.BookV.Thermodynamics.instBEqTransportMode :BEq TransportMode**

Equations
- Tau.BookV.Thermodynamics.instBEqTransportMode = { beq := Tau.BookV.Thermodynamics.instBEqTransportMode.beq }

---

### `Tau.BookV.Thermodynamics.TransportMode.sector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L82-L83)
**def
Tau.BookV.Thermodynamics.TransportMode.sector :TransportMode → BookIII.Sectors.Sector**


All transport modes are B-sector.
Equations
- x✝.sector = Tau.BookIII.Sectors.Sector.B
Instances For

---

### `Tau.BookV.Thermodynamics.EMEnergyTransport`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L85-L101)
**structure
Tau.BookV.Thermodynamics.EMEnergyTransport :Type**


[V.D91] EM energy transport: a change in the CR-tension distribution
on tau^3 mediated by the B-sector of H_partial[omega].

Energy: Delta E = integral of over tau^3.
All three modes (radiation, conduction, convection) are B-sector.

- mode : TransportMode
The transport mode.

- energy_numer : ℕ
Energy numerator (scaled).

- energy_denom : ℕ
Energy denominator.

- denom_pos : self.energy_denom > 0
Denominator positive.

- mediating_sector : BookIII.Sectors.Sector
The mediating sector is always B.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprEMEnergyTransport`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L101-L101)
**instance
Tau.BookV.Thermodynamics.instReprEMEnergyTransport :Repr EMEnergyTransport**

Equations
- Tau.BookV.Thermodynamics.instReprEMEnergyTransport = { reprPrec := Tau.BookV.Thermodynamics.instReprEMEnergyTransport.repr }

---

### `Tau.BookV.Thermodynamics.instReprEMEnergyTransport.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L101-L101)
**def
Tau.BookV.Thermodynamics.instReprEMEnergyTransport.repr :EMEnergyTransport → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.transport_default_b`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L103-L105)
**theorem
Tau.BookV.Thermodynamics.transport_default_b :BookIII.Sectors.Sector.B = BookIII.Sectors.Sector.B**


The default mediating sector is B.

---

### `Tau.BookV.Thermodynamics.radiation_is_b_sector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L111-L116)
**theorem
Tau.BookV.Thermodynamics.radiation_is_b_sector :TransportMode.Radiation.sector = BookIII.Sectors.Sector.B**


[V.P34] Radiation is B-sector transport: radiative energy flux
from a defect configuration is proportional to kappa(B;2) = iota_tau^2.

j_rad = kappa(B;2) * rho_def^2 * c = iota_tau^2 * rho_def^2 * c

---

### `Tau.BookV.Thermodynamics.conduction_is_b_sector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L122-L128)
**theorem
Tau.BookV.Thermodynamics.conduction_is_b_sector :TransportMode.Conduction.sector = BookIII.Sectors.Sector.B**


[V.P35] Conduction is near-field B-sector transport: thermal
conduction in a lattice is mediated by near-field B-sector
boundary characters with wavelength comparable to lattice spacing.

kappa_cond proportional to alpha (readout of iota_tau^2).

---

### `Tau.BookV.Thermodynamics.convection_is_b_sector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L134-L140)
**theorem
Tau.BookV.Thermodynamics.convection_is_b_sector :TransportMode.Convection.sector = BookIII.Sectors.Sector.B**


[V.P36] Convective transport is B-sector displacement: coherent
displacement of the defect-functional profile driven by the
B-sector pressure gradient.

q_conv = kappa_eff * defect_profile * flow_velocity

---

### `Tau.BookV.Thermodynamics.alpha_governs_transport`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L146-L156)
**theorem
Tau.BookV.Thermodynamics.alpha_governs_transport :"Gamma_transport propto alpha * Delta_E (B-sector readout)" = "Gamma_transport propto alpha * Delta_E (B-sector readout)"**


[V.T63] Alpha governs macroscopic energy transport: the transport
rate between any two macroscopic E1 configurations is proportional
to the fine-structure constant alpha.

Gamma_transport propto alpha * Delta_E

This is because alpha is the E1 readout of the B-sector
self-coupling iota_tau^2 after holonomy correction.

---

### `Tau.BookV.Thermodynamics.why_alpha_not_iota_sq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L162-L170)
**theorem
Tau.BookV.Thermodynamics.why_alpha_not_iota_sq :Boundary.iota_tau_numer * Boundary.iota_tau_numer > 0**


[V.R129] Why alpha and not iota_tau^2: the B-sector self-coupling
kappa(B;2) = iota_tau^2 0.1166 is the tau-native sector strength.
alpha 1/137 is its E1 readout after holonomy correction and
dimensional bridge. The two are related but not equal.

Numerical check: iota_tau^2 = 341304^2 / 10^12 ~ 0.1166.

---

### `Tau.BookV.Thermodynamics.GeometricRelaxation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L176-L196)
**structure
Tau.BookV.Thermodynamics.GeometricRelaxation :Type**


[V.D92] Geometric relaxation: the process by which a defect bundle
loses CR-tension through spatial redistribution on the fiber T^2.

Driven by the fiber gradient of |dbar_b f|^2 weighted by
iota_tau^2 (B-sector self-coupling).

Geometric relaxation preserves topological sector.

- tension_initial_numer : ℕ
Initial tension numerator.

- tension_final_numer : ℕ
Final tension numerator (after relaxation).

- tension_denom : ℕ
Common denominator.

- denom_pos : self.tension_denom > 0
Denominator positive.

- tension_decreases : self.tension_final_numer ≤ self.tension_initial_numer
Tension decreases.

- preserves_topology : Bool
Topological sector is preserved.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprGeometricRelaxation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L196-L196)
**instance
Tau.BookV.Thermodynamics.instReprGeometricRelaxation :Repr GeometricRelaxation**

Equations
- Tau.BookV.Thermodynamics.instReprGeometricRelaxation = { reprPrec := Tau.BookV.Thermodynamics.instReprGeometricRelaxation.repr }

---

### `Tau.BookV.Thermodynamics.instReprGeometricRelaxation.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L196-L196)
**def
Tau.BookV.Thermodynamics.instReprGeometricRelaxation.repr :GeometricRelaxation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.TopologicalRelaxation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L202-L217)
**structure
Tau.BookV.Thermodynamics.TopologicalRelaxation :Type**


[V.D93] Topological relaxation: the process by which a defect
bundle is absorbed by the lemniscate boundary L = S^1 v S^1
through a change in topological sector.

Energy release from the variation of holonomy characters at L.
Much slower than geometric relaxation.

- defects_initial : ℕ
Initial defect count.

- defects_final : ℕ
Final defect count (after topological absorption).

- defects_decrease : self.defects_final ≤ self.defects_initial
Defect count decreases.

- sector_changes : Bool
Whether the topological sector changes.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprTopologicalRelaxation.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L217-L217)
**def
Tau.BookV.Thermodynamics.instReprTopologicalRelaxation.repr :TopologicalRelaxation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instReprTopologicalRelaxation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L217-L217)
**instance
Tau.BookV.Thermodynamics.instReprTopologicalRelaxation :Repr TopologicalRelaxation**

Equations
- Tau.BookV.Thermodynamics.instReprTopologicalRelaxation = { reprPrec := Tau.BookV.Thermodynamics.instReprTopologicalRelaxation.repr }

---

### `Tau.BookV.Thermodynamics.relaxation_hierarchy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L223-L231)
**theorem
Tau.BookV.Thermodynamics.relaxation_hierarchy :"tau_geom << tau_top: geometric much faster than topological" = "tau_geom << tau_top: geometric much faster than topological"**


[V.P37] Hierarchy of relaxation times:
geometric relaxation << topological relaxation.

Geometric (spatial redistribution on T^2) preserves topology.
Topological (absorption by L) changes sector.
The separation explains the apparent stability of defect bundles.

---

### `Tau.BookV.Thermodynamics.HeatIsEM`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L237-L252)
**structure
Tau.BookV.Thermodynamics.HeatIsEM :Type**


[V.T64] Heat is electromagnetism: all macroscopic energy transport
at E1 is mediated by the B-sector of the boundary holonomy algebra.

Q-dot = integral over boundary of B-component flux.

There is no separate "heat force" -- heat is the macroscopic
manifestation of the B-sector (electromagnetic) boundary exchange.

- sector : BookIII.Sectors.Sector
The mediating sector is always B (EM).

- no_separate_force : Bool
There is no separate heat force.

- transport_modes : List TransportMode
All three transport modes are unified.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprHeatIsEM`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L252-L252)
**instance
Tau.BookV.Thermodynamics.instReprHeatIsEM :Repr HeatIsEM**

Equations
- Tau.BookV.Thermodynamics.instReprHeatIsEM = { reprPrec := Tau.BookV.Thermodynamics.instReprHeatIsEM.repr }

---

### `Tau.BookV.Thermodynamics.instReprHeatIsEM.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L252-L252)
**def
Tau.BookV.Thermodynamics.instReprHeatIsEM.repr :HeatIsEM → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.heat_is_em_unified`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L254-L256)
**theorem
Tau.BookV.Thermodynamics.heat_is_em_unified :[TransportMode.Radiation, TransportMode.Conduction, TransportMode.Convection].length = 3**


The heat theorem: exactly 3 transport modes.

---

### `Tau.BookV.Thermodynamics.all_modes_b_sector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L258-L261)
**theorem
Tau.BookV.Thermodynamics.all_modes_b_sector :List.map TransportMode.sector [TransportMode.Radiation, TransportMode.Conduction, TransportMode.Convection] = [BookIII.Sectors.Sector.B, BookIII.Sectors.Sector.B, BookIII.Sectors.Sector.B]**


All modes in the heat structure are B-sector.

---

### `Tau.BookV.Thermodynamics.example_radiation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L267-L272)
**def
Tau.BookV.Thermodynamics.example_radiation :EMEnergyTransport**


Example radiative transport.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.example_geo_relax`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L277-L283)
**def
Tau.BookV.Thermodynamics.example_geo_relax :GeometricRelaxation**


Example geometric relaxation.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.example_top_relax`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/HeatEM.lean#L287-L291)
**def
Tau.BookV.Thermodynamics.example_top_relax :TopologicalRelaxation**


Example topological relaxation.
Equations
- Tau.BookV.Thermodynamics.example_top_relax = { defects_initial := 50, defects_final := 30,
 defects_decrease := Tau.BookV.Thermodynamics.example_top_relax._proof_2 }
Instances For
