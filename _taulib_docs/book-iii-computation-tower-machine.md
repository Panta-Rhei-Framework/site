---
layout: taulib-doc
title: "TauLib.BookIII.Computation.TowerMachine"
permalink: /verify/taulib/docs/book-iii-computation-tower-machine/
lane: verify
module_name: "TauLib.BookIII.Computation.TowerMachine"
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

# TauLib.BookIII.Computation.TowerMachine


τ-Tower Machine, TTM τ-Nativity, and Observable Transition.

## Registry Cross-References


- [III.D51] τ-Tower Machine -- `TTMConfig`, `ttm_step`, `ttm_check`

- [III.T30] TTM τ-Nativity -- `ttm_nativity_check`

- [III.D52] Observable Transition -- `observable_transition_check`


## Mathematical Content


**III.D51 (τ-Tower Machine):** The TTM at E₂: a state machine operating on
τ-addresses. Configuration = (state, register_values, depth). Transitions
are modular operations at primorial level k. Extends Book I's TTM (I.D69)
to the enriched E₂ setting.

**III.T30 (TTM τ-Nativity):** Program IS τ-address operating ON τ-addresses.
Code = data = τ-address. No external representation needed: the machine's
program is itself a cylinder in ℤ̂_τ.

**III.D52 (Observable Transition):** The observable transition function
δ^obs operates on bounded configurations. The Cook-Levin width W = 1 + m
bounds the observable state at each step.

---

### `Tau.BookIII.Computation.TTMConfig`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L41-L48)
**structure
Tau.BookIII.Computation.TTMConfig :Type**


[III.D51] TTM configuration at E₂ level: state + register values at
primorial depth k. The registers hold τ-addresses.

- state : Denotation.TauIdx
- reg_a : Denotation.TauIdx
- reg_b : Denotation.TauIdx
- depth : Denotation.TauIdx
Instances For

---

### `Tau.BookIII.Computation.instReprTTMConfig`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L48-L48)
**instance
Tau.BookIII.Computation.instReprTTMConfig :Repr TTMConfig**

Equations
- Tau.BookIII.Computation.instReprTTMConfig = { reprPrec := Tau.BookIII.Computation.instReprTTMConfig.repr }

---

### `Tau.BookIII.Computation.instReprTTMConfig.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L48-L48)
**def
Tau.BookIII.Computation.instReprTTMConfig.repr :TTMConfig → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.instDecidableEqTTMConfig.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L48-L48)
**def
Tau.BookIII.Computation.instDecidableEqTTMConfig.decEq
(x✝ x✝¹ : TTMConfig)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.instDecidableEqTTMConfig`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L48-L48)
**instance
Tau.BookIII.Computation.instDecidableEqTTMConfig :DecidableEq TTMConfig**

Equations
- Tau.BookIII.Computation.instDecidableEqTTMConfig = Tau.BookIII.Computation.instDecidableEqTTMConfig.decEq

---

### `Tau.BookIII.Computation.instBEqTTMConfig.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L48-L48)
**def
Tau.BookIII.Computation.instBEqTTMConfig.beq :TTMConfig → TTMConfig → Bool**

Equations
- One or more equations did not get rendered due to their size.
- Tau.BookIII.Computation.instBEqTTMConfig.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIII.Computation.instBEqTTMConfig`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L48-L48)
**instance
Tau.BookIII.Computation.instBEqTTMConfig :BEq TTMConfig**

Equations
- Tau.BookIII.Computation.instBEqTTMConfig = { beq := Tau.BookIII.Computation.instBEqTTMConfig.beq }

---

### `Tau.BookIII.Computation.ttm_step`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L50-L65)
**def
Tau.BookIII.Computation.ttm_step
(cfg : TTMConfig)
 :TTMConfig**


[III.D51] TTM transition: one step of computation at primorial level k.
The transition is a modular operation determined by the state.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.ttm_run`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L67-L74)
**def
Tau.BookIII.Computation.ttm_run
(cfg : TTMConfig)

(n : Denotation.TauIdx)
 :TTMConfig**


[III.D51] TTM multi-step: run n steps from initial configuration.
Equations
- Tau.BookIII.Computation.ttm_run cfg n = Tau.BookIII.Computation.ttm_run.go cfg n
Instances For

---

### `Tau.BookIII.Computation.ttm_run.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L71-L73)@[irreducible]

**def
Tau.BookIII.Computation.ttm_run.go
(c : TTMConfig)

(fuel : ℕ)
 :TTMConfig**

Equations
- Tau.BookIII.Computation.ttm_run.go c fuel = if fuel = 0 then c else Tau.BookIII.Computation.ttm_run.go (Tau.BookIII.Computation.ttm_step c) (fuel - 1)
Instances For

---

### `Tau.BookIII.Computation.ttm_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L76-L99)
**def
Tau.BookIII.Computation.ttm_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D51] TTM check: transitions preserve validity (registers stay
within primorial range).
Equations
- Tau.BookIII.Computation.ttm_check bound db = Tau.BookIII.Computation.ttm_check.go bound db 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Computation.ttm_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L81-L98)@[irreducible]

**def
Tau.BookIII.Computation.ttm_check.go
(bound db : Denotation.TauIdx)

(a b k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.ttm_nativity_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L105-L131)
**def
Tau.BookIII.Computation.ttm_nativity_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T30] TTM τ-nativity check: program IS τ-address. The machine's
transition function is determined by the registers themselves (no
external instruction tape). Code = data.
Equations
- Tau.BookIII.Computation.ttm_nativity_check bound db = Tau.BookIII.Computation.ttm_nativity_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Computation.ttm_nativity_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L111-L130)@[irreducible]

**def
Tau.BookIII.Computation.ttm_nativity_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.observable_width`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L137-L139)
**def
Tau.BookIII.Computation.observable_width :Denotation.TauIdx**


[III.D52] Observable width: the number of register bits visible at
each step. W = 1 + m where m = number of registers (here m = 2).
Equations
- Tau.BookIII.Computation.observable_width = 3
Instances For

---

### `Tau.BookIII.Computation.observable_transition_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L141-L165)
**def
Tau.BookIII.Computation.observable_transition_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D52] Observable transition check: the observable state at each
step is bounded by the Cook-Levin width.
Equations
- Tau.BookIII.Computation.observable_transition_check bound db = Tau.BookIII.Computation.observable_transition_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Computation.observable_transition_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L146-L164)@[irreducible]

**def
Tau.BookIII.Computation.observable_transition_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.ttm_5_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L181-L182)
**theorem
Tau.BookIII.Computation.ttm_5_3 :ttm_check 5 3 = true**


---

### `Tau.BookIII.Computation.ttm_nativity_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L184-L185)
**theorem
Tau.BookIII.Computation.ttm_nativity_10_3 :ttm_nativity_check 10 3 = true**


---

### `Tau.BookIII.Computation.observable_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L187-L188)
**theorem
Tau.BookIII.Computation.observable_10_3 :observable_transition_check 10 3 = true**


---

### `Tau.BookIII.Computation.ttm_preserves_depth`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L194-L198)
**theorem
Tau.BookIII.Computation.ttm_preserves_depth
(cfg : TTMConfig)
 :(ttm_step cfg).depth = cfg.depth**


[III.D51] Structural: TTM step preserves depth.

---

### `Tau.BookIII.Computation.ttm_depth_0`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L200-L202)
**theorem
Tau.BookIII.Computation.ttm_depth_0 :(ttm_step { state := 0, reg_a := 42, reg_b := 7, depth := 0 }).depth = 0**


[III.D51] Structural: TTM at depth 0 (Prim(0)=1, all ops mod 1).

---

### `Tau.BookIII.Computation.code_is_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L204-L206)
**theorem
Tau.BookIII.Computation.code_is_data :(ttm_step { state := 0, reg_a := 7, reg_b := 7, depth := 3 }).reg_a = (7 + 7) % 30**


[III.T30] Structural: code=data (self-application).

---

### `Tau.BookIII.Computation.obs_width`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/TowerMachine.lean#L208-L209)
**theorem
Tau.BookIII.Computation.obs_width :observable_width = 3**


[III.D52] Structural: observable width is 3.
