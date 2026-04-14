---
layout: taulib-doc
title: "TauLib.BookVI.LifeCore.SelfDesc"
permalink: /verify/taulib/docs/book-vi-life-core-self-desc/
lane: verify
module_name: "TauLib.BookVI.LifeCore.SelfDesc"
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

# TauLib.BookVI.LifeCore.SelfDesc


SelfDesc: the second of two Life predicates. An internal evaluator
Eval_X satisfying completeness, internality, and refinement coherence.

## Registry Cross-References


- [VI.D08] SelfDesc Predicate — `SelfDescPredicate`

- [VI.D09] Internal Evaluator — `InternalEvaluator`

- [VI.P02] Code Reconstruction — `code_reconstruction`

- [VI.T03] SelfDesc Closure Theorem — `selfdesc_closure_theorem`

- [VI.P04] Seven Hallmarks Complete — `seven_hallmarks_complete`


## Ground Truth Sources


- Book VI Chapter 5 (2nd Edition): SelfDesc


---

### `Tau.BookVI.SelfDesc.SelfDescPredicate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L23-L31)
**structure
Tau.BookVI.SelfDesc.SelfDescPredicate :Type**


[VI.D08] SelfDesc predicate: internal evaluator Eval_X satisfying
completeness, internality, refinement coherence.

- condition_count : ℕ
- count_eq : self.condition_count = 3
- completeness : Bool
- internality : Bool
- refinement_coherence : Bool
Instances For

---

### `Tau.BookVI.SelfDesc.instReprSelfDescPredicate.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L31-L31)
**def
Tau.BookVI.SelfDesc.instReprSelfDescPredicate.repr :SelfDescPredicate → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.SelfDesc.instReprSelfDescPredicate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L31-L31)
**instance
Tau.BookVI.SelfDesc.instReprSelfDescPredicate :Repr SelfDescPredicate**

Equations
- Tau.BookVI.SelfDesc.instReprSelfDescPredicate = { reprPrec := Tau.BookVI.SelfDesc.instReprSelfDescPredicate.repr }

---

### `Tau.BookVI.SelfDesc.canonical_selfdesc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L33-L35)
**def
Tau.BookVI.SelfDesc.canonical_selfdesc :SelfDescPredicate**

Equations
- Tau.BookVI.SelfDesc.canonical_selfdesc = { condition_count := 3, count_eq := Tau.BookVI.SelfDesc.canonical_selfdesc._proof_1 }
Instances For

---

### `Tau.BookVI.SelfDesc.InternalEvaluator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L37-L42)
**structure
Tau.BookVI.SelfDesc.InternalEvaluator :Type**


[VI.D09] Internal evaluator: morphism in End(X), no oracle needed.

- is_endomorphism : Bool
- domain_in_carrier : Bool
- no_oracle : Bool
Instances For

---

### `Tau.BookVI.SelfDesc.instReprInternalEvaluator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L42-L42)
**instance
Tau.BookVI.SelfDesc.instReprInternalEvaluator :Repr InternalEvaluator**

Equations
- Tau.BookVI.SelfDesc.instReprInternalEvaluator = { reprPrec := Tau.BookVI.SelfDesc.instReprInternalEvaluator.repr }

---

### `Tau.BookVI.SelfDesc.instReprInternalEvaluator.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L42-L42)
**def
Tau.BookVI.SelfDesc.instReprInternalEvaluator.repr :InternalEvaluator → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.SelfDesc.internal_eval`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L44-L44)
**def
Tau.BookVI.SelfDesc.internal_eval :InternalEvaluator**

Equations
- Tau.BookVI.SelfDesc.internal_eval = { }
Instances For

---

### `Tau.BookVI.SelfDesc.code_reconstruction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L46-L48)
**theorem
Tau.BookVI.SelfDesc.code_reconstruction :internal_eval.no_oracle = true**


[VI.P02] Code reconstruction: ω-germ code encodes distinction.

---

### `Tau.BookVI.SelfDesc.SelfDescClosure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L50-L55)
**structure
Tau.BookVI.SelfDesc.SelfDescClosure :Type**


[VI.T03] SelfDesc Closure: SelfDesc pair is self-maintaining.

- basin_correction : Bool
- code_integrity : Bool
- closure_under_eval : Bool
Instances For

---

### `Tau.BookVI.SelfDesc.instReprSelfDescClosure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L55-L55)
**instance
Tau.BookVI.SelfDesc.instReprSelfDescClosure :Repr SelfDescClosure**

Equations
- Tau.BookVI.SelfDesc.instReprSelfDescClosure = { reprPrec := Tau.BookVI.SelfDesc.instReprSelfDescClosure.repr }

---

### `Tau.BookVI.SelfDesc.instReprSelfDescClosure.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L55-L55)
**def
Tau.BookVI.SelfDesc.instReprSelfDescClosure.repr :SelfDescClosure → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.SelfDesc.closure_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L57-L57)
**def
Tau.BookVI.SelfDesc.closure_thm :SelfDescClosure**

Equations
- Tau.BookVI.SelfDesc.closure_thm = { }
Instances For

---

### `Tau.BookVI.SelfDesc.selfdesc_closure_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L59-L63)
**theorem
Tau.BookVI.SelfDesc.selfdesc_closure_theorem :closure_thm.basin_correction = true ∧ closure_thm.code_integrity = true ∧ closure_thm.closure_under_eval = true**


---

### `Tau.BookVI.SelfDesc.SevenHallmarksComplete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L65-L72)
**structure
Tau.BookVI.SelfDesc.SevenHallmarksComplete :Type**


[VI.P04] Seven hallmarks complete: bijection H → F, |H| = |F| = 7.

- hallmark_count : ℕ
- count_eq : self.hallmark_count = 7
- formal_count : ℕ
- formal_eq : self.formal_count = 7
- is_bijection : Bool
Instances For

---

### `Tau.BookVI.SelfDesc.instReprSevenHallmarksComplete.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L72-L72)
**def
Tau.BookVI.SelfDesc.instReprSevenHallmarksComplete.repr :SevenHallmarksComplete → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.SelfDesc.instReprSevenHallmarksComplete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L72-L72)
**instance
Tau.BookVI.SelfDesc.instReprSevenHallmarksComplete :Repr SevenHallmarksComplete**

Equations
- Tau.BookVI.SelfDesc.instReprSevenHallmarksComplete = { reprPrec := Tau.BookVI.SelfDesc.instReprSevenHallmarksComplete.repr }

---

### `Tau.BookVI.SelfDesc.seven_hallmarks`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L74-L78)
**def
Tau.BookVI.SelfDesc.seven_hallmarks :SevenHallmarksComplete**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.SelfDesc.seven_hallmarks_complete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L80-L84)
**theorem
Tau.BookVI.SelfDesc.seven_hallmarks_complete :seven_hallmarks.hallmark_count = 7 ∧ seven_hallmarks.formal_count = 7 ∧ seven_hallmarks.is_bijection = true**


---

### `Tau.BookVI.SelfDesc.life_requires_both`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/LifeCore/SelfDesc.lean#L86-L90)
**theorem
Tau.BookVI.SelfDesc.life_requires_both :canonical_selfdesc.condition_count = 3 ∧ Distinction.canonical_distinction.condition_count = 5**


Life = Distinction AND SelfDesc.
