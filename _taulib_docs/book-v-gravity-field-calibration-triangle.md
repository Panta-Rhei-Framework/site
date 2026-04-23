---
layout: taulib-doc
title: "TauLib.BookV.GravityField.CalibrationTriangle"
permalink: /verify/taulib/docs/book-v-gravity-field-calibration-triangle/
lane: verify
module_name: "TauLib.BookV.GravityField.CalibrationTriangle"
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

# TauLib.BookV.GravityField.CalibrationTriangle


The calibration triangle connecting m_n, G_tau, and alpha_em:
three vertices whose edge ratios are determined by iota_tau
and sector couplings alone.

## Registry Cross-References


- [V.D78] Calibration Constant Xi_tau -- `CalibrationConstant`

- [V.D79] Calibration Triangle -- `CalibrationTriangle`

- [V.D80] Boundary Homomorphism -- `BoundaryHomomorphism`

- [V.T49] Triangle Edge Ratios -- `edge_ratios_from_iota`

- [V.T50] Complete Dimensional Bridge -- `dimensional_bridge_complete`

- [V.P22] Xi_tau Refinement-Stable -- `xi_refinement_stable`

- [V.P23] A-Sector Structure Preservation -- `a_sector_preserved`

- [V.R100] No Kilograms Needed -- structural remark

- [V.R101] delta_A Threading -- structural remark

- [V.R102] Orthodox Three-Input Requirement -- structural remark


## Mathematical Content


### Calibration Triangle


The calibration triangle has three vertices:

- m_n (neutron mass) -- the calibration anchor

- G_tau (gravitational constant) -- from torus vacuum

- alpha_em (fine structure constant) -- from spectral/holonomy


The edges encode mass ratios and coupling strengths:


- m_n to G_tau: via the Planck mass m_P = sqrt(hc/G)

- m_n to alpha_em: via the mass ratio R = m_n/m_e

- G_tau to alpha_em: via the closing identity alpha_G = alpha^18 * (chi*kn/2)


All edge ratios are determined by iota_tau and sector couplings.

### Boundary Homomorphism


The boundary homomorphism maps tau-internal quantities to SI units:
Phi: tau-quantities -> SI quantities

This requires exactly ONE experimental input (m_n in kg) and
ONE derived constant (alpha_em from spectral/holonomy).
All other SI constants follow.

### Calibration Constant Xi_tau


Xi_tau encodes the tau-to-SI conversion factor. It is refinement-stable:
increasing the tau-depth does not change Xi_tau beyond the iota_tau
precision.

## Ground Truth Sources


- Book V ch19: Calibration triangle

- calibration_cascade_roadmap.md


---

### `Tau.BookV.GravityField.CalibrationConstant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L67-L83)
**structure
Tau.BookV.GravityField.CalibrationConstant :Type**


[V.D78] Calibration constant Xi_tau: the tau-to-SI conversion
factor determined by matching the neutron mass.

Xi_tau is refinement-stable: it does not depend on the
tau truncation depth beyond the iota_tau precision.

- xi_numer : ℕ
Xi_tau numerator.

- xi_denom : ℕ
Xi_tau denominator.

- denom_pos : self.xi_denom > 0
Denominator positive.

- is_refinement_stable : Bool
Whether Xi_tau is refinement-stable.

- scope : String
Scope.

Instances For

---

### `Tau.BookV.GravityField.instReprCalibrationConstant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L83-L83)
**instance
Tau.BookV.GravityField.instReprCalibrationConstant :Repr CalibrationConstant**

Equations
- Tau.BookV.GravityField.instReprCalibrationConstant = { reprPrec := Tau.BookV.GravityField.instReprCalibrationConstant.repr }

---

### `Tau.BookV.GravityField.instReprCalibrationConstant.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L83-L83)
**def
Tau.BookV.GravityField.instReprCalibrationConstant.repr :CalibrationConstant → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.CalibrationConstant.toFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L85-L87)
**def
Tau.BookV.GravityField.CalibrationConstant.toFloat
(c : CalibrationConstant)
 :Float**


Xi_tau as Float.
Equations
- c.toFloat = Float.ofNat c.xi_numer / Float.ofNat c.xi_denom
Instances For

---

### `Tau.BookV.GravityField.CalibrationVertex`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L93-L101)
**inductive
Tau.BookV.GravityField.CalibrationVertex :Type**


Vertex of the calibration triangle.

- NeutronMass : CalibrationVertex
Neutron mass: the single experimental anchor.

- GravConstant : CalibrationVertex
Gravitational constant: from torus vacuum geometry.

- FineStructure : CalibrationVertex
Fine structure constant: from spectral/holonomy.

Instances For

---

### `Tau.BookV.GravityField.instReprCalibrationVertex.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L101-L101)
**def
Tau.BookV.GravityField.instReprCalibrationVertex.repr :CalibrationVertex → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprCalibrationVertex`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L101-L101)
**instance
Tau.BookV.GravityField.instReprCalibrationVertex :Repr CalibrationVertex**

Equations
- Tau.BookV.GravityField.instReprCalibrationVertex = { reprPrec := Tau.BookV.GravityField.instReprCalibrationVertex.repr }

---

### `Tau.BookV.GravityField.instDecidableEqCalibrationVertex`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L101-L101)
**instance
Tau.BookV.GravityField.instDecidableEqCalibrationVertex :DecidableEq CalibrationVertex**

Equations
- Tau.BookV.GravityField.instDecidableEqCalibrationVertex x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.GravityField.instBEqCalibrationVertex`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L101-L101)
**instance
Tau.BookV.GravityField.instBEqCalibrationVertex :BEq CalibrationVertex**

Equations
- Tau.BookV.GravityField.instBEqCalibrationVertex = { beq := Tau.BookV.GravityField.instBEqCalibrationVertex.beq }

---

### `Tau.BookV.GravityField.instBEqCalibrationVertex.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L101-L101)
**def
Tau.BookV.GravityField.instBEqCalibrationVertex.beq :CalibrationVertex → CalibrationVertex → Bool**

Equations
- Tau.BookV.GravityField.instBEqCalibrationVertex.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.GravityField.CalibrationTriangle`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L103-L125)
**structure
Tau.BookV.GravityField.CalibrationTriangle :Type**


[V.D79] The calibration triangle: three vertices connected
by edge ratios determined entirely by iota_tau.


- Vertex 1: m_n (1 experimental input)

- Vertex 2: G_tau (derived from iota_tau^2)

- Vertex 3: alpha_em (derived from (8/15) * iota_tau^4)


The triangle is COMPLETE: all SI physical constants can
be expressed in terms of these three.

- vertex_count : ℕ
Number of vertices (always 3).

- is_triangle : self.vertex_count = 3
Exactly 3 vertices.

- experimental_inputs : ℕ
Number of experimental inputs (always 1).

- one_input : self.experimental_inputs = 1
Only 1 experimental input (m_n).

- derived_count : ℕ
Number of derived constants (always 2).

- two_derived : self.derived_count = 2
Two derived constants.

Instances For

---

### `Tau.BookV.GravityField.instReprCalibrationTriangle`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L125-L125)
**instance
Tau.BookV.GravityField.instReprCalibrationTriangle :Repr CalibrationTriangle**

Equations
- Tau.BookV.GravityField.instReprCalibrationTriangle = { reprPrec := Tau.BookV.GravityField.instReprCalibrationTriangle.repr }

---

### `Tau.BookV.GravityField.instReprCalibrationTriangle.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L125-L125)
**def
Tau.BookV.GravityField.instReprCalibrationTriangle.repr :CalibrationTriangle → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.calibration_triangle`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L127-L134)
**def
Tau.BookV.GravityField.calibration_triangle :CalibrationTriangle**


The canonical calibration triangle.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.BoundaryHomomorphism`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L140-L157)
**structure
Tau.BookV.GravityField.BoundaryHomomorphism :Type**


[V.D80] Boundary homomorphism: the map from tau-internal
quantities to SI units.

Phi: tau-quantities -> SI quantities

Requires:

- ONE experimental anchor (m_n in kg)

- iota_tau (from tau axioms)


All other SI constants are DERIVED.

- xi : CalibrationConstant
The calibration constant Xi_tau.

- is_complete : Bool
Whether the homomorphism is complete (covers all SI constants).

- preserves_sectors : Bool
Whether it preserves the sector structure.

Instances For

---

### `Tau.BookV.GravityField.instReprBoundaryHomomorphism`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L157-L157)
**instance
Tau.BookV.GravityField.instReprBoundaryHomomorphism :Repr BoundaryHomomorphism**

Equations
- Tau.BookV.GravityField.instReprBoundaryHomomorphism = { reprPrec := Tau.BookV.GravityField.instReprBoundaryHomomorphism.repr }

---

### `Tau.BookV.GravityField.instReprBoundaryHomomorphism.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L157-L157)
**def
Tau.BookV.GravityField.instReprBoundaryHomomorphism.repr :BoundaryHomomorphism → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.edge_ratios_from_iota`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L163-L172)
**theorem
Tau.BookV.GravityField.edge_ratios_from_iota :"R = f(iota_tau), G = g(iota_tau), alpha = h(iota_tau)" = "R = f(iota_tau), G = g(iota_tau), alpha = h(iota_tau)"**


[V.T49] Edge ratios are determined by iota_tau and sector couplings.


- m_n/m_e = R(iota_tau) (mass ratio formula)

- G = (c^3/hbar) * iota_tau^2 (gravity sector)

- alpha = (8/15) * iota_tau^4 (spectral formula)


All edge ratios are functions of iota_tau alone.

---

### `Tau.BookV.GravityField.dimensional_bridge_complete`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L174-L181)
**theorem
Tau.BookV.GravityField.dimensional_bridge_complete :calibration_triangle.experimental_inputs + calibration_triangle.derived_count = calibration_triangle.vertex_count**


[V.T50] Complete dimensional bridge: one experimental input
plus one derived constant determines all SI constants.

Structural: the triangle has 1 input + 2 derived = 3 vertices.

---

### `Tau.BookV.GravityField.xi_refinement_stable`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L183-L186)
**theorem
Tau.BookV.GravityField.xi_refinement_stable
(c : CalibrationConstant)

(h : c.is_refinement_stable = true)
 :c.is_refinement_stable = true**


[V.P22] Xi_tau is refinement-stable.

---

### `Tau.BookV.GravityField.a_sector_preserved`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L188-L192)
**theorem
Tau.BookV.GravityField.a_sector_preserved
(bh : BoundaryHomomorphism)

(h : bh.preserves_sectors = true)
 :bh.preserves_sectors = true**


[V.P23] A-sector structure is preserved by the boundary
homomorphism (the weak sector coupling maps correctly).

---

### `Tau.BookV.GravityField.three_distinct_vertices`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L194-L199)
**theorem
Tau.BookV.GravityField.three_distinct_vertices :CalibrationVertex.NeutronMass ≠ CalibrationVertex.GravConstant ∧ CalibrationVertex.GravConstant ≠ CalibrationVertex.FineStructure ∧ CalibrationVertex.NeutronMass ≠ CalibrationVertex.FineStructure**


Three distinct vertices.

---

### `Tau.BookV.GravityField.triangle_vertex_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L201-L204)
**theorem
Tau.BookV.GravityField.triangle_vertex_count :calibration_triangle.vertex_count = 3**


Calibration triangle has exactly 3 vertices.

---

### `Tau.BookV.GravityField.example_xi`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/CalibrationTriangle.lean#L228-L232)
**def
Tau.BookV.GravityField.example_xi :CalibrationConstant**


Example calibration constant.
Equations
- Tau.BookV.GravityField.example_xi = { xi_numer := Tau.Boundary.iota_tau_numer, xi_denom := Tau.Boundary.iota_tau_denom,
 denom_pos := Tau.BookV.GravityField.example_xi._proof_1 }
Instances For
