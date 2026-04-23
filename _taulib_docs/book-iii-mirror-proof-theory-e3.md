---
layout: taulib-doc
title: "TauLib.BookIII.Mirror.ProofTheoryE3"
permalink: /verify/taulib/docs/book-iii-mirror-proof-theory-e3/
lane: verify
module_name: "TauLib.BookIII.Mirror.ProofTheoryE3"
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

# TauLib.BookIII.Mirror.ProofTheoryE3


Proof Theory as E3, Self-Model Functor, Four Paradox Diagnostic,
and Paradox Resolution Theorem.

## Registry Cross-References


- [III.D73] Proof Theory as E3 -- `proof_theory_e3_check`

- [III.D74] Self-Model Functor -- `self_model_check`

- [III.D75] Four Paradox Diagnostic -- `four_paradox_check`

- [III.T48] Paradox Resolution -- `paradox_resolution_check`


## Mathematical Content


**III.D73 (Proof Theory as E3):** Self-modelling applied to E2 code:
E3 = proof theory about proofs. The E3 layer template applied to E2
outputs produces valid higher-level checks. E3 objects are codes that
model their own modelling process.

**III.D74 (Self-Model Functor):** The functor E2 -> E3 that takes E2
objects (self-referential codes) and produces proofs about them (self-
modelling codes). Structurally: the self-model functor applies the E3
layer's carrier check to E2 layer outputs.

**III.D75 (Four Paradox Diagnostic):** Cantor, Russell, Goedel, Turing
as E2->E3 boundary phenomena. Each paradox type maps to a specific
forbidden move in the tau-framework:


- Cantor -> unbounded_fanout (diagonal exceeds any tower level)

- Russell -> global_equality (self-membership violates locality)

- Goedel -> succinct_circuits (self-reference needs E3, not E2)

- Turing -> exponential_quantification (halting needs infinite tower)


**III.T48 (Paradox Resolution):** All four paradoxes are RESOLVED by
the enrichment tower. They are not contradictions but boundary phenomena
between enrichment levels: each paradox arises from applying an E2
question at E0/E1 level. At E3, the self-model absorbs the paradox.

---

### `Tau.BookIII.Mirror.Paradox`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L53-L60)
**inductive
Tau.BookIII.Mirror.Paradox :Type**


[III.D75] The four classical paradoxes, each arising at a
specific boundary in the enrichment tower.

- Cantor : Paradox
- Russell : Paradox
- Goedel : Paradox
- Turing : Paradox
Instances For

---

### `Tau.BookIII.Mirror.instReprParadox`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L60-L60)
**instance
Tau.BookIII.Mirror.instReprParadox :Repr Paradox**

Equations
- Tau.BookIII.Mirror.instReprParadox = { reprPrec := Tau.BookIII.Mirror.instReprParadox.repr }

---

### `Tau.BookIII.Mirror.instReprParadox.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L60-L60)
**def
Tau.BookIII.Mirror.instReprParadox.repr :Paradox → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.instDecidableEqParadox`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L60-L60)
**instance
Tau.BookIII.Mirror.instDecidableEqParadox :DecidableEq Paradox**

Equations
- Tau.BookIII.Mirror.instDecidableEqParadox x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIII.Mirror.instBEqParadox`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L60-L60)
**instance
Tau.BookIII.Mirror.instBEqParadox :BEq Paradox**

Equations
- Tau.BookIII.Mirror.instBEqParadox = { beq := Tau.BookIII.Mirror.instBEqParadox.beq }

---

### `Tau.BookIII.Mirror.instBEqParadox.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L60-L60)
**def
Tau.BookIII.Mirror.instBEqParadox.beq :Paradox → Paradox → Bool**

Equations
- Tau.BookIII.Mirror.instBEqParadox.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIII.Mirror.Paradox.toNat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L62-L67)
**def
Tau.BookIII.Mirror.Paradox.toNat :Paradox → ℕ**


Numeric index of a paradox (stable ordering).
Equations
- Tau.BookIII.Mirror.Paradox.Cantor.toNat = 0
- Tau.BookIII.Mirror.Paradox.Russell.toNat = 1
- Tau.BookIII.Mirror.Paradox.Goedel.toNat = 2
- Tau.BookIII.Mirror.Paradox.Turing.toNat = 3
Instances For

---

### `Tau.BookIII.Mirror.Paradox.level`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L69-L75)
**def
Tau.BookIII.Mirror.Paradox.level :Paradox → Enrichment.EnrLevel**


The enrichment level at which the paradox arises.
All four are E2->E3 boundary phenomena.
Equations
- Tau.BookIII.Mirror.Paradox.Cantor.level = Tau.BookIII.Enrichment.EnrLevel.E2
- Tau.BookIII.Mirror.Paradox.Russell.level = Tau.BookIII.Enrichment.EnrLevel.E2
- Tau.BookIII.Mirror.Paradox.Goedel.level = Tau.BookIII.Enrichment.EnrLevel.E2
- Tau.BookIII.Mirror.Paradox.Turing.level = Tau.BookIII.Enrichment.EnrLevel.E2
Instances For

---

### `Tau.BookIII.Mirror.Paradox.resolution_level`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L77-L83)
**def
Tau.BookIII.Mirror.Paradox.resolution_level :Paradox → Enrichment.EnrLevel**


The enrichment level at which the paradox is resolved.
All four are resolved at E3 (self-modelling absorbs the paradox).
Equations
- Tau.BookIII.Mirror.Paradox.Cantor.resolution_level = Tau.BookIII.Enrichment.EnrLevel.E3
- Tau.BookIII.Mirror.Paradox.Russell.resolution_level = Tau.BookIII.Enrichment.EnrLevel.E3
- Tau.BookIII.Mirror.Paradox.Goedel.resolution_level = Tau.BookIII.Enrichment.EnrLevel.E3
- Tau.BookIII.Mirror.Paradox.Turing.resolution_level = Tau.BookIII.Enrichment.EnrLevel.E3
Instances For

---

### `Tau.BookIII.Mirror.Paradox.forbidden_move_idx`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L85-L93)
**def
Tau.BookIII.Mirror.Paradox.forbidden_move_idx :Paradox → ℕ**


[III.D75] Forbidden move type associated with each paradox.
Maps each classical paradox to the structural violation it encodes.
0 = unbounded_fanout, 1 = global_equality,
2 = succinct_circuits, 3 = exponential_quantification
Equations
- Tau.BookIII.Mirror.Paradox.Cantor.forbidden_move_idx = 0
- Tau.BookIII.Mirror.Paradox.Russell.forbidden_move_idx = 1
- Tau.BookIII.Mirror.Paradox.Goedel.forbidden_move_idx = 2
- Tau.BookIII.Mirror.Paradox.Turing.forbidden_move_idx = 3
Instances For

---

### `Tau.BookIII.Mirror.all_paradoxes`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L95-L97)
**def
Tau.BookIII.Mirror.all_paradoxes :List Paradox**


All four paradoxes as a list.
Equations
- Tau.BookIII.Mirror.all_paradoxes = [Tau.BookIII.Mirror.Paradox.Cantor, Tau.BookIII.Mirror.Paradox.Russell, Tau.BookIII.Mirror.Paradox.Goedel, Tau.BookIII.Mirror.Paradox.Turing]
Instances For

**Scope limitation (E3 collapse):** At finite primorial level, the E3
predicate degenerates to E0 because `reduce` is idempotent. This check
is vacuous but correctly models the mathematical structure. The E3 layer
is correctly DEFINED but finite verification is vacuous.
See audit DASHBOARD.md §E3 Collapse.

---

### `Tau.BookIII.Mirror.proof_theory_e3_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L109-L140)
**def
Tau.BookIII.Mirror.proof_theory_e3_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D73] E3 layer applied to E2 output: the E3 carrier check
applied to E2 decoded values. This verifies that the E3 layer
"wraps" E2 outputs as valid higher-level objects.

At finite level: for each x, k, the E3 carrier accepts the
E2 decoder output (decoder = reduce, a fixpoint).
Equations
- Tau.BookIII.Mirror.proof_theory_e3_check bound db = Tau.BookIII.Mirror.proof_theory_e3_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Mirror.proof_theory_e3_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L118-L139)@[irreducible]

**def
Tau.BookIII.Mirror.proof_theory_e3_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

**Scope limitation (E3 collapse):** At finite primorial level, the E3
predicate degenerates to E0 because `reduce` is idempotent. This check
is vacuous but correctly models the mathematical structure. The E3 layer
is correctly DEFINED but finite verification is vacuous.
See audit DASHBOARD.md §E3 Collapse.

---

### `Tau.BookIII.Mirror.self_model_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L152-L176)
**def
Tau.BookIII.Mirror.self_model_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D74] Self-model functor: E2 -> E3. Takes E2 objects (codes
with operational closure) and produces E3 objects (self-modelling
codes). The functor applies the E3 predicate to E2 carriers.

Verified by: if E2 carrier + predicate hold, then E3 carrier +
predicate hold on the E2 decoded value.
Equations
- Tau.BookIII.Mirror.self_model_check bound db = Tau.BookIII.Mirror.self_model_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Mirror.self_model_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L161-L175)@[irreducible]

**def
Tau.BookIII.Mirror.self_model_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.self_model_invariant_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L178-L199)
**def
Tau.BookIII.Mirror.self_model_invariant_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D74] Self-model functor preserves invariants: E2 invariant
implies E3 invariant on the functor image.
Equations
- Tau.BookIII.Mirror.self_model_invariant_check bound db = Tau.BookIII.Mirror.self_model_invariant_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Mirror.self_model_invariant_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L183-L198)@[irreducible]

**def
Tau.BookIII.Mirror.self_model_invariant_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

**Scope limitation (E3 collapse):** At finite primorial level, the E3
predicate degenerates to E0 because `reduce` is idempotent. This check
is vacuous but correctly models the mathematical structure. The E3 layer
is correctly DEFINED but finite verification is vacuous.
See audit DASHBOARD.md §E3 Collapse.

---

### `Tau.BookIII.Mirror.paradox_single_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L211-L226)
**def
Tau.BookIII.Mirror.paradox_single_check
(p : Paradox)

(bound db : Denotation.TauIdx)
 :Bool**


Check a single paradox: it arises at E2 and resolves at E3.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.four_paradox_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L228-L240)
**def
Tau.BookIII.Mirror.four_paradox_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D75] Paradox diagnostic: each paradox is a boundary phenomenon.
At E2 level, the paradoxical construction attempts a move that
requires E3 self-modelling. The diagnostic verifies:

- The paradox operation fails at E2 (forbidden move)

- The paradox resolves at E3 (self-model absorbs it)


Modelled computationally: each paradox corresponds to a specific
relationship between E2 and E3 layer checks.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.forbidden_moves_distinct`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L242-L251)
**def
Tau.BookIII.Mirror.forbidden_moves_distinct :Bool**


[III.D75] All four forbidden move indices are distinct.
Equations
- Tau.BookIII.Mirror.forbidden_moves_distinct = Tau.BookIII.Mirror.forbidden_moves_distinct.go
 (List.map Tau.BookIII.Mirror.Paradox.forbidden_move_idx Tau.BookIII.Mirror.all_paradoxes)
Instances For

---

### `Tau.BookIII.Mirror.forbidden_moves_distinct.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L248-L251)
**def
Tau.BookIII.Mirror.forbidden_moves_distinct.go
(xs : List ℕ)
 :Bool**

Equations
- Tau.BookIII.Mirror.forbidden_moves_distinct.go [] = true
- Tau.BookIII.Mirror.forbidden_moves_distinct.go (x :: rest) = ((rest.all fun (y : ℕ) => x != y) && Tau.BookIII.Mirror.forbidden_moves_distinct.go rest)
Instances For

---

### `Tau.BookIII.Mirror.paradox_resolution_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L257-L277)
**def
Tau.BookIII.Mirror.paradox_resolution_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T48] Paradox resolution: all four paradoxes are resolved by
the enrichment tower. Each paradox is a boundary phenomenon between
E2 and E3, and the E3 self-modelling absorbs the paradoxical move.

Verified computationally:

- All four paradoxes are diagnosed (arise at E2)

- All four resolve at E3 (self-model functor absorbs them)

- The E3 layer is self-consistent (invariant is idempotent)

- Forbidden moves are distinct (no two paradoxes are the same)

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.proof_theory_e3_8_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L317-L318)
**theorem
Tau.BookIII.Mirror.proof_theory_e3_8_3 :proof_theory_e3_check 8 3 = true**


---

### `Tau.BookIII.Mirror.self_model_8_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L321-L322)
**theorem
Tau.BookIII.Mirror.self_model_8_3 :self_model_check 8 3 = true**


---

### `Tau.BookIII.Mirror.self_model_inv_8_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L325-L326)
**theorem
Tau.BookIII.Mirror.self_model_inv_8_3 :self_model_invariant_check 8 3 = true**


---

### `Tau.BookIII.Mirror.four_paradox_8_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L329-L330)
**theorem
Tau.BookIII.Mirror.four_paradox_8_3 :four_paradox_check 8 3 = true**


---

### `Tau.BookIII.Mirror.forbidden_moves_distinct_thm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L333-L334)
**theorem
Tau.BookIII.Mirror.forbidden_moves_distinct_thm :forbidden_moves_distinct = true**


---

### `Tau.BookIII.Mirror.paradox_resolution_8_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L337-L338)
**theorem
Tau.BookIII.Mirror.paradox_resolution_8_3 :paradox_resolution_check 8 3 = true**


---

### `Tau.BookIII.Mirror.e3_is_proof_theory`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L344-L345)
**theorem
Tau.BookIII.Mirror.e3_is_proof_theory :Enrichment.EnrLevel.E3.toNat = 3**


[III.D73] Structural: E3 is the proof-theoretic level.

---

### `Tau.BookIII.Mirror.self_model_levels`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L347-L349)
**theorem
Tau.BookIII.Mirror.self_model_levels :Enrichment.EnrLevel.E2.lt Enrichment.EnrLevel.E3 = true**


[III.D74] Structural: self-model functor goes from E2 to E3.

---

### `Tau.BookIII.Mirror.all_paradoxes_at_e2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L351-L353)
**theorem
Tau.BookIII.Mirror.all_paradoxes_at_e2 :(all_paradoxes.all fun (p : Paradox) => p.level == Enrichment.EnrLevel.E2) = true**


[III.D75] Structural: all paradoxes arise at E2.

---

### `Tau.BookIII.Mirror.all_paradoxes_resolve_e3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L355-L357)
**theorem
Tau.BookIII.Mirror.all_paradoxes_resolve_e3 :(all_paradoxes.all fun (p : Paradox) => p.resolution_level == Enrichment.EnrLevel.E3) = true**


[III.D75] Structural: all paradoxes resolve at E3.

---

### `Tau.BookIII.Mirror.exactly_four_paradoxes`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L359-L360)
**theorem
Tau.BookIII.Mirror.exactly_four_paradoxes :all_paradoxes.length = 4**


[III.D75] Structural: exactly four paradoxes.

---

### `Tau.BookIII.Mirror.forbidden_move_range`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L362-L364)
**theorem
Tau.BookIII.Mirror.forbidden_move_range :List.map Paradox.forbidden_move_idx all_paradoxes = [0, 1, 2, 3]**


[III.D75] Structural: forbidden move indices cover 0..3.

---

### `Tau.BookIII.Mirror.paradox_move_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L366-L374)
**theorem
Tau.BookIII.Mirror.paradox_move_injective :Paradox.Cantor.forbidden_move_idx ≠ Paradox.Russell.forbidden_move_idx ∧ Paradox.Cantor.forbidden_move_idx ≠ Paradox.Goedel.forbidden_move_idx ∧ Paradox.Cantor.forbidden_move_idx ≠ Paradox.Turing.forbidden_move_idx ∧ Paradox.Russell.forbidden_move_idx ≠ Paradox.Goedel.forbidden_move_idx ∧ Paradox.Russell.forbidden_move_idx ≠ Paradox.Turing.forbidden_move_idx ∧ Paradox.Goedel.forbidden_move_idx ≠ Paradox.Turing.forbidden_move_idx**


[III.T48] Structural: each paradox maps to a unique forbidden move.

---

### `Tau.BookIII.Mirror.paradox_gap`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L376-L378)
**theorem
Tau.BookIII.Mirror.paradox_gap :Enrichment.EnrLevel.E2.toNat + 1 = Enrichment.EnrLevel.E3.toNat**


[III.T48] Structural: E2 < E3 is the paradox gap.
