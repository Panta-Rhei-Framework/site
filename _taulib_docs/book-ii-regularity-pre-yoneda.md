---
layout: taulib-doc
title: "TauLib.BookII.Regularity.PreYoneda"
permalink: /verify/taulib/docs/book-ii-regularity-pre-yoneda/
lane: verify
module_name: "TauLib.BookII.Regularity.PreYoneda"
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

# TauLib.BookII.Regularity.PreYoneda


Pre-Yoneda embedding: holomorphic functions as objects in the presheaf topos.

## Registry Cross-References


- [II.D50] Pre-Yoneda Embedding — `preyoneda_embed`, `preyoneda_tower_check`

- [II.P11] Functions as Objects — `preyoneda_bipolar_check`

- [II.R12] Probe Naturality = Holomorphy — `probe_naturality_check`


## Mathematical Content


The pre-Yoneda embedding y : Hol_tau -> d(tau^3) sends a holomorphic function f
to its omega-germ class, represented by its restriction tower. At each stage k:

preyoneda(f, x, k) = f(reduce(x, k))

This reads f at the stage-k representative of x. The tower of such readings
forms an element of the presheaf topos d(tau^3).

**Pre-Yoneda Embedding (II.D50):**
The map y(f)(x, k) = f(reduce(x, k)) is tower-coherent by construction:
reduce(y(f)(x, k+1), k) = reduce(f(reduce(x, k+1)), k)
and if f is reduce-compatible, this equals f(reduce(x, k)) = y(f)(x, k).

**Functions as Objects (II.P11):**
Holomorphic functions inherit ABCD coordinates via the embedding.
The bipolar decomposition is preserved: the B-channel of the embedded
function reads from the B-channel of f, and likewise for C.

**Probe Naturality = Holomorphy (II.R12):**
A function f is natural with respect to cylinder probes phi_{k,p} iff
preyoneda(f, x, k) = reduce(preyoneda(f, x, k+1), k)
This IS tower coherence, which IS holomorphy. The pre-Yoneda embedding
characterizes holomorphy as naturality of the probe system.

---

### `Tau.BookII.Regularity.preyoneda_embed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L51-L60)
**def
Tau.BookII.Regularity.preyoneda_embed
(f : Denotation.TauIdx → ℤ)

(x k : Denotation.TauIdx)
 :ℤ**


[II.D50] Pre-Yoneda embedding: maps a function f to its restriction tower.
At stage k, the embedding reads f at the stage-k representative of x.

preyoneda_embed(f, x, k) = f(reduce(x, k))

This is the fundamental representable presheaf construction:
f becomes the natural transformation Hom(-, f) restricted to the
primorial tower.
Equations
- Tau.BookII.Regularity.preyoneda_embed f x k = f (Tau.Polarity.reduce x k)
Instances For

---

### `Tau.BookII.Regularity.preyoneda_embed_nat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L62-L64)
**def
Tau.BookII.Regularity.preyoneda_embed_nat
(f : Denotation.TauIdx → Denotation.TauIdx)

(x k : Denotation.TauIdx)
 :Denotation.TauIdx**


Pre-Yoneda embedding for Nat-valued functions (used in decidable checks).
Equations
- Tau.BookII.Regularity.preyoneda_embed_nat f x k = f (Tau.Polarity.reduce x k)
Instances For

---

### `Tau.BookII.Regularity.preyoneda_tower_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L70-L96)
**def
Tau.BookII.Regularity.preyoneda_tower_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.D50] Tower coherence check for the pre-Yoneda embedding:
verify that for a reduce-based function f,
reduce(preyoneda(f, x, k+1), k) = preyoneda(f, x, k).

A reduce-based function satisfies f(reduce(x, k)) = reduce(f(x), k).
For such f, the pre-Yoneda embedding is tower-coherent:
reduce(f(reduce(x, k+1)), k) = f(reduce(reduce(x, k+1), k))
= f(reduce(x, k))

We test with f = reduce(_, stage) for various stages.
Equations
- Tau.BookII.Regularity.preyoneda_tower_check bound db = Tau.BookII.Regularity.preyoneda_tower_check.go bound db 2 1 (bound * db + bound + db + 1)
Instances For

---

### `Tau.BookII.Regularity.preyoneda_tower_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L83-L95)@[irreducible]

**def
Tau.BookII.Regularity.preyoneda_tower_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.preyoneda_identity_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L98-L110)
**def
Tau.BookII.Regularity.preyoneda_identity_check
(bound db : Denotation.TauIdx)
 :Bool**


Pre-Yoneda preserves the identity: preyoneda(id, x, k) = reduce(x, k).
The identity function embeds as the canonical reduction map.
Equations
- Tau.BookII.Regularity.preyoneda_identity_check bound db = Tau.BookII.Regularity.preyoneda_identity_check.go bound db 2 1 (bound * db + bound + db + 1)
Instances For

---

### `Tau.BookII.Regularity.preyoneda_identity_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L103-L109)@[irreducible]

**def
Tau.BookII.Regularity.preyoneda_identity_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.preyoneda_composition_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L112-L136)
**def
Tau.BookII.Regularity.preyoneda_composition_check
(bound db : Denotation.TauIdx)
 :Bool**


Pre-Yoneda commutes with composition:
preyoneda(g . f, x, k) = g(f(reduce(x, k)))
= g(preyoneda(f, x, k))

For reduce-based f and g, this also equals:
preyoneda(g, preyoneda(f, x, k), k).
Equations
- Tau.BookII.Regularity.preyoneda_composition_check bound db = Tau.BookII.Regularity.preyoneda_composition_check.go bound db 2 1 (bound * db + bound + db + 1)
Instances For

---

### `Tau.BookII.Regularity.preyoneda_composition_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L121-L135)@[irreducible]

**def
Tau.BookII.Regularity.preyoneda_composition_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.preyoneda_bipolar_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L142-L171)
**def
Tau.BookII.Regularity.preyoneda_bipolar_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.P11] Bipolar structure of the pre-Yoneda embedding:
the B-channel and C-channel of the embedded function decompose
independently.

For a function f, the pre-Yoneda image has bipolar coordinates:


- B-channel: from_tau_idx(preyoneda(f, x, k)).b

- C-channel: from_tau_idx(preyoneda(f, x, k)).c


We verify that the bipolar decomposition is consistent:
the sector pair from interior_bipolar applied to the embedded
point decomposes into e_plus and e_minus projections that
recombine to give the full sector pair.
Equations
- Tau.BookII.Regularity.preyoneda_bipolar_check bound db = Tau.BookII.Regularity.preyoneda_bipolar_check.go bound db 2 1 (bound * db + bound + db + 1)
Instances For

---

### `Tau.BookII.Regularity.preyoneda_bipolar_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L157-L170)@[irreducible]

**def
Tau.BookII.Regularity.preyoneda_bipolar_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.preyoneda_abcd_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L173-L189)
**def
Tau.BookII.Regularity.preyoneda_abcd_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.P11] ABCD coordinate check: the embedded function value
has well-defined ABCD coordinates at each stage.
from_tau_idx(preyoneda(id, x, k)) always produces a valid point.
Equations
- Tau.BookII.Regularity.preyoneda_abcd_check bound db = Tau.BookII.Regularity.preyoneda_abcd_check.go bound db 2 1 (bound * db + bound + db + 1)
Instances For

---

### `Tau.BookII.Regularity.preyoneda_abcd_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L179-L188)@[irreducible]

**def
Tau.BookII.Regularity.preyoneda_abcd_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.probe_naturality_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L195-L233)
**def
Tau.BookII.Regularity.probe_naturality_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.R12] Probe naturality check: a function f is natural with respect
to cylinder probes iff it is tower-coherent.

For cylinder probe phi_{k,prime_idx}: the probe evaluates f at
residue class v mod p at stage k. Naturality means:

preyoneda(f, x, k) = reduce(preyoneda(f, x, k+1), k)

This IS tower coherence. We verify for the canonical probes
(cylinder generators) that the naturality condition matches
tower coherence.
Equations
- Tau.BookII.Regularity.probe_naturality_check bound db = Tau.BookII.Regularity.probe_naturality_check.go bound db 2 1 1 (bound * db * db + bound + 1)
Instances For

---

### `Tau.BookII.Regularity.probe_naturality_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L209-L232)@[irreducible]

**def
Tau.BookII.Regularity.probe_naturality_check.go
(bound db : Denotation.TauIdx)

(x k pi_idx fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.probe_implies_tower_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L235-L252)
**def
Tau.BookII.Regularity.probe_implies_tower_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.R12] Probe naturality implies tower coherence:
if a function is natural with respect to ALL cylinder probes,
then it is tower-coherent. This is verified by checking that
naturality at every probe (k, pi_idx) implies the reduction
compatibility condition.
Equations
- Tau.BookII.Regularity.probe_implies_tower_check bound db = Tau.BookII.Regularity.probe_implies_tower_check.go bound db 2 1 (bound * db + bound + db + 1)
Instances For

---

### `Tau.BookII.Regularity.probe_implies_tower_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L243-L251)@[irreducible]

**def
Tau.BookII.Regularity.probe_implies_tower_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.full_preyoneda_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L258-L268)
**def
Tau.BookII.Regularity.full_preyoneda_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.D50 + II.P11 + II.R12] Complete pre-Yoneda verification:
embedding well-definedness, tower coherence, bipolar structure,
and probe naturality.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.preyoneda_tower_15_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L313-L314)
**theorem
Tau.BookII.Regularity.preyoneda_tower_15_4 :preyoneda_tower_check 15 4 = true**


---

### `Tau.BookII.Regularity.preyoneda_tower_20_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L316-L317)
**theorem
Tau.BookII.Regularity.preyoneda_tower_20_3 :preyoneda_tower_check 20 3 = true**


---

### `Tau.BookII.Regularity.preyoneda_identity_15_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L320-L321)
**theorem
Tau.BookII.Regularity.preyoneda_identity_15_4 :preyoneda_identity_check 15 4 = true**


---

### `Tau.BookII.Regularity.preyoneda_composition_12_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L324-L325)
**theorem
Tau.BookII.Regularity.preyoneda_composition_12_3 :preyoneda_composition_check 12 3 = true**


---

### `Tau.BookII.Regularity.preyoneda_bipolar_12_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L328-L329)
**theorem
Tau.BookII.Regularity.preyoneda_bipolar_12_3 :preyoneda_bipolar_check 12 3 = true**


---

### `Tau.BookII.Regularity.preyoneda_abcd_12_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L332-L333)
**theorem
Tau.BookII.Regularity.preyoneda_abcd_12_3 :preyoneda_abcd_check 12 3 = true**


---

### `Tau.BookII.Regularity.probe_nat_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L336-L337)
**theorem
Tau.BookII.Regularity.probe_nat_10_3 :probe_naturality_check 10 3 = true**


---

### `Tau.BookII.Regularity.probe_tower_15_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L340-L341)
**theorem
Tau.BookII.Regularity.probe_tower_15_4 :probe_implies_tower_check 15 4 = true**


---

### `Tau.BookII.Regularity.full_preyoneda_10_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L344-L345)
**theorem
Tau.BookII.Regularity.full_preyoneda_10_3 :full_preyoneda_check 10 3 = true**


---

### `Tau.BookII.Regularity.preyoneda_id_tower_coherent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L351-L360)
**theorem
Tau.BookII.Regularity.preyoneda_id_tower_coherent
(x : Denotation.TauIdx)

{k l : Denotation.TauIdx}

(h : k ≤ l)
 :Polarity.reduce (preyoneda_embed_nat (fun (n : Denotation.TauIdx) => n) x l) k = preyoneda_embed_nat (fun (n : Denotation.TauIdx) => n) x k**


[II.D50] Formal proof: the pre-Yoneda embedding of the identity
function is tower-coherent.

preyoneda(id, x, k) = reduce(x, k), so tower coherence reduces to
reduce(reduce(x, k+1), k) = reduce(x, k), which is reduction_compat.

---

### `Tau.BookII.Regularity.probe_naturality_is_tower_coherence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Regularity/PreYoneda.lean#L362-L367)
**theorem
Tau.BookII.Regularity.probe_naturality_is_tower_coherence
(x : Denotation.TauIdx)

{k l : Denotation.TauIdx}

(h : k ≤ l)
 :Polarity.reduce (Polarity.reduce x l) k = Polarity.reduce x k**


[II.R12] Formal proof: probe naturality IS tower coherence.
For the identity embedding, naturality at stage transition (k, k+1)
is exactly reduction_compat.
