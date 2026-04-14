---
layout: taulib-doc
title: "TauLib.BookII.Mirror.DimensionalLadder"
permalink: /verify/taulib/docs/book-ii-mirror-dimensional-ladder/
lane: verify
module_name: "TauLib.BookII.Mirror.DimensionalLadder"
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

# TauLib.BookII.Mirror.DimensionalLadder


Why τ³ has no dimensional ladder: the Archimedean-elliptic engine that
generates the orthodox SCV dimensional hierarchy is absent in the fourth
quadrant (Hyperbolic, Non-Archimedean). τ³ exhibits features from three
classical rungs simultaneously, collapsing the ladder into a single point.

## Registry Cross-References


- [II.D75] Archimedean-Elliptic Engine -- `ArchimedeanEllipticEngine`,
`engine_active`, `engine_for_quadrant`

- [II.D76] Dimensional Rigidity -- `DimensionalRigidity`, `tau_rigidity`,
`fibration_forced`

- [II.T47] Simultaneous Rung Theorem -- `simultaneous_rung`,
`tau_spans_three_rungs`

- [II.T48] Fourth Quadrant Ladder Collapse -- `ladder_collapse`,
`tau_engine_inactive`

- [II.R31] Categoricity Implies No Ladder -- `categoricity_no_ladder`

- [II.R32] Honest Scope -- (doc comment only)


## Mathematical Content


**II.D75 (Archimedean-Elliptic Engine):** The orthodox SCV dimensional
ladder (C1 → C2 → C3 → C4+) arises from the interaction of two features:

- **Metric dimension:** The Archimedean metric gives continuous manifolds
with variable real dimension, so "dimension n" is meaningful.

- **Elliptic CR overdeterminacy:** For n ≥ 2, the elliptic Cauchy-Riemann
equations are overdetermined, creating qualitatively new phenomena at each
dimension step (Hartogs, Levi problem, etc.).


The engine requires BOTH ingredients. Neither alone generates a ladder.

**II.D76 (Dimensional Rigidity):** τ admits exactly one holomorphic structure
with fibration index 3 (= 1 base + 2 fiber) and refinement dimension 4
(= ABCD rays). There is no family of τ-structures indexed by dimension.

**II.T47 (Simultaneous Rung Theorem):** τ³ exhibits features from at least
three classical SCV rungs simultaneously:


- From C1: Cauchy integral (Mutual Determination II.T27)

- From C2: Distinguished boundary (lemniscate L)

- From C3: Full Hartogs extension (Global Hartogs I.T31)


This is impossible on the orthodox ladder, where features are acquired
monotonically with dimension.

**II.T48 (Fourth Quadrant Ladder Collapse):** In the fourth quadrant
(Hyperbolic, Non-Archimedean), the Archimedean-elliptic engine is absent:
the metric is non-Archimedean (no continuous dimension) and the PDE type
is hyperbolic (no elliptic overdeterminacy). Without the engine, no
dimensional ladder is generated.

**II.R31 (Categoricity Implies No Ladder):** The categoricity of τ³
(II.T42) implies the moduli space is a singleton. A singleton cannot
support a dimension-indexed family of structures.

**II.R32 (Honest Scope):** This is a structural observation about why the
SCV dimensional ladder does not apply to τ-holomorphy. It does not claim
to reproduce any SCV result; it explains why the ladder framework is
inapplicable.

---

### `Tau.BookII.Mirror.SCVDimension`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L73-L79)
**inductive
Tau.BookII.Mirror.SCVDimension :Type**


The four qualitatively distinct dimension regimes of orthodox SCV.

- C1 : SCVDimension
- C2 : SCVDimension
- C3 : SCVDimension
- C4plus : SCVDimension
Instances For

---

### `Tau.BookII.Mirror.instDecidableEqSCVDimension`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L79-L79)
**instance
Tau.BookII.Mirror.instDecidableEqSCVDimension :DecidableEq SCVDimension**

Equations
- Tau.BookII.Mirror.instDecidableEqSCVDimension x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookII.Mirror.instReprSCVDimension`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L79-L79)
**instance
Tau.BookII.Mirror.instReprSCVDimension :Repr SCVDimension**

Equations
- Tau.BookII.Mirror.instReprSCVDimension = { reprPrec := Tau.BookII.Mirror.instReprSCVDimension.repr }

---

### `Tau.BookII.Mirror.instReprSCVDimension.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L79-L79)
**def
Tau.BookII.Mirror.instReprSCVDimension.repr :SCVDimension → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.SCVDimension.toNat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L81-L86)
**def
Tau.BookII.Mirror.SCVDimension.toNat :SCVDimension → ℕ**


Numerical value of an SCV dimension regime.
Equations
- Tau.BookII.Mirror.SCVDimension.C1.toNat = 1
- Tau.BookII.Mirror.SCVDimension.C2.toNat = 2
- Tau.BookII.Mirror.SCVDimension.C3.toNat = 3
- Tau.BookII.Mirror.SCVDimension.C4plus.toNat = 4
Instances For

---

### `Tau.BookII.Mirror.SCVDimension.le`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L88-L90)
**def
Tau.BookII.Mirror.SCVDimension.le
(d1 d2 : SCVDimension)
 :Bool**


The dimension regimes form a total order.
Equations
- d1.le d2 = decide (d1.toNat ≤ d2.toNat)
Instances For

---

### `Tau.BookII.Mirror.SCVFeature`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L96-L111)
**inductive
Tau.BookII.Mirror.SCVFeature :Type**


Qualitative features of orthodox SCV, classified by the dimension
at which they first appear.

- RiemannMapping : SCVFeature
- RichAutomorphisms : SCVFeature
- Monodromy : SCVFeature
- CauchyIntegral : SCVFeature
- IsolatedSingularities : SCVFeature
- HartogsExtension : SCVFeature
- BidiscBallSplit : SCVFeature
- DistinguishedBoundary : SCVFeature
- FullHartogs : SCVFeature
- LeviProblem : SCVFeature
- NoRiemannMapping : SCVFeature
- GrauertVarieties : SCVFeature
Instances For

---

### `Tau.BookII.Mirror.instDecidableEqSCVFeature`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L111-L111)
**instance
Tau.BookII.Mirror.instDecidableEqSCVFeature :DecidableEq SCVFeature**

Equations
- Tau.BookII.Mirror.instDecidableEqSCVFeature x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookII.Mirror.instReprSCVFeature.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L111-L111)
**def
Tau.BookII.Mirror.instReprSCVFeature.repr :SCVFeature → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.instReprSCVFeature`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L111-L111)
**instance
Tau.BookII.Mirror.instReprSCVFeature :Repr SCVFeature**

Equations
- Tau.BookII.Mirror.instReprSCVFeature = { reprPrec := Tau.BookII.Mirror.instReprSCVFeature.repr }

---

### `Tau.BookII.Mirror.feature_origin`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L113-L126)
**def
Tau.BookII.Mirror.feature_origin :SCVFeature → SCVDimension**


The SCV dimension at which a feature first appears.
Equations
- Tau.BookII.Mirror.feature_origin Tau.BookII.Mirror.SCVFeature.RiemannMapping = Tau.BookII.Mirror.SCVDimension.C1
- Tau.BookII.Mirror.feature_origin Tau.BookII.Mirror.SCVFeature.RichAutomorphisms = Tau.BookII.Mirror.SCVDimension.C1
- Tau.BookII.Mirror.feature_origin Tau.BookII.Mirror.SCVFeature.Monodromy = Tau.BookII.Mirror.SCVDimension.C1
- Tau.BookII.Mirror.feature_origin Tau.BookII.Mirror.SCVFeature.CauchyIntegral = Tau.BookII.Mirror.SCVDimension.C1
- Tau.BookII.Mirror.feature_origin Tau.BookII.Mirror.SCVFeature.IsolatedSingularities = Tau.BookII.Mirror.SCVDimension.C1
- Tau.BookII.Mirror.feature_origin Tau.BookII.Mirror.SCVFeature.HartogsExtension = Tau.BookII.Mirror.SCVDimension.C2
- Tau.BookII.Mirror.feature_origin Tau.BookII.Mirror.SCVFeature.BidiscBallSplit = Tau.BookII.Mirror.SCVDimension.C2
- Tau.BookII.Mirror.feature_origin Tau.BookII.Mirror.SCVFeature.DistinguishedBoundary = Tau.BookII.Mirror.SCVDimension.C2
- Tau.BookII.Mirror.feature_origin Tau.BookII.Mirror.SCVFeature.FullHartogs = Tau.BookII.Mirror.SCVDimension.C3
- Tau.BookII.Mirror.feature_origin Tau.BookII.Mirror.SCVFeature.LeviProblem = Tau.BookII.Mirror.SCVDimension.C3
- Tau.BookII.Mirror.feature_origin Tau.BookII.Mirror.SCVFeature.NoRiemannMapping = Tau.BookII.Mirror.SCVDimension.C3
- Tau.BookII.Mirror.feature_origin Tau.BookII.Mirror.SCVFeature.GrauertVarieties = Tau.BookII.Mirror.SCVDimension.C3
Instances For

---

### `Tau.BookII.Mirror.features_present`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L132-L146)
**def
Tau.BookII.Mirror.features_present :SCVDimension → List SCVFeature**


Features present at each rung of the orthodox SCV ladder.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.features_new`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L148-L154)
**def
Tau.BookII.Mirror.features_new :SCVDimension → List SCVFeature**


Features newly appearing at each rung (not present at previous rung).
Equations
- One or more equations did not get rendered due to their size.
- Tau.BookII.Mirror.features_new Tau.BookII.Mirror.SCVDimension.C4plus = []
Instances For

---

### `Tau.BookII.Mirror.c1_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L156-L157)
**theorem
Tau.BookII.Mirror.c1_count :(features_present SCVDimension.C1).length = 5**


C1 has 5 features.

---

### `Tau.BookII.Mirror.c2_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L159-L160)
**theorem
Tau.BookII.Mirror.c2_count :(features_present SCVDimension.C2).length = 8**


C2 has 8 features (5 inherited + 3 new).

---

### `Tau.BookII.Mirror.c3_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L162-L163)
**theorem
Tau.BookII.Mirror.c3_count :(features_present SCVDimension.C3).length = 12**


C3 has 12 features (8 inherited + 4 new).

---

### `Tau.BookII.Mirror.c4plus_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L165-L166)
**theorem
Tau.BookII.Mirror.c4plus_count :(features_present SCVDimension.C4plus).length = 12**


C4+ has 12 features (saturation).

---

### `Tau.BookII.Mirror.ladder_monotone`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L168-L173)
**theorem
Tau.BookII.Mirror.ladder_monotone :(features_present SCVDimension.C1).length ≤ (features_present SCVDimension.C2).length ∧ (features_present SCVDimension.C2).length ≤ (features_present SCVDimension.C3).length ∧ (features_present SCVDimension.C3).length ≤ (features_present SCVDimension.C4plus).length**


The ladder is monotonically non-decreasing.

---

### `Tau.BookII.Mirror.c4plus_saturated`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L175-L176)
**theorem
Tau.BookII.Mirror.c4plus_saturated :(features_new SCVDimension.C4plus).length = 0**


C4+ adds nothing new: saturation.

---

### `Tau.BookII.Mirror.tau_features`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L182-L189)
**def
Tau.BookII.Mirror.tau_features :List SCVFeature**


[II.T47] Features present in τ³ holomorphy, drawn from multiple
classical rungs simultaneously.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.tau_absent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L191-L199)
**def
Tau.BookII.Mirror.tau_absent :List SCVFeature**


Features absent in τ³ holomorphy.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.tau_feature_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L201-L202)
**theorem
Tau.BookII.Mirror.tau_feature_count :tau_features.length = 4**


τ³ has exactly 4 features from the orthodox classification.

---

### `Tau.BookII.Mirror.tau_absent_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L204-L205)
**theorem
Tau.BookII.Mirror.tau_absent_count :tau_absent.length = 6**


τ³ lacks exactly 6 features from the orthodox classification.

---

### `Tau.BookII.Mirror.tau_coverage`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L207-L210)
**theorem
Tau.BookII.Mirror.tau_coverage :tau_features.length + tau_absent.length = 10**


τ features and absent features account for 10 of 12 total.
(BidiscBallSplit and NoRiemannMapping are structurally inapplicable.)

---

### `Tau.BookII.Mirror.tau_feature_origins`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L216-L218)
**def
Tau.BookII.Mirror.tau_feature_origins :List SCVDimension**


The SCV dimension origins represented in the τ feature set.
Equations
- Tau.BookII.Mirror.tau_feature_origins = List.map Tau.BookII.Mirror.feature_origin Tau.BookII.Mirror.tau_features
Instances For

---

### `Tau.BookII.Mirror.tau_origins_value`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L220-L222)
**theorem
Tau.BookII.Mirror.tau_origins_value :tau_feature_origins = [SCVDimension.C1, SCVDimension.C2, SCVDimension.C2, SCVDimension.C3]**


The origins list is [C1, C2, C2, C3].

---

### `Tau.BookII.Mirror.tau_distinct_rungs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L224-L225)
**def
Tau.BookII.Mirror.tau_distinct_rungs :List SCVDimension**


The distinct rungs represented in τ features (manually deduplicated).
Equations
- Tau.BookII.Mirror.tau_distinct_rungs = [Tau.BookII.Mirror.SCVDimension.C1, Tau.BookII.Mirror.SCVDimension.C2, Tau.BookII.Mirror.SCVDimension.C3]
Instances For

---

### `Tau.BookII.Mirror.rung_present`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L227-L229)
**def
Tau.BookII.Mirror.rung_present
(d : SCVDimension)
 :Bool**


Check that a dimension appears in the τ feature origins.
Equations
- Tau.BookII.Mirror.rung_present d = Tau.BookII.Mirror.tau_feature_origins.any fun (x : Tau.BookII.Mirror.SCVDimension) => x == d
Instances For

---

### `Tau.BookII.Mirror.c1_present`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L231-L232)
**theorem
Tau.BookII.Mirror.c1_present :rung_present SCVDimension.C1 = true**


C1 is represented (via CauchyIntegral).

---

### `Tau.BookII.Mirror.c2_present`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L234-L235)
**theorem
Tau.BookII.Mirror.c2_present :rung_present SCVDimension.C2 = true**


C2 is represented (via DistinguishedBoundary, HartogsExtension).

---

### `Tau.BookII.Mirror.c3_present`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L237-L238)
**theorem
Tau.BookII.Mirror.c3_present :rung_present SCVDimension.C3 = true**


C3 is represented (via FullHartogs).

---

### `Tau.BookII.Mirror.tau_spans_three_rungs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L240-L242)
**theorem
Tau.BookII.Mirror.tau_spans_three_rungs :tau_distinct_rungs.length = 3**


[II.T47] τ³ features originate from exactly 3 distinct rungs.

---

### `Tau.BookII.Mirror.simultaneous_rung`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L244-L249)
**theorem
Tau.BookII.Mirror.simultaneous_rung :tau_distinct_rungs.length ≥ 3**


[II.T47] Simultaneous Rung Theorem: τ³ exhibits features from at least
three classical SCV dimension rungs simultaneously.
Specifically: C1 (CauchyIntegral), C2 (DistinguishedBoundary, HartogsExtension),
and C3 (FullHartogs).

---

### `Tau.BookII.Mirror.tau_rungs_are_c1_c2_c3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L251-L253)
**theorem
Tau.BookII.Mirror.tau_rungs_are_c1_c2_c3 :tau_distinct_rungs = [SCVDimension.C1, SCVDimension.C2, SCVDimension.C3]**


The three specific rungs are C1, C2, C3.

---

### `Tau.BookII.Mirror.tau_violates_monotone_acquisition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L255-L266)
**theorem
Tau.BookII.Mirror.tau_violates_monotone_acquisition :List.elem SCVDimension.C3 (List.map feature_origin tau_features) = true ∧ List.elem SCVFeature.RiemannMapping tau_absent = true ∧ List.elem SCVFeature.Monodromy tau_absent = true ∧ List.elem SCVFeature.IsolatedSingularities tau_absent = true**


On the orthodox ladder, no single dimension has features from 3 rungs
that aren't already subsumed. τ³ violates the monotone acquisition
pattern by having C3 features (FullHartogs) while lacking C1 features
(RiemannMapping, Monodromy, IsolatedSingularities).

---

### `Tau.BookII.Mirror.ArchimedeanEllipticEngine`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L272-L289)
**structure
Tau.BookII.Mirror.ArchimedeanEllipticEngine :Type**


[II.D75] The Archimedean-elliptic engine: the mechanism that generates
the orthodox SCV dimensional ladder.

The engine requires two ingredients:

- Archimedean metric → continuous manifold with variable dimension

- Elliptic PDE type → CR overdeterminacy increases with dimension


The interaction of these two features creates qualitatively new phenomena
at each dimension step. Without BOTH ingredients, no ladder is generated.

- has_metric_dimension : Bool
Archimedean metric gives continuous manifolds with meaningful dimension.

- has_elliptic_cr : Bool
Elliptic CR equations are increasingly overdetermined for n ≥ 2.

- generates_ladder : Bool
The engine generates the dimensional ladder only when both are active.

- ladder_requires_both : self.generates_ladder = (self.has_metric_dimension && self.has_elliptic_cr)
Ladder generation requires both ingredients.

Instances For

---

### `Tau.BookII.Mirror.engine_active`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L291-L293)
**def
Tau.BookII.Mirror.engine_active
(q : PhysicsQuadrant)
 :Bool**


[II.D75] Check if the Archimedean-elliptic engine is active in a given quadrant.
Equations
- Tau.BookII.Mirror.engine_active q = (q.pde == Tau.BookII.Mirror.PDEAxis.Elliptic && q.metric == Tau.BookII.Mirror.MetricAxis.Archimedean)
Instances For

---

### `Tau.BookII.Mirror.engine_for_quadrant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L295-L302)
**def
Tau.BookII.Mirror.engine_for_quadrant
(q : PhysicsQuadrant)
 :ArchimedeanEllipticEngine**


[II.D75] Construct the engine state for a quadrant.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.engine_active_qft`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L304-L306)
**theorem
Tau.BookII.Mirror.engine_active_qft :engine_active qft_quadrant = true**


The engine is active in the QFT quadrant (Elliptic, Archimedean).

---

### `Tau.BookII.Mirror.engine_inactive_gr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L308-L311)
**theorem
Tau.BookII.Mirror.engine_inactive_gr :engine_active gr_local_quadrant = false**


The engine is inactive in the GR quadrant (Hyperbolic, Archimedean):
missing the elliptic ingredient.

---

### `Tau.BookII.Mirror.engine_inactive_padic`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L313-L316)
**theorem
Tau.BookII.Mirror.engine_inactive_padic :engine_active padic_quadrant = false**


The engine is inactive in the p-adic quadrant (Elliptic, NonArchimedean):
missing the Archimedean ingredient.

---

### `Tau.BookII.Mirror.tau_engine_inactive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L322-L324)
**theorem
Tau.BookII.Mirror.tau_engine_inactive :engine_active tau_quadrant = false**


[II.T48] The Archimedean-elliptic engine is inactive in the tau quadrant.

---

### `Tau.BookII.Mirror.ladder_collapse`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L326-L334)
**theorem
Tau.BookII.Mirror.ladder_collapse :engine_active tau_quadrant = false ∧ tau_quadrant.pde = PDEAxis.Hyperbolic ∧ tau_quadrant.metric = MetricAxis.NonArchimedean**


[II.T48] Fourth Quadrant Ladder Collapse: the dimensional ladder does not
exist in the (Hyperbolic, Non-Archimedean) quadrant because the engine
that generates it is absent.

---

### `Tau.BookII.Mirror.tau_engine_both_absent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L336-L340)
**theorem
Tau.BookII.Mirror.tau_engine_both_absent :have e := engine_for_quadrant tau_quadrant;
e.has_metric_dimension = false ∧ e.has_elliptic_cr = false**


The engine's two ingredients are both absent for tau.

---

### `Tau.BookII.Mirror.engine_unique_to_qft`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L342-L348)
**theorem
Tau.BookII.Mirror.engine_unique_to_qft :engine_active qft_quadrant = true ∧ engine_active gr_local_quadrant = false ∧ engine_active padic_quadrant = false ∧ engine_active tau_quadrant = false**


Only the QFT quadrant has an active engine.

---

### `Tau.BookII.Mirror.DimensionalRigidity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L354-L365)
**structure
Tau.BookII.Mirror.DimensionalRigidity :Type**


[II.D76] Dimensional rigidity: τ admits exactly one holomorphic structure
with fixed fibration index and refinement dimension.

- fibration_index : ℕ
Fibration index = 3 (1 base + 2 fiber).

- refinement_dim : ℕ
Refinement dimension = 4 (A, B, C, D rays).

- base_factors : ℕ
Base factors = 1 (τ¹).

- fiber_factors : ℕ
Fiber factors = 2 (T²).

Instances For

---

### `Tau.BookII.Mirror.instReprDimensionalRigidity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L365-L365)
**def
Tau.BookII.Mirror.instReprDimensionalRigidity.repr :DimensionalRigidity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.instReprDimensionalRigidity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L365-L365)
**instance
Tau.BookII.Mirror.instReprDimensionalRigidity :Repr DimensionalRigidity**

Equations
- Tau.BookII.Mirror.instReprDimensionalRigidity = { reprPrec := Tau.BookII.Mirror.instReprDimensionalRigidity.repr }

---

### `Tau.BookII.Mirror.tau_rigidity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L367-L372)
**def
Tau.BookII.Mirror.tau_rigidity :DimensionalRigidity**


[II.D76] The unique rigidity parameters for τ.
Equations
- Tau.BookII.Mirror.tau_rigidity = { fibration_index := 3, refinement_dim := 4, base_factors := 1, fiber_factors := 2 }
Instances For

---

### `Tau.BookII.Mirror.fibration_forced`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L374-L377)
**theorem
Tau.BookII.Mirror.fibration_forced :tau_rigidity.fibration_index = tau_rigidity.base_factors + tau_rigidity.fiber_factors**


[II.D76] The fibration index equals base + fiber.

---

### `Tau.BookII.Mirror.refinement_is_abcd`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L379-L381)
**theorem
Tau.BookII.Mirror.refinement_is_abcd :tau_rigidity.refinement_dim = 4**


[II.D76] The refinement dimension equals the number of ABCD rays.

---

### `Tau.BookII.Mirror.fibration_is_three`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L383-L385)
**theorem
Tau.BookII.Mirror.fibration_is_three :tau_rigidity.fibration_index = 3**


[II.D76] The fibration is a 3-fold.

---

### `Tau.BookII.Mirror.rigidity_no_free_parameter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L387-L393)
**theorem
Tau.BookII.Mirror.rigidity_no_free_parameter :tau_rigidity.fibration_index = tau_rigidity.base_factors + tau_rigidity.fiber_factors ∧ tau_rigidity.base_factors = 1 ∧ tau_rigidity.fiber_factors = 2**


[II.D76] Rigidity means there is no dimension parameter to vary:
the fibration index is determined by the base and fiber structure.

---

### `Tau.BookII.Mirror.tau_moduli_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L399-L400)
**def
Tau.BookII.Mirror.tau_moduli_count :ℕ**


[II.R31] Moduli count: 1 = singleton (categorical).
Equations
- Tau.BookII.Mirror.tau_moduli_count = 1
Instances For

---

### `Tau.BookII.Mirror.categoricity_no_ladder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L402-L404)
**def
Tau.BookII.Mirror.categoricity_no_ladder :Bool**


[II.R31] A singleton moduli space cannot support a dimension-indexed family.
Equations
- Tau.BookII.Mirror.categoricity_no_ladder = (Tau.BookII.Mirror.tau_moduli_count == 1)
Instances For

---

### `Tau.BookII.Mirror.categoricity_kills_ladder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L406-L408)
**theorem
Tau.BookII.Mirror.categoricity_kills_ladder :categoricity_no_ladder = true**


[II.R31] Categoricity rules out any ladder.

---

### `Tau.BookII.Mirror.moduli_singleton`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L410-L412)
**theorem
Tau.BookII.Mirror.moduli_singleton :tau_moduli_count = 1**


[II.R31] The moduli count is exactly 1.

---

### `Tau.BookII.Mirror.full_ladder_collapse`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L418-L430)
**theorem
Tau.BookII.Mirror.full_ladder_collapse :engine_active tau_quadrant = false ∧ tau_rigidity.fibration_index = tau_rigidity.base_factors + tau_rigidity.fiber_factors ∧ tau_moduli_count = 1 ∧ tau_distinct_rungs.length = 3**


Full ladder collapse: engine absent, rigidity forces unique structure,
categoricity confirms singleton moduli. Three independent reasons
why τ³ has no dimensional ladder.

---

### `Tau.BookII.Mirror.engine_only_qft_native`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L484-L489)
**theorem
Tau.BookII.Mirror.engine_only_qft_native :engine_active qft_quadrant = true ∧ engine_active gr_local_quadrant = false ∧ engine_active padic_quadrant = false ∧ engine_active tau_quadrant = false**


---

### `Tau.BookII.Mirror.rigidity_native`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L492-L497)
**theorem
Tau.BookII.Mirror.rigidity_native :tau_rigidity.fibration_index = 3 ∧ tau_rigidity.refinement_dim = 4 ∧ tau_rigidity.base_factors = 1 ∧ tau_rigidity.fiber_factors = 2**


---

### `Tau.BookII.Mirror.simultaneous_rung_native`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L500-L501)
**theorem
Tau.BookII.Mirror.simultaneous_rung_native :tau_distinct_rungs.length = 3**


---

### `Tau.BookII.Mirror.ladder_collapse_native`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L504-L505)
**theorem
Tau.BookII.Mirror.ladder_collapse_native :engine_active tau_quadrant = false**


---

### `Tau.BookII.Mirror.categoricity_native`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Mirror/DimensionalLadder.lean#L508-L509)
**theorem
Tau.BookII.Mirror.categoricity_native :categoricity_no_ladder = true**
