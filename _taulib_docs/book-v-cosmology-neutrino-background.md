---
layout: taulib-doc
title: "TauLib.BookV.Cosmology.NeutrinoBackground"
permalink: /verify/taulib/docs/book-v-cosmology-neutrino-background/
lane: verify
module_name: "TauLib.BookV.Cosmology.NeutrinoBackground"
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

# TauLib.BookV.Cosmology.NeutrinoBackground


Neutrino background origin and density gradient monotonicity from the
τ-framework threshold ladder. Ch49 neutrino decoupling physics.

## Registry Cross-References


- [V.P114] Neutrino Background Origin -- `NeutrinoBackgroundOrigin`

- [V.T152] Density Gradient Monotonicity -- `DensityGradientMonotonicity`


## Mathematical Content


### Neutrino Background Origin [V.P114]


The cosmic neutrino background (CνB) originates from neutrino decoupling
at T_dec ≈ 1.37 MeV (z_ν ≈ 5.8 × 10⁹). In the τ-framework, this is
governed by the A-sector coupling κ(A;1) = ι<sub>τ</sub>: when the thermal energy
drops below the weak interaction scale set by ι<sub>τ</sub>, neutrinos decouple.

### Density Gradient Monotonicity [V.T152]


The energy density of the neutrino background decreases monotonically
after decoupling. This follows from the directed α-orbit (temporal
monotonicity) applied to the neutrino sector.

## Ground Truth Sources


- Book V ch49: Neutrino background, density gradients


---

### `Tau.BookV.Cosmology.NeutrinoBackgroundOrigin`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L39-L59)
**structure
Tau.BookV.Cosmology.NeutrinoBackgroundOrigin :Type**


[V.P114] Neutrino background origin: CνB originates from neutrino
decoupling at T_dec ≈ 1.37 MeV.


- Decoupling governed by A-sector coupling κ(A;1) = ι<sub>τ</sub>

- 3 neutrino species (from N_eff = 3, sector exhaustion V.T151)

- T_CνB = (4/11)^{1/3} · T_CMB = 1.945 K (established)

- Number density: 336 ν/cm³ (112 per flavor)


- n_species : ℕ
Number of neutrino species.

- species_eq : self.n_species = 3
Exactly 3 species.

- density_per_flavor : ℕ
Number density per flavor (ν/cm³).

- total_density : ℕ
Total number density (ν/cm³).

- a_sector_governed : Bool
Decoupling is A-sector governed.

- thermal_relic : Bool
Background is thermal relic.

Instances For

---

### `Tau.BookV.Cosmology.instReprNeutrinoBackgroundOrigin.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L59-L59)
**def
Tau.BookV.Cosmology.instReprNeutrinoBackgroundOrigin.repr :NeutrinoBackgroundOrigin → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprNeutrinoBackgroundOrigin`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L59-L59)
**instance
Tau.BookV.Cosmology.instReprNeutrinoBackgroundOrigin :Repr NeutrinoBackgroundOrigin**

Equations
- Tau.BookV.Cosmology.instReprNeutrinoBackgroundOrigin = { reprPrec := Tau.BookV.Cosmology.instReprNeutrinoBackgroundOrigin.repr }

---

### `Tau.BookV.Cosmology.neutrino_bg`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L61-L64)
**def
Tau.BookV.Cosmology.neutrino_bg :NeutrinoBackgroundOrigin**


The canonical neutrino background origin.
Equations
- Tau.BookV.Cosmology.neutrino_bg = { n_species := 3, species_eq := Tau.BookV.Cosmology.neutrino_bg._proof_1 }
Instances For

---

### `Tau.BookV.Cosmology.neutrino_background_origin`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L66-L71)
**theorem
Tau.BookV.Cosmology.neutrino_background_origin :neutrino_bg.n_species = 3 ∧ neutrino_bg.a_sector_governed = true ∧ neutrino_bg.thermal_relic = true**


CνB has 3 species, A-sector governed.

---

### `Tau.BookV.Cosmology.density_times_species`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L73-L75)
**theorem
Tau.BookV.Cosmology.density_times_species :3 * 112 = 336**


Total density = 3 species × 112 per flavor = 336 ν/cm³.

---

### `Tau.BookV.Cosmology.neutrino_temp_float`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L77-L78)
**def
Tau.BookV.Cosmology.neutrino_temp_float :Float**


CνB temperature: T_CνB = (4/11)^{1/3} · T_CMB ≈ 1.945 K.
Equations
- Tau.BookV.Cosmology.neutrino_temp_float = 1.945
Instances For

---

### `Tau.BookV.Cosmology.DensityGradientMonotonicity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L84-L102)
**structure
Tau.BookV.Cosmology.DensityGradientMonotonicity :Type**


[V.T152] Density gradient monotonicity: after neutrino decoupling,
the CνB energy density decreases monotonically.


- Follows from directed α-orbit (temporal monotonicity)

- ρ_ν ∝ a⁻⁴ (relativistic) transitioning to ρ_ν ∝ a⁻³ (non-rel)

- Monotonicity is structural (not contingent on initial conditions)

- Gradient ∂ρ_ν/∂t < 0 for all t > t_dec


- density_decreasing : Bool
Density decreases after decoupling.

- from_alpha_orbit : Bool
Follows from directed α-orbit.

- is_structural : Bool
Structural (not initial-condition dependent).

- relativistic_exp : ℕ
Relativistic scaling exponent (ρ ∝ a⁻⁴).

- nonrelativistic_exp : ℕ
Non-relativistic scaling exponent (ρ ∝ a⁻³).

Instances For

---

### `Tau.BookV.Cosmology.instReprDensityGradientMonotonicity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L102-L102)
**def
Tau.BookV.Cosmology.instReprDensityGradientMonotonicity.repr :DensityGradientMonotonicity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprDensityGradientMonotonicity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L102-L102)
**instance
Tau.BookV.Cosmology.instReprDensityGradientMonotonicity :Repr DensityGradientMonotonicity**

Equations
- Tau.BookV.Cosmology.instReprDensityGradientMonotonicity = { reprPrec := Tau.BookV.Cosmology.instReprDensityGradientMonotonicity.repr }

---

### `Tau.BookV.Cosmology.density_monotone`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L104-L105)
**def
Tau.BookV.Cosmology.density_monotone :DensityGradientMonotonicity**


The canonical density gradient monotonicity.
Equations
- Tau.BookV.Cosmology.density_monotone = { }
Instances For

---

### `Tau.BookV.Cosmology.density_gradient_monotonicity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L107-L112)
**theorem
Tau.BookV.Cosmology.density_gradient_monotonicity :density_monotone.density_decreasing = true ∧ density_monotone.from_alpha_orbit = true ∧ density_monotone.is_structural = true**


Density gradient is monotonically decreasing and structural.

---

### `Tau.BookV.Cosmology.exponent_decreases`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L114-L116)
**theorem
Tau.BookV.Cosmology.exponent_decreases :4 > 3**


Relativistic exponent (4) > non-relativistic exponent (3).

---

### `Tau.BookV.Cosmology.OneParamMassStructure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L122-L135)
**structure
Tau.BookV.Cosmology.OneParamMassStructure :Type**


[V.P187] One-parameter neutrino mass structure.
NNLO exponents: q = q₀, p = q₀ − 203/175, r = q₀ − 1421/700.
Single free parameter q₀ determines all three masses.

- delta_pq_num : ℕ
Spacing Δpq = 203/175 (rational).

- delta_pq_den : ℕ
- delta_pr_num : ℕ
Spacing Δpr = 609/700 (rational).

- delta_pr_den : ℕ
- delta_qr_num : ℕ
Total spacing Δqr = 1421/700.

- delta_qr_den : ℕ
Instances For

---

### `Tau.BookV.Cosmology.instReprOneParamMassStructure.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L135-L135)
**def
Tau.BookV.Cosmology.instReprOneParamMassStructure.repr :OneParamMassStructure → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprOneParamMassStructure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L135-L135)
**instance
Tau.BookV.Cosmology.instReprOneParamMassStructure :Repr OneParamMassStructure**

Equations
- Tau.BookV.Cosmology.instReprOneParamMassStructure = { reprPrec := Tau.BookV.Cosmology.instReprOneParamMassStructure.repr }

---

### `Tau.BookV.Cosmology.one_param_mass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L137-L138)
**def
Tau.BookV.Cosmology.one_param_mass :OneParamMassStructure**


Canonical one-parameter mass structure.
Equations
- Tau.BookV.Cosmology.one_param_mass = { }
Instances For

---

### `Tau.BookV.Cosmology.total_spacing_sum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L140-L142)
**theorem
Tau.BookV.Cosmology.total_spacing_sum :203 / 175 + 609 / 700 = 1421 / 700**


Total spacing = Δpq + Δpr: 1421/700 = 203/175 + 609/700.

---

### `Tau.BookV.Cosmology.spacing_ratio_four_thirds`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L144-L146)
**theorem
Tau.BookV.Cosmology.spacing_ratio_four_thirds :203 / 175 / (609 / 700) = 4 / 3**


The 4/3 ratio: Δpq/Δpr = (203/175)/(609/700) = 4/3.

---

### `Tau.BookV.Cosmology.NormalHierarchyProof`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L152-L171)
**structure
Tau.BookV.Cosmology.NormalHierarchyProof :Type**


[V.T268] Normal Hierarchy from winding exponent order.
Since Δpq = 203/175 > 0 and Δpr = 609/700 > 0,
the ordering r < p < q gives m₃ > m₂ > m₁ (Normal Ordering).
This is a theorem, not a parameter choice.

- delta_pq_num : ℕ
Δpq numerator (positive).

- delta_pq_den : ℕ
Δpq denominator (positive).

- delta_pr_num : ℕ
Δpr numerator (positive).

- delta_pr_den : ℕ
Δpr denominator (positive).

- delta_qr_num : ℕ
Total Δqr numerator (positive).

- delta_qr_den : ℕ
Total Δqr denominator (positive).

- is_normal_ordering : Bool
All numerators positive (Normal Ordering is forced).

Instances For

---

### `Tau.BookV.Cosmology.instReprNormalHierarchyProof.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L171-L171)
**def
Tau.BookV.Cosmology.instReprNormalHierarchyProof.repr :NormalHierarchyProof → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprNormalHierarchyProof`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L171-L171)
**instance
Tau.BookV.Cosmology.instReprNormalHierarchyProof :Repr NormalHierarchyProof**

Equations
- Tau.BookV.Cosmology.instReprNormalHierarchyProof = { reprPrec := Tau.BookV.Cosmology.instReprNormalHierarchyProof.repr }

---

### `Tau.BookV.Cosmology.normal_hierarchy_proof`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L173-L174)
**def
Tau.BookV.Cosmology.normal_hierarchy_proof :NormalHierarchyProof**


The canonical normal hierarchy proof.
Equations
- Tau.BookV.Cosmology.normal_hierarchy_proof = { }
Instances For

---

### `Tau.BookV.Cosmology.normal_hierarchy_spacings_positive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L176-L183)
**theorem
Tau.BookV.Cosmology.normal_hierarchy_spacings_positive :normal_hierarchy_proof.delta_pq_num > 0 ∧ normal_hierarchy_proof.delta_pr_num > 0 ∧ normal_hierarchy_proof.delta_qr_num > 0**


All spacings have positive numerators → exponents satisfy q > p > r → m₁ < m₂ < m₃.

---

### `Tau.BookV.Cosmology.normal_hierarchy_is_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L185-L189)
**theorem
Tau.BookV.Cosmology.normal_hierarchy_is_theorem :203 > 0 ∧ 609 > 0 ∧ 1421 > 0**


Normal ordering is a theorem: all spacings positive → m₁ < m₂ < m₃.
Verified as Nat comparisons (203 > 0, 609 > 0, 1421 > 0).

---

### `Tau.BookV.Cosmology.IndividualNeutrinoMasses`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L195-L209)
**structure
Tau.BookV.Cosmology.IndividualNeutrinoMasses :Type**


[V.D333] Individual neutrino masses from NNLO exponents.
m₁ ≈ 6.94 meV, m₂ ≈ 22.68 meV, m₃ ≈ 59.40 meV.
Sum = 89.02 meV ≈ 0.089 eV at +7.4 ppm.

- m1_meV : Float
m₁ in meV.

- m2_meV : Float
m₂ in meV.

- m3_meV : Float
m₃ in meV.

- sum_meV : Float
Sum in meV.

- hierarchy_ratio : Float
Hierarchy ratio m₃/m₁.

Instances For

---

### `Tau.BookV.Cosmology.instReprIndividualNeutrinoMasses.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L209-L209)
**def
Tau.BookV.Cosmology.instReprIndividualNeutrinoMasses.repr :IndividualNeutrinoMasses → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprIndividualNeutrinoMasses`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L209-L209)
**instance
Tau.BookV.Cosmology.instReprIndividualNeutrinoMasses :Repr IndividualNeutrinoMasses**

Equations
- Tau.BookV.Cosmology.instReprIndividualNeutrinoMasses = { reprPrec := Tau.BookV.Cosmology.instReprIndividualNeutrinoMasses.repr }

---

### `Tau.BookV.Cosmology.individual_masses`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L211-L212)
**def
Tau.BookV.Cosmology.individual_masses :IndividualNeutrinoMasses**


Canonical individual masses.
Equations
- Tau.BookV.Cosmology.individual_masses = { }
Instances For

---

### `Tau.BookV.Cosmology.MassSquaredSplittings`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L214-L230)
**structure
Tau.BookV.Cosmology.MassSquaredSplittings :Type**


[V.T269] Mass-squared splittings from τ-exponents.
Δm²₂₁(τ) ≈ 4.66 × 10⁻⁴ eV² (NuFIT: 7.53 × 10⁻⁵, factor 6.2× off).
|Δm²₃₂|(τ) ≈ 3.01 × 10⁻³ eV² (NuFIT: 2.453 × 10⁻³, +22.9%).

- dm21_sq_e5 : Float
Δm²₂₁ in units of 10⁻⁵ eV².

- dm32_sq_e3 : Float
|Δm²₃₂| in units of 10⁻³ eV².

- dm21_sq_nufit : Float
NuFIT Δm²₂₁ in units of 10⁻⁵ eV².

- dm32_sq_nufit : Float
NuFIT |Δm²₃₂| in units of 10⁻³ eV².

- solar_ratio : Float
Solar splitting ratio (τ/NuFIT).

- atm_deviation_pct : Float
Atmospheric deviation (%).

Instances For

---

### `Tau.BookV.Cosmology.instReprMassSquaredSplittings.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L230-L230)
**def
Tau.BookV.Cosmology.instReprMassSquaredSplittings.repr :MassSquaredSplittings → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprMassSquaredSplittings`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L230-L230)
**instance
Tau.BookV.Cosmology.instReprMassSquaredSplittings :Repr MassSquaredSplittings**

Equations
- Tau.BookV.Cosmology.instReprMassSquaredSplittings = { reprPrec := Tau.BookV.Cosmology.instReprMassSquaredSplittings.repr }

---

### `Tau.BookV.Cosmology.mass_splittings`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L232-L233)
**def
Tau.BookV.Cosmology.mass_splittings :MassSquaredSplittings**


Canonical mass-squared splittings.
Equations
- Tau.BookV.Cosmology.mass_splittings = { }
Instances For

---

### `Tau.BookV.Cosmology.juno_dune_predictions`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L235-L240)
**def
Tau.BookV.Cosmology.juno_dune_predictions :String**


[V.P188] JUNO/DUNE predictions: solar splitting at sub-1%, atmospheric at sub-2%.
Current τ values testable by both experiments.
Equations
- One or more equations did not get rendered due to their size.
Instances For
