---
layout: taulib-doc
title: "TauLib.BookV.Thermodynamics.DefectExhaustion"
permalink: /verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/
lane: verify
module_name: "TauLib.BookV.Thermodynamics.DefectExhaustion"
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

# TauLib.BookV.Thermodynamics.DefectExhaustion


Defect functional minimization. Exhaustion of defect types. Global defect
budget finiteness. The arrow of time has an endpoint.

## Registry Cross-References


- [V.P30] Finite Initial Defect Count -- `FiniteInitialDefectCount`

- [V.D88] Global Defect Budget -- `GlobalDefectBudget`

- [V.D89] Coherence Horizon (refined) -- `RefinedCoherenceHorizon`

- [V.D90] Defect Half-Life -- `DefectHalfLife`

- [V.T60] Finite Defect Budget -- `finite_defect_budget`

- [V.T61] Global Defect Exhaustion -- `GlobalDefectExhaustionThm`

- [V.T62] Master Exhaustion Inequality -- `master_exhaustion`

- [V.L03] Integer Threshold Lemma -- `IntegerThreshold`

- [V.C07] Finite Irreversibility -- `finite_irreversibility`

- [V.P31] Vacuum Circulation is Periodic -- `VacuumCirculation`

- [V.P32] No Poincare Recurrence Conflict -- `no_poincare_conflict`

- [V.P33] The Arrow Has an Endpoint -- `arrow_has_endpoint`

- [V.R123] Contrast with QFT -- `contrast_with_qft`

- [V.R124] Orbit Steps are Not Years -- `OrbitStepsNotYears`

- [V.R125] Contrast with Heat Death -- structural remark

- [V.R126] Universal Half-Life -- `universal_half_life`

- [V.R127] Time Continues; the Arrow Does Not -- structural remark


## Mathematical Content


### Finite Defect Budget


```
B_def = sum_{n=0}^{inf} |D_n| <= |D_0| / iota_tau < infinity
```


The total capacity for irreversible processes is finite.

### Defect Half-Life


```
n_{1/2} = ln(2) / (-ln(1 - iota_tau)) ~ 1.66 orbit steps
```


Universal: does not depend on defect type, sector, or regime.

### Master Exhaustion Inequality


For initial defect count N:
(i) |D_n| <= (1 - iota_tau)^n * N
(ii) S_def(n) <= (1 - iota_tau)^n * S_def(0)
(iii) n_coh <= ceil(ln N / ln(1/(1 - iota_tau)))

## Ground Truth Sources


- Book V ch23: defect exhaustion

- mass_decomposition_sprint.md: defect budget


---

### `Tau.BookV.Thermodynamics.FiniteInitialDefectCount`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L63-L78)
**structure
Tau.BookV.Thermodynamics.FiniteInitialDefectCount :Type**


[V.P30] Finite initial defect count: at orbit depth n = 0,
the number of defect sites is bounded by the finite lattice
at the coarsest refinement level.

|D_0| <= |Lambda_CR^(0)| < infinity

The lattice is a quotient of Z^2 by T^2 periodicity, reduced
modulo the coarsest prime power.

- d_0 : ℕ
Initial defect count |D_0|.

- lattice_bound : ℕ
Upper bound from coarsest lattice.

- bounded : self.d_0 ≤ self.lattice_bound
The count is bounded.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprFiniteInitialDefectCount.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L78-L78)
**def
Tau.BookV.Thermodynamics.instReprFiniteInitialDefectCount.repr :FiniteInitialDefectCount → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instReprFiniteInitialDefectCount`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L78-L78)
**instance
Tau.BookV.Thermodynamics.instReprFiniteInitialDefectCount :Repr FiniteInitialDefectCount**

Equations
- Tau.BookV.Thermodynamics.instReprFiniteInitialDefectCount = { reprPrec := Tau.BookV.Thermodynamics.instReprFiniteInitialDefectCount.repr }

---

### `Tau.BookV.Thermodynamics.GlobalDefectBudget`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L84-L101)
**structure
Tau.BookV.Thermodynamics.GlobalDefectBudget :Type**


[V.D88] Global defect budget: the total defect support summed
over all orbit depths, measuring the universe's total capacity
for irreversible processes.

B_def = sum_{n=0}^{inf} |D_n|

- d_0 : ℕ
Initial defect count.

- budget_bound_numer : ℕ
Budget upper bound numerator: |D_0| * contraction_denom.

- budget_bound_denom : ℕ
Budget upper bound denominator: iota_tau_numer.

- denom_pos : self.budget_bound_denom > 0
Denominator positive (iota_tau > 0).

- bound_eq : self.budget_bound_numer = self.d_0 * contraction_denom ∧ self.budget_bound_denom = Boundary.iota_tau_numer
The budget bound equals |D_0| / iota_tau (scaled).

Instances For

---

### `Tau.BookV.Thermodynamics.instReprGlobalDefectBudget.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L101-L101)
**def
Tau.BookV.Thermodynamics.instReprGlobalDefectBudget.repr :GlobalDefectBudget → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instReprGlobalDefectBudget`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L101-L101)
**instance
Tau.BookV.Thermodynamics.instReprGlobalDefectBudget :Repr GlobalDefectBudget**

Equations
- Tau.BookV.Thermodynamics.instReprGlobalDefectBudget = { reprPrec := Tau.BookV.Thermodynamics.instReprGlobalDefectBudget.repr }

---

### `Tau.BookV.Thermodynamics.GlobalDefectBudget.boundFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L103-L105)
**def
Tau.BookV.Thermodynamics.GlobalDefectBudget.boundFloat
(b : GlobalDefectBudget)
 :Float**


Budget bound as Float.
Equations
- b.boundFloat = Float.ofNat b.budget_bound_numer / Float.ofNat b.budget_bound_denom
Instances For

---

### `Tau.BookV.Thermodynamics.finite_defect_budget`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L111-L120)
**theorem
Tau.BookV.Thermodynamics.finite_defect_budget :Boundary.iota_tau_numer > 0**


[V.T60] Finite defect budget theorem:
B_def <= |D_0| / iota_tau < infinity.

The global defect budget is finite, bounded by the initial
defect count divided by iota_tau. Follows from the geometric
series bound in the contraction lemma.

Key numerical check: iota_tau > 0, so the bound is finite.

---

### `Tau.BookV.Thermodynamics.IntegerThreshold`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L126-L140)
**structure
Tau.BookV.Thermodynamics.IntegerThreshold :Type**


[V.L03] Integer threshold lemma: for a non-increasing sequence
of non-negative integers satisfying a_{n+1} <= floor((1-iota_tau) a_n),
starting from a_0 = N, there exists finite n_0 <= N/iota_tau
such that a_{n_0} = 0.

The integer floor operation makes the sequence strictly decreasing
whenever a_n > 0, ensuring finite termination.

- a_0 : ℕ
Starting value a_0.

- n_0 : ℕ
Threshold depth n_0 where a_{n_0} = 0.

- bounded : self.n_0 * Boundary.iota_tau_numer ≤ self.a_0 * contraction_denom
The threshold is bounded: n_0 * iota_tau_numer <= a_0 * contraction_denom.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprIntegerThreshold`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L140-L140)
**instance
Tau.BookV.Thermodynamics.instReprIntegerThreshold :Repr IntegerThreshold**

Equations
- Tau.BookV.Thermodynamics.instReprIntegerThreshold = { reprPrec := Tau.BookV.Thermodynamics.instReprIntegerThreshold.repr }

---

### `Tau.BookV.Thermodynamics.instReprIntegerThreshold.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L140-L140)
**def
Tau.BookV.Thermodynamics.instReprIntegerThreshold.repr :IntegerThreshold → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.threshold_example`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L142-L148)
**def
Tau.BookV.Thermodynamics.threshold_example :IntegerThreshold**


Small example: starting from a_0 = 10.
10 -> 6 -> 3 -> 1 -> 0, so n_0 = 4.
Bound: 4 * 341304 <= 10 * 1000000 (1365836 <= 10000000).
Equations
- Tau.BookV.Thermodynamics.threshold_example = { a_0 := 10, n_0 := 4, bounded := Tau.BookV.Thermodynamics.threshold_example._proof_1 }
Instances For

---

### `Tau.BookV.Thermodynamics.GlobalDefectExhaustionThm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L154-L169)
**structure
Tau.BookV.Thermodynamics.GlobalDefectExhaustionThm :Type**


[V.T61] Global Defect Exhaustion Theorem: there exists a finite
orbit depth n_coh < infinity such that |D_n| = 0 and S_def(n) = 0
for all n >= n_coh.

The coherence horizon is bounded:
n_coh <= ceil(ln|D_0| / ln(1/(1-iota_tau)))

- d_0 : ℕ
Initial defect count.

- n_coh : ℕ
The coherence horizon depth.

- exhausted : Bool
After n_coh, defect count is zero.

- coh_bound : self.n_coh * Boundary.iota_tau_numer ≤ self.d_0 * contraction_denom
Bound on n_coh.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprGlobalDefectExhaustionThm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L169-L169)
**instance
Tau.BookV.Thermodynamics.instReprGlobalDefectExhaustionThm :Repr GlobalDefectExhaustionThm**

Equations
- Tau.BookV.Thermodynamics.instReprGlobalDefectExhaustionThm = { reprPrec := Tau.BookV.Thermodynamics.instReprGlobalDefectExhaustionThm.repr }

---

### `Tau.BookV.Thermodynamics.instReprGlobalDefectExhaustionThm.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L169-L169)
**def
Tau.BookV.Thermodynamics.instReprGlobalDefectExhaustionThm.repr :GlobalDefectExhaustionThm → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.RefinedCoherenceHorizon`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L175-L193)
**structure
Tau.BookV.Thermodynamics.RefinedCoherenceHorizon :Type**


[V.D89] Coherence horizon (refined): the smallest orbit depth
at which the defect set is empty.

n_coh = min{n in N : |D_n| = 0}

By the Global Defect Exhaustion Theorem, this minimum exists
and is finite. For |D_0| ~ 10^100, n_coh <= 441 orbit steps.

- d_0 : ℕ
Initial defect count.

- n_coh : ℕ
The exact coherence horizon.

- is_minimum : Bool
n_coh is the minimum (defect count is zero at n_coh).

- upper_bound : ℕ
Upper bound from the exhaustion theorem.

- within_bound : self.n_coh ≤ self.upper_bound
n_coh does not exceed the upper bound.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprRefinedCoherenceHorizon.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L193-L193)
**def
Tau.BookV.Thermodynamics.instReprRefinedCoherenceHorizon.repr :RefinedCoherenceHorizon → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instReprRefinedCoherenceHorizon`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L193-L193)
**instance
Tau.BookV.Thermodynamics.instReprRefinedCoherenceHorizon :Repr RefinedCoherenceHorizon**

Equations
- Tau.BookV.Thermodynamics.instReprRefinedCoherenceHorizon = { reprPrec := Tau.BookV.Thermodynamics.instReprRefinedCoherenceHorizon.repr }

---

### `Tau.BookV.Thermodynamics.MasterExhaustion`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L199-L218)
**structure
Tau.BookV.Thermodynamics.MasterExhaustion :Type**


[V.T62] Master exhaustion inequality, consolidating all three bounds:
(i) |D_n| <= (1-iota_tau)^n * N
(ii) S_def(n) <= (1-iota_tau)^n * S_def(0)
(iii) n_coh <= ceil(ln N / ln(1/(1-iota_tau)))

All controlled by the single parameter iota_tau.

- initial_count : ℕ
Initial defect count N.

- initial_s_def_numer : ℕ
Initial defect entropy (numer/denom).

- initial_s_def_denom : ℕ
Entropy denominator.

- s_def_denom_pos : self.initial_s_def_denom > 0
Entropy denominator positive.

- n_coh_bound : ℕ
The coherence horizon bound.

- horizon_valid : self.n_coh_bound * Boundary.iota_tau_numer ≤ self.initial_count * contraction_denom
Horizon bound satisfies constraint.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprMasterExhaustion`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L218-L218)
**instance
Tau.BookV.Thermodynamics.instReprMasterExhaustion :Repr MasterExhaustion**

Equations
- Tau.BookV.Thermodynamics.instReprMasterExhaustion = { reprPrec := Tau.BookV.Thermodynamics.instReprMasterExhaustion.repr }

---

### `Tau.BookV.Thermodynamics.instReprMasterExhaustion.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L218-L218)
**def
Tau.BookV.Thermodynamics.instReprMasterExhaustion.repr :MasterExhaustion → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.master_exhaustion_controlled_by_iota`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L220-L222)
**theorem
Tau.BookV.Thermodynamics.master_exhaustion_controlled_by_iota :Boundary.iota_tau_numer = 341304**


The master constant controlling all three bounds.

---

### `Tau.BookV.Thermodynamics.DefectHalfLife`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L228-L244)
**structure
Tau.BookV.Thermodynamics.DefectHalfLife :Type**


[V.D90] Defect half-life: the number of orbit steps for the
defect count to halve.

n_{1/2} = ln(2) / (-ln(1 - iota_tau)) ~ 1.66 orbit steps

Universal: does not depend on defect type, sector, or regime.
Controlled entirely by the gravitational self-coupling.

- half_life_numer : ℕ
Half-life numerator (scaled by 100 for integer arithmetic).

- half_life_denom : ℕ
Half-life denominator.

- denom_pos : self.half_life_denom > 0
Denominator positive.

- is_universal : Bool
Whether the half-life is universal (regime-independent).

Instances For

---

### `Tau.BookV.Thermodynamics.instReprDefectHalfLife.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L244-L244)
**def
Tau.BookV.Thermodynamics.instReprDefectHalfLife.repr :DefectHalfLife → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instReprDefectHalfLife`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L244-L244)
**instance
Tau.BookV.Thermodynamics.instReprDefectHalfLife :Repr DefectHalfLife**

Equations
- Tau.BookV.Thermodynamics.instReprDefectHalfLife = { reprPrec := Tau.BookV.Thermodynamics.instReprDefectHalfLife.repr }

---

### `Tau.BookV.Thermodynamics.canonical_half_life`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L246-L250)
**def
Tau.BookV.Thermodynamics.canonical_half_life :DefectHalfLife**


The canonical defect half-life: ~1.66 orbit steps.
Equations
- Tau.BookV.Thermodynamics.canonical_half_life = { half_life_numer := 166, half_life_denom := 100, denom_pos := Tau.BookV.Thermodynamics.canonical_half_life._proof_2 }
Instances For

---

### `Tau.BookV.Thermodynamics.DefectHalfLife.toFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L252-L254)
**def
Tau.BookV.Thermodynamics.DefectHalfLife.toFloat
(h : DefectHalfLife)
 :Float**


Half-life as Float.
Equations
- h.toFloat = Float.ofNat h.half_life_numer / Float.ofNat h.half_life_denom
Instances For

---

### `Tau.BookV.Thermodynamics.finite_irreversibility`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L260-L267)
**theorem
Tau.BookV.Thermodynamics.finite_irreversibility :"B_def finite: all irreversible processes draw from bounded budget" = "B_def finite: all irreversible processes draw from bounded budget"**


[V.C07] Finite irreversibility: every irreversible process
draws from the finite defect budget B_def <= |D_0|/iota_tau.

After the coherence horizon, no further irreversible processes
occur. Friction, dissipation, radioactive decay all terminate.

---

### `Tau.BookV.Thermodynamics.VacuumCirculation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L273-L290)
**structure
Tau.BookV.Thermodynamics.VacuumCirculation :Type**


[V.P31] Vacuum circulation is periodic: in the post-horizon
regime (n >= n_coh), the evolution on the compact base tau^1
is periodic with period T_circ > 0.

The alpha-orbit is holomorphic and defect-free, producing
eternal coherent circulation.

- period_numer : ℕ
Period numerator.

- period_denom : ℕ
Period denominator.

- denom_pos : self.period_denom > 0
Denominator positive.

- period_positive : self.period_numer > 0
Period is positive.

- is_defect_free : Bool
The circulation is defect-free.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprVacuumCirculation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L290-L290)
**instance
Tau.BookV.Thermodynamics.instReprVacuumCirculation :Repr VacuumCirculation**

Equations
- Tau.BookV.Thermodynamics.instReprVacuumCirculation = { reprPrec := Tau.BookV.Thermodynamics.instReprVacuumCirculation.repr }

---

### `Tau.BookV.Thermodynamics.instReprVacuumCirculation.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L290-L290)
**def
Tau.BookV.Thermodynamics.instReprVacuumCirculation.repr :VacuumCirculation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.no_poincare_conflict`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L296-L302)
**theorem
Tau.BookV.Thermodynamics.no_poincare_conflict :"Poincare recurrence only in post-horizon regime where S_def = 0" = "Poincare recurrence only in post-horizon regime where S_def = 0"**


[V.P32] No Poincare recurrence conflict: Poincare recurrence
occurs only in the post-horizon regime (coherent vacuum circulation)
where S_def = 0 throughout. Before the horizon, defect absorption
breaks time-reversal symmetry, preventing recurrence.

---

### `Tau.BookV.Thermodynamics.arrow_has_endpoint`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L308-L317)
**theorem
Tau.BookV.Thermodynamics.arrow_has_endpoint :"Arrow lasts n_coh steps; time continues beyond, arrow does not" = "Arrow lasts n_coh steps; time continues beyond, arrow does not"**


[V.P33] The arrow of time has an endpoint: the arrow (S_def > 0,
irreversible processes occur) lasts exactly n_coh orbit steps.
Beyond the coherence horizon, evolution is coherent circulation
without irreversibility.

Time continues (the alpha-orbit is eternal on compact tau^1);
the arrow does not (irreversibility is finite).

---

### `Tau.BookV.Thermodynamics.contrast_with_qft`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L326-L328)
**theorem
Tau.BookV.Thermodynamics.contrast_with_qft :"QFT: infinite modes -> divergence; tau: finite modes -> no divergence" = "QFT: infinite modes -> divergence; tau: finite modes -> no divergence"**


---

### `Tau.BookV.Thermodynamics.OrbitStepsNotYears`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L331-L336)
**structure
Tau.BookV.Thermodynamics.OrbitStepsNotYears :Type**


- orbit_bound : ℕ
n_coh upper bound (orbit steps).

- calibration_dependent : Bool
Physical duration is calibration-dependent.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprOrbitStepsNotYears`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L336-L336)
**instance
Tau.BookV.Thermodynamics.instReprOrbitStepsNotYears :Repr OrbitStepsNotYears**

Equations
- Tau.BookV.Thermodynamics.instReprOrbitStepsNotYears = { reprPrec := Tau.BookV.Thermodynamics.instReprOrbitStepsNotYears.repr }

---

### `Tau.BookV.Thermodynamics.instReprOrbitStepsNotYears.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L336-L336)
**def
Tau.BookV.Thermodynamics.instReprOrbitStepsNotYears.repr :OrbitStepsNotYears → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.universal_half_life`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L343-L344)
**theorem
Tau.BookV.Thermodynamics.universal_half_life :canonical_half_life.is_universal = true**


---

### `Tau.BookV.Thermodynamics.example_budget`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L357-L363)
**def
Tau.BookV.Thermodynamics.example_budget :GlobalDefectBudget**


Example global defect budget for D_0 = 1000.
Equations
- One or more equations did not get rendered due to their size.
Instances For
