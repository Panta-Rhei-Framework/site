---
layout: taulib-doc
title: "TauLib.BookI.Boundary.Ring"
permalink: /verify/taulib/docs/book-i-boundary-ring/
lane: verify
module_name: "TauLib.BookI.Boundary.Ring"
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

# TauLib.Boundary.Ring


Boundary ring negation and the full ring axiom suite for omega-tails.

## Registry Cross-References


- [I.D28] Boundary Local Ring — `BdryRing`, `mk_omega_tail_neg`


## Ground Truth Sources


- chunk_0243_M002286: Boundary ring with levelwise addition/multiplication

- chunk_0314_M002691: Negation, additive inverse, ring axiom collection


## Mathematical Content


The boundary ring Z_hat_tau = lim Z/M_kZ carries componentwise ring operations.
This module extends OmegaRing with:


- Negation: neg(x)_k = (M_k - x_k) mod M_k

- Additive inverse: x + neg(x) = 0

- Double negation: neg(neg(x)) = x

- Full ring axiom collection: add_comm, add_assoc, add_zero, add_neg,
mul_comm, mul_assoc, mul_one, left_distrib


---

### `Tau.Boundary.BdryRing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Ring.lean#L37-L38)@[reducible, inline]

**abbrev
Tau.Boundary.BdryRing :Type**


Boundary ring element: an omega-tail in the primorial tower.
Equations
- Tau.Boundary.BdryRing = Tau.Polarity.OmegaTail
Instances For

---

### `Tau.Boundary.mk_omega_tail_neg`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Ring.lean#L129-L133)
**def
Tau.Boundary.mk_omega_tail_neg
(n d : Denotation.TauIdx)
 :Polarity.OmegaTail**


Omega-tail negation via canonical embedding.
Equations
- Tau.Boundary.mk_omega_tail_neg n d = { depth := d, components := Tau.Boundary.omega_neg_list✝ n d, depth_eq := ⋯ }
Instances For

---

### `Tau.Boundary.omega_neg_components_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Ring.lean#L163-L176)
**theorem
Tau.Boundary.omega_neg_components_eq
(n d : Denotation.TauIdx)
 :(mk_omega_tail_neg n d).components = (Polarity.mk_omega_tail ((Polarity.primorial d - n % Polarity.primorial d) % Polarity.primorial d) d).components**


Bridge: componentwise negation produces the negation representative at each stage.

---

### `Tau.Boundary.Compatible_neg`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Ring.lean#L182-L194)
**theorem
Tau.Boundary.Compatible_neg
(n d : Denotation.TauIdx)
 :Polarity.Compatible (mk_omega_tail_neg n d)**


Negation of canonical tails is compatible.

---

### `Tau.Boundary.omega_neg_neg_eq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Ring.lean#L213-L225)
**theorem
Tau.Boundary.omega_neg_neg_eq
(n d : Denotation.TauIdx)

(i : ℕ)
 :i < d →
 (Tau.Boundary.omega_neg_list✝ ((Polarity.primorial d - n % Polarity.primorial d) % Polarity.primorial d) d).getD i 0 = (Polarity.mk_omega_tail n d).components.getD i 0**


Double negation is identity: neg(neg(n)) has the same components as n.

---

### `Tau.Boundary.omega_add_neg_cancel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Ring.lean#L244-L263)
**theorem
Tau.Boundary.omega_add_neg_cancel
(n d : Denotation.TauIdx)

(i : ℕ)
 :i < d →
 (Polarity.mk_omega_tail_add n ((Polarity.primorial d - n % Polarity.primorial d) % Polarity.primorial d)
 d).components.getD
 i 0 = (Polarity.mk_omega_zero d).components.getD i 0**


Additive inverse: n + neg(n) = 0 (on components).

---

### `Tau.Boundary.bdry_ring_axioms`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Ring.lean#L269-L292)
**theorem
Tau.Boundary.bdry_ring_axioms :(∀ (n1 n2 d : Denotation.TauIdx),
 (Polarity.mk_omega_tail_add n1 n2 d).components = (Polarity.mk_omega_tail_add n2 n1 d).components) ∧ (∀ (n1 n2 n3 d : Denotation.TauIdx),
 (Polarity.mk_omega_tail_add (n1 + n2) n3 d).components = (Polarity.mk_omega_tail_add n1 (n2 + n3) d).components) ∧ (∀ (n d : Denotation.TauIdx),
 (Polarity.mk_omega_tail_add n 0 d).components = (Polarity.mk_omega_tail n d).components) ∧ (∀ (n d : Denotation.TauIdx) (i : ℕ),
 i < d →
 (Polarity.mk_omega_tail_add n ((Polarity.primorial d - n % Polarity.primorial d) % Polarity.primorial d)
 d).components.getD
 i 0 = (Polarity.mk_omega_zero d).components.getD i 0) ∧ (∀ (n1 n2 d : Denotation.TauIdx),
 (Polarity.mk_omega_tail_mul n1 n2 d).components = (Polarity.mk_omega_tail_mul n2 n1 d).components) ∧ (∀ (n1 n2 n3 d : Denotation.TauIdx),
 (Polarity.mk_omega_tail_mul (n1 * n2) n3 d).components = (Polarity.mk_omega_tail_mul n1 (n2 * n3) d).components) ∧ (∀ (n d : Denotation.TauIdx),
 (Polarity.mk_omega_tail_mul n 1 d).components = (Polarity.mk_omega_tail n d).components) ∧ ∀ (n1 n2 n3 d : Denotation.TauIdx),
 (Polarity.mk_omega_tail_mul n1 (n2 + n3) d).components = (Polarity.mk_omega_tail_add (n1 * n2) (n1 * n3) d).components**


Full boundary ring axioms: all eight ring properties, proved universally.

---

### `Tau.Boundary.neg_compat_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Ring.lean#L298-L299)
**def
Tau.Boundary.neg_compat_check
(n d : Denotation.TauIdx)
 :Bool**

Equations
- Tau.Boundary.neg_compat_check n d = Tau.Polarity.compat_check (Tau.Boundary.mk_omega_tail_neg n d)
Instances For

---

### `Tau.Boundary.add_neg_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Ring.lean#L301-L303)
**def
Tau.Boundary.add_neg_check
(n d : Denotation.TauIdx)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.double_neg_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Boundary/Ring.lean#L305-L308)
**def
Tau.Boundary.double_neg_check
(n d : Denotation.TauIdx)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For
