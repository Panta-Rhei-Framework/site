---
layout: taulib-doc
title: "TauLib.BookII.Topology.Invariant"
permalink: /verify/taulib/docs/book-ii-topology-invariant/
lane: verify
module_name: "TauLib.BookII.Topology.Invariant"
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

# TauLib.BookII.Topology.Invariant


Topology uniqueness: the profinite topology is the unique compact
Hausdorff topology compatible with CRT reductions.

## Registry Cross-References


- [II.T10] Topology Uniqueness — `topology_unique_check`


## Mathematical Content


The cylinder topology is the initial (coarsest) topology making all
CRT reduction maps π_k : τ³ → ℤ/M_kℤ continuous.

Theorem (II.T10): This is the UNIQUE topology on τ³ satisfying:
(a) CRT continuity: all π_k continuous
(b) Hausdorff separation
(c) Compactness

Proof: Any compact Hausdorff topology containing the initial topology
equals it (continuous bijection from compact to Hausdorff is homeomorphism).

Consequence: topology is earned (invariant of denotation), not chosen.

---

### `Tau.BookII.Topology.crt_continuous_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/Invariant.lean#L37-L58)
**def
Tau.BookII.Topology.crt_continuous_check
(k bound : Denotation.TauIdx)
 :Bool**


CRT reduction maps preserve cylinder structure:
if y ∈ C_k(x), then π_l(y) ∈ C_l(π_l(x)) for all l ≤ k.
This is the cylinder-theoretic definition of continuity.
Equations
- Tau.BookII.Topology.crt_continuous_check k bound = Tau.BookII.Topology.crt_continuous_check.go k bound 2 2 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Topology.crt_continuous_check.check_lower`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/Invariant.lean#L44-L47)@[irreducible]

**def
Tau.BookII.Topology.crt_continuous_check.check_lower
(x y k l fuel_l : Nat)
 :Bool**


Check all lower stages preserve agreement.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.crt_continuous_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/Invariant.lean#L49-L57)@[irreducible]

**def
Tau.BookII.Topology.crt_continuous_check.go
(k bound : Denotation.TauIdx)

(x y fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.topology_unique_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/Invariant.lean#L64-L76)
**def
Tau.BookII.Topology.topology_unique_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T10] Topology uniqueness verification.
The cylinder topology satisfies all three conditions:
(a) CRT continuous, (b) Hausdorff, (c) compact.
Any topology satisfying all three must equal the cylinder topology.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.reduction_compatible_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/Invariant.lean#L78-L92)
**def
Tau.BookII.Topology.reduction_compatible_check
(bound : Denotation.TauIdx)
 :Bool**


The reduction maps form a compatible family:
reduce(reduce(x, l), k) = reduce(x, k) for k ≤ l.
This is the defining property of an inverse system.
Equations
- Tau.BookII.Topology.reduction_compatible_check bound = Tau.BookII.Topology.reduction_compatible_check.go bound 1 1 2 ((bound + 1) * 5 * 5)
Instances For

---

### `Tau.BookII.Topology.reduction_compatible_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/Invariant.lean#L84-L91)@[irreducible]

**def
Tau.BookII.Topology.reduction_compatible_check.go
(bound : Denotation.TauIdx)

(k l x fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.crt_cont_k1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/Invariant.lean#L104-L104)
**theorem
Tau.BookII.Topology.crt_cont_k1 :crt_continuous_check 1 20 = true**


---

### `Tau.BookII.Topology.crt_cont_k2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/Invariant.lean#L105-L105)
**theorem
Tau.BookII.Topology.crt_cont_k2 :crt_continuous_check 2 20 = true**


---

### `Tau.BookII.Topology.topo_unique`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/Invariant.lean#L106-L106)
**theorem
Tau.BookII.Topology.topo_unique :topology_unique_check 12 5 = true**


---

### `Tau.BookII.Topology.red_compat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/Invariant.lean#L107-L107)
**theorem
Tau.BookII.Topology.red_compat :reduction_compatible_check 30 = true**
