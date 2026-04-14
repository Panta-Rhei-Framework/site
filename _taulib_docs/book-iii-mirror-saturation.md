---
layout: taulib-doc
title: "TauLib.BookIII.Mirror.Saturation"
permalink: /verify/taulib/docs/book-iii-mirror-saturation/
lane: verify
module_name: "TauLib.BookIII.Mirror.Saturation"
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

# TauLib.BookIII.Mirror.Saturation


Applied Saturation, Terminal Level Characterization, and Tower Closure.

## Registry Cross-References


- [III.T49] Applied Saturation -- `applied_saturation_check`

- [III.P31] Terminal Level Characterization -- `terminal_level_check`


## Mathematical Content


**III.T49 (Applied Saturation):** E3 is terminal in the enrichment tower:
self-modelling applied twice is idempotent. At finite level: the E3 layer
applied to E3 output equals E3 output. This is the "applied" version of
the categorical saturation theorem (III.T03): whereas III.T03 proves
E3.succ = E3 by definition, III.T49 proves it computationally by showing
the E3 layer template is a fixpoint under self-application.

**III.P31 (Terminal Level Characterization):** Self-modelling is idempotent:
E3 applied to E3 data is E3 data. At finite level: E3.toNat is the maximum
level (3), and EnrLevel.lt .E3 .E3 = false. Combined with III.T49, this
gives the complete characterization: E3 is the unique terminal object in
the enrichment tower.

**Scope limitation (E3 collapse):** At finite primorial level, the E3
predicate degenerates to E0 because `reduce` is idempotent. This check
is vacuous but correctly models the mathematical structure. The E3 layer
is correctly DEFINED but finite verification is vacuous.
See audit DASHBOARD.md §E3 Collapse.

---

### `Tau.BookIII.Mirror.applied_saturation_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L46-L81)
**def
Tau.BookIII.Mirror.applied_saturation_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T49] Applied saturation: the E3 layer template is a fixpoint
under self-application. For each x, k:


- E3 decoder applied to E3 decoder output equals E3 decoder output

- E3 carrier applied to E3 decoder output remains true

- E3 invariant applied to E3 decoder output remains true


This is the computational witness of E4 = E3.
Equations
- Tau.BookIII.Mirror.applied_saturation_check bound db = Tau.BookIII.Mirror.applied_saturation_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Mirror.applied_saturation_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L56-L80)@[irreducible]

**def
Tau.BookIII.Mirror.applied_saturation_check.go
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

### `Tau.BookIII.Mirror.full_saturation_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L89-L114)
**def
Tau.BookIII.Mirror.full_saturation_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T49] Saturation at all four components: carrier, predicate,
decoder, and invariant are all fixpoints at E3.
Equations
- Tau.BookIII.Mirror.full_saturation_check bound db = Tau.BookIII.Mirror.full_saturation_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Mirror.full_saturation_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L94-L113)@[irreducible]

**def
Tau.BookIII.Mirror.full_saturation_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.terminal_level_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L120-L141)
**def
Tau.BookIII.Mirror.terminal_level_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.P31] Terminal level check: E3 is the maximum enrichment level.
Verified by:

- E3.toNat = 3 (maximum index)

- EnrLevel.lt .E3 .E3 = false (not self-exceeding)

- E3.succ = E3 (successor saturates)

- The four levels [E0, E1, E2, E3] are exhaustive

- Applied saturation holds (E3 template is fixpoint)

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.tower_complete_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L147-L169)
**def
Tau.BookIII.Mirror.tower_complete_check :Bool**


Tower completeness: the full enrichment tower E0 < E1 < E2 < E3
is a total order on exactly 4 elements.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.reachability_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L171-L176)
**def
Tau.BookIII.Mirror.reachability_check :Bool**


Each enrichment level is reachable from E0 by iterated succ.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.mirror_master_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L178-L197)
**def
Tau.BookIII.Mirror.mirror_master_check
(bound db : Denotation.TauIdx)
 :Bool**


Master mirror check: combines all Sprint 10 verifications.
Proof theory (E3), self-model functor, paradox resolution,
applied saturation, and terminal level characterization.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Mirror.applied_saturation_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L228-L229)
**theorem
Tau.BookIII.Mirror.applied_saturation_8_3 :applied_saturation_check 8 3 = true**


---

### `Tau.BookIII.Mirror.full_saturation_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L232-L233)
**theorem
Tau.BookIII.Mirror.full_saturation_8_3 :full_saturation_check 8 3 = true**


---

### `Tau.BookIII.Mirror.terminal_level_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L236-L237)
**theorem
Tau.BookIII.Mirror.terminal_level_8_3 :terminal_level_check 8 3 = true**


---

### `Tau.BookIII.Mirror.tower_complete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L240-L241)
**theorem
Tau.BookIII.Mirror.tower_complete :tower_complete_check = true**


---

### `Tau.BookIII.Mirror.reachability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L244-L245)
**theorem
Tau.BookIII.Mirror.reachability :reachability_check = true**


---

### `Tau.BookIII.Mirror.mirror_master_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L248-L249)
**theorem
Tau.BookIII.Mirror.mirror_master_8_3 :mirror_master_check 8 3 = true**


---

### `Tau.BookIII.Mirror.e3_is_terminal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L255-L256)
**theorem
Tau.BookIII.Mirror.e3_is_terminal :Enrichment.EnrLevel.E3.lt Enrichment.EnrLevel.E3 = false**


[III.T49] E3 is terminal: E3 does not exceed itself.

---

### `Tau.BookIII.Mirror.e3_is_max`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L258-L259)
**theorem
Tau.BookIII.Mirror.e3_is_max :Enrichment.EnrLevel.E3.toNat = 3**


[III.P31] E3 is the maximum level.

---

### `Tau.BookIII.Mirror.four_levels`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L261-L263)
**theorem
Tau.BookIII.Mirror.four_levels :[Enrichment.EnrLevel.E0, Enrichment.EnrLevel.E1, Enrichment.EnrLevel.E2, Enrichment.EnrLevel.E3].length = 4**


Tower has exactly four levels.

---

### `Tau.BookIII.Mirror.tower_complete_order`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L265-L270)
**theorem
Tau.BookIII.Mirror.tower_complete_order :Enrichment.EnrLevel.E0.lt Enrichment.EnrLevel.E1 = true ∧ Enrichment.EnrLevel.E1.lt Enrichment.EnrLevel.E2 = true ∧ Enrichment.EnrLevel.E2.lt Enrichment.EnrLevel.E3 = true**


Tower ordering: E0 < E1 < E2 < E3 is a strict chain.

---

### `Tau.BookIII.Mirror.tower_irreflexive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L272-L278)
**theorem
Tau.BookIII.Mirror.tower_irreflexive :Enrichment.EnrLevel.E0.lt Enrichment.EnrLevel.E0 = false ∧ Enrichment.EnrLevel.E1.lt Enrichment.EnrLevel.E1 = false ∧ Enrichment.EnrLevel.E2.lt Enrichment.EnrLevel.E2 = false ∧ Enrichment.EnrLevel.E3.lt Enrichment.EnrLevel.E3 = false**


Tower irreflexivity: no level exceeds itself.

---

### `Tau.BookIII.Mirror.e3_succ_saturates`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L280-L281)
**theorem
Tau.BookIII.Mirror.e3_succ_saturates :Enrichment.EnrLevel.E3.succ = Enrichment.EnrLevel.E3**


E3.succ = E3: successor saturates at E3.

---

### `Tau.BookIII.Mirror.all_reachable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L283-L288)
**theorem
Tau.BookIII.Mirror.all_reachable :Enrichment.EnrLevel.E0.succ = Enrichment.EnrLevel.E1 ∧ Enrichment.EnrLevel.E0.succ.succ = Enrichment.EnrLevel.E2 ∧ Enrichment.EnrLevel.E0.succ.succ.succ = Enrichment.EnrLevel.E3**


All levels reachable from E0 by iterated succ.

---

### `Tau.BookIII.Mirror.e3_succ_nat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L290-L291)
**theorem
Tau.BookIII.Mirror.e3_succ_nat :Enrichment.EnrLevel.E3.succ.toNat = Enrichment.EnrLevel.E3.toNat**


[III.T49] Structural: E3.succ.toNat = E3.toNat (numeric saturation).

---

### `Tau.BookIII.Mirror.e3_unique_fixpoint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L293-L300)
**theorem
Tau.BookIII.Mirror.e3_unique_fixpoint :Enrichment.EnrLevel.E0.succ ≠ Enrichment.EnrLevel.E0 ∧ Enrichment.EnrLevel.E1.succ ≠ Enrichment.EnrLevel.E1 ∧ Enrichment.EnrLevel.E2.succ ≠ Enrichment.EnrLevel.E2 ∧ Enrichment.EnrLevel.E3.succ = Enrichment.EnrLevel.E3**


[III.P31] Structural: E3 is the unique fixpoint of succ.
(E0, E1, E2 all advance; only E3 is fixed.)

---

### `Tau.BookIII.Mirror.strictly_increasing_nat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Mirror/Saturation.lean#L302-L308)
**theorem
Tau.BookIII.Mirror.strictly_increasing_nat :Enrichment.EnrLevel.E0.toNat < Enrichment.EnrLevel.E1.toNat ∧ Enrichment.EnrLevel.E1.toNat < Enrichment.EnrLevel.E2.toNat ∧ Enrichment.EnrLevel.E2.toNat < Enrichment.EnrLevel.E3.toNat**


[III.P31] Structural: the enrichment levels have strictly
increasing toNat values (witnesses total order).
