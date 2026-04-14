---
layout: taulib-doc
title: "TauLib.BookII.Enrichment.SelfEnrichment"
permalink: /verify/taulib/docs/book-ii-enrichment-self-enrichment/
lane: verify
module_name: "TauLib.BookII.Enrichment.SelfEnrichment"
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

# TauLib.BookII.Enrichment.SelfEnrichment


Self-enrichment of the category Cat_τ: hom-objects are themselves τ-objects.

## Registry Cross-References


- [II.D53] Self-Enrichment Structure — `SelfEnrich`, `self_enrichment_check`

- [II.D54] Hom Object — `hom_obj_count`, `hom_obj_identity_check`

- [II.P12] Hom Bipolar Decomposition — `hom_bipolar_check`


## Mathematical Content


**Self-Enrichment (II.D53):** The category Cat_τ is self-enriched: for any
two τ-objects A, B, the morphism space Hom(A, B) is itself a τ-object.
At each stage k, Hom_k(A, B) = {f : Z/P_kZ → Z/P_kZ | reduce-compatible}.
The inverse limit gives Hom(A, B) = lim_k Hom_k(A, B).

The key insight is that the hom-space at each stage is a finite set of
reduce-compatible maps between finite cyclic groups, and these sets form
an inverse system (restrict from stage k+1 to stage k).

**Hom Object (II.D54):** Concretely, the Hom object at stage k counts
reduce-compatible maps. The identity and constant maps are always present,
so the count is always >= 2 (for non-trivial stages).

**Hom Bipolar Decomposition (II.P12):** The Hom object inherits bipolar
structure from the codomain. For any hom-element f, applying
interior_bipolar to f(x) and decomposing via e_plus/e_minus yields
independent B-channel and C-channel components. The decomposition is
orthogonal and complete.

---

### `Tau.BookII.Enrichment.hom_stage`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L46-L52)
**def
Tau.BookII.Enrichment.hom_stage
(a b k : Denotation.TauIdx)
 :Denotation.TauIdx**


[II.D53] Self-enrichment structure: hom-space at stage k.
hom_stage(a, b, k) = reduce(a, k) applied to b at stage k.
This represents the evaluation of the canonical hom-map:
the set of reduce-compatible maps on Z/P_kZ forms a τ-object
because it is itself closed under stage reduction.
Equations
- Tau.BookII.Enrichment.hom_stage a b k = Tau.Polarity.reduce (Tau.Polarity.reduce a k + Tau.Polarity.reduce b k) k
Instances For

---

### `Tau.BookII.Enrichment.hom_tower_coherent_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L54-L71)
**def
Tau.BookII.Enrichment.hom_tower_coherent_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.D53] Hom tower coherence check:
verify that hom_stage at stage k+1 reduces to hom_stage at stage k.
reduce(hom_stage(a, b, k+1), k) = hom_stage(a, b, k).
This ensures the hom-spaces form an inverse system.
Equations
- Tau.BookII.Enrichment.hom_tower_coherent_check bound db = Tau.BookII.Enrichment.hom_tower_coherent_check.go bound db 2 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Enrichment.hom_tower_coherent_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L61-L70)@[irreducible]

**def
Tau.BookII.Enrichment.hom_tower_coherent_check.go
(bound db : Denotation.TauIdx)

(a b k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.self_enrichment_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L73-L93)
**def
Tau.BookII.Enrichment.self_enrichment_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.D53] Self-enrichment check: for every pair (a, b) at stage k,
the hom-space is nonempty (at least the constant map sends a to 0,
and the identity sends a to reduce(a, k)).
We verify hom_stage is well-defined for all inputs.
Equations
- Tau.BookII.Enrichment.self_enrichment_check bound db = Tau.BookII.Enrichment.self_enrichment_check.go bound db 2 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Enrichment.self_enrichment_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L80-L92)@[irreducible]

**def
Tau.BookII.Enrichment.self_enrichment_check.go
(bound db : Denotation.TauIdx)

(a b k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.SelfEnrich`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L95-L102)
**structure
Tau.BookII.Enrichment.SelfEnrich :Type**


[II.D53] Self-enrichment structure.
Packages the hom-stage function with its tower coherence property.

- max_stage : Denotation.TauIdx
Maximum stage depth for verification.

- max_val : Denotation.TauIdx
Maximum input for verification.

Instances For

---

### `Tau.BookII.Enrichment.instReprSelfEnrich.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L102-L102)
**def
Tau.BookII.Enrichment.instReprSelfEnrich.repr :SelfEnrich → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.instReprSelfEnrich`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L102-L102)
**instance
Tau.BookII.Enrichment.instReprSelfEnrich :Repr SelfEnrich**

Equations
- Tau.BookII.Enrichment.instReprSelfEnrich = { reprPrec := Tau.BookII.Enrichment.instReprSelfEnrich.repr }

---

### `Tau.BookII.Enrichment.mk_self_enrich`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L104-L106)
**def
Tau.BookII.Enrichment.mk_self_enrich
(max_stage max_val : Denotation.TauIdx)
 :SelfEnrich**


Construct a SelfEnrich certificate.
Equations
- Tau.BookII.Enrichment.mk_self_enrich max_stage max_val = { max_stage := max_stage, max_val := max_val }
Instances For

---

### `Tau.BookII.Enrichment.is_reduce_compat_at`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L112-L125)
**def
Tau.BookII.Enrichment.is_reduce_compat_at
(f : Denotation.TauIdx → Denotation.TauIdx)

(k : Denotation.TauIdx)
 :Bool**


[II.D54] Helper: check if a map f on [0, P_k) is reduce-compatible.
A map f is reduce-compatible at stage k if f(reduce(x, k)) = reduce(f(x), k)
for all x in [0, P_k). For endomorphisms on Z/P_kZ, this means
f is a well-defined endomorphism of the cyclic group.
Equations
- Tau.BookII.Enrichment.is_reduce_compat_at f k = Tau.BookII.Enrichment.is_reduce_compat_at.go f k 0 (Tau.Polarity.primorial k + 1)
Instances For

---

### `Tau.BookII.Enrichment.is_reduce_compat_at.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L119-L124)@[irreducible]

**def
Tau.BookII.Enrichment.is_reduce_compat_at.go
(f : Denotation.TauIdx → Denotation.TauIdx)

(k x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.hom_obj_count_affine`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L127-L146)
**def
Tau.BookII.Enrichment.hom_obj_count_affine
(k : Denotation.TauIdx)
 :Denotation.TauIdx**


[II.D54] Hom object count at stage k: the number of reduce-compatible
endomorphisms on Z/P_kZ. We enumerate all maps of the form
x ↦ (a * x + b) mod P_k and count which are reduce-compatible.
(Affine maps are a subset; the full count includes more, but these
provide a lower bound.)
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.hom_obj_count_affine.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L137-L145)@[irreducible]

**def
Tau.BookII.Enrichment.hom_obj_count_affine.go
(k : Denotation.TauIdx)

(pk a b acc fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.hom_obj_identity_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L148-L158)
**def
Tau.BookII.Enrichment.hom_obj_identity_check
(db : Denotation.TauIdx)
 :Bool**


[II.D54] Identity map is always in Hom(A, A): reduce is a valid endomorphism.
Equations
- Tau.BookII.Enrichment.hom_obj_identity_check db = Tau.BookII.Enrichment.hom_obj_identity_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookII.Enrichment.hom_obj_identity_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L152-L157)@[irreducible]

**def
Tau.BookII.Enrichment.hom_obj_identity_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.hom_obj_constant_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L160-L170)
**def
Tau.BookII.Enrichment.hom_obj_constant_check
(db : Denotation.TauIdx)
 :Bool**


[II.D54] Constant 0 map is always in Hom(A, B): the zero map is reduce-compatible.
Equations
- Tau.BookII.Enrichment.hom_obj_constant_check db = Tau.BookII.Enrichment.hom_obj_constant_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookII.Enrichment.hom_obj_constant_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L164-L169)@[irreducible]

**def
Tau.BookII.Enrichment.hom_obj_constant_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.hom_obj_count_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L172-L184)
**def
Tau.BookII.Enrichment.hom_obj_count_check
(db : Denotation.TauIdx)
 :Bool**


[II.D54] Hom object count check: at each stage k >= 1, the number of
affine reduce-compatible endomorphisms is at least 2 (identity and constant).
For k=1 (P_1=2): identity x↦x, constant x↦0 are both reduce-compatible.
Equations
- Tau.BookII.Enrichment.hom_obj_count_check db = Tau.BookII.Enrichment.hom_obj_count_check.go db 1 (db + 1)
Instances For

---

### `Tau.BookII.Enrichment.hom_obj_count_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L178-L183)@[irreducible]

**def
Tau.BookII.Enrichment.hom_obj_count_check.go
(db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.hom_bipolar_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L190-L219)
**def
Tau.BookII.Enrichment.hom_bipolar_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.P12] Hom bipolar decomposition check.
For each hom-element (encoded as hom_stage(a, b, k)), decompose
the output via interior_bipolar and verify:

- e_plus projection + e_minus projection = full sector pair (completeness)

- e_plus(e_minus(x)) = 0 (orthogonality)


This verifies that the hom-object inherits the bipolar structure
from the codomain's sector decomposition.
Equations
- Tau.BookII.Enrichment.hom_bipolar_check bound db = Tau.BookII.Enrichment.hom_bipolar_check.go bound db 2 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Enrichment.hom_bipolar_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L201-L218)@[irreducible]

**def
Tau.BookII.Enrichment.hom_bipolar_check.go
(bound db : Denotation.TauIdx)

(a b k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.hom_channel_independence_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L221-L246)
**def
Tau.BookII.Enrichment.hom_channel_independence_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.P12] Bipolar channel independence check.
The B-channel of the hom-element depends only on the B-data of the inputs,
and similarly for the C-channel. Verified by checking that the sector
projections are consistent with the input structure.
Equations
- Tau.BookII.Enrichment.hom_channel_independence_check bound db = Tau.BookII.Enrichment.hom_channel_independence_check.go bound db 2 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Enrichment.hom_channel_independence_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L228-L245)@[irreducible]

**def
Tau.BookII.Enrichment.hom_channel_independence_check.go
(bound db : Denotation.TauIdx)

(a b k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.full_self_enrichment_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L252-L262)
**def
Tau.BookII.Enrichment.full_self_enrichment_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.D53 + II.D54 + II.P12] Full self-enrichment verification:
tower coherence, enrichment well-definedness, hom object properties,
and bipolar decomposition.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.hom_tower_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L305-L306)
**theorem
Tau.BookII.Enrichment.hom_tower_8_3 :hom_tower_coherent_check 8 3 = true**


---

### `Tau.BookII.Enrichment.self_enrich_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L309-L310)
**theorem
Tau.BookII.Enrichment.self_enrich_8_3 :self_enrichment_check 8 3 = true**


---

### `Tau.BookII.Enrichment.hom_identity_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L313-L314)
**theorem
Tau.BookII.Enrichment.hom_identity_3 :hom_obj_identity_check 3 = true**


---

### `Tau.BookII.Enrichment.hom_constant_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L317-L318)
**theorem
Tau.BookII.Enrichment.hom_constant_3 :hom_obj_constant_check 3 = true**


---

### `Tau.BookII.Enrichment.hom_count_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L321-L322)
**theorem
Tau.BookII.Enrichment.hom_count_3 :hom_obj_count_check 3 = true**


---

### `Tau.BookII.Enrichment.hom_bipolar_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L325-L326)
**theorem
Tau.BookII.Enrichment.hom_bipolar_8_3 :hom_bipolar_check 8 3 = true**


---

### `Tau.BookII.Enrichment.hom_channel_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L329-L330)
**theorem
Tau.BookII.Enrichment.hom_channel_8_3 :hom_channel_independence_check 8 3 = true**


---

### `Tau.BookII.Enrichment.full_self_enrich_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L333-L334)
**theorem
Tau.BookII.Enrichment.full_self_enrich_8_3 :full_self_enrichment_check 8 3 = true**


---

### `Tau.BookII.Enrichment.hom_stage_reduce_stable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L340-L346)
**theorem
Tau.BookII.Enrichment.hom_stage_reduce_stable
(a b k : Denotation.TauIdx)
 :Polarity.reduce (hom_stage a b k) k = hom_stage a b k**


[II.D53] Formal proof: hom_stage is reduce-stable.
reduce(hom_stage(a, b, k), k) = hom_stage(a, b, k).
This follows from reduce(reduce(x, k), k) = reduce(x, k).

---

### `Tau.BookII.Enrichment.hom_bipolar_complete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L348-L356)
**theorem
Tau.BookII.Enrichment.hom_bipolar_complete
(sp : Polarity.SectorPair)
 :(Polarity.e_plus_sector.mul sp).add (Polarity.e_minus_sector.mul sp) = sp**


[II.P12] Formal proof: bipolar decomposition of hom outputs is complete.
proj_plus(sp) + proj_minus(sp) = sp, for any sector pair sp.
This follows from e_plus * sp + e_minus * sp = (1,0)*(B,C) + (0,1)*(B,C)
= (B,0) + (0,C) = (B,C) = sp.

---

### `Tau.BookII.Enrichment.hom_bipolar_orthogonal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L358-L363)
**theorem
Tau.BookII.Enrichment.hom_bipolar_orthogonal
(sp : Polarity.SectorPair)
 :Polarity.e_plus_sector.mul (Polarity.e_minus_sector.mul sp) = { b_sector := 0, c_sector := 0 }**


[II.P12] Formal proof: bipolar projections are orthogonal.
e_plus * (e_minus * sp) = (0, 0) for any sector pair sp.

---

### `Tau.BookII.Enrichment.zero_map_compat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfEnrichment.lean#L365-L370)
**theorem
Tau.BookII.Enrichment.zero_map_compat
(_x k : Denotation.TauIdx)
 :Polarity.reduce 0 k = 0**


[II.D54] Formal proof: the constant 0 map is reduce-compatible.
reduce(0, k) = 0 for all k, so the zero map trivially satisfies
f(reduce(x, k)) = reduce(f(x), k).
