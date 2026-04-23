---
layout: taulib-doc
title: "TauLib.BookII.CentralTheorem.HartogsExtension"
permalink: /verify/taulib/docs/book-ii-central-theorem-hartogs-extension/
lane: verify
module_name: "TauLib.BookII.CentralTheorem.HartogsExtension"
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

# TauLib.BookII.CentralTheorem.HartogsExtension


Extension of idempotent-supported characters to the interior via BndLift,
and uniqueness of the Hartogs extension.

## Registry Cross-References


- [II.L12] Extension in H_tau -- `extension_channel_check`

- [II.T37] Hartogs Extension Uniqueness -- `hartogs_uniqueness_check`, `boundary_determines_interior_check`


## Mathematical Content


**II.L12 (Extension in H_tau):** Every idempotent-supported character extends
to the interior via BndLift, channel by channel. The B-channel extends
independently, the C-channel extends independently.

BndLift(x, k) = reduce(x, k+1) gives the stage-(k+1) extension of
stage-k data. The key insight is that the extension preserves the
bipolar decomposition:


- The B-channel of bndlift(x, k) comes from the B-channel of x

- The C-channel of bndlift(x, k) comes from the C-channel of x


This is because from_tau_idx applied to reduce(x, k+1) decomposes via
the same ABCD chart, and the bipolar (B, C) channels are read from
the chart's B and C coordinates.

**II.T37 (Hartogs Extension Uniqueness):** Any tau-holomorphic function
on tau^3 whose boundary restriction is chi must coincide with the BndLift
extension. Uniqueness follows from:

- Bipolar channel independence (the B and C channels evolve independently)

- Code/Decode bijection (every function on Z/P_kZ is determined by its
CRT-indexed coefficients)

- Tower coherence (reduce(bndlift(x, k+1), k) = reduce(x, k))


If two extensions agree on the boundary (all stages), they agree everywhere.

---

### `Tau.BookII.CentralTheorem.extension_channel_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L51-L90)
**def
Tau.BookII.CentralTheorem.extension_channel_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L12] Extension channel check: for each boundary point x,
bndlift(x, k) preserves the B/C decomposition.

The B-channel of the lifted value comes from the B-channel of x:
specifically, the B-coordinate of from_tau_idx(bndlift(x, k))
is determined by the B-coordinate of from_tau_idx(reduce(x, k)).

Similarly, the C-channel of the lifted value comes from the
C-channel of x.

Since bndlift(x, k) = reduce(x, k+1), and
reduce(reduce(x, k+1), k) = reduce(x, k), the stage-k projection
of the lifted value recovers the original stage-k data. The ABCD chart
of the recovered data matches the original chart.
Equations
- Tau.BookII.CentralTheorem.extension_channel_check bound db = Tau.BookII.CentralTheorem.extension_channel_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.extension_channel_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L68-L89)@[irreducible]

**def
Tau.BookII.CentralTheorem.extension_channel_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.b_channel_extension_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L92-L116)
**def
Tau.BookII.CentralTheorem.b_channel_extension_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L12] Independent B-channel extension: the B-channel of the
bndlift extension is determined solely by the B-channel of the input.

Evidence: for inputs that differ only in C-coordinate (same B),
the B-component of the lifted value is the same. We check this
by comparing pairs of points with same reduce(x, k) but
different full values.
Equations
- Tau.BookII.CentralTheorem.b_channel_extension_check bound db = Tau.BookII.CentralTheorem.b_channel_extension_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.b_channel_extension_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L102-L115)@[irreducible]

**def
Tau.BookII.CentralTheorem.b_channel_extension_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.c_channel_extension_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L118-L135)
**def
Tau.BookII.CentralTheorem.c_channel_extension_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L12] Independent C-channel extension: the C-channel of the
bndlift extension is determined solely by the C-channel of the input.
Equations
- Tau.BookII.CentralTheorem.c_channel_extension_check bound db = Tau.BookII.CentralTheorem.c_channel_extension_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.c_channel_extension_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L123-L134)@[irreducible]

**def
Tau.BookII.CentralTheorem.c_channel_extension_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.hartogs_uniqueness_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L141-L170)
**def
Tau.BookII.CentralTheorem.hartogs_uniqueness_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T37] Hartogs uniqueness check: for test functions, verify that
two different extensions from the same boundary data give the same result.

The "two extensions" are:

- Direct bndlift: bndlift(x, k) = reduce(x, k+1)

- Alternative: reduce(bndlift(x, k+1), k) (lift one stage further, then reduce back)


Both must agree at stage k by tower coherence.
Equations
- Tau.BookII.CentralTheorem.hartogs_uniqueness_check bound db = Tau.BookII.CentralTheorem.hartogs_uniqueness_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.hartogs_uniqueness_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L152-L169)@[irreducible]

**def
Tau.BookII.CentralTheorem.hartogs_uniqueness_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.boundary_determines_interior_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L172-L212)
**def
Tau.BookII.CentralTheorem.boundary_determines_interior_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T37] Boundary determines interior check: for any two "functions"
that agree on the boundary (all stage reductions agree), they must
agree everywhere.

We verify this by checking that reduce(x, k) is determined by
the sequence of reduce(x, j) for j <= k. Specifically:
if reduce(x, k) = reduce(y, k) for all k <= db, then x and y
agree at all stages.
Equations
- Tau.BookII.CentralTheorem.boundary_determines_interior_check bound db = Tau.BookII.CentralTheorem.boundary_determines_interior_check.go bound db 2 2 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.boundary_determines_interior_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L183-L201)@[irreducible]

**def
Tau.BookII.CentralTheorem.boundary_determines_interior_check.go
(bound db : Denotation.TauIdx)

(x y fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.boundary_determines_interior_check.stages_agree`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L203-L206)@[irreducible]

**def
Tau.BookII.CentralTheorem.boundary_determines_interior_check.stages_agree
(db : Denotation.TauIdx)

(x y k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.boundary_determines_interior_check.lifts_agree`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L208-L211)@[irreducible]

**def
Tau.BookII.CentralTheorem.boundary_determines_interior_check.lifts_agree
(db : Denotation.TauIdx)

(x y k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.code_decode_uniqueness_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L214-L236)
**def
Tau.BookII.CentralTheorem.code_decode_uniqueness_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T37] Code/Decode witness for uniqueness: the Code/Decode bijection
(II.T35) ensures that a function on Z/P_kZ is uniquely determined by
its values. Combined with BndLift tower coherence, this means the
Hartogs extension is unique.

We verify: code_extract(bndlift_fn, k, x) = reduce(x, k) for
the bndlift "function" at stage k.
Equations
- Tau.BookII.CentralTheorem.code_decode_uniqueness_check bound db = Tau.BookII.CentralTheorem.code_decode_uniqueness_check.go bound db 2 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookII.CentralTheorem.code_decode_uniqueness_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L224-L235)@[irreducible]

**def
Tau.BookII.CentralTheorem.code_decode_uniqueness_check.go
(bound db : Denotation.TauIdx)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.full_hartogs_extension_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L242-L255)
**def
Tau.BookII.CentralTheorem.full_hartogs_extension_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.L12 + II.T37] Complete Hartogs extension verification:


- Extension channel preservation (II.L12)

- B-channel independence (II.L12)

- C-channel independence (II.L12)

- Uniqueness (II.T37)

- Boundary determines interior (II.T37)

- Code/Decode uniqueness witness (II.T37)

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.CentralTheorem.extension_preserves_stage`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L261-L268)
**theorem
Tau.BookII.CentralTheorem.extension_preserves_stage
(x k : Denotation.TauIdx)
 :Polarity.reduce (Hartogs.bndlift x k) k = Polarity.reduce x k**


[II.L12] Extension preserves stage-k data: the reduction of the
bndlift extension back to stage k recovers the original stage-k value.
reduce(bndlift(x, k), k) = reduce(x, k).
This follows from reduction_compat since bndlift(x, k) = reduce(x, k+1).

---

### `Tau.BookII.CentralTheorem.uniqueness_from_agreement`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L270-L277)
**theorem
Tau.BookII.CentralTheorem.uniqueness_from_agreement
(x y k : Denotation.TauIdx)

(h : Polarity.reduce x k = Polarity.reduce y k)
 :Polarity.reduce (Hartogs.bndlift x k) k = Polarity.reduce (Hartogs.bndlift y k) k**


[II.T37] Uniqueness structural core: two extensions that agree on all
stages must agree on the bndlift extension.
If reduce(x, k) = reduce(y, k), then bndlift at stage k gives the same
stage-k data: reduce(bndlift(x,k), k) = reduce(bndlift(y,k), k).

---

### `Tau.BookII.CentralTheorem.bndlift_tower`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L279-L285)
**theorem
Tau.BookII.CentralTheorem.bndlift_tower
(x k : Denotation.TauIdx)
 :Polarity.reduce (Hartogs.bndlift x (k + 1)) k = Polarity.reduce x k**


[II.T37] BndLift is tower-coherent: reduce(bndlift(x, k+1), k) = reduce(x, k).
This is the key structural property for Hartogs extension uniqueness.

---

### `Tau.BookII.CentralTheorem.extension_bipolar_recovery`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L287-L293)
**theorem
Tau.BookII.CentralTheorem.extension_bipolar_recovery
(x k : Denotation.TauIdx)
 :have bp := Interior.interior_bipolar (Interior.from_tau_idx (Hartogs.bndlift x k));
(Polarity.e_plus_sector.mul bp).add (Polarity.e_minus_sector.mul bp) = bp**


[II.L12] The interior bipolar decomposition of the extension
recovers via idempotent projections.

---

### `Tau.BookII.CentralTheorem.ext_channel_20_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L329-L330)
**theorem
Tau.BookII.CentralTheorem.ext_channel_20_4 :extension_channel_check 20 4 = true**


---

### `Tau.BookII.CentralTheorem.b_channel_20_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L333-L334)
**theorem
Tau.BookII.CentralTheorem.b_channel_20_4 :b_channel_extension_check 20 4 = true**


---

### `Tau.BookII.CentralTheorem.c_channel_20_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L337-L338)
**theorem
Tau.BookII.CentralTheorem.c_channel_20_4 :c_channel_extension_check 20 4 = true**


---

### `Tau.BookII.CentralTheorem.hartogs_uniq_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L341-L342)
**theorem
Tau.BookII.CentralTheorem.hartogs_uniq_15_4 :hartogs_uniqueness_check 15 4 = true**


---

### `Tau.BookII.CentralTheorem.bnd_det_int_10_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L345-L346)
**theorem
Tau.BookII.CentralTheorem.bnd_det_int_10_3 :boundary_determines_interior_check 10 3 = true**


---

### `Tau.BookII.CentralTheorem.cd_uniq_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L349-L350)
**theorem
Tau.BookII.CentralTheorem.cd_uniq_15_4 :code_decode_uniqueness_check 15 4 = true**


---

### `Tau.BookII.CentralTheorem.full_hartogs_ext_12_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L353-L354)
**theorem
Tau.BookII.CentralTheorem.full_hartogs_ext_12_3 :full_hartogs_extension_check 12 3 = true**
