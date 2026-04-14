---
layout: taulib-doc
title: "TauLib.BookIII.Bridge.TranslationTopo"
permalink: /verify/taulib/docs/book-iii-bridge-translation-topo/
lane: verify
module_name: "TauLib.BookIII.Bridge.TranslationTopo"
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

# TauLib.BookIII.Bridge.TranslationTopo


Topological fragment of the translation functor: τ-internal tower
structure maps to classical filtration and manifold stratification.

## Registry Cross-References


- [III.D89] Topological Translation Functor — `topo_translation_check`

- [III.D90] Dimension Recovery — `dimension_recovery_check`

- [III.T60] Topological Faithfulness — `topo_faithful_check`

- [III.P37] Boundary Restriction — `boundary_restriction_check`


## Mathematical Content


**III.D89 (Topological Translation Functor):** Topo_tr maps the primorial
tower filtration Z/M_1 ← Z/M_2 ← ... to a classical inverse system
of finite spaces. The tower coherence (reduce compatibility) translates
to the projective limit property.

**III.D90 (Dimension Recovery):** The primorial depth k corresponds to
intrinsic dimension: dim = k. At stage k, the space Z/M_k Z has k
independent prime coordinates (by CRT), giving a k-dimensional torus
T^k = Π_{i=1}^k Z/p_i Z.

**III.T60 (Topological Faithfulness):** Topo_tr preserves and reflects
the tower structure: open sets (cylinders) map to open sets, and the
restriction maps are continuous. The ultrametric topology on the tower
translates faithfully.

**III.P37 (Boundary Restriction):** Restriction from stage k+1 to stage k
(the reduce map) corresponds to the classical boundary restriction in
the projective limit. The fiber over a point x at stage k has exactly
p_{k+1} preimages at stage k+1.

---

### `Tau.BookIII.Bridge.tower_projection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L53-L55)
**def
Tau.BookIII.Bridge.tower_projection
(x k : ℕ)
 :ℕ**


[III.D89] Tower projection: the canonical map π_k : Z/M_{k+1} → Z/M_k.
This is reduce(x, k) and is the fundamental topological structure.
Equations
- Tau.BookIII.Bridge.tower_projection x k = Tau.Polarity.reduce x k
Instances For

---

### `Tau.BookIII.Bridge.topo_translation_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L57-L77)
**def
Tau.BookIII.Bridge.topo_translation_check
(bound db : ℕ)
 :Bool**


[III.D89] Tower coherence for translation: π_k ∘ π_{k+1} factors
through π_k. That is, reduce(reduce(x, k+1), k) = reduce(x, k).
Equations
- Tau.BookIII.Bridge.topo_translation_check bound db = Tau.BookIII.Bridge.topo_translation_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Bridge.topo_translation_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L62-L76)@[irreducible]

**def
Tau.BookIII.Bridge.topo_translation_check.go
(bound db x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.crt_dimension`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L83-L85)
**def
Tau.BookIII.Bridge.crt_dimension
(k : ℕ)
 :ℕ**


[III.D90] CRT dimension: number of prime factors at stage k.
dim(Z/M_k Z) = k (by CRT: Z/M_k ≅ Z/p_1 × ... × Z/p_k).
Equations
- Tau.BookIII.Bridge.crt_dimension k = k
Instances For

---

### `Tau.BookIII.Bridge.dimension_recovery_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L87-L110)
**def
Tau.BookIII.Bridge.dimension_recovery_check
(db : ℕ)
 :Bool**


[III.D90] Dimension recovery check: the number of independent
prime coordinates equals the stage depth.
Equations
- Tau.BookIII.Bridge.dimension_recovery_check db = Tau.BookIII.Bridge.dimension_recovery_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Bridge.dimension_recovery_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L92-L99)@[irreducible]

**def
Tau.BookIII.Bridge.dimension_recovery_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.dimension_recovery_check.count_prime_factors`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L101-L102)
**def
Tau.BookIII.Bridge.dimension_recovery_check.count_prime_factors
(pk k : ℕ)
 :ℕ**

Equations
- Tau.BookIII.Bridge.dimension_recovery_check.count_prime_factors pk k = Tau.BookIII.Bridge.dimension_recovery_check.go_count 1 (k + 1) pk 0
Instances For

---

### `Tau.BookIII.Bridge.dimension_recovery_check.go_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L104-L109)@[irreducible]

**def
Tau.BookIII.Bridge.dimension_recovery_check.go_count
(i bound pk acc : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.cylinder_preservation_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L116-L145)
**def
Tau.BookIII.Bridge.cylinder_preservation_check
(bound db : ℕ)
 :Bool**


[III.T60] Cylinder preservation: cylinders at stage k (sets of the
form {x : reduce(x,k) = a}) map to open balls in the ultrametric.
Equations
- Tau.BookIII.Bridge.cylinder_preservation_check bound db = Tau.BookIII.Bridge.cylinder_preservation_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Bridge.cylinder_preservation_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L121-L135)@[irreducible]

**def
Tau.BookIII.Bridge.cylinder_preservation_check.go
(bound db a k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.cylinder_preservation_check.count_fiber`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L137-L138)
**def
Tau.BookIII.Bridge.cylinder_preservation_check.count_fiber
(a k pk1 : ℕ)
 :ℕ**

Equations
- Tau.BookIII.Bridge.cylinder_preservation_check.count_fiber a k pk1 = Tau.BookIII.Bridge.cylinder_preservation_check.go_cf 0 pk1 0 a k
Instances For

---

### `Tau.BookIII.Bridge.cylinder_preservation_check.go_cf`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L140-L144)@[irreducible]

**def
Tau.BookIII.Bridge.cylinder_preservation_check.go_cf
(y bound acc a k : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.topo_faithful_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L147-L150)
**def
Tau.BookIII.Bridge.topo_faithful_check
(bound db : ℕ)
 :Bool**


[III.T60] Full topological faithfulness.
Equations
- Tau.BookIII.Bridge.topo_faithful_check bound db = (Tau.BookIII.Bridge.topo_translation_check bound db && Tau.BookIII.Bridge.cylinder_preservation_check bound db)
Instances For

---

### `Tau.BookIII.Bridge.boundary_restriction_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L156-L188)
**def
Tau.BookIII.Bridge.boundary_restriction_check
(db : ℕ)
 :Bool**


[III.P37] Boundary restriction: the fiber of π_k over a ∈ Z/M_k Z
has exactly p_{k+1} elements in Z/M_{k+1} Z.
Equations
- Tau.BookIII.Bridge.boundary_restriction_check db = Tau.BookIII.Bridge.boundary_restriction_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookIII.Bridge.boundary_restriction_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L161-L171)@[irreducible]

**def
Tau.BookIII.Bridge.boundary_restriction_check.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.boundary_restriction_check.go_a`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L173-L178)@[irreducible]

**def
Tau.BookIII.Bridge.boundary_restriction_check.go_a
(a pk pk1 p_next k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.boundary_restriction_check.count_fiber_size`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L180-L181)
**def
Tau.BookIII.Bridge.boundary_restriction_check.count_fiber_size
(a k pk1 : ℕ)
 :ℕ**

Equations
- Tau.BookIII.Bridge.boundary_restriction_check.count_fiber_size a k pk1 = Tau.BookIII.Bridge.boundary_restriction_check.go_cf 0 pk1 0 a k
Instances For

---

### `Tau.BookIII.Bridge.boundary_restriction_check.go_cf`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L183-L187)@[irreducible]

**def
Tau.BookIII.Bridge.boundary_restriction_check.go_cf
(y bound acc a k : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Bridge.topo_translation_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L194-L196)
**theorem
Tau.BookIII.Bridge.topo_translation_10_3 :topo_translation_check 10 3 = true**


[III.D89] Tower coherence at bound 10, depth 3.

---

### `Tau.BookIII.Bridge.dimension_recovery_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L198-L200)
**theorem
Tau.BookIII.Bridge.dimension_recovery_3 :dimension_recovery_check 3 = true**


[III.D90] Dimension recovery at depth 3.

---

### `Tau.BookIII.Bridge.topo_faithful_6_2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L202-L204)
**theorem
Tau.BookIII.Bridge.topo_faithful_6_2 :topo_faithful_check 6 2 = true**


[III.T60] Topological faithfulness at bound 6, depth 2.

---

### `Tau.BookIII.Bridge.boundary_restriction_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Bridge/TranslationTopo.lean#L206-L208)
**theorem
Tau.BookIII.Bridge.boundary_restriction_3 :boundary_restriction_check 3 = true**


[III.P37] Boundary restriction at depth 3.
