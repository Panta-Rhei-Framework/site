---
layout: taulib-doc
title: "TauLib.BookIII.Computation.E2Agent"
permalink: /verify/taulib/docs/book-iii-computation-e2agent/
lane: verify
module_name: "TauLib.BookIII.Computation.E2Agent"
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

# TauLib.BookIII.Computation.E2Agent


E₂ Computational Agent and Operational Closure.

## Registry Cross-References


- [III.D49] E₂ Computational Agent -- `E2Agent`, `e2_agent_check`

- [III.D50] Operational Closure -- `operational_closure_check`


## Mathematical Content


**III.D49 (E₂ Computational Agent):** A self-referential code+decoder structure
at E₂ level. An E₂ agent is a pair (C, D) where C is a τ-address (the code)
and D is a τ-address (the decoder). The agent cycle: C → D(C) → C' → D(C') → ...

**III.D50 (Operational Closure):** Programs operate on programs with no meta-level
escape required. D applied to C produces another valid code. The E₂ level is
"operationally closed" if every decoder applied to every code yields a valid output.

---

### `Tau.BookIII.Computation.E2Agent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L35-L41)
**structure
Tau.BookIII.Computation.E2Agent :Type**


[III.D49] E₂ agent: code + decoder pair. Both are τ-addresses at
some primorial depth. The decoder transforms codes into new codes.

- code : Denotation.TauIdx
- decoder : Denotation.TauIdx
- depth : Denotation.TauIdx
Instances For

---

### `Tau.BookIII.Computation.instReprE2Agent.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L41-L41)
**def
Tau.BookIII.Computation.instReprE2Agent.repr :E2Agent → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.instReprE2Agent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L41-L41)
**instance
Tau.BookIII.Computation.instReprE2Agent :Repr E2Agent**

Equations
- Tau.BookIII.Computation.instReprE2Agent = { reprPrec := Tau.BookIII.Computation.instReprE2Agent.repr }

---

### `Tau.BookIII.Computation.instDecidableEqE2Agent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L41-L41)
**instance
Tau.BookIII.Computation.instDecidableEqE2Agent :DecidableEq E2Agent**

Equations
- Tau.BookIII.Computation.instDecidableEqE2Agent = Tau.BookIII.Computation.instDecidableEqE2Agent.decEq

---

### `Tau.BookIII.Computation.instDecidableEqE2Agent.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L41-L41)
**def
Tau.BookIII.Computation.instDecidableEqE2Agent.decEq
(x✝ x✝¹ : E2Agent)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.instBEqE2Agent.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L41-L41)
**def
Tau.BookIII.Computation.instBEqE2Agent.beq :E2Agent → E2Agent → Bool**

Equations
- Tau.BookIII.Computation.instBEqE2Agent.beq { code := a, decoder := a_1, depth := a_2 }
 { code := b, decoder := b_1, depth := b_2 } = (a == b && (a_1 == b_1 && a_2 == b_2))
- Tau.BookIII.Computation.instBEqE2Agent.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIII.Computation.instBEqE2Agent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L41-L41)
**instance
Tau.BookIII.Computation.instBEqE2Agent :BEq E2Agent**

Equations
- Tau.BookIII.Computation.instBEqE2Agent = { beq := Tau.BookIII.Computation.instBEqE2Agent.beq }

---

### `Tau.BookIII.Computation.agent_step`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L43-L48)
**def
Tau.BookIII.Computation.agent_step
(a : E2Agent)
 :Denotation.TauIdx**


[III.D49] Apply the decoder to the code: D(C) at primorial level k.
The decoder operates by modular arithmetic on the code.
Equations
- Tau.BookIII.Computation.agent_step a = if (Tau.Polarity.primorial a.depth == 0) = true then 0 else (a.code + a.decoder) % Tau.Polarity.primorial a.depth
Instances For

---

### `Tau.BookIII.Computation.agent_iterate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L50-L60)
**def
Tau.BookIII.Computation.agent_iterate
(a : E2Agent)

(n : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D49] Agent iteration: apply the decoder n times.
Equations
- Tau.BookIII.Computation.agent_iterate a n = Tau.BookIII.Computation.agent_iterate.go a.code a.decoder a.depth n
Instances For

---

### `Tau.BookIII.Computation.agent_iterate.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L54-L59)@[irreducible]

**def
Tau.BookIII.Computation.agent_iterate.go
(code decoder depth fuel : ℕ)
 :Denotation.TauIdx**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.e2_agent_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L62-L85)
**def
Tau.BookIII.Computation.e2_agent_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D49] Agent well-formedness: code and decoder are valid addresses
(within primorial range).
Equations
- Tau.BookIII.Computation.e2_agent_check bound db = Tau.BookIII.Computation.e2_agent_check.go bound db 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Computation.e2_agent_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L67-L84)@[irreducible]

**def
Tau.BookIII.Computation.e2_agent_check.go
(bound db : Denotation.TauIdx)

(c d k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.operational_closure_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L91-L117)
**def
Tau.BookIII.Computation.operational_closure_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D50] Operational closure: decoder applied to any code produces
another valid code at the same depth.
Equations
- Tau.BookIII.Computation.operational_closure_check bound db = Tau.BookIII.Computation.operational_closure_check.go bound db 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Computation.operational_closure_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L96-L116)@[irreducible]

**def
Tau.BookIII.Computation.operational_closure_check.go
(bound db : Denotation.TauIdx)

(c d k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.cycle_detection_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L119-L138)
**def
Tau.BookIII.Computation.cycle_detection_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D50] Cycle detection: agent iteration eventually returns to start
(finite state space).
Equations
- Tau.BookIII.Computation.cycle_detection_check bound db = Tau.BookIII.Computation.cycle_detection_check.go bound db 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Computation.cycle_detection_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L124-L137)@[irreducible]

**def
Tau.BookIII.Computation.cycle_detection_check.go
(bound db : Denotation.TauIdx)

(c d k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Computation.e2_agent_5_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L154-L155)
**theorem
Tau.BookIII.Computation.e2_agent_5_3 :e2_agent_check 5 3 = true**


---

### `Tau.BookIII.Computation.operational_closure_5_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L157-L158)
**theorem
Tau.BookIII.Computation.operational_closure_5_3 :operational_closure_check 5 3 = true**


---

### `Tau.BookIII.Computation.cycle_detection_5_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L160-L161)
**theorem
Tau.BookIII.Computation.cycle_detection_5_3 :cycle_detection_check 5 3 = true**


---

### `Tau.BookIII.Computation.agent_step_depth_0`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L167-L169)
**theorem
Tau.BookIII.Computation.agent_step_depth_0 :agent_step { code := 42, decoder := 7, depth := 0 } = 0**


[III.D49] Structural: agent step at depth 0 is 0.

---

### `Tau.BookIII.Computation.agent_step_mod`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L171-L173)
**theorem
Tau.BookIII.Computation.agent_step_mod :agent_step { code := 7, decoder := 3, depth := 3 } = 10**


[III.D49] Structural: agent step is modular.

---

### `Tau.BookIII.Computation.identity_decoder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Computation/E2Agent.lean#L175-L177)
**theorem
Tau.BookIII.Computation.identity_decoder :agent_step { code := 7, decoder := 0, depth := 3 } = 7**


[III.D50] Structural: identity decoder (d=0) is a fixpoint.
