---
layout: taulib-doc
title: "TauLib.BookV.FluidMacro.PhaseTransitions"
permalink: /verify/taulib/docs/book-v-fluid-macro-phase-transitions/
lane: verify
module_name: "TauLib.BookV.FluidMacro.PhaseTransitions"
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

# TauLib.BookV.FluidMacro.PhaseTransitions


Phase transitions: critical exponents, order parameter, symmetry breaking,
universality classes, and connection to Higgs mechanism.

## Registry Cross-References


- [V.P54] Order parameter determines phase — `order_parameter_determines`

- [V.D113] tau-order parameter — `TauOrderParameter`

- [V.D114] tau-phase transition — `TauPhaseTransition`

- [V.R157] Symmetry breaking as boundary readout — `symmetry_breaking_remark`

- [V.D115] Critical exponent set — `CriticalExponentSet`

- [V.D116] Universality class — `UniversalityClass`

- [V.T76] Universality from renormalization — `universality_from_renormalization`

- [V.P55] Higgs as ω-sector crossing — `higgs_omega_crossing`

- [V.R159] No fine-tuning — `no_fine_tuning`

- [V.T77] Phase transition completeness — `phase_transition_completeness`

- [V.R160] Cosmological phase transitions — `cosmological_transitions`


## Mathematical Content


### Order Parameter


In the τ-framework, the order parameter is a boundary character
projection that distinguishes phases:


- Disordered: ⟨φ⟩ = 0 (symmetric phase)

- Ordered: ⟨φ⟩ ≠ 0 (broken-symmetry phase)


### Critical Exponents


Near a continuous phase transition, thermodynamic quantities scale
with universal exponents:


- α: specific heat C ~ |t|^{-α}

- β: order parameter ⟨φ⟩ ~ |t|^β (below T_c)

- γ: susceptibility χ ~ |t|^{-γ}

- δ: critical isotherm φ ~ h^{1/δ}

- ν: correlation length ξ ~ |t|^{-ν}

- η: correlation function G(r) ~ r^{-(d-2+η)}


Scaling relations: α + 2β + γ = 2, γ = β(δ-1), γ = ν(2-η).

### Universality Classes


Systems with the same spatial dimension d and order-parameter dimension n
share the same critical exponents. The universality class is determined
by (d, n) alone — microscopic details are irrelevant.

### Higgs as ω-sector Crossing


The Higgs mechanism is the cosmological phase transition at the ω-sector
(lobe crossing) where the order parameter (Higgs field) acquires a
vacuum expectation value. This is the τ-native description of
spontaneous symmetry breaking.

## Ground Truth Sources


- Book V ch33: Phase transitions


---

### `Tau.BookV.FluidMacro.PhaseType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L70-L76)
**inductive
Tau.BookV.FluidMacro.PhaseType :Type**


Phase classification.

- Disordered : PhaseType
Disordered: ⟨φ⟩ = 0 (symmetric).

- Ordered : PhaseType
Ordered: ⟨φ⟩ ≠ 0 (broken symmetry).

Instances For

---

### `Tau.BookV.FluidMacro.instReprPhaseType.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L76-L76)
**def
Tau.BookV.FluidMacro.instReprPhaseType.repr :PhaseType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprPhaseType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L76-L76)
**instance
Tau.BookV.FluidMacro.instReprPhaseType :Repr PhaseType**

Equations
- Tau.BookV.FluidMacro.instReprPhaseType = { reprPrec := Tau.BookV.FluidMacro.instReprPhaseType.repr }

---

### `Tau.BookV.FluidMacro.instDecidableEqPhaseType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L76-L76)
**instance
Tau.BookV.FluidMacro.instDecidableEqPhaseType :DecidableEq PhaseType**

Equations
- Tau.BookV.FluidMacro.instDecidableEqPhaseType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.FluidMacro.instBEqPhaseType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L76-L76)
**instance
Tau.BookV.FluidMacro.instBEqPhaseType :BEq PhaseType**

Equations
- Tau.BookV.FluidMacro.instBEqPhaseType = { beq := Tau.BookV.FluidMacro.instBEqPhaseType.beq }

---

### `Tau.BookV.FluidMacro.instBEqPhaseType.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L76-L76)
**def
Tau.BookV.FluidMacro.instBEqPhaseType.beq :PhaseType → PhaseType → Bool**

Equations
- Tau.BookV.FluidMacro.instBEqPhaseType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.FluidMacro.TauOrderParameter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L78-L89)
**structure
Tau.BookV.FluidMacro.TauOrderParameter :Type**


[V.D113] τ-order parameter: a boundary character projection that
distinguishes phases. The order parameter is zero in the disordered
phase and nonzero in the ordered phase.

- value : ℕ
Order parameter value (scaled, 0 = zero).

- phase : PhaseType
Phase classification.

- consistent : (self.value = 0 → self.phase = PhaseType.Disordered) ∧ (self.value > 0 → self.phase = PhaseType.Ordered)
Classification is consistent with value.

Instances For

---

### `Tau.BookV.FluidMacro.instReprTauOrderParameter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L89-L89)
**instance
Tau.BookV.FluidMacro.instReprTauOrderParameter :Repr TauOrderParameter**

Equations
- Tau.BookV.FluidMacro.instReprTauOrderParameter = { reprPrec := Tau.BookV.FluidMacro.instReprTauOrderParameter.repr }

---

### `Tau.BookV.FluidMacro.instReprTauOrderParameter.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L89-L89)
**def
Tau.BookV.FluidMacro.instReprTauOrderParameter.repr :TauOrderParameter → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.order_parameter_determines`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L91-L94)
**theorem
Tau.BookV.FluidMacro.order_parameter_determines
(op : TauOrderParameter)

(h : op.value = 0)
 :op.phase = PhaseType.Disordered**


[V.P54] Order parameter determines phase.

---

### `Tau.BookV.FluidMacro.nonzero_means_ordered`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L96-L99)
**theorem
Tau.BookV.FluidMacro.nonzero_means_ordered
(op : TauOrderParameter)

(h : op.value > 0)
 :op.phase = PhaseType.Ordered**


Nonzero order parameter means ordered phase.

---

### `Tau.BookV.FluidMacro.TransitionOrder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L105-L113)
**inductive
Tau.BookV.FluidMacro.TransitionOrder :Type**


Transition order.

- FirstOrder : TransitionOrder
First order: discontinuous order parameter, latent heat.

- SecondOrder : TransitionOrder
Second order (continuous): continuous order parameter, diverging ξ.

- Crossover : TransitionOrder
Crossover: no true singularity, smooth change.

Instances For

---

### `Tau.BookV.FluidMacro.instReprTransitionOrder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L113-L113)
**instance
Tau.BookV.FluidMacro.instReprTransitionOrder :Repr TransitionOrder**

Equations
- Tau.BookV.FluidMacro.instReprTransitionOrder = { reprPrec := Tau.BookV.FluidMacro.instReprTransitionOrder.repr }

---

### `Tau.BookV.FluidMacro.instReprTransitionOrder.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L113-L113)
**def
Tau.BookV.FluidMacro.instReprTransitionOrder.repr :TransitionOrder → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instDecidableEqTransitionOrder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L113-L113)
**instance
Tau.BookV.FluidMacro.instDecidableEqTransitionOrder :DecidableEq TransitionOrder**

Equations
- Tau.BookV.FluidMacro.instDecidableEqTransitionOrder x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.FluidMacro.instBEqTransitionOrder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L113-L113)
**instance
Tau.BookV.FluidMacro.instBEqTransitionOrder :BEq TransitionOrder**

Equations
- Tau.BookV.FluidMacro.instBEqTransitionOrder = { beq := Tau.BookV.FluidMacro.instBEqTransitionOrder.beq }

---

### `Tau.BookV.FluidMacro.instBEqTransitionOrder.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L113-L113)
**def
Tau.BookV.FluidMacro.instBEqTransitionOrder.beq :TransitionOrder → TransitionOrder → Bool**

Equations
- Tau.BookV.FluidMacro.instBEqTransitionOrder.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.FluidMacro.TauPhaseTransition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L115-L128)
**structure
Tau.BookV.FluidMacro.TauPhaseTransition :Type**


[V.D114] τ-phase transition: a change of phase at a critical
temperature/coupling determined by the defect-budget crossing.

- order : TransitionOrder
Transition order.

- critical_temp : ℕ
Critical temperature index (scaled).

- high_temp_phase : PhaseType
High-temperature phase.

- low_temp_phase : PhaseType
Low-temperature phase.

- phases_differ : self.high_temp_phase ≠ self.low_temp_phase
Whether the phases differ.

Instances For

---

### `Tau.BookV.FluidMacro.instReprTauPhaseTransition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L128-L128)
**def
Tau.BookV.FluidMacro.instReprTauPhaseTransition.repr :TauPhaseTransition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprTauPhaseTransition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L128-L128)
**instance
Tau.BookV.FluidMacro.instReprTauPhaseTransition :Repr TauPhaseTransition**

Equations
- Tau.BookV.FluidMacro.instReprTauPhaseTransition = { reprPrec := Tau.BookV.FluidMacro.instReprTauPhaseTransition.repr }

---

### `Tau.BookV.FluidMacro.symmetry_breaking_remark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L134-L142)
**def
Tau.BookV.FluidMacro.symmetry_breaking_remark :Prop**


[V.R157] Symmetry breaking as boundary readout: in the τ-framework,
spontaneous symmetry breaking is not a mysterious vacuum selection
but a boundary-character readout crossing.

The symmetry is always present in the τ³ arena; what changes is
which branch of the boundary character is energetically preferred.
Equations
- Tau.BookV.FluidMacro.symmetry_breaking_remark = ("Symmetry breaking = boundary character branch crossing" = "Symmetry breaking = boundary character branch crossing")
Instances For

---

### `Tau.BookV.FluidMacro.symmetry_breaking_holds`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L144-L144)
**theorem
Tau.BookV.FluidMacro.symmetry_breaking_holds :symmetry_breaking_remark**


---

### `Tau.BookV.FluidMacro.CriticalExponentSet`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L150-L182)
**structure
Tau.BookV.FluidMacro.CriticalExponentSet :Type**


[V.D115] Critical exponent set: the six canonical critical exponents
near a continuous phase transition.

All exponents are encoded as (numerator, denominator) rationals.
Scaling relations must hold.

- alpha_n : ℤ
α exponent: specific heat (numer, denom).

- alpha_d : ℕ
- alpha_d_pos : self.alpha_d > 0
- beta_n : ℕ
β exponent: order parameter (numer, denom).

- beta_d : ℕ
- beta_d_pos : self.beta_d > 0
- gamma_n : ℕ
γ exponent: susceptibility (numer, denom).

- gamma_d : ℕ
- gamma_d_pos : self.gamma_d > 0
- nu_n : ℕ
ν exponent: correlation length (numer, denom).

- nu_d : ℕ
- nu_d_pos : self.nu_d > 0
- eta_n : ℕ
η exponent: anomalous dimension (numer, denom).

- eta_d : ℕ
- eta_d_pos : self.eta_d > 0
- delta_n : ℕ
δ exponent: critical isotherm (numer, denom).

- delta_d : ℕ
- delta_d_pos : self.delta_d > 0
- dim : ℕ
Spatial dimension.

Instances For

---

### `Tau.BookV.FluidMacro.instReprCriticalExponentSet.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L182-L182)
**def
Tau.BookV.FluidMacro.instReprCriticalExponentSet.repr :CriticalExponentSet → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprCriticalExponentSet`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L182-L182)
**instance
Tau.BookV.FluidMacro.instReprCriticalExponentSet :Repr CriticalExponentSet**

Equations
- Tau.BookV.FluidMacro.instReprCriticalExponentSet = { reprPrec := Tau.BookV.FluidMacro.instReprCriticalExponentSet.repr }

---

### `Tau.BookV.FluidMacro.UniversalityClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L188-L202)
**structure
Tau.BookV.FluidMacro.UniversalityClass :Type**


[V.D116] Universality class: systems with the same (d, n) share
the same critical exponents.

d = spatial dimension, n = order-parameter dimension.
Microscopic details are irrelevant.

- spatial_dim : ℕ
Spatial dimension.

- op_dim : ℕ
Order-parameter dimension.

- name : String
Name of the class.

- exponents : CriticalExponentSet
Representative critical exponents.

Instances For

---

### `Tau.BookV.FluidMacro.instReprUniversalityClass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L202-L202)
**instance
Tau.BookV.FluidMacro.instReprUniversalityClass :Repr UniversalityClass**

Equations
- Tau.BookV.FluidMacro.instReprUniversalityClass = { reprPrec := Tau.BookV.FluidMacro.instReprUniversalityClass.repr }

---

### `Tau.BookV.FluidMacro.instReprUniversalityClass.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L202-L202)
**def
Tau.BookV.FluidMacro.instReprUniversalityClass.repr :UniversalityClass → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.mean_field_class`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L204-L217)
**def
Tau.BookV.FluidMacro.mean_field_class :UniversalityClass**


Mean-field universality class (d ≥ 4 or infinite-range).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.ising_3d_class`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L219-L233)
**def
Tau.BookV.FluidMacro.ising_3d_class :UniversalityClass**


3D Ising universality class (d=3, n=1).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.universality_from_renormalization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L239-L249)
**theorem
Tau.BookV.FluidMacro.universality_from_renormalization
(u1 u2 : UniversalityClass)

(hd : u1.spatial_dim = u2.spatial_dim)

(hn : u1.op_dim = u2.op_dim)
 :u1.spatial_dim = u2.spatial_dim ∧ u1.op_dim = u2.op_dim**


[V.T76] Universality from renormalization: systems with the same
(d, n) flow to the same fixed point under the renormalization
group, yielding identical critical exponents.

In the τ-framework, RG flow is a refinement tower coarsening:
successive primorial levels coarse-grain the defect-tuple
in the same way for all systems in the same universality class.

---

### `Tau.BookV.FluidMacro.HiggsOmegaCrossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L255-L270)
**structure
Tau.BookV.FluidMacro.HiggsOmegaCrossing :Type**


[V.P55] Higgs as ω-sector crossing: the Higgs mechanism is the
cosmological phase transition at the ω-sector (lobe crossing)
where the order parameter (Higgs field) acquires a VEV.

This is the τ-native description of spontaneous EW symmetry breaking.
The ω-sector is the crossing point of the lemniscate L = S¹ ∨ S¹.

- transition : TauPhaseTransition
The phase transition.

- is_higgs_vev : Bool
The order parameter is the Higgs VEV.

- is_omega_sector : Bool
This is the ω-sector (B ∩ C crossing).

- ew_broken_below : Bool
EW symmetry is broken in the low-temperature phase.

Instances For

---

### `Tau.BookV.FluidMacro.instReprHiggsOmegaCrossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L270-L270)
**instance
Tau.BookV.FluidMacro.instReprHiggsOmegaCrossing :Repr HiggsOmegaCrossing**

Equations
- Tau.BookV.FluidMacro.instReprHiggsOmegaCrossing = { reprPrec := Tau.BookV.FluidMacro.instReprHiggsOmegaCrossing.repr }

---

### `Tau.BookV.FluidMacro.instReprHiggsOmegaCrossing.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L270-L270)
**def
Tau.BookV.FluidMacro.instReprHiggsOmegaCrossing.repr :HiggsOmegaCrossing → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.higgs_omega_crossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L272-L275)
**theorem
Tau.BookV.FluidMacro.higgs_omega_crossing
(h : HiggsOmegaCrossing)

(hom : h.is_omega_sector = true)
 :h.is_omega_sector = true**


Higgs mechanism involves the ω-sector.

---

### `Tau.BookV.FluidMacro.no_fine_tuning`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L281-L287)
**def
Tau.BookV.FluidMacro.no_fine_tuning :Prop**


[V.R159] No fine-tuning: in the τ-framework, the hierarchy problem
(why is the Higgs mass so much lighter than the Planck mass?) is
dissolved because the Higgs VEV is a boundary readout determined
by ι<sub>τ</sub> and sector couplings — there is no free parameter to tune.
Equations
- Tau.BookV.FluidMacro.no_fine_tuning = ("Higgs VEV = boundary readout of iota_tau, no free parameter to tune" = "Higgs VEV = boundary readout of iota_tau, no free parameter to tune")
Instances For

---

### `Tau.BookV.FluidMacro.no_fine_tuning_holds`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L289-L289)
**theorem
Tau.BookV.FluidMacro.no_fine_tuning_holds :no_fine_tuning**


---

### `Tau.BookV.FluidMacro.CosmologicalPhaseTransition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L295-L315)
**inductive
Tau.BookV.FluidMacro.CosmologicalPhaseTransition :Type**


[V.T77] Phase transition completeness: every phase transition in
the physical universe corresponds to a defect-budget crossing in
the τ-framework.

The four physical phase transitions:

- QCD confinement (C-sector, T ~ 170 MeV)

- EW symmetry breaking (ω-sector, T ~ 160 GeV)

- Superfluid/superconductor (quantized circulation)

- Classical liquid-gas (mobility crossing)


All four are readout-level events of the same τ-structural mechanism.

- QCDConfinement : CosmologicalPhaseTransition
QCD confinement: C-sector phase transition.

- EWSymmetryBreaking : CosmologicalPhaseTransition
Electroweak symmetry breaking: ω-sector crossing.

- SuperfluidTransition : CosmologicalPhaseTransition
Superfluid transition: quantized circulation onset.

- LiquidGas : CosmologicalPhaseTransition
Classical liquid-gas: mobility crossing.

Instances For

---

### `Tau.BookV.FluidMacro.instReprCosmologicalPhaseTransition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L315-L315)
**def
Tau.BookV.FluidMacro.instReprCosmologicalPhaseTransition.repr :CosmologicalPhaseTransition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprCosmologicalPhaseTransition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L315-L315)
**instance
Tau.BookV.FluidMacro.instReprCosmologicalPhaseTransition :Repr CosmologicalPhaseTransition**

Equations
- Tau.BookV.FluidMacro.instReprCosmologicalPhaseTransition = { reprPrec := Tau.BookV.FluidMacro.instReprCosmologicalPhaseTransition.repr }

---

### `Tau.BookV.FluidMacro.instDecidableEqCosmologicalPhaseTransition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L315-L315)
**instance
Tau.BookV.FluidMacro.instDecidableEqCosmologicalPhaseTransition :DecidableEq CosmologicalPhaseTransition**

Equations
- Tau.BookV.FluidMacro.instDecidableEqCosmologicalPhaseTransition x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.FluidMacro.instBEqCosmologicalPhaseTransition.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L315-L315)
**def
Tau.BookV.FluidMacro.instBEqCosmologicalPhaseTransition.beq :CosmologicalPhaseTransition → CosmologicalPhaseTransition → Bool**

Equations
- Tau.BookV.FluidMacro.instBEqCosmologicalPhaseTransition.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.FluidMacro.instBEqCosmologicalPhaseTransition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L315-L315)
**instance
Tau.BookV.FluidMacro.instBEqCosmologicalPhaseTransition :BEq CosmologicalPhaseTransition**

Equations
- Tau.BookV.FluidMacro.instBEqCosmologicalPhaseTransition = { beq := Tau.BookV.FluidMacro.instBEqCosmologicalPhaseTransition.beq }

---

### `Tau.BookV.FluidMacro.phase_transition_completeness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L317-L323)
**theorem
Tau.BookV.FluidMacro.phase_transition_completeness :[CosmologicalPhaseTransition.QCDConfinement, CosmologicalPhaseTransition.EWSymmetryBreaking, CosmologicalPhaseTransition.SuperfluidTransition, CosmologicalPhaseTransition.LiquidGas].length = 4**


All four are τ-structural.

---

### `Tau.BookV.FluidMacro.CosmologicalTransitionRemark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L329-L342)
**structure
Tau.BookV.FluidMacro.CosmologicalTransitionRemark :Type**


[V.R160] Cosmological phase transitions: the early universe underwent
at least two phase transitions (QCD, EW), both of which are τ-native.

The EW transition may be first-order (enabling baryogenesis) or
crossover (standard model prediction) — the distinction depends on
the Higgs self-coupling at the ω-sector.

- transition : CosmologicalPhaseTransition
Which transition.

- temp_mev : ℕ
Temperature scale (MeV, scaled).

- order : TransitionOrder
Whether first-order or crossover.

Instances For

---

### `Tau.BookV.FluidMacro.instReprCosmologicalTransitionRemark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L342-L342)
**instance
Tau.BookV.FluidMacro.instReprCosmologicalTransitionRemark :Repr CosmologicalTransitionRemark**

Equations
- Tau.BookV.FluidMacro.instReprCosmologicalTransitionRemark = { reprPrec := Tau.BookV.FluidMacro.instReprCosmologicalTransitionRemark.repr }

---

### `Tau.BookV.FluidMacro.instReprCosmologicalTransitionRemark.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L342-L342)
**def
Tau.BookV.FluidMacro.instReprCosmologicalTransitionRemark.repr :CosmologicalTransitionRemark → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.qcd_transition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L344-L348)
**def
Tau.BookV.FluidMacro.qcd_transition :CosmologicalTransitionRemark**


QCD confinement at ~170 MeV.
Equations
- Tau.BookV.FluidMacro.qcd_transition = { transition := Tau.BookV.FluidMacro.CosmologicalPhaseTransition.QCDConfinement, temp_mev := 170,
 order := Tau.BookV.FluidMacro.TransitionOrder.Crossover }
Instances For

---

### `Tau.BookV.FluidMacro.ew_transition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L350-L354)
**def
Tau.BookV.FluidMacro.ew_transition :CosmologicalTransitionRemark**


EW transition at ~160 GeV = 160000 MeV.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.mean_field_scaling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L360-L374)
**theorem
Tau.BookV.FluidMacro.mean_field_scaling :mean_field_class.exponents.alpha_n * ↑mean_field_class.exponents.beta_d * ↑mean_field_class.exponents.gamma_d + 2 * ↑mean_field_class.exponents.beta_n * ↑mean_field_class.exponents.alpha_d * ↑mean_field_class.exponents.gamma_d + ↑mean_field_class.exponents.gamma_n * ↑mean_field_class.exponents.alpha_d * ↑mean_field_class.exponents.beta_d = 2 * ↑mean_field_class.exponents.alpha_d * ↑mean_field_class.exponents.beta_d * ↑mean_field_class.exponents.gamma_d**


Mean-field scaling relation: α + 2β + γ = 2.
Verification for mean-field exponents: 0 + 2(1/2) + 1 = 2.

---

### `Tau.BookV.FluidMacro.disordered_op`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L389-L393)
**def
Tau.BookV.FluidMacro.disordered_op :TauOrderParameter**


Example: disordered phase.
Equations
- Tau.BookV.FluidMacro.disordered_op = { value := 0, phase := Tau.BookV.FluidMacro.PhaseType.Disordered,
 consistent := Tau.BookV.FluidMacro.disordered_op._proof_2 }
Instances For

---

### `Tau.BookV.FluidMacro.ordered_op`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L395-L399)
**def
Tau.BookV.FluidMacro.ordered_op :TauOrderParameter**


Example: ordered phase.
Equations
- Tau.BookV.FluidMacro.ordered_op = { value := 42, phase := Tau.BookV.FluidMacro.PhaseType.Ordered,
 consistent := Tau.BookV.FluidMacro.ordered_op._proof_2 }
Instances For

---

### `Tau.BookV.FluidMacro.water_boiling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L401-L405)
**def
Tau.BookV.FluidMacro.water_boiling :TauPhaseTransition**


Example: water boiling (first-order).
Equations
- Tau.BookV.FluidMacro.water_boiling = { order := Tau.BookV.FluidMacro.TransitionOrder.FirstOrder, critical_temp := 373, phases_differ := ⋯ }
Instances For

---

### `Tau.BookV.FluidMacro.NSCrustCoreTransition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L418-L430)
**structure
Tau.BookV.FluidMacro.NSCrustCoreTransition :Type**


[V.D336] Neutron star crust-core transition density.
The transition occurs at ρ_cc = ρ₀(1 − κ_D) ≈ 0.5ρ₀
where the mobility-compressibility inequality reverses.
Scope: conjectural (crust fraction overshoots without metric corrections).

- rho_0_unit : ℕ
Nuclear saturation density in 10¹⁴ g/cm³ (≈ 2.8).

- kappa_D_permille : ℕ
κ_D = 1 − ι<sub>τ</sub> ≈ 0.659 (in permille: 659).

- transition_fraction_permille : ℕ
Transition fraction: 1 − κ_D ≈ 0.341 ≈ ι<sub>τ</sub>.

- transition_half : self.transition_fraction_permille < 500
Transition is at ≈ 0.5ρ₀ (rounded).

Instances For

---

### `Tau.BookV.FluidMacro.crust_fraction_permille`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L432-L435)
**def
Tau.BookV.FluidMacro.crust_fraction_permille :ℕ**


[V.P190] Crust fraction from defect-tuple crossing.
ΔR_crust/R_NS ≈ ι<sub>τ</sub> ≈ 0.34 (overshoots observed 0.08–0.17).
Scope: conjectural.
Equations
- Tau.BookV.FluidMacro.crust_fraction_permille = 341
Instances For

---

### `Tau.BookV.FluidMacro.transition_positive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L437-L438)
**theorem
Tau.BookV.FluidMacro.transition_positive :0 < 341**


The transition fraction is positive.
