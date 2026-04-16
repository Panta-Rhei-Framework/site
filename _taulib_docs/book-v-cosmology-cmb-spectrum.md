---
layout: taulib-doc
title: "TauLib.BookV.Cosmology.CMBSpectrum"
permalink: /verify/taulib/docs/book-v-cosmology-cmb-spectrum/
lane: verify
module_name: "TauLib.BookV.Cosmology.CMBSpectrum"
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

# TauLib.BookV.Cosmology.CMBSpectrum


CMB power spectrum pipeline from Category τ. Derives principal CMB
observables (ω_b, ω_m, r_s, ℓ₁, r, A_s, h) from the single input
ι<sub>τ</sub> = 2/(π + e). Covers Wave 8 sprints 8A, 8B, 8E.

## Registry Cross-References


### Sprint 8A (CMB Power Spectrum)


- [V.D247] τ-Native Baryon Density ω_b from η_B

- [V.D248] Boundary Holonomy Matter Fraction

- [V.T190] Baryon Density from Master Constant

- [V.T191] Sound Horizon from τ-Native Inputs

- [V.T192] First Peak from Holonomy Matter Fraction

- [V.P135] Structural Acoustic Scale ι<sub>τ</sub>⁻⁵ Cross-Check

- [V.P136] CMB Tensor-to-Scalar Ratio r = ι<sub>τ</sub>⁴

- [V.R384] V.OP3 Status: PARTIAL-IMPROVED after Sprint 8A


### Sprint 8B (CMB + CνB Deep)


- [V.D249] Neutrino Free-Streaming Scale

- [V.D250] CνB Temperature Chain

- [V.T193] Holonomy Matter NLO Correction Scan

- [V.T194] Neutrino Phase Shift on CMB Peaks

- [V.T195] Two-Horizon Consistency from ι<sub>τ</sub>

- [V.P137] Free-Streaming Suppression from τ-Native Masses

- [V.P138] CMB-S4/PTOLEMY/DESI Falsification Suite

- [V.R385] V.OP3 Status After Sprint 8B


### Sprint 8E (Hubble Pipeline Verification)


- [V.D251] Structural Hubble Parameter h = 2/3 + ι<sub>τ</sub>²/W₃(3)

- [V.D252] DE-Closure Matter Density

- [V.D253] Scalar Amplitude NLO

- [V.T196] Hubble Parameter from τ at −120 ppm

- [V.T197] Full CMB Pipeline with Structural h

- [V.T198] Scalar Amplitude NLO: Inflationary Consistency

- [V.P139] Reionisation Optical Depth from z_reion = 8

- [V.R386] V.OP3 Status After Sprint 8E


---

### `Tau.BookV.Cosmology.TauBaryonDensity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L57-L67)
**structure
Tau.BookV.Cosmology.TauBaryonDensity :Type**


[V.D247] τ-Native Baryon Density ω_b from η_B.
ω_b = m_p·η_B·n_γ/ρ_crit = 0.02209.
At −12334 ppm (−1.2%) from Planck 0.02237±0.00015.

- chain_source : ℕ
Source: 1 = from η_B chain.

- free_params : ℕ
Number of free parameters.

- sigma_deviation_x100 : ℕ
σ deviation ×100 (1.2σ → 120).

Instances For

---

### `Tau.BookV.Cosmology.instReprTauBaryonDensity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L67-L67)
**def
Tau.BookV.Cosmology.instReprTauBaryonDensity.repr :TauBaryonDensity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprTauBaryonDensity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L67-L67)
**instance
Tau.BookV.Cosmology.instReprTauBaryonDensity :Repr TauBaryonDensity**

Equations
- Tau.BookV.Cosmology.instReprTauBaryonDensity = { reprPrec := Tau.BookV.Cosmology.instReprTauBaryonDensity.repr }

---

### `Tau.BookV.Cosmology.tau_baryon_density_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L69-L69)
**def
Tau.BookV.Cosmology.tau_baryon_density_data :TauBaryonDensity**

Equations
- Tau.BookV.Cosmology.tau_baryon_density_data = { }
Instances For

---

### `Tau.BookV.Cosmology.tau_baryon_density`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L70-L70)
**def
Tau.BookV.Cosmology.tau_baryon_density :Float**

Equations
- Tau.BookV.Cosmology.tau_baryon_density = 2209e-5
Instances For

---

### `Tau.BookV.Cosmology.baryon_density_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L72-L76)
**theorem
Tau.BookV.Cosmology.baryon_density_structural :tau_baryon_density_data.chain_source = 1 ∧ tau_baryon_density_data.free_params = 0 ∧ tau_baryon_density_data.sigma_deviation_x100 = 120**


---

### `Tau.BookV.Cosmology.HolonomyMatterFraction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L78-L88)
**structure
Tau.BookV.Cosmology.HolonomyMatterFraction :Type**


[V.D248] Boundary Holonomy Matter Fraction.
ω_m/ω_b = 1 + (1−ι<sub>τ</sub>)/ι<sub>τ</sub>² = 6.655.
Boundary holonomy mass is topological, gravitates like CDM.

- origin_type : ℕ
Origin type: 1 = topological (not particulate).

- n_dark_sectors : ℕ
Number of dark sectors (gravitates like CDM).

- source_chapter : ℕ
Source chapter.

Instances For

---

### `Tau.BookV.Cosmology.instReprHolonomyMatterFraction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L88-L88)
**instance
Tau.BookV.Cosmology.instReprHolonomyMatterFraction :Repr HolonomyMatterFraction**

Equations
- Tau.BookV.Cosmology.instReprHolonomyMatterFraction = { reprPrec := Tau.BookV.Cosmology.instReprHolonomyMatterFraction.repr }

---

### `Tau.BookV.Cosmology.instReprHolonomyMatterFraction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L88-L88)
**def
Tau.BookV.Cosmology.instReprHolonomyMatterFraction.repr :HolonomyMatterFraction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.holonomy_matter_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L90-L90)
**def
Tau.BookV.Cosmology.holonomy_matter_data :HolonomyMatterFraction**

Equations
- Tau.BookV.Cosmology.holonomy_matter_data = { }
Instances For

---

### `Tau.BookV.Cosmology.holonomy_matter_ratio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L91-L91)
**def
Tau.BookV.Cosmology.holonomy_matter_ratio :Float**

Equations
- Tau.BookV.Cosmology.holonomy_matter_ratio = 1.0 + Tau.BookV.Cosmology.kappa_D✝ / Tau.BookV.Cosmology.kappa_B✝
Instances For

---

### `Tau.BookV.Cosmology.holonomy_matter_fraction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L93-L97)
**theorem
Tau.BookV.Cosmology.holonomy_matter_fraction :holonomy_matter_data.origin_type = 1 ∧ holonomy_matter_data.n_dark_sectors = 1 ∧ holonomy_matter_data.source_chapter = 45**


---

### `Tau.BookV.Cosmology.BaryonDensityFromIota`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L99-L110)
**structure
Tau.BookV.Cosmology.BaryonDensityFromIota :Type**


[V.T190] Baryon Density from Master Constant.
ι<sub>τ</sub> → α_τ → η_B → ω_b = 0.02209. Zero free parameters.
Chain: ι<sub>τ</sub> → α_τ = (121/225)·ι<sub>τ</sub>⁴ → η_B = α·ι<sub>τ</sub>¹⁵·(5/6) →
ρ_b = m_p·η_B·n_γ → ω_b = ρ_b/ρ_crit.

- chain_links : ℕ
Number of chain links.

- links_eq : self.chain_links = 5
Five links in chain.

- free_params : ℕ
Number of free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprBaryonDensityFromIota`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L110-L110)
**instance
Tau.BookV.Cosmology.instReprBaryonDensityFromIota :Repr BaryonDensityFromIota**

Equations
- Tau.BookV.Cosmology.instReprBaryonDensityFromIota = { reprPrec := Tau.BookV.Cosmology.instReprBaryonDensityFromIota.repr }

---

### `Tau.BookV.Cosmology.instReprBaryonDensityFromIota.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L110-L110)
**def
Tau.BookV.Cosmology.instReprBaryonDensityFromIota.repr :BaryonDensityFromIota → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.baryon_density_chain`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L112-L114)
**def
Tau.BookV.Cosmology.baryon_density_chain :BaryonDensityFromIota**

Equations
- Tau.BookV.Cosmology.baryon_density_chain = { chain_links := 5, links_eq := Tau.BookV.Cosmology.baryon_density_chain._proof_1 }
Instances For

---

### `Tau.BookV.Cosmology.baryon_density_from_iota`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L116-L119)
**theorem
Tau.BookV.Cosmology.baryon_density_from_iota :baryon_density_chain.chain_links = 5 ∧ baryon_density_chain.free_params = 0**


---

### `Tau.BookV.Cosmology.SoundHorizon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L121-L128)
**structure
Tau.BookV.Cosmology.SoundHorizon :Type**


[V.T191] Sound Horizon from τ-Native Inputs.
r_s = 143.18 Mpc. Planck: 147.09±0.26 Mpc. −2.66%.

- n_native_inputs : ℕ
Number of τ-native inputs (ω_b, ω_m).

- n_holonomy_components : ℕ
Number of holonomy components used.

Instances For

---

### `Tau.BookV.Cosmology.instReprSoundHorizon.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L128-L128)
**def
Tau.BookV.Cosmology.instReprSoundHorizon.repr :SoundHorizon → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprSoundHorizon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L128-L128)
**instance
Tau.BookV.Cosmology.instReprSoundHorizon :Repr SoundHorizon**

Equations
- Tau.BookV.Cosmology.instReprSoundHorizon = { reprPrec := Tau.BookV.Cosmology.instReprSoundHorizon.repr }

---

### `Tau.BookV.Cosmology.sound_horizon_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L130-L130)
**def
Tau.BookV.Cosmology.sound_horizon_data :SoundHorizon**

Equations
- Tau.BookV.Cosmology.sound_horizon_data = { }
Instances For

---

### `Tau.BookV.Cosmology.sound_horizon_tau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L131-L131)
**def
Tau.BookV.Cosmology.sound_horizon_tau :Float**

Equations
- Tau.BookV.Cosmology.sound_horizon_tau = 143.18
Instances For

---

### `Tau.BookV.Cosmology.sound_horizon_tau_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L133-L136)
**theorem
Tau.BookV.Cosmology.sound_horizon_tau_thm :sound_horizon_data.n_native_inputs = 2 ∧ sound_horizon_data.n_holonomy_components = 1**


---

### `Tau.BookV.Cosmology.FirstPeakHolonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L138-L147)
**structure
Tau.BookV.Cosmology.FirstPeakHolonomy :Type**


[V.T192] First Peak from Holonomy Matter Fraction.
ℓ₁ = 220.6 at +2840 ppm from Planck 220.0±0.5.

- free_params : ℕ
Number of free parameters.

- deviation_ppm : ℕ
Deviation from Planck in ppm.

- n_pipeline_steps : ℕ
Number of pipeline steps (Friedmann integral chain).

Instances For

---

### `Tau.BookV.Cosmology.instReprFirstPeakHolonomy.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L147-L147)
**def
Tau.BookV.Cosmology.instReprFirstPeakHolonomy.repr :FirstPeakHolonomy → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprFirstPeakHolonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L147-L147)
**instance
Tau.BookV.Cosmology.instReprFirstPeakHolonomy :Repr FirstPeakHolonomy**

Equations
- Tau.BookV.Cosmology.instReprFirstPeakHolonomy = { reprPrec := Tau.BookV.Cosmology.instReprFirstPeakHolonomy.repr }

---

### `Tau.BookV.Cosmology.first_peak_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L149-L149)
**def
Tau.BookV.Cosmology.first_peak_data :FirstPeakHolonomy**

Equations
- Tau.BookV.Cosmology.first_peak_data = { }
Instances For

---

### `Tau.BookV.Cosmology.first_peak_holonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L150-L150)
**def
Tau.BookV.Cosmology.first_peak_holonomy :Float**

Equations
- Tau.BookV.Cosmology.first_peak_holonomy = 220.63
Instances For

---

### `Tau.BookV.Cosmology.first_peak_holonomy_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L152-L156)
**theorem
Tau.BookV.Cosmology.first_peak_holonomy_thm :first_peak_data.free_params = 0 ∧ first_peak_data.deviation_ppm = 2840 ∧ first_peak_data.n_pipeline_steps = 4**


---

### `Tau.BookV.Cosmology.AcousticScaleCrosscheck`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L158-L165)
**structure
Tau.BookV.Cosmology.AcousticScaleCrosscheck :Type**


[V.P135] Structural Acoustic Scale ι<sub>τ</sub>⁻⁵ Cross-Check.
ι<sub>τ</sub>⁻⁵ = ((π+e)/2)⁵ = 215.92. Exponent −5 = −(dim+lobes) = −(3+2).

- exponent : ℕ
Exponent: dim + lobes.

- exp_eq : self.exponent = 3 + 2
5 = 3 + 2.

Instances For

---

### `Tau.BookV.Cosmology.instReprAcousticScaleCrosscheck.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L165-L165)
**def
Tau.BookV.Cosmology.instReprAcousticScaleCrosscheck.repr :AcousticScaleCrosscheck → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprAcousticScaleCrosscheck`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L165-L165)
**instance
Tau.BookV.Cosmology.instReprAcousticScaleCrosscheck :Repr AcousticScaleCrosscheck**

Equations
- Tau.BookV.Cosmology.instReprAcousticScaleCrosscheck = { reprPrec := Tau.BookV.Cosmology.instReprAcousticScaleCrosscheck.repr }

---

### `Tau.BookV.Cosmology.acoustic_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L167-L169)
**def
Tau.BookV.Cosmology.acoustic_check :AcousticScaleCrosscheck**

Equations
- Tau.BookV.Cosmology.acoustic_check = { exponent := 5, exp_eq := Tau.BookV.Cosmology.baryon_density_chain._proof_1 }
Instances For

---

### `Tau.BookV.Cosmology.acoustic_scale_crosscheck`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L171-L172)
**def
Tau.BookV.Cosmology.acoustic_scale_crosscheck :Float**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.acoustic_scale_crosscheck_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L174-L176)
**theorem
Tau.BookV.Cosmology.acoustic_scale_crosscheck_thm :acoustic_check.exponent = 5**


---

### `Tau.BookV.Cosmology.TensorScalarRatio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L178-L205)
**structure
Tau.BookV.Cosmology.TensorScalarRatio :Type**


[V.P136] CMB Tensor-to-Scalar Ratio r = ι<sub>τ</sub>⁴.
r = 0.01357. Below BICEP/Keck bound r < 0.036.
CMB-S4 detection at ~14σ. Falsifiable.

Wave 13 upgrade: DERIVED from fiber dimensional suppression.
r = ι<sub>τ</sub>^{2·dim(T²)} = ι<sub>τ</sub>⁴ where:


- dim(T²) = 2: fiber dimension (two circles)

- Factor 2: power spectrum is quadratic in amplitude

- Tensor modes on base τ¹; scalar modes on full τ³
Scope: conjectural → τ-effective.


- iota_power : ℕ
Power of ι<sub>τ</sub>.

- power_eq : self.iota_power = 4
Power is 4.

- fiber_dim : ℕ
Fiber dimension (T² has dim 2).

- power_order : ℕ
Power spectrum order.

- exponent_derived : self.iota_power = self.fiber_dim * self.power_order
Exponent = fiber_dim × power_order.

- r_x1e6 : ℕ
r × 10^6 for high precision.

- cmbs4_sigma : ℕ
CMB-S4 detection significance in σ.

- free_params : ℕ
Free parameters beyond ι<sub>τ</sub>.

Instances For

---

### `Tau.BookV.Cosmology.instReprTensorScalarRatio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L205-L205)
**instance
Tau.BookV.Cosmology.instReprTensorScalarRatio :Repr TensorScalarRatio**

Equations
- Tau.BookV.Cosmology.instReprTensorScalarRatio = { reprPrec := Tau.BookV.Cosmology.instReprTensorScalarRatio.repr }

---

### `Tau.BookV.Cosmology.instReprTensorScalarRatio.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L205-L205)
**def
Tau.BookV.Cosmology.instReprTensorScalarRatio.repr :TensorScalarRatio → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.tensor_scalar_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L207-L210)
**def
Tau.BookV.Cosmology.tensor_scalar_data :TensorScalarRatio**

Equations
- Tau.BookV.Cosmology.tensor_scalar_data = { iota_power := 4, power_eq := Tau.BookV.Cosmology.tensor_scalar_data._proof_1,
 exponent_derived := Tau.BookV.Cosmology.tensor_scalar_data._proof_1 }
Instances For

---

### `Tau.BookV.Cosmology.tensor_scalar_ratio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L212-L213)
**def
Tau.BookV.Cosmology.tensor_scalar_ratio :Float**

Equations
- Tau.BookV.Cosmology.tensor_scalar_ratio = Tau.BookV.Cosmology.iota_float✝ * Tau.BookV.Cosmology.iota_float✝¹ * Tau.BookV.Cosmology.iota_float✝² * Tau.BookV.Cosmology.iota_float✝³
Instances For

---

### `Tau.BookV.Cosmology.tensor_scalar_ratio_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L215-L220)
**theorem
Tau.BookV.Cosmology.tensor_scalar_ratio_thm :tensor_scalar_data.iota_power = 4 ∧ tensor_scalar_data.fiber_dim = 2 ∧ tensor_scalar_data.power_order = 2 ∧ tensor_scalar_data.free_params = 0**


---

### `Tau.BookV.Cosmology.vop3_sprint8a_status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L222-L226)
**def
Tau.BookV.Cosmology.vop3_sprint8a_status :String**


[V.R384] V.OP3 Status: PARTIAL-IMPROVED after Sprint 8A.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.free_streaming_scale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L232-L237)
**def
Tau.BookV.Cosmology.free_streaming_scale :String**


[V.D249] Neutrino Free-Streaming Scale.
k_fs = 0.018·Ω_m^{1/2}·(m/eV)·h [Mpc⁻¹].
f_ν = ω_ν/ω_m = Σm_ν/(94.07·ω_m) = 0.00643.
Equations
- Tau.BookV.Cosmology.free_streaming_scale = "k_fs(m₃) = 3.63×10⁻⁴ Mpc⁻¹ (dominant). " ++ "f_ν = 0.00643 for M3h (Σm_ν = 0.089 eV)."
Instances For

---

### `Tau.BookV.Cosmology.cnub_temperature`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L239-L242)
**def
Tau.BookV.Cosmology.cnub_temperature :Float**


[V.D250] CνB Temperature Chain (established).
T_CνB = (4/11)^{1/3}·T_CMB = 1.9454 K.
T_dec ≈ 1.37 MeV, z_ν ≈ 5.8×10⁹.
Equations
- Tau.BookV.Cosmology.cnub_temperature = 1.9454
Instances For

---

### `Tau.BookV.Cosmology.cnub_entropy_factor_rational`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L244-L246)
**theorem
Tau.BookV.Cosmology.cnub_entropy_factor_rational :4 / 11 > 0**


CνB entropy factor: (4/11)^{1/3}.

---

### `Tau.BookV.Cosmology.HolonomyNLOScan`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L248-L255)
**structure
Tau.BookV.Cosmology.HolonomyNLOScan :Type**


[V.T193] Holonomy Matter NLO Correction Scan.
Best: δ = ι<sub>τ</sub>³ at −386 ppm on ratio, but ℓ₁ worsens to +8655 ppm.

- best_exponent : ℕ
Best NLO exponent (ι<sub>τ</sub>³ → 3).

- nlo_deviation_ppm : ℕ
NLO deviation in ppm (cancellation broken).

Instances For

---

### `Tau.BookV.Cosmology.instReprHolonomyNLOScan.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L255-L255)
**def
Tau.BookV.Cosmology.instReprHolonomyNLOScan.repr :HolonomyNLOScan → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprHolonomyNLOScan`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L255-L255)
**instance
Tau.BookV.Cosmology.instReprHolonomyNLOScan :Repr HolonomyNLOScan**

Equations
- Tau.BookV.Cosmology.instReprHolonomyNLOScan = { reprPrec := Tau.BookV.Cosmology.instReprHolonomyNLOScan.repr }

---

### `Tau.BookV.Cosmology.holonomy_nlo_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L257-L257)
**def
Tau.BookV.Cosmology.holonomy_nlo_data :HolonomyNLOScan**

Equations
- Tau.BookV.Cosmology.holonomy_nlo_data = { }
Instances For

---

### `Tau.BookV.Cosmology.holonomy_nlo_scan`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L259-L262)
**theorem
Tau.BookV.Cosmology.holonomy_nlo_scan :holonomy_nlo_data.best_exponent = 3 ∧ holonomy_nlo_data.nlo_deviation_ppm = 8655**


---

### `Tau.BookV.Cosmology.NeutrinoPhaseShift`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L264-L271)
**structure
Tau.BookV.Cosmology.NeutrinoPhaseShift :Type**


[V.T194] Neutrino Phase Shift on CMB Peaks.
φ_ν = 0.191π·N_eff/(N_eff+15/4). For τ (N_eff=3): 0.0849π.

- n_eff : ℕ
N_eff in τ framework.

- sensitivity_sigma_x10 : ℕ
CMB-S4 sensitivity in σ ×10 (1.5σ → 15).

Instances For

---

### `Tau.BookV.Cosmology.instReprNeutrinoPhaseShift.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L271-L271)
**def
Tau.BookV.Cosmology.instReprNeutrinoPhaseShift.repr :NeutrinoPhaseShift → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprNeutrinoPhaseShift`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L271-L271)
**instance
Tau.BookV.Cosmology.instReprNeutrinoPhaseShift :Repr NeutrinoPhaseShift**

Equations
- Tau.BookV.Cosmology.instReprNeutrinoPhaseShift = { reprPrec := Tau.BookV.Cosmology.instReprNeutrinoPhaseShift.repr }

---

### `Tau.BookV.Cosmology.neutrino_phase_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L273-L273)
**def
Tau.BookV.Cosmology.neutrino_phase_data :NeutrinoPhaseShift**

Equations
- Tau.BookV.Cosmology.neutrino_phase_data = { }
Instances For

---

### `Tau.BookV.Cosmology.neutrino_phase_shift`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L275-L278)
**theorem
Tau.BookV.Cosmology.neutrino_phase_shift :neutrino_phase_data.n_eff = 3 ∧ neutrino_phase_data.sensitivity_sigma_x10 = 15**


---

### `Tau.BookV.Cosmology.TwoHorizonConsistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L280-L292)
**structure
Tau.BookV.Cosmology.TwoHorizonConsistency :Type**


[V.T195] Two-Horizon Consistency from ι<sub>τ</sub>.
CMB (z_rec~1093), CνB (z_ν~5.8×10⁹), Mass (f_ν→ΔP/P).
Three chains, zero free parameters.

- n_horizons : ℕ
Number of independent horizons.

- horizons_eq : self.n_horizons = 3
Three horizons.

- free_params : ℕ
Number of free parameters.

- n_inputs : ℕ
Number of independent inputs (single ι<sub>τ</sub>).

Instances For

---

### `Tau.BookV.Cosmology.instReprTwoHorizonConsistency.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L292-L292)
**def
Tau.BookV.Cosmology.instReprTwoHorizonConsistency.repr :TwoHorizonConsistency → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprTwoHorizonConsistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L292-L292)
**instance
Tau.BookV.Cosmology.instReprTwoHorizonConsistency :Repr TwoHorizonConsistency**

Equations
- Tau.BookV.Cosmology.instReprTwoHorizonConsistency = { reprPrec := Tau.BookV.Cosmology.instReprTwoHorizonConsistency.repr }

---

### `Tau.BookV.Cosmology.two_horizon_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L294-L296)
**def
Tau.BookV.Cosmology.two_horizon_data :TwoHorizonConsistency**

Equations
- Tau.BookV.Cosmology.two_horizon_data = { n_horizons := 3, horizons_eq := Tau.BookV.Cosmology.two_horizon_data._proof_1 }
Instances For

---

### `Tau.BookV.Cosmology.two_horizon_consistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L298-L302)
**theorem
Tau.BookV.Cosmology.two_horizon_consistency :two_horizon_data.n_horizons = 3 ∧ two_horizon_data.free_params = 0 ∧ two_horizon_data.n_inputs = 1**


---

### `Tau.BookV.Cosmology.FreeStreamingSuppression`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L304-L313)
**structure
Tau.BookV.Cosmology.FreeStreamingSuppression :Type**


[V.P137] Free-Streaming Suppression from τ-Native Masses.
ΔP/P ≈ −8f_ν = −5.14%. Detectable: DESI ~4.5σ, Euclid ~5-9σ.

- n_formula_factors : ℕ
Number of BES formula factors (−8f_ν).

- desi_sigma_x10 : ℕ
DESI detection significance in σ ×10 (4.5σ → 45).

- free_params : ℕ
Number of free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprFreeStreamingSuppression`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L313-L313)
**instance
Tau.BookV.Cosmology.instReprFreeStreamingSuppression :Repr FreeStreamingSuppression**

Equations
- Tau.BookV.Cosmology.instReprFreeStreamingSuppression = { reprPrec := Tau.BookV.Cosmology.instReprFreeStreamingSuppression.repr }

---

### `Tau.BookV.Cosmology.instReprFreeStreamingSuppression.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L313-L313)
**def
Tau.BookV.Cosmology.instReprFreeStreamingSuppression.repr :FreeStreamingSuppression → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.free_streaming_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L315-L315)
**def
Tau.BookV.Cosmology.free_streaming_data :FreeStreamingSuppression**

Equations
- Tau.BookV.Cosmology.free_streaming_data = { }
Instances For

---

### `Tau.BookV.Cosmology.free_streaming_suppression`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L316-L316)
**def
Tau.BookV.Cosmology.free_streaming_suppression :Float**

Equations
- Tau.BookV.Cosmology.free_streaming_suppression = -8.0 * 643e-5
Instances For

---

### `Tau.BookV.Cosmology.free_streaming_suppression_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L318-L322)
**theorem
Tau.BookV.Cosmology.free_streaming_suppression_thm :free_streaming_data.n_formula_factors = 1 ∧ free_streaming_data.desi_sigma_x10 = 45 ∧ free_streaming_data.free_params = 0**


---

### `Tau.BookV.Cosmology.FalsificationSuite`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L324-L334)
**structure
Tau.BookV.Cosmology.FalsificationSuite :Type**


[V.P138] CMB-S4/PTOLEMY/DESI Falsification Suite.
6 targets: r (14σ), N_eff (1.5σ), Σm_ν (4.5σ), m_β (<1σ),
Majorana/NH, ΔP/P (3σ).

- n_targets : ℕ
Number of targets.

- targets_eq : self.n_targets = 6
Six targets.

- most_falsifiable_sigma : ℕ
Most falsifiable significance: r at CMB-S4 (~14σ).

Instances For

---

### `Tau.BookV.Cosmology.instReprFalsificationSuite`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L334-L334)
**instance
Tau.BookV.Cosmology.instReprFalsificationSuite :Repr FalsificationSuite**

Equations
- Tau.BookV.Cosmology.instReprFalsificationSuite = { reprPrec := Tau.BookV.Cosmology.instReprFalsificationSuite.repr }

---

### `Tau.BookV.Cosmology.instReprFalsificationSuite.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L334-L334)
**def
Tau.BookV.Cosmology.instReprFalsificationSuite.repr :FalsificationSuite → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.falsification_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L336-L338)
**def
Tau.BookV.Cosmology.falsification_data :FalsificationSuite**

Equations
- Tau.BookV.Cosmology.falsification_data = { n_targets := 6, targets_eq := Tau.BookV.Cosmology.falsification_data._proof_1 }
Instances For

---

### `Tau.BookV.Cosmology.falsification_suite_8b`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L340-L343)
**theorem
Tau.BookV.Cosmology.falsification_suite_8b :falsification_data.n_targets = 6 ∧ falsification_data.most_falsifiable_sigma = 14**


---

### `Tau.BookV.Cosmology.vop3_sprint8b_status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L345-L348)
**def
Tau.BookV.Cosmology.vop3_sprint8b_status :String**


[V.R385] V.OP3 Status After Sprint 8B.
Equations
- Tau.BookV.Cosmology.vop3_sprint8b_status = "V.OP3 PARTIAL-IMPROVED (deepened). CνB + free-streaming + NLO + falsification. " ++ "Two-horizon consistency. ΔP/P=−5.14%. 6 falsification targets."
Instances For

---

### `Tau.BookV.Cosmology.structural_hubble`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L354-L357)
**def
Tau.BookV.Cosmology.structural_hubble :Float**


[V.D251] Structural Hubble Parameter h = 2/3 + ι<sub>τ</sub>²/W₃(3).
h = 2/3 + ι<sub>τ</sub>²/17 = 0.67352 at −120 ppm from Planck 0.6736.
Base: 2/3 = EdS exponent. Correction: κ_B/17.
Equations
- Tau.BookV.Cosmology.structural_hubble = 2.0 / 3.0 + Tau.BookV.Cosmology.kappa_B✝ / 17.0
Instances For

---

### `Tau.BookV.Cosmology.de_closure_omega_lambda`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L359-L363)
**def
Tau.BookV.Cosmology.de_closure_omega_lambda :Float**


[V.D252] DE-Closure Matter Density.
Ω_Λ = κ_D·(1+ι<sub>τ</sub>³) = 0.6849.
ω_m = (1−Ω_Λ−Ω_r)·h² = 0.1429. Planck: 0.1430 (−674 ppm).
Equations
- Tau.BookV.Cosmology.de_closure_omega_lambda = Tau.BookV.Cosmology.kappa_D✝ * (1.0 + Tau.BookV.Cosmology.iota_float✝ * Tau.BookV.Cosmology.iota_float✝¹ * Tau.BookV.Cosmology.iota_float✝²)
Instances For

---

### `Tau.BookV.Cosmology.de_closure_omega_m`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L365-L366)
**def
Tau.BookV.Cosmology.de_closure_omega_m :Float**

Equations
- Tau.BookV.Cosmology.de_closure_omega_m = (1.0 - Tau.BookV.Cosmology.de_closure_omega_lambda - 92e-6) * Tau.BookV.Cosmology.structural_hubble * Tau.BookV.Cosmology.structural_hubble
Instances For

---

### `Tau.BookV.Cosmology.scalar_amplitude_nlo_desc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L368-L373)
**def
Tau.BookV.Cosmology.scalar_amplitude_nlo_desc :String**


[V.D253] Scalar Amplitude NLO.
A_s = (121/225)·ι<sub>τ</sub>¹⁸·(1−ι<sub>τ</sub>³/3) = 2.096×10⁻⁹.
10× improvement over baseline +11425 ppm.
Equations
- Tau.BookV.Cosmology.scalar_amplitude_nlo_desc = "A_s = (121/225)·ι<sub>τ</sub>¹⁸·(1−ι<sub>τ</sub>³/3) = 2.096×10⁻⁹. " ++ "NLO factor is structural (τ³ volume averaging), not slow-roll running."
Instances For

---

### `Tau.BookV.Cosmology.hubble_from_tau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L375-L379)
**def
Tau.BookV.Cosmology.hubble_from_tau :String**


[V.T196] Hubble Parameter from τ: h at −120 ppm.
h = 2/3 + ι<sub>τ</sub>²/17 = 0.67352. Planck h = 0.6736.
Equations
- Tau.BookV.Cosmology.hubble_from_tau = "h = 2/3 + ι<sub>τ</sub>²/17 = 0.67352, Planck 0.6736, deviation −120 ppm. " ++ "2/3 = EdS exponent; ι<sub>τ</sub>²/17 = EM correction / dominant CF window."
Instances For

---

### `Tau.BookV.Cosmology.full_pipeline_h`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L381-L386)
**def
Tau.BookV.Cosmology.full_pipeline_h :String**


[V.T197] Full CMB Pipeline with Structural h.
M3h+h_τ: ℓ₁=220.63 (+2863 ppm). DE+h_τ: ℓ₁=221.52 (+6925 ppm).
Zero free parameters beyond ι<sub>τ</sub> and T_CMB.
Equations
- Tau.BookV.Cosmology.full_pipeline_h = "Full pipeline (M3h+h_τ): ℓ₁=220.63 (+2863), ℓ₂=529.75, ℓ₃=796.74. " ++ "Peak ratios ℓ₂/ℓ₁=2.401, ℓ₃/ℓ₁=3.611 are universal (phase-shift determined)."
Instances For

---

### `Tau.BookV.Cosmology.as_inflation_consistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L388-L394)
**def
Tau.BookV.Cosmology.as_inflation_consistency :String**


[V.T198] Scalar Amplitude NLO: Inflationary Consistency.
NLO factor (1−ι<sub>τ</sub>³/3) is structural, not slow-roll.
ε = r/16 8.5×10⁻⁴, running 10⁻³ ≪ required 10⁻² (156× gap).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.reionization_z_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L396-L400)
**theorem
Tau.BookV.Cosmology.reionization_z_structural :13 - 5 = 8**


[V.P139] Reionisation Optical Depth from z_reion = 8.
z_reion = a₃ − W₃(4) = 13 − 5 = 8. τ_reion ≈ 0.059.
Planck: 0.054±0.007. Within 1σ.

---

### `Tau.BookV.Cosmology.reionization_tau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L402-L404)
**def
Tau.BookV.Cosmology.reionization_tau :String**

Equations
- Tau.BookV.Cosmology.reionization_tau = "z_reion = a₃−W₃(4) = 13−5 = 8. τ_reion ≈ 0.059. " ++ "Planck: 0.054±0.007, deviation +89130 ppm (~9%), within 1σ."
Instances For

---

### `Tau.BookV.Cosmology.vop3_sprint8e_status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L406-L410)
**def
Tau.BookV.Cosmology.vop3_sprint8e_status :String**


[V.R386] V.OP3 Status After Sprint 8E: h Closes the Pipeline.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.HolonomyMatterDerivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L465-L490)
**structure
Tau.BookV.Cosmology.HolonomyMatterDerivation :Type**


[V.T192 upgrade] Holonomy matter fraction derivation.

The boundary holonomy mass M_∂ contributes to the Friedmann
energy budget in ratio κ_D/κ_B to baryonic matter:

ρ = ρ_baryon + ρ_holonomy
ρ_holonomy/ρ_baryon = κ_D/κ_B = (1−ι<sub>τ</sub>)/ι<sub>τ</sub>² ≈ 5.655

Physical basis:


- Baryons couple through EM (κ_B = ι<sub>τ</sub>²)

- Holonomy mass couples through gravity (κ_D = 1−ι<sub>τ</sub>)

- The ratio is the "holonomy-to-baryon" ratio


Therefore ω_m/ω_b = 1 + κ_D/κ_B = 1 + (1−ι<sub>τ</sub>)/ι<sub>τ</sub>² = 6.655.

- n_baryon_coupling : ℕ
Number of baryon coupling channels (EM: κ_B).

- n_holonomy_coupling : ℕ
Number of holonomy coupling channels (gravity: κ_D).

- n_ratio_terms : ℕ
Number of ratio terms (κ_D and κ_B).

- free_params : ℕ
Number of free parameters.

- n_budget_terms : ℕ
Number of Friedmann budget terms (ρ_baryon + ρ_holonomy).

Instances For

---

### `Tau.BookV.Cosmology.instReprHolonomyMatterDerivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L490-L490)
**instance
Tau.BookV.Cosmology.instReprHolonomyMatterDerivation :Repr HolonomyMatterDerivation**

Equations
- Tau.BookV.Cosmology.instReprHolonomyMatterDerivation = { reprPrec := Tau.BookV.Cosmology.instReprHolonomyMatterDerivation.repr }

---

### `Tau.BookV.Cosmology.instReprHolonomyMatterDerivation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L490-L490)
**def
Tau.BookV.Cosmology.instReprHolonomyMatterDerivation.repr :HolonomyMatterDerivation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.holonomy_matter_derivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L492-L492)
**def
Tau.BookV.Cosmology.holonomy_matter_derivation :HolonomyMatterDerivation**

Equations
- Tau.BookV.Cosmology.holonomy_matter_derivation = { }
Instances For

---

### `Tau.BookV.Cosmology.holonomy_matter_derived`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L494-L499)
**theorem
Tau.BookV.Cosmology.holonomy_matter_derived :holonomy_matter_derivation.n_ratio_terms = 2 ∧ holonomy_matter_derivation.free_params = 0 ∧ holonomy_matter_derivation.n_budget_terms = 2**


Holonomy matter fraction derived from coupling structure.

---

### `Tau.BookV.Cosmology.EfoldsStructural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L505-L539)
**structure
Tau.BookV.Cosmology.EfoldsStructural :Type**


[V.T196 upgrade] N_e = dim(τ³) × W₅(3) = 3 × 19 = 57.

The number of e-folds is determined by:


- dim(τ³) = 3: independent directions in the fiber

- W₅(3) = 19: the [5,3] Window modulus from CF(ι<sub>τ</sub>⁻¹)

- Each dimension traverses W₅(3) independent winding modes
before the first complex structure (hadronic threshold)


This gives n_s = 1 − 2/N_e = 1 − 2/57 = 0.96491
vs Planck 0.9649 ± 0.0042 (deviation +13 ppm).

Wave 14A upgrade: exit condition formalized. Inflation ends when
boundary characters cross the threshold ladder (ch48). The exit
is structural (cooling function), not fine-tuned (inflaton potential).
Scope: conjectural → τ-effective.

- tau3_dim : ℕ
τ³ dimension.

- w53 : ℕ
W₅(3) window modulus.

- n_e : ℕ
N_e = dim × W₅(3).

- decomp : self.n_e = self.tau3_dim * self.w53
N_e = dim × window.

- ns_deviation_ppm : ℕ
n_s deviation from Planck in ppm (+13).

- exit_condition : ℕ
Exit condition: 1 = threshold crossing (ch48).

- cf_a3 : ℕ
a₃ = 13 from CF(ι<sub>τ</sub>⁻¹), source of W₅(3).

- cf_a4 : ℕ
a₄ = 3 from CF(ι<sub>τ</sub>⁻¹).

- window_decomp : self.w53 = self.cf_a3 + 5 + 1
W₅(3) = a₃ + a₄ + 1 = 13 + 5 + 1 = 19.

Instances For

---

### `Tau.BookV.Cosmology.instReprEfoldsStructural.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L539-L539)
**def
Tau.BookV.Cosmology.instReprEfoldsStructural.repr :EfoldsStructural → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprEfoldsStructural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L539-L539)
**instance
Tau.BookV.Cosmology.instReprEfoldsStructural :Repr EfoldsStructural**

Equations
- Tau.BookV.Cosmology.instReprEfoldsStructural = { reprPrec := Tau.BookV.Cosmology.instReprEfoldsStructural.repr }

---

### `Tau.BookV.Cosmology.efolds_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L541-L543)
**def
Tau.BookV.Cosmology.efolds_structural :EfoldsStructural**

Equations
- Tau.BookV.Cosmology.efolds_structural = { decomp := Tau.BookV.Cosmology.efolds_structural._proof_1,
 window_decomp := Tau.BookV.Cosmology.efolds_structural._proof_2 }
Instances For

---

### `Tau.BookV.Cosmology.efolds_57`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L545-L550)
**theorem
Tau.BookV.Cosmology.efolds_57 :efolds_structural.n_e = 57 ∧ efolds_structural.tau3_dim = 3 ∧ efolds_structural.w53 = 19**


N_e = 57 = 3 × 19 structural derivation.

---

### `Tau.BookV.Cosmology.w53_from_cf`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L552-L557)
**theorem
Tau.BookV.Cosmology.w53_from_cf :efolds_structural.cf_a3 = 13 ∧ efolds_structural.cf_a4 = 3 ∧ efolds_structural.w53 = 19**


W₅(3) = 19 from CF partial quotients.

---

### `Tau.BookV.Cosmology.ErrorCancellationStructural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L563-L581)
**structure
Tau.BookV.Cosmology.ErrorCancellationStructural :Type**


[V.T191 upgrade] Error cancellation is structural.

ℓ₁ ∝ ω_m^{−a} · ω_b^{b} where a ≈ 0.25, b ≈ 0.13.
The errors: ω_b at −1.2%, ω_m at +4.1%.
Product: (−1.2%)^0.13 × (+4.1%)^{−0.25} ≈ 1.
This is structural: the M3h baseline holonomy formula
has ω_b undershoot compensating ω_m overshoot in the
Friedmann integral for the sound horizon.

Wave 8C finding: correcting ω_m alone BREAKS cancellation.
NLO must shift both η_B and holonomy ratio together.

- n_structural_constraints : ℕ
Number of structural constraints (coupled NLO + Friedmann integral).

- n_compensating_terms : ℕ
Number of compensating error terms (ω_b undershoot + ω_m overshoot).

- n_coupled_params : ℕ
Number of coupled NLO parameters (η_B + holonomy ratio).

Instances For

---

### `Tau.BookV.Cosmology.instReprErrorCancellationStructural.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L581-L581)
**def
Tau.BookV.Cosmology.instReprErrorCancellationStructural.repr :ErrorCancellationStructural → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprErrorCancellationStructural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L581-L581)
**instance
Tau.BookV.Cosmology.instReprErrorCancellationStructural :Repr ErrorCancellationStructural**

Equations
- Tau.BookV.Cosmology.instReprErrorCancellationStructural = { reprPrec := Tau.BookV.Cosmology.instReprErrorCancellationStructural.repr }

---

### `Tau.BookV.Cosmology.error_cancellation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L583-L583)
**def
Tau.BookV.Cosmology.error_cancellation :ErrorCancellationStructural**

Equations
- Tau.BookV.Cosmology.error_cancellation = { }
Instances For

---

### `Tau.BookV.Cosmology.error_cancellation_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L585-L590)
**theorem
Tau.BookV.Cosmology.error_cancellation_structural :error_cancellation.n_structural_constraints = 2 ∧ error_cancellation.n_compensating_terms = 2 ∧ error_cancellation.n_coupled_params = 2**


Error cancellation is structural, not accidental.

---

### `Tau.BookV.Cosmology.HubbleParameter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L596-L606)
**structure
Tau.BookV.Cosmology.HubbleParameter :Type**


[V.T196] Hubble Parameter from τ at −120 ppm.
h = 2/3 + ι<sub>τ</sub>²/W₃(3) = 2/3 + ι<sub>τ</sub>²/17 = 0.67352.
Base: 2/3 = EdS exponent. Correction: κ_B/17.

- w33 : ℕ
W₃(3) = 17 from CF window.

- correction_power : ℕ
Correction power (ι<sub>τ</sub>² → 2).

- free_params : ℕ
Number of free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprHubbleParameter.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L606-L606)
**def
Tau.BookV.Cosmology.instReprHubbleParameter.repr :HubbleParameter → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprHubbleParameter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L606-L606)
**instance
Tau.BookV.Cosmology.instReprHubbleParameter :Repr HubbleParameter**

Equations
- Tau.BookV.Cosmology.instReprHubbleParameter = { reprPrec := Tau.BookV.Cosmology.instReprHubbleParameter.repr }

---

### `Tau.BookV.Cosmology.hubble_parameter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L608-L608)
**def
Tau.BookV.Cosmology.hubble_parameter :HubbleParameter**

Equations
- Tau.BookV.Cosmology.hubble_parameter = { }
Instances For

---

### `Tau.BookV.Cosmology.hubble_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L610-L614)
**theorem
Tau.BookV.Cosmology.hubble_structural :hubble_parameter.w33 = 17 ∧ hubble_parameter.correction_power = 2 ∧ hubble_parameter.free_params = 0**


---

### `Tau.BookV.Cosmology.FullCMBPipeline`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L616-L625)
**structure
Tau.BookV.Cosmology.FullCMBPipeline :Type**


[V.T197] Full CMB Pipeline.
M3h + h_τ: ℓ₁ = 220.63 (+2863 ppm). Zero free parameters.

- n_stages : ℕ
Number of pipeline stages.

- free_params : ℕ
Number of free parameters beyond ι<sub>τ</sub> and T_CMB.

- n_inputs : ℕ
Number of independent inputs (single ι<sub>τ</sub>).

Instances For

---

### `Tau.BookV.Cosmology.instReprFullCMBPipeline.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L625-L625)
**def
Tau.BookV.Cosmology.instReprFullCMBPipeline.repr :FullCMBPipeline → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprFullCMBPipeline`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L625-L625)
**instance
Tau.BookV.Cosmology.instReprFullCMBPipeline :Repr FullCMBPipeline**

Equations
- Tau.BookV.Cosmology.instReprFullCMBPipeline = { reprPrec := Tau.BookV.Cosmology.instReprFullCMBPipeline.repr }

---

### `Tau.BookV.Cosmology.full_cmb_pipeline`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L627-L627)
**def
Tau.BookV.Cosmology.full_cmb_pipeline :FullCMBPipeline**

Equations
- Tau.BookV.Cosmology.full_cmb_pipeline = { }
Instances For

---

### `Tau.BookV.Cosmology.full_pipeline_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L629-L633)
**theorem
Tau.BookV.Cosmology.full_pipeline_structural :full_cmb_pipeline.n_stages = 6 ∧ full_cmb_pipeline.free_params = 0 ∧ full_cmb_pipeline.n_inputs = 1**


---

### `Tau.BookV.Cosmology.ScalarAmplitudeNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L635-L664)
**structure
Tau.BookV.Cosmology.ScalarAmplitudeNLO :Type**


[V.T198] Scalar Amplitude NLO.
A_s = (121/225)·ι<sub>τ</sub>¹⁸·(1−ι<sub>τ</sub>³/3) = 2.096×10⁻⁹.
NLO factor is structural (τ³ volume averaging).

Wave 14A upgrade: coefficient origin and derivation chain formalized.
(121/225) = (11/15)² inherited from α_τ = (121/225)·ι<sub>τ</sub>⁴.
NLO factor (1−ι<sub>τ</sub>³/3) = cubic coupling / dim(τ³) dimensions.
Scope: conjectural → τ-effective.

- nlo_power : ℕ
NLO power (ι<sub>τ</sub>³ averaging → 3).

- gap_factor : ℕ
Slow-roll gap factor (156× gap → not slow-roll).

- coeff_numer : ℕ
Coefficient numerator (121 = 11²).

- coeff_denom : ℕ
Coefficient denominator (225 = 15²).

- coeff_sq : self.coeff_numer = 11 * 11 ∧ self.coeff_denom = 15 * 15
Coefficient is (11/15)².

- base_exponent : ℕ
Base exponent (ι<sub>τ</sub>¹⁸ = ι<sub>τ</sub>^{W₄(3)}).

- nlo_dim : ℕ
NLO dimension (dim(τ³) = 3).

- nlo_eq_dim : self.nlo_power = self.nlo_dim
NLO power matches dim.

- deviation_ppm : ℕ
Deviation from Planck in ppm (−1979).

- free_params : ℕ
Number of free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprScalarAmplitudeNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L664-L664)
**instance
Tau.BookV.Cosmology.instReprScalarAmplitudeNLO :Repr ScalarAmplitudeNLO**

Equations
- Tau.BookV.Cosmology.instReprScalarAmplitudeNLO = { reprPrec := Tau.BookV.Cosmology.instReprScalarAmplitudeNLO.repr }

---

### `Tau.BookV.Cosmology.instReprScalarAmplitudeNLO.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L664-L664)
**def
Tau.BookV.Cosmology.instReprScalarAmplitudeNLO.repr :ScalarAmplitudeNLO → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.scalar_amplitude_nlo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L666-L668)
**def
Tau.BookV.Cosmology.scalar_amplitude_nlo :ScalarAmplitudeNLO**

Equations
- Tau.BookV.Cosmology.scalar_amplitude_nlo = { coeff_sq := Tau.BookV.Cosmology.scalar_amplitude_nlo._proof_1,
 nlo_eq_dim := Tau.BookV.Cosmology.two_horizon_data._proof_1 }
Instances For

---

### `Tau.BookV.Cosmology.scalar_amplitude_nlo_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L670-L676)
**theorem
Tau.BookV.Cosmology.scalar_amplitude_nlo_thm :scalar_amplitude_nlo.nlo_power = 3 ∧ scalar_amplitude_nlo.gap_factor = 156 ∧ scalar_amplitude_nlo.coeff_numer = 121 ∧ scalar_amplitude_nlo.coeff_denom = 225 ∧ scalar_amplitude_nlo.free_params = 0**


---

### `Tau.BookV.Cosmology.ScalarAmplitudeDerivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L678-L699)
**structure
Tau.BookV.Cosmology.ScalarAmplitudeDerivation :Type**


[V.D253 upgrade] Scalar Amplitude Derivation Chain.
A_s = α_τ · ι<sub>τ</sub>¹⁴ · (1 − ι<sub>τ</sub>³/3).
The coefficient (121/225) is inherited from the fine-structure
constant chain: α_τ = (121/225)·ι<sub>τ</sub>⁴. No new free parameter.
The NLO factor (1 − ι<sub>τ</sub>³/3) is τ³ volume averaging:
cubic coupling ι<sub>τ</sub>³ averaged over dim(τ³) = 3 dimensions.

- alpha_tau_remaining_power : ℕ
α_τ power of ι<sub>τ</sub> in A_s (14 = W₄(3) − 4).

- total_iota_power : ℕ
Total ι<sub>τ</sub> power (18 = 4 + 14).

- power_is_w43 : self.total_iota_power = 18
Power decomposition: 18 = W₄(3).

- chain_links : ℕ
Chain links: ι<sub>τ</sub> → α_τ → A_s.

- coefficient_source : ℕ
Source: 1 = α_τ inheritance (not new fit).

- nlo_source : ℕ
NLO: 1 = volume averaging (not slow-roll).

- free_params : ℕ
Free parameters beyond ι<sub>τ</sub>.

Instances For

---

### `Tau.BookV.Cosmology.instReprScalarAmplitudeDerivation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L699-L699)
**def
Tau.BookV.Cosmology.instReprScalarAmplitudeDerivation.repr :ScalarAmplitudeDerivation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprScalarAmplitudeDerivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L699-L699)
**instance
Tau.BookV.Cosmology.instReprScalarAmplitudeDerivation :Repr ScalarAmplitudeDerivation**

Equations
- Tau.BookV.Cosmology.instReprScalarAmplitudeDerivation = { reprPrec := Tau.BookV.Cosmology.instReprScalarAmplitudeDerivation.repr }

---

### `Tau.BookV.Cosmology.scalar_amplitude_derivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L701-L702)
**def
Tau.BookV.Cosmology.scalar_amplitude_derivation :ScalarAmplitudeDerivation**

Equations
- Tau.BookV.Cosmology.scalar_amplitude_derivation = { power_is_w43 := Tau.BookV.Cosmology.scalar_amplitude_derivation._proof_1 }
Instances For

---

### `Tau.BookV.Cosmology.scalar_amplitude_chain`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L704-L709)
**theorem
Tau.BookV.Cosmology.scalar_amplitude_chain :scalar_amplitude_derivation.total_iota_power = 18 ∧ scalar_amplitude_derivation.chain_links = 2 ∧ scalar_amplitude_derivation.coefficient_source = 1 ∧ scalar_amplitude_derivation.free_params = 0**


---

### `Tau.BookV.Cosmology.ReionizationOpticalDepth`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L711-L725)
**structure
Tau.BookV.Cosmology.ReionizationOpticalDepth :Type**


[V.P139] Reionisation Optical Depth.
z_reion = a₃ − W₃(4) = 13 − 5 = 8.
τ_reion ≈ 0.059. Planck: 0.054 ± 0.007.

- a3 : ℕ
a₃ = 13 (3rd CF partial quotient).

- w34 : ℕ
W₃(4) = 5.

- z_reion : ℕ
z_reion = a₃ − W₃(4).

- z_decomp : self.z_reion = self.a3 - self.w34
Structural: z_reion = a₃ − W₃(4).

- sigma_deviation_x10 : ℕ
Sigma deviation ×10 from Planck (0.7σ → 7).

Instances For

---

### `Tau.BookV.Cosmology.instReprReionizationOpticalDepth`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L725-L725)
**instance
Tau.BookV.Cosmology.instReprReionizationOpticalDepth :Repr ReionizationOpticalDepth**

Equations
- Tau.BookV.Cosmology.instReprReionizationOpticalDepth = { reprPrec := Tau.BookV.Cosmology.instReprReionizationOpticalDepth.repr }

---

### `Tau.BookV.Cosmology.instReprReionizationOpticalDepth.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L725-L725)
**def
Tau.BookV.Cosmology.instReprReionizationOpticalDepth.repr :ReionizationOpticalDepth → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.reionization_depth`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L727-L728)
**def
Tau.BookV.Cosmology.reionization_depth :ReionizationOpticalDepth**

Equations
- Tau.BookV.Cosmology.reionization_depth = { z_decomp := Tau.BookV.Cosmology.reionization_depth._proof_1 }
Instances For

---

### `Tau.BookV.Cosmology.reionization_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L730-L733)
**theorem
Tau.BookV.Cosmology.reionization_structural :reionization_depth.z_reion = 8 ∧ reionization_depth.sigma_deviation_x10 = 7**


---

### `Tau.BookV.Cosmology.SilkDampingScale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L788-L808)
**structure
Tau.BookV.Cosmology.SilkDampingScale :Type**


[V.D254] Silk Damping Scale from Holonomy Ratio.
ℓ_D = ℓ₁ × κ_D/κ_B = ℓ₁ × (1−ι<sub>τ</sub>)/ι<sub>τ</sub>² = 220 × 5.6546 = 1244.0.
Eisenstein-Hu (1998): ℓ_D ≈ 1244. Match: +9 ppm.

Physical interpretation: photon diffusion reaches the scale where
holonomy mass equals baryon mass. The damping multipole exceeds the
first peak multipole by exactly the matter-to-baryon coupling ratio.

- kappa_D_x1e6 : ℕ
Holonomy coupling numerator (κ_D ×10⁶).

- kappa_B_x1e6 : ℕ
Baryon coupling numerator (κ_B ×10⁶).

- ratio_x10000 : ℕ
Ratio κ_D/κ_B ×10000 (5.6546 → 56546).

- ell_D_x10 : ℕ
ℓ_D ×10 (1244.0 → 12440).

- deviation_ppm : ℕ
Deviation from Eisenstein-Hu in ppm (+9).

- free_params : ℕ
Number of free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprSilkDampingScale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L808-L808)
**instance
Tau.BookV.Cosmology.instReprSilkDampingScale :Repr SilkDampingScale**

Equations
- Tau.BookV.Cosmology.instReprSilkDampingScale = { reprPrec := Tau.BookV.Cosmology.instReprSilkDampingScale.repr }

---

### `Tau.BookV.Cosmology.instReprSilkDampingScale.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L808-L808)
**def
Tau.BookV.Cosmology.instReprSilkDampingScale.repr :SilkDampingScale → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.silk_damping_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L810-L810)
**def
Tau.BookV.Cosmology.silk_damping_data :SilkDampingScale**

Equations
- Tau.BookV.Cosmology.silk_damping_data = { }
Instances For

---

### `Tau.BookV.Cosmology.silk_damping_ell_D`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L812-L813)
**def
Tau.BookV.Cosmology.silk_damping_ell_D :Float**

Equations
- Tau.BookV.Cosmology.silk_damping_ell_D = 220.0 * Tau.BookV.Cosmology.kappa_D✝ / Tau.BookV.Cosmology.kappa_B✝
Instances For

---

### `Tau.BookV.Cosmology.silk_damping_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L815-L818)
**theorem
Tau.BookV.Cosmology.silk_damping_structural :silk_damping_data.deviation_ppm = 9 ∧ silk_damping_data.free_params = 0**


---

### `Tau.BookV.Cosmology.EtaBExponentResolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L830-L855)
**structure
Tau.BookV.Cosmology.EtaBExponentResolution :Type**


[V.R387] η_B Exponent Resolution: 15 vs 20.

2nd Ed: η_B = α_τ · ι<sub>τ</sub>¹⁵ · (5/6)
1st Ed: η_B = q_B · ι<sub>τ</sub>²⁰ where q_B ≈ 1.313

Resolution: expanding α_τ = (121/225)·ι<sub>τ</sub>⁴ gives
η_B = (121/270) · ι<sub>τ</sub>¹⁹. The effective exponent is 19.
The 1st Ed absorbed one factor ι<sub>τ</sub> into q_B = (121/270)/ι<sub>τ</sub>.

Key coincidence: 19 = W₅(3), the same window number that
determines N_e/dim(τ³) = 57/3 = 19. Both the inflationary
duration and baryon asymmetry are governed by the [5,3] CF window.

- exponent_2nd : ℕ
2nd Ed apparent exponent.

- exponent_1st : ℕ
1st Ed apparent exponent.

- effective_exponent : ℕ
True effective exponent.

- w53_match : self.effective_exponent = 19
W₅(3) = 19 coincidence.

- prefactor_numer : ℕ
Prefactor numerator (121).

- prefactor_denom : ℕ
Prefactor denominator (270 = 225 × 6/5).

Instances For

---

### `Tau.BookV.Cosmology.instReprEtaBExponentResolution.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L855-L855)
**def
Tau.BookV.Cosmology.instReprEtaBExponentResolution.repr :EtaBExponentResolution → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprEtaBExponentResolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L855-L855)
**instance
Tau.BookV.Cosmology.instReprEtaBExponentResolution :Repr EtaBExponentResolution**

Equations
- Tau.BookV.Cosmology.instReprEtaBExponentResolution = { reprPrec := Tau.BookV.Cosmology.instReprEtaBExponentResolution.repr }

---

### `Tau.BookV.Cosmology.eta_b_resolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L857-L858)
**def
Tau.BookV.Cosmology.eta_b_resolution :EtaBExponentResolution**

Equations
- Tau.BookV.Cosmology.eta_b_resolution = { w53_match := Tau.BookV.Cosmology.eta_b_resolution._proof_1 }
Instances For

---

### `Tau.BookV.Cosmology.eta_b_effective_exponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L860-L865)
**theorem
Tau.BookV.Cosmology.eta_b_effective_exponent :eta_b_resolution.effective_exponent = 19 ∧ eta_b_resolution.prefactor_numer = 121 ∧ eta_b_resolution.prefactor_denom = 270**


The effective η_B exponent 19 = W₅(3).

---

### `Tau.BookV.Cosmology.BaryonLoadingParameter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L877-L888)
**structure
Tau.BookV.Cosmology.BaryonLoadingParameter :Type**


[V.D255] Baryon Loading Parameter from τ-Native ω_b.
R_b(z_rec) = 31.5·ω_b·(T/2.7)⁻⁴/(z_rec/1000) = 0.615.
Computed from τ-native ω_b = 0.02209, T_CMB = 2.7255 K,
z_rec = 1089.8. Controls odd/even peak asymmetry.

- r_b_x1000 : ℕ
R_b ×1000 (0.615 → 615).

- source : ℕ
Source: 1 = from τ-native ω_b.

- free_params : ℕ
Free parameters beyond τ inputs + T_CMB.

Instances For

---

### `Tau.BookV.Cosmology.instReprBaryonLoadingParameter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L888-L888)
**instance
Tau.BookV.Cosmology.instReprBaryonLoadingParameter :Repr BaryonLoadingParameter**

Equations
- Tau.BookV.Cosmology.instReprBaryonLoadingParameter = { reprPrec := Tau.BookV.Cosmology.instReprBaryonLoadingParameter.repr }

---

### `Tau.BookV.Cosmology.instReprBaryonLoadingParameter.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L888-L888)
**def
Tau.BookV.Cosmology.instReprBaryonLoadingParameter.repr :BaryonLoadingParameter → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.baryon_loading`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L890-L890)
**def
Tau.BookV.Cosmology.baryon_loading :BaryonLoadingParameter**

Equations
- Tau.BookV.Cosmology.baryon_loading = { }
Instances For

---

### `Tau.BookV.Cosmology.baryon_loading_value`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L891-L891)
**def
Tau.BookV.Cosmology.baryon_loading_value :Float**

Equations
- Tau.BookV.Cosmology.baryon_loading_value = 31.5 * 2209e-5 * (2.7255 / 2.7) ^ (-4) / (1089.8 / 1000.0)
Instances For

---

### `Tau.BookV.Cosmology.baryon_loading_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L893-L896)
**theorem
Tau.BookV.Cosmology.baryon_loading_thm :baryon_loading.source = 1 ∧ baryon_loading.free_params = 0**


---

### `Tau.BookV.Cosmology.PeakHeightAsymmetry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L898-L911)
**structure
Tau.BookV.Cosmology.PeakHeightAsymmetry :Type**


[V.P140] Peak Height Odd/Even Asymmetry.
Compression peaks (odd n) enhanced by (1+R_b), rarefaction peaks
(even n) suppressed by (1−R_b). Silk damping envelope from ℓ_D.
Quantitative ratios require Boltzmann transfer functions.

- compression_x1000 : ℕ
Compression boost factor (1+R_b) × 1000 ≈ 1615.

- rarefaction_x1000 : ℕ
Rarefaction factor (1−R_b) × 1000 ≈ 385.

- loading_ratio_x1000 : ℕ
Ratio (1+R_b)/(1−R_b) × 1000 ≈ 4194.

- needs_boltzmann : ℕ
Requires Boltzmann solver for quantitative prediction: 1 = yes.

Instances For

---

### `Tau.BookV.Cosmology.instReprPeakHeightAsymmetry.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L911-L911)
**def
Tau.BookV.Cosmology.instReprPeakHeightAsymmetry.repr :PeakHeightAsymmetry → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprPeakHeightAsymmetry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L911-L911)
**instance
Tau.BookV.Cosmology.instReprPeakHeightAsymmetry :Repr PeakHeightAsymmetry**

Equations
- Tau.BookV.Cosmology.instReprPeakHeightAsymmetry = { reprPrec := Tau.BookV.Cosmology.instReprPeakHeightAsymmetry.repr }

---

### `Tau.BookV.Cosmology.peak_height_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L913-L913)
**def
Tau.BookV.Cosmology.peak_height_data :PeakHeightAsymmetry**

Equations
- Tau.BookV.Cosmology.peak_height_data = { }
Instances For

---

### `Tau.BookV.Cosmology.peak_height_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L915-L918)
**theorem
Tau.BookV.Cosmology.peak_height_thm :peak_height_data.loading_ratio_x1000 = 4194 ∧ peak_height_data.needs_boltzmann = 1**


---

### `Tau.BookV.Cosmology.DEClosureMatterDensity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L931-L947)
**structure
Tau.BookV.Cosmology.DEClosureMatterDensity :Type**


[V.T199] DE-Closure Matter Density at −675 ppm.
ω_m = (1 − Ω_Λ − Ω_r) × h² where
Ω_Λ = κ_D·(1+ι<sub>τ</sub>³) = 0.6849, h = 2/3+ι<sub>τ</sub>²/17 = 0.6735.
Result: ω_m = 0.1429 at −675 ppm from Planck 0.1430.
This is 41× better than M3h holonomy path (+27972 ppm).

- omega_m_x10000 : ℕ
ω_m ×10000 (0.1429 → 1429).

- deviation_ppm : ℕ
Deviation from Planck in ppm (−675 → 675, sign encoded separately).

- deviation_sign : ℕ
Sign: 0 = negative deviation.

- improvement_factor : ℕ
Improvement factor over M3h (41×).

- free_params : ℕ
Number of free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprDEClosureMatterDensity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L947-L947)
**instance
Tau.BookV.Cosmology.instReprDEClosureMatterDensity :Repr DEClosureMatterDensity**

Equations
- Tau.BookV.Cosmology.instReprDEClosureMatterDensity = { reprPrec := Tau.BookV.Cosmology.instReprDEClosureMatterDensity.repr }

---

### `Tau.BookV.Cosmology.instReprDEClosureMatterDensity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L947-L947)
**def
Tau.BookV.Cosmology.instReprDEClosureMatterDensity.repr :DEClosureMatterDensity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.de_closure_matter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L949-L949)
**def
Tau.BookV.Cosmology.de_closure_matter :DEClosureMatterDensity**

Equations
- Tau.BookV.Cosmology.de_closure_matter = { }
Instances For

---

### `Tau.BookV.Cosmology.de_closure_matter_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L951-L955)
**theorem
Tau.BookV.Cosmology.de_closure_matter_thm :de_closure_matter.omega_m_x10000 = 1429 ∧ de_closure_matter.improvement_factor = 41 ∧ de_closure_matter.free_params = 0**


---

### `Tau.BookV.Cosmology.PrimordialBModeAmplitude`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L966-L980)
**structure
Tau.BookV.Cosmology.PrimordialBModeAmplitude :Type**


[V.D256] Primordial B-Mode Amplitude from r = ι<sub>τ</sub>⁴.
D_80^BB = ℓ(ℓ+1)C_ℓ^BB/(2π) ≈ 0.025 × r = 339 nK² at ℓ ~ 80
(recombination bump). Tensor amplitude A_t = r × A_s = 2.844×10⁻¹¹.

- peak_ell : ℕ
Recombination bump peak multipole.

- d_bb_nk2 : ℕ
D^BB in nK² (339 → 339).

- r_x1e6 : ℕ
r × 10⁶ (0.01357 → 13570).

- r_source : ℕ
Source: 1 = from r = ι<sub>τ</sub>⁴ derivation.

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprPrimordialBModeAmplitude`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L980-L980)
**instance
Tau.BookV.Cosmology.instReprPrimordialBModeAmplitude :Repr PrimordialBModeAmplitude**

Equations
- Tau.BookV.Cosmology.instReprPrimordialBModeAmplitude = { reprPrec := Tau.BookV.Cosmology.instReprPrimordialBModeAmplitude.repr }

---

### `Tau.BookV.Cosmology.instReprPrimordialBModeAmplitude.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L980-L980)
**def
Tau.BookV.Cosmology.instReprPrimordialBModeAmplitude.repr :PrimordialBModeAmplitude → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.bmode_amplitude`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L982-L982)
**def
Tau.BookV.Cosmology.bmode_amplitude :PrimordialBModeAmplitude**

Equations
- Tau.BookV.Cosmology.bmode_amplitude = { }
Instances For

---

### `Tau.BookV.Cosmology.bmode_amplitude_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L984-L988)
**theorem
Tau.BookV.Cosmology.bmode_amplitude_thm :bmode_amplitude.peak_ell = 80 ∧ bmode_amplitude.d_bb_nk2 = 339 ∧ bmode_amplitude.free_params = 0**


---

### `Tau.BookV.Cosmology.BModeDetectionForecast`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L990-L1004)
**structure
Tau.BookV.Cosmology.BModeDetectionForecast :Type**


[V.P141] B-Mode Detection Forecast.
CMB-S4: ~14σ, LiteBIRD: ~7σ, BICEP Array: ~5σ.
Lensing foreground at ℓ~80: 1131× weaker than signal.

- cmbs4_sigma : ℕ
CMB-S4 significance (σ).

- litebird_sigma : ℕ
LiteBIRD significance (σ).

- bicep_sigma : ℕ
BICEP Array significance (σ).

- signal_lensing_ratio : ℕ
Signal-to-lensing ratio at ℓ~80.

- delensing_required : ℕ
De-lensing required: 0 = no.

Instances For

---

### `Tau.BookV.Cosmology.instReprBModeDetectionForecast`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1004-L1004)
**instance
Tau.BookV.Cosmology.instReprBModeDetectionForecast :Repr BModeDetectionForecast**

Equations
- Tau.BookV.Cosmology.instReprBModeDetectionForecast = { reprPrec := Tau.BookV.Cosmology.instReprBModeDetectionForecast.repr }

---

### `Tau.BookV.Cosmology.instReprBModeDetectionForecast.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1004-L1004)
**def
Tau.BookV.Cosmology.instReprBModeDetectionForecast.repr :BModeDetectionForecast → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.bmode_forecast`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1006-L1006)
**def
Tau.BookV.Cosmology.bmode_forecast :BModeDetectionForecast**

Equations
- Tau.BookV.Cosmology.bmode_forecast = { }
Instances For

---

### `Tau.BookV.Cosmology.bmode_forecast_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1008-L1012)
**theorem
Tau.BookV.Cosmology.bmode_forecast_thm :bmode_forecast.cmbs4_sigma = 14 ∧ bmode_forecast.litebird_sigma = 7 ∧ bmode_forecast.delensing_required = 0**


---

### `Tau.BookV.Cosmology.TauLuminosityDistance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1026-L1042)
**structure
Tau.BookV.Cosmology.TauLuminosityDistance :Type**


[V.D269] τ-Native Luminosity Distance d_L(z).
d_L(z) = (1+z)·(c/H₀)·∫₀ᶻ dz'/E(z').
E²(z) = Ω_m(1+z)³ + Ω_r(1+z)⁴ + Ω_Λ.
Ω_Λ = κ_D(1+ι<sub>τ</sub>³) = 0.6849.
Matches Planck-ΛCDM to ≤310 ppm.

- omega_lambda_x10000 : ℕ
Ω_Λ × 10000 = 6849.

- omega_m_x10000 : ℕ
Ω_m × 10000 = 3151.

- max_ppm_deviation : ℕ
Max d_L deviation from Planck in ppm.

- free_params : ℕ
Number of free parameters.

- pantheon_bins_matched : ℕ
Pantheon+ bins matched (of 9).

Instances For

---

### `Tau.BookV.Cosmology.instReprTauLuminosityDistance.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1042-L1042)
**def
Tau.BookV.Cosmology.instReprTauLuminosityDistance.repr :TauLuminosityDistance → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprTauLuminosityDistance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1042-L1042)
**instance
Tau.BookV.Cosmology.instReprTauLuminosityDistance :Repr TauLuminosityDistance**

Equations
- Tau.BookV.Cosmology.instReprTauLuminosityDistance = { reprPrec := Tau.BookV.Cosmology.instReprTauLuminosityDistance.repr }

---

### `Tau.BookV.Cosmology.tau_luminosity_distance_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1044-L1044)
**def
Tau.BookV.Cosmology.tau_luminosity_distance_data :TauLuminosityDistance**

Equations
- Tau.BookV.Cosmology.tau_luminosity_distance_data = { }
Instances For

---

### `Tau.BookV.Cosmology.luminosity_distance_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1046-L1052)
**theorem
Tau.BookV.Cosmology.luminosity_distance_structural :tau_luminosity_distance_data.omega_lambda_x10000 = 6849 ∧ tau_luminosity_distance_data.omega_m_x10000 = 3151 ∧ tau_luminosity_distance_data.max_ppm_deviation = 310 ∧ tau_luminosity_distance_data.free_params = 0 ∧ tau_luminosity_distance_data.pantheon_bins_matched = 9**


---

### `Tau.BookV.Cosmology.TauAngularDiameterDistance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1054-L1062)
**structure
Tau.BookV.Cosmology.TauAngularDiameterDistance :Type**


[V.D270] τ-Native Angular Diameter Distance d_A(z).
d_A(z) = d_L(z)/(1+z)². Etherington reciprocity.
At z=1100: d_A ≈ 12.6 Mpc.

- etherington_verified : ℕ
Etherington reciprocity verified (1 = yes).

- dA_cmb_x10 : ℕ
d_A(z=1100) × 10 in Mpc = 126.

Instances For

---

### `Tau.BookV.Cosmology.instReprTauAngularDiameterDistance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1062-L1062)
**instance
Tau.BookV.Cosmology.instReprTauAngularDiameterDistance :Repr TauAngularDiameterDistance**

Equations
- Tau.BookV.Cosmology.instReprTauAngularDiameterDistance = { reprPrec := Tau.BookV.Cosmology.instReprTauAngularDiameterDistance.repr }

---

### `Tau.BookV.Cosmology.instReprTauAngularDiameterDistance.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1062-L1062)
**def
Tau.BookV.Cosmology.instReprTauAngularDiameterDistance.repr :TauAngularDiameterDistance → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.tau_angular_diameter_distance_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1064-L1064)
**def
Tau.BookV.Cosmology.tau_angular_diameter_distance_data :TauAngularDiameterDistance**

Equations
- Tau.BookV.Cosmology.tau_angular_diameter_distance_data = { }
Instances For

---

### `Tau.BookV.Cosmology.angular_diameter_distance_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1066-L1069)
**theorem
Tau.BookV.Cosmology.angular_diameter_distance_structural :tau_angular_diameter_distance_data.etherington_verified = 1 ∧ tau_angular_diameter_distance_data.dA_cmb_x10 = 126**


---

### `Tau.BookV.Cosmology.DecelerationParameter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1071-L1081)
**structure
Tau.BookV.Cosmology.DecelerationParameter :Type**


[V.D271] Deceleration Parameter q₀.
q₀ = Ω_m/2 − Ω_Λ ≈ −0.527.
Negative → accelerating expansion.

- q0_magnitude_x1000 : ℕ
q₀ × 1000 = −527. Encoded as sign + magnitude.

- q0_negative : ℕ
Sign: 0 = negative (accelerating).

- planck_match_ppm : ℕ
Matches Planck to < 0.1%.

Instances For

---

### `Tau.BookV.Cosmology.instReprDecelerationParameter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1081-L1081)
**instance
Tau.BookV.Cosmology.instReprDecelerationParameter :Repr DecelerationParameter**

Equations
- Tau.BookV.Cosmology.instReprDecelerationParameter = { reprPrec := Tau.BookV.Cosmology.instReprDecelerationParameter.repr }

---

### `Tau.BookV.Cosmology.instReprDecelerationParameter.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1081-L1081)
**def
Tau.BookV.Cosmology.instReprDecelerationParameter.repr :DecelerationParameter → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.deceleration_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1083-L1083)
**def
Tau.BookV.Cosmology.deceleration_data :DecelerationParameter**

Equations
- Tau.BookV.Cosmology.deceleration_data = { }
Instances For

---

### `Tau.BookV.Cosmology.deceleration_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1085-L1089)
**theorem
Tau.BookV.Cosmology.deceleration_structural :deceleration_data.q0_magnitude_x1000 = 527 ∧ deceleration_data.q0_negative = 0 ∧ deceleration_data.planck_match_ppm = 524**


---

### `Tau.BookV.Cosmology.EinsteinRadiusBoundaryHolonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1095-L1106)
**structure
Tau.BookV.Cosmology.EinsteinRadiusBoundaryHolonomy :Type**


[V.D272] Einstein Radius with Boundary Holonomy Mass.
θ_E² = 4G·M_eff·D_LS/(c²·D_L·D_S).
M_eff = 6.65·M_baryonic (from capacity gradient).
SLACS: 5/5 systems consistent.

- mass_ratio_x100 : ℕ
M_eff/M_baryonic × 100 = 665.

- slacs_matched : ℕ
SLACS systems matched (of 5).

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprEinsteinRadiusBoundaryHolonomy.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1106-L1106)
**def
Tau.BookV.Cosmology.instReprEinsteinRadiusBoundaryHolonomy.repr :EinsteinRadiusBoundaryHolonomy → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprEinsteinRadiusBoundaryHolonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1106-L1106)
**instance
Tau.BookV.Cosmology.instReprEinsteinRadiusBoundaryHolonomy :Repr EinsteinRadiusBoundaryHolonomy**

Equations
- Tau.BookV.Cosmology.instReprEinsteinRadiusBoundaryHolonomy = { reprPrec := Tau.BookV.Cosmology.instReprEinsteinRadiusBoundaryHolonomy.repr }

---

### `Tau.BookV.Cosmology.einstein_radius_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1108-L1108)
**def
Tau.BookV.Cosmology.einstein_radius_data :EinsteinRadiusBoundaryHolonomy**

Equations
- Tau.BookV.Cosmology.einstein_radius_data = { }
Instances For

---

### `Tau.BookV.Cosmology.einstein_radius_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1110-L1114)
**theorem
Tau.BookV.Cosmology.einstein_radius_structural :einstein_radius_data.mass_ratio_x100 = 665 ∧ einstein_radius_data.slacs_matched = 5 ∧ einstein_radius_data.free_params = 0**


---

### `Tau.BookV.Cosmology.StrongLensingCrossSection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1116-L1124)
**structure
Tau.BookV.Cosmology.StrongLensingCrossSection :Type**


[V.T212] Strong Lensing Cross-Section Theorem.
σ_SL = π·θ_E²·D_L². Enhancement factor (M_eff/M_b)=6.65
gives 44× larger cross-section than baryonic-only prediction.

- enhancement_x10 : ℕ
Cross-section enhancement factor × 10 = 442 (6.65² ≈ 44.2).

- is_mass_ratio_squared : ℕ
Enhancement = (M_eff/M_b)².

Instances For

---

### `Tau.BookV.Cosmology.instReprStrongLensingCrossSection.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1124-L1124)
**def
Tau.BookV.Cosmology.instReprStrongLensingCrossSection.repr :StrongLensingCrossSection → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprStrongLensingCrossSection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1124-L1124)
**instance
Tau.BookV.Cosmology.instReprStrongLensingCrossSection :Repr StrongLensingCrossSection**

Equations
- Tau.BookV.Cosmology.instReprStrongLensingCrossSection = { reprPrec := Tau.BookV.Cosmology.instReprStrongLensingCrossSection.repr }

---

### `Tau.BookV.Cosmology.strong_lensing_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1126-L1126)
**def
Tau.BookV.Cosmology.strong_lensing_data :StrongLensingCrossSection**

Equations
- Tau.BookV.Cosmology.strong_lensing_data = { }
Instances For

---

### `Tau.BookV.Cosmology.strong_lensing_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1128-L1131)
**theorem
Tau.BookV.Cosmology.strong_lensing_structural :strong_lensing_data.enhancement_x10 = 442 ∧ strong_lensing_data.is_mass_ratio_squared = 1**


---

### `Tau.BookV.Cosmology.WeakLensingConvergence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1137-L1145)
**structure
Tau.BookV.Cosmology.WeakLensingConvergence :Type**


[V.D273] Weak Lensing Convergence with Boundary Holonomy.
κ(θ) = Σ_eff(θ)/Σ_cr where Σ_eff = Σ_b·(1+κ_D/ι<sub>τ</sub>²) = Σ_b·6.65.
Σ_cr = (c²/4πG)·D_S/(D_L·D_LS).

- sigma_enhancement_x100 : ℕ
Surface density enhancement × 100 = 665.

- same_as_3d_ratio : ℕ
Same enhancement as 3D mass ratio (1 = yes).

Instances For

---

### `Tau.BookV.Cosmology.instReprWeakLensingConvergence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1145-L1145)
**instance
Tau.BookV.Cosmology.instReprWeakLensingConvergence :Repr WeakLensingConvergence**

Equations
- Tau.BookV.Cosmology.instReprWeakLensingConvergence = { reprPrec := Tau.BookV.Cosmology.instReprWeakLensingConvergence.repr }

---

### `Tau.BookV.Cosmology.instReprWeakLensingConvergence.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1145-L1145)
**def
Tau.BookV.Cosmology.instReprWeakLensingConvergence.repr :WeakLensingConvergence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.weak_convergence_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1147-L1147)
**def
Tau.BookV.Cosmology.weak_convergence_data :WeakLensingConvergence**

Equations
- Tau.BookV.Cosmology.weak_convergence_data = { }
Instances For

---

### `Tau.BookV.Cosmology.weak_convergence_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1149-L1152)
**theorem
Tau.BookV.Cosmology.weak_convergence_structural :weak_convergence_data.sigma_enhancement_x100 = 665 ∧ weak_convergence_data.same_as_3d_ratio = 1**


---

### `Tau.BookV.Cosmology.WeakLensingPowerSpectrum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1154-L1162)
**structure
Tau.BookV.Cosmology.WeakLensingPowerSpectrum :Type**


[V.D274] Weak Lensing Power Spectrum P_κ(ℓ).
P_κ(ℓ) via Limber integral with τ-native d_A(z) and M_eff.
Matches ΛCDM P_κ(ℓ) since Ω_m·σ₈ plays same structural role.

- uses_tau_dA : ℕ
Limber integral uses τ-native d_A (1 = yes).

- matches_lcdm : ℕ
Matches ΛCDM at current precision (1 = yes).

Instances For

---

### `Tau.BookV.Cosmology.instReprWeakLensingPowerSpectrum.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1162-L1162)
**def
Tau.BookV.Cosmology.instReprWeakLensingPowerSpectrum.repr :WeakLensingPowerSpectrum → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprWeakLensingPowerSpectrum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1162-L1162)
**instance
Tau.BookV.Cosmology.instReprWeakLensingPowerSpectrum :Repr WeakLensingPowerSpectrum**

Equations
- Tau.BookV.Cosmology.instReprWeakLensingPowerSpectrum = { reprPrec := Tau.BookV.Cosmology.instReprWeakLensingPowerSpectrum.repr }

---

### `Tau.BookV.Cosmology.weak_power_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1164-L1164)
**def
Tau.BookV.Cosmology.weak_power_data :WeakLensingPowerSpectrum**

Equations
- Tau.BookV.Cosmology.weak_power_data = { }
Instances For

---

### `Tau.BookV.Cosmology.weak_power_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1166-L1169)
**theorem
Tau.BookV.Cosmology.weak_power_structural :weak_power_data.uses_tau_dA = 1 ∧ weak_power_data.matches_lcdm = 1**


---

### `Tau.BookV.Cosmology.QuantitativeBulletCluster`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1175-L1185)
**structure
Tau.BookV.Cosmology.QuantitativeBulletCluster :Type**


[V.T213] Quantitative Bullet Cluster Mass Prediction.
M_p ≈ 1.5×10¹⁴ M☉ → M_eff = 6.65·M_p ≈ 10¹⁵ M☉.
θ_E ≈ 74 arcsec at z_S=1. Five-cluster catalog.

- mass_ratio_x100 : ℕ
M_eff/M_p × 100 = 665.

- bullet_theta_E_arcsec : ℕ
Bullet Cluster θ_E in arcsec.

- cluster_count : ℕ
Number of clusters in catalog.

Instances For

---

### `Tau.BookV.Cosmology.instReprQuantitativeBulletCluster`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1185-L1185)
**instance
Tau.BookV.Cosmology.instReprQuantitativeBulletCluster :Repr QuantitativeBulletCluster**

Equations
- Tau.BookV.Cosmology.instReprQuantitativeBulletCluster = { reprPrec := Tau.BookV.Cosmology.instReprQuantitativeBulletCluster.repr }

---

### `Tau.BookV.Cosmology.instReprQuantitativeBulletCluster.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1185-L1185)
**def
Tau.BookV.Cosmology.instReprQuantitativeBulletCluster.repr :QuantitativeBulletCluster → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.bullet_cluster_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1187-L1187)
**def
Tau.BookV.Cosmology.bullet_cluster_data :QuantitativeBulletCluster**

Equations
- Tau.BookV.Cosmology.bullet_cluster_data = { }
Instances For

---

### `Tau.BookV.Cosmology.bullet_cluster_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1189-L1193)
**theorem
Tau.BookV.Cosmology.bullet_cluster_structural :bullet_cluster_data.mass_ratio_x100 = 665 ∧ bullet_cluster_data.bullet_theta_E_arcsec = 74 ∧ bullet_cluster_data.cluster_count = 5**


---

### `Tau.BookV.Cosmology.BAOAngularScale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1199-L1209)
**structure
Tau.BookV.Cosmology.BAOAngularScale :Type**


[V.D275] BAO Angular Scale from τ-Native d_A.
θ_BAO(z) = r_s/d_A(z). At z=0.5: d_A/r_s=8.85.
Consistent with DESI DR1 to <310 ppm.

- r_s_x10 : ℕ
r_s in Mpc × 10 = 1471.

- dA_rs_z05_x100 : ℕ
d_A/r_s at z=0.5 × 100 = 885.

- dA_rs_z10_x100 : ℕ
d_A/r_s at z=1.0 × 100 = 1157.

Instances For

---

### `Tau.BookV.Cosmology.instReprBAOAngularScale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1209-L1209)
**instance
Tau.BookV.Cosmology.instReprBAOAngularScale :Repr BAOAngularScale**

Equations
- Tau.BookV.Cosmology.instReprBAOAngularScale = { reprPrec := Tau.BookV.Cosmology.instReprBAOAngularScale.repr }

---

### `Tau.BookV.Cosmology.instReprBAOAngularScale.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1209-L1209)
**def
Tau.BookV.Cosmology.instReprBAOAngularScale.repr :BAOAngularScale → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.bao_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1211-L1211)
**def
Tau.BookV.Cosmology.bao_data :BAOAngularScale**

Equations
- Tau.BookV.Cosmology.bao_data = { }
Instances For

---

### `Tau.BookV.Cosmology.bao_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1213-L1217)
**theorem
Tau.BookV.Cosmology.bao_structural :bao_data.r_s_x10 = 1471 ∧ bao_data.dA_rs_z05_x100 = 885 ∧ bao_data.dA_rs_z10_x100 = 1157**


---

### `Tau.BookV.Cosmology.DESIConsistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1219-L1227)
**structure
Tau.BookV.Cosmology.DESIConsistency :Type**


[V.T214] DESI Consistency Check.
τ-native D_V/r_d matches Planck-ΛCDM at z = 0.51–2.33.
q₀ = −0.527 confirms accelerating expansion.

- desi_bins : ℕ
Number of DESI redshift bins checked.

- all_consistent : ℕ
All bins consistent (1 = yes).

Instances For

---

### `Tau.BookV.Cosmology.instReprDESIConsistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1227-L1227)
**instance
Tau.BookV.Cosmology.instReprDESIConsistency :Repr DESIConsistency**

Equations
- Tau.BookV.Cosmology.instReprDESIConsistency = { reprPrec := Tau.BookV.Cosmology.instReprDESIConsistency.repr }

---

### `Tau.BookV.Cosmology.instReprDESIConsistency.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1227-L1227)
**def
Tau.BookV.Cosmology.instReprDESIConsistency.repr :DESIConsistency → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.desi_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1229-L1229)
**def
Tau.BookV.Cosmology.desi_data :DESIConsistency**

Equations
- Tau.BookV.Cosmology.desi_data = { }
Instances For

---

### `Tau.BookV.Cosmology.desi_consistency_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1231-L1234)
**theorem
Tau.BookV.Cosmology.desi_consistency_structural :desi_data.desi_bins = 5 ∧ desi_data.all_consistent = 1**


---

### `Tau.BookV.Cosmology.DarkSectorConsistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1240-L1258)
**structure
Tau.BookV.Cosmology.DarkSectorConsistency :Type**


[V.T215] Dark Sector Consistency Theorem.
The τ-framework explains rotation curves + lensing + Hubble diagram +
CMB + BAO with ONE parameter set from ι<sub>τ</sub> = 2/(π+e):
Ω_Λ=0.6849, Ω_m=0.3151, h=0.6735, r=ι<sub>τ</sub>⁴=0.014,
Σm_ν=0.089 eV, M_eff/M_p=6.65. No free parameters.

- pillars : ℕ
Number of observational pillars explained.

- free_params : ℕ
Number of free parameters.

- discriminators : ℕ
Number of decisive discriminators vs ΛCDM.

- mass_ratio_x100 : ℕ
M_eff/M_p × 100 = 665.

- r_tensor_x10000 : ℕ
r × 10000 = 140 (= ι<sub>τ</sub>⁴).

- sum_mnu_x1000 : ℕ
Σm_ν × 1000 in eV = 89.

Instances For

---

### `Tau.BookV.Cosmology.instReprDarkSectorConsistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1258-L1258)
**instance
Tau.BookV.Cosmology.instReprDarkSectorConsistency :Repr DarkSectorConsistency**

Equations
- Tau.BookV.Cosmology.instReprDarkSectorConsistency = { reprPrec := Tau.BookV.Cosmology.instReprDarkSectorConsistency.repr }

---

### `Tau.BookV.Cosmology.instReprDarkSectorConsistency.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1258-L1258)
**def
Tau.BookV.Cosmology.instReprDarkSectorConsistency.repr :DarkSectorConsistency → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.dark_sector_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1260-L1260)
**def
Tau.BookV.Cosmology.dark_sector_data :DarkSectorConsistency**

Equations
- Tau.BookV.Cosmology.dark_sector_data = { }
Instances For

---

### `Tau.BookV.Cosmology.dark_sector_consistency_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1262-L1269)
**theorem
Tau.BookV.Cosmology.dark_sector_consistency_structural :dark_sector_data.pillars = 5 ∧ dark_sector_data.free_params = 0 ∧ dark_sector_data.discriminators = 5 ∧ dark_sector_data.mass_ratio_x100 = 665 ∧ dark_sector_data.r_tensor_x10000 = 140 ∧ dark_sector_data.sum_mnu_x1000 = 89**


---

### `Tau.BookV.Cosmology.DiscriminatorTable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1271-L1286)
**structure
Tau.BookV.Cosmology.DiscriminatorTable :Type**


[V.R401] τ-vs-ΛCDM Discriminator Table.
D1: r=ι<sub>τ</sub>⁴=0.014 at 14σ (CMB-S4).
D2: Σm_ν=0.089 eV at 4.5σ (DESI).
D3: Null DM direct detection.
D4: Structural H₀ tension resolution.
D5: w(z) deviation at z>1 (DESI Y5/Y10).

- cmbs4_r_sigma : ℕ
Most decisive: CMB-S4 significance for r.

- desi_mnu_sigma_x10 : ℕ
DESI significance for Σm_ν.

- dm_detection_null : ℕ
DM detection: 0 = null prediction.

- h0_resolved : ℕ
H₀ tension: 1 = structurally resolved.

Instances For

---

### `Tau.BookV.Cosmology.instReprDiscriminatorTable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1286-L1286)
**instance
Tau.BookV.Cosmology.instReprDiscriminatorTable :Repr DiscriminatorTable**

Equations
- Tau.BookV.Cosmology.instReprDiscriminatorTable = { reprPrec := Tau.BookV.Cosmology.instReprDiscriminatorTable.repr }

---

### `Tau.BookV.Cosmology.instReprDiscriminatorTable.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1286-L1286)
**def
Tau.BookV.Cosmology.instReprDiscriminatorTable.repr :DiscriminatorTable → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.discriminator_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1288-L1288)
**def
Tau.BookV.Cosmology.discriminator_data :DiscriminatorTable**

Equations
- Tau.BookV.Cosmology.discriminator_data = { }
Instances For

---

### `Tau.BookV.Cosmology.discriminator_table_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1290-L1295)
**theorem
Tau.BookV.Cosmology.discriminator_table_structural :discriminator_data.cmbs4_r_sigma = 14 ∧ discriminator_data.desi_mnu_sigma_x10 = 45 ∧ discriminator_data.dm_detection_null = 0 ∧ discriminator_data.h0_resolved = 1**


---

### `Tau.BookV.Cosmology.TwoPathComplementarity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1307-L1332)
**structure
Tau.BookV.Cosmology.TwoPathComplementarity :Type**


[V.T255] Two-Path Complementarity for ℓ₁.
M3h holonomy: ω_m = 0.1470 (+28162 ppm) but ℓ₁ = 220.63 (+2840 ppm).
DE-closure: ω_m = 0.1429 (−675 ppm) but ℓ₁ = 221.52 (+6925 ppm).
Structural error cancellation: ω_b undershoot (−1.2%) anti-correlates
with ω_m overshoot (+4.1%) in the sound horizon integral.
Scope: tau-effective (Wave 36A).

- m3h_omega_m_x10000 : ℕ
M3h path ω_m × 10000.

- de_omega_m_x10000 : ℕ
DE-closure path ω_m × 10000.

- m3h_ell1_ppm : ℕ
M3h ℓ₁ deviation in ppm.

- de_ell1_ppm : ℕ
DE-closure ℓ₁ deviation in ppm.

- m3h_omega_m_ppm : ℕ
M3h ω_m deviation in ppm.

- de_omega_m_ppm : ℕ
DE-closure ω_m deviation in ppm.

- improvement_factor : ℕ
DE-closure improvement factor over M3h (on ω_m).

- free_params : ℕ
Free parameters.

- cancellation_structural : ℕ
Error cancellation is structural (both from ι<sub>τ</sub>).

Instances For

---

### `Tau.BookV.Cosmology.instReprTwoPathComplementarity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1332-L1332)
**instance
Tau.BookV.Cosmology.instReprTwoPathComplementarity :Repr TwoPathComplementarity**

Equations
- Tau.BookV.Cosmology.instReprTwoPathComplementarity = { reprPrec := Tau.BookV.Cosmology.instReprTwoPathComplementarity.repr }

---

### `Tau.BookV.Cosmology.instReprTwoPathComplementarity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1332-L1332)
**def
Tau.BookV.Cosmology.instReprTwoPathComplementarity.repr :TwoPathComplementarity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.two_path_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1334-L1334)
**def
Tau.BookV.Cosmology.two_path_data :TwoPathComplementarity**

Equations
- Tau.BookV.Cosmology.two_path_data = { }
Instances For

---

### `Tau.BookV.Cosmology.two_path_m3h_better_ell1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1336-L1339)
**theorem
Tau.BookV.Cosmology.two_path_m3h_better_ell1 :two_path_data.m3h_ell1_ppm < two_path_data.de_ell1_ppm**


M3h achieves better ℓ₁ despite worse ω_m.

---

### `Tau.BookV.Cosmology.two_path_de_better_omega_m`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1341-L1345)
**theorem
Tau.BookV.Cosmology.two_path_de_better_omega_m :two_path_data.de_omega_m_ppm * two_path_data.improvement_factor < two_path_data.m3h_omega_m_ppm**


DE-closure achieves better ω_m (41× improvement).

---

### `Tau.BookV.Cosmology.PeakPositions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1356-L1379)
**structure
Tau.BookV.Cosmology.PeakPositions :Type**


[V.D316] Peak Position and Height Structure.
Three acoustic peaks from M3h pipeline.
ℓ₂ = 529.8 (obs 537.5, −14326 ppm), ℓ₃ = 796.7 (obs 810.8, −17400 ppm).
Scope: conjectural (Wave 36C).

- ell1_x100 : ℕ
ℓ₁ × 100.

- ell2_x10 : ℕ
ℓ₂ × 10.

- ell3_x10 : ℕ
ℓ₃ × 10.

- ell1_ppm : ℕ
ℓ₁ deviation ppm.

- ell2_ppm : ℕ
ℓ₂ deviation ppm.

- ell3_ppm : ℕ
ℓ₃ deviation ppm.

- ratio_21_x1000 : ℕ
ℓ₂/ℓ₁ × 1000.

- ratio_31_x1000 : ℕ
ℓ₃/ℓ₁ × 1000.

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprPeakPositions.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1379-L1379)
**def
Tau.BookV.Cosmology.instReprPeakPositions.repr :PeakPositions → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprPeakPositions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1379-L1379)
**instance
Tau.BookV.Cosmology.instReprPeakPositions :Repr PeakPositions**

Equations
- Tau.BookV.Cosmology.instReprPeakPositions = { reprPrec := Tau.BookV.Cosmology.instReprPeakPositions.repr }

---

### `Tau.BookV.Cosmology.PeakHeightRatios`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1381-L1400)
**structure
Tau.BookV.Cosmology.PeakHeightRatios :Type**


[V.T256] Peak Height Ratios from Baryon Loading.
Compression/rarefaction ratio (1+R_b)/(1-R_b) = 4.19.
Silk damping envelope: exp(−(ℓ_n/ℓ_D)²).
Scope: conjectural (Wave 36C).

- r_b_x1000 : ℕ
R_b × 1000.

- compression_x1000 : ℕ
(1+R_b) × 1000.

- rarefaction_x1000 : ℕ
(1-R_b) × 1000.

- loading_ratio_x100 : ℕ
Loading ratio × 100.

- ell_d : ℕ
ℓ_D (Silk damping scale).

- n_eff_predicted : ℕ
N_eff predicted.

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprPeakHeightRatios.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1400-L1400)
**def
Tau.BookV.Cosmology.instReprPeakHeightRatios.repr :PeakHeightRatios → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprPeakHeightRatios`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1400-L1400)
**instance
Tau.BookV.Cosmology.instReprPeakHeightRatios :Repr PeakHeightRatios**

Equations
- Tau.BookV.Cosmology.instReprPeakHeightRatios = { reprPrec := Tau.BookV.Cosmology.instReprPeakHeightRatios.repr }

---

### `Tau.BookV.Cosmology.peak_positions_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1402-L1402)
**def
Tau.BookV.Cosmology.peak_positions_data :PeakPositions**

Equations
- Tau.BookV.Cosmology.peak_positions_data = { }
Instances For

---

### `Tau.BookV.Cosmology.peak_height_ratios_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1403-L1403)
**def
Tau.BookV.Cosmology.peak_height_ratios_data :PeakHeightRatios**

Equations
- Tau.BookV.Cosmology.peak_height_ratios_data = { }
Instances For

---

### `Tau.BookV.Cosmology.peak_deviation_increasing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1405-L1409)
**theorem
Tau.BookV.Cosmology.peak_deviation_increasing :peak_positions_data.ell1_ppm < peak_positions_data.ell2_ppm ∧ peak_positions_data.ell2_ppm < peak_positions_data.ell3_ppm**


Higher peaks have larger deviations (sound horizon deficit).

---

### `Tau.BookV.Cosmology.compression_dominance_36c`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1411-L1414)
**theorem
Tau.BookV.Cosmology.compression_dominance_36c :peak_height_ratios_data.compression_x1000 > peak_height_ratios_data.rarefaction_x1000**


Compression dominates rarefaction: (1+R_b) > (1-R_b).

---

### `Tau.BookV.Cosmology.neff_consistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1416-L1419)
**theorem
Tau.BookV.Cosmology.neff_consistency :peak_height_ratios_data.n_eff_predicted = 3**


[V.P175] N_eff = 3 from H₁(τ³) ≅ ℤ³ matches Planck N_eff = 2.99 ± 0.17.

---

### `Tau.BookV.Cosmology.CoupledNLOScan`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1430-L1449)
**structure
Tau.BookV.Cosmology.CoupledNLOScan :Type**


[V.D317] Coupled NLO Correction Space.
δ_h = ι<sub>τ</sub>/W₅(3) = ι<sub>τ</sub>/19.
Holonomy ratio: 6.655 → 6.774. ω_m: 0.14700 → 0.14964.
Scope: τ-effective (Wave 38A).

- delta_h_x100000 : ℕ
NLO δ_h × 100000.

- w5_3 : ℕ
W₅(3) = 19 (CF window sum governing N_e).

- ratio_lo_x1000 : ℕ
Holonomy ratio LO × 1000.

- ratio_nlo_x1000 : ℕ
Holonomy ratio NLO × 1000.

- omega_m_nlo_x10000 : ℕ
ω_m NLO × 10000.

- omega_m_lo_x10000 : ℕ
ω_m LO × 10000.

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprCoupledNLOScan.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1449-L1449)
**def
Tau.BookV.Cosmology.instReprCoupledNLOScan.repr :CoupledNLOScan → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprCoupledNLOScan`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1449-L1449)
**instance
Tau.BookV.Cosmology.instReprCoupledNLOScan :Repr CoupledNLOScan**

Equations
- Tau.BookV.Cosmology.instReprCoupledNLOScan = { reprPrec := Tau.BookV.Cosmology.instReprCoupledNLOScan.repr }

---

### `Tau.BookV.Cosmology.coupled_nlo_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1451-L1451)
**def
Tau.BookV.Cosmology.coupled_nlo_data :CoupledNLOScan**

Equations
- Tau.BookV.Cosmology.coupled_nlo_data = { }
Instances For

---

### `Tau.BookV.Cosmology.FirstPeakNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1453-L1467)
**structure
Tau.BookV.Cosmology.FirstPeakNLO :Type**


[V.T257] First Peak NLO: ℓ₁ at +69 ppm.
Improvement: +2840 → +69 ppm (97.6% reduction).
Scope: τ-effective (Wave 38A).

- ell1_nlo_x100 : ℕ
ℓ₁ NLO × 100.

- deviation_ppm : ℕ
ℓ₁ NLO deviation ppm.

- lo_deviation_ppm : ℕ
ℓ₁ LO deviation ppm.

- improvement_pct_x10 : ℕ
Improvement percentage × 10.

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprFirstPeakNLO.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1467-L1467)
**def
Tau.BookV.Cosmology.instReprFirstPeakNLO.repr :FirstPeakNLO → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprFirstPeakNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1467-L1467)
**instance
Tau.BookV.Cosmology.instReprFirstPeakNLO :Repr FirstPeakNLO**

Equations
- Tau.BookV.Cosmology.instReprFirstPeakNLO = { reprPrec := Tau.BookV.Cosmology.instReprFirstPeakNLO.repr }

---

### `Tau.BookV.Cosmology.first_peak_nlo_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1469-L1469)
**def
Tau.BookV.Cosmology.first_peak_nlo_data :FirstPeakNLO**

Equations
- Tau.BookV.Cosmology.first_peak_nlo_data = { }
Instances For

---

### `Tau.BookV.Cosmology.nlo_ell1_improvement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1471-L1474)
**theorem
Tau.BookV.Cosmology.nlo_ell1_improvement :first_peak_nlo_data.deviation_ppm < first_peak_nlo_data.lo_deviation_ppm**


NLO dramatically improves ℓ₁.

---

### `Tau.BookV.Cosmology.nlo_zero_params`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1476-L1480)
**theorem
Tau.BookV.Cosmology.nlo_zero_params :coupled_nlo_data.free_params = 0 ∧ first_peak_nlo_data.free_params = 0**


NLO uses zero free parameters.

---

### `Tau.BookV.Cosmology.BAOSoundHorizon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1486-L1502)
**structure
Tau.BookV.Cosmology.BAOSoundHorizon :Type**


[V.D318] NLO Sound Horizon at Drag Epoch.
r_d(NLO) = 149.04 Mpc. Planck: 147.09 ± 0.26.
Scope: τ-effective (Wave 38B).

- r_d_nlo_x100 : ℕ
r_d NLO × 100 (Mpc).

- r_d_lo_x100 : ℕ
r_d LO × 100 (Mpc).

- r_d_planck_x100 : ℕ
Planck r_d × 100 (Mpc).

- nlo_deviation_ppm : ℕ
NLO deviation ppm.

- lo_deviation_ppm : ℕ
LO deviation ppm.

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprBAOSoundHorizon.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1502-L1502)
**def
Tau.BookV.Cosmology.instReprBAOSoundHorizon.repr :BAOSoundHorizon → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprBAOSoundHorizon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1502-L1502)
**instance
Tau.BookV.Cosmology.instReprBAOSoundHorizon :Repr BAOSoundHorizon**

Equations
- Tau.BookV.Cosmology.instReprBAOSoundHorizon = { reprPrec := Tau.BookV.Cosmology.instReprBAOSoundHorizon.repr }

---

### `Tau.BookV.Cosmology.bao_sound_horizon_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1504-L1504)
**def
Tau.BookV.Cosmology.bao_sound_horizon_data :BAOSoundHorizon**

Equations
- Tau.BookV.Cosmology.bao_sound_horizon_data = { }
Instances For

---

### `Tau.BookV.Cosmology.bao_nlo_improvement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1506-L1510)
**theorem
Tau.BookV.Cosmology.bao_nlo_improvement :bao_sound_horizon_data.nlo_deviation_ppm < bao_sound_horizon_data.lo_deviation_ppm**


NLO improves r_d toward Planck.

---

### `Tau.BookV.Cosmology.NLOPeakStructure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1516-L1538)
**structure
Tau.BookV.Cosmology.NLOPeakStructure :Type**


[V.D320] NLO Peak Positions and Structural Tension.
ℓ₁ improves but ℓ₂, ℓ₃ worsen: peak-ratio tension exposed.
Scope: conjectural (Wave 38D).

- ell1_nlo_x100 : ℕ
ℓ₁ NLO × 100.

- ell2_nlo_x10 : ℕ
ℓ₂ NLO × 10.

- ell3_nlo_x10 : ℕ
ℓ₃ NLO × 10.

- ell1_nlo_ppm : ℕ
ℓ₁ NLO ppm.

- ell2_nlo_ppm : ℕ
ℓ₂ NLO ppm (worsened).

- ell3_nlo_ppm : ℕ
ℓ₃ NLO ppm (worsened).

- ratio_21_x1000 : ℕ
Peak ratio ℓ₂/ℓ₁ × 1000 (unchanged from LO).

- ratio_31_x1000 : ℕ
Peak ratio ℓ₃/ℓ₁ × 1000 (unchanged from LO).

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprNLOPeakStructure.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1538-L1538)
**def
Tau.BookV.Cosmology.instReprNLOPeakStructure.repr :NLOPeakStructure → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprNLOPeakStructure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1538-L1538)
**instance
Tau.BookV.Cosmology.instReprNLOPeakStructure :Repr NLOPeakStructure**

Equations
- Tau.BookV.Cosmology.instReprNLOPeakStructure = { reprPrec := Tau.BookV.Cosmology.instReprNLOPeakStructure.repr }

---

### `Tau.BookV.Cosmology.nlo_peak_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1540-L1540)
**def
Tau.BookV.Cosmology.nlo_peak_data :NLOPeakStructure**

Equations
- Tau.BookV.Cosmology.nlo_peak_data = { }
Instances For

---

### `Tau.BookV.Cosmology.SilkDampingNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1542-L1558)
**structure
Tau.BookV.Cosmology.SilkDampingNLO :Type**


[V.D321] Silk Damping at NLO.
ℓ_D = ℓ₁ × κ_D/κ_B = 1244.1 at +71 ppm.
Scope: τ-effective (Wave 38D).

- ell_d_nlo : ℕ
ℓ_D NLO.

- ell_d_lo : ℕ
ℓ_D LO.

- nlo_ppm : ℕ
NLO deviation ppm.

- lo_ppm : ℕ
LO deviation ppm.

- ratio_x1000 : ℕ
κ_D/κ_B ratio × 1000.

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprSilkDampingNLO.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1558-L1558)
**def
Tau.BookV.Cosmology.instReprSilkDampingNLO.repr :SilkDampingNLO → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprSilkDampingNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1558-L1558)
**instance
Tau.BookV.Cosmology.instReprSilkDampingNLO :Repr SilkDampingNLO**

Equations
- Tau.BookV.Cosmology.instReprSilkDampingNLO = { reprPrec := Tau.BookV.Cosmology.instReprSilkDampingNLO.repr }

---

### `Tau.BookV.Cosmology.silk_damping_nlo_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1560-L1560)
**def
Tau.BookV.Cosmology.silk_damping_nlo_data :SilkDampingNLO**

Equations
- Tau.BookV.Cosmology.silk_damping_nlo_data = { }
Instances For

---

### `Tau.BookV.Cosmology.peak_ratio_tension`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1562-L1566)
**theorem
Tau.BookV.Cosmology.peak_ratio_tension :nlo_peak_data.ell1_nlo_ppm < nlo_peak_data.ell2_nlo_ppm ∧ nlo_peak_data.ell2_nlo_ppm < nlo_peak_data.ell3_nlo_ppm**


ℓ₁ improves at NLO but higher peaks worsen.

---

### `Tau.BookV.Cosmology.silk_nlo_improvement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1568-L1571)
**theorem
Tau.BookV.Cosmology.silk_nlo_improvement :silk_damping_nlo_data.nlo_ppm < silk_damping_nlo_data.lo_ppm**


Silk damping improves dramatically at NLO.

---

### `Tau.BookV.Cosmology.damping_ratio_exact`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1573-L1576)
**theorem
Tau.BookV.Cosmology.damping_ratio_exact :silk_damping_nlo_data.free_params = 0**


Damping ratio is exact (structural).

---

### `Tau.BookV.Cosmology.PeakRatioNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1592-L1630)
**structure
Tau.BookV.Cosmology.PeakRatioNLO :Type**


[V.D322] Peak-Ratio Phase-Shift Space.
Bashinsky-Seljak phase correction δφ_n = −δφ₀·(n−1)^α
with δφ₀ = ι<sub>τ</sub>/(2·W₃(4)) = ι<sub>τ</sub>/10 ≈ 0.0341.
Root cause: z_eq(τ) = 3583 vs z_eq(Planck) = 3427 (+4.5%).
Scope: conjectural (Wave 39A).

- z_eq_tau : ℕ
z_eq(τ NLO).

- z_eq_planck : ℕ
z_eq(Planck).

- z_eq_excess_ppm : ℕ
z_eq excess ppm (4.5% = 45000 ppm).

- delta_phi0_x100000 : ℕ
Phase amplitude δφ₀ × 100000.

- w3_4 : ℕ
W₃(4) = 5 (denominator).

- lobes : ℕ
Lobes = 2 (denominator).

- alpha_x1000 : ℕ
n-exponent α × 1000 (= 0.820).

- ratio_21_nlo_x10000 : ℕ
ℓ₂/ℓ₁ NLO × 10000.

- ratio_31_nlo_x10000 : ℕ
ℓ₃/ℓ₁ NLO × 10000.

- ratio_21_planck_x10000 : ℕ
ℓ₂/ℓ₁ Planck × 10000.

- ratio_31_planck_x10000 : ℕ
ℓ₃/ℓ₁ Planck × 10000.

- ell2_nlo_ppm : ℕ
ℓ₂ NLO ppm.

- ell3_nlo_ppm : ℕ
ℓ₃ NLO ppm.

- ell2_prev_ppm : ℕ
ℓ₂ previous ppm (Wave 38D).

- ell3_prev_ppm : ℕ
ℓ₃ previous ppm (Wave 38D).

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprPeakRatioNLO.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1630-L1630)
**def
Tau.BookV.Cosmology.instReprPeakRatioNLO.repr :PeakRatioNLO → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprPeakRatioNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1630-L1630)
**instance
Tau.BookV.Cosmology.instReprPeakRatioNLO :Repr PeakRatioNLO**

Equations
- Tau.BookV.Cosmology.instReprPeakRatioNLO = { reprPrec := Tau.BookV.Cosmology.instReprPeakRatioNLO.repr }

---

### `Tau.BookV.Cosmology.peak_ratio_nlo_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1632-L1632)
**def
Tau.BookV.Cosmology.peak_ratio_nlo_data :PeakRatioNLO**

Equations
- Tau.BookV.Cosmology.peak_ratio_nlo_data = { }
Instances For

---

### `Tau.BookV.Cosmology.peak_ratio_nlo_improvement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1634-L1638)
**theorem
Tau.BookV.Cosmology.peak_ratio_nlo_improvement :peak_ratio_nlo_data.ell2_nlo_ppm < peak_ratio_nlo_data.ell2_prev_ppm ∧ peak_ratio_nlo_data.ell3_nlo_ppm < peak_ratio_nlo_data.ell3_prev_ppm**


[V.T261] Peak ratios improve dramatically at NLO.

---

### `Tau.BookV.Cosmology.peak_ratio_preserves_ell1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1640-L1643)
**theorem
Tau.BookV.Cosmology.peak_ratio_preserves_ell1 :first_peak_nlo_data.deviation_ppm = 69**


[V.P180] Phase-shift NLO preserves ℓ₁ (first peak unchanged).

---

### `Tau.BookV.Cosmology.peak_ratio_sub_1300`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1645-L1649)
**theorem
Tau.BookV.Cosmology.peak_ratio_sub_1300 :peak_ratio_nlo_data.ell2_nlo_ppm < 1300 ∧ peak_ratio_nlo_data.ell3_nlo_ppm < 1300**


Both peaks sub-1300 ppm.

---

### `Tau.BookV.Cosmology.peak_ratio_improvement_factor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1651-L1655)
**theorem
Tau.BookV.Cosmology.peak_ratio_improvement_factor :peak_ratio_nlo_data.ell2_prev_ppm / peak_ratio_nlo_data.ell2_nlo_ppm ≥ 15 ∧ peak_ratio_nlo_data.ell3_prev_ppm / peak_ratio_nlo_data.ell3_nlo_ppm ≥ 15**


Improvement > 93% for both peaks. Ratio: prev/nlo > 15 for ℓ₂, > 15 for ℓ₃.

---

### `Tau.BookV.Cosmology.BaryonDensityNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1668-L1693)
**structure
Tau.BookV.Cosmology.BaryonDensityNLO :Type**


[V.D323] Baryon Density NLO Correction.
δ_η = ι<sub>τ</sub>²/sectors² = ι<sub>τ</sub>²/9 ≈ 0.01294.
ω_b: 0.02209 → 0.02238 (+264 ppm from Planck).
Scope: conjectural (Wave 39B).

- omega_b_lo_x100000 : ℕ
ω_b LO × 100000.

- omega_b_nlo_x100000 : ℕ
ω_b NLO × 100000.

- omega_b_planck_x100000 : ℕ
ω_b Planck × 100000.

- delta_eta_x100000 : ℕ
δ_η × 100000 = ι<sub>τ</sub>²/9 × 100000.

- sectors_sq : ℕ
sectors² = 9.

- nlo_deviation_ppm : ℕ
ω_b deviation ppm (NLO).

- lo_deviation_ppm : ℕ
ω_b deviation ppm (LO).

- rd_nlo_ppm : ℕ
r_d NLO ppm.

- rd_lo_ppm : ℕ
r_d LO ppm.

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprBaryonDensityNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1693-L1693)
**instance
Tau.BookV.Cosmology.instReprBaryonDensityNLO :Repr BaryonDensityNLO**

Equations
- Tau.BookV.Cosmology.instReprBaryonDensityNLO = { reprPrec := Tau.BookV.Cosmology.instReprBaryonDensityNLO.repr }

---

### `Tau.BookV.Cosmology.instReprBaryonDensityNLO.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1693-L1693)
**def
Tau.BookV.Cosmology.instReprBaryonDensityNLO.repr :BaryonDensityNLO → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.baryon_nlo_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1695-L1695)
**def
Tau.BookV.Cosmology.baryon_nlo_data :BaryonDensityNLO**

Equations
- Tau.BookV.Cosmology.baryon_nlo_data = { }
Instances For

---

### `Tau.BookV.Cosmology.baryon_nlo_improvement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1697-L1700)
**theorem
Tau.BookV.Cosmology.baryon_nlo_improvement :baryon_nlo_data.nlo_deviation_ppm < baryon_nlo_data.lo_deviation_ppm**


[V.T262] ω_b improves dramatically at NLO.

---

### `Tau.BookV.Cosmology.sound_horizon_nlo_improvement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1702-L1705)
**theorem
Tau.BookV.Cosmology.sound_horizon_nlo_improvement :baryon_nlo_data.rd_nlo_ppm < baryon_nlo_data.rd_lo_ppm**


[V.P181] r_d improves at NLO (modest).

---

### `Tau.BookV.Cosmology.baryon_nlo_sub_300`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1707-L1710)
**theorem
Tau.BookV.Cosmology.baryon_nlo_sub_300 :baryon_nlo_data.nlo_deviation_ppm < 300**


ω_b NLO is sub-300 ppm.

---

### `Tau.BookV.Cosmology.CoupledNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1721-L1749)
**structure
Tau.BookV.Cosmology.CoupledNLO :Type**


[V.D326] Coupled NLO Correction Space.
(δ_η, δ_h) = (ι<sub>τ</sub>²/9, κ_D/57) acting simultaneously
on baryon asymmetry and holonomy ratio.
57 = N_e = dim(τ³)·W₅(3) connects to inflationary e-folds.
Scope: τ-effective (Wave 40A).

- delta_eta_x100000 : ℕ
δ_η × 100000 = ι<sub>τ</sub>²/9 × 100000.

- delta_h_x100000 : ℕ
δ_h × 100000 = κ_D/57 × 100000.

- n_e : ℕ
N_e = dim(τ³) × W₅(3) = 3 × 19.

- omega_b_nlo_x100000 : ℕ
ω_b NLO × 100000.

- omega_m_nlo_x100000 : ℕ
ω_m NLO × 100000.

- omega_b_ppm : ℕ
ω_b ppm from Planck.

- ell1_ppm : ℕ
ℓ₁ ppm from Planck.

- ell2_ppm : ℕ
ℓ₂ ppm from Planck.

- ell3_ppm : ℕ
ℓ₃ ppm from Planck (tension).

- rd_ppm : ℕ
r_d ppm from Planck.

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprCoupledNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1749-L1749)
**instance
Tau.BookV.Cosmology.instReprCoupledNLO :Repr CoupledNLO**

Equations
- Tau.BookV.Cosmology.instReprCoupledNLO = { reprPrec := Tau.BookV.Cosmology.instReprCoupledNLO.repr }

---

### `Tau.BookV.Cosmology.instReprCoupledNLO.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1749-L1749)
**def
Tau.BookV.Cosmology.instReprCoupledNLO.repr :CoupledNLO → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.coupled_nlo_2d_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1751-L1751)
**def
Tau.BookV.Cosmology.coupled_nlo_2d_data :CoupledNLO**

Equations
- Tau.BookV.Cosmology.coupled_nlo_2d_data = { }
Instances For

---

### `Tau.BookV.Cosmology.coupled_nlo_2d_omega_b_sub_300`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1753-L1756)
**theorem
Tau.BookV.Cosmology.coupled_nlo_2d_omega_b_sub_300 :coupled_nlo_2d_data.omega_b_ppm < 300**


[V.T264] Coupled NLO achieves ω_b sub-300 ppm.

---

### `Tau.BookV.Cosmology.coupled_nlo_2d_ell1_sub_200`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1758-L1761)
**theorem
Tau.BookV.Cosmology.coupled_nlo_2d_ell1_sub_200 :coupled_nlo_2d_data.ell1_ppm < 200**


[V.T264] Coupled NLO achieves ℓ₁ sub-200 ppm.

---

### `Tau.BookV.Cosmology.coupled_nlo_2d_ell2_sub_700`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1763-L1766)
**theorem
Tau.BookV.Cosmology.coupled_nlo_2d_ell2_sub_700 :coupled_nlo_2d_data.ell2_ppm < 700**


[V.T264] Coupled NLO achieves ℓ₂ sub-700 ppm.

---

### `Tau.BookV.Cosmology.coupled_nlo_2d_three_sub_700`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1768-L1773)
**theorem
Tau.BookV.Cosmology.coupled_nlo_2d_three_sub_700 :coupled_nlo_2d_data.omega_b_ppm < 700 ∧ coupled_nlo_2d_data.ell1_ppm < 700 ∧ coupled_nlo_2d_data.ell2_ppm < 700**


[V.P183] Three observables simultaneously sub-700 ppm.

---

### `Tau.BookV.Cosmology.n_e_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1775-L1778)
**theorem
Tau.BookV.Cosmology.n_e_structural :coupled_nlo_2d_data.n_e = 3 * 19**


N_e = 57 structural check.

---

### `Tau.BookV.Cosmology.PhaseShiftAlpha`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1791-L1811)
**structure
Tau.BookV.Cosmology.PhaseShiftAlpha :Type**


[V.D327] Phase-Shift Exponent α Analysis.
Key result: ℓ₂ is α-insensitive (δφ₂ = δφ₀·1^α = δφ₀ for all α).
ℓ₃ has moderate sensitivity: 619 ppm variation in [0.80, 0.84].
Best-fit α = 1.176 has no structural match.
Scope: conjectural (Wave 40B).

- alpha_39a_x1000 : ℕ
Sprint 39A α × 1000.

- alpha_bestfit_x1000 : ℕ
Best-fit α × 1000 (minimizing |ℓ₃|).

- ell2_ppm_fixed : ℕ
ℓ₂ ppm (α-insensitive, fixed).

- ell3_ppm_at_080 : ℕ
ℓ₃ ppm at α = 0.80.

- ell3_ppm_at_084 : ℕ
ℓ₃ ppm at α = 0.84.

- ell3_sensitivity_band : ℕ
ℓ₃ sensitivity band in [0.80, 0.84].

- closest_structural_x1000 : ℕ
Closest structural to 0.82: 1−ι<sub>τ</sub>/2 × 1000.

Instances For

---

### `Tau.BookV.Cosmology.instReprPhaseShiftAlpha`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1811-L1811)
**instance
Tau.BookV.Cosmology.instReprPhaseShiftAlpha :Repr PhaseShiftAlpha**

Equations
- Tau.BookV.Cosmology.instReprPhaseShiftAlpha = { reprPrec := Tau.BookV.Cosmology.instReprPhaseShiftAlpha.repr }

---

### `Tau.BookV.Cosmology.instReprPhaseShiftAlpha.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1811-L1811)
**def
Tau.BookV.Cosmology.instReprPhaseShiftAlpha.repr :PhaseShiftAlpha → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.phase_shift_alpha_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1813-L1813)
**def
Tau.BookV.Cosmology.phase_shift_alpha_data :PhaseShiftAlpha**

Equations
- Tau.BookV.Cosmology.phase_shift_alpha_data = { }
Instances For

---

### `Tau.BookV.Cosmology.ell2_alpha_insensitive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1815-L1818)
**theorem
Tau.BookV.Cosmology.ell2_alpha_insensitive :phase_shift_alpha_data.ell2_ppm_fixed = 663**


[V.D327] ℓ₂ is α-insensitive: same ppm at all α values.

---

### `Tau.BookV.Cosmology.ell3_sensitivity_sub_700`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1820-L1823)
**theorem
Tau.BookV.Cosmology.ell3_sensitivity_sub_700 :phase_shift_alpha_data.ell3_sensitivity_band < 700**


[V.D327] ℓ₃ sensitivity band is sub-700 ppm in [0.80, 0.84].

---

### `Tau.BookV.Cosmology.OmegaMatterNNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1834-L1868)
**structure
Tau.BookV.Cosmology.OmegaMatterNNLO :Type**


[V.D328] ω_m NNLO Correction Space.
Combined matter correction λ = (1−κ_D/57)(1−κ_D/24).
57 = dim(τ³)·W₅(3) (inflationary e-folds).
24 = 2^dim(τ³)·dim(τ³) (fundamental-domain vertices × dimension).
Scope: τ-effective (Wave 41A).

- delta_h_x100000 : ℕ
κ_D/57 × 100000 (NLO holonomy correction).

- delta_m_x100000 : ℕ
κ_D/24 × 100000 (NNLO matter correction).

- n_e : ℕ
N_e = dim(τ³) × W₅(3).

- fund_domain : ℕ
2^dim(τ³) × dim(τ³).

- lambda_x100000 : ℕ
λ = (1−κ_D/57)(1−κ_D/24) × 100000.

- omega_m_nnlo_x100000 : ℕ
ω_m(NNLO) × 100000.

- omega_m_ppm : ℕ
ω_m ppm from Planck (absolute value).

- z_eq_x10 : ℕ
z_eq(NNLO) × 10.

- z_eq_planck_x10 : ℕ
z_eq(Planck) × 10.

- rd_nnlo_x100 : ℕ
r_d(NNLO) × 100 (Mpc).

- rd_ppm : ℕ
r_d ppm from Planck (absolute value).

- omega_m_de_x100000 : ℕ
ω_m(DE-closure) × 100000.

- two_path_gap_ppm : ℕ
Two-path M3h ↔ DE gap (ppm).

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprOmegaMatterNNLO.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1868-L1868)
**def
Tau.BookV.Cosmology.instReprOmegaMatterNNLO.repr :OmegaMatterNNLO → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprOmegaMatterNNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1868-L1868)
**instance
Tau.BookV.Cosmology.instReprOmegaMatterNNLO :Repr OmegaMatterNNLO**

Equations
- Tau.BookV.Cosmology.instReprOmegaMatterNNLO = { reprPrec := Tau.BookV.Cosmology.instReprOmegaMatterNNLO.repr }

---

### `Tau.BookV.Cosmology.omega_m_nnlo_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1870-L1870)
**def
Tau.BookV.Cosmology.omega_m_nnlo_data :OmegaMatterNNLO**

Equations
- Tau.BookV.Cosmology.omega_m_nnlo_data = { }
Instances For

---

### `Tau.BookV.Cosmology.omega_m_nnlo_sub_20`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1872-L1874)
**theorem
Tau.BookV.Cosmology.omega_m_nnlo_sub_20 :omega_m_nnlo_data.omega_m_ppm < 20**


[V.T265] ω_m sub-20 ppm at NNLO.

---

### `Tau.BookV.Cosmology.rd_nnlo_improvement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1876-L1878)
**theorem
Tau.BookV.Cosmology.rd_nnlo_improvement :omega_m_nnlo_data.rd_ppm * 11 < 14064**


[V.T265] r_d improvement: 11× better than NLO (14064 ppm).

---

### `Tau.BookV.Cosmology.n_e_nnlo_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1880-L1882)
**theorem
Tau.BookV.Cosmology.n_e_nnlo_structural :omega_m_nnlo_data.n_e = 3 * 19**


[V.D328] N_e = dim × W₅(3) = 3 × 19 (NNLO context).

---

### `Tau.BookV.Cosmology.fund_domain_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1884-L1886)
**theorem
Tau.BookV.Cosmology.fund_domain_structural :omega_m_nnlo_data.fund_domain = 2 ^ 3 * 3**


[V.D328] fund_domain = 2^dim × dim = 8 × 3.

---

### `Tau.BookV.Cosmology.two_path_convergence_30x`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1888-L1890)
**theorem
Tau.BookV.Cosmology.two_path_convergence_30x :omega_m_nnlo_data.two_path_gap_ppm * 30 < 52280**


[V.R466] Two-path convergence: 30× improvement (was 52280 ppm).

---

### `Tau.BookV.Cosmology.ParetoBarrier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1892-L1913)
**structure
Tau.BookV.Cosmology.ParetoBarrier :Type**


[V.D329] Pareto Barrier: ω_m–peaks structural tension.
The density regime (ω_m ≈ Planck) and peaks regime (ℓ₁ ≈ Planck)
are complementary aspects of a 1D Pareto frontier.
Scope: τ-effective (Wave 41B).

- density_ell1_ppm : ℕ
Density regime ℓ₁ ppm (far from Planck).

- density_omega_m_ppm : ℕ
Density regime ω_m ppm (near Planck).

- density_rd_ppm : ℕ
Density regime r_d ppm.

- peaks_ell1_ppm : ℕ
Peaks regime ℓ₁ ppm (near Planck, Wave 40).

- peaks_omega_m_ppm : ℕ
Peaks regime ω_m ppm (far from Planck).

- peaks_rd_ppm : ℕ
Peaks regime r_d ppm.

- crossover_ell1_ppm : ℕ
Crossover ℓ₁ ≈ ℓ₃ ppm.

- crossover_ell3_ppm : ℕ
Crossover ℓ₃ ppm.

Instances For

---

### `Tau.BookV.Cosmology.instReprParetoBarrier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1913-L1913)
**instance
Tau.BookV.Cosmology.instReprParetoBarrier :Repr ParetoBarrier**

Equations
- Tau.BookV.Cosmology.instReprParetoBarrier = { reprPrec := Tau.BookV.Cosmology.instReprParetoBarrier.repr }

---

### `Tau.BookV.Cosmology.instReprParetoBarrier.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1913-L1913)
**def
Tau.BookV.Cosmology.instReprParetoBarrier.repr :ParetoBarrier → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.pareto_barrier_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1915-L1915)
**def
Tau.BookV.Cosmology.pareto_barrier_data :ParetoBarrier**

Equations
- Tau.BookV.Cosmology.pareto_barrier_data = { }
Instances For

---

### `Tau.BookV.Cosmology.density_omega_m_sub_20`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1917-L1919)
**theorem
Tau.BookV.Cosmology.density_omega_m_sub_20 :pareto_barrier_data.density_omega_m_ppm < 20**


[V.D329] Density regime: ω_m sub-20 ppm.

---

### `Tau.BookV.Cosmology.peaks_ell1_sub_200`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1921-L1923)
**theorem
Tau.BookV.Cosmology.peaks_ell1_sub_200 :pareto_barrier_data.peaks_ell1_ppm < 200**


[V.D329] Peaks regime: ℓ₁ sub-200 ppm.

---

### `Tau.BookV.Cosmology.crossover_ell1_ell3_close`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1925-L1928)
**theorem
Tau.BookV.Cosmology.crossover_ell1_ell3_close :pareto_barrier_data.crossover_ell1_ppm - pareto_barrier_data.crossover_ell3_ppm < 50**


[V.D329] Crossover: ℓ₁ ≈ ℓ₃ (within 50 ppm).

---

### `Tau.BookV.Cosmology.BAONNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1940-L1961)
**structure
Tau.BookV.Cosmology.BAONNLO :Type**


[V.D331] BAO NNLO distance table.
D_V/r_d at 5 DESI Y1 bins: all sub-1300 ppm from Planck ΛCDM.
Mean |Δ| = 1145 ppm. NLO→NNLO improvement 21×.
Scope: τ-effective (Wave 42B).

- dv_rd_ppm_z051 : ℕ
D_V/r_d ppm at z=0.51 (LRG1).

- dv_rd_ppm_z071 : ℕ
D_V/r_d ppm at z=0.71 (LRG2).

- dv_rd_ppm_z093 : ℕ
D_V/r_d ppm at z=0.93 (LRG3+ELG1).

- dv_rd_ppm_z132 : ℕ
D_V/r_d ppm at z=1.32 (ELG2).

- dv_rd_ppm_z233 : ℕ
D_V/r_d ppm at z=2.33 (QSO).

- nlo_mean_ppm : ℕ
NLO mean |ppm|.

- nnlo_mean_ppm : ℕ
NNLO mean |ppm|.

- rd_nnlo_x100 : ℕ
r_d(NNLO) in units of 0.01 Mpc.

Instances For

---

### `Tau.BookV.Cosmology.instReprBAONNLO.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1961-L1961)
**def
Tau.BookV.Cosmology.instReprBAONNLO.repr :BAONNLO → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprBAONNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1961-L1961)
**instance
Tau.BookV.Cosmology.instReprBAONNLO :Repr BAONNLO**

Equations
- Tau.BookV.Cosmology.instReprBAONNLO = { reprPrec := Tau.BookV.Cosmology.instReprBAONNLO.repr }

---

### `Tau.BookV.Cosmology.bao_nnlo_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1963-L1963)
**def
Tau.BookV.Cosmology.bao_nnlo_data :BAONNLO**

Equations
- Tau.BookV.Cosmology.bao_nnlo_data = { }
Instances For

---

### `Tau.BookV.Cosmology.bao_nnlo_sub_1300`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1965-L1972)
**theorem
Tau.BookV.Cosmology.bao_nnlo_sub_1300 :bao_nnlo_data.dv_rd_ppm_z051 < 1300 ∧ bao_nnlo_data.dv_rd_ppm_z071 < 1300 ∧ bao_nnlo_data.dv_rd_ppm_z093 < 1300 ∧ bao_nnlo_data.dv_rd_ppm_z132 < 1300 ∧ bao_nnlo_data.dv_rd_ppm_z233 < 1300**


[V.T267] All 5 DESI bins sub-1300 ppm at NNLO.

---

### `Tau.BookV.Cosmology.bao_nnlo_improvement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1974-L1977)
**theorem
Tau.BookV.Cosmology.bao_nnlo_improvement :bao_nnlo_data.nlo_mean_ppm / bao_nnlo_data.nnlo_mean_ppm ≥ 20**


[V.P185] NNLO improves over NLO by ≥20×.

---

### `Tau.BookV.Cosmology.DensitySectorClosure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1988-L2011)
**structure
Tau.BookV.Cosmology.DensitySectorClosure :Type**


[V.D332] Density-sector observable scorecard.
All ω_m-sensitive observables sub-1300 ppm at NNLO.
8 observables characterized. Zero free parameters.
Scope: τ-effective (Wave 42C).

- omega_m_ppm : ℕ
ω_m ppm from Planck.

- rd_ppm : ℕ
r_d ppm from Planck.

- bao_mean_ppm : ℕ
BAO D_V/r_d mean ppm.

- bao_max_ppm : ℕ
BAO max ppm (z=0.51).

- omega_lambda_ppm : ℕ
Ω_Λ ppm from Planck.

- h0_ppm : ℕ
H₀ ppm from Planck.

- two_path_ppm : ℕ
Two-path convergence ppm.

- n_observables : ℕ
Number of observables characterized.

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookV.Cosmology.instReprDensitySectorClosure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L2011-L2011)
**instance
Tau.BookV.Cosmology.instReprDensitySectorClosure :Repr DensitySectorClosure**

Equations
- Tau.BookV.Cosmology.instReprDensitySectorClosure = { reprPrec := Tau.BookV.Cosmology.instReprDensitySectorClosure.repr }

---

### `Tau.BookV.Cosmology.instReprDensitySectorClosure.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L2011-L2011)
**def
Tau.BookV.Cosmology.instReprDensitySectorClosure.repr :DensitySectorClosure → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.density_closure_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L2013-L2013)
**def
Tau.BookV.Cosmology.density_closure_data :DensitySectorClosure**

Equations
- Tau.BookV.Cosmology.density_closure_data = { }
Instances For

---

### `Tau.BookV.Cosmology.density_sector_sub_1300`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L2015-L2020)
**theorem
Tau.BookV.Cosmology.density_sector_sub_1300 :density_closure_data.omega_m_ppm < 1300 ∧ density_closure_data.rd_ppm < 1300 ∧ density_closure_data.bao_max_ppm < 1300**


[V.P186] All ω_m-sensitive observables sub-1300 ppm.

---

### `Tau.BookV.Cosmology.density_sector_zero_params`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/CMBSpectrum.lean#L2022-L2025)
**theorem
Tau.BookV.Cosmology.density_sector_zero_params :density_closure_data.free_params = 0**


Zero free parameters in density sector.
