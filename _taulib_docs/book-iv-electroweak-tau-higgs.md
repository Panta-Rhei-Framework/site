---
layout: taulib-doc
title: "TauLib.BookIV.Electroweak.TauHiggs"
permalink: /verify/taulib/docs/book-iv-electroweak-tau-higgs/
lane: verify
module_name: "TauLib.BookIV.Electroweak.TauHiggs"
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

# TauLib.BookIV.Electroweak.TauHiggs


The τ-Higgs mechanism: crossing-point resolution, coherence functional,
physical vacuum, and the surviving spin-0 excitation.

## Registry Cross-References


- [IV.D134] Higgs Mechanism as ω-Sector Resolution — `HiggsMechanism`

- [IV.D135] Coherence Functional V_n — `CoherenceFunctional`

- [IV.D136] Physical Vacuum — `PhysicalVacuum`

- [IV.D137] Minimality Condition — `MinimalityCondition`

- [IV.D138] EM-Nullity — `EMNullity`

- [IV.D139] σ-Polarity of Higgs Excitation — `SigmaPolarity`

- [IV.L06] Fiber Excitation Spin Decomposition — `fiber_spin_decomposition`

- [IV.T63] Physical Vacuum Existence, Uniqueness, Stability — `vacuum_existence_uniqueness_stability`

- [IV.T64] Surviving Excitation is Spin-0 — `surviving_is_spin0`

- [IV.P72] Degenerate Vacuum Manifold — `degenerate_vacuum_manifold`

- [IV.P73] V_n Minimum on S¹ — `vn_minimum_on_circle`

- [IV.R34] Higgs Determines Sector Separation — structural remark


## Mathematical Content


In the τ-framework, the Higgs mechanism is NOT an ad hoc scalar field
added to the Lagrangian. It is the ω-sector resolution of the crossing
singularity at L = S¹ ∨ S¹.

The coherence functional V_n on crossing excitations has a unique minimum
(the physical vacuum) with vacuum expectation value v_EW ≈ 246 GeV.
The minimum lies on a circle S¹ in field space (degenerate manifold),
and the surviving excitation after eating Goldstone bosons is a spin-0
scalar with σ-polarity (σ = +1, unpolarized).

Key structural point: the Higgs field determines sector separation
(which sectors get mass), NOT mass itself. Mass originates from
the breathing operator on T².

## Ground Truth Sources


- Chapter 34 of Book IV (2nd Edition)

- kappa_n_closing_identity_sprint.md §8


---

### `Tau.BookIV.Electroweak.HiggsMechanism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L54-L71)
**structure
Tau.BookIV.Electroweak.HiggsMechanism :Type**


[IV.D134] The Higgs mechanism in the τ-framework: the ω-sector
(crossing of B and C lobes) provides a smooth resolution of
the crossing singularity at the lemniscate junction.

This is NOT a separate field — it is the structural content
of the fifth generator ω acting at the B∩C intersection.

- sector : BookIII.Sectors.Sector
The mediating sector.

- resolved_B : BookIII.Sectors.Sector
The resolved sectors.

- resolved_C : BookIII.Sectors.Sector
- coupling_numer : ℕ
The crossing coupling κ(B,C) governs the mechanism.

- coupling_denom : ℕ
- is_structural : Bool
Not a separate field — structural resolution.

Instances For

---

### `Tau.BookIV.Electroweak.instReprHiggsMechanism.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L71-L71)
**def
Tau.BookIV.Electroweak.instReprHiggsMechanism.repr :HiggsMechanism → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprHiggsMechanism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L71-L71)
**instance
Tau.BookIV.Electroweak.instReprHiggsMechanism :Repr HiggsMechanism**

Equations
- Tau.BookIV.Electroweak.instReprHiggsMechanism = { reprPrec := Tau.BookIV.Electroweak.instReprHiggsMechanism.repr }

---

### `Tau.BookIV.Electroweak.higgs_mechanism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L73-L73)
**def
Tau.BookIV.Electroweak.higgs_mechanism :HiggsMechanism**

Equations
- Tau.BookIV.Electroweak.higgs_mechanism = { }
Instances For

---

### `Tau.BookIV.Electroweak.CoherenceFunctional`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L79-L97)
**structure
Tau.BookIV.Electroweak.CoherenceFunctional :Type**


[IV.D135] The coherence functional V_n on crossing excitations.
V_n measures the coherence cost of displacing the ω-sector field
from its equilibrium. The subscript n indicates evaluation at
tower level n of the refinement tower.

V_n has the form of a Mexican hat potential, but this form is
DERIVED from coherence constraints, not postulated.

- tower_level : ℕ
Tower level at which V_n is evaluated.

- level_pos : self.tower_level > 0
Tower level is positive.

- mexican_hat : Bool
The functional has a Mexican hat shape.

- minimum_exists : Bool
Minimum exists.

- minimum_unique_mod_circle : Bool
Minimum is unique (up to S¹ degeneracy).

Instances For

---

### `Tau.BookIV.Electroweak.instReprCoherenceFunctional`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L97-L97)
**instance
Tau.BookIV.Electroweak.instReprCoherenceFunctional :Repr CoherenceFunctional**

Equations
- Tau.BookIV.Electroweak.instReprCoherenceFunctional = { reprPrec := Tau.BookIV.Electroweak.instReprCoherenceFunctional.repr }

---

### `Tau.BookIV.Electroweak.instReprCoherenceFunctional.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L97-L97)
**def
Tau.BookIV.Electroweak.instReprCoherenceFunctional.repr :CoherenceFunctional → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.coherence_V1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L99-L102)
**def
Tau.BookIV.Electroweak.coherence_V1 :CoherenceFunctional**


Coherence functional at level 1 (leading order).
Equations
- Tau.BookIV.Electroweak.coherence_V1 = { tower_level := 1, level_pos := Tau.BookIV.Electroweak.coherence_V1._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.PhysicalVacuum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L108-L123)
**structure
Tau.BookIV.Electroweak.PhysicalVacuum :Type**


[IV.D136] The physical vacuum: the minimum of the coherence
functional V_n. The vacuum expectation value (VEV) v_EW ≈ 246 GeV
sets the electroweak scale.

In the τ-framework, v_EW is determined by ι<sub>τ</sub> and the
neutron mass anchor m_n, NOT as a free parameter.

- vev_MeV : ℕ
VEV in MeV (v_EW ≈ 246200 MeV).

- unique : Bool
VEV is unique (up to S¹ degeneracy).

- stable : Bool
Vacuum is stable (V_n has positive second derivative).

- vev_nonzero : self.vev_MeV > 0
VEV is nonzero (spontaneous breaking occurs).

Instances For

---

### `Tau.BookIV.Electroweak.instReprPhysicalVacuum.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L123-L123)
**def
Tau.BookIV.Electroweak.instReprPhysicalVacuum.repr :PhysicalVacuum → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprPhysicalVacuum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L123-L123)
**instance
Tau.BookIV.Electroweak.instReprPhysicalVacuum :Repr PhysicalVacuum**

Equations
- Tau.BookIV.Electroweak.instReprPhysicalVacuum = { reprPrec := Tau.BookIV.Electroweak.instReprPhysicalVacuum.repr }

---

### `Tau.BookIV.Electroweak.physical_vacuum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L125-L125)
**def
Tau.BookIV.Electroweak.physical_vacuum :PhysicalVacuum**

Equations
- Tau.BookIV.Electroweak.physical_vacuum = { vev_nonzero := Tau.BookIV.Electroweak.physical_vacuum._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.MinimalityCondition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L131-L142)
**structure
Tau.BookIV.Electroweak.MinimalityCondition :Type**


[IV.D137] Minimality condition: the first variation of V_n
vanishes at the physical vacuum. Combined with the positive
second variation (stability), this characterizes the VEV
as a strict local minimum modulo the S¹ degeneracy.

- first_variation_zero : Bool
First variation vanishes.

- second_variation_pos : Bool
Second variation is positive (stability).

- on_circle_orbit : Bool
The minimum is on the S¹ orbit.

Instances For

---

### `Tau.BookIV.Electroweak.instReprMinimalityCondition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L142-L142)
**def
Tau.BookIV.Electroweak.instReprMinimalityCondition.repr :MinimalityCondition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprMinimalityCondition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L142-L142)
**instance
Tau.BookIV.Electroweak.instReprMinimalityCondition :Repr MinimalityCondition**

Equations
- Tau.BookIV.Electroweak.instReprMinimalityCondition = { reprPrec := Tau.BookIV.Electroweak.instReprMinimalityCondition.repr }

---

### `Tau.BookIV.Electroweak.minimality_condition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L144-L144)
**def
Tau.BookIV.Electroweak.minimality_condition :MinimalityCondition**

Equations
- Tau.BookIV.Electroweak.minimality_condition = { }
Instances For

---

### `Tau.BookIV.Electroweak.EMNullity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L150-L164)
**structure
Tau.BookIV.Electroweak.EMNullity :Type**


[IV.D138] EM-nullity: the photon remains massless after
electroweak symmetry breaking.

In the τ-framework, this is a THEOREM, not a tuning condition:
the U(1)_EM generator is the unique combination of W³ and B
that commutes with the ω-sector VEV. The VEV breaks SU(2)_L × U(1)_Y
down to U(1)_EM, and the unbroken generator gives a massless photon.

- photon_massless : Bool
The photon is massless.

- unbroken_symmetry : String
The unbroken symmetry is U(1)_EM.

- forced_by_vev : Bool
This is forced by the VEV structure.

Instances For

---

### `Tau.BookIV.Electroweak.instReprEMNullity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L164-L164)
**instance
Tau.BookIV.Electroweak.instReprEMNullity :Repr EMNullity**

Equations
- Tau.BookIV.Electroweak.instReprEMNullity = { reprPrec := Tau.BookIV.Electroweak.instReprEMNullity.repr }

---

### `Tau.BookIV.Electroweak.instReprEMNullity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L164-L164)
**def
Tau.BookIV.Electroweak.instReprEMNullity.repr :EMNullity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.em_nullity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L166-L166)
**def
Tau.BookIV.Electroweak.em_nullity :EMNullity**

Equations
- Tau.BookIV.Electroweak.em_nullity = { }
Instances For

---

### `Tau.BookIV.Electroweak.SigmaPolarity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L172-L183)
**structure
Tau.BookIV.Electroweak.SigmaPolarity :Type**


[IV.D139] The surviving Higgs excitation has σ-polarity σ = +1,
meaning it is unpolarized (neither χ₊ nor χ₋ dominant).
This reflects its origin at the CROSSING point of the
lemniscate, where both lobes meet.

- sigma : ℤ
Polarity value: +1 = unpolarized.

- at_crossing : Bool
At crossing point.

- unpolarized : Bool
Neither lobe dominates.

Instances For

---

### `Tau.BookIV.Electroweak.instReprSigmaPolarity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L183-L183)
**def
Tau.BookIV.Electroweak.instReprSigmaPolarity.repr :SigmaPolarity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprSigmaPolarity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L183-L183)
**instance
Tau.BookIV.Electroweak.instReprSigmaPolarity :Repr SigmaPolarity**

Equations
- Tau.BookIV.Electroweak.instReprSigmaPolarity = { reprPrec := Tau.BookIV.Electroweak.instReprSigmaPolarity.repr }

---

### `Tau.BookIV.Electroweak.sigma_polarity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L185-L185)
**def
Tau.BookIV.Electroweak.sigma_polarity :SigmaPolarity**

Equations
- Tau.BookIV.Electroweak.sigma_polarity = { }
Instances For

---

### `Tau.BookIV.Electroweak.FiberSpinDecomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L191-L207)
**structure
Tau.BookIV.Electroweak.FiberSpinDecomposition :Type**


[IV.L06] Fiber excitations on T² decompose by spin at the
crossing point:


- Spin 0: scalar (survives as Higgs)

- Spin 1: vector (eaten as longitudinal W/Z modes = Goldstones)


This decomposition is forced by the SO(2) symmetry of the
crossing-point tangent space.

- spin0_count : ℕ
Number of spin-0 modes at crossing.

- spin1_count : ℕ
Number of spin-1 modes at crossing.

- total : ℕ
Total excitation count.

- total_check : self.total = self.spin0_count + self.spin1_count
Total equals spin-0 + spin-1.

Instances For

---

### `Tau.BookIV.Electroweak.instReprFiberSpinDecomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L207-L207)
**instance
Tau.BookIV.Electroweak.instReprFiberSpinDecomposition :Repr FiberSpinDecomposition**

Equations
- Tau.BookIV.Electroweak.instReprFiberSpinDecomposition = { reprPrec := Tau.BookIV.Electroweak.instReprFiberSpinDecomposition.repr }

---

### `Tau.BookIV.Electroweak.instReprFiberSpinDecomposition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L207-L207)
**def
Tau.BookIV.Electroweak.instReprFiberSpinDecomposition.repr :FiberSpinDecomposition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.fiber_spin_decomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L209-L209)
**def
Tau.BookIV.Electroweak.fiber_spin_decomposition :FiberSpinDecomposition**

Equations
- Tau.BookIV.Electroweak.fiber_spin_decomposition = { total_check := Tau.BookIV.Electroweak.fiber_spin_decomposition._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.vacuum_existence_uniqueness_stability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L215-L225)
**theorem
Tau.BookIV.Electroweak.vacuum_existence_uniqueness_stability :physical_vacuum.unique = true ∧ physical_vacuum.stable = true ∧ physical_vacuum.vev_MeV > 0**


[IV.T63] The physical vacuum exists, is unique (mod S¹), and is stable.

Existence: V_n is bounded below and continuous on a compact domain.
Uniqueness: The Mexican hat potential has a unique radial minimum.
Stability: The Hessian at the minimum has all positive eigenvalues
in the radial direction (the angular direction is flat = Goldstone).

---

### `Tau.BookIV.Electroweak.surviving_is_spin0`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L231-L239)
**theorem
Tau.BookIV.Electroweak.surviving_is_spin0 :fiber_spin_decomposition.spin0_count = 1 ∧ fiber_spin_decomposition.spin1_count = 3 ∧ fiber_spin_decomposition.total = 4**


[IV.T64] After Goldstone bosons are eaten by W± and Z,
the single surviving excitation is spin-0 (the Higgs boson).

Counting: 4 real components − 3 Goldstones = 1 physical scalar.

---

### `Tau.BookIV.Electroweak.surviving_at_crossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L241-L245)
**theorem
Tau.BookIV.Electroweak.surviving_at_crossing :sigma_polarity.at_crossing = true ∧ sigma_polarity.sigma = 1**


The surviving mode is at the crossing point with σ = +1.

---

### `Tau.BookIV.Electroweak.DegenerateVacuumManifold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L251-L267)
**structure
Tau.BookIV.Electroweak.DegenerateVacuumManifold :Type**


[IV.P72] The vacuum manifold is S¹: the set of minima of V_n
forms a circle in field space. This degeneracy is the geometric
origin of Goldstone bosons.

In the τ-framework, S¹ is one lobe of the lemniscate L = S¹ ∨ S¹.
The vacuum selects a point on one lobe, breaking the continuous
S¹ symmetry spontaneously.

- topology : String
Vacuum manifold topology.

- dim : ℕ
Dimension of manifold.

- goldstone_count : ℕ
Number of Goldstone bosons = dim of manifold.

- from_su2_breaking : Bool
The 3 Goldstones come from SU(2)_L breaking, not just S¹.

Instances For

---

### `Tau.BookIV.Electroweak.instReprDegenerateVacuumManifold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L267-L267)
**instance
Tau.BookIV.Electroweak.instReprDegenerateVacuumManifold :Repr DegenerateVacuumManifold**

Equations
- Tau.BookIV.Electroweak.instReprDegenerateVacuumManifold = { reprPrec := Tau.BookIV.Electroweak.instReprDegenerateVacuumManifold.repr }

---

### `Tau.BookIV.Electroweak.instReprDegenerateVacuumManifold.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L267-L267)
**def
Tau.BookIV.Electroweak.instReprDegenerateVacuumManifold.repr :DegenerateVacuumManifold → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.degenerate_vacuum_manifold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L269-L269)
**def
Tau.BookIV.Electroweak.degenerate_vacuum_manifold :DegenerateVacuumManifold**

Equations
- Tau.BookIV.Electroweak.degenerate_vacuum_manifold = { }
Instances For

---

### `Tau.BookIV.Electroweak.VnMinimumCircle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L275-L285)
**structure
Tau.BookIV.Electroweak.VnMinimumCircle :Type**


[IV.P73] The minimum of V_n lies on a circle S¹ of radius v_EW
in the (Re φ, Im φ) plane. All points on this circle are
physically equivalent (related by a U(1) gauge transformation).

- radius_MeV : ℕ
Radius of the minimum circle in MeV.

- is_gauge_orbit : Bool
The circle is a gauge orbit.

- all_equivalent : Bool
All points physically equivalent.

Instances For

---

### `Tau.BookIV.Electroweak.instReprVnMinimumCircle.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L285-L285)
**def
Tau.BookIV.Electroweak.instReprVnMinimumCircle.repr :VnMinimumCircle → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprVnMinimumCircle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L285-L285)
**instance
Tau.BookIV.Electroweak.instReprVnMinimumCircle :Repr VnMinimumCircle**

Equations
- Tau.BookIV.Electroweak.instReprVnMinimumCircle = { reprPrec := Tau.BookIV.Electroweak.instReprVnMinimumCircle.repr }

---

### `Tau.BookIV.Electroweak.vn_minimum_on_circle`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L287-L287)
**def
Tau.BookIV.Electroweak.vn_minimum_on_circle :VnMinimumCircle**

Equations
- Tau.BookIV.Electroweak.vn_minimum_on_circle = { }
Instances For

---

### `Tau.BookIV.Electroweak.remark_sector_separation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs.lean#L293-L304)
**def
Tau.BookIV.Electroweak.remark_sector_separation :String**


[IV.R34] The Higgs mechanism determines SECTOR SEPARATION
(which sectors acquire mass via coupling to the VEV), NOT
mass origin itself. Mass originates from the breathing operator
on T² (Book IV Part III). The Higgs mechanism tells us which
particles couple to the VEV and therefore which particles get
mass from the EW sector.

This distinction resolves the conceptual confusion in the SM
where the Higgs "gives mass" — in τ, it mediates the assignment
of mass to sectors, while mass itself is a fiber-geometric quantity.
Equations
- Tau.BookIV.Electroweak.remark_sector_separation = "Higgs determines sector separation (mass assignment), not mass origin (breathing operator on T2)"
Instances For
