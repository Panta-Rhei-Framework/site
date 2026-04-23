---
layout: taulib-doc
title: "TauLib.BookII.Regularity.IdempotentDecomposition"
permalink: /verify/taulib/docs/book-ii-regularity-idempotent-decomposition/
lane: verify
module_name: "TauLib.BookII.Regularity.IdempotentDecomposition"
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

# TauLib.BookII.Regularity.IdempotentDecomposition


Idempotent decomposition of tau-holomorphic functions into B-channel
and C-channel components via the canonical idempotents e₊, e₋.

## Registry Cross-References


- [II.L07] Idempotent Decomposition Lemma — `decompose_recovery_check`

- [II.D48] Canonical Decomposition — `idempotent_decompose`

- [II.P10] Decomposition Functoriality — `decompose_functorial_check`


## Mathematical Content


Every tau-holomorphic function f decomposes uniquely as
f = e₊ · f₊ + e₋ · f₋
where f₊(x) = e₊ · f(x) keeps the B-channel and f₋(x) = e₋ · f(x)
keeps the C-channel.

In sector coordinates (where multiplication is componentwise):


- e₊ = (1, 0) projects onto the B-sector

- e₋ = (0, 1) projects onto the C-sector


Key properties:


- **Recovery (II.L07):** proj_plus(f(x)) + proj_minus(f(x)) = f(x)

- **Orthogonality:** proj_plus * proj_minus = 0

- **Idempotency:** proj_plus² = proj_plus, proj_minus² = proj_minus

- **Functoriality (II.P10):** decomposition commutes with hol_compose


These follow from the sector-coordinate representation of SectorPair,
where mul and add are both componentwise.

---

### `Tau.BookII.Regularity.idempotent_decompose`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L45-L55)
**def
Tau.BookII.Regularity.idempotent_decompose
(bp : Polarity.SectorPair)
 :Polarity.SectorPair × Polarity.SectorPair**


[II.D48] Idempotent decomposition of a SectorPair into
B-channel and C-channel components.

Given bp = (B, C), returns:


- fst = e₊ · bp = (1,0) * (B,C) = (B, 0) [B-channel]

- snd = e₋ · bp = (0,1) * (B,C) = (0, C) [C-channel]


The decomposition is canonical: determined entirely by the
idempotent structure of the sector algebra.
Equations
- Tau.BookII.Regularity.idempotent_decompose bp = (Tau.Polarity.e_plus_sector.mul bp, Tau.Polarity.e_minus_sector.mul bp)
Instances For

---

### `Tau.BookII.Regularity.proj_plus`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L57-L59)
**def
Tau.BookII.Regularity.proj_plus
(bp : Polarity.SectorPair)
 :Polarity.SectorPair**


B-channel projection: keeps only the B-sector component.
Equations
- Tau.BookII.Regularity.proj_plus bp = Tau.Polarity.e_plus_sector.mul bp
Instances For

---

### `Tau.BookII.Regularity.proj_minus`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L61-L63)
**def
Tau.BookII.Regularity.proj_minus
(bp : Polarity.SectorPair)
 :Polarity.SectorPair**


C-channel projection: keeps only the C-sector component.
Equations
- Tau.BookII.Regularity.proj_minus bp = Tau.Polarity.e_minus_sector.mul bp
Instances For

---

### `Tau.BookII.Regularity.proj_plus_kills_c`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L69-L72)
**theorem
Tau.BookII.Regularity.proj_plus_kills_c
(bp : Polarity.SectorPair)
 :(proj_plus bp).c_sector = 0**


proj_plus kills the C-channel: the C-sector of e₊ · bp is always 0.

---

### `Tau.BookII.Regularity.proj_minus_kills_b`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L74-L77)
**theorem
Tau.BookII.Regularity.proj_minus_kills_b
(bp : Polarity.SectorPair)
 :(proj_minus bp).b_sector = 0**


proj_minus kills the B-channel: the B-sector of e₋ · bp is always 0.

---

### `Tau.BookII.Regularity.proj_plus_preserves_b`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L79-L82)
**theorem
Tau.BookII.Regularity.proj_plus_preserves_b
(bp : Polarity.SectorPair)
 :(proj_plus bp).b_sector = bp.b_sector**


proj_plus preserves the B-channel: the B-sector of e₊ · bp equals bp.b.

---

### `Tau.BookII.Regularity.proj_minus_preserves_c`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L84-L87)
**theorem
Tau.BookII.Regularity.proj_minus_preserves_c
(bp : Polarity.SectorPair)
 :(proj_minus bp).c_sector = bp.c_sector**


proj_minus preserves the C-channel: the C-sector of e₋ · bp equals bp.c.

---

### `Tau.BookII.Regularity.decompose_recovery`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L93-L102)
**theorem
Tau.BookII.Regularity.decompose_recovery
(bp : Polarity.SectorPair)
 :(proj_plus bp).add (proj_minus bp) = bp**


[II.L07] Idempotent Decomposition Lemma (formal):
e₊ · bp + e₋ · bp = bp for all sector pairs bp.

This is the fundamental decomposition: every element of the
bipolar spectral algebra decomposes uniquely into B-channel
and C-channel components, and the sum recovers the original.

---

### `Tau.BookII.Regularity.proj_orthogonal`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L104-L108)
**theorem
Tau.BookII.Regularity.proj_orthogonal
(bp : Polarity.SectorPair)
 :(proj_plus bp).mul (proj_minus bp) = { b_sector := 0, c_sector := 0 }**


Orthogonality: proj_plus(bp) * proj_minus(bp) = (0, 0).
The B-channel and C-channel carry independent information.

---

### `Tau.BookII.Regularity.proj_plus_idem`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L110-L113)
**theorem
Tau.BookII.Regularity.proj_plus_idem
(bp : Polarity.SectorPair)
 :proj_plus (proj_plus bp) = proj_plus bp**


Idempotency of proj_plus: projecting twice is the same as projecting once.

---

### `Tau.BookII.Regularity.proj_minus_idem`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L115-L118)
**theorem
Tau.BookII.Regularity.proj_minus_idem
(bp : Polarity.SectorPair)
 :proj_minus (proj_minus bp) = proj_minus bp**


Idempotency of proj_minus: projecting twice is the same as projecting once.

---

### `Tau.BookII.Regularity.decompose_recovery_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L124-L146)
**def
Tau.BookII.Regularity.decompose_recovery_check
(bound : Denotation.TauIdx)
 :Bool**


[II.L07] Computational check: e₊ · bp + e₋ · bp = bp
for all tau-admissible points in [2, bound].
Equations
- Tau.BookII.Regularity.decompose_recovery_check bound = Tau.BookII.Regularity.decompose_recovery_check.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Regularity.decompose_recovery_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L129-L145)@[irreducible]

**def
Tau.BookII.Regularity.decompose_recovery_check.go
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.stagefun_decompose`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L152-L162)
**def
Tau.BookII.Regularity.stagefun_decompose
(sf : Holomorphy.StageFun)
 :Holomorphy.StageFun × Holomorphy.StageFun**


[II.D48] Decompose a StageFun into its B-channel and C-channel
components. The B-channel component has c_fun = 0, the C-channel
component has b_fun = 0.

This is the stagewise lift of the idempotent decomposition.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.stagefun_decompose_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L164-L186)
**def
Tau.BookII.Regularity.stagefun_decompose_check
(bound db : Denotation.TauIdx)
 :Bool**


Stagewise decomposition recovery check: the B-part and C-part
of a StageFun, evaluated and combined as SectorPairs, recover
the original StageFun evaluation.
Equations
- Tau.BookII.Regularity.stagefun_decompose_check bound db = Tau.BookII.Regularity.stagefun_decompose_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Regularity.stagefun_decompose_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L170-L185)@[irreducible]

**def
Tau.BookII.Regularity.stagefun_decompose_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.decompose_functorial_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L192-L225)
**def
Tau.BookII.Regularity.decompose_functorial_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.P10] Decomposition functoriality check:
the idempotent decomposition commutes with holomorphic composition.

For endomorphisms f, g on the primorial tower:
proj_plus(f . g) = proj_plus(f) . proj_plus(g)
proj_minus(f . g) = proj_minus(f) . proj_minus(g)

In the stagefun setting, this means the B-channel of a composition
equals the composition of B-channels, and similarly for C-channels.
Equations
- Tau.BookII.Regularity.decompose_functorial_check bound db = Tau.BookII.Regularity.decompose_functorial_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Regularity.decompose_functorial_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L204-L224)@[irreducible]

**def
Tau.BookII.Regularity.decompose_functorial_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.decompose_functorial_extended`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L227-L255)
**def
Tau.BookII.Regularity.decompose_functorial_extended
(bound db : Denotation.TauIdx)
 :Bool**


[II.P10] Extended functoriality: test with multiple endomorphism pairs.
Equations
- Tau.BookII.Regularity.decompose_functorial_extended bound db = Tau.BookII.Regularity.decompose_functorial_extended.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.Regularity.decompose_functorial_extended.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L231-L254)@[irreducible]

**def
Tau.BookII.Regularity.decompose_functorial_extended.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.full_idempotent_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L261-L266)
**def
Tau.BookII.Regularity.full_idempotent_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L07 + II.D48 + II.P10] Complete idempotent decomposition verification.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.recovery_30`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L309-L310)
**theorem
Tau.BookII.Regularity.recovery_30 :decompose_recovery_check 30 = true**


---

### `Tau.BookII.Regularity.stagefun_decompose_12_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L313-L314)
**theorem
Tau.BookII.Regularity.stagefun_decompose_12_4 :stagefun_decompose_check 12 4 = true**


---

### `Tau.BookII.Regularity.functorial_12_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L317-L318)
**theorem
Tau.BookII.Regularity.functorial_12_4 :decompose_functorial_check 12 4 = true**


---

### `Tau.BookII.Regularity.functorial_ext_12_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L320-L321)
**theorem
Tau.BookII.Regularity.functorial_ext_12_4 :decompose_functorial_extended 12 4 = true**


---

### `Tau.BookII.Regularity.full_idempotent_12_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L324-L325)
**theorem
Tau.BookII.Regularity.full_idempotent_12_4 :full_idempotent_check 12 4 = true**
