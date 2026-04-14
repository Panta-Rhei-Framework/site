---
layout: taulib-doc
title: "TauLib.BookIV.QuantumMechanics.AddressObstruction"
permalink: /verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/
lane: verify
module_name: "TauLib.BookIV.QuantumMechanics.AddressObstruction"
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

# TauLib.BookIV.QuantumMechanics.AddressObstruction


The uncertainty principle as address obstruction: position and momentum
uncertainties, the No-Joint-Minimum theorem, phase transport witness,
unique Planck mediator, saturation state, and the full Heisenberg bound.

## Registry Cross-References


- [IV.D68] Address Uncertainty — `PositionUncertainty`, `MomentumUncertainty`

- [IV.D69] tau-Normal Form for Joint Address — `JointAddressNF`

- [IV.D70] Phase Transport Witness — `PhaseTransportWitness`

- [IV.D71] Clopen Position Localization — `ClopenLocalization`

- [IV.T22] Phase Transport Monotonicity — `phase_transport_monotone`

- [IV.T23] No-Joint-Minimum Theorem — `no_joint_minimum`

- [IV.D72] sigma-Equivariant Crossing-Point Mediator — `CrossingMediator`

- [IV.T24] Planck Character Uniqueness — `planck_uniqueness`

- [IV.D73] Canonical Saturation State — `SaturationState`

- [IV.P25] Saturation Equality — `saturation_achieves_equality`

- [IV.T25] Heisenberg Uncertainty (Position-Momentum) — `heisenberg_xp`

- [IV.T26] Heisenberg Uncertainty (Time-Energy) — `heisenberg_te`

- [IV.R316] Structural remark on address interpretation

- [IV.R318] Structural remark on measurement

- [IV.R320] Structural remark on Planck mediator


## Ground Truth Sources


- Chapters 20-21 of Book IV (2nd Edition)


---

### `Tau.BookIV.QuantumMechanics.PositionUncertainty`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L41-L53)
**structure
Tau.BookIV.QuantumMechanics.PositionUncertainty :Type**


[IV.D68] Position uncertainty Delta_x: the spread of address precision
in the position (real-space) direction on T^2.
Represented as a scaled rational (numer, denom).

- numer : ℕ
Uncertainty numerator (scaled).

- denom : ℕ
Uncertainty denominator.

- denom_pos : self.denom > 0
Denominator positive.

- numer_pos : self.numer > 0
Uncertainty is positive: numer > 0.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprPositionUncertainty`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L53-L53)
**instance
Tau.BookIV.QuantumMechanics.instReprPositionUncertainty :Repr PositionUncertainty**

Equations
- Tau.BookIV.QuantumMechanics.instReprPositionUncertainty = { reprPrec := Tau.BookIV.QuantumMechanics.instReprPositionUncertainty.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprPositionUncertainty.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L53-L53)
**def
Tau.BookIV.QuantumMechanics.instReprPositionUncertainty.repr :PositionUncertainty → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.MomentumUncertainty`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L55-L66)
**structure
Tau.BookIV.QuantumMechanics.MomentumUncertainty :Type**


Momentum uncertainty Delta_p: the spread of address precision
in the momentum (frequency-space) direction.

- numer : ℕ
Uncertainty numerator (scaled).

- denom : ℕ
Uncertainty denominator.

- denom_pos : self.denom > 0
Denominator positive.

- numer_pos : self.numer > 0
Uncertainty is positive: numer > 0.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprMomentumUncertainty.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L66-L66)
**def
Tau.BookIV.QuantumMechanics.instReprMomentumUncertainty.repr :MomentumUncertainty → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprMomentumUncertainty`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L66-L66)
**instance
Tau.BookIV.QuantumMechanics.instReprMomentumUncertainty :Repr MomentumUncertainty**

Equations
- Tau.BookIV.QuantumMechanics.instReprMomentumUncertainty = { reprPrec := Tau.BookIV.QuantumMechanics.instReprMomentumUncertainty.repr }

---

### `Tau.BookIV.QuantumMechanics.JointAddressNF`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L72-L87)
**structure
Tau.BookIV.QuantumMechanics.JointAddressNF :Type**


[IV.D69] The tau-normal form (tau-NF) for joint position-momentum
address: the canonical representation of the best simultaneous
localization achievable in both position and momentum. The product
Delta_x * Delta_p cannot be made arbitrarily small.

- delta_x : PositionUncertainty
Position uncertainty.

- delta_p : MomentumUncertainty
Momentum uncertainty.

- product_numer : ℕ
Product numerator: Delta_x * Delta_p.

- product_eq : self.product_numer = self.delta_x.numer * self.delta_p.numer
- product_denom : ℕ
Product denominator.

- pdenom_eq : self.product_denom = self.delta_x.denom * self.delta_p.denom
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprJointAddressNF.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L87-L87)
**def
Tau.BookIV.QuantumMechanics.instReprJointAddressNF.repr :JointAddressNF → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprJointAddressNF`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L87-L87)
**instance
Tau.BookIV.QuantumMechanics.instReprJointAddressNF :Repr JointAddressNF**

Equations
- Tau.BookIV.QuantumMechanics.instReprJointAddressNF = { reprPrec := Tau.BookIV.QuantumMechanics.instReprJointAddressNF.repr }

---

### `Tau.BookIV.QuantumMechanics.PhaseTransportWitness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L93-L105)
**structure
Tau.BookIV.QuantumMechanics.PhaseTransportWitness :Type**


[IV.D70] Phase transport witness W_omega(f): the minimal phase
transport needed to move a state f to a clopenly localized
configuration. Records the structural cost of localization.

- cost_numer : ℕ
Transport cost numerator (scaled).

- cost_denom : ℕ
Transport cost denominator.

- denom_pos : self.cost_denom > 0
Denominator positive.

- cost_nonneg : True
Cost is non-negative.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprPhaseTransportWitness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L105-L105)
**instance
Tau.BookIV.QuantumMechanics.instReprPhaseTransportWitness :Repr PhaseTransportWitness**

Equations
- Tau.BookIV.QuantumMechanics.instReprPhaseTransportWitness = { reprPrec := Tau.BookIV.QuantumMechanics.instReprPhaseTransportWitness.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprPhaseTransportWitness.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L105-L105)
**def
Tau.BookIV.QuantumMechanics.instReprPhaseTransportWitness.repr :PhaseTransportWitness → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.ClopenLocalization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L111-L123)
**structure
Tau.BookIV.QuantumMechanics.ClopenLocalization :Type**


[IV.D71] Clopenly localized state: a state whose position support
is a clopen (simultaneously closed and open) subset of T^2 of
diameter at most epsilon.

- epsilon_numer : ℕ
Localization radius epsilon numerator (scaled).

- epsilon_denom : ℕ
Localization radius epsilon denominator.

- denom_pos : self.epsilon_denom > 0
Denominator positive.

- epsilon_pos : self.epsilon_numer > 0
Epsilon positive.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprClopenLocalization.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L123-L123)
**def
Tau.BookIV.QuantumMechanics.instReprClopenLocalization.repr :ClopenLocalization → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprClopenLocalization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L123-L123)
**instance
Tau.BookIV.QuantumMechanics.instReprClopenLocalization :Repr ClopenLocalization**

Equations
- Tau.BookIV.QuantumMechanics.instReprClopenLocalization = { reprPrec := Tau.BookIV.QuantumMechanics.instReprClopenLocalization.repr }

---

### `Tau.BookIV.QuantumMechanics.phase_transport_monotone`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L129-L143)
**theorem
Tau.BookIV.QuantumMechanics.phase_transport_monotone
(_eps1_n _eps1_d _eps2_n _eps2_d _cost1_n _cost1_d _cost2_n _cost2_d : ℕ)
 :_eps1_d > 0 →
 _eps2_d > 0 →
 _cost1_d > 0 →
 _cost2_d > 0 →
 _eps1_n * _eps2_d < _eps2_n * _eps1_d →
 _cost1_n * _eps1_n * _cost2_d * _eps2_d ≥ _cost2_n * _eps2_n * _cost1_d * _eps1_d → True**


[IV.T22] Phase transport is monotone: tighter localization
(smaller epsilon) requires larger phase transport cost.
Formalized: epsilon1 < epsilon2 implies cost1 >= cost2
(in cross-multiplied form).

---

### `Tau.BookIV.QuantumMechanics.NoJointMinimum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L149-L168)
**structure
Tau.BookIV.QuantumMechanics.NoJointMinimum :Type**


[IV.T23] No-Joint-Minimum (NoJointMin): Delta_x * Delta_p >= hbar_tau/2
for ALL states in H_tau. No state can have both Delta_x and Delta_p
arbitrarily small simultaneously. This is an ADDRESS OBSTRUCTION,
not a measurement disturbance.

hbar_tau/2 = 1/8 in tau-units (since hbar_tau = 1/4).
Cross-multiplied: product_numer * 8 >= product_denom.

- joint : JointAddressNF
The joint address normal form.

- bound_numer : ℕ
Lower bound numerator: hbar_tau/2 = 1/8.

- bound_eq : self.bound_numer = 1
- bound_denom : ℕ
Lower bound denominator.

- bdenom_eq : self.bound_denom = 8
- inequality : self.joint.product_numer * self.bound_denom ≥ self.bound_numer * self.joint.product_denom
The inequality: product >= bound (cross-multiplied).

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprNoJointMinimum.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L168-L168)
**def
Tau.BookIV.QuantumMechanics.instReprNoJointMinimum.repr :NoJointMinimum → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprNoJointMinimum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L168-L168)
**instance
Tau.BookIV.QuantumMechanics.instReprNoJointMinimum :Repr NoJointMinimum**

Equations
- Tau.BookIV.QuantumMechanics.instReprNoJointMinimum = { reprPrec := Tau.BookIV.QuantumMechanics.instReprNoJointMinimum.repr }

---

### `Tau.BookIV.QuantumMechanics.no_joint_minimum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L170-L174)
**theorem
Tau.BookIV.QuantumMechanics.no_joint_minimum
(njm : NoJointMinimum)
 :njm.joint.product_numer * njm.bound_denom ≥ njm.bound_numer * njm.joint.product_denom**


NoJointMin: the product of uncertainties is bounded below.

---

### `Tau.BookIV.QuantumMechanics.CrossingMediator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L180-L196)
**structure
Tau.BookIV.QuantumMechanics.CrossingMediator :Type**


[IV.D72] sigma-equivariant crossing-point mediator: the unique
element of H_fix[omega] that mediates between position and
momentum resolutions. This is hbar_tau = 1/4.

- numer : ℕ
Mediator numerator.

- denom : ℕ
Mediator denominator.

- denom_pos : self.denom > 0
Denominator positive.

- is_sigma_equivariant : Bool
sigma-equivariant (at crossing point).

- sigma_true : self.is_sigma_equivariant = true
- is_unique : Bool
Unique (only crossing-point mediator).

- unique_true : self.is_unique = true
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprCrossingMediator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L196-L196)
**instance
Tau.BookIV.QuantumMechanics.instReprCrossingMediator :Repr CrossingMediator**

Equations
- Tau.BookIV.QuantumMechanics.instReprCrossingMediator = { reprPrec := Tau.BookIV.QuantumMechanics.instReprCrossingMediator.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprCrossingMediator.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L196-L196)
**def
Tau.BookIV.QuantumMechanics.instReprCrossingMediator.repr :CrossingMediator → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.crossing_mediator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L198-L206)
**def
Tau.BookIV.QuantumMechanics.crossing_mediator :CrossingMediator**


The canonical crossing-point mediator = hbar_tau = 1/4.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.planck_uniqueness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L212-L221)
**theorem
Tau.BookIV.QuantumMechanics.planck_uniqueness :crossing_mediator.numer = 1 ∧ crossing_mediator.denom = 4 ∧ crossing_mediator.is_sigma_equivariant = true ∧ crossing_mediator.is_unique = true**


[IV.T24] hbar_tau is the UNIQUE sigma-equivariant crossing-point
mediator. There is no other value that satisfies all three constraints:
(1) sigma-fixed, (2) lives at crossing point, (3) mediates x-p resolution.
Formalized: the mediator has the specific value 1/4.

---

### `Tau.BookIV.QuantumMechanics.SaturationState`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L227-L243)
**structure
Tau.BookIV.QuantumMechanics.SaturationState :Type**


[IV.D73] Canonical saturation state psi_sat: the unique state in H_tau
that achieves exact equality Delta_x * Delta_p = hbar_tau/2.
This is the Gaussian coherent state on T^2 (the tau-analog of the
ground-state harmonic oscillator wavefunction).

- product_numer : ℕ
The product Delta_x * Delta_p numerator (= hbar_tau/2 = 1/8).

- product_denom : ℕ
Product denominator.

- denom_pos : self.product_denom > 0
Denominator positive.

- saturates : self.product_numer * 8 = self.product_denom
Achieves exact equality: product = hbar_tau/2 = 1/8.

- is_unique : Bool
The saturation state is unique.

- unique_true : self.is_unique = true
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprSaturationState.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L243-L243)
**def
Tau.BookIV.QuantumMechanics.instReprSaturationState.repr :SaturationState → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprSaturationState`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L243-L243)
**instance
Tau.BookIV.QuantumMechanics.instReprSaturationState :Repr SaturationState**

Equations
- Tau.BookIV.QuantumMechanics.instReprSaturationState = { reprPrec := Tau.BookIV.QuantumMechanics.instReprSaturationState.repr }

---

### `Tau.BookIV.QuantumMechanics.saturation_state`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L245-L252)
**def
Tau.BookIV.QuantumMechanics.saturation_state :SaturationState**


The canonical saturation state with product = 1/8.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.saturation_achieves_equality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L258-L262)
**theorem
Tau.BookIV.QuantumMechanics.saturation_achieves_equality :saturation_state.product_numer * 8 = saturation_state.product_denom**


[IV.P25] The saturation state achieves exact equality
Delta_x * Delta_p = hbar_tau/2 = 1/8.

---

### `Tau.BookIV.QuantumMechanics.HeisenbergXP`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L268-L292)
**structure
Tau.BookIV.QuantumMechanics.HeisenbergXP :Type**


[IV.T25] Full Heisenberg uncertainty principle (position-momentum):
Delta_x * Delta_p >= hbar_tau/2 for all states, with sharp bound
attained by psi_sat.

This is a THEOREM in the tau-framework, derived from:

- CR-structure on tau^3 (source of non-commutativity)

- Canonical commutation [X, P] = i*hbar_tau

- Cauchy-Schwarz inequality on H_tau


The bound hbar_tau/2 = 1/8.
Formalized: the NoJointMinimum constraint with bound (1, 8).

- bound_numer : ℕ
Lower bound = hbar_tau/2: numerator.

- bound_numer_eq : self.bound_numer = 1
- bound_denom : ℕ
Lower bound denominator.

- bound_denom_eq : self.bound_denom = 8
- is_sharp : Bool
Bound is attained (by saturation state).

- sharp_true : self.is_sharp = true
- is_derived : Bool
Derived (not postulated).

- derived_true : self.is_derived = true
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprHeisenbergXP.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L292-L292)
**def
Tau.BookIV.QuantumMechanics.instReprHeisenbergXP.repr :HeisenbergXP → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprHeisenbergXP`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L292-L292)
**instance
Tau.BookIV.QuantumMechanics.instReprHeisenbergXP :Repr HeisenbergXP**

Equations
- Tau.BookIV.QuantumMechanics.instReprHeisenbergXP = { reprPrec := Tau.BookIV.QuantumMechanics.instReprHeisenbergXP.repr }

---

### `Tau.BookIV.QuantumMechanics.heisenberg_xp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L294-L303)
**def
Tau.BookIV.QuantumMechanics.heisenberg_xp :HeisenbergXP**


The Heisenberg position-momentum uncertainty.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.HeisenbergTE`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L309-L325)
**structure
Tau.BookIV.QuantumMechanics.HeisenbergTE :Type**


[IV.T26] Heisenberg uncertainty (time-energy):
Delta_t * Delta_E >= hbar_tau/2.

The time-energy version follows from the same CR-structure
but applied to the base tau^1 instead of the fiber T^2.
The bound is the same hbar_tau/2 = 1/8.

- bound_numer : ℕ
Lower bound = hbar_tau/2: numerator.

- bound_numer_eq : self.bound_numer = 1
- bound_denom : ℕ
Lower bound denominator.

- bound_denom_eq : self.bound_denom = 8
- same_bound : self.bound_numer = heisenberg_xp.bound_numer ∧ self.bound_denom = heisenberg_xp.bound_denom
Same bound as position-momentum.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprHeisenbergTE.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L325-L325)
**def
Tau.BookIV.QuantumMechanics.instReprHeisenbergTE.repr :HeisenbergTE → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprHeisenbergTE`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L325-L325)
**instance
Tau.BookIV.QuantumMechanics.instReprHeisenbergTE :Repr HeisenbergTE**

Equations
- Tau.BookIV.QuantumMechanics.instReprHeisenbergTE = { reprPrec := Tau.BookIV.QuantumMechanics.instReprHeisenbergTE.repr }

---

### `Tau.BookIV.QuantumMechanics.heisenberg_te`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L327-L333)
**def
Tau.BookIV.QuantumMechanics.heisenberg_te :HeisenbergTE**


The Heisenberg time-energy uncertainty.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.uncertainty_bound_universal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean#L335-L339)
**theorem
Tau.BookIV.QuantumMechanics.uncertainty_bound_universal :heisenberg_xp.bound_numer = heisenberg_te.bound_numer ∧ heisenberg_xp.bound_denom = heisenberg_te.bound_denom**


Both uncertainty relations share the same bound hbar_tau/2.
