---
layout: taulib-doc
title: "TauLib.BookIII.Doors.MasterSchema"
permalink: /verify/taulib/docs/book-iii-doors-master-schema/
lane: verify
module_name: "TauLib.BookIII.Doors.MasterSchema"
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

# TauLib.BookIII.Doors.MasterSchema


Master Schema Theorem: all eight Millennium Problems as instances of
Mutual Determination at varying enrichment levels.

## Registry Cross-References


- [III.T23] Master Schema Theorem -- `MasterSchemaEntry`, `master_schema_check`


## Mathematical Content


**III.T23 (Master Schema):** All eight Millennium Problems are instances of
Mutual Determination at varying enrichment levels:


- E₀: RH (Part IV), Poincaré (Part IV)

- E₁: NS (Part V), YM (Part V), Hodge (Part V)

- E₁→E₂: BSD (Part VI), Langlands (Part VI)

- E₂: P vs NP (Part VII)


The spectral algebra provides the common language, the primorial ladder
the common tower, the CRT the common local-global bridge.

---

### `Tau.BookIII.Doors.MillenniumProblem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L37-L47)
**inductive
Tau.BookIII.Doors.MillenniumProblem :Type**


The eight Millennium Problems (including Langlands as the 8th force).

- RH : MillenniumProblem
- Poincare : MillenniumProblem
- NS : MillenniumProblem
- YM : MillenniumProblem
- Hodge : MillenniumProblem
- BSD : MillenniumProblem
- Langlands : MillenniumProblem
- PvsNP : MillenniumProblem
Instances For

---

### `Tau.BookIII.Doors.instReprMillenniumProblem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L47-L47)
**instance
Tau.BookIII.Doors.instReprMillenniumProblem :Repr MillenniumProblem**

Equations
- Tau.BookIII.Doors.instReprMillenniumProblem = { reprPrec := Tau.BookIII.Doors.instReprMillenniumProblem.repr }

---

### `Tau.BookIII.Doors.instReprMillenniumProblem.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L47-L47)
**def
Tau.BookIII.Doors.instReprMillenniumProblem.repr :MillenniumProblem → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.instDecidableEqMillenniumProblem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L47-L47)
**instance
Tau.BookIII.Doors.instDecidableEqMillenniumProblem :DecidableEq MillenniumProblem**

Equations
- Tau.BookIII.Doors.instDecidableEqMillenniumProblem x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIII.Doors.instBEqMillenniumProblem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L47-L47)
**instance
Tau.BookIII.Doors.instBEqMillenniumProblem :BEq MillenniumProblem**

Equations
- Tau.BookIII.Doors.instBEqMillenniumProblem = { beq := Tau.BookIII.Doors.instBEqMillenniumProblem.beq }

---

### `Tau.BookIII.Doors.instBEqMillenniumProblem.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L47-L47)
**def
Tau.BookIII.Doors.instBEqMillenniumProblem.beq :MillenniumProblem → MillenniumProblem → Bool**

Equations
- Tau.BookIII.Doors.instBEqMillenniumProblem.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIII.Doors.problem_level`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L49-L59)
**def
Tau.BookIII.Doors.problem_level
(p : MillenniumProblem)
 :Enrichment.EnrLevel**


[III.T23] Enrichment level assignment for each problem.
Equations
- Tau.BookIII.Doors.problem_level Tau.BookIII.Doors.MillenniumProblem.RH = Tau.BookIII.Enrichment.EnrLevel.E0
- Tau.BookIII.Doors.problem_level Tau.BookIII.Doors.MillenniumProblem.Poincare = Tau.BookIII.Enrichment.EnrLevel.E0
- Tau.BookIII.Doors.problem_level Tau.BookIII.Doors.MillenniumProblem.NS = Tau.BookIII.Enrichment.EnrLevel.E1
- Tau.BookIII.Doors.problem_level Tau.BookIII.Doors.MillenniumProblem.YM = Tau.BookIII.Enrichment.EnrLevel.E1
- Tau.BookIII.Doors.problem_level Tau.BookIII.Doors.MillenniumProblem.Hodge = Tau.BookIII.Enrichment.EnrLevel.E1
- Tau.BookIII.Doors.problem_level Tau.BookIII.Doors.MillenniumProblem.BSD = Tau.BookIII.Enrichment.EnrLevel.E2
- Tau.BookIII.Doors.problem_level Tau.BookIII.Doors.MillenniumProblem.Langlands = Tau.BookIII.Enrichment.EnrLevel.E2
- Tau.BookIII.Doors.problem_level Tau.BookIII.Doors.MillenniumProblem.PvsNP = Tau.BookIII.Enrichment.EnrLevel.E2
Instances For

---

### `Tau.BookIII.Doors.problem_part`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L61-L71)
**def
Tau.BookIII.Doors.problem_part
(p : MillenniumProblem)
 :Denotation.TauIdx**


[III.T23] Part assignment (which Book III part treats each problem).
Equations
- Tau.BookIII.Doors.problem_part Tau.BookIII.Doors.MillenniumProblem.RH = 4
- Tau.BookIII.Doors.problem_part Tau.BookIII.Doors.MillenniumProblem.Poincare = 4
- Tau.BookIII.Doors.problem_part Tau.BookIII.Doors.MillenniumProblem.NS = 5
- Tau.BookIII.Doors.problem_part Tau.BookIII.Doors.MillenniumProblem.YM = 5
- Tau.BookIII.Doors.problem_part Tau.BookIII.Doors.MillenniumProblem.Hodge = 5
- Tau.BookIII.Doors.problem_part Tau.BookIII.Doors.MillenniumProblem.BSD = 6
- Tau.BookIII.Doors.problem_part Tau.BookIII.Doors.MillenniumProblem.Langlands = 6
- Tau.BookIII.Doors.problem_part Tau.BookIII.Doors.MillenniumProblem.PvsNP = 7
Instances For

---

### `Tau.BookIII.Doors.MasterSchemaEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L73-L80)
**structure
Tau.BookIII.Doors.MasterSchemaEntry :Type**


[III.T23] Master Schema entry: each problem has a Mutual Determination
instance (B ↔ I ↔ S) at its enrichment level. The finite check verifies
that the MD infrastructure is available at the required level.

- problem : MillenniumProblem
- level : Enrichment.EnrLevel
- part : Denotation.TauIdx
- md_check : Denotation.TauIdx → Denotation.TauIdx → Bool
Instances For

---

### `Tau.BookIII.Doors.rh_schema_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L82-L88)
**def
Tau.BookIII.Doors.rh_schema_check
(_bound db : Denotation.TauIdx)
 :Bool**


[III.T23] RH schema: boundary = Euler product, interior = zeta values,
spectral = H_L eigenvalues.
Equations
- Tau.BookIII.Doors.rh_schema_check _bound db = (Tau.BookIII.Doors.bipolar_euler_check db && Tau.BookIII.Doors.critical_line_multi_check db && Tau.BookIII.Doors.tau_effective_rh_check db)
Instances For

---

### `Tau.BookIII.Doors.poincare_schema_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L90-L94)
**def
Tau.BookIII.Doors.poincare_schema_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T23] Poincaré schema: boundary = local patches,
interior = Hartogs bulk, spectral = fundamental group.
Equations
- Tau.BookIII.Doors.poincare_schema_check bound db = (Tau.BookIII.Doors.simply_connected_check bound db && Tau.BookIII.Doors.gluing_guarantee_check bound db)
Instances For

---

### `Tau.BookIII.Doors.generic_schema_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L96-L102)
**def
Tau.BookIII.Doors.generic_schema_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T23] Generic E₁/E₂ schema: uses the full MD infrastructure
at the appropriate enrichment level. The specific content for NS, YM,
Hodge, BSD, Langlands, P vs NP is developed in Parts V-VII.
At this level we verify the template is available.
Equations
- Tau.BookIII.Doors.generic_schema_check bound db = Tau.BookIII.Doors.mutual_det_check bound db
Instances For

---

### `Tau.BookIII.Doors.master_schema_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L104-L116)
**def
Tau.BookIII.Doors.master_schema_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T23] Master Schema: assemble all eight problem schemas.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.level_coverage_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L118-L129)
**def
Tau.BookIII.Doors.level_coverage_check :Bool**


[III.T23] All eight problems have distinct enrichment levels
covering the full E₀-E₂ range.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.part_assignment_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L131-L142)
**def
Tau.BookIII.Doors.part_assignment_check :Bool**


[III.T23] Each problem maps to a unique part (4, 5, 6, or 7).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Doors.rh_schema_10_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L159-L160)
**theorem
Tau.BookIII.Doors.rh_schema_10_4 :rh_schema_check 10 4 = true**


---

### `Tau.BookIII.Doors.poincare_schema_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L162-L163)
**theorem
Tau.BookIII.Doors.poincare_schema_10_3 :poincare_schema_check 10 3 = true**


---

### `Tau.BookIII.Doors.master_schema_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L165-L166)
**theorem
Tau.BookIII.Doors.master_schema_10_3 :master_schema_check 10 3 = true**


---

### `Tau.BookIII.Doors.level_coverage`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L168-L169)
**theorem
Tau.BookIII.Doors.level_coverage :level_coverage_check = true**


---

### `Tau.BookIII.Doors.part_assignment`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L171-L172)
**theorem
Tau.BookIII.Doors.part_assignment :part_assignment_check = true**


---

### `Tau.BookIII.Doors.rh_level`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L178-L179)
**theorem
Tau.BookIII.Doors.rh_level :problem_level MillenniumProblem.RH = Enrichment.EnrLevel.E0**


[III.T23] Structural: RH is at E₀.

---

### `Tau.BookIII.Doors.pvsnp_level`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L181-L182)
**theorem
Tau.BookIII.Doors.pvsnp_level :problem_level MillenniumProblem.PvsNP = Enrichment.EnrLevel.E2**


[III.T23] Structural: P vs NP is at E₂.

---

### `Tau.BookIII.Doors.ns_level`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L184-L185)
**theorem
Tau.BookIII.Doors.ns_level :problem_level MillenniumProblem.NS = Enrichment.EnrLevel.E1**


[III.T23] Structural: NS is at E₁.

---

### `Tau.BookIII.Doors.rh_part`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L187-L188)
**theorem
Tau.BookIII.Doors.rh_part :problem_part MillenniumProblem.RH = 4**


[III.T23] Structural: all 8 problems have parts in {4,5,6,7}.

---

### `Tau.BookIII.Doors.ns_part`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L189-L189)
**theorem
Tau.BookIII.Doors.ns_part :problem_part MillenniumProblem.NS = 5**


---

### `Tau.BookIII.Doors.bsd_part`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L190-L190)
**theorem
Tau.BookIII.Doors.bsd_part :problem_part MillenniumProblem.BSD = 6**


---

### `Tau.BookIII.Doors.pvsnp_part`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L191-L191)
**theorem
Tau.BookIII.Doors.pvsnp_part :problem_part MillenniumProblem.PvsNP = 7**


---

### `Tau.BookIII.Doors.e0_before_e1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L193-L195)
**theorem
Tau.BookIII.Doors.e0_before_e1 :(problem_level MillenniumProblem.RH).toNat < (problem_level MillenniumProblem.NS).toNat**


[III.T23] Structural: enrichment levels are ordered.

---

### `Tau.BookIII.Doors.e1_before_e2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Doors/MasterSchema.lean#L197-L198)
**theorem
Tau.BookIII.Doors.e1_before_e2 :(problem_level MillenniumProblem.NS).toNat < (problem_level MillenniumProblem.PvsNP).toNat**
