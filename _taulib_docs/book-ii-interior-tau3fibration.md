---
layout: taulib-doc
title: "TauLib.BookII.Interior.Tau3Fibration"
permalink: /verify/taulib/docs/book-ii-interior-tau3fibration/
lane: verify
module_name: "TauLib.BookII.Interior.Tau3Fibration"
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

# TauLib.BookII.Interior.Tau3Fibration


The τ³ fibration: τ³ = τ¹ ×_f T² as a fibered product.

## Registry Cross-References


- [II.D05] Base τ¹ — `BaseTau1`

- [II.D06] Fiber T² — `FiberT2`

- [II.D07] Fibered Product τ³ — `Tau3`, `tau3_proj`, `tau3_fiber_proj`

- [II.T03] Fibration Structure — `proj_surjective_check`, `non_trivial_check`


## Mathematical Content


The ABCD chart decomposes into base and fiber:


- Base τ¹ = { (D, A) : A ∈ ℙ_τ ∪ {1}, prime factors of D < A }

- Fiber T² = { (B, C) : B, C ≥ 0 }

- τ³ = τ¹ ×_f T²: fibered product (NOT Cartesian)


Two reasons τ³ ≠ τ¹ × T²:

- Peel-order coupling: prime factors of D must be < A

- Base-to-fiber coupling: admissible (B,C) depends on (D,A)


Fibration structure (II.T03):

- pr : τ³ → τ¹ is surjective (every base point has fiber B=1,C=0)

- Fibers vary (different A yield different admissible ranges)

- Not a product bundle (peel-order constraint)

- Faithful (Φ : Obj(τ) → τ³ is injective, by I.T04)


---

### `Tau.BookII.Interior.BaseTau1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L41-L47)
**structure
Tau.BookII.Interior.BaseTau1 :Type**


[II.D05] Base τ¹: the (D, A) coordinate space.
D = radial depth (α-channel), A = prime direction (π-channel).
Constraint: A ∈ ℙ_τ ∪ {1}, all prime factors of D < A.

- d : Denotation.TauIdx
- a : Denotation.TauIdx
Instances For

---

### `Tau.BookII.Interior.instReprBaseTau1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L47-L47)
**instance
Tau.BookII.Interior.instReprBaseTau1 :Repr BaseTau1**

Equations
- Tau.BookII.Interior.instReprBaseTau1 = { reprPrec := Tau.BookII.Interior.instReprBaseTau1.repr }

---

### `Tau.BookII.Interior.instReprBaseTau1.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L47-L47)
**def
Tau.BookII.Interior.instReprBaseTau1.repr :BaseTau1 → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.instDecidableEqBaseTau1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L47-L47)
**instance
Tau.BookII.Interior.instDecidableEqBaseTau1 :DecidableEq BaseTau1**

Equations
- Tau.BookII.Interior.instDecidableEqBaseTau1 = Tau.BookII.Interior.instDecidableEqBaseTau1.decEq

---

### `Tau.BookII.Interior.instDecidableEqBaseTau1.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L47-L47)
**def
Tau.BookII.Interior.instDecidableEqBaseTau1.decEq
(x✝ x✝¹ : BaseTau1)
 :Decidable (x✝ = x✝¹)**

Equations
- Tau.BookII.Interior.instDecidableEqBaseTau1.decEq { d := a, a := a_1 } { d := b, a := b_1 } = if h : a = b then h ▸ if h : a_1 = b_1 then h ▸ isTrue ⋯ else isFalse ⋯ else isFalse ⋯
Instances For

---

### `Tau.BookII.Interior.BaseTau1.valid`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L49-L51)
**def
Tau.BookII.Interior.BaseTau1.valid
(b : BaseTau1)
 :Bool**


Validity check for base point.
Equations
- b.valid = (Tau.BookII.Interior.constraint_C1 b.a && Tau.BookII.Interior.constraint_C3 b.d b.a)
Instances For

---

### `Tau.BookII.Interior.FiberT2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L57-L64)
**structure
Tau.BookII.Interior.FiberT2 :Type**


[II.D06] Fiber T²: the (B, C) coordinate space.
B = exponent (γ-channel), C = tetration height (η-channel).
Both non-negative (automatic for ℕ).
Notation T² anticipates torus-like winding structure (Book II Part III).

- b : Denotation.TauIdx
- c : Denotation.TauIdx
Instances For

---

### `Tau.BookII.Interior.instReprFiberT2.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L64-L64)
**def
Tau.BookII.Interior.instReprFiberT2.repr :FiberT2 → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.instReprFiberT2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L64-L64)
**instance
Tau.BookII.Interior.instReprFiberT2 :Repr FiberT2**

Equations
- Tau.BookII.Interior.instReprFiberT2 = { reprPrec := Tau.BookII.Interior.instReprFiberT2.repr }

---

### `Tau.BookII.Interior.instDecidableEqFiberT2.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L64-L64)
**def
Tau.BookII.Interior.instDecidableEqFiberT2.decEq
(x✝ x✝¹ : FiberT2)
 :Decidable (x✝ = x✝¹)**

Equations
- Tau.BookII.Interior.instDecidableEqFiberT2.decEq { b := a, c := a_1 } { b := b, c := b_1 } = if h : a = b then h ▸ if h : a_1 = b_1 then h ▸ isTrue ⋯ else isFalse ⋯ else isFalse ⋯
Instances For

---

### `Tau.BookII.Interior.instDecidableEqFiberT2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L64-L64)
**instance
Tau.BookII.Interior.instDecidableEqFiberT2 :DecidableEq FiberT2**

Equations
- Tau.BookII.Interior.instDecidableEqFiberT2 = Tau.BookII.Interior.instDecidableEqFiberT2.decEq

---

### `Tau.BookII.Interior.Tau3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L70-L75)
**structure
Tau.BookII.Interior.Tau3 :Type**


[II.D07] τ³ = τ¹ ×_f T²: the fibered product.
A τ-admissible quadruple viewed as base + fiber.

- base : BaseTau1
- fiber : FiberT2
Instances For

---

### `Tau.BookII.Interior.instReprTau3.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L75-L75)
**def
Tau.BookII.Interior.instReprTau3.repr :Tau3 → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.instReprTau3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L75-L75)
**instance
Tau.BookII.Interior.instReprTau3 :Repr Tau3**

Equations
- Tau.BookII.Interior.instReprTau3 = { reprPrec := Tau.BookII.Interior.instReprTau3.repr }

---

### `Tau.BookII.Interior.instDecidableEqTau3.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L75-L75)
**def
Tau.BookII.Interior.instDecidableEqTau3.decEq
(x✝ x✝¹ : Tau3)
 :Decidable (x✝ = x✝¹)**

Equations
- Tau.BookII.Interior.instDecidableEqTau3.decEq { base := a, fiber := a_1 } { base := b, fiber := b_1 } = if h : a = b then h ▸ if h : a_1 = b_1 then h ▸ isTrue ⋯ else isFalse ⋯ else isFalse ⋯
Instances For

---

### `Tau.BookII.Interior.instDecidableEqTau3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L75-L75)
**instance
Tau.BookII.Interior.instDecidableEqTau3 :DecidableEq Tau3**

Equations
- Tau.BookII.Interior.instDecidableEqTau3 = Tau.BookII.Interior.instDecidableEqTau3.decEq

---

### `Tau.BookII.Interior.to_tau3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L77-L79)
**def
Tau.BookII.Interior.to_tau3
(p : TauAdmissiblePoint)
 :Tau3**


Convert TauAdmissiblePoint to Tau3 (fibered product form).
Equations
- Tau.BookII.Interior.to_tau3 p = { base := { d := p.d, a := p.a }, fiber := { b := p.b, c := p.c } }
Instances For

---

### `Tau.BookII.Interior.from_tau3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L81-L83)
**def
Tau.BookII.Interior.from_tau3
(t : Tau3)
 :TauAdmissiblePoint**


Convert Tau3 back to TauAdmissiblePoint.
Equations
- Tau.BookII.Interior.from_tau3 t = { a := t.base.a, b := t.fiber.b, c := t.fiber.c, d := t.base.d }
Instances For

---

### `Tau.BookII.Interior.tau3_proj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L85-L86)
**def
Tau.BookII.Interior.tau3_proj
(t : Tau3)
 :BaseTau1**


Projection pr : τ³ → τ¹.
Equations
- Tau.BookII.Interior.tau3_proj t = t.base
Instances For

---

### `Tau.BookII.Interior.tau3_fiber_proj`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L88-L89)
**def
Tau.BookII.Interior.tau3_fiber_proj
(t : Tau3)
 :FiberT2**


Fiber projection: τ³ → T².
Equations
- Tau.BookII.Interior.tau3_fiber_proj t = t.fiber
Instances For

---

### `Tau.BookII.Interior.tau3_round_trip`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L95-L98)
**theorem
Tau.BookII.Interior.tau3_round_trip
(p : TauAdmissiblePoint)
 :from_tau3 (to_tau3 p) = p**


from_tau3 ∘ to_tau3 = id.

---

### `Tau.BookII.Interior.tau3_round_trip'`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L100-L103)
**theorem
Tau.BookII.Interior.tau3_round_trip'
(t : Tau3)
 :to_tau3 (from_tau3 t) = t**


to_tau3 ∘ from_tau3 = id.

---

### `Tau.BookII.Interior.proj_surjective_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L109-L121)
**def
Tau.BookII.Interior.proj_surjective_check
(bound : Denotation.TauIdx)
 :Bool**


[II.T03, clause 1] Surjectivity: every valid base point admits
at least one fiber point (B=1, C=0 is always admissible).
Equations
- Tau.BookII.Interior.proj_surjective_check bound = Tau.BookII.Interior.proj_surjective_check.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Interior.proj_surjective_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L114-L120)@[irreducible]

**def
Tau.BookII.Interior.proj_surjective_check.go
(bound : Denotation.TauIdx)

(x fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.non_trivial_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L123-L142)
**def
Tau.BookII.Interior.non_trivial_check :Bool**


[II.T03, clause 3] Non-triviality: demonstrate that the fibration
is NOT a product bundle by showing different base points yield
different fiber behavior.

Example: X=12 has (A=3, D=4) while X=64 has (A=2, D=1).
At A=3: B can be up to what 3^B allows.
At A=2: B can be up to what 2^B allows (different range).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.faithful_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L144-L156)
**def
Tau.BookII.Interior.faithful_check
(bound : Denotation.TauIdx)
 :Bool**


[II.T03, clause 4] Faithfulness: Φ is injective.
Different X values produce different ABCD quadruples.
Equations
- Tau.BookII.Interior.faithful_check bound = Tau.BookII.Interior.faithful_check.go bound 2 (bound + 1) []
Instances For

---

### `Tau.BookII.Interior.faithful_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L149-L155)@[irreducible]

**def
Tau.BookII.Interior.faithful_check.go
(bound : Denotation.TauIdx)

(x fuel : Nat)

(seen : List TauAdmissiblePoint)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Interior.surjective_2_to_20`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L177-L177)
**theorem
Tau.BookII.Interior.surjective_2_to_20 :proj_surjective_check 20 = true**


---

### `Tau.BookII.Interior.faithful_2_to_50`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Interior/Tau3Fibration.lean#L178-L178)
**theorem
Tau.BookII.Interior.faithful_2_to_50 :faithful_check 50 = true**
