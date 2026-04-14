---
layout: taulib-doc
title: "TauLib.BookI.Denotation.Order"
permalink: /verify/taulib/docs/book-i-denotation-order/
lane: verify
module_name: "TauLib.BookI.Denotation.Order"
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

# TauLib.Denotation.Order


Denotational ordering on Obj(τ): lexicographic on (seed.toNat, depth).

## Registry Cross-References


- [I.D16a] Denotational Order — `denotational_lt`

- [I.P07] Well-Ordering — `denotational_lt_wf`


## Mathematical Content


The denotational order is lexicographic:


- First compare seed indices (α=0 < π=1 < γ=2 < η=3 < ω=4)

- Then compare depths within the same seed


This gives a well-ordering of type ω·4 + ω (four copies of ω for the
orbit rays, plus one copy for the omega fiber).

---

### `Tau.Denotation.denotational_lt`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Order.lean#L39-L42)
**def
Tau.Denotation.denotational_lt
(x y : Kernel.TauObj)
 :Prop**


[I.D16a] Denotational strict order: lexicographic on (seed.toNat, depth).
Equations
- Tau.Denotation.denotational_lt x y = (x.seed.toNat < y.seed.toNat ∨ x.seed = y.seed ∧ x.depth < y.depth)
Instances For

---

### `Tau.Denotation.denotational_lt_decidable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Order.lean#L44-L46)
**instance
Tau.Denotation.denotational_lt_decidable
(x y : Kernel.TauObj)
 :Decidable (denotational_lt x y)**


Decidability of the denotational order.
Equations
- Tau.Denotation.denotational_lt_decidable x y = inferInstanceAs (Decidable (x.seed.toNat < y.seed.toNat ∨ x.seed = y.seed ∧ x.depth < y.depth))

---

### `Tau.Denotation.denotational_lt_irrefl`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Order.lean#L52-L57)
**theorem
Tau.Denotation.denotational_lt_irrefl
(x : Kernel.TauObj)
 :¬denotational_lt x x**


Irreflexivity.

---

### `Tau.Denotation.denotational_lt_trans`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Order.lean#L59-L71)
**theorem
Tau.Denotation.denotational_lt_trans
{x y z : Kernel.TauObj}

(h1 : denotational_lt x y)

(h2 : denotational_lt y z)
 :denotational_lt x z**


Transitivity.

---

### `Tau.Denotation.denotational_lt_trichotomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Order.lean#L73-L93)
**theorem
Tau.Denotation.denotational_lt_trichotomy
(x y : Kernel.TauObj)
 :denotational_lt x y ∨ x = y ∨ denotational_lt y x**


Trichotomy: for any two TauObj, exactly one of <, =, > holds.

---

### `Tau.Denotation.alpha_zero_minimum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Order.lean#L99-L113)
**theorem
Tau.Denotation.alpha_zero_minimum
(x : Kernel.TauObj)

(hx : x ≠ { seed := Kernel.Generator.alpha, depth := 0 })
 :denotational_lt { seed := Kernel.Generator.alpha, depth := 0 } x**


⟨α, 0⟩ is the minimum element.

---

### `Tau.Denotation.orbit_depth_order`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Order.lean#L115-L118)
**theorem
Tau.Denotation.orbit_depth_order
(g : Kernel.Generator)

(n m : Nat)

(h : n < m)
 :denotational_lt { seed := g, depth := n } { seed := g, depth := m }**


Within each orbit ray, depth gives a total order.

---

### `Tau.Denotation.seed_order_alpha_pi`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Order.lean#L120-L122)
**theorem
Tau.Denotation.seed_order_alpha_pi :denotational_lt { seed := Kernel.Generator.alpha, depth := 0 } { seed := Kernel.Generator.pi, depth := 0 }**


Different seeds have a definite order.

---

### `Tau.Denotation.seed_order_pi_gamma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Order.lean#L124-L125)
**theorem
Tau.Denotation.seed_order_pi_gamma :denotational_lt { seed := Kernel.Generator.pi, depth := 0 } { seed := Kernel.Generator.gamma, depth := 0 }**


---

### `Tau.Denotation.seed_order_gamma_eta`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Order.lean#L127-L128)
**theorem
Tau.Denotation.seed_order_gamma_eta :denotational_lt { seed := Kernel.Generator.gamma, depth := 0 } { seed := Kernel.Generator.eta, depth := 0 }**


---

### `Tau.Denotation.seed_order_eta_omega`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Order.lean#L130-L131)
**theorem
Tau.Denotation.seed_order_eta_omega :denotational_lt { seed := Kernel.Generator.eta, depth := 0 } { seed := Kernel.Generator.omega, depth := 0 }**


---

### `Tau.Denotation.denotational_lt_wf`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Denotation/Order.lean#L151-L157)
**theorem
Tau.Denotation.denotational_lt_wf :WellFounded denotational_lt**


[I.P07] Well-foundedness of the denotational order:
denotational_lt is a subrelation of the lexicographic order on (Nat, Nat),
which is well-founded since Nat is well-ordered.
