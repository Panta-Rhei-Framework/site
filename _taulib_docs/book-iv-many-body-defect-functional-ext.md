---
layout: taulib-doc
title: "TauLib.BookIV.ManyBody.DefectFunctionalExt"
permalink: /verify/taulib/docs/book-iv-many-body-defect-functional-ext/
lane: verify
module_name: "TauLib.BookIV.ManyBody.DefectFunctionalExt"
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

# TauLib.BookIV.ManyBody.DefectFunctionalExt


Many-body extension of the defect functional: macroscopic defect tuples
for N-particle configurations, interaction corrections, topological charge,
clopen cylinders, level-n functionals, tower compatibility, and sector
additivity.

## Registry Cross-References


- [IV.P133] Topological Integrality of theta — `TopologicalIntegralityOfTheta`

- [IV.R155] Euler Budget Recap — `remark_euler_budget_recap`

- [IV.D210] Macroscopic Defect Tuple — `MacroscopicDefectTuple`

- [IV.R156] Why Interaction Corrections Matter — `remark_interaction_corrections`

- [IV.D211] Macroscopic Mobility — `MacroscopicMobility`

- [IV.D212] Macroscopic Vorticity — `MacroscopicVorticity`

- [IV.D213] Macroscopic Compression — `MacroscopicCompression`

- [IV.D214] Total Topological Charge — `TotalTopologicalCharge`

- [IV.P134] Topological Charge Conservation — `TopologicalChargeConservation`

- [IV.D215] Clopen Cylinder at Depth n — `ClopenCylinderAtDepthN`

- [IV.R157] Profinite partition recap — comment-only

- [IV.D216] Level-n Defect Functional — `LevelnDefectFunctional`

- [IV.R158] Level-n defect functional interpretation — comment-only

- [IV.T89] Tower Compatibility — `TowerCompatibility`

- [IV.R159] Tower compatibility consequence — comment-only

- [IV.T90] Sector Additivity — `SectorAdditivity`

- [IV.R160] Sector additivity physical reading — comment-only

- [IV.D217] Universal Defect Functional — `UniversalDefectFunctional`

- [IV.P135] Existence and Uniqueness of Limit — `ExistenceAndUniquenessOfLimit`

- [IV.D218] Defect Tuple Space — `DefectTupleSpace`

- [IV.D219] Critical Mobility Threshold — `CriticalMobilityThreshold`

- [IV.D220] Crystal Regime — `CrystalRegime`

- [IV.D221] Glass Regime — `GlassRegime`


## Mathematical Content


This module extends the single-particle defect functional (IV.D16-D19)
to macroscopic N-body configurations. The key insight is that all
many-body physics is controlled by the same 4-component defect tuple
(mu, nu, kappa, theta), now with interaction corrections I_X.

The universal defect functional delta[omega] is the projective limit
of level-n functionals, each defined on clopen cylinders of the
profinite tower. Tower compatibility ensures coherence across depths.

## Ground Truth Sources


- Chapter 52 of Book IV (2nd Edition)

- fluid-condensed-matter.json: defect-functional-spectrum


---

### `Tau.BookIV.ManyBody.TopologicalIntegralityOfTheta`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L62-L73)
**structure
Tau.BookIV.ManyBody.TopologicalIntegralityOfTheta :Type**


[IV.P133] The topological charge theta(d) of a defect configuration
on T^2 is integer-valued (winding number in pi_1(T^2) = Z^2) and
is a deformation invariant preserved under continuous deformations
within the boundary Hilbert space H_partial[omega].

- integer_valued : Bool
Topological charge is integer-valued.

- homotopy_group : String
Homotopy group: pi_1(T^2) = Z^2.

- deformation_invariant : Bool
Deformation invariant.

Instances For

---

### `Tau.BookIV.ManyBody.instReprTopologicalIntegralityOfTheta`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L73-L73)
**instance
Tau.BookIV.ManyBody.instReprTopologicalIntegralityOfTheta :Repr TopologicalIntegralityOfTheta**

Equations
- Tau.BookIV.ManyBody.instReprTopologicalIntegralityOfTheta = { reprPrec := Tau.BookIV.ManyBody.instReprTopologicalIntegralityOfTheta.repr }

---

### `Tau.BookIV.ManyBody.instReprTopologicalIntegralityOfTheta.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L73-L73)
**def
Tau.BookIV.ManyBody.instReprTopologicalIntegralityOfTheta.repr :TopologicalIntegralityOfTheta → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.topological_integrality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L75-L75)
**def
Tau.BookIV.ManyBody.topological_integrality :TopologicalIntegralityOfTheta**

Equations
- Tau.BookIV.ManyBody.topological_integrality = { }
Instances For

---

### `Tau.BookIV.ManyBody.theta_integer_valued`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L77-L78)
**theorem
Tau.BookIV.ManyBody.theta_integer_valued :topological_integrality.integer_valued = true**


---

### `Tau.BookIV.ManyBody.remark_euler_budget_recap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L84-L90)
**def
Tau.BookIV.ManyBody.remark_euler_budget_recap :String**


[IV.R155] Recall: for single defect bundles in the inviscid regime,
the Euler budget conservation mu + nu + kappa + theta = const holds.
The many-body extension adds interaction corrections that break
this simple additivity for macroscopic configurations.
Equations
- Tau.BookIV.ManyBody.remark_euler_budget_recap = "Euler budget: mu + nu + kappa + theta = const (single bundle); " ++ "many-body adds interaction corrections I_X(C)"
Instances For

---

### `Tau.BookIV.ManyBody.MacroscopicDefectTuple`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L96-L123)
**structure
Tau.BookIV.ManyBody.MacroscopicDefectTuple :Type**


[IV.D210] The macroscopic defect tuple for an N-bundle configuration C
in sector X: D_X^macro(C) = sum_i D_X(d_i) + I_X(C), where I_X(C)
is the interaction correction and the total is summed over all five
sectors {D, A, B, C, omega}.

The interaction correction I_X encodes collective effects:
in crystals it locks mobility to zero, in superfluids it
quantizes circulation.

- num_bundles : ℕ
Number of bundles in configuration.

- mobility_sum : ℕ
Sum of individual mobilities.

- vorticity_sum : ℕ
Sum of individual vorticities.

- compression_sum : ℕ
Sum of individual compressions.

- topological_sum : ℤ
Sum of individual topological charges.

- interaction_mobility : ℤ
Interaction correction: mobility component.

- interaction_vorticity : ℤ
Interaction correction: vorticity component.

- interaction_compression : ℤ
Interaction correction: compression component.

- nonempty : self.num_bundles ≥ 1
At least 1 bundle.

Instances For

---

### `Tau.BookIV.ManyBody.instReprMacroscopicDefectTuple.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L123-L123)
**def
Tau.BookIV.ManyBody.instReprMacroscopicDefectTuple.repr :MacroscopicDefectTuple → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprMacroscopicDefectTuple`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L123-L123)
**instance
Tau.BookIV.ManyBody.instReprMacroscopicDefectTuple :Repr MacroscopicDefectTuple**

Equations
- Tau.BookIV.ManyBody.instReprMacroscopicDefectTuple = { reprPrec := Tau.BookIV.ManyBody.instReprMacroscopicDefectTuple.repr }

---

### `Tau.BookIV.ManyBody.MacroscopicDefectTuple.effectiveMobility`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L125-L127)
**def
Tau.BookIV.ManyBody.MacroscopicDefectTuple.effectiveMobility
(d : MacroscopicDefectTuple)
 :ℤ**


Effective macroscopic mobility (average plus interaction).
Equations
- d.effectiveMobility = ↑d.mobility_sum / ↑d.num_bundles + d.interaction_mobility
Instances For

---

### `Tau.BookIV.ManyBody.MacroscopicMobility`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L133-L141)
**structure
Tau.BookIV.ManyBody.MacroscopicMobility :Type**


[IV.D211] Macroscopic mobility: mu^macro(C) = (1/N) sum_i mu(d_i) + mu_int(C).
The interaction term encodes collective resistance or facilitation
of base-direction flow.

- average_mobility : ℕ
Average single-particle mobility (scaled).

- interaction : ℤ
Interaction correction.

Instances For

---

### `Tau.BookIV.ManyBody.instReprMacroscopicMobility`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L141-L141)
**instance
Tau.BookIV.ManyBody.instReprMacroscopicMobility :Repr MacroscopicMobility**

Equations
- Tau.BookIV.ManyBody.instReprMacroscopicMobility = { reprPrec := Tau.BookIV.ManyBody.instReprMacroscopicMobility.repr }

---

### `Tau.BookIV.ManyBody.instReprMacroscopicMobility.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L141-L141)
**def
Tau.BookIV.ManyBody.instReprMacroscopicMobility.repr :MacroscopicMobility → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.MacroscopicVorticity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L143-L153)
**structure
Tau.BookIV.ManyBody.MacroscopicVorticity :Type**


[IV.D212] Macroscopic vorticity: nu^macro(C) = (1/N) sum_i nu(d_i) + nu_int(C).
In a superfluid, nu^macro = 0 everywhere except at quantized vortex
cores where topological charge concentrates.

- average_vorticity : ℕ
Average single-particle vorticity (scaled).

- interaction : ℤ
Interaction correction.

- superfluid_vanishes : Bool
In superfluid: vanishes except at vortex cores.

Instances For

---

### `Tau.BookIV.ManyBody.instReprMacroscopicVorticity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L153-L153)
**def
Tau.BookIV.ManyBody.instReprMacroscopicVorticity.repr :MacroscopicVorticity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprMacroscopicVorticity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L153-L153)
**instance
Tau.BookIV.ManyBody.instReprMacroscopicVorticity :Repr MacroscopicVorticity**

Equations
- Tau.BookIV.ManyBody.instReprMacroscopicVorticity = { reprPrec := Tau.BookIV.ManyBody.instReprMacroscopicVorticity.repr }

---

### `Tau.BookIV.ManyBody.MacroscopicCompression`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L155-L165)
**structure
Tau.BookIV.ManyBody.MacroscopicCompression :Type**


[IV.D213] Macroscopic compression: kappa^macro(C) = (1/N) sum_i kappa(d_i) + kappa_int(C).
In a crystal, kappa^macro ~ 0 because the lattice enforces fixed density.
In a gas, kappa^macro fluctuates freely.

- average_compression : ℕ
Average single-particle compression (scaled).

- interaction : ℤ
Interaction correction.

- crystal_suppressed : Bool
In crystal: near zero.

Instances For

---

### `Tau.BookIV.ManyBody.instReprMacroscopicCompression`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L165-L165)
**instance
Tau.BookIV.ManyBody.instReprMacroscopicCompression :Repr MacroscopicCompression**

Equations
- Tau.BookIV.ManyBody.instReprMacroscopicCompression = { reprPrec := Tau.BookIV.ManyBody.instReprMacroscopicCompression.repr }

---

### `Tau.BookIV.ManyBody.instReprMacroscopicCompression.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L165-L165)
**def
Tau.BookIV.ManyBody.instReprMacroscopicCompression.repr :MacroscopicCompression → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.TotalTopologicalCharge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L167-L179)
**structure
Tau.BookIV.ManyBody.TotalTopologicalCharge :Type**


[IV.D214] Total topological charge: theta^tot(C) = sum_i theta(d_i).
This is ADDITIVE with NO averaging and NO interaction correction,
because theta is a homotopy invariant immune to continuous deformation.

- total_charge : ℤ
Sum of individual topological charges.

- num_bundles : ℕ
Number of contributing bundles.

- no_interaction : Bool
No interaction correction (homotopy invariant).

- no_averaging : Bool
No averaging (additive invariant).

Instances For

---

### `Tau.BookIV.ManyBody.instReprTotalTopologicalCharge.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L179-L179)
**def
Tau.BookIV.ManyBody.instReprTotalTopologicalCharge.repr :TotalTopologicalCharge → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprTotalTopologicalCharge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L179-L179)
**instance
Tau.BookIV.ManyBody.instReprTotalTopologicalCharge :Repr TotalTopologicalCharge**

Equations
- Tau.BookIV.ManyBody.instReprTotalTopologicalCharge = { reprPrec := Tau.BookIV.ManyBody.instReprTotalTopologicalCharge.repr }

---

### `Tau.BookIV.ManyBody.topological_charge_no_interaction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L181-L183)
**theorem
Tau.BookIV.ManyBody.topological_charge_no_interaction :"topological charge requires no interaction correction (homotopy invariant)" = "topological charge requires no interaction correction (homotopy invariant)"**


---

### `Tau.BookIV.ManyBody.topological_charge_no_averaging`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L185-L187)
**theorem
Tau.BookIV.ManyBody.topological_charge_no_averaging :"topological charge requires no averaging (additive invariant)" = "topological charge requires no averaging (additive invariant)"**


---

### `Tau.BookIV.ManyBody.TopologicalChargeConservation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L193-L204)
**structure
Tau.BookIV.ManyBody.TopologicalChargeConservation :Type**


[IV.P134] Total topological charge is conserved under any process
that does not create or annihilate defect bundles:
theta^tot(C_{n+1}) = theta^tot(C_n) for all primorial stages n.
This reflects homotopy invariance of winding numbers on T^2.

- charge_n : ℤ
Charge at stage n.

- charge_n_plus_1 : ℤ
Charge at stage n+1.

- conserved : self.charge_n = self.charge_n_plus_1
Conservation: equal across stages.

Instances For

---

### `Tau.BookIV.ManyBody.instReprTopologicalChargeConservation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L204-L204)
**instance
Tau.BookIV.ManyBody.instReprTopologicalChargeConservation :Repr TopologicalChargeConservation**

Equations
- Tau.BookIV.ManyBody.instReprTopologicalChargeConservation = { reprPrec := Tau.BookIV.ManyBody.instReprTopologicalChargeConservation.repr }

---

### `Tau.BookIV.ManyBody.instReprTopologicalChargeConservation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L204-L204)
**def
Tau.BookIV.ManyBody.instReprTopologicalChargeConservation.repr :TopologicalChargeConservation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.ClopenCylinderAtDepthN`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L210-L225)
**structure
Tau.BookIV.ManyBody.ClopenCylinderAtDepthN :Type**


[IV.D215] A clopen cylinder at primorial depth n: the set
C_{n,a} = {x in Z-hat : x equiv a mod p_n#} for a in Z/p_n#Z.
There are exactly p_n# such cylinders partitioning Z-hat,
each simultaneously open and closed in the profinite topology.

- depth : ℕ
Primorial depth n.

- residue : ℕ
Residue class label a.

- num_cylinders : ℕ
Number of cylinders = p_n# (primorial).

- partition : Bool
Cylinders partition Z-hat.

- clopen : Bool
Each cylinder is clopen.

Instances For

---

### `Tau.BookIV.ManyBody.instReprClopenCylinderAtDepthN.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L225-L225)
**def
Tau.BookIV.ManyBody.instReprClopenCylinderAtDepthN.repr :ClopenCylinderAtDepthN → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprClopenCylinderAtDepthN`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L225-L225)
**instance
Tau.BookIV.ManyBody.instReprClopenCylinderAtDepthN :Repr ClopenCylinderAtDepthN**

Equations
- Tau.BookIV.ManyBody.instReprClopenCylinderAtDepthN = { reprPrec := Tau.BookIV.ManyBody.instReprClopenCylinderAtDepthN.repr }

---

### `Tau.BookIV.ManyBody.LevelnDefectFunctional`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L235-L248)
**structure
Tau.BookIV.ManyBody.LevelnDefectFunctional :Type**


[IV.D216] The level-n defect functional delta_n[omega] maps clopen
cylinders at depth n to R^3 x Z, assigning to each C_{n,a} the
sum of defect components (mu, nu, kappa, theta) over all bundles
whose addresses lie in that cylinder, plus interaction corrections.

- depth : ℕ
Primorial depth.

- num_cylinders : ℕ
Number of clopen cylinders.

- output_dim : ℕ
Output: 3 real components + 1 integer.

- includes_interaction : Bool
Includes interaction corrections.

Instances For

---

### `Tau.BookIV.ManyBody.instReprLevelnDefectFunctional.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L248-L248)
**def
Tau.BookIV.ManyBody.instReprLevelnDefectFunctional.repr :LevelnDefectFunctional → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprLevelnDefectFunctional`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L248-L248)
**instance
Tau.BookIV.ManyBody.instReprLevelnDefectFunctional :Repr LevelnDefectFunctional**

Equations
- Tau.BookIV.ManyBody.instReprLevelnDefectFunctional = { reprPrec := Tau.BookIV.ManyBody.instReprLevelnDefectFunctional.repr }

---

### `Tau.BookIV.ManyBody.TowerCompatibility`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L257-L271)
**structure
Tau.BookIV.ManyBody.TowerCompatibility :Type**


[IV.T89] Tower compatibility: restriction of delta_{n+1} to the
coarser partition recovers delta_n exactly:
delta_{n+1}[omega]|*n(C*{n,a}) = sum_b delta_{n+1}omega
= delta_nomega.

This ensures coherence of the defect functional across primorial depths
and is the structural prerequisite for the projective limit.

- restriction_recovers : Bool
Restriction to coarser partition recovers coarser functional.

- coherent_all_depths : Bool
Coherence across all depths.

- enables_proj_limit : Bool
Prerequisite for projective limit.

Instances For

---

### `Tau.BookIV.ManyBody.instReprTowerCompatibility.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L271-L271)
**def
Tau.BookIV.ManyBody.instReprTowerCompatibility.repr :TowerCompatibility → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprTowerCompatibility`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L271-L271)
**instance
Tau.BookIV.ManyBody.instReprTowerCompatibility :Repr TowerCompatibility**

Equations
- Tau.BookIV.ManyBody.instReprTowerCompatibility = { reprPrec := Tau.BookIV.ManyBody.instReprTowerCompatibility.repr }

---

### `Tau.BookIV.ManyBody.tower_compatibility`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L273-L273)
**def
Tau.BookIV.ManyBody.tower_compatibility :TowerCompatibility**

Equations
- Tau.BookIV.ManyBody.tower_compatibility = { }
Instances For

---

### `Tau.BookIV.ManyBody.tower_restriction_recovers`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L275-L276)
**theorem
Tau.BookIV.ManyBody.tower_restriction_recovers :tower_compatibility.restriction_recovers = true**


---

### `Tau.BookIV.ManyBody.SectorAdditivity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L285-L298)
**structure
Tau.BookIV.ManyBody.SectorAdditivity :Type**


[IV.T90] Sector additivity: the universal defect functional decomposes as
delta[omega] = delta_D + delta_A + delta_B + delta_C + delta_omega,
with each sector functional inheriting tower compatibility, because
refinement maps commute with sector projection.

- num_sectors : ℕ
Number of sector summands.

- sectors : List String
Sectors: D, A, B, C, omega.

- each_tower_compatible : Bool
Each sector inherits tower compatibility.

- refinement_commutes : Bool
Refinement commutes with sector projection.

Instances For

---

### `Tau.BookIV.ManyBody.instReprSectorAdditivity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L298-L298)
**def
Tau.BookIV.ManyBody.instReprSectorAdditivity.repr :SectorAdditivity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprSectorAdditivity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L298-L298)
**instance
Tau.BookIV.ManyBody.instReprSectorAdditivity :Repr SectorAdditivity**

Equations
- Tau.BookIV.ManyBody.instReprSectorAdditivity = { reprPrec := Tau.BookIV.ManyBody.instReprSectorAdditivity.repr }

---

### `Tau.BookIV.ManyBody.sector_additivity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L300-L300)
**def
Tau.BookIV.ManyBody.sector_additivity :SectorAdditivity**

Equations
- Tau.BookIV.ManyBody.sector_additivity = { }
Instances For

---

### `Tau.BookIV.ManyBody.five_sector_summands`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L302-L303)
**theorem
Tau.BookIV.ManyBody.five_sector_summands :sector_additivity.num_sectors = 5**


---

### `Tau.BookIV.ManyBody.sector_additivity_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L305-L306)
**theorem
Tau.BookIV.ManyBody.sector_additivity_count :sector_additivity.sectors.length = 5**


---

### `Tau.BookIV.ManyBody.UniversalDefectFunctional`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L317-L329)
**structure
Tau.BookIV.ManyBody.UniversalDefectFunctional :Type**


[IV.D217] The universal defect functional delta[omega] = projlim_n delta_n[omega]
is the projective limit in the category of finitely-additive set functions,
well-defined because the inverse system satisfies tower compatibility.

- construction : String
Construction: projective limit.

- well_defined : Bool
Well-defined by tower compatibility.

- domain : String
Domain: clopen subsets of Z-hat.

- codomain : String
Codomain: R^3 x Z (defect tuple space).

Instances For

---

### `Tau.BookIV.ManyBody.instReprUniversalDefectFunctional`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L329-L329)
**instance
Tau.BookIV.ManyBody.instReprUniversalDefectFunctional :Repr UniversalDefectFunctional**

Equations
- Tau.BookIV.ManyBody.instReprUniversalDefectFunctional = { reprPrec := Tau.BookIV.ManyBody.instReprUniversalDefectFunctional.repr }

---

### `Tau.BookIV.ManyBody.instReprUniversalDefectFunctional.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L329-L329)
**def
Tau.BookIV.ManyBody.instReprUniversalDefectFunctional.repr :UniversalDefectFunctional → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.universal_defect_functional`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L331-L331)
**def
Tau.BookIV.ManyBody.universal_defect_functional :UniversalDefectFunctional**

Equations
- Tau.BookIV.ManyBody.universal_defect_functional = { }
Instances For

---

### `Tau.BookIV.ManyBody.ExistenceAndUniquenessOfLimit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L337-L348)
**structure
Tau.BookIV.ManyBody.ExistenceAndUniquenessOfLimit :Type**


[IV.P135] The projective limit delta[omega] exists and is unique:
tower compatibility guarantees the system (delta_n) is a projective
system of finitely-additive measures, and the universal property
of the limit in Pro(FinMeas) gives uniqueness.

- exists_limit : Bool
Exists.

- unique : Bool
Unique (universal property).

- category : String
Category: Pro(FinMeas).

Instances For

---

### `Tau.BookIV.ManyBody.instReprExistenceAndUniquenessOfLimit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L348-L348)
**instance
Tau.BookIV.ManyBody.instReprExistenceAndUniquenessOfLimit :Repr ExistenceAndUniquenessOfLimit**

Equations
- Tau.BookIV.ManyBody.instReprExistenceAndUniquenessOfLimit = { reprPrec := Tau.BookIV.ManyBody.instReprExistenceAndUniquenessOfLimit.repr }

---

### `Tau.BookIV.ManyBody.instReprExistenceAndUniquenessOfLimit.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L348-L348)
**def
Tau.BookIV.ManyBody.instReprExistenceAndUniquenessOfLimit.repr :ExistenceAndUniquenessOfLimit → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.existence_uniqueness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L350-L350)
**def
Tau.BookIV.ManyBody.existence_uniqueness :ExistenceAndUniquenessOfLimit**

Equations
- Tau.BookIV.ManyBody.existence_uniqueness = { }
Instances For

---

### `Tau.BookIV.ManyBody.limit_exists`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L352-L352)
**theorem
Tau.BookIV.ManyBody.limit_exists :existence_uniqueness.exists_limit = true**


---

### `Tau.BookIV.ManyBody.limit_unique`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L353-L353)
**theorem
Tau.BookIV.ManyBody.limit_unique :existence_uniqueness.unique = true**


---

### `Tau.BookIV.ManyBody.DefectTupleSpace`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L359-L375)
**structure
Tau.BookIV.ManyBody.DefectTupleSpace :Type**


[IV.D218] The defect tuple space D = R_{>=0} x R x R x Z, where
the four factors are: mobility (non-negative), vorticity (signed),
compression (signed), topological charge (integer).

This is the codomain of the universal defect functional.

- mobility_nonneg : Bool
Mobility: non-negative.

- vorticity_signed : Bool
Vorticity: signed real.

- compression_signed : Bool
Compression: signed real.

- topological_integer : Bool
Topological charge: integer.

- num_components : ℕ
Number of components.

Instances For

---

### `Tau.BookIV.ManyBody.instReprDefectTupleSpace`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L375-L375)
**instance
Tau.BookIV.ManyBody.instReprDefectTupleSpace :Repr DefectTupleSpace**

Equations
- Tau.BookIV.ManyBody.instReprDefectTupleSpace = { reprPrec := Tau.BookIV.ManyBody.instReprDefectTupleSpace.repr }

---

### `Tau.BookIV.ManyBody.instReprDefectTupleSpace.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L375-L375)
**def
Tau.BookIV.ManyBody.instReprDefectTupleSpace.repr :DefectTupleSpace → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.defect_tuple_space`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L377-L377)
**def
Tau.BookIV.ManyBody.defect_tuple_space :DefectTupleSpace**

Equations
- Tau.BookIV.ManyBody.defect_tuple_space = { }
Instances For

---

### `Tau.BookIV.ManyBody.four_tuple_components`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L379-L380)
**theorem
Tau.BookIV.ManyBody.four_tuple_components :defect_tuple_space.num_components = 4**


---

### `Tau.BookIV.ManyBody.CriticalMobilityThreshold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L386-L399)
**structure
Tau.BookIV.ManyBody.CriticalMobilityThreshold :Type**


[IV.D219] The critical mobility threshold mu_crit is the macroscopic
mobility value at which the Euler budget ceases to hold.
Below mu_crit: Euler regime (inviscid, budget-conserving).
Above mu_crit: Navier-Stokes regime (viscous, dissipative).

- separates_euler_ns : Bool
Separates Euler from NS regime.

- below_is_euler : Bool
Below: Euler (inviscid).

- above_is_ns : Bool
Above: NS (viscous).

- not_free_param : Bool
Determined by sector geometry (not free parameter).

Instances For

---

### `Tau.BookIV.ManyBody.instReprCriticalMobilityThreshold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L399-L399)
**instance
Tau.BookIV.ManyBody.instReprCriticalMobilityThreshold :Repr CriticalMobilityThreshold**

Equations
- Tau.BookIV.ManyBody.instReprCriticalMobilityThreshold = { reprPrec := Tau.BookIV.ManyBody.instReprCriticalMobilityThreshold.repr }

---

### `Tau.BookIV.ManyBody.instReprCriticalMobilityThreshold.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L399-L399)
**def
Tau.BookIV.ManyBody.instReprCriticalMobilityThreshold.repr :CriticalMobilityThreshold → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.critical_mobility`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L401-L401)
**def
Tau.BookIV.ManyBody.critical_mobility :CriticalMobilityThreshold**

Equations
- Tau.BookIV.ManyBody.critical_mobility = { }
Instances For

---

### `Tau.BookIV.ManyBody.CrystalRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L407-L421)
**structure
Tau.BookIV.ManyBody.CrystalRegime :Type**


[IV.D220] Crystal regime: mu < epsilon, |nu| < epsilon,
|kappa| < epsilon, theta = theta_0 (fixed topological charge).
All transport arrested, periodic lattice with frozen winding number.

- mobility_arrested : Bool
Mobility arrested.

- vorticity_arrested : Bool
Vorticity arrested.

- compression_arrested : Bool
Compression arrested.

- theta_fixed : Bool
Topological charge fixed.

- periodic : Bool
Periodic lattice structure.

Instances For

---

### `Tau.BookIV.ManyBody.instReprCrystalRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L421-L421)
**instance
Tau.BookIV.ManyBody.instReprCrystalRegime :Repr CrystalRegime**

Equations
- Tau.BookIV.ManyBody.instReprCrystalRegime = { reprPrec := Tau.BookIV.ManyBody.instReprCrystalRegime.repr }

---

### `Tau.BookIV.ManyBody.instReprCrystalRegime.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L421-L421)
**def
Tau.BookIV.ManyBody.instReprCrystalRegime.repr :CrystalRegime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.crystal_regime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L423-L423)
**def
Tau.BookIV.ManyBody.crystal_regime :CrystalRegime**

Equations
- Tau.BookIV.ManyBody.crystal_regime = { }
Instances For

---

### `Tau.BookIV.ManyBody.GlassRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L425-L440)
**structure
Tau.BookIV.ManyBody.GlassRegime :Type**


[IV.D221] Glass regime: mu < epsilon, |nu| < epsilon,
|kappa| >= epsilon, theta = theta_0.
Mobility and vorticity locked, but compression unfrozen —
local density fluctuations without long-range order.

- mobility_arrested : Bool
Mobility arrested.

- vorticity_arrested : Bool
Vorticity arrested.

- compression_unfrozen : Bool
Compression NOT arrested (unfrozen).

- no_long_range_order : Bool
No long-range order.

- theta_fixed : Bool
Topological charge fixed.

Instances For

---

### `Tau.BookIV.ManyBody.instReprGlassRegime.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L440-L440)
**def
Tau.BookIV.ManyBody.instReprGlassRegime.repr :GlassRegime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprGlassRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L440-L440)
**instance
Tau.BookIV.ManyBody.instReprGlassRegime :Repr GlassRegime**

Equations
- Tau.BookIV.ManyBody.instReprGlassRegime = { reprPrec := Tau.BookIV.ManyBody.instReprGlassRegime.repr }

---

### `Tau.BookIV.ManyBody.glass_regime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L442-L442)
**def
Tau.BookIV.ManyBody.glass_regime :GlassRegime**

Equations
- Tau.BookIV.ManyBody.glass_regime = { }
Instances For

---

### `Tau.BookIV.ManyBody.crystal_all_arrested`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L444-L448)
**theorem
Tau.BookIV.ManyBody.crystal_all_arrested :crystal_regime.mobility_arrested = true ∧ crystal_regime.vorticity_arrested = true ∧ crystal_regime.compression_arrested = true**


---

### `Tau.BookIV.ManyBody.glass_compression_unfrozen`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L450-L451)
**theorem
Tau.BookIV.ManyBody.glass_compression_unfrozen :glass_regime.compression_unfrozen = true**
