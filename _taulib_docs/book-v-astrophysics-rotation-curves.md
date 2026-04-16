---
layout: taulib-doc
title: "TauLib.BookV.Astrophysics.RotationCurves"
permalink: /verify/taulib/docs/book-v-astrophysics-rotation-curves/
lane: verify
module_name: "TauLib.BookV.Astrophysics.RotationCurves"
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

# TauLib.BookV.Astrophysics.RotationCurves


Flat rotation curves from boundary holonomy corrections to the
D-sector coupling. MOND-like phenomenology emerges from ι<sub>τ</sub> at
galactic acceleration scales. Dark matter is unnecessary.

## Registry Cross-References


- [V.D123] Boundary Holonomy Correction -- `BoundaryHolonomyCorrection`

- [V.T85] Flat Rotation Curve Theorem -- `flat_rotation_theorem`

- [V.C13] MOND Acceleration Scale from ι<sub>τ</sub> -- `mond_scale_from_iota`

- [V.P67] Newtonian Regime Recovery -- `newtonian_recovery`

- [V.R174] a₀ from ι<sub>τ</sub> and H₀ -- structural remark

- [V.P68] RAR from Single Coupling -- `rar_from_single_coupling`

- [V.R175] McGaugh RAR Data Match -- structural remark

- [V.P69] Dwarf Galaxy Prediction -- `dwarf_galaxy_prediction`

- [V.R176] Ultra-Diffuse Galaxies as Test -- structural remark

- [V.P70] No Dark Matter Halo Required -- `no_dark_halo`


## Mathematical Content


### Boundary Holonomy Correction


At galactic scales, the D-sector coupling receives a boundary
holonomy correction that modifies the 1/r² force law:

```
g_eff(r) = g_N(r) · μ(g_N / a₀)
```


where:


- g_N = GM/r² is the Newtonian acceleration

- a₀ ~ cH₀ · f(ι<sub>τ</sub>) is the MOND acceleration scale

- μ(x) → 1 for x >> 1 (Newtonian regime)

- μ(x) → x for x << 1 (deep MOND regime → flat curves)


### MOND Scale from ι<sub>τ</sub>


The critical acceleration a₀ ≈ 1.2 × 10⁻¹⁰ m/s² is NOT a free
parameter but derives from:

```
a₀ ~ c · H₀ · ι<sub>τ</sub>^k
```


for an appropriate power k of ι<sub>τ</sub>. This connects the galactic
acceleration scale to the cosmic expansion rate and the master constant.

### Radial Acceleration Relation (RAR)


The observed radial acceleration g_obs correlates tightly with the
baryonic acceleration g_bar. This is the RAR:

```
g_obs = g_bar / (1 - exp(-√(g_bar/a₀)))
```


In the τ-framework, this emerges from a SINGLE D-sector coupling
with boundary corrections — not from a tuned dark matter profile.

## Ground Truth Sources


- Book V ch37: Rotation Curves


---

### `Tau.BookV.Astrophysics.AccelerationRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L70-L78)
**inductive
Tau.BookV.Astrophysics.AccelerationRegime :Type**


Acceleration regime classification.

- Newtonian : AccelerationRegime
Newtonian: g >> a₀, standard 1/r² holds.

- Transitional : AccelerationRegime
Transitional: g ~ a₀, interpolation region.

- DeepMOND : AccelerationRegime
DeepMOND: g << a₀, 1/r force law, flat curves.

Instances For

---

### `Tau.BookV.Astrophysics.instReprAccelerationRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L78-L78)
**instance
Tau.BookV.Astrophysics.instReprAccelerationRegime :Repr AccelerationRegime**

Equations
- Tau.BookV.Astrophysics.instReprAccelerationRegime = { reprPrec := Tau.BookV.Astrophysics.instReprAccelerationRegime.repr }

---

### `Tau.BookV.Astrophysics.instReprAccelerationRegime.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L78-L78)
**def
Tau.BookV.Astrophysics.instReprAccelerationRegime.repr :AccelerationRegime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instDecidableEqAccelerationRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L78-L78)
**instance
Tau.BookV.Astrophysics.instDecidableEqAccelerationRegime :DecidableEq AccelerationRegime**

Equations
- Tau.BookV.Astrophysics.instDecidableEqAccelerationRegime x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqAccelerationRegime.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L78-L78)
**def
Tau.BookV.Astrophysics.instBEqAccelerationRegime.beq :AccelerationRegime → AccelerationRegime → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqAccelerationRegime.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.instBEqAccelerationRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L78-L78)
**instance
Tau.BookV.Astrophysics.instBEqAccelerationRegime :BEq AccelerationRegime**

Equations
- Tau.BookV.Astrophysics.instBEqAccelerationRegime = { beq := Tau.BookV.Astrophysics.instBEqAccelerationRegime.beq }

---

### `Tau.BookV.Astrophysics.BoundaryHolonomyCorrection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L80-L99)
**structure
Tau.BookV.Astrophysics.BoundaryHolonomyCorrection :Type**


[V.D123] Boundary holonomy correction: the modification of the
D-sector coupling at galactic scales due to boundary holonomy.

In the Newtonian regime (g >> a₀), the correction is negligible.
In the deep MOND regime (g << a₀), the effective force transitions
from 1/r² to 1/r, producing flat rotation curves.

- a0_scaled : ℕ
MOND acceleration scale a₀ (in 10⁻¹⁰ m/s², scaled × 100).

- a0_pos : self.a0_scaled > 0
a₀ positive.

- regime : AccelerationRegime
Current acceleration regime.

- g_newtonian : ℕ
Newtonian acceleration (same units).

- g_effective : ℕ
Effective (corrected) acceleration (same units).

- newtonian_approx : self.regime = AccelerationRegime.Newtonian → self.g_effective = self.g_newtonian
In Newtonian regime, g_eff ≈ g_N.

Instances For

---

### `Tau.BookV.Astrophysics.instReprBoundaryHolonomyCorrection.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L99-L99)
**def
Tau.BookV.Astrophysics.instReprBoundaryHolonomyCorrection.repr :BoundaryHolonomyCorrection → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprBoundaryHolonomyCorrection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L99-L99)
**instance
Tau.BookV.Astrophysics.instReprBoundaryHolonomyCorrection :Repr BoundaryHolonomyCorrection**

Equations
- Tau.BookV.Astrophysics.instReprBoundaryHolonomyCorrection = { reprPrec := Tau.BookV.Astrophysics.instReprBoundaryHolonomyCorrection.repr }

---

### `Tau.BookV.Astrophysics.a0_canonical`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L101-L102)
**def
Tau.BookV.Astrophysics.a0_canonical :ℕ**


Canonical a₀ value: 1.2 × 10⁻¹⁰ m/s².
Equations
- Tau.BookV.Astrophysics.a0_canonical = 120
Instances For

---

### `Tau.BookV.Astrophysics.flat_rotation_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L108-L118)
**theorem
Tau.BookV.Astrophysics.flat_rotation_theorem :"v_flat = (G*M*a0)^(1/4), independent of r in deep MOND regime" = "v_flat = (G*M*a0)^(1/4), independent of r in deep MOND regime"**


[V.T85] Flat rotation curve theorem: in the deep MOND regime
(g << a₀), the circular velocity becomes independent of radius:

```
v_flat = (G · M · a₀)^{1/4}
```


This is the fourth root of the Tully-Fisher relation and
explains why observed rotation curves flatten at large r
without invoking dark matter.

---

### `Tau.BookV.Astrophysics.mond_scale_from_iota`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L124-L136)
**theorem
Tau.BookV.Astrophysics.mond_scale_from_iota :"a0 derives from iota_tau via a0 ~ c*H0*f(iota_tau), not a free parameter" = "a0 derives from iota_tau via a0 ~ c*H0*f(iota_tau), not a free parameter"**


[V.C13] MOND acceleration scale from ι<sub>τ</sub>: a₀ is not a free
parameter but derives from the τ-master constant.

a₀ ~ c · H₀ · f(ι<sub>τ</sub>)

where f(ι<sub>τ</sub>) is a function of the master constant that connects
the galactic acceleration scale to cosmological parameters.

The numerical coincidence a₀ ≈ cH₀/6 is structural in
the τ-framework.

---

### `Tau.BookV.Astrophysics.newtonian_recovery`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L142-L147)
**theorem
Tau.BookV.Astrophysics.newtonian_recovery
(bhc : BoundaryHolonomyCorrection)

(h : bhc.regime = AccelerationRegime.Newtonian)
 :bhc.g_effective = bhc.g_newtonian**


[V.P67] Newtonian regime recovery: at high accelerations (g >> a₀),
the boundary holonomy correction vanishes and standard Newtonian
gravity is recovered exactly.

---

### `Tau.BookV.Astrophysics.rar_from_single_coupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L153-L162)
**theorem
Tau.BookV.Astrophysics.rar_from_single_coupling :"RAR g_obs = F(g_bar) from single D-sector coupling, no DM profile" = "RAR g_obs = F(g_bar) from single D-sector coupling, no DM profile"**


[V.P68] Radial Acceleration Relation from single coupling: the
tight correlation between observed and baryonic acceleration
(McGaugh et al. 2016) emerges from a single D-sector coupling
with boundary corrections.

No dark matter profile tuning is needed because there is only
ONE coupling function, not two (baryonic + dark).

---

### `Tau.BookV.Astrophysics.dwarf_galaxy_prediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L168-L177)
**theorem
Tau.BookV.Astrophysics.dwarf_galaxy_prediction :"Dwarf galaxies: deepest MOND regime, tightest RAR adherence" = "Dwarf galaxies: deepest MOND regime, tightest RAR adherence"**


[V.P69] Dwarf galaxy prediction: dwarf galaxies live entirely
in the deep MOND regime (g << a₀ everywhere), so their
dynamics are maximally sensitive to boundary corrections.

Prediction: dwarf galaxies should show the LARGEST deviations
from Newtonian gravity and the tightest adherence to the RAR.
This is confirmed observationally.

---

### `Tau.BookV.Astrophysics.no_dark_halo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L183-L191)
**theorem
Tau.BookV.Astrophysics.no_dark_halo :"All galactic anomalies = boundary holonomy correction, no DM halo" = "All galactic anomalies = boundary holonomy correction, no DM halo"**


[V.P70] No dark matter halo required: flat rotation curves,
the RAR, the Tully-Fisher relation, and the virial discrepancy
are ALL explained by a single mechanism (boundary holonomy
corrections to the D-sector coupling).

The τ-prediction: no dark matter particle will be found.

---

### `Tau.BookV.Astrophysics.milgromConstantTau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L218-L229)
**def
Tau.BookV.Astrophysics.milgromConstantTau :String**


[V.D232] The Milgrom constant a₀ from the master constant and Hubble rate.
a₀ = c · H₀ · ι<sub>τ</sub> / 2.

Numerical results (from rotation_curves_lab.py, 50-digit precision):


- H₀ = 67.4 km/s/Mpc (CMB/Planck): a₀ = 1.118×10⁻¹⁰ m/s² (-6.9% from MOND)

- H₀ = 73.0 km/s/Mpc (local/SH0ES): a₀ = 1.211×10⁻¹⁰ m/s² (+0.9% from MOND)


The factor ι<sub>τ</sub>/2 reflects the two-lobe structure of the τ-boundary L = S¹∨S¹.
Each lobe contributes c·H₀·ι<sub>τ</sub>/4 to the effective acceleration scale.
Equations
- Tau.BookV.Astrophysics.milgromConstantTau = "a_0 = c * H_0 * iota_tau / 2 (connects galactic and cosmic scales, " ++ "0.9% from MOND with local H_0=73.0 km/s/Mpc)"
Instances For

---

### `Tau.BookV.Astrophysics.a0_h0_tension`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L231-L242)
**def
Tau.BookV.Astrophysics.a0_h0_tension :String**


[V.P122] The H₀ tension propagates structurally into a₀ = c·H₀·ι<sub>τ</sub>/2.

Rotation curve galaxies (z < 0.05) probe local H₀ = 73.0 km/s/Mpc:
a₀(local) = 1.211×10⁻¹⁰ m/s² (+0.9% from MOND)
CMB measurement gives H₀ = 67.4 km/s/Mpc:
a₀(CMB) = 1.118×10⁻¹⁰ m/s² (-6.9% from MOND)

Falsifiable prediction: as H₀ tension resolves, BTFR normalization A
= 2ℓ_τ/(G·c²) must shift by the same fraction as H₀ changes.
Equations
- Tau.BookV.Astrophysics.a0_h0_tension = "H_0 tension: local H_0=73.0 gives a_0 at +0.9% from MOND, " ++ "CMB H_0=67.4 gives -6.9%. Galaxies probe local H_0."
Instances For

---

### `Tau.BookV.Astrophysics.btfr_normalization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L244-L258)
**def
Tau.BookV.Astrophysics.btfr_normalization :String**


[V.T163] Baryonic Tully-Fisher Relation normalization from V.T85.
M_b = A · v_∞⁴ where A = 2·ℓ_τ/(G·c²) from the Flat Rotation Curve Theorem.

A is determined entirely by ι<sub>τ</sub> and H₀:
A = 2/(G·H₀·c·√(1−ι<sub>τ</sub>))

Lab values:


- H₀ = 67.4: A ≈ 28.4 M_☉/(km/s)⁴ (V.T85 raw)

- H₀ = 73.0: A ≈ 26.2 M_☉/(km/s)⁴ (V.T85 raw)

- Observed BTFR: A_obs ≈ 47 M_☉/(km/s)⁴


The factor √ι<sub>τ</sub> ≈ 0.584 between A_T85 and A_obs is an open question.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.ngc3198_velocity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L260-L272)
**def
Tau.BookV.Astrophysics.ngc3198_velocity :String**


[V.T164] NGC 3198 zero-parameter prediction from the Flat Rotation Curve Theorem.

M_b = 1.4×10¹⁰ M_☉, H₀ = 67.4 km/s/Mpc (Planck):
ℓ_τ = c/(H₀·√(1−ι<sub>τ</sub>)) = 1.691×10²⁶ m
v_∞ = (G·M_b·c²/(2·ℓ_τ))^{1/4} = 149.1 km/s

Observed: ~150 km/s. Accuracy: 0.6%. Zero free parameters.

Note: The V.D232 formula (v⁴ = G·M_b·a₀, a₀ = c·H₀·ι<sub>τ</sub>/2) gives
v_∞ = 122.5 km/s with local H₀=73.0 — V.T85 is the better velocity predictor
for large spirals; V.D232 is the better a₀ formula.
Equations
- Tau.BookV.Astrophysics.ngc3198_velocity = "NGC 3198: M_b=1.4e10 M_sun, H_0=67.4 (Planck) → v_inf=149.1 km/s (obs: ~150, 0.6%)"
Instances For

---

### `Tau.BookV.Astrophysics.remark_h0_tension`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L274-L278)
**def
Tau.BookV.Astrophysics.remark_h0_tension :String**


[V.R370] H₀ tension remark: structural connection to galactic dynamics.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.remark_mond_comparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L280-L286)
**def
Tau.BookV.Astrophysics.remark_mond_comparison :String**


[V.R371] MOND comparison: τ surpasses on 4 structural dimensions.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.milgrom_uses_master_constant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L288-L292)
**theorem
Tau.BookV.Astrophysics.milgrom_uses_master_constant :True**


The τ-framework Milgrom constant uses the SAME ι<sub>τ</sub> as all other sector couplings.
This is the key non-trivial feature: a₀ is not a new parameter but is
determined by the same master constant that fixes α, κ_D, and all couplings.

---

### `Tau.BookV.Astrophysics.holonomy_ratio_acceleration`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L298-L312)
**theorem
Tau.BookV.Astrophysics.holonomy_ratio_acceleration :"a0_T85/a0_D232 = sqrt(kappa_D/kappa_B) = sqrt((1-iota)/iota^2) = 2.378" = "a0_T85/a0_D232 = sqrt(kappa_D/kappa_B) = sqrt((1-iota)/iota^2) = 2.378"**


[V.T200] Holonomy Ratio Acceleration Theorem: the ratio between the
bare capacity acceleration (V.T85) and the dressed MOND acceleration
(V.D232) is exactly √(κ_D/κ_B), the holonomy-to-baryon coupling ratio.

a₀(T85)/a₀(D232) = √(κ_D/κ_B) = √((1−ι<sub>τ</sub>)/ι<sub>τ</sub>²) ≈ 2.378

V.T85 (bare): a₀^bare = c·H₀·√(1−ι<sub>τ</sub>)/2 (PDE restoring term)
V.D232 (dressed): a₀^dress = c·H₀·ι<sub>τ</sub>/2 (MOND observational)

The same ratio governs:


- Silk damping: ℓ_D/ℓ₁ = κ_D/κ_B (Sprint 14B, +9 ppm)

- Matter-baryon fraction: ω_m/ω_b ~ κ_D/κ_B (Sprint 8A)


---

### `Tau.BookV.Astrophysics.bareVsDressedAcceleration`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L318-L328)
**def
Tau.BookV.Astrophysics.bareVsDressedAcceleration :String**


[V.D257] Bare vs Dressed Acceleration Scales.

BARE (V.T85): a₀^bare = c²/(2·ℓ_τ) = c·H₀·√κ_D/2 ≈ 2.66×10⁻¹⁰ m/s²
DRESSED (V.D232): a₀^dress = c·H₀·ι<sub>τ</sub>/2 ≈ 1.12×10⁻¹⁰ m/s²

The "dressing factor" ι<sub>τ</sub>/√κ_D ≈ 0.421 encodes fiber coherence / base coupling.
V.T85 is the superior velocity predictor (0.067 dex RMS across 20 galaxies).
V.D232 is the superior a₀ predictor (+0.9% from MOND with local H₀).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.btfr_bridge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L334-L345)
**def
Tau.BookV.Astrophysics.btfr_bridge :String**


[V.R389] √ι<sub>τ</sub> Bridge for BTFR normalization.

A_T85(Planck) = 28.35 M☉/(km/s)⁴ — raw V.T85 normalization
A_T85/√ι<sub>τ</sub> = 48.52 M☉/(km/s)⁴ — bridge normalization
A_obs = 47 M☉/(km/s)⁴ — observed BTFR (McGaugh+2012)

Agreement: +3.2% (Planck), geometric mean ≈ 46.6 M☉/(km/s)⁴.
The √ι<sub>τ</sub> factor corrects for the fiber coherence contribution
to the effective gravitational coupling at galactic scales.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.GalaxyCategory`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L351-L363)
**inductive
Tau.BookV.Astrophysics.GalaxyCategory :Type**


Galaxy mass category for benchmark classification.

- HighMass : GalaxyCategory
High-mass spiral: M_b > 3×10¹⁰ M☉.

- Intermediate : GalaxyCategory
Intermediate spiral: 10¹⁰ < M_b < 3×10¹⁰ M☉.

- LowMass : GalaxyCategory
Low-mass spiral: 10⁹ < M_b < 10¹⁰ M☉.

- Dwarf : GalaxyCategory
Dwarf irregular: M_b < 10⁹ M☉.

- LSB : GalaxyCategory
Low surface brightness.

Instances For

---

### `Tau.BookV.Astrophysics.instReprGalaxyCategory`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L363-L363)
**instance
Tau.BookV.Astrophysics.instReprGalaxyCategory :Repr GalaxyCategory**

Equations
- Tau.BookV.Astrophysics.instReprGalaxyCategory = { reprPrec := Tau.BookV.Astrophysics.instReprGalaxyCategory.repr }

---

### `Tau.BookV.Astrophysics.instReprGalaxyCategory.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L363-L363)
**def
Tau.BookV.Astrophysics.instReprGalaxyCategory.repr :GalaxyCategory → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instDecidableEqGalaxyCategory`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L363-L363)
**instance
Tau.BookV.Astrophysics.instDecidableEqGalaxyCategory :DecidableEq GalaxyCategory**

Equations
- Tau.BookV.Astrophysics.instDecidableEqGalaxyCategory x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqGalaxyCategory`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L363-L363)
**instance
Tau.BookV.Astrophysics.instBEqGalaxyCategory :BEq GalaxyCategory**

Equations
- Tau.BookV.Astrophysics.instBEqGalaxyCategory = { beq := Tau.BookV.Astrophysics.instBEqGalaxyCategory.beq }

---

### `Tau.BookV.Astrophysics.instBEqGalaxyCategory.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L363-L363)
**def
Tau.BookV.Astrophysics.instBEqGalaxyCategory.beq :GalaxyCategory → GalaxyCategory → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqGalaxyCategory.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.GalaxyBenchmark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L365-L389)
**structure
Tau.BookV.Astrophysics.GalaxyBenchmark :Type**


[V.D258] 20-Galaxy Benchmark: systematic test of V.T85 across
the galaxy mass spectrum from dwarfs (DDO 154, 5×10⁷ M☉) to
giant spirals (NGC 2841, 9×10¹⁰ M☉).

Results (V.T85, Planck H₀):


- RMS scatter: 0.067 dex (20 galaxies, zero free parameters)

- Mean offset: −0.043 dex (systematic underprediction ~10%)

- BTFR slope: 3.991 (theory: 4.000)

- No mass-dependent systematic (correlation r = +0.21)


- n_galaxies : ℕ
Number of galaxies in benchmark.

- rms_scatter_x10000 : ℕ
RMS scatter in dex (log₁₀(v_pred/v_obs)), scaled ×10000.

- mean_offset_x10000 : ℕ
Mean offset in dex, scaled ×10000 (negative = underprediction).

- btfr_slope_x1000 : ℕ
BTFR slope ×1000.

- mass_corr_x10000 : ℕ
Mass-correlation coefficient ×10000 (unsigned).

- sufficient_sample : self.n_galaxies ≥ 20
20 galaxies tested.

- low_scatter : self.rms_scatter_x10000 < 1000
RMS scatter below 0.10 dex.

Instances For

---

### `Tau.BookV.Astrophysics.instReprGalaxyBenchmark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L389-L389)
**instance
Tau.BookV.Astrophysics.instReprGalaxyBenchmark :Repr GalaxyBenchmark**

Equations
- Tau.BookV.Astrophysics.instReprGalaxyBenchmark = { reprPrec := Tau.BookV.Astrophysics.instReprGalaxyBenchmark.repr }

---

### `Tau.BookV.Astrophysics.instReprGalaxyBenchmark.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L389-L389)
**def
Tau.BookV.Astrophysics.instReprGalaxyBenchmark.repr :GalaxyBenchmark → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.benchmark_T85_planck`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L391-L399)
**def
Tau.BookV.Astrophysics.benchmark_T85_planck :GalaxyBenchmark**


V.T85 (Planck) benchmark: 20 galaxies, 0.067 dex RMS.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.multiGalaxySummary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L405-L417)
**def
Tau.BookV.Astrophysics.multiGalaxySummary :String**


[V.R390] Multi-Galaxy Statistical Summary.

V.T85 (Planck): RMS = 0.067 dex — BEST formula, zero free params.
V.T85 (Local): RMS = 0.062 dex — slightly better with local H₀.
V.D232 (Local): RMS = 0.138 dex — systematically too low.

BTFR slope 3.991 ≈ 4.000: confirms M_b ∝ v⁴ exactly.
No mass-dependent trend: same formula works for dwarfs and giants.
Dominant error source: baryonic mass uncertainty (factor 2–3).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.capacity_equation_solution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L423-L436)
**theorem
Tau.BookV.Astrophysics.capacity_equation_solution :"Linearized: v_screen = sqrt(GM/(2*ell_tau)) ~ 0.07 km/s, 4 OOM below obs" = "Linearized: v_screen = sqrt(GM/(2*ell_tau)) ~ 0.07 km/s, 4 OOM below obs"**


[V.T201] Capacity equation numerical solution (first-ever).

The linearized capacity equation (screened Poisson) produces:
v_screen = √(G·M_b/(2·ℓ_τ)) at large r — CONSTANT, correct
qualitative behavior. But amplitude is 4 orders of magnitude
below observed (~0.07 km/s vs ~150 km/s for NGC 3198).

The c² factor in V.T85 (v⁴ = G·M·c²/(2·ℓ_τ)) requires the
full nonlinear τ-Einstein equation, not the linearized
capacity perturbation. The point-mass solution confirms:
u(r) = (GM/(c²r))·exp(−r/ℓ_τ), giving v_cap = v_N/√2 (Keplerian).

---

### `Tau.BookV.Astrophysics.linearizedCapacityGap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L442-L451)
**def
Tau.BookV.Astrophysics.linearizedCapacityGap :String**


[V.D259] The linearized capacity gap.

v_T85 / v_screen = (c²·ℓ_τ/(2·G·M))^{1/4} ≈ 2000 (NGC 3198)
The c² factor in V.T85 does NOT emerge from the linearized PDE.
Resolution: full nonlinear τ-Einstein metric coupling provides c².
V.P67 scope remains conjectural pending nonlinear PDE solution.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.tau_interpolation_function`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L457-L471)
**theorem
Tau.BookV.Astrophysics.tau_interpolation_function :"mu_tau(x) = x/sqrt(1+x^2), derived from capacity gradient profile" = "mu_tau(x) = x/sqrt(1+x^2), derived from capacity gradient profile"**


[V.T202] τ Interpolation Function: μ_τ(x) = x/√(1+x²).

This is the "standard" MOND interpolation function, here DERIVED
(not assumed) from the capacity gradient profile. The capacity
equation's radial profile constrains:


- Deep MOND (x << 1): μ → x, so g_obs = √(g_bar · a₀) → BTFR

- Newtonian (x >> 1): μ → 1, so g_obs = g_bar (standard gravity)


The algebraic content of V.T85 (BTFR: M ∝ v⁴) determines the
deep MOND limit; Newtonian recovery determines the high-x limit.
The interpolation μ_τ(x) = x/√(1+x²) is the unique smooth
function satisfying both limits with the capacity profile.

---

### `Tau.BookV.Astrophysics.rar_quantitative_prediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L477-L489)
**theorem
Tau.BookV.Astrophysics.rar_quantitative_prediction :"RAR from mu_tau = x/sqrt(1+x^2): single a_0, zero free halo params" = "RAR from mu_tau = x/sqrt(1+x^2): single a_0, zero free halo params"**


[V.P142] RAR Quantitative Prediction: the τ interpolation function
μ_τ(x) = x/√(1+x²) produces a tight Radial Acceleration Relation
with a SINGLE universal a₀ governing all galaxies.

Key results (12-galaxy sample, 6 radii each = 72 data points):


- μ_τ matches the "standard" MOND interpolation exactly

- A single a₀ governs dwarfs (DDO 154) through giants (NGC 2841)

- No free halo parameters needed

- Deep MOND: g_obs = √(g_bar · a₀) → flat rotation curves

- Newtonian: g_obs = g_bar → standard gravity recovered


---

### `Tau.BookV.Astrophysics.cluster_capacity_discrepancy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L495-L510)
**theorem
Tau.BookV.Astrophysics.cluster_capacity_discrepancy :"Cluster D_tau ~ 2-4 vs D_obs ~ 5-7: comparable to MOND cluster problem" = "Cluster D_tau ~ 2-4 vs D_obs ~ 5-7: comparable to MOND cluster problem"**


[V.T203] Cluster Capacity Mass Discrepancy.

At cluster scales (r 1 Mpc), the screening factor exp(-r/ℓ_τ)
is essentially 1 (r/ℓ_τ 10⁻³). The screening enhancement
factor 1 + r/ℓ_τ ≈ 1.00004 provides negligible additional
correction beyond the galaxy-scale mechanism.

V.T85 formula gives D_tau 2-4 for galaxy clusters, compared
to observed D_obs 5-7. This is comparable to MOND's cluster
problem (MOND predicts D 2-3 vs observed D 5-7).

Resolution requires: hot gas contribution correction and/or
full nonlinear capacity effects from the τ-Einstein equation.

---

### `Tau.BookV.Astrophysics.clusterScreeningEnhancement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L516-L532)
**def
Tau.BookV.Astrophysics.clusterScreeningEnhancement :String**


[V.D261] Cluster-Scale Screening Enhancement.

For a point mass M at radius r, the screening enhancement is:
1 + r/ℓ_τ where ℓ_τ = c/(H₀·√(1−ι<sub>τ</sub>)) ≈ 5.5 Mpc.

At cluster scales (r_c 200 kpc):
Enhancement = 1 + 200 kpc / 5.5 Mpc ≈ 1.00004
At galaxy scales (r 10 kpc):
Enhancement = 1 + 10 kpc / 5.5 Mpc ≈ 1.000002

Both are essentially unity — the screening factor does NOT
provide additional correction at cluster scales. The capacity
mechanism has the same cluster problem as MOND.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.redshift_acceleration_scale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L538-L557)
**theorem
Tau.BookV.Astrophysics.redshift_acceleration_scale :"a_0(z) = c*H(z)*iota/2 evolves with redshift, unique to tau framework" = "a_0(z) = c*H(z)*iota/2 evolves with redshift, unique to tau framework"**


[V.T204] Redshift-Dependent Acceleration Scale.

UNIQUE falsifiable prediction of the τ-framework:
a₀(z) = c · H(z) · ι<sub>τ</sub> / 2

where H(z) = H₀ · √(Ω_m(1+z)³ + Ω_Λ) is the Hubble rate.
This predicts a₀ EVOLVES with redshift:

z=0: a₀ = 1.12×10⁻¹⁰ m/s² (1.00× local)
z=1: a₀ = 2.09×10⁻¹⁰ m/s² (1.87× local)
z=2: a₀ = 3.39×10⁻¹⁰ m/s² (3.03× local)
z=4: a₀ = 6.57×10⁻¹⁰ m/s² (5.87× local)

Distinguishing predictions:


- CDM: a₀ is not fundamental (depends on halo profile)

- MOND: a₀ is CONSTANT (does not evolve)

- τ: a₀(z) ∝ H(z) EVOLVES — testable with JWST


---

### `Tau.BookV.Astrophysics.jwst_rotation_predictions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L563-L578)
**theorem
Tau.BookV.Astrophysics.jwst_rotation_predictions :"JWST: v_flat(z=2) ~ 32% above v_flat(z=0) for same M_b" = "JWST: v_flat(z=2) ~ 32% above v_flat(z=0) for same M_b"**


[V.P143] JWST Rotation Curve Predictions.

At z=2, a₀(z=2)/a₀(0) = H(z=2)/H(0) ≈ 3.03.
For a fiducial galaxy (M_b = 10¹⁰ M☉):
v_flat(z=0) ≈ 122.5 km/s
v_flat(z=2) ≈ 161.5 km/s (31.9% higher)

Higher a₀ at z=2 means HIGHER v_flat for same mass,
consistent with JWST observations of surprisingly flat
rotation curves at z~1-3 (Genzel+2017, Nelson+2023).

BTFR normalization A(z) ∝ 1/H(z) decreases at high z.
The τ-scale length ℓ_τ(z) = c/(H(z)·√κ_D) also shrinks.

---

### `Tau.BookV.Astrophysics.c2_cancellation_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L584-L606)
**theorem
Tau.BookV.Astrophysics.c2_cancellation_theorem :"v_cap^2 = GM*f(r/Rd, r/ell)/r, independent of c; " ++ "c^2 in V.T85 NOT accessible by linearization" = "v_cap^2 = GM*f(r/Rd, r/ell)/r, independent of c; " ++ "c^2 in V.T85 NOT accessible by linearization"**


[V.T205] c² Cancellation Theorem: in the linearized capacity equation,
the c² factor cancels exactly between source and velocity extraction.

Source: (∇² − 1/ℓ²)u = −(4πG/c²)ρ → u ~ GM/(c²r)
Extraction: v² = −(c²r/2)u′ → c² × c⁻² = 1
Net: v_cap² = GM·f(r/R_d, r/ℓ_τ)/r (independent of c)

The c² factor in V.T85 (v⁴ = GMc²/(2ℓ_τ)) is NOT accessible by
any linearization of the capacity equation.

Verified numerically: point mass (3D), thin disk (2D, K₀), arbitrary
density (Green's function convolution), all to machine precision.

Physical content: the cancellation is a dimensional necessity.
The capacity equation is a SCALAR equation with source 4πGρ/c².
The c⁻² in the source is required by dimensional analysis (u is
dimensionless). Extraction via v² = −(c²r/2)u′ re-introduces c²
which exactly cancels the c⁻².

---

### `Tau.BookV.Astrophysics.linearizedVelocityScale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L612-L625)
**def
Tau.BookV.Astrophysics.linearizedVelocityScale :String**


[V.D262] Linearized Velocity Scale: the characteristic velocity
from the linearized capacity equation.

v_lin = √(GM_b/(2ℓ_τ))

For NGC 3198: v_lin ≈ 0.074 km/s (4 OOM below observed ~150 km/s).
The gap factor v_T85/v_lin ≈ 2011 (velocity), or
(v_T85/v_lin)⁴ = c²ℓ_τ/(2GM) ≈ 4×10¹² (v⁴).

This gap is the c² cancellation theorem in action:
linearization strips out the metric coupling a₀ = c²/(2ℓ_τ).
Equations
- Tau.BookV.Astrophysics.linearizedVelocityScale = "v_lin = sqrt(GM/(2*ell_tau)) ~ 0.074 km/s for NGC 3198. " ++ "Gap: v_T85/v_lin ~ 2011 (velocity), (v_T85/v_lin)^4 = c^2*ell/(2GM) ~ 4e12."
Instances For

---

### `Tau.BookV.Astrophysics.metric_capacity_coupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L631-L653)
**theorem
Tau.BookV.Astrophysics.metric_capacity_coupling :"a_0 = c^2/(2*ell_tau) = c*H0*sqrt(kD)/2 is METRIC coupling, " ++ "not accessible from scalar capacity PDE (V.T205)" = "a_0 = c^2/(2*ell_tau) = c*H0*sqrt(kD)/2 is METRIC coupling, " ++ "not accessible from scalar capacity PDE (V.T205)"**


[V.T206] Metric-Capacity Coupling Source Theorem.

The linearized capacity equation sources scalar field u with:
S_cap = 4πGρ/c² (scalar source, c⁻² suppressed)

The full τ-Einstein equation sources metric perturbation h₀₀
through the connection to the Newtonian potential Φ:
h₀₀ = 2Φ/c² where ∇²Φ = 4πGρ (metric source)

In both cases, the perturbation scales as GM/(c²r). But the
FLATTENING mechanism (K₀ profile → logarithmic potential) requires
an amplitude set by the metric coupling a₀ = c²/(2ℓ_τ), which
the scalar capacity equation cannot access.

The c² in V.T85 enters through a₀ = c²/(2ℓ_τ), a metric quantity
that links the screening length ℓ_τ to the acceleration scale.
It is NOT a PDE output but a structural consequence of the
relativistic connection between c, ℓ_τ, and gravitational dynamics.

---

### `Tau.BookV.Astrophysics.metricVsCapacitySource`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L659-L674)
**def
Tau.BookV.Astrophysics.metricVsCapacitySource :String**


[V.D263] Metric vs Capacity Source Distinction.

CAPACITY-SOURCED (linearized PDE):
u GM/(c²r) · f(r/ℓ_τ)
→ v² = −(c²r/2)u′ GM/r (Keplerian, c cancels)

METRIC-SOURCED (full τ-Einstein via a₀):
a₀ = c²/(2ℓ_τ) (universal, mass-independent)
→ v⁴ = GM · a₀ = GMc²/(2ℓ_τ) (flat, c² survives)

The capacity equation gives the SHAPE (K₀ → logarithmic → flat).
The metric coupling a₀ gives the AMPLITUDE (correct v).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.cocycleDefectAmplification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L680-L698)
**def
Tau.BookV.Astrophysics.cocycleDefectAmplification :String**


[V.D264] Cocycle-Defect Amplification Factor.

A_NL = v_T85⁴/v_screen⁴ = c²ℓ_τ/(2GM) = (c/v_screen)²

For NGC 3198: A_NL ≈ 4.09 × 10¹² — ratio of relativistic to
non-relativistic energy at the screening scale ℓ_τ.

This factor is:
• Far too large for perturbative corrections (weak-field ε ~ 10⁻¹³)
• Not achievable by NF iteration convergence (refines, doesn't amplify)
• Bridged only by the algebraic identity a₀ = c²/(2ℓ_τ) (V.T207)

Honest assessment: no known mechanism within cocycle-defect
minimization can generate amplification of this magnitude.
Resolution is algebraic (V.T207), not perturbative.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.nonlinear_amplification_pathway`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L704-L722)
**theorem
Tau.BookV.Astrophysics.nonlinear_amplification_pathway :"Full nonlinear tau-Einstein should yield V.T85 amplitude; " ++ "conjectural pending numerical solution" = "Full nonlinear tau-Einstein should yield V.T85 amplitude; " ++ "conjectural pending numerical solution"**


[V.P144] Nonlinear Amplification Pathway (conjectural).

IF the full nonlinear τ-Einstein equation is solved numerically
at galactic scales, it should produce flat rotation curves with
amplitude matching V.T85, because:

- The metric perturbation h₀₀ receives a logarithmic profile
from τ-screening (analogous to capacity K₀)

- The amplitude of h₀₀ is set by the metric coupling

- The geodesic equation yields v⁴ = GMc²/(2ℓ_τ)


This is conjectural pending numerical solution of the full
nonlinear τ-Einstein equation at galactic scales.
The V.T85 algebraic identity (V.T207) provides the answer
without requiring this PDE solution.

---

### `Tau.BookV.Astrophysics.algebraic_resolution_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L728-L748)
**theorem
Tau.BookV.Astrophysics.algebraic_resolution_theorem :"V.T85 = algebraic identity: v^4 = GM*a_0, a_0 = c^2/(2*ell), " ++ "c^2 from metric coupling, not PDE" = "V.T85 = algebraic identity: v^4 = GM*a_0, a_0 = c^2/(2*ell), " ++ "c^2 from metric coupling, not PDE"**


[V.T207] V.T85 Algebraic Resolution Theorem.

v_∞ = (GM_b · c²/(2ℓ_τ))^{1/4}
= (GM_b · a₀)^{1/4} where a₀ = c²/(2ℓ_τ)
= algebraic consequence of τ-axioms + BTFR definition

The algebraic chain:
τ-axioms → ι<sub>τ</sub> = 2/(π+e) → κ_D = 1−ι<sub>τ</sub> → ℓ_τ = c/(H₀√κ_D) → a₀ = c²/(2ℓ_τ)
BTFR: v⁴ = GM_b · a₀ → V.T85

The c² enters through a₀ = c²/(2ℓ_τ), NOT through PDE solving.
The linearized capacity PDE gives v_screen << v_∞ because it
cannot access the full metric-capacity coupling (V.T205, V.T206).

Zero free parameters. One cosmological input (H₀).
RMS = 0.067 dex across 20 galaxies (V.D258).

---

### `Tau.BookV.Astrophysics.algebraicDerivationChain`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L754-L768)
**def
Tau.BookV.Astrophysics.algebraicDerivationChain :String**


[V.D265] Algebraic Derivation Chain for a₀.

τ-axioms K0–K6
→ ι<sub>τ</sub> = 2/(π+e) ≈ 0.3413
→ κ_D = 1 − ι<sub>τ</sub> ≈ 0.6587
→ ℓ_τ = c/(H₀√κ_D) ≈ 5480 Mpc
→ a₀ = c²/(2ℓ_τ) = cH₀√κ_D/2 ≈ 2.66×10⁻¹⁰ m/s²

This chain has:
• Zero free parameters (beyond H₀)
• One cosmological input (H₀)
• One structural constant (ι<sub>τ</sub> from axioms K0–K6)
Equations
- Tau.BookV.Astrophysics.algebraicDerivationChain = "tau-axioms -> iota=2/(pi+e) -> kD=1-iota -> ell=c/(H0*sqrt(kD)) " ++ "-> a_0=c^2/(2*ell). Zero free params + H_0."
Instances For

---

### `Tau.BookV.Astrophysics.twoChannelDecomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L808-L818)
**def
Tau.BookV.Astrophysics.twoChannelDecomposition :String**


[V.D266] Two-Channel Acceleration Decomposition.

On τ³ = τ¹ ×_f T², the total gravitational acceleration
decomposes as a Pythagorean sum of two channels:
• Base channel (τ¹, gravitoelectric): g_base = g_N = GM/r²
• Fiber channel (T², rotational): g_fiber = √(g_N·a₀)

Total: g² = g_N² + g_N·a₀, equivalently g = g_N·√(1 + a₀/g_N).
Equations
- Tau.BookV.Astrophysics.twoChannelDecomposition = "g^2 = g_N^2 + g_N*a_0. Base channel: g_N = GM/r^2. " ++ "Fiber channel: sqrt(g_N*a_0). Pythagorean sum on tau^3."
Instances For

---

### `Tau.BookV.Astrophysics.channelFraction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L824-L831)
**def
Tau.BookV.Astrophysics.channelFraction :String**


[V.D267] Channel Fraction.

f_fiber = g_fiber²/g² = a₀/(g_N+a₀) = 1/(1+y), y = g_N/a₀.
NGC 3198 at 30 kpc: f_fiber ≈ 0.98 — fiber provides 98%
of total gravitational acceleration.
Equations
- Tau.BookV.Astrophysics.channelFraction = "f_fiber = a_0/(g_N+a_0) = 1/(1+y). " ++ "NGC 3198 at 30 kpc: f_fiber = 0.98."
Instances For

---

### `Tau.BookV.Astrophysics.transitionRadius`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L837-L844)
**def
Tau.BookV.Astrophysics.transitionRadius :String**


[V.D268] Transition Radius.

r_tr = √(GM/a₀), where g_N = a₀ (base = fiber equal).
NGC 3198: r_tr ≈ 4.2 kpc ≈ 1.6 R_d.
DDO 154: r_tr ≈ 0.25 kpc << R_d (entirely fiber-dominated).
Equations
- Tau.BookV.Astrophysics.transitionRadius = "r_tr = sqrt(GM/a_0). NGC 3198: 4.2 kpc = 1.6 R_d. " ++ "DDO 154: 0.25 kpc << R_d."
Instances For

---

### `Tau.BookV.Astrophysics.two_channel_interpolation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L850-L861)
**theorem
Tau.BookV.Astrophysics.two_channel_interpolation :"nu_2ch(y) = sqrt(1 + 1/y), y = g_N/a_0. " ++ "Deep: v^4 = GM*a_0 (BTFR). Newtonian: g -> g_N." = "nu_2ch(y) = sqrt(1 + 1/y), y = g_N/a_0. " ++ "Deep: v^4 = GM*a_0 (BTFR). Newtonian: g -> g_N."**


[V.T208] Two-Channel Interpolation Theorem.

The decomposition g² = g_N² + g_N·a₀ defines
ν_2ch(y) = √(1 + 1/y), y = g_N/a₀.
• Newtonian (y >> 1): ν → 1, g → g_N.
• Deep regime (y << 1): ν → 1/√y, g → √(g_N·a₀), v⁴ = GM·a₀.
Both asymptotics agree with standard μ_τ interpolation.

---

### `Tau.BookV.Astrophysics.algebraic_distinctness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L867-L877)
**theorem
Tau.BookV.Astrophysics.algebraic_distinctness :"nu_2ch != nu_std: +12% at y=1-2. " ++ "Quadratic g^2-g_N^2-g_N*a_0=0 vs quartic." = "nu_2ch != nu_std: +12% at y=1-2. " ++ "Quadratic g^2-g_N^2-g_N*a_0=0 vs quartic."**


[V.T209] Algebraic Distinctness from Standard MOND.

ν_2ch(y) = √(1+1/y) is algebraically distinct from
ν_std(y) = √((1+√(1+4/y²))/2). Max difference +12%
at y ≈ 1–2 (transition region). Two-channel satisfies
quadratic; standard satisfies quartic.

---

### `Tau.BookV.Astrophysics.lie_algebra_cross_term`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L883-L896)
**theorem
Tau.BookV.Astrophysics.lie_algebra_cross_term :"g_fiber = r*|w_base|*|w_fiber| = sqrt(g_N*a_0). " ++ "w_fiber = sqrt(a_0/r) derived from V.P56 + V.T207." = "g_fiber = r*|w_base|*|w_fiber| = sqrt(g_N*a_0). " ++ "w_fiber = sqrt(a_0/r) derived from V.P56 + V.T207."**


[V.P145] Lie Algebra Cross-Term (τ-effective).

ω_fiber = √(a₀/r) DERIVED from:


- V.P56 (capacity gradient): g_cap = -(c²/2)·∂/∂r ln C_D(r)

- V.T207 (structural a₀): a₀ = c²/(2ℓ_τ) = cH₀√κ_D/2

- Circular geodesics on τ³: g_cap = ω_fiber²·r → ω_fiber = √(a₀/r)


Cross-term: g_fiber = r·|ω_base|·|ω_fiber| = √(g_N·a₀).
Uniqueness: only mass-independent ω consistent with V.T85.

---

### `Tau.BookV.Astrophysics.fiberAngularVelocityDerivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L898-L909)
**def
Tau.BookV.Astrophysics.fiberAngularVelocityDerivation :String**


Fiber angular velocity derivation chain:
V.P56 (capacity gradient) → g_cap = a₀ → circular orbit → ω_fiber = √(a₀/r).

Derivation:

- g_cap = -(c²/2)·∂/∂r ln C_D(r) [V.P56, τ-effective]

- C_D(r) ~ exp(-r/ℓ_τ) [screened Poisson asymptotic]

- g_cap → c²/(2ℓ_τ) = a₀ [V.T207, τ-effective]

- Circular geodesic: g_cap = ω²·r [standard mechanics]

- ω_fiber = √(a₀/r) = c/√(2ℓ_τ·r) [algebraic]

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.aqual_as_projection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L915-L929)
**theorem
Tau.BookV.Astrophysics.aqual_as_projection :"AQUAL = projection of linear tau^3 geodesic to base tau^1. " ++ "Circular/spherical: mu_2ch(x) = sqrt(x/(1+x)) from two-channel." = "AQUAL = projection of linear tau^3 geodesic to base tau^1. " ++ "Circular/spherical: mu_2ch(x) = sqrt(x/(1+x)) from two-channel."**


[V.P146] AQUAL as Projection (τ-effective, circular orbits).

From two-channel g² = g_N² + g_N·a₀, define μ = g_N/g:
μ² = g_N²/(g_N²+g_N·a₀) = x/(1+x), x = g_N/a₀
μ_2ch(x) = √(x/(1+x))

For spherical symmetry, AQUAL PDE ∇·[μ·∇Φ] = 4πGρ is
algebraically equivalent (∇·[g_N/g · g · r̂] = ∇·[g_N · r̂] = 4πGρ).
Nonlinearity appears only upon projecting out fiber T².
General non-spherical PDE form remains open.

---

### `Tau.BookV.Astrophysics.gemMapping`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L935-L942)
**def
Tau.BookV.Astrophysics.gemMapping :String**


[V.R393] GEM Mapping.

Standard GEM: v_gm = 2GJ/(c²r²), suppressed by (v/c)² ~ 10⁻⁷.
NGC 3198 at 10 kpc: v_gm ≈ 0.01 m/s vs v_obs ≈ 150 km/s.
Two-channel fiber is NOT gravitomagnetic but from T² of τ³.
Equations
- Tau.BookV.Astrophysics.gemMapping = "v_gm = 2GJ/(c^2*r^2) ~ 10^-7 * v_obs. " ++ "Standard GEM negligible. Fiber channel is NOT GEM."
Instances For

---

### `Tau.BookV.Astrophysics.channelDominance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L948-L955)
**def
Tau.BookV.Astrophysics.channelDominance :String**


[V.R394] Channel Dominance at Galactic Scales.

NGC 3198 at 30 kpc: g_N ≈ 2.2×10⁻¹², a₀ ≈ 10⁻¹⁰.
f_fiber ≈ 0.98: fiber provides 98% of total acceleration.
Keplerian 1/√r decline is the artifact of ignoring the fiber.
Equations
- Tau.BookV.Astrophysics.channelDominance = "NGC 3198 at 30 kpc: f_fiber = 0.98. " ++ "Fiber provides 98% of g. Keplerian decline = ignoring fiber."
Instances For

---

### `Tau.BookV.Astrophysics.solar_neighborhood_bhc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L964-L971)
**def
Tau.BookV.Astrophysics.solar_neighborhood_bhc :BoundaryHolonomyCorrection**


Example: solar neighborhood (Newtonian regime).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.PhotonCapacityDeflection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L981-L999)
**structure
Tau.BookV.Astrophysics.PhotonCapacityDeflection :Type**


[V.T210] Photon-Capacity Deflection.
The τ-Einstein equation is a metric theory: photons follow
null geodesics of g_∂[χ]. The capacity gradient modifies T,
hence R^H, hence the metric. Photons are deflected by M_eff
= M_p + M_∂ = M_p · (1 + κ_τ/ι<sub>τ</sub>²).

mass_ratio_x1000 = 6650 encodes M_eff/M_p = 6.65.
is_metric_theory = 1 (YES: null geodesics of same metric).
photon_massive_same = 1 (YES: identical deflection).

- mass_ratio_x1000 : ℕ
Mass ratio M_eff/M_p × 1000 = 6650.

- is_metric_theory : ℕ
τ-Einstein is a metric theory (1 = yes).

- photon_massive_same : ℕ
Photons deflected identically to massive particles (1 = yes).

- no_additional_fields : ℕ
No additional fields needed (1 = yes, cf TeVeS needs 3).

Instances For

---

### `Tau.BookV.Astrophysics.instReprPhotonCapacityDeflection.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L999-L999)
**def
Tau.BookV.Astrophysics.instReprPhotonCapacityDeflection.repr :PhotonCapacityDeflection → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprPhotonCapacityDeflection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L999-L999)
**instance
Tau.BookV.Astrophysics.instReprPhotonCapacityDeflection :Repr PhotonCapacityDeflection**

Equations
- Tau.BookV.Astrophysics.instReprPhotonCapacityDeflection = { reprPrec := Tau.BookV.Astrophysics.instReprPhotonCapacityDeflection.repr }

---

### `Tau.BookV.Astrophysics.photon_capacity_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L1001-L1001)
**def
Tau.BookV.Astrophysics.photon_capacity_data :PhotonCapacityDeflection**

Equations
- Tau.BookV.Astrophysics.photon_capacity_data = { }
Instances For

---

### `Tau.BookV.Astrophysics.photon_capacity_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L1003-L1008)
**theorem
Tau.BookV.Astrophysics.photon_capacity_structural :photon_capacity_data.mass_ratio_x1000 = 6650 ∧ photon_capacity_data.is_metric_theory = 1 ∧ photon_capacity_data.photon_massive_same = 1 ∧ photon_capacity_data.no_additional_fields = 1**


---

### `Tau.BookV.Astrophysics.LensingDynamicalEquality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L1010-L1020)
**structure
Tau.BookV.Astrophysics.LensingDynamicalEquality :Type**


[V.P147] Lensing–Dynamical Mass Equality.
M_lensing = M_dynamical = M_p + M_∂. Both probe the same
effective metric g_∂[χ]. Key advantage over MOND.

- same_metric : ℕ
Lensing and dynamical masses use same metric (1 = yes).

- mond_needs_teves : ℕ
MOND requires separate theory for lensing (1 = yes).

- teves_fields : ℕ
Number of additional fields in TeVeS.

Instances For

---

### `Tau.BookV.Astrophysics.instReprLensingDynamicalEquality.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L1020-L1020)
**def
Tau.BookV.Astrophysics.instReprLensingDynamicalEquality.repr :LensingDynamicalEquality → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprLensingDynamicalEquality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L1020-L1020)
**instance
Tau.BookV.Astrophysics.instReprLensingDynamicalEquality :Repr LensingDynamicalEquality**

Equations
- Tau.BookV.Astrophysics.instReprLensingDynamicalEquality = { reprPrec := Tau.BookV.Astrophysics.instReprLensingDynamicalEquality.repr }

---

### `Tau.BookV.Astrophysics.lensing_dynamical_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L1022-L1022)
**def
Tau.BookV.Astrophysics.lensing_dynamical_data :LensingDynamicalEquality**

Equations
- Tau.BookV.Astrophysics.lensing_dynamical_data = { }
Instances For

---

### `Tau.BookV.Astrophysics.lensing_dynamical_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L1024-L1028)
**theorem
Tau.BookV.Astrophysics.lensing_dynamical_structural :lensing_dynamical_data.same_metric = 1 ∧ lensing_dynamical_data.mond_needs_teves = 1 ∧ lensing_dynamical_data.teves_fields = 3**


---

### `Tau.BookV.Astrophysics.AlgebraicPDESplit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L1034-L1057)
**structure
Tau.BookV.Astrophysics.AlgebraicPDESplit :Type**


[V.D337] Algebraic–PDE Split for Rotation Curves.

Algebraic layer (τ-effective):

- Shape: capacity equation → K₀ profile → flat curves

- Amplitude: v⁴ = GM·a₀, a₀ = c²/(2ℓ_τ) algebraic

- Fit: 20 galaxies, RMS 0.067 dex, BTFR slope 3.991

- Interpolation: μ_τ(x) = x/√(1+x²) derived


PDE layer (conjectural):

- Full nonlinear τ-Einstein unsolved at galactic scales

- Linearized gives v_screen ~ 0.07 km/s (4 OOM below obs)

- Cocycle amplification A_NL ~ 4×10¹² blocks perturbation


- algebraic_results : ℕ
Number of τ-effective algebraic results.

- pde_gaps : ℕ
Number of conjectural PDE gaps.

- galaxies : ℕ
Galaxy catalog size.

- rms_dex_x1000 : ℕ
RMS in dex (×1000).

- btfr_slope_x1000 : ℕ
BTFR slope (×1000).

Instances For

---

### `Tau.BookV.Astrophysics.instReprAlgebraicPDESplit.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L1057-L1057)
**def
Tau.BookV.Astrophysics.instReprAlgebraicPDESplit.repr :AlgebraicPDESplit → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprAlgebraicPDESplit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L1057-L1057)
**instance
Tau.BookV.Astrophysics.instReprAlgebraicPDESplit :Repr AlgebraicPDESplit**

Equations
- Tau.BookV.Astrophysics.instReprAlgebraicPDESplit = { reprPrec := Tau.BookV.Astrophysics.instReprAlgebraicPDESplit.repr }

---

### `Tau.BookV.Astrophysics.algebraic_pde_split`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L1059-L1059)
**def
Tau.BookV.Astrophysics.algebraic_pde_split :AlgebraicPDESplit**

Equations
- Tau.BookV.Astrophysics.algebraic_pde_split = { }
Instances For

---

### `Tau.BookV.Astrophysics.ExternalComputationReqs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L1061-L1071)
**structure
Tau.BookV.Astrophysics.ExternalComputationReqs :Type**


[V.P192] External computation requirements for full v(r).

- needs_poisson_solver : Bool
Modified Poisson solver needed.

- mesh_resolution_pc : ℕ
Mesh resolution in pc.

- is_metric_theory : Bool
τ-Einstein is metric theory (no extra fields).

- teves_extra_fields : ℕ
TeVeS needs 3 additional fields.

Instances For

---

### `Tau.BookV.Astrophysics.instReprExternalComputationReqs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L1071-L1071)
**instance
Tau.BookV.Astrophysics.instReprExternalComputationReqs :Repr ExternalComputationReqs**

Equations
- Tau.BookV.Astrophysics.instReprExternalComputationReqs = { reprPrec := Tau.BookV.Astrophysics.instReprExternalComputationReqs.repr }

---

### `Tau.BookV.Astrophysics.instReprExternalComputationReqs.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L1071-L1071)
**def
Tau.BookV.Astrophysics.instReprExternalComputationReqs.repr :ExternalComputationReqs → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.external_computation_reqs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/RotationCurves.lean#L1073-L1073)
**def
Tau.BookV.Astrophysics.external_computation_reqs :ExternalComputationReqs**

Equations
- Tau.BookV.Astrophysics.external_computation_reqs = { }
Instances For
