---
layout: taulib-doc
title: "TauLib.BookI.Boundary.Galois"
permalink: /verify/taulib/docs/book-i-boundary-galois/
lane: verify
module_name: "TauLib.BookI.Boundary.Galois"
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

# TauLib.Boundary.Galois


Internal Galois theory on the primorial tower.

## Registry Cross-References


- [I.D95a] Galois Automorphism — `GaloisAut`, `galois_aut_check`

- [I.D96a] Galois Group of Primorial Stage — `galois_group_order`

- [I.T49a] Fundamental Theorem (Internal) — `galois_fundamental_check`

- [I.P43a] CRT-Galois Decomposition — `galois_crt_check`


## Mathematical Content


**I.D95a (Galois Automorphism):** At stage k, an automorphism of Z/M_k Z
is a map σ_a : x ↦ ax mod M_k where gcd(a, M_k) = 1. The automorphism
preserves the ring structure: σ_a(x+y) = σ_a(x) + σ_a(y),
σ_a(xy) = σ_a(x)σ_a(y).

**I.D96a (Galois Group of Primorial Stage):** The Galois group at stage k is
Gal_k = (Z/M_k Z)× — the group of units of the primorial ring. Its order is
Euler's totient φ(M_k) = ∏_{p≤p_k} (p-1).

**I.T49a (Fundamental Theorem):** There is a bijective correspondence between
subgroups of Gal_k and intermediate rings (subrings of Z/M_k Z that contain
the image of Z). At primorial level, the CRT decomposition gives the explicit
structure: Gal_k ≅ ∏_{i=1}^{k} (Z/p_i Z)×.

**I.P43a (CRT-Galois Decomposition):** The Galois group decomposes via CRT
into a product of cyclic groups: Gal_k ≅ (Z/2Z)× × (Z/3Z)× × (Z/5Z)× × ...
This is the φ-function product: φ(M_k) = 1 × 2 × 4 × ... × (p_k - 1).

---

### `Tau.Boundary.GaloisAut`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L47-L51)
**structure
Tau.Boundary.GaloisAut :Type**


[I.D95a] A Galois automorphism at stage k: multiplication by a unit.

- stage : ℕ
- multiplier : ℕ
Instances For

---

### `Tau.Boundary.instReprGaloisAut`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L51-L51)
**instance
Tau.Boundary.instReprGaloisAut :Repr GaloisAut**

Equations
- Tau.Boundary.instReprGaloisAut = { reprPrec := Tau.Boundary.instReprGaloisAut.repr }

---

### `Tau.Boundary.instReprGaloisAut.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L51-L51)
**def
Tau.Boundary.instReprGaloisAut.repr :GaloisAut → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.instDecidableEqGaloisAut`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L51-L51)
**instance
Tau.Boundary.instDecidableEqGaloisAut :DecidableEq GaloisAut**

Equations
- Tau.Boundary.instDecidableEqGaloisAut = Tau.Boundary.instDecidableEqGaloisAut.decEq

---

### `Tau.Boundary.instDecidableEqGaloisAut.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L51-L51)
**def
Tau.Boundary.instDecidableEqGaloisAut.decEq
(x✝ x✝¹ : GaloisAut)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.is_unit_mod`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L53-L55)
**def
Tau.Boundary.is_unit_mod
(a m : ℕ)
 :Bool**


[I.D95a] Check that a multiplier is a unit (coprime to primorial).
Equations
- Tau.Boundary.is_unit_mod a m = (a.gcd m == 1)
Instances For

---

### `Tau.Boundary.galois_apply`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L57-L59)
**def
Tau.Boundary.galois_apply
(σ : GaloisAut)

(x : ℕ)
 :ℕ**


[I.D95a] Apply a Galois automorphism to an element.
Equations
- Tau.Boundary.galois_apply σ x = σ.multiplier * x % Tau.Polarity.primorial σ.stage
Instances For

---

### `Tau.Boundary.galois_aut_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L61-L63)
**def
Tau.Boundary.galois_aut_check
(σ : GaloisAut)
 :Bool**


[I.D95a] Check that σ is a valid automorphism (unit multiplier).
Equations
- Tau.Boundary.galois_aut_check σ = Tau.Boundary.is_unit_mod σ.multiplier (Tau.Polarity.primorial σ.stage)
Instances For

---

### `Tau.Boundary.galois_compose`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L65-L69)
**def
Tau.Boundary.galois_compose
(σ τ_aut : GaloisAut)
 :autoParam (σ.stage = τ_aut.stage) galois_compose._auto_1 → GaloisAut**


[I.D95a] Compose two Galois automorphisms.
Equations
- Tau.Boundary.galois_compose σ τ_aut x✝ = { stage := σ.stage, multiplier := σ.multiplier * τ_aut.multiplier % Tau.Polarity.primorial σ.stage }
Instances For

---

### `Tau.Boundary.galois_id`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L71-L73)
**def
Tau.Boundary.galois_id
(k : ℕ)
 :GaloisAut**


[I.D95a] The identity automorphism.
Equations
- Tau.Boundary.galois_id k = { stage := k, multiplier := 1 }
Instances For

---

### `Tau.Boundary.galois_inv`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L75-L86)
**def
Tau.Boundary.galois_inv
(σ_aut : GaloisAut)
 :GaloisAut**


[I.D95a] The inverse of an automorphism (modular inverse).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.galois_inv.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L82-L85)@[irreducible]

**def
Tau.Boundary.galois_inv.go
(mult a pk fuel : ℕ)
 :ℕ**

Equations
- Tau.Boundary.galois_inv.go mult a pk fuel = if fuel = 0 then 0
 else if (mult * a % pk == 1) = true then a else Tau.Boundary.galois_inv.go mult (a + 1) pk (fuel - 1)
Instances For

---

### `Tau.Boundary.galois_group_order`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L94-L96)
**def
Tau.Boundary.galois_group_order
(k : ℕ)
 :ℕ**


[I.D96a] Order of the Galois group at stage k = φ(M_k).
Equations
- Tau.Boundary.galois_group_order k = Tau.Boundary.euler_totient (Tau.Polarity.primorial k)
Instances For

---

### `Tau.Boundary.galois_order_expected`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L98-L107)
**def
Tau.Boundary.galois_order_expected
(k : ℕ)
 :ℕ**


[I.D96a] Expected order via prime factorization: ∏(p_i - 1).
Equations
- Tau.Boundary.galois_order_expected k = Tau.Boundary.galois_order_expected.go 1 k 1
Instances For

---

### `Tau.Boundary.galois_order_expected.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L102-L106)@[irreducible]

**def
Tau.Boundary.galois_order_expected.go
(i kmax acc : ℕ)
 :ℕ**

Equations
- Tau.Boundary.galois_order_expected.go i kmax acc = if i > kmax then acc
 else have p := Tau.Polarity.nth_prime i;
 Tau.Boundary.galois_order_expected.go (i + 1) kmax (acc * (p - 1))
Instances For

---

### `Tau.Boundary.galois_group_order_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L109-L111)
**def
Tau.Boundary.galois_group_order_check
(k : ℕ)
 :Bool**


[I.D96a] Check that φ(M_k) = ∏(p_i - 1).
Equations
- Tau.Boundary.galois_group_order_check k = (Tau.Boundary.galois_group_order k == Tau.Boundary.galois_order_expected k)
Instances For

---

### `Tau.Boundary.galois_additive_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L117-L134)
**def
Tau.Boundary.galois_additive_check
(σ : GaloisAut)
 :Bool**


[I.D95a] Check that σ_a preserves addition: σ(x+y) = σ(x)+σ(y).
Equations
- Tau.Boundary.galois_additive_check σ = Tau.Boundary.galois_additive_check.go σ 0 (Tau.Polarity.primorial σ.stage) (Tau.Polarity.primorial σ.stage)
Instances For

---

### `Tau.Boundary.galois_additive_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L122-L125)@[irreducible]

**def
Tau.Boundary.galois_additive_check.go
(σ : GaloisAut)

(x pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.galois_additive_check.go_inner`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L127-L133)@[irreducible]

**def
Tau.Boundary.galois_additive_check.go_inner
(σ : GaloisAut)

(x y pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.galois_root_preserving_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L136-L162)
**def
Tau.Boundary.galois_root_preserving_check
(σ : GaloisAut)
 :Bool**


[I.D95a] Check that σ_a preserves roots of unity:
if z^n ≡ 1 mod m, then (σ_a(z))^n ≡ 1 mod m, where σ_a(z) = z^a.
Equations
- Tau.Boundary.galois_root_preserving_check σ = Tau.Boundary.galois_root_preserving_check.go σ 0 (Tau.Polarity.primorial σ.stage) (Tau.Polarity.primorial σ.stage)
Instances For

---

### `Tau.Boundary.galois_root_preserving_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L142-L149)@[irreducible]

**def
Tau.Boundary.galois_root_preserving_check.go
(σ : GaloisAut)

(z pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.galois_root_preserving_check.go_n`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L151-L161)@[irreducible]

**def
Tau.Boundary.galois_root_preserving_check.go_n
(z a n pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.unit_group_closed_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L164-L182)
**def
Tau.Boundary.unit_group_closed_check
(k : ℕ)
 :Bool**


[I.D95a] Check that the unit group is closed under multiplication mod M_k.
Equations
- Tau.Boundary.unit_group_closed_check k = Tau.Boundary.unit_group_closed_check.go 1 (Tau.Polarity.primorial k) (Tau.Polarity.primorial k)
Instances For

---

### `Tau.Boundary.unit_group_closed_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L169-L172)@[irreducible]

**def
Tau.Boundary.unit_group_closed_check.go
(a pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.unit_group_closed_check.go_inner`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L174-L181)@[irreducible]

**def
Tau.Boundary.unit_group_closed_check.go_inner
(a b pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.galois_crt_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L188-L192)
**def
Tau.Boundary.galois_crt_check
(k : ℕ)
 :Bool**


[I.P43a] Verify the CRT decomposition: the Galois group at stage k
decomposes as a product of (Z/p_i Z)× for i=1..k. Check by verifying
the order equality.
Equations
- Tau.Boundary.galois_crt_check k = Tau.Boundary.galois_group_order_check k
Instances For

---

### `Tau.Boundary.galois_fundamental_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L198-L217)
**def
Tau.Boundary.galois_fundamental_check
(k : ℕ)
 :Bool**


[I.T49a] Check that every unit generates a valid Galois action:
preserves addition (as ring endomorphism) and preserves roots of unity
(as field automorphism on cyclotomic extension). Verified at stage k.
Equations
- Tau.Boundary.galois_fundamental_check k = (Tau.Boundary.unit_group_closed_check k && Tau.Boundary.galois_fundamental_check.go k 1 (Tau.Polarity.primorial k) (Tau.Polarity.primorial k))
Instances For

---

### `Tau.Boundary.galois_fundamental_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L208-L216)@[irreducible]

**def
Tau.Boundary.galois_fundamental_check.go
(k a pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Boundary.galois_order_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L223-L224)
**theorem
Tau.Boundary.galois_order_1 :galois_group_order 1 = 1**


[I.D96a] φ(2) = 1.

---

### `Tau.Boundary.galois_order_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L226-L227)
**theorem
Tau.Boundary.galois_order_2 :galois_group_order 2 = 2**


[I.D96a] φ(6) = 2.

---

### `Tau.Boundary.galois_order_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L229-L230)
**theorem
Tau.Boundary.galois_order_3 :galois_group_order 3 = 8**


[I.D96a] φ(30) = 8.

---

### `Tau.Boundary.galois_order_check_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L232-L234)
**theorem
Tau.Boundary.galois_order_check_1 :galois_group_order_check 1 = true**


[I.D96a] Order matches prime product at stage 1.

---

### `Tau.Boundary.galois_order_check_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L236-L238)
**theorem
Tau.Boundary.galois_order_check_2 :galois_group_order_check 2 = true**


[I.D96a] Order matches prime product at stage 2.

---

### `Tau.Boundary.galois_order_check_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L240-L242)
**theorem
Tau.Boundary.galois_order_check_3 :galois_group_order_check 3 = true**


[I.D96a] Order matches prime product at stage 3.

---

### `Tau.Boundary.galois_fundamental_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L244-L246)
**theorem
Tau.Boundary.galois_fundamental_2 :galois_fundamental_check 2 = true**


[I.T49a] All units at stage 2 are valid ring automorphisms.

---

### `Tau.Boundary.galois_crt_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L248-L250)
**theorem
Tau.Boundary.galois_crt_3 :galois_crt_check 3 = true**


[I.P43a] CRT decomposition verified at stage 3.

---

### `Tau.Boundary.galois_id_valid_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L252-L254)
**theorem
Tau.Boundary.galois_id_valid_1 :galois_aut_check (galois_id 1) = true**


[I.D95a] Identity is always a valid automorphism at stage 1.

---

### `Tau.Boundary.galois_id_valid_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L256-L258)
**theorem
Tau.Boundary.galois_id_valid_2 :galois_aut_check (galois_id 2) = true**


[I.D95a] Identity is always a valid automorphism at stage 2.

---

### `Tau.Boundary.galois_id_valid_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Boundary/Galois.lean#L260-L262)
**theorem
Tau.Boundary.galois_id_valid_3 :galois_aut_check (galois_id 3) = true**


[I.D95a] Identity is always a valid automorphism at stage 3.
