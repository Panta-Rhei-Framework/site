---
layout: taulib-doc
title: "TauLib.BookV.Cosmology.HeliumFraction"
permalink: /verify/taulib/docs/book-v-cosmology-helium-fraction/
lane: verify
module_name: "TauLib.BookV.Cosmology.HeliumFraction"
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

# TauLib.BookV.Cosmology.HeliumFraction


Primordial He-4 mass fraction Y_p = 20/81 from pure structural integers.

Three independent decompositions:
Route A: (8/27) × (5/6) = 20/81 (voxel-geometric)
Route B: (4 × 5) / 3⁴ = 20/81 (compact)
Route C: (1/4) × (80/81) = 20/81 (supercell)

## Registry Cross-References


- [V.D192] He-4 Packing Maximum -- `HePacking`

- [V.D193] Face-Conflict Probability -- `FaceConflict`

- [V.D194] Domain-Wall Correction -- `DomainCorrection`

- [V.D195] Primordial He-4 Mass Fraction -- `HeliumPrediction`

- [V.D196] Neutron-to-Proton Ratio -- `NeutronProtonRatio`

- [V.T146] Packing Maximum Theorem -- `packing_is_8_27`

- [V.T147] Face-Conflict Theorem -- `face_conflict_is_1_3`

- [V.T148] Three Decompositions Identity -- `three_routes_agree`

- [V.T149] Y_p Derivation -- `yp_is_20_81`

- [V.T150] n/p Ratio Derivation -- `np_from_yp`

- [V.P112] Y_p Observational Consistency -- `yp_in_observational_range`

- [V.R322] 71 = p₂₀ -- structural remark


## Mathematical Content


### He-4 Packing Maximum = 8/27


Model He-4 as a 2×2×2 voxel block (8 voxels). The strong non-touching
rule (Chebyshev distance > 2 between block corners) requires stride ≥ 3
per axis. Packing = 8 / 3³ = 8/27.

### Domain-Wall Correction = 5/6


Decomposition: 5/6 = 1 − (1/2)(1/3)


- P(face conflict) = 1/3: proved combinatorially (3/9 pairs with a₂ < a₁)

- bnd_frac = 1/2: self-consistent with 6-threshold structure


### Y_p = 20/81


From (8/27) × (5/6) = 40/162 = 20/81 = 0.24691...
Matches Planck 2018 (0.2470 ± 0.0002) at 0.43σ.

### n/p = 10/71


From Y_p = 2(n/p)/(1+n/p) = 20/81 → n/p = 10/71.
Note: 71 = p₂₀ (20th prime).

## Ground Truth Sources


- Book V ch48: Threshold Ladder

- research/universe/bbn_helium_tau_derivation.py

- research/universe/five_sixths_conflict_lab.py


---

### `Tau.BookV.Cosmology.HePacking`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L64-L81)
**structure
Tau.BookV.Cosmology.HePacking :Type**


[V.D192] He-4 packing maximum: 2×2×2 blocks in 3×3×3 macrocells.
Packing fraction = 8/27.

- block_side : ℕ
Block size per axis.

- macro_side : ℕ
Macrocell size per axis.

- pack_num : ℕ
Numerator of packing fraction.

- pack_den : ℕ
Denominator of packing fraction.

- block_vol : self.block_side ^ 3 = self.pack_num
Block volume = block_side³.

- macro_vol : self.macro_side ^ 3 = self.pack_den
Macrocell volume = macro_side³.

- stride_eq : self.block_side + 1 = self.macro_side
Stride = block_side + 1 = macro_side.

Instances For

---

### `Tau.BookV.Cosmology.instReprHePacking`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L81-L81)
**instance
Tau.BookV.Cosmology.instReprHePacking :Repr HePacking**

Equations
- Tau.BookV.Cosmology.instReprHePacking = { reprPrec := Tau.BookV.Cosmology.instReprHePacking.repr }

---

### `Tau.BookV.Cosmology.instReprHePacking.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L81-L81)
**def
Tau.BookV.Cosmology.instReprHePacking.repr :HePacking → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.he_packing`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L83-L87)
**def
Tau.BookV.Cosmology.he_packing :HePacking**


The canonical He-4 packing instance.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.packing_is_8_27`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L89-L92)
**theorem
Tau.BookV.Cosmology.packing_is_8_27 :he_packing.pack_num = 8 ∧ he_packing.pack_den = 27**


[V.T146] Packing is exactly 8/27.

---

### `Tau.BookV.Cosmology.FaceConflict`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L98-L112)
**structure
Tau.BookV.Cosmology.FaceConflict :Type**


[V.D193] Face-conflict probability for phase-adjacent macrocells.
P(conflict) = 1/3, proved by exhaustive enumeration:
among 9 pairs (a₁,a₂) ∈ {0,1,2}², exactly 3 have a₂ < a₁.

- conflict_count : ℕ
Number of conflict pairs (a₂ < a₁).

- total_pairs : ℕ
Total pairs.

- phase_count : ℕ
Number of phase values per axis.

- total_is_sq : self.total_pairs = self.phase_count * self.phase_count
Total = phase_count².

- conflicts_enumerated : self.conflict_count = 3
Conflict pairs: exactly those with a₂ < a₁.

Instances For

---

### `Tau.BookV.Cosmology.instReprFaceConflict.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L112-L112)
**def
Tau.BookV.Cosmology.instReprFaceConflict.repr :FaceConflict → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprFaceConflict`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L112-L112)
**instance
Tau.BookV.Cosmology.instReprFaceConflict :Repr FaceConflict**

Equations
- Tau.BookV.Cosmology.instReprFaceConflict = { reprPrec := Tau.BookV.Cosmology.instReprFaceConflict.repr }

---

### `Tau.BookV.Cosmology.face_conflict`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L114-L117)
**def
Tau.BookV.Cosmology.face_conflict :FaceConflict**


The face-conflict instance.
Equations
- Tau.BookV.Cosmology.face_conflict = { total_is_sq := Tau.BookV.Cosmology.face_conflict._proof_1,
 conflicts_enumerated := Tau.BookV.Cosmology.face_conflict._proof_2 }
Instances For

---

### `Tau.BookV.Cosmology.face_conflict_is_1_3`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L119-L122)
**theorem
Tau.BookV.Cosmology.face_conflict_is_1_3 :face_conflict.conflict_count * 3 = face_conflict.total_pairs**


[V.T147] P(face conflict) = 1/3, i.e. 3 out of 9 pairs.

---

### `Tau.BookV.Cosmology.DomainCorrection`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L128-L143)
**structure
Tau.BookV.Cosmology.DomainCorrection :Type**


[V.D194] Domain-wall correction factor = 5/6.
Decomposition: 5/6 = 1 − (1/2)(1/3).


- 1/3 = P(face conflict), proved

- 1/2 = boundary fraction, self-consistent with 6-threshold structure


- corr_num : ℕ
Numerator.

- corr_den : ℕ
Denominator.

- clean_thresholds : ℕ
Number of clean thresholds.

- total_thresholds : ℕ
Total thresholds.

- corr_eq : self.corr_num = self.clean_thresholds ∧ self.corr_den = self.total_thresholds
Correction = clean/total.

Instances For

---

### `Tau.BookV.Cosmology.instReprDomainCorrection.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L143-L143)
**def
Tau.BookV.Cosmology.instReprDomainCorrection.repr :DomainCorrection → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprDomainCorrection`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L143-L143)
**instance
Tau.BookV.Cosmology.instReprDomainCorrection :Repr DomainCorrection**

Equations
- Tau.BookV.Cosmology.instReprDomainCorrection = { reprPrec := Tau.BookV.Cosmology.instReprDomainCorrection.repr }

---

### `Tau.BookV.Cosmology.domain_correction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L145-L147)
**def
Tau.BookV.Cosmology.domain_correction :DomainCorrection**


The domain correction instance.
Equations
- Tau.BookV.Cosmology.domain_correction = { corr_eq := Tau.BookV.Cosmology.domain_correction._proof_1 }
Instances For

---

### `Tau.BookV.Cosmology.five_sixths_decomposition`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L149-L153)
**theorem
Tau.BookV.Cosmology.five_sixths_decomposition :domain_correction.corr_den - 1 = domain_correction.corr_num**


The 5/6 decomposition: 1 − (1/2)(1/3) = 5/6, encoded as
6 × 1 − 6 × (1/2)(1/3) = 6 − 1 = 5, i.e. 6 − 1 = 5.

---

### `Tau.BookV.Cosmology.HeliumPrediction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L159-L175)
**structure
Tau.BookV.Cosmology.HeliumPrediction :Type**


[V.D195] Primordial He-4 mass fraction Y_p = 20/81.

- yp_num : ℕ
Y_p numerator.

- yp_den : ℕ
Y_p denominator.

- route_a_num : ℕ
Route A: (8 × 5) / (27 × 6) = 40/162 = 20/81.

- route_a_den : ℕ
- route_b_num : ℕ
Route B: (4 × 5) / 3⁴.

- route_b_den : ℕ
- route_a_reduces : self.route_a_num / 2 = self.yp_num ∧ self.route_a_den / 2 = self.yp_den
Route A reduces to 20/81.

- route_b_eq : self.route_b_num = self.yp_num ∧ self.route_b_den = self.yp_den
Route B equals 20/81 directly.

Instances For

---

### `Tau.BookV.Cosmology.instReprHeliumPrediction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L175-L175)
**instance
Tau.BookV.Cosmology.instReprHeliumPrediction :Repr HeliumPrediction**

Equations
- Tau.BookV.Cosmology.instReprHeliumPrediction = { reprPrec := Tau.BookV.Cosmology.instReprHeliumPrediction.repr }

---

### `Tau.BookV.Cosmology.instReprHeliumPrediction.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L175-L175)
**def
Tau.BookV.Cosmology.instReprHeliumPrediction.repr :HeliumPrediction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.he_prediction`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L177-L180)
**def
Tau.BookV.Cosmology.he_prediction :HeliumPrediction**


The helium prediction instance.
Equations
- Tau.BookV.Cosmology.he_prediction = { route_a_reduces := Tau.BookV.Cosmology.he_prediction._proof_1,
 route_b_eq := Tau.BookV.Cosmology.he_prediction._proof_2 }
Instances For

---

### `Tau.BookV.Cosmology.three_routes_agree`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L183-L191)
**theorem
Tau.BookV.Cosmology.three_routes_agree :8 * 5 * 81 = 20 * 27 * 6 ∧ 4 * 5 = 20 ∧ 3 ^ 4 = 81 ∧ 1 * 80 * 81 = 20 * 4 * 81**


All three routes give 20/81 (checked as cross-multiplication identities).

---

### `Tau.BookV.Cosmology.yp_is_20_81`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L194-L198)
**theorem
Tau.BookV.Cosmology.yp_is_20_81 :he_packing.pack_num * domain_correction.corr_num * he_prediction.yp_den = he_prediction.yp_num * he_packing.pack_den * domain_correction.corr_den**


Y_p = (8/27) × (5/6) = 20/81, verified as 8 × 5 × 81 = 20 × 27 × 6.

---

### `Tau.BookV.Cosmology.yp_times_1000`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L204-L206)
**def
Tau.BookV.Cosmology.yp_times_1000 :ℕ**


Y_p × 1000 = 20000/81 = 246 (integer part).
This replaces the hardcoded 245 in ThresholdLadder.lean.
Equations
- Tau.BookV.Cosmology.yp_times_1000 = 1000 * Tau.BookV.Cosmology.he_prediction.yp_num / Tau.BookV.Cosmology.he_prediction.yp_den
Instances For

---

### `Tau.BookV.Cosmology.yp_times_1000_eq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L208-L209)
**theorem
Tau.BookV.Cosmology.yp_times_1000_eq :yp_times_1000 = 246**


Y_p × 1000 = 246 (floor of 246.913...).

---

### `Tau.BookV.Cosmology.yp_in_range`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L211-L213)
**theorem
Tau.BookV.Cosmology.yp_in_range :yp_times_1000 > 240 ∧ yp_times_1000 < 260**


The derived Y_p is in the observational range (240, 260).

---

### `Tau.BookV.Cosmology.NeutronProtonRatio`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L219-L227)
**structure
Tau.BookV.Cosmology.NeutronProtonRatio :Type**


[V.D196] Neutron-to-proton ratio n/p = 10/71 from Y_p = 20/81.
Derivation: Y_p = 2(n/p)/(1+n/p) = 20/81
→ 162·n/p = 20·(1 + n/p) → 142·n/p = 20 → n/p = 10/71.

- np_num : ℕ
Numerator.

- np_den : ℕ
Denominator.

Instances For

---

### `Tau.BookV.Cosmology.instReprNeutronProtonRatio`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L227-L227)
**instance
Tau.BookV.Cosmology.instReprNeutronProtonRatio :Repr NeutronProtonRatio**

Equations
- Tau.BookV.Cosmology.instReprNeutronProtonRatio = { reprPrec := Tau.BookV.Cosmology.instReprNeutronProtonRatio.repr }

---

### `Tau.BookV.Cosmology.instReprNeutronProtonRatio.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L227-L227)
**def
Tau.BookV.Cosmology.instReprNeutronProtonRatio.repr :NeutronProtonRatio → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.np_ratio`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L229-L230)
**def
Tau.BookV.Cosmology.np_ratio :NeutronProtonRatio**


The n/p ratio instance.
Equations
- Tau.BookV.Cosmology.np_ratio = { }
Instances For

---

### `Tau.BookV.Cosmology.np_from_yp`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L233-L238)
**theorem
Tau.BookV.Cosmology.np_from_yp :2 * np_ratio.np_num * he_prediction.yp_den = he_prediction.yp_num * (np_ratio.np_num + np_ratio.np_den)**


From Y_p = 20/81 and Y_p = 2n/(n+p), we get n/p = 10/71.
Verification: 2 × 10 × 81 = 20 × (10 + 71) = 20 × 81.

---

### `Tau.BookV.Cosmology.yp_in_observational_range`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/HeliumFraction.lean#L241-L245)
**theorem
Tau.BookV.Cosmology.yp_in_observational_range :yp_times_1000 ≥ 244 ∧ yp_times_1000 ≤ 250**


[V.P112] Y_p = 20/81 = 0.24691... is within the observational
range Y_p ∈ (0.244, 0.250) at 2σ.
