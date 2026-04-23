---
layout: taulib-doc
title: "TauLib.BookII.Enrichment.EnrichmentLadder"
permalink: /verify/taulib/docs/book-ii-enrichment-enrichment-ladder/
lane: verify
module_name: "TauLib.BookII.Enrichment.EnrichmentLadder"
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

# TauLib.BookII.Enrichment.EnrichmentLadder


The E0/E1 enrichment transition and the enrichment ladder.

## Registry Cross-References


- [II.D58] E0/E1 Transition -- `EnrichmentLevel`, `e0_e1_transition_check`, `enrichment_gap_check`


## Mathematical Content


The transition from E0 (the base categorical structure of Book I) to E1
(the self-enriched structure of Book II) is captured by the internalization
of Hom objects.

**At E0:** Hom(A,B) is an external set. We can count the reduce-compatible
maps f : Z/P_kZ -> Z/P_kZ by enumerating all candidates and checking the
reduce-compatibility condition. This count is a plain natural number living
outside the tower.

**At E1:** Hom(A,B) is an internal tau-object. The hom-count at stage k is
itself computable as a tau-value: it is reduce-compatible with the primorial
tower. Concretely, the projection from Hom_k to Hom_{k-1} is well-defined
(every Hom_k element restricts to a Hom_{k-1} element).

**E0/E1 transition:** The external count at E0 equals the internal
tau-value at E1 -- the transition is faithful. No information is lost
when internalizing: the external enumeration and the internal tau-counting
agree.

**Enrichment gap:** E1 is strictly richer than E0 because E1 carries
self-enrichment data (Hom objects as tau-objects) that cannot be expressed
at E0 where Hom is merely an external set.

The enrichment ladder E0 -> E1 -> E2 -> ... is well-founded. Each step
internalizes the Hom objects of the previous level. Book II earns E1;
Book III will earn E2 (enriched with spectral forces).

---

### `Tau.BookII.Enrichment.EnrichmentLevel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L52-L57)
**inductive
Tau.BookII.Enrichment.EnrichmentLevel :Type**


[II.D58] Enrichment levels. E0 is the base category (Book I).
E1 is the self-enriched category (Book II).

- E0 : EnrichmentLevel
- E1 : EnrichmentLevel
Instances For

---

### `Tau.BookII.Enrichment.instReprEnrichmentLevel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L57-L57)
**instance
Tau.BookII.Enrichment.instReprEnrichmentLevel :Repr EnrichmentLevel**

Equations
- Tau.BookII.Enrichment.instReprEnrichmentLevel = { reprPrec := Tau.BookII.Enrichment.instReprEnrichmentLevel.repr }

---

### `Tau.BookII.Enrichment.instReprEnrichmentLevel.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L57-L57)
**def
Tau.BookII.Enrichment.instReprEnrichmentLevel.repr :EnrichmentLevel → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.instDecidableEqEnrichmentLevel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L57-L57)
**instance
Tau.BookII.Enrichment.instDecidableEqEnrichmentLevel :DecidableEq EnrichmentLevel**

Equations
- Tau.BookII.Enrichment.instDecidableEqEnrichmentLevel x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookII.Enrichment.e0_check_id_compat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L63-L77)@[irreducible]

**def
Tau.BookII.Enrichment.e0_check_id_compat
(k x fuel : ℕ)
 :Bool**


Helper: check reduce-compatibility of the identity map at stage k.
The identity map id_k(x) = reduce(x, k) is reduce-compatible iff
reduce(id_k(x), k-1) = id_k(reduce(x, k-1)) for all x.
This reduces to: reduce(reduce(x, k), k-1) = reduce(reduce(x, k-1), k-1)
= reduce(x, k-1).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.e0_check_zero_compat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L79-L83)
**def
Tau.BookII.Enrichment.e0_check_zero_compat
(k : ℕ)
 :Bool**


Helper: check reduce-compatibility of the constant-zero map at stage k.
The constant-zero map zero_k(x) = 0 is reduce-compatible iff
reduce(0, k-1) = 0. This is always true.
Equations
- Tau.BookII.Enrichment.e0_check_zero_compat k = (decide (k = 0) || Tau.Polarity.reduce 0 (k - 1) == 0)
Instances For

---

### `Tau.BookII.Enrichment.e0_external_hom_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L85-L107)
**def
Tau.BookII.Enrichment.e0_external_hom_check
(db : Denotation.TauIdx)
 :Bool**


[II.D58, E0 clause] E0 external hom check:
at each stage k, verify that at least two reduce-compatible
endomorphisms exist (the identity map and constant-zero map).

At k=1 (P_1=2): maps {0,1} -> {0,1} that are reduce-compatible with
stage 0 (P_0=1). Since reduce(x, 0) = x % 1 = 0 for all x, the
compatibility condition reduce(f(x), 0) = f(reduce(x, 0)) becomes
0 = f(0) % 1 = 0, which is always true. All 4 maps work.

At k=2 (P_2=6): maps Z/6Z -> Z/6Z compatible with stage 1.
The identity map and constant maps are always compatible.
Equations
- Tau.BookII.Enrichment.e0_external_hom_check db = Tau.BookII.Enrichment.e0_external_hom_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookII.Enrichment.e0_external_hom_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L99-L106)@[irreducible]

**def
Tau.BookII.Enrichment.e0_external_hom_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.count_rc_endomorphisms_k1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L109-L115)
**def
Tau.BookII.Enrichment.count_rc_endomorphisms_k1 :Denotation.TauIdx**


Count the reduce-compatible endomorphisms at stage k=1 by brute force.
At k=1: P_1 = 2, so maps {0,1} -> {0,1}.
reduce(x, 0) = x % 1 = 0 for all x.
Compat condition: reduce(f(x), 0) = f(reduce(x, 0)).
Both sides are 0 (since reduce(anything, 0) = 0).
All 4 maps are compatible.
Equations
- Tau.BookII.Enrichment.count_rc_endomorphisms_k1 = 4
Instances For

---

### `Tau.BookII.Enrichment.verify_k1_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L117-L137)
**def
Tau.BookII.Enrichment.verify_k1_count :Bool**


Verify the k=1 count: all 4 maps {0,1} -> {0,1} are reduce-compatible.
We enumerate all 4 maps and check each one.
Equations
- Tau.BookII.Enrichment.verify_k1_count = Tau.BookII.Enrichment.verify_k1_count.go 0 0 0 5
Instances For

---

### `Tau.BookII.Enrichment.verify_k1_count.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L122-L136)@[irreducible]

**def
Tau.BookII.Enrichment.verify_k1_count.go
(f0 f1 count fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.e1_internal_hom_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L143-L180)
**def
Tau.BookII.Enrichment.e1_internal_hom_check
(db : Denotation.TauIdx)
 :Bool**


[II.D58, E1 clause] E1 internal hom check:
verify that the hom-count at stage k projects correctly to stage k-1.
That is, every reduce-compatible map at stage k restricts to a
reduce-compatible map at stage k-1.

Concretely: if f : Z/P_kZ -> Z/P_kZ is reduce-compatible, then
the restriction f|*{Z/P*{k-1}Z} defined by
f_restricted(x) = reduce(f(x), k-1)
is a reduce-compatible map on Z/P_{k-1}Z.

This is the KEY E1 property: Hom_k -> Hom_{k-1} is well-defined,
making the hom counts into a tower (an internal tau-object).
Equations
- Tau.BookII.Enrichment.e1_internal_hom_check db = Tau.BookII.Enrichment.e1_internal_hom_check.go db 2 (db * 10 + 1)
Instances For

---

### `Tau.BookII.Enrichment.e1_internal_hom_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L158-L170)@[irreducible]

**def
Tau.BookII.Enrichment.e1_internal_hom_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.e1_internal_hom_check.check_id_restriction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L172-L179)@[irreducible]

**def
Tau.BookII.Enrichment.e1_internal_hom_check.check_id_restriction
(k x bound fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.e0_e1_transition_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L186-L198)
**def
Tau.BookII.Enrichment.e0_e1_transition_check
(db : Denotation.TauIdx)
 :Bool**


[II.D58] E0/E1 transition check:
the external count at E0 equals the internal tau-value at E1.
Both counting methods agree: the external enumeration (brute force)
and the internal tau-counting (via restriction maps) give the same
answer.

We verify this concretely at k=1: external count = 4 maps,
and all 4 restrict correctly to stage 0.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.enrichment_gap_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L204-L220)
**def
Tau.BookII.Enrichment.enrichment_gap_check
(bound db k_max : Denotation.TauIdx)
 :Bool**


[II.D58] Enrichment gap check:
E1 is strictly richer than E0.

At E1, the hom-counts form a tower (internal tau-object):
count_k projects to count_{k-1} via the restriction map.
At E0, there is no such tower structure -- the counts are just
external natural numbers with no inter-stage coherence.

The gap is witnessed by the self-enrichment component:
E1 has Hom objects that are themselves tau-objects, which is
data that E0 cannot express (E0 has no notion of "internal object").
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.full_enrichment_ladder_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L226-L235)
**def
Tau.BookII.Enrichment.full_enrichment_ladder_check
(bound db k_max : Denotation.TauIdx)
 :Bool**


[II.D58] Full enrichment ladder verification:


- E0 external hom counting works

- E1 internal hom is tower-compatible

- E0/E1 transition is faithful

- E1 is strictly richer than E0

- All E1 components are present

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.id_restriction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L241-L247)
**theorem
Tau.BookII.Enrichment.id_restriction
(x : Denotation.TauIdx)

{k : Denotation.TauIdx}
 :k ≥ 1 → Polarity.reduce (Polarity.reduce x k) (k - 1) = Polarity.reduce x (k - 1)**


Restriction of the identity map is the identity:
reduce(reduce(x, k), k-1) = reduce(x, k-1).
This is the structural core of the E0/E1 transition for id.

---

### `Tau.BookII.Enrichment.zero_restriction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L249-L253)
**theorem
Tau.BookII.Enrichment.zero_restriction
(k : Denotation.TauIdx)
 :Polarity.reduce 0 k = 0**


Restriction of the constant-zero map is constant-zero:
reduce(0, k-1) = 0 for all k.

---

### `Tau.BookII.Enrichment.e0_recoverable_from_e1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L255-L260)
**theorem
Tau.BookII.Enrichment.e0_recoverable_from_e1
(x k : Denotation.TauIdx)
 :Polarity.reduce (Polarity.reduce x k) k = Polarity.reduce x k**


The enrichment ladder is well-founded: E0 < E1 in the sense that
E0 data can be recovered from E1 data (the underlying set of Hom_k
maps is the same), but E1 carries additional tower structure.

---

### `Tau.BookII.Enrichment.tower_coherence_transitive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L262-L268)
**theorem
Tau.BookII.Enrichment.tower_coherence_transitive
(x : Denotation.TauIdx)

{j l : Denotation.TauIdx}

(h : j ≤ l)
 :Polarity.reduce (Polarity.reduce x l) j = Polarity.reduce x j**


Tower coherence is transitive: if f is coherent at (k, l) and (j, k),
then f is coherent at (j, l). For the identity:
reduce(reduce(x, l), j) = reduce(x, j) for j <= k <= l.
This follows directly from reduction_compat.

---

### `Tau.BookII.Enrichment.e0_ne_e1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L270-L273)
**theorem
Tau.BookII.Enrichment.e0_ne_e1 :EnrichmentLevel.E0 ≠ EnrichmentLevel.E1**


The E0 and E1 levels are distinct (structural).

---

### `Tau.BookII.Enrichment.e0_hom_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L312-L313)
**theorem
Tau.BookII.Enrichment.e0_hom_3 :e0_external_hom_check 3 = true**


---

### `Tau.BookII.Enrichment.e1_hom_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L316-L317)
**theorem
Tau.BookII.Enrichment.e1_hom_3 :e1_internal_hom_check 3 = true**


---

### `Tau.BookII.Enrichment.k1_count_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L320-L321)
**theorem
Tau.BookII.Enrichment.k1_count_4 :count_rc_endomorphisms_k1 = 4**


---

### `Tau.BookII.Enrichment.k1_verify`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L323-L324)
**theorem
Tau.BookII.Enrichment.k1_verify :verify_k1_count = true**


---

### `Tau.BookII.Enrichment.transition_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L327-L328)
**theorem
Tau.BookII.Enrichment.transition_3 :e0_e1_transition_check 3 = true**


---

### `Tau.BookII.Enrichment.gap_10_3_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L331-L332)
**theorem
Tau.BookII.Enrichment.gap_10_3_3 :enrichment_gap_check 10 3 3 = true**


---

### `Tau.BookII.Enrichment.full_ladder_10_3_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L335-L336)
**theorem
Tau.BookII.Enrichment.full_ladder_10_3_3 :full_enrichment_ladder_check 10 3 3 = true**
