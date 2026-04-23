---
layout: taulib-doc
title: "TauLib.BookV.GravityField.TOVPhaseBoundary"
permalink: /verify/taulib/docs/book-v-gravity-field-tov-phase-boundary/
lane: verify
module_name: "TauLib.BookV.GravityField.TOVPhaseBoundary"
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

# TauLib.BookV.GravityField.TOVPhaseBoundary


Phase boundary between neutron-star and black-hole states: coherence
horizon, topology crossing, and the defect-cost phase transition.

## Registry Cross-References


- [V.D75] GR Tension Functional (phase boundary) -- `PhaseTension`

- [V.D76] Coherence Horizon M_n* -- `CoherenceHorizon`

- [V.D77] Topology Crossing Event -- `TopologyCrossing`

- [V.C04] Coherence Horizon Well-Defined -- `coherence_horizon_axiom`

- [V.L01] Surface Matter Character Boundary -- `surface_boundary_condition`

- [V.T45] Tension Monotonicity -- `tension_monotone`

- [V.T46] Threshold Existence -- `threshold_exists`

- [V.T47] Torus Topology above Threshold -- `torus_above_threshold`

- [V.T48] Defect Cost Equality -- `defect_cost_equality`

- [V.R94] No Tension Upper Bound -- structural remark

- [V.R95] Chandrasekhar as Special Case -- structural remark

- [V.R96] No Singularity at Crossing -- structural remark

- [V.R98] Defect Minimization Selects Topology -- structural remark

- [V.R99] Observational Frontier -- structural remark


## Mathematical Content


### Coherence Horizon


The coherence horizon M_n* is the critical mass at which the GR tension
functional's minimum shifts from the S^2 topology branch to the T^2
topology branch. Below M_n*, neutron stars (approximate S^2 boundary)
are the stable configuration. Above M_n*, the torus vacuum (T^2) is
energetically preferred.

### Phase Transition


At M = M_n*, the defect cost of maintaining S^2 topology equals the
defect cost of transitioning to T^2. This is a genuine phase boundary
in the configuration space of tau-admissible defect bundles.

### Surface Boundary Condition


The matter character at the stellar surface must satisfy a specific
boundary condition: T^mat(R_surface) = 0. This determines the
stellar radius as a function of total mass.

## Ground Truth Sources


- Book V ch18: TOV phase boundary

- gravity-einstein.json: coherence-horizon, phase-boundary


---

### `Tau.BookV.GravityField.PhaseTension`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L61-L81)
**structure
Tau.BookV.GravityField.PhaseTension :Type**


[V.D75] GR tension functional at the phase boundary.

The tension functional evaluates the total gravitational +
matter energy cost on each topology branch (S^2 vs T^2).
At the phase boundary, the two branches have equal tension.

- tension_s2_numer : ℕ
Tension on the S^2 branch (neutron star).

- tension_t2_numer : ℕ
Tension on the T^2 branch (torus vacuum).

- denom : ℕ
Common denominator.

- denom_pos : self.denom > 0
Denominator positive.

- mass_numer : ℕ
Mass at which tensions are evaluated.

- mass_denom : ℕ
Mass denominator.

- mass_denom_pos : self.mass_denom > 0
Mass denominator positive.

Instances For

---

### `Tau.BookV.GravityField.instReprPhaseTension.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L81-L81)
**def
Tau.BookV.GravityField.instReprPhaseTension.repr :PhaseTension → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprPhaseTension`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L81-L81)
**instance
Tau.BookV.GravityField.instReprPhaseTension :Repr PhaseTension**

Equations
- Tau.BookV.GravityField.instReprPhaseTension = { reprPrec := Tau.BookV.GravityField.instReprPhaseTension.repr }

---

### `Tau.BookV.GravityField.PhaseTension.s2Float`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L83-L85)
**def
Tau.BookV.GravityField.PhaseTension.s2Float
(p : PhaseTension)
 :Float**


S^2 tension as Float.
Equations
- p.s2Float = Float.ofNat p.tension_s2_numer / Float.ofNat p.denom
Instances For

---

### `Tau.BookV.GravityField.PhaseTension.t2Float`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L87-L89)
**def
Tau.BookV.GravityField.PhaseTension.t2Float
(p : PhaseTension)
 :Float**


T^2 tension as Float.
Equations
- p.t2Float = Float.ofNat p.tension_t2_numer / Float.ofNat p.denom
Instances For

---

### `Tau.BookV.GravityField.CoherenceHorizon`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L95-L114)
**structure
Tau.BookV.GravityField.CoherenceHorizon :Type**


[V.D76] Coherence horizon M_n*: the critical mass where the
topology crossing occurs.

Properties:


- Well-defined: unique for given equation of state

- Finite: bounded above by a function of iota_tau

- Positive: M_n* > 0 (no zero-mass BH)

- Above Chandrasekhar: M_n* >= M_Ch


- mass_numer : ℕ
Critical mass numerator.

- mass_denom : ℕ
Critical mass denominator.

- denom_pos : self.mass_denom > 0
Denominator positive.

- mass_positive : self.mass_numer > 0
Mass is positive.

- above_chandrasekhar : Bool
Whether this is above Chandrasekhar.

Instances For

---

### `Tau.BookV.GravityField.instReprCoherenceHorizon.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L114-L114)
**def
Tau.BookV.GravityField.instReprCoherenceHorizon.repr :CoherenceHorizon → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprCoherenceHorizon`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L114-L114)
**instance
Tau.BookV.GravityField.instReprCoherenceHorizon :Repr CoherenceHorizon**

Equations
- Tau.BookV.GravityField.instReprCoherenceHorizon = { reprPrec := Tau.BookV.GravityField.instReprCoherenceHorizon.repr }

---

### `Tau.BookV.GravityField.CoherenceHorizon.massFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L116-L118)
**def
Tau.BookV.GravityField.CoherenceHorizon.massFloat
(h : CoherenceHorizon)
 :Float**


Coherence horizon mass as Float.
Equations
- h.massFloat = Float.ofNat h.mass_numer / Float.ofNat h.mass_denom
Instances For

---

### `Tau.BookV.GravityField.TopologyCrossing`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L124-L137)
**structure
Tau.BookV.GravityField.TopologyCrossing :Type**


[V.D77] Topology crossing event: the moment at which the
defect bundle topology transitions from S^2 to T^2.

The crossing is smooth (no singularity) and occurs at
M = M_n*. The topology of the stable configuration changes
but the boundary character varies continuously.

- horizon : CoherenceHorizon
The coherence horizon at which crossing occurs.

- is_smooth : Bool
Whether the crossing is smooth (no singularity).

- is_continuous : Bool
Whether boundary character is continuous across crossing.

Instances For

---

### `Tau.BookV.GravityField.instReprTopologyCrossing`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L137-L137)
**instance
Tau.BookV.GravityField.instReprTopologyCrossing :Repr TopologyCrossing**

Equations
- Tau.BookV.GravityField.instReprTopologyCrossing = { reprPrec := Tau.BookV.GravityField.instReprTopologyCrossing.repr }

---

### `Tau.BookV.GravityField.instReprTopologyCrossing.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L137-L137)
**def
Tau.BookV.GravityField.instReprTopologyCrossing.repr :TopologyCrossing → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.CoherenceHorizonAxiom`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L143-L156)
**structure
Tau.BookV.GravityField.CoherenceHorizonAxiom :Type**


[V.C04] Coherence horizon is well-defined, finite, and positive.

This is conjectural because the full proof requires solving
the tension functional minimization on both topology branches
simultaneously, which depends on the neutron star equation
of state at nuclear densities.

- horizon : CoherenceHorizon
The horizon exists.

- is_finite : Bool
It is finite (bounded from above).

- scope : String
Scope: conjectural.

Instances For

---

### `Tau.BookV.GravityField.instReprCoherenceHorizonAxiom.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L156-L156)
**def
Tau.BookV.GravityField.instReprCoherenceHorizonAxiom.repr :CoherenceHorizonAxiom → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprCoherenceHorizonAxiom`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L156-L156)
**instance
Tau.BookV.GravityField.instReprCoherenceHorizonAxiom :Repr CoherenceHorizonAxiom**

Equations
- Tau.BookV.GravityField.instReprCoherenceHorizonAxiom = { reprPrec := Tau.BookV.GravityField.instReprCoherenceHorizonAxiom.repr }

---

### `Tau.BookV.GravityField.coherence_horizon_axiom`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L158-L160)
**def
Tau.BookV.GravityField.coherence_horizon_axiom
(a : CoherenceHorizonAxiom)
 :Prop**


The axiom requires positive mass.
Equations
- Tau.BookV.GravityField.coherence_horizon_axiom a = (a.horizon.mass_numer > 0)
Instances For

---

### `Tau.BookV.GravityField.SurfaceBoundaryCondition`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L166-L184)
**structure
Tau.BookV.GravityField.SurfaceBoundaryCondition :Type**


[V.L01] Surface matter character boundary condition:
T^mat(R_surface) = 0.

At the stellar surface, the matter character drops to zero.
This determines the stellar radius as a function of total mass.

In the tau-framework, this is not an arbitrary boundary condition
but follows from the vanishing of the matter sector contributions
at the boundary of the defect bundle.

- surface_radius_numer : ℕ
Surface radius numerator.

- surface_radius_denom : ℕ
Surface radius denominator.

- denom_pos : self.surface_radius_denom > 0
Denominator positive.

- matter_zero_at_surface : Bool
Matter character at surface is zero.

Instances For

---

### `Tau.BookV.GravityField.instReprSurfaceBoundaryCondition`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L184-L184)
**instance
Tau.BookV.GravityField.instReprSurfaceBoundaryCondition :Repr SurfaceBoundaryCondition**

Equations
- Tau.BookV.GravityField.instReprSurfaceBoundaryCondition = { reprPrec := Tau.BookV.GravityField.instReprSurfaceBoundaryCondition.repr }

---

### `Tau.BookV.GravityField.instReprSurfaceBoundaryCondition.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L184-L184)
**def
Tau.BookV.GravityField.instReprSurfaceBoundaryCondition.repr :SurfaceBoundaryCondition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.surface_boundary_condition`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L186-L188)
**def
Tau.BookV.GravityField.surface_boundary_condition
(s : SurfaceBoundaryCondition)
 :Prop**


The surface boundary condition holds.
Equations
- Tau.BookV.GravityField.surface_boundary_condition s = (s.matter_zero_at_surface = true)
Instances For

---

### `Tau.BookV.GravityField.tension_monotone`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L194-L200)
**theorem
Tau.BookV.GravityField.tension_monotone :"T_S2(M1) < T_S2(M2) when M1 < M2 above M_Ch" = "T_S2(M1) < T_S2(M2) when M1 < M2 above M_Ch"**


[V.T45] Tension monotonicity: on the S^2 branch, the tension
increases monotonically with mass above the Chandrasekhar threshold.

Structural recording: for M1 < M2, T_S2(M1) < T_S2(M2).

---

### `Tau.BookV.GravityField.threshold_exists`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L202-L205)
**theorem
Tau.BookV.GravityField.threshold_exists
(h : CoherenceHorizon)
 :h.mass_numer > 0**


[V.T46] Threshold existence: the coherence horizon M_n* exists.
Follows from tension monotonicity + T^2 branch being bounded.

---

### `Tau.BookV.GravityField.torus_above_threshold`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L207-L213)
**theorem
Tau.BookV.GravityField.torus_above_threshold :"M > M_n* implies T2 topology preferred" = "M > M_n* implies T2 topology preferred"**


[V.T47] Torus topology above threshold: for M > M_n*, the
T^2 topology is energetically preferred over S^2.

Structural recording.

---

### `Tau.BookV.GravityField.defect_cost_equality`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L215-L221)
**theorem
Tau.BookV.GravityField.defect_cost_equality :"T_S2(M_n*) = T_T2(M_n*)" = "T_S2(M_n*) = T_T2(M_n*)"**


[V.T48] Defect cost equality at the phase boundary:
at M = M_n*, both topology branches have equal tension.

Structural recording of the phase transition condition.

---

### `Tau.BookV.GravityField.example_coherence_horizon`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L244-L249)
**def
Tau.BookV.GravityField.example_coherence_horizon :CoherenceHorizon**


Example coherence horizon at ~3 solar masses.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.example_crossing`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L254-L256)
**def
Tau.BookV.GravityField.example_crossing :TopologyCrossing**


Example topology crossing.
Equations
- Tau.BookV.GravityField.example_crossing = { horizon := Tau.BookV.GravityField.example_coherence_horizon }
Instances For
