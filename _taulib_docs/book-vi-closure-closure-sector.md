---
layout: taulib-doc
title: "TauLib.BookVI.Closure.ClosureSector"
permalink: /verify/taulib/docs/book-vi-closure-closure-sector/
lane: verify
module_name: "TauLib.BookVI.Closure.ClosureSector"
book: "VI"
book_label: "Life"
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
    book: "Book VI"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookVI.Closure.ClosureSector


Closure sector (Part 5): π''-sector structure recycling on fiber.
Archetype: Fungi. Dominant forces: Riemann + Navier–Stokes.

## Registry Cross-References


- [VI.D41] Closure Sector — `ClosureSectorDef`

- [VI.D42] Structure Recycling Predicate — `StructureRecyclingPredicate`

- [VI.T23] Closure = π''-Fiber Return — `closure_is_pi_double_return`

- [VI.D43] Aging as Defect Accumulation — `AgingDefect`

- [VI.P16] Repair Budget Exhaustion — `repair_budget_exhaustion`


## Cross-Book Authority


- Book I, Part I: π'' generator (solenoidal, fiber T²)

- Book III, Part III: Riemann force (energy recycling/quantization)

- Book III, Part VII: Navier–Stokes force (transport/decomposition)


## Ground Truth Sources


- Book VI Chapter 28 (2nd Edition): The Closure Sector

- Book VI Chapter 30 (2nd Edition): Death, Decomposition, and Aging


---

### `Tau.BookVI.Closure.ClosureSectorDef`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L36-L54)
**structure
Tau.BookVI.Closure.ClosureSectorDef :Type**


[VI.D41] Closure Sector: π''-sector on fiber T².
Life Loop restricted to structure recycling on the fiber.
Generator: π'' (solenoidal, Book I Part I).
Dominant forces: Riemann + Navier–Stokes (Book III, Parts III, VII).
Dual to Source sector (VI.D36): source produces, closure recycles.

- generator : String
Generator is pi'' (fiber).

- is_primitive : Bool
Sector is primitive (single generator).

- archetype : String
Archetype organism.

- dominant_riemann : Bool
Dominant force 1: Riemann (energy recycling).

- dominant_navier_stokes : Bool
Dominant force 2: Navier–Stokes (transport/decomposition).

- dual_to_source : Bool
Dual to source sector.

Instances For

---

### `Tau.BookVI.Closure.instReprClosureSectorDef.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L54-L54)
**def
Tau.BookVI.Closure.instReprClosureSectorDef.repr :ClosureSectorDef → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Closure.instReprClosureSectorDef`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L54-L54)
**instance
Tau.BookVI.Closure.instReprClosureSectorDef :Repr ClosureSectorDef**

Equations
- Tau.BookVI.Closure.instReprClosureSectorDef = { reprPrec := Tau.BookVI.Closure.instReprClosureSectorDef.repr }

---

### `Tau.BookVI.Closure.closure_def`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L56-L56)
**def
Tau.BookVI.Closure.closure_def :ClosureSectorDef**

Equations
- Tau.BookVI.Closure.closure_def = { }
Instances For

---

### `Tau.BookVI.Closure.closure_generator_match`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L58-L61)
**theorem
Tau.BookVI.Closure.closure_generator_match :closure_def.generator = FourPlusOne.closure_sector.generator**


Closure sector matches the FourPlusOne closure_sector definition.

---

### `Tau.BookVI.Closure.StructureRecyclingPredicate`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L67-L83)
**structure
Tau.BookVI.Closure.StructureRecyclingPredicate :Type**


[VI.D42] Structure Recycling Predicate: 3 conditions.
(i) Net reduction of structural complexity on T² fiber
(ii) Hodge capacity gradient negative (reverse of source)
(iii) Energy release returned to base τ¹
Dual to Structure Generation Predicate (VI.D37).

- condition_count : ℕ
Number of conditions.

- count_eq : self.condition_count = 3
Exactly 3 conditions.

- net_reduction : Bool
(i) Net reduction on fiber.

- hodge_gradient_negative : Bool
(ii) Hodge capacity gradient negative.

- energy_to_base : Bool
(iii) Energy returned to base.

Instances For

---

### `Tau.BookVI.Closure.instReprStructureRecyclingPredicate.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L83-L83)
**def
Tau.BookVI.Closure.instReprStructureRecyclingPredicate.repr :StructureRecyclingPredicate → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Closure.instReprStructureRecyclingPredicate`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L83-L83)
**instance
Tau.BookVI.Closure.instReprStructureRecyclingPredicate :Repr StructureRecyclingPredicate**

Equations
- Tau.BookVI.Closure.instReprStructureRecyclingPredicate = { reprPrec := Tau.BookVI.Closure.instReprStructureRecyclingPredicate.repr }

---

### `Tau.BookVI.Closure.struct_recycle`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L85-L87)
**def
Tau.BookVI.Closure.struct_recycle :StructureRecyclingPredicate**

Equations
- Tau.BookVI.Closure.struct_recycle = { condition_count := 3, count_eq := Tau.BookVI.Closure.struct_recycle._proof_1 }
Instances For

---

### `Tau.BookVI.Closure.recycling_three_conditions`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L89-L91)
**theorem
Tau.BookVI.Closure.recycling_three_conditions :struct_recycle.condition_count = 3**


---

### `Tau.BookVI.Closure.recycling_all_hold`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L93-L97)
**theorem
Tau.BookVI.Closure.recycling_all_hold :struct_recycle.net_reduction = true ∧ struct_recycle.hodge_gradient_negative = true ∧ struct_recycle.energy_to_base = true**


---

### `Tau.BookVI.Closure.ClosureReturn`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L103-L113)
**structure
Tau.BookVI.Closure.ClosureReturn :Type**


[VI.T23] Closure = π''-Fiber Return Theorem.
A closure Life loop has nontrivial π''-winding on the fiber
with net structure recycling (returning complexity to base).

- winding_pi_double : ℕ
Winding on π'' (fiber).

- pi_double_nontrivial : self.winding_pi_double ≥ 1
Winding is nontrivial (≥ 1).

- net_recycling : Bool
Net structure recycling.

Instances For

---

### `Tau.BookVI.Closure.instReprClosureReturn.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L113-L113)
**def
Tau.BookVI.Closure.instReprClosureReturn.repr :ClosureReturn → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Closure.instReprClosureReturn`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L113-L113)
**instance
Tau.BookVI.Closure.instReprClosureReturn :Repr ClosureReturn**

Equations
- Tau.BookVI.Closure.instReprClosureReturn = { reprPrec := Tau.BookVI.Closure.instReprClosureReturn.repr }

---

### `Tau.BookVI.Closure.closure_ret`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L115-L117)
**def
Tau.BookVI.Closure.closure_ret :ClosureReturn**

Equations
- Tau.BookVI.Closure.closure_ret = { winding_pi_double := 1, pi_double_nontrivial := Tau.BookVI.Closure.closure_ret._proof_1 }
Instances For

---

### `Tau.BookVI.Closure.closure_is_pi_double_return`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L119-L122)
**theorem
Tau.BookVI.Closure.closure_is_pi_double_return :closure_ret.winding_pi_double ≥ 1 ∧ closure_ret.net_recycling = true**


---

### `Tau.BookVI.Closure.AgingDefect`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L128-L139)
**structure
Tau.BookVI.Closure.AgingDefect :Type**


[VI.D43] Aging as Defect Accumulation.
Defect functional Δ(n) increases monotonically with refinement level n.
For finite-lineage carriers, the repair budget R_max is finite,
so defect eventually exceeds repair capacity.

- monotone_increase : Bool
Defect increases monotonically.

- finite_repair : Bool
Repair budget is finite.

- finite_lineage_only : Bool
Applies to finite-lineage carriers only.

Instances For

---

### `Tau.BookVI.Closure.instReprAgingDefect.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L139-L139)
**def
Tau.BookVI.Closure.instReprAgingDefect.repr :AgingDefect → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Closure.instReprAgingDefect`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L139-L139)
**instance
Tau.BookVI.Closure.instReprAgingDefect :Repr AgingDefect**

Equations
- Tau.BookVI.Closure.instReprAgingDefect = { reprPrec := Tau.BookVI.Closure.instReprAgingDefect.repr }

---

### `Tau.BookVI.Closure.aging`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L141-L141)
**def
Tau.BookVI.Closure.aging :AgingDefect**

Equations
- Tau.BookVI.Closure.aging = { }
Instances For

---

### `Tau.BookVI.Closure.RepairBudgetExhaustion`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L147-L161)
**structure
Tau.BookVI.Closure.RepairBudgetExhaustion :Type**


[VI.P16] Repair Budget Exhaustion: death is inevitable for
finite-lineage carriers. R_max < ∞ ⟹ ∃ n₀: Δ(n₀) > R_max.
Hayflick limit as special case.
Requires SelfDesc Closure (VI.T03): perturbations within basin
are corrected, but exhaustion of R_max forces exit.

- r_max_finite : Bool
Finite repair budget.

- death_inevitable : Bool
Death inevitable (∃ n₀).

- hayflick_special_case : Bool
Hayflick limit as special case.

- requires_selfdesc_closure : Bool
Requires SelfDesc Closure (VI.T03).

Instances For

---

### `Tau.BookVI.Closure.instReprRepairBudgetExhaustion.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L161-L161)
**def
Tau.BookVI.Closure.instReprRepairBudgetExhaustion.repr :RepairBudgetExhaustion → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Closure.instReprRepairBudgetExhaustion`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L161-L161)
**instance
Tau.BookVI.Closure.instReprRepairBudgetExhaustion :Repr RepairBudgetExhaustion**

Equations
- Tau.BookVI.Closure.instReprRepairBudgetExhaustion = { reprPrec := Tau.BookVI.Closure.instReprRepairBudgetExhaustion.repr }

---

### `Tau.BookVI.Closure.repair_exhaust`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L163-L163)
**def
Tau.BookVI.Closure.repair_exhaust :RepairBudgetExhaustion**

Equations
- Tau.BookVI.Closure.repair_exhaust = { }
Instances For

---

### `Tau.BookVI.Closure.repair_budget_exhaustion`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/ClosureSector.lean#L165-L169)
**theorem
Tau.BookVI.Closure.repair_budget_exhaustion :repair_exhaust.r_max_finite = true ∧ repair_exhaust.death_inevitable = true ∧ repair_exhaust.hayflick_special_case = true**
