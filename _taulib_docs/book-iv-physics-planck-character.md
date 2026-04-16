---
layout: taulib-doc
title: "TauLib.BookIV.Physics.PlanckCharacter"
permalink: /verify/taulib/docs/book-iv-physics-planck-character/
lane: verify
module_name: "TauLib.BookIV.Physics.PlanckCharacter"
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

# TauLib.BookIV.Physics.PlanckCharacter


The Planck character ℏ_τ as sector lift of ι<sub>τ</sub> into the quantum regime,
plus uncertainty product templates and the sector lift functor framework.

## Registry Cross-References


- [IV.D13] Planck Character — `PlanckCharacter`

- [IV.D14] Uncertainty Product — `UncertaintyProduct`

- [IV.D15] Sector Lift — `SectorLift`

- [IV.R03] ℏ_τ as crossing mediator — structural remark

- [IV.T03] σ-fixed characterization — `planck_sigma_fixed`


## Mathematical Content


### Planck Character ℏ_τ


The Planck character is the **universal lower bound** in the boundary
holonomy algebra H_∂[ω]:

```
ℏ_τ := Δx_ω(x*) · Δp_ω(x*)
```


where x* is the canonical saturating chain (stagewise NF-minimizer).

Key properties:


- ℏ_τ is **σ-fixed** (lives at lemniscate crossing point)

- ℏ_τ is the **attained minimum** (not merely infimum) via saturation theorem

- ℏ_τ = Lift_QM(ι<sub>τ</sub>) — the QM sector lift of the master constant

- All physical constants form: C_phys = Q(ι<sub>τ</sub>) (closure under field ops + lifts)


### Sector Lift Functors


Each sector S has a unique lift functor Lift_S : H_fix[ω] → H_fix[ω] that is:


- A ring homomorphism (preserves 0, 1, +, ×)

- σ-equivariant (preserves lobe swap)

- Uniquely determined by the sector's saturation chain


The physical constants are the images: Lift_S(ι<sub>τ</sub>) = c_S

### Uncertainty Relations


The τ-Heisenberg inequalities are:


- Δx_n(x) · Δp_n(x) ≥ ℏ_τ (position-momentum)

- Δt_n · ΔE_n ≥ ℏ_τ (time-energy)


These arise from **incompatible address constraints**, NOT measurement disturbance.

## Ground Truth Sources


- quantum-mechanics.json: planck-character, tau-heisenberg, sector-lift-functors

- particle-physics-defects.json: iota-tau-constructive-generation


---

### `Tau.BookIV.Physics.PlanckCharacter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L65-L81)
**structure
Tau.BookIV.Physics.PlanckCharacter :Type**


[IV.D13] The Planck character ℏ_τ: universal lower bound in the
boundary holonomy algebra H_∂[ω].

ℏ_τ = Δx_ω(x*) · Δp_ω(x*) where x* is the canonical saturating chain.
It is the QM sector lift of the master constant ι<sub>τ</sub>.

- numer : ℕ
ℏ_τ numerator (scaled rational representation).

- denom : ℕ
ℏ_τ denominator (scaled rational representation).

- denom_pos : self.denom > 0
Denominator is positive.

- sigma_fixed : Bool
ℏ_τ is σ-fixed (unpolarized, lives at lemniscate crossing point).

- is_minimum : Bool
ℏ_τ is the attained minimum (not merely infimum) via saturation.

Instances For

---

### `Tau.BookIV.Physics.instReprPlanckCharacter.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L81-L81)
**def
Tau.BookIV.Physics.instReprPlanckCharacter.repr :PlanckCharacter → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instReprPlanckCharacter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L81-L81)
**instance
Tau.BookIV.Physics.instReprPlanckCharacter :Repr PlanckCharacter**

Equations
- Tau.BookIV.Physics.instReprPlanckCharacter = { reprPrec := Tau.BookIV.Physics.instReprPlanckCharacter.repr }

---

### `Tau.BookIV.Physics.PlanckCharacter.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L83-L85)
**def
Tau.BookIV.Physics.PlanckCharacter.toFloat
(h : PlanckCharacter)
 :Float**


Float display for Planck character.
Equations
- h.toFloat = Float.ofNat h.numer / Float.ofNat h.denom
Instances For

---

### `Tau.BookIV.Physics.SectorLift`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L91-L114)
**structure
Tau.BookIV.Physics.SectorLift :Type**


[IV.D15] Sector lift functor: Lift_S : H_fix[ω] → H_fix[ω].

Each sector S has a unique unpolarized field endomorphism that
maps ι<sub>τ</sub> to the sector-specific physical constant:
Lift_S(ι<sub>τ</sub>) = c_S

Key properties:


- Ring homomorphism (preserves 0, 1, +, ×)

- σ-equivariant (preserves lobe swap)

- Uniquely determined by sector saturation chain


- source_sector : BookIII.Sectors.Sector
Source sector for this lift.

- target_numer : ℕ
Lift_S(ι<sub>τ</sub>) numerator — the sector-specific constant.

- target_denom : ℕ
Lift_S(ι<sub>τ</sub>) denominator.

- denom_pos : self.target_denom > 0
Denominator is positive.

- preserves_sigma : Bool
All physical sector lifts are σ-equivariant.

- is_ring_hom : Bool
Sector lifts are ring homomorphisms.

Instances For

---

### `Tau.BookIV.Physics.instReprSectorLift`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L114-L114)
**instance
Tau.BookIV.Physics.instReprSectorLift :Repr SectorLift**

Equations
- Tau.BookIV.Physics.instReprSectorLift = { reprPrec := Tau.BookIV.Physics.instReprSectorLift.repr }

---

### `Tau.BookIV.Physics.instReprSectorLift.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L114-L114)
**def
Tau.BookIV.Physics.instReprSectorLift.repr :SectorLift → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.SectorLift.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L116-L118)
**def
Tau.BookIV.Physics.SectorLift.toFloat
(s : SectorLift)
 :Float**


Float display for sector lift.
Equations
- s.toFloat = Float.ofNat s.target_numer / Float.ofNat s.target_denom
Instances For

---

### `Tau.BookIV.Physics.lift_em`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L131-L136)
**def
Tau.BookIV.Physics.lift_em :SectorLift**


EM sector lift: Lift_B(ι<sub>τ</sub>) = ι<sub>τ</sub>² (EM self-coupling).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.lift_weak`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L138-L143)
**def
Tau.BookIV.Physics.lift_weak :SectorLift**


Weak sector lift: Lift_A(ι<sub>τ</sub>) = ι<sub>τ</sub> (weak self-coupling = master constant).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.lift_strong`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L145-L150)
**def
Tau.BookIV.Physics.lift_strong :SectorLift**


Strong sector lift: Lift_C(ι<sub>τ</sub>) = ι<sub>τ</sub>³/(1−ι<sub>τ</sub>) (confinement coupling).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.lift_gravity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L152-L157)
**def
Tau.BookIV.Physics.lift_gravity :SectorLift**


Gravity sector lift: Lift_D(ι<sub>τ</sub>) = 1−ι<sub>τ</sub> (gravity self-coupling).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.lift_higgs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L159-L164)
**def
Tau.BookIV.Physics.lift_higgs :SectorLift**


Higgs/crossing sector lift: Lift_ω(ι<sub>τ</sub>) = ι<sub>τ</sub>³/(1+ι<sub>τ</sub>) (mass coupling).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.all_sector_lifts`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L166-L168)
**def
Tau.BookIV.Physics.all_sector_lifts :List SectorLift**


All 5 canonical sector lifts.
Equations
- Tau.BookIV.Physics.all_sector_lifts = [Tau.BookIV.Physics.lift_em, Tau.BookIV.Physics.lift_weak, Tau.BookIV.Physics.lift_strong, Tau.BookIV.Physics.lift_gravity, Tau.BookIV.Physics.lift_higgs]
Instances For

---

### `Tau.BookIV.Physics.UncertaintyProduct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L174-L194)
**structure
Tau.BookIV.Physics.UncertaintyProduct :Type**


[IV.D14] Uncertainty product template: the product Δx · Δp
(or Δt · ΔE) that must satisfy the τ-Heisenberg inequality.

The uncertainty arises from **incompatible address constraints**
in τ-NF, NOT from measurement disturbance.

Δx_n(x) = tau-position = rad(U_n(β_n(x)))
Δp_n(x) = tau-momentum = min{t | Π^ph_n(x;t) exists}

- delta_x_numer : ℕ
Position/time resolution numerator.

- delta_x_denom : ℕ
Position/time resolution denominator.

- delta_p_numer : ℕ
Momentum/energy resolution numerator.

- delta_p_denom : ℕ
Momentum/energy resolution denominator.

- denom_pos_x : self.delta_x_denom > 0
Both denominators positive.

- denom_pos_p : self.delta_p_denom > 0
Instances For

---

### `Tau.BookIV.Physics.instReprUncertaintyProduct.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L194-L194)
**def
Tau.BookIV.Physics.instReprUncertaintyProduct.repr :UncertaintyProduct → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instReprUncertaintyProduct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L194-L194)
**instance
Tau.BookIV.Physics.instReprUncertaintyProduct :Repr UncertaintyProduct**

Equations
- Tau.BookIV.Physics.instReprUncertaintyProduct = { reprPrec := Tau.BookIV.Physics.instReprUncertaintyProduct.repr }

---

### `Tau.BookIV.Physics.UncertaintyProduct.product_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L196-L198)
**def
Tau.BookIV.Physics.UncertaintyProduct.product_numer
(u : UncertaintyProduct)
 :ℕ**


The product Δx · Δp as a scaled rational.
Equations
- u.product_numer = u.delta_x_numer * u.delta_p_numer
Instances For

---

### `Tau.BookIV.Physics.UncertaintyProduct.product_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L200-L202)
**def
Tau.BookIV.Physics.UncertaintyProduct.product_denom
(u : UncertaintyProduct)
 :ℕ**


The product Δx · Δp denominator.
Equations
- u.product_denom = u.delta_x_denom * u.delta_p_denom
Instances For

---

### `Tau.BookIV.Physics.PhysicalConstantsCore`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L208-L228)
**structure
Tau.BookIV.Physics.PhysicalConstantsCore :Type**


[IV.R03] The physical constants core C_phys = Q(ι<sub>τ</sub>):
the closure of ι<sub>τ</sub> under field operations and all sector lift functors.

Every physical constant is an ι<sub>τ</sub>-image:


- ℏ_τ = Lift_QM(ι<sub>τ</sub>)

- κ_τ = Lift_GR(ι<sub>τ</sub>)

- α_EM = (8/15) · ι<sub>τ</sub>⁴

- All sector vacua Ω*_S = F_S(ι<sub>τ</sub>)

- All excitation quanta q_S[ω] = G_S(ι<sub>τ</sub>)


C_phys is **countably generated** by a single element (ι<sub>τ</sub>).

- master_numer : ℕ
The master constant ι<sub>τ</sub> = 2/(π+e) numerator.

- master_denom : ℕ
The master constant denominator.

- num_lifts : ℕ
Number of sector lifts (= 5).

- all_sigma_fixed : Bool
All constants are σ-fixed (unpolarized).

Instances For

---

### `Tau.BookIV.Physics.instReprPhysicalConstantsCore.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L228-L228)
**def
Tau.BookIV.Physics.instReprPhysicalConstantsCore.repr :PhysicalConstantsCore → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instReprPhysicalConstantsCore`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L228-L228)
**instance
Tau.BookIV.Physics.instReprPhysicalConstantsCore :Repr PhysicalConstantsCore**

Equations
- Tau.BookIV.Physics.instReprPhysicalConstantsCore = { reprPrec := Tau.BookIV.Physics.instReprPhysicalConstantsCore.repr }

---

### `Tau.BookIV.Physics.physical_constants_core`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L230-L231)
**def
Tau.BookIV.Physics.physical_constants_core :PhysicalConstantsCore**


The canonical physical constants core.
Equations
- Tau.BookIV.Physics.physical_constants_core = { }
Instances For

---

### `Tau.BookIV.Physics.planck_sigma_fixed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L237-L239)
**theorem
Tau.BookIV.Physics.planck_sigma_fixed
(h : PlanckCharacter)

(hσ : h.sigma_fixed = true)
 :h.sigma_fixed = true**


[IV.T03] ℏ_τ is σ-fixed by definition (structural property).

---

### `Tau.BookIV.Physics.all_lifts_sigma_equivariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L241-L244)
**theorem
Tau.BookIV.Physics.all_lifts_sigma_equivariant :((List.map SectorLift.preserves_sigma all_sector_lifts).all fun (x : Bool) => x == true) = true**


All 5 sector lifts preserve σ-equivariance.

---

### `Tau.BookIV.Physics.five_sector_lifts`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L246-L247)
**theorem
Tau.BookIV.Physics.five_sector_lifts :all_sector_lifts.length = 5**


Exactly 5 sector lifts (one per sector).

---

### `Tau.BookIV.Physics.all_lifts_ring_hom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L249-L252)
**theorem
Tau.BookIV.Physics.all_lifts_ring_hom :((List.map SectorLift.is_ring_hom all_sector_lifts).all fun (x : Bool) => x == true) = true**


All sector lifts are ring homomorphisms.

---

### `Tau.BookIV.Physics.uncertainty_product_denom_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L254-L257)
**theorem
Tau.BookIV.Physics.uncertainty_product_denom_pos
(u : UncertaintyProduct)
 :u.product_denom > 0**


The uncertainty product has positive denominator.

---

### `Tau.BookIV.Physics.weak_lift_is_master`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L259-L262)
**theorem
Tau.BookIV.Physics.weak_lift_is_master :lift_weak.target_numer = Sectors.iota ∧ lift_weak.target_denom = Sectors.iotaD**


The weak sector lift IS the master constant (ι<sub>τ</sub> itself).

---

### `Tau.BookIV.Physics.em_lift_is_iota_squared`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/PlanckCharacter.lean#L264-L268)
**theorem
Tau.BookIV.Physics.em_lift_is_iota_squared :lift_em.target_numer = Sectors.iota_sq_numer ∧ lift_em.target_denom = Sectors.iota_sq_denom**


The EM sector lift is ι<sub>τ</sub>² (weak squared).
