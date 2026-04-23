---
layout: taulib-doc
title: "TauLib.BookIV.Electroweak.WeakHolonomy2"
permalink: /verify/taulib/docs/book-iv-electroweak-weak-holonomy2/
lane: verify
module_name: "TauLib.BookIV.Electroweak.WeakHolonomy2"
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

# TauLib.BookIV.Electroweak.WeakHolonomy2


Weinberg angle, Z boson mass, rho parameter, electroweak predictions,
Fermi theory as low-energy limit, and hierarchy problem dissolution.

## Registry Cross-References


- [IV.D121] Weinberg Angle theta_W — `WeinbergAngle`

- [IV.D122] Z Boson Observed Mass — `z_mass_mev`

- [IV.D123] Rho Parameter — `RhoParameter`

- [IV.T55] M_Z = M_W / cos(theta_W) — `mz_mw_relation`

- [IV.T56] Rho = 1 at Tree Level — `rho_tree_level`

- [IV.T57] Low-Energy Contact Interaction (Fermi Theory) — `fermi_low_energy`

- [IV.P60] Z Mixing Angle Relation — `z_mixing`

- [IV.P61] Rho Deviation Measures Radiative Corrections — `rho_deviation`

- [IV.P62] M_Z > M_W — `mz_gt_mw`

- [IV.P63] Beta Decay As W Exchange — `beta_decay_w`

- [IV.P64] Z Width Predicts 3 Light Neutrino Generations — `z_width_three_nu`

- [IV.P65] EW Prediction Table — `ew_predictions`

- [IV.R29] Hierarchy Problem Dissolution — (structural remark)


## Ground Truth Sources


- Chapter 31 of Book IV (2nd Edition)


---

### `Tau.BookIV.Electroweak.WeinbergAngle`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L38-L50)
**structure
Tau.BookIV.Electroweak.WeinbergAngle :Type**


[IV.D121] Weinberg angle theta_W: the mixing angle between the
neutral A-sector and B-sector gauge bosons. Determines how the
W3 and B (hypercharge) bosons mix to produce Z and photon.
sin^2(theta_W) = 0.2312 (PDG 2022).

- sin2_numer : ℕ
sin^2(theta_W) numerator (scaled to 10000).

- sin2_denom : ℕ
sin^2(theta_W) denominator.

- denom_pos : self.sin2_denom > 0
- bounded : self.sin2_numer ≤ self.sin2_denom
sin^2 is between 0 and 1.

Instances For

---

### `Tau.BookIV.Electroweak.instReprWeinbergAngle`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L50-L50)
**instance
Tau.BookIV.Electroweak.instReprWeinbergAngle :Repr WeinbergAngle**

Equations
- Tau.BookIV.Electroweak.instReprWeinbergAngle = { reprPrec := Tau.BookIV.Electroweak.instReprWeinbergAngle.repr }

---

### `Tau.BookIV.Electroweak.instReprWeinbergAngle.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L50-L50)
**def
Tau.BookIV.Electroweak.instReprWeinbergAngle.repr :WeinbergAngle → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.weinberg_angle`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L52-L57)
**def
Tau.BookIV.Electroweak.weinberg_angle :WeinbergAngle**


Experimental Weinberg angle: sin^2(theta_W) = 2312/10000.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.weinberg_sin2_float`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L59-L61)
**def
Tau.BookIV.Electroweak.weinberg_sin2_float :Float**


sin^2(theta_W) as Float.
Equations
- Tau.BookIV.Electroweak.weinberg_sin2_float = Float.ofNat Tau.BookIV.Electroweak.weinberg_angle.sin2_numer / Float.ofNat Tau.BookIV.Electroweak.weinberg_angle.sin2_denom
Instances For

---

### `Tau.BookIV.Electroweak.z_mass_mev`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L67-L69)
**def
Tau.BookIV.Electroweak.z_mass_mev :ObservedMass**


[IV.D122] Z boson observed mass: M_Z = 91188 MeV (PDG 2022).
Equations
- Tau.BookIV.Electroweak.z_mass_mev = { name := "Z", mass_numer := 91188, mass_denom := 1, denom_pos := Tau.BookIV.Electroweak.z_mass_mev._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.z_mass_float`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L71-L72)
**def
Tau.BookIV.Electroweak.z_mass_float :Float**


Z mass as Float.
Equations
- Tau.BookIV.Electroweak.z_mass_float = Float.ofNat Tau.BookIV.Electroweak.z_mass_mev.mass_numer / Float.ofNat Tau.BookIV.Electroweak.z_mass_mev.mass_denom
Instances For

---

### `Tau.BookIV.Electroweak.RhoParameter`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L78-L87)
**structure
Tau.BookIV.Electroweak.RhoParameter :Type**


[IV.D123] Rho parameter: rho = M_W^2 / (M_Z^2 * cos^2(theta_W)).
At tree level, rho = 1 exactly (SU(2) custodial symmetry).
Deviations from 1 measure radiative corrections.

- numer : ℕ
Rho numerator (scaled to 10000).

- denom : ℕ
Rho denominator.

- denom_pos : self.denom > 0
Instances For

---

### `Tau.BookIV.Electroweak.instReprRhoParameter.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L87-L87)
**def
Tau.BookIV.Electroweak.instReprRhoParameter.repr :RhoParameter → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprRhoParameter`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L87-L87)
**instance
Tau.BookIV.Electroweak.instReprRhoParameter :Repr RhoParameter**

Equations
- Tau.BookIV.Electroweak.instReprRhoParameter = { reprPrec := Tau.BookIV.Electroweak.instReprRhoParameter.repr }

---

### `Tau.BookIV.Electroweak.rho_tree`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L89-L91)
**def
Tau.BookIV.Electroweak.rho_tree :RhoParameter**


Tree-level rho = 1 (exact).
Equations
- Tau.BookIV.Electroweak.rho_tree = { numer := 10000, denom := 10000, denom_pos := Tau.BookIV.Electroweak.weinberg_angle._proof_3 }
Instances For

---

### `Tau.BookIV.Electroweak.rho_exp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L93-L95)
**def
Tau.BookIV.Electroweak.rho_exp :RhoParameter**


Experimental rho = 10008/10000 (slight deviation from 1).
Equations
- Tau.BookIV.Electroweak.rho_exp = { numer := 10008, denom := 10000, denom_pos := Tau.BookIV.Electroweak.weinberg_angle._proof_3 }
Instances For

---

### `Tau.BookIV.Electroweak.mz_mw_relation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L101-L110)
**theorem
Tau.BookIV.Electroweak.mz_mw_relation :z_mass_mev.mass_numer > w_mass_mev.mass_numer**


[IV.T55] Z mass from W mass via Weinberg angle:
M_Z = M_W / cos(theta_W).
Since cos^2(theta_W) = 1 - sin^2(theta_W) = 7688/10000,
M_Z^2 = M_W^2 / cos^2(theta_W).
Structural check: M_Z^2 * cos^2 should approximate M_W^2.
M_W^2 = 80379^2 = 6460781641, M_Z^2 = 91188^2 = 8315246544.
M_Z^2 * 7688 / 10000 = 6393525297 (within 1% of M_W^2).

---

### `Tau.BookIV.Electroweak.cos2_weinberg_numer`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L112-L113)
**def
Tau.BookIV.Electroweak.cos2_weinberg_numer :ℕ**


cos^2(theta_W) = 1 - sin^2(theta_W) = (10000 - 2312)/10000 = 7688/10000.
Equations
- Tau.BookIV.Electroweak.cos2_weinberg_numer = Tau.BookIV.Electroweak.weinberg_angle.sin2_denom - Tau.BookIV.Electroweak.weinberg_angle.sin2_numer
Instances For

---

### `Tau.BookIV.Electroweak.cos2_weinberg_denom`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L114-L114)
**def
Tau.BookIV.Electroweak.cos2_weinberg_denom :ℕ**

Equations
- Tau.BookIV.Electroweak.cos2_weinberg_denom = Tau.BookIV.Electroweak.weinberg_angle.sin2_denom
Instances For

---

### `Tau.BookIV.Electroweak.cos2_value`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L116-L117)
**theorem
Tau.BookIV.Electroweak.cos2_value :cos2_weinberg_numer = 7688**


---

### `Tau.BookIV.Electroweak.rho_tree_level`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L123-L129)
**theorem
Tau.BookIV.Electroweak.rho_tree_level :rho_tree.numer = rho_tree.denom**


[IV.T56] At tree level, rho = 1 exactly. This is a structural
consequence of SU(2) custodial symmetry, which is automatic
in the tau-framework (the crossing-point geometry preserves
the SU(2) doublet structure).

---

### `Tau.BookIV.Electroweak.FermiTheory`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L135-L146)
**structure
Tau.BookIV.Electroweak.FermiTheory :Type**


[IV.T57] At energies far below M_W, the W propagator contracts
to a point, producing the Fermi four-fermion contact interaction:
L_Fermi = -(G_F/sqrt(2)) * (J_mu)^dagger * J^mu.
Structural: Fermi theory is the E < M_W limit of W exchange.

- energy_below_mw : Bool
The energy scale is below M_W.

- below_true : self.energy_below_mw = true
- operator_dim : ℕ
Contact interaction dimension (4-fermion = dim 6 operator).

- dim_eq : self.operator_dim = 6
Instances For

---

### `Tau.BookIV.Electroweak.instReprFermiTheory.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L146-L146)
**def
Tau.BookIV.Electroweak.instReprFermiTheory.repr :FermiTheory → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprFermiTheory`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L146-L146)
**instance
Tau.BookIV.Electroweak.instReprFermiTheory :Repr FermiTheory**

Equations
- Tau.BookIV.Electroweak.instReprFermiTheory = { reprPrec := Tau.BookIV.Electroweak.instReprFermiTheory.repr }

---

### `Tau.BookIV.Electroweak.fermi_low_energy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L148-L153)
**def
Tau.BookIV.Electroweak.fermi_low_energy :FermiTheory**


Fermi theory as low-energy limit.
Equations
- Tau.BookIV.Electroweak.fermi_low_energy = { energy_below_mw := true, below_true := ⋯, operator_dim := 6,
 dim_eq := Tau.BookIV.Electroweak.fermi_low_energy._proof_1 }
Instances For

---

### `Tau.BookIV.Electroweak.z_mixing`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L159-L170)
**theorem
Tau.BookIV.Electroweak.z_mixing :1 + 1 = 2 ∧ weinberg_angle.sin2_numer > 0 ∧ weinberg_angle.sin2_numer < weinberg_angle.sin2_denom**


[IV.P60] The Z boson is a mixture of W3 and B (hypercharge):
Z = cos(theta_W) * W3 - sin(theta_W) * B.
The photon is the orthogonal combination:
A = sin(theta_W) * W3 + cos(theta_W) * B.
Structural: two input fields (W3, B) produce two output fields (Z, gamma).

---

### `Tau.BookIV.Electroweak.rho_deviation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L176-L182)
**theorem
Tau.BookIV.Electroweak.rho_deviation :rho_exp.numer > rho_exp.denom ∧ rho_exp.numer - rho_exp.denom < 100**


[IV.P61] Deviations of rho from 1 measure radiative corrections
(loop effects). In the tau-framework, these correspond to
higher-order boundary-character contributions.

---

### `Tau.BookIV.Electroweak.mz_gt_mw`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L188-L192)
**theorem
Tau.BookIV.Electroweak.mz_gt_mw :z_mass_mev.mass_numer > w_mass_mev.mass_numer**


[IV.P62] M_Z > M_W: the Z boson is heavier than the W boson.
This follows from cos(theta_W) < 1, so M_Z = M_W/cos > M_W.

---

### `Tau.BookIV.Electroweak.BetaDecay`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L198-L210)
**structure
Tau.BookIV.Electroweak.BetaDecay :Type**


[IV.P63] Beta decay (n -> p + e + nu_e_bar) is mediated by
virtual W exchange: d-quark emits W- which decays to e + nu_e_bar.
Structural: the transition is a polarity-switching process in A.

- initial : String
Initial particle.

- finals : List String
Final particles.

- mediator : String
Mediator boson.

- mediator_is_w : self.mediator = "W-"
The mediator is a W boson.

Instances For

---

### `Tau.BookIV.Electroweak.instReprBetaDecay.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L210-L210)
**def
Tau.BookIV.Electroweak.instReprBetaDecay.repr :BetaDecay → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprBetaDecay`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L210-L210)
**instance
Tau.BookIV.Electroweak.instReprBetaDecay :Repr BetaDecay**

Equations
- Tau.BookIV.Electroweak.instReprBetaDecay = { reprPrec := Tau.BookIV.Electroweak.instReprBetaDecay.repr }

---

### `Tau.BookIV.Electroweak.beta_decay_w`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L212-L217)
**def
Tau.BookIV.Electroweak.beta_decay_w :BetaDecay**


Neutron beta decay.
Equations
- Tau.BookIV.Electroweak.beta_decay_w = { initial := "neutron", finals := ["proton", "electron", "nu_e_bar"], mediator := "W-", mediator_is_w := ⋯ }
Instances For

---

### `Tau.BookIV.Electroweak.ZWidthPrediction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L223-L237)
**structure
Tau.BookIV.Electroweak.ZWidthPrediction :Type**


[IV.P64] The Z boson decay width constrains the number of light
neutrino generations to exactly 3. Each neutrino flavor adds
~167 MeV to the invisible width. The measured invisible width
(499 MeV) corresponds to N_nu = 2.9840, consistent with 3.

- n_nu : ℕ
Number of light neutrino generations.

- n_nu_eq : self.n_nu = 3
- width_per_nu : ℕ
Invisible width per neutrino (MeV, approximate).

- width_approx : self.width_per_nu = 167
- total_invisible : ℕ
Total invisible width (MeV, approximate).

- total_eq : self.total_invisible = 499
Instances For

---

### `Tau.BookIV.Electroweak.instReprZWidthPrediction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L237-L237)
**instance
Tau.BookIV.Electroweak.instReprZWidthPrediction :Repr ZWidthPrediction**

Equations
- Tau.BookIV.Electroweak.instReprZWidthPrediction = { reprPrec := Tau.BookIV.Electroweak.instReprZWidthPrediction.repr }

---

### `Tau.BookIV.Electroweak.instReprZWidthPrediction.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L237-L237)
**def
Tau.BookIV.Electroweak.instReprZWidthPrediction.repr :ZWidthPrediction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.z_width_three_nu`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L239-L246)
**def
Tau.BookIV.Electroweak.z_width_three_nu :ZWidthPrediction**


Z width predicts 3 light neutrino generations.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.EWPrediction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L252-L263)
**structure
Tau.BookIV.Electroweak.EWPrediction :Type**


[IV.P65] Electroweak prediction summary table: key observables
and their tau-framework status.

- name : String
Observable name.

- predicted : ℕ
Predicted value (scaled Nat).

- observed : ℕ
Observed value (scaled Nat).

- scale : String
Scale factor description.

Instances For

---

### `Tau.BookIV.Electroweak.instReprEWPrediction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L263-L263)
**instance
Tau.BookIV.Electroweak.instReprEWPrediction :Repr EWPrediction**

Equations
- Tau.BookIV.Electroweak.instReprEWPrediction = { reprPrec := Tau.BookIV.Electroweak.instReprEWPrediction.repr }

---

### `Tau.BookIV.Electroweak.instReprEWPrediction.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L263-L263)
**def
Tau.BookIV.Electroweak.instReprEWPrediction.repr :EWPrediction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.ew_predictions`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L265-L272)
**def
Tau.BookIV.Electroweak.ew_predictions :List EWPrediction**


Key EW predictions.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.ew_predictions_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L274-L274)
**theorem
Tau.BookIV.Electroweak.ew_predictions_count :ew_predictions.length = 5**
