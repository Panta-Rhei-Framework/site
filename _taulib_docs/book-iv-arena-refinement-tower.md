---
layout: taulib-doc
title: "TauLib.BookIV.Arena.RefinementTower"
permalink: /verify/taulib/docs/book-iv-arena-refinement-tower/
lane: verify
module_name: "TauLib.BookIV.Arena.RefinementTower"
book: "IV"
book_label: "Microcosm"
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
    book: "Book IV"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookIV.Arena.RefinementTower


Refinement tower and profinite structure of Category τ at E₁.

## Registry Cross-References


- [IV.D249] Refinement Tower R — `RefinementTower`

- [IV.D250] Profinite Limit α̂ — `ProfiniteLimit`

- [IV.P147] Subsystem Horizon — `subsystem_horizon`

- [IV.D251] Proto-Time t_p — `ProtoTime`

- [IV.P148] NNO from α-Orbit — `nno_from_alpha`

- [IV.T95] Structural Arrow of Time — `structural_arrow`


## Mathematical Content


The refinement tower R = lim←_n (τ/τ_n) of finite quotients provides the
microscopic structure. The completion α̂ of the α-orbit defines proto-time
as a directed ordering. The natural numbers object is recovered from orbit
depth indexing, and the irreversible arrow of time from the tower's directedness.

## Ground Truth Sources


- Chapter 3 of Book IV (2nd Edition)


---

### `Tau.BookIV.Arena.TowerLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L36-L43)
**structure
Tau.BookIV.Arena.TowerLevel :Type**


[IV.D249] A level in the refinement tower: quotient at depth n.
Each level captures the observable physics up to that resolution.

- depth : ℕ
Depth index (positive natural).

- depth_pos : self.depth > 0
Depth is positive (meaningful orbit level).

Instances For

---

### `Tau.BookIV.Arena.instReprTowerLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L43-L43)
**instance
Tau.BookIV.Arena.instReprTowerLevel :Repr TowerLevel**

Equations
- Tau.BookIV.Arena.instReprTowerLevel = { reprPrec := Tau.BookIV.Arena.instReprTowerLevel.repr }

---

### `Tau.BookIV.Arena.instReprTowerLevel.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L43-L43)
**def
Tau.BookIV.Arena.instReprTowerLevel.repr :TowerLevel → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.RefinementTower`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L45-L51)
**structure
Tau.BookIV.Arena.RefinementTower :Type**


[IV.D249] The refinement tower R: a sequence of levels ordered by depth.
R = lim←_n (τ/τ_n) — the profinite inverse limit.

- level : ℕ → TowerLevel
Level accessor.

- level_depth
(n : ℕ)
 : n > 0 → (self.level n).depth = n
Levels are indexed consecutively starting at 1.

Instances For

---

### `Tau.BookIV.Arena.canonical_tower`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L53-L57)
**def
Tau.BookIV.Arena.canonical_tower :RefinementTower**


Canonical refinement tower: level n has depth n.
Equations
- Tau.BookIV.Arena.canonical_tower = { level := fun (n : ℕ) => { depth := if n > 0 then n else 1, depth_pos := ⋯ },
 level_depth := Tau.BookIV.Arena.canonical_tower._proof_3 }
Instances For

---

### `Tau.BookIV.Arena.ProfiniteLimit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L63-L72)
**structure
Tau.BookIV.Arena.ProfiniteLimit :Type**


[IV.D250] The profinite limit α̂ = lim←_n α_n: completion of
the α-orbit providing the temporal substrate. Structurally,
α̂ is the sequence of all orbit levels.

- seed : Kernel.Generator
The generating generator (always α for temporal).

- seed_is_alpha : self.seed = Kernel.Generator.alpha
Seed is alpha.

- tower : RefinementTower
The tower providing the levels.

Instances For

---

### `Tau.BookIV.Arena.alpha_profinite`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L74-L78)
**def
Tau.BookIV.Arena.alpha_profinite :ProfiniteLimit**


The canonical profinite limit of the α-orbit.
Equations
- Tau.BookIV.Arena.alpha_profinite = { seed := Tau.Kernel.Generator.alpha, seed_is_alpha := ⋯, tower := Tau.BookIV.Arena.canonical_tower }
Instances For

---

### `Tau.BookIV.Arena.subsystem_horizon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L84-L87)
**theorem
Tau.BookIV.Arena.subsystem_horizon
(B : ℕ)
 :∃ (n : ℕ), n > B**


[IV.P147] Subsystem horizon: every finite subsystem can only
observe finitely many orbit levels. The profinite limit captures all.
Formalized as: for any finite bound B, there exist levels beyond B.

---

### `Tau.BookIV.Arena.ProtoTime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L93-L101)
**structure
Tau.BookIV.Arena.ProtoTime :Type**


[IV.D251] Proto-time: the ordering on α-orbit levels that defines
temporal succession before any metric. Earlier levels (smaller depth)
precede later levels (larger depth).

- tick : ℕ
Current depth in the tower.

- tick_pos : self.tick > 0
Tick is positive.

Instances For

---

### `Tau.BookIV.Arena.instReprProtoTime.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L101-L101)
**def
Tau.BookIV.Arena.instReprProtoTime.repr :ProtoTime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.instReprProtoTime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L101-L101)
**instance
Tau.BookIV.Arena.instReprProtoTime :Repr ProtoTime**

Equations
- Tau.BookIV.Arena.instReprProtoTime = { reprPrec := Tau.BookIV.Arena.instReprProtoTime.repr }

---

### `Tau.BookIV.Arena.instDecidableEqProtoTime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L101-L101)
**instance
Tau.BookIV.Arena.instDecidableEqProtoTime :DecidableEq ProtoTime**

Equations
- Tau.BookIV.Arena.instDecidableEqProtoTime = Tau.BookIV.Arena.instDecidableEqProtoTime.decEq

---

### `Tau.BookIV.Arena.instDecidableEqProtoTime.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L101-L101)
**def
Tau.BookIV.Arena.instDecidableEqProtoTime.decEq
(x✝ x✝¹ : ProtoTime)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Arena.instLTProtoTime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L103-L105)
**instance
Tau.BookIV.Arena.instLTProtoTime :LT ProtoTime**


Proto-time ordering: earlier ticks precede later ticks.
Equations
- Tau.BookIV.Arena.instLTProtoTime = { lt := fun (a b : Tau.BookIV.Arena.ProtoTime) => a.tick < b.tick }

---

### `Tau.BookIV.Arena.instDecidableRelProtoTimeLt`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L107-L108)
**instance
Tau.BookIV.Arena.instDecidableRelProtoTimeLt :DecidableRel fun (x1 x2 : ProtoTime) => x1 < x2**

Equations
- Tau.BookIV.Arena.instDecidableRelProtoTimeLt a b = inferInstanceAs (Decidable (a.tick < b.tick))

---

### `Tau.BookIV.Arena.prototime_to_nat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L114-L116)
**def
Tau.BookIV.Arena.prototime_to_nat
(t : ProtoTime)
 :ℕ**


[IV.P148] The natural numbers object ℕ is recovered from α-orbit
depth indexing: depth 1 ↦ 0, depth 2 ↦ 1, ...
Equations
- Tau.BookIV.Arena.prototime_to_nat t = t.tick - 1
Instances For

---

### `Tau.BookIV.Arena.nno_from_alpha`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L118-L120)
**theorem
Tau.BookIV.Arena.nno_from_alpha
(n : ℕ)
 :∃ (t : ProtoTime), prototime_to_nat t = n**


The map is surjective onto ℕ.

---

### `Tau.BookIV.Arena.structural_arrow`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L126-L130)
**theorem
Tau.BookIV.Arena.structural_arrow
(t1 t2 : ProtoTime)

(h : t1 < t2)
 :t2.tick > t1.tick**


[IV.T95] Structural arrow of time: the refinement tower is directed,
meaning deeper levels always refine shallower ones. This gives an
irreversible arrow: once at depth n, you cannot "un-refine" to n-1.

---

### `Tau.BookIV.Arena.arrow_transitive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L132-L135)
**theorem
Tau.BookIV.Arena.arrow_transitive
(t1 t2 t3 : ProtoTime)

(h12 : t1 < t2)

(h23 : t2 < t3)
 :t1 < t3**


Transitivity of the arrow.

---

### `Tau.BookIV.Arena.arrow_irreflexive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Arena/RefinementTower.lean#L137-L138)
**theorem
Tau.BookIV.Arena.arrow_irreflexive
(t : ProtoTime)
 :¬t < t**


Irreflexivity: no time tick precedes itself.
