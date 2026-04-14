---
layout: taulib-doc
title: "TauLib.BookIII.Bridge.TranslationObstruction"
permalink: /verify/taulib/docs/book-iii-bridge-translation-obstruction/
lane: verify
module_name: "TauLib.BookIII.Bridge.TranslationObstruction"
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

# TauLib.BookIII.Bridge.TranslationObstruction


Translation obstruction theory: where arithmetic and topological
translations fail, characterized by forbidden moves.

## Registry Cross-References


- [III.D91] Obstruction Cocycle — `obstruction_value`, `obstruction_check`

- [III.D92] Forbidden Move Obstruction Classes — `move_obstructs_arith`, `move_obstructs_topo`

- [III.T61] Translation Failure Boundary — `translation_failure_boundary_check`

- [III.P38] P vs NP as Polynomial Translation Obstruction — `pvsnp_obstruction_check`


## Mathematical Content


**III.D91 (Obstruction Cocycle):** For each forbidden move fm, the
obstruction value measures how much the translation deviates from
faithfulness. For mild moves (damage 1), the deviation is bounded.
For breaking moves (damage 3), the deviation grows with primorial depth.

**III.D92 (Forbidden Move Obstruction Classes):** Each of the 5 forbidden
moves obstructs either the arithmetic or topological translation in a
specific way:


- unbounded_fanout: blocks arithmetic (CRT decomposition unbounded)

- global_equality: blocks topological (NF not unique globally)

- succinct_circuits: blocks both (P vs NP)

- exponential_quantification: blocks both (requires E₃)

- nonlocal_disguise: blocks topological (multiple representations)


**III.T61 (Translation Failure Boundary):** The translations Arith_tr and
Topo_tr are faithful EXACTLY on the complement of the 5 forbidden moves.
The failure boundary is sharp: the translation works perfectly within
the safe region and degenerates precisely at forbidden operations.

**III.P38 (P vs NP Obstruction):** P vs NP is the statement that
polynomial-time translation of NP-complete problems is impossible.
In τ-terms: the succinct_circuits forbidden move has damage 3 (bridge
breaks), meaning P_adm = NP_adm in τ (internal equivalence) but this
cannot be translated to ZFC as P = NP or P ≠ NP (independence).

---

### `Tau.BookIII.Bridge.TranslationObstruction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L58-L65)
**inductive
Tau.BookIII.Bridge.TranslationObstruction :Type**


Forbidden move type (mirrors ForbiddenMoves.lean).

- unbounded_fanout : TranslationObstruction
- global_equality : TranslationObstruction
- succinct_circuits : TranslationObstruction
- exponential_quantification : TranslationObstruction
- nonlocal_disguise : TranslationObstruction
Instances For

---

### `Tau.BookIII.Bridge.instReprTranslationObstruction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L65-L65)
**def
Tau.BookIII.Bridge.instReprTranslationObstruction.repr :TranslationObstruction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.instReprTranslationObstruction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L65-L65)
**instance
Tau.BookIII.Bridge.instReprTranslationObstruction :Repr TranslationObstruction**

Equations
- Tau.BookIII.Bridge.instReprTranslationObstruction = { reprPrec := Tau.BookIII.Bridge.instReprTranslationObstruction.repr }

---

### `Tau.BookIII.Bridge.instDecidableEqTranslationObstruction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L65-L65)
**instance
Tau.BookIII.Bridge.instDecidableEqTranslationObstruction :DecidableEq TranslationObstruction**

Equations
- Tau.BookIII.Bridge.instDecidableEqTranslationObstruction x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIII.Bridge.instBEqTranslationObstruction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L65-L65)
**instance
Tau.BookIII.Bridge.instBEqTranslationObstruction :BEq TranslationObstruction**

Equations
- Tau.BookIII.Bridge.instBEqTranslationObstruction = { beq := Tau.BookIII.Bridge.instBEqTranslationObstruction.beq }

---

### `Tau.BookIII.Bridge.instBEqTranslationObstruction.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L65-L65)
**def
Tau.BookIII.Bridge.instBEqTranslationObstruction.beq :TranslationObstruction → TranslationObstruction → Bool**

Equations
- Tau.BookIII.Bridge.instBEqTranslationObstruction.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIII.Bridge.obstruction_damage`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L67-L74)
**def
Tau.BookIII.Bridge.obstruction_damage
(obs : TranslationObstruction)
 :ℕ**


Bridge damage level for each obstruction.
Equations
- Tau.BookIII.Bridge.obstruction_damage Tau.BookIII.Bridge.TranslationObstruction.unbounded_fanout = 2
- Tau.BookIII.Bridge.obstruction_damage Tau.BookIII.Bridge.TranslationObstruction.global_equality = 1
- Tau.BookIII.Bridge.obstruction_damage Tau.BookIII.Bridge.TranslationObstruction.succinct_circuits = 3
- Tau.BookIII.Bridge.obstruction_damage Tau.BookIII.Bridge.TranslationObstruction.exponential_quantification = 3
- Tau.BookIII.Bridge.obstruction_damage Tau.BookIII.Bridge.TranslationObstruction.nonlocal_disguise = 1
Instances For

---

### `Tau.BookIII.Bridge.obstruction_value`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L76-L98)
**def
Tau.BookIII.Bridge.obstruction_value
(obs : TranslationObstruction)

(k : ℕ)
 :ℕ**


[III.D91] Obstruction value at stage k: measures deviation from
faithful translation. Higher = worse.
Equations
- Tau.BookIII.Bridge.obstruction_value Tau.BookIII.Bridge.TranslationObstruction.unbounded_fanout k = k
- Tau.BookIII.Bridge.obstruction_value Tau.BookIII.Bridge.TranslationObstruction.global_equality k = 0
- Tau.BookIII.Bridge.obstruction_value Tau.BookIII.Bridge.TranslationObstruction.succinct_circuits k = if Tau.Polarity.primorial k > 0 then Tau.Polarity.primorial k else 0
- Tau.BookIII.Bridge.obstruction_value Tau.BookIII.Bridge.TranslationObstruction.exponential_quantification k = if Tau.Polarity.primorial k > 0 then Tau.Polarity.primorial k else 0
- Tau.BookIII.Bridge.obstruction_value Tau.BookIII.Bridge.TranslationObstruction.nonlocal_disguise k = 0
Instances For

---

### `Tau.BookIII.Bridge.obstruction_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L100-L121)
**def
Tau.BookIII.Bridge.obstruction_check
(db : ℕ)
 :Bool**


[III.D91] Obstruction check: verify obstruction values match
expected damage levels.
Equations
- Tau.BookIII.Bridge.obstruction_check db = Tau.BookIII.Bridge.obstruction_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Bridge.obstruction_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L105-L120)@[irreducible]

**def
Tau.BookIII.Bridge.obstruction_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.move_obstructs_arith`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L127-L134)
**def
Tau.BookIII.Bridge.move_obstructs_arith
(obs : TranslationObstruction)
 :Bool**


[III.D92] Does this move obstruct arithmetic translation?
Equations
- Tau.BookIII.Bridge.move_obstructs_arith Tau.BookIII.Bridge.TranslationObstruction.unbounded_fanout = true
- Tau.BookIII.Bridge.move_obstructs_arith Tau.BookIII.Bridge.TranslationObstruction.global_equality = false
- Tau.BookIII.Bridge.move_obstructs_arith Tau.BookIII.Bridge.TranslationObstruction.succinct_circuits = true
- Tau.BookIII.Bridge.move_obstructs_arith Tau.BookIII.Bridge.TranslationObstruction.exponential_quantification = true
- Tau.BookIII.Bridge.move_obstructs_arith Tau.BookIII.Bridge.TranslationObstruction.nonlocal_disguise = false
Instances For

---

### `Tau.BookIII.Bridge.move_obstructs_topo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L136-L143)
**def
Tau.BookIII.Bridge.move_obstructs_topo
(obs : TranslationObstruction)
 :Bool**


[III.D92] Does this move obstruct topological translation?
Equations
- Tau.BookIII.Bridge.move_obstructs_topo Tau.BookIII.Bridge.TranslationObstruction.unbounded_fanout = false
- Tau.BookIII.Bridge.move_obstructs_topo Tau.BookIII.Bridge.TranslationObstruction.global_equality = true
- Tau.BookIII.Bridge.move_obstructs_topo Tau.BookIII.Bridge.TranslationObstruction.succinct_circuits = true
- Tau.BookIII.Bridge.move_obstructs_topo Tau.BookIII.Bridge.TranslationObstruction.exponential_quantification = true
- Tau.BookIII.Bridge.move_obstructs_topo Tau.BookIII.Bridge.TranslationObstruction.nonlocal_disguise = true
Instances For

---

### `Tau.BookIII.Bridge.arith_obstruction_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L145-L150)
**def
Tau.BookIII.Bridge.arith_obstruction_count :ℕ**


[III.D92] Count how many obstructions affect arithmetic.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.topo_obstruction_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L152-L157)
**def
Tau.BookIII.Bridge.topo_obstruction_count :ℕ**


[III.D92] Count how many obstructions affect topology.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.safe_region_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L163-L184)
**def
Tau.BookIII.Bridge.safe_region_check
(bound db : ℕ)
 :Bool**


[III.T61] Safe region check: within the safe region (no forbidden
moves invoked), both translations are perfectly faithful.
Equations
- Tau.BookIII.Bridge.safe_region_check bound db = Tau.BookIII.Bridge.safe_region_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Bridge.safe_region_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L168-L183)@[irreducible]

**def
Tau.BookIII.Bridge.safe_region_check.go
(bound db x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.translation_failure_boundary_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L186-L193)
**def
Tau.BookIII.Bridge.translation_failure_boundary_check
(bound db : ℕ)
 :Bool**


[III.T61] Full translation failure boundary.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.pvsnp_obstruction_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L199-L231)
**def
Tau.BookIII.Bridge.pvsnp_obstruction_check
(db : ℕ)
 :Bool**


[III.P38] P vs NP obstruction: the succinct_circuits move has
damage 3, meaning the bridge breaks entirely. At each finite
stage k, P_adm = NP_adm (all problems decidable in finite Z/M_k Z),
but this internal equivalence cannot be translated.
Equations
- Tau.BookIII.Bridge.pvsnp_obstruction_check db = Tau.BookIII.Bridge.pvsnp_obstruction_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Bridge.pvsnp_obstruction_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L206-L222)@[irreducible]

**def
Tau.BookIII.Bridge.pvsnp_obstruction_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.pvsnp_obstruction_check.log_approx`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L224-L226)
**def
Tau.BookIII.Bridge.pvsnp_obstruction_check.log_approx
(n : ℕ)
 :ℕ**

Equations
- Tau.BookIII.Bridge.pvsnp_obstruction_check.log_approx n = Tau.BookIII.Bridge.pvsnp_obstruction_check.go_log n 0
Instances For

---

### `Tau.BookIII.Bridge.pvsnp_obstruction_check.go_log`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L228-L230)@[irreducible]

**def
Tau.BookIII.Bridge.pvsnp_obstruction_check.go_log
(n acc : ℕ)
 :ℕ**

Equations
- Tau.BookIII.Bridge.pvsnp_obstruction_check.go_log n acc = if n ≤ 1 then acc else Tau.BookIII.Bridge.pvsnp_obstruction_check.go_log (n / 2) (acc + 1)
Instances For

---

### `Tau.BookIII.Bridge.obstruction_check_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L237-L239)
**theorem
Tau.BookIII.Bridge.obstruction_check_3 :obstruction_check 3 = true**


[III.D91] Obstruction values correct at depth 3.

---

### `Tau.BookIII.Bridge.arith_obstruction_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L241-L243)
**theorem
Tau.BookIII.Bridge.arith_obstruction_3 :arith_obstruction_count = 3**


[III.D92] Arithmetic has 3 obstruction classes.

---

### `Tau.BookIII.Bridge.topo_obstruction_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L245-L247)
**theorem
Tau.BookIII.Bridge.topo_obstruction_4 :topo_obstruction_count = 4**


[III.D92] Topology has 4 obstruction classes.

---

### `Tau.BookIII.Bridge.safe_region_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L249-L251)
**theorem
Tau.BookIII.Bridge.safe_region_8_3 :safe_region_check 8 3 = true**


[III.T61] Safe region faithful at bound 8, depth 3.

---

### `Tau.BookIII.Bridge.translation_boundary_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L253-L255)
**theorem
Tau.BookIII.Bridge.translation_boundary_8_3 :translation_failure_boundary_check 8 3 = true**


[III.T61] Translation failure boundary at bound 8, depth 3.

---

### `Tau.BookIII.Bridge.pvsnp_obstruction_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationObstruction.lean#L257-L259)
**theorem
Tau.BookIII.Bridge.pvsnp_obstruction_3 :pvsnp_obstruction_check 3 = true**


[III.P38] P vs NP obstruction at depth 3.
