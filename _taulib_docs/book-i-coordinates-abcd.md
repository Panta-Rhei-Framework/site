---
layout: taulib-doc
title: "TauLib.BookI.Coordinates.ABCD"
permalink: /verify/taulib/docs/book-i-coordinates-abcd/
lane: verify
module_name: "TauLib.BookI.Coordinates.ABCD"
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

# TauLib.Coordinates.ABCD


ABCD coordinate chart, address DAG, and complexity metrics.

## Registry Cross-References


- [I.D17] ABCD Coordinate Chart — `abcd_chart`, `coord_A/B/C/D`

- [I.D24] Address DAG — `dag_indices`, `dag_size`

- [I.P08] Dimension (dim τ = 4) — `dim_tau_eq_four` (structural)

- [I.P09] Metric Inequality — `metric_inequality_check`


## Ground Truth Sources


- chunk_0241_M002280: ABCD coordinate chart Φ(X), address DAG structure


## Mathematical Content


The ABCD chart Φ(X) = (A, B, C, D) maps each X ≥ 2 to its greedy peel
decomposition. The four coordinates are:


- A = largest prime divisor (generator π-coordinate)

- B = maximal exponent quotient (generator γ-coordinate)

- C = maximal tetration height (generator η-coordinate)

- D = remainder after tower atom extraction (generator α-coordinate)


Recursing into all four coordinates produces a DAG (not a tree, since
distinct coordinates may coincide). Three complexity metrics satisfy
ℓ_spine(X) ≤ ℓ_DAG(X) ≤ ℓ_occ(X).

---

### `Tau.Coordinates.abcd_chart`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/ABCD.lean#L40-L41)
**def
Tau.Coordinates.abcd_chart
(x : Denotation.TauIdx)
 :Denotation.TauIdx × Denotation.TauIdx × Denotation.TauIdx × Denotation.TauIdx**


[I.D17] ABCD coordinate chart: Φ(X) = (A, B, C, D).
Equations
- Tau.Coordinates.abcd_chart x = Tau.Coordinates.greedy_peel x
Instances For

---

### `Tau.Coordinates.coord_A`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/ABCD.lean#L43-L44)
**def
Tau.Coordinates.coord_A
(x : Denotation.TauIdx)
 :Denotation.TauIdx**


A-coordinate (largest prime divisor).
Equations
- Tau.Coordinates.coord_A x = (Tau.Coordinates.abcd_chart x).fst
Instances For

---

### `Tau.Coordinates.coord_B`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/ABCD.lean#L46-L47)
**def
Tau.Coordinates.coord_B
(x : Denotation.TauIdx)
 :Denotation.TauIdx**


B-coordinate (exponent quotient).
Equations
- Tau.Coordinates.coord_B x = (Tau.Coordinates.abcd_chart x).snd.fst
Instances For

---

### `Tau.Coordinates.coord_C`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/ABCD.lean#L49-L50)
**def
Tau.Coordinates.coord_C
(x : Denotation.TauIdx)
 :Denotation.TauIdx**


C-coordinate (tetration height).
Equations
- Tau.Coordinates.coord_C x = (Tau.Coordinates.abcd_chart x).snd.snd.fst
Instances For

---

### `Tau.Coordinates.coord_D`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/ABCD.lean#L52-L53)
**def
Tau.Coordinates.coord_D
(x : Denotation.TauIdx)
 :Denotation.TauIdx**


D-coordinate (remainder).
Equations
- Tau.Coordinates.coord_D x = (Tau.Coordinates.abcd_chart x).snd.snd.snd
Instances For

---

### `Tau.Coordinates.chart_value`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/ABCD.lean#L55-L57)
**def
Tau.Coordinates.chart_value
(x : Denotation.TauIdx)
 :Denotation.TauIdx**


Reconstruction: T(A,B,C) * D.
Equations
- Tau.Coordinates.chart_value x = Tau.Coordinates.tower_atom (Tau.Coordinates.coord_A x) (Tau.Coordinates.coord_B x) (Tau.Coordinates.coord_C x) * Tau.Coordinates.coord_D x
Instances For

---

### `Tau.Coordinates.dag_indices_go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/ABCD.lean#L63-L78)@[irreducible]

**def
Tau.Coordinates.dag_indices_go
(worklist visited : List Denotation.TauIdx)

(fuel : Nat)
 :List Denotation.TauIdx**


[I.D24] Collect all distinct indices reachable by recursing into ABCD
coordinates. Uses a visited set for deduplication (DAG, not tree).
Equations
- One or more equations did not get rendered due to their size.
- Tau.Coordinates.dag_indices_go [] visited fuel = if fuel = 0 then visited else visited
Instances For

---

### `Tau.Coordinates.dag_indices`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/ABCD.lean#L80-L80)
**def
Tau.Coordinates.dag_indices
(x : Denotation.TauIdx)
 :List Denotation.TauIdx**

Equations
- Tau.Coordinates.dag_indices x = Tau.Coordinates.dag_indices_go [x] [] x
Instances For

---

### `Tau.Coordinates.dag_size`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/ABCD.lean#L82-L83)
**def
Tau.Coordinates.dag_size
(x : Denotation.TauIdx)
 :Nat**


DAG size: number of distinct indices reachable from x.
Equations
- Tau.Coordinates.dag_size x = (Tau.Coordinates.dag_indices x).length
Instances For

---

### `Tau.Coordinates.occ_size_go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/ABCD.lean#L89-L100)@[irreducible]

**def
Tau.Coordinates.occ_size_go
(x : Denotation.TauIdx)

(fuel : Nat)
 :Denotation.TauIdx**


Occurrence size: total node count in the ABCD tree (without deduplication).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Coordinates.occ_size`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/ABCD.lean#L102-L104)
**def
Tau.Coordinates.occ_size
(x : Denotation.TauIdx)
 :Denotation.TauIdx**

Equations
- Tau.Coordinates.occ_size x = if x ≤ 1 then 1 else Tau.Coordinates.occ_size_go x x
Instances For

---

### `Tau.Coordinates.metric_inequality_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/ABCD.lean#L110-L112)
**def
Tau.Coordinates.metric_inequality_check
(x : Denotation.TauIdx)
 :Bool**


[I.P09] Check: spine_length ≤ dag_size ≤ occ_size.
Equations
- Tau.Coordinates.metric_inequality_check x = (decide (Tau.Coordinates.spine_length x ≤ Tau.Coordinates.dag_size x) && decide (Tau.Coordinates.dag_size x ≤ Tau.Coordinates.occ_size x))
Instances For

---

### `Tau.Coordinates.dim_tau_witnesses`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/ABCD.lean#L118-L126)
**def
Tau.Coordinates.dim_tau_witnesses :List (Denotation.TauIdx × Denotation.TauIdx × Denotation.TauIdx × Denotation.TauIdx × Denotation.TauIdx)**


[I.P08] Four-dimensionality witness: exhibit X values where each
coordinate varies independently. Computable certificate.
Equations
- Tau.Coordinates.dim_tau_witnesses = [(12, 3, 1, 1, 4), (18, 3, 2, 1, 2), (16, 2, 1, 3, 1), (64, 2, 3, 2, 1)]
Instances For

---

### `Tau.Coordinates.dim_tau_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Coordinates/ABCD.lean#L128-L131)
**def
Tau.Coordinates.dim_tau_check :Bool**


Check that dim_tau_witnesses are consistent with the chart.
Equations
- One or more equations did not get rendered due to their size.
Instances For
