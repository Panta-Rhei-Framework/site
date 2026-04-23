---
layout: taulib-doc
title: "TauLib.BookII.Mirror.PhysicsQuadrant"
permalink: /verify/taulib/docs/book-ii-mirror-physics-quadrant/
lane: verify
module_name: "TauLib.BookII.Mirror.PhysicsQuadrant"
book: "II"
book_label: "Holomorphy"
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
    book: "Book II"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookII.Mirror.PhysicsQuadrant


The physics quadrant matrix: PDE type x metric axis classification
of physical theories. The unification obstruction in the Archimedean
column and its resolution in the fourth (non-Archimedean, hyperbolic)
quadrant.

## Registry Cross-References


- [II.D73] Physics Quadrant Matrix -- `PDEAxis`, `MetricAxis`, `PhysicsQuadrant`

- [II.D74] Unification Obstruction -- `same_archimedean_column`, `compatible_pde`,
`unification_obstructed`

- [II.T46] Fourth Quadrant Resolution -- `tau_is_non_archimedean`,
`tau_is_hyperbolic`, `tau_escapes_obstruction`


## Mathematical Content


**II.D73 (Physics Quadrant Matrix):** Physical theories can be classified
along two axes:

- **PDE axis:** Elliptic (maximum principle, diffusion) vs Hyperbolic
(wave equation, propagation)

- **Metric axis:** Archimedean (real-valued distances, epsilon-delta) vs
Non-Archimedean (primorial distances, finite stages)


This gives four quadrants:


- QFT: (Elliptic, Archimedean) -- quantum field theory, path integrals

- GR-local: (Hyperbolic, Archimedean) -- general relativity, local Lorentzian

- Orthodox-nonarch: (Elliptic, NonArchimedean) -- p-adic physics, not mainstream

- tau: (Hyperbolic, NonArchimedean) -- the category-tau quadrant


**II.D74 (Unification Obstruction):** In the Archimedean column, QFT (elliptic)
and GR (hyperbolic) have incompatible PDE types. This is the structural reason
orthodox unification fails: no single Archimedean theory can be simultaneously
elliptic (for QFT renormalization) and hyperbolic (for GR wave propagation).

**II.T46 (Fourth Quadrant Resolution):** The tau framework lives in the fourth
quadrant (Hyperbolic, NonArchimedean). Since tau is NOT in the Archimedean
column, the unification obstruction does not apply. The non-Archimedean
metric resolves the PDE-type conflict because finite stages are always
Euclidean (II.T45), and the hyperbolic structure emerges only in the limit.

---

### `Tau.BookII.Mirror.PDEAxis`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L52-L56)
**inductive
Tau.BookII.Mirror.PDEAxis :Type**


[II.D73] PDE axis for physics classification.

- Elliptic : PDEAxis
- Hyperbolic : PDEAxis
Instances For

---

### `Tau.BookII.Mirror.instDecidableEqPDEAxis`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L56-L56)
**instance
Tau.BookII.Mirror.instDecidableEqPDEAxis :DecidableEq PDEAxis**

Equations
- Tau.BookII.Mirror.instDecidableEqPDEAxis x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookII.Mirror.instReprPDEAxis.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L56-L56)
**def
Tau.BookII.Mirror.instReprPDEAxis.repr :PDEAxis → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.instReprPDEAxis`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L56-L56)
**instance
Tau.BookII.Mirror.instReprPDEAxis :Repr PDEAxis**

Equations
- Tau.BookII.Mirror.instReprPDEAxis = { reprPrec := Tau.BookII.Mirror.instReprPDEAxis.repr }

---

### `Tau.BookII.Mirror.MetricAxis`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L58-L62)
**inductive
Tau.BookII.Mirror.MetricAxis :Type**


[II.D73] Metric axis for physics classification.

- Archimedean : MetricAxis
- NonArchimedean : MetricAxis
Instances For

---

### `Tau.BookII.Mirror.instDecidableEqMetricAxis`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L62-L62)
**instance
Tau.BookII.Mirror.instDecidableEqMetricAxis :DecidableEq MetricAxis**

Equations
- Tau.BookII.Mirror.instDecidableEqMetricAxis x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookII.Mirror.instReprMetricAxis`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L62-L62)
**instance
Tau.BookII.Mirror.instReprMetricAxis :Repr MetricAxis**

Equations
- Tau.BookII.Mirror.instReprMetricAxis = { reprPrec := Tau.BookII.Mirror.instReprMetricAxis.repr }

---

### `Tau.BookII.Mirror.instReprMetricAxis.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L62-L62)
**def
Tau.BookII.Mirror.instReprMetricAxis.repr :MetricAxis → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.PhysicsQuadrant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L66-L71)
**structure
Tau.BookII.Mirror.PhysicsQuadrant :Type**


[II.D73] A physics quadrant: a point in the PDE x Metric classification.

- pde : PDEAxis
- metric : MetricAxis
- description : String
Instances For

---

### `Tau.BookII.Mirror.instReprPhysicsQuadrant.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L71-L71)
**def
Tau.BookII.Mirror.instReprPhysicsQuadrant.repr :PhysicsQuadrant → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.instReprPhysicsQuadrant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L71-L71)
**instance
Tau.BookII.Mirror.instReprPhysicsQuadrant :Repr PhysicsQuadrant**

Equations
- Tau.BookII.Mirror.instReprPhysicsQuadrant = { reprPrec := Tau.BookII.Mirror.instReprPhysicsQuadrant.repr }

---

### `Tau.BookII.Mirror.qft_quadrant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L73-L77)
**def
Tau.BookII.Mirror.qft_quadrant :PhysicsQuadrant**


[II.D73] QFT quadrant: Elliptic, Archimedean.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.gr_local_quadrant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L79-L83)
**def
Tau.BookII.Mirror.gr_local_quadrant :PhysicsQuadrant**


[II.D73] GR-local quadrant: Hyperbolic, Archimedean.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.padic_quadrant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L85-L89)
**def
Tau.BookII.Mirror.padic_quadrant :PhysicsQuadrant**


[II.D73] Orthodox non-Archimedean quadrant: Elliptic, NonArchimedean.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.tau_quadrant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L91-L95)
**def
Tau.BookII.Mirror.tau_quadrant :PhysicsQuadrant**


[II.D73] The tau quadrant: Hyperbolic, NonArchimedean.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.all_quadrants`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L97-L99)
**def
Tau.BookII.Mirror.all_quadrants :List PhysicsQuadrant**


All four quadrants.
Equations
- Tau.BookII.Mirror.all_quadrants = [Tau.BookII.Mirror.qft_quadrant, Tau.BookII.Mirror.gr_local_quadrant, Tau.BookII.Mirror.padic_quadrant, Tau.BookII.Mirror.tau_quadrant]
Instances For

---

### `Tau.BookII.Mirror.quadrant_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L101-L102)
**theorem
Tau.BookII.Mirror.quadrant_count :all_quadrants.length = 4**


There are exactly 4 quadrants.

---

### `Tau.BookII.Mirror.same_archimedean_column`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L108-L110)
**def
Tau.BookII.Mirror.same_archimedean_column
(q1 q2 : PhysicsQuadrant)
 :Bool**


[II.D74] Check if two quadrants are in the same Archimedean column.
Equations
- Tau.BookII.Mirror.same_archimedean_column q1 q2 = (q1.metric == Tau.BookII.Mirror.MetricAxis.Archimedean && q2.metric == Tau.BookII.Mirror.MetricAxis.Archimedean)
Instances For

---

### `Tau.BookII.Mirror.compatible_pde`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L112-L114)
**def
Tau.BookII.Mirror.compatible_pde
(q1 q2 : PhysicsQuadrant)
 :Bool**


[II.D74] Check if two quadrants have compatible (same) PDE type.
Equations
- Tau.BookII.Mirror.compatible_pde q1 q2 = (q1.pde == q2.pde)
Instances For

---

### `Tau.BookII.Mirror.unification_obstructed`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L116-L120)
**def
Tau.BookII.Mirror.unification_obstructed
(q1 q2 : PhysicsQuadrant)
 :Bool**


[II.D74] Unification is obstructed when two theories are in the
same Archimedean column but have different PDE types.
This models the QFT/GR incompatibility.
Equations
- Tau.BookII.Mirror.unification_obstructed q1 q2 = (Tau.BookII.Mirror.same_archimedean_column q1 q2 && !Tau.BookII.Mirror.compatible_pde q1 q2)
Instances For

---

### `Tau.BookII.Mirror.qft_gr_same_column`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L122-L124)
**theorem
Tau.BookII.Mirror.qft_gr_same_column :same_archimedean_column qft_quadrant gr_local_quadrant = true**


[II.D74] QFT and GR are in the Archimedean column.

---

### `Tau.BookII.Mirror.qft_gr_incompatible_pde`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L126-L128)
**theorem
Tau.BookII.Mirror.qft_gr_incompatible_pde :compatible_pde qft_quadrant gr_local_quadrant = false**


[II.D74] QFT and GR have incompatible PDE types.

---

### `Tau.BookII.Mirror.qft_gr_obstructed`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L130-L132)
**theorem
Tau.BookII.Mirror.qft_gr_obstructed :unification_obstructed qft_quadrant gr_local_quadrant = true**


[II.D74] QFT/GR unification IS obstructed.

---

### `Tau.BookII.Mirror.tau_is_non_archimedean`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L138-L140)
**theorem
Tau.BookII.Mirror.tau_is_non_archimedean :tau_quadrant.metric = MetricAxis.NonArchimedean**


[II.T46] The tau quadrant is non-Archimedean.

---

### `Tau.BookII.Mirror.tau_is_hyperbolic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L142-L144)
**theorem
Tau.BookII.Mirror.tau_is_hyperbolic :tau_quadrant.pde = PDEAxis.Hyperbolic**


[II.T46] The tau quadrant is hyperbolic.

---

### `Tau.BookII.Mirror.tau_not_archimedean_with_qft`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L146-L148)
**theorem
Tau.BookII.Mirror.tau_not_archimedean_with_qft :same_archimedean_column tau_quadrant qft_quadrant = false**


[II.T46] Tau is NOT in the Archimedean column with QFT.

---

### `Tau.BookII.Mirror.tau_not_archimedean_with_gr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L150-L152)
**theorem
Tau.BookII.Mirror.tau_not_archimedean_with_gr :same_archimedean_column tau_quadrant gr_local_quadrant = false**


[II.T46] Tau is NOT in the Archimedean column with GR.

---

### `Tau.BookII.Mirror.tau_qft_not_obstructed`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L154-L156)
**theorem
Tau.BookII.Mirror.tau_qft_not_obstructed :unification_obstructed tau_quadrant qft_quadrant = false**


[II.T46] The unification obstruction does NOT apply to tau and QFT.

---

### `Tau.BookII.Mirror.tau_gr_not_obstructed`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L158-L160)
**theorem
Tau.BookII.Mirror.tau_gr_not_obstructed :unification_obstructed tau_quadrant gr_local_quadrant = false**


[II.T46] The unification obstruction does NOT apply to tau and GR.

---

### `Tau.BookII.Mirror.tau_escapes_obstruction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L162-L168)
**theorem
Tau.BookII.Mirror.tau_escapes_obstruction :tau_quadrant.metric = MetricAxis.NonArchimedean ∧ unification_obstructed tau_quadrant qft_quadrant = false ∧ unification_obstructed tau_quadrant gr_local_quadrant = false**


[II.T46] Fourth quadrant resolution: tau escapes the obstruction because
it is in the non-Archimedean column.

---

### `Tau.BookII.Mirror.tau_distinct_from_qft`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L170-L173)
**theorem
Tau.BookII.Mirror.tau_distinct_from_qft :tau_quadrant.pde ≠ qft_quadrant.pde**


[II.T46] The tau quadrant is structurally distinct from both QFT and GR.

---

### `Tau.BookII.Mirror.tau_distinct_from_gr_metric`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L175-L177)
**theorem
Tau.BookII.Mirror.tau_distinct_from_gr_metric :tau_quadrant.metric ≠ gr_local_quadrant.metric**


---

### `Tau.BookII.Mirror.is_non_archimedean`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L183-L185)
**def
Tau.BookII.Mirror.is_non_archimedean
(q : PhysicsQuadrant)
 :Bool**


Check if a quadrant is in the non-Archimedean column.
Equations
- Tau.BookII.Mirror.is_non_archimedean q = (q.metric == Tau.BookII.Mirror.MetricAxis.NonArchimedean)
Instances For

---

### `Tau.BookII.Mirror.non_archimedean_quadrants`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L187-L189)
**def
Tau.BookII.Mirror.non_archimedean_quadrants :List PhysicsQuadrant**


The non-Archimedean quadrants.
Equations
- Tau.BookII.Mirror.non_archimedean_quadrants = List.filter Tau.BookII.Mirror.is_non_archimedean Tau.BookII.Mirror.all_quadrants
Instances For

---

### `Tau.BookII.Mirror.archimedean_quadrants`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L191-L193)
**def
Tau.BookII.Mirror.archimedean_quadrants :List PhysicsQuadrant**


The Archimedean quadrants.
Equations
- Tau.BookII.Mirror.archimedean_quadrants = List.filter (fun (q : Tau.BookII.Mirror.PhysicsQuadrant) => q.metric == Tau.BookII.Mirror.MetricAxis.Archimedean)
 Tau.BookII.Mirror.all_quadrants
Instances For

---

### `Tau.BookII.Mirror.non_arch_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L195-L197)
**theorem
Tau.BookII.Mirror.non_arch_count :non_archimedean_quadrants.length = 2**


There are exactly 2 non-Archimedean quadrants.

---

### `Tau.BookII.Mirror.arch_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L199-L201)
**theorem
Tau.BookII.Mirror.arch_count :archimedean_quadrants.length = 2**


There are exactly 2 Archimedean quadrants.

---

### `Tau.BookII.Mirror.obstruction_in_archimedean`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L203-L208)
**def
Tau.BookII.Mirror.obstruction_in_archimedean :Bool**


The obstruction exists only in the Archimedean column.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.obstruction_confined`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L210-L212)
**theorem
Tau.BookII.Mirror.obstruction_confined :obstruction_in_archimedean = true**


The obstruction is confined to the Archimedean column.

---

### `Tau.BookII.Mirror.pde_axis_exhaustive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L218-L221)
**theorem
Tau.BookII.Mirror.pde_axis_exhaustive
(a : PDEAxis)
 :a = PDEAxis.Elliptic ∨ a = PDEAxis.Hyperbolic**


PDEAxis has exactly 2 values.

---

### `Tau.BookII.Mirror.metric_axis_exhaustive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L223-L226)
**theorem
Tau.BookII.Mirror.metric_axis_exhaustive
(a : MetricAxis)
 :a = MetricAxis.Archimedean ∨ a = MetricAxis.NonArchimedean**


MetricAxis has exactly 2 values.

---

### `Tau.BookII.Mirror.same_pde_not_obstructed`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L228-L232)
**theorem
Tau.BookII.Mirror.same_pde_not_obstructed
(q1 q2 : PhysicsQuadrant)
 :compatible_pde q1 q2 = true → unification_obstructed q1 q2 = false**


Two quadrants in the same column with the same PDE type are NOT obstructed.

---

### `Tau.BookII.Mirror.different_column_not_obstructed`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L234-L238)
**theorem
Tau.BookII.Mirror.different_column_not_obstructed
(q1 q2 : PhysicsQuadrant)

(h : same_archimedean_column q1 q2 = false)
 :unification_obstructed q1 q2 = false**


Two quadrants in different columns are NOT obstructed.

---

### `Tau.BookII.Mirror.four_quadrants`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L275-L276)
**theorem
Tau.BookII.Mirror.four_quadrants :all_quadrants.length = 4**


---

### `Tau.BookII.Mirror.qft_gr_obstructed_native`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L279-L280)
**theorem
Tau.BookII.Mirror.qft_gr_obstructed_native :unification_obstructed qft_quadrant gr_local_quadrant = true**


---

### `Tau.BookII.Mirror.tau_escapes_qft`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L283-L284)
**theorem
Tau.BookII.Mirror.tau_escapes_qft :unification_obstructed tau_quadrant qft_quadrant = false**


---

### `Tau.BookII.Mirror.tau_escapes_gr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L286-L287)
**theorem
Tau.BookII.Mirror.tau_escapes_gr :unification_obstructed tau_quadrant gr_local_quadrant = false**


---

### `Tau.BookII.Mirror.tau_hyp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L290-L291)
**theorem
Tau.BookII.Mirror.tau_hyp :tau_quadrant.pde = PDEAxis.Hyperbolic**


---

### `Tau.BookII.Mirror.tau_non_arch`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L293-L294)
**theorem
Tau.BookII.Mirror.tau_non_arch :tau_quadrant.metric = MetricAxis.NonArchimedean**


---

### `Tau.BookII.Mirror.obstruction_confined_native`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L297-L298)
**theorem
Tau.BookII.Mirror.obstruction_confined_native :obstruction_in_archimedean = true**


---

### `Tau.BookII.Mirror.arch_plus_nonarch`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/PhysicsQuadrant.lean#L301-L302)
**theorem
Tau.BookII.Mirror.arch_plus_nonarch :archimedean_quadrants.length + non_archimedean_quadrants.length = 4**
