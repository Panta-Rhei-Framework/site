---
layout: taulib-doc
title: "TauLib.BookI.Polarity.Lemniscate"
permalink: /verify/taulib/docs/book-i-polarity-lemniscate/
lane: verify
module_name: "TauLib.BookI.Polarity.Lemniscate"
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

# TauLib.Polarity.Lemniscate


The algebraic lemniscate: the pre-geometric boundary of Category τ.

## Registry Cross-References


- [I.D18] Algebraic Lemniscate — `AlgebraicLemniscate`, `algebraic_lemniscate_exists`


## Ground Truth Sources


- chunk_0123_M001424: Algebraic lemniscate as boundary of τ³, wedge structure

- chunk_0228_M002194: Split-complex extension giving H_τ = ℤ̂_τ[j]


## Mathematical Content


The algebraic lemniscate L is the triple (H_τ, ω_L, σ) where:


- H_τ is the bipolar spectral algebra (split-complex over the boundary ring)

- ω_L is the crossing-point germ (where neither polarity channel freezes)

- σ is the polarity involution (j ↦ -j, swaps B/C sectors)


This is the algebraic, pre-topological definition of the lemniscate boundary.
In Book II, when topology is earned via Global Hartogs, this becomes the
geometric lemniscate S¹ ∨ S¹.

Key properties:


- σ² = id (involution)

- σ swaps e+ ↔ e- (sector exchange)

- σ fixes the crossing point ω_L

- The two sectors e+·H_τ and e-·H_τ are the two lobes


---

### `Tau.Polarity.AlgebraicLemniscate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/Lemniscate.lean#L42-L58)
**structure
Tau.Polarity.AlgebraicLemniscate :Type**


[I.D18] The algebraic lemniscate: a triple (algebra, crossing point, involution).
This is the pre-geometric boundary structure of Category τ.

- j_unit : SplitComplex
The bipolar spectral algebra H_τ, represented by its unit j.

- j_sq : self.j_unit.mul self.j_unit = SplitComplex.one
j² = 1 (split-complex identity).

- crossing_point : SectorPair
The crossing-point germ ω_L (sector-balanced: both components equal).

- crossing_balanced : self.crossing_point.b_sector = self.crossing_point.c_sector
The crossing point has equal sector components (balance).

- involution : SplitComplex → SplitComplex
The polarity involution σ.

- involution_sq
(z : SplitComplex)
 : self.involution (self.involution z) = z
σ² = id.

- involution_j : self.involution self.j_unit = self.j_unit.neg
σ(j) = -j.

Instances For

---

### `Tau.Polarity.canonical_lemniscate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/Lemniscate.lean#L64-L72)
**def
Tau.Polarity.canonical_lemniscate :AlgebraicLemniscate**


The canonical algebraic lemniscate constructed from the split-complex algebra.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Polarity.algebraic_lemniscate_exists`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/Lemniscate.lean#L74-L76)
**theorem
Tau.Polarity.algebraic_lemniscate_exists :Nonempty AlgebraicLemniscate**


[I.D18] The algebraic lemniscate exists.

---

### `Tau.Polarity.canonical_swaps_sectors`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/Lemniscate.lean#L82-L86)
**theorem
Tau.Polarity.canonical_swaps_sectors
(z : SplitComplex)
 :to_sectors (canonical_lemniscate.involution z) = { b_sector := (to_sectors z).c_sector, c_sector := (to_sectors z).b_sector }**


The canonical involution swaps sectors.

---

### `Tau.Polarity.b_lobe`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/Lemniscate.lean#L88-L89)
**def
Tau.Polarity.b_lobe :SectorPair**


The two sectors (lobes) of the lemniscate.
Equations
- Tau.Polarity.b_lobe = Tau.Polarity.e_plus_sector
Instances For

---

### `Tau.Polarity.c_lobe`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/Lemniscate.lean#L90-L90)
**def
Tau.Polarity.c_lobe :SectorPair**

Equations
- Tau.Polarity.c_lobe = Tau.Polarity.e_minus_sector
Instances For

---

### `Tau.Polarity.involution_swaps_lobes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/Lemniscate.lean#L92-L96)
**theorem
Tau.Polarity.involution_swaps_lobes :to_sectors (polarity_inv { re := 1, im := 1 }) = { b_sector := (to_sectors { re := 1, im := 1 }).c_sector, c_sector := (to_sectors { re := 1, im := 1 }).b_sector }**


The involution swaps the lobes.

---

### `Tau.Polarity.sector_ring_iso`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/Lemniscate.lean#L102-L105)
**theorem
Tau.Polarity.sector_ring_iso
(a b : SplitComplex)
 :to_sectors (a.mul b) = (to_sectors a).mul (to_sectors b)**


The sector decomposition is a ring isomorphism (proved via sectors_mul).

---

### `Tau.Polarity.sector_unique`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/Lemniscate.lean#L107-L113)
**theorem
Tau.Polarity.sector_unique
(z : SplitComplex)
 :z = { re := ((to_sectors z).b_sector + (to_sectors z).c_sector) / 2,
 im := ((to_sectors z).b_sector - (to_sectors z).c_sector) / 2 }**


Every split-complex element has a unique sector decomposition.

---

### `Tau.Polarity.split_complex_zero_divisor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/Lemniscate.lean#L119-L122)
**theorem
Tau.Polarity.split_complex_zero_divisor :{ re := 1, im := 1 }.mul { re := 1, im := -1 } = SplitComplex.zero**


The split-complex algebra has zero divisors: (1+j)(1-j) = 0.

---

### `Tau.Polarity.zero_divisor_via_sectors`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Polarity/Lemniscate.lean#L124-L127)
**theorem
Tau.Polarity.zero_divisor_via_sectors :to_sectors { re := 1, im := 1 } = { b_sector := 2, c_sector := 0 } ∧ to_sectors { re := 1, im := -1 } = { b_sector := 0, c_sector := 2 }**


The zero divisors correspond to the sector idempotents.
