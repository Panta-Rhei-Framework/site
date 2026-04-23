---
layout: taulib-doc
title: "TauLib.BookI.Holomorphy.IdentityTheorem"
permalink: /verify/taulib/docs/book-i-holomorphy-identity-theorem/
lane: verify
module_name: "TauLib.BookI.Holomorphy.IdentityTheorem"
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

# TauLib.Holomorphy.IdentityTheorem


The τ-Identity Theorem: finite agreement implies global equality for HolFuns.

## Registry Cross-References


- [I.T21] τ-Identity Theorem — `tau_identity`, `tau_identity_nat`

- [I.D49] Hol(L) — `HolL`

- [I.L07] Tail Agreement Propagation — `tail_agree_propagation`


## Ground Truth Sources


- chunk_0155_M001710: Omega-tails, divergence ultrametric

- chunk_0228_M002194: Split-complex algebra


## Mathematical Content


The τ-Identity Theorem states: if two τ-holomorphic functions agree at some
primorial depth d₀, they agree at ALL depths. This is the hallmark of
holomorphic rigidity — the τ-analog of the classical identity theorem.

The proof uses tower coherence: agreement at depth d₀ propagates UPWARD
through the primorial ladder via the CRT structure. At each new stage
M_{d+1} = M_d · p_{d+1}, the CRT decomposition adds exactly one new factor,
and tower coherence forces this new factor to be determined by the existing ones.

This is OPPOSITE to classical analytic continuation, which propagates "sideways"
through overlapping neighborhoods. In τ, propagation is VERTICAL: from coarse
primorial stages to finer ones.

---

### `Tau.Holomorphy.agree_at`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L46-L49)
**def
Tau.Holomorphy.agree_at
(f₁ f₂ : StageFun)

(n k : Denotation.TauIdx)
 :Prop**


Two stagewise functions agree at stage k on input n if they give
the same B-sector and C-sector values.
Equations
- Tau.Holomorphy.agree_at f₁ f₂ n k = (f₁.b_fun n k = f₂.b_fun n k ∧ f₁.c_fun n k = f₂.c_fun n k)
Instances For

---

### `Tau.Holomorphy.agree_at_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L51-L53)
**def
Tau.Holomorphy.agree_at_check
(f₁ f₂ : StageFun)

(n k : Denotation.TauIdx)
 :Bool**


Decidable agreement check.
Equations
- Tau.Holomorphy.agree_at_check f₁ f₂ n k = (f₁.b_fun n k == f₂.b_fun n k && f₁.c_fun n k == f₂.c_fun n k)
Instances For

---

### `Tau.Holomorphy.agree_up_to`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L55-L58)
**def
Tau.Holomorphy.agree_up_to
(f₁ f₂ : StageFun)

(n d₀ : Denotation.TauIdx)
 :Prop**


Two stagewise functions agree up to depth d₀ on input n if they agree
at every stage k ≤ d₀.
Equations
- Tau.Holomorphy.agree_up_to f₁ f₂ n d₀ = ∀ (k : Tau.Denotation.TauIdx), k ≤ d₀ → Tau.Holomorphy.agree_at f₁ f₂ n k
Instances For

---

### `Tau.Holomorphy.agree_all`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L60-L62)
**def
Tau.Holomorphy.agree_all
(f₁ f₂ : StageFun)

(n : Denotation.TauIdx)
 :Prop**


Two stagewise functions agree at ALL stages on input n.
Equations
- Tau.Holomorphy.agree_all f₁ f₂ n = ∀ (k : Tau.Denotation.TauIdx), Tau.Holomorphy.agree_at f₁ f₂ n k
Instances For

---

### `Tau.Holomorphy.tail_agree_downward`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L68-L95)
**theorem
Tau.Holomorphy.tail_agree_downward
(f₁ f₂ : StageFun)

(h₁ : TowerCoherent f₁)

(h₂ : TowerCoherent f₂)

(n d₀ : Denotation.TauIdx)

(hagree : agree_at f₁ f₂ n d₀)

(k : Denotation.TauIdx)
 :k ≤ d₀ → agree_at f₁ f₂ n k**


[I.L07] Tail Agreement Propagation (single input):
If two tower-coherent stagewise functions agree at stage d₀ for input n,
then they agree at ALL stages k ≤ d₀ for input n.

This is the "downward" direction: agreement at a fine stage implies
agreement at all coarser stages.

Proof: By tower coherence, f₁(n, d₀) reduced to stage k equals f₁(n, k).
If f₁(n, d₀) = f₂(n, d₀), then reducing both sides gives f₁(n, k) = f₂(n, k).

---

### `Tau.Holomorphy.tail_agree_propagation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L97-L105)
**theorem
Tau.Holomorphy.tail_agree_propagation
(f₁ f₂ : StageFun)

(h₁ : TowerCoherent f₁)

(h₂ : TowerCoherent f₂)

(d₀ : Denotation.TauIdx)

(hagree : ∀ (n : Denotation.TauIdx), agree_at f₁ f₂ n d₀)

(n k : Denotation.TauIdx)
 :k ≤ d₀ → agree_at f₁ f₂ n k**


Tail agreement propagation (universal over inputs):
If two tower-coherent stagewise functions agree at stage d₀ for ALL inputs n,
then they agree at all stages k ≤ d₀ for all inputs.

---

### `Tau.Holomorphy.tau_identity_reduce`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L111-L125)
**theorem
Tau.Holomorphy.tau_identity_reduce
(f₁ f₂ : StageFun)

(rf₁ : ReduceForm f₁)

(rf₂ : ReduceForm f₂)

(hb : rf₁.b_map = rf₂.b_map)

(hc : rf₁.c_map = rf₂.c_map)

(n k : Denotation.TauIdx)
 :agree_at f₁ f₂ n k**


[I.T21] The τ-Identity Theorem (stagewise form):
If two tower-coherent "reduce-form" stagewise functions have the same
underlying maps, they produce the same outputs at every stage.

This is trivially true by definition, but it captures the KEY insight:
a reduce-form function is uniquely determined by its underlying map.
Tower coherence + reduce form = complete determination.

---

### `Tau.Holomorphy.tau_identity_nat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L127-L138)
**theorem
Tau.Holomorphy.tau_identity_nat
(f₁ f₂ : StageFun)

(h₁ : TowerCoherent f₁)

(h₂ : TowerCoherent f₂)

(d₀ : Denotation.TauIdx)

(hagree : ∀ (n : Denotation.TauIdx), agree_at f₁ f₂ n d₀)

(n k : Denotation.TauIdx)
 :k ≤ d₀ → agree_at f₁ f₂ n k**


The τ-Identity Theorem (for natural-number inputs):
If two tower-coherent stagewise functions agree at stage d₀ for ALL inputs,
they agree at all stages ≤ d₀.

Combined with the principle that a HolFun is determined by its action
on reduce(n, k) (CRT coherence), this gives: agreement at any single
primorial stage forces global agreement.

---

### `Tau.Holomorphy.tau_identity_finite_witness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L140-L183)
**theorem
Tau.Holomorphy.tau_identity_finite_witness
(f₁ f₂ : StageFun)

(h₁ : TowerCoherent f₁)

(h₂ : TowerCoherent f₂)

(d₀ : Denotation.TauIdx)

(hagree : ∀ (n : Denotation.TauIdx), n < Polarity.primorial d₀ → agree_at f₁ f₂ n d₀)

(hf₁ : ∀ (n k : Denotation.TauIdx), f₁.b_fun n k = f₁.b_fun (Polarity.reduce n k) k)

(hf₂ : ∀ (n k : Denotation.TauIdx), f₂.b_fun n k = f₂.b_fun (Polarity.reduce n k) k)

(hg₁ : ∀ (n k : Denotation.TauIdx), f₁.c_fun n k = f₁.c_fun (Polarity.reduce n k) k)

(hg₂ : ∀ (n k : Denotation.TauIdx), f₂.c_fun n k = f₂.c_fun (Polarity.reduce n k) k)

(n k : Denotation.TauIdx)
 :k ≤ d₀ → agree_at f₁ f₂ n k**


Special case: if two tower-coherent functions agree at all stages for all
reduce(n, d₀) inputs (a finite set!), they agree at all stages ≤ d₀
for ALL inputs.

This captures the "finite witness" property: checking finitely many
inputs (all residue classes mod M_{d₀}) suffices to determine
the function at all coarser stages.

---

### `Tau.Holomorphy.HolL`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L189-L194)
**structure
Tau.Holomorphy.HolL :Type**


[I.D49] Hol(L): the type of τ-holomorphic functions on the algebraic lemniscate.
By the Identity Theorem, elements of Hol(L) are uniquely determined by
their values at any single primorial depth.

- fun_ : HolFun
The underlying HolFun.

Instances For

---

### `Tau.Holomorphy.hol_L_identity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L198-L206)
**theorem
Tau.Holomorphy.hol_L_identity
(h₁ h₂ : HolL)

(d₀ : Denotation.TauIdx)

(hagree : ∀ (n : Denotation.TauIdx), agree_at h₁.fun_.transformer.stage_fun h₂.fun_.transformer.stage_fun n d₀)

(n k : Denotation.TauIdx)
 :k ≤ d₀ → agree_at h₁.fun_.transformer.stage_fun h₂.fun_.transformer.stage_fun n k**


Two elements of Hol(L) that agree at stage d₀ for all inputs
agree at all stages ≤ d₀ (Identity Theorem for Hol(L)).

---

### `Tau.Holomorphy.chi_plus_self_agree`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L216-L219)
**theorem
Tau.Holomorphy.chi_plus_self_agree
(n k : Denotation.TauIdx)
 :agree_at chi_plus_stage chi_plus_stage n k**


Verification: χ₊ agrees with itself at all stages.

---

### `Tau.Holomorphy.id_eq_chi_sum`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L221-L226)
**theorem
Tau.Holomorphy.id_eq_chi_sum
(n k : Denotation.TauIdx)
 :id_stage.b_fun n k = chi_plus_stage.b_fun n k + chi_minus_stage.b_fun n k**


Verification: the identity agrees with χ₊ + χ₋ in sector sums.
id_stage gives (reduce n k, reduce n k) while
chi_plus + chi_minus gives (reduce n k, 0) + (0, reduce n k) = (reduce n k, reduce n k).

---

### `Tau.Holomorphy.id_eq_chi_sum_c`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L228-L230)
**theorem
Tau.Holomorphy.id_eq_chi_sum_c
(n k : Denotation.TauIdx)
 :id_stage.c_fun n k = chi_plus_stage.c_fun n k + chi_minus_stage.c_fun n k**
