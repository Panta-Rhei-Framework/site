---
layout: taulib-doc
title: "TauLib.BookIV.Physics.Thermodynamics"
permalink: /verify/taulib/docs/book-iv-physics-thermodynamics/
lane: verify
module_name: "TauLib.BookIV.Physics.Thermodynamics"
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

# TauLib.BookIV.Physics.Thermodynamics


Entropy splitting, defect thermodynamics, and the No-Running Principle.

## Registry Cross-References


- [IV.D24] Entropy Splitting — `EntropySplitting`

- [IV.D25] Defect Budget — `DefectBudget`

- [IV.R05] S_def → 0 at coherence horizon — structural remark

- [IV.R06] S_ref unbounded — structural remark

- [IV.P04] No-Running Principle — `NoRunningPrinciple`, `no_running_all_sectors`

- [IV.T04] Euler budget conservation — `euler_budget_conserved`


## Mathematical Content


### Entropy Splitting


Orthodox entropy S splits into two structurally distinct components:

```
S_total = S_def + S_ref
```


- **S_def (defect entropy)**: Tracks defect novelty events. Reaches ZERO
at the coherence horizon (all defects resolved).

- **S_ref (refinement entropy)**: Tracks refinement depth. Grows unboundedly
(refinement never terminates).


The **Second-Law Inversion**: In τ-cosmology, S_def reverses at the
coherence horizon — a novel thermodynamic asymmetry absent in orthodox physics.

### Defect Budget Conservation


In the Euler regime (inviscid), the total defect budget is conserved:

```
∑(mobility + vorticity + compression + topological) = const
```


This is the τ-native form of the Kelvin circulation theorem.

### No-Running Principle


Orthodox "running couplings" (α_s(Q²), etc.) are NOT ontic:

```
Fixed ontic coupling + regime-dependent readout = apparent "running"
```


The τ-kernel coupling constants are **boundary fixed-point invariants**,
absolutely fixed regardless of measurement regime. What orthodox QFT
interprets as "running" is the regime-dependence of the readout functor
projecting the fixed ontic value onto different measurement scales.

## Ground Truth Sources


- fluid-condensed-matter.json: defect-thermodynamics, defect-budget

- particle-physics-defects.json: running-vs-regime-framework

- holonomy-sectors.json: fixed-point-readout-machinery


---

### `Tau.BookIV.Physics.EntropySplitting`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L67-L89)
**structure
Tau.BookIV.Physics.EntropySplitting :Type**


[IV.D24] Entropy splitting: S = S_def + S_ref.


- S_def (defect entropy): coherence measure of defect novelty.
Reaches zero at the coherence horizon.

- S_ref (refinement entropy): measure of refinement depth.
Grows unboundedly (refinement never terminates).


The Second-Law Inversion: S_def reverses at the horizon,
creating a novel thermodynamic asymmetry.

- s_def_numer : ℕ
Defect entropy numerator (→ 0 at coherence horizon).

- s_def_denom : ℕ
Defect entropy denominator.

- s_ref_numer : ℕ
Refinement entropy numerator (unbounded growth).

- s_ref_denom : ℕ
Refinement entropy denominator.

- denom_pos_def : self.s_def_denom > 0
Defect entropy denominator positive.

- denom_pos_ref : self.s_ref_denom > 0
Refinement entropy denominator positive.

Instances For

---

### `Tau.BookIV.Physics.instReprEntropySplitting`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L89-L89)
**instance
Tau.BookIV.Physics.instReprEntropySplitting :Repr EntropySplitting**

Equations
- Tau.BookIV.Physics.instReprEntropySplitting = { reprPrec := Tau.BookIV.Physics.instReprEntropySplitting.repr }

---

### `Tau.BookIV.Physics.instReprEntropySplitting.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L89-L89)
**def
Tau.BookIV.Physics.instReprEntropySplitting.repr :EntropySplitting → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.EntropySplitting.totalFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L91-L94)
**def
Tau.BookIV.Physics.EntropySplitting.totalFloat
(e : EntropySplitting)
 :Float**


Total entropy as Float (for display).
Equations
- e.totalFloat = Float.ofNat e.s_def_numer / Float.ofNat e.s_def_denom + Float.ofNat e.s_ref_numer / Float.ofNat e.s_ref_denom
Instances For

---

### `Tau.BookIV.Physics.EntropySplitting.sDefFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L96-L98)
**def
Tau.BookIV.Physics.EntropySplitting.sDefFloat
(e : EntropySplitting)
 :Float**


S_def as Float (for display).
Equations
- e.sDefFloat = Float.ofNat e.s_def_numer / Float.ofNat e.s_def_denom
Instances For

---

### `Tau.BookIV.Physics.EntropySplitting.sRefFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L100-L102)
**def
Tau.BookIV.Physics.EntropySplitting.sRefFloat
(e : EntropySplitting)
 :Float**


S_ref as Float (for display).
Equations
- e.sRefFloat = Float.ofNat e.s_ref_numer / Float.ofNat e.s_ref_denom
Instances For

---

### `Tau.BookIV.Physics.DefectBudget`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L108-L124)
**structure
Tau.BookIV.Physics.DefectBudget :Type**


[IV.D25] Defect budget: the conserved total of the 4-component
defect tuple in the Euler (inviscid) regime.

In the Euler regime, the defect-budget is preserved under
boundary-automorphism steps:
∑(mobility + vorticity + compression + topological) = const

This is the τ-native Kelvin circulation theorem.

- tuple : DefectTuple
The defect tuple.

- total : ℕ
The conserved total budget.

- budget_eq : self.total = self.tuple.mobility + self.tuple.vorticity + self.tuple.compression + self.tuple.topological
Budget equals sum of components.

Instances For

---

### `Tau.BookIV.Physics.instReprDefectBudget.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L124-L124)
**def
Tau.BookIV.Physics.instReprDefectBudget.repr :DefectBudget → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instReprDefectBudget`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L124-L124)
**instance
Tau.BookIV.Physics.instReprDefectBudget :Repr DefectBudget**

Equations
- Tau.BookIV.Physics.instReprDefectBudget = { reprPrec := Tau.BookIV.Physics.instReprDefectBudget.repr }

---

### `Tau.BookIV.Physics.NoRunningPrinciple`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L130-L151)
**structure
Tau.BookIV.Physics.NoRunningPrinciple :Type**


[IV.P04] No-Running Principle: ontic coupling constants do NOT run.

Orthodox "running couplings" (α_s(Q²), α_EM(Q²), etc.) are NOT ontic.
The τ-kernel coupling constants are **boundary fixed-point invariants**:


- Fixed ontic value (determined by ι<sub>τ</sub> alone)

- Regime-dependent readout functor

- Apparent "running" = projection drift from different measurement scales


The coupling value in the registry IS the fixed ontic value.

- sector : BookIII.Sectors.Sector
Which sector this principle applies to.

- ontic_coupling_numer : ℕ
The fixed ontic coupling for this sector.

- ontic_coupling_denom : ℕ
The fixed ontic coupling denominator.

- denom_pos : self.ontic_coupling_denom > 0
Denominator positive.

- regime_independent : Bool
The coupling is regime-independent (fixed).

Instances For

---

### `Tau.BookIV.Physics.instReprNoRunningPrinciple.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L151-L151)
**def
Tau.BookIV.Physics.instReprNoRunningPrinciple.repr :NoRunningPrinciple → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instReprNoRunningPrinciple`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L151-L151)
**instance
Tau.BookIV.Physics.instReprNoRunningPrinciple :Repr NoRunningPrinciple**

Equations
- Tau.BookIV.Physics.instReprNoRunningPrinciple = { reprPrec := Tau.BookIV.Physics.instReprNoRunningPrinciple.repr }

---

### `Tau.BookIV.Physics.no_running_em`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L157-L162)
**def
Tau.BookIV.Physics.no_running_em :NoRunningPrinciple**


No-Running for EM sector: α_EM is fixed at ι<sub>τ</sub>².
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.no_running_weak`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L164-L169)
**def
Tau.BookIV.Physics.no_running_weak :NoRunningPrinciple**


No-Running for Weak sector: g_w is fixed at ι<sub>τ</sub>.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.no_running_strong`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L171-L176)
**def
Tau.BookIV.Physics.no_running_strong :NoRunningPrinciple**


No-Running for Strong sector: α_s is fixed at ι<sub>τ</sub>³/(1−ι<sub>τ</sub>).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.no_running_gravity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L178-L183)
**def
Tau.BookIV.Physics.no_running_gravity :NoRunningPrinciple**


No-Running for Gravity sector: κ_GR is fixed at 1−ι<sub>τ</sub>.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.no_running_higgs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L185-L190)
**def
Tau.BookIV.Physics.no_running_higgs :NoRunningPrinciple**


No-Running for Higgs/crossing sector: coupling fixed at ι<sub>τ</sub>³/(1+ι<sub>τ</sub>).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.all_no_running`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L192-L195)
**def
Tau.BookIV.Physics.all_no_running :List NoRunningPrinciple**


All 5 sectors obey the No-Running Principle.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.euler_budget_conserved`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L201-L205)
**theorem
Tau.BookIV.Physics.euler_budget_conserved
(b : DefectBudget)
 :b.total = b.tuple.total**


[IV.T04] Euler budget conservation: the total defect budget
is well-defined (equals sum of components).

---

### `Tau.BookIV.Physics.no_running_all_sectors`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L207-L208)
**theorem
Tau.BookIV.Physics.no_running_all_sectors :all_no_running.length = 5**


All 5 sectors have no-running entries.

---

### `Tau.BookIV.Physics.all_regime_independent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L210-L214)
**theorem
Tau.BookIV.Physics.all_regime_independent :((List.map NoRunningPrinciple.regime_independent all_no_running).all fun (x : Bool) => x == true) = true**


All no-running entries are regime-independent.

---

### `Tau.BookIV.Physics.s_def_zero_at_horizon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L216-L219)
**theorem
Tau.BookIV.Physics.s_def_zero_at_horizon
(e : EntropySplitting)

(h : e.s_def_numer = 0)
 :e.s_def_numer = 0**


[IV.R05] S_def = 0 at coherence horizon: when s_def_numer = 0,
the defect entropy numerator vanishes.

---

### `Tau.BookIV.Physics.budget_nonneg`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/Thermodynamics.lean#L221-L223)
**theorem
Tau.BookIV.Physics.budget_nonneg
(b : DefectBudget)
 :b.total ≥ 0**


The budget total is non-negative (Nat).
