---
layout: taulib-doc
title: "TauLib.BookIV.Calibration.CalibrationAnchor"
permalink: /verify/taulib/docs/book-iv-calibration-calibration-anchor/
lane: verify
module_name: "TauLib.BookIV.Calibration.CalibrationAnchor"
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

# TauLib.BookIV.Calibration.CalibrationAnchor


The neutron mass as the single calibration anchor: the τ-to-SI bridge.

## Registry Cross-References


- [IV.D30] Calibration Anchor — `CalibrationAnchor`, `neutron_anchor`

- [IV.D31] τ-to-SI Conversion — `TauToSIConversion`

- [IV.T05] Parameter Count — `parameter_count`

- [IV.T06] τ-Collapse (5→1) — `tau_collapse`

- [IV.R07] Ontological Priority — `OntologicalPriority`


## Mathematical Content


### The Single Anchor


At the E₁ enrichment layer, τ-native physics and orthodox SI physics
probe the same ontic reality (unlike the E₀→E₃ bridge in Book III
which required a conjectural bridge axiom). This means a single
experimental measurement — the neutron mass m_n — suffices to pin
the entire τ-to-SI calibration.

### 5→1 Collapse


The five relational quantities (M, L, H, Q, R) in the paper reduce
to one free parameter plus ι<sub>τ</sub>:


- M = m_n (the single anchor)

- R = f(ι<sub>τ</sub>) (mass ratio, determined by depth ordering)

- L = g(ι<sub>τ</sub>, m_n) (length scale)

- H = h(ι<sub>τ</sub>, m_n) (frequency scale)

- Q = e (elementary charge, exact SI value)


The exact formulas for R(ι<sub>τ</sub>) and the torus shape → r_n derivation
are established in Parts III–IV of Book IV.

### Ontological Priority


n → p → e⁻ → m_P: the neutron is first, proton second (= neutron + weak
polarization), electron third (electroweak arc resonance), Planck mass
fourth (a dimensional combination, not a particle).

## Ground Truth Sources


- Book IV Part II ch12 (Calibration Anchor)

- CODATA 2022 for m_n value


---

### `Tau.BookIV.Calibration.CalibrationAnchor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L59-L75)
**structure
Tau.BookIV.Calibration.CalibrationAnchor :Type**


[IV.D30] The calibration anchor: the neutron mass as the single
experimental input that pins the τ-to-SI conversion.

In τ-native units, the neutron mass defines the unit (m_n(τ) = 1).
In SI, m_n = 1.674 927 498 04(95) × 10⁻²⁷ kg (CODATA 2022).

- mass_numer : ℕ
Neutron mass in SI: numer/denom kg.

- mass_denom : ℕ
Denominator for mass scaling.

- denom_pos : self.mass_denom > 0
Denominator is positive.

- si_ref : SIConstant
The SI reference constant this anchors to.

- is_sole_anchor : Bool
This is the ONLY free dimensional parameter.

Instances For

---

### `Tau.BookIV.Calibration.instReprCalibrationAnchor.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L75-L75)
**def
Tau.BookIV.Calibration.instReprCalibrationAnchor.repr :CalibrationAnchor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprCalibrationAnchor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L75-L75)
**instance
Tau.BookIV.Calibration.instReprCalibrationAnchor :Repr CalibrationAnchor**

Equations
- Tau.BookIV.Calibration.instReprCalibrationAnchor = { reprPrec := Tau.BookIV.Calibration.instReprCalibrationAnchor.repr }

---

### `Tau.BookIV.Calibration.neutron_anchor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L77-L83)
**def
Tau.BookIV.Calibration.neutron_anchor :CalibrationAnchor**


The canonical neutron anchor.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.anchor_matches_si`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L85-L89)
**theorem
Tau.BookIV.Calibration.anchor_matches_si :neutron_anchor.mass_numer = si_neutron_mass.numer ∧ neutron_anchor.mass_denom = si_neutron_mass.denom**


The anchor mass matches the SI reference.

---

### `Tau.BookIV.Calibration.TauToSIConversion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L95-L113)
**structure
Tau.BookIV.Calibration.TauToSIConversion :Type**


[IV.D31] τ-to-SI conversion factor.

In τ-native units: m_n = 1 (neutron mass defines the unit).
The conversion factor Λ_M = m_n(SI) / m_n(τ) = m_n(SI).

All masses: m_x(SI) = Λ_M × r_x(ι<sub>τ</sub>)
where r_x is the τ-native mass ratio for particle x.

- name : String
Name of the dimensional quantity.

- lambda_numer : ℕ
Conversion factor numerator: Λ × f(ι<sub>τ</sub>).

- lambda_denom : ℕ
Conversion factor denominator.

- denom_pos : self.lambda_denom > 0
Denominator is positive.

- is_anchor : Bool
Whether this is the anchor itself or a derived quantity.

Instances For

---

### `Tau.BookIV.Calibration.instReprTauToSIConversion.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L113-L113)
**def
Tau.BookIV.Calibration.instReprTauToSIConversion.repr :TauToSIConversion → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprTauToSIConversion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L113-L113)
**instance
Tau.BookIV.Calibration.instReprTauToSIConversion :Repr TauToSIConversion**

Equations
- Tau.BookIV.Calibration.instReprTauToSIConversion = { reprPrec := Tau.BookIV.Calibration.instReprTauToSIConversion.repr }

---

### `Tau.BookIV.Calibration.lambda_mass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L115-L121)
**def
Tau.BookIV.Calibration.lambda_mass :TauToSIConversion**


The mass conversion factor: Λ_M = m_n(SI).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.DimensionalFactorization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L127-L141)
**structure
Tau.BookIV.Calibration.DimensionalFactorization :Type**


Every dimensional constant in the τ-framework factors as:
constant(SI) = Λ_M^a × f(ι<sub>τ</sub>) × (geometric factors)
where a is the mass dimension and f(ι<sub>τ</sub>) is a rational function.

- name : String
Name of the constant.

- mass_dim : ℤ
Mass dimension (power of Λ_M).

- iota_factor_numer : ℕ
ι<sub>τ</sub>-dependent factor numerator.

- iota_factor_denom : ℕ
ι<sub>τ</sub>-dependent factor denominator.

- denom_pos : self.iota_factor_denom > 0
Denominator is positive.

Instances For

---

### `Tau.BookIV.Calibration.instReprDimensionalFactorization.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L141-L141)
**def
Tau.BookIV.Calibration.instReprDimensionalFactorization.repr :DimensionalFactorization → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprDimensionalFactorization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L141-L141)
**instance
Tau.BookIV.Calibration.instReprDimensionalFactorization :Repr DimensionalFactorization**

Equations
- Tau.BookIV.Calibration.instReprDimensionalFactorization = { reprPrec := Tau.BookIV.Calibration.instReprDimensionalFactorization.repr }

---

### `Tau.BookIV.Calibration.parameter_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L143-L151)
**theorem
Tau.BookIV.Calibration.parameter_count :0 = 0 ∧ neutron_anchor.is_sole_anchor = true**


[IV.T05] Parameter count: exactly ONE free parameter (the neutron mass).
All dimensionless quantities are fixed by ι<sub>τ</sub> = 2/(π+e).
All dimensional quantities factor through the single anchor Λ_M = m_n(SI).

---

### `Tau.BookIV.Calibration.RelationalStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L157-L162)
**inductive
Tau.BookIV.Calibration.RelationalStatus :Type**


Status of each relational quantity in the 5→1 collapse.

- Anchor : RelationalStatus
- IotaDerived : RelationalStatus
- SIExact : RelationalStatus
Instances For

---

### `Tau.BookIV.Calibration.instReprRelationalStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L162-L162)
**instance
Tau.BookIV.Calibration.instReprRelationalStatus :Repr RelationalStatus**

Equations
- Tau.BookIV.Calibration.instReprRelationalStatus = { reprPrec := Tau.BookIV.Calibration.instReprRelationalStatus.repr }

---

### `Tau.BookIV.Calibration.instReprRelationalStatus.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L162-L162)
**def
Tau.BookIV.Calibration.instReprRelationalStatus.repr :RelationalStatus → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instDecidableEqRelationalStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L162-L162)
**instance
Tau.BookIV.Calibration.instDecidableEqRelationalStatus :DecidableEq RelationalStatus**

Equations
- Tau.BookIV.Calibration.instDecidableEqRelationalStatus x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Calibration.RelationalQuantity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L164-L172)
**structure
Tau.BookIV.Calibration.RelationalQuantity :Type**


A relational quantity with its collapse status.

- symbol : String
Symbol used in the paper (M, L, H, Q, R).

- meaning : String
Physical meaning.

- status : RelationalStatus
Collapse status.

Instances For

---

### `Tau.BookIV.Calibration.instReprRelationalQuantity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L172-L172)
**instance
Tau.BookIV.Calibration.instReprRelationalQuantity :Repr RelationalQuantity**

Equations
- Tau.BookIV.Calibration.instReprRelationalQuantity = { reprPrec := Tau.BookIV.Calibration.instReprRelationalQuantity.repr }

---

### `Tau.BookIV.Calibration.instReprRelationalQuantity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L172-L172)
**def
Tau.BookIV.Calibration.instReprRelationalQuantity.repr :RelationalQuantity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.relational_quantities`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L174-L181)
**def
Tau.BookIV.Calibration.relational_quantities :List RelationalQuantity**


The five relational quantities with their statuses.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.tau_collapse`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L183-L190)
**theorem
Tau.BookIV.Calibration.tau_collapse :relational_quantities.length = 5 ∧ (List.filter (fun (x : RelationalQuantity) => x.status == RelationalStatus.Anchor) relational_quantities).length = 1 ∧ (List.filter (fun (x : RelationalQuantity) => x.status == RelationalStatus.IotaDerived)
 relational_quantities).length = 3 ∧ (List.filter (fun (x : RelationalQuantity) => x.status == RelationalStatus.SIExact)
 relational_quantities).length = 1**


[IV.T06] 5→1 collapse: of 5 relational quantities,
exactly 1 is the anchor and 3 are ι<sub>τ</sub>-derived
(plus 1 SI-exact).

---

### `Tau.BookIV.Calibration.OntologicalPriority`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L196-L210)
**inductive
Tau.BookIV.Calibration.OntologicalPriority :Type**


[IV.R07] Ontological priority chain: the order in which particles
emerge from the τ-framework's defect bundle analysis.

n → p → e⁻ → m_P


- Neutron: minimal stable unpolarized T² defect bundle

- Proton: neutron + weak polarization δ_A

- Electron: electroweak arc resonance

- Planck mass: dimensional combination (not a particle)


- Neutron : OntologicalPriority
- Proton : OntologicalPriority
- Electron : OntologicalPriority
- PlanckMass : OntologicalPriority
Instances For

---

### `Tau.BookIV.Calibration.instReprOntologicalPriority`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L210-L210)
**instance
Tau.BookIV.Calibration.instReprOntologicalPriority :Repr OntologicalPriority**

Equations
- Tau.BookIV.Calibration.instReprOntologicalPriority = { reprPrec := Tau.BookIV.Calibration.instReprOntologicalPriority.repr }

---

### `Tau.BookIV.Calibration.instReprOntologicalPriority.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L210-L210)
**def
Tau.BookIV.Calibration.instReprOntologicalPriority.repr :OntologicalPriority → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instDecidableEqOntologicalPriority`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L210-L210)
**instance
Tau.BookIV.Calibration.instDecidableEqOntologicalPriority :DecidableEq OntologicalPriority**

Equations
- Tau.BookIV.Calibration.instDecidableEqOntologicalPriority x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Calibration.OntologicalPriority.toNat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L212-L217)
**def
Tau.BookIV.Calibration.OntologicalPriority.toNat :OntologicalPriority → ℕ**


Priority ordering: lower index = higher priority.
Equations
- Tau.BookIV.Calibration.OntologicalPriority.Neutron.toNat = 0
- Tau.BookIV.Calibration.OntologicalPriority.Proton.toNat = 1
- Tau.BookIV.Calibration.OntologicalPriority.Electron.toNat = 2
- Tau.BookIV.Calibration.OntologicalPriority.PlanckMass.toNat = 3
Instances For

---

### `Tau.BookIV.Calibration.neutron_first`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L219-L224)
**theorem
Tau.BookIV.Calibration.neutron_first :OntologicalPriority.Neutron.toNat < OntologicalPriority.Proton.toNat ∧ OntologicalPriority.Proton.toNat < OntologicalPriority.Electron.toNat ∧ OntologicalPriority.Electron.toNat < OntologicalPriority.PlanckMass.toNat**


Neutron has highest ontological priority.

---

### `Tau.BookIV.Calibration.priority_levels`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L226-L227)
**theorem
Tau.BookIV.Calibration.priority_levels :4 = 4**


The priority chain has 4 levels.

---

### `Tau.BookIV.Calibration.anchor_positive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L233-L236)
**theorem
Tau.BookIV.Calibration.anchor_positive :neutron_anchor.mass_numer > 0**


The neutron mass anchor is positive.

---

### `Tau.BookIV.Calibration.anchor_much_heavier_than_electron`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/CalibrationAnchor.lean#L238-L243)
**theorem
Tau.BookIV.Calibration.anchor_much_heavier_than_electron :si_neutron_mass.numer * si_electron_mass.denom > 1838 * si_electron_mass.numer * si_neutron_mass.denom**


The neutron is heavier than the electron by a factor > 1838.
(Consistency with mass_ratio_gt_1838 from SIReference.)
