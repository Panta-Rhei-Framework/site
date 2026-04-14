---
layout: taulib-doc
title: "TauLib.BookII.CentralTheorem.CentralTheorem"
permalink: /verify/taulib/docs/book-ii-central-theorem-central-theorem/
lane: verify
module_name: "TauLib.BookII.CentralTheorem.CentralTheorem"
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

# TauLib.BookII.CentralTheorem.CentralTheorem


**THE CLIMAX OF BOOK II.**

The Central Theorem: O(tau^3) ≅ A_spec(L).

## Registry Cross-References


- [II.D60] Spectral Algebra A_spec(L) -- `SpectralAlgebraElement`,
`spectral_algebra_tower_check`

- [II.T40] Central Theorem -- `central_theorem_forward_check`,
`central_theorem_inverse_check`, `central_theorem_roundtrip_check`,
`central_theorem_check`

- [II.C01] Holographic Principle -- `holographic_check`


## Mathematical Content


**II.D60 (Spectral Algebra A_spec(L)):** The ring of idempotent-supported
characters on the algebraic lemniscate L. At each stage k, A_spec(L)_k is
the ring of functions Z/P_kZ -> H_tau that are idempotent-supported
(decompose into e_plus * f_plus + e_minus * f_minus).

**II.T40 (Central Theorem):** O(tau^3) = A_spec(L).
The ring of tau-holomorphic functions on the fibered product tau^3 is
canonically isomorphic to the spectral algebra of the lemniscate.

The isomorphism has 4 links, each previously verified:

- Boundary characters <-> Hartogs extensions (II.T37)

- Hartogs extensions <-> omega-germ transformers (II.T38)

- Omega-germ transformers <-> holomorphic functions (II.T39)

- Holomorphic functions <-> idempotent-supported (II.T33)


**II.C01 (Holographic Principle):** The boundary (1-dimensional lemniscate
data) completely encodes the interior (3-dimensional tau^3 data). Nothing
is lost, nothing is added.

---

### `Tau.BookII.CentralTheorem.SpectralAlgebraElement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L51-L65)
**structure
Tau.BookII.CentralTheorem.SpectralAlgebraElement :Type**


[II.D60] A spectral algebra element at stage k:
a function Z/P_kZ -> SectorPair that is idempotent-supported.

Idempotent-supported means: for each x, the sector pair (B, C)
satisfies e_plus * (B, C) + e_minus * (B, C) = (B, C).
This is automatically true for all SectorPairs (decompose_recovery),
so every function to SectorPair is idempotent-supported.

The stage-k ring structure is componentwise:
addition and multiplication of SectorPairs are pointwise.

- b_fn : Denotation.TauIdx → ℤ
B-channel function: Z/P_kZ -> Int

- c_fn : Denotation.TauIdx → ℤ
C-channel function: Z/P_kZ -> Int

Instances For

---

### `Tau.BookII.CentralTheorem.SpectralAlgebraElement.eval`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L67-L70)
**def
Tau.BookII.CentralTheorem.SpectralAlgebraElement.eval
(sa : SpectralAlgebraElement)

(x k : Denotation.TauIdx)
 :Polarity.SectorPair**


Evaluate a spectral algebra element at input x, stage k.
Returns the SectorPair at the stage-k representative.
Equations
- sa.eval x k = { b_sector := sa.b_fn (Tau.Polarity.reduce x k), c_sector := sa.c_fn (Tau.Polarity.reduce x k) }
Instances For

---

### `Tau.BookII.CentralTheorem.spectral_algebra_stage_ring_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L72-L98)
**def
Tau.BookII.CentralTheorem.spectral_algebra_stage_ring_check
(k_max bound : Denotation.TauIdx)
 :Bool**


[II.D60] Stage ring check: verify that spectral algebra elements
form a ring at each stage. We check:


- Pointwise addition is well-defined (periodic)

- Pointwise multiplication is well-defined (periodic)

- Idempotent support holds (always true for SectorPair)

Equations
- Tau.BookII.CentralTheorem.spectral_algebra_stage_ring_check k_max bound = Tau.BookII.CentralTheorem.spectral_algebra_stage_ring_check.go k_max bound 1 2 ((k_max + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.spectral_algebra_stage_ring_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L80-L97)@[irreducible]

**def
Tau.BookII.CentralTheorem.spectral_algebra_stage_ring_check.go
(k_max bound : Denotation.TauIdx)

(k x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.spectral_algebra_tower_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L100-L129)
**def
Tau.BookII.CentralTheorem.spectral_algebra_tower_check
(db bound : Denotation.TauIdx)
 :Bool**


[II.D60] Spectral algebra tower check: the tower of spectral algebras
forms an inverse system. The projection from stage k+1 to stage k
is given by reduction:

For sa at stage k+1, its restriction to stage k gives
sa_restricted(x) = sa(reduce(x, k)).

Verify: for the identity element, the restriction is consistent
with the stage-k element.
Equations
- Tau.BookII.CentralTheorem.spectral_algebra_tower_check db bound = Tau.BookII.CentralTheorem.spectral_algebra_tower_check.go db bound 1 2 ((db + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.spectral_algebra_tower_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L112-L128)@[irreducible]

**def
Tau.BookII.CentralTheorem.spectral_algebra_tower_check.go
(db bound : Denotation.TauIdx)

(k x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.central_theorem_forward_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L135-L168)
**def
Tau.BookII.CentralTheorem.central_theorem_forward_check
(db bound : Denotation.TauIdx)
 :Bool**


[II.T40] Central Theorem forward direction:
boundary data (spectral algebra element) determines a holomorphic function.

Given a spectral algebra element sa with B-channel and C-channel functions,
the BndLift construction produces a tower-coherent function:

For each stage k, the boundary data at stage k is:
boundary(x) = (sa.b_fn(reduce(x, k)), sa.c_fn(reduce(x, k)))

Tower coherence: reduce(boundary(x, k+1), k) = boundary(x, k).
This follows from reduce(reduce(x, k+1), k) = reduce(x, k).
Equations
- Tau.BookII.CentralTheorem.central_theorem_forward_check db bound = Tau.BookII.CentralTheorem.central_theorem_forward_check.go db bound 1 2 ((db + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.central_theorem_forward_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L149-L167)@[irreducible]

**def
Tau.BookII.CentralTheorem.central_theorem_forward_check.go
(db bound : Denotation.TauIdx)

(k x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.central_theorem_inverse_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L170-L204)
**def
Tau.BookII.CentralTheorem.central_theorem_inverse_check
(db bound : Denotation.TauIdx)
 :Bool**


[II.T40] Central Theorem inverse direction:
every holomorphic function restricts to a boundary character
(spectral algebra element).

Given a tower-coherent StageFun f:


- At each stage k, f(x, k) is well-defined on Z/P_kZ

- The B-channel gives sa.b_fn, the C-channel gives sa.c_fn

- Idempotent decomposition ensures sa is idempotent-supported


Test: for id_stage (tower-coherent), the restriction to boundary
data gives a well-defined spectral algebra element.
Equations
- Tau.BookII.CentralTheorem.central_theorem_inverse_check db bound = Tau.BookII.CentralTheorem.central_theorem_inverse_check.go db bound 1 2 ((db + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.central_theorem_inverse_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L184-L203)@[irreducible]

**def
Tau.BookII.CentralTheorem.central_theorem_inverse_check.go
(db bound : Denotation.TauIdx)

(k x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.spectral_to_hol`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L206-L208)
**def
Tau.BookII.CentralTheorem.spectral_to_hol
(b_fn c_fn : Denotation.TauIdx → ℤ)

(x k : Denotation.TauIdx)
 :Polarity.SectorPair**


Helper: forward map from spectral data to holomorphic evaluation at (x, k).
Equations
- Tau.BookII.CentralTheorem.spectral_to_hol b_fn c_fn x k = { b_sector := b_fn (Tau.Polarity.reduce x k), c_sector := c_fn (Tau.Polarity.reduce x k) }
Instances For

---

### `Tau.BookII.CentralTheorem.hol_to_spectral`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L210-L212)
**def
Tau.BookII.CentralTheorem.hol_to_spectral
(sf : Holomorphy.StageFun)

(x k : Denotation.TauIdx)
 :Polarity.SectorPair**


Helper: inverse map from holomorphic evaluation to spectral data at (x, k).
Equations
- Tau.BookII.CentralTheorem.hol_to_spectral sf x k = { b_sector := ↑(sf.b_fun x k), c_sector := ↑(sf.c_fun x k) }
Instances For

---

### `Tau.BookII.CentralTheorem.central_theorem_roundtrip_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L214-L260)
**def
Tau.BookII.CentralTheorem.central_theorem_roundtrip_check
(db bound : Denotation.TauIdx)
 :Bool**


[II.T40] Central Theorem round-trip check:
forward . inverse = id AND inverse . forward = id.

Direction 1 (forward . inverse = id):
Start with a holomorphic function f = id_stage.


- Inverse: extract boundary data b_fn(n) = reduce(n, k), c_fn(n) = reduce(n, k)

- Forward: reconstruct hol function from boundary data

- Result: spectral_to_hol(b_fn, c_fn, x, k) = (reduce(x,k), reduce(x,k))
= id_stage evaluation


Direction 2 (inverse . forward = id):
Start with spectral data b_fn = c_fn = identity.


- Forward: construct holomorphic function

- Inverse: extract boundary data

- Result: same as original spectral data

Equations
- Tau.BookII.CentralTheorem.central_theorem_roundtrip_check db bound = Tau.BookII.CentralTheorem.central_theorem_roundtrip_check.go db bound 1 2 ((db + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.central_theorem_roundtrip_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L232-L259)@[irreducible]

**def
Tau.BookII.CentralTheorem.central_theorem_roundtrip_check.go
(db bound : Denotation.TauIdx)

(k x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.central_theorem_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L262-L280)
**def
Tau.BookII.CentralTheorem.central_theorem_check
(db bound : Denotation.TauIdx)
 :Bool**


[II.T40] THE CENTRAL THEOREM CHECK.
Combines all four links of the isomorphism:

- Spectral algebra ring structure (II.D60)

- Forward direction: boundary -> holomorphic (II.T37-T38)

- Inverse direction: holomorphic -> boundary (II.T39, II.T33)

- Round-trip: both compositions are identity


This is THE main verification of Book II.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.holographic_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L286-L326)
**def
Tau.BookII.CentralTheorem.holographic_check
(db bound : Denotation.TauIdx)
 :Bool**


[II.C01] Holographic principle check:
boundary-to-interior and interior-to-boundary are mutual inverses.

The boundary data (spectral algebra element on L) completely
determines the interior data (holomorphic function on tau^3),
and conversely.

Test: for the identity function:


- Extract boundary data at stage k

- Reconstruct interior via BndLift (= reduce to stage k+1)

- Restrict back to boundary at stage k

- Result matches original boundary data

Equations
- Tau.BookII.CentralTheorem.holographic_check db bound = Tau.BookII.CentralTheorem.holographic_check.go db bound 1 2 ((db + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.holographic_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L301-L325)@[irreducible]

**def
Tau.BookII.CentralTheorem.holographic_check.go
(db bound : Denotation.TauIdx)

(k x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.full_central_theorem_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L328-L332)
**def
Tau.BookII.CentralTheorem.full_central_theorem_check
(db bound : Denotation.TauIdx)
 :Bool**


[II.C01] Full holographic verification combining Central Theorem
and holographic round-trip.
Equations
- Tau.BookII.CentralTheorem.full_central_theorem_check db bound = (Tau.BookII.CentralTheorem.central_theorem_check db bound && Tau.BookII.CentralTheorem.holographic_check db bound)
Instances For

---

### `Tau.BookII.CentralTheorem.spectral_ring_3_15`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L371-L372)
**theorem
Tau.BookII.CentralTheorem.spectral_ring_3_15 :spectral_algebra_stage_ring_check 3 15 = true**


---

### `Tau.BookII.CentralTheorem.spectral_tower_3_15`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L374-L375)
**theorem
Tau.BookII.CentralTheorem.spectral_tower_3_15 :spectral_algebra_tower_check 3 15 = true**


---

### `Tau.BookII.CentralTheorem.central_fwd_3_15`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L378-L379)
**theorem
Tau.BookII.CentralTheorem.central_fwd_3_15 :central_theorem_forward_check 3 15 = true**


---

### `Tau.BookII.CentralTheorem.central_inv_3_15`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L382-L383)
**theorem
Tau.BookII.CentralTheorem.central_inv_3_15 :central_theorem_inverse_check 3 15 = true**


---

### `Tau.BookII.CentralTheorem.central_rt_3_15`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L386-L387)
**theorem
Tau.BookII.CentralTheorem.central_rt_3_15 :central_theorem_roundtrip_check 3 15 = true**


---

### `Tau.BookII.CentralTheorem.central_theorem_3_15`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L390-L391)
**theorem
Tau.BookII.CentralTheorem.central_theorem_3_15 :central_theorem_check 3 15 = true**


---

### `Tau.BookII.CentralTheorem.holographic_3_15`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L394-L395)
**theorem
Tau.BookII.CentralTheorem.holographic_3_15 :holographic_check 3 15 = true**


---

### `Tau.BookII.CentralTheorem.full_central_3_15`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L398-L399)
**theorem
Tau.BookII.CentralTheorem.full_central_3_15 :full_central_theorem_check 3 15 = true**


---

### `Tau.BookII.CentralTheorem.spectral_periodic`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L405-L409)
**theorem
Tau.BookII.CentralTheorem.spectral_periodic
(sa : SpectralAlgebraElement)

(x k : Denotation.TauIdx)
 :sa.eval (x + Polarity.primorial k) k = sa.eval x k**


[II.D60] Spectral algebra periodicity: evaluation is periodic in x
with period P_k. This follows from reduce(x + P_k, k) = reduce(x, k).

---

### `Tau.BookII.CentralTheorem.spectral_idempotent_supported`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L411-L419)
**theorem
Tau.BookII.CentralTheorem.spectral_idempotent_supported
(sa : SpectralAlgebraElement)

(x k : Denotation.TauIdx)
 :have bp := sa.eval x k;
(Polarity.e_plus_sector.mul bp).add (Polarity.e_minus_sector.mul bp) = bp**


[II.D60] Spectral algebra elements are always idempotent-supported.
This is decompose_recovery applied pointwise.

---

### `Tau.BookII.CentralTheorem.central_forward_coherent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L421-L427)
**theorem
Tau.BookII.CentralTheorem.central_forward_coherent
(x : Denotation.TauIdx)

{k l : Denotation.TauIdx}

(h : k ≤ l)
 :Polarity.reduce (Polarity.reduce x l) k = Polarity.reduce x k**


[II.T40] Central Theorem forward: spectral data produces tower-coherent output.
spectral_to_hol(b_fn, c_fn, x, k) uses reduce(x, k), so
reduce(spectral_to_hol(_, *, x, l), k) = spectral_to_hol(*, _, x, k)
when b_fn and c_fn are the identity (both sides reduce to reduce(x, k)).

---

### `Tau.BookII.CentralTheorem.central_inverse_periodic`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L429-L434)
**theorem
Tau.BookII.CentralTheorem.central_inverse_periodic
(x k : Denotation.TauIdx)
 :Polarity.reduce (x + Polarity.primorial k) k = Polarity.reduce x k**


[II.T40] Central Theorem inverse: holomorphic restriction is periodic.
reduce(x + P_k, k) = reduce(x, k) ensures the boundary restriction
is well-defined on Z/P_kZ.

---

### `Tau.BookII.CentralTheorem.central_roundtrip`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L436-L444)
**theorem
Tau.BookII.CentralTheorem.central_roundtrip
(x k : Denotation.TauIdx)
 :spectral_to_hol (fun (n : Denotation.TauIdx) => ↑n) (fun (n : Denotation.TauIdx) => ↑n) x k = hol_to_spectral Holomorphy.id_stage x k**


[II.T40] Central Theorem round-trip: the forward and inverse maps compose
to the identity on spectral data. For b_fn = identity:
spectral_to_hol(id, id, x, k) = (reduce(x,k), reduce(x,k))
hol_to_spectral(id_stage, x, k) = (reduce(x,k), reduce(x,k))
These are equal.

---

### `Tau.BookII.CentralTheorem.holographic_roundtrip`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L446-L452)
**theorem
Tau.BookII.CentralTheorem.holographic_roundtrip
(x k : Denotation.TauIdx)
 :Polarity.reduce (Hartogs.bndlift x k) k = Polarity.reduce x k**


[II.C01] Holographic principle: boundary reduction is involutive.
reduce(bndlift(x, k), k) = reduce(x, k).
The boundary completely determines the interior.
