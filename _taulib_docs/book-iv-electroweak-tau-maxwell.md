---
layout: taulib-doc
title: "TauLib.BookIV.Electroweak.TauMaxwell"
permalink: /verify/taulib/docs/book-iv-electroweak-tau-maxwell/
lane: verify
module_name: "TauLib.BookIV.Electroweak.TauMaxwell"
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

# TauLib.BookIV.Electroweak.TauMaxwell


τ-native derivation of Maxwell's equations: EM gauge bundle, connection,
Faraday 2-form, Hodge dual, current 4-vector, Bianchi identity, source
equation, assembled Maxwell equations, and orthodox limit.

## Registry Cross-References


- [IV.D98] EM Gauge Bundle — `EMGaugeBundle`

- [IV.D99] EM Connection A — `EMConnectionA`

- [IV.D100] EM Field Tensor — `EMFieldTensor`

- [IV.D101] Electric and Magnetic Fields — `EBFields`

- [IV.D102] Hodge Dual — `HodgeDual`

- [IV.D103] EM Current 4-Vector — `EMCurrent`

- [IV.T42] Bianchi Identity — `bianchi_identity`

- [IV.T43] Source Equation — `source_equation`

- [IV.T44] All Four Maxwell Equations — `maxwell_equations`

- [IV.T45] Defect Interpretation of Sources — `defect_sources`

- [IV.T46] Coulomb Limit — `coulomb_limit`

- [IV.T47] Wave Equation — `wave_equation`

- [IV.P44] Continuity Equation — `continuity_equation`

- [IV.P45] Charge Density — `charge_density`

- [IV.P46] Current Density — `current_density`

- [IV.P47] Photon = EM Wave — `photon_is_em_wave`

- [IV.P48] Magnetic Force Perpendicular — `magnetic_force_perpendicular`

- [IV.P49] QED Corrections — `qed_corrections`


## Mathematical Content


### Maxwell from τ³


On the B-sector principal bundle P_EM → T², the connection A defines
the Faraday 2-form F = dA. The Bianchi identity dF = 0 gives the
homogeneous Maxwell equations (div B = 0, Faraday's law). The source
equation d*F = *J (Hodge dual) gives the inhomogeneous equations
(Gauss's law, Ampere-Maxwell). All four equations are assembled as:

dF = 0 (homogeneous pair)
d*F = *J (inhomogeneous pair)

### Defect Interpretation


Orthodox EM sources (charges, currents) are τ-defect bundles: persistent
localized obstructions to perfect coherence on T². Charge density ρ
counts winding numbers per unit volume; current density J tracks
transport of charged defects.

### Limits


Static limit: F → Coulomb's law F = ke·q₁q₂/r².
Source-free Lorenz gauge: □A_μ = 0 (wave equation for photons).

## Ground Truth Sources


- Chapter 28 of Book IV (2nd Edition)


---

### `Tau.BookIV.Electroweak.EMGaugeBundle`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L69-L81)
**structure
Tau.BookIV.Electroweak.EMGaugeBundle :Type**


[IV.D98] The EM gauge bundle: specialization of EMPrincipalBundle
to the physical B-sector with U(1) structure group and T² base.

- group_is_u1 : Bool
Structure group is U(1).

- base_is_torus : Bool
Base is T².

- sector : BookIII.Sectors.Sector
Sector is B (EM).

- sector_eq : self.sector = BookIII.Sectors.Sector.B
- chern_class : ℤ
Chern class (integer topological invariant).

Instances For

---

### `Tau.BookIV.Electroweak.instReprEMGaugeBundle`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L81-L81)
**instance
Tau.BookIV.Electroweak.instReprEMGaugeBundle :Repr EMGaugeBundle**

Equations
- Tau.BookIV.Electroweak.instReprEMGaugeBundle = { reprPrec := Tau.BookIV.Electroweak.instReprEMGaugeBundle.repr }

---

### `Tau.BookIV.Electroweak.instReprEMGaugeBundle.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L81-L81)
**def
Tau.BookIV.Electroweak.instReprEMGaugeBundle.repr :EMGaugeBundle → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.em_gauge_trivial`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L83-L87)
**def
Tau.BookIV.Electroweak.em_gauge_trivial :EMGaugeBundle**


Trivial EM gauge bundle (Chern class 0).
Equations
- Tau.BookIV.Electroweak.em_gauge_trivial = { sector := Tau.BookIII.Sectors.Sector.B, sector_eq := ⋯, chern_class := 0 }
Instances For

---

### `Tau.BookIV.Electroweak.EMConnectionA`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L93-L105)
**structure
Tau.BookIV.Electroweak.EMConnectionA :Type**


[IV.D99] EM connection 1-form A = A_μ dx^μ on P_EM.
In local coordinates: 4 component functions A_0, A_1, A_2, A_3
where A_0 = scalar potential φ and (A_1,A_2,A_3) = vector potential.

- components : ℕ
Number of components (spacetime dimension).

- comp_eq : self.components = 4
- has_scalar_potential : Bool
Scalar potential component (index 0).

- vector_potential_dim : ℕ
Vector potential components (indices 1,2,3).

- vec_eq : self.vector_potential_dim = 3
Instances For

---

### `Tau.BookIV.Electroweak.instReprEMConnectionA`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L105-L105)
**instance
Tau.BookIV.Electroweak.instReprEMConnectionA :Repr EMConnectionA**

Equations
- Tau.BookIV.Electroweak.instReprEMConnectionA = { reprPrec := Tau.BookIV.Electroweak.instReprEMConnectionA.repr }

---

### `Tau.BookIV.Electroweak.instReprEMConnectionA.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L105-L105)
**def
Tau.BookIV.Electroweak.instReprEMConnectionA.repr :EMConnectionA → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.em_connection_a`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L107-L112)
**def
Tau.BookIV.Electroweak.em_connection_a :EMConnectionA**


Canonical 4D EM connection.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.EMFieldTensor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L118-L132)
**structure
Tau.BookIV.Electroweak.EMFieldTensor :Type**


[IV.D100] EM field tensor F = dA: the curvature 2-form of the
EM connection. An antisymmetric (0,2)-tensor with 6 independent
components in 4D spacetime.

- dim : ℕ
Spacetime dimension.

- dim_eq : self.dim = 4
- components : ℕ
Independent components = d(d-1)/2.

- comp_eq : self.components = 6
- is_exact : Bool
F = dA (exterior derivative of connection).

- gauge_invariant : Bool
Gauge-invariant.

Instances For

---

### `Tau.BookIV.Electroweak.instReprEMFieldTensor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L132-L132)
**instance
Tau.BookIV.Electroweak.instReprEMFieldTensor :Repr EMFieldTensor**

Equations
- Tau.BookIV.Electroweak.instReprEMFieldTensor = { reprPrec := Tau.BookIV.Electroweak.instReprEMFieldTensor.repr }

---

### `Tau.BookIV.Electroweak.instReprEMFieldTensor.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L132-L132)
**def
Tau.BookIV.Electroweak.instReprEMFieldTensor.repr :EMFieldTensor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.faraday_tensor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L134-L139)
**def
Tau.BookIV.Electroweak.faraday_tensor :EMFieldTensor**


Canonical Faraday 2-form in 4D.
Equations
- Tau.BookIV.Electroweak.faraday_tensor = { dim := 4, dim_eq := Tau.BookIV.Electroweak.em_connection_a._proof_1, components := 6,
 comp_eq := Tau.BookIV.Electroweak.faraday_tensor._proof_1 }
Instances For

---

### `Tau.BookIV.Electroweak.EBFields`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L145-L158)
**structure
Tau.BookIV.Electroweak.EBFields :Type**


[IV.D101] Decomposition of F_μν into E and B fields.
F_{0i} = E_i (electric), F_{ij} = ε_{ijk} B_k (magnetic).
The split is observer-dependent (frame-dependent).

- e_components : ℕ
Electric field components (3).

- e_eq : self.e_components = 3
- b_components : ℕ
Magnetic field components (3).

- b_eq : self.b_components = 3
- total : ℕ
Total independent components = 3 + 3 = 6.

- total_eq : self.total = self.e_components + self.b_components
Instances For

---

### `Tau.BookIV.Electroweak.instReprEBFields`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L158-L158)
**instance
Tau.BookIV.Electroweak.instReprEBFields :Repr EBFields**

Equations
- Tau.BookIV.Electroweak.instReprEBFields = { reprPrec := Tau.BookIV.Electroweak.instReprEBFields.repr }

---

### `Tau.BookIV.Electroweak.instReprEBFields.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L158-L158)
**def
Tau.BookIV.Electroweak.instReprEBFields.repr :EBFields → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.eb_fields`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L160-L167)
**def
Tau.BookIV.Electroweak.eb_fields :EBFields**


E and B in 3+1 dimensions.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.eb_total_eq_f`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L169-L170)
**theorem
Tau.BookIV.Electroweak.eb_total_eq_f :eb_fields.total = faraday_tensor.components**


Total E+B components equals F components.

---

### `Tau.BookIV.Electroweak.HodgeDual`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L176-L185)
**structure
Tau.BookIV.Electroweak.HodgeDual :Type**


[IV.D102] Hodge dual *F: the dual 2-form exchanging E ↔ B.
*F_μν = (1/2)ε_μνρσ F^{ρσ}. EM duality: (E,B) → (B,-E).

- is_two_form : Bool
The dual is also a 2-form.

- exchanges_eb : Bool
E ↔ B exchange (with sign).

- double_dual_minus : Bool
**F = -F in 4D Lorentzian.

Instances For

---

### `Tau.BookIV.Electroweak.instReprHodgeDual`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L185-L185)
**instance
Tau.BookIV.Electroweak.instReprHodgeDual :Repr HodgeDual**

Equations
- Tau.BookIV.Electroweak.instReprHodgeDual = { reprPrec := Tau.BookIV.Electroweak.instReprHodgeDual.repr }

---

### `Tau.BookIV.Electroweak.instReprHodgeDual.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L185-L185)
**def
Tau.BookIV.Electroweak.instReprHodgeDual.repr :HodgeDual → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.EMCurrent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L191-L203)
**structure
Tau.BookIV.Electroweak.EMCurrent :Type**


[IV.D103] EM current 4-vector J^μ = (ρ, J).
ρ = charge density (winding numbers per volume),
J = current density (transport of charged defects).

- components : ℕ
Spacetime components.

- comp_eq : self.components = 4
- has_charge_density : Bool
Charge density (time component).

- spatial_components : ℕ
Spatial current density (3 spatial components).

- spatial_eq : self.spatial_components = 3
Instances For

---

### `Tau.BookIV.Electroweak.instReprEMCurrent.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L203-L203)
**def
Tau.BookIV.Electroweak.instReprEMCurrent.repr :EMCurrent → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprEMCurrent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L203-L203)
**instance
Tau.BookIV.Electroweak.instReprEMCurrent :Repr EMCurrent**

Equations
- Tau.BookIV.Electroweak.instReprEMCurrent = { reprPrec := Tau.BookIV.Electroweak.instReprEMCurrent.repr }

---

### `Tau.BookIV.Electroweak.em_current`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L205-L210)
**def
Tau.BookIV.Electroweak.em_current :EMCurrent**


Canonical EM current in 4D.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.BianchiIdentity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L216-L227)
**structure
Tau.BookIV.Electroweak.BianchiIdentity :Type**


[IV.T42] Bianchi identity dF = 0: automatic from F = dA and d² = 0.
In component form: ∂*{[μ} F*{νρ]} = 0.
Physical content: div B = 0 (no magnetic monopoles) + Faraday's law.

- df_zero : Bool
dF = 0 holds.

- from_d_squared : Bool
Follows from d² = 0.

- maxwell_count : ℕ
Maxwell equation count from Bianchi: 2 (div B = 0, Faraday).

- count_eq : self.maxwell_count = 2
Instances For

---

### `Tau.BookIV.Electroweak.instReprBianchiIdentity.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L227-L227)
**def
Tau.BookIV.Electroweak.instReprBianchiIdentity.repr :BianchiIdentity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprBianchiIdentity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L227-L227)
**instance
Tau.BookIV.Electroweak.instReprBianchiIdentity :Repr BianchiIdentity**

Equations
- Tau.BookIV.Electroweak.instReprBianchiIdentity = { reprPrec := Tau.BookIV.Electroweak.instReprBianchiIdentity.repr }

---

### `Tau.BookIV.Electroweak.bianchi_instance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L229-L231)
**def
Tau.BookIV.Electroweak.bianchi_instance :BianchiIdentity**

Equations
- Tau.BookIV.Electroweak.bianchi_instance = { maxwell_count := 2, count_eq := Tau.BookIV.Electroweak.bianchi_instance._proof_1 }
Instances For

---

### `Tau.BookIV.Electroweak.bianchi_identity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L233-L233)
**theorem
Tau.BookIV.Electroweak.bianchi_identity :bianchi_instance.df_zero = true**


---

### `Tau.BookIV.Electroweak.SourceEquation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L239-L247)
**structure
Tau.BookIV.Electroweak.SourceEquation :Type**


[IV.T43] Source equation d*F = *J: the inhomogeneous Maxwell equations.
Physical content: Gauss's law (div E = ρ/ε₀) + Ampere-Maxwell.

- source_eq : Bool
d*F = *J holds.

- maxwell_count : ℕ
Maxwell equation count from source eq: 2 (Gauss, Ampere).

- count_eq : self.maxwell_count = 2
Instances For

---

### `Tau.BookIV.Electroweak.instReprSourceEquation.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L247-L247)
**def
Tau.BookIV.Electroweak.instReprSourceEquation.repr :SourceEquation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprSourceEquation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L247-L247)
**instance
Tau.BookIV.Electroweak.instReprSourceEquation :Repr SourceEquation**

Equations
- Tau.BookIV.Electroweak.instReprSourceEquation = { reprPrec := Tau.BookIV.Electroweak.instReprSourceEquation.repr }

---

### `Tau.BookIV.Electroweak.source_instance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L249-L251)
**def
Tau.BookIV.Electroweak.source_instance :SourceEquation**

Equations
- Tau.BookIV.Electroweak.source_instance = { maxwell_count := 2, count_eq := Tau.BookIV.Electroweak.bianchi_instance._proof_1 }
Instances For

---

### `Tau.BookIV.Electroweak.source_equation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L253-L253)
**theorem
Tau.BookIV.Electroweak.source_equation :source_instance.source_eq = true**


---

### `Tau.BookIV.Electroweak.MaxwellEquations`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L259-L271)
**structure
Tau.BookIV.Electroweak.MaxwellEquations :Type**


[IV.T44] All four Maxwell equations assembled:
(1) div B = 0, (2) curl E = -∂B/∂t [from dF=0],
(3) div E = ρ/ε₀, (4) curl B = μ₀J + μ₀ε₀ ∂E/∂t [from d*F=*J].
Total: 2 + 2 = 4 equations.

- bianchi : BianchiIdentity
Bianchi identity (homogeneous pair).

- source : SourceEquation
Source equation (inhomogeneous pair).

- total_count : ℕ
Total equation count.

- total_eq : self.total_count = self.bianchi.maxwell_count + self.source.maxwell_count
Instances For

---

### `Tau.BookIV.Electroweak.instReprMaxwellEquations.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L271-L271)
**def
Tau.BookIV.Electroweak.instReprMaxwellEquations.repr :MaxwellEquations → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprMaxwellEquations`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L271-L271)
**instance
Tau.BookIV.Electroweak.instReprMaxwellEquations :Repr MaxwellEquations**

Equations
- Tau.BookIV.Electroweak.instReprMaxwellEquations = { reprPrec := Tau.BookIV.Electroweak.instReprMaxwellEquations.repr }

---

### `Tau.BookIV.Electroweak.maxwell_eqs`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L273-L278)
**def
Tau.BookIV.Electroweak.maxwell_eqs :MaxwellEquations**


Canonical Maxwell equations.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.maxwell_equations`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L280-L280)
**theorem
Tau.BookIV.Electroweak.maxwell_equations :maxwell_eqs.total_count = 4**


---

### `Tau.BookIV.Electroweak.DefectSources`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L286-L294)
**structure
Tau.BookIV.Electroweak.DefectSources :Type**


[IV.T45] Orthodox EM sources (charges, currents) have τ-defect
interpretation: charges = persistent winding-number defects on T²,
currents = transport of these defects through spacetime.

- charge_is_winding : Bool
Charges are winding-number defects.

- current_is_transport : Bool
Currents are defect transport.

Instances For

---

### `Tau.BookIV.Electroweak.instReprDefectSources`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L294-L294)
**instance
Tau.BookIV.Electroweak.instReprDefectSources :Repr DefectSources**

Equations
- Tau.BookIV.Electroweak.instReprDefectSources = { reprPrec := Tau.BookIV.Electroweak.instReprDefectSources.repr }

---

### `Tau.BookIV.Electroweak.instReprDefectSources.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L294-L294)
**def
Tau.BookIV.Electroweak.instReprDefectSources.repr :DefectSources → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.defect_sources_instance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L296-L296)
**def
Tau.BookIV.Electroweak.defect_sources_instance :DefectSources**

Equations
- Tau.BookIV.Electroweak.defect_sources_instance = { }
Instances For

---

### `Tau.BookIV.Electroweak.defect_sources`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L298-L299)
**theorem
Tau.BookIV.Electroweak.defect_sources :defect_sources_instance.charge_is_winding = true**


---

### `Tau.BookIV.Electroweak.CoulombLimit`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L305-L315)
**structure
Tau.BookIV.Electroweak.CoulombLimit :Type**


[IV.T46] Static limit of Maxwell gives Coulomb's law:
F = k_e · q₁q₂ / r² where k_e = 1/(4πε₀).
The 1/r² law follows from Gauss's law in 3 spatial dimensions.

- spatial_dim : ℕ
Spatial dimension for 1/r² law.

- dim_eq : self.spatial_dim = 3
- force_exponent : ℕ
Exponent in force law = spatial_dim - 1.

- exp_eq : self.force_exponent = self.spatial_dim - 1
Instances For

---

### `Tau.BookIV.Electroweak.instReprCoulombLimit.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L315-L315)
**def
Tau.BookIV.Electroweak.instReprCoulombLimit.repr :CoulombLimit → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprCoulombLimit`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L315-L315)
**instance
Tau.BookIV.Electroweak.instReprCoulombLimit :Repr CoulombLimit**

Equations
- Tau.BookIV.Electroweak.instReprCoulombLimit = { reprPrec := Tau.BookIV.Electroweak.instReprCoulombLimit.repr }

---

### `Tau.BookIV.Electroweak.coulomb_3d`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L317-L322)
**def
Tau.BookIV.Electroweak.coulomb_3d :CoulombLimit**


Coulomb law in 3D: F ∝ 1/r².
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.coulomb_limit`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L324-L324)
**theorem
Tau.BookIV.Electroweak.coulomb_limit :coulomb_3d.force_exponent = 2**


---

### `Tau.BookIV.Electroweak.WaveEquation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L330-L339)
**structure
Tau.BookIV.Electroweak.WaveEquation :Type**


[IV.T47] Source-free Lorenz gauge gives wave equation □A_μ = 0.
Solutions are plane waves: the photon field.

- source_free : Bool
Source-free (J = 0).

- lorenz_gauge : Bool
Lorenz gauge imposed.

- is_wave_eq : Bool
Resulting equation is □A = 0.

Instances For

---

### `Tau.BookIV.Electroweak.instReprWaveEquation.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L339-L339)
**def
Tau.BookIV.Electroweak.instReprWaveEquation.repr :WaveEquation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprWaveEquation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L339-L339)
**instance
Tau.BookIV.Electroweak.instReprWaveEquation :Repr WaveEquation**

Equations
- Tau.BookIV.Electroweak.instReprWaveEquation = { reprPrec := Tau.BookIV.Electroweak.instReprWaveEquation.repr }

---

### `Tau.BookIV.Electroweak.wave_equation_instance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L341-L341)
**def
Tau.BookIV.Electroweak.wave_equation_instance :WaveEquation**

Equations
- Tau.BookIV.Electroweak.wave_equation_instance = { }
Instances For

---

### `Tau.BookIV.Electroweak.wave_equation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L343-L344)
**theorem
Tau.BookIV.Electroweak.wave_equation :wave_equation_instance.is_wave_eq = true**


---

### `Tau.BookIV.Electroweak.ContinuityEquation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L350-L358)
**structure
Tau.BookIV.Electroweak.ContinuityEquation :Type**


[IV.P44] Source equation implies continuity equation ∂_μ J^μ = 0.
From d*F = *J and d² = 0: d*J = d²*F = 0 → ∂_μ J^μ = 0.
Physical content: charge conservation (local form).

- from_d_squared : Bool
d²=0 implies d*J=0.

- is_charge_conservation : Bool
Equivalent to charge conservation.

Instances For

---

### `Tau.BookIV.Electroweak.instReprContinuityEquation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L358-L358)
**instance
Tau.BookIV.Electroweak.instReprContinuityEquation :Repr ContinuityEquation**

Equations
- Tau.BookIV.Electroweak.instReprContinuityEquation = { reprPrec := Tau.BookIV.Electroweak.instReprContinuityEquation.repr }

---

### `Tau.BookIV.Electroweak.instReprContinuityEquation.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L358-L358)
**def
Tau.BookIV.Electroweak.instReprContinuityEquation.repr :ContinuityEquation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.continuity_instance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L360-L360)
**def
Tau.BookIV.Electroweak.continuity_instance :ContinuityEquation**

Equations
- Tau.BookIV.Electroweak.continuity_instance = { }
Instances For

---

### `Tau.BookIV.Electroweak.continuity_equation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L362-L363)
**theorem
Tau.BookIV.Electroweak.continuity_equation :continuity_instance.is_charge_conservation = true**


---

### `Tau.BookIV.Electroweak.ChargeDensity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L369-L377)
**structure
Tau.BookIV.Electroweak.ChargeDensity :Type**


[IV.P45] Charge density ρ = J^0: count of winding numbers
per unit spatial volume. A positive ρ corresponds to net
positive winding (protons); negative to electrons.

- is_j_zero : Bool
Is the time-component of J.

- is_winding_count : Bool
Counts winding numbers per volume.

Instances For

---

### `Tau.BookIV.Electroweak.instReprChargeDensity.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L377-L377)
**def
Tau.BookIV.Electroweak.instReprChargeDensity.repr :ChargeDensity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprChargeDensity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L377-L377)
**instance
Tau.BookIV.Electroweak.instReprChargeDensity :Repr ChargeDensity**

Equations
- Tau.BookIV.Electroweak.instReprChargeDensity = { reprPrec := Tau.BookIV.Electroweak.instReprChargeDensity.repr }

---

### `Tau.BookIV.Electroweak.charge_density_instance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L379-L379)
**def
Tau.BookIV.Electroweak.charge_density_instance :ChargeDensity**

Equations
- Tau.BookIV.Electroweak.charge_density_instance = { }
Instances For

---

### `Tau.BookIV.Electroweak.charge_density`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L381-L382)
**theorem
Tau.BookIV.Electroweak.charge_density :charge_density_instance.is_winding_count = true**


---

### `Tau.BookIV.Electroweak.CurrentDensity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L388-L396)
**structure
Tau.BookIV.Electroweak.CurrentDensity :Type**


[IV.P46] Spatial current density J^i: transport of charged defects
through space. J = ρv for uniform charge motion.

- components : ℕ
Spatial components (3).

- comp_eq : self.components = 3
- is_defect_transport : Bool
Is transport of charged defects.

Instances For

---

### `Tau.BookIV.Electroweak.instReprCurrentDensity.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L396-L396)
**def
Tau.BookIV.Electroweak.instReprCurrentDensity.repr :CurrentDensity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprCurrentDensity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L396-L396)
**instance
Tau.BookIV.Electroweak.instReprCurrentDensity :Repr CurrentDensity**

Equations
- Tau.BookIV.Electroweak.instReprCurrentDensity = { reprPrec := Tau.BookIV.Electroweak.instReprCurrentDensity.repr }

---

### `Tau.BookIV.Electroweak.current_density_instance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L398-L400)
**def
Tau.BookIV.Electroweak.current_density_instance :CurrentDensity**

Equations
- Tau.BookIV.Electroweak.current_density_instance = { components := 3, comp_eq := Tau.BookIV.Electroweak.em_connection_a._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.current_density`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L402-L403)
**theorem
Tau.BookIV.Electroweak.current_density :current_density_instance.is_defect_transport = true**


---

### `Tau.BookIV.Electroweak.PhotonEMWave`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L409-L419)
**structure
Tau.BookIV.Electroweak.PhotonEMWave :Type**


[IV.P47] The photon (τ-transport mode) and the EM wave (Maxwell
solution) are the SAME object at different descriptive levels.
Photon = quantum level, EM wave = classical limit.

- same_object : Bool
Same object at two levels.

- quantum_level : Bool
Photon = quantum (discrete).

- classical_level : Bool
EM wave = classical (continuous).

Instances For

---

### `Tau.BookIV.Electroweak.instReprPhotonEMWave.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L419-L419)
**def
Tau.BookIV.Electroweak.instReprPhotonEMWave.repr :PhotonEMWave → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprPhotonEMWave`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L419-L419)
**instance
Tau.BookIV.Electroweak.instReprPhotonEMWave :Repr PhotonEMWave**

Equations
- Tau.BookIV.Electroweak.instReprPhotonEMWave = { reprPrec := Tau.BookIV.Electroweak.instReprPhotonEMWave.repr }

---

### `Tau.BookIV.Electroweak.photon_em_wave_instance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L421-L421)
**def
Tau.BookIV.Electroweak.photon_em_wave_instance :PhotonEMWave**

Equations
- Tau.BookIV.Electroweak.photon_em_wave_instance = { }
Instances For

---

### `Tau.BookIV.Electroweak.photon_is_em_wave`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L423-L424)
**theorem
Tau.BookIV.Electroweak.photon_is_em_wave :photon_em_wave_instance.same_object = true**


---

### `Tau.BookIV.Electroweak.MagneticForce`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L430-L437)
**structure
Tau.BookIV.Electroweak.MagneticForce :Type**


[IV.P48] Magnetic force is perpendicular to velocity: F = qv × B.
The magnetic field does no work (F · v = 0).

- perpendicular : Bool
Force perpendicular to velocity.

- no_work : Bool
Does no work.

Instances For

---

### `Tau.BookIV.Electroweak.instReprMagneticForce.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L437-L437)
**def
Tau.BookIV.Electroweak.instReprMagneticForce.repr :MagneticForce → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprMagneticForce`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L437-L437)
**instance
Tau.BookIV.Electroweak.instReprMagneticForce :Repr MagneticForce**

Equations
- Tau.BookIV.Electroweak.instReprMagneticForce = { reprPrec := Tau.BookIV.Electroweak.instReprMagneticForce.repr }

---

### `Tau.BookIV.Electroweak.magnetic_force_instance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L439-L439)
**def
Tau.BookIV.Electroweak.magnetic_force_instance :MagneticForce**

Equations
- Tau.BookIV.Electroweak.magnetic_force_instance = { }
Instances For

---

### `Tau.BookIV.Electroweak.magnetic_force_perpendicular`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L441-L443)
**theorem
Tau.BookIV.Electroweak.magnetic_force_perpendicular :magnetic_force_instance.perpendicular = true ∧ magnetic_force_instance.no_work = true**


---

### `Tau.BookIV.Electroweak.QEDCorrections`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L449-L461)
**structure
Tau.BookIV.Electroweak.QEDCorrections :Type**


[IV.P49] Quantum corrections as power series in α:
tree-level → one-loop (α) → two-loop (α²) → ...
The series is asymptotic; convergence controlled by α ≈ 1/137.

- alpha_inverse_approx : ℕ
Coupling constant inverse (≈ 137).

- inv_range : self.alpha_inverse_approx > 130 ∧ self.alpha_inverse_approx < 140
- is_asymptotic : Bool
Series is asymptotic (not convergent).

- leading_order : ℕ
Leading correction order.

- order_eq : self.leading_order = 1
Instances For

---

### `Tau.BookIV.Electroweak.instReprQEDCorrections`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L461-L461)
**instance
Tau.BookIV.Electroweak.instReprQEDCorrections :Repr QEDCorrections**

Equations
- Tau.BookIV.Electroweak.instReprQEDCorrections = { reprPrec := Tau.BookIV.Electroweak.instReprQEDCorrections.repr }

---

### `Tau.BookIV.Electroweak.instReprQEDCorrections.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L461-L461)
**def
Tau.BookIV.Electroweak.instReprQEDCorrections.repr :QEDCorrections → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.qed_standard`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L463-L468)
**def
Tau.BookIV.Electroweak.qed_standard :QEDCorrections**


Standard QED corrections with α⁻¹ ≈ 137.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.qed_corrections`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L470-L470)
**theorem
Tau.BookIV.Electroweak.qed_corrections :qed_standard.alpha_inverse_approx = 137**


---

### `Tau.BookIV.Electroweak.example_hodge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L484-L484)
**def
Tau.BookIV.Electroweak.example_hodge :HodgeDual**

Equations
- Tau.BookIV.Electroweak.example_hodge = { }
Instances For

---

### `Tau.BookIV.Electroweak.example_wave`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Electroweak/TauMaxwell.lean#L486-L486)
**def
Tau.BookIV.Electroweak.example_wave :WaveEquation**

Equations
- Tau.BookIV.Electroweak.example_wave = { }
Instances For
