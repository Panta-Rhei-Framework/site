---
layout: taulib-doc
title: "TauLib.BookI.Orbit.Ladder"
permalink: /verify/taulib/docs/book-i-orbit-ladder/
lane: verify
module_name: "TauLib.BookI.Orbit.Ladder"
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

# TauLib.Orbit.Ladder


The iterator ladder: 4 levels of meta-iteration, and saturation at tetration.

## Registry Cross-References


- [I.D06] Iterator Ladder — `LadderLevel`, `ladderOp`

- [I.T02] Iterator Ladder Saturation — `ladder_saturation`

- [I.L01] Pentation Non-Injectivity — `pentation_channel_exhaustion`


## Ground Truth Sources


- chunk_0060_M000698: UR-ITER requirement, ladder saturation forced by arity exhaustion

- chunk_0050_M000608: Diagonal rewiring, typed channel assignments


## Mathematical Content


The iterator ladder has 4 levels:


- Level 0: ρ (successor / depth increment)

- Level 1: iterated ρ (addition on depths)

- Level 2: iterated addition (multiplication)

- Level 3: iterated multiplication (exponentiation)


Each level is canonically injective (in its second argument for fixed first).
At level 4 (tetration), the operations can still be defined, but there is
no 5th orbit channel to associate with pentation. Since there are only
4 non-omega generators, the ladder saturates at 4 levels (3 rewiring levels).

---

### `Tau.Orbit.LadderLevel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Ladder.lean#L41-L49)
**inductive
Tau.Orbit.LadderLevel :Type**


[I.D06] The 5 hyperoperation levels (ρ through tetration).
Only levels 0-3 have canonical orbit channel assignments.

- rho_level : LadderLevel
- add_level : LadderLevel
- mul_level : LadderLevel
- exp_level : LadderLevel
- tet_level : LadderLevel
Instances For

---

### `Tau.Orbit.instDecidableEqLadderLevel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Ladder.lean#L49-L49)
**instance
Tau.Orbit.instDecidableEqLadderLevel :DecidableEq LadderLevel**

Equations
- Tau.Orbit.instDecidableEqLadderLevel x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.Orbit.instReprLadderLevel.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Ladder.lean#L49-L49)
**def
Tau.Orbit.instReprLadderLevel.repr :LadderLevel → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Orbit.instReprLadderLevel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Ladder.lean#L49-L49)
**instance
Tau.Orbit.instReprLadderLevel :Repr LadderLevel**

Equations
- Tau.Orbit.instReprLadderLevel = { reprPrec := Tau.Orbit.instReprLadderLevel.repr }

---

### `Tau.Orbit.tetration`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Ladder.lean#L51-L54)
**def
Tau.Orbit.tetration :Nat → Nat → Nat**


Tetration (iterated exponentiation): a ↑↑ 0 = 1, a ↑↑ (n+1) = a ^ (a ↑↑ n).
Equations
- Tau.Orbit.tetration x✝ 0 = 1
- Tau.Orbit.tetration x✝ m.succ = x✝ ^ Tau.Orbit.tetration x✝ m
Instances For

---

### `Tau.Orbit.ladderOp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Ladder.lean#L56-L62)
**def
Tau.Orbit.ladderOp :LadderLevel → Nat → Nat → Nat**


The hyperoperation at each ladder level (on Nat = depth values).
Equations
- Tau.Orbit.ladderOp Tau.Orbit.LadderLevel.rho_level x✝¹ x✝ = x✝ + 1
- Tau.Orbit.ladderOp Tau.Orbit.LadderLevel.add_level x✝¹ x✝ = x✝¹ + x✝
- Tau.Orbit.ladderOp Tau.Orbit.LadderLevel.mul_level x✝¹ x✝ = x✝¹ * x✝
- Tau.Orbit.ladderOp Tau.Orbit.LadderLevel.exp_level x✝¹ x✝ = x✝¹ ^ x✝
- Tau.Orbit.ladderOp Tau.Orbit.LadderLevel.tet_level x✝¹ x✝ = Tau.Orbit.tetration x✝¹ x✝
Instances For

---

### `Tau.Orbit.ladderChannel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Ladder.lean#L64-L72)
**def
Tau.Orbit.ladderChannel :LadderLevel → Option Kernel.Generator**


The canonical orbit channel assigned to each rewiring level.
Level 0 (ρ) uses all channels uniformly.
Levels 1-3 each consume one solenoidal generator.
Equations
- Tau.Orbit.ladderChannel Tau.Orbit.LadderLevel.rho_level = none
- Tau.Orbit.ladderChannel Tau.Orbit.LadderLevel.add_level = some Tau.Kernel.Generator.pi
- Tau.Orbit.ladderChannel Tau.Orbit.LadderLevel.mul_level = some Tau.Kernel.Generator.gamma
- Tau.Orbit.ladderChannel Tau.Orbit.LadderLevel.exp_level = some Tau.Kernel.Generator.eta
- Tau.Orbit.ladderChannel Tau.Orbit.LadderLevel.tet_level = none
Instances For

---

### `Tau.Orbit.add_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Ladder.lean#L78-L82)
**theorem
Tau.Orbit.add_injective
(n : Nat)
 :Function.Injective fun (x : Nat) => n + x**


Addition is injective in the second argument (for any fixed first).

---

### `Tau.Orbit.mul_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Ladder.lean#L84-L103)
**theorem
Tau.Orbit.mul_injective
(n : Nat)

(hn : n > 0)
 :Function.Injective fun (x : Nat) => n * x**


Multiplication by n > 0 is injective in the second argument.

---

### `Tau.Orbit.exp_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Ladder.lean#L105-L117)
**theorem
Tau.Orbit.exp_injective
(n : Nat)

(hn : n ≥ 2)
 :Function.Injective fun (x : Nat) => n ^ x**


Exponentiation with base n ≥ 2 is injective in the exponent.

---

### `Tau.Orbit.available_channels`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Ladder.lean#L123-L125)
**theorem
Tau.Orbit.available_channels :Kernel.solenoidalGenerators.length = 3**


The number of available orbit channels for rewiring.

---

### `Tau.Orbit.pentation_channel_exhaustion`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Ladder.lean#L127-L134)
**theorem
Tau.Orbit.pentation_channel_exhaustion :ladderChannel LadderLevel.tet_level = none**


[I.L01] Pentation cannot be assigned a canonical orbit channel:
all 3 solenoidal generators are consumed by levels 1-3,
and alpha is the counting scaffold. No 5th channel exists (K6).

This is the channel-exhaustion form of the saturation argument.

---

### `Tau.Orbit.ladder_saturation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Ladder.lean#L136-L144)
**theorem
Tau.Orbit.ladder_saturation :Kernel.solenoidalGenerators.length = 3 ∧ ladderChannel LadderLevel.tet_level = none**


[I.T02] The iterator ladder saturates at 4 levels:
exactly 3 solenoidal generators exist (solenoidalGenerators.length = 3),
so exactly 3 rewiring levels can be canonically assigned,
giving 4 total operation levels (ρ + 3 rewirings).

The 4th rewiring level (pentation/level 4) has no channel.

---

### `Tau.Orbit.ladder_channels_assigned`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Ladder.lean#L146-L151)
**theorem
Tau.Orbit.ladder_channels_assigned :ladderChannel LadderLevel.add_level = some Kernel.Generator.pi ∧ ladderChannel LadderLevel.mul_level = some Kernel.Generator.gamma ∧ ladderChannel LadderLevel.exp_level = some Kernel.Generator.eta**


Each of the first 3 rewiring levels has an assigned channel.

---

### `Tau.Orbit.ladder_channels_distinct`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Ladder.lean#L153-L156)
**theorem
Tau.Orbit.ladder_channels_distinct :Kernel.Generator.pi ≠ Kernel.Generator.gamma ∧ Kernel.Generator.pi ≠ Kernel.Generator.eta ∧ Kernel.Generator.gamma ≠ Kernel.Generator.eta**


The assigned channels are pairwise distinct.
