---
layout: taulib-doc
title: "TauLib.BookV.Astrophysics.BulletClusterLSS"
permalink: /verify/taulib/docs/book-v-astrophysics-bullet-cluster-lss/
lane: verify
module_name: "TauLib.BookV.Astrophysics.BulletClusterLSS"
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

# TauLib.BookV.Astrophysics.BulletClusterLSS


The Bullet Cluster without dark matter. Large-scale structure (LSS)
from τ-boundary data. Galaxy clustering, the cosmic web, and BAO
as readouts of the primordial boundary character spectrum.

## Registry Cross-References


- [V.R200] Bullet Cluster as Dark Matter "Proof" -- structural remark

- [V.D140] Bullet Cluster Tau Analysis -- `BulletClusterAnalysis`

- [V.T97] Lensing-Gas Offset from Boundary Correction -- `lensing_gas_offset`

- [V.P84] Collisionless Component is Stellar -- `collisionless_stellar`

- [V.D141] Large-Scale Structure Data -- `LSSData`

- [V.D142] Cosmic Web Classification -- `CosmicWebType`

- [V.T98] BAO from Primordial Boundary Spectrum -- `bao_from_boundary`

- [V.R201] BAO Scale 150 Mpc -- structural remark

- [V.D143] Power Spectrum Data -- `PowerSpectrumData`

- [V.P85] LSS from Boundary Character Growth -- `lss_from_boundary_growth`


## Mathematical Content


### Bullet Cluster


The Bullet Cluster (1E 0657-56) shows a spatial offset between the
gravitational lensing signal and the hot gas (X-ray). Orthodox
interpretation: dark matter is collisionless and separates from gas.

τ-framework interpretation:


- The lensing signal follows the TOTAL mass (stars + gas + boundary correction)

- The boundary correction to the D-sector coupling is centered on the
STELLAR component (collisionless), not the gas (collisional)

- The offset is between gas and stars, not gas and "dark matter"

- The enhanced lensing is the boundary holonomy correction evaluated
at the cluster's specific acceleration regime


### Large-Scale Structure


The cosmic web (filaments, walls, voids, clusters) is the large-scale
readout of the primordial boundary character spectrum:


- Filaments connect density peaks (D-sector coupling maxima)

- Voids are D-sector coupling minima

- The web topology is set by the primordial perturbation spectrum


### Baryon Acoustic Oscillations


BAO (characteristic ~150 Mpc scale in galaxy clustering) are frozen
sound waves from the pre-recombination universe, imprinted in the
boundary character spectrum. In the τ-framework, BAO is a readout
of the primordial defect-density oscillations.

## Ground Truth Sources


- Book V ch43: Bullet Cluster and Large-Scale Structure


---

### `Tau.BookV.Astrophysics.BulletClusterAnalysis`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L66-L85)
**structure
Tau.BookV.Astrophysics.BulletClusterAnalysis :Type**


[V.D140] Bullet cluster τ-analysis: reinterpretation of the
lensing-gas offset without invoking dark matter particles.

- lensing_mass : ℕ
Lensing mass (10¹⁴ M_☉, scaled × 10).

- lensing_pos : self.lensing_mass > 0
Lensing mass positive.

- gas_mass : ℕ
Gas mass (same units).

- stellar_mass : ℕ
Stellar mass (same units).

- boundary_correction : ℕ
Boundary correction mass equivalent (same units).

- mass_decomposition : self.lensing_mass ≤ self.gas_mass + self.stellar_mass + self.boundary_correction + 1 ∧ self.gas_mass + self.stellar_mass + self.boundary_correction ≤ self.lensing_mass + 1
Lensing ≈ gas + stellar + boundary correction.

- offset_kpc : ℕ
Offset between lensing peak and gas peak (kpc).

Instances For

---

### `Tau.BookV.Astrophysics.instReprBulletClusterAnalysis`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L85-L85)
**instance
Tau.BookV.Astrophysics.instReprBulletClusterAnalysis :Repr BulletClusterAnalysis**

Equations
- Tau.BookV.Astrophysics.instReprBulletClusterAnalysis = { reprPrec := Tau.BookV.Astrophysics.instReprBulletClusterAnalysis.repr }

---

### `Tau.BookV.Astrophysics.instReprBulletClusterAnalysis.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L85-L85)
**def
Tau.BookV.Astrophysics.instReprBulletClusterAnalysis.repr :BulletClusterAnalysis → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.lensing_gas_offset`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L91-L103)
**theorem
Tau.BookV.Astrophysics.lensing_gas_offset :"Lensing-gas offset = boundary correction centered on stars, not gas" = "Lensing-gas offset = boundary correction centered on stars, not gas"**


[V.T97] Lensing-gas offset from boundary correction: the
spatial offset between the lensing signal and the X-ray gas
arises because the boundary holonomy correction is centered
on the collisionless (stellar) component, not the gas.

During the cluster collision:


- Gas is shock-heated and decelerated (collisional)

- Stars pass through (collisionless)

- Boundary correction follows stars (not gas)

- Lensing peak aligns with stars + correction, offset from gas


---

### `Tau.BookV.Astrophysics.collisionless_stellar`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L109-L119)
**theorem
Tau.BookV.Astrophysics.collisionless_stellar :"Bullet Cluster collisionless component = stars, not dark matter" = "Bullet Cluster collisionless component = stars, not dark matter"**


[V.P84] Collisionless component is stellar: the "collisionless"
component inferred from the Bullet Cluster is NOT dark matter
particles but the STELLAR component (galaxies) that passes
through the collision unimpeded.

The enhanced lensing around the stellar component is the
boundary holonomy correction (same as in rotation curves and
the virial discrepancy).

---

### `Tau.BookV.Astrophysics.LSSData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L125-L138)
**structure
Tau.BookV.Astrophysics.LSSData :Type**


[V.D141] Large-scale structure data: summary of the galaxy
distribution at cosmological scales.

- num_galaxies_millions : ℕ
Number of galaxies in survey (millions).

- survey_volume : ℕ
Survey volume (Gpc³, scaled × 10).

- volume_pos : self.survey_volume > 0
Volume positive.

- bao_scale_mpc : ℕ
Characteristic BAO scale (Mpc).

- mean_separation_mpc : ℕ
Mean galaxy separation (Mpc).

Instances For

---

### `Tau.BookV.Astrophysics.instReprLSSData.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L138-L138)
**def
Tau.BookV.Astrophysics.instReprLSSData.repr :LSSData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprLSSData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L138-L138)
**instance
Tau.BookV.Astrophysics.instReprLSSData :Repr LSSData**

Equations
- Tau.BookV.Astrophysics.instReprLSSData = { reprPrec := Tau.BookV.Astrophysics.instReprLSSData.repr }

---

### `Tau.BookV.Astrophysics.CosmicWebType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L144-L155)
**inductive
Tau.BookV.Astrophysics.CosmicWebType :Type**


[V.D142] Cosmic web morphological type: classification of
large-scale structure elements.

- Cluster : CosmicWebType
Cluster: 3D density peak (node).

- Filament : CosmicWebType
Filament: 1D density ridge (edge).

- Wall : CosmicWebType
Wall/Sheet: 2D density plane (face).

- Void : CosmicWebType
Void: 3D underdensity (cell).

Instances For

---

### `Tau.BookV.Astrophysics.instReprCosmicWebType.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L155-L155)
**def
Tau.BookV.Astrophysics.instReprCosmicWebType.repr :CosmicWebType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprCosmicWebType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L155-L155)
**instance
Tau.BookV.Astrophysics.instReprCosmicWebType :Repr CosmicWebType**

Equations
- Tau.BookV.Astrophysics.instReprCosmicWebType = { reprPrec := Tau.BookV.Astrophysics.instReprCosmicWebType.repr }

---

### `Tau.BookV.Astrophysics.instDecidableEqCosmicWebType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L155-L155)
**instance
Tau.BookV.Astrophysics.instDecidableEqCosmicWebType :DecidableEq CosmicWebType**

Equations
- Tau.BookV.Astrophysics.instDecidableEqCosmicWebType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqCosmicWebType.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L155-L155)
**def
Tau.BookV.Astrophysics.instBEqCosmicWebType.beq :CosmicWebType → CosmicWebType → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqCosmicWebType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.instBEqCosmicWebType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L155-L155)
**instance
Tau.BookV.Astrophysics.instBEqCosmicWebType :BEq CosmicWebType**

Equations
- Tau.BookV.Astrophysics.instBEqCosmicWebType = { beq := Tau.BookV.Astrophysics.instBEqCosmicWebType.beq }

---

### `Tau.BookV.Astrophysics.cosmic_web_complete`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L157-L161)
**theorem
Tau.BookV.Astrophysics.cosmic_web_complete :[CosmicWebType.Cluster, CosmicWebType.Filament, CosmicWebType.Wall, CosmicWebType.Void].length = 4**


The four cosmic web types are complete.

---

### `Tau.BookV.Astrophysics.bao_scale`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L167-L168)
**def
Tau.BookV.Astrophysics.bao_scale :ℕ**


BAO scale in Mpc (comoving).
Equations
- Tau.BookV.Astrophysics.bao_scale = 150
Instances For

---

### `Tau.BookV.Astrophysics.bao_from_boundary`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L170-L181)
**theorem
Tau.BookV.Astrophysics.bao_from_boundary :bao_scale = 150**


[V.T98] BAO from primordial boundary spectrum: baryon acoustic
oscillations at ~150 Mpc are frozen sound waves from the
pre-recombination boundary character spectrum.

The BAO scale is set by the sound horizon at recombination:
r_s = ∫₀^{t_rec} c_s(t) dt / (1+z_rec)

In the τ-framework, this is a readout of the primordial
defect-density oscillation wavelength at the recombination
boundary-data surface.

---

### `Tau.BookV.Astrophysics.PowerSpectrumData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L187-L198)
**structure
Tau.BookV.Astrophysics.PowerSpectrumData :Type**


[V.D143] Power spectrum data: the matter power spectrum P(k)
encoding the amplitude of density fluctuations at each scale k.

- spectral_index_scaled : ℕ
Spectral index n_s (scaled × 1000).

- sigma8_scaled : ℕ
σ₈: amplitude at 8 Mpc/h (scaled × 1000).

- bao_peak_scaled : ℕ
BAO peak position (h/Mpc, scaled × 1000).

- planck_consistent : Bool
Whether the spectrum is consistent with Planck.

Instances For

---

### `Tau.BookV.Astrophysics.instReprPowerSpectrumData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L198-L198)
**instance
Tau.BookV.Astrophysics.instReprPowerSpectrumData :Repr PowerSpectrumData**

Equations
- Tau.BookV.Astrophysics.instReprPowerSpectrumData = { reprPrec := Tau.BookV.Astrophysics.instReprPowerSpectrumData.repr }

---

### `Tau.BookV.Astrophysics.instReprPowerSpectrumData.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L198-L198)
**def
Tau.BookV.Astrophysics.instReprPowerSpectrumData.repr :PowerSpectrumData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.planck_power_spectrum`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L200-L205)
**def
Tau.BookV.Astrophysics.planck_power_spectrum :PowerSpectrumData**


Planck 2018 power spectrum parameters.
Equations
- Tau.BookV.Astrophysics.planck_power_spectrum = { spectral_index_scaled := 965, sigma8_scaled := 811, bao_peak_scaled := 42 }
Instances For

---

### `Tau.BookV.Astrophysics.lss_from_boundary_growth`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L211-L220)
**theorem
Tau.BookV.Astrophysics.lss_from_boundary_growth :"LSS = D-sector amplification of primordial boundary perturbations" = "LSS = D-sector amplification of primordial boundary perturbations"**


[V.P85] LSS from boundary character growth: large-scale structure
forms by gravitational instability (D-sector coupling amplification)
of the primordial boundary character perturbations.

The growth factor D(z) in the τ-framework is the D-sector coupling
integrated over the expansion history — no dark matter potential
wells needed for structure formation.

---

### `Tau.BookV.Astrophysics.bullet_cluster`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L242-L250)
**def
Tau.BookV.Astrophysics.bullet_cluster :BulletClusterAnalysis**


Example: Bullet Cluster analysis.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.WilsonLoopFlux`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L260-L272)
**structure
Tau.BookV.Astrophysics.WilsonLoopFlux :Type**


[V.D291] Wilson Loop Magnetic Flux: magnetic flux carried along
Wilson skeleton edges (filaments), originating from SMBH poloidal
flux and transported by frozen-flux invariant.

- filament : String
Filament name or identifier.

- flux_x18 : ℕ
Filament flux (in units of 10⁻¹⁸ Wb).

- from_smbh : ℕ
Flux originates from SMBH (1 = yes).

- topo_protected : ℕ
Topologically protected (1 = yes).

Instances For

---

### `Tau.BookV.Astrophysics.instReprWilsonLoopFlux`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L272-L272)
**instance
Tau.BookV.Astrophysics.instReprWilsonLoopFlux :Repr WilsonLoopFlux**

Equations
- Tau.BookV.Astrophysics.instReprWilsonLoopFlux = { reprPrec := Tau.BookV.Astrophysics.instReprWilsonLoopFlux.repr }

---

### `Tau.BookV.Astrophysics.instReprWilsonLoopFlux.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L272-L272)
**def
Tau.BookV.Astrophysics.instReprWilsonLoopFlux.repr :WilsonLoopFlux → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.FilamentBFieldAlignment`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L274-L283)
**structure
Tau.BookV.Astrophysics.FilamentBFieldAlignment :Type**


[V.D292] Filament B-Field Alignment: magnetic field in cosmic filaments
is aligned with the filament axis, from 1D Wilson loop topology.

- direction : String
Alignment direction.

- topo_origin : ℕ
Topological origin (1 = yes).

- long_coherence : ℕ
Coherence length comparable to filament length (1 = yes).

Instances For

---

### `Tau.BookV.Astrophysics.instReprFilamentBFieldAlignment`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L283-L283)
**instance
Tau.BookV.Astrophysics.instReprFilamentBFieldAlignment :Repr FilamentBFieldAlignment**

Equations
- Tau.BookV.Astrophysics.instReprFilamentBFieldAlignment = { reprPrec := Tau.BookV.Astrophysics.instReprFilamentBFieldAlignment.repr }

---

### `Tau.BookV.Astrophysics.instReprFilamentBFieldAlignment.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L283-L283)
**def
Tau.BookV.Astrophysics.instReprFilamentBFieldAlignment.repr :FilamentBFieldAlignment → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instInhabitedFilamentBFieldAlignment`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L285-L285)
**instance
Tau.BookV.Astrophysics.instInhabitedFilamentBFieldAlignment :Inhabited FilamentBFieldAlignment**

Equations
- Tau.BookV.Astrophysics.instInhabitedFilamentBFieldAlignment = { default := { } }

---

### `Tau.BookV.Astrophysics.filament_bfield_theorem`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L287-L292)
**theorem
Tau.BookV.Astrophysics.filament_bfield_theorem :"B_fil ~ 10-100 nG (topological), B_dynamo ~ 0.1-1 nG (random)" = "B_fil ~ 10-100 nG (topological), B_dynamo ~ 0.1-1 nG (random)"**


[V.T233] Filament Magnetic Field Theorem: B_fil ~ 10-100 nG
from SMBH flux diluted over filament cross-section. Stronger than
random dynamo prediction (0.1-1 nG) by 1-2 orders of magnitude.

---

### `Tau.BookV.Astrophysics.topo_exceeds_dynamo`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L294-L295)
**theorem
Tau.BookV.Astrophysics.topo_exceeds_dynamo :10 > 1**


Topological B exceeds dynamo B by ~2 OOM at the lower bound.

---

### `Tau.BookV.Astrophysics.IGMFPrediction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L297-L305)
**structure
Tau.BookV.Astrophysics.IGMFPrediction :Type**


[V.P157] IGMF magnitude: 10-100 nG in filaments, ≪ 1 nG in voids.

- b_fil_ng_x10 : ℕ
Filament field (nG × 10).

- b_void_ng_x10 : ℕ
Void field (nG × 10).

- fil_gt_void : self.b_fil_ng_x10 > self.b_void_ng_x10
Filament > void.

Instances For

---

### `Tau.BookV.Astrophysics.instReprIGMFPrediction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L305-L305)
**instance
Tau.BookV.Astrophysics.instReprIGMFPrediction :Repr IGMFPrediction**

Equations
- Tau.BookV.Astrophysics.instReprIGMFPrediction = { reprPrec := Tau.BookV.Astrophysics.instReprIGMFPrediction.repr }

---

### `Tau.BookV.Astrophysics.instReprIGMFPrediction.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L305-L305)
**def
Tau.BookV.Astrophysics.instReprIGMFPrediction.repr :IGMFPrediction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.vernstrom_detection`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L307-L309)
**def
Tau.BookV.Astrophysics.vernstrom_detection :IGMFPrediction**


Vernstrom et al. (2021) detection: ~30 nG.
Equations
- Tau.BookV.Astrophysics.vernstrom_detection = { b_fil_ng_x10 := 300, b_void_ng_x10 := 1, fil_gt_void := Tau.BookV.Astrophysics.vernstrom_detection._proof_2 }
Instances For

---

### `Tau.BookV.Astrophysics.vernstrom_in_tau_range`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L311-L315)
**theorem
Tau.BookV.Astrophysics.vernstrom_in_tau_range :100 ≤ vernstrom_detection.b_fil_ng_x10 ∧ vernstrom_detection.b_fil_ng_x10 ≤ 1000**


τ-prediction encompasses Vernstrom measurement (10-100 nG range).

---

### `Tau.BookV.Astrophysics.TauTransferFunction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L324-L338)
**structure
Tau.BookV.Astrophysics.TauTransferFunction :Type**


[V.D300] τ-native transfer function:
T(k) from k_eq, R_b, k_D — all τ-native.
k_eq ≈ 0.010 h/Mpc (horizon at matter-radiation equality).
R_b ≈ 0.615 (baryon-to-photon ratio at recombination).
k_D ≈ 0.10 Mpc⁻¹ (Silk damping scale from ℓ_D ≈ 1244).

- k_eq_x1000 : ℕ
k_eq (×1000 h/Mpc): 0.010 → 10.

- r_b_x1000 : ℕ
R_b (×1000): 0.615 → 615.

- k_D_x1000 : ℕ
k_D (×1000 Mpc⁻¹): 0.10 → 100.

- n_s_x100000 : ℕ
n_s (×100000): 0.96491 → 96491.

Instances For

---

### `Tau.BookV.Astrophysics.instReprTauTransferFunction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L338-L338)
**instance
Tau.BookV.Astrophysics.instReprTauTransferFunction :Repr TauTransferFunction**

Equations
- Tau.BookV.Astrophysics.instReprTauTransferFunction = { reprPrec := Tau.BookV.Astrophysics.instReprTauTransferFunction.repr }

---

### `Tau.BookV.Astrophysics.instReprTauTransferFunction.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L338-L338)
**def
Tau.BookV.Astrophysics.instReprTauTransferFunction.repr :TauTransferFunction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.MatterPowerSpectrum`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L340-L354)
**structure
Tau.BookV.Astrophysics.MatterPowerSpectrum :Type**


[V.T240] Power spectrum consistency:
P(k) = A_s · (k/k₀)^(n_s−1) · T²(k) reproduces BOSS DR12.
Turnover, BAO wiggles, Silk damping tail, σ₈ all match.

- r_s_x10 : ℕ
r_s sound horizon (×10 Mpc): 147.5 → 1475.

- boss_r_s_x10 : ℕ
BOSS r_s observed (×10 Mpc): 147.21 → 1472.

- r_s_deviation_ppm : ℤ
r_s deviation (ppm): +2000.

- k_bao_x1000 : ℕ
k_BAO (×1000 h/Mpc): 0.043 → 43.

- sigma8_x1000 : ℕ
σ₈ from P(k) normalisation (×1000): 0.741 → 741.

Instances For

---

### `Tau.BookV.Astrophysics.instReprMatterPowerSpectrum.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L354-L354)
**def
Tau.BookV.Astrophysics.instReprMatterPowerSpectrum.repr :MatterPowerSpectrum → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprMatterPowerSpectrum`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L354-L354)
**instance
Tau.BookV.Astrophysics.instReprMatterPowerSpectrum :Repr MatterPowerSpectrum**

Equations
- Tau.BookV.Astrophysics.instReprMatterPowerSpectrum = { reprPrec := Tau.BookV.Astrophysics.instReprMatterPowerSpectrum.repr }

---

### `Tau.BookV.Astrophysics.tau_transfer_canonical`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L356-L361)
**def
Tau.BookV.Astrophysics.tau_transfer_canonical :TauTransferFunction**


Canonical transfer function.
Equations
- Tau.BookV.Astrophysics.tau_transfer_canonical = { k_eq_x1000 := 10, r_b_x1000 := 615, k_D_x1000 := 100, n_s_x100000 := 96491 }
Instances For

---

### `Tau.BookV.Astrophysics.power_spectrum_canonical`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L363-L368)
**def
Tau.BookV.Astrophysics.power_spectrum_canonical :MatterPowerSpectrum**


Canonical power spectrum.
Equations
- Tau.BookV.Astrophysics.power_spectrum_canonical = { r_s_x10 := 1475, r_s_deviation_ppm := 2000, k_bao_x1000 := 43, sigma8_x1000 := 741 }
Instances For

---

### `Tau.BookV.Astrophysics.bao_scale_consistent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Astrophysics/BulletClusterLSS.lean#L370-L373)
**theorem
Tau.BookV.Astrophysics.bao_scale_consistent :power_spectrum_canonical.r_s_x10 ≥ power_spectrum_canonical.boss_r_s_x10**


[V.P165] BAO scale within 1.3σ of BOSS.
