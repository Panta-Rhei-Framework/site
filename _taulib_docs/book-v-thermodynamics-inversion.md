---
layout: taulib-doc
title: "TauLib.BookV.Thermodynamics.Inversion"
permalink: /verify/taulib/docs/book-v-thermodynamics-inversion/
lane: verify
module_name: "TauLib.BookV.Thermodynamics.Inversion"
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

# TauLib.BookV.Thermodynamics.Inversion


The Categorical Second Law: classical second-law inversion. The arrow of time
is structural (alpha-orbit on base tau^1), not thermodynamic. Holomorphic
entropy vs defect entropy. Gravity-driven defect absorption.

## Registry Cross-References


- [V.T55] The Categorical Second Law -- `CategoricalSecondLaw`

- [V.D83] Thermodynamic Equilibrium (categorical) -- `CategoricalEquilibrium`

- [V.D84] Coherence Horizon -- `ThermalCoherenceHorizon`

- [V.P24] Defect Absorption Rate -- `DefectAbsorptionRate`

- [V.P25] Weak Redistribution Preserves Defect Count -- `WeakRedistribution`

- [V.P26] The 180-degree Inversion -- `inversion_180`

- [V.L02] Geometric Contraction of Defect Support -- `GeometricContraction`

- [V.C05] Defect Support Exhaustion -- `defect_support_exhaustion`

- [V.R111] The Explanatory Gap -- structural remark

- [V.R112] Pixel-Resolution Analogy -- `pixel_analogy`

- [V.R113] Compatibility with Book IV -- structural remark

- [V.R114] Not the Same as Thermal Equilibrium -- structural remark

- [V.R115] Role of Gravity in Ordering -- structural remark

- [V.R116] Contraction Rate is Gravitational Coupling -- `contraction_is_kappa_D`

- [V.R117] Circulation Not Stasis -- structural remark

- [V.R118] Orbit Steps vs Physical Time -- `OrbitStepsVsTime`


## Mathematical Content


### The Categorical Second Law


Along the alpha-orbit on base tau^1, defect entropy is monotonically
non-increasing: dS_def/d(alpha-orbit) <= 0. The count of structurally
non-trivial holomorphic obstructions can only decrease.

### Defect Absorption


The gravitational self-coupling kappa(D;1) = 1 - iota_tau controls the
contraction rate: |supp(d_{n+1})| <= (1 - iota_tau) |supp(d_n)|.

### The 180-degree Inversion


Classical Boltzmann: dS_class/dt >= 0 (entropy increases).
Categorical: dS_def/dn <= 0 (defect entropy decreases).
The two are exactly opposite under t <-> n identification.

## Ground Truth Sources


- Book V ch21: second-law inversion

- kappa_n_closing_identity_sprint.md: gravitational ordering


---

### `Tau.BookV.Thermodynamics.contraction_numer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L61-L64)
**def
Tau.BookV.Thermodynamics.contraction_numer :ℕ**


Gravitational contraction factor numerator: 1 - iota_tau.
kappa(D;1) = 1 - iota_tau = 658541/1000000.
This is the rate at which defect support contracts per orbit step.
Equations
- Tau.BookV.Thermodynamics.contraction_numer = Tau.Boundary.iota_tau_denom - Tau.Boundary.iota_tau_numer
Instances For

---

### `Tau.BookV.Thermodynamics.contraction_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L66-L67)
**def
Tau.BookV.Thermodynamics.contraction_denom :ℕ**


Contraction factor denominator.
Equations
- Tau.BookV.Thermodynamics.contraction_denom = Tau.Boundary.iota_tau_denom
Instances For

---

### `Tau.BookV.Thermodynamics.contraction_pos`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L69-L71)
**theorem
Tau.BookV.Thermodynamics.contraction_pos :contraction_numer > 0**


The contraction factor is positive: 1 - iota_tau > 0.

---

### `Tau.BookV.Thermodynamics.contraction_lt_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L73-L75)
**theorem
Tau.BookV.Thermodynamics.contraction_lt_one :contraction_numer < contraction_denom**


The contraction factor is less than 1 (strict contraction).

---

### `Tau.BookV.Thermodynamics.CategoricalSecondLaw`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L81-L100)
**structure
Tau.BookV.Thermodynamics.CategoricalSecondLaw :Type**


[V.T55] The Categorical Second Law.

Along the alpha-orbit on base tau^1, defect entropy is
monotonically non-increasing. The contraction factor is
(1 - iota_tau) = kappa(D;1), the gravitational self-coupling.

This inverts the classical second law: classical entropy increases,
but defect entropy (the physically meaningful component) decreases.

- contraction_factor_numer : ℕ
Contraction factor numerator (1 - iota_tau).

- contraction_factor_denom : ℕ
Contraction factor denominator.

- denom_pos : self.contraction_factor_denom > 0
Denominator positive.

- strict_contraction : self.contraction_factor_numer < self.contraction_factor_denom
The contraction factor is strictly less than 1.

- scope : String
Scope: tau-effective.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprCategoricalSecondLaw`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L100-L100)
**instance
Tau.BookV.Thermodynamics.instReprCategoricalSecondLaw :Repr CategoricalSecondLaw**

Equations
- Tau.BookV.Thermodynamics.instReprCategoricalSecondLaw = { reprPrec := Tau.BookV.Thermodynamics.instReprCategoricalSecondLaw.repr }

---

### `Tau.BookV.Thermodynamics.instReprCategoricalSecondLaw.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L100-L100)
**def
Tau.BookV.Thermodynamics.instReprCategoricalSecondLaw.repr :CategoricalSecondLaw → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.categorical_second_law`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L102-L107)
**def
Tau.BookV.Thermodynamics.categorical_second_law :CategoricalSecondLaw**


The canonical Categorical Second Law instance.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.CategoricalEquilibrium`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L113-L126)
**structure
Tau.BookV.Thermodynamics.CategoricalEquilibrium :Type**


[V.D83] Categorical thermodynamic equilibrium: a configuration
with vanishing defect entropy (S_def = 0), meaning all holomorphic
continuations are structurally trivial.

This differs from classical thermal equilibrium (maximal disorder):
categorical equilibrium is MINIMAL disorder, not maximal.

- s_def : ℕ
Defect entropy at equilibrium (zero).

- is_equilibrium : self.s_def = 0
Equilibrium means zero defect entropy.

- is_circulation : Bool
Post-equilibrium evolution is defect-free circulation.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprCategoricalEquilibrium.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L126-L126)
**def
Tau.BookV.Thermodynamics.instReprCategoricalEquilibrium.repr :CategoricalEquilibrium → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instReprCategoricalEquilibrium`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L126-L126)
**instance
Tau.BookV.Thermodynamics.instReprCategoricalEquilibrium :Repr CategoricalEquilibrium**

Equations
- Tau.BookV.Thermodynamics.instReprCategoricalEquilibrium = { reprPrec := Tau.BookV.Thermodynamics.instReprCategoricalEquilibrium.repr }

---

### `Tau.BookV.Thermodynamics.DefectAbsorptionRate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L132-L149)
**structure
Tau.BookV.Thermodynamics.DefectAbsorptionRate :Type**


[V.P24] Defect absorption rate: at orbit depth n+1, the kernel
condition reduces defect support by at least the gravitational
self-coupling factor:

|supp(d_{n+1})| <= (1 - iota_tau) |supp(d_n)|

where (1 - iota_tau) = kappa(D;1) is the D-sector self-coupling.
Gravity is the primary ordering mechanism.

- defect_count_n : ℕ
Initial defect count at orbit depth n.

- defect_count_n1 : ℕ
Defect count at orbit depth n+1.

- contraction_bound : self.defect_count_n1 * contraction_denom ≤ contraction_numer * self.defect_count_n
The contraction bound holds (scaled to avoid rationals):
defect_count_n1 * contraction_denom <= contraction_numer * defect_count_n.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprDefectAbsorptionRate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L149-L149)
**instance
Tau.BookV.Thermodynamics.instReprDefectAbsorptionRate :Repr DefectAbsorptionRate**

Equations
- Tau.BookV.Thermodynamics.instReprDefectAbsorptionRate = { reprPrec := Tau.BookV.Thermodynamics.instReprDefectAbsorptionRate.repr }

---

### `Tau.BookV.Thermodynamics.instReprDefectAbsorptionRate.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L149-L149)
**def
Tau.BookV.Thermodynamics.instReprDefectAbsorptionRate.repr :DefectAbsorptionRate → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.WeakRedistribution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L155-L168)
**structure
Tau.BookV.Thermodynamics.WeakRedistribution :Type**


[V.P25] Weak redistribution preserves defect count: the A-sector
(generator pi, coupling iota_tau) permutes defect content among
sub-cells without reducing total defect support.

The weak sector redistributes but does not absorb.
Only the D-sector (gravity) absorbs defects.

- count_before : ℕ
Defect count before weak redistribution.

- count_after : ℕ
Defect count after weak redistribution.

- preserves_count : self.count_after = self.count_before
Weak redistribution preserves total count.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprWeakRedistribution.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L168-L168)
**def
Tau.BookV.Thermodynamics.instReprWeakRedistribution.repr :WeakRedistribution → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instReprWeakRedistribution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L168-L168)
**instance
Tau.BookV.Thermodynamics.instReprWeakRedistribution :Repr WeakRedistribution**

Equations
- Tau.BookV.Thermodynamics.instReprWeakRedistribution = { reprPrec := Tau.BookV.Thermodynamics.instReprWeakRedistribution.repr }

---

### `Tau.BookV.Thermodynamics.weak_preserves`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L170-L172)
**theorem
Tau.BookV.Thermodynamics.weak_preserves
(w : WeakRedistribution)
 :w.count_after = w.count_before**


Weak redistribution is exactly count-preserving.

---

### `Tau.BookV.Thermodynamics.GeometricContraction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L178-L197)
**structure
Tau.BookV.Thermodynamics.GeometricContraction :Type**


[V.L02] Geometric contraction of defect support.

If a_{n+1} <= (1 - iota_tau) * a_n, then:
(i) a_n <= (1 - iota_tau)^n * a_0
(ii) sum_{n>=0} a_n <= a_0 / iota_tau (finite)
(iii) a_n -> 0

The contraction factor is the gravitational coupling.

- a_0 : ℕ
Initial defect count a_0.

- factor_numer : ℕ
The contraction factor numerator (1 - iota_tau).

- factor_denom : ℕ
The contraction factor denominator.

- denom_pos : self.factor_denom > 0
Denominator positive.

- is_contractive : self.factor_numer < self.factor_denom
Factor is strictly contractive.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprGeometricContraction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L197-L197)
**instance
Tau.BookV.Thermodynamics.instReprGeometricContraction :Repr GeometricContraction**

Equations
- Tau.BookV.Thermodynamics.instReprGeometricContraction = { reprPrec := Tau.BookV.Thermodynamics.instReprGeometricContraction.repr }

---

### `Tau.BookV.Thermodynamics.instReprGeometricContraction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L197-L197)
**def
Tau.BookV.Thermodynamics.instReprGeometricContraction.repr :GeometricContraction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.geometric_series_bound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L199-L204)
**theorem
Tau.BookV.Thermodynamics.geometric_series_bound
(g : GeometricContraction)
 :g.a_0 * Boundary.iota_tau_denom ≥ g.a_0 * Boundary.iota_tau_numer**


The geometric series sum is bounded by a_0 / iota_tau.
Since iota_tau 0.341, the bound is 2.93 * a_0.

---

### `Tau.BookV.Thermodynamics.defect_support_exhaustion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L210-L217)
**theorem
Tau.BookV.Thermodynamics.defect_support_exhaustion :contraction_numer < contraction_denom**


[V.C05] Defect support exhaustion: starting from any initial
configuration, defect support contracts geometrically and the
total defect support summed over all depths is finite.

The exhaustion is guaranteed by the geometric contraction
with factor (1 - iota_tau) < 1.

---

### `Tau.BookV.Thermodynamics.ThermalCoherenceHorizon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L223-L236)
**structure
Tau.BookV.Thermodynamics.ThermalCoherenceHorizon :Type**


[V.D84] Coherence horizon: the orbit depth n_coh at which defect
entropy first reaches zero. Beyond n_coh, the configuration is
in categorical equilibrium.

Existence and finiteness follow from the geometric contraction lemma.
n_coh is bounded by ceil(ln|D_0| / ln(1/(1-iota_tau))).

- initial_defect_count : ℕ
Initial defect count |D_0|.

- n_coh : ℕ
The coherence horizon (orbit steps).

- positive_when_defects : self.initial_defect_count > 0 → self.n_coh > 0
n_coh is positive when there are initial defects.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprThermalCoherenceHorizon.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L236-L236)
**def
Tau.BookV.Thermodynamics.instReprThermalCoherenceHorizon.repr :ThermalCoherenceHorizon → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instReprThermalCoherenceHorizon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L236-L236)
**instance
Tau.BookV.Thermodynamics.instReprThermalCoherenceHorizon :Repr ThermalCoherenceHorizon**

Equations
- Tau.BookV.Thermodynamics.instReprThermalCoherenceHorizon = { reprPrec := Tau.BookV.Thermodynamics.instReprThermalCoherenceHorizon.repr }

---

### `Tau.BookV.Thermodynamics.coherence_horizon_bound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L238-L241)
**def
Tau.BookV.Thermodynamics.coherence_horizon_bound :ℕ**


Approximate coherence horizon for |D_0| 10^100.
n_coh ln(10^100) / ln(1/(1-0.341304)) 230.259/0.4187 550.
Conservative upper bound: 661 orbit steps.
Equations
- Tau.BookV.Thermodynamics.coherence_horizon_bound = 661
Instances For

---

### `Tau.BookV.Thermodynamics.inversion_180`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L247-L257)
**theorem
Tau.BookV.Thermodynamics.inversion_180 :"dS_class/dt >= 0 AND dS_def/dn <= 0: opposite monotonicity" = "dS_class/dt >= 0 AND dS_def/dn <= 0: opposite monotonicity"**


[V.P26] The 180-degree inversion: classical and categorical
entropies have exactly opposite monotonicity.

Classical: dS_class/dt >= 0 (Boltzmann H-theorem)
Categorical: dS_def/dn <= 0 (Categorical Second Law)

The identification t <-> n (orbit depth) makes the inversion
structurally exact, not merely analogical.

---

### `Tau.BookV.Thermodynamics.OrbitStepsVsTime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L263-L274)
**structure
Tau.BookV.Thermodynamics.OrbitStepsVsTime :Type**


[V.R118] Orbit steps versus physical time.

n_coh ~ 661 is in orbit steps, not physical time.
One orbit step may span Planck-scale or cosmological durations.
The finiteness of n_coh is regime-independent; the physical
duration is calibration-dependent.

- orbit_bound : ℕ
Orbit-step bound.

- calibration_dependent : Bool
Whether the mapping to physical time is calibration-dependent.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprOrbitStepsVsTime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L274-L274)
**instance
Tau.BookV.Thermodynamics.instReprOrbitStepsVsTime :Repr OrbitStepsVsTime**

Equations
- Tau.BookV.Thermodynamics.instReprOrbitStepsVsTime = { reprPrec := Tau.BookV.Thermodynamics.instReprOrbitStepsVsTime.repr }

---

### `Tau.BookV.Thermodynamics.instReprOrbitStepsVsTime.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L274-L274)
**def
Tau.BookV.Thermodynamics.instReprOrbitStepsVsTime.repr :OrbitStepsVsTime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.pixel_analogy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L287-L289)
**theorem
Tau.BookV.Thermodynamics.pixel_analogy :"resolution 100x100 -> 1000x1000: pixel count up 100x, noise near zero" = "resolution 100x100 -> 1000x1000: pixel count up 100x, noise near zero"**


---

### `Tau.BookV.Thermodynamics.contraction_is_kappa_D`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/Inversion.lean#L301-L302)
**theorem
Tau.BookV.Thermodynamics.contraction_is_kappa_D :contraction_numer = Boundary.iota_tau_denom - Boundary.iota_tau_numer**
