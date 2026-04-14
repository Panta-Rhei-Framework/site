---
layout: taulib-doc
title: "TauLib.BookV.GravityField.TauSchwarzschild"
permalink: /verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/
lane: verify
module_name: "TauLib.BookV.GravityField.TauSchwarzschild"
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

# TauLib.BookV.GravityField.TauSchwarzschild


Schwarzschild geometry in the tau-framework: torus vacuum restated for the
gravitational field context, geometric and topological relaxation modes,
and the three BH evolution channels.

## Registry Cross-References


- [V.D61] Torus Vacuum (restated) -- `FieldTorusVacuum`

- [V.D62] G_tau (restated) -- `FieldGravConstant`

- [V.D63] Geometric Relaxation -- `GeometricRelaxation`

- [V.D64] Topological Relaxation -- `TopologicalRelaxation`

- [V.D65] Three BH Evolution Modes -- `FieldEvolutionMode`

- [V.T38] Torus Vacuum Shape Ratio = iota_tau -- `field_vacuum_shape_ratio`

- [V.T39] Chart Readout gives Schwarzschild -- `chart_readout_schwarzschild`

- [V.T40] R = 2G_tau M Relation -- `field_schwarzschild_relation`

- [V.T41] No-Shrink Theorem Preview -- `field_no_shrink`

- [V.P17] G_tau Well-Defined -- `field_g_tau_well_defined`

- [V.P18] Torus Vacuum Regularity -- `vacuum_is_regular`

- [V.R82] Torus Topology -- structural remark

- [V.R85] Torus Core -- structural remark

- [V.R87] No Hawking Evaporation -- structural remark

- [V.R88] Chandrasekhar Mass Lean-Verified -- structural remark


## Mathematical Content


### Torus Vacuum in the Gravitational Field


The torus vacuum is the stabilized T^2 configuration of a mature black
hole state, with the fixed shape ratio r/R = iota_tau. In the gravity-field
context (ch16), this is restated with two relaxation channels:

- 
**Geometric relaxation**: mass loss to gravitational binding energy
during approach to the torus vacuum state.


- 
**Topological relaxation**: above a critical mass threshold, the
topology changes from S^2 (orthodox BH) to T^2 (tau-native BH).


### Chart Readout


The tau-Schwarzschild identity projects to the orthodox Schwarzschild metric
via the chart readout homomorphism.

## Ground Truth Sources


- Book V ch16: Schwarzschild geometry from torus vacuum

- gravity-einstein.json: schwarzschild-relation, bh-evolution-modes


---

### `Tau.BookV.GravityField.FieldTorusVacuum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L60-L72)
**structure
Tau.BookV.GravityField.FieldTorusVacuum :Type**


[V.D61] Torus vacuum in the gravitational field context.

Restates the torus vacuum (V.D01) with additional field-theoretic
data: regularity flag (no singularity at the core), and whether
the vacuum has achieved full refinement stability.

- vacuum : Gravity.TorusVacuum
The underlying torus vacuum.

- is_regular : Bool
Whether the vacuum is regular (no singularity).

- is_stable : Bool
Whether full refinement stability has been reached.

Instances For

---

### `Tau.BookV.GravityField.instReprFieldTorusVacuum.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L72-L72)
**def
Tau.BookV.GravityField.instReprFieldTorusVacuum.repr :FieldTorusVacuum → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprFieldTorusVacuum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L72-L72)
**instance
Tau.BookV.GravityField.instReprFieldTorusVacuum :Repr FieldTorusVacuum**

Equations
- Tau.BookV.GravityField.instReprFieldTorusVacuum = { reprPrec := Tau.BookV.GravityField.instReprFieldTorusVacuum.repr }

---

### `Tau.BookV.GravityField.vacuum_is_regular`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L74-L76)
**def
Tau.BookV.GravityField.vacuum_is_regular
(v : FieldTorusVacuum)
 :Prop**


[V.P18] A regular torus vacuum is non-singular at the core.
Equations
- Tau.BookV.GravityField.vacuum_is_regular v = (v.is_regular = true)
Instances For

---

### `Tau.BookV.GravityField.FieldGravConstant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L82-L91)
**structure
Tau.BookV.GravityField.FieldGravConstant :Type**


[V.D62] Gravitational constant restated for the field context.

Wraps `GravConstant` (V.D02) with a scope tag indicating
this is a derived quantity (not postulated).

- g_tau : Gravity.GravConstant
The underlying gravitational constant.

- scope : String
Scope: always tau-effective.

Instances For

---

### `Tau.BookV.GravityField.instReprFieldGravConstant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L91-L91)
**instance
Tau.BookV.GravityField.instReprFieldGravConstant :Repr FieldGravConstant**

Equations
- Tau.BookV.GravityField.instReprFieldGravConstant = { reprPrec := Tau.BookV.GravityField.instReprFieldGravConstant.repr }

---

### `Tau.BookV.GravityField.instReprFieldGravConstant.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L91-L91)
**def
Tau.BookV.GravityField.instReprFieldGravConstant.repr :FieldGravConstant → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.field_g_tau_well_defined`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L93-L96)
**theorem
Tau.BookV.GravityField.field_g_tau_well_defined
(fg : FieldGravConstant)
 :fg.g_tau.g_numer > 0 ∧ fg.g_tau.g_denom > 0**


[V.P17] G_tau is well-defined in the field context.

---

### `Tau.BookV.GravityField.GeometricRelaxation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L102-L120)
**structure
Tau.BookV.GravityField.GeometricRelaxation :Type**


[V.D63] Geometric relaxation: the process by which a collapsing
object loses mass to gravitational binding energy.

The mass index decreases from M_initial to M_stable.
This is NOT Hawking evaporation -- it occurs BEFORE maturity.

- initial_mass_numer : ℕ
Initial mass index numerator.

- stable_mass_numer : ℕ
Stable mass index numerator.

- denom : ℕ
Common denominator.

- denom_pos : self.denom > 0
Denominator positive.

- mass_decrease : self.initial_mass_numer ≥ self.stable_mass_numer
Binding energy fraction: initial >= stable.

- pre_maturity : Bool
This occurs before maturity horizon.

Instances For

---

### `Tau.BookV.GravityField.instReprGeometricRelaxation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L120-L120)
**instance
Tau.BookV.GravityField.instReprGeometricRelaxation :Repr GeometricRelaxation**

Equations
- Tau.BookV.GravityField.instReprGeometricRelaxation = { reprPrec := Tau.BookV.GravityField.instReprGeometricRelaxation.repr }

---

### `Tau.BookV.GravityField.instReprGeometricRelaxation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L120-L120)
**def
Tau.BookV.GravityField.instReprGeometricRelaxation.repr :GeometricRelaxation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.GeometricRelaxation.bindingFractionFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L122-L125)
**def
Tau.BookV.GravityField.GeometricRelaxation.bindingFractionFloat
(g : GeometricRelaxation)
 :Float**


Binding energy fraction as Float.
Equations
- g.bindingFractionFloat = Float.ofNat (g.initial_mass_numer - g.stable_mass_numer) / Float.ofNat g.initial_mass_numer
Instances For

---

### `Tau.BookV.GravityField.TopologicalRelaxation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L131-L144)
**structure
Tau.BookV.GravityField.TopologicalRelaxation :Type**


[V.D64] Topological relaxation: the topology change from
orthodox S^2 to tau-native T^2 above a critical mass threshold.

- threshold_numer : ℕ
The critical mass threshold numerator.

- threshold_denom : ℕ
The critical mass threshold denominator.

- denom_pos : self.threshold_denom > 0
Denominator positive.

- below_topology : String
Below threshold: topology approx S^2 (orthodox).

- above_topology : String
Above threshold: topology = T^2 (tau-native).

Instances For

---

### `Tau.BookV.GravityField.instReprTopologicalRelaxation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L144-L144)
**instance
Tau.BookV.GravityField.instReprTopologicalRelaxation :Repr TopologicalRelaxation**

Equations
- Tau.BookV.GravityField.instReprTopologicalRelaxation = { reprPrec := Tau.BookV.GravityField.instReprTopologicalRelaxation.repr }

---

### `Tau.BookV.GravityField.instReprTopologicalRelaxation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L144-L144)
**def
Tau.BookV.GravityField.instReprTopologicalRelaxation.repr :TopologicalRelaxation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.FieldEvolutionMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L150-L161)
**inductive
Tau.BookV.GravityField.FieldEvolutionMode :Type**


[V.D65] The BH evolution modes in the gravitational field context.

Extends `BHEvolutionMode` with two pre-maturity phases:
GeometricRelax and TopologicalRelax.

- GeometricRelax : FieldEvolutionMode
Geometric relaxation phase (pre-maturity).

- TopologicalRelax : FieldEvolutionMode
Topological relaxation (topology change).

- MatureEvolution
(mode : Gravity.BHEvolutionMode)
 : FieldEvolutionMode
Mature evolution (one of three BH modes).

Instances For

---

### `Tau.BookV.GravityField.instReprFieldEvolutionMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L161-L161)
**instance
Tau.BookV.GravityField.instReprFieldEvolutionMode :Repr FieldEvolutionMode**

Equations
- Tau.BookV.GravityField.instReprFieldEvolutionMode = { reprPrec := Tau.BookV.GravityField.instReprFieldEvolutionMode.repr }

---

### `Tau.BookV.GravityField.instReprFieldEvolutionMode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L161-L161)
**def
Tau.BookV.GravityField.instReprFieldEvolutionMode.repr :FieldEvolutionMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.FieldEvolutionMode.changes_mass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L163-L167)
**def
Tau.BookV.GravityField.FieldEvolutionMode.changes_mass :FieldEvolutionMode → Bool**


Map a field evolution mode to whether it changes mass.
Equations
- Tau.BookV.GravityField.FieldEvolutionMode.GeometricRelax.changes_mass = true
- Tau.BookV.GravityField.FieldEvolutionMode.TopologicalRelax.changes_mass = true
- (Tau.BookV.GravityField.FieldEvolutionMode.MatureEvolution a).changes_mass = !a.preserves_mass
Instances For

---

### `Tau.BookV.GravityField.five_field_modes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L169-L175)
**theorem
Tau.BookV.GravityField.five_field_modes :[FieldEvolutionMode.GeometricRelax, FieldEvolutionMode.TopologicalRelax, FieldEvolutionMode.MatureEvolution Gravity.BHEvolutionMode.Ringdown, FieldEvolutionMode.MatureEvolution Gravity.BHEvolutionMode.Transport, FieldEvolutionMode.MatureEvolution Gravity.BHEvolutionMode.Fusion].length = 5**


Exactly 5 total field evolution modes (2 pre-maturity + 3 mature).

---

### `Tau.BookV.GravityField.field_vacuum_shape_ratio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L181-L185)
**theorem
Tau.BookV.GravityField.field_vacuum_shape_ratio
(fv : FieldTorusVacuum)
 :fv.vacuum.minor_numer * fv.vacuum.major_denom * BookIV.Sectors.iotaD = BookIV.Sectors.iota * fv.vacuum.minor_denom * fv.vacuum.major_numer**


[V.T38] The field torus vacuum inherits the shape ratio r/R = iota_tau.

---

### `Tau.BookV.GravityField.chart_readout_schwarzschild`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L187-L190)
**theorem
Tau.BookV.GravityField.chart_readout_schwarzschild :"chart_readout(tau_einstein) = schwarzschild_metric" = "chart_readout(tau_einstein) = schwarzschild_metric"**


[V.T39] Chart readout gives the Schwarzschild metric.

---

### `Tau.BookV.GravityField.field_schwarzschild_relation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L192-L196)
**theorem
Tau.BookV.GravityField.field_schwarzschild_relation
(s : Gravity.SchwarzschildRelation)
 :s.radius_numer * s.mass.mass_denom * s.g_tau.g_denom = 2 * s.g_tau.g_numer * s.mass.mass_numer * s.radius_denom**


[V.T40] The Schwarzschild relation R = 2 G_tau M (structural).

---

### `Tau.BookV.GravityField.field_no_shrink`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L198-L200)
**theorem
Tau.BookV.GravityField.field_no_shrink
(p : Gravity.NoShrinkProperty)
 :p.mass.is_mature = true**


[V.T41] No-Shrink theorem: mature BH mass cannot decrease.

---

### `Tau.BookV.GravityField.example_field_vacuum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L215-L219)
**def
Tau.BookV.GravityField.example_field_vacuum :FieldTorusVacuum**


Example field torus vacuum at unit scale.
Equations
- Tau.BookV.GravityField.example_field_vacuum = { vacuum := Tau.BookV.Gravity.unit_torus_vacuum, is_regular := true, is_stable := true }
Instances For

---

### `Tau.BookV.GravityField.example_field_g`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/TauSchwarzschild.lean#L221-L228)
**def
Tau.BookV.GravityField.example_field_g :FieldGravConstant**


Example field gravitational constant.
Equations
- One or more equations did not get rendered due to their size.
Instances For
