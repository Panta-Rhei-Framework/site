---
layout: taulib-doc
title: "TauLib.BookI.Polarity.OmegaRing"
permalink: /verify/taulib/docs/book-i-polarity-omega-ring/
lane: verify
module_name: "TauLib.BookI.Polarity.OmegaRing"
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

# TauLib.Polarity.OmegaRing


Stagewise ring operations on omega-tails with compatibility preservation.

## Registry Cross-References


- [I.D28] Boundary Local Ring — `mk_omega_tail_add`, `mk_omega_tail_mul`

- [I.D25] Omega-Tail — `Compatible_add`, `Compatible_mul`


## Ground Truth Sources


- chunk_0243_M002286: Boundary ring with levelwise addition/multiplication

- chunk_0314_M002691: Stagewise ring operations preserve compatibility


## Mathematical Content


The boundary ring ℤ̂_τ = lim Z/M_kZ carries componentwise ring operations:


- Addition: (x_k) + (y_k) = ((x_k + y_k) mod M_k)

- Multiplication: (x_k) · (y_k) = ((x_k · y_k) mod M_k)


Both operations preserve tower compatibility (the key structural theorem).
The proofs use: reduction_compat, Nat.add_mod / Nat.mul_mod, mod_mod_of_dvd.

---

### `Tau.Polarity.mk_omega_tail_add`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L55-L57)
**def
Tau.Polarity.mk_omega_tail_add
(n1 n2 d : Denotation.TauIdx)
 :OmegaTail**


Omega-tail addition via canonical embedding.
Equations
- Tau.Polarity.mk_omega_tail_add n1 n2 d = { depth := d, components := Tau.Polarity.omega_add_list✝ n1 n2 d, depth_eq := ⋯ }
Instances For

---

### `Tau.Polarity.omega_add_eq_reduce`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L75-L80)
**theorem
Tau.Polarity.omega_add_eq_reduce
(n1 n2 d i : Nat)

(hi : i < d)
 :(Tau.Polarity.omega_add_list✝ n1 n2 d).getD i 0 = reduce (n1 + n2) (i + 1)**


Bridge: componentwise addition equals global addition under reduce.

---

### `Tau.Polarity.Compatible_add`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L82-L92)
**theorem
Tau.Polarity.Compatible_add
(n1 n2 d : Denotation.TauIdx)
 :Compatible (mk_omega_tail_add n1 n2 d)**


Componentwise addition of canonical tails produces compatible towers.

---

### `Tau.Polarity.mk_omega_tail_mul`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L108-L110)
**def
Tau.Polarity.mk_omega_tail_mul
(n1 n2 d : Denotation.TauIdx)
 :OmegaTail**


Omega-tail multiplication via canonical embedding.
Equations
- Tau.Polarity.mk_omega_tail_mul n1 n2 d = { depth := d, components := Tau.Polarity.omega_mul_list✝ n1 n2 d, depth_eq := ⋯ }
Instances For

---

### `Tau.Polarity.omega_mul_eq_reduce`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L128-L133)
**theorem
Tau.Polarity.omega_mul_eq_reduce
(n1 n2 d i : Nat)

(hi : i < d)
 :(Tau.Polarity.omega_mul_list✝ n1 n2 d).getD i 0 = reduce (n1 * n2) (i + 1)**


Bridge: componentwise multiplication equals global multiplication under reduce.

---

### `Tau.Polarity.Compatible_mul`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L135-L145)
**theorem
Tau.Polarity.Compatible_mul
(n1 n2 d : Denotation.TauIdx)
 :Compatible (mk_omega_tail_mul n1 n2 d)**


Componentwise multiplication of canonical tails produces compatible towers.

---

### `Tau.Polarity.OmegaTail.add`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L151-L156)
**def
Tau.Polarity.OmegaTail.add
(t1 t2 : OmegaTail)

(_hd : t1.depth = t2.depth)
 :OmegaTail**


General componentwise addition of two omega-tails of equal depth.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.Compatible_add_general`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L167-L186)
**theorem
Tau.Polarity.Compatible_add_general
(t1 t2 : OmegaTail)

(hd : t1.depth = t2.depth)

(h1 : Compatible t1)

(h2 : Compatible t2)
 :Compatible (t1.add t2 hd)**


General compatibility preservation under addition.

---

### `Tau.Polarity.OmegaTail.mul`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L188-L193)
**def
Tau.Polarity.OmegaTail.mul
(t1 t2 : OmegaTail)

(_hd : t1.depth = t2.depth)
 :OmegaTail**


General componentwise multiplication of two omega-tails of equal depth.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.Compatible_mul_general`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L204-L223)
**theorem
Tau.Polarity.Compatible_mul_general
(t1 t2 : OmegaTail)

(hd : t1.depth = t2.depth)

(h1 : Compatible t1)

(h2 : Compatible t2)
 :Compatible (t1.mul t2 hd)**


General compatibility preservation under multiplication.

---

### `Tau.Polarity.mk_omega_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L229-L230)
**def
Tau.Polarity.mk_omega_zero
(d : Denotation.TauIdx)
 :OmegaTail**


Zero omega-tail: all components are 0 mod M_k = 0.
Equations
- Tau.Polarity.mk_omega_zero d = Tau.Polarity.mk_omega_tail 0 d
Instances For

---

### `Tau.Polarity.mk_omega_one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L232-L233)
**def
Tau.Polarity.mk_omega_one
(d : Denotation.TauIdx)
 :OmegaTail**


One omega-tail: all components are 1 mod M_k = 1 (for k ≥ 1).
Equations
- Tau.Polarity.mk_omega_one d = Tau.Polarity.mk_omega_tail 1 d
Instances For

---

### `Tau.Polarity.omega_zero_compat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L235-L237)
**theorem
Tau.Polarity.omega_zero_compat
(d : Denotation.TauIdx)
 :Compatible (mk_omega_zero d)**


Zero is compatible.

---

### `Tau.Polarity.omega_one_compat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L239-L241)
**theorem
Tau.Polarity.omega_one_compat
(d : Denotation.TauIdx)
 :Compatible (mk_omega_one d)**


One is compatible.

---

### `Tau.Polarity.omega_add_components_eq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L247-L259)
**theorem
Tau.Polarity.omega_add_components_eq
(n1 n2 d : Denotation.TauIdx)
 :(mk_omega_tail_add n1 n2 d).components = (mk_omega_tail (n1 + n2) d).components**


mk_omega_tail_add produces the same components as mk_omega_tail of the sum.
This is the master bridge: componentwise addition = global addition.

---

### `Tau.Polarity.omega_mul_components_eq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L261-L273)
**theorem
Tau.Polarity.omega_mul_components_eq
(n1 n2 d : Denotation.TauIdx)
 :(mk_omega_tail_mul n1 n2 d).components = (mk_omega_tail (n1 * n2) d).components**


mk_omega_tail_mul produces the same components as mk_omega_tail of the product.
This is the master bridge: componentwise multiplication = global multiplication.

---

### `Tau.Polarity.omega_add_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L277-L280)
**theorem
Tau.Polarity.omega_add_zero
(n d : Denotation.TauIdx)
 :(mk_omega_tail_add n 0 d).components = (mk_omega_tail n d).components**


Additive identity: n + 0 = n (on omega-tails).

---

### `Tau.Polarity.omega_mul_one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L282-L285)
**theorem
Tau.Polarity.omega_mul_one
(n d : Denotation.TauIdx)
 :(mk_omega_tail_mul n 1 d).components = (mk_omega_tail n d).components**


Multiplicative identity: n * 1 = n (on omega-tails).

---

### `Tau.Polarity.omega_add_comm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L287-L290)
**theorem
Tau.Polarity.omega_add_comm
(n1 n2 d : Denotation.TauIdx)
 :(mk_omega_tail_add n1 n2 d).components = (mk_omega_tail_add n2 n1 d).components**


Additive commutativity: n + m = m + n (on omega-tails).

---

### `Tau.Polarity.omega_mul_comm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L292-L295)
**theorem
Tau.Polarity.omega_mul_comm
(n1 n2 d : Denotation.TauIdx)
 :(mk_omega_tail_mul n1 n2 d).components = (mk_omega_tail_mul n2 n1 d).components**


Multiplicative commutativity: n * m = m * n (on omega-tails).

---

### `Tau.Polarity.omega_add_assoc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L297-L301)
**theorem
Tau.Polarity.omega_add_assoc
(n1 n2 n3 d : Denotation.TauIdx)
 :(mk_omega_tail_add (n1 + n2) n3 d).components = (mk_omega_tail_add n1 (n2 + n3) d).components**


Additive associativity: (a + b) + c = a + (b + c) (on omega-tails).

---

### `Tau.Polarity.omega_mul_assoc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L303-L307)
**theorem
Tau.Polarity.omega_mul_assoc
(n1 n2 n3 d : Denotation.TauIdx)
 :(mk_omega_tail_mul (n1 * n2) n3 d).components = (mk_omega_tail_mul n1 (n2 * n3) d).components**


Multiplicative associativity: (a * b) * c = a * (b * c) (on omega-tails).

---

### `Tau.Polarity.omega_left_distrib`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L309-L313)
**theorem
Tau.Polarity.omega_left_distrib
(n1 n2 n3 d : Denotation.TauIdx)
 :(mk_omega_tail_mul n1 (n2 + n3) d).components = (mk_omega_tail_add (n1 * n2) (n1 * n3) d).components**


Distributivity: a * (b + c) = a*b + a*c (on omega-tails).

---

### `Tau.Polarity.add_zero_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L319-L321)
**def
Tau.Polarity.add_zero_check
(n d : Denotation.TauIdx)
 :Bool**


Check: n + 0 = n (additive identity).
Equations
- Tau.Polarity.add_zero_check n d = ((Tau.Polarity.mk_omega_tail_add n 0 d).components == (Tau.Polarity.mk_omega_tail n d).components)
Instances For

---

### `Tau.Polarity.mul_one_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L323-L325)
**def
Tau.Polarity.mul_one_check
(n d : Denotation.TauIdx)
 :Bool**


Check: n * 1 = n (multiplicative identity).
Equations
- Tau.Polarity.mul_one_check n d = ((Tau.Polarity.mk_omega_tail_mul n 1 d).components == (Tau.Polarity.mk_omega_tail n d).components)
Instances For

---

### `Tau.Polarity.add_comm_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L327-L329)
**def
Tau.Polarity.add_comm_check
(n1 n2 d : Denotation.TauIdx)
 :Bool**


Check: n + m = m + n (additive commutativity).
Equations
- Tau.Polarity.add_comm_check n1 n2 d = ((Tau.Polarity.mk_omega_tail_add n1 n2 d).components == (Tau.Polarity.mk_omega_tail_add n2 n1 d).components)
Instances For

---

### `Tau.Polarity.mul_comm_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Polarity/OmegaRing.lean#L331-L333)
**def
Tau.Polarity.mul_comm_check
(n1 n2 d : Denotation.TauIdx)
 :Bool**


Check: n * m = m * n (multiplicative commutativity).
Equations
- Tau.Polarity.mul_comm_check n1 n2 d = ((Tau.Polarity.mk_omega_tail_mul n1 n2 d).components == (Tau.Polarity.mk_omega_tail_mul n2 n1 d).components)
Instances For
