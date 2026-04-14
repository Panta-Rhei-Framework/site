---
layout: taulib-doc
title: "TauLib.BookIII.Enrichment.Functor"
permalink: /verify/taulib/docs/book-iii-enrichment-functor/
lane: verify
module_name: "TauLib.BookIII.Enrichment.Functor"
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

# TauLib.BookIII.Enrichment.Functor


The enrichment functor F_E and the ladder checker.

## Registry Cross-References


- [III.D04] Enrichment Functor -- `enrichment_functor_check`, `enrichment_functor_faithful`

- [III.D10] Ladder Checker -- `ladder_checker`


## Mathematical Content


**III.D04 (Enrichment Functor):** F_E takes a category and produces its
self-enrichment over H_τ. E₀ = Cat_τ, E_{k+1} = F_E(E_k). Each application
creates a new layer with strictly richer structure. The iteration terminates
at E₃ because the functor category [E₃^op, E₃] collapses back to E₃.

The functor is faithful: the layer template (Carrier, Predicate, Decoder,
Invariant) is preserved at each step, but the content enriches.

**III.D10 (Ladder Checker):** A Lean-grade proof harness that verifies:


- existence_checker(k): non-emptiness at level k

- stability_checker(k): template preservation under enrichment

- strictness_checker(k): E_k \ E_{k-1} ≠ ∅

- saturation_checker(k_max): [E_{k_max}^op, E_{k_max}] ⊆ E_{k_max}


---

### `Tau.BookIII.Enrichment.enrichment_functor_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/Functor.lean#L39-L67)
**def
Tau.BookIII.Enrichment.enrichment_functor_check
(k : EnrLevel)

(bound db : Denotation.TauIdx)
 :Bool**


[III.D04] Enrichment functor F_E: enriches from level k to level k+1.
At the computable level, this checks that the layer template at level k+1
is a valid enrichment of the template at level k:

- k+1 carrier contains k carrier (inclusion)

- k+1 decoder can access k data (projection)

- k invariant flows into k+1 carrier (template flow)


The functor is computable at finite cutoffs (bound, db).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Enrichment.enrichment_functor_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/Functor.lean#L52-L66)@[irreducible]

**def
Tau.BookIII.Enrichment.enrichment_functor_check.go
(bound db : Denotation.TauIdx)

(src tgt : LayerTemplate)

(x k_stage fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Enrichment.enrichment_functor_faithful`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/Functor.lean#L69-L88)
**def
Tau.BookIII.Enrichment.enrichment_functor_faithful
(k : EnrLevel)

(bound db : Denotation.TauIdx)
 :Bool**


[III.D04] Enrichment functor is faithful: the template structure is
preserved. Specifically, if the source predicate holds, then the
target predicate also holds (predicate monotonicity).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Enrichment.enrichment_functor_faithful.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/Functor.lean#L77-L87)@[irreducible]

**def
Tau.BookIII.Enrichment.enrichment_functor_faithful.go
(bound db : Denotation.TauIdx)

(src tgt : LayerTemplate)

(x k_stage fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Enrichment.full_enrichment_functor_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/Functor.lean#L90-L98)
**def
Tau.BookIII.Enrichment.full_enrichment_functor_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D04] Full enrichment functor verification: check at all three
transition steps E₀→E₁, E₁→E₂, E₂→E₃.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Enrichment.existence_checker`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/Functor.lean#L104-L120)
**def
Tau.BookIII.Enrichment.existence_checker
(k : EnrLevel)

(bound db : Denotation.TauIdx)
 :Bool**


[III.D10] Existence checker: verify that level k has at least one
valid carrier element. Constructive witness required.
Equations
- Tau.BookIII.Enrichment.existence_checker k bound db = Tau.BookIII.Enrichment.existence_checker.go bound db (Tau.BookIII.Enrichment.layer_of k bound db) 0 1
 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Enrichment.existence_checker.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/Functor.lean#L111-L119)@[irreducible]

**def
Tau.BookIII.Enrichment.existence_checker.go
(bound db : Denotation.TauIdx)

(lt : LayerTemplate)

(x k_stage fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Enrichment.stability_checker`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/Functor.lean#L122-L125)
**def
Tau.BookIII.Enrichment.stability_checker
(k : EnrLevel)

(bound db : Denotation.TauIdx)
 :Bool**


[III.D10] Stability checker: verify that the layer template at level k
is structurally valid.
Equations
- Tau.BookIII.Enrichment.stability_checker k bound db = Tau.BookIII.Enrichment.layer_valid_at k bound db
Instances For

---

### `Tau.BookIII.Enrichment.strictness_checker`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/Functor.lean#L127-L162)
**def
Tau.BookIII.Enrichment.strictness_checker
(k : EnrLevel)

(bound db : Denotation.TauIdx)
 :Bool**


[III.D10] Strictness checker: verify that E_k has elements not in E_{k-1}.
For E₀, this is trivially true (no E_{-1}). For E₁+, we need a witness
that is in E_k's carrier but not in E_{k-1}'s carrier, or that satisfies
E_k's predicate but not E_{k-1}'s predicate.
Equations
- One or more equations did not get rendered due to their size.
- Tau.BookIII.Enrichment.strictness_checker Tau.BookIII.Enrichment.EnrLevel.E0 bound db = true
Instances For

**Scope limitation (E3 collapse):** At finite primorial level, the E3
predicate degenerates to E0 because `reduce` is idempotent. This check
is vacuous but correctly models the mathematical structure. The E3 layer
is correctly DEFINED but finite verification is vacuous.
See audit DASHBOARD.md §E3 Collapse.

---

### `Tau.BookIII.Enrichment.saturation_checker`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/Functor.lean#L170-L194)
**def
Tau.BookIII.Enrichment.saturation_checker
(bound db : Denotation.TauIdx)
 :Bool**


[III.D10] Saturation checker: verify that [E_{k_max}^op, E_{k_max}] ⊆ E_{k_max}.
At E₃, applying the enrichment functor again gives back E₃.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Enrichment.saturation_checker.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/Functor.lean#L184-L193)@[irreducible]

**def
Tau.BookIII.Enrichment.saturation_checker.go
(bound db : Denotation.TauIdx)

(l1 l2 : LayerTemplate)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Enrichment.ladder_checker`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/Functor.lean#L196-L210)
**def
Tau.BookIII.Enrichment.ladder_checker
(bound db : Denotation.TauIdx)
 :Bool**


[III.D10] Full ladder checker: all four properties.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Enrichment.enr_functor_e0_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/Functor.lean#L258-L259)
**theorem
Tau.BookIII.Enrichment.enr_functor_e0_8_3 :enrichment_functor_check EnrLevel.E0 8 3 = true**


---

### `Tau.BookIII.Enrichment.enr_functor_e1_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/Functor.lean#L262-L263)
**theorem
Tau.BookIII.Enrichment.enr_functor_e1_8_3 :enrichment_functor_check EnrLevel.E1 8 3 = true**


---

### `Tau.BookIII.Enrichment.enr_functor_e2_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/Functor.lean#L266-L267)
**theorem
Tau.BookIII.Enrichment.enr_functor_e2_8_3 :enrichment_functor_check EnrLevel.E2 8 3 = true**


---

### `Tau.BookIII.Enrichment.full_enr_functor_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/Functor.lean#L270-L271)
**theorem
Tau.BookIII.Enrichment.full_enr_functor_8_3 :full_enrichment_functor_check 8 3 = true**


---

### `Tau.BookIII.Enrichment.ladder_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/Functor.lean#L274-L275)
**theorem
Tau.BookIII.Enrichment.ladder_8_3 :ladder_checker 8 3 = true**


---

### `Tau.BookIII.Enrichment.succ_idempotent_e3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/Functor.lean#L281-L283)
**theorem
Tau.BookIII.Enrichment.succ_idempotent_e3 :EnrLevel.E3.succ.succ = EnrLevel.E3.succ**


[III.D04] Structural proof: EnrLevel.succ is idempotent at E₃.
This is the functor-level expression of saturation.

---

### `Tau.BookIII.Enrichment.three_steps_to_e3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Enrichment/Functor.lean#L285-L289)
**theorem
Tau.BookIII.Enrichment.three_steps_to_e3
(k : EnrLevel)
 :k.succ.succ.succ = EnrLevel.E3**


[III.D04] Enrichment functor terminates: after at most 3 applications,
we reach E₃ regardless of starting level.
