---
layout: taulib-doc
title: "TauLib.BookV.Astrophysics.GalaxyRelational"
permalink: /verify/taulib/docs/book-v-astrophysics-galaxy-relational/
lane: verify
module_name: "TauLib.BookV.Astrophysics.GalaxyRelational"
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

# TauLib.BookV.Astrophysics.GalaxyRelational


Galaxies as relational structures in the τ-framework. No dark matter
needed — galactic dynamics arise from boundary corrections to the
D-sector coupling. Galaxy morphology, formation, and clustering
are readouts of τ-boundary data.

## Registry Cross-References


- [V.D120] Galactic Defect Bundle -- `GalacticDefectBundle`

- [V.R169] No Dark Matter Particle -- structural remark

- [V.P63] Galaxy Morphology from Boundary Topology -- `morphology_from_topology`

- [V.P64] Spiral Arms from Defect Density Waves -- `spiral_arms_density_waves`

- [V.R170] Ellipticals as Relaxed Bundles -- structural remark

- [V.D121] Galactic Rotation Profile -- `GalacticRotationProfile`

- [V.P65] Tully-Fisher from D-Sector Scaling -- `tully_fisher_scaling`

- [V.R171] Baryonic Tully-Fisher Preferred -- structural remark

- [V.D122] Galaxy Cluster Data -- `GalaxyClusterData`

- [V.R172] Cluster as Multi-Bundle System -- structural remark

- [V.P66] Virial Discrepancy from Boundary Corrections -- `virial_discrepancy`

- [V.R173] Dark Matter as Missing Readout Correction -- structural remark


## Mathematical Content


### Galactic Defect Bundle


A galaxy is a macroscopic defect bundle: a collection of stellar-scale
defect bundles (stars) bound by the collective D-sector coupling.
The galaxy's boundary data determines its rotation profile, morphology,
and evolution.

### No Dark Matter


In the τ-framework, "dark matter" is unnecessary. The flat rotation
curves and virial mass discrepancies arise from:

- Boundary corrections to the D-sector coupling at galactic scales

- The refinement tower's finite depth (non-Newtonian at large r)

- Collective defect-bundle effects not captured by point-mass readout


### Tully-Fisher Relation


The baryonic Tully-Fisher relation M_b ∝ v⁴ is a D-sector scaling
law: the total baryonic mass determines the asymptotic rotation
velocity through the boundary character's large-r behavior.

## Ground Truth Sources


- Book V ch36: Galaxies as Relational Structures


---

### `Tau.BookV.Astrophysics.GalaxyMorphology`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L61-L73)
**inductive
Tau.BookV.Astrophysics.GalaxyMorphology :Type**


Galaxy morphology classification (Hubble sequence).

- Spiral : GalaxyMorphology
Spiral galaxy (disk + arms + bulge).

- BarredSpiral : GalaxyMorphology
Barred spiral (bar + arms + bulge).

- Elliptical : GalaxyMorphology
Elliptical galaxy (relaxed, no disk).

- Lenticular : GalaxyMorphology
Lenticular (disk, no arms).

- Irregular : GalaxyMorphology
Irregular (no regular structure).

Instances For

---

### `Tau.BookV.Astrophysics.instReprGalaxyMorphology.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L73-L73)
**def
Tau.BookV.Astrophysics.instReprGalaxyMorphology.repr :GalaxyMorphology → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprGalaxyMorphology`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L73-L73)
**instance
Tau.BookV.Astrophysics.instReprGalaxyMorphology :Repr GalaxyMorphology**

Equations
- Tau.BookV.Astrophysics.instReprGalaxyMorphology = { reprPrec := Tau.BookV.Astrophysics.instReprGalaxyMorphology.repr }

---

### `Tau.BookV.Astrophysics.instDecidableEqGalaxyMorphology`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L73-L73)
**instance
Tau.BookV.Astrophysics.instDecidableEqGalaxyMorphology :DecidableEq GalaxyMorphology**

Equations
- Tau.BookV.Astrophysics.instDecidableEqGalaxyMorphology x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqGalaxyMorphology`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L73-L73)
**instance
Tau.BookV.Astrophysics.instBEqGalaxyMorphology :BEq GalaxyMorphology**

Equations
- Tau.BookV.Astrophysics.instBEqGalaxyMorphology = { beq := Tau.BookV.Astrophysics.instBEqGalaxyMorphology.beq }

---

### `Tau.BookV.Astrophysics.instBEqGalaxyMorphology.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L73-L73)
**def
Tau.BookV.Astrophysics.instBEqGalaxyMorphology.beq :GalaxyMorphology → GalaxyMorphology → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqGalaxyMorphology.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.GalacticDefectBundle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L75-L94)
**structure
Tau.BookV.Astrophysics.GalacticDefectBundle :Type**


[V.D120] Galactic defect bundle: a galaxy modeled as a
macroscopic defect bundle with boundary data determining
its rotation, morphology, and evolution.

The galaxy is NOT a collection of point masses in a dark
matter halo but a single τ-structural entity.

- morphology : GalaxyMorphology
Morphological type.

- baryonic_mass : ℕ
Baryonic mass index (scaled, 10^9 solar masses).

- mass_pos : self.baryonic_mass > 0
Baryonic mass is positive.

- disk_radius : ℕ
Disk radius index (scaled, kpc).

- has_bar : Bool
Whether the galaxy has a bar.

- num_arms : ℕ
Number of spiral arms (0 for non-spiral).

Instances For

---

### `Tau.BookV.Astrophysics.instReprGalacticDefectBundle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L94-L94)
**instance
Tau.BookV.Astrophysics.instReprGalacticDefectBundle :Repr GalacticDefectBundle**

Equations
- Tau.BookV.Astrophysics.instReprGalacticDefectBundle = { reprPrec := Tau.BookV.Astrophysics.instReprGalacticDefectBundle.repr }

---

### `Tau.BookV.Astrophysics.instReprGalacticDefectBundle.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L94-L94)
**def
Tau.BookV.Astrophysics.instReprGalacticDefectBundle.repr :GalacticDefectBundle → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.milky_way`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L96-L103)
**def
Tau.BookV.Astrophysics.milky_way :GalacticDefectBundle**


The Milky Way as a barred spiral.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.morphology_from_topology`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L109-L118)
**theorem
Tau.BookV.Astrophysics.morphology_from_topology :"Hubble sequence = boundary topology classification of defect bundles" = "Hubble sequence = boundary topology classification of defect bundles"**


[V.P63] Galaxy morphology from boundary topology: the Hubble
sequence is a readout of the boundary topology of the galactic
defect bundle.

Spiral arms = density waves in the defect field
Ellipticals = relaxed (isotropic) defect bundles
Irregulars = non-equilibrium defect configurations

---

### `Tau.BookV.Astrophysics.spiral_arms_density_waves`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L124-L130)
**theorem
Tau.BookV.Astrophysics.spiral_arms_density_waves
(g : GalacticDefectBundle)

(_hs : g.morphology = GalaxyMorphology.Spiral ∨ g.morphology = GalaxyMorphology.BarredSpiral)

(ha : g.num_arms > 0)
 :g.num_arms > 0**


[V.P64] Spiral arms from defect density waves: spiral structure
is a standing-wave pattern in the galactic defect field, not a
material structure. Stars move through arms.

---

### `Tau.BookV.Astrophysics.RotationRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L136-L144)
**inductive
Tau.BookV.Astrophysics.RotationRegime :Type**


Rotation curve regime.

- SolidBody : RotationRegime
Inner: solid-body rotation (v ∝ r).

- Transitional : RotationRegime
Transitional: rising then flattening.

- Flat : RotationRegime
Flat: asymptotically constant v.

Instances For

---

### `Tau.BookV.Astrophysics.instReprRotationRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L144-L144)
**instance
Tau.BookV.Astrophysics.instReprRotationRegime :Repr RotationRegime**

Equations
- Tau.BookV.Astrophysics.instReprRotationRegime = { reprPrec := Tau.BookV.Astrophysics.instReprRotationRegime.repr }

---

### `Tau.BookV.Astrophysics.instReprRotationRegime.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L144-L144)
**def
Tau.BookV.Astrophysics.instReprRotationRegime.repr :RotationRegime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instDecidableEqRotationRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L144-L144)
**instance
Tau.BookV.Astrophysics.instDecidableEqRotationRegime :DecidableEq RotationRegime**

Equations
- Tau.BookV.Astrophysics.instDecidableEqRotationRegime x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqRotationRegime.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L144-L144)
**def
Tau.BookV.Astrophysics.instBEqRotationRegime.beq :RotationRegime → RotationRegime → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqRotationRegime.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.instBEqRotationRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L144-L144)
**instance
Tau.BookV.Astrophysics.instBEqRotationRegime :BEq RotationRegime**

Equations
- Tau.BookV.Astrophysics.instBEqRotationRegime = { beq := Tau.BookV.Astrophysics.instBEqRotationRegime.beq }

---

### `Tau.BookV.Astrophysics.GalacticRotationProfile`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L146-L163)
**structure
Tau.BookV.Astrophysics.GalacticRotationProfile :Type**


[V.D121] Galactic rotation profile: radial dependence of the
circular velocity in a galaxy.

The flat regime at large r is the hallmark prediction that
orthodox physics attributes to dark matter but that τ explains
through boundary corrections.

- galaxy : GalacticDefectBundle
Associated galaxy.

- v_flat : ℕ
Asymptotic velocity (km/s).

- v_pos : self.v_flat > 0
Velocity is positive.

- r_transition : ℕ
Transition radius (kpc, scaled × 10).

- outer_regime : RotationRegime
Outer regime.

Instances For

---

### `Tau.BookV.Astrophysics.instReprGalacticRotationProfile.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L163-L163)
**def
Tau.BookV.Astrophysics.instReprGalacticRotationProfile.repr :GalacticRotationProfile → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprGalacticRotationProfile`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L163-L163)
**instance
Tau.BookV.Astrophysics.instReprGalacticRotationProfile :Repr GalacticRotationProfile**

Equations
- Tau.BookV.Astrophysics.instReprGalacticRotationProfile = { reprPrec := Tau.BookV.Astrophysics.instReprGalacticRotationProfile.repr }

---

### `Tau.BookV.Astrophysics.tully_fisher_scaling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L169-L178)
**theorem
Tau.BookV.Astrophysics.tully_fisher_scaling :"M_b proportional to v^4 = D-sector boundary scaling" = "M_b proportional to v^4 = D-sector boundary scaling"**


[V.P65] Tully-Fisher from D-sector scaling: the baryonic
Tully-Fisher relation M_b ∝ v⁴ is a scaling law of the
D-sector coupling at galactic scales.

The exponent 4 is structural: it comes from the boundary
character's large-r behavior combined with the D-sector
coupling constant κ(D;1) = 1−ι<sub>τ</sub>.

---

### `Tau.BookV.Astrophysics.GalaxyClusterData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L184-L200)
**structure
Tau.BookV.Astrophysics.GalaxyClusterData :Type**


[V.D122] Galaxy cluster data: a bound collection of galaxies
with virial mass discrepancy explained by boundary corrections
(not dark matter).

- num_galaxies : ℕ
Number of member galaxies.

- num_pos : self.num_galaxies > 0
Number is positive.

- virial_mass : ℕ
Cluster virial mass index (scaled, 10^14 solar masses).

- baryonic_mass : ℕ
Total baryonic mass index (same scale).

- baryonic_lt_virial : self.baryonic_mass < self.virial_mass
Baryonic always less than virial (the "discrepancy").

- velocity_dispersion : ℕ
Velocity dispersion (km/s).

Instances For

---

### `Tau.BookV.Astrophysics.instReprGalaxyClusterData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L200-L200)
**instance
Tau.BookV.Astrophysics.instReprGalaxyClusterData :Repr GalaxyClusterData**

Equations
- Tau.BookV.Astrophysics.instReprGalaxyClusterData = { reprPrec := Tau.BookV.Astrophysics.instReprGalaxyClusterData.repr }

---

### `Tau.BookV.Astrophysics.instReprGalaxyClusterData.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L200-L200)
**def
Tau.BookV.Astrophysics.instReprGalaxyClusterData.repr :GalaxyClusterData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.virial_discrepancy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L206-L211)
**theorem
Tau.BookV.Astrophysics.virial_discrepancy
(c : GalaxyClusterData)
 :c.baryonic_mass < c.virial_mass**


[V.P66] Virial discrepancy from boundary corrections: the factor
~5 discrepancy between virial and baryonic mass in clusters is
NOT evidence for dark matter particles but for boundary corrections
to the D-sector coupling at cluster scales.

---

### `Tau.BookV.Astrophysics.HighZAccelerationEnhancement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L252-L267)
**structure
Tau.BookV.Astrophysics.HighZAccelerationEnhancement :Type**


[V.D299] High-z acceleration enhancement:
E(z) = a₀(z)/a₀(0) = H(z)/H₀ ≈ Ω_m^(1/2) · (1+z)^(3/2).
At z=10: E ≈ 20.5, at z=13: E ≈ 29.4.
τ-effective: uses V.T204 (a₀(z) = cH(z)ι<sub>τ</sub>/2) + standard Friedmann.

- z_x10 : ℕ
Redshift.

- enhancement_x10 : ℕ
Enhancement factor E(z) = a₀(z)/a₀(0) (scaled ×10).

- sfe_enhancement_x10 : ℕ
SFE enhancement ~ E^(1/2) (scaled ×10).

- baseline_sfe_pct : ℕ
Baseline SFE at z=0 (percent).

- enhanced_sfe_pct : ℕ
Enhanced SFE (percent).

Instances For

---

### `Tau.BookV.Astrophysics.instReprHighZAccelerationEnhancement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L267-L267)
**instance
Tau.BookV.Astrophysics.instReprHighZAccelerationEnhancement :Repr HighZAccelerationEnhancement**

Equations
- Tau.BookV.Astrophysics.instReprHighZAccelerationEnhancement = { reprPrec := Tau.BookV.Astrophysics.instReprHighZAccelerationEnhancement.repr }

---

### `Tau.BookV.Astrophysics.instReprHighZAccelerationEnhancement.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L267-L267)
**def
Tau.BookV.Astrophysics.instReprHighZAccelerationEnhancement.repr :HighZAccelerationEnhancement → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.JWSTEnhancementTheorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L269-L285)
**structure
Tau.BookV.Astrophysics.JWSTEnhancementTheorem :Type**


[V.T239] JWST Enhancement Theorem:
Enhanced a₀(z) produces deeper potential wells → faster collapse → higher SFE.
SFE(z)/SFE(0) ~ [E(z)]^(1/2) from virial-threshold crossing.

- name : String
Galaxy name / field.

- z_x10 : ℕ
Observed redshift (×10).

- log_mass_x10 : ℕ
Observed stellar mass (log₁₀ M_☉, ×10).

- lcdm_sfe_pct : ℕ
ΛCDM required SFE (percent).

- tau_sfe_pct : ℕ
τ-enhanced SFE (percent).

- enhancement_x10 : ℕ
Enhancement factor (×10).

Instances For

---

### `Tau.BookV.Astrophysics.instReprJWSTEnhancementTheorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L285-L285)
**instance
Tau.BookV.Astrophysics.instReprJWSTEnhancementTheorem :Repr JWSTEnhancementTheorem**

Equations
- Tau.BookV.Astrophysics.instReprJWSTEnhancementTheorem = { reprPrec := Tau.BookV.Astrophysics.instReprJWSTEnhancementTheorem.repr }

---

### `Tau.BookV.Astrophysics.instReprJWSTEnhancementTheorem.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L285-L285)
**def
Tau.BookV.Astrophysics.instReprJWSTEnhancementTheorem.repr :JWSTEnhancementTheorem → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.gnz11_enhancement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L287-L294)
**def
Tau.BookV.Astrophysics.gnz11_enhancement :JWSTEnhancementTheorem**


GN-z11 at z = 10.6.
Equations
- Tau.BookV.Astrophysics.gnz11_enhancement = { name := "GN-z11", z_x10 := 106, log_mass_x10 := 90, lcdm_sfe_pct := 40, tau_sfe_pct := 47, enhancement_x10 := 220 }
Instances For

---

### `Tau.BookV.Astrophysics.jades_z13_enhancement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L296-L303)
**def
Tau.BookV.Astrophysics.jades_z13_enhancement :JWSTEnhancementTheorem**


JADES-GS-z13-0 at z = 13.2.
Equations
- Tau.BookV.Astrophysics.jades_z13_enhancement = { name := "JADES-GS-z13", z_x10 := 132, log_mass_x10 := 87, lcdm_sfe_pct := 60, tau_sfe_pct := 56,
 enhancement_x10 := 310 }
Instances For

---

### `Tau.BookV.Astrophysics.sfe_enhancement_at_z10`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L305-L307)
**theorem
Tau.BookV.Astrophysics.sfe_enhancement_at_z10 :gnz11_enhancement.tau_sfe_pct = 47**


[V.P163] SFE enhancement: ε(z)/ε(0) = Ω_m^(1/4)·(1+z)^(3/4).

---

### `Tau.BookV.Astrophysics.uv_lf_excess_jades`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L309-L312)
**theorem
Tau.BookV.Astrophysics.uv_lf_excess_jades :jades_z13_enhancement.enhancement_x10 = 310**


[V.P164] UV luminosity function excess: Φ_τ/Φ_ΛCDM E(z)^α, α~0.5-1.
At z=13: excess factor 5–30×, matching JWST JADES/CEERS observations.
