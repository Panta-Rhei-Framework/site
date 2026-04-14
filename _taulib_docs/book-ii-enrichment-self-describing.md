---
layout: taulib-doc
title: "TauLib.BookII.Enrichment.SelfDescribing"
permalink: /verify/taulib/docs/book-ii-enrichment-self-describing/
lane: verify
module_name: "TauLib.BookII.Enrichment.SelfDescribing"
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

# TauLib.BookII.Enrichment.SelfDescribing


E1 Enrichment Layer: the self-describing layer of the primorial tower.

## Registry Cross-References


- [II.D57] E1 Enrichment Layer -- `E1Layer`, `compute_e1_layer`, `e1_layer_check`


## Mathematical Content


The E1 layer combines four ingredients:

- **Self-enrichment**: Hom objects are tau-objects (constant/identity maps exist at
each stage, so Hom(A,B) has a tau-index representation).

- **Yoneda embedding**: the pre-Yoneda embedding is faithful (Code extracts original
function values from the embedded tower).

- **2-category structure**: 2-morphisms (identity natural transformations) compose
vertically and horizontally, and vertical composition is tower-coherent.

- **Code/Decode bijection**: spectral analysis/synthesis bijection holds (from II.T35).


The E1 layer is the self-describing layer: the structure can describe its own
morphism spaces. This is E0 + "objects know their own morphism spaces". The
diagonal discipline (K5) prevents paradox because the primorial tower doesn't
allow unrestricted self-reference.

Key insight: at E0, Hom(A,B) is an external set of maps. At E1, Hom(A,B)
is an internal tau-object -- the count of reduce-compatible maps at each stage
is itself a tau-value that participates in the tower structure.

---

### `Tau.BookII.Enrichment.E1Layer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L43-L52)
**structure
Tau.BookII.Enrichment.E1Layer :Type**


[II.D57] The E1 enrichment layer bundles four boolean witnesses:
self-enrichment, Yoneda faithfulness, 2-category structure,
and Code/Decode bijection. All four must hold simultaneously
for the layer to be active.

- has_self_enrichment : Bool
- has_yoneda : Bool
- has_2cat : Bool
- has_code_decode : Bool
Instances For

---

### `Tau.BookII.Enrichment.instReprE1Layer.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L52-L52)
**def
Tau.BookII.Enrichment.instReprE1Layer.repr :E1Layer → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.instReprE1Layer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L52-L52)
**instance
Tau.BookII.Enrichment.instReprE1Layer :Repr E1Layer**

Equations
- Tau.BookII.Enrichment.instReprE1Layer = { reprPrec := Tau.BookII.Enrichment.instReprE1Layer.repr }

---

### `Tau.BookII.Enrichment.instDecidableEqE1Layer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L52-L52)
**instance
Tau.BookII.Enrichment.instDecidableEqE1Layer :DecidableEq E1Layer**

Equations
- Tau.BookII.Enrichment.instDecidableEqE1Layer = Tau.BookII.Enrichment.instDecidableEqE1Layer.decEq

---

### `Tau.BookII.Enrichment.instDecidableEqE1Layer.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L52-L52)
**def
Tau.BookII.Enrichment.instDecidableEqE1Layer.decEq
(x✝ x✝¹ : E1Layer)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.e1_self_enrichment_witness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L58-L93)
**def
Tau.BookII.Enrichment.e1_self_enrichment_witness
(bound db : Denotation.TauIdx)
 :Bool**


[II.D57, clause 1] Self-enrichment witness:
for each stage k in [1, db], verify that at least one
reduce-compatible endomorphism exists (the identity map and
constant maps are always reduce-compatible).

The identity map: reduce(reduce(x, k), k-1) = reduce(x, k-1)
follows from reduction_compat. This makes Hom(A,A) nonempty
at every stage, so Hom objects are genuine tau-objects.
Equations
- Tau.BookII.Enrichment.e1_self_enrichment_witness bound db = Tau.BookII.Enrichment.e1_self_enrichment_witness.go bound db 1 (bound * db + bound + db + 1)
Instances For

---

### `Tau.BookII.Enrichment.e1_self_enrichment_witness.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L69-L75)@[irreducible]

**def
Tau.BookII.Enrichment.e1_self_enrichment_witness.go
(bound db : Denotation.TauIdx)

(k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.e1_self_enrichment_witness.check_id`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L77-L85)@[irreducible]

**def
Tau.BookII.Enrichment.e1_self_enrichment_witness.check_id
(k x bound fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.e1_self_enrichment_witness.check_const`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L87-L92)@[irreducible]

**def
Tau.BookII.Enrichment.e1_self_enrichment_witness.check_const
(k x bound fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.e1_yoneda_witness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L99-L121)
**def
Tau.BookII.Enrichment.e1_yoneda_witness
(bound db : Denotation.TauIdx)
 :Bool**


[II.D57, clause 2] Yoneda witness:
the pre-Yoneda embedding is faithful -- for the identity function,
preyoneda_embed_nat(id, x, k) = reduce(x, k), and Code extracts
the original function value back.

Concretely: code_extract(f, k, x) = f(reduce(x, k)), so if
f = id then code_extract(id, k, x) = reduce(x, k) = preyoneda(id, x, k).
This is the Yoneda lemma in action: the embedding records enough data
to recover the original map.
Equations
- Tau.BookII.Enrichment.e1_yoneda_witness bound db = Tau.BookII.Enrichment.e1_yoneda_witness.go bound db 2 1 (bound * db + bound + db + 1)
Instances For

---

### `Tau.BookII.Enrichment.e1_yoneda_witness.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L111-L120)@[irreducible]

**def
Tau.BookII.Enrichment.e1_yoneda_witness.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.twocat_id_check_levels`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L127-L135)@[irreducible]

**def
Tau.BookII.Enrichment.twocat_id_check_levels
(x k l db fuel : ℕ)
 :Bool**


Helper: check tower coherence at levels k <= l <= db.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.twocat_id_tower_scan`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L137-L146)@[irreducible]

**def
Tau.BookII.Enrichment.twocat_id_tower_scan
(x k db fuel : ℕ)
 :Bool**


Helper: check that the identity 2-morphism is tower-coherent.
The identity 2-morphism maps (x, k) -> (reduce(x, k), k).
Tower coherence: reduce(reduce(x, l), k) = reduce(x, k) for k <= l.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.twocat_vert_comp_scan`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L148-L162)@[irreducible]

**def
Tau.BookII.Enrichment.twocat_vert_comp_scan
(x k db fuel : ℕ)
 :Bool**


Helper: vertical composition of squaring after identity.
sq ∘_v id at stage k: reduce((reduce(x, k))², k) should equal reduce(x², k).
This tests that composition of 2-cells is coherent with modular arithmetic
(relies on Nat.mul_mod, not just mod idempotence).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.twocat_horiz_comp_scan`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L164-L175)@[irreducible]

**def
Tau.BookII.Enrichment.twocat_horiz_comp_scan
(x k db fuel : ℕ)
 :Bool**


Helper: horizontal composition of squaring after doubling.
sq(dbl(x, k), k) = reduce((reduce(2x, k))², k) should equal
reduce((2x)², k) = reduce(4x², k). Tests mul_mod coherence.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.e1_2cat_witness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L177-L192)
**def
Tau.BookII.Enrichment.e1_2cat_witness
(bound db : Denotation.TauIdx)
 :Bool**


[II.D57, clause 3] 2-category witness:
verify that the identity 2-morphism is tower-coherent and that
vertical composition (id . id = id) holds at all stages.
Horizontal composition is also verified.
Equations
- Tau.BookII.Enrichment.e1_2cat_witness bound db = Tau.BookII.Enrichment.e1_2cat_witness.go bound db 2 (bound * (db + 1) + bound + 1)
Instances For

---

### `Tau.BookII.Enrichment.e1_2cat_witness.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L184-L191)@[irreducible]

**def
Tau.BookII.Enrichment.e1_2cat_witness.go
(bound db : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.e1_code_decode_witness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L198-L201)
**def
Tau.BookII.Enrichment.e1_code_decode_witness
(k_max : Denotation.TauIdx)
 :Bool**


[II.D57, clause 4] Code/Decode witness:
delegates to full_code_decode_check from CodeDecode.lean (II.T35).
Equations
- Tau.BookII.Enrichment.e1_code_decode_witness k_max = Tau.BookII.Regularity.full_code_decode_check k_max
Instances For

---

### `Tau.BookII.Enrichment.compute_e1_layer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L207-L213)
**def
Tau.BookII.Enrichment.compute_e1_layer
(bound db k_max : Denotation.TauIdx)
 :E1Layer**


[II.D57] Compute the E1 layer by evaluating all four witnesses.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.e1_layer_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L215-L219)
**def
Tau.BookII.Enrichment.e1_layer_check
(bound db k_max : Denotation.TauIdx)
 :Bool**


[II.D57] Check that all four E1 components are present.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.e1_completeness_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L221-L223)
**def
Tau.BookII.Enrichment.e1_completeness_check
(bound db k_max : Denotation.TauIdx)
 :Bool**


[II.D57] E1 completeness: all four components present simultaneously.
Equations
- Tau.BookII.Enrichment.e1_completeness_check bound db k_max = Tau.BookII.Enrichment.e1_layer_check bound db k_max
Instances For

---

### `Tau.BookII.Enrichment.const_zero_reduce_compat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L229-L235)
**theorem
Tau.BookII.Enrichment.const_zero_reduce_compat
(k : Denotation.TauIdx)
 :Polarity.reduce 0 k = 0**


Self-enrichment is closed under composition: if the identity
and constant maps are reduce-compatible, then their composition
(which is a constant map) is also reduce-compatible.
Formally: reduce(0, k) = 0 for all k.

---

### `Tau.BookII.Enrichment.id_reduce_compat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L237-L242)
**theorem
Tau.BookII.Enrichment.id_reduce_compat
(x : Denotation.TauIdx)

{j k : Denotation.TauIdx}

(h : j ≤ k)
 :Polarity.reduce (Polarity.reduce x k) j = Polarity.reduce x j**


The identity map is reduce-compatible: the Yoneda direction.
reduce(reduce(x, k), j) = reduce(x, j) for j <= k.
This is reduction_compat from ModArith.

---

### `Tau.BookII.Enrichment.vert_comp_idempotent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L244-L249)
**theorem
Tau.BookII.Enrichment.vert_comp_idempotent
(x k : Denotation.TauIdx)
 :Polarity.reduce (Polarity.reduce x k) k = Polarity.reduce x k**


Vertical composition of identity 2-morphisms is idempotent:
reduce(reduce(x, k), k) = reduce(x, k).
This is reduction_compat with k <= k.

---

### `Tau.BookII.Enrichment.self_enrichment_from_reduce_compat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L251-L257)
**theorem
Tau.BookII.Enrichment.self_enrichment_from_reduce_compat
(x k : Denotation.TauIdx)
 :k ≥ 1 → Polarity.reduce (Polarity.reduce x k) (k - 1) = Polarity.reduce x (k - 1)**


The E1 layer witnesses are individually well-defined:
self-enrichment follows from id_reduce_compat.
For k >= 1: reduce(reduce(x, k), k-1) = reduce(x, k-1).

---

### `Tau.BookII.Enrichment.e1_code_decode_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L259-L264)
**theorem
Tau.BookII.Enrichment.e1_code_decode_structural
(x k : Denotation.TauIdx)
 :Regularity.decode_reconstruct
 (fun (a : Denotation.TauIdx) => Regularity.code_extract (fun (n : Denotation.TauIdx) => ↑n) k a) k x = Regularity.code_extract (fun (n : Denotation.TauIdx) => ↑n) k x**


Code/Decode bijection correctness: Decode . Code = id for the identity.
This is structural from code_decode_id_roundtrip in CodeDecode.lean.

---

### `Tau.BookII.Enrichment.self_enrichment_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L295-L296)
**theorem
Tau.BookII.Enrichment.self_enrichment_10_3 :e1_self_enrichment_witness 10 3 = true**


---

### `Tau.BookII.Enrichment.yoneda_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L299-L300)
**theorem
Tau.BookII.Enrichment.yoneda_10_3 :e1_yoneda_witness 10 3 = true**


---

### `Tau.BookII.Enrichment.twocat_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L303-L304)
**theorem
Tau.BookII.Enrichment.twocat_10_3 :e1_2cat_witness 10 3 = true**


---

### `Tau.BookII.Enrichment.code_decode_bij_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L307-L308)
**theorem
Tau.BookII.Enrichment.code_decode_bij_3 :e1_code_decode_witness 3 = true**


---

### `Tau.BookII.Enrichment.e1_layer_10_3_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L311-L312)
**theorem
Tau.BookII.Enrichment.e1_layer_10_3_3 :e1_layer_check 10 3 3 = true**


---

### `Tau.BookII.Enrichment.e1_complete_10_3_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/SelfDescribing.lean#L315-L316)
**theorem
Tau.BookII.Enrichment.e1_complete_10_3_3 :e1_completeness_check 10 3 3 = true**
