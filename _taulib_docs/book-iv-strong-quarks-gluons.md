---
layout: taulib-doc
title: "TauLib.BookIV.Strong.QuarksGluons"
permalink: /verify/taulib/docs/book-iv-strong-quarks-gluons/
lane: verify
module_name: "TauLib.BookIV.Strong.QuarksGluons"
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

# TauLib.BookIV.Strong.QuarksGluons


Quark flavors, gluon fields, confinement in hadrons, jets,
baryon-meson classification, quark generations, asymptotic freedom.

## Registry Cross-References


- [IV.D187] Quark Mode — `QuarkMode`

- [IV.D188] Antiquark Mode — `AntiquarkMode`

- [IV.D189] Quark Generations from Lemniscate — `QuarkGenerations`

- [IV.D190] Meson State — `MesonState`

- [IV.D191] Baryon State — `BaryonState`

- [IV.P113] Quark Electric Charges — `quark_charges`

- [IV.P114] Generation Mass Ordering — `generation_mass_ordering` (conjectural)

- [IV.P115] Gluon Count — `gluon_count`

- [IV.P116] Gluon Self-interaction Vertices — `gluon_vertices`

- [IV.P117] Structural Asymptotic Freedom — `structural_af`

- [IV.P118] Asymptotic Freedom from N_c and N_f — `af_from_nc_nf`

- [IV.R92-R98] Structural remarks (comment-only)


## Mathematical Content


Quarks are character modes with fractional eta-winding (n not equiv 0 mod 3).
Electric charges -1/3 and +2/3 arise from the ternary structure.
Three generations come from three lemniscate mode classes (crossing,
single-lobe, full-L). Eight gluons from dim su(3) = 3^2 - 1 = 8.
Mesons (q-qbar) and baryons (qqq) are the minimal color singlets.

## Ground Truth Sources


- Chapter 43 of Book IV (2nd Edition)


---

### `Tau.BookIV.Strong.QuarkType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L45-L51)
**inductive
Tau.BookIV.Strong.QuarkType :Type**


Quark type: up-type (charge +2/3) or down-type (charge -1/3).

- up : QuarkType
Up-type: n equiv 2 mod 3, charge +2/3.

- down : QuarkType
Down-type: n equiv 1 mod 3, charge -1/3.

Instances For

---

### `Tau.BookIV.Strong.instReprQuarkType.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L51-L51)
**def
Tau.BookIV.Strong.instReprQuarkType.repr :QuarkType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprQuarkType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L51-L51)
**instance
Tau.BookIV.Strong.instReprQuarkType :Repr QuarkType**

Equations
- Tau.BookIV.Strong.instReprQuarkType = { reprPrec := Tau.BookIV.Strong.instReprQuarkType.repr }

---

### `Tau.BookIV.Strong.instDecidableEqQuarkType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L51-L51)
**instance
Tau.BookIV.Strong.instDecidableEqQuarkType :DecidableEq QuarkType**

Equations
- Tau.BookIV.Strong.instDecidableEqQuarkType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Strong.instBEqQuarkType`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L51-L51)
**instance
Tau.BookIV.Strong.instBEqQuarkType :BEq QuarkType**

Equations
- Tau.BookIV.Strong.instBEqQuarkType = { beq := Tau.BookIV.Strong.instBEqQuarkType.beq }

---

### `Tau.BookIV.Strong.instBEqQuarkType.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L51-L51)
**def
Tau.BookIV.Strong.instBEqQuarkType.beq :QuarkType → QuarkType → Bool**

Equations
- Tau.BookIV.Strong.instBEqQuarkType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Strong.QuarkMode`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L53-L67)
**structure
Tau.BookIV.Strong.QuarkMode :Type**


[IV.D187] A quark mode: character mode chi_{m,n} on T^2 with
n not equiv 0 mod 3, carrying color class c = n mod 3.
Cannot exist as isolated state by the Confinement Theorem.

- gamma_winding : ℤ
Gamma-winding (EM component).

- eta_winding : ℤ
Eta-winding (strong component, not divisible by 3).

- quark_type : QuarkType
Quark type derived from eta_winding mod 3.

- generation : ℕ
Generation (1, 2, or 3).

- gen_valid : self.generation ≥ 1 ∧ self.generation ≤ 3
Generation is valid.

Instances For

---

### `Tau.BookIV.Strong.instReprQuarkMode.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L67-L67)
**def
Tau.BookIV.Strong.instReprQuarkMode.repr :QuarkMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprQuarkMode`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L67-L67)
**instance
Tau.BookIV.Strong.instReprQuarkMode :Repr QuarkMode**

Equations
- Tau.BookIV.Strong.instReprQuarkMode = { reprPrec := Tau.BookIV.Strong.instReprQuarkMode.repr }

---

### `Tau.BookIV.Strong.QuarkChargeSpec`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L73-L85)
**structure
Tau.BookIV.Strong.QuarkChargeSpec :Type**


[IV.P113] Quark electric charges from the ternary structure:


- d-type (n equiv 1 mod 3): Q = -1/3 e

- u-type (n equiv 2 mod 3): Q = +2/3 e


Charges are given as (numerator, denominator) pairs.

- quark_type : QuarkType
Quark type.

- charge_numer : ℤ
Charge numerator.

- charge_denom : ℕ
Charge denominator.

Instances For

---

### `Tau.BookIV.Strong.instReprQuarkChargeSpec.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L85-L85)
**def
Tau.BookIV.Strong.instReprQuarkChargeSpec.repr :QuarkChargeSpec → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprQuarkChargeSpec`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L85-L85)
**instance
Tau.BookIV.Strong.instReprQuarkChargeSpec :Repr QuarkChargeSpec**

Equations
- Tau.BookIV.Strong.instReprQuarkChargeSpec = { reprPrec := Tau.BookIV.Strong.instReprQuarkChargeSpec.repr }

---

### `Tau.BookIV.Strong.down_type_charge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L87-L89)
**def
Tau.BookIV.Strong.down_type_charge :QuarkChargeSpec**

Equations
- Tau.BookIV.Strong.down_type_charge = { quark_type := Tau.BookIV.Strong.QuarkType.down, charge_numer := -1 }
Instances For

---

### `Tau.BookIV.Strong.up_type_charge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L91-L93)
**def
Tau.BookIV.Strong.up_type_charge :QuarkChargeSpec**

Equations
- Tau.BookIV.Strong.up_type_charge = { quark_type := Tau.BookIV.Strong.QuarkType.up, charge_numer := 2 }
Instances For

---

### `Tau.BookIV.Strong.down_charge_minus_third`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L95-L99)
**theorem
Tau.BookIV.Strong.down_charge_minus_third :down_type_charge.charge_numer = -1 ∧ down_type_charge.charge_denom = 3**


Down-type charge is -1/3.

---

### `Tau.BookIV.Strong.up_charge_plus_two_thirds`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L101-L105)
**theorem
Tau.BookIV.Strong.up_charge_plus_two_thirds :up_type_charge.charge_numer = 2 ∧ up_type_charge.charge_denom = 3**


Up-type charge is +2/3.

---

### `Tau.BookIV.Strong.ud_charge_sum`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L107-L110)
**theorem
Tau.BookIV.Strong.ud_charge_sum :up_type_charge.charge_numer + down_type_charge.charge_numer = 1**


Charge sum of u + d = 2/3 + (-1/3) = 1/3.

---

### `Tau.BookIV.Strong.proton_charge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L112-L116)
**theorem
Tau.BookIV.Strong.proton_charge :up_type_charge.charge_numer + up_type_charge.charge_numer + down_type_charge.charge_numer = 3**


Charge sum of u + u + d = 2/3 + 2/3 + (-1/3) = 3/3 = 1 (proton).

---

### `Tau.BookIV.Strong.neutron_charge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L118-L122)
**theorem
Tau.BookIV.Strong.neutron_charge :up_type_charge.charge_numer + down_type_charge.charge_numer + down_type_charge.charge_numer = 0**


Charge sum of u + d + d = 2/3 + (-1/3) + (-1/3) = 0 (neutron).

---

### `Tau.BookIV.Strong.AntiquarkMode`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L128-L139)
**structure
Tau.BookIV.Strong.AntiquarkMode :Type**


[IV.D188] Antiquark: conjugate mode bar{chi}*{m,n} = chi*{-m,-n}
with reversed color class and reversed electric charge.

- gamma_winding : ℤ
Reversed gamma-winding.

- eta_winding : ℤ
Reversed eta-winding.

- anti_type : QuarkType
Anti-quark type (opposite of quark).

- generation : ℕ
Generation (same as the quark).

Instances For

---

### `Tau.BookIV.Strong.instReprAntiquarkMode.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L139-L139)
**def
Tau.BookIV.Strong.instReprAntiquarkMode.repr :AntiquarkMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprAntiquarkMode`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L139-L139)
**instance
Tau.BookIV.Strong.instReprAntiquarkMode :Repr AntiquarkMode**

Equations
- Tau.BookIV.Strong.instReprAntiquarkMode = { reprPrec := Tau.BookIV.Strong.instReprAntiquarkMode.repr }

---

### `Tau.BookIV.Strong.quark_to_antiquark`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L141-L148)
**def
Tau.BookIV.Strong.quark_to_antiquark
(q : QuarkMode)
 :AntiquarkMode**


Construct antiquark from quark.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.LemniscateModeClass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L154-L162)
**inductive
Tau.BookIV.Strong.LemniscateModeClass :Type**


Lemniscate mode class determining the generation.

- crossing : LemniscateModeClass
Crossing-point modes: lightest (Generation 1).

- singleLobe : LemniscateModeClass
Single-lobe modes: intermediate (Generation 2).

- fullL : LemniscateModeClass
Full-lemniscate modes: heaviest (Generation 3).

Instances For

---

### `Tau.BookIV.Strong.instReprLemniscateModeClass.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L162-L162)
**def
Tau.BookIV.Strong.instReprLemniscateModeClass.repr :LemniscateModeClass → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprLemniscateModeClass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L162-L162)
**instance
Tau.BookIV.Strong.instReprLemniscateModeClass :Repr LemniscateModeClass**

Equations
- Tau.BookIV.Strong.instReprLemniscateModeClass = { reprPrec := Tau.BookIV.Strong.instReprLemniscateModeClass.repr }

---

### `Tau.BookIV.Strong.instDecidableEqLemniscateModeClass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L162-L162)
**instance
Tau.BookIV.Strong.instDecidableEqLemniscateModeClass :DecidableEq LemniscateModeClass**

Equations
- Tau.BookIV.Strong.instDecidableEqLemniscateModeClass x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Strong.instBEqLemniscateModeClass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L162-L162)
**instance
Tau.BookIV.Strong.instBEqLemniscateModeClass :BEq LemniscateModeClass**

Equations
- Tau.BookIV.Strong.instBEqLemniscateModeClass = { beq := Tau.BookIV.Strong.instBEqLemniscateModeClass.beq }

---

### `Tau.BookIV.Strong.instBEqLemniscateModeClass.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L162-L162)
**def
Tau.BookIV.Strong.instBEqLemniscateModeClass.beq :LemniscateModeClass → LemniscateModeClass → Bool**

Equations
- Tau.BookIV.Strong.instBEqLemniscateModeClass.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Strong.QuarkGenerations`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L164-L177)
**structure
Tau.BookIV.Strong.QuarkGenerations :Type**


[IV.D189] Three quark generations from three lemniscate mode classes:
Gen 1 (u,d) = crossing-point modes
Gen 2 (c,s) = single-lobe modes
Gen 3 (t,b) = full-lemniscate modes

- num_generations : ℕ
Number of generations.

- gen1_class : LemniscateModeClass
Generation 1: crossing-point.

- gen2_class : LemniscateModeClass
Generation 2: single-lobe.

- gen3_class : LemniscateModeClass
Generation 3: full-lemniscate.

Instances For

---

### `Tau.BookIV.Strong.instReprQuarkGenerations`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L177-L177)
**instance
Tau.BookIV.Strong.instReprQuarkGenerations :Repr QuarkGenerations**

Equations
- Tau.BookIV.Strong.instReprQuarkGenerations = { reprPrec := Tau.BookIV.Strong.instReprQuarkGenerations.repr }

---

### `Tau.BookIV.Strong.instReprQuarkGenerations.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L177-L177)
**def
Tau.BookIV.Strong.instReprQuarkGenerations.repr :QuarkGenerations → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.quark_generations`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L179-L179)
**def
Tau.BookIV.Strong.quark_generations :QuarkGenerations**

Equations
- Tau.BookIV.Strong.quark_generations = { }
Instances For

---

### `Tau.BookIV.Strong.three_generations`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L181-L182)
**theorem
Tau.BookIV.Strong.three_generations :quark_generations.num_generations = 3**


---

### `Tau.BookIV.Strong.mode_classes_distinct`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L184-L189)
**theorem
Tau.BookIV.Strong.mode_classes_distinct :quark_generations.gen1_class ≠ quark_generations.gen2_class ∧ quark_generations.gen2_class ≠ quark_generations.gen3_class ∧ quark_generations.gen1_class ≠ quark_generations.gen3_class**


All three mode classes are distinct.

---

### `Tau.BookIV.Strong.GenerationMassOrdering`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L195-L207)
**structure
Tau.BookIV.Strong.GenerationMassOrdering :Type**


[IV.P114] Generation mass ordering (conjectural):
lambda_crossing < lambda_singleLobe < lambda_fullL
=> m_u < m_c < m_t and m_d < m_s < m_b.

Scope: conjectural (quantitative mass ratios not yet derived).

- follows_eigenvalue : Bool
Mass ordering follows breathing eigenvalue ordering.

- scope : String
Scope: tau-effective.

- hierarchy : String
Qualitative hierarchy: crossing < singleLobe < fullL.

Instances For

---

### `Tau.BookIV.Strong.instReprGenerationMassOrdering.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L207-L207)
**def
Tau.BookIV.Strong.instReprGenerationMassOrdering.repr :GenerationMassOrdering → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprGenerationMassOrdering`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L207-L207)
**instance
Tau.BookIV.Strong.instReprGenerationMassOrdering :Repr GenerationMassOrdering**

Equations
- Tau.BookIV.Strong.instReprGenerationMassOrdering = { reprPrec := Tau.BookIV.Strong.instReprGenerationMassOrdering.repr }

---

### `Tau.BookIV.Strong.generation_mass_ordering`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L209-L209)
**def
Tau.BookIV.Strong.generation_mass_ordering :GenerationMassOrdering**

Equations
- Tau.BookIV.Strong.generation_mass_ordering = { }
Instances For

---

### `Tau.BookIV.Strong.GluonCount`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L215-L224)
**structure
Tau.BookIV.Strong.GluonCount :Type**


[IV.P115] Exactly 8 independent gluon connection modes:
dim_R su(3) = 3^2 - 1 = 8.

- count : ℕ
Number of gluon types.

- formula : String
Formula: N_c^2 - 1.

- basis_elements : Bool
Each basis element = independent gluon.

Instances For

---

### `Tau.BookIV.Strong.instReprGluonCount.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L224-L224)
**def
Tau.BookIV.Strong.instReprGluonCount.repr :GluonCount → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprGluonCount`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L224-L224)
**instance
Tau.BookIV.Strong.instReprGluonCount :Repr GluonCount**

Equations
- Tau.BookIV.Strong.instReprGluonCount = { reprPrec := Tau.BookIV.Strong.instReprGluonCount.repr }

---

### `Tau.BookIV.Strong.gluon_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L226-L226)
**def
Tau.BookIV.Strong.gluon_count :GluonCount**

Equations
- Tau.BookIV.Strong.gluon_count = { }
Instances For

---

### `Tau.BookIV.Strong.eight_gluons`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L228-L228)
**theorem
Tau.BookIV.Strong.eight_gluons :gluon_count.count = 8**


---

### `Tau.BookIV.Strong.gluon_dim_formula`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L230-L231)
**theorem
Tau.BookIV.Strong.gluon_dim_formula :3 ^ 2 - 1 = 8**


Verify 3^2 - 1 = 8.

---

### `Tau.BookIV.Strong.GluonVertices`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L237-L248)
**structure
Tau.BookIV.Strong.GluonVertices :Type**


[IV.P116] Two self-interaction vertices from non-abelian field strength:


- Three-gluon vertex: proportional to g_s f_{abc}

- Four-gluon vertex: proportional to g_s^2 f_{abe} f_{cde}
These produce jet events and are the structural origin of confinement.


- three_vertex : Bool
Three-gluon vertex (from [A_mu, A_nu] commutator).

- four_vertex : Bool
Four-gluon vertex (from [A,A]^2 term).

- vertex_types : ℕ
Total self-interaction vertex types.

Instances For

---

### `Tau.BookIV.Strong.instReprGluonVertices`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L248-L248)
**instance
Tau.BookIV.Strong.instReprGluonVertices :Repr GluonVertices**

Equations
- Tau.BookIV.Strong.instReprGluonVertices = { reprPrec := Tau.BookIV.Strong.instReprGluonVertices.repr }

---

### `Tau.BookIV.Strong.instReprGluonVertices.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L248-L248)
**def
Tau.BookIV.Strong.instReprGluonVertices.repr :GluonVertices → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.gluon_vertices`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L250-L250)
**def
Tau.BookIV.Strong.gluon_vertices :GluonVertices**

Equations
- Tau.BookIV.Strong.gluon_vertices = { }
Instances For

---

### `Tau.BookIV.Strong.two_vertex_types`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L252-L252)
**theorem
Tau.BookIV.Strong.two_vertex_types :gluon_vertices.vertex_types = 2**


---

### `Tau.BookIV.Strong.StructuralAF`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L258-L267)
**structure
Tau.BookIV.Strong.StructuralAF :Type**


[IV.P117] The C-sector readout R_C(n) is monotonically decreasing
with refinement depth n => alpha_s^eff(n) decreases at high energy.

- monotone_decreasing : Bool
Readout monotonically decreasing.

- coupling_decreases : Bool
Effective coupling decreases at high energy.

- source : String
Source: chi_minus spectral tightening.

Instances For

---

### `Tau.BookIV.Strong.instReprStructuralAF`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L267-L267)
**instance
Tau.BookIV.Strong.instReprStructuralAF :Repr StructuralAF**

Equations
- Tau.BookIV.Strong.instReprStructuralAF = { reprPrec := Tau.BookIV.Strong.instReprStructuralAF.repr }

---

### `Tau.BookIV.Strong.instReprStructuralAF.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L267-L267)
**def
Tau.BookIV.Strong.instReprStructuralAF.repr :StructuralAF → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.structural_af`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L269-L269)
**def
Tau.BookIV.Strong.structural_af :StructuralAF**

Equations
- Tau.BookIV.Strong.structural_af = { }
Instances For

---

### `Tau.BookIV.Strong.AFFromNcNf`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L275-L287)
**structure
Tau.BookIV.Strong.AFFromNcNf :Type**


[IV.P118] N_c = 3 and N_f = 6 satisfy the asymptotic freedom
condition: N_f < 11*N_c/2 = 16.5.
6 < 16.5: true. (Or equivalently, 2*N_f < 11*N_c: 12 < 33.)

- nc : ℕ
N_c = 3.

- nf : ℕ
N_f = 6 (u,d,c,s,t,b).

- condition_holds : Bool
2*N_f < 11*N_c.

- agreement : String
Both tau and orthodox agree.

Instances For

---

### `Tau.BookIV.Strong.instReprAFFromNcNf.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L287-L287)
**def
Tau.BookIV.Strong.instReprAFFromNcNf.repr :AFFromNcNf → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprAFFromNcNf`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L287-L287)
**instance
Tau.BookIV.Strong.instReprAFFromNcNf :Repr AFFromNcNf**

Equations
- Tau.BookIV.Strong.instReprAFFromNcNf = { reprPrec := Tau.BookIV.Strong.instReprAFFromNcNf.repr }

---

### `Tau.BookIV.Strong.af_from_nc_nf`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L289-L289)
**def
Tau.BookIV.Strong.af_from_nc_nf :AFFromNcNf**

Equations
- Tau.BookIV.Strong.af_from_nc_nf = { }
Instances For

---

### `Tau.BookIV.Strong.af_condition`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L291-L293)
**theorem
Tau.BookIV.Strong.af_condition :2 * af_from_nc_nf.nf < 11 * af_from_nc_nf.nc**


2 * 6 < 11 * 3 (asymptotic freedom).

---

### `Tau.BookIV.Strong.six_flavors`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L295-L296)
**theorem
Tau.BookIV.Strong.six_flavors :af_from_nc_nf.nf = 6**


N_f = 6: exactly 6 quark flavors.

---

### `Tau.BookIV.Strong.MesonState`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L302-L315)
**structure
Tau.BookIV.Strong.MesonState :Type**


[IV.D190] A meson: composite |q qbar> with total color 0 mod 3.
Minimal mesonic singlet: one quark + one antiquark.

- quark_flavor : String
Quark flavor.

- antiquark_flavor : String
Antiquark flavor.

- quark_color : ℕ
Quark color class.

- antiquark_color : ℕ
Antiquark color class (must complement quark).

- is_singlet : Bool
Color singlet condition.

Instances For

---

### `Tau.BookIV.Strong.instReprMesonState.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L315-L315)
**def
Tau.BookIV.Strong.instReprMesonState.repr :MesonState → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprMesonState`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L315-L315)
**instance
Tau.BookIV.Strong.instReprMesonState :Repr MesonState**

Equations
- Tau.BookIV.Strong.instReprMesonState = { reprPrec := Tau.BookIV.Strong.instReprMesonState.repr }

---

### `Tau.BookIV.Strong.mk_meson`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L317-L323)
**def
Tau.BookIV.Strong.mk_meson
(q_flavor aq_flavor : String)

(q_color : ℕ)
 :MesonState**


Construct a meson from quark and antiquark color windings.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.pi_plus`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L325-L326)
**def
Tau.BookIV.Strong.pi_plus :MesonState**


Example: pi+ meson (u dbar).
Equations
- Tau.BookIV.Strong.pi_plus = Tau.BookIV.Strong.mk_meson "u" "dbar" 1
Instances For

---

### `Tau.BookIV.Strong.pi_plus_singlet`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L328-L329)
**theorem
Tau.BookIV.Strong.pi_plus_singlet :pi_plus.is_singlet = true**


Pi+ is a color singlet.

---

### `Tau.BookIV.Strong.BaryonState`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L335-L348)
**structure
Tau.BookIV.Strong.BaryonState :Type**


[IV.D191] A baryon: composite |q_r q_g q_b> with three quarks,
pairwise distinct colors {0,1,2}, total color 0 mod 3.

- flavor_1 : String
Three quark flavors.

- flavor_2 : String
- flavor_3 : String
- color_1 : ℕ
Three color classes (must be {0,1,2}).

- color_2 : ℕ
- color_3 : ℕ
- is_singlet : Bool
Total color mod 3 = 0.

Instances For

---

### `Tau.BookIV.Strong.instReprBaryonState.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L348-L348)
**def
Tau.BookIV.Strong.instReprBaryonState.repr :BaryonState → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprBaryonState`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L348-L348)
**instance
Tau.BookIV.Strong.instReprBaryonState :Repr BaryonState**

Equations
- Tau.BookIV.Strong.instReprBaryonState = { reprPrec := Tau.BookIV.Strong.instReprBaryonState.repr }

---

### `Tau.BookIV.Strong.proton_state`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L350-L354)
**def
Tau.BookIV.Strong.proton_state :BaryonState**


Proton: u(red) u(green) d(blue).
Equations
- Tau.BookIV.Strong.proton_state = { flavor_1 := "u", flavor_2 := "u", flavor_3 := "d" }
Instances For

---

### `Tau.BookIV.Strong.neutron_state`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L356-L360)
**def
Tau.BookIV.Strong.neutron_state :BaryonState**


Neutron: u(red) d(green) d(blue).
Equations
- Tau.BookIV.Strong.neutron_state = { flavor_1 := "u", flavor_2 := "d", flavor_3 := "d" }
Instances For

---

### `Tau.BookIV.Strong.proton_singlet`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L362-L365)
**theorem
Tau.BookIV.Strong.proton_singlet :(proton_state.color_1 + proton_state.color_2 + proton_state.color_3) % 3 = 0**


Proton is a color singlet: (0+1+2) mod 3 = 0.

---

### `Tau.BookIV.Strong.neutron_singlet`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/QuarksGluons.lean#L367-L370)
**theorem
Tau.BookIV.Strong.neutron_singlet :(neutron_state.color_1 + neutron_state.color_2 + neutron_state.color_3) % 3 = 0**


Neutron is a color singlet.
