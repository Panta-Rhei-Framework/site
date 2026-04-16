---
layout: taulib-doc
title: "TauLib.BookV.Astrophysics.AccretionJets"
permalink: /verify/taulib/docs/book-v-astrophysics-accretion-jets/
lane: verify
module_name: "TauLib.BookV.Astrophysics.AccretionJets"
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

# TauLib.BookV.Astrophysics.AccretionJets


Accretion disk physics and jet formation from bipolar topology.
The Eddington limit, disk structure, and relativistic jets emerge
from the τ-framework's bipolar lemniscate boundary L = S¹ ∨ S¹.

## Registry Cross-References


- [V.P77] Accretion as Defect Infall -- `accretion_as_defect_infall`

- [V.D129] Accretion Disk Structure -- `AccretionDiskStructure`

- [V.R185] Shakura-Sunyaev from D-Sector Viscosity -- structural remark

- [V.D130] Eddington Limit Data -- `EddingtonLimitData`

- [V.P78] Eddington from Sector Balance -- `eddington_sector_balance`

- [V.T90] Bipolar Jet Theorem -- `bipolar_jet_theorem`

- [V.R186] Lemniscate Topology Forces Bipolarity -- structural remark

- [V.T91] Jet Power from Spin Readout -- `jet_power_from_spin`

- [V.R187] Blandford-Znajek as Readout Mechanism -- structural remark

- [V.D131] Jet Collimation Data -- `JetCollimationData`

- [V.R188] AGN Unification from Viewing Angle -- structural remark

- [V.P79] Quasar Luminosity from Accretion Rate -- `quasar_luminosity`

- [V.R189] Feedback from Jet-ISM Interaction -- structural remark

- [V.D132] AGN Classification -- `AGNType`

- [V.T92] Accretion Efficiency Bound -- `accretion_efficiency_bound`

- [V.R190] Efficiency Exceeds Nuclear -- structural remark

- [V.R191] Accretion-Jet Cycle as Defect Pump -- structural remark


## Mathematical Content


### Accretion Disk Structure


Accretion disks form when matter spiraling toward a compact object
has sufficient angular momentum. In the τ-framework, the disk is a
steady-state defect flow where:


- Gravitational defect (D-sector) drives inward flow

- Angular momentum defect resists compression

- Viscous defect transport mediates angular momentum outward


### Bipolar Jet Formation


Jets are bipolar because the lemniscate boundary L = S¹ ∨ S¹ has
TWO lobes. The disk plane coincides with the crossing point of L.
Material can only escape along the two polar directions — the
lobe axes. This is a TOPOLOGICAL prediction, not a dynamical one.

### Eddington Limit


The Eddington luminosity L_Edd = 4πGMm_pc/σ_T is the balance
between D-sector (gravity) and B-sector (EM radiation pressure).
Above L_Edd, radiation pressure disrupts the accretion flow.

### Accretion Efficiency


Gravitational accretion can convert up to ~40% of rest mass to
radiation (for maximally spinning BH), far exceeding nuclear
fusion efficiency (~0.7%). This is the most efficient energy
extraction mechanism in nature.

## Ground Truth Sources


- Book V ch40: Accretion and Jets


---

### `Tau.BookV.Astrophysics.accretion_as_defect_infall`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L73-L81)
**theorem
Tau.BookV.Astrophysics.accretion_as_defect_infall :"Accretion = defect-bundle infall along D-sector coupling gradient" = "Accretion = defect-bundle infall along D-sector coupling gradient"**


[V.P77] Accretion as defect infall: matter accreting onto a
compact object is defect-bundle material flowing down the
D-sector coupling gradient.

The accretion rate is determined by the defect-transport
rate through the angular-momentum barrier.

---

### `Tau.BookV.Astrophysics.DiskModel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L87-L95)
**inductive
Tau.BookV.Astrophysics.DiskModel :Type**


Disk model type.

- ThinDisk : DiskModel
Thin disk (Shakura-Sunyaev): H/R << 1.

- ThickDisk : DiskModel
Thick disk (torus/ADAF): H/R ~ 1.

- SlimDisk : DiskModel
Slim disk: intermediate, radiation-trapped.

Instances For

---

### `Tau.BookV.Astrophysics.instReprDiskModel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L95-L95)
**instance
Tau.BookV.Astrophysics.instReprDiskModel :Repr DiskModel**

Equations
- Tau.BookV.Astrophysics.instReprDiskModel = { reprPrec := Tau.BookV.Astrophysics.instReprDiskModel.repr }

---

### `Tau.BookV.Astrophysics.instReprDiskModel.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L95-L95)
**def
Tau.BookV.Astrophysics.instReprDiskModel.repr :DiskModel → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instDecidableEqDiskModel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L95-L95)
**instance
Tau.BookV.Astrophysics.instDecidableEqDiskModel :DecidableEq DiskModel**

Equations
- Tau.BookV.Astrophysics.instDecidableEqDiskModel x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqDiskModel.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L95-L95)
**def
Tau.BookV.Astrophysics.instBEqDiskModel.beq :DiskModel → DiskModel → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqDiskModel.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.instBEqDiskModel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L95-L95)
**instance
Tau.BookV.Astrophysics.instBEqDiskModel :BEq DiskModel**

Equations
- Tau.BookV.Astrophysics.instBEqDiskModel = { beq := Tau.BookV.Astrophysics.instBEqDiskModel.beq }

---

### `Tau.BookV.Astrophysics.AccretionDiskStructure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L97-L115)
**structure
Tau.BookV.Astrophysics.AccretionDiskStructure :Type**


[V.D129] Accretion disk structure: parametrization of the
steady-state accretion disk around a compact object.

All disk properties are readouts of the D-sector coupling
combined with angular momentum conservation.

- central_object : CompactObjectType
Central object type.

- model : DiskModel
Disk model.

- inner_radius : ℕ
Inner disk radius (Schwarzschild radii, scaled × 10).

- inner_pos : self.inner_radius > 0
Inner radius positive.

- accretion_rate : ℕ
Accretion rate (scaled, 10⁻⁸ M_☉/yr × 100).

- efficiency_permil : ℕ
Radiative efficiency (percent × 10).

Instances For

---

### `Tau.BookV.Astrophysics.instReprAccretionDiskStructure.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L115-L115)
**def
Tau.BookV.Astrophysics.instReprAccretionDiskStructure.repr :AccretionDiskStructure → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprAccretionDiskStructure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L115-L115)
**instance
Tau.BookV.Astrophysics.instReprAccretionDiskStructure :Repr AccretionDiskStructure**

Equations
- Tau.BookV.Astrophysics.instReprAccretionDiskStructure = { reprPrec := Tau.BookV.Astrophysics.instReprAccretionDiskStructure.repr }

---

### `Tau.BookV.Astrophysics.EddingtonLimitData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L121-L134)
**structure
Tau.BookV.Astrophysics.EddingtonLimitData :Type**


[V.D130] Eddington limit data: the maximum luminosity at which
radiation pressure (B-sector) balances gravity (D-sector).

L_Edd = 4πGMm_pc / σ_T ≈ 1.26 × 10³⁸ (M/M_☉) erg/s.

- mass_tenth_solar : ℕ
Mass of the accreting object (tenths of solar mass).

- mass_pos : self.mass_tenth_solar > 0
Mass positive.

- l_edd_scaled : ℕ
Eddington luminosity (10³⁸ erg/s, scaled × 100).

- is_super_eddington : Bool
Whether the source is super-Eddington.

Instances For

---

### `Tau.BookV.Astrophysics.instReprEddingtonLimitData.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L134-L134)
**def
Tau.BookV.Astrophysics.instReprEddingtonLimitData.repr :EddingtonLimitData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprEddingtonLimitData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L134-L134)
**instance
Tau.BookV.Astrophysics.instReprEddingtonLimitData :Repr EddingtonLimitData**

Equations
- Tau.BookV.Astrophysics.instReprEddingtonLimitData = { reprPrec := Tau.BookV.Astrophysics.instReprEddingtonLimitData.repr }

---

### `Tau.BookV.Astrophysics.eddington_sector_balance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L136-L144)
**theorem
Tau.BookV.Astrophysics.eddington_sector_balance :"Eddington limit = D-sector (gravity) balanced by B-sector (radiation)" = "Eddington limit = D-sector (gravity) balanced by B-sector (radiation)"**


[V.P78] Eddington from sector balance: the Eddington limit
is the balance point between D-sector (gravity) and B-sector
(electromagnetic radiation pressure). Two sectors, one limit.

Super-Eddington accretion is possible when photon trapping
reduces the effective radiation pressure (slim disk regime).

---

### `Tau.BookV.Astrophysics.bipolar_jet_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L150-L161)
**theorem
Tau.BookV.Astrophysics.bipolar_jet_theorem :"Jets are always bipolar: 2 lobes of L = S^1 v S^1" = "Jets are always bipolar: 2 lobes of L = S^1 v S^1"**


[V.T90] Bipolar jet theorem: relativistic jets from accreting
compact objects are ALWAYS bipolar (two opposing jets) because
the lemniscate boundary L = S¹ ∨ S¹ has exactly two lobes.

The disk plane contains the crossing point of L.
The jet axes align with the lobe axes.

This is a topological prediction: jets cannot be unipolar
or have more than two lobes in the τ-framework.

---

### `Tau.BookV.Astrophysics.jet_power_from_spin`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L167-L179)
**theorem
Tau.BookV.Astrophysics.jet_power_from_spin :"P_jet proportional to a^2*B^2*M^2 = spin readout of T^2 rotation" = "P_jet proportional to a^2*B^2*M^2 = spin readout of T^2 rotation"**


[V.T91] Jet power from spin readout: the mechanical power of a
relativistic jet scales with the spin of the central BH:

```
P_jet ∝ a² · B² · M²
```


where a = dimensionless spin parameter, B = magnetic field
strength, M = BH mass.

In the τ-framework, the spin is a rotation index of the
torus vacuum T², and the jet power is its D-sector readout.

---

### `Tau.BookV.Astrophysics.JetCollimationData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L185-L199)
**structure
Tau.BookV.Astrophysics.JetCollimationData :Type**


[V.D131] Jet collimation data: the opening angle and extent of
a relativistic jet, determined by the lemniscate boundary
geometry and the ambient pressure profile.

- half_angle : ℕ
Opening half-angle (degrees × 10).

- extent_kpc : ℕ
Jet extent (kpc, scaled × 10).

- lorentz_factor : ℕ
Lorentz factor (bulk).

- lorentz_ge_one : self.lorentz_factor ≥ 1
Lorentz factor at least 1.

- is_relativistic : Bool
Whether the jet is relativistic (Γ > 2).

Instances For

---

### `Tau.BookV.Astrophysics.instReprJetCollimationData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L199-L199)
**instance
Tau.BookV.Astrophysics.instReprJetCollimationData :Repr JetCollimationData**

Equations
- Tau.BookV.Astrophysics.instReprJetCollimationData = { reprPrec := Tau.BookV.Astrophysics.instReprJetCollimationData.repr }

---

### `Tau.BookV.Astrophysics.instReprJetCollimationData.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L199-L199)
**def
Tau.BookV.Astrophysics.instReprJetCollimationData.repr :JetCollimationData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.AGNType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L205-L224)
**inductive
Tau.BookV.Astrophysics.AGNType :Type**


[V.D132] AGN classification: active galactic nuclei classified
by accretion rate and viewing angle.

In the τ-framework, the AGN "zoo" is a single phenomenon
(accretion + jets around a supermassive BH) viewed from
different angles and accretion states.

- Seyfert1 : AGNType
Seyfert 1: face-on view, broad lines visible.

- Seyfert2 : AGNType
Seyfert 2: edge-on, broad lines obscured.

- Quasar : AGNType
Quasar: high-luminosity AGN.

- Blazar : AGNType
Blazar: jet pointed at observer.

- RadioGalaxy : AGNType
Radio galaxy: powerful jets, large lobes.

- LINER : AGNType
LINER: low-ionization nuclear emission region.

Instances For

---

### `Tau.BookV.Astrophysics.instReprAGNType.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L224-L224)
**def
Tau.BookV.Astrophysics.instReprAGNType.repr :AGNType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprAGNType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L224-L224)
**instance
Tau.BookV.Astrophysics.instReprAGNType :Repr AGNType**

Equations
- Tau.BookV.Astrophysics.instReprAGNType = { reprPrec := Tau.BookV.Astrophysics.instReprAGNType.repr }

---

### `Tau.BookV.Astrophysics.instDecidableEqAGNType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L224-L224)
**instance
Tau.BookV.Astrophysics.instDecidableEqAGNType :DecidableEq AGNType**

Equations
- Tau.BookV.Astrophysics.instDecidableEqAGNType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqAGNType.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L224-L224)
**def
Tau.BookV.Astrophysics.instBEqAGNType.beq :AGNType → AGNType → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqAGNType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.instBEqAGNType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L224-L224)
**instance
Tau.BookV.Astrophysics.instBEqAGNType :BEq AGNType**

Equations
- Tau.BookV.Astrophysics.instBEqAGNType = { beq := Tau.BookV.Astrophysics.instBEqAGNType.beq }

---

### `Tau.BookV.Astrophysics.quasar_luminosity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L230-L237)
**theorem
Tau.BookV.Astrophysics.quasar_luminosity :"L_quasar = eta*Mdot*c^2, eta ~ 0.1 for thin disk accretion" = "L_quasar = eta*Mdot*c^2, eta ~ 0.1 for thin disk accretion"**


[V.P79] Quasar luminosity from accretion rate: quasar
luminosities (up to 10⁴⁷ erg/s) derive from accretion onto
supermassive BH (10⁸-10⁹ M_☉) at near-Eddington rates.

L_quasar = η · M_dot · c² where η ~ 0.1 for a thin disk.

---

### `Tau.BookV.Astrophysics.nuclear_efficiency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L243-L244)
**def
Tau.BookV.Astrophysics.nuclear_efficiency :ℕ**


Nuclear fusion efficiency (percent × 10).
Equations
- Tau.BookV.Astrophysics.nuclear_efficiency = 7
Instances For

---

### `Tau.BookV.Astrophysics.max_accretion_efficiency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L245-L246)
**def
Tau.BookV.Astrophysics.max_accretion_efficiency :ℕ**


Maximum accretion efficiency (percent × 10).
Equations
- Tau.BookV.Astrophysics.max_accretion_efficiency = 400
Instances For

---

### `Tau.BookV.Astrophysics.accretion_efficiency_bound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L248-L256)
**theorem
Tau.BookV.Astrophysics.accretion_efficiency_bound :nuclear_efficiency < max_accretion_efficiency**


[V.T92] Accretion efficiency bound: gravitational accretion
efficiency (up to ~40% for max spin) greatly exceeds nuclear
fusion efficiency (~0.7%).

This is the most efficient energy extraction mechanism and
explains why quasars outshine their host galaxies despite
accreting modest mass rates.

---

### `Tau.BookV.Astrophysics.stellar_bh_disk`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L299-L306)
**def
Tau.BookV.Astrophysics.stellar_bh_disk :AccretionDiskStructure**


Example: thin disk around stellar-mass BH.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.m87_jet`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L308-L314)
**def
Tau.BookV.Astrophysics.m87_jet :JetCollimationData**


Example: M87 jet.
Equations
- Tau.BookV.Astrophysics.m87_jet = { half_angle := 10, extent_kpc := 500, lorentz_factor := 6, lorentz_ge_one := Tau.BookV.Astrophysics.m87_jet._proof_2,
 is_relativistic := true }
Instances For

---

### `Tau.BookV.Astrophysics.ToroidalFluxIntegral`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L325-L334)
**structure
Tau.BookV.Astrophysics.ToroidalFluxIntegral :Type**


[V.D285] Toroidal Flux Integral: magnetic flux through a meridional
cross-section of the torus, measuring the poloidal field component.

- surface : String
Description of the flux surface.

- flux_x1000 : ℕ
Flux value (arbitrary units × 1000).

- flux_nonneg : self.flux_x1000 ≥ 0
Flux is non-negative.

Instances For

---

### `Tau.BookV.Astrophysics.instReprToroidalFluxIntegral`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L334-L334)
**instance
Tau.BookV.Astrophysics.instReprToroidalFluxIntegral :Repr ToroidalFluxIntegral**

Equations
- Tau.BookV.Astrophysics.instReprToroidalFluxIntegral = { reprPrec := Tau.BookV.Astrophysics.instReprToroidalFluxIntegral.repr }

---

### `Tau.BookV.Astrophysics.instReprToroidalFluxIntegral.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L334-L334)
**def
Tau.BookV.Astrophysics.instReprToroidalFluxIntegral.repr :ToroidalFluxIntegral → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.PoloidalFluxIntegral`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L336-L345)
**structure
Tau.BookV.Astrophysics.PoloidalFluxIntegral :Type**


[V.D286] Poloidal Flux Integral: magnetic flux through the torus hole,
topologically protected in ideal MHD. Requires genus ≥ 1.

- surface : String
Description of the flux surface.

- flux_x1000 : ℕ
Flux value (arbitrary units × 1000).

- topo_protected : ℕ
Topologically protected (1 = yes).

Instances For

---

### `Tau.BookV.Astrophysics.instReprPoloidalFluxIntegral.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L345-L345)
**def
Tau.BookV.Astrophysics.instReprPoloidalFluxIntegral.repr :PoloidalFluxIntegral → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprPoloidalFluxIntegral`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L345-L345)
**instance
Tau.BookV.Astrophysics.instReprPoloidalFluxIntegral :Repr PoloidalFluxIntegral**

Equations
- Tau.BookV.Astrophysics.instReprPoloidalFluxIntegral = { reprPrec := Tau.BookV.Astrophysics.instReprPoloidalFluxIntegral.repr }

---

### `Tau.BookV.Astrophysics.flux_threading_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L347-L352)
**theorem
Tau.BookV.Astrophysics.flux_threading_theorem :"Φ_pol(T²) topologically protected; Φ_hole(S²) = 0" = "Φ_pol(T²) topologically protected; Φ_hole(S²) = 0"**


[V.T228] Flux Threading Theorem: both toroidal and poloidal fluxes
are conserved on T². Poloidal flux is topologically protected.
On S², there is no topological flux (H_1(S²) = 0).

---

### `Tau.BookV.Astrophysics.homology_rank_t2_vs_s2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L354-L355)
**theorem
Tau.BookV.Astrophysics.homology_rank_t2_vs_s2 :2 > 0**


H_1(T²) ≅ Z² (rank 2 homology), H_1(S²) = 0 (rank 0).

---

### `Tau.BookV.Astrophysics.FluxRatio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L357-L367)
**structure
Tau.BookV.Astrophysics.FluxRatio :Type**


[V.P153] Flux Ratio: Φ_pol/Φ_tor ~ ι<sub>τ</sub> ≈ 0.341 from area ratio.

- phi_pol_x1000 : ℕ
Poloidal flux (units × 1000).

- phi_tor_x1000 : ℕ
Toroidal flux (units × 1000).

- tor_pos : self.phi_tor_x1000 > 0
Toroidal flux is positive.

- ratio_x1000 : ℕ
Ratio × 1000 (should be ≈ 341).

Instances For

---

### `Tau.BookV.Astrophysics.instReprFluxRatio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L367-L367)
**instance
Tau.BookV.Astrophysics.instReprFluxRatio :Repr FluxRatio**

Equations
- Tau.BookV.Astrophysics.instReprFluxRatio = { reprPrec := Tau.BookV.Astrophysics.instReprFluxRatio.repr }

---

### `Tau.BookV.Astrophysics.instReprFluxRatio.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L367-L367)
**def
Tau.BookV.Astrophysics.instReprFluxRatio.repr :FluxRatio → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.JetPoloidalField`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L373-L386)
**structure
Tau.BookV.Astrophysics.JetPoloidalField :Type**


[V.D289] Jet Poloidal Field: axial B-field component in the jet,
originating from topologically protected flux through the torus hole.

- source : String
Source name.

- b_z_base_x100 : ℕ
Poloidal field at base (Gauss × 100).

- b_phi_base_x100 : ℕ
Toroidal field at base (Gauss × 100).

- ratio_x1000 : ℕ
Ratio B_z/B_phi × 1000 at base (should be ≈ 341).

- topo_anchored : ℕ
Topologically anchored (1 = yes).

Instances For

---

### `Tau.BookV.Astrophysics.instReprJetPoloidalField.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L386-L386)
**def
Tau.BookV.Astrophysics.instReprJetPoloidalField.repr :JetPoloidalField → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprJetPoloidalField`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L386-L386)
**instance
Tau.BookV.Astrophysics.instReprJetPoloidalField :Repr JetPoloidalField**

Equations
- Tau.BookV.Astrophysics.instReprJetPoloidalField = { reprPrec := Tau.BookV.Astrophysics.instReprJetPoloidalField.repr }

---

### `Tau.BookV.Astrophysics.JetHelicity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L388-L398)
**structure
Tau.BookV.Astrophysics.JetHelicity :Type**


[V.D290] Jet Magnetic Helicity: H_m = ∫ A·B dV, conserved in ideal MHD.

- sign : ℤ
Helicity sign: +1 or -1, fixed by T² topology.

- sign_valid : self.sign = 1 ∨ self.sign = -1
Sign is ±1.

- conserved : ℕ
Conserved in ideal MHD (1 = yes).

- fixed_by_topology : ℕ
Fixed by topology (1 = yes).

Instances For

---

### `Tau.BookV.Astrophysics.instReprJetHelicity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L398-L398)
**instance
Tau.BookV.Astrophysics.instReprJetHelicity :Repr JetHelicity**

Equations
- Tau.BookV.Astrophysics.instReprJetHelicity = { reprPrec := Tau.BookV.Astrophysics.instReprJetHelicity.repr }

---

### `Tau.BookV.Astrophysics.instReprJetHelicity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L398-L398)
**def
Tau.BookV.Astrophysics.instReprJetHelicity.repr :JetHelicity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.jet_helicity_conserved`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L400-L404)
**theorem
Tau.BookV.Astrophysics.jet_helicity_conserved :"H_m(jet) is topologically fixed and conserved (frozen flux + Taylor)" = "H_m(jet) is topologically fixed and conserved (frozen flux + Taylor)"**


[V.T231] Jet Helicity Conservation: helicity is topologically fixed
at the jet base and conserved along the jet (frozen flux + Taylor).

---

### `Tau.BookV.Astrophysics.jet_collimation_from_hoop_stress`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L406-L410)
**theorem
Tau.BookV.Astrophysics.jet_collimation_from_hoop_stress :"sin(θ_jet) ≤ B_z/B_φ = ι<sub>τ</sub> ≈ 0.341 → θ_jet ≤ 20°" = "sin(θ_jet) ≤ B_z/B_φ = ι<sub>τ</sub> ≈ 0.341 → θ_jet ≤ 20°"**


[V.T232] Jet Collimation from Hoop Stress: B_phi hoop stress gives
sin(θ_jet) ≤ B_z/B_phi = ι<sub>τ</sub>, recovering the Jet Collimation Theorem.

---

### `Tau.BookV.Astrophysics.m87_jet_magnetic`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L412-L414)
**def
Tau.BookV.Astrophysics.m87_jet_magnetic :JetPoloidalField**


M87 jet magnetic structure.
Equations
- Tau.BookV.Astrophysics.m87_jet_magnetic = { source := "M87*", b_z_base_x100 := 480, b_phi_base_x100 := 1400 }
Instances For

---

### `Tau.BookV.Astrophysics.m87_jet_helicity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/AccretionJets.lean#L416-L418)
**def
Tau.BookV.Astrophysics.m87_jet_helicity :JetHelicity**


Positive helicity example.
Equations
- Tau.BookV.Astrophysics.m87_jet_helicity = { sign := 1, sign_valid := Tau.BookV.Astrophysics.m87_jet_helicity._proof_1 }
Instances For
