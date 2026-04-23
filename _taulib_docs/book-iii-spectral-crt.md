---
layout: taulib-doc
title: "TauLib.BookIII.Spectral.CRT"
permalink: /verify/taulib/docs/book-iii-spectral-crt/
lane: verify
module_name: "TauLib.BookIII.Spectral.CRT"
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

# TauLib.BookIII.Spectral.CRT


CRT Decomposition Theorem at spectral level, Reconstruction Functor,
and Independence of Prime-Level Actions.

## Registry Cross-References


- [III.T10] CRT Decomposition Theorem -- `crt_spectral_check`

- [III.D20] Reconstruction Functor -- `reconstruction_functor_check`

- [III.P05] Independence of Prime-Level Actions -- `prime_independence_check`


## Mathematical Content


**III.T10 (CRT Decomposition):** τ-native Chinese Remainder Theorem:
ℤ/Prim(k)ℤ ≅ ∏ᵢ₌₁ᵏ ℤ/pᵢℤ proved constructively without signed
arithmetic. CRT = algebraic Euler product.

**III.D20 (Reconstruction Functor):** CRT defines a functor R_k from
∏(ℤ/pᵢℤ-Mod) to ℤ/Prim(k)ℤ-Mod. This functor is an equivalence.

**III.P05 (Prime Independence):** Prime-level actions T^(i) on ℤ/pᵢℤ
are independent. CRT guarantees unique reassembly.

---

### `Tau.BookIII.Spectral.crt_spectral_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L38-L59)
**def
Tau.BookIII.Spectral.crt_spectral_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T10] CRT spectral decomposition at enriched level.
Verifies that crt_decompose ∘ crt_reconstruct = id at each
primorial level, enriched by tower coherence.
Equations
- Tau.BookIII.Spectral.crt_spectral_check bound db = Tau.BookIII.Spectral.crt_spectral_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Spectral.crt_spectral_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L44-L58)@[irreducible]

**def
Tau.BookIII.Spectral.crt_spectral_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.crt_add_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L61-L91)
**def
Tau.BookIII.Spectral.crt_add_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T10] CRT ring homomorphism: addition is preserved.
Equations
- Tau.BookIII.Spectral.crt_add_check bound db = Tau.BookIII.Spectral.crt_add_check.go bound db 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Spectral.crt_add_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L65-L81)@[irreducible]

**def
Tau.BookIII.Spectral.crt_add_check.go
(bound db : Denotation.TauIdx)

(x y k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.crt_add_check.go_components`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L83-L91)@[irreducible]

**def
Tau.BookIII.Spectral.crt_add_check.go_components
(rx ry rsum : List Denotation.TauIdx)

(i k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.crt_mul_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L93-L121)
**def
Tau.BookIII.Spectral.crt_mul_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T10] CRT ring homomorphism: multiplication is preserved.
Equations
- Tau.BookIII.Spectral.crt_mul_check bound db = Tau.BookIII.Spectral.crt_mul_check.go bound db 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Spectral.crt_mul_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L97-L111)@[irreducible]

**def
Tau.BookIII.Spectral.crt_mul_check.go
(bound db : Denotation.TauIdx)

(x y k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.crt_mul_check.go_mul_components`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L113-L121)@[irreducible]

**def
Tau.BookIII.Spectral.crt_mul_check.go_mul_components
(rx ry rprod : List Denotation.TauIdx)

(i k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.reconstruction_functor_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L127-L144)
**def
Tau.BookIII.Spectral.reconstruction_functor_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D20] Reconstruction functor R_k: given residues, reconstruct
the unique element mod Prim(k). Checks that R_k is inverse to S_k
(the restriction/decomposition functor).
Equations
- Tau.BookIII.Spectral.reconstruction_functor_check bound db = Tau.BookIII.Spectral.reconstruction_functor_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Spectral.reconstruction_functor_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L133-L143)@[irreducible]

**def
Tau.BookIII.Spectral.reconstruction_functor_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.reconstruction_tower_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L146-L161)
**def
Tau.BookIII.Spectral.reconstruction_tower_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D20] Reconstruction functor respects tower: R_{k+1} projects
to R_k under reduce.
Equations
- Tau.BookIII.Spectral.reconstruction_tower_check bound db = Tau.BookIII.Spectral.reconstruction_tower_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Spectral.reconstruction_tower_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L151-L160)@[irreducible]

**def
Tau.BookIII.Spectral.reconstruction_tower_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.prime_independence_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L167-L195)
**def
Tau.BookIII.Spectral.prime_independence_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.P05] Prime-level independence: modifying one residue does not
affect others. The CRT structure guarantees orthogonality.
Equations
- Tau.BookIII.Spectral.prime_independence_check bound db = Tau.BookIII.Spectral.prime_independence_check.go bound db 0 1 0 ((bound + 1) * (db + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Spectral.prime_independence_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L172-L186)@[irreducible]

**def
Tau.BookIII.Spectral.prime_independence_check.go
(bound db : Denotation.TauIdx)

(x k i fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.prime_independence_check.check_off_diag`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L188-L195)@[irreducible]

**def
Tau.BookIII.Spectral.prime_independence_check.check_off_diag
(residues : List Denotation.TauIdx)

(i j k : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Spectral.crt_spectral_20_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L218-L219)
**theorem
Tau.BookIII.Spectral.crt_spectral_20_4 :crt_spectral_check 20 4 = true**


---

### `Tau.BookIII.Spectral.crt_add_10_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L222-L223)
**theorem
Tau.BookIII.Spectral.crt_add_10_3 :crt_add_check 10 3 = true**


---

### `Tau.BookIII.Spectral.crt_mul_10_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L225-L226)
**theorem
Tau.BookIII.Spectral.crt_mul_10_3 :crt_mul_check 10 3 = true**


---

### `Tau.BookIII.Spectral.reconstruction_20_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L229-L230)
**theorem
Tau.BookIII.Spectral.reconstruction_20_4 :reconstruction_functor_check 20 4 = true**


---

### `Tau.BookIII.Spectral.reconstruction_tower_20_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L232-L233)
**theorem
Tau.BookIII.Spectral.reconstruction_tower_20_4 :reconstruction_tower_check 20 4 = true**


---

### `Tau.BookIII.Spectral.prime_independence_5_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L236-L237)
**theorem
Tau.BookIII.Spectral.prime_independence_5_4 :prime_independence_check 5 4 = true**


---

### `Tau.BookIII.Spectral.crt_roundtrip_42`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L243-L245)
**theorem
Tau.BookIII.Spectral.crt_roundtrip_42 :Polarity.crt_reconstruct (Polarity.crt_decompose 42 3) 3 = Polarity.reduce 42 3**


[III.T10] Structural: CRT round-trip at depth 3 for x = 42.

---

### `Tau.BookIII.Spectral.crt_decompose_42`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L247-L250)
**theorem
Tau.BookIII.Spectral.crt_decompose_42 :Polarity.crt_decompose 42 3 = [0, 0, 2]**


[III.T10] Structural: CRT decomposes 42 mod 30 = 12 into
(12 mod 2, 12 mod 3, 12 mod 5) = (0, 0, 2).

---

### `Tau.BookIII.Spectral.crt_basis_0_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Spectral/CRT.lean#L252-L255)
**theorem
Tau.BookIII.Spectral.crt_basis_0_3 :Polarity.crt_decompose (Polarity.crt_basis 3 0) 3 = [1, 0, 0]**


[III.P05] Structural: CRT basis element 0 at depth 3
has residue 1 mod 2, 0 mod 3, 0 mod 5.
