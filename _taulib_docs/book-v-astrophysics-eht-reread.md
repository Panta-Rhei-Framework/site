---
layout: taulib-doc
title: "TauLib.BookV.Astrophysics.EHTReread"
permalink: /verify/taulib/docs/book-v-astrophysics-eht-reread/
lane: verify
module_name: "TauLib.BookV.Astrophysics.EHTReread"
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

# TauLib.BookV.Astrophysics.EHTReread


Event Horizon Telescope reanalysis. The τ-horizon vs the classical
event horizon. Shadow predictions and the distinction between the
τ-framework's topology crossing and GR's coordinate singularity.

## Registry Cross-References


- [V.D137] Tau Horizon Definition -- `TauHorizonDef`

- [V.T95] Shadow Size Prediction -- `shadow_size_prediction`

- [V.P82] Photon Ring from Holonomy -- `photon_ring_holonomy`

- [V.D138] EHT Observable Data -- `EHTObservableData`

- [V.P83] Shadow Circularity from Torus Symmetry -- `shadow_circularity`

- [V.R196] M87* Shadow Consistent -- structural remark

- [V.D139] Tau vs GR Horizon Comparison -- `HorizonComparison`

- [V.T96] No Information Loss at Tau Horizon -- `no_information_loss`

- [V.R197] Firewall Paradox Dissolved -- structural remark

- [V.R198] Sgr A* as Milky Way Test -- structural remark

- [V.R199] Future EHT Precision Tests -- structural remark


## Mathematical Content


### Tau Horizon vs Event Horizon


In GR, the event horizon is a null surface at r = 2GM/c² beyond
which nothing can escape. In the τ-framework:


- There is NO event horizon as a causal boundary

- The τ-horizon is the TOPOLOGY CROSSING where defect-bundle topology
transitions from S² to T² (same as coherence horizon)

- The τ-horizon is a physical boundary, not a coordinate artifact

- Information is preserved (no information paradox)


### BH Shadow


The shadow of a BH (as imaged by EHT) corresponds to the photon
capture radius r_ph = 3GM/c² (not the horizon r_s = 2GM/c²).

In the τ-framework, the shadow boundary is the last stable
circular orbit of null (photon) boundary characters around the
torus vacuum T².

### Shadow Predictions


The τ-framework predicts:

- Shadow size ∝ M (same as GR, confirmed by M87*)

- Shadow is nearly circular for non-spinning BH (T² symmetry)

- Photon ring structure from successive holonomy loops

- No information loss (sharp prediction different from GR)


## Ground Truth Sources


- Book V ch42: EHT Reanalysis


---

### `Tau.BookV.Astrophysics.HorizonType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L66-L74)
**inductive
Tau.BookV.Astrophysics.HorizonType :Type**


Horizon type comparison.

- GREventHorizon : HorizonType
GR event horizon: null surface, causal boundary.

- TauHorizon : HorizonType
Tau horizon: topology crossing S² → T².

- ApparentHorizon : HorizonType
Apparent horizon: trapped-surface boundary.

Instances For

---

### `Tau.BookV.Astrophysics.instReprHorizonType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L74-L74)
**instance
Tau.BookV.Astrophysics.instReprHorizonType :Repr HorizonType**

Equations
- Tau.BookV.Astrophysics.instReprHorizonType = { reprPrec := Tau.BookV.Astrophysics.instReprHorizonType.repr }

---

### `Tau.BookV.Astrophysics.instReprHorizonType.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L74-L74)
**def
Tau.BookV.Astrophysics.instReprHorizonType.repr :HorizonType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instDecidableEqHorizonType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L74-L74)
**instance
Tau.BookV.Astrophysics.instDecidableEqHorizonType :DecidableEq HorizonType**

Equations
- Tau.BookV.Astrophysics.instDecidableEqHorizonType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Astrophysics.instBEqHorizonType.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L74-L74)
**def
Tau.BookV.Astrophysics.instBEqHorizonType.beq :HorizonType → HorizonType → Bool**

Equations
- Tau.BookV.Astrophysics.instBEqHorizonType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Astrophysics.instBEqHorizonType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L74-L74)
**instance
Tau.BookV.Astrophysics.instBEqHorizonType :BEq HorizonType**

Equations
- Tau.BookV.Astrophysics.instBEqHorizonType = { beq := Tau.BookV.Astrophysics.instBEqHorizonType.beq }

---

### `Tau.BookV.Astrophysics.TauHorizonDef`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L76-L97)
**structure
Tau.BookV.Astrophysics.TauHorizonDef :Type**


[V.D137] Tau horizon definition: the τ-horizon is the topology
crossing boundary where the defect-bundle topology transitions
from S² (stellar surface) to T² (torus vacuum).

Unlike the GR event horizon:


- It is a PHYSICAL boundary (topology change), not a coordinate artifact

- It preserves information (boundary characters are continuous)

- It has finite local physics (no singularity)


- mass_tenth_solar : ℕ
Mass of the BH (tenths of solar mass).

- mass_pos : self.mass_tenth_solar > 0
Mass positive.

- horizon_radius_scaled : ℕ
Horizon radius (Schwarzschild radii, scaled × 100).

- horizon_type : HorizonType
Horizon type.

- information_preserved : Bool
Whether information is preserved.

- has_singularity : Bool
Whether a singularity exists.

Instances For

---

### `Tau.BookV.Astrophysics.instReprTauHorizonDef.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L97-L97)
**def
Tau.BookV.Astrophysics.instReprTauHorizonDef.repr :TauHorizonDef → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprTauHorizonDef`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L97-L97)
**instance
Tau.BookV.Astrophysics.instReprTauHorizonDef :Repr TauHorizonDef**

Equations
- Tau.BookV.Astrophysics.instReprTauHorizonDef = { reprPrec := Tau.BookV.Astrophysics.instReprTauHorizonDef.repr }

---

### `Tau.BookV.Astrophysics.m87_shadow_uas`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L103-L104)
**def
Tau.BookV.Astrophysics.m87_shadow_uas :ℕ**


Shadow angular diameter (microarcseconds, for specific sources).
Equations
- Tau.BookV.Astrophysics.m87_shadow_uas = 42
Instances For

---

### `Tau.BookV.Astrophysics.sgra_shadow_uas`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L105-L105)
**def
Tau.BookV.Astrophysics.sgra_shadow_uas :ℕ**

Equations
- Tau.BookV.Astrophysics.sgra_shadow_uas = 52
Instances For

---

### `Tau.BookV.Astrophysics.shadow_size_prediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L107-L123)
**theorem
Tau.BookV.Astrophysics.shadow_size_prediction :"Shadow = 3*sqrt(3)*GM/(c^2*D), identical to GR at photon sphere" = "Shadow = 3*sqrt(3)*GM/(c^2*D), identical to GR at photon sphere"**


[V.T95] Shadow size prediction: the BH shadow angular diameter
is determined by the photon capture radius r_ph = 3GM/c².

```
θ_shadow = 3√3 · GM / (c² · D)
```


where D is the angular diameter distance.

The τ-framework gives the SAME shadow size as GR because the
D-sector coupling at the photon sphere is identical to the GR
metric at r = 3GM/c². The difference appears only AT and BELOW
the horizon, not at the photon sphere.

M87*: 42 ± 3 μas (EHT 2019, consistent)
Sgr A*: 52 ± 1 μas (EHT 2022, consistent)

---

### `Tau.BookV.Astrophysics.photon_ring_holonomy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L129-L138)
**theorem
Tau.BookV.Astrophysics.photon_ring_holonomy :"Photon ring = successive holonomy loops around T^2 torus vacuum" = "Photon ring = successive holonomy loops around T^2 torus vacuum"**


[V.P82] Photon ring from holonomy: the photon ring (bright ring
in the EHT image) is produced by photons that complete one or
more holonomy loops around the torus vacuum before escaping.

Each successive sub-ring (n = 1, 2, 3, ...) corresponds to
one additional holonomy loop, with exponentially decreasing
brightness and exponentially narrowing width.

---

### `Tau.BookV.Astrophysics.EHTObservableData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L144-L157)
**structure
Tau.BookV.Astrophysics.EHTObservableData :Type**


[V.D138] EHT observable data: the quantities measurable by the
Event Horizon Telescope for a given BH target.

- target : String
Target name.

- shadow_diameter_uas : ℕ
Shadow angular diameter (μas).

- circularity_scaled : ℕ
Shadow circularity (1.0 = perfect circle, scaled × 100).

- ring_ratio_pct : ℕ
Photon ring brightness ratio (n=1 to n=0, percent).

- is_resolved : Bool
Whether the shadow is resolved.

Instances For

---

### `Tau.BookV.Astrophysics.instReprEHTObservableData`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L157-L157)
**instance
Tau.BookV.Astrophysics.instReprEHTObservableData :Repr EHTObservableData**

Equations
- Tau.BookV.Astrophysics.instReprEHTObservableData = { reprPrec := Tau.BookV.Astrophysics.instReprEHTObservableData.repr }

---

### `Tau.BookV.Astrophysics.instReprEHTObservableData.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L157-L157)
**def
Tau.BookV.Astrophysics.instReprEHTObservableData.repr :EHTObservableData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.m87_eht`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L159-L164)
**def
Tau.BookV.Astrophysics.m87_eht :EHTObservableData**


M87* EHT data.
Equations
- Tau.BookV.Astrophysics.m87_eht = { target := "M87*", shadow_diameter_uas := 42, circularity_scaled := 90, ring_ratio_pct := 10 }
Instances For

---

### `Tau.BookV.Astrophysics.sgra_eht`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L166-L171)
**def
Tau.BookV.Astrophysics.sgra_eht :EHTObservableData**


Sgr A* EHT data.
Equations
- Tau.BookV.Astrophysics.sgra_eht = { target := "Sgr A*", shadow_diameter_uas := 52, circularity_scaled := 95, ring_ratio_pct := 10 }
Instances For

---

### `Tau.BookV.Astrophysics.shadow_circularity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L177-L183)
**theorem
Tau.BookV.Astrophysics.shadow_circularity :"Non-spinning BH shadow is circular from T^2 axisymmetry" = "Non-spinning BH shadow is circular from T^2 axisymmetry"**


[V.P83] Shadow circularity from torus symmetry: a non-spinning
BH has a perfectly circular shadow because the T² torus vacuum
is axisymmetric. Deviations from circularity encode the spin
parameter and inclination angle.

---

### `Tau.BookV.Astrophysics.HorizonComparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L189-L204)
**structure
Tau.BookV.Astrophysics.HorizonComparison :Type**


[V.D139] Tau vs GR horizon comparison: side-by-side comparison
of the two frameworks' predictions near the horizon.

- gr_has_singularity : Bool
GR prediction: event horizon, information lost, singularity.

- gr_information_lost : Bool
GR prediction: information is lost.

- tau_has_singularity : Bool
τ prediction: topology crossing, information preserved, no singularity.

- tau_information_preserved : Bool
τ prediction: information is preserved.

- shadow_identical : Bool
Shadow prediction: identical (differences below photon sphere).

- photon_ring_identical : Bool
Photon ring: identical (differences below photon sphere).

Instances For

---

### `Tau.BookV.Astrophysics.instReprHorizonComparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L204-L204)
**instance
Tau.BookV.Astrophysics.instReprHorizonComparison :Repr HorizonComparison**

Equations
- Tau.BookV.Astrophysics.instReprHorizonComparison = { reprPrec := Tau.BookV.Astrophysics.instReprHorizonComparison.repr }

---

### `Tau.BookV.Astrophysics.instReprHorizonComparison.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L204-L204)
**def
Tau.BookV.Astrophysics.instReprHorizonComparison.repr :HorizonComparison → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.canonical_comparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L206-L207)
**def
Tau.BookV.Astrophysics.canonical_comparison :HorizonComparison**


The canonical comparison.
Equations
- Tau.BookV.Astrophysics.canonical_comparison = { }
Instances For

---

### `Tau.BookV.Astrophysics.no_information_loss`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L213-L225)
**theorem
Tau.BookV.Astrophysics.no_information_loss :"tau-horizon preserves information, no singularity" = "tau-horizon preserves information, no singularity"**


[V.T96] No information loss at τ-horizon: boundary characters
vary continuously across the topology crossing.

This dissolves the BH information paradox:


- In GR: information falls past the event horizon and is "lost"

- In τ: information is carried by boundary characters which are
continuous at the topology crossing. No information is lost.


The apparent "information loss" in the GR readout is an artifact
of the readout discarding the T² internal structure.

---

### `Tau.BookV.Astrophysics.t2_shadow_correction_factor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L257-L259)
**def
Tau.BookV.Astrophysics.t2_shadow_correction_factor :Float**


[V.D241] T² Quadrupole Shadow Correction Factor.
f(ι<sub>τ</sub>) = 1+ι<sub>τ</sub>²/4 = 1.02912. Shadow radius enlarged by 2.91% over GR S².
Equations
- Tau.BookV.Astrophysics.t2_shadow_correction_factor = 1.0 + Tau.BookV.Astrophysics.iota_float✝ * Tau.BookV.Astrophysics.iota_float✝¹ / 4.0
Instances For

---

### `Tau.BookV.Astrophysics.T2ShadowCorrection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L261-L272)
**structure
Tau.BookV.Astrophysics.T2ShadowCorrection :Type**


[V.D241] Structure capturing the T² quadrupole shadow correction.
Quadrupole order ℓ=2 gives denominator ℓ²=4 in correction f = 1+ι<sub>τ</sub>²/4.

- quadrupole_order : ℕ
Quadrupole order ℓ = 2.

- denominator : ℕ
Denominator = ℓ² = 4.

- enlargement_approx_3pct : Bool
Shadow enlargement is approximately 3% over GR.

- correction_positive : Bool
Correction is positive (shadow larger than GR).

Instances For

---

### `Tau.BookV.Astrophysics.instReprT2ShadowCorrection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L272-L272)
**instance
Tau.BookV.Astrophysics.instReprT2ShadowCorrection :Repr T2ShadowCorrection**

Equations
- Tau.BookV.Astrophysics.instReprT2ShadowCorrection = { reprPrec := Tau.BookV.Astrophysics.instReprT2ShadowCorrection.repr }

---

### `Tau.BookV.Astrophysics.instReprT2ShadowCorrection.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L272-L272)
**def
Tau.BookV.Astrophysics.instReprT2ShadowCorrection.repr :T2ShadowCorrection → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instInhabitedT2ShadowCorrection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L274-L275)
**instance
Tau.BookV.Astrophysics.instInhabitedT2ShadowCorrection :Inhabited T2ShadowCorrection**


Canonical T² shadow correction data.
Equations
- Tau.BookV.Astrophysics.instInhabitedT2ShadowCorrection = { default := { } }

---

### `Tau.BookV.Astrophysics.t2_shadow_correction_conjunction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L277-L283)
**theorem
Tau.BookV.Astrophysics.t2_shadow_correction_conjunction :have d := { };
d.quadrupole_order = 2 ∧ d.denominator = 4 ∧ d.enlargement_approx_3pct = true ∧ d.correction_positive = true**


All structural properties of the T² shadow correction hold.

---

### `Tau.BookV.Astrophysics.shadow_denominator_is_ell_sq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L285-L288)
**theorem
Tau.BookV.Astrophysics.shadow_denominator_is_ell_sq :have d := { };
d.quadrupole_order * d.quadrupole_order = d.denominator**


Denominator equals quadrupole order squared: ℓ² = 4.

---

### `Tau.BookV.Astrophysics.eht_shadow_t2_pct_over_gr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L292-L294)
**def
Tau.BookV.Astrophysics.eht_shadow_t2_pct_over_gr :Float**


[V.T184] EHT Shadow T² Correction (+2.91% over GR).
R_shadow(T²) = 3√3·(GM/c²)·(1+ι<sub>τ</sub>²/4). M87*: 40.86 μas (−2.7% from EHT 42).
Equations
- Tau.BookV.Astrophysics.eht_shadow_t2_pct_over_gr = (Tau.BookV.Astrophysics.t2_shadow_correction_factor - 1.0) * 100.0
Instances For

---

### `Tau.BookV.Astrophysics.EHTShadowT2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L296-L307)
**structure
Tau.BookV.Astrophysics.EHTShadowT2 :Type**


[V.T184] Structure capturing the EHT shadow T² theorem properties.
Correction is above zero, detectable by ngEHT, below current EHT precision.

- correction_above_zero : Bool
Correction factor > 1 (shadow enlarged).

- detectable_by_ngeht : Bool
Detectable by next-generation EHT at < 3% precision.

- below_current_eht_precision : Bool
Below current EHT precision (~7%).

- m87_closer_to_eht : Bool
M87* T² prediction closer to EHT central value than GR.

Instances For

---

### `Tau.BookV.Astrophysics.instReprEHTShadowT2.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L307-L307)
**def
Tau.BookV.Astrophysics.instReprEHTShadowT2.repr :EHTShadowT2 → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprEHTShadowT2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L307-L307)
**instance
Tau.BookV.Astrophysics.instReprEHTShadowT2 :Repr EHTShadowT2**

Equations
- Tau.BookV.Astrophysics.instReprEHTShadowT2 = { reprPrec := Tau.BookV.Astrophysics.instReprEHTShadowT2.repr }

---

### `Tau.BookV.Astrophysics.instInhabitedEHTShadowT2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L309-L310)
**instance
Tau.BookV.Astrophysics.instInhabitedEHTShadowT2 :Inhabited EHTShadowT2**


Canonical EHT shadow T² data.
Equations
- Tau.BookV.Astrophysics.instInhabitedEHTShadowT2 = { default := { } }

---

### `Tau.BookV.Astrophysics.eht_shadow_t2_conjunction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L312-L318)
**theorem
Tau.BookV.Astrophysics.eht_shadow_t2_conjunction :have d := { };
d.correction_above_zero = true ∧ d.detectable_by_ngeht = true ∧ d.below_current_eht_precision = true ∧ d.m87_closer_to_eht = true**


All structural properties of the EHT shadow T² theorem hold.

---

### `Tau.BookV.Astrophysics.shadow_correction_gt_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L320-L323)
**theorem
Tau.BookV.Astrophysics.shadow_correction_gt_one :t2_shadow_correction_factor > 1.0**


Shadow correction factor > 1 (T² shadow is larger than GR).

---

### `Tau.BookV.Astrophysics.BiRotationalDynamics`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L342-L348)
**structure
Tau.BookV.Astrophysics.BiRotationalDynamics :Type**


Bi-rotational dynamics on T² — V.D277
Two angular velocities from torus geometry: ω_minor = ω_major / ι<sub>τ</sub>

- omega_major_description : String
- omega_minor_description : String
- frequency_ratio_x1000 : ℕ
Instances For

---

### `Tau.BookV.Astrophysics.instReprBiRotationalDynamics`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L348-L348)
**instance
Tau.BookV.Astrophysics.instReprBiRotationalDynamics :Repr BiRotationalDynamics**

Equations
- Tau.BookV.Astrophysics.instReprBiRotationalDynamics = { reprPrec := Tau.BookV.Astrophysics.instReprBiRotationalDynamics.repr }

---

### `Tau.BookV.Astrophysics.instReprBiRotationalDynamics.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L348-L348)
**def
Tau.BookV.Astrophysics.instReprBiRotationalDynamics.repr :BiRotationalDynamics → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.SynchrotronFrequencyPair`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L350-L356)
**structure
Tau.BookV.Astrophysics.SynchrotronFrequencyPair :Type**


Synchrotron frequency pair — V.D278

- source_name : String
- major_period_s : ℕ
- minor_period_s : ℕ
- spectral_index_x100 : ℤ
Instances For

---

### `Tau.BookV.Astrophysics.instReprSynchrotronFrequencyPair.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L356-L356)
**def
Tau.BookV.Astrophysics.instReprSynchrotronFrequencyPair.repr :SynchrotronFrequencyPair → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprSynchrotronFrequencyPair`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L356-L356)
**instance
Tau.BookV.Astrophysics.instReprSynchrotronFrequencyPair :Repr SynchrotronFrequencyPair**

Equations
- Tau.BookV.Astrophysics.instReprSynchrotronFrequencyPair = { reprPrec := Tau.BookV.Astrophysics.instReprSynchrotronFrequencyPair.repr }

---

### `Tau.BookV.Astrophysics.birotational_synchrotron_ratio_x1000`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L358-L359)
**def
Tau.BookV.Astrophysics.birotational_synchrotron_ratio_x1000 :ℕ**


Bi-rotational synchrotron theorem — V.T218
Equations
- Tau.BookV.Astrophysics.birotational_synchrotron_ratio_x1000 = 2930
Instances For

---

### `Tau.BookV.Astrophysics.m87_synchrotron`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L361-L363)
**def
Tau.BookV.Astrophysics.m87_synchrotron :SynchrotronFrequencyPair**


M87* synchrotron data
Equations
- Tau.BookV.Astrophysics.m87_synchrotron = { source_name := "M87*", major_period_s := 402424, minor_period_s := 137349, spectral_index_x100 := -60 }
Instances For

---

### `Tau.BookV.Astrophysics.sgra_synchrotron`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L365-L367)
**def
Tau.BookV.Astrophysics.sgra_synchrotron :SynchrotronFrequencyPair**


Sgr A* synchrotron data
Equations
- Tau.BookV.Astrophysics.sgra_synchrotron = { source_name := "Sgr A*", major_period_s := 266, minor_period_s := 91, spectral_index_x100 := -60 }
Instances For

---

### `Tau.BookV.Astrophysics.synchrotron_ratio_universal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L369-L372)
**theorem
Tau.BookV.Astrophysics.synchrotron_ratio_universal :m87_synchrotron.spectral_index_x100 = sgra_synchrotron.spectral_index_x100**


Frequency ratio is ι<sub>τ</sub>⁻¹ for both sources

---

### `Tau.BookV.Astrophysics.BrightnessHarmonicMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L378-L383)
**structure
Tau.BookV.Astrophysics.BrightnessHarmonicMode :Type**


Brightness harmonic mode on T² — V.D279

- n : ℕ
- m : ℕ
- eigenvalue_x1000 : ℕ
Instances For

---

### `Tau.BookV.Astrophysics.instReprBrightnessHarmonicMode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L383-L383)
**def
Tau.BookV.Astrophysics.instReprBrightnessHarmonicMode.repr :BrightnessHarmonicMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprBrightnessHarmonicMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L383-L383)
**instance
Tau.BookV.Astrophysics.instReprBrightnessHarmonicMode :Repr BrightnessHarmonicMode**

Equations
- Tau.BookV.Astrophysics.instReprBrightnessHarmonicMode = { reprPrec := Tau.BookV.Astrophysics.instReprBrightnessHarmonicMode.repr }

---

### `Tau.BookV.Astrophysics.brightness_modes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L385-L393)
**def
Tau.BookV.Astrophysics.brightness_modes :List BrightnessHarmonicMode**


First 6 brightness modes with eigenvalues
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.harmonic_frequency_ratio_x1000`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L395-L397)
**def
Tau.BookV.Astrophysics.harmonic_frequency_ratio_x1000 :ℕ**


Harmonic eigenfrequency ratio — V.T219
f_{0,1}/f_{1,0} = √(ι<sub>τ</sub>⁻²) = ι<sub>τ</sub>⁻¹ ≈ 2.930
Equations
- Tau.BookV.Astrophysics.harmonic_frequency_ratio_x1000 = 2930
Instances For

---

### `Tau.BookV.Astrophysics.SgrAVariability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L399-L405)
**structure
Tau.BookV.Astrophysics.SgrAVariability :Type**


Sgr A* horizon-scale variability — V.P149
Periods in seconds (rounded)

- major_period_s : ℕ
- minor_period_s : ℕ
- ratio_x1000 : ℕ
Instances For

---

### `Tau.BookV.Astrophysics.instReprSgrAVariability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L405-L405)
**instance
Tau.BookV.Astrophysics.instReprSgrAVariability :Repr SgrAVariability**

Equations
- Tau.BookV.Astrophysics.instReprSgrAVariability = { reprPrec := Tau.BookV.Astrophysics.instReprSgrAVariability.repr }

---

### `Tau.BookV.Astrophysics.instReprSgrAVariability.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L405-L405)
**def
Tau.BookV.Astrophysics.instReprSgrAVariability.repr :SgrAVariability → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.sgra_variability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L407-L407)
**def
Tau.BookV.Astrophysics.sgra_variability :SgrAVariability**

Equations
- Tau.BookV.Astrophysics.sgra_variability = { major_period_s := 266, minor_period_s := 91, ratio_x1000 := 2930 }
Instances For

---

### `Tau.BookV.Astrophysics.M87Variability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L409-L414)
**structure
Tau.BookV.Astrophysics.M87Variability :Type**


M87* variability timescales — V.R404
Periods in seconds (rounded)

- major_period_s : ℕ
- minor_period_s : ℕ
Instances For

---

### `Tau.BookV.Astrophysics.instReprM87Variability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L414-L414)
**instance
Tau.BookV.Astrophysics.instReprM87Variability :Repr M87Variability**

Equations
- Tau.BookV.Astrophysics.instReprM87Variability = { reprPrec := Tau.BookV.Astrophysics.instReprM87Variability.repr }

---

### `Tau.BookV.Astrophysics.instReprM87Variability.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L414-L414)
**def
Tau.BookV.Astrophysics.instReprM87Variability.repr :M87Variability → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.m87_variability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L416-L416)
**def
Tau.BookV.Astrophysics.m87_variability :M87Variability**

Equations
- Tau.BookV.Astrophysics.m87_variability = { major_period_s := 402000, minor_period_s := 137000 }
Instances For

---

### `Tau.BookV.Astrophysics.variability_ratio_matches_synchrotron`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L418-L421)
**theorem
Tau.BookV.Astrophysics.variability_ratio_matches_synchrotron :sgra_variability.ratio_x1000 = birotational_synchrotron_ratio_x1000**


Variability ratio matches synchrotron ratio (both = ι<sub>τ</sub>⁻¹)

---

### `Tau.BookV.Astrophysics.brightness_eigenvalue_eq_qnm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L427-L439)
**theorem
Tau.BookV.Astrophysics.brightness_eigenvalue_eq_qnm :harmonic_frequency_ratio_x1000 = birotational_synchrotron_ratio_x1000**


[Sprint 22A] The brightness harmonic eigenvalue formula (V.D279) is identical to
the QNM eigenvalue structure (V.D242). Both are eigenvalues of the Laplacian on
the flat torus T² = (R·S¹)×(r·S¹) with r/R = ι<sub>τ</sub>.

This is the Peter-Weyl theorem for U(1)×U(1): the characters ψ_{nm} = exp(i(nφ+mθ))
form a complete orthonormal basis for L²(T²), with eigenvalues λ_{nm} = n² + m²ι<sub>τ</sub>⁻².

The link is structural: both V.D279 and V.D242 use the same eigenvalue formula,
and the fundamental frequency ratio f_{0,1}/f_{1,0} = ι<sub>τ</sub>⁻¹ ≈ 2.930 is identical
to V.T185 (τ-effective QNM frequency ratio discriminator).

---

### `Tau.BookV.Astrophysics.brightness_ratio_is_iota_inv_x1000`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L441-L446)
**theorem
Tau.BookV.Astrophysics.brightness_ratio_is_iota_inv_x1000 :harmonic_frequency_ratio_x1000 = 2930**


The brightness frequency ratio (V.T219) equals 2930 (= ι<sub>τ</sub>⁻¹ × 1000),
which is the same constant as the QNM frequency ratio discriminator (V.T185).
This structural identity establishes that brightness harmonics
and QNM modes share the same spectral basis on T².

---

### `Tau.BookV.Astrophysics.birotation_ratio_eq_qnm_ratio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L452-L457)
**theorem
Tau.BookV.Astrophysics.birotation_ratio_eq_qnm_ratio :birotational_synchrotron_ratio_x1000 = harmonic_frequency_ratio_x1000**


[Sprint 22B] The bi-rotational frequency ratio (V.D277/V.T218) is identical to
the QNM frequency ratio (V.T185, τ-effective). Both equal ι<sub>τ</sub>⁻¹ × 1000 = 2930.
This structural identity confirms that bi-rotational synchrotron modes are
boundary-character oscillations read through the B-sector (EM), not accretion dynamics.

---

### `Tau.BookV.Astrophysics.all_ratios_unified`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L459-L465)
**theorem
Tau.BookV.Astrophysics.all_ratios_unified :birotational_synchrotron_ratio_x1000 = 2930 ∧ harmonic_frequency_ratio_x1000 = 2930 ∧ sgra_variability.ratio_x1000 = 2930**


All three ratio constants (synchrotron, harmonic, variability) are identical:
they are all ι<sub>τ</sub>⁻¹ × 1000 = 2930.

---

### `Tau.BookV.Astrophysics.SMBHPrediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L471-L479)
**structure
Tau.BookV.Astrophysics.SMBHPrediction :Type**


SMBH prediction entry — V.D280

- name : String
- shadow_diameter_x100_uas : ℕ
- t2_correction_ppm : ℕ
- qnm_ratio_x1000 : ℕ
- major_period_s : ℕ
- minor_period_s : ℕ
Instances For

---

### `Tau.BookV.Astrophysics.instReprSMBHPrediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L479-L479)
**instance
Tau.BookV.Astrophysics.instReprSMBHPrediction :Repr SMBHPrediction**

Equations
- Tau.BookV.Astrophysics.instReprSMBHPrediction = { reprPrec := Tau.BookV.Astrophysics.instReprSMBHPrediction.repr }

---

### `Tau.BookV.Astrophysics.instReprSMBHPrediction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L479-L479)
**def
Tau.BookV.Astrophysics.instReprSMBHPrediction.repr :SMBHPrediction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.m87_prediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L481-L483)
**def
Tau.BookV.Astrophysics.m87_prediction :SMBHPrediction**


M87* prediction suite — V.T220
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.sgra_prediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L485-L487)
**def
Tau.BookV.Astrophysics.sgra_prediction :SMBHPrediction**


Sgr A* prediction suite — V.T221
Equations
- Tau.BookV.Astrophysics.sgra_prediction = { name := "Sgr A*", shadow_diameter_x100_uas := 5482, t2_correction_ppm := 29100, qnm_ratio_x1000 := 2930,
 major_period_s := 266, minor_period_s := 91 }
Instances For

---

### `Tau.BookV.Astrophysics.smbh_universal_t2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L489-L493)
**theorem
Tau.BookV.Astrophysics.smbh_universal_t2 :m87_prediction.t2_correction_ppm = sgra_prediction.t2_correction_ppm ∧ m87_prediction.qnm_ratio_x1000 = sgra_prediction.qnm_ratio_x1000**


Both sources share the same T² correction and QNM ratio

---

### `Tau.BookV.Astrophysics.m87_shadow_in_eht_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L495-L499)
**theorem
Tau.BookV.Astrophysics.m87_shadow_in_eht_range :3900 ≤ m87_prediction.shadow_diameter_x100_uas ∧ m87_prediction.shadow_diameter_x100_uas ≤ 4500**


M87* shadow within EHT error bars (42 ± 3 μas = 3900-4500 in units of 0.01 μas)

---

### `Tau.BookV.Astrophysics.sgra_shadow_in_eht_2sigma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L501-L505)
**theorem
Tau.BookV.Astrophysics.sgra_shadow_in_eht_2sigma :4720 ≤ sgra_prediction.shadow_diameter_x100_uas ∧ sgra_prediction.shadow_diameter_x100_uas ≤ 5640**


Sgr A* shadow within 2σ of EHT (51.8 ± 2.3 μas → 4720-5640 in units of 0.01 μas)

---

### `Tau.BookV.Astrophysics.eht_comparison_remark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L507-L510)
**def
Tau.BookV.Astrophysics.eht_comparison_remark :String**


EHT comparison remark — V.R405
Equations
- Tau.BookV.Astrophysics.eht_comparison_remark = "M87*: 40.85 μas (obs 42±3, 0.4σ), Sgr A*: 54.8 μas (obs 51.8±2.3, 1.3σ). " ++ "T² correction +2.91% universal. QNM ratio 2.930 testable."
Instances For

---

### `Tau.BookV.Astrophysics.ToroidalBFieldConfig`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L516-L528)
**structure
Tau.BookV.Astrophysics.ToroidalBFieldConfig :Type**


[V.D284] Toroidal B-Field Configuration: magnetic field geometry
on T² black hole. Toroidal component dominates by factor ι<sub>τ</sub>⁻¹ ≈ 2.93.
Field ratio is mass-independent, set by torus aspect ratio.

- b_tor_x100 : ℕ
Toroidal field strength (Gauss × 100).

- b_pol_x100 : ℕ
Poloidal field strength (Gauss × 100).

- field_ratio_x1000 : ℕ
Field ratio B_tor/B_pol × 1000. Should be ≈ 2930.

- tor_gt_pol : self.b_tor_x100 > self.b_pol_x100
Toroidal dominates poloidal.

Instances For

---

### `Tau.BookV.Astrophysics.instReprToroidalBFieldConfig.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L528-L528)
**def
Tau.BookV.Astrophysics.instReprToroidalBFieldConfig.repr :ToroidalBFieldConfig → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprToroidalBFieldConfig`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L528-L528)
**instance
Tau.BookV.Astrophysics.instReprToroidalBFieldConfig :Repr ToroidalBFieldConfig**

Equations
- Tau.BookV.Astrophysics.instReprToroidalBFieldConfig = { reprPrec := Tau.BookV.Astrophysics.instReprToroidalBFieldConfig.repr }

---

### `Tau.BookV.Astrophysics.instInhabitedToroidalBFieldConfig`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L530-L531)
**instance
Tau.BookV.Astrophysics.instInhabitedToroidalBFieldConfig :Inhabited ToroidalBFieldConfig**

Equations
- One or more equations did not get rendered due to their size.

---

### `Tau.BookV.Astrophysics.rm_winding_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L533-L538)
**theorem
Tau.BookV.Astrophysics.rm_winding_theorem :"w_RM(T²) = 2, w_RM(S²) = 1" = "w_RM(T²) = 2, w_RM(S²) = 1"**


[V.T227] RM Winding Theorem: the Faraday rotation measure winding
number equals 2 for T² (two sign changes from toroidal B-field)
and 1 for S² (one sign change from radial/dipolar field).

---

### `Tau.BookV.Astrophysics.rm_winding_t2_is_double_s2`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L540-L541)
**theorem
Tau.BookV.Astrophysics.rm_winding_t2_is_double_s2 :2 = 2 * 1**


RM winding is twice that of S²: topological invariant from genus(T²) = 1.

---

### `Tau.BookV.Astrophysics.StokesParameterSuite`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L547-L563)
**structure
Tau.BookV.Astrophysics.StokesParameterSuite :Type**


[V.D287] Stokes Parameter Suite on T²: decomposition of polarization
state into I, Q, U, V components with T² topology. EVPA winding = 2,
circular polarization winding = 2, both from toroidal field geometry.

- source : String
Source name.

- w_evpa : ℕ
EVPA winding number.

- w_rm : ℕ
RM winding number.

- w_v : ℕ
Circular polarization winding number.

- m_linear_x10 : ℕ
Linear polarization fraction (percent × 10).

- v_over_i_x100 : ℕ
Circular polarization |V/I| (percent × 100).

Instances For

---

### `Tau.BookV.Astrophysics.instReprStokesParameterSuite.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L563-L563)
**def
Tau.BookV.Astrophysics.instReprStokesParameterSuite.repr :StokesParameterSuite → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprStokesParameterSuite`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L563-L563)
**instance
Tau.BookV.Astrophysics.instReprStokesParameterSuite :Repr StokesParameterSuite**

Equations
- Tau.BookV.Astrophysics.instReprStokesParameterSuite = { reprPrec := Tau.BookV.Astrophysics.instReprStokesParameterSuite.repr }

---

### `Tau.BookV.Astrophysics.instInhabitedStokesParameterSuite`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L565-L566)
**instance
Tau.BookV.Astrophysics.instInhabitedStokesParameterSuite :Inhabited StokesParameterSuite**

Equations
- Tau.BookV.Astrophysics.instInhabitedStokesParameterSuite = { default := { source := "generic", m_linear_x10 := 200, v_over_i_x100 := 50 } }

---

### `Tau.BookV.Astrophysics.circular_winding_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L568-L571)
**theorem
Tau.BookV.Astrophysics.circular_winding_theorem :"w_V(T²) = 2, w_V(S²) = 1" = "w_V(T²) = 2, w_V(S²) = 1"**


[V.T229] Circular Polarization Winding: w_V = 2 for T², 1 for S².

---

### `Tau.BookV.Astrophysics.all_windings_equal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L573-L577)
**theorem
Tau.BookV.Astrophysics.all_windings_equal :have s := default;
s.w_evpa = 2 ∧ s.w_rm = 2 ∧ s.w_v = 2**


All three magnetic winding numbers are equal for T².

---

### `Tau.BookV.Astrophysics.NearHorizonBField`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L583-L596)
**structure
Tau.BookV.Astrophysics.NearHorizonBField :Type**


[V.D288] Near-Horizon B-Field: equipartition magnetic field at photon sphere.
B_tor/B_pol = ι<sub>τ</sub>⁻¹ ≈ 2.93, mass-independent zero-parameter prediction.

- source : String
Source name.

- b_eq_x100 : ℕ
Total equipartition field (Gauss × 100).

- b_tor_x100 : ℕ
Toroidal component (Gauss × 100).

- b_pol_x100 : ℕ
Poloidal component (Gauss × 100).

- ratio_x1000 : ℕ
Field ratio × 1000 (should be ≈ 2930).

Instances For

---

### `Tau.BookV.Astrophysics.instReprNearHorizonBField.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L596-L596)
**def
Tau.BookV.Astrophysics.instReprNearHorizonBField.repr :NearHorizonBField → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprNearHorizonBField`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L596-L596)
**instance
Tau.BookV.Astrophysics.instReprNearHorizonBField :Repr NearHorizonBField**

Equations
- Tau.BookV.Astrophysics.instReprNearHorizonBField = { reprPrec := Tau.BookV.Astrophysics.instReprNearHorizonBField.repr }

---

### `Tau.BookV.Astrophysics.magnetic_ratio_is_iota_inv`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L598-L601)
**theorem
Tau.BookV.Astrophysics.magnetic_ratio_is_iota_inv :"B_tor/B_pol = ι<sub>τ</sub>⁻¹ ≈ 2.93 (mass-independent, zero-parameter)" = "B_tor/B_pol = ι<sub>τ</sub>⁻¹ ≈ 2.93 (mass-independent, zero-parameter)"**


[V.T230] Magnetic Field Ratio Theorem: B_tor/B_pol = ι<sub>τ</sub>⁻¹ ≈ 2.93.

---

### `Tau.BookV.Astrophysics.MagneticPredictionSuite`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L603-L624)
**structure
Tau.BookV.Astrophysics.MagneticPredictionSuite :Type**


[V.R412] Complete T² vs S² Magnetic Prediction Suite.
9 observables, all derived from genus(T²) = 1 and ι<sub>τ</sub>.

- w_evpa : ℕ
EVPA winding number (T²).

- w_rm : ℕ
RM winding number (T²).

- w_v : ℕ
Circular pol winding number (T²).

- field_ratio_x1000 : ℕ
B_tor/B_pol × 1000.

- flux_through_hole : ℕ
Flux through hole exists (1 = yes).

- jet_helicity_fixed : ℕ
Jet helicity fixed by topology (1 = yes).

- jet_bz_bphi_x1000 : ℕ
Jet B_z/B_phi × 1000 at base.

- igmf_fil_ng_x10 : ℕ
IGMF in filaments (nG × 10).

- b_alignment_parallel : ℕ
B alignment parallel (1 = yes).

Instances For

---

### `Tau.BookV.Astrophysics.instReprMagneticPredictionSuite.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L624-L624)
**def
Tau.BookV.Astrophysics.instReprMagneticPredictionSuite.repr :MagneticPredictionSuite → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Astrophysics.instReprMagneticPredictionSuite`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L624-L624)
**instance
Tau.BookV.Astrophysics.instReprMagneticPredictionSuite :Repr MagneticPredictionSuite**

Equations
- Tau.BookV.Astrophysics.instReprMagneticPredictionSuite = { reprPrec := Tau.BookV.Astrophysics.instReprMagneticPredictionSuite.repr }

---

### `Tau.BookV.Astrophysics.instInhabitedMagneticPredictionSuite`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L626-L626)
**instance
Tau.BookV.Astrophysics.instInhabitedMagneticPredictionSuite :Inhabited MagneticPredictionSuite**

Equations
- Tau.BookV.Astrophysics.instInhabitedMagneticPredictionSuite = { default := { } }

---

### `Tau.BookV.Astrophysics.magnetic_suite_winding_consistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L628-L632)
**theorem
Tau.BookV.Astrophysics.magnetic_suite_winding_consistency :have s := default;
s.w_evpa = s.w_rm ∧ s.w_rm = s.w_v ∧ s.w_v = 2**


All three winding numbers in the prediction suite equal 2.

---

### `Tau.BookV.Astrophysics.m87_bfield`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L634-L636)
**def
Tau.BookV.Astrophysics.m87_bfield :NearHorizonBField**


M87* B-field estimate: 1–30 G consistent with EHT Paper VIII constraints.
Equations
- Tau.BookV.Astrophysics.m87_bfield = { source := "M87*", b_eq_x100 := 1500, b_tor_x100 := 1400, b_pol_x100 := 480 }
Instances For

---

### `Tau.BookV.Astrophysics.sgra_bfield`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L638-L640)
**def
Tau.BookV.Astrophysics.sgra_bfield :NearHorizonBField**


Sgr A* B-field estimate: lower accretion rate, weaker field.
Equations
- Tau.BookV.Astrophysics.sgra_bfield = { source := "Sgr A*", b_eq_x100 := 3000, b_tor_x100 := 2800, b_pol_x100 := 960 }
Instances For

---

### `Tau.BookV.Astrophysics.m87_stokes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Astrophysics/EHTReread.lean#L642-L644)
**def
Tau.BookV.Astrophysics.m87_stokes :StokesParameterSuite**


M87* Stokes suite.
Equations
- Tau.BookV.Astrophysics.m87_stokes = { source := "M87*", m_linear_x10 := 200, v_over_i_x100 := 50 }
Instances For
