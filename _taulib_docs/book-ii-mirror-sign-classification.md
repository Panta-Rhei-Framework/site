---
layout: taulib-doc
title: "TauLib.BookII.Mirror.SignClassification"
permalink: /verify/taulib/docs/book-ii-mirror-sign-classification/
lane: verify
module_name: "TauLib.BookII.Mirror.SignClassification"
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

# TauLib.BookII.Mirror.SignClassification


Structural sign classification: the 12-level rewiring table and the
infinity trade-off between orthodox and tau approaches.

## Registry Cross-References


- [II.D68] Structural Sign Classification -- `SignLevel`, `orthodox_property`, `tau_property`

- [II.D69] The Infinity Trade-Off -- `InfinityTradeOff`, `orthodox_path`, `tau_path`

- [II.T43] Structural Incompatibility -- `orthodox_path_no_unique_omega`,
`tau_path_no_archimedean`, `structural_incompatibility`


## Mathematical Content


**II.D68 (Structural Sign Classification):** Category tau rewires 12 structural
features relative to orthodox mathematics. At each level, the orthodox and tau
approaches make different choices. This classification is exhaustive: every
feature of the tau framework corresponds to one of these 12 sign levels.

**II.D69 (The Infinity Trade-Off):** The orthodox and tau paths through the
sign classification are mutually exclusive at the infinity level. Unique omega
(tau's single countable infinity) and Archimedean density (orthodox real line)
cannot coexist. This is not a deficiency but a structural trade-off: each path
gets advantages that the other cannot have.

**II.T43 (Structural Incompatibility):** The orthodox path necessarily lacks
unique omega; the tau path necessarily lacks Archimedean density. This is
proved by construction: we exhibit both paths and verify the incompatibility
at the infinity level.

---

### `Tau.BookII.Mirror.SignLevel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L44-L60)
**inductive
Tau.BookII.Mirror.SignLevel :Type**


[II.D68] The 12 structural sign levels.
Each level represents a feature where orthodox and tau approaches
make different structural choices.

- ScalarAlgebra : SignLevel
- HolomorphyPDE : SignLevel
- BoundaryInterior : SignLevel
- Infinity : SignLevel
- Cardinality : SignLevel
- Topology : SignLevel
- Geometry : SignLevel
- Compactness : SignLevel
- Idempotents : SignLevel
- Liouville : SignLevel
- Gluing : SignLevel
- Spectrum : SignLevel
Instances For

---

### `Tau.BookII.Mirror.instDecidableEqSignLevel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L60-L60)
**instance
Tau.BookII.Mirror.instDecidableEqSignLevel :DecidableEq SignLevel**

Equations
- Tau.BookII.Mirror.instDecidableEqSignLevel x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookII.Mirror.instReprSignLevel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L60-L60)
**instance
Tau.BookII.Mirror.instReprSignLevel :Repr SignLevel**

Equations
- Tau.BookII.Mirror.instReprSignLevel = { reprPrec := Tau.BookII.Mirror.instReprSignLevel.repr }

---

### `Tau.BookII.Mirror.instReprSignLevel.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L60-L60)
**def
Tau.BookII.Mirror.instReprSignLevel.repr :SignLevel → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.orthodox_property`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L68-L81)
**def
Tau.BookII.Mirror.orthodox_property :SignLevel → String**


[II.D68] The orthodox property at each sign level.
Equations
- Tau.BookII.Mirror.orthodox_property Tau.BookII.Mirror.SignLevel.ScalarAlgebra = "i^2 = -1 (Gaussian integers, complex numbers)"
- Tau.BookII.Mirror.orthodox_property Tau.BookII.Mirror.SignLevel.HolomorphyPDE = "elliptic Cauchy-Riemann PDE (Laplacian)"
- Tau.BookII.Mirror.orthodox_property Tau.BookII.Mirror.SignLevel.BoundaryInterior = "interior determines boundary (maximum principle)"
- Tau.BookII.Mirror.orthodox_property Tau.BookII.Mirror.SignLevel.Infinity = "Cantor cardinal hierarchy (aleph_0, aleph_1, ...)"
- Tau.BookII.Mirror.orthodox_property Tau.BookII.Mirror.SignLevel.Cardinality = "uncountable real line (2^aleph_0 elements)"
- Tau.BookII.Mirror.orthodox_property Tau.BookII.Mirror.SignLevel.Topology = "Hausdorff, second countable, locally Euclidean"
- Tau.BookII.Mirror.orthodox_property Tau.BookII.Mirror.SignLevel.Geometry = "Riemannian metric (inner product on tangent bundle)"
- Tau.BookII.Mirror.orthodox_property Tau.BookII.Mirror.SignLevel.Compactness = "locally compact Hausdorff (Alexandrov extension)"
- Tau.BookII.Mirror.orthodox_property Tau.BookII.Mirror.SignLevel.Idempotents = "no nontrivial idempotents (C is a field)"
- Tau.BookII.Mirror.orthodox_property Tau.BookII.Mirror.SignLevel.Liouville = "bounded entire function is constant (Liouville)"
- Tau.BookII.Mirror.orthodox_property Tau.BookII.Mirror.SignLevel.Gluing = "sheaf on open covers (Leray, Cech)"
- Tau.BookII.Mirror.orthodox_property Tau.BookII.Mirror.SignLevel.Spectrum = "Gelfand spectrum (maximal ideals of C*-algebra)"
Instances For

---

### `Tau.BookII.Mirror.tau_property`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L83-L96)
**def
Tau.BookII.Mirror.tau_property :SignLevel → String**


[II.D68] The tau property at each sign level.
Equations
- Tau.BookII.Mirror.tau_property Tau.BookII.Mirror.SignLevel.ScalarAlgebra = "j^2 = +1 (split-complex, bipolar scalars)"
- Tau.BookII.Mirror.tau_property Tau.BookII.Mirror.SignLevel.HolomorphyPDE = "hyperbolic split-CR PDE (wave equation)"
- Tau.BookII.Mirror.tau_property Tau.BookII.Mirror.SignLevel.BoundaryInterior = "boundary determines interior (Hartogs extension)"
- Tau.BookII.Mirror.tau_property Tau.BookII.Mirror.SignLevel.Infinity = "unique omega (omega-germs, no cardinal hierarchy)"
- Tau.BookII.Mirror.tau_property Tau.BookII.Mirror.SignLevel.Cardinality = "countable tau-reals (primorial tower limit)"
- Tau.BookII.Mirror.tau_property Tau.BookII.Mirror.SignLevel.Topology = "Stone space (profinite, totally disconnected)"
- Tau.BookII.Mirror.tau_property Tau.BookII.Mirror.SignLevel.Geometry = "betweenness-first (earned from divisibility order)"
- Tau.BookII.Mirror.tau_property Tau.BookII.Mirror.SignLevel.Compactness = "profinitely compact (inverse limit of finite stages)"
- Tau.BookII.Mirror.tau_property Tau.BookII.Mirror.SignLevel.Idempotents = "nontrivial idempotents e+, e- (bipolar decomposition)"
- Tau.BookII.Mirror.tau_property Tau.BookII.Mirror.SignLevel.Liouville = "bounded hol implies sector-balanced (bipolar Liouville)"
- Tau.BookII.Mirror.tau_property Tau.BookII.Mirror.SignLevel.Gluing = "sheaf on clopen covers (Stone topology gluing)"
- Tau.BookII.Mirror.tau_property Tau.BookII.Mirror.SignLevel.Spectrum = "primorial spectrum (tower of Z/M_kZ spectra)"
Instances For

---

### `Tau.BookII.Mirror.allSignLevels`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L102-L106)
**def
Tau.BookII.Mirror.allSignLevels :List SignLevel**


Complete list of all 12 sign levels.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.sign_level_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L108-L109)
**theorem
Tau.BookII.Mirror.sign_level_count :allSignLevels.length = 12**


[II.D68] There are exactly 12 sign levels.

---

### `Tau.BookII.Mirror.orthodox_nonempty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L111-L113)
**def
Tau.BookII.Mirror.orthodox_nonempty
(sl : SignLevel)
 :Bool**


Each sign level has a nonempty orthodox description.
Equations
- Tau.BookII.Mirror.orthodox_nonempty sl = decide ((Tau.BookII.Mirror.orthodox_property sl).length > 0)
Instances For

---

### `Tau.BookII.Mirror.tau_nonempty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L115-L117)
**def
Tau.BookII.Mirror.tau_nonempty
(sl : SignLevel)
 :Bool**


Each sign level has a nonempty tau description.
Equations
- Tau.BookII.Mirror.tau_nonempty sl = decide ((Tau.BookII.Mirror.tau_property sl).length > 0)
Instances For

---

### `Tau.BookII.Mirror.all_orthodox_nonempty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L119-L121)
**theorem
Tau.BookII.Mirror.all_orthodox_nonempty :allSignLevels.all orthodox_nonempty = true**


All orthodox descriptions are nonempty.

---

### `Tau.BookII.Mirror.all_tau_nonempty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L123-L125)
**theorem
Tau.BookII.Mirror.all_tau_nonempty :allSignLevels.all tau_nonempty = true**


All tau descriptions are nonempty.

---

### `Tau.BookII.Mirror.descriptions_differ`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L127-L129)
**def
Tau.BookII.Mirror.descriptions_differ
(sl : SignLevel)
 :Bool**


Orthodox and tau descriptions differ at every level.
Equations
- Tau.BookII.Mirror.descriptions_differ sl = (Tau.BookII.Mirror.orthodox_property sl != Tau.BookII.Mirror.tau_property sl)
Instances For

---

### `Tau.BookII.Mirror.all_descriptions_differ`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L131-L133)
**theorem
Tau.BookII.Mirror.all_descriptions_differ :allSignLevels.all descriptions_differ = true**


[II.D68] At every sign level, the orthodox and tau descriptions are distinct.

---

### `Tau.BookII.Mirror.InfinityTradeOff`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L139-L151)
**structure
Tau.BookII.Mirror.InfinityTradeOff :Type**


[II.D69] The infinity trade-off: four boolean witnesses
encoding the structural choices at the infinity level.


- has_unique_omega: tau's single countable infinity

- has_archimedean_density: orthodox Archimedean property of R

- has_epsilon_delta: orthodox epsilon-delta continuity

- has_finite_witnesses: tau's finite-stage witnesses


- has_unique_omega : Bool
- has_archimedean_density : Bool
- has_epsilon_delta : Bool
- has_finite_witnesses : Bool
Instances For

---

### `Tau.BookII.Mirror.instDecidableEqInfinityTradeOff.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L151-L151)
**def
Tau.BookII.Mirror.instDecidableEqInfinityTradeOff.decEq
(x✝ x✝¹ : InfinityTradeOff)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.instDecidableEqInfinityTradeOff`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L151-L151)
**instance
Tau.BookII.Mirror.instDecidableEqInfinityTradeOff :DecidableEq InfinityTradeOff**

Equations
- Tau.BookII.Mirror.instDecidableEqInfinityTradeOff = Tau.BookII.Mirror.instDecidableEqInfinityTradeOff.decEq

---

### `Tau.BookII.Mirror.instReprInfinityTradeOff.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L151-L151)
**def
Tau.BookII.Mirror.instReprInfinityTradeOff.repr :InfinityTradeOff → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.instReprInfinityTradeOff`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L151-L151)
**instance
Tau.BookII.Mirror.instReprInfinityTradeOff :Repr InfinityTradeOff**

Equations
- Tau.BookII.Mirror.instReprInfinityTradeOff = { reprPrec := Tau.BookII.Mirror.instReprInfinityTradeOff.repr }

---

### `Tau.BookII.Mirror.orthodox_path`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L153-L159)
**def
Tau.BookII.Mirror.orthodox_path :InfinityTradeOff**


[II.D69] The orthodox path: Archimedean with epsilon-delta,
but no unique omega and no finite witnesses.
Equations
- Tau.BookII.Mirror.orthodox_path = { has_unique_omega := false, has_archimedean_density := true, has_epsilon_delta := true,
 has_finite_witnesses := false }
Instances For

---

### `Tau.BookII.Mirror.tau_path`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L161-L167)
**def
Tau.BookII.Mirror.tau_path :InfinityTradeOff**


[II.D69] The tau path: unique omega with finite witnesses,
but no Archimedean density and no epsilon-delta.
Equations
- Tau.BookII.Mirror.tau_path = { has_unique_omega := true, has_archimedean_density := false, has_epsilon_delta := false,
 has_finite_witnesses := true }
Instances For

---

### `Tau.BookII.Mirror.orthodox_path_no_unique_omega`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L173-L175)
**theorem
Tau.BookII.Mirror.orthodox_path_no_unique_omega :orthodox_path.has_unique_omega = false**


[II.T43] The orthodox path does not have unique omega.

---

### `Tau.BookII.Mirror.tau_path_no_archimedean`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L177-L179)
**theorem
Tau.BookII.Mirror.tau_path_no_archimedean :tau_path.has_archimedean_density = false**


[II.T43] The tau path does not have Archimedean density.

---

### `Tau.BookII.Mirror.orthodox_path_no_finite_witnesses`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L181-L183)
**theorem
Tau.BookII.Mirror.orthodox_path_no_finite_witnesses :orthodox_path.has_finite_witnesses = false**


[II.T43] The orthodox path does not have finite witnesses.

---

### `Tau.BookII.Mirror.tau_path_no_epsilon_delta`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L185-L187)
**theorem
Tau.BookII.Mirror.tau_path_no_epsilon_delta :tau_path.has_epsilon_delta = false**


[II.T43] The tau path does not have epsilon-delta.

---

### `Tau.BookII.Mirror.structural_incompatibility`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L189-L194)
**theorem
Tau.BookII.Mirror.structural_incompatibility :orthodox_path.has_unique_omega = false ∧ tau_path.has_archimedean_density = false**


[II.T43] Structural incompatibility: unique omega and Archimedean density
cannot both hold. Proved by case analysis on the two paths.

---

### `Tau.BookII.Mirror.paths_distinct`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L196-L200)
**theorem
Tau.BookII.Mirror.paths_distinct :orthodox_path ≠ tau_path**


[II.T43] The two paths are distinct structures.

---

### `Tau.BookII.Mirror.no_both_omega_and_archimedean_orthodox`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L202-L209)
**theorem
Tau.BookII.Mirror.no_both_omega_and_archimedean_orthodox :orthodox_path.has_unique_omega = true → orthodox_path.has_archimedean_density = true → False**


[II.T43] No trade-off can have both unique omega and Archimedean density
if it agrees with one of the two canonical paths.

---

### `Tau.BookII.Mirror.no_both_omega_and_archimedean_tau`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L211-L217)
**theorem
Tau.BookII.Mirror.no_both_omega_and_archimedean_tau :tau_path.has_unique_omega = true → tau_path.has_archimedean_density = true → False**


[II.T43] Symmetrically for the tau path.

---

### `Tau.BookII.Mirror.sign_level_index`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L223-L236)
**def
Tau.BookII.Mirror.sign_level_index :SignLevel → ℕ**


Index of a sign level (0-based).
Equations
- Tau.BookII.Mirror.sign_level_index Tau.BookII.Mirror.SignLevel.ScalarAlgebra = 0
- Tau.BookII.Mirror.sign_level_index Tau.BookII.Mirror.SignLevel.HolomorphyPDE = 1
- Tau.BookII.Mirror.sign_level_index Tau.BookII.Mirror.SignLevel.BoundaryInterior = 2
- Tau.BookII.Mirror.sign_level_index Tau.BookII.Mirror.SignLevel.Infinity = 3
- Tau.BookII.Mirror.sign_level_index Tau.BookII.Mirror.SignLevel.Cardinality = 4
- Tau.BookII.Mirror.sign_level_index Tau.BookII.Mirror.SignLevel.Topology = 5
- Tau.BookII.Mirror.sign_level_index Tau.BookII.Mirror.SignLevel.Geometry = 6
- Tau.BookII.Mirror.sign_level_index Tau.BookII.Mirror.SignLevel.Compactness = 7
- Tau.BookII.Mirror.sign_level_index Tau.BookII.Mirror.SignLevel.Idempotents = 8
- Tau.BookII.Mirror.sign_level_index Tau.BookII.Mirror.SignLevel.Liouville = 9
- Tau.BookII.Mirror.sign_level_index Tau.BookII.Mirror.SignLevel.Gluing = 10
- Tau.BookII.Mirror.sign_level_index Tau.BookII.Mirror.SignLevel.Spectrum = 11
Instances For

---

### `Tau.BookII.Mirror.sign_indices_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L238-L241)
**theorem
Tau.BookII.Mirror.sign_indices_injective
(a b : SignLevel)
 :sign_level_index a = sign_level_index b → a = b**


All indices are distinct.

---

### `Tau.BookII.Mirror.sign_index_bound`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L243-L246)
**theorem
Tau.BookII.Mirror.sign_index_bound
(sl : SignLevel)
 :sign_level_index sl < 12**


All indices are in [0, 12).

---

### `Tau.BookII.Mirror.sign_count_12`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L275-L276)
**theorem
Tau.BookII.Mirror.sign_count_12 :allSignLevels.length = 12**


---

### `Tau.BookII.Mirror.orthodox_all_nonempty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L279-L280)
**theorem
Tau.BookII.Mirror.orthodox_all_nonempty :allSignLevels.all orthodox_nonempty = true**


---

### `Tau.BookII.Mirror.tau_all_nonempty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L282-L283)
**theorem
Tau.BookII.Mirror.tau_all_nonempty :allSignLevels.all tau_nonempty = true**


---

### `Tau.BookII.Mirror.all_differ`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L285-L286)
**theorem
Tau.BookII.Mirror.all_differ :allSignLevels.all descriptions_differ = true**


---

### `Tau.BookII.Mirror.orthodox_omega`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L289-L290)
**theorem
Tau.BookII.Mirror.orthodox_omega :orthodox_path.has_unique_omega = false**


---

### `Tau.BookII.Mirror.tau_archimedean`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L292-L293)
**theorem
Tau.BookII.Mirror.tau_archimedean :tau_path.has_archimedean_density = false**


---

### `Tau.BookII.Mirror.orthodox_epsilon`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L295-L296)
**theorem
Tau.BookII.Mirror.orthodox_epsilon :orthodox_path.has_epsilon_delta = true**


---

### `Tau.BookII.Mirror.tau_witnesses`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L298-L299)
**theorem
Tau.BookII.Mirror.tau_witnesses :tau_path.has_finite_witnesses = true**


---

### `Tau.BookII.Mirror.incompatibility_native`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/SignClassification.lean#L302-L305)
**theorem
Tau.BookII.Mirror.incompatibility_native :orthodox_path.has_unique_omega = false ∧ tau_path.has_archimedean_density = false**
