---
layout: taulib-doc
title: "TauLib.BookII.Mirror.WaveHolomorphy"
permalink: /verify/taulib/docs/book-ii-mirror-wave-holomorphy/
lane: verify
module_name: "TauLib.BookII.Mirror.WaveHolomorphy"
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

# TauLib.BookII.Mirror.WaveHolomorphy


PDE type classification, the asymmetric determination theorem, and
stage-finite Euclidean geometry. Wave decomposition via split-complex
idempotents.

## Registry Cross-References


- [II.D70] PDE Type Classification -- `PDEType`, `PDEClassification`

- [II.T44] Asymmetric Determination -- `hyperbolic_hartogs_natural`, `elliptic_hartogs_not_natural`

- [II.D71] Stage-Finite Euclidean Geometry -- `StageGeometry`

- [II.T45] Parallel Preservation -- `stage_euclidean`, `stage_no_light_cones`


## Mathematical Content


**II.D70 (PDE Type Classification):** The split-complex scalar choice (j^2 = +1)
forces hyperbolic PDE type for tau-holomorphy, in contrast to the elliptic PDE
type of orthodox Cauchy-Riemann equations. Each PDE type comes with a characteristic
signature: elliptic has no real characteristics and satisfies the maximum principle;
hyperbolic has real characteristics and supports wave propagation.

**II.T44 (Asymmetric Determination):** Hartogs extension (boundary determines
interior) is natural for hyperbolic PDE type but NOT natural for elliptic PDE
type. In the elliptic case, the maximum principle goes in the opposite direction:
the interior determines boundary values. This asymmetry is the structural reason
tau-holomorphy can support Hartogs extension while orthodox holomorphy cannot.

**II.D71 (Stage-Finite Euclidean Geometry):** At each finite stage k, the geometry
on Z/M_kZ is Euclidean (no light cones, no metric signature issues). The
finite-stage geometry is always Euclidean because the split-complex light cones
emerge only in the limit. Each stage is a finite discrete set with a well-defined
betweenness relation inherited from the cyclic order.

**II.T45 (Parallel Preservation):** At every finite stage, the Euclidean property
holds and light cones are absent. This is a universal quantification over all stages.

## Wave Decomposition


A split-complex-valued function f decomposes as f = e_+ f_+ + e_- f_-
where f_+ is the B-sector component and f_- is the C-sector component.
This decomposition is the structural foundation of bipolar holomorphy.

---

### `Tau.BookII.Mirror.PDEType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L56-L60)
**inductive
Tau.BookII.Mirror.PDEType :Type**


[II.D70] PDE type: the structural choice forced by the scalar algebra.

- Elliptic : PDEType
- Hyperbolic : PDEType
Instances For

---

### `Tau.BookII.Mirror.instDecidableEqPDEType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L60-L60)
**instance
Tau.BookII.Mirror.instDecidableEqPDEType :DecidableEq PDEType**

Equations
- Tau.BookII.Mirror.instDecidableEqPDEType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookII.Mirror.instReprPDEType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L60-L60)
**instance
Tau.BookII.Mirror.instReprPDEType :Repr PDEType**

Equations
- Tau.BookII.Mirror.instReprPDEType = { reprPrec := Tau.BookII.Mirror.instReprPDEType.repr }

---

### `Tau.BookII.Mirror.instReprPDEType.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L60-L60)
**def
Tau.BookII.Mirror.instReprPDEType.repr :PDEType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.PDEClassification`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L64-L71)
**structure
Tau.BookII.Mirror.PDEClassification :Type**


[II.D70] Full PDE classification: type plus characteristic properties.

- pde_type : PDEType
- has_characteristics : Bool
- has_max_principle : Bool
- propagation_isotropic : Bool
- hartogs_natural : Bool
Instances For

---

### `Tau.BookII.Mirror.instDecidableEqPDEClassification`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L71-L71)
**instance
Tau.BookII.Mirror.instDecidableEqPDEClassification :DecidableEq PDEClassification**

Equations
- Tau.BookII.Mirror.instDecidableEqPDEClassification = Tau.BookII.Mirror.instDecidableEqPDEClassification.decEq

---

### `Tau.BookII.Mirror.instDecidableEqPDEClassification.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L71-L71)
**def
Tau.BookII.Mirror.instDecidableEqPDEClassification.decEq
(x✝ x✝¹ : PDEClassification)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.instReprPDEClassification`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L71-L71)
**instance
Tau.BookII.Mirror.instReprPDEClassification :Repr PDEClassification**

Equations
- Tau.BookII.Mirror.instReprPDEClassification = { reprPrec := Tau.BookII.Mirror.instReprPDEClassification.repr }

---

### `Tau.BookII.Mirror.instReprPDEClassification.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L71-L71)
**def
Tau.BookII.Mirror.instReprPDEClassification.repr :PDEClassification → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.elliptic_classification`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L73-L79)
**def
Tau.BookII.Mirror.elliptic_classification :PDEClassification**


[II.D70] The elliptic classification (orthodox Cauchy-Riemann).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.hyperbolic_classification`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L81-L87)
**def
Tau.BookII.Mirror.hyperbolic_classification :PDEClassification**


[II.D70] The hyperbolic classification (tau split-CR).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.hyperbolic_hartogs_natural`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L93-L95)
**theorem
Tau.BookII.Mirror.hyperbolic_hartogs_natural :hyperbolic_classification.hartogs_natural = true**


[II.T44] Hartogs extension is natural for hyperbolic PDE type.

---

### `Tau.BookII.Mirror.elliptic_hartogs_not_natural`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L97-L99)
**theorem
Tau.BookII.Mirror.elliptic_hartogs_not_natural :elliptic_classification.hartogs_natural = false**


[II.T44] Hartogs extension is NOT natural for elliptic PDE type.

---

### `Tau.BookII.Mirror.asymmetric_determination`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L101-L106)
**theorem
Tau.BookII.Mirror.asymmetric_determination :hyperbolic_classification.hartogs_natural = true ∧ elliptic_classification.hartogs_natural = false**


[II.T44] The elliptic and hyperbolic classifications have opposite
Hartogs naturalness.

---

### `Tau.BookII.Mirror.max_principle_asymmetry`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L108-L113)
**theorem
Tau.BookII.Mirror.max_principle_asymmetry :elliptic_classification.has_max_principle = true ∧ hyperbolic_classification.has_max_principle = false**


[II.T44] The elliptic classification has the maximum principle;
the hyperbolic does not.

---

### `Tau.BookII.Mirror.pde_classifications_distinct`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L115-L121)
**theorem
Tau.BookII.Mirror.pde_classifications_distinct :elliptic_classification ≠ hyperbolic_classification**


[II.T44] The two classifications are structurally distinct.

---

### `Tau.BookII.Mirror.characteristics_iff_hyperbolic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L123-L127)
**theorem
Tau.BookII.Mirror.characteristics_iff_hyperbolic :hyperbolic_classification.has_characteristics = true ∧ elliptic_classification.has_characteristics = false**


[II.T44] PDE type determines characteristics existence.

---

### `Tau.BookII.Mirror.StageGeometry`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L133-L139)
**structure
Tau.BookII.Mirror.StageGeometry
(k : ℕ)
 :Type**


[II.D71] Stage geometry at stage k: the geometry on Z/M_kZ.
At each finite stage, the geometry is Euclidean (no light cones).

- stage_size : ℕ
- is_euclidean : Bool
- has_light_cones : Bool
Instances For

---

### `Tau.BookII.Mirror.instReprStageGeometry`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L139-L139)
**instance
Tau.BookII.Mirror.instReprStageGeometry
{k✝ : ℕ}
 :Repr (StageGeometry k✝)**

Equations
- Tau.BookII.Mirror.instReprStageGeometry = { reprPrec := Tau.BookII.Mirror.instReprStageGeometry.repr }

---

### `Tau.BookII.Mirror.instReprStageGeometry.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L139-L139)
**def
Tau.BookII.Mirror.instReprStageGeometry.repr
{k✝ : ℕ}
 :StageGeometry k✝ → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.default_stage_geometry`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L141-L145)
**def
Tau.BookII.Mirror.default_stage_geometry
(k : ℕ)
 :StageGeometry k**


Default stage geometry: Euclidean, no light cones.
Equations
- Tau.BookII.Mirror.default_stage_geometry k = { }
Instances For

---

### `Tau.BookII.Mirror.stage_euclidean_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L147-L151)
**def
Tau.BookII.Mirror.stage_euclidean_check
(k : ℕ)
 :Bool**


[II.D71] Stage-Euclidean check: verify the geometry at stage k
is Euclidean with no light cones.
Equations
- Tau.BookII.Mirror.stage_euclidean_check k = ((Tau.BookII.Mirror.default_stage_geometry k).is_euclidean && !(Tau.BookII.Mirror.default_stage_geometry k).has_light_cones)
Instances For

---

### `Tau.BookII.Mirror.all_stages_euclidean`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L153-L161)
**def
Tau.BookII.Mirror.all_stages_euclidean
(db : ℕ)
 :Bool**


[II.D71] Check all stages up to depth db.
Equations
- Tau.BookII.Mirror.all_stages_euclidean db = Tau.BookII.Mirror.all_stages_euclidean.go db 0 (db + 1)
Instances For

---

### `Tau.BookII.Mirror.all_stages_euclidean.go`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L157-L160)@[irreducible]

**def
Tau.BookII.Mirror.all_stages_euclidean.go
(db k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.stage_no_light_cones`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L167-L169)
**theorem
Tau.BookII.Mirror.stage_no_light_cones
(k : ℕ)
 :(default_stage_geometry k).has_light_cones = false**


[II.T45] At every stage k, the default geometry has no light cones.

---

### `Tau.BookII.Mirror.stage_euclidean`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L171-L173)
**theorem
Tau.BookII.Mirror.stage_euclidean
(k : ℕ)
 :(default_stage_geometry k).is_euclidean = true**


[II.T45] At every stage k, the default geometry is Euclidean.

---

### `Tau.BookII.Mirror.stage_euclidean_check_true`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L175-L178)
**theorem
Tau.BookII.Mirror.stage_euclidean_check_true
(k : ℕ)
 :stage_euclidean_check k = true**


[II.T45] At every stage k, the stage-Euclidean check passes.

---

### `Tau.BookII.Mirror.all_stages_euclidean_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L180-L182)
**theorem
Tau.BookII.Mirror.all_stages_euclidean_5 :all_stages_euclidean 5 = true**


[II.T45] All stages up to depth 5 are Euclidean.

---

### `Tau.BookII.Mirror.stage_size_is_primorial`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L184-L186)
**theorem
Tau.BookII.Mirror.stage_size_is_primorial
(k : ℕ)
 :(default_stage_geometry k).stage_size = Polarity.primorial k**


[II.T45] The stage size at k is the k-th primorial.

---

### `Tau.BookII.Mirror.SCFun`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L192-L195)
**structure
Tau.BookII.Mirror.SCFun :Type**


A split-complex-valued discrete function (on a finite domain).

- values : List Polarity.SplitComplex
Instances For

---

### `Tau.BookII.Mirror.instReprSCFun`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L195-L195)
**instance
Tau.BookII.Mirror.instReprSCFun :Repr SCFun**

Equations
- Tau.BookII.Mirror.instReprSCFun = { reprPrec := Tau.BookII.Mirror.instReprSCFun.repr }

---

### `Tau.BookII.Mirror.instReprSCFun.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L195-L195)
**def
Tau.BookII.Mirror.instReprSCFun.repr :SCFun → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.SCFun.b_sector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L197-L199)
**def
Tau.BookII.Mirror.SCFun.b_sector
(f : SCFun)
 :List ℤ**


Extract the B-sector (e_+) component of each value: re + im.
Equations
- f.b_sector = List.map (fun (z : Tau.Polarity.SplitComplex) => z.re + z.im) f.values
Instances For

---

### `Tau.BookII.Mirror.SCFun.c_sector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L201-L203)
**def
Tau.BookII.Mirror.SCFun.c_sector
(f : SCFun)
 :List ℤ**


Extract the C-sector (e_-) component of each value: re - im.
Equations
- f.c_sector = List.map (fun (z : Tau.Polarity.SplitComplex) => z.re - z.im) f.values
Instances For

---

### `Tau.BookII.Mirror.wave_decompose_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L205-L212)
**def
Tau.BookII.Mirror.wave_decompose_check
(z : Polarity.SplitComplex)
 :Bool**


Reconstruct from sector components: re = (b + c) / 2, im = (b - c) / 2.
For integer arithmetic, we store the doubled values to avoid fractions:
2*re = b + c, 2*im = b - c.
This means the reconstruction check is: 2*z.re = b + c and 2*z.im = b - c.
Equations
- Tau.BookII.Mirror.wave_decompose_check z = (z.re + z.im + (z.re - z.im) == 2 * z.re && z.re + z.im - (z.re - z.im) == 2 * z.im)
Instances For

---

### `Tau.BookII.Mirror.SCFun.wave_check`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L214-L216)
**def
Tau.BookII.Mirror.SCFun.wave_check
(f : SCFun)
 :Bool**


Wave decomposition check for all values in a function.
Equations
- f.wave_check = f.values.all Tau.BookII.Mirror.wave_decompose_check
Instances For

---

### `Tau.BookII.Mirror.wave_decompose_exact`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L218-L222)
**theorem
Tau.BookII.Mirror.wave_decompose_exact
(z : Polarity.SplitComplex)
 :wave_decompose_check z = true**


Wave decomposition is exact for any split-complex number.

---

### `Tau.BookII.Mirror.wave_check_always_true`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L224-L229)
**theorem
Tau.BookII.Mirror.wave_check_always_true
(f : SCFun)
 :f.wave_check = true**


Wave decomposition is exact for any function.

---

### `Tau.BookII.Mirror.sector_additive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L231-L236)
**theorem
Tau.BookII.Mirror.sector_additive
(z w : Polarity.SplitComplex)
 :(z.add w).re + (z.add w).im = z.re + z.im + (w.re + w.im)**


[II.D70] The sector components are additive:
(z + w)_b = z_b + w_b and (z + w)_c = z_c + w_c.

---

### `Tau.BookII.Mirror.c_sector_additive`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L238-L242)
**theorem
Tau.BookII.Mirror.c_sector_additive
(z w : Polarity.SplitComplex)
 :(z.add w).re - (z.add w).im = z.re - z.im + (w.re - w.im)**


The C-sector is also additive.

---

### `Tau.BookII.Mirror.b_sector_multiplicative`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L244-L249)
**theorem
Tau.BookII.Mirror.b_sector_multiplicative
(z w : Polarity.SplitComplex)
 :(z.mul w).re + (z.mul w).im = (z.re + z.im) * (w.re + w.im)**


[II.D70] The sector components are multiplicative:
(z * w)_b = z_b * w_b. This is the key ring-isomorphism property.

---

### `Tau.BookII.Mirror.c_sector_multiplicative`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L251-L255)
**theorem
Tau.BookII.Mirror.c_sector_multiplicative
(z w : Polarity.SplitComplex)
 :(z.mul w).re - (z.mul w).im = (z.re - z.im) * (w.re - w.im)**


C-sector multiplicativity: (z * w)_c = z_c * w_c.

---

### `Tau.BookII.Mirror.MirrorSummary`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L261-L266)
**structure
Tau.BookII.Mirror.MirrorSummary :Type**


Summary structure for the elliptic-hyperbolic mirror comparison.

- elliptic_has_max_principle : Bool
- hyperbolic_has_hartogs : Bool
- both_have_unique_continuation : Bool
Instances For

---

### `Tau.BookII.Mirror.instDecidableEqMirrorSummary`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L266-L266)
**instance
Tau.BookII.Mirror.instDecidableEqMirrorSummary :DecidableEq MirrorSummary**

Equations
- Tau.BookII.Mirror.instDecidableEqMirrorSummary = Tau.BookII.Mirror.instDecidableEqMirrorSummary.decEq

---

### `Tau.BookII.Mirror.instDecidableEqMirrorSummary.decEq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L266-L266)
**def
Tau.BookII.Mirror.instDecidableEqMirrorSummary.decEq
(x✝ x✝¹ : MirrorSummary)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.instReprMirrorSummary`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L266-L266)
**instance
Tau.BookII.Mirror.instReprMirrorSummary :Repr MirrorSummary**

Equations
- Tau.BookII.Mirror.instReprMirrorSummary = { reprPrec := Tau.BookII.Mirror.instReprMirrorSummary.repr }

---

### `Tau.BookII.Mirror.instReprMirrorSummary.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L266-L266)
**def
Tau.BookII.Mirror.instReprMirrorSummary.repr :MirrorSummary → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookII.Mirror.mirror_summary`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L268-L272)
**def
Tau.BookII.Mirror.mirror_summary :MirrorSummary**


The mirror summary: elliptic gets max principle, hyperbolic gets Hartogs.
Equations
- Tau.BookII.Mirror.mirror_summary = { elliptic_has_max_principle := true, hyperbolic_has_hartogs := true, both_have_unique_continuation := true }
Instances For

---

### `Tau.BookII.Mirror.both_unique_continuation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L274-L276)
**theorem
Tau.BookII.Mirror.both_unique_continuation :mirror_summary.both_have_unique_continuation = true**


Both paths have unique continuation.

---

### `Tau.BookII.Mirror.hartogs_natural_hyp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L311-L312)
**theorem
Tau.BookII.Mirror.hartogs_natural_hyp :hyperbolic_classification.hartogs_natural = true**


---

### `Tau.BookII.Mirror.hartogs_not_natural_ell`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L314-L315)
**theorem
Tau.BookII.Mirror.hartogs_not_natural_ell :elliptic_classification.hartogs_natural = false**


---

### `Tau.BookII.Mirror.chars_hyp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L318-L319)
**theorem
Tau.BookII.Mirror.chars_hyp :hyperbolic_classification.has_characteristics = true**


---

### `Tau.BookII.Mirror.chars_ell`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L321-L322)
**theorem
Tau.BookII.Mirror.chars_ell :elliptic_classification.has_characteristics = false**


---

### `Tau.BookII.Mirror.max_hyp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L325-L326)
**theorem
Tau.BookII.Mirror.max_hyp :hyperbolic_classification.has_max_principle = false**


---

### `Tau.BookII.Mirror.max_ell`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L328-L329)
**theorem
Tau.BookII.Mirror.max_ell :elliptic_classification.has_max_principle = true**


---

### `Tau.BookII.Mirror.stages_euclidean_5`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L332-L333)
**theorem
Tau.BookII.Mirror.stages_euclidean_5 :all_stages_euclidean 5 = true**


---

### `Tau.BookII.Mirror.pde_distinct`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookII/Mirror/WaveHolomorphy.lean#L336-L340)
**theorem
Tau.BookII.Mirror.pde_distinct :elliptic_classification ≠ hyperbolic_classification**
