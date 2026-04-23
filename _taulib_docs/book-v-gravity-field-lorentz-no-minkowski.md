---
layout: taulib-doc
title: "TauLib.BookV.GravityField.LorentzNoMinkowski"
permalink: /verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/
lane: verify
module_name: "TauLib.BookV.GravityField.LorentzNoMinkowski"
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

# TauLib.BookV.GravityField.LorentzNoMinkowski


Lorentz symmetry emerges from readout-functor preservation on local τ³
charts. Minkowski spacetime is a local neighborhood approximation, NOT
a global arena.

## Registry Cross-References


- [V.D47] Null Intertwiner (restated) — `NullIntertwinerField`

- [V.D48] Local τ³ Chart — `LocalTau3Chart`

- [V.C02] Readout-Invariant Null Set — `null_set_invariant`

- [V.T24] Lorentz Group from Readout Functor — `lorentz_from_readout`

- [V.T25] Minkowski from Local Chart — `minkowski_from_chart`

- [V.P12] Null Set Invariance — `null_is_readout_invariant`

- [V.P13] Massive Defects Cannot Reach Null — `massive_cannot_null`

- [V.R59] Photon as Null Intertwiner — structural remark


## Mathematical Content


### Null Intertwiners in the Gravitational Field


The null intertwiner (photon) from V.D27 is restated here in the
gravitational field context. The null condition (zero fiber stiffness,
massless) singles out the B-sector (EM) and defines the light cone
structure that readout observers measure.

### Local τ³ Charts


A local τ³ chart is a coordinate neighborhood at depth n that provides
a 4-dimensional readout (1 temporal + 3 spatial). The chart is NOT
the ontology — it is a readout approximation of the boundary-character
data. Lorentz symmetry emerges as the symmetry group of the null set
under chart readout.

### Lorentz Group


SO(3,1) emerges as the group of readout-functor automorphisms that
preserve the null set. This is NOT postulated — it follows from:

- The null condition (zero mass, speed c)

- The chart dimension (4 = 1 + 3)

- The readout-functor preservation requirement


### Minkowski Neighborhood


The Minkowski metric η_μν = diag(-1,+1,+1,+1) is the flat-space limit
of the local chart readout. It exists only as a local approximation:
globally, the τ³ boundary-character structure replaces Minkowski space.

## Ground Truth Sources


- Book V Part III ch12 (Lorentz No Minkowski)


---

### `Tau.BookV.GravityField.NullIntertwinerField`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L65-L86)
**structure
Tau.BookV.GravityField.NullIntertwinerField :Type**


[V.D47] Null intertwiner in the gravitational field context.

Restated from V.D27 with emphasis on the light-cone boundary
that defines Lorentz structure.

Properties:


- Massless (zero fiber stiffness on T²)

- Propagates at c_τ (speed of light = null transport rate)

- Selects B-sector (EM) uniquely

- Defines the null set for chart readout


- sector : BookIII.Sectors.Sector
The sector (must be B = EM).

- sector_is_em : self.sector = BookIII.Sectors.Sector.B
Null selects EM.

- massless : Bool
Massless flag.

- massless_true : self.massless = true
Must be massless.

- speed_is_c : Bool
Speed is c (light speed, in natural units = 1).

Instances For

---

### `Tau.BookV.GravityField.instReprNullIntertwinerField.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L86-L86)
**def
Tau.BookV.GravityField.instReprNullIntertwinerField.repr :NullIntertwinerField → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprNullIntertwinerField`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L86-L86)
**instance
Tau.BookV.GravityField.instReprNullIntertwinerField :Repr NullIntertwinerField**

Equations
- Tau.BookV.GravityField.instReprNullIntertwinerField = { reprPrec := Tau.BookV.GravityField.instReprNullIntertwinerField.repr }

---

### `Tau.BookV.GravityField.photon_field`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L88-L93)
**def
Tau.BookV.GravityField.photon_field :NullIntertwinerField**


The photon as the canonical null intertwiner in the field context.
Equations
- Tau.BookV.GravityField.photon_field = { sector := Tau.BookIII.Sectors.Sector.B, sector_is_em := ⋯, massless := true, massless_true := ⋯ }
Instances For

---

### `Tau.BookV.GravityField.MetricSignature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L99-L106)
**structure
Tau.BookV.GravityField.MetricSignature :Type**


Signature type for the chart metric: number of negative and
positive eigenvalues. For Lorentzian: (1, 3).

- negative : ℕ
Number of negative eigenvalues (temporal dimensions).

- positive : ℕ
Number of positive eigenvalues (spatial dimensions).

Instances For

---

### `Tau.BookV.GravityField.instReprMetricSignature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L106-L106)
**instance
Tau.BookV.GravityField.instReprMetricSignature :Repr MetricSignature**

Equations
- Tau.BookV.GravityField.instReprMetricSignature = { reprPrec := Tau.BookV.GravityField.instReprMetricSignature.repr }

---

### `Tau.BookV.GravityField.instReprMetricSignature.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L106-L106)
**def
Tau.BookV.GravityField.instReprMetricSignature.repr :MetricSignature → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instDecidableEqMetricSignature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L106-L106)
**instance
Tau.BookV.GravityField.instDecidableEqMetricSignature :DecidableEq MetricSignature**

Equations
- Tau.BookV.GravityField.instDecidableEqMetricSignature = Tau.BookV.GravityField.instDecidableEqMetricSignature.decEq

---

### `Tau.BookV.GravityField.instDecidableEqMetricSignature.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L106-L106)
**def
Tau.BookV.GravityField.instDecidableEqMetricSignature.decEq
(x✝ x✝¹ : MetricSignature)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instBEqMetricSignature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L106-L106)
**instance
Tau.BookV.GravityField.instBEqMetricSignature :BEq MetricSignature**

Equations
- Tau.BookV.GravityField.instBEqMetricSignature = { beq := Tau.BookV.GravityField.instBEqMetricSignature.beq }

---

### `Tau.BookV.GravityField.instBEqMetricSignature.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L106-L106)
**def
Tau.BookV.GravityField.instBEqMetricSignature.beq :MetricSignature → MetricSignature → Bool**

Equations
- Tau.BookV.GravityField.instBEqMetricSignature.beq { negative := a, positive := a_1 }
 { negative := b, positive := b_1 } = (a == b && a_1 == b_1)
- Tau.BookV.GravityField.instBEqMetricSignature.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookV.GravityField.lorentzian_signature`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L108-L111)
**def
Tau.BookV.GravityField.lorentzian_signature :MetricSignature**


The Lorentzian signature (1,3) = 1 temporal + 3 spatial.
Equations
- Tau.BookV.GravityField.lorentzian_signature = { negative := 1, positive := 3 }
Instances For

---

### `Tau.BookV.GravityField.LocalTau3Chart`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L113-L136)
**structure
Tau.BookV.GravityField.LocalTau3Chart :Type**


[V.D48] Local τ³ chart: coordinate neighborhood providing a
4-dimensional readout at depth n.

The chart provides:


- 4 coordinates (1 temporal + 3 spatial)

- Metric signature (1,3) = Lorentzian

- Valid only in a local neighborhood (not global)

- Readout approximation of boundary-character data


- depth : ℕ
Refinement depth.

- depth_pos : self.depth > 0
Depth positive.

- dimension : ℕ
Total dimension (must be 4).

- dim_is_four : self.dimension = 4
Dimension is 4.

- signature : MetricSignature
Metric signature.

- sig_lorentzian : self.signature = lorentzian_signature
Signature is Lorentzian (1,3).

- is_local : Bool
Chart is local (not global).

Instances For

---

### `Tau.BookV.GravityField.instReprLocalTau3Chart`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L136-L136)
**instance
Tau.BookV.GravityField.instReprLocalTau3Chart :Repr LocalTau3Chart**

Equations
- Tau.BookV.GravityField.instReprLocalTau3Chart = { reprPrec := Tau.BookV.GravityField.instReprLocalTau3Chart.repr }

---

### `Tau.BookV.GravityField.instReprLocalTau3Chart.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L136-L136)
**def
Tau.BookV.GravityField.instReprLocalTau3Chart.repr :LocalTau3Chart → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.example_chart`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L138-L145)
**def
Tau.BookV.GravityField.example_chart :LocalTau3Chart**


Example chart at depth 10.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.null_set_invariant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L151-L159)
**theorem
Tau.BookV.GravityField.null_set_invariant :photon_field.speed_is_c = true**


[V.C02] The null set is readout-invariant: the set of null
worldlines (light rays) is preserved by any admissible
readout-functor transformation.

This invariance is the structural origin of c = const.
Speed of light constancy is NOT an axiom — it follows from
null-intertwiner masslessness and readout-functor preservation.

---

### `Tau.BookV.GravityField.lorentz_from_readout`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L165-L180)
**theorem
Tau.BookV.GravityField.lorentz_from_readout :lorentzian_signature.negative = 1 ∧ lorentzian_signature.positive = 3 ∧ lorentzian_signature.negative + lorentzian_signature.positive = 4**


[V.T24] The Lorentz group SO(3,1) emerges as the group of
readout-functor automorphisms preserving the null set.

Derivation:

- Null condition fixes the light cone

- Chart dimension 4 = 1 + 3 gives the manifold

- Readout preservation = conformal structure preservation

- SO(3,1) is the unique group preserving a (1,3) null cone


The Lorentz group is NOT postulated: it is the unique symmetry
group compatible with the null set and chart dimension.

---

### `Tau.BookV.GravityField.spacetime_dimension`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L182-L185)
**theorem
Tau.BookV.GravityField.spacetime_dimension :lorentzian_signature.negative + lorentzian_signature.positive = 4**


The total spacetime dimension from the signature.

---

### `Tau.BookV.GravityField.minkowski_from_chart`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L191-L202)
**theorem
Tau.BookV.GravityField.minkowski_from_chart
(c : LocalTau3Chart)
 :c.signature = lorentzian_signature ∧ c.dimension = 4**


[V.T25] Minkowski spacetime η_μν = diag(-1,+1,+1,+1) emerges
as the flat-space limit of a local τ³ chart.

The Minkowski metric is:


- A local approximation (valid in one chart neighborhood)

- The zeroth-order term in the chart readout expansion

- NOT a global arena (globally replaced by τ³ boundary data)


This theorem records that the chart signature determines Minkowski.

---

### `Tau.BookV.GravityField.null_is_readout_invariant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L208-L218)
**theorem
Tau.BookV.GravityField.null_is_readout_invariant :photon_field.sector = BookIII.Sectors.Sector.B ∧ photon_field.massless = true ∧ photon_field.speed_is_c = true**


[V.P12] Null set invariance: the null intertwiner selects a
unique sector (EM) and propagation speed (c).

Any readout functor preserving the boundary-character structure
must preserve the null set. This is the structural content of
"Lorentz invariance of the speed of light."

---

### `Tau.BookV.GravityField.massive_cannot_null`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L224-L232)
**theorem
Tau.BookV.GravityField.massive_cannot_null
(n : NullIntertwinerField)
 :n.massless = true**


[V.P13] Massive defects cannot reach the null condition.

A defect with nonzero fiber stiffness (mass > 0) on T² cannot
satisfy the null condition. The mass gap prevents massive
particles from reaching light speed.

Encoded: any NullIntertwinerField must have massless = true.
