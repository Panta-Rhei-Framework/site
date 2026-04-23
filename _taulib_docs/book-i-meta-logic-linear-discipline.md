---
layout: taulib-doc
title: "TauLib.BookI.MetaLogic.LinearDiscipline"
permalink: /verify/taulib/docs/book-i-meta-logic-linear-discipline/
lane: verify
module_name: "TauLib.BookI.MetaLogic.LinearDiscipline"
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

# TauLib.MetaLogic.LinearDiscipline


The Diagonal-Linear Correspondence: K5's diagonal discipline maps onto
the !-free fragment of Girard's linear logic.

## Registry Cross-References


- [I.D78] Diagonal-Linear Correspondence — `DiagonalLinearCorrespondence`

- [I.D79] Program Monoid as Linear Calculus — `ProgramLinearCalc`

- [I.T37] Diagonal-Linear Correspondence Theorem — `diagonal_linear_correspondence`


## Mathematical Content


Three aspects of the correspondence:

- K5.1 (no unearned diagonals) <-> no free contraction

- K5.2 (channel consumption) <-> linear resource tracking

- K5.3 (saturation) <-> finite resource budget
Plus: NF-Confluence <-> cut-elimination, Truth4 <-> resource states


---

### `Tau.MetaLogic.LinearAspect`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L35-L40)
**inductive
Tau.MetaLogic.LinearAspect :Type**


The three aspects of linear logic that correspond to K5's discipline.

- noFreeContraction : LinearAspect
- resourceTracking : LinearAspect
- finiteResourceBudget : LinearAspect
Instances For

---

### `Tau.MetaLogic.instDecidableEqLinearAspect`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L40-L40)
**instance
Tau.MetaLogic.instDecidableEqLinearAspect :DecidableEq LinearAspect**

Equations
- Tau.MetaLogic.instDecidableEqLinearAspect x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.MetaLogic.instReprLinearAspect`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L40-L40)
**instance
Tau.MetaLogic.instReprLinearAspect :Repr LinearAspect**

Equations
- Tau.MetaLogic.instReprLinearAspect = { reprPrec := Tau.MetaLogic.instReprLinearAspect.repr }

---

### `Tau.MetaLogic.instReprLinearAspect.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L40-L40)
**def
Tau.MetaLogic.instReprLinearAspect.repr :LinearAspect → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.DiagonalAspect`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L42-L47)
**inductive
Tau.MetaLogic.DiagonalAspect :Type**


The three aspects of K5's diagonal discipline.

- noUnearnedDiagonals : DiagonalAspect
- channelConsumption : DiagonalAspect
- saturation : DiagonalAspect
Instances For

---

### `Tau.MetaLogic.instDecidableEqDiagonalAspect`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L47-L47)
**instance
Tau.MetaLogic.instDecidableEqDiagonalAspect :DecidableEq DiagonalAspect**

Equations
- Tau.MetaLogic.instDecidableEqDiagonalAspect x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.MetaLogic.instReprDiagonalAspect.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L47-L47)
**def
Tau.MetaLogic.instReprDiagonalAspect.repr :DiagonalAspect → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.instReprDiagonalAspect`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L47-L47)
**instance
Tau.MetaLogic.instReprDiagonalAspect :Repr DiagonalAspect**

Equations
- Tau.MetaLogic.instReprDiagonalAspect = { reprPrec := Tau.MetaLogic.instReprDiagonalAspect.repr }

---

### `Tau.MetaLogic.diag_to_linear`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L55-L59)
**def
Tau.MetaLogic.diag_to_linear :DiagonalAspect → LinearAspect**


The diagonal-to-linear map: each K5 aspect corresponds to a linear aspect.
Equations
- Tau.MetaLogic.diag_to_linear Tau.MetaLogic.DiagonalAspect.noUnearnedDiagonals = Tau.MetaLogic.LinearAspect.noFreeContraction
- Tau.MetaLogic.diag_to_linear Tau.MetaLogic.DiagonalAspect.channelConsumption = Tau.MetaLogic.LinearAspect.resourceTracking
- Tau.MetaLogic.diag_to_linear Tau.MetaLogic.DiagonalAspect.saturation = Tau.MetaLogic.LinearAspect.finiteResourceBudget
Instances For

---

### `Tau.MetaLogic.linear_to_diag`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L61-L65)
**def
Tau.MetaLogic.linear_to_diag :LinearAspect → DiagonalAspect**


The inverse map: each linear aspect corresponds to a K5 aspect.
Equations
- Tau.MetaLogic.linear_to_diag Tau.MetaLogic.LinearAspect.noFreeContraction = Tau.MetaLogic.DiagonalAspect.noUnearnedDiagonals
- Tau.MetaLogic.linear_to_diag Tau.MetaLogic.LinearAspect.resourceTracking = Tau.MetaLogic.DiagonalAspect.channelConsumption
- Tau.MetaLogic.linear_to_diag Tau.MetaLogic.LinearAspect.finiteResourceBudget = Tau.MetaLogic.DiagonalAspect.saturation
Instances For

---

### `Tau.MetaLogic.diag_linear_roundtrip`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L67-L70)
**theorem
Tau.MetaLogic.diag_linear_roundtrip
(d : DiagonalAspect)
 :linear_to_diag (diag_to_linear d) = d**


Round-trip: diagonal -> linear -> diagonal is the identity.

---

### `Tau.MetaLogic.linear_diag_roundtrip`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L72-L75)
**theorem
Tau.MetaLogic.linear_diag_roundtrip
(l : LinearAspect)
 :diag_to_linear (linear_to_diag l) = l**


Round-trip: linear -> diagonal -> linear is the identity.

---

### `Tau.MetaLogic.diag_to_linear_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L77-L80)
**theorem
Tau.MetaLogic.diag_to_linear_injective
(d1 d2 : DiagonalAspect)

(h : diag_to_linear d1 = diag_to_linear d2)
 :d1 = d2**


The bijection is injective in the forward direction.

---

### `Tau.MetaLogic.linear_to_diag_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L82-L85)
**theorem
Tau.MetaLogic.linear_to_diag_injective
(l1 l2 : LinearAspect)

(h : linear_to_diag l1 = linear_to_diag l2)
 :l1 = l2**


The bijection is injective in the inverse direction.

---

### `Tau.MetaLogic.allDiagonalAspects`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L87-L89)
**def
Tau.MetaLogic.allDiagonalAspects :List DiagonalAspect**


All diagonal aspects enumerated.
Equations
- Tau.MetaLogic.allDiagonalAspects = [Tau.MetaLogic.DiagonalAspect.noUnearnedDiagonals, Tau.MetaLogic.DiagonalAspect.channelConsumption, Tau.MetaLogic.DiagonalAspect.saturation]
Instances For

---

### `Tau.MetaLogic.allLinearAspects`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L91-L93)
**def
Tau.MetaLogic.allLinearAspects :List LinearAspect**


All linear aspects enumerated.
Equations
- Tau.MetaLogic.allLinearAspects = [Tau.MetaLogic.LinearAspect.noFreeContraction, Tau.MetaLogic.LinearAspect.resourceTracking, Tau.MetaLogic.LinearAspect.finiteResourceBudget]
Instances For

---

### `Tau.MetaLogic.diagonal_aspect_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L95-L96)
**theorem
Tau.MetaLogic.diagonal_aspect_count :allDiagonalAspects.length = 3**


There are exactly 3 diagonal aspects.

---

### `Tau.MetaLogic.linear_aspect_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L98-L99)
**theorem
Tau.MetaLogic.linear_aspect_count :allLinearAspects.length = 3**


There are exactly 3 linear aspects.

---

### `Tau.MetaLogic.isRhoPure`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L105-L113)
**def
Tau.MetaLogic.isRhoPure :Denotation.Program → Bool**


A program is in normal form (cut-free) when it has no redundant
sigma instructions. The simplest characterization: a program is
"rho-pure" when it contains only rho instructions.
In general, cut-freedom corresponds to NF-confluence: the
rho count is invariant under rewriting.
Equations
- Tau.MetaLogic.isRhoPure [] = true
- Tau.MetaLogic.isRhoPure (Tau.Denotation.Instruction.rho_inst :: rest) = Tau.MetaLogic.isRhoPure rest
- Tau.MetaLogic.isRhoPure (Tau.Denotation.Instruction.sigma_inst a a_1 :: tail) = false
Instances For

---

### `Tau.MetaLogic.empty_is_rho_pure`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L115-L116)
**theorem
Tau.MetaLogic.empty_is_rho_pure :isRhoPure [] = true**


The empty program is rho-pure (the identity proof).

---

### `Tau.MetaLogic.rho_pure_compose`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L118-L133)
**theorem
Tau.MetaLogic.rho_pure_compose
(p q : Denotation.Program)

(hp : isRhoPure p = true)

(hq : isRhoPure q = true)
 :isRhoPure (p.compose q) = true**


Concatenation of rho-pure programs is rho-pure.
This is the linear analogue: cut on two cut-free proofs
gives a cut-free proof (in the rho-only fragment).

---

### `Tau.MetaLogic.cut_elimination_additive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L135-L141)
**theorem
Tau.MetaLogic.cut_elimination_additive
(p q : Denotation.Program)
 :Denotation.countRho (p.compose q) = Denotation.countRho p + Denotation.countRho q**


NF-confluence as a linear property: the rho count (resource consumption)
is additive under composition (cut). This is the computational content
of cut-elimination.

---

### `Tau.MetaLogic.identity_zero_resource`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L143-L146)
**theorem
Tau.MetaLogic.identity_zero_resource :Denotation.countRho [] = 0**


The identity program consumes zero resources.

---

### `Tau.MetaLogic.ResourceState`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L152-L162)
**inductive
Tau.MetaLogic.ResourceState :Type**


The four resource states corresponding to Truth4 values.


- present: the resource is available (both sectors confirm)

- absent: the resource is consumed (both sectors deny)

- overdetermined: the resource is claimed by conflicting sources

- underdetermined: the resource status is unknown


- present : ResourceState
- absent : ResourceState
- overdetermined : ResourceState
- underdetermined : ResourceState
Instances For

---

### `Tau.MetaLogic.instDecidableEqResourceState`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L162-L162)
**instance
Tau.MetaLogic.instDecidableEqResourceState :DecidableEq ResourceState**

Equations
- Tau.MetaLogic.instDecidableEqResourceState x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.MetaLogic.instReprResourceState`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L162-L162)
**instance
Tau.MetaLogic.instReprResourceState :Repr ResourceState**

Equations
- Tau.MetaLogic.instReprResourceState = { reprPrec := Tau.MetaLogic.instReprResourceState.repr }

---

### `Tau.MetaLogic.instReprResourceState.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L162-L162)
**def
Tau.MetaLogic.instReprResourceState.repr :ResourceState → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.truth4_to_resource`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L166-L171)
**def
Tau.MetaLogic.truth4_to_resource :Logic.Truth4 → ResourceState**


Map Truth4 values to resource states.
Equations
- Tau.MetaLogic.truth4_to_resource Tau.Logic.Truth4.T = Tau.MetaLogic.ResourceState.present
- Tau.MetaLogic.truth4_to_resource Tau.Logic.Truth4.F = Tau.MetaLogic.ResourceState.absent
- Tau.MetaLogic.truth4_to_resource Tau.Logic.Truth4.B = Tau.MetaLogic.ResourceState.overdetermined
- Tau.MetaLogic.truth4_to_resource Tau.Logic.Truth4.N = Tau.MetaLogic.ResourceState.underdetermined
Instances For

---

### `Tau.MetaLogic.resource_to_truth4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L173-L178)
**def
Tau.MetaLogic.resource_to_truth4 :ResourceState → Logic.Truth4**


Map resource states back to Truth4 values.
Equations
- Tau.MetaLogic.resource_to_truth4 Tau.MetaLogic.ResourceState.present = Tau.Logic.Truth4.T
- Tau.MetaLogic.resource_to_truth4 Tau.MetaLogic.ResourceState.absent = Tau.Logic.Truth4.F
- Tau.MetaLogic.resource_to_truth4 Tau.MetaLogic.ResourceState.overdetermined = Tau.Logic.Truth4.B
- Tau.MetaLogic.resource_to_truth4 Tau.MetaLogic.ResourceState.underdetermined = Tau.Logic.Truth4.N
Instances For

---

### `Tau.MetaLogic.truth4_resource_roundtrip`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L180-L183)
**theorem
Tau.MetaLogic.truth4_resource_roundtrip
(v : Logic.Truth4)
 :resource_to_truth4 (truth4_to_resource v) = v**


Round-trip: truth4 -> resource -> truth4 is the identity.

---

### `Tau.MetaLogic.resource_truth4_roundtrip`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L185-L188)
**theorem
Tau.MetaLogic.resource_truth4_roundtrip
(r : ResourceState)
 :truth4_to_resource (resource_to_truth4 r) = r**


Round-trip: resource -> truth4 -> resource is the identity.

---

### `Tau.MetaLogic.truth4_to_resource_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L190-L193)
**theorem
Tau.MetaLogic.truth4_to_resource_injective
(a b : Logic.Truth4)

(h : truth4_to_resource a = truth4_to_resource b)
 :a = b**


Injectivity of truth4_to_resource.

---

### `Tau.MetaLogic.resource_to_truth4_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L195-L198)
**theorem
Tau.MetaLogic.resource_to_truth4_injective
(a b : ResourceState)

(h : resource_to_truth4 a = resource_to_truth4 b)
 :a = b**


Injectivity of resource_to_truth4.

---

### `Tau.MetaLogic.overdetermined_is_contraction_artifact`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L204-L208)
**theorem
Tau.MetaLogic.overdetermined_is_contraction_artifact :truth4_to_resource Logic.Truth4.B = ResourceState.overdetermined**


B (overdetermined) is the contraction artifact: a resource claimed
both present and absent — this arises when a resource is used twice
(contracted) from conflicting sources.

---

### `Tau.MetaLogic.underdetermined_is_weakening_artifact`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L210-L214)
**theorem
Tau.MetaLogic.underdetermined_is_weakening_artifact :truth4_to_resource Logic.Truth4.N = ResourceState.underdetermined**


N (underdetermined) is the weakening artifact: a resource whose
status is unknown — this arises when a resource is discarded
(weakened away) before its status is determined.

---

### `Tau.MetaLogic.present_is_T`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L216-L218)
**theorem
Tau.MetaLogic.present_is_T :truth4_to_resource Logic.Truth4.T = ResourceState.present**


The present state maps to T.

---

### `Tau.MetaLogic.absent_is_F`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L220-L222)
**theorem
Tau.MetaLogic.absent_is_F :truth4_to_resource Logic.Truth4.F = ResourceState.absent**


The absent state maps to F.

---

### `Tau.MetaLogic.allResourceStates`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L224-L226)
**def
Tau.MetaLogic.allResourceStates :List ResourceState**


All resource states enumerated.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.resource_state_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L228-L229)
**theorem
Tau.MetaLogic.resource_state_count :allResourceStates.length = 4**


There are exactly 4 resource states.

---

### `Tau.MetaLogic.contraction_produces_overdetermined`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L235-L241)
**theorem
Tau.MetaLogic.contraction_produces_overdetermined :k5_status StructuralRule.contraction = ObjectLevelStatus.refused ∧ truth4_to_resource Logic.Truth4.B = ResourceState.overdetermined**


Contraction produces overdetermined states. The refused rule
(.contraction) corresponds to the pathological resource state
(.overdetermined = B).

---

### `Tau.MetaLogic.weakening_produces_underdetermined`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L243-L249)
**theorem
Tau.MetaLogic.weakening_produces_underdetermined :k5_status StructuralRule.weakening = ObjectLevelStatus.refused ∧ truth4_to_resource Logic.Truth4.N = ResourceState.underdetermined**


Weakening produces underdetermined states. The refused rule
(.weakening) corresponds to the pathological resource state
(.underdetermined = N).

---

### `Tau.MetaLogic.DiagonalLinearCorrespondence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L255-L280)
**structure
Tau.MetaLogic.DiagonalLinearCorrespondence :Prop**


[I.T37] The Diagonal-Linear Correspondence Theorem.

The correspondence has three components:

- Aspect bijection: 3 diagonal aspects ↔ 3 linear aspects

- Resource interpretation: 4 Truth4 values ↔ 4 resource states

- Structural classification: 2 refused + 1 preserved = 3 rules


Together, these establish that K5's diagonal discipline IS the
!-free fragment of linear logic, restricted to τ's finite universe.

- aspect_count : allDiagonalAspects.length = 3
The aspect bijection has 3 components

- resource_count : allResourceStates.length = 4
The resource interpretation has 4 states matching Truth4

- aspect_roundtrip_diag
(d : DiagonalAspect)
 : linear_to_diag (diag_to_linear d) = d
The aspect bijection is a genuine bijection (round-trip)

- aspect_roundtrip_linear
(l : LinearAspect)
 : diag_to_linear (linear_to_diag l) = l
The aspect bijection is a genuine bijection (round-trip)

- resource_roundtrip_t4
(v : Logic.Truth4)
 : resource_to_truth4 (truth4_to_resource v) = v
The resource interpretation is a genuine bijection (round-trip)

- resource_roundtrip_rs
(r : ResourceState)
 : truth4_to_resource (resource_to_truth4 r) = r
The resource interpretation is a genuine bijection (round-trip)

- rules_refused : refusedRules.length = 2
Structural rules: exactly 2 refused

- rules_preserved : preservedRules.length = 1
Structural rules: exactly 1 preserved

Instances For

---

### `Tau.MetaLogic.diagonal_linear_correspondence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L282-L291)
**theorem
Tau.MetaLogic.diagonal_linear_correspondence :DiagonalLinearCorrespondence**


The correspondence theorem: all components are satisfied.
