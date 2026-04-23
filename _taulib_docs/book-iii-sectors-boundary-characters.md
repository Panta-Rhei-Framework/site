---
layout: taulib-doc
title: "TauLib.BookIII.Sectors.BoundaryCharacters"
permalink: /verify/taulib/docs/book-iii-sectors-boundary-characters/
lane: verify
module_name: "TauLib.BookIII.Sectors.BoundaryCharacters"
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

# TauLib.BookIII.Sectors.BoundaryCharacters


Boundary character space on L = S¹ ∨ S¹ and the boundary-to-interior functor.

## Registry Cross-References


- [III.D11] Boundary Character Space -- `BoundaryCharacter`, `boundary_char_check`

- [III.D12] Boundary-to-Interior Functor -- `boundary_to_interior`, `bti_functor_check`


## Mathematical Content


**III.D11 (Boundary Character Space):** Characters on L = S¹ ∨ S¹:
Char(L) = Hom(π₁(L), S¹) ≅ S¹ × S¹. The character lattice ℤ² from
H₁(L; ℤ) ≅ ℤ ⊕ ℤ. Every character indexed by (m,n) ∈ ℤ².
The m-axis = multiplicative/Galois, n-axis = additive/automorphic.

**III.D12 (Boundary-to-Interior Functor):** The functor Φ: Char(L) → O(τ³)
mapping boundary characters to interior holomorphic functions. This is
Langlands₀: boundary functoriality.

---

### `Tau.BookIII.Sectors.BoundaryCharacter`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L36-L44)
**structure
Tau.BookIII.Sectors.BoundaryCharacter :Type**


[III.D11] A boundary character on L = S¹ ∨ S¹.
Indexed by (m, n) ∈ ℤ² where:


- m = multiplicative/Galois axis (B-lobe winding number)

- n = additive/automorphic axis (C-lobe winding number)
The character lattice is ℤ² from H₁(L; ℤ) ≅ ℤ ⊕ ℤ.


- m_index : ℤ
- n_index : ℤ
Instances For

---

### `Tau.BookIII.Sectors.instReprBoundaryCharacter.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L44-L44)
**def
Tau.BookIII.Sectors.instReprBoundaryCharacter.repr :BoundaryCharacter → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.instReprBoundaryCharacter`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L44-L44)
**instance
Tau.BookIII.Sectors.instReprBoundaryCharacter :Repr BoundaryCharacter**

Equations
- Tau.BookIII.Sectors.instReprBoundaryCharacter = { reprPrec := Tau.BookIII.Sectors.instReprBoundaryCharacter.repr }

---

### `Tau.BookIII.Sectors.instDecidableEqBoundaryCharacter.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L44-L44)
**def
Tau.BookIII.Sectors.instDecidableEqBoundaryCharacter.decEq
(x✝ x✝¹ : BoundaryCharacter)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.instDecidableEqBoundaryCharacter`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L44-L44)
**instance
Tau.BookIII.Sectors.instDecidableEqBoundaryCharacter :DecidableEq BoundaryCharacter**

Equations
- Tau.BookIII.Sectors.instDecidableEqBoundaryCharacter = Tau.BookIII.Sectors.instDecidableEqBoundaryCharacter.decEq

---

### `Tau.BookIII.Sectors.instBEqBoundaryCharacter`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L44-L44)
**instance
Tau.BookIII.Sectors.instBEqBoundaryCharacter :BEq BoundaryCharacter**

Equations
- Tau.BookIII.Sectors.instBEqBoundaryCharacter = { beq := Tau.BookIII.Sectors.instBEqBoundaryCharacter.beq }

---

### `Tau.BookIII.Sectors.instBEqBoundaryCharacter.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L44-L44)
**def
Tau.BookIII.Sectors.instBEqBoundaryCharacter.beq :BoundaryCharacter → BoundaryCharacter → Bool**

Equations
- Tau.BookIII.Sectors.instBEqBoundaryCharacter.beq { m_index := a, n_index := a_1 } { m_index := b, n_index := b_1 } = (a == b && a_1 == b_1)
- Tau.BookIII.Sectors.instBEqBoundaryCharacter.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookIII.Sectors.instInhabitedBoundaryCharacter.default`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L44-L44)
**def
Tau.BookIII.Sectors.instInhabitedBoundaryCharacter.default :BoundaryCharacter**

Equations
- Tau.BookIII.Sectors.instInhabitedBoundaryCharacter.default = { m_index := default, n_index := default }
Instances For

---

### `Tau.BookIII.Sectors.instInhabitedBoundaryCharacter`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L44-L44)
**instance
Tau.BookIII.Sectors.instInhabitedBoundaryCharacter :Inhabited BoundaryCharacter**

Equations
- Tau.BookIII.Sectors.instInhabitedBoundaryCharacter = { default := Tau.BookIII.Sectors.instInhabitedBoundaryCharacter.default }

---

### `Tau.BookIII.Sectors.BoundaryCharacter.zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L46-L47)
**def
Tau.BookIII.Sectors.BoundaryCharacter.zero :BoundaryCharacter**


Zero character: (0,0) — the trivial character.
Equations
- Tau.BookIII.Sectors.BoundaryCharacter.zero = { m_index := 0, n_index := 0 }
Instances For

---

### `Tau.BookIII.Sectors.BoundaryCharacter.add`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L49-L51)
**def
Tau.BookIII.Sectors.BoundaryCharacter.add
(χ₁ χ₂ : BoundaryCharacter)
 :BoundaryCharacter**


Character addition on ℤ².
Equations
- χ₁.add χ₂ = { m_index := χ₁.m_index + χ₂.m_index, n_index := χ₁.n_index + χ₂.n_index }
Instances For

---

### `Tau.BookIII.Sectors.BoundaryCharacter.neg`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L53-L55)
**def
Tau.BookIII.Sectors.BoundaryCharacter.neg
(χ : BoundaryCharacter)
 :BoundaryCharacter**


Character negation on ℤ².
Equations
- χ.neg = { m_index := -χ.m_index, n_index := -χ.n_index }
Instances For

---

### `Tau.BookIII.Sectors.BoundaryCharacter.eval`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L57-L64)
**def
Tau.BookIII.Sectors.BoundaryCharacter.eval
(χ : BoundaryCharacter)

(x k : Denotation.TauIdx)
 :ℤ**


Evaluate a boundary character at a τ-address.
At finite cutoff: the character value is computed via the
bipolar decomposition of the interior point.
χ_{(m,n)}(x, k) = m · B(x,k) + n · C(x,k) mod P_k
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.boundary_char_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L66-L91)
**def
Tau.BookIII.Sectors.boundary_char_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D11] Boundary character space check: verify that characters
form a group under addition (closure, associativity, identity, inverse)
at finite cutoff.
Equations
- Tau.BookIII.Sectors.boundary_char_check bound db = Tau.BookIII.Sectors.boundary_char_check.go bound db 0 0 0 0 1 ((bound + 1) ^ 4 * (db + 1))
Instances For

---

### `Tau.BookIII.Sectors.boundary_char_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L72-L90)@[irreducible]

**def
Tau.BookIII.Sectors.boundary_char_check.go
(bound db : Denotation.TauIdx)

(m1 n1 m2 n2 k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.boundary_to_interior`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L97-L106)
**def
Tau.BookIII.Sectors.boundary_to_interior
(χ : BoundaryCharacter)

(x k : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D12] Boundary-to-interior functor Φ: Char(L) → O(τ³).
Maps a boundary character (m,n) to its interior holomorphic extension.
At finite cutoff: Φ(χ)(x, k) = reduce((|m| + |n|) · reduce(x, k), k).

This definition is manifestly tower-coherent: since reduce(x, k+1) ≡
reduce(x, k) mod P_k, the character-weighted value also reduces correctly.
This is Langlands₀: boundary functoriality.
Equations
- Tau.BookIII.Sectors.boundary_to_interior χ x k = Tau.Polarity.reduce (Tau.Polarity.reduce x k * (χ.m_index.natAbs + χ.n_index.natAbs)) k
Instances For

---

### `Tau.BookIII.Sectors.bti_functor_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L108-L133)
**def
Tau.BookIII.Sectors.bti_functor_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D12] BTI functor preserves tower coherence:
reduce(Φ(χ)(x, k+1), k) = Φ(χ)(x, k).
This is the holomorphic extension property.
Equations
- Tau.BookIII.Sectors.bti_functor_check bound db = Tau.BookIII.Sectors.bti_functor_check.go bound db 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Sectors.bti_functor_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L114-L132)@[irreducible]

**def
Tau.BookIII.Sectors.bti_functor_check.go
(bound db : Denotation.TauIdx)

(m x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.bti_additive_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L135-L154)
**def
Tau.BookIII.Sectors.bti_additive_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D12] BTI functor preserves character addition:
Φ(χ₁ + χ₂) tower-agrees with Φ(χ₁) + Φ(χ₂) at finite cutoff.
Equations
- Tau.BookIII.Sectors.bti_additive_check bound db = Tau.BookIII.Sectors.bti_additive_check.go bound db 0 0 0 1 ((bound + 1) ^ 3 * (db + 1))
Instances For

---

### `Tau.BookIII.Sectors.bti_additive_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L140-L153)@[irreducible]

**def
Tau.BookIII.Sectors.bti_additive_check.go
(bound db : Denotation.TauIdx)

(m1 m2 x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.boundary_char_3_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L179-L180)
**theorem
Tau.BookIII.Sectors.boundary_char_3_3 :boundary_char_check 3 3 = true**


---

### `Tau.BookIII.Sectors.bti_functor_5_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L183-L184)
**theorem
Tau.BookIII.Sectors.bti_functor_5_3 :bti_functor_check 5 3 = true**


---

### `Tau.BookIII.Sectors.bti_additive_3_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L187-L188)
**theorem
Tau.BookIII.Sectors.bti_additive_3_3 :bti_additive_check 3 3 = true**


---

### `Tau.BookIII.Sectors.zero_char_eval`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L194-L198)
**theorem
Tau.BookIII.Sectors.zero_char_eval
(x k : Denotation.TauIdx)
 :BoundaryCharacter.zero.eval x k = 0**


[III.D11] Structural: zero character evaluates to zero.

---

### `Tau.BookIII.Sectors.neg_neg_char`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L200-L203)
**theorem
Tau.BookIII.Sectors.neg_neg_char
(χ : BoundaryCharacter)
 :χ.neg.neg = χ**


[III.D11] Structural: character negation is an involution.

---

### `Tau.BookIII.Sectors.bti_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIII/Sectors/BoundaryCharacters.lean#L205-L210)
**theorem
Tau.BookIII.Sectors.bti_zero
(x k : Denotation.TauIdx)
 :boundary_to_interior BoundaryCharacter.zero x k = 0**


[III.D12] Structural: BTI of trivial character is zero.
Φ(0)(x, k) = reduce(0, k) = 0.
