---
layout: taulib-doc
title: "TauLib.BookII.Hartogs.L2Space"
permalink: /verify/taulib/docs/book-ii-hartogs-l2space/
lane: verify
module_name: "TauLib.BookII.Hartogs.L2Space"
book: "II"
book_label: "Holomorphy"
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
    book: "Book II"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookII.Hartogs.L2Space


L² space on the boundary character group Char(L).

## Registry Cross-References


- [II.D82] L² Inner Product — `l2_inner_product`, `inner_product_check`

- [II.D83] L² Norm — `l2_norm_sq`, `norm_positivity_check`

- [II.T53] Cauchy-Schwarz — `cauchy_schwarz_check`

- [II.P18] Completeness — `l2_completeness_check`


## Mathematical Content


**II.D82 (L² Inner Product):** For functions f, g : Z/M_k Z → ℤ, the inner
product at stage k is ⟨f, g⟩*k = (1/M_k) Σ*{x=0}^{M_k-1} f(x)·g(x).
Represented as a rational pair (numerator, M_k).

**II.D83 (L² Norm):** ‖f‖²_k = ⟨f, f⟩_k = (1/M_k) Σ f(x)². Non-negative
by construction (sum of squares).

**II.T53 (Cauchy-Schwarz):** |⟨f,g⟩|² ≤ ‖f‖² · ‖g‖². Verified as an
inequality of rational pairs at each finite stage.

**II.P18 (Completeness):** The L² space at each finite stage k is
automatically complete (finite-dimensional). Tower compatibility ensures
the inverse system of L² spaces is coherent.

---

### `Tau.BookII.Hartogs.inner_product_sum`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L44-L51)
**def
Tau.BookII.Hartogs.inner_product_sum
(f g : ℕ → ℤ)

(k : ℕ)
 :ℤ**


[II.D82] Inner product sum: Σ_{x=0}^{M_k-1} f(x)·g(x).
Equations
- Tau.BookII.Hartogs.inner_product_sum f g k = Tau.BookII.Hartogs.inner_product_sum.go f g 0 (Tau.Polarity.primorial k) 0
Instances For

---

### `Tau.BookII.Hartogs.inner_product_sum.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L48-L50)@[irreducible]

**def
Tau.BookII.Hartogs.inner_product_sum.go
(f g : ℕ → ℤ)

(x bound : ℕ)

(acc : ℤ)
 :ℤ**

Equations
- Tau.BookII.Hartogs.inner_product_sum.go f g x bound acc = if x ≥ bound then acc else Tau.BookII.Hartogs.inner_product_sum.go f g (x + 1) bound (acc + f x * g x)
Instances For

---

### `Tau.BookII.Hartogs.L2Inner`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L53-L56)
**structure
Tau.BookII.Hartogs.L2Inner :Type**


[II.D82] L² inner product as rational pair: ⟨f,g⟩_k = (Σ f·g, M_k).

- numerator : ℤ
- denominator : ℕ
Instances For

---

### `Tau.BookII.Hartogs.l2_inner_product`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L58-L61)
**def
Tau.BookII.Hartogs.l2_inner_product
(f g : ℕ → ℤ)

(k : ℕ)
 :L2Inner**


[II.D82] Compute the L² inner product at stage k.
Equations
- Tau.BookII.Hartogs.l2_inner_product f g k = { numerator := Tau.BookII.Hartogs.inner_product_sum f g k, denominator := Tau.Polarity.primorial k }
Instances For

---

### `Tau.BookII.Hartogs.inner_product_symmetry_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L63-L65)
**def
Tau.BookII.Hartogs.inner_product_symmetry_check
(f g : ℕ → ℤ)

(k : ℕ)
 :Bool**


[II.D82] Symmetry check: ⟨f,g⟩ = ⟨g,f⟩.
Equations
- Tau.BookII.Hartogs.inner_product_symmetry_check f g k = ((Tau.BookII.Hartogs.l2_inner_product f g k).numerator == (Tau.BookII.Hartogs.l2_inner_product g f k).numerator)
Instances For

---

### `Tau.BookII.Hartogs.inner_product_linearity_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L67-L73)
**def
Tau.BookII.Hartogs.inner_product_linearity_check
(a b : ℤ)

(f1 f2 g : ℕ → ℤ)

(k : ℕ)
 :Bool**


[II.D82] Linearity check: ⟨af₁ + bf₂, g⟩ = a⟨f₁,g⟩ + b⟨f₂,g⟩.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.l2_norm_sq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L79-L81)
**def
Tau.BookII.Hartogs.l2_norm_sq
(f : ℕ → ℤ)

(k : ℕ)
 :ℤ**


[II.D83] L² norm squared: ‖f‖²_k = ⟨f,f⟩_k numerator.
Equations
- Tau.BookII.Hartogs.l2_norm_sq f k = Tau.BookII.Hartogs.inner_product_sum f f k
Instances For

---

### `Tau.BookII.Hartogs.norm_positivity_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L83-L94)
**def
Tau.BookII.Hartogs.norm_positivity_check
(k : ℕ)
 :Bool**


[II.D83] Positivity check: ‖f‖² ≥ 0.
Equations
- Tau.BookII.Hartogs.norm_positivity_check k = Tau.BookII.Hartogs.norm_positivity_check.go k 0 (Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookII.Hartogs.norm_positivity_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L88-L93)@[irreducible]

**def
Tau.BookII.Hartogs.norm_positivity_check.go
(k seed fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.norm_definiteness_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L96-L99)
**def
Tau.BookII.Hartogs.norm_definiteness_check
(k : ℕ)
 :Bool**


[II.D83] Definiteness check: ‖f‖² = 0 implies f = 0 (on support).
Equations
- Tau.BookII.Hartogs.norm_definiteness_check k = (Tau.BookII.Hartogs.l2_norm_sq (fun (x : ℕ) => 0) k == 0)
Instances For

---

### `Tau.BookII.Hartogs.cauchy_schwarz_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L105-L111)
**def
Tau.BookII.Hartogs.cauchy_schwarz_check
(f g : ℕ → ℤ)

(k : ℕ)
 :Bool**


[II.T53] Cauchy-Schwarz check: |⟨f,g⟩|² ≤ ‖f‖² · ‖g‖².
As integers: (Σ fg)² ≤ (Σ f²)(Σ g²).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.cauchy_schwarz_exhaustive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L113-L130)
**def
Tau.BookII.Hartogs.cauchy_schwarz_exhaustive
(k : ℕ)
 :Bool**


[II.T53] Exhaustive Cauchy-Schwarz check for basis functions at stage k.
Equations
- Tau.BookII.Hartogs.cauchy_schwarz_exhaustive k = Tau.BookII.Hartogs.cauchy_schwarz_exhaustive.go_f k 0 (Tau.Polarity.primorial k) (Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookII.Hartogs.cauchy_schwarz_exhaustive.go_f`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L118-L121)@[irreducible]

**def
Tau.BookII.Hartogs.cauchy_schwarz_exhaustive.go_f
(k a pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.cauchy_schwarz_exhaustive.go_g`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L123-L129)@[irreducible]

**def
Tau.BookII.Hartogs.cauchy_schwarz_exhaustive.go_g
(k a b pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.l2_completeness_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L136-L156)
**def
Tau.BookII.Hartogs.l2_completeness_check
(k : ℕ)
 :Bool**


[II.P18] L² completeness: at each finite stage, the space is
finite-dimensional (dim = M_k), hence automatically complete.
Tower compatibility: the projection from stage k+1 to stage k
preserves inner products up to normalization.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.l2_basis_orthogonality_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L162-L182)
**def
Tau.BookII.Hartogs.l2_basis_orthogonality_check
(k : ℕ)
 :Bool**


[II.D82] Check that indicator functions form an orthogonal basis
for L²(Z/M_k Z).
Equations
- Tau.BookII.Hartogs.l2_basis_orthogonality_check k = Tau.BookII.Hartogs.l2_basis_orthogonality_check.go_a k 0 (Tau.Polarity.primorial k) (Tau.Polarity.primorial k)
Instances For

---

### `Tau.BookII.Hartogs.l2_basis_orthogonality_check.go_a`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L168-L171)@[irreducible]

**def
Tau.BookII.Hartogs.l2_basis_orthogonality_check.go_a
(k a pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.l2_basis_orthogonality_check.go_b`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L173-L181)@[irreducible]

**def
Tau.BookII.Hartogs.l2_basis_orthogonality_check.go_b
(k a b pk fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Hartogs.inner_product_symmetry_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L188-L192)
**theorem
Tau.BookII.Hartogs.inner_product_symmetry_2 :inner_product_symmetry_check (fun (x : ℕ) => ↑x) (fun (x : ℕ) => ↑x * ↑x) 2 = true**


[II.D82] Symmetry of inner product at stage 2.

---

### `Tau.BookII.Hartogs.inner_product_linearity_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L194-L198)
**theorem
Tau.BookII.Hartogs.inner_product_linearity_2 :inner_product_linearity_check 2 3 (fun (x : ℕ) => ↑x) (fun (x : ℕ) => 1) (fun (x : ℕ) => ↑x * ↑x) 2 = true**


[II.D82] Linearity of inner product at stage 2.

---

### `Tau.BookII.Hartogs.norm_positivity_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L200-L202)
**theorem
Tau.BookII.Hartogs.norm_positivity_2 :norm_positivity_check 2 = true**


[II.D83] Norm positivity at stage 2.

---

### `Tau.BookII.Hartogs.norm_definiteness_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L204-L206)
**theorem
Tau.BookII.Hartogs.norm_definiteness_2 :norm_definiteness_check 2 = true**


[II.D83] Norm definiteness at stage 2.

---

### `Tau.BookII.Hartogs.cauchy_schwarz_stage1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L208-L210)
**theorem
Tau.BookII.Hartogs.cauchy_schwarz_stage1 :cauchy_schwarz_exhaustive 1 = true**


[II.T53] Cauchy-Schwarz exhaustive at stage 1.

---

### `Tau.BookII.Hartogs.cauchy_schwarz_stage2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L212-L214)
**theorem
Tau.BookII.Hartogs.cauchy_schwarz_stage2 :cauchy_schwarz_exhaustive 2 = true**


[II.T53] Cauchy-Schwarz exhaustive at stage 2.

---

### `Tau.BookII.Hartogs.l2_completeness_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L216-L218)
**theorem
Tau.BookII.Hartogs.l2_completeness_1 :l2_completeness_check 1 = true**


[II.P18] L² completeness at stage 1.

---

### `Tau.BookII.Hartogs.l2_completeness_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L220-L222)
**theorem
Tau.BookII.Hartogs.l2_completeness_2 :l2_completeness_check 2 = true**


[II.P18] L² completeness at stage 2.

---

### `Tau.BookII.Hartogs.l2_basis_orthogonal_1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L224-L226)
**theorem
Tau.BookII.Hartogs.l2_basis_orthogonal_1 :l2_basis_orthogonality_check 1 = true**


[II.D82] Basis orthogonality at stage 1.

---

### `Tau.BookII.Hartogs.l2_basis_orthogonal_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Hartogs/L2Space.lean#L228-L230)
**theorem
Tau.BookII.Hartogs.l2_basis_orthogonal_2 :l2_basis_orthogonality_check 2 = true**


[II.D82] Basis orthogonality at stage 2.
