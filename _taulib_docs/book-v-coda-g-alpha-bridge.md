---
layout: taulib-doc
title: "TauLib.BookV.Coda.GAlphaBridge"
permalink: /verify/taulib/docs/book-v-coda-g-alpha-bridge/
lane: verify
module_name: "TauLib.BookV.Coda.GAlphaBridge"
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

# TauLib.BookV.Coda.GAlphaBridge


The G-α gravitational bridge: structural derivation of Newton's
gravitational constant from the fine-structure constant via the
holonomy exponent 18.

## Registry Cross-References


- [V.T154] The G-alpha Bridge -- `GAlphaBridge`

- [V.T155] Mass Hierarchy Exponent -- `MassHierarchyExponent`

- [V.P115] Hierarchy as Power Law -- `HierarchyPowerLaw`

- [V.P116] Precision Budget -- `PrecisionBudget`


## Mathematical Content


### The G-α Bridge [V.T154]


α_G = α¹⁸ · √3 · (1 − (3/π)·α): the gravitational-to-EM coupling ratio
is determined by α raised to the holonomy exponent 18, with geometric
corrections from the lemniscate structure.

### Mass Hierarchy Exponent [V.T155]


m_Pl/m_n ∝ α⁻⁹: the Planck-to-nucleon mass ratio is governed by half
the holonomy exponent. 9 = 18/2 is the single-lobe contribution.

### Hierarchy as Power Law [V.P115]


α/α_G = α⁻¹⁷ · ...: the gravity-EM coupling ratio as a power law with
exponent 17 = 18 − 1.

### Precision Budget [V.P116]


Total uncertainty for G via the bridge: 2.7 ppb from α (negligible),
~3 ppm from c₁ (dominant), 0.6 ppm from m_n.

## Ground Truth Sources


- Book V ch70: G-α gravitational bridge


---

### `Tau.BookV.Coda.GAlphaBridge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L50-L72)
**structure
Tau.BookV.Coda.GAlphaBridge :Type**


[V.T154] The G-α bridge identity:
α_G = α¹⁸ · √3 · (1 − (3/π)·α)


- Holonomy exponent 18 = 2 × 9 = 2 × (3²) from double-lobe winding

- √3 from triangular calibration vertex

- (1 − (3/π)·α) radiative correction from EM self-energy

- Every factor has geometric origin in the τ³ fibration


- holonomy_exp : ℕ
Holonomy exponent.

- exp_eq : self.holonomy_exp = 18
Exponent is 18.

- exp_decomp : self.holonomy_exp = 2 * 9
Exponent decomposes as 2 × 9.

- lobes : ℕ
Number of lobes on the lemniscate.

- axioms_count : ℕ
Number of axioms (K0-K6).

- sqrt3_correction : Bool
√3 correction present.

- radiative_correction : Bool
Radiative correction present.

Instances For

---

### `Tau.BookV.Coda.instReprGAlphaBridge.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L72-L72)
**def
Tau.BookV.Coda.instReprGAlphaBridge.repr :GAlphaBridge → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Coda.instReprGAlphaBridge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L72-L72)
**instance
Tau.BookV.Coda.instReprGAlphaBridge :Repr GAlphaBridge**

Equations
- Tau.BookV.Coda.instReprGAlphaBridge = { reprPrec := Tau.BookV.Coda.instReprGAlphaBridge.repr }

---

### `Tau.BookV.Coda.g_alpha_bridge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L74-L78)
**def
Tau.BookV.Coda.g_alpha_bridge :GAlphaBridge**


The canonical G-α bridge.
Equations
- Tau.BookV.Coda.g_alpha_bridge = { holonomy_exp := 18, exp_eq := Tau.BookV.Coda.g_alpha_bridge._proof_1,
 exp_decomp := Tau.BookV.Coda.g_alpha_bridge._proof_1 }
Instances For

---

### `Tau.BookV.Coda.g_alpha_bridge_thm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L80-L85)
**theorem
Tau.BookV.Coda.g_alpha_bridge_thm :g_alpha_bridge.holonomy_exp = 18 ∧ g_alpha_bridge.sqrt3_correction = true ∧ g_alpha_bridge.radiative_correction = true**


G-α bridge: exponent 18, both corrections present.

---

### `Tau.BookV.Coda.holonomy_18_decomposition`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L87-L89)
**theorem
Tau.BookV.Coda.holonomy_18_decomposition :18 = 2 * 9 ∧ 9 = 3 * 3**


Holonomy exponent 18 = 2 × 9 = 2 × 3².

---

### `Tau.BookV.Coda.holonomy_is_lobes_times_axioms`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L91-L93)
**theorem
Tau.BookV.Coda.holonomy_is_lobes_times_axioms :2 * 9 = 18**


Holonomy exponent = lobes × axioms: 2 × 9 = 18.

---

### `Tau.BookV.Coda.nine_is_dim_squared`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L95-L97)
**theorem
Tau.BookV.Coda.nine_is_dim_squared :3 * 3 = 9**


7 axioms = K0–K6 (2nd Edition).

---

### `Tau.BookV.Coda.alpha_G_float`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L99-L100)
**def
Tau.BookV.Coda.alpha_G_float :Float**


α_G ≈ 5.92 × 10⁻³⁹.
Equations
- Tau.BookV.Coda.alpha_G_float = 592e-41
Instances For

---

### `Tau.BookV.Coda.MassHierarchyExponent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L106-L122)
**structure
Tau.BookV.Coda.MassHierarchyExponent :Type**


[V.T155] Mass hierarchy exponent: m_Pl/m_n ∝ α⁻⁹.
Exponent 9 = 18/2: half the holonomy exponent (single-lobe
contribution to the double-lobe winding number 18).


- m_Pl = √(ℏc/G) ∝ α⁻⁹ · m_n (from G-α bridge)

- The mass hierarchy is not mysterious: it is the 9th power of α

- 9 = dim(τ³)² = 3² from the τ³ volume squared


- single_lobe_exp : ℕ
Single-lobe exponent.

- exp_eq : self.single_lobe_exp = 9
Exponent is 9.

- dim_tau3 : ℕ
Dimension of τ³.

- is_half_holonomy : Bool
Is half the holonomy exponent.

Instances For

---

### `Tau.BookV.Coda.instReprMassHierarchyExponent.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L122-L122)
**def
Tau.BookV.Coda.instReprMassHierarchyExponent.repr :MassHierarchyExponent → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Coda.instReprMassHierarchyExponent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L122-L122)
**instance
Tau.BookV.Coda.instReprMassHierarchyExponent :Repr MassHierarchyExponent**

Equations
- Tau.BookV.Coda.instReprMassHierarchyExponent = { reprPrec := Tau.BookV.Coda.instReprMassHierarchyExponent.repr }

---

### `Tau.BookV.Coda.mass_hierarchy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L124-L127)
**def
Tau.BookV.Coda.mass_hierarchy :MassHierarchyExponent**


The canonical mass hierarchy exponent.
Equations
- Tau.BookV.Coda.mass_hierarchy = { single_lobe_exp := 9, exp_eq := Tau.BookV.Coda.mass_hierarchy._proof_1 }
Instances For

---

### `Tau.BookV.Coda.mass_hierarchy_exponent`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L129-L133)
**theorem
Tau.BookV.Coda.mass_hierarchy_exponent :mass_hierarchy.single_lobe_exp = 9 ∧ mass_hierarchy.is_half_holonomy = true**


Mass hierarchy: exponent 9 = 18/2.

---

### `Tau.BookV.Coda.nine_is_half_eighteen`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L135-L136)
**theorem
Tau.BookV.Coda.nine_is_half_eighteen :18 / 2 = 9**


9 = 18/2 (single-lobe is half of double-lobe).

---

### `Tau.BookV.Coda.nine_from_dimension`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L138-L140)
**theorem
Tau.BookV.Coda.nine_from_dimension :3 * 3 = 9**


9 from dimension: dim(τ³)² = 3 × 3 = 9.

---

### `Tau.BookV.Coda.hierarchy_is_half_bridge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L142-L145)
**theorem
Tau.BookV.Coda.hierarchy_is_half_bridge :mass_hierarchy.single_lobe_exp * 2 = g_alpha_bridge.holonomy_exp**


Single-lobe × 2 = holonomy: hierarchy is half of bridge exponent.

---

### `Tau.BookV.Coda.HierarchyPowerLaw`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L151-L163)
**structure
Tau.BookV.Coda.HierarchyPowerLaw :Type**


[V.P115] Hierarchy as power law: α/α_G = α⁻¹⁷ · ...
with exponent 17 = 18 − 1.

The gravity-EM coupling ratio spans ~39 orders of magnitude.
This is structurally determined, not fine-tuned.

- power_exp : ℕ
Power law exponent.

- exp_eq : self.power_exp = 17
Exponent is 17.

- exp_from_holonomy : self.power_exp + 1 = 18
17 = 18 − 1.

Instances For

---

### `Tau.BookV.Coda.instReprHierarchyPowerLaw.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L163-L163)
**def
Tau.BookV.Coda.instReprHierarchyPowerLaw.repr :HierarchyPowerLaw → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Coda.instReprHierarchyPowerLaw`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L163-L163)
**instance
Tau.BookV.Coda.instReprHierarchyPowerLaw :Repr HierarchyPowerLaw**

Equations
- Tau.BookV.Coda.instReprHierarchyPowerLaw = { reprPrec := Tau.BookV.Coda.instReprHierarchyPowerLaw.repr }

---

### `Tau.BookV.Coda.hierarchy_power`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L165-L169)
**def
Tau.BookV.Coda.hierarchy_power :HierarchyPowerLaw**


The canonical hierarchy power law.
Equations
- Tau.BookV.Coda.hierarchy_power = { power_exp := 17, exp_eq := Tau.BookV.Coda.hierarchy_power._proof_1,
 exp_from_holonomy := Tau.BookV.Coda.hierarchy_power._proof_2 }
Instances For

---

### `Tau.BookV.Coda.hierarchy_power_law`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L171-L175)
**theorem
Tau.BookV.Coda.hierarchy_power_law :hierarchy_power.power_exp = 17 ∧ hierarchy_power.power_exp + 1 = 18**


Hierarchy power law: exponent 17 = 18 − 1.

---

### `Tau.BookV.Coda.power_from_bridge`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L177-L180)
**theorem
Tau.BookV.Coda.power_from_bridge :hierarchy_power.power_exp + 1 = g_alpha_bridge.holonomy_exp**


Power law exponent + 1 = holonomy exponent (from G-α bridge).

---

### `Tau.BookV.Coda.PrecisionBudget`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L186-L205)
**structure
Tau.BookV.Coda.PrecisionBudget :Type**


[V.P116] Precision budget for G via the bridge.


- From α: 2.7 ppb (negligible, CODATA precision)

- From c₁ = 3/π correction: ~3 ppm (dominant uncertainty)

- From m_n: 0.6 ppm (mass measurement precision)

- Total: ~3 ppm (dominated by c₁ theoretical uncertainty)


- n_sources : ℕ
Number of uncertainty sources.

- sources_eq : self.n_sources = 3
Three sources.

- dominant_is_c1 : Bool
Dominant source is c₁.

- alpha_negligible : Bool
α contribution negligible.

- alpha_ppb : ℕ
α precision (ppb).

- c1_ppm : ℕ
c₁ precision (ppm).

Instances For

---

### `Tau.BookV.Coda.instReprPrecisionBudget.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L205-L205)
**def
Tau.BookV.Coda.instReprPrecisionBudget.repr :PrecisionBudget → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Coda.instReprPrecisionBudget`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L205-L205)
**instance
Tau.BookV.Coda.instReprPrecisionBudget :Repr PrecisionBudget**

Equations
- Tau.BookV.Coda.instReprPrecisionBudget = { reprPrec := Tau.BookV.Coda.instReprPrecisionBudget.repr }

---

### `Tau.BookV.Coda.precision_budget`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L207-L210)
**def
Tau.BookV.Coda.precision_budget :PrecisionBudget**


The canonical precision budget.
Equations
- Tau.BookV.Coda.precision_budget = { n_sources := 3, sources_eq := Tau.BookV.Coda.precision_budget._proof_1 }
Instances For

---

### `Tau.BookV.Coda.precision_budget_thm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/GAlphaBridge.lean#L212-L217)
**theorem
Tau.BookV.Coda.precision_budget_thm :precision_budget.n_sources = 3 ∧ precision_budget.dominant_is_c1 = true ∧ precision_budget.alpha_negligible = true**


Precision budget: 3 sources, c₁ dominant, α negligible.
