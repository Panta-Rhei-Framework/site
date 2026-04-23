---
layout: taulib-doc
title: "TauLib.BookIII.Spectrum.TTM"
permalink: /verify/taulib/docs/book-iii-spectrum-ttm/
lane: verify
module_name: "TauLib.BookIII.Spectrum.TTM"
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

# TauLib.Spectrum.TTM


The tau-Tower Machine (TTM): register+port computation with the 5-generator alphabet.

## Registry Cross-References


- [I.D69] tau-Tower Machine -- `TTM`

- [I.D70] tau-Computability -- `TauComputable`


## Mathematical Content


The tau-Tower Machine (TTM) is a register machine whose alphabet is the
5-element generator set {alpha, pi, gamma, eta, omega}. Each register holds a
TauIdx value (orbit index = natural number). The machine has:


- **Bounded multiplicity**: a fixed number m of registers + b_0 ports

- **Unbounded magnitude**: each register can hold arbitrarily large TauIdx values

- **tau-native operations**: rho (successor), sigma (predecessor), multiplication,
wedge (min), and port I/O


The transition function is a list of guarded rules. Guards test register
equality or orbit membership. Operations are tau-native constructors:
rho for successor, sigma for predecessor, multiplication, and wedge (min).

This replaces the tape-based Turing machine model from the 1st Edition draft
with the register+port model specified in [I.D69].

---

### `Tau.Spectrum.Register`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L41-L42)@[reducible, inline]

**abbrev
Tau.Spectrum.Register :Type**


A register value is a TauIdx (= Nat, the orbit index).
Equations
- Tau.Spectrum.Register = Tau.Denotation.TauIdx
Instances For

---

### `Tau.Spectrum.TTMOp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L48-L65)
**inductive
Tau.Spectrum.TTMOp :Type**


[I.D69] TTM operations: the instruction set of the tau-Tower Machine.
All operations are tau-native, built from the generators and ρ.

- rho : Nat → Nat → TTMOp
r_i := rho(r_j) — successor via the progression operator

- sigma : Nat → Nat → TTMOp
r_i := sigma(r_j) — predecessor (truncated at 0)

- mul : Nat → Nat → Nat → TTMOp
r_i := r_j * r_k — multiplication

- wedge : Nat → Nat → Nat → TTMOp
r_i := r_j wedge r_k — minimum (lattice meet)

- readPort : Nat → Nat → TTMOp
r_i := read(p_j) — read from port j into register i

- writePort : Nat → Nat → TTMOp
write(p_j, r_i) — write register i to port j

- noop : TTMOp
no operation

Instances For

---

### `Tau.Spectrum.instDecidableEqTTMOp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L65-L65)
**instance
Tau.Spectrum.instDecidableEqTTMOp :DecidableEq TTMOp**

Equations
- Tau.Spectrum.instDecidableEqTTMOp = Tau.Spectrum.instDecidableEqTTMOp.decEq

---

### `Tau.Spectrum.instDecidableEqTTMOp.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L65-L65)
**def
Tau.Spectrum.instDecidableEqTTMOp.decEq
(x✝ x✝¹ : TTMOp)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.rho a a_1) (Tau.Spectrum.TTMOp.rho b b_1) = if h : a = b then h ▸ if h : a_1 = b_1 then h ▸ isTrue ⋯ else isFalse ⋯ else isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.rho a a_1) (Tau.Spectrum.TTMOp.sigma a_2 a_3) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.rho a a_1) (Tau.Spectrum.TTMOp.mul a_2 a_3 a_4) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.rho a a_1) (Tau.Spectrum.TTMOp.wedge a_2 a_3 a_4) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.rho a a_1) (Tau.Spectrum.TTMOp.readPort a_2 a_3) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.rho a a_1) (Tau.Spectrum.TTMOp.writePort a_2 a_3) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.rho a a_1) Tau.Spectrum.TTMOp.noop = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.sigma a a_1) (Tau.Spectrum.TTMOp.rho a_2 a_3) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.sigma a a_1) (Tau.Spectrum.TTMOp.sigma b b_1) = if h : a = b then h ▸ if h : a_1 = b_1 then h ▸ isTrue ⋯ else isFalse ⋯ else isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.sigma a a_1) (Tau.Spectrum.TTMOp.mul a_2 a_3 a_4) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.sigma a a_1) (Tau.Spectrum.TTMOp.wedge a_2 a_3 a_4) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.sigma a a_1) (Tau.Spectrum.TTMOp.readPort a_2 a_3) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.sigma a a_1) (Tau.Spectrum.TTMOp.writePort a_2 a_3) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.sigma a a_1) Tau.Spectrum.TTMOp.noop = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.mul a a_1 a_2) (Tau.Spectrum.TTMOp.rho a_3 a_4) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.mul a a_1 a_2) (Tau.Spectrum.TTMOp.sigma a_3 a_4) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.mul a a_1 a_2) (Tau.Spectrum.TTMOp.wedge a_3 a_4 a_5) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.mul a a_1 a_2) (Tau.Spectrum.TTMOp.readPort a_3 a_4) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.mul a a_1 a_2) (Tau.Spectrum.TTMOp.writePort a_3 a_4) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.mul a a_1 a_2) Tau.Spectrum.TTMOp.noop = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.wedge a a_1 a_2) (Tau.Spectrum.TTMOp.rho a_3 a_4) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.wedge a a_1 a_2) (Tau.Spectrum.TTMOp.sigma a_3 a_4) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.wedge a a_1 a_2) (Tau.Spectrum.TTMOp.mul a_3 a_4 a_5) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.wedge a a_1 a_2) (Tau.Spectrum.TTMOp.readPort a_3 a_4) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.wedge a a_1 a_2) (Tau.Spectrum.TTMOp.writePort a_3 a_4) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.wedge a a_1 a_2) Tau.Spectrum.TTMOp.noop = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.readPort a a_1) (Tau.Spectrum.TTMOp.rho a_2 a_3) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.readPort a a_1) (Tau.Spectrum.TTMOp.sigma a_2 a_3) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.readPort a a_1) (Tau.Spectrum.TTMOp.mul a_2 a_3 a_4) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.readPort a a_1) (Tau.Spectrum.TTMOp.wedge a_2 a_3 a_4) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.readPort a a_1) (Tau.Spectrum.TTMOp.writePort a_2 a_3) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.readPort a a_1) Tau.Spectrum.TTMOp.noop = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.writePort a a_1) (Tau.Spectrum.TTMOp.rho a_2 a_3) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.writePort a a_1) (Tau.Spectrum.TTMOp.sigma a_2 a_3) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.writePort a a_1) (Tau.Spectrum.TTMOp.mul a_2 a_3 a_4) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.writePort a a_1) (Tau.Spectrum.TTMOp.wedge a_2 a_3 a_4) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.writePort a a_1) (Tau.Spectrum.TTMOp.readPort a_2 a_3) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq (Tau.Spectrum.TTMOp.writePort a a_1) Tau.Spectrum.TTMOp.noop = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq Tau.Spectrum.TTMOp.noop (Tau.Spectrum.TTMOp.rho a a_1) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq Tau.Spectrum.TTMOp.noop (Tau.Spectrum.TTMOp.sigma a a_1) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq Tau.Spectrum.TTMOp.noop (Tau.Spectrum.TTMOp.mul a a_1 a_2) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq Tau.Spectrum.TTMOp.noop (Tau.Spectrum.TTMOp.wedge a a_1 a_2) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq Tau.Spectrum.TTMOp.noop (Tau.Spectrum.TTMOp.readPort a a_1) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq Tau.Spectrum.TTMOp.noop (Tau.Spectrum.TTMOp.writePort a a_1) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMOp.decEq Tau.Spectrum.TTMOp.noop Tau.Spectrum.TTMOp.noop = isTrue ⋯
Instances For

---

### `Tau.Spectrum.instReprTTMOp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L65-L65)
**instance
Tau.Spectrum.instReprTTMOp :Repr TTMOp**

Equations
- Tau.Spectrum.instReprTTMOp = { reprPrec := Tau.Spectrum.instReprTTMOp.repr }

---

### `Tau.Spectrum.instReprTTMOp.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L65-L65)
**def
Tau.Spectrum.instReprTTMOp.repr :TTMOp → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
- Tau.Spectrum.instReprTTMOp.repr Tau.Spectrum.TTMOp.noop prec✝ = Repr.addAppParen (Std.Format.nest (if prec✝ ≥ 1024 then 1 else 2) (Std.Format.text "Tau.Spectrum.TTMOp.noop")).group
 prec✝
Instances For

---

### `Tau.Spectrum.TTMGuard`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L71-L79)
**inductive
Tau.Spectrum.TTMGuard :Type**


Guard predicates for TTM transition rules.

- always : TTMGuard
Unconditional: always fires

- regEq : Nat → Nat → TTMGuard
Register equality: r_i = r_j

- orbitEq : Nat → Kernel.Generator → TTMGuard
Orbit membership: the orbit of r_i equals generator g

Instances For

---

### `Tau.Spectrum.instDecidableEqTTMGuard`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L79-L79)
**instance
Tau.Spectrum.instDecidableEqTTMGuard :DecidableEq TTMGuard**

Equations
- Tau.Spectrum.instDecidableEqTTMGuard = Tau.Spectrum.instDecidableEqTTMGuard.decEq

---

### `Tau.Spectrum.instDecidableEqTTMGuard.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L79-L79)
**def
Tau.Spectrum.instDecidableEqTTMGuard.decEq
(x✝ x✝¹ : TTMGuard)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
- Tau.Spectrum.instDecidableEqTTMGuard.decEq Tau.Spectrum.TTMGuard.always Tau.Spectrum.TTMGuard.always = isTrue ⋯
- Tau.Spectrum.instDecidableEqTTMGuard.decEq Tau.Spectrum.TTMGuard.always (Tau.Spectrum.TTMGuard.regEq a a_1) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMGuard.decEq Tau.Spectrum.TTMGuard.always (Tau.Spectrum.TTMGuard.orbitEq a a_1) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMGuard.decEq (Tau.Spectrum.TTMGuard.regEq a a_1) Tau.Spectrum.TTMGuard.always = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMGuard.decEq (Tau.Spectrum.TTMGuard.regEq a a_1) (Tau.Spectrum.TTMGuard.orbitEq a_2 a_3) = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMGuard.decEq (Tau.Spectrum.TTMGuard.orbitEq a a_1) Tau.Spectrum.TTMGuard.always = isFalse ⋯
- Tau.Spectrum.instDecidableEqTTMGuard.decEq (Tau.Spectrum.TTMGuard.orbitEq a a_1) (Tau.Spectrum.TTMGuard.regEq a_2 a_3) = isFalse ⋯
Instances For

---

### `Tau.Spectrum.instReprTTMGuard`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L79-L79)
**instance
Tau.Spectrum.instReprTTMGuard :Repr TTMGuard**

Equations
- Tau.Spectrum.instReprTTMGuard = { reprPrec := Tau.Spectrum.instReprTTMGuard.repr }

---

### `Tau.Spectrum.instReprTTMGuard.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L79-L79)
**def
Tau.Spectrum.instReprTTMGuard.repr :TTMGuard → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Spectrum.TTMRule`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L85-L95)
**structure
Tau.Spectrum.TTMRule :Type**


A TTM transition rule: guarded state transition with operations.

- from_state : Denotation.TauIdx
Source state

- guard : TTMGuard
Guard predicate

- ops : List TTMOp
Operations to execute (in order)

- to_state : Denotation.TauIdx
Target state

Instances For

---

### `Tau.Spectrum.instDecidableEqTTMRule`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L95-L95)
**instance
Tau.Spectrum.instDecidableEqTTMRule :DecidableEq TTMRule**

Equations
- Tau.Spectrum.instDecidableEqTTMRule = Tau.Spectrum.instDecidableEqTTMRule.decEq

---

### `Tau.Spectrum.instDecidableEqTTMRule.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L95-L95)
**def
Tau.Spectrum.instDecidableEqTTMRule.decEq
(x✝ x✝¹ : TTMRule)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Spectrum.instReprTTMRule.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L95-L95)
**def
Tau.Spectrum.instReprTTMRule.repr :TTMRule → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Spectrum.instReprTTMRule`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L95-L95)
**instance
Tau.Spectrum.instReprTTMRule :Repr TTMRule**

Equations
- Tau.Spectrum.instReprTTMRule = { reprPrec := Tau.Spectrum.instReprTTMRule.repr }

---

### `Tau.Spectrum.TTMConfig`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L101-L109)
**structure
Tau.Spectrum.TTMConfig :Type**


[I.D69] A TTM configuration: state q, register file R, port buffer E.

- state : Denotation.TauIdx
Current control state (a TauIdx)

- registers : List Register
Register file: fixed length m, each holding a TauIdx

- ports : List Register
Port buffer: fixed length b_0, each holding a TauIdx

Instances For

---

### `Tau.Spectrum.instDecidableEqTTMConfig`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L109-L109)
**instance
Tau.Spectrum.instDecidableEqTTMConfig :DecidableEq TTMConfig**

Equations
- Tau.Spectrum.instDecidableEqTTMConfig = Tau.Spectrum.instDecidableEqTTMConfig.decEq

---

### `Tau.Spectrum.instDecidableEqTTMConfig.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L109-L109)
**def
Tau.Spectrum.instDecidableEqTTMConfig.decEq
(x✝ x✝¹ : TTMConfig)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Spectrum.instReprTTMConfig.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L109-L109)
**def
Tau.Spectrum.instReprTTMConfig.repr :TTMConfig → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Spectrum.instReprTTMConfig`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L109-L109)
**instance
Tau.Spectrum.instReprTTMConfig :Repr TTMConfig**

Equations
- Tau.Spectrum.instReprTTMConfig = { reprPrec := Tau.Spectrum.instReprTTMConfig.repr }

---

### `Tau.Spectrum.TTM`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L115-L128)
**structure
Tau.Spectrum.TTM :Type**


[I.D69] The tau-Tower Machine: a register machine with tau-native operations.
Bounded multiplicity (m registers + b_0 ports), unbounded magnitude.

- num_registers : Nat
Number of registers (m >= 1)

- num_ports : Nat
Number of ports (b_0 >= 0)

- rules : List TTMRule
Transition rules

- init_state : Denotation.TauIdx
Initial control state

- accept_states : List Denotation.TauIdx
Accepting (halting) states

Instances For

---

### `Tau.Spectrum.instReprTTM.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L128-L128)
**def
Tau.Spectrum.instReprTTM.repr :TTM → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Spectrum.instReprTTM`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L128-L128)
**instance
Tau.Spectrum.instReprTTM :Repr TTM**

Equations
- Tau.Spectrum.instReprTTM = { reprPrec := Tau.Spectrum.instReprTTM.repr }

---

### `Tau.Spectrum.TTM.initConfig`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L134-L140)
**def
Tau.Spectrum.TTM.initConfig
(m : TTM)

(input : Denotation.TauIdx)
 :TTMConfig**


Create the initial configuration: r_0 = input, all other registers and ports = 0.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Spectrum.TTM.isAccepting`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L146-L148)
**def
Tau.Spectrum.TTM.isAccepting
(m : TTM)

(c : TTMConfig)
 :Bool**


Check if a configuration is in an accepting state.
Equations
- m.isAccepting c = m.accept_states.contains c.state
Instances For

---

### `Tau.Spectrum.TTM.isHalted`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L150-L152)
**def
Tau.Spectrum.TTM.isHalted
(m : TTM)

(c : TTMConfig)
 :Bool**


Check if a TTM has halted. Simplified: halted = accepting.
Equations
- m.isHalted c = m.isAccepting c
Instances For

---

### `Tau.Spectrum.readReg`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L158-L160)
**def
Tau.Spectrum.readReg
(regs : List Register)

(i : Nat)
 :Register**


Safe register read: returns 0 if index is out of bounds.
Equations
- Tau.Spectrum.readReg regs i = regs.getD i 0
Instances For

---

### `Tau.Spectrum.writeReg`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L162-L164)
**def
Tau.Spectrum.writeReg
(regs : List Register)

(i : Nat)

(v : Register)
 :List Register**


Safe register write: returns unchanged list if index is out of bounds.
Equations
- Tau.Spectrum.writeReg regs i v = if i < regs.length then regs.set i v else regs
Instances For

---

### `Tau.Spectrum.execOp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L170-L197)
**def
Tau.Spectrum.execOp
(c : TTMConfig)

(op : TTMOp)
 :TTMConfig**


Execute a single TTM operation on a configuration.
Equations
- One or more equations did not get rendered due to their size.
- Tau.Spectrum.execOp c (Tau.Spectrum.TTMOp.rho a a_1) = { state := c.state, registers := Tau.Spectrum.writeReg c.registers a (Tau.Spectrum.readReg c.registers a_1 + 1),
 ports := c.ports }
- Tau.Spectrum.execOp c (Tau.Spectrum.TTMOp.sigma a a_1) = { state := c.state, registers := Tau.Spectrum.writeReg c.registers a (Tau.Spectrum.readReg c.registers a_1 - 1),
 ports := c.ports }
- Tau.Spectrum.execOp c (Tau.Spectrum.TTMOp.readPort a a_1) = { state := c.state, registers := Tau.Spectrum.writeReg c.registers a (Tau.Spectrum.readReg c.ports a_1),
 ports := c.ports }
- Tau.Spectrum.execOp c (Tau.Spectrum.TTMOp.writePort a a_1) = { state := c.state, registers := c.registers,
 ports := Tau.Spectrum.writeReg c.ports a (Tau.Spectrum.readReg c.registers a_1) }
- Tau.Spectrum.execOp c Tau.Spectrum.TTMOp.noop = c
Instances For

---

### `Tau.Spectrum.execOps`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L199-L201)
**def
Tau.Spectrum.execOps
(c : TTMConfig)

(ops : List TTMOp)
 :TTMConfig**


Execute a list of TTM operations sequentially.
Equations
- Tau.Spectrum.execOps c ops = List.foldl Tau.Spectrum.execOp c ops
Instances For

---

### `Tau.Spectrum.evalGuard`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L207-L218)
**def
Tau.Spectrum.evalGuard
(c : TTMConfig)

(g : TTMGuard)
 :Bool**


Evaluate a guard predicate on a configuration.
Equations
- Tau.Spectrum.evalGuard c Tau.Spectrum.TTMGuard.always = true
- Tau.Spectrum.evalGuard c (Tau.Spectrum.TTMGuard.regEq a a_1) = (Tau.Spectrum.readReg c.registers a == Tau.Spectrum.readReg c.registers a_1)
- Tau.Spectrum.evalGuard c (Tau.Spectrum.TTMGuard.orbitEq a a_1) = (Tau.Spectrum.readReg c.registers a % 5 == a_1.toNat)
Instances For

---

### `Tau.Spectrum.TTM.findRule`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L224-L226)
**def
Tau.Spectrum.TTM.findRule
(m : TTM)

(c : TTMConfig)
 :Option TTMRule**


Find the first matching rule for the current configuration.
Equations
- m.findRule c = List.find? (fun (r : Tau.Spectrum.TTMRule) => r.from_state == c.state && Tau.Spectrum.evalGuard c r.guard) m.rules
Instances For

---

### `Tau.Spectrum.TTM.step`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L228-L235)
**def
Tau.Spectrum.TTM.step
(m : TTM)

(c : TTMConfig)
 :TTMConfig**


Execute one step of the TTM: apply the first matching rule.
Returns the configuration unchanged if no rule matches (halted).
Equations
- m.step c = match m.findRule c with
 | none => c
 | some rule =>
 have c' := Tau.Spectrum.execOps c rule.ops;
 { state := rule.to_state, registers := c'.registers, ports := c'.ports }
Instances For

---

### `Tau.Spectrum.TTM.run`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L237-L243)
**def
Tau.Spectrum.TTM.run
(m : TTM)

(c : TTMConfig)

(fuel : Nat)
 :TTMConfig**


Execute up to `fuel` steps. Returns the final configuration.
Equations
- m.run c 0 = c
- m.run c n.succ = if m.isHalted c = true then c else m.run (m.step c) n
Instances For

---

### `Tau.Spectrum.TauComputable`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L249-L256)
**def
Tau.Spectrum.TauComputable
(f : Denotation.TauIdx → Denotation.TauIdx)
 :Prop**


[I.D70] A function f : TauIdx -> TauIdx is tau-computable if there exists
a TTM and a fuel bound such that for every input n, the TTM halts in
an accepting state with f(n) in register 0.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Spectrum.generator_symbols_distinct`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L262-L275)
**theorem
Tau.Spectrum.generator_symbols_distinct :Kernel.Generator.alpha ≠ Kernel.Generator.pi ∧ Kernel.Generator.alpha ≠ Kernel.Generator.gamma ∧ Kernel.Generator.alpha ≠ Kernel.Generator.eta ∧ Kernel.Generator.alpha ≠ Kernel.Generator.omega ∧ Kernel.Generator.pi ≠ Kernel.Generator.gamma ∧ Kernel.Generator.pi ≠ Kernel.Generator.eta ∧ Kernel.Generator.pi ≠ Kernel.Generator.omega ∧ Kernel.Generator.gamma ≠ Kernel.Generator.eta ∧ Kernel.Generator.gamma ≠ Kernel.Generator.omega ∧ Kernel.Generator.eta ≠ Kernel.Generator.omega**


The 5 generators are pairwise distinct.

---

### `Tau.Spectrum.ttm_tau_native`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L277-L282)
**theorem
Tau.Spectrum.ttm_tau_native
(n : Denotation.TauIdx)
 :n % 5 < 5**


The 5-generator alphabet covers all orbits: every TauIdx maps to
one of the 5 generators under mod-5 orbit assignment.

---

### `Tau.Spectrum.ttm_register_bounded`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L284-L287)
**theorem
Tau.Spectrum.ttm_register_bounded
(m : TTM)
 :m.num_registers + m.num_ports = m.num_registers + m.num_ports**


Multiplicity = num_registers + num_ports: the total number of
storage cells is exactly the sum of registers and ports.

---

### `Tau.Spectrum.trivial_ttm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L293-L294)
**def
Tau.Spectrum.trivial_ttm :TTM**


A trivial TTM: 1 register, 0 ports, no rules, immediate accept at state 0.
Equations
- Tau.Spectrum.trivial_ttm = { num_registers := 1, num_ports := 0, rules := [], init_state := 0, accept_states := [0] }
Instances For

---

### `Tau.Spectrum.trivial_accepts`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L296-L299)
**theorem
Tau.Spectrum.trivial_accepts :trivial_ttm.isAccepting (trivial_ttm.initConfig 0) = true**


The trivial TTM immediately accepts from its initial state.

---

### `Tau.Spectrum.trivial_halted`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L301-L304)
**theorem
Tau.Spectrum.trivial_halted :trivial_ttm.isHalted (trivial_ttm.initConfig 0) = true**


The trivial TTM is halted from its initial state.

---

### `Tau.Spectrum.trivial_halted_any`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L306-L309)
**theorem
Tau.Spectrum.trivial_halted_any
(n : Denotation.TauIdx)
 :trivial_ttm.isHalted (trivial_ttm.initConfig n) = true**


The trivial TTM is halted from any initial input.

---

### `Tau.Spectrum.trivial_run`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectrum/TTM.lean#L311-L319)
**theorem
Tau.Spectrum.trivial_run
(n : Denotation.TauIdx)

(fuel : Nat)
 :trivial_ttm.run (trivial_ttm.initConfig n) fuel = trivial_ttm.initConfig n**


Running the trivial TTM returns the initial configuration unchanged.
