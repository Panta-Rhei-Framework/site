---
layout: taulib-doc
title: "TauLib.BookII.Topology.TorusDegeneration"
permalink: /verify/taulib/docs/book-ii-topology-torus-degeneration/
lane: verify
module_name: "TauLib.BookII.Topology.TorusDegeneration"
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

# TauLib.BookII.Topology.TorusDegeneration


Torus degeneration T² → ℒ = S¹∨S¹ via the pinch map.

## Registry Cross-References


- [II.D18] Pinch Map — `pinch_fiber`

- [II.T13] Torus Degeneration Theorem — `pinch_surjective_check`

- [II.T14] Fundamental Group Degeneration — `fund_group_check`


## Mathematical Content


The pinch map p : T² → ℒ collapses the diagonal Δ = {(θ,θ)} ⊂ T²
to the wedge point, producing the geometric lemniscate ℒ = S¹∨S¹.

The map is the unique continuous surjection preserving both gauge
factors U(1)_γ and U(1)_η while reducing dimension by 1.

Fundamental group degeneration:
π₁(T²) = ℤ² → π₁(ℒ) = F₂
The abelian fundamental group becomes free non-abelian (richer!).

---

### `Tau.BookII.Topology.PinchImage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Topology/TorusDegeneration.lean#L36-L43)
**inductive
Tau.BookII.Topology.PinchImage :Type**


Fiber classification under the pinch map.
At finite depth, (B,C) lives in T² = ℤ × ℤ.
The pinch map collapses the diagonal (B = C) to the wedge point.

- plus_lobe : ℤ → PinchImage
- minus_lobe : ℤ → PinchImage
- wedge : PinchImage
Instances For

---

### `Tau.BookII.Topology.instReprPinchImage.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Topology/TorusDegeneration.lean#L43-L43)
**def
Tau.BookII.Topology.instReprPinchImage.repr :PinchImage → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.instReprPinchImage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Topology/TorusDegeneration.lean#L43-L43)
**instance
Tau.BookII.Topology.instReprPinchImage :Repr PinchImage**

Equations
- Tau.BookII.Topology.instReprPinchImage = { reprPrec := Tau.BookII.Topology.instReprPinchImage.repr }

---

### `Tau.BookII.Topology.instDecidableEqPinchImage.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Topology/TorusDegeneration.lean#L43-L43)
**def
Tau.BookII.Topology.instDecidableEqPinchImage.decEq
(x✝ x✝¹ : PinchImage)
 :Decidable (x✝ = x✝¹)**

Equations
- Tau.BookII.Topology.instDecidableEqPinchImage.decEq (Tau.BookII.Topology.PinchImage.plus_lobe a)
 (Tau.BookII.Topology.PinchImage.plus_lobe b) = if h : a = b then h ▸ isTrue ⋯ else isFalse ⋯
- Tau.BookII.Topology.instDecidableEqPinchImage.decEq (Tau.BookII.Topology.PinchImage.plus_lobe a)
 (Tau.BookII.Topology.PinchImage.minus_lobe a_1) = isFalse ⋯
- Tau.BookII.Topology.instDecidableEqPinchImage.decEq (Tau.BookII.Topology.PinchImage.plus_lobe a)
 Tau.BookII.Topology.PinchImage.wedge = isFalse ⋯
- Tau.BookII.Topology.instDecidableEqPinchImage.decEq (Tau.BookII.Topology.PinchImage.minus_lobe a)
 (Tau.BookII.Topology.PinchImage.plus_lobe a_1) = isFalse ⋯
- Tau.BookII.Topology.instDecidableEqPinchImage.decEq (Tau.BookII.Topology.PinchImage.minus_lobe a)
 (Tau.BookII.Topology.PinchImage.minus_lobe b) = if h : a = b then h ▸ isTrue ⋯ else isFalse ⋯
- Tau.BookII.Topology.instDecidableEqPinchImage.decEq (Tau.BookII.Topology.PinchImage.minus_lobe a)
 Tau.BookII.Topology.PinchImage.wedge = isFalse ⋯
- Tau.BookII.Topology.instDecidableEqPinchImage.decEq Tau.BookII.Topology.PinchImage.wedge
 (Tau.BookII.Topology.PinchImage.plus_lobe a) = isFalse ⋯
- Tau.BookII.Topology.instDecidableEqPinchImage.decEq Tau.BookII.Topology.PinchImage.wedge
 (Tau.BookII.Topology.PinchImage.minus_lobe a) = isFalse ⋯
- Tau.BookII.Topology.instDecidableEqPinchImage.decEq Tau.BookII.Topology.PinchImage.wedge
 Tau.BookII.Topology.PinchImage.wedge = isTrue ⋯
Instances For

---

### `Tau.BookII.Topology.instDecidableEqPinchImage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Topology/TorusDegeneration.lean#L43-L43)
**instance
Tau.BookII.Topology.instDecidableEqPinchImage :DecidableEq PinchImage**

Equations
- Tau.BookII.Topology.instDecidableEqPinchImage = Tau.BookII.Topology.instDecidableEqPinchImage.decEq

---

### `Tau.BookII.Topology.pinch_fiber`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Topology/TorusDegeneration.lean#L45-L50)
**def
Tau.BookII.Topology.pinch_fiber
(b c : Denotation.TauIdx)
 :PinchImage**


[II.D18] The pinch map on fiber coordinates (B, C):
(B, C) ↦ wedge if B = C, else lobe by dominance.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.pinch_point`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Topology/TorusDegeneration.lean#L52-L55)
**def
Tau.BookII.Topology.pinch_point
(x : Denotation.TauIdx)
 :PinchImage**


Apply pinch map to a τ-admissible point.
Equations
- Tau.BookII.Topology.pinch_point x = Tau.BookII.Topology.pinch_fiber (Tau.BookII.Interior.from_tau_idx x).b (Tau.BookII.Interior.from_tau_idx x).c
Instances For

---

### `Tau.BookII.Topology.pinch_surjective_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Topology/TorusDegeneration.lean#L61-L84)
**def
Tau.BookII.Topology.pinch_surjective_check :Bool**


[II.T13] The pinch map is surjective: all three regions
(plus lobe, minus lobe, wedge) are hit.
Evidence: exhibit witnesses for each.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.pinch_surjective_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Topology/TorusDegeneration.lean#L78-L83)@[irreducible]

**def
Tau.BookII.Topology.pinch_surjective_check.go
(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.gauge_survival_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Topology/TorusDegeneration.lean#L86-L98)
**def
Tau.BookII.Topology.gauge_survival_check :Bool**


Gauge survival: both B and C channels act independently.
B-rotation shifts plus lobe parameter; C-rotation shifts minus lobe.
Evidence: varying B alone changes lobe parameter while C is fixed.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.fund_group_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Topology/TorusDegeneration.lean#L104-L128)
**def
Tau.BookII.Topology.fund_group_check :Bool**


[II.T14] Fundamental group degeneration: ℤ² → F₂.

At finite depth: π₁(T²) = ℤ² (commutative).
At boundary: π₁(ℒ) = F₂ (free, non-commutative).

Evidence: B and C loops commute at finite depth
but become non-commuting free generators at boundary.

The F₂ property is witnessed by the bipolar orthogonality:
e₊ and e₋ project onto independent lobes, and the sector
product e₊ · e₋ = 0 (they cannot be composed into one loop).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.pinch_distribution`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Topology/TorusDegeneration.lean#L134-L145)
**def
Tau.BookII.Topology.pinch_distribution
(bound : Denotation.TauIdx)
 :ℕ × ℕ × ℕ**


Count pinch image distribution in range [2, bound].
Equations
- Tau.BookII.Topology.pinch_distribution bound = Tau.BookII.Topology.pinch_distribution.go bound 2 (bound + 1) 0 0 0
Instances For

---

### `Tau.BookII.Topology.pinch_distribution.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Topology/TorusDegeneration.lean#L138-L144)@[irreducible]

**def
Tau.BookII.Topology.pinch_distribution.go
(bound : Denotation.TauIdx)

(x fuel plus minus wedge : ℕ)
 :ℕ × ℕ × ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.pinch_surj`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Topology/TorusDegeneration.lean#L162-L162)
**theorem
Tau.BookII.Topology.pinch_surj :pinch_surjective_check = true**


---

### `Tau.BookII.Topology.gauge_surv`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Topology/TorusDegeneration.lean#L163-L163)
**theorem
Tau.BookII.Topology.gauge_surv :gauge_survival_check = true**


---

### `Tau.BookII.Topology.fund_group`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Topology/TorusDegeneration.lean#L164-L164)
**theorem
Tau.BookII.Topology.fund_group :fund_group_check = true**
