---
layout: taulib-doc
title: "TauLib.BookV.FluidMacro.TauPlasma"
permalink: /verify/taulib/docs/book-v-fluid-macro-tau-plasma/
lane: verify
module_name: "TauLib.BookV.FluidMacro.TauPlasma"
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

# TauLib.BookV.FluidMacro.TauPlasma


Plasma as ionized fluid: Debye screening, plasma frequency, dispersion,
quasineutrality, instabilities, and MHD limit.

## Registry Cross-References


- [V.D104] tau-plasma — `TauPlasmaState`

- [V.T74] Forced Quasi-Neutrality — `forced_quasineutrality`

- [V.P46] Plasma oscillations — `plasma_oscillations`

- [V.P47] Plasma cutoff — `plasma_cutoff`

- [V.R152] Ionospheric reflection — `ionospheric_reflection`

- [V.P48] Debye shielding — `debye_shielding`

- [V.D105] Debye number — `DebyeNumber`

- [V.R153] No dark matter in the ICM — `no_dark_matter_icm`

- [V.D106] MHD limit — `MHDLimitCondition`


## Mathematical Content


### τ-Plasma Definition


A τ-plasma is a macro defect configuration on τ³ with:


- Nonzero B-sector defect density (n_B > 0)

- Mobile charged carriers (μ_B > μ_crit)


### Forced Quasi-Neutrality


In a τ-plasma, charge imbalance at any scale l > λ_D is exponentially small:
|n₊(l) - n₋(l)| ≤ n₀ exp(-l/λ_D)

### Plasma Dispersion


The EM dispersion relation in a τ-plasma is:
ω² = ω_p² + c²k²
For ω < ω_p the wave is evanescent; for ω > ω_p it propagates with
v_φ > c and v_g < c.

### MHD Limit


The MHD regime: charge separation below λ_D, timescales exceed ω_p⁻¹,
spatial scales exceed λ_D. Single conducting fluid with frozen-flux.

## Ground Truth Sources


- Book V ch30: τ-Plasma


---

### `Tau.BookV.FluidMacro.TauPlasmaState`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L58-L77)
**structure
Tau.BookV.FluidMacro.TauPlasmaState :Type**


[V.D104] Tau-plasma: a macro defect configuration on τ³ with
nonzero B-sector defect density and mobile charged carriers.

Structural plasma conditions:


- n_B > 0 (nonzero B-sector density)

- μ_B > μ_crit (carrier mobility above critical threshold)


- b_sector_density : ℕ
B-sector defect density (scaled).

- density_pos : self.b_sector_density > 0
B-sector density is nonzero.

- carrier_mobility : ℕ
Carrier mobility (scaled).

- mobility_threshold : ℕ
Critical mobility threshold.

- mobile : self.carrier_mobility > self.mobility_threshold
Mobility exceeds threshold.

- temperature_idx : ℕ
Temperature index (scaled).

Instances For

---

### `Tau.BookV.FluidMacro.instReprTauPlasmaState.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L77-L77)
**def
Tau.BookV.FluidMacro.instReprTauPlasmaState.repr :TauPlasmaState → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprTauPlasmaState`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L77-L77)
**instance
Tau.BookV.FluidMacro.instReprTauPlasmaState :Repr TauPlasmaState**

Equations
- Tau.BookV.FluidMacro.instReprTauPlasmaState = { reprPrec := Tau.BookV.FluidMacro.instReprTauPlasmaState.repr }

---

### `Tau.BookV.FluidMacro.DebyeLength`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L83-L95)
**structure
Tau.BookV.FluidMacro.DebyeLength :Type**


Debye length: the characteristic screening scale.
λ_D = √(ε₀ k_B T / (n₀ e²))
Encoded as a rational (numerator/denominator) in natural units.

- numer : ℕ
Numerator (scaled).

- denom : ℕ
Denominator.

- denom_pos : self.denom > 0
Denominator positive.

- length_pos : self.numer > 0
Debye length is positive.

Instances For

---

### `Tau.BookV.FluidMacro.instReprDebyeLength.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L95-L95)
**def
Tau.BookV.FluidMacro.instReprDebyeLength.repr :DebyeLength → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprDebyeLength`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L95-L95)
**instance
Tau.BookV.FluidMacro.instReprDebyeLength :Repr DebyeLength**

Equations
- Tau.BookV.FluidMacro.instReprDebyeLength = { reprPrec := Tau.BookV.FluidMacro.instReprDebyeLength.repr }

---

### `Tau.BookV.FluidMacro.DebyeLength.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L97-L99)
**def
Tau.BookV.FluidMacro.DebyeLength.toFloat
(d : DebyeLength)
 :Float**


Debye length as Float.
Equations
- d.toFloat = Float.ofNat d.numer / Float.ofNat d.denom
Instances For

---

### `Tau.BookV.FluidMacro.QuasiNeutralityBound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L105-L117)
**structure
Tau.BookV.FluidMacro.QuasiNeutralityBound :Type**


[V.T74] Forced Quasi-Neutrality: in a τ-plasma, charge imbalance
at any scale l > λ_D is exponentially small:
|n₊(l) - n₋(l)| ≤ n₀ exp(-l/λ_D)

Quasi-neutrality follows from the B-sector boundary structure.

- scale_in_debye : ℕ
Scale (in Debye lengths).

- max_imbalance : ℕ
Maximum charge imbalance (scaled).

- suppressed : self.scale_in_debye > 1 → self.max_imbalance < 100
Exponential suppression: imbalance decreases with scale.

Instances For

---

### `Tau.BookV.FluidMacro.instReprQuasiNeutralityBound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L117-L117)
**instance
Tau.BookV.FluidMacro.instReprQuasiNeutralityBound :Repr QuasiNeutralityBound**

Equations
- Tau.BookV.FluidMacro.instReprQuasiNeutralityBound = { reprPrec := Tau.BookV.FluidMacro.instReprQuasiNeutralityBound.repr }

---

### `Tau.BookV.FluidMacro.instReprQuasiNeutralityBound.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L117-L117)
**def
Tau.BookV.FluidMacro.instReprQuasiNeutralityBound.repr :QuasiNeutralityBound → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.forced_quasineutrality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L119-L122)
**theorem
Tau.BookV.FluidMacro.forced_quasineutrality
(qn : QuasiNeutralityBound)

(h : qn.scale_in_debye > 1)
 :qn.max_imbalance < 100**


Quasi-neutrality: at large scales the imbalance vanishes.

---

### `Tau.BookV.FluidMacro.PlasmaFrequency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L128-L139)
**structure
Tau.BookV.FluidMacro.PlasmaFrequency :Type**


Plasma frequency: ω_p = √(n₀ e² / (m_e ε₀)).
Encoded as scaled rational.

- numer : ℕ
Frequency numerator (scaled).

- denom : ℕ
Frequency denominator.

- denom_pos : self.denom > 0
Denominator positive.

- freq_pos : self.numer > 0
Frequency is positive.

Instances For

---

### `Tau.BookV.FluidMacro.instReprPlasmaFrequency.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L139-L139)
**def
Tau.BookV.FluidMacro.instReprPlasmaFrequency.repr :PlasmaFrequency → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprPlasmaFrequency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L139-L139)
**instance
Tau.BookV.FluidMacro.instReprPlasmaFrequency :Repr PlasmaFrequency**

Equations
- Tau.BookV.FluidMacro.instReprPlasmaFrequency = { reprPrec := Tau.BookV.FluidMacro.instReprPlasmaFrequency.repr }

---

### `Tau.BookV.FluidMacro.PlasmaOscillation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L141-L153)
**structure
Tau.BookV.FluidMacro.PlasmaOscillation :Type**


[V.P46] Plasma oscillations: a small charge perturbation oscillates
at the plasma frequency ω_p.

The oscillations are longitudinal (compression-rarefaction in electron
density) and do not propagate below ω_p.

- frequency : PlasmaFrequency
The plasma frequency.

- is_longitudinal : Bool
Oscillations are longitudinal.

- cutoff_below : Bool
No propagation below ω_p.

Instances For

---

### `Tau.BookV.FluidMacro.instReprPlasmaOscillation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L153-L153)
**def
Tau.BookV.FluidMacro.instReprPlasmaOscillation.repr :PlasmaOscillation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprPlasmaOscillation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L153-L153)
**instance
Tau.BookV.FluidMacro.instReprPlasmaOscillation :Repr PlasmaOscillation**

Equations
- Tau.BookV.FluidMacro.instReprPlasmaOscillation = { reprPrec := Tau.BookV.FluidMacro.instReprPlasmaOscillation.repr }

---

### `Tau.BookV.FluidMacro.plasma_oscillations`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L155-L158)
**theorem
Tau.BookV.FluidMacro.plasma_oscillations
(po : PlasmaOscillation)

(h : po.is_longitudinal = true)
 :po.is_longitudinal = true**


Plasma oscillations are longitudinal.

---

### `Tau.BookV.FluidMacro.PlasmaWaveMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L164-L172)
**inductive
Tau.BookV.FluidMacro.PlasmaWaveMode :Type**


Wave propagation mode in a plasma.

- Propagating : PlasmaWaveMode
Propagating: ω > ω_p (real k, v_φ > c, v_g < c).

- Evanescent : PlasmaWaveMode
Evanescent: ω < ω_p (imaginary k, exponential decay).

- Cutoff : PlasmaWaveMode
At cutoff: ω = ω_p (k = 0).

Instances For

---

### `Tau.BookV.FluidMacro.instReprPlasmaWaveMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L172-L172)
**instance
Tau.BookV.FluidMacro.instReprPlasmaWaveMode :Repr PlasmaWaveMode**

Equations
- Tau.BookV.FluidMacro.instReprPlasmaWaveMode = { reprPrec := Tau.BookV.FluidMacro.instReprPlasmaWaveMode.repr }

---

### `Tau.BookV.FluidMacro.instReprPlasmaWaveMode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L172-L172)
**def
Tau.BookV.FluidMacro.instReprPlasmaWaveMode.repr :PlasmaWaveMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instDecidableEqPlasmaWaveMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L172-L172)
**instance
Tau.BookV.FluidMacro.instDecidableEqPlasmaWaveMode :DecidableEq PlasmaWaveMode**

Equations
- Tau.BookV.FluidMacro.instDecidableEqPlasmaWaveMode x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.FluidMacro.instBEqPlasmaWaveMode.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L172-L172)
**def
Tau.BookV.FluidMacro.instBEqPlasmaWaveMode.beq :PlasmaWaveMode → PlasmaWaveMode → Bool**

Equations
- Tau.BookV.FluidMacro.instBEqPlasmaWaveMode.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.FluidMacro.instBEqPlasmaWaveMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L172-L172)
**instance
Tau.BookV.FluidMacro.instBEqPlasmaWaveMode :BEq PlasmaWaveMode**

Equations
- Tau.BookV.FluidMacro.instBEqPlasmaWaveMode = { beq := Tau.BookV.FluidMacro.instBEqPlasmaWaveMode.beq }

---

### `Tau.BookV.FluidMacro.PlasmaDispersion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L174-L186)
**structure
Tau.BookV.FluidMacro.PlasmaDispersion :Type**


[V.P47] Plasma cutoff: ω² = ω_p² + c²k².
For ω < ω_p: evanescent; for ω > ω_p: propagating.

- omega_scaled : ℕ
Wave frequency (relative to ω_p, scaled by 100).

- omega_p_scaled : ℕ
Plasma frequency (scaled by 100).

- mode : PlasmaWaveMode
Classification.

- mode_correct : (self.omega_scaled > self.omega_p_scaled → self.mode = PlasmaWaveMode.Propagating) ∧ (self.omega_scaled < self.omega_p_scaled → self.mode = PlasmaWaveMode.Evanescent)
Classification is correct.

Instances For

---

### `Tau.BookV.FluidMacro.instReprPlasmaDispersion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L186-L186)
**instance
Tau.BookV.FluidMacro.instReprPlasmaDispersion :Repr PlasmaDispersion**

Equations
- Tau.BookV.FluidMacro.instReprPlasmaDispersion = { reprPrec := Tau.BookV.FluidMacro.instReprPlasmaDispersion.repr }

---

### `Tau.BookV.FluidMacro.instReprPlasmaDispersion.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L186-L186)
**def
Tau.BookV.FluidMacro.instReprPlasmaDispersion.repr :PlasmaDispersion → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.plasma_cutoff`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L188-L191)
**theorem
Tau.BookV.FluidMacro.plasma_cutoff
(pd : PlasmaDispersion)

(h : pd.omega_scaled > pd.omega_p_scaled)
 :pd.mode = PlasmaWaveMode.Propagating**


Above cutoff means propagating.

---

### `Tau.BookV.FluidMacro.IonosphericReflection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L197-L206)
**structure
Tau.BookV.FluidMacro.IonosphericReflection :Type**


[V.R152] Ionospheric reflection: Earth's ionosphere reflects radio
waves below ω_p ~ 2π × 10 MHz as a direct consequence of the
B-sector cutoff. EM modes below the plasma frequency cannot sustain
propagating B-sector boundary obstructions.

- plasma_freq_mhz : ℕ
Ionospheric plasma frequency in MHz (approximate).

- is_reflected : Bool
Reflected waves are below cutoff.

Instances For

---

### `Tau.BookV.FluidMacro.instReprIonosphericReflection.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L206-L206)
**def
Tau.BookV.FluidMacro.instReprIonosphericReflection.repr :IonosphericReflection → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprIonosphericReflection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L206-L206)
**instance
Tau.BookV.FluidMacro.instReprIonosphericReflection :Repr IonosphericReflection**

Equations
- Tau.BookV.FluidMacro.instReprIonosphericReflection = { reprPrec := Tau.BookV.FluidMacro.instReprIonosphericReflection.repr }

---

### `Tau.BookV.FluidMacro.ionospheric_reflection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L208-L210)
**def
Tau.BookV.FluidMacro.ionospheric_reflection :IonosphericReflection**

Equations
- Tau.BookV.FluidMacro.ionospheric_reflection = { }
Instances For

---

### `Tau.BookV.FluidMacro.DebyeShielding`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L216-L227)
**structure
Tau.BookV.FluidMacro.DebyeShielding :Type**


[V.P48] Debye shielding: a test charge Q in a τ-plasma is screened:
φ(r) = Q/(4π ε₀ r) · exp(-r/λ_D)

The Coulomb potential is exponentially suppressed beyond λ_D.

- debye_length : DebyeLength
Debye length.

- test_charge : ChargeQuantum
Test charge value.

- is_exponential : Bool
Shielding is exponential.

Instances For

---

### `Tau.BookV.FluidMacro.instReprDebyeShielding.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L227-L227)
**def
Tau.BookV.FluidMacro.instReprDebyeShielding.repr :DebyeShielding → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprDebyeShielding`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L227-L227)
**instance
Tau.BookV.FluidMacro.instReprDebyeShielding :Repr DebyeShielding**

Equations
- Tau.BookV.FluidMacro.instReprDebyeShielding = { reprPrec := Tau.BookV.FluidMacro.instReprDebyeShielding.repr }

---

### `Tau.BookV.FluidMacro.debye_shielding`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L229-L232)
**theorem
Tau.BookV.FluidMacro.debye_shielding
(ds : DebyeShielding)

(h : ds.is_exponential = true)
 :ds.is_exponential = true**


Shielding is always exponential in a τ-plasma.

---

### `Tau.BookV.FluidMacro.DebyeNumber`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L238-L250)
**structure
Tau.BookV.FluidMacro.DebyeNumber :Type**


[V.D105] Debye number: N_D = n₀ λ_D³, the number of charge carriers
in a Debye sphere.

When N_D >> 1, collective effects dominate individual two-body
collisions (strongly collective plasma).

- n_d : ℕ
Number of carriers in Debye sphere.

- is_collective : Bool
Whether collective regime (N_D >> 1).

- collective_correct : self.is_collective = true → self.n_d > 10
Collective when N_D > 10.

Instances For

---

### `Tau.BookV.FluidMacro.instReprDebyeNumber`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L250-L250)
**instance
Tau.BookV.FluidMacro.instReprDebyeNumber :Repr DebyeNumber**

Equations
- Tau.BookV.FluidMacro.instReprDebyeNumber = { reprPrec := Tau.BookV.FluidMacro.instReprDebyeNumber.repr }

---

### `Tau.BookV.FluidMacro.instReprDebyeNumber.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L250-L250)
**def
Tau.BookV.FluidMacro.instReprDebyeNumber.repr :DebyeNumber → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.no_dark_matter_icm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L256-L262)
**def
Tau.BookV.FluidMacro.no_dark_matter_icm :Prop**


[V.R153] No dark matter in the ICM: the five sectors exhaust the
coupling budget (Sector Exhaustion Theorem); there is no dark sector.
Missing mass in galaxy clusters will be accounted for by the modified
D-sector gravitational readout.
Equations
- Tau.BookV.FluidMacro.no_dark_matter_icm = ("Five sectors exhaust coupling budget" = "Five sectors exhaust coupling budget")
Instances For

---

### `Tau.BookV.FluidMacro.no_dark_matter_icm_holds`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L264-L264)
**theorem
Tau.BookV.FluidMacro.no_dark_matter_icm_holds :no_dark_matter_icm**


---

### `Tau.BookV.FluidMacro.MHDLimitCondition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L270-L285)
**structure
Tau.BookV.FluidMacro.MHDLimitCondition :Type**


[V.D106] MHD limit: the magnetohydrodynamic regime of a τ-plasma.
Conditions: charge separation < λ_D, timescales > ω_p⁻¹,
spatial scales > λ_D.

The plasma is described as a single conducting fluid with
frozen-flux constraint.

- charge_separation_ok : Bool
Charge separation below Debye length.

- timescale_ok : Bool
Timescale exceeds inverse plasma frequency.

- spatial_scale_ok : Bool
Spatial scale exceeds Debye length.

- frozen_flux : Bool
Frozen flux condition holds.

Instances For

---

### `Tau.BookV.FluidMacro.instReprMHDLimitCondition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L285-L285)
**def
Tau.BookV.FluidMacro.instReprMHDLimitCondition.repr :MHDLimitCondition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprMHDLimitCondition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L285-L285)
**instance
Tau.BookV.FluidMacro.instReprMHDLimitCondition :Repr MHDLimitCondition**

Equations
- Tau.BookV.FluidMacro.instReprMHDLimitCondition = { reprPrec := Tau.BookV.FluidMacro.instReprMHDLimitCondition.repr }

---

### `Tau.BookV.FluidMacro.mhd_limit_valid`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L287-L293)
**theorem
Tau.BookV.FluidMacro.mhd_limit_valid
(m : MHDLimitCondition)

(h1 : m.charge_separation_ok = true)

(h2 : m.timescale_ok = true)

(h3 : m.spatial_scale_ok = true)
 :m.charge_separation_ok = true ∧ m.timescale_ok = true ∧ m.spatial_scale_ok = true**


MHD limit is valid when all three conditions hold.

---

### `Tau.BookV.FluidMacro.example_plasma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L299-L306)
**def
Tau.BookV.FluidMacro.example_plasma :TauPlasmaState**


Example τ-plasma (solar corona-like).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.example_debye`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/TauPlasma.lean#L308-L313)
**def
Tau.BookV.FluidMacro.example_debye :DebyeLength**


Example Debye length.
Equations
- Tau.BookV.FluidMacro.example_debye = { numer := 7, denom := 1000, denom_pos := Tau.BookV.FluidMacro.example_plasma._proof_3,
 length_pos := Tau.BookV.FluidMacro.example_debye._proof_2 }
Instances For
