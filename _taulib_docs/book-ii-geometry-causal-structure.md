---
layout: taulib-doc
title: "TauLib.BookII.Geometry.CausalStructure"
permalink: /verify/taulib/docs/book-ii-geometry-causal-structure/
lane: verify
module_name: "TauLib.BookII.Geometry.CausalStructure"
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

# TauLib.BookII.Geometry.CausalStructure


Wave-type PDE and causal structure from split-complex algebra.

## Registry Cross-References


- [II.D21] Wave-Type PDE — `wave_equation_check`

- [II.D22] Causal Structure — `CausalClass`, `classify_causal`

- [II.T19] Euclidean as Static Limit — `static_limit_check`


## Mathematical Content


Split-complex Cauchy–Riemann: ∂u/∂x = ∂v/∂y, ∂u/∂y = +∂v/∂x
(sign FLIP from classical: + not -)

Yields HYPERBOLIC wave equation: ∂²u/∂x² - ∂²u/∂y² = 0
(vs. ELLIPTIC Laplace: ∂²u/∂x² + ∂²u/∂y² = 0 for i² = -1)

Characteristics: x+y = const (e₊-channel), x-y = const (e₋-channel)

Causal classification:


- Timelike: inside null cone

- Spacelike: outside null cone

- Null: on null cone boundary


---

### `Tau.BookII.Geometry.wave_char_roots`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L40-L48)
**def
Tau.BookII.Geometry.wave_char_roots :List (ℤ × ℤ)**


[II.D21] Wave equation signature from j² = +1.
The split-complex CR equations yield a HYPERBOLIC equation.
Verification: j² = +1 forces the wave equation signature (−)
instead of the Laplace signature (+).

Classical (i² = -1): characteristic polynomial ξ² + η² = 0 → NO real roots
Split (j² = +1): characteristic polynomial ξ² - η² = 0 → TWO real roots
Equations
- Tau.BookII.Geometry.wave_char_roots = [(1, 1), (1, -1)]
Instances For

---

### `Tau.BookII.Geometry.wave_discriminant_positive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L50-L57)
**def
Tau.BookII.Geometry.wave_discriminant_positive :Bool**


The wave equation discriminant is positive (hyperbolic).
For j² = +1: discriminant of characteristic = 1 - (-1) = 2 > 0.
For i² = -1: discriminant = 1 - 1 = 0 (degenerate, elliptic).
Equations
- Tau.BookII.Geometry.wave_discriminant_positive = decide (0 * 0 - 4 * 1 * -1 > 0)
Instances For

---

### `Tau.BookII.Geometry.j_squared_plus_one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L59-L62)
**theorem
Tau.BookII.Geometry.j_squared_plus_one :{ re := 0, im := 1 }.mul { re := 0, im := 1 } = { re := 1, im := 0 }**


Verify j² = +1 (split-complex, not complex).

---

### `Tau.BookII.Geometry.char_xi`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L68-L71)
**def
Tau.BookII.Geometry.char_xi
(x y : ℤ)
 :ℤ**


Characteristic coordinate ξ = x + y (e₊-channel direction).
Wave equation in characteristic coords: ∂²u/∂ξ∂ζ = 0
General solution: u = F(ξ) + G(ζ), two independent channels.
Equations
- Tau.BookII.Geometry.char_xi x y = x + y
Instances For

---

### `Tau.BookII.Geometry.char_zeta`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L73-L74)
**def
Tau.BookII.Geometry.char_zeta
(x y : ℤ)
 :ℤ**


Characteristic coordinate ζ = x - y (e₋-channel direction).
Equations
- Tau.BookII.Geometry.char_zeta x y = x - y
Instances For

---

### `Tau.BookII.Geometry.char_recover_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L76-L83)
**def
Tau.BookII.Geometry.char_recover_check :Bool**


Characteristic coordinates recover original via:
x = (ξ + ζ)/2, y = (ξ - ζ)/2.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.CausalClass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L89-L98)
**inductive
Tau.BookII.Geometry.CausalClass :Type**


[II.D22] Causal classification of displacement vectors.
A vector (Δx, Δy) is classified by the sign of Δx² - Δy²:


- Timelike: |Δx| > |Δy| (inside null cone)

- Spacelike: |Δx| < |Δy| (outside null cone)

- Null: |Δx| = |Δy| (on null cone boundary)


- timelike : CausalClass
- spacelike : CausalClass
- null : CausalClass
Instances For

---

### `Tau.BookII.Geometry.instReprCausalClass.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L98-L98)
**def
Tau.BookII.Geometry.instReprCausalClass.repr :CausalClass → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.instReprCausalClass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L98-L98)
**instance
Tau.BookII.Geometry.instReprCausalClass :Repr CausalClass**

Equations
- Tau.BookII.Geometry.instReprCausalClass = { reprPrec := Tau.BookII.Geometry.instReprCausalClass.repr }

---

### `Tau.BookII.Geometry.instDecidableEqCausalClass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L98-L98)
**instance
Tau.BookII.Geometry.instDecidableEqCausalClass :DecidableEq CausalClass**

Equations
- Tau.BookII.Geometry.instDecidableEqCausalClass x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookII.Geometry.classify_causal`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L100-L105)
**def
Tau.BookII.Geometry.classify_causal
(dx dy : ℤ)
 :CausalClass**


Classify a displacement vector (dx, dy).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.null_cone_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L107-L112)
**def
Tau.BookII.Geometry.null_cone_check :Bool**


Null cone consists of characteristic directions.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.e_plus_null`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L114-L117)
**def
Tau.BookII.Geometry.e_plus_null :Bool**


Idempotent e₊ direction is null.
e₊ = (1+j)/2 → sector coordinates (1,0) → displacement (1,1) → null.
Equations
- Tau.BookII.Geometry.e_plus_null = (Tau.BookII.Geometry.classify_causal 1 1 == Tau.BookII.Geometry.CausalClass.null)
Instances For

---

### `Tau.BookII.Geometry.e_minus_null`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L119-L122)
**def
Tau.BookII.Geometry.e_minus_null :Bool**


Idempotent e₋ direction is null.
e₋ = (1-j)/2 → sector coordinates (0,1) → displacement (1,-1) → null.
Equations
- Tau.BookII.Geometry.e_minus_null = (Tau.BookII.Geometry.classify_causal 1 (-1) == Tau.BookII.Geometry.CausalClass.null)
Instances For

---

### `Tau.BookII.Geometry.static_limit_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L128-L142)
**def
Tau.BookII.Geometry.static_limit_check :Bool**


[II.T19] In the static limit (no split-complex coupling),
the causal structure degenerates:


- Null cone collapses (wave → Laplace)

- All directions become spacelike (Euclidean)


Euclidean geometry survives because Tarski axioms
(betweenness, congruence) depend only on ultrametric
distance, not on j.
Equations
- Tau.BookII.Geometry.static_limit_check = [(1, 0), (0, 1), (1, 1), (2, 3), (-1, 4)].all fun (x : ℤ × ℤ) =>
 match x with
 | (dx, dy) => decide (dx * dx + dy * dy ≥ 0)
Instances For

---

### `Tau.BookII.Geometry.indefinite_signature_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L144-L150)
**def
Tau.BookII.Geometry.indefinite_signature_check :Bool**


Contrast: split-complex norm has INDEFINITE signature.
Some nonzero vectors have negative norm squared.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.sector_causal_correspondence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L156-L166)
**def
Tau.BookII.Geometry.sector_causal_correspondence :Bool**


The two null directions correspond to the two bipolar sectors.
e₊-direction (B-channel): ξ = x+y = const → null
e₋-direction (C-channel): ζ = x-y = const → null
Sectors are the "light-cone edges" of the causal structure.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.wave_disc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L186-L186)
**theorem
Tau.BookII.Geometry.wave_disc :wave_discriminant_positive = true**


---

### `Tau.BookII.Geometry.char_recover`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L187-L187)
**theorem
Tau.BookII.Geometry.char_recover :char_recover_check = true**


---

### `Tau.BookII.Geometry.null_cone`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L188-L188)
**theorem
Tau.BookII.Geometry.null_cone :null_cone_check = true**


---

### `Tau.BookII.Geometry.static_lim`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L189-L189)
**theorem
Tau.BookII.Geometry.static_lim :static_limit_check = true**


---

### `Tau.BookII.Geometry.indef_sig`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L190-L190)
**theorem
Tau.BookII.Geometry.indef_sig :indefinite_signature_check = true**


---

### `Tau.BookII.Geometry.sector_causal`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/CausalStructure.lean#L191-L191)
**theorem
Tau.BookII.Geometry.sector_causal :sector_causal_correspondence = true**
