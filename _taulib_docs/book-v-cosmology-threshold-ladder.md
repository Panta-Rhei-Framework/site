---
layout: taulib-doc
title: "TauLib.BookV.Cosmology.ThresholdLadder"
permalink: /verify/taulib/docs/book-v-cosmology-threshold-ladder/
lane: verify
module_name: "TauLib.BookV.Cosmology.ThresholdLadder"
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

# TauLib.BookV.Cosmology.ThresholdLadder


Threshold ladder of cosmological phase transitions. Each threshold
is a critical refinement depth where a qualitative change occurs in
the regime boundary character.

Six canonical thresholds:
L_EW → L_B → L_N → L_nuc → L_H → L_γ

## Registry Cross-References


- [V.D158] Threshold (Regime Boundary) -- `ThresholdRegimeBoundary`

- [V.D159] Canonical Thresholds -- `CanonicalThresholds`

- [V.T107] Ladder Monotonicity -- `ladder_monotonicity`

- [V.D160] Neutron Threshold L_N -- `NeutronThreshold`

- [V.R218] The mass hierarchy at L_N -- structural remark

- [V.R219] Sphaleron Open Question -- structural remark

- [V.R220] Sakharov Conditions -- structural remark

- [V.D161] Nucleosynthetic Window -- `NucleosyntheticWindow`

- [V.T108] Nucleosynthesis from τ -- `nucleosynthesis_from_tau`

- [V.R221] The lithium problem -- structural remark

- [V.P92] CMB Origin -- `cmb_origin`

- [V.D162] Threshold Ladder -- `ThresholdLadderComplete`


## Mathematical Content


### Canonical Thresholds


Six regime transitions in monotone order of refinement depth:

- L_EW: electroweak symmetry breaking (ω-sector crossing)

- L_B: baryogenesis (CP violation + departure from equilibrium)

- L_N: neutron threshold (strong-sector below confinement coupling)

- L_nuc: nucleosynthesis window opens

- L_H: hydrogen recombination

- L_γ: photon decoupling (CMB last scattering)


### Neutron Threshold


At L_N, the strong-sector (η) character drops below the confinement
coupling κ(C;3) = ι<sub>τ</sub>³/(1−ι<sub>τ</sub>). This establishes:
m_n > m_p > m_e with m_p = m_n − δ_A, m_e = m_n/R

### Nucleosynthesis


The nucleosynthetic window produces observed light-element abundances:
He-4 mass fraction Y_p ~ 0.245 from neutron-to-proton freeze-out ratio.

## Ground Truth Sources


- Book V ch48: Threshold Ladder


---

### `Tau.BookV.Cosmology.ThresholdType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L63-L77)
**inductive
Tau.BookV.Cosmology.ThresholdType :Type**


Threshold type classification.

- EW : ThresholdType
Electroweak symmetry breaking.

- Baryogenesis : ThresholdType
Baryogenesis.

- Neutron : ThresholdType
Neutron threshold.

- Nucleosynthesis : ThresholdType
Nucleosynthesis window.

- Hydrogen : ThresholdType
Hydrogen recombination.

- PhotonDecoupling : ThresholdType
Photon decoupling (CMB).

Instances For

---

### `Tau.BookV.Cosmology.instReprThresholdType.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L77-L77)
**def
Tau.BookV.Cosmology.instReprThresholdType.repr :ThresholdType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprThresholdType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L77-L77)
**instance
Tau.BookV.Cosmology.instReprThresholdType :Repr ThresholdType**

Equations
- Tau.BookV.Cosmology.instReprThresholdType = { reprPrec := Tau.BookV.Cosmology.instReprThresholdType.repr }

---

### `Tau.BookV.Cosmology.instDecidableEqThresholdType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L77-L77)
**instance
Tau.BookV.Cosmology.instDecidableEqThresholdType :DecidableEq ThresholdType**

Equations
- Tau.BookV.Cosmology.instDecidableEqThresholdType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Cosmology.instBEqThresholdType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L77-L77)
**instance
Tau.BookV.Cosmology.instBEqThresholdType :BEq ThresholdType**

Equations
- Tau.BookV.Cosmology.instBEqThresholdType = { beq := Tau.BookV.Cosmology.instBEqThresholdType.beq }

---

### `Tau.BookV.Cosmology.instBEqThresholdType.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L77-L77)
**def
Tau.BookV.Cosmology.instBEqThresholdType.beq :ThresholdType → ThresholdType → Bool**

Equations
- Tau.BookV.Cosmology.instBEqThresholdType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Cosmology.ThresholdRegimeBoundary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L79-L95)
**structure
Tau.BookV.Cosmology.ThresholdRegimeBoundary :Type**


[V.D158] Threshold (regime boundary): a critical depth where a
qualitative change occurs in the regime boundary character.

At threshold n_*, one or more sector couplings cross a critical
value, causing a regime transition.

- kind : ThresholdType
Threshold type.

- depth_index : ℕ
Refinement depth at threshold (ordinal index).

- depth_pos : self.depth_index > 0
Depth is positive.

- sector_name : String
Which sector crosses.

- scope : String
Scope.

Instances For

---

### `Tau.BookV.Cosmology.instReprThresholdRegimeBoundary.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L95-L95)
**def
Tau.BookV.Cosmology.instReprThresholdRegimeBoundary.repr :ThresholdRegimeBoundary → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprThresholdRegimeBoundary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L95-L95)
**instance
Tau.BookV.Cosmology.instReprThresholdRegimeBoundary :Repr ThresholdRegimeBoundary**

Equations
- Tau.BookV.Cosmology.instReprThresholdRegimeBoundary = { reprPrec := Tau.BookV.Cosmology.instReprThresholdRegimeBoundary.repr }

---

### `Tau.BookV.Cosmology.CanonicalThresholds`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L101-L122)
**structure
Tau.BookV.Cosmology.CanonicalThresholds :Type**


[V.D159] Canonical thresholds: the six regime transitions in
monotone order. Depths are ordinal indices (1 = earliest).

- ew : ThresholdRegimeBoundary
Electroweak.

- baryogenesis : ThresholdRegimeBoundary
Baryogenesis.

- neutron : ThresholdRegimeBoundary
Neutron.

- nucleosynthesis : ThresholdRegimeBoundary
Nucleosynthesis.

- hydrogen : ThresholdRegimeBoundary
Hydrogen recombination.

- photon_decoupling : ThresholdRegimeBoundary
Photon decoupling.

- monotone : self.ew.depth_index < self.baryogenesis.depth_index ∧ self.baryogenesis.depth_index < self.neutron.depth_index ∧ self.neutron.depth_index < self.nucleosynthesis.depth_index ∧ self.nucleosynthesis.depth_index < self.hydrogen.depth_index ∧ self.hydrogen.depth_index < self.photon_decoupling.depth_index
Monotone ordering.

Instances For

---

### `Tau.BookV.Cosmology.instReprCanonicalThresholds.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L122-L122)
**def
Tau.BookV.Cosmology.instReprCanonicalThresholds.repr :CanonicalThresholds → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprCanonicalThresholds`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L122-L122)
**instance
Tau.BookV.Cosmology.instReprCanonicalThresholds :Repr CanonicalThresholds**

Equations
- Tau.BookV.Cosmology.instReprCanonicalThresholds = { reprPrec := Tau.BookV.Cosmology.instReprCanonicalThresholds.repr }

---

### `Tau.BookV.Cosmology.canonical_ladder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L124-L138)
**def
Tau.BookV.Cosmology.canonical_ladder :CanonicalThresholds**


The canonical threshold ladder instance.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.ladder_monotonicity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L144-L152)
**theorem
Tau.BookV.Cosmology.ladder_monotonicity :canonical_ladder.ew.depth_index < canonical_ladder.baryogenesis.depth_index ∧ canonical_ladder.baryogenesis.depth_index < canonical_ladder.neutron.depth_index ∧ canonical_ladder.neutron.depth_index < canonical_ladder.nucleosynthesis.depth_index ∧ canonical_ladder.nucleosynthesis.depth_index < canonical_ladder.hydrogen.depth_index ∧ canonical_ladder.hydrogen.depth_index < canonical_ladder.photon_decoupling.depth_index**


[V.T107] Ladder monotonicity: canonical thresholds occur in
the order n_EW < n_B < n_N < n_nuc < n_H < n_γ.

---

### `Tau.BookV.Cosmology.NeutronThreshold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L158-L173)
**structure
Tau.BookV.Cosmology.NeutronThreshold :Type**


[V.D160] Neutron threshold L_N: the refinement depth at which
the strong-sector (η) character drops below the confinement
coupling κ(C;3) = ι<sub>τ</sub>³/(1−ι<sub>τ</sub>).

At L_N, the mass hierarchy is established:
m_n > m_p > m_e
m_p = m_n − δ_A
m_e = m_n / R

- threshold : ThresholdRegimeBoundary
Threshold data.

- is_neutron : self.threshold.kind = ThresholdType.Neutron
The threshold is for neutrons.

- mass_hierarchy_established : Bool
Mass hierarchy holds below this threshold.

Instances For

---

### `Tau.BookV.Cosmology.instReprNeutronThreshold`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L173-L173)
**instance
Tau.BookV.Cosmology.instReprNeutronThreshold :Repr NeutronThreshold**

Equations
- Tau.BookV.Cosmology.instReprNeutronThreshold = { reprPrec := Tau.BookV.Cosmology.instReprNeutronThreshold.repr }

---

### `Tau.BookV.Cosmology.instReprNeutronThreshold.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L173-L173)
**def
Tau.BookV.Cosmology.instReprNeutronThreshold.repr :NeutronThreshold → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.SakharovConditions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L179-L194)
**structure
Tau.BookV.Cosmology.SakharovConditions :Type**


[V.R220] Two of three Sakharov conditions for baryogenesis are
structural in τ: CP violation from the bipolar lemniscate, and
departure from thermal equilibrium from the refinement cascade.

The third condition (baryon number violation) requires the
ω-sector crossing. All three are met at the L_B threshold.

- cp_violation : Bool
CP violation from lemniscate bipolarity.

- departure_from_eq : Bool
Departure from equilibrium from refinement cascade.

- baryon_violation : Bool
Baryon number violation from ω-sector.

- all_met : Bool
All three met.

Instances For

---

### `Tau.BookV.Cosmology.instReprSakharovConditions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L194-L194)
**instance
Tau.BookV.Cosmology.instReprSakharovConditions :Repr SakharovConditions**

Equations
- Tau.BookV.Cosmology.instReprSakharovConditions = { reprPrec := Tau.BookV.Cosmology.instReprSakharovConditions.repr }

---

### `Tau.BookV.Cosmology.instReprSakharovConditions.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L194-L194)
**def
Tau.BookV.Cosmology.instReprSakharovConditions.repr :SakharovConditions → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.NucleosyntheticWindow`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L200-L214)
**structure
Tau.BookV.Cosmology.NucleosyntheticWindow :Type**


[V.D161] Nucleosynthetic window W_nuc: the interval of refinement
depths during which light nuclei (D, He-3, He-4, Li-7) can form.

Opens at n_nuc^open and closes at n_nuc^close. The window width
determines the primordial element abundances.

- open_depth : ℕ
Opening depth.

- close_depth : ℕ
Closing depth.

- opens_before_close : self.open_depth < self.close_depth
Opens before closing.

- open_pos : self.open_depth > 0
Both positive.

Instances For

---

### `Tau.BookV.Cosmology.instReprNucleosyntheticWindow.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L214-L214)
**def
Tau.BookV.Cosmology.instReprNucleosyntheticWindow.repr :NucleosyntheticWindow → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprNucleosyntheticWindow`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L214-L214)
**instance
Tau.BookV.Cosmology.instReprNucleosyntheticWindow :Repr NucleosyntheticWindow**

Equations
- Tau.BookV.Cosmology.instReprNucleosyntheticWindow = { reprPrec := Tau.BookV.Cosmology.instReprNucleosyntheticWindow.repr }

---

### `Tau.BookV.Cosmology.NucleosynthesisResult`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L220-L233)
**structure
Tau.BookV.Cosmology.NucleosynthesisResult :Type**


[V.T108] Nucleosynthesis from τ: the nucleosynthetic window
produces observed light-element abundances.

He-4 mass fraction Y_p ~ 0.245 from the neutron-to-proton
freeze-out ratio at L_N.

Y_p = 20/81 = 0.24691..., encoded as 246/1000 (floor of 246.913...).
See HeliumFraction.lean for the full derivation.

- yp_times_1000 : ℕ
He-4 mass fraction × 1000.

- consistent : self.yp_times_1000 > 240 ∧ self.yp_times_1000 < 260
Consistent with observation: Y_p ∈ (0.24, 0.26).

Instances For

---

### `Tau.BookV.Cosmology.instReprNucleosynthesisResult`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L233-L233)
**instance
Tau.BookV.Cosmology.instReprNucleosynthesisResult :Repr NucleosynthesisResult**

Equations
- Tau.BookV.Cosmology.instReprNucleosynthesisResult = { reprPrec := Tau.BookV.Cosmology.instReprNucleosynthesisResult.repr }

---

### `Tau.BookV.Cosmology.instReprNucleosynthesisResult.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L233-L233)
**def
Tau.BookV.Cosmology.instReprNucleosynthesisResult.repr :NucleosynthesisResult → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.tau_yp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L235-L238)
**def
Tau.BookV.Cosmology.tau_yp :NucleosynthesisResult**


The τ-predicted He-4 mass fraction (Y_p = 20/81, floor(246.913) = 246).
Equations
- Tau.BookV.Cosmology.tau_yp = { yp_times_1000 := 246, consistent := Tau.BookV.Cosmology.tau_yp._proof_3 }
Instances For

---

### `Tau.BookV.Cosmology.nucleosynthesis_from_tau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L240-L243)
**theorem
Tau.BookV.Cosmology.nucleosynthesis_from_tau :tau_yp.yp_times_1000 > 240 ∧ tau_yp.yp_times_1000 < 260**


He-4 prediction is in range.

---

### `Tau.BookV.Cosmology.CmbOrigin`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L249-L264)
**structure
Tau.BookV.Cosmology.CmbOrigin :Type**


[V.P92] CMB origin: the CMB is the photon readout of the
last-scattering surface at the photon decoupling threshold L_γ.

Temperature T_CMB ≈ 2.725 K. The last-scattering surface is
at redshift z ≈ 1100 in chart-level readout coordinates.

In τ, the CMB is a boundary-character snapshot of the B-sector
at L_γ depth.

- temp_mK : ℕ
CMB temperature × 1000 (in mK).

- redshift_times_10 : ℕ
Redshift of last scattering × 10.

- temp_range : self.temp_mK > 2700 ∧ self.temp_mK < 2750
Temperature is ~ 2725 mK.

Instances For

---

### `Tau.BookV.Cosmology.instReprCmbOrigin`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L264-L264)
**instance
Tau.BookV.Cosmology.instReprCmbOrigin :Repr CmbOrigin**

Equations
- Tau.BookV.Cosmology.instReprCmbOrigin = { reprPrec := Tau.BookV.Cosmology.instReprCmbOrigin.repr }

---

### `Tau.BookV.Cosmology.instReprCmbOrigin.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L264-L264)
**def
Tau.BookV.Cosmology.instReprCmbOrigin.repr :CmbOrigin → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.observed_cmb`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L266-L270)
**def
Tau.BookV.Cosmology.observed_cmb :CmbOrigin**


The observed CMB.
Equations
- Tau.BookV.Cosmology.observed_cmb = { temp_mK := 2725, redshift_times_10 := 11000, temp_range := Tau.BookV.Cosmology.observed_cmb._proof_3 }
Instances For

---

### `Tau.BookV.Cosmology.cmb_origin`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L272-L273)
**theorem
Tau.BookV.Cosmology.cmb_origin :observed_cmb.temp_mK > 2700**


CMB temperature in range.

---

### `Tau.BookV.Cosmology.MassHierarchyAtLN`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L279-L288)
**structure
Tau.BookV.Cosmology.MassHierarchyAtLN :Type**


[V.R218] Mass hierarchy at L_N: once the strong-sector character
drops below confinement coupling, the mass hierarchy locks in:
m_n > m_p > m_e
with m_p = m_n − δ_A and m_e = m_n/R (R ≈ 1838.68).

- r_times_100 : ℕ
R ≈ 1838.68 (neutron-to-electron mass ratio, × 100).

- r_range : self.r_times_100 > 183800 ∧ self.r_times_100 < 183900
R in range.

Instances For

---

### `Tau.BookV.Cosmology.instReprMassHierarchyAtLN.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L288-L288)
**def
Tau.BookV.Cosmology.instReprMassHierarchyAtLN.repr :MassHierarchyAtLN → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprMassHierarchyAtLN`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L288-L288)
**instance
Tau.BookV.Cosmology.instReprMassHierarchyAtLN :Repr MassHierarchyAtLN**

Equations
- Tau.BookV.Cosmology.instReprMassHierarchyAtLN = { reprPrec := Tau.BookV.Cosmology.instReprMassHierarchyAtLN.repr }

---

### `Tau.BookV.Cosmology.mass_hierarchy_r`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L290-L293)
**def
Tau.BookV.Cosmology.mass_hierarchy_r :MassHierarchyAtLN**


The mass hierarchy R value.
Equations
- Tau.BookV.Cosmology.mass_hierarchy_r = { r_times_100 := 183868, r_range := Tau.BookV.Cosmology.mass_hierarchy_r._proof_3 }
Instances For

---

### `Tau.BookV.Cosmology.ThresholdLadderComplete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L299-L308)
**structure
Tau.BookV.Cosmology.ThresholdLadderComplete :Type**


[V.D162] Threshold ladder: the complete ordered sequence of
canonical thresholds. Six thresholds, monotonically ordered.

- ladder : CanonicalThresholds
The canonical ladder.

- count : ℕ
Number of thresholds.

- count_is_six : self.count = 6
Count is 6.

Instances For

---

### `Tau.BookV.Cosmology.instReprThresholdLadderComplete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L308-L308)
**instance
Tau.BookV.Cosmology.instReprThresholdLadderComplete :Repr ThresholdLadderComplete**

Equations
- Tau.BookV.Cosmology.instReprThresholdLadderComplete = { reprPrec := Tau.BookV.Cosmology.instReprThresholdLadderComplete.repr }

---

### `Tau.BookV.Cosmology.instReprThresholdLadderComplete.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L308-L308)
**def
Tau.BookV.Cosmology.instReprThresholdLadderComplete.repr :ThresholdLadderComplete → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.complete_ladder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/ThresholdLadder.lean#L310-L314)
**def
Tau.BookV.Cosmology.complete_ladder :ThresholdLadderComplete**


The complete ladder has 6 thresholds.
Equations
- Tau.BookV.Cosmology.complete_ladder = { ladder := Tau.BookV.Cosmology.canonical_ladder, count := 6,
 count_is_six := Tau.BookV.Cosmology.complete_ladder._proof_1 }
Instances For
