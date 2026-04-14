---
layout: taulib-doc
title: "TauLib.BookIII.Mirror.E3Witness"
permalink: /verify/taulib/docs/book-iii-mirror-e3witness/
lane: verify
module_name: "TauLib.BookIII.Mirror.E3Witness"
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

# TauLib.BookIII.Mirror.E3Witness


Constructive E₃ self-model witnesses: fixed-point semantics,
paradox absorption, and saturation meaning.

## Registry Cross-References


- [III.D85] Self-Referential Fixed Point — `self_ref_fixed_point`, `fixed_point_check`

- [III.D86] Paradox Absorption Map — `paradox_absorbed_check`

- [III.T58] E₃ Self-Model Completeness — `e3_self_model_complete_check`

- [III.P35] Saturation Semantics — `saturation_semantic_check`


## Mathematical Content


**III.D85 (Self-Referential Fixed Point):** At stage k, a self-referential
fixed point is c* ∈ Z/M_k Z such that the triple-reduce path
reduce(reduce(reduce(c*, k), k), k) = reduce(c*, k) AND the squaring
path reduce(c*², k) = (reduce(c*, k))². This is the E₃ predicate
applied constructively.

**III.D86 (Paradox Absorption Map):** Each of the four classical paradoxes
(Cantor, Russell, Gödel, Turing) corresponds to a forbidden move that
breaks at the E₂→E₃ boundary. The absorption map shows that at E₃,
the self-model functor maps each paradoxical construction to a well-defined
τ-object (the fixed point absorbs the self-reference).

**III.T58 (E₃ Self-Model Completeness):** The self-model at E₃ is
complete: every E₂ code has an E₃ interpretation (the functor E₂→E₃
is essentially surjective on computational content). At finite stages,
this means every reduce-stable element has a triple-reduce path.

**III.P35 (Saturation Semantics):** E₃.succ = E₃ is not merely
definitional — it has semantic content. The witness: applying the
enrichment functor F_E once more to E₃ produces no new structure.
Concretely, the self-model of the self-model is isomorphic to the
self-model (idempotence of self-awareness).

---

### `Tau.BookIII.Mirror.e3_predicate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L55-L68)
**def
Tau.BookIII.Mirror.e3_predicate
(x k : ℕ)
 :Bool**


[III.D85] E₃ predicate at stage k: triple-reduce stability and
squaring compatibility.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.count_e3_fixed_points`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L70-L80)
**def
Tau.BookIII.Mirror.count_e3_fixed_points
(k : ℕ)
 :ℕ**


[III.D85] Count self-referential fixed points at stage k.
Equations
- Tau.BookIII.Mirror.count_e3_fixed_points k = Tau.BookIII.Mirror.count_e3_fixed_points.go 0 (Tau.Polarity.primorial k) 0 k
Instances For

---

### `Tau.BookIII.Mirror.count_e3_fixed_points.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L75-L79)@[irreducible]

**def
Tau.BookIII.Mirror.count_e3_fixed_points.go
(x bound acc k : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.fixed_point_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L82-L91)
**def
Tau.BookIII.Mirror.fixed_point_check
(db : ℕ)
 :Bool**


[III.D85] Fixed point check: E₃ fixed points exist at every stage.
Equations
- Tau.BookIII.Mirror.fixed_point_check db = Tau.BookIII.Mirror.fixed_point_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Mirror.fixed_point_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L86-L90)@[irreducible]

**def
Tau.BookIII.Mirror.fixed_point_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.e3_density_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L93-L99)
**def
Tau.BookIII.Mirror.e3_density_check
(k : ℕ)
 :Bool**


[III.D85] Fixed point density: ratio of E₃ elements to total.
Equations
- Tau.BookIII.Mirror.e3_density_check k = (Tau.BookIII.Mirror.count_e3_fixed_points k == Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookIII.Mirror.ParadoxWitness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L105-L111)
**inductive
Tau.BookIII.Mirror.ParadoxWitness :Type**


[III.D86] Paradox type (mirrors ProofTheoryE3).

- cantor : ParadoxWitness
- russell : ParadoxWitness
- goedel : ParadoxWitness
- turing : ParadoxWitness
Instances For

---

### `Tau.BookIII.Mirror.instReprParadoxWitness.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L111-L111)
**def
Tau.BookIII.Mirror.instReprParadoxWitness.repr :ParadoxWitness → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.instReprParadoxWitness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L111-L111)
**instance
Tau.BookIII.Mirror.instReprParadoxWitness :Repr ParadoxWitness**

Equations
- Tau.BookIII.Mirror.instReprParadoxWitness = { reprPrec := Tau.BookIII.Mirror.instReprParadoxWitness.repr }

---

### `Tau.BookIII.Mirror.instDecidableEqParadoxWitness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L111-L111)
**instance
Tau.BookIII.Mirror.instDecidableEqParadoxWitness :DecidableEq ParadoxWitness**

Equations
- Tau.BookIII.Mirror.instDecidableEqParadoxWitness x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIII.Mirror.instBEqParadoxWitness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L111-L111)
**instance
Tau.BookIII.Mirror.instBEqParadoxWitness :BEq ParadoxWitness**

Equations
- Tau.BookIII.Mirror.instBEqParadoxWitness = { beq := Tau.BookIII.Mirror.instBEqParadoxWitness.beq }

---

### `Tau.BookIII.Mirror.instBEqParadoxWitness.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L111-L111)
**def
Tau.BookIII.Mirror.instBEqParadoxWitness.beq :ParadoxWitness → ParadoxWitness → Bool**

Equations
- Tau.BookIII.Mirror.instBEqParadoxWitness.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIII.Mirror.paradox_construction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L113-L122)
**def
Tau.BookIII.Mirror.paradox_construction
(p : ParadoxWitness)

(x k : ℕ)
 :ℕ**


[III.D86] Paradox construction at stage k: each paradox constructs
a "problematic" element via a specific operation.
Equations
- One or more equations did not get rendered due to their size.
- Tau.BookIII.Mirror.paradox_construction Tau.BookIII.Mirror.ParadoxWitness.cantor x k = if (Tau.Polarity.primorial k == 0) = true then 0 else (x + 1) % Tau.Polarity.primorial k
- Tau.BookIII.Mirror.paradox_construction Tau.BookIII.Mirror.ParadoxWitness.goedel x k = if (Tau.Polarity.primorial k == 0) = true then 0 else 2 * x % Tau.Polarity.primorial k
- Tau.BookIII.Mirror.paradox_construction Tau.BookIII.Mirror.ParadoxWitness.turing x k = if (Tau.Polarity.primorial k == 0) = true then 0 else (x * x + 1) % Tau.Polarity.primorial k
Instances For

---

### `Tau.BookIII.Mirror.paradox_absorbed_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L124-L146)
**def
Tau.BookIII.Mirror.paradox_absorbed_check
(db : ℕ)
 :Bool**


[III.D86] Paradox absorption: the result of each paradox construction
is STILL a valid E₃ element (the self-model absorbs self-reference).
Equations
- Tau.BookIII.Mirror.paradox_absorbed_check db = Tau.BookIII.Mirror.paradox_absorbed_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Mirror.paradox_absorbed_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L129-L134)@[irreducible]

**def
Tau.BookIII.Mirror.paradox_absorbed_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.paradox_absorbed_check.go_p`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L136-L145)@[irreducible]

**def
Tau.BookIII.Mirror.paradox_absorbed_check.go_p
(x pk k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.e3_self_model_complete_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L152-L173)
**def
Tau.BookIII.Mirror.e3_self_model_complete_check
(db : ℕ)
 :Bool**


[III.T58] Self-model completeness: every reduce-stable element
has the E₃ property (functor E₂→E₃ is surjective on content).
Equations
- Tau.BookIII.Mirror.e3_self_model_complete_check db = Tau.BookIII.Mirror.e3_self_model_complete_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Mirror.e3_self_model_complete_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L157-L162)@[irreducible]

**def
Tau.BookIII.Mirror.e3_self_model_complete_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.e3_self_model_complete_check.go_x`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L164-L172)@[irreducible]

**def
Tau.BookIII.Mirror.e3_self_model_complete_check.go_x
(x pk k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.saturation_semantic_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L179-L205)
**def
Tau.BookIII.Mirror.saturation_semantic_check
(db : ℕ)
 :Bool**


[III.P35] Saturation semantic check: applying the enrichment functor
once more to E₃ produces the same structure.
F_E(E₃) = E₃ witnessed by: the E₃ predicate applied to E₃ outputs
gives the same set as the E₃ predicate itself.
Equations
- Tau.BookIII.Mirror.saturation_semantic_check db = Tau.BookIII.Mirror.saturation_semantic_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Mirror.saturation_semantic_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L186-L191)@[irreducible]

**def
Tau.BookIII.Mirror.saturation_semantic_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.saturation_semantic_check.go_x`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L193-L204)@[irreducible]

**def
Tau.BookIII.Mirror.saturation_semantic_check.go_x
(x pk k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.self_model_idempotent_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L207-L227)
**def
Tau.BookIII.Mirror.self_model_idempotent_check
(db : ℕ)
 :Bool**


[III.P35] Semantic invariant: the self-model of the self-model
is isomorphic to the self-model.
Equations
- Tau.BookIII.Mirror.self_model_idempotent_check db = Tau.BookIII.Mirror.self_model_idempotent_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Mirror.self_model_idempotent_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L212-L217)@[irreducible]

**def
Tau.BookIII.Mirror.self_model_idempotent_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.self_model_idempotent_check.go_x`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L219-L226)@[irreducible]

**def
Tau.BookIII.Mirror.self_model_idempotent_check.go_x
(x pk k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.fixed_point_check_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L233-L235)
**theorem
Tau.BookIII.Mirror.fixed_point_check_3 :fixed_point_check 3 = true**


[III.D85] E₃ fixed points exist at stages 1-3.

---

### `Tau.BookIII.Mirror.e3_density_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L237-L239)
**theorem
Tau.BookIII.Mirror.e3_density_2 :e3_density_check 2 = true**


[III.D85] All elements are E₃ at stage 2.

---

### `Tau.BookIII.Mirror.paradox_absorbed_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L241-L243)
**theorem
Tau.BookIII.Mirror.paradox_absorbed_3 :paradox_absorbed_check 3 = true**


[III.D86] Paradoxes absorbed at stages 1-3.

---

### `Tau.BookIII.Mirror.self_model_complete_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L245-L247)
**theorem
Tau.BookIII.Mirror.self_model_complete_3 :e3_self_model_complete_check 3 = true**


[III.T58] Self-model completeness at stages 1-3.

---

### `Tau.BookIII.Mirror.saturation_semantic_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L249-L251)
**theorem
Tau.BookIII.Mirror.saturation_semantic_3 :saturation_semantic_check 3 = true**


[III.P35] Saturation semantics at stages 1-3.

---

### `Tau.BookIII.Mirror.self_model_idempotent_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/E3Witness.lean#L253-L255)
**theorem
Tau.BookIII.Mirror.self_model_idempotent_3 :self_model_idempotent_check 3 = true**


[III.P35] Self-model idempotent at stages 1-3.
