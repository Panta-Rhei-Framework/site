---
layout: taulib-doc
title: "TauLib.BookI.MetaLogic.ReceptionCriterion"
permalink: /verify/taulib/docs/book-i-meta-logic-reception-criterion/
lane: verify
module_name: "TauLib.BookI.MetaLogic.ReceptionCriterion"
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

# TauLib.MetaLogic.ReceptionCriterion


The Identity-Faithful Reception Criterion and Structural Instability Theorem.

## Registry Cross-References


- [I.D92] Identity-Faithful Reception — `IdentityFaithfulReception`

- [I.D93] Structural Instability — `StructuralInstability`

- [I.T48] Structural Instability Theorem — `structural_instability_theorem`

- [I.R26] Implications for Absolute Meaning — `AbsoluteMeaningImplication`

- [I.R27] Honest Scope Declaration — `ScopeDeclaration`


## Mathematical Content


A VM system can receive τ ontically only if it supports identity-faithful reception.
Diagonal-resonant foundations cannot do this: the L+E+P interaction creates identity
slack that prevents any global projection from preserving distinctness.

---

### `Tau.MetaLogic.ReceptionCondition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L29-L35)
**inductive
Tau.MetaLogic.ReceptionCondition :Type**


[I.D92] The three conditions for identity-faithful reception.
An interpretation functor P : C_τ → C_S must satisfy all three.

- preservesDistinctness : ReceptionCondition
- preservesIdentity : ReceptionCondition
- reflectsIsomorphism : ReceptionCondition
Instances For

---

### `Tau.MetaLogic.instDecidableEqReceptionCondition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L35-L35)
**instance
Tau.MetaLogic.instDecidableEqReceptionCondition :DecidableEq ReceptionCondition**

Equations
- Tau.MetaLogic.instDecidableEqReceptionCondition x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.MetaLogic.instReprReceptionCondition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L35-L35)
**def
Tau.MetaLogic.instReprReceptionCondition.repr :ReceptionCondition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.instReprReceptionCondition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L35-L35)
**instance
Tau.MetaLogic.instReprReceptionCondition :Repr ReceptionCondition**

Equations
- Tau.MetaLogic.instReprReceptionCondition = { reprPrec := Tau.MetaLogic.instReprReceptionCondition.repr }

---

### `Tau.MetaLogic.IdentityFaithfulReception`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L37-L45)
**structure
Tau.MetaLogic.IdentityFaithfulReception :Type**


[I.D92] Identity-faithful reception: a foundation can receive τ only if
its resonance profile allows preserving ontic identity.

- host_resonance : DiagonalResonance
The host foundation's resonance profile

- all_conditions_met : Bool
All three reception conditions must be satisfiable

- resonance_blocks : self.host_resonance.isFullResonance = true → self.all_conditions_met = false
If host has full resonance, conditions CANNOT be met

Instances For

---

### `Tau.MetaLogic.allReceptionConditions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L47-L49)
**def
Tau.MetaLogic.allReceptionConditions :List ReceptionCondition**


All reception conditions enumerated.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.reception_condition_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L51-L52)
**theorem
Tau.MetaLogic.reception_condition_count :allReceptionConditions.length = 3**


There are exactly 3 reception conditions.

---

### `Tau.MetaLogic.StructuralInstability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L58-L68)
**structure
Tau.MetaLogic.StructuralInstability :Type**


[I.D93] Structural instability: a foundation exhibits structural instability
when diagonal resonance prevents canonical, identity-faithful intended semantics.

- resonance : DiagonalResonance
The foundation's resonance profile

- full_resonance : self.resonance.isFullResonance = true
Full resonance is present

- no_unique_closure : Bool
Cannot stabilize unique ontic closure

- vm_relative : Bool
Cannot fix ontology without VM-relativity

Instances For

---

### `Tau.MetaLogic.InstabilitySymptom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L70-L77)
**inductive
Tau.MetaLogic.InstabilitySymptom :Type**


The known symptoms of structural instability.

- nonCategoricity : InstabilitySymptom
- independenceResults : InstabilitySymptom
- multiversePhenomenon : InstabilitySymptom
- potentialism : InstabilitySymptom
- infinityZoo : InstabilitySymptom
Instances For

---

### `Tau.MetaLogic.instDecidableEqInstabilitySymptom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L77-L77)
**instance
Tau.MetaLogic.instDecidableEqInstabilitySymptom :DecidableEq InstabilitySymptom**

Equations
- Tau.MetaLogic.instDecidableEqInstabilitySymptom x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.MetaLogic.instReprInstabilitySymptom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L77-L77)
**instance
Tau.MetaLogic.instReprInstabilitySymptom :Repr InstabilitySymptom**

Equations
- Tau.MetaLogic.instReprInstabilitySymptom = { reprPrec := Tau.MetaLogic.instReprInstabilitySymptom.repr }

---

### `Tau.MetaLogic.instReprInstabilitySymptom.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L77-L77)
**def
Tau.MetaLogic.instReprInstabilitySymptom.repr :InstabilitySymptom → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.allInstabilitySymptoms`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L79-L81)
**def
Tau.MetaLogic.allInstabilitySymptoms :List InstabilitySymptom**


All instability symptoms enumerated.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.instability_symptom_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L83-L84)
**theorem
Tau.MetaLogic.instability_symptom_count :allInstabilitySymptoms.length = 5**


There are exactly 5 instability symptoms.

---

### `Tau.MetaLogic.orthodox_instability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L86-L89)
**def
Tau.MetaLogic.orthodox_instability
(f : OrthodoxFoundation)
 :StructuralInstability**


Each orthodox foundation exhibits structural instability.
Equations
- Tau.MetaLogic.orthodox_instability f = { resonance := Tau.MetaLogic.orthodox_resonance f, full_resonance := ⋯ }
Instances For

---

### `Tau.MetaLogic.tau_no_instability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L91-L97)
**theorem
Tau.MetaLogic.tau_no_instability :¬∃ (si : StructuralInstability), si.resonance = tau_resonance**


τ does NOT exhibit structural instability (no full resonance).

---

### `Tau.MetaLogic.structural_instability_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L103-L115)
**theorem
Tau.MetaLogic.structural_instability_theorem
(dr : DiagonalResonance)

(h : dr.isFullResonance = true)
 :¬∃ (r : IdentityFaithfulReception), r.host_resonance = dr ∧ r.all_conditions_met = true**


[I.T48] The Structural Instability Theorem: diagonal-resonant foundations
cannot host identity-faithful reception of τ.

If host has full resonance, reception conditions cannot be met.

---

### `Tau.MetaLogic.tau_self_reception`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L117-L123)
**def
Tau.MetaLogic.tau_self_reception :IdentityFaithfulReception**


τ CAN receive itself (trivial identity functor).
Equations
- Tau.MetaLogic.tau_self_reception = { host_resonance := Tau.MetaLogic.tau_resonance, all_conditions_met := true,
 resonance_blocks := Tau.MetaLogic.tau_self_reception._proof_1 }
Instances For

---

### `Tau.MetaLogic.orthodox_no_reception`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L125-L129)
**theorem
Tau.MetaLogic.orthodox_no_reception
(f : OrthodoxFoundation)
 :¬∃ (r : IdentityFaithfulReception), r.host_resonance = orthodox_resonance f ∧ r.all_conditions_met = true**


No orthodox foundation can faithfully receive τ.

---

### `Tau.MetaLogic.AbsoluteMeaningImplication`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L135-L142)
**structure
Tau.MetaLogic.AbsoluteMeaningImplication :Type**


[I.R26] The relationship between identity coherence and absolute meaning.

- coherence_required : Bool
Identity coherence is a prerequisite for absolute meaning

- omega_required : Bool
Unique omega is a prerequisite for absolute meaning

- both_required : self.coherence_required = true ∧ self.omega_required = true
Both are true

Instances For

---

### `Tau.MetaLogic.tau_absolute_meaning`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L144-L148)
**def
Tau.MetaLogic.tau_absolute_meaning :AbsoluteMeaningImplication**


τ satisfies both prerequisites.
Equations
- Tau.MetaLogic.tau_absolute_meaning = { coherence_required := true, omega_required := true, both_required := Tau.MetaLogic.tau_absolute_meaning._proof_1 }
Instances For

---

### `Tau.MetaLogic.ScopeDeclaration`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L154-L160)
**inductive
Tau.MetaLogic.ScopeDeclaration :Type**


[I.R27] What the structural instability diagnosis does NOT claim.

- notInconsistency : ScopeDeclaration
- structuralDiagnosis : ScopeDeclaration
- tradeoffExists : ScopeDeclaration
- bothDirections : ScopeDeclaration
Instances For

---

### `Tau.MetaLogic.instDecidableEqScopeDeclaration`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L160-L160)
**instance
Tau.MetaLogic.instDecidableEqScopeDeclaration :DecidableEq ScopeDeclaration**

Equations
- Tau.MetaLogic.instDecidableEqScopeDeclaration x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.MetaLogic.instReprScopeDeclaration`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L160-L160)
**instance
Tau.MetaLogic.instReprScopeDeclaration :Repr ScopeDeclaration**

Equations
- Tau.MetaLogic.instReprScopeDeclaration = { reprPrec := Tau.MetaLogic.instReprScopeDeclaration.repr }

---

### `Tau.MetaLogic.instReprScopeDeclaration.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L160-L160)
**def
Tau.MetaLogic.instReprScopeDeclaration.repr :ScopeDeclaration → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.allScopeDeclarations`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L162-L164)
**def
Tau.MetaLogic.allScopeDeclarations :List ScopeDeclaration**


All scope declarations enumerated.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.scope_declaration_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L166-L167)
**theorem
Tau.MetaLogic.scope_declaration_count :allScopeDeclarations.length = 4**


There are exactly 4 scope declarations.

---

### `Tau.MetaLogic.TradeoffCost`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L169-L174)
**inductive
Tau.MetaLogic.TradeoffCost :Type**


[I.R27] What τ must earn in later books because of the trade-off.

- epsilonDelta : TradeoffCost
- localSmoothness : TradeoffCost
- classicalLaplacian : TradeoffCost
Instances For

---

### `Tau.MetaLogic.instDecidableEqTradeoffCost`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L174-L174)
**instance
Tau.MetaLogic.instDecidableEqTradeoffCost :DecidableEq TradeoffCost**

Equations
- Tau.MetaLogic.instDecidableEqTradeoffCost x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.MetaLogic.instReprTradeoffCost`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L174-L174)
**instance
Tau.MetaLogic.instReprTradeoffCost :Repr TradeoffCost**

Equations
- Tau.MetaLogic.instReprTradeoffCost = { reprPrec := Tau.MetaLogic.instReprTradeoffCost.repr }

---

### `Tau.MetaLogic.instReprTradeoffCost.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L174-L174)
**def
Tau.MetaLogic.instReprTradeoffCost.repr :TradeoffCost → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.allTradeoffCosts`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L176-L178)
**def
Tau.MetaLogic.allTradeoffCosts :List TradeoffCost**


All trade-off costs enumerated.
Equations
- Tau.MetaLogic.allTradeoffCosts = [Tau.MetaLogic.TradeoffCost.epsilonDelta, Tau.MetaLogic.TradeoffCost.localSmoothness, Tau.MetaLogic.TradeoffCost.classicalLaplacian]
Instances For

---

### `Tau.MetaLogic.tradeoff_cost_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L180-L181)
**theorem
Tau.MetaLogic.tradeoff_cost_count :allTradeoffCosts.length = 3**


There are exactly 3 trade-off costs.

---

### `Tau.MetaLogic.tradeoff_resolution_book`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L183-L187)
**def
Tau.MetaLogic.tradeoff_resolution_book :TradeoffCost → ℕ**


The book in which each trade-off cost is resolved.
Equations
- Tau.MetaLogic.tradeoff_resolution_book Tau.MetaLogic.TradeoffCost.epsilonDelta = 2
- Tau.MetaLogic.tradeoff_resolution_book Tau.MetaLogic.TradeoffCost.localSmoothness = 2
- Tau.MetaLogic.tradeoff_resolution_book Tau.MetaLogic.TradeoffCost.classicalLaplacian = 3
Instances For

---

### `Tau.MetaLogic.tradeoff_resolved_by_book_three`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L189-L192)
**theorem
Tau.MetaLogic.tradeoff_resolved_by_book_three
(c : TradeoffCost)
 :tradeoff_resolution_book c ≤ 3**


All trade-off costs are resolved no later than Book III.
