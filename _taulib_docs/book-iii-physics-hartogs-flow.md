---
layout: taulib-doc
title: "TauLib.BookIII.Physics.HartogsFlow"
permalink: /verify/taulib/docs/book-iii-physics-hartogs-flow/
lane: verify
module_name: "TauLib.BookIII.Physics.HartogsFlow"
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

# TauLib.BookIII.Physics.HartogsFlow


Hartogs Flow Operator, Flow Theorem, and Polarity Swap.

## Registry Cross-References


- [III.D40] Hartogs Flow Operator -- `hartogs_flow_step`, `flow_check`

- [III.T24] Flow Theorem -- `flow_stabilization_check`

- [III.D41] Polarity Swap -- `polarity_swap`, `polarity_swap_check`


## Mathematical Content


**III.D40 (Hartogs Flow Operator):** At primorial level k, the Hartogs flow
Φ_k: FluidData → FluidData sends each cylinder's BNF to the BNF of the
CRT-reconstructed value at the next level. The flow enriches the E₀→E₁
transition: it is a semigroup action on fluid data preserving sector structure.

**III.T24 (Flow Theorem):** The Hartogs flow stabilizes: for each fluid
datum f, there exists k₀ such that Φ_k(f) = Φ_{k₀}(f) for all k ≥ k₀.
This is the existence theorem for Navier-Stokes in τ.

**III.D41 (Polarity Swap):** The flow has a natural involution σ that swaps
B and C sectors. Combined with the functional equation involution J,
this gives σ·J = id on the spectral side.

---

### `Tau.BookIII.Physics.hartogs_flow_step`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L41-L55)
**def
Tau.BookIII.Physics.hartogs_flow_step
(x k : Denotation.TauIdx)
 :Spectral.BoundaryNF**


[III.D40] Hartogs flow step: advance fluid data from level k to k+1.
Each cylinder's value at level k is lifted to level k+1 by CRT
reconstruction, then re-decomposed into BNF at the new level.
The flow preserves sector structure while refining resolution.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.flow_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L57-L83)
**def
Tau.BookIII.Physics.flow_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D40] Flow coherence check: the flow step preserves the value
mod the original primorial (tower compatibility).
Equations
- Tau.BookIII.Physics.flow_check bound db = Tau.BookIII.Physics.flow_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Physics.flow_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L62-L82)@[irreducible]

**def
Tau.BookIII.Physics.flow_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.flow_semigroup_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L85-L105)
**def
Tau.BookIII.Physics.flow_semigroup_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D40] Semigroup projection check: applying the flow at level k,
then projecting back to level k, recovers the original value.
This is the tower-projection semigroup property: π_k ∘ Φ_k = id.
Equations
- Tau.BookIII.Physics.flow_semigroup_check bound db = Tau.BookIII.Physics.flow_semigroup_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Physics.flow_semigroup_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L91-L104)@[irreducible]

**def
Tau.BookIII.Physics.flow_semigroup_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.flow_stabilization_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L111-L130)
**def
Tau.BookIII.Physics.flow_stabilization_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T24] Flow stabilization check: at each level k, the flow does
not introduce new defects. The defect functional stays at zero
across all levels (canonical BNF is a fixed point of the flow).
Equations
- Tau.BookIII.Physics.flow_stabilization_check bound db = Tau.BookIII.Physics.flow_stabilization_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Physics.flow_stabilization_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L117-L129)@[irreducible]

**def
Tau.BookIII.Physics.flow_stabilization_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.causal_arrow_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L132-L147)
**def
Tau.BookIII.Physics.causal_arrow_check
(db : Denotation.TauIdx)
 :Bool**


[III.T24] Causal arrow: the flow is irreversible at the B/C boundary.
B-part and C-part grow at different rates, creating a natural time arrow.
Equations
- Tau.BookIII.Physics.causal_arrow_check db = Tau.BookIII.Physics.causal_arrow_check.go db 2 (db + 1)
Instances For

---

### `Tau.BookIII.Physics.causal_arrow_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L137-L146)@[irreducible]

**def
Tau.BookIII.Physics.causal_arrow_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.polarity_swap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L153-L157)
**def
Tau.BookIII.Physics.polarity_swap
(nf : Spectral.BoundaryNF)
 :Spectral.BoundaryNF**


[III.D41] Polarity swap: exchange B-part and C-part of a BNF.
This is the physics-level version of the functional equation
involution J from Part IV. σ(b, c, x) = (c, b, x).
Equations
- Tau.BookIII.Physics.polarity_swap nf = { b_part := nf.c_part, c_part := nf.b_part, x_part := nf.x_part, depth := nf.depth }
Instances For

---

### `Tau.BookIII.Physics.polarity_swap_involutive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L159-L162)
**theorem
Tau.BookIII.Physics.polarity_swap_involutive
(nf : Spectral.BoundaryNF)
 :polarity_swap (polarity_swap nf) = nf**


[III.D41] Polarity swap is involutive: σ² = id.

---

### `Tau.BookIII.Physics.polarity_swap_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L164-L189)
**def
Tau.BookIII.Physics.polarity_swap_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D41] Polarity swap check: swapping and summing gives the same
total as the original BNF.
Equations
- Tau.BookIII.Physics.polarity_swap_check bound db = Tau.BookIII.Physics.polarity_swap_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Physics.polarity_swap_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L169-L188)@[irreducible]

**def
Tau.BookIII.Physics.polarity_swap_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Physics.flow_15_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L205-L206)
**theorem
Tau.BookIII.Physics.flow_15_4 :flow_check 15 4 = true**


---

### `Tau.BookIII.Physics.flow_semigroup_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L208-L209)
**theorem
Tau.BookIII.Physics.flow_semigroup_10_3 :flow_semigroup_check 10 3 = true**


---

### `Tau.BookIII.Physics.flow_stabilization_15_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L211-L212)
**theorem
Tau.BookIII.Physics.flow_stabilization_15_4 :flow_stabilization_check 15 4 = true**


---

### `Tau.BookIII.Physics.causal_arrow_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L214-L215)
**theorem
Tau.BookIII.Physics.causal_arrow_5 :causal_arrow_check 5 = true**


---

### `Tau.BookIII.Physics.polarity_swap_15_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L217-L218)
**theorem
Tau.BookIII.Physics.polarity_swap_15_4 :polarity_swap_check 15 4 = true**


---

### `Tau.BookIII.Physics.flow_depth_0`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L224-L226)
**theorem
Tau.BookIII.Physics.flow_depth_0 :hartogs_flow_step 42 0 = { b_part := 0, c_part := 0, x_part := 0, depth := 1 }**


[III.D40] Structural: flow at depth 0 produces trivial BNF.

---

### `Tau.BookIII.Physics.swap_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L228-L230)
**theorem
Tau.BookIII.Physics.swap_zero :polarity_swap { b_part := 0, c_part := 0, x_part := 0, depth := 3 } = { b_part := 0, c_part := 0, x_part := 0, depth := 3 }**


[III.D41] Structural: polarity swap of zero is zero.

---

### `Tau.BookIII.Physics.flow_stable_1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Physics/HartogsFlow.lean#L232-L234)
**theorem
Tau.BookIII.Physics.flow_stable_1 :flow_stabilization_check 10 1 = true**


[III.T24] Structural: flow stabilization at depth 1.
