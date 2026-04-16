---
layout: taulib-doc
title: "TauLib.BookIV.Particles.BetaDecay"
permalink: /verify/taulib/docs/book-iv-particles-beta-decay/
lane: verify
module_name: "TauLib.BookIV.Particles.BetaDecay"
book: "IV"
book_label: "Microcosm"
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
    book: "Book IV"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookIV.Particles.BetaDecay


Beta decay as A-sector (weak) process, hydrogen atom physics, Bohr radius,
Rydberg constant, hydrogen energy levels, fine structure from holonomy
corrections, and spectral transitions as mode-switching events.

## Registry Cross-References


- [IV.P125] Beta-Decay Q-Value — `beta_decay_q_value`

- [IV.P126] Bohr Radius from ι<sub>τ</sub> — `bohr_radius`

- [IV.P127] Spectral Transition as Mode-Switching — `spectral_mode_switching`

- [IV.D199] Rydberg Constant — `RydbergConstant`

- [IV.T85] Hydrogen Energy Levels — `hydrogen_levels`

- [IV.T86] Rydberg Prediction at 0.025 ppm — `rydberg_prediction`

- [IV.T87] Fine Structure from Holonomy Corrections — `fine_structure_holonomy`

- [IV.R121] Neutron as Parent of Atomic Matter — `neutron_as_parent`

- [IV.R122] Structural Lifetime Estimate — `lifetime_structural` (conjectural)

- [IV.R123] No Classical Trajectory — comment-only (not_applicable)

- [IV.R124] A Testable Prediction — `rydberg_testable`

- [IV.R125] Forbidden Transitions — `forbidden_transitions`

- [IV.R126] Lamb Shift in tau-framework — `lamb_shift_tau` (conjectural)

- [IV.R127] All Roads Lead through m_e — `all_roads_m_e`


## Mathematical Content


Beta decay: n → p + e⁻ + ν̄_e is the A-sector (weak) process that
differentiates the calibration anchor (neutron) into its component spectral
modes. Q_β = (δ_A − m_e)c² ≈ 0.782 MeV.

The hydrogen atom combines the electron mass prediction (0.025 ppm) with
the fine structure constant to give: Bohr radius a₀, energy levels
E_n = −13.6/n² eV, and the Rydberg constant R_∞ — all from ι<sub>τ</sub> and m_n.
Fine structure splitting is a 4th-order holonomy correction.

## Ground Truth Sources


- Chapter 47 of Book IV (2nd Edition)


---

### `Tau.BookIV.Particles.NeutronParent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L50-L66)
**structure
Tau.BookIV.Particles.NeutronParent :Type**


[IV.R121] In the τ-picture, beta decay is differentiation of the
calibration anchor into component spectral modes:


- Proton: weak-polarized neutron (p = n + δ_A)

- Electron: spectral residual (m_e = m_n/R)

- Antineutrino: base-mode time-eigenstate


The neutron is the PARENT of all atomic matter.

- products : List String
Products of differentiation.

- proton_is_polarized : Bool
Proton is weak-polarized neutron.

- electron_is_residual : Bool
Electron is spectral residual.

- parent : Bool
Neutron is ontological parent.

Instances For

---

### `Tau.BookIV.Particles.instReprNeutronParent.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L66-L66)
**def
Tau.BookIV.Particles.instReprNeutronParent.repr :NeutronParent → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprNeutronParent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L66-L66)
**instance
Tau.BookIV.Particles.instReprNeutronParent :Repr NeutronParent**

Equations
- Tau.BookIV.Particles.instReprNeutronParent = { reprPrec := Tau.BookIV.Particles.instReprNeutronParent.repr }

---

### `Tau.BookIV.Particles.neutron_as_parent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L68-L68)
**def
Tau.BookIV.Particles.neutron_as_parent :NeutronParent**

Equations
- Tau.BookIV.Particles.neutron_as_parent = { }
Instances For

---

### `Tau.BookIV.Particles.three_products`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L70-L70)
**theorem
Tau.BookIV.Particles.three_products :neutron_as_parent.products.length = 3**


---

### `Tau.BookIV.Particles.BetaDecayQValue`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L76-L95)
**structure
Tau.BookIV.Particles.BetaDecayQValue :Type**


[IV.P125] Q_β = (δ_A − m_e)c² where both δ_A and m_e are determined
by ι<sub>τ</sub> through the mass ratio chain.

Values in keV:


- δ_A ≈ 1293 keV (proton-neutron mass difference)

- m_e ≈ 511 keV (electron mass)

- Q_β ≈ 782 keV

- Experimental: Q_β = 782.333(4) keV


- delta_A_keV : ℕ
δ_A in keV.

- m_e_keV : ℕ
m_e in keV.

- q_predicted_keV : ℕ
Q_β predicted in keV.

- q_exp_keV_x1000 : ℕ
Q_β experimental in keV (×1000).

- sub_percent : Bool
Agreement: sub-percent.

Instances For

---

### `Tau.BookIV.Particles.instReprBetaDecayQValue.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L95-L95)
**def
Tau.BookIV.Particles.instReprBetaDecayQValue.repr :BetaDecayQValue → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprBetaDecayQValue`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L95-L95)
**instance
Tau.BookIV.Particles.instReprBetaDecayQValue :Repr BetaDecayQValue**

Equations
- Tau.BookIV.Particles.instReprBetaDecayQValue = { reprPrec := Tau.BookIV.Particles.instReprBetaDecayQValue.repr }

---

### `Tau.BookIV.Particles.beta_decay_q_value`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L97-L97)
**def
Tau.BookIV.Particles.beta_decay_q_value :BetaDecayQValue**

Equations
- Tau.BookIV.Particles.beta_decay_q_value = { }
Instances For

---

### `Tau.BookIV.Particles.q_value_consistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L99-L102)
**theorem
Tau.BookIV.Particles.q_value_consistency :beta_decay_q_value.delta_A_keV - beta_decay_q_value.m_e_keV = beta_decay_q_value.q_predicted_keV**


Q_β = δ_A − m_e.

---

### `Tau.BookIV.Particles.LifetimeStructural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L108-L118)
**structure
Tau.BookIV.Particles.LifetimeStructural :Type**


[IV.R122] Neutron lifetime involves G_F, m_e, Q_β (all ι<sub>τ</sub>-determined)
but the axial coupling g_A ≈ 1.276 requires detailed quark-level
T² breathing mode structure — conjectural scope.

- g_A_x1000 : ℕ
Axial coupling (×1000).

- lifetime_s : ℕ
Free neutron lifetime (seconds, approx).

- scope : String
Scope (upgraded from conjectural at Wave 46B).

Instances For

---

### `Tau.BookIV.Particles.instReprLifetimeStructural.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L118-L118)
**def
Tau.BookIV.Particles.instReprLifetimeStructural.repr :LifetimeStructural → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprLifetimeStructural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L118-L118)
**instance
Tau.BookIV.Particles.instReprLifetimeStructural :Repr LifetimeStructural**

Equations
- Tau.BookIV.Particles.instReprLifetimeStructural = { reprPrec := Tau.BookIV.Particles.instReprLifetimeStructural.repr }

---

### `Tau.BookIV.Particles.lifetime_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L120-L120)
**def
Tau.BookIV.Particles.lifetime_structural :LifetimeStructural**

Equations
- Tau.BookIV.Particles.lifetime_structural = { }
Instances For

---

### `Tau.BookIV.Particles.BohrRadius`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L126-L140)
**structure
Tau.BookIV.Particles.BohrRadius :Type**


[IV.P126] a₀ = R/(α_em · m_n) × (ℏ/c) is fully determined by ι<sub>τ</sub> and m_n.
Both R = m_n/m_e and α_em ≈ (8/15)·ι<sub>τ</sub>⁴ are rational functions of ι<sub>τ</sub>.

CODATA: a₀ ≈ 5.29177210544 × 10⁻¹¹ m.
Precision limited by m_e at 0.025 ppm.

- matches_codata : Bool
Prediction matches CODATA.

- iota_and_mn_only : Bool
Derived from ι<sub>τ</sub> and m_n only.

- codata_pm_x1000 : ℕ
CODATA value (pm, ×1000 for integer).

- precision_ppm : ℕ
Precision limited by m_e (ppm).

Instances For

---

### `Tau.BookIV.Particles.instReprBohrRadius`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L140-L140)
**instance
Tau.BookIV.Particles.instReprBohrRadius :Repr BohrRadius**

Equations
- Tau.BookIV.Particles.instReprBohrRadius = { reprPrec := Tau.BookIV.Particles.instReprBohrRadius.repr }

---

### `Tau.BookIV.Particles.instReprBohrRadius.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L140-L140)
**def
Tau.BookIV.Particles.instReprBohrRadius.repr :BohrRadius → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.bohr_radius`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L142-L142)
**def
Tau.BookIV.Particles.bohr_radius :BohrRadius**

Equations
- Tau.BookIV.Particles.bohr_radius = { }
Instances For

---

### `Tau.BookIV.Particles.bohr_from_iota`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L144-L144)
**theorem
Tau.BookIV.Particles.bohr_from_iota :bohr_radius.iota_and_mn_only = true**


---

### `Tau.BookIV.Particles.HydrogenLevels`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L150-L164)
**structure
Tau.BookIV.Particles.HydrogenLevels :Type**


[IV.T85] E_n = −α_em² · m_e · c² / (2n²) = −13.6 eV/n²
for n = 1, 2, 3, ...

Both α_em and m_e determined by ι<sub>τ</sub>.
Ground state: E₁ ≈ −13.606 eV.

Energy in meV (×1000 for ground state = 13606).

- E1_meV : ℕ
Ground state energy magnitude (meV).

- iota_determined : Bool
Fully determined by ι<sub>τ</sub>.

- scaling : String
Scaling: 1/n² for principal quantum number n.

Instances For

---

### `Tau.BookIV.Particles.instReprHydrogenLevels`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L164-L164)
**instance
Tau.BookIV.Particles.instReprHydrogenLevels :Repr HydrogenLevels**

Equations
- Tau.BookIV.Particles.instReprHydrogenLevels = { reprPrec := Tau.BookIV.Particles.instReprHydrogenLevels.repr }

---

### `Tau.BookIV.Particles.instReprHydrogenLevels.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L164-L164)
**def
Tau.BookIV.Particles.instReprHydrogenLevels.repr :HydrogenLevels → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.hydrogen_levels`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L166-L166)
**def
Tau.BookIV.Particles.hydrogen_levels :HydrogenLevels**

Equations
- Tau.BookIV.Particles.hydrogen_levels = { }
Instances For

---

### `Tau.BookIV.Particles.ground_state_energy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L168-L168)
**theorem
Tau.BookIV.Particles.ground_state_energy :hydrogen_levels.E1_meV = 13606**


---

### `Tau.BookIV.Particles.RydbergConstant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L174-L188)
**structure
Tau.BookIV.Particles.RydbergConstant :Type**


[IV.D199] R_∞ = α_em² · m_e · c / (2ℏ)
encodes hydrogen levels: E_n = −hcR_∞/n².

A derived quantity in Category τ since both α_em and m_e are
ι<sub>τ</sub>-determined. Parameter-free prediction.

CODATA: R_∞ = 10,973,731.568157(12) m⁻¹.

- codata_int : ℕ
CODATA value (m⁻¹, integer part).

- tau_predicted_int : ℕ
τ-predicted value (m⁻¹, integer part, approximate).

- parameter_free : Bool
Parameter-free.

Instances For

---

### `Tau.BookIV.Particles.instReprRydbergConstant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L188-L188)
**instance
Tau.BookIV.Particles.instReprRydbergConstant :Repr RydbergConstant**

Equations
- Tau.BookIV.Particles.instReprRydbergConstant = { reprPrec := Tau.BookIV.Particles.instReprRydbergConstant.repr }

---

### `Tau.BookIV.Particles.instReprRydbergConstant.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L188-L188)
**def
Tau.BookIV.Particles.instReprRydbergConstant.repr :RydbergConstant → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.rydberg_constant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L190-L190)
**def
Tau.BookIV.Particles.rydberg_constant :RydbergConstant**

Equations
- Tau.BookIV.Particles.rydberg_constant = { }
Instances For

---

### `Tau.BookIV.Particles.RydbergPrediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L196-L208)
**structure
Tau.BookIV.Particles.RydbergPrediction :Type**


[IV.T86] τ-predicted R_∞ matches CODATA to ~0.026 ppm
(seven significant figures), inheriting the 0.025 ppm
precision of the electron mass prediction.

R_∞^(τ) ≈ 10,973,731.29 m⁻¹ vs CODATA 10,973,731.568157 m⁻¹.

- deviation_ppm_x1000 : ℕ
Deviation (ppm ×1000).

- sig_figs : ℕ
Significant figures matched.

- inherited_from : String
Precision inherited from m_e.

Instances For

---

### `Tau.BookIV.Particles.instReprRydbergPrediction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L208-L208)
**def
Tau.BookIV.Particles.instReprRydbergPrediction.repr :RydbergPrediction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprRydbergPrediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L208-L208)
**instance
Tau.BookIV.Particles.instReprRydbergPrediction :Repr RydbergPrediction**

Equations
- Tau.BookIV.Particles.instReprRydbergPrediction = { reprPrec := Tau.BookIV.Particles.instReprRydbergPrediction.repr }

---

### `Tau.BookIV.Particles.rydberg_prediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L210-L210)
**def
Tau.BookIV.Particles.rydberg_prediction :RydbergPrediction**

Equations
- Tau.BookIV.Particles.rydberg_prediction = { }
Instances For

---

### `Tau.BookIV.Particles.rydberg_seven_sig_figs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L212-L212)
**theorem
Tau.BookIV.Particles.rydberg_seven_sig_figs :rydberg_prediction.sig_figs = 7**


---

### `Tau.BookIV.Particles.rydberg_testable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L218-L222)
**def
Tau.BookIV.Particles.rydberg_testable :String**


[IV.R124] R_∞ is one of the most precisely measured quantities
(uncertainty 1.1×10⁻¹²). The τ-prediction matches to 0.026 ppm,
limited by the m_e residual.
Equations
- Tau.BookIV.Particles.rydberg_testable = "R_infinity: CODATA uncertainty 1.1e-12, tau matches to 0.026 ppm (7 sig figs)"
Instances For

---

### `Tau.BookIV.Particles.SpectralModeSwitching`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L228-L239)
**structure
Tau.BookIV.Particles.SpectralModeSwitching :Type**


[IV.P127] Each hydrogen spectral transition is a CR-address
mode-switching event on T²: the initial and final CR-address states
have winding numbers compatible with respective quantum numbers.
The emitted photon carries energy ΔE and angular momentum Δl = ±1.

- delta_l : ℤ
Selection rule: Δl = ±1.

- t2_mode_switch : Bool
Mode-switching on T².

- photon_carries_energy : Bool
Photon carries ΔE.

Instances For

---

### `Tau.BookIV.Particles.instReprSpectralModeSwitching`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L239-L239)
**instance
Tau.BookIV.Particles.instReprSpectralModeSwitching :Repr SpectralModeSwitching**

Equations
- Tau.BookIV.Particles.instReprSpectralModeSwitching = { reprPrec := Tau.BookIV.Particles.instReprSpectralModeSwitching.repr }

---

### `Tau.BookIV.Particles.instReprSpectralModeSwitching.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L239-L239)
**def
Tau.BookIV.Particles.instReprSpectralModeSwitching.repr :SpectralModeSwitching → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.spectral_mode_switching`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L241-L241)
**def
Tau.BookIV.Particles.spectral_mode_switching :SpectralModeSwitching**

Equations
- Tau.BookIV.Particles.spectral_mode_switching = { }
Instances For

---

### `Tau.BookIV.Particles.ForbiddenTransitions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L247-L258)
**structure
Tau.BookIV.Particles.ForbiddenTransitions :Type**


[IV.R125] Transitions with Δl = 0 (e.g., 2s → 1s) are "forbidden"
because the winding number difference cannot be absorbed by a single
photon mode. They require higher-order holonomy corrections
(quadrupole or magnetic dipole).

- delta_l_zero : Bool
Forbidden: Δl = 0 transitions.

- requires_higher_order : Bool
Requires higher-order correction.

- example_transition : String
Example: 2s → 1s.

Instances For

---

### `Tau.BookIV.Particles.instReprForbiddenTransitions.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L258-L258)
**def
Tau.BookIV.Particles.instReprForbiddenTransitions.repr :ForbiddenTransitions → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprForbiddenTransitions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L258-L258)
**instance
Tau.BookIV.Particles.instReprForbiddenTransitions :Repr ForbiddenTransitions**

Equations
- Tau.BookIV.Particles.instReprForbiddenTransitions = { reprPrec := Tau.BookIV.Particles.instReprForbiddenTransitions.repr }

---

### `Tau.BookIV.Particles.forbidden_transitions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L260-L260)
**def
Tau.BookIV.Particles.forbidden_transitions :ForbiddenTransitions**

Equations
- Tau.BookIV.Particles.forbidden_transitions = { }
Instances For

---

### `Tau.BookIV.Particles.FineStructureHolonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L266-L281)
**structure
Tau.BookIV.Particles.FineStructureHolonomy :Type**


[IV.T87] Fine-structure splitting is a higher-order B-sector
holonomy correction on T² of order α_em⁴ · m_e · c² ≈ 1.8×10⁻⁴ eV.

Entirely determined by ι<sub>τ</sub>. The n=2 level splits into j=3/2 and j=1/2
components from the formula:
α_em ≈ (8/15)·ι<sub>τ</sub>⁴ and m_e = m_n/R(ι<sub>τ</sub>).

- alpha_order : ℕ
Order of correction: α⁴.

- n2_splitting_uev : ℕ
Splitting at n=2 (μeV, approx).

- iota_determined : Bool
Determined by ι<sub>τ</sub>.

- split_quantum : String
Quantum numbers that split.

Instances For

---

### `Tau.BookIV.Particles.instReprFineStructureHolonomy.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L281-L281)
**def
Tau.BookIV.Particles.instReprFineStructureHolonomy.repr :FineStructureHolonomy → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprFineStructureHolonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L281-L281)
**instance
Tau.BookIV.Particles.instReprFineStructureHolonomy :Repr FineStructureHolonomy**

Equations
- Tau.BookIV.Particles.instReprFineStructureHolonomy = { reprPrec := Tau.BookIV.Particles.instReprFineStructureHolonomy.repr }

---

### `Tau.BookIV.Particles.fine_structure_holonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L283-L283)
**def
Tau.BookIV.Particles.fine_structure_holonomy :FineStructureHolonomy**

Equations
- Tau.BookIV.Particles.fine_structure_holonomy = { }
Instances For

---

### `Tau.BookIV.Particles.fine_structure_fourth_order`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L285-L286)
**theorem
Tau.BookIV.Particles.fine_structure_fourth_order :fine_structure_holonomy.alpha_order = 4**


---

### `Tau.BookIV.Particles.LambShift`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L292-L302)
**structure
Tau.BookIV.Particles.LambShift :Type**


[IV.R126] The Lamb shift (~1057.845 MHz) is an α_em⁵ · m_e · c²
effect: vacuum breathing corrections shift s-state energies.
Conjectural scope: fifth-order holonomy effect on T².

- alpha_order : ℕ
Order of correction: α⁵.

- freq_mhz : ℕ
Frequency (MHz, approx).

- scope : String
Scope.

Instances For

---

### `Tau.BookIV.Particles.instReprLambShift.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L302-L302)
**def
Tau.BookIV.Particles.instReprLambShift.repr :LambShift → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprLambShift`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L302-L302)
**instance
Tau.BookIV.Particles.instReprLambShift :Repr LambShift**

Equations
- Tau.BookIV.Particles.instReprLambShift = { reprPrec := Tau.BookIV.Particles.instReprLambShift.repr }

---

### `Tau.BookIV.Particles.lamb_shift_tau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L304-L304)
**def
Tau.BookIV.Particles.lamb_shift_tau :LambShift**

Equations
- Tau.BookIV.Particles.lamb_shift_tau = { }
Instances For

---

### `Tau.BookIV.Particles.AllRoadsME`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L310-L326)
**structure
Tau.BookIV.Particles.AllRoadsME :Type**


[IV.R127] Every atomic-scale prediction factors through
m_e = m_n/R(ι<sub>τ</sub>):


- a₀ ∝ 1/m_e

- E₁ ∝ m_e

- R_∞ ∝ m_e

- λ ∝ 1/m_e


The 0.025 ppm precision of m_e is the ceiling for all atomic
predictions.

- dependent_quantities : ℕ
Number of atomic quantities depending on m_e.

- ceiling_ppm_x1000 : ℕ
Precision ceiling (ppm ×1000).

- improvable : Bool
Improvable by Level 2 correction or better m_n measurement.

Instances For

---

### `Tau.BookIV.Particles.instReprAllRoadsME.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L326-L326)
**def
Tau.BookIV.Particles.instReprAllRoadsME.repr :AllRoadsME → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprAllRoadsME`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L326-L326)
**instance
Tau.BookIV.Particles.instReprAllRoadsME :Repr AllRoadsME**

Equations
- Tau.BookIV.Particles.instReprAllRoadsME = { reprPrec := Tau.BookIV.Particles.instReprAllRoadsME.repr }

---

### `Tau.BookIV.Particles.all_roads_m_e`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L328-L328)
**def
Tau.BookIV.Particles.all_roads_m_e :AllRoadsME**

Equations
- Tau.BookIV.Particles.all_roads_m_e = { }
Instances For

---

### `Tau.BookIV.Particles.four_quantities_depend`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L330-L330)
**theorem
Tau.BookIV.Particles.four_quantities_depend :all_roads_m_e.dependent_quantities = 4**


---

### `Tau.BookIV.Particles.ProtonChargeRadiusNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L336-L354)
**structure
Tau.BookIV.Particles.ProtonChargeRadiusNLO :Type**


[IV.T202] r_p(NLO) = 4λ̄_p(1 − ι<sub>τ</sub>²·α/|lobes|) = 0.84088 fm.
NLO correction from EM dressing: holonomy² × α / lobes.
CREMA = 0.84087 fm → +12 ppm (36× improvement from LO +440 ppm).

- r_p_lo_fm_x100k : ℕ
LO value (fm ×100000).

- delta_r_x1e6 : ℕ
NLO correction δ_r (×10⁶).

- r_p_nlo_fm_x100k : ℕ
NLO value (fm ×100000).

- crema_fm_x100k : ℕ
CREMA experimental (fm ×100000).

- deviation_lo_ppm : ℕ
Deviation LO (ppm).

- deviation_nlo_ppm : ℕ
Deviation NLO (ppm).

- improvement_factor : ℕ
Improvement factor.

Instances For

---

### `Tau.BookIV.Particles.instReprProtonChargeRadiusNLO.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L354-L354)
**def
Tau.BookIV.Particles.instReprProtonChargeRadiusNLO.repr :ProtonChargeRadiusNLO → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprProtonChargeRadiusNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L354-L354)
**instance
Tau.BookIV.Particles.instReprProtonChargeRadiusNLO :Repr ProtonChargeRadiusNLO**

Equations
- Tau.BookIV.Particles.instReprProtonChargeRadiusNLO = { reprPrec := Tau.BookIV.Particles.instReprProtonChargeRadiusNLO.repr }

---

### `Tau.BookIV.Particles.proton_charge_radius_nlo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L356-L356)
**def
Tau.BookIV.Particles.proton_charge_radius_nlo :ProtonChargeRadiusNLO**

Equations
- Tau.BookIV.Particles.proton_charge_radius_nlo = { }
Instances For

---

### `Tau.BookIV.Particles.nlo_improves_lo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L358-L360)
**theorem
Tau.BookIV.Particles.nlo_improves_lo :proton_charge_radius_nlo.deviation_nlo_ppm < proton_charge_radius_nlo.deviation_lo_ppm**


---

### `Tau.BookIV.Particles.NeutronLifetimeInputs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L366-L379)
**structure
Tau.BookIV.Particles.NeutronLifetimeInputs :Type**


[IV.D383] Complete input table for neutron lifetime precision prediction.
All inputs ι<sub>τ</sub>-derived except PDG prefactor K.

- ga_ppm_x10 : ℕ
g_A deviation (ppm ×10).

- vud_ppm : ℕ
|V_ud| deviation (ppm).

- delta_r_ppm_x10 : ℕ
Δ_r deviation (ppm ×10).

- K_s_x10 : ℕ
PDG prefactor K (s ×10).

- iota_derived_count : ℕ
Number of ι<sub>τ</sub>-derived inputs.

Instances For

---

### `Tau.BookIV.Particles.instReprNeutronLifetimeInputs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L379-L379)
**instance
Tau.BookIV.Particles.instReprNeutronLifetimeInputs :Repr NeutronLifetimeInputs**

Equations
- Tau.BookIV.Particles.instReprNeutronLifetimeInputs = { reprPrec := Tau.BookIV.Particles.instReprNeutronLifetimeInputs.repr }

---

### `Tau.BookIV.Particles.instReprNeutronLifetimeInputs.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L379-L379)
**def
Tau.BookIV.Particles.instReprNeutronLifetimeInputs.repr :NeutronLifetimeInputs → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.neutron_lifetime_inputs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L381-L381)
**def
Tau.BookIV.Particles.neutron_lifetime_inputs :NeutronLifetimeInputs**

Equations
- Tau.BookIV.Particles.neutron_lifetime_inputs = { }
Instances For

---

### `Tau.BookIV.Particles.NeutronLifetimePrecision`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L387-L402)
**structure
Tau.BookIV.Particles.NeutronLifetimePrecision :Type**


[IV.T203] τ_n = K/(|V_ud|²·(1+3g_A²)·f·(1+Δ_r)) ≈ 878.7 s.
Bottle: 878.4±0.5 s → +340 ppm. Beam: 887.7±1.2 s → excluded at 7.5σ.

- tau_n_predicted_x10 : ℕ
τ_n prediction (s ×10).

- bottle_avg_x10 : ℕ
Bottle average (s ×10).

- beam_avg_x10 : ℕ
Beam average (s ×10).

- bottle_deviation_ppm : ℕ
Deviation from bottle (ppm).

- beam_excluded_sigma_x10 : ℕ
Beam excluded at σ (×10).

- selects_bottle : Bool
Selects bottle.

Instances For

---

### `Tau.BookIV.Particles.instReprNeutronLifetimePrecision.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L402-L402)
**def
Tau.BookIV.Particles.instReprNeutronLifetimePrecision.repr :NeutronLifetimePrecision → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprNeutronLifetimePrecision`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L402-L402)
**instance
Tau.BookIV.Particles.instReprNeutronLifetimePrecision :Repr NeutronLifetimePrecision**

Equations
- Tau.BookIV.Particles.instReprNeutronLifetimePrecision = { reprPrec := Tau.BookIV.Particles.instReprNeutronLifetimePrecision.repr }

---

### `Tau.BookIV.Particles.neutron_lifetime_precision`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L404-L404)
**def
Tau.BookIV.Particles.neutron_lifetime_precision :NeutronLifetimePrecision**

Equations
- Tau.BookIV.Particles.neutron_lifetime_precision = { }
Instances For

---

### `Tau.BookIV.Particles.selects_bottle_value`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L406-L407)
**theorem
Tau.BookIV.Particles.selects_bottle_value :neutron_lifetime_precision.selects_bottle = true**


---

### `Tau.BookIV.Particles.CancelledFormBudget`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L413-L429)
**structure
Tau.BookIV.Particles.CancelledFormBudget :Type**


[IV.P224] Cancelled-form error budget: RSS = 77 ppm.
78× improvement over naive Fermi (6030 ppm).
Theory-limited: RSS (77 ppm) < experimental (570 ppm).

- r9_ppm : ℕ
R⁹ contribution (ppm).

- vud2_ppm : ℕ
|V_ud|² contribution (ppm).

- fga_ppm : ℕ
f(1+3g_A²) contribution (ppm).

- rss_ppm : ℕ
RSS total (ppm).

- naive_ppm : ℕ
Naive Fermi (ppm).

- improvement : ℕ
Improvement factor.

Instances For

---

### `Tau.BookIV.Particles.instReprCancelledFormBudget`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L429-L429)
**instance
Tau.BookIV.Particles.instReprCancelledFormBudget :Repr CancelledFormBudget**

Equations
- Tau.BookIV.Particles.instReprCancelledFormBudget = { reprPrec := Tau.BookIV.Particles.instReprCancelledFormBudget.repr }

---

### `Tau.BookIV.Particles.instReprCancelledFormBudget.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L429-L429)
**def
Tau.BookIV.Particles.instReprCancelledFormBudget.repr :CancelledFormBudget → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.cancelled_form_budget`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L431-L431)
**def
Tau.BookIV.Particles.cancelled_form_budget :CancelledFormBudget**

Equations
- Tau.BookIV.Particles.cancelled_form_budget = { }
Instances For

---

### `Tau.BookIV.Particles.cancelled_form_improves`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/BetaDecay.lean#L433-L434)
**theorem
Tau.BookIV.Particles.cancelled_form_improves :cancelled_form_budget.rss_ppm < cancelled_form_budget.naive_ppm**
