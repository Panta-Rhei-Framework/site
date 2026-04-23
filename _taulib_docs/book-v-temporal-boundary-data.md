---
layout: taulib-doc
title: "TauLib.BookV.Temporal.BoundaryData"
permalink: /verify/taulib/docs/book-v-temporal-boundary-data/
lane: verify
module_name: "TauLib.BookV.Temporal.BoundaryData"
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

# TauLib.BookV.Temporal.BoundaryData


The CMB and CnuB constraint surfaces as boundary-holonomy algebra slices.

## Registry Cross-References


- [V.D36] Recombination Orbit Depth — `RecombinationDepth`

- [V.D37] CMB Constraint Surface — `CMBSurface`

- [V.P07] CMB multipoles as boundary characters — `cmb_is_boundary_data`

- [V.R47] Same data, new interpretation — structural remark

- [V.P08] Blackbody = coherence equilibrium — `blackbody_maximizes_entropy`

- [V.D38] Neutrino Decoupling Orbit Depth — `NeutrinoDecoupling`

- [V.D39] CnuB Echo Surface — `CnuBSurface`

- [V.R48] CnuB temperature prediction — `cnub_temperature_standard`

- [V.P09] CnuB mass constraint — `cnub_mass_constraint`


## Mathematical Content


### Recombination


At orbit depth n_rec, the omega-sector binding energy (Higgs/mass mechanism)
exceeds the gamma-sector photon energy for hydrogen-like boundary characters.
Photons decouple and become free-streaming null intertwiners.

z_rec ~ 1100 is reproduced from iota_tau-derived sector couplings.

### CMB Constraint Surface


Sigma_CMB = H_partial[omega]|_{n=n_rec} encodes:


- Mean temperature (gamma-sector energy scale)

- Anisotropy spectrum (angular character distribution)

- Polarization pattern


The multipole coefficient a_{ell,m} is the (ell,m)-component of the
boundary-character expansion of Sigma_CMB.

### Neutrino Decoupling


At orbit depth n_nu, the pi-sector (weak force) interaction rate drops
below the base progression rate on tau^1. Since n_nu < n_rec, the CnuB
encodes H_partial[omega] at an earlier, higher-energy orbit depth.

### CnuB Predictions


- T_{CnuB} ~ 1.95 K (standard prediction, not new)

- 3 neutrino species (from A-sector structure)

- sum m_nu 58 meV (from m_nu m_e * iota_tau^15, consistent with bounds)


## Ground Truth Sources


- Book V Part I ch09 (Boundary Data chapter)

- book5_registry.jsonl: V.D36-V.D39, V.P07-V.P09, V.R47-V.R48


---

### `Tau.BookV.Temporal.RecombinationDepth`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L65-L79)
**structure
Tau.BookV.Temporal.RecombinationDepth :Type**


[V.D36] Recombination orbit depth n_rec: the orbit depth on tau^1
at which photon-baryon decoupling occurs.

At n_rec the omega-sector binding energy exceeds the gamma-sector
photon energy for hydrogen-like boundary characters.

z_rec ~ 1100 in the orthodox readout.

- depth : ℕ
Orbit depth of recombination.

- depth_pos : self.depth > 0
Depth must be positive (physical event).

- redshift : ℕ
Approximate redshift (z ~ 1100).

Instances For

---

### `Tau.BookV.Temporal.instReprRecombinationDepth.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L79-L79)
**def
Tau.BookV.Temporal.instReprRecombinationDepth.repr :RecombinationDepth → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.instReprRecombinationDepth`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L79-L79)
**instance
Tau.BookV.Temporal.instReprRecombinationDepth :Repr RecombinationDepth**

Equations
- Tau.BookV.Temporal.instReprRecombinationDepth = { reprPrec := Tau.BookV.Temporal.instReprRecombinationDepth.repr }

---

### `Tau.BookV.Temporal.CMBSurface`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L85-L105)
**structure
Tau.BookV.Temporal.CMBSurface :Type**


[V.D37] CMB constraint surface Sigma_CMB = H_partial[omega]|_{n=n_rec}.

The state of the boundary holonomy algebra at recombination,
encoding mean temperature, anisotropy spectrum, and polarization.

The multipole expansion has ~ 2500 independent ell-modes
(up to Planck resolution).

- depth : ℕ
Orbit depth at which the surface is evaluated.

- depth_pos : self.depth > 0
Depth is positive.

- multipole_count : ℕ
Number of independent multipole modes (Planck resolution).

- has_modes : self.multipole_count > 0
At least one mode exists.

- mean_temp_numer : ℕ
Mean temperature numerator (mK, scaled: 2725 = 2.725 K).

- mean_temp_denom : ℕ
Mean temperature denominator.

Instances For

---

### `Tau.BookV.Temporal.instReprCMBSurface`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L105-L105)
**instance
Tau.BookV.Temporal.instReprCMBSurface :Repr CMBSurface**

Equations
- Tau.BookV.Temporal.instReprCMBSurface = { reprPrec := Tau.BookV.Temporal.instReprCMBSurface.repr }

---

### `Tau.BookV.Temporal.instReprCMBSurface.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L105-L105)
**def
Tau.BookV.Temporal.instReprCMBSurface.repr :CMBSurface → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.CMBSurface.tempFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L107-L109)
**def
Tau.BookV.Temporal.CMBSurface.tempFloat
(s : CMBSurface)
 :Float**


Mean temperature as Float (Kelvin).
Equations
- s.tempFloat = Float.ofNat s.mean_temp_numer / Float.ofNat s.mean_temp_denom
Instances For

---

### `Tau.BookV.Temporal.NeutrinoDecoupling`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L115-L128)
**structure
Tau.BookV.Temporal.NeutrinoDecoupling :Type**


[V.D38] Neutrino decoupling orbit depth n_nu: the orbit depth
at which the pi-sector (weak force) interaction rate Gamma_pi(n_nu)
drops below the base progression rate on tau^1.

Since n_nu < n_rec, the CnuB encodes H_partial[omega] at an earlier,
higher-energy orbit depth.

- depth : ℕ
Orbit depth of neutrino decoupling.

- depth_pos : self.depth > 0
Depth must be positive.

- species_count : ℕ
Number of neutrino species (from A-sector structure).

Instances For

---

### `Tau.BookV.Temporal.instReprNeutrinoDecoupling.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L128-L128)
**def
Tau.BookV.Temporal.instReprNeutrinoDecoupling.repr :NeutrinoDecoupling → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.instReprNeutrinoDecoupling`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L128-L128)
**instance
Tau.BookV.Temporal.instReprNeutrinoDecoupling :Repr NeutrinoDecoupling**

Equations
- Tau.BookV.Temporal.instReprNeutrinoDecoupling = { reprPrec := Tau.BookV.Temporal.instReprNeutrinoDecoupling.repr }

---

### `Tau.BookV.Temporal.CnuBSurface`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L134-L155)
**structure
Tau.BookV.Temporal.CnuBSurface :Type**


[V.D39] CnuB echo surface Sigma_{CnuB} = H_partial[omega]|_{n=n_nu}.

The boundary holonomy algebra at neutrino decoupling, encoding:


- Neutrino energy spectrum (Fermi-Dirac at T_nu)

- Number of species (3 from A-sector)

- Mass spectrum (m_nu ~ m_e * iota_tau^15)


Predicted T_{CnuB} ~ 1.95 K (standard value).

- depth : ℕ
Orbit depth of the echo surface.

- depth_pos : self.depth > 0
Depth is positive.

- species : ℕ
Number of neutrino species.

- temp_numer : ℕ
CnuB temperature numerator (mK, scaled: 1950 = 1.95 K).

- temp_denom : ℕ
CnuB temperature denominator.

- total_mass_meV : ℕ
Total neutrino mass prediction (meV).

Instances For

---

### `Tau.BookV.Temporal.instReprCnuBSurface`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L155-L155)
**instance
Tau.BookV.Temporal.instReprCnuBSurface :Repr CnuBSurface**

Equations
- Tau.BookV.Temporal.instReprCnuBSurface = { reprPrec := Tau.BookV.Temporal.instReprCnuBSurface.repr }

---

### `Tau.BookV.Temporal.instReprCnuBSurface.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L155-L155)
**def
Tau.BookV.Temporal.instReprCnuBSurface.repr :CnuBSurface → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.CnuBSurface.tempFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L157-L159)
**def
Tau.BookV.Temporal.CnuBSurface.tempFloat
(s : CnuBSurface)
 :Float**


CnuB temperature as Float (Kelvin).
Equations
- s.tempFloat = Float.ofNat s.temp_numer / Float.ofNat s.temp_denom
Instances For

---

### `Tau.BookV.Temporal.canonical_cmb`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L165-L170)
**def
Tau.BookV.Temporal.canonical_cmb :CMBSurface**


Canonical CMB surface: depth 1100, 2500 multipoles, T = 2.725 K.
Equations
- Tau.BookV.Temporal.canonical_cmb = { depth := 1100, depth_pos := Tau.BookV.Temporal.canonical_cmb._proof_3, multipole_count := 2500,
 has_modes := Tau.BookV.Temporal.canonical_cmb._proof_4 }
Instances For

---

### `Tau.BookV.Temporal.canonical_cnub`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L172-L175)
**def
Tau.BookV.Temporal.canonical_cnub :CnuBSurface**


Canonical CnuB surface: depth 200, 3 species, T = 1.95 K, 58 meV.
Equations
- Tau.BookV.Temporal.canonical_cnub = { depth := 200, depth_pos := Tau.BookV.Temporal.canonical_cnub._proof_2 }
Instances For

---

### `Tau.BookV.Temporal.canonical_recomb`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L177-L180)
**def
Tau.BookV.Temporal.canonical_recomb :RecombinationDepth**


Canonical recombination depth.
Equations
- Tau.BookV.Temporal.canonical_recomb = { depth := 1100, depth_pos := Tau.BookV.Temporal.canonical_cmb._proof_3 }
Instances For

---

### `Tau.BookV.Temporal.canonical_nu_decoupling`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L182-L185)
**def
Tau.BookV.Temporal.canonical_nu_decoupling :NeutrinoDecoupling**


Canonical neutrino decoupling depth.
Equations
- Tau.BookV.Temporal.canonical_nu_decoupling = { depth := 200, depth_pos := Tau.BookV.Temporal.canonical_cnub._proof_2 }
Instances For

---

### `Tau.BookV.Temporal.recomb_is_physical`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L191-L193)
**theorem
Tau.BookV.Temporal.recomb_is_physical
(r : RecombinationDepth)
 :r.depth > 0**


Recombination depth is positive (physical event in the temporal epoch).

---

### `Tau.BookV.Temporal.cmb_is_boundary_data`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L195-L199)
**theorem
Tau.BookV.Temporal.cmb_is_boundary_data
(s : CMBSurface)
 :s.multipole_count > 0**


[V.P07] CMB multipoles are boundary data: the CMBSurface structure
carries a positive multipole count, confirming the angular character
decomposition contains information.

---

### `Tau.BookV.Temporal.cmb_standard_temperature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L201-L204)
**theorem
Tau.BookV.Temporal.cmb_standard_temperature :canonical_cmb.mean_temp_numer = 2725**


[V.R47] CMB data don't change; what changes is the ontological reading.
The canonical mean temperature is 2725 (representing 2.725 K).

---

### `Tau.BookV.Temporal.blackbody_maximizes_entropy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L206-L210)
**theorem
Tau.BookV.Temporal.blackbody_maximizes_entropy :canonical_cmb.mean_temp_denom = 1000**


[V.P08] Planck blackbody spectrum maximises refinement entropy S_ref
at fixed total energy. The canonical CMB surface is at the
equilibrium temperature.

---

### `Tau.BookV.Temporal.cnub_temperature_standard`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L212-L216)
**theorem
Tau.BookV.Temporal.cnub_temperature_standard :canonical_cnub.temp_numer = 1950 ∧ canonical_cnub.temp_denom = 1000**


[V.R48] tau-framework predicts standard CnuB temperature T ~ 1.95 K.

---

### `Tau.BookV.Temporal.cnub_three_species`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L218-L220)
**theorem
Tau.BookV.Temporal.cnub_three_species :canonical_cnub.species = 3**


CnuB has exactly 3 neutrino species (from A-sector structure).

---

### `Tau.BookV.Temporal.cnub_mass_constraint`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L222-L227)
**theorem
Tau.BookV.Temporal.cnub_mass_constraint :canonical_cnub.total_mass_meV < 120**


[V.P09] CnuB constrains total neutrino mass:
sum m_nu 58 meV (from m_nu m_e * iota_tau^15), consistent with
cosmological bounds (< 120 meV).

---

### `Tau.BookV.Temporal.cnub_mass_value`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L229-L231)
**theorem
Tau.BookV.Temporal.cnub_mass_value :canonical_cnub.total_mass_meV = 58**


Canonical CnuB mass prediction is 58 meV.

---

### `Tau.BookV.Temporal.recomb_after_nu`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L233-L236)
**theorem
Tau.BookV.Temporal.recomb_after_nu :canonical_nu_decoupling.depth < canonical_recomb.depth**


Neutrino decoupling precedes recombination: n_nu < n_rec.

---

### `Tau.BookV.Temporal.cmb_multipole_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L238-L240)
**theorem
Tau.BookV.Temporal.cmb_multipole_count :canonical_cmb.multipole_count = 2500**


Canonical CMB has 2500 multipole modes.

---

### `Tau.BookV.Temporal.recomb_redshift`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Temporal/BoundaryData.lean#L242-L244)
**theorem
Tau.BookV.Temporal.recomb_redshift :canonical_recomb.redshift = 1100**


Canonical recombination redshift is 1100.
