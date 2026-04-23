---
layout: taulib-doc
title: "TauLib.BookVI.Closure.Ecosystem"
permalink: /verify/taulib/docs/book-vi-closure-ecosystem/
lane: verify
module_name: "TauLib.BookVI.Closure.Ecosystem"
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

# TauLib.BookVI.Closure.Ecosystem


Ecosystems: inter-sector web, biogeochemical circulation, repair budget.

## Registry Cross-References


- [VI.D44] Inter-Sector Web — `InterSectorWeb`

- [VI.D45] Repair Budget — `RepairBudget`

- [VI.T24] Ecosystem as Multi-Scale Poincaré Circulation — `ecosystem_poincare`

- [VI.P17] Metamorphosis Preserves SelfDesc — `metamorphosis_selfdesc`


## Cross-Book Authority


- Book III, Part II: Poincaré force (periodic orbits → biogeochemical cycles)

- Book I, Part VII: Colimits (categorical universal construction → lichen)


## Ground Truth Sources


- Book VI Chapter 31 (2nd Edition): Symbiosis and Ecosystems

- Book VI Chapter 32 (2nd Edition): Healing, Regeneration, and Repair


---

### `Tau.BookVI.Ecosystem.InterSectorWeb`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L31-L44)
**structure
Tau.BookVI.Ecosystem.InterSectorWeb :Type**


[VI.D44] Inter-Sector Web: coupling graph between Life sectors.
Each sector (persistence, agency, source, closure, consumer) is a node;
edges represent inter-sector metabolic or informational coupling.
Every ecosystem is an Inter-Sector Web.

- sector_count : ℕ
Number of sector nodes.

- count_eq : self.sector_count = 5
Exactly 5 sectors.

- connected : Bool
Web is connected (every sector couples to at least one other).

- source_closure_dual : Bool
Source-closure duality: these two sectors are always coupled.

Instances For

---

### `Tau.BookVI.Ecosystem.instReprInterSectorWeb`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L44-L44)
**instance
Tau.BookVI.Ecosystem.instReprInterSectorWeb :Repr InterSectorWeb**

Equations
- Tau.BookVI.Ecosystem.instReprInterSectorWeb = { reprPrec := Tau.BookVI.Ecosystem.instReprInterSectorWeb.repr }

---

### `Tau.BookVI.Ecosystem.instReprInterSectorWeb.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L44-L44)
**def
Tau.BookVI.Ecosystem.instReprInterSectorWeb.repr :InterSectorWeb → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Ecosystem.isw`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L46-L48)
**def
Tau.BookVI.Ecosystem.isw :InterSectorWeb**

Equations
- Tau.BookVI.Ecosystem.isw = { sector_count := 5, count_eq := Tau.BookVI.Ecosystem.isw._proof_1 }
Instances For

---

### `Tau.BookVI.Ecosystem.inter_sector_web_five`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L50-L51)
**theorem
Tau.BookVI.Ecosystem.inter_sector_web_five :isw.sector_count = 5**


---

### `Tau.BookVI.Ecosystem.inter_sector_web_connected`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L53-L55)
**theorem
Tau.BookVI.Ecosystem.inter_sector_web_connected :isw.connected = true ∧ isw.source_closure_dual = true**


---

### `Tau.BookVI.Ecosystem.EcosystemPoincare`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L61-L77)
**structure
Tau.BookVI.Ecosystem.EcosystemPoincare :Type**


[VI.T24] Ecosystem as Multi-Scale Poincaré Circulation.
Every biogeochemical element traces a closed orbit in the
inter-sector coupling graph. This is Poincaré circulation
(Book III, Part II) at the ecosystem scale.
Examples: carbon cycle, nitrogen cycle (6 steps), water cycle.

- major_cycles : ℕ
Number of major biogeochemical cycles formalized.

- cycles_ge : self.major_cycles ≥ 3
At least 3 (C, N, H₂O).

- all_closed : Bool
All cycles are closed (Poincaré circulation).

- multi_scale : Bool
Multi-scale: cell → organism → ecosystem.

- poincare_authority : Bool
Authority: Book III, Part II (Poincaré force).

Instances For

---

### `Tau.BookVI.Ecosystem.instReprEcosystemPoincare.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L77-L77)
**def
Tau.BookVI.Ecosystem.instReprEcosystemPoincare.repr :EcosystemPoincare → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Ecosystem.instReprEcosystemPoincare`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L77-L77)
**instance
Tau.BookVI.Ecosystem.instReprEcosystemPoincare :Repr EcosystemPoincare**

Equations
- Tau.BookVI.Ecosystem.instReprEcosystemPoincare = { reprPrec := Tau.BookVI.Ecosystem.instReprEcosystemPoincare.repr }

---

### `Tau.BookVI.Ecosystem.eco_poincare`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L79-L81)
**def
Tau.BookVI.Ecosystem.eco_poincare :EcosystemPoincare**

Equations
- Tau.BookVI.Ecosystem.eco_poincare = { major_cycles := 3, cycles_ge := Tau.BookVI.Ecosystem.eco_poincare._proof_1 }
Instances For

---

### `Tau.BookVI.Ecosystem.ecosystem_poincare`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L83-L87)
**theorem
Tau.BookVI.Ecosystem.ecosystem_poincare :eco_poincare.major_cycles ≥ 3 ∧ eco_poincare.all_closed = true ∧ eco_poincare.multi_scale = true**


---

### `Tau.BookVI.Ecosystem.RepairBudget`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L93-L104)
**structure
Tau.BookVI.Ecosystem.RepairBudget :Type**


[VI.D45] Repair Budget: finite resource for SelfDesc maintenance.
R_max = maximum cumulative repair before defect overwhelms.
Connects to SelfDesc Closure Theorem (VI.T03):
perturbations within basin are corrected, but R_max bounds the basin.

- finite_budget : Bool
Budget is finite for finite-lineage carriers.

- bounds_basin : Bool
Budget bounds the SelfDesc basin.

- selfdesc_connection : Bool
Connects to SelfDesc Closure (VI.T03).

Instances For

---

### `Tau.BookVI.Ecosystem.instReprRepairBudget`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L104-L104)
**instance
Tau.BookVI.Ecosystem.instReprRepairBudget :Repr RepairBudget**

Equations
- Tau.BookVI.Ecosystem.instReprRepairBudget = { reprPrec := Tau.BookVI.Ecosystem.instReprRepairBudget.repr }

---

### `Tau.BookVI.Ecosystem.instReprRepairBudget.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L104-L104)
**def
Tau.BookVI.Ecosystem.instReprRepairBudget.repr :RepairBudget → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Ecosystem.repair_budget`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L106-L106)
**def
Tau.BookVI.Ecosystem.repair_budget :RepairBudget**

Equations
- Tau.BookVI.Ecosystem.repair_budget = { }
Instances For

---

### `Tau.BookVI.Ecosystem.repair_budget_finite`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L108-L111)
**theorem
Tau.BookVI.Ecosystem.repair_budget_finite :repair_budget.finite_budget = true ∧ repair_budget.bounds_basin = true**


---

### `Tau.BookVI.Ecosystem.MetamorphosisSelfDesc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L117-L129)
**structure
Tau.BookVI.Ecosystem.MetamorphosisSelfDesc :Type**


[VI.P17] Metamorphosis Preserves SelfDesc.
ω-germ codes are identical in larva and adult;
SelfDesc holds at every instant of metamorphosis.
The code is a profinite invariant (Book II, Part X) that
persists through substrate replacement.

- code_preserved : Bool
ω-germ code preserved across metamorphosis.

- selfdesc_continuous : Bool
SelfDesc holds at every instant.

- profinite_invariant : Bool
Code is profinite invariant (Book II, Part X).

Instances For

---

### `Tau.BookVI.Ecosystem.instReprMetamorphosisSelfDesc.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L129-L129)
**def
Tau.BookVI.Ecosystem.instReprMetamorphosisSelfDesc.repr :MetamorphosisSelfDesc → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.Ecosystem.instReprMetamorphosisSelfDesc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L129-L129)
**instance
Tau.BookVI.Ecosystem.instReprMetamorphosisSelfDesc :Repr MetamorphosisSelfDesc**

Equations
- Tau.BookVI.Ecosystem.instReprMetamorphosisSelfDesc = { reprPrec := Tau.BookVI.Ecosystem.instReprMetamorphosisSelfDesc.repr }

---

### `Tau.BookVI.Ecosystem.metamorphosis`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L131-L131)
**def
Tau.BookVI.Ecosystem.metamorphosis :MetamorphosisSelfDesc**

Equations
- Tau.BookVI.Ecosystem.metamorphosis = { }
Instances For

---

### `Tau.BookVI.Ecosystem.metamorphosis_selfdesc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookVI/Closure/Ecosystem.lean#L133-L137)
**theorem
Tau.BookVI.Ecosystem.metamorphosis_selfdesc :metamorphosis.code_preserved = true ∧ metamorphosis.selfdesc_continuous = true ∧ metamorphosis.profinite_invariant = true**
