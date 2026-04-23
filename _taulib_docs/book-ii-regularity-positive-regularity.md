---
layout: taulib-doc
title: "TauLib.BookII.Regularity.PositiveRegularity"
permalink: /verify/taulib/docs/book-ii-regularity-positive-regularity/
lane: verify
module_name: "TauLib.BookII.Regularity.PositiveRegularity"
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

# TauLib.BookII.Regularity.PositiveRegularity


tau-Regularity: stabilization of the evolution operator at finite depth,
and the regularity criterion via channel decomposition.

## Registry Cross-References


- [II.D49] tau-Regularity — `regularity_depth`, `is_regular`

- [II.T34] Regularity Criterion — `regularity_criterion_check`


## Mathematical Content


**D49 (tau-Regularity):** A point p is tau-regular for a function f if the
evolution operator stabilizes at some finite stage N. Concretely: there
exists N such that for all m >= N, the ABCD chart of reduce(x, m)
produces the same B and C coordinates as reduce(x, N).

The regularity depth rd_f(x) is the smallest such N. Since the primorial
tower is a profinite completion, stabilization at a finite stage means
the point's data is determined by finitely many prime factors.

**T34 (Regularity Criterion):** A point x is regular if and only if both
its B-channel and C-channel components stabilize independently:

is_regular(x) <=> is_b_stable(x) AND is_c_stable(x)

Moreover, the regularity depth is the maximum of the two channel depths:

rd_f(x) = max(rd_b(x), rd_c(x))

This follows from the idempotent decomposition (II.L07): since the
channels are orthogonal and complete, stabilization of the whole function
is equivalent to stabilization of each channel separately.

---

### `Tau.BookII.Regularity.b_stabilization_depth`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L48-L72)
**def
Tau.BookII.Regularity.b_stabilization_depth
(x db : Denotation.TauIdx)
 :ℕ**


[II.D49] B-channel stabilization depth: the smallest stage k
(starting from 1) at which the B-coordinate of from_tau_idx(reduce(x, k))
equals the B-coordinate at all subsequent stages up to db.

Returns the stabilization stage, or db+1 if no stabilization.
Equations
- Tau.BookII.Regularity.b_stabilization_depth x db = Tau.BookII.Regularity.b_stabilization_depth.go db x 1 (db + 1)
Instances For

---

### `Tau.BookII.Regularity.b_stabilization_depth.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L56-L64)@[irreducible]

**def
Tau.BookII.Regularity.b_stabilization_depth.go
(db : Denotation.TauIdx)

(x k fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.b_stabilization_depth.check_stable`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L66-L71)@[irreducible]

**def
Tau.BookII.Regularity.b_stabilization_depth.check_stable
(db : Denotation.TauIdx)

(x target j fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.c_stabilization_depth`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L74-L94)
**def
Tau.BookII.Regularity.c_stabilization_depth
(x db : Denotation.TauIdx)
 :ℕ**


[II.D49] C-channel stabilization depth: the smallest stage k
at which the C-coordinate stabilizes through all subsequent stages.
Equations
- Tau.BookII.Regularity.c_stabilization_depth x db = Tau.BookII.Regularity.c_stabilization_depth.go db x 1 (db + 1)
Instances For

---

### `Tau.BookII.Regularity.c_stabilization_depth.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L79-L86)@[irreducible]

**def
Tau.BookII.Regularity.c_stabilization_depth.go
(db : Denotation.TauIdx)

(x k fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.c_stabilization_depth.check_stable`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L88-L93)@[irreducible]

**def
Tau.BookII.Regularity.c_stabilization_depth.check_stable
(db : Denotation.TauIdx)

(x target j fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.regularity_depth`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L96-L123)
**def
Tau.BookII.Regularity.regularity_depth
(x db : Denotation.TauIdx)
 :ℕ**


[II.D49] Full regularity depth: the smallest stage k at which
BOTH the B-coordinate and C-coordinate stabilize.

By the regularity criterion (II.T34), this equals
max(b_depth, c_depth). We compute it directly for verification.
Equations
- Tau.BookII.Regularity.regularity_depth x db = Tau.BookII.Regularity.regularity_depth.go db x 1 (db + 1)
Instances For

---

### `Tau.BookII.Regularity.regularity_depth.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L104-L114)@[irreducible]

**def
Tau.BookII.Regularity.regularity_depth.go
(db : Denotation.TauIdx)

(x k fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.regularity_depth.check_both_stable`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L116-L122)@[irreducible]

**def
Tau.BookII.Regularity.regularity_depth.check_both_stable
(db : Denotation.TauIdx)

(x b_target c_target j fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.is_regular`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L129-L133)
**def
Tau.BookII.Regularity.is_regular
(x db : Denotation.TauIdx)
 :Bool**


[II.D49] A point x is tau-regular (within depth bound db) if the
evolution operator stabilizes before reaching the depth bound.
Returns true iff regularity_depth(x, db) <= db.
Equations
- Tau.BookII.Regularity.is_regular x db = decide (Tau.BookII.Regularity.regularity_depth x db ≤ db)
Instances For

---

### `Tau.BookII.Regularity.is_b_regular`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L135-L137)
**def
Tau.BookII.Regularity.is_b_regular
(x db : Denotation.TauIdx)
 :Bool**


B-channel regularity: the B-coordinate stabilizes.
Equations
- Tau.BookII.Regularity.is_b_regular x db = decide (Tau.BookII.Regularity.b_stabilization_depth x db ≤ db)
Instances For

---

### `Tau.BookII.Regularity.is_c_regular`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L139-L141)
**def
Tau.BookII.Regularity.is_c_regular
(x db : Denotation.TauIdx)
 :Bool**


C-channel regularity: the C-coordinate stabilizes.
Equations
- Tau.BookII.Regularity.is_c_regular x db = decide (Tau.BookII.Regularity.c_stabilization_depth x db ≤ db)
Instances For

---

### `Tau.BookII.Regularity.regularity_depth_max_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L147-L165)
**def
Tau.BookII.Regularity.regularity_depth_max_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T34] Regularity depth equals max of channel depths.
rd_f(x) = max(rd_b(x), rd_c(x)).

This follows from the orthogonality of the idempotent decomposition:
the full stabilization happens precisely when both channels have
independently stabilized.
Equations
- Tau.BookII.Regularity.regularity_depth_max_check bound db = Tau.BookII.Regularity.regularity_depth_max_check.go bound db 2 (bound + 1)
Instances For

---

### `Tau.BookII.Regularity.regularity_depth_max_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L156-L164)@[irreducible]

**def
Tau.BookII.Regularity.regularity_depth_max_check.go
(bound db : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.regularity_criterion_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L171-L192)
**def
Tau.BookII.Regularity.regularity_criterion_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T34] Regularity criterion: x is regular iff both B-channel
and C-channel are individually regular.

is_regular(x, db) <=> is_b_regular(x, db) AND is_c_regular(x, db)

This is the channel decomposition of regularity: the idempotent
decomposition (II.L07) guarantees that stabilization decomposes
into independent channel conditions.
Equations
- Tau.BookII.Regularity.regularity_criterion_check bound db = Tau.BookII.Regularity.regularity_criterion_check.go bound db 2 (bound + 1)
Instances For

---

### `Tau.BookII.Regularity.regularity_criterion_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L182-L191)@[irreducible]

**def
Tau.BookII.Regularity.regularity_criterion_check.go
(bound db : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.small_point_regularity_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L198-L211)
**def
Tau.BookII.Regularity.small_point_regularity_check
(db : Denotation.TauIdx)
 :Bool**


Small points (x < P_k for some k) are always regular at depth k,
because reduce(x, k) = x for x < P_k, so the ABCD chart is
constant from stage k onward.
Equations
- Tau.BookII.Regularity.small_point_regularity_check db = Tau.BookII.Regularity.small_point_regularity_check.go db 2 (Tau.Polarity.primorial db + 1)
Instances For

---

### `Tau.BookII.Regularity.small_point_regularity_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L204-L210)@[irreducible]

**def
Tau.BookII.Regularity.small_point_regularity_check.go
(db : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.evolution_stabilization_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L213-L239)
**def
Tau.BookII.Regularity.evolution_stabilization_check
(bound db : Denotation.TauIdx)
 :Bool**


Evolution stabilization: for regular points, the evolution operator
output at the regularity depth equals the output at all deeper stages.
Equations
- Tau.BookII.Regularity.evolution_stabilization_check bound db = Tau.BookII.Regularity.evolution_stabilization_check.go bound db 2 (bound + 1)
Instances For

---

### `Tau.BookII.Regularity.evolution_stabilization_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L218-L229)@[irreducible]

**def
Tau.BookII.Regularity.evolution_stabilization_check.go
(bound db : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.evolution_stabilization_check.check_deep`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L231-L238)@[irreducible]

**def
Tau.BookII.Regularity.evolution_stabilization_check.check_deep
(db : Denotation.TauIdx)

(x : ℕ)

(bp_rd : Polarity.SectorPair)

(rd k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.channel_stabilization_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L245-L282)
**def
Tau.BookII.Regularity.channel_stabilization_check
(bound db : Denotation.TauIdx)
 :Bool**


Channel-wise evolution stabilization: the B-component stabilizes
independently of the C-component, and vice versa.
This connects regularity back to the idempotent decomposition.
Equations
- Tau.BookII.Regularity.channel_stabilization_check bound db = Tau.BookII.Regularity.channel_stabilization_check.go bound db 2 (bound + 1)
Instances For

---

### `Tau.BookII.Regularity.channel_stabilization_check.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L251-L267)@[irreducible]

**def
Tau.BookII.Regularity.channel_stabilization_check.go
(bound db : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.channel_stabilization_check.check_b_stable`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L269-L274)@[irreducible]

**def
Tau.BookII.Regularity.channel_stabilization_check.check_b_stable
(x target from_k to_k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.channel_stabilization_check.check_c_stable`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L276-L281)@[irreducible]

**def
Tau.BookII.Regularity.channel_stabilization_check.check_c_stable
(x target from_k to_k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.full_regularity_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L288-L299)
**def
Tau.BookII.Regularity.full_regularity_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.D49 + II.T34] Complete regularity verification:


- Regularity depth = max of channel depths

- Regularity criterion (channel decomposition)

- Small point regularity

- Evolution stabilization

- Channel stabilization

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Regularity.depth_max_20_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L340-L341)
**theorem
Tau.BookII.Regularity.depth_max_20_4 :regularity_depth_max_check 20 4 = true**


---

### `Tau.BookII.Regularity.criterion_20_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L344-L345)
**theorem
Tau.BookII.Regularity.criterion_20_4 :regularity_criterion_check 20 4 = true**


---

### `Tau.BookII.Regularity.small_point_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L348-L349)
**theorem
Tau.BookII.Regularity.small_point_3 :small_point_regularity_check 3 = true**


---

### `Tau.BookII.Regularity.evolution_stab_20_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L352-L353)
**theorem
Tau.BookII.Regularity.evolution_stab_20_4 :evolution_stabilization_check 20 4 = true**


---

### `Tau.BookII.Regularity.channel_stab_20_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L356-L357)
**theorem
Tau.BookII.Regularity.channel_stab_20_4 :channel_stabilization_check 20 4 = true**


---

### `Tau.BookII.Regularity.full_regularity_15_4`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Regularity/PositiveRegularity.lean#L360-L361)
**theorem
Tau.BookII.Regularity.full_regularity_15_4 :full_regularity_check 15 4 = true**
