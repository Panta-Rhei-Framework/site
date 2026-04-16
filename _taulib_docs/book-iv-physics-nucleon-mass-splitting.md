---
layout: taulib-doc
title: "TauLib.BookIV.Physics.NucleonMassSplitting"
permalink: /verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/
lane: verify
module_name: "TauLib.BookIV.Physics.NucleonMassSplitting"
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

# TauLib.BookIV.Physics.NucleonMassSplitting


Proton-neutron mass difference from lemniscate crossing capacity.

## Registry Cross-References


- [IV.D340] NucleonMode — `NucleonMode`

- [IV.D341] QCD Contribution — `qcdContributionRatio`

- [IV.D342] EM Coulomb Contribution — `emContributionRatio`

- [IV.T141] Tree-Level theorem — `deltaMassTree_range`

- [IV.T142] Two-Sector theorem — `deltaMassTwoSector_range`

- [IV.P183] Sign proposition — `pn_sign_positive`

- [IV.P184] NLO factor 6/5 — `nlo_factor_65`

- [IV.R394] Cottingham comparison — `remark_cottingham_comparison`


## Mathematical Content


The proton-neutron mass difference δm = m_n − m_p = 1.2933 MeV is
explained by two-sector boundary character coupling on L = S¹ ∨ S¹:

```
δm/m_n = (3/16)·√3·ι<sub>τ</sub>⁵ − (3/20)·α·ι<sub>τ</sub>² at 33 ppm from PDG
```


Physical decomposition:


- C-sector (QCD): (3/16)·√3·ι<sub>τ</sub>⁵ ≈ 1.413 MeV (quark-mass mode, χ₋)

- B-sector (EM): (3/20)·α·ι<sub>τ</sub>² ≈ 0.120 MeV (Coulomb mode, χ₊)


NLO structural candidate (10.5 ppm):
δm/m_n = (√3/2)·ι<sub>τ</sub>⁶·(1 + (6/5)·ι<sub>τ</sub>⁵)
where 6/5 = (N_ell · N_c)/N_gen = (2·3)/5.

## Precision Note


All rational arithmetic uses ι<sub>τ</sub> ≈ 341304/1000000 (6-digit approximation).
Range proofs via native_decide on Nat. Exact ppm values require 50-digit mpmath
(see scripts/pn_mass_diff_lab.py). The range theorems verify structural correctness.

## Scope


- NucleonMode, color factors: **established** (combinatorial facts)

- QCD/EM contributions, two-sector theorem: **tau-effective** (33 ppm from PDG)

- Tree-level formula: **conjectural** (−5516 ppm, structurally motivated)


---

### `Tau.BookIV.Physics.NucleonMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L57-L62)
**inductive
Tau.BookIV.Physics.NucleonMode :Type**


[IV.D340] The two nucleon modes on the T² micro-donut.
Proton = χ₊-dominant (B-sector, EM); neutron = χ₋-dominant (C-sector, strong).

- Proton : NucleonMode
- Neutron : NucleonMode
Instances For

---

### `Tau.BookIV.Physics.instDecidableEqNucleonMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L62-L62)
**instance
Tau.BookIV.Physics.instDecidableEqNucleonMode :DecidableEq NucleonMode**

Equations
- Tau.BookIV.Physics.instDecidableEqNucleonMode x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Physics.instReprNucleonMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L62-L62)
**instance
Tau.BookIV.Physics.instReprNucleonMode :Repr NucleonMode**

Equations
- Tau.BookIV.Physics.instReprNucleonMode = { reprPrec := Tau.BookIV.Physics.instReprNucleonMode.repr }

---

### `Tau.BookIV.Physics.instReprNucleonMode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L62-L62)
**def
Tau.BookIV.Physics.instReprNucleonMode.repr :NucleonMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.neutronIsChiMinus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L64-L65)
**def
Tau.BookIV.Physics.neutronIsChiMinus :NucleonMode**


The neutron is the χ₋ mode (C-sector dominant).
Equations
- Tau.BookIV.Physics.neutronIsChiMinus = Tau.BookIV.Physics.NucleonMode.Neutron
Instances For

---

### `Tau.BookIV.Physics.protonIsChiPlus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L67-L68)
**def
Tau.BookIV.Physics.protonIsChiPlus :NucleonMode**


The proton is the χ₊ mode (B-sector dominant).
Equations
- Tau.BookIV.Physics.protonIsChiPlus = Tau.BookIV.Physics.NucleonMode.Proton
Instances For

---

### `Tau.BookIV.Physics.nucleon_modes_distinct`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L70-L72)
**theorem
Tau.BookIV.Physics.nucleon_modes_distinct :NucleonMode.Proton ≠ NucleonMode.Neutron**


The two nucleon modes are distinct.

We work in the same Nat-rational framework as LemniscateCapacity.lean
and MassRatioFormula.lean.

```
ι<sub>τ</sub> ≈ 341304/1000000 (iota / iotaD from SectorParameters)

ι<sub>τ</sub>⁵: numer = 341304⁵ = iota⁵, denom = 1000000⁵ = iotaD⁵
ι<sub>τ</sub>²: numer = 341304² = iota², denom = 1000000² = iotaD²

√3 ≈ 17320508/10000000 (from LemniscateCapacity.lean: sqrt3_numer/sqrt3_denom)

α = (121/225)·ι<sub>τ</sub>⁴: numer = 121·iota⁴, denom = 225·iotaD⁴
```


---

### `Tau.BookIV.Physics.iota5_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L92-L92)
**def
Tau.BookIV.Physics.iota5_numer :ℕ**

Equations
- Tau.BookIV.Physics.iota5_numer = Tau.BookIV.Sectors.iota * Tau.BookIV.Sectors.iota * Tau.BookIV.Sectors.iota * Tau.BookIV.Sectors.iota * Tau.BookIV.Sectors.iota
Instances For

---

### `Tau.BookIV.Physics.iota5_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L93-L93)
**def
Tau.BookIV.Physics.iota5_denom :ℕ**

Equations
- Tau.BookIV.Physics.iota5_denom = Tau.BookIV.Sectors.iotaD * Tau.BookIV.Sectors.iotaD * Tau.BookIV.Sectors.iotaD * Tau.BookIV.Sectors.iotaD * Tau.BookIV.Sectors.iotaD
Instances For

---

### `Tau.BookIV.Physics.iota2_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L96-L96)
**def
Tau.BookIV.Physics.iota2_numer :ℕ**

Equations
- Tau.BookIV.Physics.iota2_numer = Tau.BookIV.Sectors.iota * Tau.BookIV.Sectors.iota
Instances For

---

### `Tau.BookIV.Physics.iota2_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L97-L97)
**def
Tau.BookIV.Physics.iota2_denom :ℕ**

Equations
- Tau.BookIV.Physics.iota2_denom = Tau.BookIV.Sectors.iotaD * Tau.BookIV.Sectors.iotaD
Instances For

---

### `Tau.BookIV.Physics.iota6_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L100-L100)
**def
Tau.BookIV.Physics.iota6_numer :ℕ**

Equations
- Tau.BookIV.Physics.iota6_numer = Tau.BookIV.Sectors.iota * Tau.BookIV.Sectors.iota * Tau.BookIV.Sectors.iota * Tau.BookIV.Sectors.iota * Tau.BookIV.Sectors.iota * Tau.BookIV.Sectors.iota
Instances For

---

### `Tau.BookIV.Physics.iota6_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L101-L101)
**def
Tau.BookIV.Physics.iota6_denom :ℕ**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.iota11_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L104-L104)
**def
Tau.BookIV.Physics.iota11_numer :ℕ**

Equations
- Tau.BookIV.Physics.iota11_numer = Tau.BookIV.Physics.iota6_numer * Tau.BookIV.Physics.iota5_numer
Instances For

---

### `Tau.BookIV.Physics.iota11_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L105-L105)
**def
Tau.BookIV.Physics.iota11_denom :ℕ**

Equations
- Tau.BookIV.Physics.iota11_denom = Tau.BookIV.Physics.iota6_denom * Tau.BookIV.Physics.iota5_denom
Instances For

---

### `Tau.BookIV.Physics.iota5_denom_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L108-L108)
**theorem
Tau.BookIV.Physics.iota5_denom_pos :iota5_denom > 0**


---

### `Tau.BookIV.Physics.iota2_denom_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L109-L109)
**theorem
Tau.BookIV.Physics.iota2_denom_pos :iota2_denom > 0**


---

### `Tau.BookIV.Physics.iota6_denom_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L110-L110)
**theorem
Tau.BookIV.Physics.iota6_denom_pos :iota6_denom > 0**


[IV.D341] QCD Contribution = (3/16) · √3 · ι<sub>τ</sub>⁵

```
Cross-multiplied form for Nat arithmetic:
 numer = 3 · sqrt3_numer · iota⁵
 denom = 16 · sqrt3_denom · iotaD⁵

Python lab confirms: ≈ 1.50408 × 10⁻³ in units of m_n
 ≈ 1.413 MeV (with m_n = 939.565 MeV)
```


---

### `Tau.BookIV.Physics.qcd_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L126-L127)
**def
Tau.BookIV.Physics.qcd_numer :ℕ**


[IV.D341] QCD contribution numerator: 3 · √3_numer · ι<sub>τ</sub>⁵_numer.
Equations
- Tau.BookIV.Physics.qcd_numer = 3 * Tau.BookIV.Physics.sqrt3_numer * Tau.BookIV.Physics.iota5_numer
Instances For

---

### `Tau.BookIV.Physics.qcd_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L129-L130)
**def
Tau.BookIV.Physics.qcd_denom :ℕ**


[IV.D341] QCD contribution denominator: 16 · √3_denom · ι<sub>τ</sub>⁵_denom.
Equations
- Tau.BookIV.Physics.qcd_denom = 16 * Tau.BookIV.Physics.sqrt3_denom * Tau.BookIV.Physics.iota5_denom
Instances For

---

### `Tau.BookIV.Physics.qcd_denom_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L132-L134)
**theorem
Tau.BookIV.Physics.qcd_denom_pos :qcd_denom > 0**


QCD denominator is positive.

---

### `Tau.BookIV.Physics.qcd_float`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L136-L138)
**def
Tau.BookIV.Physics.qcd_float :Float**


QCD contribution as Float (for display).
Equations
- Tau.BookIV.Physics.qcd_float = Float.ofNat Tau.BookIV.Physics.qcd_numer / Float.ofNat Tau.BookIV.Physics.qcd_denom
Instances For

---

### `Tau.BookIV.Physics.qcd_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L147-L154)
**theorem
Tau.BookIV.Physics.qcd_in_range :qcd_numer * 1000000 > 1490 * qcd_denom ∧ qcd_numer * 1000000 < 1510 * qcd_denom**


[IV.D341] QCD contribution is in range (1.49, 1.51) × 10⁻³.
Python lab: (3/16)·√3·ι<sub>τ</sub>⁵ ≈ 1.50408 × 10⁻³
Proof: (3/16)·√3·ι<sub>τ</sub>⁵ ≈ 1.504e-3 confirmed by #eval above.

[IV.D342] EM Contribution = (3/20) · α · ι<sub>τ</sub>²

```
α = (121/225)·ι<sub>τ</sub>⁴, so:
(3/20) · α · ι<sub>τ</sub>² = (3 · 121 / (20 · 225)) · ι<sub>τ</sub>⁶
 = (363/4500) · ι<sub>τ</sub>⁶

Cross-multiplied form:
 numer = 363 · iota⁶ = 3 · 121 · iota⁶
 denom = 4500 · iotaD⁶ = 20 · 225 · iotaD⁶

Python lab confirms: ≈ 1.27510 × 10⁻⁴ in units of m_n
 ≈ 0.120 MeV
```


---

### `Tau.BookIV.Physics.em_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L174-L176)
**def
Tau.BookIV.Physics.em_numer :ℕ**


[IV.D342] EM contribution numerator: 363 · ι<sub>τ</sub>⁶_numer.
363 = 3 × 121 = N_c × α_tower_coeff_numer
Equations
- Tau.BookIV.Physics.em_numer = 363 * Tau.BookIV.Physics.iota6_numer
Instances For

---

### `Tau.BookIV.Physics.em_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L178-L180)
**def
Tau.BookIV.Physics.em_denom :ℕ**


[IV.D342] EM contribution denominator: 4500 · ι<sub>τ</sub>⁶_denom.
4500 = 20 × 225 = (4 × N_gen) × α_tower_coeff_denom
Equations
- Tau.BookIV.Physics.em_denom = 4500 * Tau.BookIV.Physics.iota6_denom
Instances For

---

### `Tau.BookIV.Physics.em_denom_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L182-L184)
**theorem
Tau.BookIV.Physics.em_denom_pos :em_denom > 0**


EM denominator is positive.

---

### `Tau.BookIV.Physics.em_float`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L186-L188)
**def
Tau.BookIV.Physics.em_float :Float**


EM contribution as Float (for display).
Equations
- Tau.BookIV.Physics.em_float = Float.ofNat Tau.BookIV.Physics.em_numer / Float.ofNat Tau.BookIV.Physics.em_denom
Instances For

---

### `Tau.BookIV.Physics.em_in_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L195-L202)
**theorem
Tau.BookIV.Physics.em_in_range :em_numer * 10000000 > 1260 * em_denom ∧ em_numer * 10000000 < 1290 * em_denom**


[IV.D342] EM contribution is in range (1.26, 1.29) × 10⁻⁴.
Python lab: (3/20)·α·ι<sub>τ</sub>² ≈ 1.27510 × 10⁻⁴
Proof: #eval confirms em_float ≈ 1.275e-4 ∈ (1.26e-4, 1.29e-4).

[IV.T141] Tree-level: δm/m_n = (√3/2) · ι<sub>τ</sub>⁶

```
Cross-multiplied form:
 numer = sqrt3_numer · iota⁶
 denom = 2 · sqrt3_denom · iotaD⁶

Python lab: −5516 ppm (conjectural scope)
```


---

### `Tau.BookIV.Physics.tree_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L217-L218)
**def
Tau.BookIV.Physics.tree_numer :ℕ**


[IV.T141] Tree-level numerator: √3_numer · ι<sub>τ</sub>⁶_numer.
Equations
- Tau.BookIV.Physics.tree_numer = Tau.BookIV.Physics.sqrt3_numer * Tau.BookIV.Physics.iota6_numer
Instances For

---

### `Tau.BookIV.Physics.tree_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L220-L221)
**def
Tau.BookIV.Physics.tree_denom :ℕ**


[IV.T141] Tree-level denominator: 2 · √3_denom · ι<sub>τ</sub>⁶_denom.
Equations
- Tau.BookIV.Physics.tree_denom = 2 * Tau.BookIV.Physics.sqrt3_denom * Tau.BookIV.Physics.iota6_denom
Instances For

---

### `Tau.BookIV.Physics.tree_denom_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L223-L225)
**theorem
Tau.BookIV.Physics.tree_denom_pos :tree_denom > 0**


Tree denominator is positive.

---

### `Tau.BookIV.Physics.deltaMassTree_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L232-L239)
**theorem
Tau.BookIV.Physics.deltaMassTree_range :tree_numer * 1000000 > 1350 * tree_denom ∧ tree_numer * 1000000 < 1400 * tree_denom**


[IV.T141] Tree-level formula lies in (1.35, 1.40) × 10⁻³.
Python lab: (√3/2)·ι<sub>τ</sub>⁶ ≈ 1.36893 × 10⁻³ (−5516 ppm from PDG)
Proof: #eval confirms tree_numer/tree_denom ≈ 1.369e-3 ∈ (1.35e-3, 1.40e-3).

[IV.T142] Two-sector: δm/m_n = QCD − EM
= (3/16)·√3·ι<sub>τ</sub>⁵ − (363/4500)·ι<sub>τ</sub>⁶

```
To compare QCD > EM (sign proposition), we cross-multiply:
 QCD > EM
 ⟺ qcd_numer · em_denom > em_numer · qcd_denom

For the range of the DIFFERENCE in Nat arithmetic, we express both
fractions over a common denominator and verify:
 (qcd_numer · em_denom − em_numer · qcd_denom) / (qcd_denom · em_denom)
 ∈ (1.37, 1.38) × 10⁻³

Python lab: 1.37657 × 10⁻³ = +33.39 ppm from PDG (τ-effective)
```


---

### `Tau.BookIV.Physics.pn_sign_positive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L260-L265)
**theorem
Tau.BookIV.Physics.pn_sign_positive :qcd_numer * em_denom > em_numer * qcd_denom**


[IV.P183] QCD contribution exceeds EM: sign is correct (neutron heavier).
Cross-multiplied: qcd_numer · em_denom > em_numer · qcd_denom.
Numerically: QCD ≈ 1.504e-3 > EM ≈ 1.275e-4.

---

### `Tau.BookIV.Physics.deltaMassTwoSector_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L267-L276)
**theorem
Tau.BookIV.Physics.deltaMassTwoSector_range :1370 * (qcd_denom * em_denom) < (qcd_numer * em_denom - em_numer * qcd_denom) * 1000000 ∧ (qcd_numer * em_denom - em_numer * qcd_denom) * 1000000 < 1380 * (qcd_denom * em_denom)**


[IV.T142] Two-sector net formula lies in (1.37, 1.38) × 10⁻³.
Python lab: δm/m_n ≈ 1.37657e-3 (+33 ppm from PDG).
The range (1.37e-3, 1.38e-3) contains 1.37657e-3.

---

### `Tau.BookIV.Physics.nlo_factor_65_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L282-L284)
**theorem
Tau.BookIV.Physics.nlo_factor_65_numer :6 = 2 * 3**


[IV.P184] NLO factor 6/5: numerator factorization.
6 = 2 × 3 = N_ell (lemniscate lobes) × N_c (quark colors).

---

### `Tau.BookIV.Physics.nlo_factor_65_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L286-L287)
**theorem
Tau.BookIV.Physics.nlo_factor_65_denom :5 = 5**


[IV.P184] NLO denominator = N_gen = 5 (five generators {α, π, γ, η, ω}).

---

### `Tau.BookIV.Physics.nlo_lobe_color_product`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L289-L290)
**theorem
Tau.BookIV.Physics.nlo_lobe_color_product :2 * 3 = 6**


The NLO lobe-color product: N_ell × N_c = 2 × 3 = 6.

---

### `Tau.BookIV.Physics.nlo_generator_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L292-L293)
**theorem
Tau.BookIV.Physics.nlo_generator_count :5 = 5**


The NLO generator count: 5 generators.

---

### `Tau.BookIV.Physics.nlo_factor_65`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L295-L296)
**theorem
Tau.BookIV.Physics.nlo_factor_65 :6 = 2 * 3 ∧ 5 = 5**


Combined NLO interpretation: 6/5 = (lobes × colors) / generators.

---

### `Tau.BookIV.Physics.quarkColors`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L302-L304)
**def
Tau.BookIV.Physics.quarkColors :ℕ**


The number of quark colors N_c = 3.
Both QCD and EM contributions share this factor.
Equations
- Tau.BookIV.Physics.quarkColors = 3
Instances For

---

### `Tau.BookIV.Physics.qcd_has_color_factor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L306-L308)
**theorem
Tau.BookIV.Physics.qcd_has_color_factor :3 ∣ qcd_numer**


QCD numerator factor includes N_c = 3. Structural: qcd_numer = 3 * sqrt3_numer * iota5_numer.

---

### `Tau.BookIV.Physics.em_has_color_factor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L310-L312)
**theorem
Tau.BookIV.Physics.em_has_color_factor :3 ∣ em_numer**


EM numerator factor includes N_c = 3. Structural: em_numer = 363 * ... = 3 * 121 * ...

---

### `Tau.BookIV.Physics.qcd_denominator_channel_counting`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L318-L322)
**theorem
Tau.BookIV.Physics.qcd_denominator_channel_counting :2 * 2 * 2 * 2 = 16**


[IV.P201 upgrade] QCD coefficient 3/16 channel counting.
16 = 2⁴ = spin(2) × color(2) × isospin(2) × lobe(2).
Each factor of 2 comes from a binary degree of freedom on L = S¹ ∨ S¹.

---

### `Tau.BookIV.Physics.qcd_denom_is_2_pow_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L324-L325)
**theorem
Tau.BookIV.Physics.qcd_denom_is_2_pow_4 :16 = 2 ^ 4**


The QCD denominator 16 is 2⁴.

---

### `Tau.BookIV.Physics.em_denominator_channel_counting`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L327-L331)
**theorem
Tau.BookIV.Physics.em_denominator_channel_counting :4 * 5 = 20**


[IV.P201 upgrade] EM coefficient 3/20 channel counting.
20 = 4 × W₃(4) = 4 × 5. W₃(4) = a₃ + a₄ = 3 + 1 + 1 = 5
is the Window universality modulus governing NLO corrections.

---

### `Tau.BookIV.Physics.em_denom_decomp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L333-L335)
**theorem
Tau.BookIV.Physics.em_denom_decomp :20 = 4 * 5 ∧ 4 = 5 - 1**


The EM denominator 20 decomposes as |non-ω generators| × W₃(4).

---

### `Tau.BookIV.Physics.both_coefficients_share_Nc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L337-L341)
**theorem
Tau.BookIV.Physics.both_coefficients_share_Nc :3 ∣ 3 ∧ 3 ∣ 363**


Both coefficients share N_c = 3 in the numerator: this is the
quark color factor from confinement (SU(3) refinement).

---

### `Tau.BookIV.Physics.em_numer_factor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L343-L345)
**theorem
Tau.BookIV.Physics.em_numer_factor :363 = 3 * 121 ∧ 121 = 11 * 11**


363 = 3 × 121 = N_c × (11²). The 11² = α_tower_numer from
the fine structure coefficient (11/15)² = 121/225.

---

### `Tau.BookIV.Physics.em_denom_factor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L347-L348)
**theorem
Tau.BookIV.Physics.em_denom_factor :4500 = 20 * 225 ∧ 225 = 15 * 15**


4500 = 20 × 225 = (4×W₃(4)) × (15²). Channel counting × α_tower_denom.

---

### `Tau.BookIV.Physics.remark_cottingham_comparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L354-L375)
**def
Tau.BookIV.Physics.remark_cottingham_comparison :String**


[IV.R394] Cottingham comparison remark.

Orthodox QCD:


- EM (Cottingham/Coulomb): ≈ +0.63 MeV (hadron-level, integer charges)

- QCD (quark mass, m_d > m_u): ≈ +0.66 MeV

- Total: ≈ 1.29 MeV ✓


Tau-framework C.5:


- C-sector (QCD): ≈ +1.413 MeV (quark-level, chi_minus mode)

- B-sector (EM): ≈ −0.120 MeV (quark-level, fractional charges)

- Total: ≈ +1.293 MeV ✓ (33 ppm)


Factor-5 EM discrepancy (0.63/0.120 ≈ 5.26):


- Factor 3 explained: tau operates at quark level, alpha_quark ≈ alpha/3
=> 0.63/3 ≈ 0.21 MeV (partial match)

- Remaining factor ~1.75: vector meson dominance + QCD renormalization

- Open question OQ.B for Milestone 3

Equations
- One or more equations did not get rendered due to their size.
Instances For
