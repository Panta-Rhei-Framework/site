---
layout: taulib-doc
title: "TauLib.BookI.MetaLogic.Substrate"
permalink: /verify/taulib/docs/book-i-meta-logic-substrate/
lane: verify
module_name: "TauLib.BookI.MetaLogic.Substrate"
book: "I"
book_label: "Foundations"
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
    book: "Book I"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.MetaLogic.Substrate


The meta-logical substrate: CIC structural rules and their status in τ.

## Registry Cross-References


- [I.D77] Meta-Logical Substrate — `MetaLogicalSubstrate`

- [I.R15] Structural Rules Inventory — structural rule classification


## Mathematical Content


CIC provides three structural rules: contraction, weakening, exchange.
K5's diagonal discipline refuses contraction and weakening at the object level
while preserving exchange. This module formalizes that classification.

---

### `Tau.MetaLogic.StructuralRule`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L28-L33)
**inductive
Tau.MetaLogic.StructuralRule :Type**


The three structural rules of classical sequent calculus.

- contraction : StructuralRule
- weakening : StructuralRule
- exchange : StructuralRule
Instances For

---

### `Tau.MetaLogic.instDecidableEqStructuralRule`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L33-L33)
**instance
Tau.MetaLogic.instDecidableEqStructuralRule :DecidableEq StructuralRule**

Equations
- Tau.MetaLogic.instDecidableEqStructuralRule x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.MetaLogic.instReprStructuralRule`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L33-L33)
**instance
Tau.MetaLogic.instReprStructuralRule :Repr StructuralRule**

Equations
- Tau.MetaLogic.instReprStructuralRule = { reprPrec := Tau.MetaLogic.instReprStructuralRule.repr }

---

### `Tau.MetaLogic.instReprStructuralRule.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L33-L33)
**def
Tau.MetaLogic.instReprStructuralRule.repr :StructuralRule → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.ObjectLevelStatus`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L41-L45)
**inductive
Tau.MetaLogic.ObjectLevelStatus :Type**


The object-level status of a structural rule under K5's diagonal discipline.

- refused : ObjectLevelStatus
- preserved : ObjectLevelStatus
Instances For

---

### `Tau.MetaLogic.instDecidableEqObjectLevelStatus`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L45-L45)
**instance
Tau.MetaLogic.instDecidableEqObjectLevelStatus :DecidableEq ObjectLevelStatus**

Equations
- Tau.MetaLogic.instDecidableEqObjectLevelStatus x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.MetaLogic.instReprObjectLevelStatus`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L45-L45)
**instance
Tau.MetaLogic.instReprObjectLevelStatus :Repr ObjectLevelStatus**

Equations
- Tau.MetaLogic.instReprObjectLevelStatus = { reprPrec := Tau.MetaLogic.instReprObjectLevelStatus.repr }

---

### `Tau.MetaLogic.instReprObjectLevelStatus.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L45-L45)
**def
Tau.MetaLogic.instReprObjectLevelStatus.repr :ObjectLevelStatus → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.k5_status`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L49-L54)
**def
Tau.MetaLogic.k5_status :StructuralRule → ObjectLevelStatus**


K5's classification: contraction and weakening are refused,
exchange is preserved.
Equations
- Tau.MetaLogic.k5_status Tau.MetaLogic.StructuralRule.contraction = Tau.MetaLogic.ObjectLevelStatus.refused
- Tau.MetaLogic.k5_status Tau.MetaLogic.StructuralRule.weakening = Tau.MetaLogic.ObjectLevelStatus.refused
- Tau.MetaLogic.k5_status Tau.MetaLogic.StructuralRule.exchange = Tau.MetaLogic.ObjectLevelStatus.preserved
Instances For

---

### `Tau.MetaLogic.contraction_refused`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L60-L61)
**theorem
Tau.MetaLogic.contraction_refused :k5_status StructuralRule.contraction = ObjectLevelStatus.refused**


Contraction is refused at the object level.

---

### `Tau.MetaLogic.weakening_refused`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L63-L64)
**theorem
Tau.MetaLogic.weakening_refused :k5_status StructuralRule.weakening = ObjectLevelStatus.refused**


Weakening is refused at the object level.

---

### `Tau.MetaLogic.exchange_preserved`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L66-L67)
**theorem
Tau.MetaLogic.exchange_preserved :k5_status StructuralRule.exchange = ObjectLevelStatus.preserved**


Exchange is preserved at the object level.

---

### `Tau.MetaLogic.allRules`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L73-L74)
**def
Tau.MetaLogic.allRules :List StructuralRule**


The complete list of structural rules.
Equations
- Tau.MetaLogic.allRules = [Tau.MetaLogic.StructuralRule.contraction, Tau.MetaLogic.StructuralRule.weakening, Tau.MetaLogic.StructuralRule.exchange]
Instances For

---

### `Tau.MetaLogic.allRules_length`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L76-L77)
**theorem
Tau.MetaLogic.allRules_length :allRules.length = 3**


There are exactly 3 structural rules.

---

### `Tau.MetaLogic.refusedRules`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L79-L81)
**def
Tau.MetaLogic.refusedRules :List StructuralRule**


The rules refused by K5 at the object level.
Equations
- Tau.MetaLogic.refusedRules = List.filter
 (fun (r : Tau.MetaLogic.StructuralRule) => Tau.MetaLogic.k5_status r == Tau.MetaLogic.ObjectLevelStatus.refused)
 Tau.MetaLogic.allRules
Instances For

---

### `Tau.MetaLogic.preservedRules`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L83-L85)
**def
Tau.MetaLogic.preservedRules :List StructuralRule**


The rules preserved by K5 at the object level.
Equations
- Tau.MetaLogic.preservedRules = List.filter
 (fun (r : Tau.MetaLogic.StructuralRule) => Tau.MetaLogic.k5_status r == Tau.MetaLogic.ObjectLevelStatus.preserved)
 Tau.MetaLogic.allRules
Instances For

---

### `Tau.MetaLogic.refused_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L87-L88)
**theorem
Tau.MetaLogic.refused_count :refusedRules.length = 2**


Exactly 2 rules are refused.

---

### `Tau.MetaLogic.preserved_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L90-L91)
**theorem
Tau.MetaLogic.preserved_count :preservedRules.length = 1**


Exactly 1 rule is preserved.

---

### `Tau.MetaLogic.refused_are`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L93-L94)
**theorem
Tau.MetaLogic.refused_are :refusedRules = [StructuralRule.contraction, StructuralRule.weakening]**


The refused rules are contraction and weakening.

---

### `Tau.MetaLogic.preserved_is`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L96-L97)
**theorem
Tau.MetaLogic.preserved_is :preservedRules = [StructuralRule.exchange]**


The preserved rule is exchange.

---

### `Tau.MetaLogic.count_partition`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L99-L101)
**theorem
Tau.MetaLogic.count_partition :refusedRules.length + preservedRules.length = allRules.length**


Count consistency: refused + preserved = total.

---

### `Tau.MetaLogic.diagonal_discipline_refuses_contraction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L107-L115)
**theorem
Tau.MetaLogic.diagonal_discipline_refuses_contraction :Kernel.solenoidalGenerators.length < Kernel.nonOmegaGenerators.length**


The 3 solenoidal generators correspond to 3 controlled rewiring levels.
Free contraction would require unbounded rewiring. Since K6 bounds
the universe at 4 non-omega generators, free contraction is structurally
impossible: there are fewer rewiring targets (3) than total channels (4),
so at least one channel (α) is NEVER a rewiring target and serves as
the scaffold.

---

### `Tau.MetaLogic.diagonal_discipline_refuses_weakening`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L117-L122)
**theorem
Tau.MetaLogic.diagonal_discipline_refuses_weakening
(g : Kernel.Generator)
 :g ≠ Kernel.Generator.omega → g ∈ Kernel.nonOmegaGenerators**


Every generator in `nonOmegaGenerators` is reachable by construction.
No generator can be discarded — each participates in the orbit structure.
The list is complete: every non-omega generator appears.

---

### `Tau.MetaLogic.scaffold_invariant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L124-L126)
**theorem
Tau.MetaLogic.scaffold_invariant :¬Kernel.Generator.alpha ∈ Kernel.solenoidalGenerators**


The scaffold invariant: α is not a solenoidal generator.
It is the unique channel that is never consumed by rewiring.

---

### `Tau.MetaLogic.rewiring_budget`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/Substrate.lean#L128-L133)
**theorem
Tau.MetaLogic.rewiring_budget :Kernel.solenoidalGenerators.length = Kernel.nonOmegaGenerators.length - 1**


The rewiring budget is exactly 3 = 4 - 1.
This means 3 levels of rewiring (addition, multiplication, exponentiation)
and no room for a 4th.
