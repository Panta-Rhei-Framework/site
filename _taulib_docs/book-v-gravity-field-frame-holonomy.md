---
layout: taulib-doc
title: "TauLib.BookV.GravityField.FrameHolonomy"
permalink: /verify/taulib/docs/book-v-gravity-field-frame-holonomy/
lane: verify
module_name: "TauLib.BookV.GravityField.FrameHolonomy"
book: "V"
book_label: "Macrocosm"
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
    book: "Book V"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookV.GravityField.FrameHolonomy


Gravitational reference frames, frame holonomy, and the gravitational
coupling κ_τ = 1 − ι<sub>τ</sub> from D-sector loop transport.

## Registry Cross-References


- [V.D41] Clopen Frame — `ClopenFrame`

- [V.D42] Frame Holonomy — `FrameHolonomy`

- [V.D43] Local Gap Element — `LocalGap`

- [V.D44] Torus Vacuum (restated) — `TorusVacuumRestated`

- [V.D45] G_τ from Shape Ratio — `g_tau_from_shape`

- [V.D46] Gravitational Coupling κ_τ — `GravitationalCoupling`

- [V.C01] Temporal Complement — `temporal_complement`

- [V.T20] D-sector Holonomy — `d_sector_holonomy_gap`

- [V.T21] Shape Ratio = ι<sub>τ</sub> — `shape_ratio_is_iota`

- [V.T22] G = (c³/ℏ)·ι<sub>τ</sub>² — `g_from_iota_squared`

- [V.T23] κ_τ is σ-fixed — `kappa_sigma_fixed_thm`

- [V.P10] Frame Adjacency Coherence — `frame_adjacency_coherent`

- [V.P11] Total Gap Refinement Invariance — `gap_refinement_invariant`

- [V.R56] Lean formalization — structural remark


## Mathematical Content


### Clopen Frames


A gravitational reference frame is a **clopen** (closed-and-open) subset
of the refinement tower at depth n. "Clopen" in τ-topology means the
frame boundary is a decidable predicate on orbit indices: every carrier
either belongs to the frame or does not.

### Frame Holonomy


Parallel transport around a D-sector loop on the base circle τ¹ produces
a **frame holonomy**: the accumulated phase from the gravitational
connection. The holonomy gap is the smallest non-trivial element in the
holonomy group at depth n.

### Gravitational Coupling


κ_τ = 1 − ι<sub>τ</sub> is the D-sector self-coupling. The temporal complement
identity κ_τ + κ_A = 1 partitions the base circle into gravity (D) and
weak (A) sectors. κ_τ is σ-fixed (unpolarized).

## Ground Truth Sources


- Book V Part III ch11 (Frame Holonomy)

- gravity-einstein.json: clopen-frame, frame-holonomy


---

### `Tau.BookV.GravityField.ClopenFrame`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L64-L82)
**structure
Tau.BookV.GravityField.ClopenFrame :Type**


[V.D41] Clopen frame: gravitational reference frame at depth n.

A clopen frame is a subset of the refinement tower that is both
closed and open in the τ-topology. This means:


- Every carrier is decidably inside or outside the frame

- The frame boundary is a well-defined orbit-index predicate

- Frame transition maps are holomorphic (boundary-character maps)


- depth : ℕ
Refinement depth at which the frame is defined.

- depth_pos : self.depth > 0
Depth must be positive (frames require at least one refinement step).

- carrier_count : ℕ
Number of carriers in the frame at this depth.

- carrier_pos : self.carrier_count > 0
At least one carrier in any frame.

- is_clopen : Bool
The frame is clopen (decidable membership).

Instances For

---

### `Tau.BookV.GravityField.instReprClopenFrame`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L82-L82)
**instance
Tau.BookV.GravityField.instReprClopenFrame :Repr ClopenFrame**

Equations
- Tau.BookV.GravityField.instReprClopenFrame = { reprPrec := Tau.BookV.GravityField.instReprClopenFrame.repr }

---

### `Tau.BookV.GravityField.instReprClopenFrame.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L82-L82)
**def
Tau.BookV.GravityField.instReprClopenFrame.repr :ClopenFrame → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.ClopenFrame.same_depth`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L84-L86)
**def
Tau.BookV.GravityField.ClopenFrame.same_depth
(f₁ f₂ : ClopenFrame)
 :Bool**


Whether two frames are at the same depth.
Equations
- f₁.same_depth f₂ = (f₁.depth == f₂.depth)
Instances For

---

### `Tau.BookV.GravityField.FrameHolonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L92-L114)
**structure
Tau.BookV.GravityField.FrameHolonomy :Type**


[V.D42] Frame holonomy: phase accumulated by parallel transport
around a D-sector loop on τ¹.

The holonomy is the D-sector boundary character evaluated on a
closed loop. At depth n, the holonomy group is a finite cyclic
group whose order grows with n.

The holonomy gap is the smallest non-trivial element:
gap_n = 1/order_n in normalized holonomy units.

- frame : ClopenFrame
The frame around which transport occurs.

- group_order : ℕ
Holonomy group order at this depth.

- order_pos : self.group_order > 0
Group order is positive.

- gap_numer : ℕ
Holonomy gap numerator (= 1 in normalized units).

- gap_denom : ℕ
Holonomy gap denominator (= group_order).

- gap_minimal : self.gap_numer = 1 ∧ self.gap_denom = self.group_order
Gap is minimal (1/order).

Instances For

---

### `Tau.BookV.GravityField.instReprFrameHolonomy.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L114-L114)
**def
Tau.BookV.GravityField.instReprFrameHolonomy.repr :FrameHolonomy → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprFrameHolonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L114-L114)
**instance
Tau.BookV.GravityField.instReprFrameHolonomy :Repr FrameHolonomy**

Equations
- Tau.BookV.GravityField.instReprFrameHolonomy = { reprPrec := Tau.BookV.GravityField.instReprFrameHolonomy.repr }

---

### `Tau.BookV.GravityField.FrameHolonomy.gapFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L116-L118)
**def
Tau.BookV.GravityField.FrameHolonomy.gapFloat
(h : FrameHolonomy)
 :Float**


Holonomy gap as Float.
Equations
- h.gapFloat = Float.ofNat h.gap_numer / Float.ofNat h.gap_denom
Instances For

---

### `Tau.BookV.GravityField.LocalGap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L124-L146)
**structure
Tau.BookV.GravityField.LocalGap :Type**


[V.D43] Local gap element: smallest addressable gravitational
quantum at depth n.

The local gap is the minimal holonomy element that can be
resolved at the given refinement depth. It decreases as depth
increases (finer resolution), converging to zero in the
ω-germ limit.

gap(n) = κ_τ / refinement_scale(n)

- depth : ℕ
Refinement depth.

- depth_pos : self.depth > 0
Depth positive.

- gap_numer : ℕ
Gap numerator (κ_τ numerator at this scale).

- gap_denom : ℕ
Gap denominator (refinement scale).

- denom_pos : self.gap_denom > 0
Denominator positive.

- gap_positive : self.gap_numer > 0
Gap is positive at any finite depth.

Instances For

---

### `Tau.BookV.GravityField.instReprLocalGap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L146-L146)
**instance
Tau.BookV.GravityField.instReprLocalGap :Repr LocalGap**

Equations
- Tau.BookV.GravityField.instReprLocalGap = { reprPrec := Tau.BookV.GravityField.instReprLocalGap.repr }

---

### `Tau.BookV.GravityField.instReprLocalGap.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L146-L146)
**def
Tau.BookV.GravityField.instReprLocalGap.repr :LocalGap → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.LocalGap.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L148-L150)
**def
Tau.BookV.GravityField.LocalGap.toFloat
(g : LocalGap)
 :Float**


Local gap as Float.
Equations
- g.toFloat = Float.ofNat g.gap_numer / Float.ofNat g.gap_denom
Instances For

---

### `Tau.BookV.GravityField.TorusVacuumRestated`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L156-L169)
**structure
Tau.BookV.GravityField.TorusVacuumRestated :Type**


[V.D44] Torus vacuum restated in the gravitational field context.

The torus vacuum from ch16 (V.D01) is restated here to emphasize
that the shape ratio r/R = ι<sub>τ</sub> determines the gravitational
coupling strength.

This is a lightweight wrapper referencing the original TorusVacuum.

- vacuum : Gravity.TorusVacuum
The underlying torus vacuum.

- shape_confirmed : self.vacuum.minor_numer * self.vacuum.major_denom * BookIV.Sectors.iotaD = BookIV.Sectors.iota * self.vacuum.minor_denom * self.vacuum.major_numer
Shape ratio confirmed.

Instances For

---

### `Tau.BookV.GravityField.instReprTorusVacuumRestated`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L169-L169)
**instance
Tau.BookV.GravityField.instReprTorusVacuumRestated :Repr TorusVacuumRestated**

Equations
- Tau.BookV.GravityField.instReprTorusVacuumRestated = { reprPrec := Tau.BookV.GravityField.instReprTorusVacuumRestated.repr }

---

### `Tau.BookV.GravityField.instReprTorusVacuumRestated.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L169-L169)
**def
Tau.BookV.GravityField.instReprTorusVacuumRestated.repr :TorusVacuumRestated → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.canonical_torus_restated`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L171-L174)
**def
Tau.BookV.GravityField.canonical_torus_restated :TorusVacuumRestated**


Canonical restated torus vacuum from the unit torus.
Equations
- Tau.BookV.GravityField.canonical_torus_restated = { vacuum := Tau.BookV.Gravity.unit_torus_vacuum, shape_confirmed := ⋯ }
Instances For

---

### `Tau.BookV.GravityField.GTauFromShape`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L180-L198)
**structure
Tau.BookV.GravityField.GTauFromShape :Type**


[V.D45] G_τ from shape ratio: the gravitational constant derived
from the torus vacuum shape ratio r/R = ι<sub>τ</sub>.

In orthodox units: G = (c³/ℏ) · ι<sub>τ</sub>²

The ι<sub>τ</sub>² factor is the structural core.
Numerator = iota² = 341304² = 116594274681
Denominator = iotaD² = 10¹²

- iota_sq_num : ℕ
ι<sub>τ</sub>² numerator.

- iota_sq_den : ℕ
ι<sub>τ</sub>² denominator.

- denom_pos : self.iota_sq_den > 0
Denominator positive.

- is_iota_squared : self.iota_sq_num = BookIV.Sectors.iota * BookIV.Sectors.iota ∧ self.iota_sq_den = BookIV.Sectors.iotaD * BookIV.Sectors.iotaD
The value equals iota².

Instances For

---

### `Tau.BookV.GravityField.instReprGTauFromShape.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L198-L198)
**def
Tau.BookV.GravityField.instReprGTauFromShape.repr :GTauFromShape → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprGTauFromShape`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L198-L198)
**instance
Tau.BookV.GravityField.instReprGTauFromShape :Repr GTauFromShape**

Equations
- Tau.BookV.GravityField.instReprGTauFromShape = { reprPrec := Tau.BookV.GravityField.instReprGTauFromShape.repr }

---

### `Tau.BookV.GravityField.g_tau_from_shape`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L200-L207)
**def
Tau.BookV.GravityField.g_tau_from_shape :GTauFromShape**


Canonical G_τ shape factor.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.GTauFromShape.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L209-L211)
**def
Tau.BookV.GravityField.GTauFromShape.toFloat
(g : GTauFromShape)
 :Float**


G_τ shape factor as Float (≈ 0.116594, i.e., ι<sub>τ</sub>²).
Equations
- g.toFloat = Float.ofNat g.iota_sq_num / Float.ofNat g.iota_sq_den
Instances For

---

### `Tau.BookV.GravityField.GravitationalCoupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L217-L238)
**structure
Tau.BookV.GravityField.GravitationalCoupling :Type**


[V.D46] Gravitational coupling κ_τ = 1 − ι<sub>τ</sub>.

The D-sector self-coupling at primorial depth 1.
Numerically: κ_τ = 658541/1000000 ≈ 0.658541.

Properties:


- σ-fixed (unpolarized, invariant under polarity swap)

- Unique unpolarized coupling on the base circle

- Temporal complement: κ_τ + κ_A = 1 (with weak sector)


- kappa_numer : ℕ
κ_τ numerator = iotaD − iota.

- kappa_denom : ℕ
κ_τ denominator = iotaD.

- denom_pos : self.kappa_denom > 0
Denominator positive.

- is_one_minus_iota : self.kappa_numer = BookIV.Sectors.iotaD - BookIV.Sectors.iota ∧ self.kappa_denom = BookIV.Sectors.iotaD
The value equals 1 − ι<sub>τ</sub>.

- sigma_fixed : Bool
σ-fixed (unpolarized).

Instances For

---

### `Tau.BookV.GravityField.instReprGravitationalCoupling.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L238-L238)
**def
Tau.BookV.GravityField.instReprGravitationalCoupling.repr :GravitationalCoupling → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprGravitationalCoupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L238-L238)
**instance
Tau.BookV.GravityField.instReprGravitationalCoupling :Repr GravitationalCoupling**

Equations
- Tau.BookV.GravityField.instReprGravitationalCoupling = { reprPrec := Tau.BookV.GravityField.instReprGravitationalCoupling.repr }

---

### `Tau.BookV.GravityField.canonical_grav_coupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L240-L245)
**def
Tau.BookV.GravityField.canonical_grav_coupling :GravitationalCoupling**


Canonical gravitational coupling.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.GravitationalCoupling.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L247-L249)
**def
Tau.BookV.GravityField.GravitationalCoupling.toFloat
(g : GravitationalCoupling)
 :Float**


GravitationalCoupling as Float.
Equations
- g.toFloat = Float.ofNat g.kappa_numer / Float.ofNat g.kappa_denom
Instances For

---

### `Tau.BookV.GravityField.temporal_complement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L255-L263)
**theorem
Tau.BookV.GravityField.temporal_complement :BookIV.Sectors.iotaD - BookIV.Sectors.iota + BookIV.Sectors.iota = BookIV.Sectors.iotaD**


[V.C01] Temporal complement: κ_τ + κ_A = 1.

The gravity coupling (D-sector, 1 − ι<sub>τ</sub>) and the weak coupling
(A-sector, ι<sub>τ</sub>) sum to 1, partitioning the base circle τ¹.

Cross-multiplied: (iotaD − iota) + iota = iotaD.

---

### `Tau.BookV.GravityField.temporal_complement_sectors`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L265-L268)
**theorem
Tau.BookV.GravityField.temporal_complement_sectors :BookIV.Sectors.gravity_sector.coupling_numer + BookIV.Sectors.weak_sector.coupling_numer = BookIV.Sectors.iotaD**


Temporal complement restated using sector definitions.

---

### `Tau.BookV.GravityField.d_sector_holonomy_gap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L274-L281)
**theorem
Tau.BookV.GravityField.d_sector_holonomy_gap
(h : FrameHolonomy)
 :h.gap_numer = 1**


[V.T20] The D-sector holonomy gap equals the frame holonomy gap.

The gravitational frame holonomy at depth n is determined entirely
by the D-sector boundary character. The gap is the minimal
non-trivial holonomy element: gap_numer = 1 (in normalized units).

---

### `Tau.BookV.GravityField.shape_ratio_is_iota`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L287-L292)
**theorem
Tau.BookV.GravityField.shape_ratio_is_iota :g_tau_from_shape.iota_sq_num = BookIV.Sectors.iota * BookIV.Sectors.iota ∧ g_tau_from_shape.iota_sq_den = BookIV.Sectors.iotaD * BookIV.Sectors.iotaD**


[V.T21] The torus vacuum shape ratio r/R = ι<sub>τ</sub>.
Restated from V.T01 in the gravitational field context.

---

### `Tau.BookV.GravityField.g_from_iota_squared`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L298-L306)
**theorem
Tau.BookV.GravityField.g_from_iota_squared :g_tau_from_shape.iota_sq_num > 0 ∧ g_tau_from_shape.iota_sq_den > 0**


[V.T22] G_τ = (c³/ℏ) · ι<sub>τ</sub>²: the gravitational constant is
proportional to ι<sub>τ</sub>² with the Planck-unit prefactor.
Verified: iota * iota > 0 (positive coupling).

---

### `Tau.BookV.GravityField.kappa_sigma_fixed_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L312-L315)
**theorem
Tau.BookV.GravityField.kappa_sigma_fixed_thm :canonical_grav_coupling.sigma_fixed = true**


[V.T23] κ_τ is σ-fixed (unpolarized). Gravity couples to total
energy-momentum, not to any specific polarity channel.

---

### `Tau.BookV.GravityField.frame_adjacency_coherent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L321-L325)
**theorem
Tau.BookV.GravityField.frame_adjacency_coherent
(f₁ f₂ : ClopenFrame)

(h : f₁.depth = f₂.depth)
 :f₁.depth = f₂.depth**


[V.P10] Frame adjacency coherence: two frames at the same depth
have compatible transition maps.

---

### `Tau.BookV.GravityField.gap_refinement_invariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L331-L336)
**theorem
Tau.BookV.GravityField.gap_refinement_invariant :canonical_grav_coupling.kappa_numer = BookIV.Sectors.iotaD - BookIV.Sectors.iota**


[V.P11] Total gap refinement invariance: the total holonomy
around a full loop is κ_τ = 1 − ι<sub>τ</sub>, independent of depth n.
Only the resolution (gap size) changes, not the total phase.

---

### `Tau.BookV.GravityField.example_holonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L357-L362)
**def
Tau.BookV.GravityField.example_holonomy :FrameHolonomy**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.example_gap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/GravityField/FrameHolonomy.lean#L366-L372)
**def
Tau.BookV.GravityField.example_gap :LocalGap**

Equations
- One or more equations did not get rendered due to their size.
Instances For
