---
layout: taulib-doc
title: "TauLib.BookIII.Bridge.ForbiddenMoves"
permalink: /verify/taulib/docs/book-iii-bridge-forbidden-moves/
lane: verify
module_name: "TauLib.BookIII.Bridge.ForbiddenMoves"
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

# TauLib.BookIII.Bridge.ForbiddenMoves


Five Forbidden Moves and Move-Bridge Correspondence.

## Registry Cross-References


- [III.D69] Five Forbidden Moves -- `ForbiddenMove`, `forbidden_moves_check`

- [III.T43] Move-Bridge Correspondence -- `move_bridge_check`


## Mathematical Content


**III.D69 (Five Forbidden Moves):** Five operations ZFC allows but tau forbids:
(1) Unbounded fan-out (K3 axiom violation),
(2) Global equality (K5 axiom violation),
(3) Succinct circuits (operational closure violation),
(4) Exponential quantification (observation-finiteness violation),
(5) Non-local disguise (NF uniqueness violation).
Each forbidden move requires unbounded primorial depth: no finite
primorial level k can express the operation.

**III.T43 (Move-Bridge Correspondence):** Each forbidden move corresponds to
a specific enrichment level boundary. The bridge functor is faithful on the
complement of the five forbidden moves and degenerates precisely at them.

---

### `Tau.BookIII.Bridge.ForbiddenMove`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L40-L49)
**inductive
Tau.BookIII.Bridge.ForbiddenMove :Type**


[III.D69] The five operations ZFC allows but tau forbids.
Each represents a structural feature that exceeds finite
primorial capacity.

- unbounded_fanout : ForbiddenMove
- global_equality : ForbiddenMove
- succinct_circuits : ForbiddenMove
- exponential_quantification : ForbiddenMove
- nonlocal_disguise : ForbiddenMove
Instances For

---

### `Tau.BookIII.Bridge.instReprForbiddenMove`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L49-L49)
**instance
Tau.BookIII.Bridge.instReprForbiddenMove :Repr ForbiddenMove**

Equations
- Tau.BookIII.Bridge.instReprForbiddenMove = { reprPrec := Tau.BookIII.Bridge.instReprForbiddenMove.repr }

---

### `Tau.BookIII.Bridge.instReprForbiddenMove.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L49-L49)
**def
Tau.BookIII.Bridge.instReprForbiddenMove.repr :ForbiddenMove → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.instDecidableEqForbiddenMove`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L49-L49)
**instance
Tau.BookIII.Bridge.instDecidableEqForbiddenMove :DecidableEq ForbiddenMove**

Equations
- Tau.BookIII.Bridge.instDecidableEqForbiddenMove x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIII.Bridge.instBEqForbiddenMove.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L49-L49)
**def
Tau.BookIII.Bridge.instBEqForbiddenMove.beq :ForbiddenMove → ForbiddenMove → Bool**

Equations
- Tau.BookIII.Bridge.instBEqForbiddenMove.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIII.Bridge.instBEqForbiddenMove`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L49-L49)
**instance
Tau.BookIII.Bridge.instBEqForbiddenMove :BEq ForbiddenMove**

Equations
- Tau.BookIII.Bridge.instBEqForbiddenMove = { beq := Tau.BookIII.Bridge.instBEqForbiddenMove.beq }

---

### `Tau.BookIII.Bridge.forbidden_move_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L51-L52)
**def
Tau.BookIII.Bridge.forbidden_move_count :ℕ**


[III.D69] Number of forbidden moves.
Equations
- Tau.BookIII.Bridge.forbidden_move_count = 5
Instances For

---

### `Tau.BookIII.Bridge.ForbiddenMove.toNat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L54-L60)
**def
Tau.BookIII.Bridge.ForbiddenMove.toNat :ForbiddenMove → ℕ**


[III.D69] Numeric index of each forbidden move.
Equations
- Tau.BookIII.Bridge.ForbiddenMove.unbounded_fanout.toNat = 0
- Tau.BookIII.Bridge.ForbiddenMove.global_equality.toNat = 1
- Tau.BookIII.Bridge.ForbiddenMove.succinct_circuits.toNat = 2
- Tau.BookIII.Bridge.ForbiddenMove.exponential_quantification.toNat = 3
- Tau.BookIII.Bridge.ForbiddenMove.nonlocal_disguise.toNat = 4
Instances For

---

### `Tau.BookIII.Bridge.all_forbidden_moves`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L62-L65)
**def
Tau.BookIII.Bridge.all_forbidden_moves :List ForbiddenMove**


All forbidden moves as a list.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.violated_axiom`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L67-L74)
**def
Tau.BookIII.Bridge.violated_axiom :ForbiddenMove → Hinge.ChainLink**


[III.D69] The tau axiom that each forbidden move violates.
Returns the ChainLink (K0-K6) that imposes the constraint.
Equations
- Tau.BookIII.Bridge.violated_axiom Tau.BookIII.Bridge.ForbiddenMove.unbounded_fanout = Tau.BookIII.Hinge.ChainLink.K3
- Tau.BookIII.Bridge.violated_axiom Tau.BookIII.Bridge.ForbiddenMove.global_equality = Tau.BookIII.Hinge.ChainLink.K5
- Tau.BookIII.Bridge.violated_axiom Tau.BookIII.Bridge.ForbiddenMove.succinct_circuits = Tau.BookIII.Hinge.ChainLink.E2
- Tau.BookIII.Bridge.violated_axiom Tau.BookIII.Bridge.ForbiddenMove.exponential_quantification = Tau.BookIII.Hinge.ChainLink.K4
- Tau.BookIII.Bridge.violated_axiom Tau.BookIII.Bridge.ForbiddenMove.nonlocal_disguise = Tau.BookIII.Hinge.ChainLink.K4
Instances For

---

### `Tau.BookIII.Bridge.move_threshold`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L76-L85)
**def
Tau.BookIII.Bridge.move_threshold
(fm : ForbiddenMove)

(db : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D69] The minimum primorial depth at which the forbidden move
manifests. Below this depth, the move is harmless (finite state space
makes everything bounded).
Equations
- Tau.BookIII.Bridge.move_threshold Tau.BookIII.Bridge.ForbiddenMove.unbounded_fanout db = db + 1
- Tau.BookIII.Bridge.move_threshold Tau.BookIII.Bridge.ForbiddenMove.global_equality db = db + 1
- Tau.BookIII.Bridge.move_threshold Tau.BookIII.Bridge.ForbiddenMove.succinct_circuits db = db + 1
- Tau.BookIII.Bridge.move_threshold Tau.BookIII.Bridge.ForbiddenMove.exponential_quantification db = db + 1
- Tau.BookIII.Bridge.move_threshold Tau.BookIII.Bridge.ForbiddenMove.nonlocal_disguise db = db + 1
Instances For

---

### `Tau.BookIII.Bridge.forbidden_witness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L87-L113)
**def
Tau.BookIII.Bridge.forbidden_witness
(fm : ForbiddenMove)

(x k : Denotation.TauIdx)
 :Bool**


[III.D69] Forbidden move witness: at any fixed depth k, the tau-system
CANNOT express the forbidden operation. Each move is demonstrated by
showing that the required operation exceeds primorial capacity.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.forbidden_moves_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L115-L133)
**def
Tau.BookIII.Bridge.forbidden_moves_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D69] Forbidden moves check: verify that at each finite depth k,
all five forbidden operations are constrained (i.e., the tau-system
cannot express them unboundedly).
Equations
- Tau.BookIII.Bridge.forbidden_moves_check bound db = Tau.BookIII.Bridge.forbidden_moves_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Bridge.forbidden_moves_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L121-L132)@[irreducible]

**def
Tau.BookIII.Bridge.forbidden_moves_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.bridge_damage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L139-L150)
**def
Tau.BookIII.Bridge.bridge_damage :ForbiddenMove → ℕ**


[III.T43] Bridge degradation: how each forbidden move affects the
bridge functor. Returns the "bridge damage" category:


- 0 = no damage (move not applicable)

- 1 = mild (bridge loses injectivity)

- 2 = severe (bridge loses faithfulness)

- 3 = break (bridge degenerates entirely)

Equations
- Tau.BookIII.Bridge.bridge_damage Tau.BookIII.Bridge.ForbiddenMove.unbounded_fanout = 2
- Tau.BookIII.Bridge.bridge_damage Tau.BookIII.Bridge.ForbiddenMove.global_equality = 1
- Tau.BookIII.Bridge.bridge_damage Tau.BookIII.Bridge.ForbiddenMove.succinct_circuits = 3
- Tau.BookIII.Bridge.bridge_damage Tau.BookIII.Bridge.ForbiddenMove.exponential_quantification = 3
- Tau.BookIII.Bridge.bridge_damage Tau.BookIII.Bridge.ForbiddenMove.nonlocal_disguise = 1
Instances For

---

### `Tau.BookIII.Bridge.move_bridge_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L152-L182)
**def
Tau.BookIII.Bridge.move_bridge_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T43] Move-bridge correspondence check: verify that the bridge
functor degenerates precisely at the five forbidden moves.
At each depth k, the "safe" operations (non-forbidden) preserve
full bridge structure, while forbidden operations degrade it.
Equations
- Tau.BookIII.Bridge.move_bridge_check bound db = Tau.BookIII.Bridge.move_bridge_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Bridge.move_bridge_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L159-L181)@[irreducible]

**def
Tau.BookIII.Bridge.move_bridge_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.move_correspondence_exhaustive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L184-L197)
**def
Tau.BookIII.Bridge.move_correspondence_exhaustive :Bool**


[III.T43] Correspondence exhaustiveness: all 5 moves are distinct
and each has a violated axiom.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.pvsnp_forbidden_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L199-L202)
**def
Tau.BookIII.Bridge.pvsnp_forbidden_count :ℕ**


[III.T43] P vs NP uses exactly 3 of the 5 forbidden moves
(the three with bridge_damage = 3 or 2).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.forbidden_moves_8_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L233-L234)
**theorem
Tau.BookIII.Bridge.forbidden_moves_8_3 :forbidden_moves_check 8 3 = true**


---

### `Tau.BookIII.Bridge.move_bridge_8_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L237-L238)
**theorem
Tau.BookIII.Bridge.move_bridge_8_3 :move_bridge_check 8 3 = true**


---

### `Tau.BookIII.Bridge.move_correspondence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L241-L242)
**theorem
Tau.BookIII.Bridge.move_correspondence :move_correspondence_exhaustive = true**


---

### `Tau.BookIII.Bridge.five_forbidden`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L248-L249)
**theorem
Tau.BookIII.Bridge.five_forbidden :all_forbidden_moves.length = 5**


[III.D69] Structural: there are exactly 5 forbidden moves.

---

### `Tau.BookIII.Bridge.move_index_0`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L251-L252)
**theorem
Tau.BookIII.Bridge.move_index_0 :ForbiddenMove.unbounded_fanout.toNat = 0**


[III.D69] Structural: forbidden move indices are 0..4.

---

### `Tau.BookIII.Bridge.move_index_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L253-L253)
**theorem
Tau.BookIII.Bridge.move_index_4 :ForbiddenMove.nonlocal_disguise.toNat = 4**


---

### `Tau.BookIII.Bridge.fanout_violates_K3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L255-L257)
**theorem
Tau.BookIII.Bridge.fanout_violates_K3 :violated_axiom ForbiddenMove.unbounded_fanout = Hinge.ChainLink.K3**


[III.D69] Structural: unbounded fanout violates K3 (boundary).

---

### `Tau.BookIII.Bridge.equality_violates_K5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L259-L261)
**theorem
Tau.BookIII.Bridge.equality_violates_K5 :violated_axiom ForbiddenMove.global_equality = Hinge.ChainLink.K5**


[III.D69] Structural: global equality violates K5 (composition).

---

### `Tau.BookIII.Bridge.circuits_break_bridge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L263-L265)
**theorem
Tau.BookIII.Bridge.circuits_break_bridge :bridge_damage ForbiddenMove.succinct_circuits = 3**


[III.T43] Structural: succinct circuits cause bridge break.

---

### `Tau.BookIII.Bridge.pvsnp_uses_3_moves`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L267-L269)
**theorem
Tau.BookIII.Bridge.pvsnp_uses_3_moves :pvsnp_forbidden_count = 3**


[III.T43] Structural: P vs NP involves 3 forbidden moves.

---

### `Tau.BookIII.Bridge.max_damage_is_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L271-L274)
**theorem
Tau.BookIII.Bridge.max_damage_is_3 :(all_forbidden_moves.all fun (fm : ForbiddenMove) => decide (bridge_damage fm ≤ 3)) = true**


[III.T43] Structural: maximum bridge damage is 3 (break).

---

### `Tau.BookIII.Bridge.threshold_exceeds`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L276-L280)
**theorem
Tau.BookIII.Bridge.threshold_exceeds
(fm : ForbiddenMove)

(db : Denotation.TauIdx)
 :move_threshold fm db > db**


[III.D69] Structural: all moves have threshold > db (requires
unbounded depth).
