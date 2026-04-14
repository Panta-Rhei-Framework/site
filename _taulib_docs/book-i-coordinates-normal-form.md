---
layout: taulib-doc
title: "TauLib.BookI.Coordinates.NormalForm"
permalink: /verify/taulib/docs/book-i-coordinates-normal-form/
lane: verify
module_name: "TauLib.BookI.Coordinates.NormalForm"
book: "I"
book_label: "Foundations"
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
    book: "Book I"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.Coordinates.NormalForm


Normal form encoding and spine decomposition on τ-Idx.

## Registry Cross-References


- [I.D16] Normal Form Encoding — `NFStep`, `NFStep.ofPeel`

- [I.D23] Spine Decomposition — `spine`, `list_tower_prod`, `spine_reconstruction`


## Ground Truth Sources


- chunk_0241_M002280: NF peel-off term definition (Def 2.12), spine decomposition


## Mathematical Content


Every X ≥ 2 in τ-Idx decomposes as T(A,B,C) · D via the greedy peel.
Iterating this peel until D = 1 produces the **spine**: an ordered list of
tower atom triples (Aᵢ, Bᵢ, Cᵢ) whose product equals X.

The spine is computable. Its correctness (product = X) is verified
computationally here; formal descent (D < X) is proved in the
Descent module.

---

### `Tau.Coordinates.NFStep`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/NormalForm.lean#L35-L41)
**structure
Tau.Coordinates.NFStep :Type**


[I.D16] A normal form step: (A, B, C, D) decomposing X = T(A,B,C) · D.

- A : Denotation.TauIdx
- B : Denotation.TauIdx
- C : Denotation.TauIdx
- D : Denotation.TauIdx
Instances For

---

### `Tau.Coordinates.instReprNFStep`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/NormalForm.lean#L41-L41)
**instance
Tau.Coordinates.instReprNFStep :Repr NFStep**

Equations
- Tau.Coordinates.instReprNFStep = { reprPrec := Tau.Coordinates.instReprNFStep.repr }

---

### `Tau.Coordinates.instReprNFStep.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/NormalForm.lean#L41-L41)
**def
Tau.Coordinates.instReprNFStep.repr :NFStep → Nat → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Coordinates.instDecidableEqNFStep`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/NormalForm.lean#L41-L41)
**instance
Tau.Coordinates.instDecidableEqNFStep :DecidableEq NFStep**

Equations
- Tau.Coordinates.instDecidableEqNFStep = Tau.Coordinates.instDecidableEqNFStep.decEq

---

### `Tau.Coordinates.instDecidableEqNFStep.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/NormalForm.lean#L41-L41)
**def
Tau.Coordinates.instDecidableEqNFStep.decEq
(x✝ x✝¹ : NFStep)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Coordinates.NFStep.ofPeel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/NormalForm.lean#L43-L46)
**def
Tau.Coordinates.NFStep.ofPeel
(x : Denotation.TauIdx)
 :NFStep**


Convert greedy_peel output to NFStep.
Equations
- Tau.Coordinates.NFStep.ofPeel x = match Tau.Coordinates.greedy_peel x with
 | (a, b, c, d) => { A := a, B := b, C := c, D := d }
Instances For

---

### `Tau.Coordinates.NFStep.atom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/NormalForm.lean#L48-L49)
**def
Tau.Coordinates.NFStep.atom
(s : NFStep)
 :Denotation.TauIdx**


The tower atom of an NF step.
Equations
- s.atom = Tau.Coordinates.tower_atom s.A s.B s.C
Instances For

---

### `Tau.Coordinates.NFStep.value`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/NormalForm.lean#L51-L52)
**def
Tau.Coordinates.NFStep.value
(s : NFStep)
 :Denotation.TauIdx**


NF step reconstruction value: T(A,B,C) * D.
Equations
- s.value = s.atom * s.D
Instances For

---

### `Tau.Coordinates.list_tower_prod`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/NormalForm.lean#L58-L61)
**def
Tau.Coordinates.list_tower_prod :List (Denotation.TauIdx × Denotation.TauIdx × Denotation.TauIdx) → Denotation.TauIdx**


Product of a list of tower atoms.
Equations
- Tau.Coordinates.list_tower_prod [] = 1
- Tau.Coordinates.list_tower_prod ((a, b, c) :: rest) = Tau.Coordinates.tower_atom a b c * Tau.Coordinates.list_tower_prod rest
Instances For

---

### `Tau.Coordinates.list_tower_prod_nil`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/NormalForm.lean#L63-L63)
**theorem
Tau.Coordinates.list_tower_prod_nil :list_tower_prod [] = 1**


---

### `Tau.Coordinates.list_tower_prod_cons`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/NormalForm.lean#L65-L66)
**theorem
Tau.Coordinates.list_tower_prod_cons
(a b c : Denotation.TauIdx)

(rest : List (Denotation.TauIdx × Denotation.TauIdx × Denotation.TauIdx))
 :list_tower_prod ((a, b, c) :: rest) = tower_atom a b c * list_tower_prod rest**


---

### `Tau.Coordinates.spine`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/NormalForm.lean#L72-L85)
**def
Tau.Coordinates.spine
(x : Denotation.TauIdx)
 :List (Denotation.TauIdx × Denotation.TauIdx × Denotation.TauIdx)**


[I.D23] Iterated greedy peel producing a spine of (A,B,C) triples.
Fuel-bounded; formal descent proved in the Descent module.
Equations
- Tau.Coordinates.spine x = if x ≤ 1 then [] else Tau.Coordinates.spine.go x x
Instances For

---

### `Tau.Coordinates.spine.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/NormalForm.lean#L78-L83)@[irreducible]

**def
Tau.Coordinates.spine.go
(x fuel : Denotation.TauIdx)
 :List (Denotation.TauIdx × Denotation.TauIdx × Denotation.TauIdx)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Coordinates.spine_length`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/NormalForm.lean#L87-L88)
**def
Tau.Coordinates.spine_length
(x : Denotation.TauIdx)
 :Nat**


Length of a spine.
Equations
- Tau.Coordinates.spine_length x = (Tau.Coordinates.spine x).length
Instances For

---

### `Tau.Coordinates.spine_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/NormalForm.lean#L94-L95)
**def
Tau.Coordinates.spine_check
(x : Denotation.TauIdx)
 :Bool**


Check that spine(x) reconstructs to x. Computable boolean test.
Equations
- Tau.Coordinates.spine_check x = (Tau.Coordinates.list_tower_prod (Tau.Coordinates.spine x) == x)
Instances For
