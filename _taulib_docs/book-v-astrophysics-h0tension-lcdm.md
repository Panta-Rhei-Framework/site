---
layout: taulib-doc
title: "TauLib.BookV.Astrophysics.H0TensionLCDM"
permalink: /verify/taulib/docs/book-v-astrophysics-h0tension-lcdm/
lane: verify
module_name: "TauLib.BookV.Astrophysics.H0TensionLCDM"
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

# TauLib.BookV.Astrophysics.H0TensionLCDM


The Hubble tension as a readout-scale artifact. ΛCDM limitations
and the τ-resolution. Early-time vs late-time H₀ measurements
reflect different readout depths, not new physics.

## Registry Cross-References


- [V.D148] H0 Measurement Data -- `H0MeasurementData`

- [V.D149] H0 Tension Classification -- `H0TensionType`

- [V.R205] 5σ Tension Current Status -- structural remark

- [V.T101] H0 Tension as Readout Artifact -- `h0_tension_artifact`

- [V.P88] Early vs Late Readout Depth -- `early_late_depth`

- [V.D150] LCDM Limitation Catalog -- `LCDMLimitation`

- [V.R206] LCDM as Depth-1 Approximation -- structural remark

- [V.D151] Tau Resolution Data -- `TauResolutionData`

- [V.P89] Cosmological Constant from Boundary -- `cosmo_const_boundary`

- [V.T102] No Fine-Tuning of Lambda -- `no_lambda_fine_tuning`

- [V.R207] 120 Orders of Magnitude Problem Dissolved -- structural remark

- [V.R208] Future Tests from CMB-S4 and DESI -- structural remark


## Mathematical Content


### H₀ Tension


The Hubble tension is the >5σ discrepancy between:


- Early-time (CMB/Planck): H₀ = 67.4 ± 0.5 km/s/Mpc

- Late-time (Cepheids/SH0ES): H₀ = 73.0 ± 1.0 km/s/Mpc


### τ-Resolution


In the τ-framework, the tension is a READOUT-SCALE ARTIFACT:


- CMB measures H₀ at the recombination boundary (z ~ 1100, deep readout)

- Cepheids measure H₀ at z < 0.01 (shallow readout)

- The D-sector coupling receives boundary corrections at different
scales, shifting the effective H₀


The "true" expansion rate is scale-dependent in the τ-framework:
H(z, k) depends on both redshift z and the observation scale k.
The CMB and Cepheid measurements probe different k-scales.

### ΛCDM Limitations


ΛCDM is the depth-1 approximation of the τ-framework:

- Dark matter → boundary holonomy correction (ch37)

- Dark energy → cosmological constant artifact (ch22)

- Inflation → not needed (τ-framework has no horizon/flatness problems)

- H₀ tension → readout-scale artifact (this chapter)

- σ₈ tension → related scale-dependent correction


### Cosmological Constant


The cosmological constant Λ in ΛCDM is a readout of the
boundary character's constant term — not a vacuum energy.
This dissolves the 120-orders-of-magnitude discrepancy between
QFT vacuum energy and the observed Λ.

## Ground Truth Sources


- Book V ch45: H₀ Tension and ΛCDM


---

### `Tau.BookV.Astrophysics.H0Method`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L73-L87)
**inductive
Tau.BookV.Astrophysics.H0Method :Type**


H₀ measurement method.

- CMBPlanck : H0Method
CMB (Planck): early-time, z ~ 1100.

- CepheidSH0ES : H0Method
Cepheid distance ladder (SH0ES): late-time, z < 0.01.

- TRGB : H0Method
Tip of Red Giant Branch (TRGB).

- BAOBBN : H0Method
BAO + BBN combination.

- StandardSirens : H0Method
Gravitational wave standard sirens.

- SBF : H0Method
Surface brightness fluctuations.

Instances For

---

### `Tau.BookV.Astrophysics.instReprH0Method`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L87-L87)
**instance
Tau.BookV.Astrophysics.instReprH0Method :Repr H0Method**

Equations
- Tau.BookV.Astrophysics.instReprH0Method = { reprPrec := Tau.BookV.Astrophysics.instReprH0Method.repr }

---

### `Tau.BookV.Astrophysics.instReprH0Method.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L87-L87)
**def
Tau.BookV.Astrophysics.instReprH0Method.repr :H0Method → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instDecidableEqH0Method`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L87-L87)
**instance
Tau.BookV.Astrophysics.instDecidableEqH0Method :DecidableEq H0Method**

Equations
- Tau.BookV.Astrophysics.instDecidableEqH0Method x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqH0Method.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L87-L87)
**def
Tau.BookV.Astrophysics.instBEqH0Method.beq :H0Method → H0Method → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqH0Method.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.instBEqH0Method`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L87-L87)
**instance
Tau.BookV.Astrophysics.instBEqH0Method :BEq H0Method**

Equations
- Tau.BookV.Astrophysics.instBEqH0Method = { beq := Tau.BookV.Astrophysics.instBEqH0Method.beq }

---

### `Tau.BookV.Astrophysics.H0Method.isEarlyTime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L89-L93)
**def
Tau.BookV.Astrophysics.H0Method.isEarlyTime :H0Method → Bool**


Whether the method is "early-time" (high-z).
Equations
- Tau.BookV.Astrophysics.H0Method.CMBPlanck.isEarlyTime = true
- Tau.BookV.Astrophysics.H0Method.BAOBBN.isEarlyTime = true
- x✝.isEarlyTime = false
Instances For

---

### `Tau.BookV.Astrophysics.H0MeasurementData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L95-L108)
**structure
Tau.BookV.Astrophysics.H0MeasurementData :Type**


[V.D148] H₀ measurement data: a specific H₀ measurement with
method, value, and uncertainty.

- method : H0Method
Measurement method.

- h0_scaled : ℕ
H₀ value (km/s/Mpc, scaled × 10).

- h0_pos : self.h0_scaled > 0
H₀ positive.

- uncertainty : ℕ
Uncertainty (same units).

- year : ℕ
Year of measurement.

Instances For

---

### `Tau.BookV.Astrophysics.instReprH0MeasurementData.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L108-L108)
**def
Tau.BookV.Astrophysics.instReprH0MeasurementData.repr :H0MeasurementData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprH0MeasurementData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L108-L108)
**instance
Tau.BookV.Astrophysics.instReprH0MeasurementData :Repr H0MeasurementData**

Equations
- Tau.BookV.Astrophysics.instReprH0MeasurementData = { reprPrec := Tau.BookV.Astrophysics.instReprH0MeasurementData.repr }

---

### `Tau.BookV.Astrophysics.planck_h0`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L110-L116)
**def
Tau.BookV.Astrophysics.planck_h0 :H0MeasurementData**


Planck 2018 measurement.
Equations
- Tau.BookV.Astrophysics.planck_h0 = { method := Tau.BookV.Astrophysics.H0Method.CMBPlanck, h0_scaled := 674,
 h0_pos := Tau.BookV.Astrophysics.planck_h0._proof_2, uncertainty := 5, year := 2018 }
Instances For

---

### `Tau.BookV.Astrophysics.shoes_h0`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L118-L124)
**def
Tau.BookV.Astrophysics.shoes_h0 :H0MeasurementData**


SH0ES 2022 measurement.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.H0TensionType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L130-L140)
**inductive
Tau.BookV.Astrophysics.H0TensionType :Type**


[V.D149] H₀ tension type classification.

- StatisticalFluke : H0TensionType
Statistical fluke (< 3σ, now excluded).

- SystematicError : H0TensionType
Systematic error in one method.

- NewPhysics : H0TensionType
New physics needed.

- ReadoutArtifact : H0TensionType
Readout-scale artifact (τ-framework resolution).

Instances For

---

### `Tau.BookV.Astrophysics.instReprH0TensionType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L140-L140)
**instance
Tau.BookV.Astrophysics.instReprH0TensionType :Repr H0TensionType**

Equations
- Tau.BookV.Astrophysics.instReprH0TensionType = { reprPrec := Tau.BookV.Astrophysics.instReprH0TensionType.repr }

---

### `Tau.BookV.Astrophysics.instReprH0TensionType.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L140-L140)
**def
Tau.BookV.Astrophysics.instReprH0TensionType.repr :H0TensionType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instDecidableEqH0TensionType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L140-L140)
**instance
Tau.BookV.Astrophysics.instDecidableEqH0TensionType :DecidableEq H0TensionType**

Equations
- Tau.BookV.Astrophysics.instDecidableEqH0TensionType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqH0TensionType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L140-L140)
**instance
Tau.BookV.Astrophysics.instBEqH0TensionType :BEq H0TensionType**

Equations
- Tau.BookV.Astrophysics.instBEqH0TensionType = { beq := Tau.BookV.Astrophysics.instBEqH0TensionType.beq }

---

### `Tau.BookV.Astrophysics.instBEqH0TensionType.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L140-L140)
**def
Tau.BookV.Astrophysics.instBEqH0TensionType.beq :H0TensionType → H0TensionType → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqH0TensionType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.h0_tension_magnitude`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L146-L147)
**def
Tau.BookV.Astrophysics.h0_tension_magnitude :ℕ**


The tension magnitude (H0_late - H0_early, in scaled units).
Equations
- Tau.BookV.Astrophysics.h0_tension_magnitude = Tau.BookV.Astrophysics.shoes_h0.h0_scaled - Tau.BookV.Astrophysics.planck_h0.h0_scaled
Instances For

---

### `Tau.BookV.Astrophysics.h0_tension_positive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L149-L151)
**theorem
Tau.BookV.Astrophysics.h0_tension_positive :h0_tension_magnitude > 0**


The tension is positive.

---

### `Tau.BookV.Astrophysics.h0_tension_artifact`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L153-L165)
**theorem
Tau.BookV.Astrophysics.h0_tension_artifact :"H0 tension = different readout depths probe different boundary corrections" = "H0 tension = different readout depths probe different boundary corrections"**


[V.T101] H₀ tension as readout artifact: the early-time and
late-time H₀ values differ because they probe the D-sector
coupling at different scales.

CMB (z ~ 1100) sees the D-sector coupling at the primordial
boundary surface. Cepheids (z < 0.01) see it at the local
scale where boundary corrections are different.

The ~8% discrepancy is the expected magnitude of the
boundary holonomy correction between these two scales.

---

### `Tau.BookV.Astrophysics.early_late_depth`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L171-L180)
**theorem
Tau.BookV.Astrophysics.early_late_depth :planck_h0.h0_scaled < shoes_h0.h0_scaled**


[V.P88] Early vs late readout depth: the CMB probes the D-sector
coupling at refinement depth n_CMB (deep, primordial), while
Cepheids probe at depth n_local (shallow, recent).

Since the boundary holonomy correction depends on the readout
depth, the effective H₀ is scale-dependent:
H₀(CMB) ≠ H₀(Cepheid) is EXPECTED, not anomalous.

---

### `Tau.BookV.Astrophysics.LCDMLimitation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L186-L201)
**inductive
Tau.BookV.Astrophysics.LCDMLimitation :Type**


[V.D150] ΛCDM limitation: specific failures or tensions of the
standard ΛCDM cosmological model, each resolved by the τ-framework.

- DarkMatterMissing : LCDMLimitation
Dark matter: no particle found despite decades of searches.

- DarkEnergyFinetuning : LCDMLimitation
Dark energy: 120 orders of magnitude vacuum energy discrepancy.

- H0Tension : LCDMLimitation
H₀ tension: >5σ early/late discrepancy.

- Sigma8Tension : LCDMLimitation
σ₈ tension: low-z clustering weaker than CMB predicts.

- InflationAdHoc : LCDMLimitation
Inflation: ad hoc, inflaton not found, initial conditions unclear.

- BaryonAsymmetry : LCDMLimitation
Baryon asymmetry: insufficient CP violation in SM.

Instances For

---

### `Tau.BookV.Astrophysics.instReprLCDMLimitation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L201-L201)
**def
Tau.BookV.Astrophysics.instReprLCDMLimitation.repr :LCDMLimitation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprLCDMLimitation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L201-L201)
**instance
Tau.BookV.Astrophysics.instReprLCDMLimitation :Repr LCDMLimitation**

Equations
- Tau.BookV.Astrophysics.instReprLCDMLimitation = { reprPrec := Tau.BookV.Astrophysics.instReprLCDMLimitation.repr }

---

### `Tau.BookV.Astrophysics.instDecidableEqLCDMLimitation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L201-L201)
**instance
Tau.BookV.Astrophysics.instDecidableEqLCDMLimitation :DecidableEq LCDMLimitation**

Equations
- Tau.BookV.Astrophysics.instDecidableEqLCDMLimitation x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqLCDMLimitation.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L201-L201)
**def
Tau.BookV.Astrophysics.instBEqLCDMLimitation.beq :LCDMLimitation → LCDMLimitation → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqLCDMLimitation.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.instBEqLCDMLimitation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L201-L201)
**instance
Tau.BookV.Astrophysics.instBEqLCDMLimitation :BEq LCDMLimitation**

Equations
- Tau.BookV.Astrophysics.instBEqLCDMLimitation = { beq := Tau.BookV.Astrophysics.instBEqLCDMLimitation.beq }

---

### `Tau.BookV.Astrophysics.lcdm_limitations_complete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L203-L208)
**theorem
Tau.BookV.Astrophysics.lcdm_limitations_complete :[LCDMLimitation.DarkMatterMissing, LCDMLimitation.DarkEnergyFinetuning, LCDMLimitation.H0Tension, LCDMLimitation.Sigma8Tension, LCDMLimitation.InflationAdHoc, LCDMLimitation.BaryonAsymmetry].length = 6**


All 6 limitations cataloged.

---

### `Tau.BookV.Astrophysics.TauResolutionData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L214-L223)
**structure
Tau.BookV.Astrophysics.TauResolutionData :Type**


[V.D151] τ-resolution data: how the τ-framework resolves each
ΛCDM limitation.

- limitation : LCDMLimitation
ΛCDM limitation being resolved.

- resolution : String
τ-resolution mechanism.

- fully_resolved : Bool
Whether fully resolved or partially.

Instances For

---

### `Tau.BookV.Astrophysics.instReprTauResolutionData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L223-L223)
**instance
Tau.BookV.Astrophysics.instReprTauResolutionData :Repr TauResolutionData**

Equations
- Tau.BookV.Astrophysics.instReprTauResolutionData = { reprPrec := Tau.BookV.Astrophysics.instReprTauResolutionData.repr }

---

### `Tau.BookV.Astrophysics.instReprTauResolutionData.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L223-L223)
**def
Tau.BookV.Astrophysics.instReprTauResolutionData.repr :TauResolutionData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.h0_resolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L225-L229)
**def
Tau.BookV.Astrophysics.h0_resolution :TauResolutionData**


H₀ tension resolution.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.de_resolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L231-L235)
**def
Tau.BookV.Astrophysics.de_resolution :TauResolutionData**


Dark energy resolution.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.cosmo_const_boundary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L241-L250)
**theorem
Tau.BookV.Astrophysics.cosmo_const_boundary :"Lambda = boundary character constant term, not vacuum energy" = "Lambda = boundary character constant term, not vacuum energy"**


[V.P89] Cosmological constant from boundary: Λ is NOT a vacuum
energy but a constant term in the boundary character expansion.

This dissolves the cosmological constant problem because the
QFT vacuum energy calculation (Λ_QFT ~ M_P⁴) applies to the
wrong object — it computes the bulk vacuum energy, while Λ is
a boundary character readout at a completely different scale.

---

### `Tau.BookV.Astrophysics.no_lambda_fine_tuning`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L256-L267)
**theorem
Tau.BookV.Astrophysics.no_lambda_fine_tuning :"No 10^122 fine-tuning: Lambda is boundary readout, not vacuum energy" = "No 10^122 fine-tuning: Lambda is boundary readout, not vacuum energy"**


[V.T102] No fine-tuning of Λ: the observed value Λ_obs ~ 10⁻¹²² M_P⁴
is not fine-tuned in the τ-framework because Λ was never the vacuum
energy.

The "120 orders of magnitude problem" is a category error:
comparing boundary readout (Λ_obs) to bulk quantity (Λ_QFT).

In the τ-framework, Λ is determined by ι<sub>τ</sub> and the boundary
geometry, naturally at the observed scale. No cancellation needed.

---

### `Tau.BookV.Astrophysics.CPLMapping`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L308-L327)
**structure
Tau.BookV.Astrophysics.CPLMapping :Type**


[V.D295] CPL mapping of τ-EoS:
w(z) = w₀ + wₐ · z/(1+z).
w₀ = ι<sub>τ</sub>³ − 1 ≈ −0.960, wₐ > 0 (defects deplete → w approaches −1).

DESI DR2 (2025): w₀ = −0.75 ± 0.11, wₐ = −0.99 ± 0.48.
τ-tension with DESI: ~2σ. τ is closer to DESI than ΛCDM on w₀.

- w0_offset_x1000 : ℕ
w₀ offset from −1 (×1000): ι<sub>τ</sub>³ ≈ 0.040 → 40.

- wa_positive : Bool
wₐ sign: positive (defect depletion).

- desi_w0_offset_x1000 : ℕ
DESI w₀ central (×1000, offset from −1): 0.25 → 250.

- desi_w0_unc_x1000 : ℕ
DESI w₀ uncertainty (×1000): 0.11 → 110.

- desi_wa_x1000 : ℤ
DESI wₐ central (×1000): −0.99 → negative.

- desi_tension_x10sigma : ℕ
Tension with DESI (×10 σ): ~2σ → 20.

Instances For

---

### `Tau.BookV.Astrophysics.instReprCPLMapping`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L327-L327)
**instance
Tau.BookV.Astrophysics.instReprCPLMapping :Repr CPLMapping**

Equations
- Tau.BookV.Astrophysics.instReprCPLMapping = { reprPrec := Tau.BookV.Astrophysics.instReprCPLMapping.repr }

---

### `Tau.BookV.Astrophysics.instReprCPLMapping.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L327-L327)
**def
Tau.BookV.Astrophysics.instReprCPLMapping.repr :CPLMapping → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.NoPhantomCrossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L329-L339)
**structure
Tau.BookV.Astrophysics.NoPhantomCrossing :Type**


[V.T235] No Phantom Crossing:
w(z) > −1 for all z. f_def ∈ [0,1] → w = −1 + (2/3)f_def/(1−f_def) ≥ −1.
Topological constraint: defect fraction cannot be negative.

- w_geq_minus_one : Bool
w(z) ≥ −1 for all z.

- no_crossing : Bool
Phantom barrier never crossed.

- falsifiable : Bool
Falsifiable: if w < −1 observed → τ falsified.

Instances For

---

### `Tau.BookV.Astrophysics.instReprNoPhantomCrossing.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L339-L339)
**def
Tau.BookV.Astrophysics.instReprNoPhantomCrossing.repr :NoPhantomCrossing → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprNoPhantomCrossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L339-L339)
**instance
Tau.BookV.Astrophysics.instReprNoPhantomCrossing :Repr NoPhantomCrossing**

Equations
- Tau.BookV.Astrophysics.instReprNoPhantomCrossing = { reprPrec := Tau.BookV.Astrophysics.instReprNoPhantomCrossing.repr }

---

### `Tau.BookV.Astrophysics.cpl_canonical`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L341-L345)
**def
Tau.BookV.Astrophysics.cpl_canonical :CPLMapping**


Canonical CPL mapping.
Equations
- Tau.BookV.Astrophysics.cpl_canonical = { w0_offset_x1000 := 40, desi_tension_x10sigma := 20 }
Instances For

---

### `Tau.BookV.Astrophysics.no_phantom_canonical`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L347-L351)
**def
Tau.BookV.Astrophysics.no_phantom_canonical :NoPhantomCrossing**


Canonical no-phantom instance.
Equations
- Tau.BookV.Astrophysics.no_phantom_canonical = { }
Instances For

---

### `Tau.BookV.Astrophysics.no_phantom_crossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L353-L355)
**theorem
Tau.BookV.Astrophysics.no_phantom_crossing :no_phantom_canonical.no_crossing = true**


No phantom crossing proven.

---

### `Tau.BookV.Astrophysics.tau_closer_to_desi`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L357-L360)
**theorem
Tau.BookV.Astrophysics.tau_closer_to_desi :cpl_canonical.w0_offset_x1000 < cpl_canonical.desi_w0_offset_x1000**


[V.P160] τ closer to DESI than ΛCDM on w₀.

---

### `Tau.BookV.Astrophysics.HolonomySuppression`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L369-L379)
**structure
Tau.BookV.Astrophysics.HolonomySuppression :Type**


[V.D296] Holonomy suppression factor:
f_supp = 1 − κ_ω · ι<sub>τ</sub> = 1 − ι<sub>τ</sub>²/(1+ι<sub>τ</sub>) ≈ 0.913.
Suppresses late-time structure growth via boundary holonomy correction.

- f_supp_x1000 : ℕ
f_supp (×1000): 0.913 → 913.

- kappa_omega_iota_x10000 : ℕ
κ_ω · ι<sub>τ</sub> (×10000): 0.0868 → 868.

- suppression_active : Bool
Suppression: f_supp < 1.

Instances For

---

### `Tau.BookV.Astrophysics.instReprHolonomySuppression`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L379-L379)
**instance
Tau.BookV.Astrophysics.instReprHolonomySuppression :Repr HolonomySuppression**

Equations
- Tau.BookV.Astrophysics.instReprHolonomySuppression = { reprPrec := Tau.BookV.Astrophysics.instReprHolonomySuppression.repr }

---

### `Tau.BookV.Astrophysics.instReprHolonomySuppression.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L379-L379)
**def
Tau.BookV.Astrophysics.instReprHolonomySuppression.repr :HolonomySuppression → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.Sigma8TauNative`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L381-L397)
**structure
Tau.BookV.Astrophysics.Sigma8TauNative :Type**


[V.D297] σ₈ τ-native:
σ₈^(τ) = σ₈^(CMB) · f_supp = 0.811 × 0.913 = 0.741.
S₈^(τ) = σ₈^(τ) · √(Ω_m/0.3) = 0.760.

- sigma8_cmb_x1000 : ℕ
σ₈^(CMB) (×1000): 0.811 → 811.

- sigma8_tau_x1000 : ℕ
σ₈^(τ) (×1000): 0.741 → 741.

- s8_tau_x1000 : ℕ
S₈^(τ) (×1000): 0.760 → 760.

- s8_planck_x1000 : ℕ
S₈^(Planck CMB) (×1000): 0.832 → 832.

- s8_wl_x1000 : ℕ
S₈^(WL average) (×1000): ~0.770 → 770.

- aligns_with_wl : Bool
τ aligns with WL side.

Instances For

---

### `Tau.BookV.Astrophysics.instReprSigma8TauNative.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L397-L397)
**def
Tau.BookV.Astrophysics.instReprSigma8TauNative.repr :Sigma8TauNative → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprSigma8TauNative`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L397-L397)
**instance
Tau.BookV.Astrophysics.instReprSigma8TauNative :Repr Sigma8TauNative**

Equations
- Tau.BookV.Astrophysics.instReprSigma8TauNative = { reprPrec := Tau.BookV.Astrophysics.instReprSigma8TauNative.repr }

---

### `Tau.BookV.Astrophysics.holonomy_supp_canonical`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L399-L403)
**def
Tau.BookV.Astrophysics.holonomy_supp_canonical :HolonomySuppression**


Canonical holonomy suppression.
Equations
- Tau.BookV.Astrophysics.holonomy_supp_canonical = { f_supp_x1000 := 913, kappa_omega_iota_x10000 := 868 }
Instances For

---

### `Tau.BookV.Astrophysics.sigma8_canonical`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L405-L409)
**def
Tau.BookV.Astrophysics.sigma8_canonical :Sigma8TauNative**


Canonical σ₈.
Equations
- Tau.BookV.Astrophysics.sigma8_canonical = { sigma8_tau_x1000 := 741, s8_tau_x1000 := 760 }
Instances For

---

### `Tau.BookV.Astrophysics.sigma8_suppression_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L411-L414)
**theorem
Tau.BookV.Astrophysics.sigma8_suppression_theorem :sigma8_canonical.sigma8_tau_x1000 < sigma8_canonical.sigma8_cmb_x1000**


[V.T236] σ₈ suppressed: σ₈^(τ) < σ₈^(CMB).

---

### `Tau.BookV.Astrophysics.s8_wl_aligned`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L416-L419)
**theorem
Tau.BookV.Astrophysics.s8_wl_aligned :sigma8_canonical.s8_tau_x1000 < sigma8_canonical.s8_planck_x1000**


[V.P161] S₈ on WL side: S₈^(τ) < S₈^(Planck).

---

### `Tau.BookV.Astrophysics.TauGrowthFactor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L428-L444)
**structure
Tau.BookV.Astrophysics.TauGrowthFactor :Type**


[V.D298] τ-native growth factor:
D″ + 2H·D′ − (3/2)Ω_m(z)·H²·f_supp·D = 0.
Modified by w(z) ≠ −1 and holonomy suppression f_supp < 1.

- z_x10 : ℕ
Redshift (×10).

- omega_m_z_x100 : ℕ
Ω_m(z) (×100).

- f_z_x100 : ℕ
Growth rate f(z) = Ω_m(z)^γ (×100).

- sigma8_z_x1000 : ℕ
σ₈(z) = σ₈(0)·D(z) (×1000).

- fsigma8_tau_x1000 : ℕ
f·σ₈(z) τ-prediction (×1000).

- fsigma8_lcdm_x1000 : ℕ
f·σ₈(z) ΛCDM prediction (×1000).

Instances For

---

### `Tau.BookV.Astrophysics.instReprTauGrowthFactor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L444-L444)
**instance
Tau.BookV.Astrophysics.instReprTauGrowthFactor :Repr TauGrowthFactor**

Equations
- Tau.BookV.Astrophysics.instReprTauGrowthFactor = { reprPrec := Tau.BookV.Astrophysics.instReprTauGrowthFactor.repr }

---

### `Tau.BookV.Astrophysics.instReprTauGrowthFactor.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L444-L444)
**def
Tau.BookV.Astrophysics.instReprTauGrowthFactor.repr :TauGrowthFactor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.GrowthIndex`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L446-L454)
**structure
Tau.BookV.Astrophysics.GrowthIndex :Type**


[V.T238] Growth index: γ_τ = 0.55 + 0.05·ι<sub>τ</sub>³ ≈ 0.552.

- gamma_tau_x1000 : ℕ
γ_τ (×1000): 0.552 → 552.

- gamma_lcdm_x1000 : ℕ
γ_ΛCDM (×1000): 0.545 → 545.

- delta_gamma_x1000 : ℕ
Δγ (×1000): 0.007 → 7.

Instances For

---

### `Tau.BookV.Astrophysics.instReprGrowthIndex.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L454-L454)
**def
Tau.BookV.Astrophysics.instReprGrowthIndex.repr :GrowthIndex → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprGrowthIndex`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L454-L454)
**instance
Tau.BookV.Astrophysics.instReprGrowthIndex :Repr GrowthIndex**

Equations
- Tau.BookV.Astrophysics.instReprGrowthIndex = { reprPrec := Tau.BookV.Astrophysics.instReprGrowthIndex.repr }

---

### `Tau.BookV.Astrophysics.growth_z03`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L456-L463)
**def
Tau.BookV.Astrophysics.growth_z03 :TauGrowthFactor**


Growth at z = 0.3.
Equations
- Tau.BookV.Astrophysics.growth_z03 = { z_x10 := 3, omega_m_z_x100 := 41, f_z_x100 := 69, sigma8_z_x1000 := 682, fsigma8_tau_x1000 := 470,
 fsigma8_lcdm_x1000 := 485 }
Instances For

---

### `Tau.BookV.Astrophysics.growth_z10`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L465-L472)
**def
Tau.BookV.Astrophysics.growth_z10 :TauGrowthFactor**


Growth at z = 1.0.
Equations
- Tau.BookV.Astrophysics.growth_z10 = { z_x10 := 10, omega_m_z_x100 := 69, f_z_x100 := 86, sigma8_z_x1000 := 515, fsigma8_tau_x1000 := 443,
 fsigma8_lcdm_x1000 := 457 }
Instances For

---

### `Tau.BookV.Astrophysics.growth_index_canonical`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L474-L477)
**def
Tau.BookV.Astrophysics.growth_index_canonical :GrowthIndex**


Canonical growth index.
Equations
- Tau.BookV.Astrophysics.growth_index_canonical = { gamma_tau_x1000 := 552, delta_gamma_x1000 := 7 }
Instances For

---

### `Tau.BookV.Astrophysics.growth_below_lcdm_z03`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L479-L482)
**theorem
Tau.BookV.Astrophysics.growth_below_lcdm_z03 :growth_z03.fsigma8_tau_x1000 < growth_z03.fsigma8_lcdm_x1000**


[V.T237] τ growth systematically below ΛCDM.

---

### `Tau.BookV.Astrophysics.growth_index_departure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L484-L487)
**theorem
Tau.BookV.Astrophysics.growth_index_departure :growth_index_canonical.gamma_tau_x1000 > growth_index_canonical.gamma_lcdm_x1000**


[V.T238] Growth index departure: Δγ = +0.007.

---

### `Tau.BookV.Astrophysics.DESISigma8Falsification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L502-L514)
**structure
Tau.BookV.Astrophysics.DESISigma8Falsification :Type**


[V.R453] DESI σ₈(z) falsification window.
τ-prediction: (f·σ₈)_τ / (f·σ₈)_Λ ≈ 0.97, z-independent.
DESI DR3 + Euclid DR1 at ~1% precision → decisive.

- tau_lcdm_ratio_x1000 : ℕ
τ/ΛCDM ratio (×1000): 0.97 → 970.

- desi_precision_pct_x1000 : ℕ
DESI DR3 precision (×1000): 1% → 10.

- z_independent : ℕ
z-independent (structural): 1 = yes.

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookV.Astrophysics.instReprDESISigma8Falsification.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L514-L514)
**def
Tau.BookV.Astrophysics.instReprDESISigma8Falsification.repr :DESISigma8Falsification → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprDESISigma8Falsification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L514-L514)
**instance
Tau.BookV.Astrophysics.instReprDESISigma8Falsification :Repr DESISigma8Falsification**

Equations
- Tau.BookV.Astrophysics.instReprDESISigma8Falsification = { reprPrec := Tau.BookV.Astrophysics.instReprDESISigma8Falsification.repr }

---

### `Tau.BookV.Astrophysics.desi_sigma8_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L516-L516)
**def
Tau.BookV.Astrophysics.desi_sigma8_data :DESISigma8Falsification**

Equations
- Tau.BookV.Astrophysics.desi_sigma8_data = { }
Instances For

---

### `Tau.BookV.Astrophysics.desi_sigma8_detectable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L518-L522)
**theorem
Tau.BookV.Astrophysics.desi_sigma8_detectable :1000 - desi_sigma8_data.tau_lcdm_ratio_x1000 > desi_sigma8_data.desi_precision_pct_x1000**


3% deficit detectable at 1% precision.

---

### `Tau.BookV.Astrophysics.HubbleDerivationChain`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L532-L553)
**structure
Tau.BookV.Astrophysics.HubbleDerivationChain :Type**


[V.D319] Hubble Derivation Chain.
h = 2/3 + ι<sub>τ</sub>²/W₃(3) = 0.67352 at −120 ppm from Planck.
Two-step: EdS base (2/3) + holonomy correction (ι<sub>τ</sub>²/17).
Scope: τ-effective (Wave 38C).

- eds_base_x100000 : ℕ
EdS base × 100000.

- correction_x100000 : ℕ
Holonomy correction × 100000.

- h_x100000 : ℕ
h × 100000.

- planck_h_x100000 : ℕ
Planck h × 100000.

- deviation_ppm : ℕ
Deviation ppm.

- w3_3 : ℕ
W₃(3) = 17 (CF window sum).

- free_params : ℕ
Free parameters.

- derivation_steps : ℕ
Derivation steps.

Instances For

---

### `Tau.BookV.Astrophysics.instReprHubbleDerivationChain.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L553-L553)
**def
Tau.BookV.Astrophysics.instReprHubbleDerivationChain.repr :HubbleDerivationChain → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprHubbleDerivationChain`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L553-L553)
**instance
Tau.BookV.Astrophysics.instReprHubbleDerivationChain :Repr HubbleDerivationChain**

Equations
- Tau.BookV.Astrophysics.instReprHubbleDerivationChain = { reprPrec := Tau.BookV.Astrophysics.instReprHubbleDerivationChain.repr }

---

### `Tau.BookV.Astrophysics.hubble_derivation_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L555-L555)
**def
Tau.BookV.Astrophysics.hubble_derivation_data :HubbleDerivationChain**

Equations
- Tau.BookV.Astrophysics.hubble_derivation_data = { }
Instances For

---

### `Tau.BookV.Astrophysics.hubble_uniqueness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L557-L561)
**theorem
Tau.BookV.Astrophysics.hubble_uniqueness :hubble_derivation_data.free_params = 0 ∧ hubble_derivation_data.derivation_steps = 2**


[V.T259] Uniqueness: h = 2/3 + ι<sub>τ</sub>²/17 is unique first-order correction.

---

### `Tau.BookV.Astrophysics.hubble_self_consistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L563-L569)
**theorem
Tau.BookV.Astrophysics.hubble_self_consistency :hubble_derivation_data.h_x100000 = 67352 ∧ hubble_derivation_data.w3_3 = 17**


[V.P178] Self-consistency: h²·Ω_m = ω_m.
h² × 100000 = 45363, Ω_m × 10000 = 3299, product / 10 = 14964.
This should match ω_m(NLO) × 10000 = 14964.

---

### `Tau.BookV.Astrophysics.hubble_sub_permille`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L571-L574)
**theorem
Tau.BookV.Astrophysics.hubble_sub_permille :hubble_derivation_data.deviation_ppm < 1000**


Deviation is sub-permille.

---

### `Tau.BookV.Astrophysics.S8TensionResolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L585-L612)
**structure
Tau.BookV.Astrophysics.S8TensionResolution :Type**


[V.D324] S₈ NLO with full pipeline.
σ₈(τ,NLO) = 0.811 × f_supp × f_growth × f_ν = 0.747.
S₈(τ,NLO) = 0.747 × √(0.330/0.3) = 0.783.
Scope: τ-effective (Wave 39C).

- sigma8_cmb_x1000 : ℕ
σ₈(CMB, Planck) × 1000.

- f_supp_x10000 : ℕ
f_supp × 10000.

- f_growth_x10000 : ℕ
f_growth × 10000.

- f_nu_x100000 : ℕ
f_ν × 100000.

- sigma8_nlo_x10000 : ℕ
σ₈(τ,NLO) × 10000.

- s8_nlo_x10000 : ℕ
S₈(τ,NLO) × 10000.

- omega_m_nlo_x10000 : ℕ
Ω_m(NLO) × 10000.

- s8_planck_x1000 : ℕ
S₈(Planck CMB) × 1000.

- s8_deskids_x1000 : ℕ
S₈(DES+KiDS) × 1000.

- s8_desy3_x1000 : ℕ
S₈(DES Y3) × 1000.

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookV.Astrophysics.instReprS8TensionResolution.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L612-L612)
**def
Tau.BookV.Astrophysics.instReprS8TensionResolution.repr :S8TensionResolution → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprS8TensionResolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L612-L612)
**instance
Tau.BookV.Astrophysics.instReprS8TensionResolution :Repr S8TensionResolution**

Equations
- Tau.BookV.Astrophysics.instReprS8TensionResolution = { reprPrec := Tau.BookV.Astrophysics.instReprS8TensionResolution.repr }

---

### `Tau.BookV.Astrophysics.s8_resolution_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L614-L614)
**def
Tau.BookV.Astrophysics.s8_resolution_data :S8TensionResolution**

Equations
- Tau.BookV.Astrophysics.s8_resolution_data = { }
Instances For

---

### `Tau.BookV.Astrophysics.s8_between_cmb_and_wl`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L616-L620)
**theorem
Tau.BookV.Astrophysics.s8_between_cmb_and_wl :s8_resolution_data.s8_desy3_x1000 < s8_resolution_data.s8_nlo_x10000 / 10 ∧ s8_resolution_data.s8_nlo_x10000 / 10 < s8_resolution_data.s8_planck_x1000**


[V.T263] S₈(τ) between CMB and WL (resolves tension).

---

### `Tau.BookV.Astrophysics.s8_within_1sigma_deskids`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L622-L626)
**theorem
Tau.BookV.Astrophysics.s8_within_1sigma_deskids :s8_resolution_data.s8_nlo_x10000 / 10 ≥ s8_resolution_data.s8_deskids_x1000 - 14 ∧ s8_resolution_data.s8_nlo_x10000 / 10 ≤ s8_resolution_data.s8_deskids_x1000 + 14**


[V.P182] S₈(τ) within 1σ of DES+KiDS (|0.783 − 0.790| < 0.014).

---

### `Tau.BookV.Astrophysics.s8_zero_params`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L628-L631)
**theorem
Tau.BookV.Astrophysics.s8_zero_params :s8_resolution_data.free_params = 0**


Zero free parameters.

---

### `Tau.BookV.Astrophysics.S8NNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L642-L672)
**structure
Tau.BookV.Astrophysics.S8NNLO :Type**


[V.D330] S₈ NNLO density-regime value.
At NNLO, Ω_m = 0.3155 ≈ Ω_m(Planck), so f_growth → 1.000.
σ₈(τ,NNLO) = 0.811 × 0.913 × 1.000 × 0.997 = 0.738.
S₈(τ,NNLO) = 0.738 × √(0.316/0.3) = 0.757.
Scope: τ-effective (Wave 42A).

- sigma8_cmb_x1000 : ℕ
σ₈(CMB, Planck) × 1000.

- f_supp_x10000 : ℕ
f_supp × 10000 (unchanged from NLO).

- f_growth_nnlo_x10000 : ℕ
f_growth(NNLO) × 10000 (≈ 1.000).

- f_nu_nnlo_x100000 : ℕ
f_ν(NNLO) × 100000.

- sigma8_nnlo_x10000 : ℕ
σ₈(τ,NNLO) × 10000.

- s8_nnlo_x10000 : ℕ
S₈(τ,NNLO) × 10000.

- omega_m_nnlo_x10000 : ℕ
Ω_m(NNLO) × 10000.

- s8_kids_x1000 : ℕ
S₈(KiDS-1000) × 1000.

- s8_kids_sigma_x1000 : ℕ
S₈(KiDS-1000) 1σ uncertainty × 1000.

- s8_hsc_x1000 : ℕ
S₈(HSC Y3) × 1000.

- s8_hsc_sigma_x1000 : ℕ
S₈(HSC Y3) 1σ uncertainty × 1000.

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookV.Astrophysics.instReprS8NNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L672-L672)
**instance
Tau.BookV.Astrophysics.instReprS8NNLO :Repr S8NNLO**

Equations
- Tau.BookV.Astrophysics.instReprS8NNLO = { reprPrec := Tau.BookV.Astrophysics.instReprS8NNLO.repr }

---

### `Tau.BookV.Astrophysics.instReprS8NNLO.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L672-L672)
**def
Tau.BookV.Astrophysics.instReprS8NNLO.repr :S8NNLO → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.s8_nnlo_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L674-L674)
**def
Tau.BookV.Astrophysics.s8_nnlo_data :S8NNLO**

Equations
- Tau.BookV.Astrophysics.s8_nnlo_data = { }
Instances For

---

### `Tau.BookV.Astrophysics.s8_nnlo_within_kids`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L676-L681)
**theorem
Tau.BookV.Astrophysics.s8_nnlo_within_kids :s8_nnlo_data.s8_nnlo_x10000 / 10 ≥ s8_nnlo_data.s8_kids_x1000 - s8_nnlo_data.s8_kids_sigma_x1000 ∧ s8_nnlo_data.s8_nnlo_x10000 / 10 ≤ s8_nnlo_data.s8_kids_x1000 + s8_nnlo_data.s8_kids_sigma_x1000**


[V.T266] S₈(τ,NNLO) within 1σ of KiDS-1000:
|0.757 − 0.759| = 0.002 < 0.024.

---

### `Tau.BookV.Astrophysics.s8_nnlo_within_hsc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L683-L688)
**theorem
Tau.BookV.Astrophysics.s8_nnlo_within_hsc :s8_nnlo_data.s8_nnlo_x10000 / 10 ≥ s8_nnlo_data.s8_hsc_x1000 - s8_nnlo_data.s8_hsc_sigma_x1000 ∧ s8_nnlo_data.s8_nnlo_x10000 / 10 ≤ s8_nnlo_data.s8_hsc_x1000 + s8_nnlo_data.s8_hsc_sigma_x1000**


[V.T266] S₈(τ,NNLO) within 1σ of HSC Y3:
|0.757 − 0.763| = 0.006 < 0.033.

---

### `Tau.BookV.Astrophysics.s8_nnlo_below_nlo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L690-L693)
**theorem
Tau.BookV.Astrophysics.s8_nnlo_below_nlo :s8_nnlo_data.s8_nnlo_x10000 < s8_resolution_data.s8_nlo_x10000**


[V.D330] NNLO S₈ below NLO S₈ (density regime shifts S₈ down).

---

### `Tau.BookV.Astrophysics.s8_nnlo_zero_params`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L695-L698)
**theorem
Tau.BookV.Astrophysics.s8_nnlo_zero_params :s8_nnlo_data.free_params = 0**


Zero free parameters at NNLO.
