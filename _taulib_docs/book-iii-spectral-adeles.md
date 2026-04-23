---
layout: taulib-doc
title: "TauLib.BookIII.Spectral.Adeles"
permalink: /verify/taulib/docs/book-iii-spectral-adeles/
lane: verify
module_name: "TauLib.BookIII.Spectral.Adeles"
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

# TauLib.BookIII.Spectral.Adeles


τ-Adele Ring, Adelic Embedding Theorem, and Adelic Euler Product.

## Registry Cross-References


- [III.D22] τ-Adele Ring -- `AdeleElement`, `adele_ring_check`

- [III.T12] Adelic Embedding Theorem -- `adelic_embedding_check`

- [III.P07] Adelic Euler Product -- `euler_product_check`


## Mathematical Content


**III.D22 (τ-Adele Ring):** 𝔸_τ = restricted product of local fields
ℤ_p^τ with respect to unit groups. Almost all components integral.

**III.T12 (Adelic Embedding):** The canonical map τ → 𝔸_τ is injective
with dense image. Every τ-object maps to an adelic tuple.

**III.P07 (Adelic Euler Product):** τ-holomorphic function on 𝔸_τ
decomposes into local factors at each prime. CRT lifted to holomorphic level.

---

### `Tau.BookIII.Spectral.AdeleElement`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L36-L41)
**structure
Tau.BookIII.Spectral.AdeleElement :Type**


[III.D22] An adele element at finite depth: a tuple of local field
elements, one per prime, with almost all integral (= unit mod p).

- depth : Denotation.TauIdx
- components : List Denotation.TauIdx
Instances For

---

### `Tau.BookIII.Spectral.instReprAdeleElement`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L41-L41)
**instance
Tau.BookIII.Spectral.instReprAdeleElement :Repr AdeleElement**

Equations
- Tau.BookIII.Spectral.instReprAdeleElement = { reprPrec := Tau.BookIII.Spectral.instReprAdeleElement.repr }

---

### `Tau.BookIII.Spectral.instReprAdeleElement.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L41-L41)
**def
Tau.BookIII.Spectral.instReprAdeleElement.repr :AdeleElement → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.instDecidableEqAdeleElement`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L41-L41)
**instance
Tau.BookIII.Spectral.instDecidableEqAdeleElement :DecidableEq AdeleElement**

Equations
- Tau.BookIII.Spectral.instDecidableEqAdeleElement = Tau.BookIII.Spectral.instDecidableEqAdeleElement.decEq

---

### `Tau.BookIII.Spectral.instDecidableEqAdeleElement.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L41-L41)
**def
Tau.BookIII.Spectral.instDecidableEqAdeleElement.decEq
(x✝ x✝¹ : AdeleElement)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.instBEqAdeleElement.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L41-L41)
**def
Tau.BookIII.Spectral.instBEqAdeleElement.beq :AdeleElement → AdeleElement → Bool**

Equations
- Tau.BookIII.Spectral.instBEqAdeleElement.beq { depth := a, components := a_1 } { depth := b, components := b_1 } = (a == b && a_1 == b_1)
- Tau.BookIII.Spectral.instBEqAdeleElement.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIII.Spectral.instBEqAdeleElement`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L41-L41)
**instance
Tau.BookIII.Spectral.instBEqAdeleElement :BEq AdeleElement**

Equations
- Tau.BookIII.Spectral.instBEqAdeleElement = { beq := Tau.BookIII.Spectral.instBEqAdeleElement.beq }

---

### `Tau.BookIII.Spectral.to_adele`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L43-L46)
**def
Tau.BookIII.Spectral.to_adele
(x k : Denotation.TauIdx)
 :AdeleElement**


[III.D22] Build an adele element from a global τ-value x at depth k.
The i-th component is x mod p_{i+1} (using CRT decomposition).
Equations
- Tau.BookIII.Spectral.to_adele x k = { depth := k, components := Tau.Polarity.crt_decompose x k }
Instances For

---

### `Tau.BookIII.Spectral.adele_add`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L48-L61)
**def
Tau.BookIII.Spectral.adele_add
(a b : AdeleElement)
 :AdeleElement**


[III.D22] Adele addition: component-wise addition mod p_i.
Equations
- Tau.BookIII.Spectral.adele_add a b = { depth := a.depth, components := Tau.BookIII.Spectral.adele_add.go a.components b.components 0 a.depth [] }
Instances For

---

### `Tau.BookIII.Spectral.adele_add.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L54-L61)@[irreducible]

**def
Tau.BookIII.Spectral.adele_add.go
(as_ bs : List Denotation.TauIdx)

(i k : ℕ)

(acc : List Denotation.TauIdx)
 :List Denotation.TauIdx**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.adele_mul`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L63-L76)
**def
Tau.BookIII.Spectral.adele_mul
(a b : AdeleElement)
 :AdeleElement**


[III.D22] Adele multiplication: component-wise multiplication mod p_i.
Equations
- Tau.BookIII.Spectral.adele_mul a b = { depth := a.depth, components := Tau.BookIII.Spectral.adele_mul.go a.components b.components 0 a.depth [] }
Instances For

---

### `Tau.BookIII.Spectral.adele_mul.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L69-L76)@[irreducible]

**def
Tau.BookIII.Spectral.adele_mul.go
(as_ bs : List Denotation.TauIdx)

(i k : ℕ)

(acc : List Denotation.TauIdx)
 :List Denotation.TauIdx**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.adele_ring_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L78-L102)
**def
Tau.BookIII.Spectral.adele_ring_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D22] Adele ring check: verify ring axioms component-wise.
Equations
- Tau.BookIII.Spectral.adele_ring_check bound db = Tau.BookIII.Spectral.adele_ring_check.go bound db 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Spectral.adele_ring_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L82-L101)@[irreducible]

**def
Tau.BookIII.Spectral.adele_ring_check.go
(bound db : Denotation.TauIdx)

(x y k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.adelic_embedding_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L108-L130)
**def
Tau.BookIII.Spectral.adelic_embedding_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T12] Adelic embedding: the map x ↦ (x mod p₁, ..., x mod pₖ)
is injective on ℤ/Prim(k)ℤ. This is CRT injectivity.
Equations
- Tau.BookIII.Spectral.adelic_embedding_check bound db = Tau.BookIII.Spectral.adelic_embedding_check.go bound db 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Spectral.adelic_embedding_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L113-L129)@[irreducible]

**def
Tau.BookIII.Spectral.adelic_embedding_check.go
(bound db : Denotation.TauIdx)

(x y k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.adelic_dense_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L132-L146)
**def
Tau.BookIII.Spectral.adelic_dense_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T12] Dense image: for any adelic tuple (r₁, ..., rₖ),
there exists x with x ≡ rᵢ mod pᵢ. This is CRT surjectivity.
Equations
- Tau.BookIII.Spectral.adelic_dense_check bound db = Tau.BookIII.Spectral.adelic_dense_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Spectral.adelic_dense_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L137-L145)@[irreducible]

**def
Tau.BookIII.Spectral.adelic_dense_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.euler_product_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L152-L173)
**def
Tau.BookIII.Spectral.euler_product_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.P07] Euler product: a multiplicative function on ℤ/Prim(k)ℤ
decomposes as a product of local factors.
f(x) = ∏ f_p(x mod p) where f_p is the p-local factor.
Equations
- Tau.BookIII.Spectral.euler_product_check bound db = Tau.BookIII.Spectral.euler_product_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Spectral.euler_product_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L158-L172)@[irreducible]

**def
Tau.BookIII.Spectral.euler_product_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.local_factor_independence_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L175-L199)
**def
Tau.BookIII.Spectral.local_factor_independence_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.P07] Local factor independence: modifying one local factor
only changes that component, not others.
Equations
- Tau.BookIII.Spectral.local_factor_independence_check bound db = Tau.BookIII.Spectral.local_factor_independence_check.go bound db 0 1 0 ((bound + 1) * (db + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Spectral.local_factor_independence_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L180-L192)@[irreducible]

**def
Tau.BookIII.Spectral.local_factor_independence_check.go
(bound db : Denotation.TauIdx)

(x k i fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.local_factor_independence_check.check_others`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L194-L199)@[irreducible]

**def
Tau.BookIII.Spectral.local_factor_independence_check.check_others
(orig modified : List Denotation.TauIdx)

(skip j k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.adele_ring_10_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L225-L226)
**theorem
Tau.BookIII.Spectral.adele_ring_10_3 :adele_ring_check 10 3 = true**


---

### `Tau.BookIII.Spectral.adelic_embedding_15_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L229-L230)
**theorem
Tau.BookIII.Spectral.adelic_embedding_15_3 :adelic_embedding_check 15 3 = true**


---

### `Tau.BookIII.Spectral.adelic_dense_20_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L233-L234)
**theorem
Tau.BookIII.Spectral.adelic_dense_20_4 :adelic_dense_check 20 4 = true**


---

### `Tau.BookIII.Spectral.euler_product_20_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L237-L238)
**theorem
Tau.BookIII.Spectral.euler_product_20_4 :euler_product_check 20 4 = true**


---

### `Tau.BookIII.Spectral.local_factor_ind_10_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L241-L242)
**theorem
Tau.BookIII.Spectral.local_factor_ind_10_3 :local_factor_independence_check 10 3 = true**


---

### `Tau.BookIII.Spectral.adele_zero_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L248-L249)
**theorem
Tau.BookIII.Spectral.adele_zero_3 :(to_adele 0 3).components = [0, 0, 0]**


[III.D22] Structural: adele of 0 has all-zero components.

---

### `Tau.BookIII.Spectral.adele_is_crt`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L251-L253)
**theorem
Tau.BookIII.Spectral.adele_is_crt :(to_adele 42 3).components = Polarity.crt_decompose 42 3**


[III.T12] Structural: adelic embedding is CRT decomposition.

---

### `Tau.BookIII.Spectral.adele_injective_1_2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/Adeles.lean#L255-L257)
**theorem
Tau.BookIII.Spectral.adele_injective_1_2 :(to_adele 1 3).components ≠ (to_adele 2 3).components**


[III.T12] Structural: distinct values have distinct adelic images.
