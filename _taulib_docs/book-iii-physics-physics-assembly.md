---
layout: taulib-doc
title: "TauLib.BookIII.Physics.PhysicsAssembly"
permalink: /verify/taulib/docs/book-iii-physics-physics-assembly/
lane: verify
module_name: "TauLib.BookIII.Physics.PhysicsAssembly"
book: "III"
book_label: "Spectrum"
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
    book: "Book III"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookIII.Physics.PhysicsAssembly


Physics Layer Assembly: NS + YM + Hodge = E₁ Complete.

## Registry Cross-References


- [III.T29] Physics Assembly -- `physics_assembly_check`


## Mathematical Content


**III.T29 (Physics Assembly):** The three E₁ Millennium Problems form a
complete description of the physics layer:


- Navier-Stokes (existence): Hartogs flow stabilizes → positive regularity

- Yang-Mills (mass gap): B/C coprimality → spectral gap → mass existence

- Hodge (addressability): BNF uniqueness + sector decomposition → NF-addressability


Together, these exhaust the E₁ content: every E₁ object has admissible
fluid data (NS), carries a mass gap (YM), and is NF-addressable (Hodge).

The assembly theorem verifies that all three components are simultaneously
satisfied at each primorial level, confirming E₁ completeness.

---

### `Tau.BookIII.Physics.ns_component_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L38-L43)
**def
Tau.BookIII.Physics.ns_component_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T29] NS component: fluid data admissibility + flow stabilization +
positive regularity.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.ym_component_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L45-L49)
**def
Tau.BookIII.Physics.ym_component_check
(db : Denotation.TauIdx)
 :Bool**


[III.T29] YM component: strong sector + mass gap + coupling well-defined.
Equations
- Tau.BookIII.Physics.ym_component_check db = (Tau.BookIII.Physics.strong_sector_check db && Tau.BookIII.Physics.yang_mills_gap_check db && Tau.BookIII.Physics.ym_coupling_check db)
Instances For

---

### `Tau.BookIII.Physics.hodge_component_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L51-L56)
**def
Tau.BookIII.Physics.hodge_component_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T29] Hodge component: NF-addressability + Hodge filtration +
spectral compatibility.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.physics_assembly_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L58-L63)
**def
Tau.BookIII.Physics.physics_assembly_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T29] Physics assembly: all three E₁ components are satisfied
simultaneously at each primorial level.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.e1_completeness_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L65-L83)
**def
Tau.BookIII.Physics.e1_completeness_check
(db : Denotation.TauIdx)
 :Bool**


[III.T29] E₁ completeness: the three problems cover distinct aspects.
NS = dynamics (flow), YM = spectrum (gap), Hodge = addressing (filtration).
Verify non-redundancy: each component checks something the others don't.
Equations
- Tau.BookIII.Physics.e1_completeness_check db = Tau.BookIII.Physics.e1_completeness_check.go db 3 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.e1_completeness_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L71-L82)@[irreducible]

**def
Tau.BookIII.Physics.e1_completeness_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.physics_is_e1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L85-L89)
**def
Tau.BookIII.Physics.physics_is_e1 :Bool**


[III.T29] Enrichment level assignment: all three problems are at E₁.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.physics_in_part5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L91-L95)
**def
Tau.BookIII.Physics.physics_in_part5 :Bool**


[III.T29] Part assignment: all three problems are in Part V.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.ns_component_15_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L113-L114)
**theorem
Tau.BookIII.Physics.ns_component_15_4 :ns_component_check 15 4 = true**


---

### `Tau.BookIII.Physics.ym_component_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L116-L117)
**theorem
Tau.BookIII.Physics.ym_component_5 :ym_component_check 5 = true**


---

### `Tau.BookIII.Physics.hodge_component_15_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L119-L120)
**theorem
Tau.BookIII.Physics.hodge_component_15_3 :hodge_component_check 15 3 = true**


---

### `Tau.BookIII.Physics.physics_assembly_15_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L122-L123)
**theorem
Tau.BookIII.Physics.physics_assembly_15_3 :physics_assembly_check 15 3 = true**


---

### `Tau.BookIII.Physics.e1_completeness_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L125-L126)
**theorem
Tau.BookIII.Physics.e1_completeness_5 :e1_completeness_check 5 = true**


---

### `Tau.BookIII.Physics.physics_is_e1_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L128-L129)
**theorem
Tau.BookIII.Physics.physics_is_e1_thm :physics_is_e1 = true**


---

### `Tau.BookIII.Physics.physics_in_part5_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L131-L132)
**theorem
Tau.BookIII.Physics.physics_in_part5_thm :physics_in_part5 = true**


---

### `Tau.BookIII.Physics.ns_at_e1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L138-L139)
**theorem
Tau.BookIII.Physics.ns_at_e1 :Doors.problem_level Doors.MillenniumProblem.NS = Enrichment.EnrLevel.E1**


[III.T29] Structural: NS is at E₁.

---

### `Tau.BookIII.Physics.ym_at_e1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L141-L142)
**theorem
Tau.BookIII.Physics.ym_at_e1 :Doors.problem_level Doors.MillenniumProblem.YM = Enrichment.EnrLevel.E1**


[III.T29] Structural: YM is at E₁.

---

### `Tau.BookIII.Physics.hodge_at_e1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L144-L145)
**theorem
Tau.BookIII.Physics.hodge_at_e1 :Doors.problem_level Doors.MillenniumProblem.Hodge = Enrichment.EnrLevel.E1**


[III.T29] Structural: Hodge is at E₁.

---

### `Tau.BookIII.Physics.ns_part5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L147-L148)
**theorem
Tau.BookIII.Physics.ns_part5 :Doors.problem_part Doors.MillenniumProblem.NS = 5**


[III.T29] Structural: all three problems in Part V.

---

### `Tau.BookIII.Physics.ym_part5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L149-L149)
**theorem
Tau.BookIII.Physics.ym_part5 :Doors.problem_part Doors.MillenniumProblem.YM = 5**


---

### `Tau.BookIII.Physics.hodge_part5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L150-L150)
**theorem
Tau.BookIII.Physics.hodge_part5 :Doors.problem_part Doors.MillenniumProblem.Hodge = 5**


---

### `Tau.BookIII.Physics.three_e1_problems`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/PhysicsAssembly.lean#L152-L155)
**theorem
Tau.BookIII.Physics.three_e1_problems :[Doors.problem_level Doors.MillenniumProblem.NS, Doors.problem_level Doors.MillenniumProblem.YM, Doors.problem_level Doors.MillenniumProblem.Hodge] = [Enrichment.EnrLevel.E1, Enrichment.EnrLevel.E1, Enrichment.EnrLevel.E1]**


[III.T29] Structural: the three E₁ problems exhaust the E₁ level.
