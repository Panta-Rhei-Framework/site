---
layout: taulib-doc
title: "TauLib.BookIV.Electroweak.GaugeInvariance"
permalink: /verify/taulib/docs/book-iv-electroweak-gauge-invariance/
lane: verify
module_name: "TauLib.BookIV.Electroweak.GaugeInvariance"
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

# TauLib.BookIV.Electroweak.GaugeInvariance


EM principal bundle, local trivializations, transition functions,
sections, connections, covariant derivatives, parallel transport,
field strength, Aharonov-Bohm phase, and EM loop space.

## Registry Cross-References


- [IV.D85] EM Principal Bundle — `EMPrincipalBundle`

- [IV.D86] Local Trivialization — `LocalTrivialization`

- [IV.D87] Transition Function — `TransitionFunction`

- [IV.D88] Section of P_EM — `BundleSection`

- [IV.D89] EM Connection — `EMConnection`

- [IV.D90] Covariant Derivative — `CovariantDerivative`

- [IV.D91] Parallel Transport — `ParallelTransport`

- [IV.D92] Field Strength Tensor — `FieldStrengthTensor`

- [IV.D93] Aharonov-Bohm Phase — `AharonovBohmPhase`

- [IV.D94] EM Loop Space — `EMLoopSpace`

- [IV.D95] Sigma-Equivariant Functional — `SigmaEquivariant`

- [IV.T37] Gauge Invariance — `gauge_invariance`

- [IV.T38] Field Strength Gauge-Invariant — `field_strength_invariant`

- [IV.P37] First Chern Class — `chern_class_classifier`

- [IV.P38] Parallel Transport Covariance — `parallel_transport_covariance`

- [IV.P39] F from Commutator — `f_from_commutator`


## Mathematical Content


### EM Principal Bundle


The electromagnetic field on τ³ is a U(1) principal bundle P_EM → T².
The structure group U(1) acts on fibers by phase rotation.

### Gauge Invariance


Gauge invariance is NOT an extra postulate: it is the structural theorem
that the physics on τ³ is independent of the choice of local trivialization.
The connection A_μ transforms as A_μ → A_μ + ∂_μΛ under gauge,
but the curvature F_μν = ∂_μA_ν − ∂_νA_μ is gauge-invariant.

### Aharonov-Bohm Phase


The AB phase Φ_AB = exp(ie/ℏ ∮ A·dl) is the holonomy of the EM connection.
It is physically observable (interference experiments) even when F = 0 locally.

## Ground Truth Sources


- Chapter 27 of Book IV (2nd Edition)


---

### `Tau.BookIV.Electroweak.EMPrincipalBundle`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L61-L76)
**structure
Tau.BookIV.Electroweak.EMPrincipalBundle :Type**


[IV.D85] The EM principal bundle P_EM → T² with structure group U(1).
The B-sector gauge field lives on this bundle.

- base_dim : ℕ
Base space dimension (T² = 2).

- base_eq : self.base_dim = 2
- group_dim : ℕ
Structure group dimension (U(1) = 1).

- group_eq : self.group_dim = 1
- total_dim : ℕ
Total space dimension = base + group.

- total_eq : self.total_dim = self.base_dim + self.group_dim
- sector : BookIII.Sectors.Sector
The sector: must be B (EM).

- sector_eq : self.sector = BookIII.Sectors.Sector.B
Instances For

---

### `Tau.BookIV.Electroweak.instReprEMPrincipalBundle`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L76-L76)
**instance
Tau.BookIV.Electroweak.instReprEMPrincipalBundle :Repr EMPrincipalBundle**

Equations
- Tau.BookIV.Electroweak.instReprEMPrincipalBundle = { reprPrec := Tau.BookIV.Electroweak.instReprEMPrincipalBundle.repr }

---

### `Tau.BookIV.Electroweak.instReprEMPrincipalBundle.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L76-L76)
**def
Tau.BookIV.Electroweak.instReprEMPrincipalBundle.repr :EMPrincipalBundle → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.em_bundle`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L78-L87)
**def
Tau.BookIV.Electroweak.em_bundle :EMPrincipalBundle**


Canonical EM principal bundle.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.LocalTrivialization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L93-L100)
**structure
Tau.BookIV.Electroweak.LocalTrivialization :Type**


[IV.D86] A local trivialization of P_EM over a patch U_i ⊂ T².
On each patch, P_EM|_{U_i} ≅ U_i × U(1).

- patch_index : ℕ
Patch index.

- smooth : Bool
The trivialization is smooth.

Instances For

---

### `Tau.BookIV.Electroweak.instReprLocalTrivialization.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L100-L100)
**def
Tau.BookIV.Electroweak.instReprLocalTrivialization.repr :LocalTrivialization → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprLocalTrivialization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L100-L100)
**instance
Tau.BookIV.Electroweak.instReprLocalTrivialization :Repr LocalTrivialization**

Equations
- Tau.BookIV.Electroweak.instReprLocalTrivialization = { reprPrec := Tau.BookIV.Electroweak.instReprLocalTrivialization.repr }

---

### `Tau.BookIV.Electroweak.TransitionFunction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L106-L118)
**structure
Tau.BookIV.Electroweak.TransitionFunction :Type**


[IV.D87] Transition function g_{UV}: U ∩ V → U(1).
On overlaps, relates two local trivializations.
The cocycle condition g_{UV}·g_{VW} = g_{UW} holds.

- patch_u : ℕ
Source patch index.

- patch_v : ℕ
Target patch index.

- winding : ℤ
Winding number of the transition function (integer for T²).

- cocycle : Bool
Satisfies cocycle condition.

Instances For

---

### `Tau.BookIV.Electroweak.instReprTransitionFunction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L118-L118)
**instance
Tau.BookIV.Electroweak.instReprTransitionFunction :Repr TransitionFunction**

Equations
- Tau.BookIV.Electroweak.instReprTransitionFunction = { reprPrec := Tau.BookIV.Electroweak.instReprTransitionFunction.repr }

---

### `Tau.BookIV.Electroweak.instReprTransitionFunction.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L118-L118)
**def
Tau.BookIV.Electroweak.instReprTransitionFunction.repr :TransitionFunction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.TransitionFunction.compose`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L120-L125)
**def
Tau.BookIV.Electroweak.TransitionFunction.compose
(g₁ g₂ : TransitionFunction)

(_h : g₁.patch_v = g₂.patch_u)
 :TransitionFunction**


Cocycle composition: transition function winding numbers add.
Equations
- g₁.compose g₂ _h = { patch_u := g₁.patch_u, patch_v := g₂.patch_v, winding := g₁.winding + g₂.winding }
Instances For

---

### `Tau.BookIV.Electroweak.BundleSection`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L131-L138)
**structure
Tau.BookIV.Electroweak.BundleSection :Type**


[IV.D88] A section of P_EM: a smooth map s: T² → P_EM with
π ∘ s = id. Existence of a global section iff bundle is trivial.

- is_global : Bool
Whether the section is global (defined on all of T²).

- chern_is_zero : Bool
Chern class is zero (required for global section to exist).

Instances For

---

### `Tau.BookIV.Electroweak.instReprBundleSection.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L138-L138)
**def
Tau.BookIV.Electroweak.instReprBundleSection.repr :BundleSection → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprBundleSection`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L138-L138)
**instance
Tau.BookIV.Electroweak.instReprBundleSection :Repr BundleSection**

Equations
- Tau.BookIV.Electroweak.instReprBundleSection = { reprPrec := Tau.BookIV.Electroweak.instReprBundleSection.repr }

---

### `Tau.BookIV.Electroweak.global_section_chern`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L140-L143)
**theorem
Tau.BookIV.Electroweak.global_section_chern
(s : BundleSection)

(hg : s.is_global = true)

(hc : s.chern_is_zero = true)
 :s.is_global = true ∧ s.chern_is_zero = true**


Global section requires zero Chern class.

---

### `Tau.BookIV.Electroweak.EMConnection`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L149-L158)
**structure
Tau.BookIV.Electroweak.EMConnection :Type**


[IV.D89] Connection A on P_EM: a Lie-algebra-valued 1-form on T².
In local coordinates A = A_μ dx^μ where A_μ: T² → ℝ.
Under gauge transformation: A_μ → A_μ + ∂_μΛ.

- components : ℕ
Number of spacetime components.

- comp_eq : self.components = 4
- smooth : Bool
The connection is smooth.

Instances For

---

### `Tau.BookIV.Electroweak.instReprEMConnection.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L158-L158)
**def
Tau.BookIV.Electroweak.instReprEMConnection.repr :EMConnection → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprEMConnection`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L158-L158)
**instance
Tau.BookIV.Electroweak.instReprEMConnection :Repr EMConnection**

Equations
- Tau.BookIV.Electroweak.instReprEMConnection = { reprPrec := Tau.BookIV.Electroweak.instReprEMConnection.repr }

---

### `Tau.BookIV.Electroweak.em_connection`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L160-L163)
**def
Tau.BookIV.Electroweak.em_connection :EMConnection**


Canonical EM connection on T² (4 components in spacetime).
Equations
- Tau.BookIV.Electroweak.em_connection = { components := 4, comp_eq := Tau.BookIV.Electroweak.em_connection._proof_1 }
Instances For

---

### `Tau.BookIV.Electroweak.CovariantDerivative`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L169-L177)
**structure
Tau.BookIV.Electroweak.CovariantDerivative :Type**


[IV.D90] Covariant derivative D_μ = ∂_μ + ieA_μ on charged fields.
The minimal coupling prescription of the B-sector connection.

- charge_units : ℤ
Coupling constant (charge in units of e).

- connection_components : ℕ
The connection used.

- conn_eq : self.connection_components = 4
Instances For

---

### `Tau.BookIV.Electroweak.instReprCovariantDerivative.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L177-L177)
**def
Tau.BookIV.Electroweak.instReprCovariantDerivative.repr :CovariantDerivative → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprCovariantDerivative`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L177-L177)
**instance
Tau.BookIV.Electroweak.instReprCovariantDerivative :Repr CovariantDerivative**

Equations
- Tau.BookIV.Electroweak.instReprCovariantDerivative = { reprPrec := Tau.BookIV.Electroweak.instReprCovariantDerivative.repr }

---

### `Tau.BookIV.Electroweak.ParallelTransport`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L183-L192)
**structure
Tau.BookIV.Electroweak.ParallelTransport :Type**


[IV.D91] Parallel transport along a path γ in T²:
the solution to D_γ ψ = 0. For U(1), this is a phase rotation.

- is_loop : Bool
Whether the path is closed (loop).

- phase_numer : ℤ
Phase accumulated (as scaled integer, in units of 2π/N).

- phase_denom : ℕ
- denom_pos : self.phase_denom > 0
Instances For

---

### `Tau.BookIV.Electroweak.instReprParallelTransport`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L192-L192)
**instance
Tau.BookIV.Electroweak.instReprParallelTransport :Repr ParallelTransport**

Equations
- Tau.BookIV.Electroweak.instReprParallelTransport = { reprPrec := Tau.BookIV.Electroweak.instReprParallelTransport.repr }

---

### `Tau.BookIV.Electroweak.instReprParallelTransport.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L192-L192)
**def
Tau.BookIV.Electroweak.instReprParallelTransport.repr :ParallelTransport → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.ParallelTransport.compose`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L194-L199)
**def
Tau.BookIV.Electroweak.ParallelTransport.compose
(t₁ t₂ : ParallelTransport)
 :ParallelTransport**


Parallel transport composition.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.FieldStrengthTensor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L205-L217)
**structure
Tau.BookIV.Electroweak.FieldStrengthTensor :Type**


[IV.D92] Field strength tensor F_μν = ∂_μA_ν − ∂_νA_μ (curvature).
Antisymmetric 2-form on spacetime; encodes E and B fields.
Independent components in 4D: 6 = 4·3/2.

- spacetime_dim : ℕ
Spacetime dimension.

- dim_eq : self.spacetime_dim = 4
- independent_components : ℕ
Number of independent components = d(d-1)/2.

- comp_eq : self.independent_components = 6
- gauge_invariant : Bool
Gauge-invariant (structural property).

Instances For

---

### `Tau.BookIV.Electroweak.instReprFieldStrengthTensor.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L217-L217)
**def
Tau.BookIV.Electroweak.instReprFieldStrengthTensor.repr :FieldStrengthTensor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprFieldStrengthTensor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L217-L217)
**instance
Tau.BookIV.Electroweak.instReprFieldStrengthTensor :Repr FieldStrengthTensor**

Equations
- Tau.BookIV.Electroweak.instReprFieldStrengthTensor = { reprPrec := Tau.BookIV.Electroweak.instReprFieldStrengthTensor.repr }

---

### `Tau.BookIV.Electroweak.field_strength`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L219-L224)
**def
Tau.BookIV.Electroweak.field_strength :FieldStrengthTensor**


Canonical field strength tensor in 4D.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.AharonovBohmPhase`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L230-L241)
**structure
Tau.BookIV.Electroweak.AharonovBohmPhase :Type**


[IV.D93] Aharonov-Bohm phase: Φ_AB = exp(ie/ℏ ∮ A·dl).
Observable even when F=0 locally; encodes global topology.
The phase is the holonomy of the EM connection around a loop.

- flux_numer : ℤ
Enclosed magnetic flux (scaled).

- flux_denom : ℕ
- denom_pos : self.flux_denom > 0
- is_loop : Bool
The path is a closed loop.

- loop_true : self.is_loop = true
Instances For

---

### `Tau.BookIV.Electroweak.instReprAharonovBohmPhase.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L241-L241)
**def
Tau.BookIV.Electroweak.instReprAharonovBohmPhase.repr :AharonovBohmPhase → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprAharonovBohmPhase`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L241-L241)
**instance
Tau.BookIV.Electroweak.instReprAharonovBohmPhase :Repr AharonovBohmPhase**

Equations
- Tau.BookIV.Electroweak.instReprAharonovBohmPhase = { reprPrec := Tau.BookIV.Electroweak.instReprAharonovBohmPhase.repr }

---

### `Tau.BookIV.Electroweak.EMLoopSpace`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L247-L256)
**structure
Tau.BookIV.Electroweak.EMLoopSpace :Type**


[IV.D94] EM loop space: the space of closed loops on T² equipped
with the holonomy map. Loops compose by concatenation, giving
a group structure on holonomies.

- base_dim : ℕ
Base space (T²).

- base_eq : self.base_dim = 2
- holonomy_multiplicative : Bool
The holonomy is multiplicative under loop composition.

Instances For

---

### `Tau.BookIV.Electroweak.instReprEMLoopSpace`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L256-L256)
**instance
Tau.BookIV.Electroweak.instReprEMLoopSpace :Repr EMLoopSpace**

Equations
- Tau.BookIV.Electroweak.instReprEMLoopSpace = { reprPrec := Tau.BookIV.Electroweak.instReprEMLoopSpace.repr }

---

### `Tau.BookIV.Electroweak.instReprEMLoopSpace.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L256-L256)
**def
Tau.BookIV.Electroweak.instReprEMLoopSpace.repr :EMLoopSpace → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.SigmaEquivariant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L262-L271)
**structure
Tau.BookIV.Electroweak.SigmaEquivariant :Type**


[IV.D95] A σ-equivariant functional on P_EM: a functional that
commutes with the U(1) action (σ). Physical observables must
be σ-equivariant; this is the structural content of gauge invariance.

- equivariant : Bool
The functional commutes with U(1) action.

- is_observable : Bool
Observable iff equivariant.

- obs_eq : self.is_observable = self.equivariant
Instances For

---

### `Tau.BookIV.Electroweak.instReprSigmaEquivariant.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L271-L271)
**def
Tau.BookIV.Electroweak.instReprSigmaEquivariant.repr :SigmaEquivariant → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprSigmaEquivariant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L271-L271)
**instance
Tau.BookIV.Electroweak.instReprSigmaEquivariant :Repr SigmaEquivariant**

Equations
- Tau.BookIV.Electroweak.instReprSigmaEquivariant = { reprPrec := Tau.BookIV.Electroweak.instReprSigmaEquivariant.repr }

---

### `Tau.BookIV.Electroweak.gauge_invariance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L277-L281)
**theorem
Tau.BookIV.Electroweak.gauge_invariance
(s : SigmaEquivariant)

(h : s.equivariant = true)
 :s.is_observable = true**


[IV.T37] Gauge invariance as structural theorem: physics on τ³
is independent of the choice of local trivialization.
All physical observables are σ-equivariant functionals.

---

### `Tau.BookIV.Electroweak.field_strength_invariant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L287-L289)
**theorem
Tau.BookIV.Electroweak.field_strength_invariant :field_strength.gauge_invariant = true**


[IV.T38] F_μν is gauge-invariant: since F = dA and d² = 0,
the substitution A → A + dΛ gives F → F + d²Λ = F.

---

### `Tau.BookIV.Electroweak.ChernClassifier`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L295-L302)
**structure
Tau.BookIV.Electroweak.ChernClassifier :Type**


[IV.P37] P_EM is classified by its first Chern class c₁ ∈ ℤ.
The Chern number is the total magnetic flux through T².

- chern_class : ℤ
First Chern class (integer).

- classifies_bundle : Bool
Chern class determines bundle up to isomorphism.

Instances For

---

### `Tau.BookIV.Electroweak.instReprChernClassifier`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L302-L302)
**instance
Tau.BookIV.Electroweak.instReprChernClassifier :Repr ChernClassifier**

Equations
- Tau.BookIV.Electroweak.instReprChernClassifier = { reprPrec := Tau.BookIV.Electroweak.instReprChernClassifier.repr }

---

### `Tau.BookIV.Electroweak.instReprChernClassifier.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L302-L302)
**def
Tau.BookIV.Electroweak.instReprChernClassifier.repr :ChernClassifier → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.chern_class_classifier`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L304-L306)
**theorem
Tau.BookIV.Electroweak.chern_class_classifier
(c : ChernClassifier)

(h : c.classifies_bundle = true)
 :c.classifies_bundle = true**


---

### `Tau.BookIV.Electroweak.TransportCovariance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L312-L320)
**structure
Tau.BookIV.Electroweak.TransportCovariance :Type**


[IV.P38] Parallel transport is gauge-covariant for open paths and
gauge-invariant for closed paths (loops). The holonomy around a
loop is a physical observable (the AB phase).

- open_covariant : Bool
Open-path transport is gauge-covariant.

- closed_invariant : Bool
Closed-path (loop) holonomy is gauge-invariant.

Instances For

---

### `Tau.BookIV.Electroweak.instReprTransportCovariance.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L320-L320)
**def
Tau.BookIV.Electroweak.instReprTransportCovariance.repr :TransportCovariance → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprTransportCovariance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L320-L320)
**instance
Tau.BookIV.Electroweak.instReprTransportCovariance :Repr TransportCovariance**

Equations
- Tau.BookIV.Electroweak.instReprTransportCovariance = { reprPrec := Tau.BookIV.Electroweak.instReprTransportCovariance.repr }

---

### `Tau.BookIV.Electroweak.parallel_transport_covariance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L322-L324)
**theorem
Tau.BookIV.Electroweak.parallel_transport_covariance
(tc : TransportCovariance)

(h : tc.closed_invariant = true)
 :tc.closed_invariant = true**


---

### `Tau.BookIV.Electroweak.FFromCommutator`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L330-L337)
**structure
Tau.BookIV.Electroweak.FFromCommutator :Type**


[IV.P39] F_μν arises from the commutator of covariant derivatives:
[D_μ, D_ν] = ieF_μν. This is the geometric definition of curvature.

- is_commutator : Bool
F is the commutator of D.

- factor_is_ie : Bool
The factor is ie.

Instances For

---

### `Tau.BookIV.Electroweak.instReprFFromCommutator`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L337-L337)
**instance
Tau.BookIV.Electroweak.instReprFFromCommutator :Repr FFromCommutator**

Equations
- Tau.BookIV.Electroweak.instReprFFromCommutator = { reprPrec := Tau.BookIV.Electroweak.instReprFFromCommutator.repr }

---

### `Tau.BookIV.Electroweak.instReprFFromCommutator.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L337-L337)
**def
Tau.BookIV.Electroweak.instReprFFromCommutator.repr :FFromCommutator → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.f_from_commutator`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L339-L341)
**theorem
Tau.BookIV.Electroweak.f_from_commutator
(fc : FFromCommutator)

(h1 : fc.is_commutator = true)

(h2 : fc.factor_is_ie = true)
 :fc.is_commutator = true ∧ fc.factor_is_ie = true**


---

### `Tau.BookIV.Electroweak.example_triv`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L353-L353)
**def
Tau.BookIV.Electroweak.example_triv :LocalTrivialization**

Equations
- Tau.BookIV.Electroweak.example_triv = { patch_index := 0 }
Instances For

---

### `Tau.BookIV.Electroweak.example_transport`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L355-L356)
**def
Tau.BookIV.Electroweak.example_transport :ParallelTransport**

Equations
- Tau.BookIV.Electroweak.example_transport = { is_loop := true, phase_numer := 1, phase_denom := 4,
 denom_pos := Tau.BookIV.Electroweak.example_transport._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.example_ab`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/GaugeInvariance.lean#L358-L359)
**def
Tau.BookIV.Electroweak.example_ab :AharonovBohmPhase**

Equations
- Tau.BookIV.Electroweak.example_ab = { flux_numer := 1, flux_denom := 2, denom_pos := Tau.BookIV.Electroweak.example_ab._proof_2, is_loop := true,
 loop_true := ⋯ }
Instances For
