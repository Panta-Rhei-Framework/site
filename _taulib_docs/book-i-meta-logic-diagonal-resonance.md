---
layout: taulib-doc
title: "TauLib.BookI.MetaLogic.DiagonalResonance"
permalink: /verify/taulib/docs/book-i-meta-logic-diagonal-resonance/
lane: verify
module_name: "TauLib.BookI.MetaLogic.DiagonalResonance"
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

# TauLib.MetaLogic.DiagonalResonance


Diagonal resonance, identity slippage, and shadow identities.

## Registry Cross-References


- [I.D89] Diagonal Resonance — `DiagonalResonance`

- [I.D90] Identity Slippage — `IdentitySlippage`

- [I.D91] Shadow Identity — `ShadowIdentity`

- [I.R24] Five Reasons Why The Bug Hides — `BugHidingReason`

- [I.R25] Orthodox Foundations Under the Lens — `OrthodoxFoundation`


## Mathematical Content


Diagonal resonance is the interaction between three individually benign components:
(L) meta-level contraction, (E) equality-as-congruence, (P) ontic self-products.
When all three are present, they produce identity slippage: the partial decoherence
of ontic self-identity. Shadow identities are the implicit identification channels
that arise from this interaction.

---

### `Tau.MetaLogic.ResonanceComponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L31-L36)
**inductive
Tau.MetaLogic.ResonanceComponent :Type**


[I.D89] The three components of diagonal resonance.

- L : ResonanceComponent
- E : ResonanceComponent
- P : ResonanceComponent
Instances For

---

### `Tau.MetaLogic.instDecidableEqResonanceComponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L36-L36)
**instance
Tau.MetaLogic.instDecidableEqResonanceComponent :DecidableEq ResonanceComponent**

Equations
- Tau.MetaLogic.instDecidableEqResonanceComponent x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.MetaLogic.instReprResonanceComponent.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L36-L36)
**def
Tau.MetaLogic.instReprResonanceComponent.repr :ResonanceComponent → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.instReprResonanceComponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L36-L36)
**instance
Tau.MetaLogic.instReprResonanceComponent :Repr ResonanceComponent**

Equations
- Tau.MetaLogic.instReprResonanceComponent = { reprPrec := Tau.MetaLogic.instReprResonanceComponent.repr }

---

### `Tau.MetaLogic.DiagonalResonance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L38-L43)
**structure
Tau.MetaLogic.DiagonalResonance :Type**


[I.D89] A foundation's diagonal resonance profile: which components are present.

- contraction_present : Bool
- equality_congruence : Bool
- self_products : Bool
Instances For

---

### `Tau.MetaLogic.instDecidableEqDiagonalResonance.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L43-L43)
**def
Tau.MetaLogic.instDecidableEqDiagonalResonance.decEq
(x✝ x✝¹ : DiagonalResonance)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.instDecidableEqDiagonalResonance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L43-L43)
**instance
Tau.MetaLogic.instDecidableEqDiagonalResonance :DecidableEq DiagonalResonance**

Equations
- Tau.MetaLogic.instDecidableEqDiagonalResonance = Tau.MetaLogic.instDecidableEqDiagonalResonance.decEq

---

### `Tau.MetaLogic.instReprDiagonalResonance.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L43-L43)
**def
Tau.MetaLogic.instReprDiagonalResonance.repr :DiagonalResonance → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.instReprDiagonalResonance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L43-L43)
**instance
Tau.MetaLogic.instReprDiagonalResonance :Repr DiagonalResonance**

Equations
- Tau.MetaLogic.instReprDiagonalResonance = { reprPrec := Tau.MetaLogic.instReprDiagonalResonance.repr }

---

### `Tau.MetaLogic.DiagonalResonance.isFullResonance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L45-L47)
**def
Tau.MetaLogic.DiagonalResonance.isFullResonance
(dr : DiagonalResonance)
 :Bool**


A foundation has full diagonal resonance when all three components are present.
Equations
- dr.isFullResonance = (dr.contraction_present && dr.equality_congruence && dr.self_products)
Instances For

---

### `Tau.MetaLogic.allResonanceComponents`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L49-L50)
**def
Tau.MetaLogic.allResonanceComponents :List ResonanceComponent**


All resonance components enumerated.
Equations
- Tau.MetaLogic.allResonanceComponents = [Tau.MetaLogic.ResonanceComponent.L, Tau.MetaLogic.ResonanceComponent.E, Tau.MetaLogic.ResonanceComponent.P]
Instances For

---

### `Tau.MetaLogic.resonance_component_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L52-L53)
**theorem
Tau.MetaLogic.resonance_component_count :allResonanceComponents.length = 3**


There are exactly 3 resonance components.

---

### `Tau.MetaLogic.tau_resonance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L59-L63)
**def
Tau.MetaLogic.tau_resonance :DiagonalResonance**


τ's diagonal resonance profile: K5 blocks (L) and (P), NF-confluence controls (E).
Equations
- Tau.MetaLogic.tau_resonance = { contraction_present := false, equality_congruence := false, self_products := false }
Instances For

---

### `Tau.MetaLogic.tau_no_full_resonance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L65-L66)
**theorem
Tau.MetaLogic.tau_no_full_resonance :tau_resonance.isFullResonance = false**


τ does NOT exhibit full diagonal resonance.

---

### `Tau.MetaLogic.IdentitySlippage`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L72-L77)
**structure
Tau.MetaLogic.IdentitySlippage :Type**


[I.D90] Identity slippage: a foundation exhibits identity slippage if
diagonal resonance prevents distinct ontic objects from being preserved
as distinct under global projection.

- resonance : DiagonalResonance
- is_full : self.resonance.isFullResonance = true
Instances For

---

### `Tau.MetaLogic.tau_no_slippage`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L80-L85)
**theorem
Tau.MetaLogic.tau_no_slippage :¬∃ (s : IdentitySlippage), s.resonance = tau_resonance**


τ cannot exhibit identity slippage because it lacks full resonance.

---

### `Tau.MetaLogic.ShadowIdentityType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L91-L96)
**inductive
Tau.MetaLogic.ShadowIdentityType :Type**


[I.D91] Shadow identity: an implicit identification channel type.

- equivalenceWitness : ShadowIdentityType
- substitutionBridge : ShadowIdentityType
- diagonalProjection : ShadowIdentityType
Instances For

---

### `Tau.MetaLogic.instDecidableEqShadowIdentityType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L96-L96)
**instance
Tau.MetaLogic.instDecidableEqShadowIdentityType :DecidableEq ShadowIdentityType**

Equations
- Tau.MetaLogic.instDecidableEqShadowIdentityType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.MetaLogic.instReprShadowIdentityType.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L96-L96)
**def
Tau.MetaLogic.instReprShadowIdentityType.repr :ShadowIdentityType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.instReprShadowIdentityType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L96-L96)
**instance
Tau.MetaLogic.instReprShadowIdentityType :Repr ShadowIdentityType**

Equations
- Tau.MetaLogic.instReprShadowIdentityType = { reprPrec := Tau.MetaLogic.instReprShadowIdentityType.repr }

---

### `Tau.MetaLogic.shadowRequires`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L98-L102)
**def
Tau.MetaLogic.shadowRequires :ShadowIdentityType → List ResonanceComponent**


A shadow identity requires the relevant resonance components.
Equations
- Tau.MetaLogic.shadowRequires Tau.MetaLogic.ShadowIdentityType.equivalenceWitness = [Tau.MetaLogic.ResonanceComponent.E]
- Tau.MetaLogic.shadowRequires Tau.MetaLogic.ShadowIdentityType.substitutionBridge = [Tau.MetaLogic.ResonanceComponent.E, Tau.MetaLogic.ResonanceComponent.L]
- Tau.MetaLogic.shadowRequires Tau.MetaLogic.ShadowIdentityType.diagonalProjection = [Tau.MetaLogic.ResonanceComponent.P]
Instances For

---

### `Tau.MetaLogic.ShadowIdentity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L104-L113)
**structure
Tau.MetaLogic.ShadowIdentity :Type**


[I.D91] Shadow identity witness: a channel that acts like identity without being
ontically constructed.

- kind : ShadowIdentityType
- resonance : DiagonalResonance
- component_present : match self.kind with
| ShadowIdentityType.equivalenceWitness => self.resonance.equality_congruence = true
| ShadowIdentityType.substitutionBridge =>
 self.resonance.equality_congruence = true ∧ self.resonance.contraction_present = true
| ShadowIdentityType.diagonalProjection => self.resonance.self_products = true
Instances For

---

### `Tau.MetaLogic.tau_no_shadow_equivalence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L115-L121)
**theorem
Tau.MetaLogic.tau_no_shadow_equivalence :¬∃ (s : ShadowIdentity), s.resonance = tau_resonance ∧ s.kind = ShadowIdentityType.equivalenceWitness**


τ admits no shadow identities of equivalenceWitness type.

---

### `Tau.MetaLogic.tau_no_shadow_substitution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L123-L129)
**theorem
Tau.MetaLogic.tau_no_shadow_substitution :¬∃ (s : ShadowIdentity), s.resonance = tau_resonance ∧ s.kind = ShadowIdentityType.substitutionBridge**


τ admits no shadow identities of substitutionBridge type.

---

### `Tau.MetaLogic.tau_no_shadow_diagonal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L131-L137)
**theorem
Tau.MetaLogic.tau_no_shadow_diagonal :¬∃ (s : ShadowIdentity), s.resonance = tau_resonance ∧ s.kind = ShadowIdentityType.diagonalProjection**


τ admits no shadow identities of diagonalProjection type.

---

### `Tau.MetaLogic.BugHidingReason`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L143-L150)
**inductive
Tau.MetaLogic.BugHidingReason :Type**


[I.R24] Five reasons why diagonal resonance is hard to detect.

- notOneBug : BugHidingReason
- slippageNotCrash : BugHidingReason
- everywhereNowhere : BugHidingReason
- hidesBehindUtility : BugHidingReason
- needsClosureDemand : BugHidingReason
Instances For

---

### `Tau.MetaLogic.instDecidableEqBugHidingReason`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L150-L150)
**instance
Tau.MetaLogic.instDecidableEqBugHidingReason :DecidableEq BugHidingReason**

Equations
- Tau.MetaLogic.instDecidableEqBugHidingReason x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.MetaLogic.instReprBugHidingReason`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L150-L150)
**instance
Tau.MetaLogic.instReprBugHidingReason :Repr BugHidingReason**

Equations
- Tau.MetaLogic.instReprBugHidingReason = { reprPrec := Tau.MetaLogic.instReprBugHidingReason.repr }

---

### `Tau.MetaLogic.instReprBugHidingReason.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L150-L150)
**def
Tau.MetaLogic.instReprBugHidingReason.repr :BugHidingReason → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.allBugHidingReasons`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L152-L154)
**def
Tau.MetaLogic.allBugHidingReasons :List BugHidingReason**


All bug hiding reasons enumerated.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.bug_hiding_reason_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L156-L157)
**theorem
Tau.MetaLogic.bug_hiding_reason_count :allBugHidingReasons.length = 5**


There are exactly 5 bug hiding reasons.

---

### `Tau.MetaLogic.OrthodoxFoundation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L163-L168)
**inductive
Tau.MetaLogic.OrthodoxFoundation :Type**


[I.R25] Three orthodox foundations examined for diagonal resonance.

- ZFC : OrthodoxFoundation
- CIC : OrthodoxFoundation
- HoTT : OrthodoxFoundation
Instances For

---

### `Tau.MetaLogic.instDecidableEqOrthodoxFoundation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L168-L168)
**instance
Tau.MetaLogic.instDecidableEqOrthodoxFoundation :DecidableEq OrthodoxFoundation**

Equations
- Tau.MetaLogic.instDecidableEqOrthodoxFoundation x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.MetaLogic.instReprOrthodoxFoundation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L168-L168)
**def
Tau.MetaLogic.instReprOrthodoxFoundation.repr :OrthodoxFoundation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.instReprOrthodoxFoundation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L168-L168)
**instance
Tau.MetaLogic.instReprOrthodoxFoundation :Repr OrthodoxFoundation**

Equations
- Tau.MetaLogic.instReprOrthodoxFoundation = { reprPrec := Tau.MetaLogic.instReprOrthodoxFoundation.repr }

---

### `Tau.MetaLogic.orthodox_resonance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L170-L174)
**def
Tau.MetaLogic.orthodox_resonance :OrthodoxFoundation → DiagonalResonance**


Each orthodox foundation's resonance profile.
Equations
- Tau.MetaLogic.orthodox_resonance Tau.MetaLogic.OrthodoxFoundation.ZFC = { contraction_present := true, equality_congruence := true, self_products := true }
- Tau.MetaLogic.orthodox_resonance Tau.MetaLogic.OrthodoxFoundation.CIC = { contraction_present := true, equality_congruence := true, self_products := true }
- Tau.MetaLogic.orthodox_resonance Tau.MetaLogic.OrthodoxFoundation.HoTT = { contraction_present := true, equality_congruence := true, self_products := true }
Instances For

---

### `Tau.MetaLogic.orthodox_full_resonance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L176-L179)
**theorem
Tau.MetaLogic.orthodox_full_resonance
(f : OrthodoxFoundation)
 :(orthodox_resonance f).isFullResonance = true**


All orthodox foundations exhibit full diagonal resonance.

---

### `Tau.MetaLogic.allOrthodoxFoundations`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L181-L182)
**def
Tau.MetaLogic.allOrthodoxFoundations :List OrthodoxFoundation**


All orthodox foundations enumerated.
Equations
- Tau.MetaLogic.allOrthodoxFoundations = [Tau.MetaLogic.OrthodoxFoundation.ZFC, Tau.MetaLogic.OrthodoxFoundation.CIC, Tau.MetaLogic.OrthodoxFoundation.HoTT]
Instances For

---

### `Tau.MetaLogic.orthodox_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L184-L185)
**theorem
Tau.MetaLogic.orthodox_count :allOrthodoxFoundations.length = 3**


There are exactly 3 orthodox foundations.
