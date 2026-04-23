---
layout: taulib-doc
title: "TauLib.BookII.Geometry.OrthodoxBridge"
permalink: /verify/taulib/docs/book-ii-geometry-orthodox-bridge/
lane: verify
module_name: "TauLib.BookII.Geometry.OrthodoxBridge"
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

# TauLib.BookII.Geometry.OrthodoxBridge


Approximation sequences and denotation-to-geometry bridge.

## Registry Cross-References


- [II.D23] Approximation Sequence — `approx_seq`

- [II.R07] Orthodox Denotation Bridge — remark (structural observation)


## Mathematical Content


**Approximation Sequence (II.D23):**
The stage-k approximation of x is reduce(x, k) = x mod M_k. The sequence
(approx_seq x 1, approx_seq x 2, ...) is Cauchy in the ultrametric: for
k₂ > k₁, the stage-k₁ projections of stages k₁ and k₂ agree.

This is the inverse system compatibility: reduce(reduce(x, k₂), k₁) = reduce(x, k₁).

**Denotation Map Properties:**
The ABCD denotation Phi: TauIdx -> tau-cubed is compatible with the Tarski geometry:

- Cauchy: approximation sequences are Cauchy in the ultrametric

- Injective: distinct indices eventually separate under reduction

- Geometric: betweenness is preserved by approximation (monotone)


This establishes the bridge from the earned denotation (Book I) to the
orthodox geometry (Tarski axioms) -- the two descriptions of the same space
are compatible. The Tarski model earned in Part IV sits on top of the
profinite topology from Part III.

---

### `Tau.BookII.Geometry.approx_seq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L42-L44)
**def
Tau.BookII.Geometry.approx_seq
(x k : Denotation.TauIdx)
 :Denotation.TauIdx**


[II.D23] The stage-k approximation of x: CRT reduction to stage k.
This is the canonical projection pi_k(x) = x mod M_k.
Equations
- Tau.BookII.Geometry.approx_seq x k = Tau.Polarity.reduce x k
Instances For

---

### `Tau.BookII.Geometry.approx_stabilizes`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L46-L57)
**def
Tau.BookII.Geometry.approx_stabilizes
(x stages : Denotation.TauIdx)
 :Bool**


The approximation sequence stabilizes at the point itself:
for k large enough, reduce x k = x (when x < M_k).
Equations
- Tau.BookII.Geometry.approx_stabilizes x stages = Tau.BookII.Geometry.approx_stabilizes.go x stages 1 (stages + 1)
Instances For

---

### `Tau.BookII.Geometry.approx_stabilizes.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L51-L56)@[irreducible]

**def
Tau.BookII.Geometry.approx_stabilizes.go
(x stages : Denotation.TauIdx)

(k fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.cauchy_check_k2`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L63-L73)
**def
Tau.BookII.Geometry.cauchy_check_k2
(x k1 stages : Denotation.TauIdx)
 :Bool**


Inner loop: check reduce(reduce(x, k₂), k₁) = reduce(x, k₁) for all k₂ > k₁.
Equations
- Tau.BookII.Geometry.cauchy_check_k2 x k1 stages = Tau.BookII.Geometry.cauchy_check_k2.go x k1 stages (k1 + 1) (stages + 1)
Instances For

---

### `Tau.BookII.Geometry.cauchy_check_k2.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L67-L72)@[irreducible]

**def
Tau.BookII.Geometry.cauchy_check_k2.go
(x k1 stages : Denotation.TauIdx)

(k2 fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.cauchy_check_k1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L75-L84)
**def
Tau.BookII.Geometry.cauchy_check_k1
(x stages : Denotation.TauIdx)
 :Bool**


Inner loop: iterate over k₁ for fixed x.
Equations
- Tau.BookII.Geometry.cauchy_check_k1 x stages = Tau.BookII.Geometry.cauchy_check_k1.go x stages 1 (stages + 1)
Instances For

---

### `Tau.BookII.Geometry.cauchy_check_k1.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L79-L83)@[irreducible]

**def
Tau.BookII.Geometry.cauchy_check_k1.go
(x stages : Denotation.TauIdx)

(k1 fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.den_cauchy_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L86-L97)
**def
Tau.BookII.Geometry.den_cauchy_check
(bound stages : Denotation.TauIdx)
 :Bool**


Cauchy property: for all x in [2, bound] and k₂ > k₁,
reduce(reduce(x, k₂), k₁) = reduce(x, k₁).
This is the inverse system compatibility from ModArith.
Equations
- Tau.BookII.Geometry.den_cauchy_check bound stages = Tau.BookII.Geometry.den_cauchy_check.go bound stages 2 (bound + 1)
Instances For

---

### `Tau.BookII.Geometry.den_cauchy_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L92-L96)@[irreducible]

**def
Tau.BookII.Geometry.den_cauchy_check.go
(bound stages : Denotation.TauIdx)

(x fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.find_separating_stage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L103-L112)
**def
Tau.BookII.Geometry.find_separating_stage
(x y stages : Denotation.TauIdx)
 :Bool**


Find the first stage k where reduce x k != reduce y k.
Equations
- Tau.BookII.Geometry.find_separating_stage x y stages = Tau.BookII.Geometry.find_separating_stage.go x y stages 1 (stages + 1)
Instances For

---

### `Tau.BookII.Geometry.find_separating_stage.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L107-L111)@[irreducible]

**def
Tau.BookII.Geometry.find_separating_stage.go
(x y stages : Denotation.TauIdx)

(k fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.injective_check_y`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L114-L123)
**def
Tau.BookII.Geometry.injective_check_y
(x bound stages : Denotation.TauIdx)
 :Bool**


Inner loop: for fixed x, check all y > x are separable.
Equations
- Tau.BookII.Geometry.injective_check_y x bound stages = Tau.BookII.Geometry.injective_check_y.go x bound stages (x + 1) (bound + 1)
Instances For

---

### `Tau.BookII.Geometry.injective_check_y.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L118-L122)@[irreducible]

**def
Tau.BookII.Geometry.injective_check_y.go
(x bound stages : Denotation.TauIdx)

(y fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.den_injective_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L125-L135)
**def
Tau.BookII.Geometry.den_injective_check
(bound stages : Denotation.TauIdx)
 :Bool**


Injective: for x != y in [2, bound], there exists k <= stages
such that reduce x k != reduce y k.
Equations
- Tau.BookII.Geometry.den_injective_check bound stages = Tau.BookII.Geometry.den_injective_check.go bound stages 2 (bound + 1)
Instances For

---

### `Tau.BookII.Geometry.den_injective_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L130-L134)@[irreducible]

**def
Tau.BookII.Geometry.den_injective_check.go
(bound stages : Denotation.TauIdx)

(x fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.between_mono_stages`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L141-L155)
**def
Tau.BookII.Geometry.between_mono_stages
(x y z db stages : Denotation.TauIdx)
 :Bool**


Check betweenness preservation at each stage for a fixed triple.
Equations
- Tau.BookII.Geometry.between_mono_stages x y z db stages = Tau.BookII.Geometry.between_mono_stages.go x y z db stages 1 (stages + 1)
Instances For

---

### `Tau.BookII.Geometry.between_mono_stages.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L145-L154)@[irreducible]

**def
Tau.BookII.Geometry.between_mono_stages.go
(x y z db stages : Denotation.TauIdx)

(k fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.between_mono_z`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L157-L168)
**def
Tau.BookII.Geometry.between_mono_z
(x y bound db stages : Denotation.TauIdx)
 :Bool**


Inner loop: iterate over z for fixed x, y.
Equations
- Tau.BookII.Geometry.between_mono_z x y bound db stages = Tau.BookII.Geometry.between_mono_z.go x y bound db stages 2 (bound + 1)
Instances For

---

### `Tau.BookII.Geometry.between_mono_z.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L161-L167)@[irreducible]

**def
Tau.BookII.Geometry.between_mono_z.go
(x y bound db stages : Denotation.TauIdx)

(z fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.between_mono_y`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L170-L179)
**def
Tau.BookII.Geometry.between_mono_y
(x bound db stages : Denotation.TauIdx)
 :Bool**


Inner loop: iterate over y for fixed x.
Equations
- Tau.BookII.Geometry.between_mono_y x bound db stages = Tau.BookII.Geometry.between_mono_y.go x bound db stages 2 (bound + 1)
Instances For

---

### `Tau.BookII.Geometry.between_mono_y.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L174-L178)@[irreducible]

**def
Tau.BookII.Geometry.between_mono_y.go
(x bound db stages : Denotation.TauIdx)

(y fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.den_between_mono_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L181-L192)
**def
Tau.BookII.Geometry.den_between_mono_check
(bound db stages : Denotation.TauIdx)
 :Bool**


Betweenness monotonicity: if B(x,y,z) at full resolution,
then B(reduce x k, reduce y k, reduce z k) at stage k.
Approximation preserves the tree structure.
Equations
- Tau.BookII.Geometry.den_between_mono_check bound db stages = Tau.BookII.Geometry.den_between_mono_check.go bound db stages 2 (bound + 1)
Instances For

---

### `Tau.BookII.Geometry.den_between_mono_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L187-L191)@[irreducible]

**def
Tau.BookII.Geometry.den_between_mono_check.go
(bound db stages : Denotation.TauIdx)

(x fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.cong_compat_stages`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L198-L213)
**def
Tau.BookII.Geometry.cong_compat_stages
(a b c d db : Denotation.TauIdx)
 :Bool**


Check congruence preservation at each stage for a fixed quadruple.
Equations
- Tau.BookII.Geometry.cong_compat_stages a b c d db = Tau.BookII.Geometry.cong_compat_stages.go a b c d db 1 4
Instances For

---

### `Tau.BookII.Geometry.cong_compat_stages.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L202-L212)@[irreducible]

**def
Tau.BookII.Geometry.cong_compat_stages.go
(a b c d db : Denotation.TauIdx)

(k fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.den_cong_compat_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L215-L220)
**def
Tau.BookII.Geometry.den_cong_compat_check
(db : Denotation.TauIdx)
 :Bool**


Spot check: congruence compatibility for selected point quadruples.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.orthodox_bridge_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L226-L232)
**def
Tau.BookII.Geometry.orthodox_bridge_check
(bound db stages : Denotation.TauIdx)
 :Bool**


[II.R07] Orthodox denotation bridge: the full compatibility check.
The earned denotation (ABCD chart) is compatible with the orthodox
Tarski geometry (betweenness + congruence + Pasch).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Geometry.cauchy_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L270-L270)
**theorem
Tau.BookII.Geometry.cauchy_15_4 :den_cauchy_check 15 4 = true**


---

### `Tau.BookII.Geometry.injective_12_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L271-L271)
**theorem
Tau.BookII.Geometry.injective_12_4 :den_injective_check 12 4 = true**


---

### `Tau.BookII.Geometry.between_mono_8`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L272-L272)
**theorem
Tau.BookII.Geometry.between_mono_8 :den_between_mono_check 8 5 3 = true**


---

### `Tau.BookII.Geometry.cong_compat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L273-L273)
**theorem
Tau.BookII.Geometry.cong_compat :den_cong_compat_check 5 = true**


---

### `Tau.BookII.Geometry.bridge_8_5_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Geometry/OrthodoxBridge.lean#L274-L274)
**theorem
Tau.BookII.Geometry.bridge_8_5_3 :orthodox_bridge_check 8 5 3 = true**
