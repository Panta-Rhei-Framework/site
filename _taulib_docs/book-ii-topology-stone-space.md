---
layout: taulib-doc
title: "TauLib.BookII.Topology.StoneSpace"
permalink: /verify/taulib/docs/book-ii-topology-stone-space/
lane: verify
module_name: "TauLib.BookII.Topology.StoneSpace"
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

# TauLib.BookII.Topology.StoneSpace


Stone space structure: compact, Hausdorff, totally disconnected.

## Registry Cross-References


- [II.D14] Stone Space — `StoneWitness`

- [II.T07] Compactness — `finite_subcover_check`

- [II.T08] Hausdorff Property — `hausdorff_check`

- [II.T09] Total Disconnectedness — `totally_disconnected_check`


## Mathematical Content


τ³ = lim←_k ℤ/M_kℤ is a Stone space:

- Compact: inverse limit of finite discrete spaces

- Hausdorff: distinct points separated by disjoint cylinders

- Totally disconnected: every connected component is a singleton


Proof of Hausdorff: for x ≠ y, let k = δ(x,y). Then C_{k+1}(x) and
C_{k+1}(y) are disjoint clopen sets separating x and y.

Proof of total disconnectedness: for x ≠ y in S ⊆ τ³, the clopen
cylinder C_{k+1}(x) splits S into two nonempty open parts.

---

### `Tau.BookII.Topology.hausdorff_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/StoneSpace.lean#L37-L55)
**def
Tau.BookII.Topology.hausdorff_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T08] Hausdorff: distinct points have disjoint cylinder
neighborhoods. For x ≠ y with δ(x,y) = k, the cylinders
C_{k+1}(x) and C_{k+1}(y) are disjoint.
Check: for all x ≠ y, find separating stage.
Equations
- Tau.BookII.Topology.hausdorff_check bound db = Tau.BookII.Topology.hausdorff_check.go bound db 2 2 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Topology.hausdorff_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/StoneSpace.lean#L44-L54)@[irreducible]

**def
Tau.BookII.Topology.hausdorff_check.go
(bound db : Denotation.TauIdx)

(x y fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.separating_stage`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/StoneSpace.lean#L57-L60)
**def
Tau.BookII.Topology.separating_stage
(x y db : Denotation.TauIdx)
 :Denotation.TauIdx**


Constructive witness: return the separating stage for x ≠ y.
Equations
- Tau.BookII.Topology.separating_stage x y db = if (x == y) = true then db + 1 else Tau.BookII.Domains.disagree_depth x y db + 1
Instances For

---

### `Tau.BookII.Topology.totally_disconnected_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/StoneSpace.lean#L66-L81)
**def
Tau.BookII.Topology.totally_disconnected_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.T09] Total disconnectedness: for x ≠ y, there exists a
clopen set containing x but not y (the separating cylinder).
Check: for all x ≠ y, verify the separating cylinder works.
Equations
- Tau.BookII.Topology.totally_disconnected_check bound db = Tau.BookII.Topology.totally_disconnected_check.go bound db 2 2 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookII.Topology.totally_disconnected_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/StoneSpace.lean#L72-L80)@[irreducible]

**def
Tau.BookII.Topology.totally_disconnected_check.go
(bound db : Denotation.TauIdx)

(x y fuel : Nat)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.finite_subcover_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/StoneSpace.lean#L87-L105)
**def
Tau.BookII.Topology.finite_subcover_check
(k bound : Denotation.TauIdx)
 :Bool**


[II.T07] Compactness: every cover by cylinders at stage k has
a finite subcover. For finite ranges, this is automatic since
ℤ/M_kℤ is finite (|ℤ/M_kℤ| = M_k residue classes).
Check: the number of stage-k cylinders in [2, bound] is finite.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.finite_subcover_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/StoneSpace.lean#L101-L104)@[irreducible]

**def
Tau.BookII.Topology.finite_subcover_check.go
(k bound : Denotation.TauIdx)

(y fuel : Nat)

(acc : List Denotation.TauIdx)
 :List Denotation.TauIdx**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.stone_space_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/StoneSpace.lean#L111-L118)
**def
Tau.BookII.Topology.stone_space_check
(bound db : Denotation.TauIdx)
 :Bool**


[II.D14] Stone space: compact + Hausdorff + totally disconnected.
Combined verification.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.StoneWitness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/StoneSpace.lean#L120-L126)
**structure
Tau.BookII.Topology.StoneWitness :Type**


Stone space witness structure: for each pair (x,y) with x ≠ y,
records the separating stage.

- x : Denotation.TauIdx
- y : Denotation.TauIdx
- sep_stage : Denotation.TauIdx
Instances For

---

### `Tau.BookII.Topology.instReprStoneWitness.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/StoneSpace.lean#L126-L126)
**def
Tau.BookII.Topology.instReprStoneWitness.repr :StoneWitness → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Topology.instReprStoneWitness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/StoneSpace.lean#L126-L126)
**instance
Tau.BookII.Topology.instReprStoneWitness :Repr StoneWitness**

Equations
- Tau.BookII.Topology.instReprStoneWitness = { reprPrec := Tau.BookII.Topology.instReprStoneWitness.repr }

---

### `Tau.BookII.Topology.stone_witness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/StoneSpace.lean#L128-L130)
**def
Tau.BookII.Topology.stone_witness
(x y db : Denotation.TauIdx)
 :StoneWitness**


Produce separation witness.
Equations
- Tau.BookII.Topology.stone_witness x y db = { x := x, y := y, sep_stage := Tau.BookII.Topology.separating_stage x y db }
Instances For

---

### `Tau.BookII.Topology.hausdorff_15`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/StoneSpace.lean#L150-L150)
**theorem
Tau.BookII.Topology.hausdorff_15 :hausdorff_check 15 5 = true**


---

### `Tau.BookII.Topology.td_15`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/StoneSpace.lean#L151-L151)
**theorem
Tau.BookII.Topology.td_15 :totally_disconnected_check 15 5 = true**


---

### `Tau.BookII.Topology.subcover_k1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/StoneSpace.lean#L152-L152)
**theorem
Tau.BookII.Topology.subcover_k1 :finite_subcover_check 1 20 = true**


---

### `Tau.BookII.Topology.subcover_k2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/StoneSpace.lean#L153-L153)
**theorem
Tau.BookII.Topology.subcover_k2 :finite_subcover_check 2 30 = true**


---

### `Tau.BookII.Topology.stone_12`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookII/Topology/StoneSpace.lean#L154-L154)
**theorem
Tau.BookII.Topology.stone_12 :stone_space_check 12 5 = true**
