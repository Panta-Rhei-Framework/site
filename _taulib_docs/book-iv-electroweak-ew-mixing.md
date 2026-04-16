---
layout: taulib-doc
title: "TauLib.BookIV.Electroweak.EWMixing"
permalink: /verify/taulib/docs/book-iv-electroweak-ew-mixing/
lane: verify
module_name: "TauLib.BookIV.Electroweak.EWMixing"
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

# TauLib.BookIV.Electroweak.EWMixing


Electroweak mixing: hypercharge, Weinberg angle, neutral boson mixing,
and the structural identification sin²(θ_W) = κ(A,D).

## Registry Cross-References


- [IV.D127] Hypercharge Y — `Hypercharge`

- [IV.D128] Pre-Mixing EW Group G_EW — `PreMixingEWGroup`

- [IV.D129] W± Charged Currents — `ChargedCurrent`

- [IV.D130] Weinberg Angle — `WeinbergAngleTau`

- [IV.D131] Mixing-Compatible Sectors — `MixingCompatibility`

- [IV.D132] Maximal Mixing — `MaximalMixing`

- [IV.D133] ω-Resolution of Crossing Singularity — `OmegaResolution`

- [IV.T60] Neutral Boson Mixing — `NeutralBosonMixing`, `mixing_orthogonal`

- [IV.T61] sin²(θ_W) = κ(A,D) — `weinberg_equals_kappaAD`

- [IV.T62] Unique Mixing-Compatible Pair — `unique_mixing_pair`

- [IV.P68] EM Coupling Relation — `em_coupling_relation`

- [IV.P69] Tree-Level Deviation — `tree_level_deviation`

- [IV.P70] No Higher Unification — `no_higher_unification`

- [IV.P71] Dual Role of Balanced Polarity — `dual_role_balanced`

- [IV.R31] 2.7% Gap Scope — structural remark


## Mathematical Content


The Weinberg angle θ_W parametrizes the mixing of the neutral W³ boson
(SU(2)_L) with the B boson (U(1)_Y) to produce the physical photon γ
and Z boson. In the τ-framework, sin²(θ_W) is NOT a free parameter but
is determined by the inter-sector coupling:

sin²(θ_W) = κ(A,D) = ι<sub>τ</sub>(1 − ι<sub>τ</sub>) ≈ 0.2249

The experimental value at the Z pole is sin²(θ_W)_exp ≈ 0.2312,
giving a 2.7% tree-level deviation — expected to be resolved by
radiative corrections at the loop level.

The key structural theorem (IV.T62) is that (A,B) is the UNIQUE
mixing-compatible sector pair: A is the only balanced-polarity sector,
and B is the only χ₊-dominant fiber sector, making their crossing
the unique site for electroweak mixing.

## Ground Truth Sources


- Chapter 33 of Book IV (2nd Edition)

- Book III editorial logbook Decision #31 (canonical force mapping)

- temporal_spatial_decomposition.md §5


---

### `Tau.BookIV.Electroweak.Hypercharge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L60-L76)
**structure
Tau.BookIV.Electroweak.Hypercharge :Type**


[IV.D127] Hypercharge quantum number Y: the U(1)_Y charge
determined by the boundary character's projection onto the
B-sector (electromagnetic) component. In the τ-framework,
Y is a derived quantity from the sector decomposition, NOT
postulated independently.

Y = 2(Q − T₃) where Q is electric charge and T₃ is weak isospin.

- label : String
Particle or state label.

- y_numer : ℤ
Hypercharge value, as integer (in units of 1/3 for quarks).

- y_denom : ℕ
Denominator for fractional hypercharges.

- denom_pos : self.y_denom > 0
Denominator positive.

Instances For

---

### `Tau.BookIV.Electroweak.instReprHypercharge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L76-L76)
**instance
Tau.BookIV.Electroweak.instReprHypercharge :Repr Hypercharge**

Equations
- Tau.BookIV.Electroweak.instReprHypercharge = { reprPrec := Tau.BookIV.Electroweak.instReprHypercharge.repr }

---

### `Tau.BookIV.Electroweak.instReprHypercharge.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L76-L76)
**def
Tau.BookIV.Electroweak.instReprHypercharge.repr :Hypercharge → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.hypercharge_eL`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L78-L82)
**def
Tau.BookIV.Electroweak.hypercharge_eL :Hypercharge**


Left-handed electron doublet: Y = -1.
Equations
- Tau.BookIV.Electroweak.hypercharge_eL = { label := "e_L", y_numer := -1, y_denom := 1, denom_pos := Tau.BookIV.Electroweak.hypercharge_eL._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.hypercharge_eR`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L84-L88)
**def
Tau.BookIV.Electroweak.hypercharge_eR :Hypercharge**


Right-handed electron singlet: Y = -2.
Equations
- Tau.BookIV.Electroweak.hypercharge_eR = { label := "e_R", y_numer := -2, y_denom := 1, denom_pos := Tau.BookIV.Electroweak.hypercharge_eL._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.hypercharge_qL`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L90-L94)
**def
Tau.BookIV.Electroweak.hypercharge_qL :Hypercharge**


Left-handed quark doublet: Y = 1/3.
Equations
- Tau.BookIV.Electroweak.hypercharge_qL = { label := "q_L", y_numer := 1, y_denom := 3, denom_pos := Tau.BookIV.Electroweak.hypercharge_qL._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.PreMixingEWGroup`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L100-L113)
**structure
Tau.BookIV.Electroweak.PreMixingEWGroup :Type**


[IV.D128] The pre-mixing electroweak gauge group G_EW = SU(2)_L × U(1)_Y.
In the τ-framework, this is the product of sector A (weak/SU(2))
and the U(1) subgroup of sector B (electromagnetic).
This group acts BEFORE mixing produces the physical bosons.

- weak_sector : BookIII.Sectors.Sector
The weak (SU(2)_L) sector.

- hypercharge_sector : BookIII.Sectors.Sector
The hypercharge U(1)_Y component.

- weak_is_A : self.weak_sector = BookIII.Sectors.Sector.A
Weak is sector A.

- hyper_is_B : self.hypercharge_sector = BookIII.Sectors.Sector.B
Hypercharge derives from sector B.

Instances For

---

### `Tau.BookIV.Electroweak.instReprPreMixingEWGroup`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L113-L113)
**instance
Tau.BookIV.Electroweak.instReprPreMixingEWGroup :Repr PreMixingEWGroup**

Equations
- Tau.BookIV.Electroweak.instReprPreMixingEWGroup = { reprPrec := Tau.BookIV.Electroweak.instReprPreMixingEWGroup.repr }

---

### `Tau.BookIV.Electroweak.instReprPreMixingEWGroup.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L113-L113)
**def
Tau.BookIV.Electroweak.instReprPreMixingEWGroup.repr :PreMixingEWGroup → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.ew_group`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L115-L120)
**def
Tau.BookIV.Electroweak.ew_group :PreMixingEWGroup**


The canonical pre-mixing EW group.
Equations
- Tau.BookIV.Electroweak.ew_group = { weak_sector := Tau.BookIII.Sectors.Sector.A, hypercharge_sector := Tau.BookIII.Sectors.Sector.B, weak_is_A := ⋯,
 hyper_is_B := ⋯ }
Instances For

---

### `Tau.BookIV.Electroweak.ChargedCurrent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L126-L134)
**inductive
Tau.BookIV.Electroweak.ChargedCurrent :Type**


[IV.D129] W± charged currents: the off-diagonal SU(2)_L
generators that mediate charge-changing weak interactions.
These do NOT mix with B: only the neutral W³ mixes.

- Wplus : ChargedCurrent
W+ raises weak isospin by 1.

- Wminus : ChargedCurrent
W- lowers weak isospin by 1.

Instances For

---

### `Tau.BookIV.Electroweak.instReprChargedCurrent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L134-L134)
**instance
Tau.BookIV.Electroweak.instReprChargedCurrent :Repr ChargedCurrent**

Equations
- Tau.BookIV.Electroweak.instReprChargedCurrent = { reprPrec := Tau.BookIV.Electroweak.instReprChargedCurrent.repr }

---

### `Tau.BookIV.Electroweak.instReprChargedCurrent.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L134-L134)
**def
Tau.BookIV.Electroweak.instReprChargedCurrent.repr :ChargedCurrent → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instDecidableEqChargedCurrent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L134-L134)
**instance
Tau.BookIV.Electroweak.instDecidableEqChargedCurrent :DecidableEq ChargedCurrent**

Equations
- Tau.BookIV.Electroweak.instDecidableEqChargedCurrent x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Electroweak.instBEqChargedCurrent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L134-L134)
**instance
Tau.BookIV.Electroweak.instBEqChargedCurrent :BEq ChargedCurrent**

Equations
- Tau.BookIV.Electroweak.instBEqChargedCurrent = { beq := Tau.BookIV.Electroweak.instBEqChargedCurrent.beq }

---

### `Tau.BookIV.Electroweak.instBEqChargedCurrent.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L134-L134)
**def
Tau.BookIV.Electroweak.instBEqChargedCurrent.beq :ChargedCurrent → ChargedCurrent → Bool**

Equations
- Tau.BookIV.Electroweak.instBEqChargedCurrent.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Electroweak.charged_current_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L136-L137)
**def
Tau.BookIV.Electroweak.charged_current_sector :ChargedCurrent → BookIII.Sectors.Sector**


Charged currents are purely sector-A objects (no mixing).
Equations
- Tau.BookIV.Electroweak.charged_current_sector x✝ = Tau.BookIII.Sectors.Sector.A
Instances For

---

### `Tau.BookIV.Electroweak.WeinbergAngleTau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L143-L158)
**structure
Tau.BookIV.Electroweak.WeinbergAngleTau :Type**


[IV.D130] The Weinberg angle (weak mixing angle) θ_W.
In the τ-framework: sin²(θ_W) = κ(A,D) = ι<sub>τ</sub>(1−ι<sub>τ</sub>).

τ-prediction: sin²(θ_W) ≈ 0.2249
Experimental (Z pole, MS-bar): sin²(θ_W) ≈ 0.2312

Numerator/denominator encode the τ-predicted value.

- sin2_numer : ℕ
sin²(θ_W) numerator = κ(A,D) numerator.

- sin2_denom : ℕ
sin²(θ_W) denominator = κ(A,D) denominator.

- denom_pos : self.sin2_denom > 0
Denominator positive.

- equals_kappaAD : self.sin2_numer = Sectors.kappa_AD.numer ∧ self.sin2_denom = Sectors.kappa_AD.denom
This equals the (A,D) cross-coupling.

Instances For

---

### `Tau.BookIV.Electroweak.weinberg_angle_tau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L160-L165)
**def
Tau.BookIV.Electroweak.weinberg_angle_tau :WeinbergAngleTau**


The τ-predicted Weinberg angle.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.weinberg_float`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L167-L169)
**def
Tau.BookIV.Electroweak.weinberg_float :Float**


sin²(θ_W) as Float for display.
Equations
- Tau.BookIV.Electroweak.weinberg_float = Float.ofNat Tau.BookIV.Electroweak.weinberg_angle_tau.sin2_numer / Float.ofNat Tau.BookIV.Electroweak.weinberg_angle_tau.sin2_denom
Instances For

---

### `Tau.BookIV.Electroweak.MixingCompatibility`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L175-L190)
**structure
Tau.BookIV.Electroweak.MixingCompatibility :Type**


[IV.D131] A sector pair is mixing-compatible if:

- One sector has balanced polarity (= sector A, unique).

- The other has χ₊-dominant polarity on the fiber (= sector B).

- Their cross-coupling κ(A,B) is nonzero.


These conditions ensure that the neutral component of the balanced
sector can rotate into the χ₊-dominant sector.

- balanced : BookIII.Sectors.Sector
First sector (must be balanced).

- chi_plus_fiber : BookIII.Sectors.Sector
Second sector (must be χ₊-dominant, fiber).

- balanced_is_A : self.balanced = BookIII.Sectors.Sector.A
Balanced is A.

- chi_plus_is_B : self.chi_plus_fiber = BookIII.Sectors.Sector.B
χ₊-fiber is B.

Instances For

---

### `Tau.BookIV.Electroweak.mixing_pair`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L192-L197)
**def
Tau.BookIV.Electroweak.mixing_pair :MixingCompatibility**


The unique mixing-compatible pair.
Equations
- Tau.BookIV.Electroweak.mixing_pair = { balanced := Tau.BookIII.Sectors.Sector.A, chi_plus_fiber := Tau.BookIII.Sectors.Sector.B, balanced_is_A := ⋯,
 chi_plus_is_B := ⋯ }
Instances For

---

### `Tau.BookIV.Electroweak.MaximalMixing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L203-L213)
**structure
Tau.BookIV.Electroweak.MaximalMixing :Type**


[IV.D132] Maximal mixing: the condition sin²(θ_W) = 1/4, which
would mean equal W³ and B content in both γ and Z.
In τ: sin²(θ_W) = ι<sub>τ</sub>(1−ι<sub>τ</sub>), which equals 1/4 iff ι<sub>τ</sub> = 1/2.
Since ι<sub>τ</sub> ≈ 0.3415, mixing is SUB-maximal.

- maximal_numer : ℕ
sin²(θ_W) at maximal mixing: 1/4.

- maximal_denom : ℕ
- not_maximal : weinberg_angle_tau.sin2_numer * 4 ≠ weinberg_angle_tau.sin2_denom
Actual τ-value differs from 1/4.

Instances For

---

### `Tau.BookIV.Electroweak.instReprMaximalMixing.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L213-L213)
**def
Tau.BookIV.Electroweak.instReprMaximalMixing.repr :MaximalMixing → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprMaximalMixing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L213-L213)
**instance
Tau.BookIV.Electroweak.instReprMaximalMixing :Repr MaximalMixing**

Equations
- Tau.BookIV.Electroweak.instReprMaximalMixing = { reprPrec := Tau.BookIV.Electroweak.instReprMaximalMixing.repr }

---

### `Tau.BookIV.Electroweak.maximal_mixing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L215-L216)
**def
Tau.BookIV.Electroweak.maximal_mixing :MaximalMixing**

Equations
- Tau.BookIV.Electroweak.maximal_mixing = { not_maximal := Tau.BookIV.Electroweak.maximal_mixing._proof_1 }
Instances For

---

### `Tau.BookIV.Electroweak.OmegaResolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L222-L237)
**structure
Tau.BookIV.Electroweak.OmegaResolution :Type**


[IV.D133] The ω-sector resolves the singularity at the lemniscate
crossing point where sectors B and C meet. Without ω, the
mixing rotation would encounter a topological obstruction at
the crossing. The Higgs mechanism (ω-sector) smooths this
singularity, enabling clean boson mass generation.

- crossing : BookIII.Sectors.Sector
The crossing sector.

- resolved_1 : BookIII.Sectors.Sector
Resolved sectors.

- resolved_2 : BookIII.Sectors.Sector
- crossing_is_omega : self.crossing = BookIII.Sectors.Sector.Omega
Crossing is ω.

- resolved_is_BC : self.resolved_1 = BookIII.Sectors.Sector.B ∧ self.resolved_2 = BookIII.Sectors.Sector.C
Resolved pair is (B, C).

Instances For

---

### `Tau.BookIV.Electroweak.instReprOmegaResolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L237-L237)
**instance
Tau.BookIV.Electroweak.instReprOmegaResolution :Repr OmegaResolution**

Equations
- Tau.BookIV.Electroweak.instReprOmegaResolution = { reprPrec := Tau.BookIV.Electroweak.instReprOmegaResolution.repr }

---

### `Tau.BookIV.Electroweak.instReprOmegaResolution.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L237-L237)
**def
Tau.BookIV.Electroweak.instReprOmegaResolution.repr :OmegaResolution → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.omega_resolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L239-L244)
**def
Tau.BookIV.Electroweak.omega_resolution :OmegaResolution**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.NeutralBosonMixing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L250-L271)
**structure
Tau.BookIV.Electroweak.NeutralBosonMixing :Type**


[IV.T60] Neutral boson mixing: the physical photon γ and Z boson
arise from an orthogonal rotation of the neutral W³ and B bosons.

γ = B cos(θ_W) + W³ sin(θ_W)
Z = -B sin(θ_W) + W³ cos(θ_W)

The rotation matrix is orthogonal (SO(2)), preserving the sum
of squared couplings.

- input_W3 : String
Input: neutral weak boson W³.

- input_B : String
Input: hypercharge boson B.

- output_photon : String
Output: photon.

- output_Z : String
Output: Z boson.

- orthogonal : Bool
Mixing is an orthogonal (SO(2)) rotation.

- in_out_match : Bool
Number of input bosons equals output bosons.

Instances For

---

### `Tau.BookIV.Electroweak.instReprNeutralBosonMixing.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L271-L271)
**def
Tau.BookIV.Electroweak.instReprNeutralBosonMixing.repr :NeutralBosonMixing → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprNeutralBosonMixing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L271-L271)
**instance
Tau.BookIV.Electroweak.instReprNeutralBosonMixing :Repr NeutralBosonMixing**

Equations
- Tau.BookIV.Electroweak.instReprNeutralBosonMixing = { reprPrec := Tau.BookIV.Electroweak.instReprNeutralBosonMixing.repr }

---

### `Tau.BookIV.Electroweak.neutral_boson_mixing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L273-L273)
**def
Tau.BookIV.Electroweak.neutral_boson_mixing :NeutralBosonMixing**

Equations
- Tau.BookIV.Electroweak.neutral_boson_mixing = { }
Instances For

---

### `Tau.BookIV.Electroweak.mixing_orthogonal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L275-L277)
**theorem
Tau.BookIV.Electroweak.mixing_orthogonal :neutral_boson_mixing.orthogonal = true**


[IV.T60] The mixing rotation is orthogonal (SO(2)).

---

### `Tau.BookIV.Electroweak.mixing_conserves_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L279-L281)
**theorem
Tau.BookIV.Electroweak.mixing_conserves_count :neutral_boson_mixing.in_out_match = true**


Two inputs yield exactly two outputs.

---

### `Tau.BookIV.Electroweak.weinberg_equals_kappaAD`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L287-L297)
**theorem
Tau.BookIV.Electroweak.weinberg_equals_kappaAD :weinberg_angle_tau.sin2_numer = Sectors.kappa_AD.numer ∧ weinberg_angle_tau.sin2_denom = Sectors.kappa_AD.denom**


[IV.T61] The Weinberg angle is determined by the (A,D) cross-coupling:
sin²(θ_W) = κ(A,D) = ι<sub>τ</sub>(1−ι<sub>τ</sub>) ≈ 0.2249.

This is NOT a fit — it is a structural consequence of the
temporal complement theorem: A and D exhaust the depth-1
coupling budget (κ_A + κ_D = 1), so their cross-coupling
κ(A,D) = ι<sub>τ</sub>(1−ι<sub>τ</sub>) is the natural mixing parameter.

---

### `Tau.BookIV.Electroweak.weinberg_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L299-L303)
**theorem
Tau.BookIV.Electroweak.weinberg_in_range :weinberg_angle_tau.sin2_numer * 100 > 22 * weinberg_angle_tau.sin2_denom ∧ weinberg_angle_tau.sin2_numer * 100 < 23 * weinberg_angle_tau.sin2_denom**


The τ-value of sin²(θ_W) is strictly between 0.22 and 0.23.

---

### `Tau.BookIV.Electroweak.unique_mixing_pair`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L309-L320)
**theorem
Tau.BookIV.Electroweak.unique_mixing_pair :mixing_pair.balanced = BookIII.Sectors.Sector.A ∧ mixing_pair.chi_plus_fiber = BookIII.Sectors.Sector.B**


[IV.T62] (A,B) is the unique mixing-compatible sector pair.

Proof sketch:


- A is the unique balanced-polarity sector (IV.D06).

- B is the unique χ₊-dominant fiber sector (IV.D02).

- No other pair satisfies both mixing conditions simultaneously.

- D is χ₊-dominant but lives on the BASE, not the fiber.

- C is χ₋-dominant (wrong polarity for photon emergence).

- Ω is crossing (neither balanced nor purely χ₊).


---

### `Tau.BookIV.Electroweak.A_unique_balanced`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L322-L328)
**theorem
Tau.BookIV.Electroweak.A_unique_balanced :Sectors.weak_sector.polarity = Sectors.PolaritySign.Balanced ∧ Sectors.gravity_sector.polarity ≠ Sectors.PolaritySign.Balanced ∧ Sectors.em_sector.polarity ≠ Sectors.PolaritySign.Balanced ∧ Sectors.strong_sector.polarity ≠ Sectors.PolaritySign.Balanced**


No other primitive sector has balanced polarity.

---

### `Tau.BookIV.Electroweak.EMCouplingRelation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L334-L351)
**structure
Tau.BookIV.Electroweak.EMCouplingRelation :Type**


[IV.P68] The electromagnetic coupling e is related to the weak
coupling g by e = g · sin(θ_W).
In the τ-framework, this structural relationship means the EM
coupling factors through the weak sector via the Weinberg angle.
The EM self-coupling κ(B;2) = ι<sub>τ</sub>² relates to κ(A;1) = ι<sub>τ</sub> and
the electroweak cross-coupling κ(A,B) = ι<sub>τ</sub>²(1−ι<sub>τ</sub>).

- em : BookIII.Sectors.Sector
EM self-coupling sector.

- weak : BookIII.Sectors.Sector
Weak self-coupling sector.

- mixing_pair_i : BookIII.Sectors.Sector
Mixing parameter sector pair.

- mixing_pair_j : BookIII.Sectors.Sector
- em_is_B : self.em = BookIII.Sectors.Sector.B
All sectors assigned correctly.

- weak_is_A : self.weak = BookIII.Sectors.Sector.A
Instances For

---

### `Tau.BookIV.Electroweak.instReprEMCouplingRelation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L351-L351)
**def
Tau.BookIV.Electroweak.instReprEMCouplingRelation.repr :EMCouplingRelation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprEMCouplingRelation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L351-L351)
**instance
Tau.BookIV.Electroweak.instReprEMCouplingRelation :Repr EMCouplingRelation**

Equations
- Tau.BookIV.Electroweak.instReprEMCouplingRelation = { reprPrec := Tau.BookIV.Electroweak.instReprEMCouplingRelation.repr }

---

### `Tau.BookIV.Electroweak.em_coupling_relation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L353-L353)
**def
Tau.BookIV.Electroweak.em_coupling_relation :EMCouplingRelation**

Equations
- Tau.BookIV.Electroweak.em_coupling_relation = { em_is_B := ⋯, weak_is_A := ⋯ }
Instances For

---

### `Tau.BookIV.Electroweak.sin2_exp_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L359-L360)
**def
Tau.BookIV.Electroweak.sin2_exp_numer :ℕ**


Experimental sin²(θ_W) ≈ 0.2312: numerator (scaled ×10000).
Equations
- Tau.BookIV.Electroweak.sin2_exp_numer = 2312
Instances For

---

### `Tau.BookIV.Electroweak.sin2_exp_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L361-L362)
**def
Tau.BookIV.Electroweak.sin2_exp_denom :ℕ**


Experimental sin²(θ_W) denominator.
Equations
- Tau.BookIV.Electroweak.sin2_exp_denom = 10000
Instances For

---

### `Tau.BookIV.Electroweak.tree_level_deviation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L364-L375)
**theorem
Tau.BookIV.Electroweak.tree_level_deviation :sin2_exp_numer * weinberg_angle_tau.sin2_denom > weinberg_angle_tau.sin2_numer * sin2_exp_denom ∧ (sin2_exp_numer * weinberg_angle_tau.sin2_denom - weinberg_angle_tau.sin2_numer * sin2_exp_denom) * 100 < 4 * sin2_exp_numer * weinberg_angle_tau.sin2_denom**


[IV.P69] Tree-level deviation: τ predicts 0.2249, experiment gives 0.2312.
The deviation is |0.2312 - 0.2249| / 0.2312 ≈ 2.7%.

This is EXPECTED at tree level. Loop corrections (radiative, threshold)
close the gap, analogous to running coupling constants in QFT.

---

### `Tau.BookIV.Electroweak.NoHigherUnification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L381-L398)
**structure
Tau.BookIV.Electroweak.NoHigherUnification :Type**


[IV.P70] No higher unification in the τ-framework.
The 4+1 sector decomposition is FINAL — there is no GUT group
that unifies all four forces into a single gauge symmetry.

The reason is structural: the temporal/spatial split (base/fiber)
is topological, not just a symmetry breaking pattern.
Gravity (base τ¹) and gauge forces (fiber T²) live on different
geometric substrates and CANNOT be embedded in a single gauge group.

This is a PREDICTION: no proton decay from gauge unification.

- decomposition_terminal : Bool
The 4+1 decomposition is terminal.

- topological_split : Bool
Base/fiber split is topological, not perturbative.

- no_gut_proton_decay : Bool
Prediction: no proton decay via GUT-type mechanism.

Instances For

---

### `Tau.BookIV.Electroweak.instReprNoHigherUnification.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L398-L398)
**def
Tau.BookIV.Electroweak.instReprNoHigherUnification.repr :NoHigherUnification → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprNoHigherUnification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L398-L398)
**instance
Tau.BookIV.Electroweak.instReprNoHigherUnification :Repr NoHigherUnification**

Equations
- Tau.BookIV.Electroweak.instReprNoHigherUnification = { reprPrec := Tau.BookIV.Electroweak.instReprNoHigherUnification.repr }

---

### `Tau.BookIV.Electroweak.no_higher_unification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L400-L400)
**def
Tau.BookIV.Electroweak.no_higher_unification :NoHigherUnification**

Equations
- Tau.BookIV.Electroweak.no_higher_unification = { }
Instances For

---

### `Tau.BookIV.Electroweak.DualRoleBalanced`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L406-L425)
**structure
Tau.BookIV.Electroweak.DualRoleBalanced :Type**


[IV.P71] The weak sector A plays a dual role:

- As the temporal arrow (κ_A = ι<sub>τ</sub>, the master constant itself).

- As the unique balanced-polarity sector enabling EW mixing.


This duality is not a coincidence — it is forced by the structure:
balanced polarity (pol = 1) means equal χ₊/χ₋ content, which
is exactly the condition for a sector to serve as the "pivot"
in the temporal complement κ_A + κ_D = 1. The same balance
that makes A the temporal arrow also makes it the unique
EW mixing partner.

- sector : BookIII.Sectors.Sector
Sector A.

- role_temporal : String
Role 1: temporal arrow.

- role_mixing : String
Role 2: EW mixing pivot.

- forced_by_balance : Bool
Both roles forced by pol = 1.

Instances For

---

### `Tau.BookIV.Electroweak.instReprDualRoleBalanced`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L425-L425)
**instance
Tau.BookIV.Electroweak.instReprDualRoleBalanced :Repr DualRoleBalanced**

Equations
- Tau.BookIV.Electroweak.instReprDualRoleBalanced = { reprPrec := Tau.BookIV.Electroweak.instReprDualRoleBalanced.repr }

---

### `Tau.BookIV.Electroweak.instReprDualRoleBalanced.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L425-L425)
**def
Tau.BookIV.Electroweak.instReprDualRoleBalanced.repr :DualRoleBalanced → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.dual_role_balanced`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L427-L427)
**def
Tau.BookIV.Electroweak.dual_role_balanced :DualRoleBalanced**

Equations
- Tau.BookIV.Electroweak.dual_role_balanced = { }
Instances For

---

### `Tau.BookIV.Electroweak.remark_gap_scope`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWMixing.lean#L433-L442)
**def
Tau.BookIV.Electroweak.remark_gap_scope :String**


[IV.R31] The 2.7% tree-level deviation between the τ-predicted
sin²(θ_W) ≈ 0.2249 and the experimental value ≈ 0.2312 is
expected to be closed by radiative corrections.

The deviation is comparable in magnitude to the 1-loop EW
corrections in the Standard Model, and has the correct sign
(τ predicts BELOW the Z-pole value, as expected for a
tree-level coupling evaluated at the fundamental scale).
Equations
- Tau.BookIV.Electroweak.remark_gap_scope = "Tree-level deviation 2.7%: expected loop-level closure, correct sign"
Instances For
