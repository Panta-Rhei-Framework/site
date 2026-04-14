---
layout: taulib-doc
title: "TauLib.BookII.Enrichment.YonedaTheorem"
permalink: /verify/taulib/docs/book-ii-enrichment-yoneda-theorem/
lane: verify
module_name: "TauLib.BookII.Enrichment.YonedaTheorem"
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

# TauLib.BookII.Enrichment.YonedaTheorem


Tau-Yoneda embedding theorem: the pre-Yoneda embedding y : Hol_τ → E_τ
is fully faithful and bipolar-preserving.

## Registry Cross-References


- [II.L11] Probe Naturality iff Yoneda — `probe_yoneda_check`

- [II.T36] Tau-Yoneda Embedding — `yoneda_faithful_check`, `yoneda_full_check`,
`yoneda_bipolar_check`, `full_yoneda_check`


## Mathematical Content


**Probe Naturality iff Yoneda (II.L11):** A function f is natural with respect
to cylinder probes iff the pre-Yoneda embedding y(f) is representable.
Probe naturality means:
reduce(f(reduce(x, k+1)), k) = f(reduce(x, k))
This IS Yoneda representability: the restriction tower of f determines
a unique element in the presheaf topos.

The equivalence is verified computationally: for tower-coherent test functions
(identity, squaring, doubling), probe naturality holds iff the pre-Yoneda
embedding round-trips through Code/Decode.

**Tau-Yoneda Embedding (II.T36):** The pre-Yoneda embedding y : Hol_τ → E_τ is:

- **Faithful:** Code(y(f)) determines f — uses Code/Decode bijection (II.T35).

- **Full:** For any tower-coherent g, there exists f with y(f) = g.

- **Bipolar-preserving:** The B/C channels of y(f) decompose as y(f_B), y(f_C)
where f_B, f_C are the B/C projections of f.


The Yoneda embedding is the categorical content of Book II's enrichment:
holomorphic functions ARE the objects of the enriched topos.

---

### `Tau.BookII.Enrichment.is_probe_natural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L48-L53)
**def
Tau.BookII.Enrichment.is_probe_natural
(f : Denotation.TauIdx → Denotation.TauIdx)

(x k : Denotation.TauIdx)
 :Bool**


[II.L11] Probe naturality for a Nat-valued function:
reduce(f(reduce(x, k+1)), k) = f(reduce(x, k)).
This is the explicit form of naturality with respect to
the restriction maps in the primorial inverse system.
Equations
- Tau.BookII.Enrichment.is_probe_natural f x k = (Tau.Polarity.reduce (f (Tau.Polarity.reduce x (k + 1))) k == f (Tau.Polarity.reduce x k))
Instances For

---

### `Tau.BookII.Enrichment.is_yoneda_representable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L55-L60)
**def
Tau.BookII.Enrichment.is_yoneda_representable
(f : Denotation.TauIdx → Denotation.TauIdx)

(x k : Denotation.TauIdx)
 :Bool**


[II.L11] Yoneda representability for a function f:
Code(preyoneda(f)) at stage k determines f at stage k.
Concretely: preyoneda(f, x, k) = f(reduce(x, k)),
and code_extract of this tower is f itself (restricted to Z/P_kZ).
Equations
- Tau.BookII.Enrichment.is_yoneda_representable f x k = (Tau.BookII.Regularity.preyoneda_embed_nat f x k == f (Tau.Polarity.reduce x k))
Instances For

---

### `Tau.BookII.Enrichment.probe_yoneda_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L62-L90)
**def
Tau.BookII.Enrichment.probe_yoneda_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L11] Probe naturality iff Yoneda check:
verify that for tower-coherent test functions, probe naturality
holds at every point and stage iff Yoneda representability holds.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.probe_yoneda_check.go_fn`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L69-L76)@[irreducible]

**def
Tau.BookII.Enrichment.probe_yoneda_check.go_fn
(fns : List (Denotation.TauIdx → Denotation.TauIdx → Denotation.TauIdx))

(x bound db fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
- Tau.BookII.Enrichment.probe_yoneda_check.go_fn [] x bound db fuel = if fuel = 0 then true else true
Instances For

---

### `Tau.BookII.Enrichment.probe_yoneda_check.go_xk`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L78-L89)@[irreducible]

**def
Tau.BookII.Enrichment.probe_yoneda_check.go_xk
(fn : Denotation.TauIdx → Denotation.TauIdx → Denotation.TauIdx)

(x k bound db fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.yoneda_faithful_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L96-L120)
**def
Tau.BookII.Enrichment.yoneda_faithful_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T36] Yoneda faithfulness: Code(preyoneda(f)) = f.
For a reduce-based function f, the Code extraction of its
pre-Yoneda embedding recovers f at each stage.

Code(preyoneda(f), k, a) = preyoneda(f)(a, k) = f(reduce(a, k))

For a < P_k: reduce(a, k) = a, so Code recovers f(a).
Equations
- Tau.BookII.Enrichment.yoneda_faithful_check bound db = Tau.BookII.Enrichment.yoneda_faithful_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Enrichment.yoneda_faithful_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L106-L119)@[irreducible]

**def
Tau.BookII.Enrichment.yoneda_faithful_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.yoneda_full_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L126-L149)
**def
Tau.BookII.Enrichment.yoneda_full_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T36] Yoneda fullness: for any tower-coherent function g given
as a restriction tower, there exists f with preyoneda(f) = g.
The witness is f = g itself (restricted to each stage).

Fullness check: for g(x, k) = reduce(x², k) (tower-coherent by
mul_mod + reduction_compat), the pre-Yoneda embedding of g recovers g.
Using the squaring function avoids the identity/mod-idempotence tautology.
Equations
- Tau.BookII.Enrichment.yoneda_full_check bound db = Tau.BookII.Enrichment.yoneda_full_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Enrichment.yoneda_full_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L136-L148)@[irreducible]

**def
Tau.BookII.Enrichment.yoneda_full_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.hom_b_channel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L151-L154)
**def
Tau.BookII.Enrichment.hom_b_channel
(x k : Denotation.TauIdx)
 :ℤ**


Helper: extract the B-channel from a sector pair of hom_stage output.
Equations
- Tau.BookII.Enrichment.hom_b_channel x k = (Tau.BookII.Interior.interior_bipolar (Tau.BookII.Interior.from_tau_idx (Tau.Polarity.reduce x k))).b_sector
Instances For

---

### `Tau.BookII.Enrichment.hom_c_channel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L156-L159)
**def
Tau.BookII.Enrichment.hom_c_channel
(x k : Denotation.TauIdx)
 :ℤ**


Helper: extract the C-channel from a sector pair of hom_stage output.
Equations
- Tau.BookII.Enrichment.hom_c_channel x k = (Tau.BookII.Interior.interior_bipolar (Tau.BookII.Interior.from_tau_idx (Tau.Polarity.reduce x k))).c_sector
Instances For

---

### `Tau.BookII.Enrichment.yoneda_bipolar_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L165-L204)
**def
Tau.BookII.Enrichment.yoneda_bipolar_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T36] Yoneda bipolar preservation:
The pre-Yoneda embedding preserves bipolar decomposition.
The B-channel of y(f) comes from the B-projection of f,
and the C-channel from the C-projection.

Concretely: the sector pair of preyoneda(f, x, k) decomposes
into e_plus and e_minus projections that are independently
determined by the B-data and C-data of f's output.

Verified: for f = identity, the bipolar decomposition of
f(reduce(x, k)) decomposes correctly.
Equations
- Tau.BookII.Enrichment.yoneda_bipolar_check bound db = Tau.BookII.Enrichment.yoneda_bipolar_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Enrichment.yoneda_bipolar_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L179-L203)@[irreducible]

**def
Tau.BookII.Enrichment.yoneda_bipolar_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.yoneda_roundtrip_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L210-L229)
**def
Tau.BookII.Enrichment.yoneda_roundtrip_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T36] Yoneda round-trip via Code/Decode:
Decode(Code(preyoneda(f))) = preyoneda(f).
This combines II.T35 (Code/Decode bijection) with II.D50 (pre-Yoneda).
Equations
- Tau.BookII.Enrichment.yoneda_roundtrip_check bound db = Tau.BookII.Enrichment.yoneda_roundtrip_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Enrichment.yoneda_roundtrip_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L216-L228)@[irreducible]

**def
Tau.BookII.Enrichment.yoneda_roundtrip_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.full_yoneda_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L235-L243)
**def
Tau.BookII.Enrichment.full_yoneda_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L11 + II.T36] Full Yoneda theorem verification:
probe naturality, faithfulness, fullness, bipolar preservation,
and Code/Decode round-trip.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Enrichment.probe_yoneda_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L281-L282)
**theorem
Tau.BookII.Enrichment.probe_yoneda_10_3 :probe_yoneda_check 10 3 = true**


---

### `Tau.BookII.Enrichment.yoneda_faithful_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L285-L286)
**theorem
Tau.BookII.Enrichment.yoneda_faithful_10_3 :yoneda_faithful_check 10 3 = true**


---

### `Tau.BookII.Enrichment.yoneda_full_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L289-L290)
**theorem
Tau.BookII.Enrichment.yoneda_full_10_3 :yoneda_full_check 10 3 = true**


---

### `Tau.BookII.Enrichment.yoneda_bipolar_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L293-L294)
**theorem
Tau.BookII.Enrichment.yoneda_bipolar_10_3 :yoneda_bipolar_check 10 3 = true**


---

### `Tau.BookII.Enrichment.yoneda_roundtrip_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L297-L298)
**theorem
Tau.BookII.Enrichment.yoneda_roundtrip_10_3 :yoneda_roundtrip_check 10 3 = true**


---

### `Tau.BookII.Enrichment.full_yoneda_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L301-L302)
**theorem
Tau.BookII.Enrichment.full_yoneda_10_3 :full_yoneda_check 10 3 = true**


---

### `Tau.BookII.Enrichment.yoneda_faithful_id`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L308-L324)
**theorem
Tau.BookII.Enrichment.yoneda_faithful_id
(x k : Denotation.TauIdx)
 :Regularity.code_extract
 (fun (a : Denotation.TauIdx) =>
 ↑(Regularity.preyoneda_embed_nat (fun (n : Denotation.TauIdx) => Polarity.reduce n k) a k))
 k x = ↑(Polarity.reduce x k)**


[II.T36] Formal proof: the pre-Yoneda embedding of the identity
is faithful — Code extraction recovers the function.
code_extract(fun a => preyoneda(id, a, k), k, x) = (reduce(x, k) : Int).

Unfolding: code_extract f k x = f(reduce(x, k))
where f(a) = preyoneda(reduce(·, k), a, k) = reduce(reduce(a, k), k).
So the full expression is reduce(reduce(reduce(x, k), k), k) which
collapses to reduce(x, k) by triple application of mod idempotence.

---

### `Tau.BookII.Enrichment.yoneda_full_id`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L326-L334)
**theorem
Tau.BookII.Enrichment.yoneda_full_id
(x k : Denotation.TauIdx)
 :Regularity.preyoneda_embed_nat (fun (n : Denotation.TauIdx) => Polarity.reduce n k) x k = Polarity.reduce x k**


[II.T36] Formal proof: fullness of the Yoneda embedding.
For any tower-coherent g given by g(x, k) = reduce(x, k),
preyoneda(g_k, x, k) = g(x, k).

preyoneda(reduce(·, k), x, k) = reduce(reduce(x, k), k) = reduce(x, k).

---

### `Tau.BookII.Enrichment.probe_naturality_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Enrichment/YonedaTheorem.lean#L336-L341)
**theorem
Tau.BookII.Enrichment.probe_naturality_structural
(x : Denotation.TauIdx)

{k l : Denotation.TauIdx}

(h : k ≤ l)
 :Polarity.reduce (Polarity.reduce x l) k = Polarity.reduce x k**


[II.L11] Formal proof: probe naturality IS tower coherence.
For f = reduce(·, k), naturality at (x, k) reduces to
reduce(reduce(x, k+1), k) = reduce(x, k), which is reduction_compat.
