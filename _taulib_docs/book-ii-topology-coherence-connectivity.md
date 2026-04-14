---
layout: taulib-doc
title: "TauLib.BookII.Topology.CoherenceConnectivity"
permalink: /verify/taulib/docs/book-ii-topology-coherence-connectivity/
lane: verify
module_name: "TauLib.BookII.Topology.CoherenceConnectivity"
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

# TauLib.BookII.Topology.CoherenceConnectivity


Connectivity via coherence: the two-readout principle.

## Registry Cross-References


- [II.D18a] Two-Readout Principle — `two_readout_check`

- [II.D18b] Spine Address Path — `spine_address_path`

- [II.R06a] Refinement Rays — `refinement_ray_check`


## Mathematical Content


The coherence kernel provides two parallel readouts on τ³:
(F) Fine-grain (topology): ultrametric cylinders, totally disconnected
(C) Coarse-grain (geometry): betweenness, congruence

These are parallel, not layered: topology does not produce geometry
via continuous paths (which don't exist in a Stone space).

Address-space connectivity replaces classical path-connectedness:
any two finite-stage points are connected by a spine address path
through the canonical base index α₁ = 2.

Refinement rays (one-sided ℕ-indexed orbit iterations via ρ) provide
the four independent canonical directions (A, B, C, D).

---

### `Tau.BookII.Topology.two_readout_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/CoherenceConnectivity.lean#L41-L81)
**def
Tau.BookII.Topology.two_readout_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.D18a] The two-readout principle: topology (fine-grain) and geometry
(coarse-grain) are parallel readouts of the coherence kernel.

Evidence: for pairs (x, y, z) where betweenness holds (B(x,y,z) = true),
the topological separating stage between x and y is INDEPENDENT of
the geometric betweenness relation — they probe different structure.

We verify:

- Topological separation always exists (Stone space, II.T09)

- Geometric betweenness exists for specific triples

- Both coexist on the same point set without contradiction

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.two_readout_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/CoherenceConnectivity.lean#L65-L71)@[irreducible]

**def
Tau.BookII.Topology.two_readout_check.go
(bound db : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.two_readout_check.go_yz`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/CoherenceConnectivity.lean#L73-L80)@[irreducible]

**def
Tau.BookII.Topology.two_readout_check.go_yz
(x y z bound db : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.spine_address_length`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/CoherenceConnectivity.lean#L87-L105)
**def
Tau.BookII.Topology.spine_address_length
(x : Denotation.TauIdx)
 :Denotation.TauIdx**


[II.D18b] Spine address path: the canonical route from X to Y through α₁ = 2.

Descent: X → greedy peel → (A,B,C,D) → extract D → continue until base
Ascent: α₁ → build up Y's ABCD address

The spine address length ℓ(X,Y) counts total peel steps.
Equations
- Tau.BookII.Topology.spine_address_length x = if x ≤ 2 then 0 else Tau.BookII.Topology.spine_address_length.go x 100
Instances For

---

### `Tau.BookII.Topology.spine_address_length.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/CoherenceConnectivity.lean#L98-L104)@[irreducible]

**def
Tau.BookII.Topology.spine_address_length.go
(n fuel : ℕ)
 :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.spine_address_path`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/CoherenceConnectivity.lean#L107-L109)
**def
Tau.BookII.Topology.spine_address_path
(x y : Denotation.TauIdx)
 :Denotation.TauIdx**


Spine address path from X to Y: total peel steps via α₁.
Equations
- Tau.BookII.Topology.spine_address_path x y = Tau.BookII.Topology.spine_address_length x + Tau.BookII.Topology.spine_address_length y
Instances For

---

### `Tau.BookII.Topology.address_connectivity_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/CoherenceConnectivity.lean#L111-L131)
**def
Tau.BookII.Topology.address_connectivity_check
(bound : Denotation.TauIdx)
 :Bool**


[II.D18b] Universal address connectivity: every pair of finite-stage
points has a spine address path of bounded length.
Verify: for all x, y in [2, bound], the path length is finite and bounded.
Equations
- Tau.BookII.Topology.address_connectivity_check bound = Tau.BookII.Topology.address_connectivity_check.go bound 2 (bound + 1)
Instances For

---

### `Tau.BookII.Topology.address_connectivity_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/CoherenceConnectivity.lean#L117-L122)@[irreducible]

**def
Tau.BookII.Topology.address_connectivity_check.go
(bound : Denotation.TauIdx)

(x fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.address_connectivity_check.go_y`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/CoherenceConnectivity.lean#L124-L130)@[irreducible]

**def
Tau.BookII.Topology.address_connectivity_check.go_y
(x y bound : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.alpha1_base_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/CoherenceConnectivity.lean#L133-L139)
**def
Tau.BookII.Topology.alpha1_base_check :Bool**


α₁ = 2 is the base index: its peel length is 0 (canonical root).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.refinement_ray_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/CoherenceConnectivity.lean#L145-L187)
**def
Tau.BookII.Topology.refinement_ray_check :Bool**


[II.R06a] Refinement rays: verify the four orbit rays are
one-sided (ℕ-indexed), independent, and canonical.

(i) One-sided: each ray starts at a fixed base element
(ii) Independent: ABCD coordinates of successive elements differ in one coordinate
(iii) Discrete: no intermediate points between successive orbit elements
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.two_readout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/CoherenceConnectivity.lean#L206-L206)
**theorem
Tau.BookII.Topology.two_readout :two_readout_check 12 5 = true**


---

### `Tau.BookII.Topology.addr_conn`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/CoherenceConnectivity.lean#L207-L207)
**theorem
Tau.BookII.Topology.addr_conn :address_connectivity_check 30 = true**


---

### `Tau.BookII.Topology.alpha1_base`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/CoherenceConnectivity.lean#L208-L208)
**theorem
Tau.BookII.Topology.alpha1_base :alpha1_base_check = true**


---

### `Tau.BookII.Topology.refine_ray`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/CoherenceConnectivity.lean#L209-L209)
**theorem
Tau.BookII.Topology.refine_ray :refinement_ray_check = true**
