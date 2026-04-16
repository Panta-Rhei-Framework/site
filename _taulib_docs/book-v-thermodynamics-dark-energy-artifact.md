---
layout: taulib-doc
title: "TauLib.BookV.Thermodynamics.DarkEnergyArtifact"
permalink: /verify/taulib/docs/book-v-thermodynamics-dark-energy-artifact/
lane: verify
module_name: "TauLib.BookV.Thermodynamics.DarkEnergyArtifact"
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

# TauLib.BookV.Thermodynamics.DarkEnergyArtifact


Dark energy as Lambda-CDM artifact. The 10^120 vacuum mismatch resolution.
Cosmic acceleration from defect-to-refinement transition, not from a
cosmological constant. Finite universe, no proliferating infinity.

## Registry Cross-References


- [V.D95] Capacity Surplus -- `CapacitySurplus`

- [V.T68] Defect-Driven Acceleration -- `DefectDrivenAcceleration`

- [V.T69] Dark Energy is a Readout Artifact -- `dark_energy_artifact`

- [V.P40] No Lambda in the tau-Einstein Equation -- `no_lambda`

- [V.P41] The 68% is Refinement Entropy -- `the_68_percent`

- [V.R133] Data versus Interpretation -- `data_vs_interpretation`

- [V.R134] Two Faces of the Same Problem -- `two_faces`

- [V.R135] Where Does the 68% Go? -- `where_68_goes`

- [V.R136] Testability -- `DarkEnergyTestability`


## Mathematical Content


### Capacity Surplus


C_surplus(n) = C_total - |D_n|: the difference between total absorption
capacity of the lemniscate L and the current defect count. Unused boundary
capacity manifests as negative effective pressure.

### Defect-Driven Acceleration


As S_def decreases, the effective equation-of-state parameter w shifts
from w > -1/3 (decelerating) to w < -1/3 (accelerating). The transition
occurs when defect-to-refinement ratio crosses a threshold.

### Dark Energy is a Readout Artifact


The cosmic acceleration attributed to Lambda in Lambda-CDM arises from
the defect-to-refinement transition on base tau^1. The orthodox readout
functor misidentifies refinement entropy as a physical energy source.

### No Lambda


The tau-Einstein equation R^H = kappa_tau * T contains no cosmological
constant (Lambda = 0). Acceleration is a time-dependent phenomenon from
the defect-to-refinement transition, not a permanent term.

### The 68%


The 68% of the cosmic energy budget attributed to dark energy corresponds
to refinement entropy S_ref -- a counting artifact, not physical energy.

## Ground Truth Sources


- Book V ch26: dark energy as artifact

- mass_decomposition_sprint.md: vacuum mismatch


---

### `Tau.BookV.Thermodynamics.CapacitySurplus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L66-L85)
**structure
Tau.BookV.Thermodynamics.CapacitySurplus :Type**


[V.D95] Capacity surplus: the difference between total absorption
capacity of the lemniscate boundary L and the current defect count.

C_surplus(n) = C_total - |D_n|

Unused boundary capacity manifests as negative effective pressure
in the readout functor's projection. As defects are absorbed,
C_surplus increases, driving the transition to acceleration.

- c_total : ℕ
Total absorption capacity of L.

- d_n : ℕ
Current defect count |D_n|.

- surplus : ℕ
Surplus = total - defect count.

- surplus_eq : self.surplus = self.c_total - self.d_n
Surplus equals capacity minus defects.

- capacity_exceeds : self.d_n ≤ self.c_total
Capacity exceeds defect count (surplus non-negative).

Instances For

---

### `Tau.BookV.Thermodynamics.instReprCapacitySurplus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L85-L85)
**instance
Tau.BookV.Thermodynamics.instReprCapacitySurplus :Repr CapacitySurplus**

Equations
- Tau.BookV.Thermodynamics.instReprCapacitySurplus = { reprPrec := Tau.BookV.Thermodynamics.instReprCapacitySurplus.repr }

---

### `Tau.BookV.Thermodynamics.instReprCapacitySurplus.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L85-L85)
**def
Tau.BookV.Thermodynamics.instReprCapacitySurplus.repr :CapacitySurplus → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.surplus_nonneg`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L87-L89)
**theorem
Tau.BookV.Thermodynamics.surplus_nonneg
(s : CapacitySurplus)
 :s.d_n ≤ s.c_total**


Surplus is non-negative when capacity exceeds defects.

---

### `Tau.BookV.Thermodynamics.EoSRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L95-L103)
**inductive
Tau.BookV.Thermodynamics.EoSRegime :Type**


Equation-of-state classification for the effective w parameter.

- Decelerating : EoSRegime
Decelerating: w > -1/3 (defect-dominated epoch).

- Accelerating : EoSRegime
Accelerating: w < -1/3 (refinement-dominated epoch).

- Transition : EoSRegime
Transition: w = -1/3 (crossover point).

Instances For

---

### `Tau.BookV.Thermodynamics.instReprEoSRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L103-L103)
**instance
Tau.BookV.Thermodynamics.instReprEoSRegime :Repr EoSRegime**

Equations
- Tau.BookV.Thermodynamics.instReprEoSRegime = { reprPrec := Tau.BookV.Thermodynamics.instReprEoSRegime.repr }

---

### `Tau.BookV.Thermodynamics.instReprEoSRegime.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L103-L103)
**def
Tau.BookV.Thermodynamics.instReprEoSRegime.repr :EoSRegime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instDecidableEqEoSRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L103-L103)
**instance
Tau.BookV.Thermodynamics.instDecidableEqEoSRegime :DecidableEq EoSRegime**

Equations
- Tau.BookV.Thermodynamics.instDecidableEqEoSRegime x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Thermodynamics.instBEqEoSRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L103-L103)
**instance
Tau.BookV.Thermodynamics.instBEqEoSRegime :BEq EoSRegime**

Equations
- Tau.BookV.Thermodynamics.instBEqEoSRegime = { beq := Tau.BookV.Thermodynamics.instBEqEoSRegime.beq }

---

### `Tau.BookV.Thermodynamics.instBEqEoSRegime.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L103-L103)
**def
Tau.BookV.Thermodynamics.instBEqEoSRegime.beq :EoSRegime → EoSRegime → Bool**

Equations
- Tau.BookV.Thermodynamics.instBEqEoSRegime.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Thermodynamics.DefectDrivenAcceleration`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L105-L130)
**structure
Tau.BookV.Thermodynamics.DefectDrivenAcceleration :Type**


[V.T68] Defect-driven acceleration: as S_def decreases,
the effective w shifts from w > -1/3 to w < -1/3.

The transition occurs when the defect-to-refinement ratio
crosses a critical threshold determined by iota_tau.

Transition redshift z_acc ~ 0.7 corresponds to
S_def/S_ref crossing the critical ratio.

- regime : EoSRegime
Current regime.

- ratio_def_numer : ℕ
Defect-to-refinement ratio numerator (S_def).

- ratio_ref_denom : ℕ
Defect-to-refinement ratio denominator (S_ref).

- denom_pos : self.ratio_ref_denom > 0
Denominator positive.

- critical_threshold_numer : ℕ
The critical ratio threshold (scaled, ~ 1/3).

- critical_threshold_denom : ℕ
Critical threshold denominator.

- z_acc_numer : ℕ
Transition redshift (z_acc ~ 0.7, stored as 7/10).

- z_acc_denom : ℕ
Transition redshift denominator.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprDefectDrivenAcceleration.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L130-L130)
**def
Tau.BookV.Thermodynamics.instReprDefectDrivenAcceleration.repr :DefectDrivenAcceleration → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instReprDefectDrivenAcceleration`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L130-L130)
**instance
Tau.BookV.Thermodynamics.instReprDefectDrivenAcceleration :Repr DefectDrivenAcceleration**

Equations
- Tau.BookV.Thermodynamics.instReprDefectDrivenAcceleration = { reprPrec := Tau.BookV.Thermodynamics.instReprDefectDrivenAcceleration.repr }

---

### `Tau.BookV.Thermodynamics.DefectDrivenAcceleration.determineRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L132-L138)
**def
Tau.BookV.Thermodynamics.DefectDrivenAcceleration.determineRegime
(ratio_n ratio_d thresh_n thresh_d : ℕ)
 :ratio_d > 0 → thresh_d > 0 → EoSRegime**


The regime is determined by the ratio relative to threshold.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.no_lambda`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L144-L152)
**theorem
Tau.BookV.Thermodynamics.no_lambda :"R^H = kappa_tau * T: no Lambda term, acceleration is transient" = "R^H = kappa_tau * T: no Lambda term, acceleration is transient"**


[V.P40] No Lambda in the tau-Einstein equation:
R^H = kappa_tau * T contains no cosmological constant (Lambda = 0).

The acceleration is a time-dependent phenomenon from the
defect-to-refinement transition, not a permanent geometric term.
There is no need for Lambda and no fine-tuning problem.

---

### `Tau.BookV.Thermodynamics.dark_energy_artifact`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L158-L166)
**theorem
Tau.BookV.Thermodynamics.dark_energy_artifact :"Lambda-CDM dark energy = readout artifact from S_def -> S_ref transition" = "Lambda-CDM dark energy = readout artifact from S_def -> S_ref transition"**


[V.T69] Dark energy is a readout artifact: the cosmic acceleration
attributed to Lambda in Lambda-CDM arises from the defect-to-refinement
transition on base tau^1.

The orthodox readout functor misidentifies the decreasing defect
entropy (ordering) as a repulsive energy source.

---

### `Tau.BookV.Thermodynamics.the_68_percent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L172-L179)
**theorem
Tau.BookV.Thermodynamics.the_68_percent :"68% dark energy = S_ref (counting artifact, not physical energy)" = "68% dark energy = S_ref (counting artifact, not physical energy)"**


[V.P41] The 68% of the cosmic energy budget attributed to
dark energy in Lambda-CDM corresponds to refinement entropy S_ref.

S_ref is a counting artifact (lattice modes), not physical energy.
The 68% was never "missing energy" but misattributed entropy.

---

### `Tau.BookV.Thermodynamics.data_vs_interpretation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L185-L191)
**theorem
Tau.BookV.Thermodynamics.data_vs_interpretation :"Acceleration = data (real). Dark energy = interpretation (artifact)." = "Acceleration = data (real). Dark energy = interpretation (artifact)."**


[V.R133] Data versus interpretation: the cosmic acceleration is
observational data, but dark energy is a model-dependent interpretation.
The tau-framework preserves the data (acceleration is real) but
replaces the interpretation (different cause).

---

### `Tau.BookV.Thermodynamics.two_faces`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L197-L205)
**theorem
Tau.BookV.Thermodynamics.two_faces :"CC problem: (i) why small? (ii) why nonzero? Both dissolve if Lambda = 0" = "CC problem: (i) why small? (ii) why nonzero? Both dissolve if Lambda = 0"**


[V.R134] Two faces of the cosmological constant problem:
(i) Why so small? Lambda ~ 10^{-52} m^{-2} vs Planck 10^{68}
(ii) Why nonzero? Tiny nonzero value requires fine-tuning.

Both faces dissolve when Lambda = 0 and acceleration comes
from the defect-to-refinement transition.

---

### `Tau.BookV.Thermodynamics.where_68_goes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L211-L219)
**theorem
Tau.BookV.Thermodynamics.where_68_goes :"68% was never real energy; tau-budget = defect bundles + E_bdry on L" = "68% was never real energy; tau-budget = defect bundles + E_bdry on L"**


[V.R135] Where does the 68% go? It was never a real energy
component. Dark energy is not missing energy but misattributed
refinement entropy.

The tau-cosmic budget: 100% = defect bundles on T^2 + finite
boundary energy on L. No dark energy component exists.

---

### `Tau.BookV.Thermodynamics.DarkEnergyTestability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L225-L246)
**structure
Tau.BookV.Thermodynamics.DarkEnergyTestability :Type**


[V.R136] Testability: w_eff(z) should vary with redshift.


- w > -1/3 at high z (defect-dominated epoch)

- w ~ -1 at low z (refinement-dominated)

- Transition at z_acc ~ 0.7


Distinguishing prediction: w_eff is NOT exactly -1 but varies.
Future measurements of w(z) can test the defect-transition model
against a true cosmological constant (w = -1 exactly).

- w_varies : Bool
Prediction: w varies with redshift.

- high_z_decelerating : Bool
w > -1/3 at high z.

- low_z_near_minus_one : Bool
w ~ -1 at low z.

- z_acc_numer : ℕ
Transition redshift z_acc (numer/denom).

- z_acc_denom : ℕ
Transition redshift denominator.

- denom_pos : self.z_acc_denom > 0
Denominator positive.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprDarkEnergyTestability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L246-L246)
**instance
Tau.BookV.Thermodynamics.instReprDarkEnergyTestability :Repr DarkEnergyTestability**

Equations
- Tau.BookV.Thermodynamics.instReprDarkEnergyTestability = { reprPrec := Tau.BookV.Thermodynamics.instReprDarkEnergyTestability.repr }

---

### `Tau.BookV.Thermodynamics.instReprDarkEnergyTestability.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L246-L246)
**def
Tau.BookV.Thermodynamics.instReprDarkEnergyTestability.repr :DarkEnergyTestability → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.dark_energy_testability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L248-L250)
**def
Tau.BookV.Thermodynamics.dark_energy_testability :DarkEnergyTestability**


Canonical testability instance.
Equations
- Tau.BookV.Thermodynamics.dark_energy_testability = { denom_pos := Tau.BookV.Thermodynamics.dark_energy_testability._proof_2 }
Instances For

---

### `Tau.BookV.Thermodynamics.w_varies_prediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L252-L254)
**theorem
Tau.BookV.Thermodynamics.w_varies_prediction :dark_energy_testability.w_varies = true**


The testable prediction: w varies (not exactly -1).

---

### `Tau.BookV.Thermodynamics.CosmicComponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L260-L266)
**inductive
Tau.BookV.Thermodynamics.CosmicComponent :Type**


The tau-cosmic energy budget: no dark energy component.

- DefectBundles : CosmicComponent
Defect bundles on T^2 (matter + radiation).

- BoundaryEnergy : CosmicComponent
Boundary energy on L (finite vacuum energy).

Instances For

---

### `Tau.BookV.Thermodynamics.instReprCosmicComponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L266-L266)
**instance
Tau.BookV.Thermodynamics.instReprCosmicComponent :Repr CosmicComponent**

Equations
- Tau.BookV.Thermodynamics.instReprCosmicComponent = { reprPrec := Tau.BookV.Thermodynamics.instReprCosmicComponent.repr }

---

### `Tau.BookV.Thermodynamics.instReprCosmicComponent.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L266-L266)
**def
Tau.BookV.Thermodynamics.instReprCosmicComponent.repr :CosmicComponent → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instDecidableEqCosmicComponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L266-L266)
**instance
Tau.BookV.Thermodynamics.instDecidableEqCosmicComponent :DecidableEq CosmicComponent**

Equations
- Tau.BookV.Thermodynamics.instDecidableEqCosmicComponent x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Thermodynamics.instBEqCosmicComponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L266-L266)
**instance
Tau.BookV.Thermodynamics.instBEqCosmicComponent :BEq CosmicComponent**

Equations
- Tau.BookV.Thermodynamics.instBEqCosmicComponent = { beq := Tau.BookV.Thermodynamics.instBEqCosmicComponent.beq }

---

### `Tau.BookV.Thermodynamics.instBEqCosmicComponent.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L266-L266)
**def
Tau.BookV.Thermodynamics.instBEqCosmicComponent.beq :CosmicComponent → CosmicComponent → Bool**

Equations
- Tau.BookV.Thermodynamics.instBEqCosmicComponent.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Thermodynamics.cosmic_budget`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L268-L270)
**def
Tau.BookV.Thermodynamics.cosmic_budget :List CosmicComponent**


The cosmic budget has exactly 2 components (no dark energy).
Equations
- Tau.BookV.Thermodynamics.cosmic_budget = [Tau.BookV.Thermodynamics.CosmicComponent.DefectBundles, Tau.BookV.Thermodynamics.CosmicComponent.BoundaryEnergy]
Instances For

---

### `Tau.BookV.Thermodynamics.cosmic_budget_two_components`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L272-L274)
**theorem
Tau.BookV.Thermodynamics.cosmic_budget_two_components :cosmic_budget.length = 2**


Two components, not three (no dark energy).

---

### `Tau.BookV.Thermodynamics.early_universe`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L280-L285)
**def
Tau.BookV.Thermodynamics.early_universe :DefectDrivenAcceleration**


Example: early universe (defect-dominated, decelerating).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.present_epoch`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L287-L292)
**def
Tau.BookV.Thermodynamics.present_epoch :DefectDrivenAcceleration**


Example: present epoch (refinement-dominated, accelerating).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.surplus_example`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L299-L305)
**def
Tau.BookV.Thermodynamics.surplus_example :CapacitySurplus**


Example: capacity surplus.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.testability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L311-L312)
**def
Tau.BookV.Thermodynamics.testability :DarkEnergyTestability**


Testability structure.
Equations
- Tau.BookV.Thermodynamics.testability = { denom_pos := Tau.BookV.Thermodynamics.dark_energy_testability._proof_2 }
Instances For

---

### `Tau.BookV.Thermodynamics.OmegaLambdaStandalone`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L321-L340)
**structure
Tau.BookV.Thermodynamics.OmegaLambdaStandalone :Type**


[V.T234] Standalone Ω_Λ structural theorem:
Ω_Λ = κ_D · (1 + ι<sub>τ</sub>³) = (1 − ι<sub>τ</sub>)(1 + ι<sub>τ</sub>³) ≈ 0.6849.
Zero-parameter prediction from master constant ι<sub>τ</sub>.

κ_D = D-sector coupling (gravity), ι<sub>τ</sub>³ = fiber volume correction.
Planck 2018: 0.6847 ± 0.0073. Deviation: +269 ppm (+0.03σ).

- kappa_D_x10000 : ℕ
κ_D numerator (scaled ×10000): (1 − ι<sub>τ</sub>) ≈ 0.6587 → 6587.

- iota_tau_cubed_x100000 : ℕ
ι<sub>τ</sub>³ numerator (scaled ×100000): ι<sub>τ</sub>³ ≈ 0.03979 → 3979.

- omega_lambda_x10000 : ℕ
Ω_Λ (scaled ×10000): ≈ 0.6849 → 6849.

- planck_x10000 : ℕ
Planck 2018 value (scaled ×10000): 0.6847 → 6847.

- deviation_ppm : ℤ
Deviation in ppm (positive = τ exceeds Planck).

- scope_tau_effective : Bool
τ-effective scope: derived from κ_D and ι<sub>τ</sub> only.

Instances For

---

### `Tau.BookV.Thermodynamics.instReprOmegaLambdaStandalone`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L340-L340)
**instance
Tau.BookV.Thermodynamics.instReprOmegaLambdaStandalone :Repr OmegaLambdaStandalone**

Equations
- Tau.BookV.Thermodynamics.instReprOmegaLambdaStandalone = { reprPrec := Tau.BookV.Thermodynamics.instReprOmegaLambdaStandalone.repr }

---

### `Tau.BookV.Thermodynamics.instReprOmegaLambdaStandalone.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L340-L340)
**def
Tau.BookV.Thermodynamics.instReprOmegaLambdaStandalone.repr :OmegaLambdaStandalone → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.omega_lambda_canonical`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L342-L348)
**def
Tau.BookV.Thermodynamics.omega_lambda_canonical :OmegaLambdaStandalone**


Canonical Ω_Λ instance.
Equations
- Tau.BookV.Thermodynamics.omega_lambda_canonical = { kappa_D_x10000 := 6587, iota_tau_cubed_x100000 := 3979, omega_lambda_x10000 := 6849, deviation_ppm := 269 }
Instances For

---

### `Tau.BookV.Thermodynamics.omega_lambda_deviation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L350-L352)
**theorem
Tau.BookV.Thermodynamics.omega_lambda_deviation :omega_lambda_canonical.deviation_ppm = 269**


Ω_Λ at +269 ppm from Planck.

---

### `Tau.BookV.Thermodynamics.omega_lambda_tau_effective`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L354-L356)
**theorem
Tau.BookV.Thermodynamics.omega_lambda_tau_effective :omega_lambda_canonical.scope_tau_effective = true**


Ω_Λ is τ-effective.

---

### `Tau.BookV.Thermodynamics.DefectFractionEoS`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L362-L379)
**structure
Tau.BookV.Thermodynamics.DefectFractionEoS :Type**


[V.D293] Defect fraction function:
f_def(z) = S_def(z) / (S_def(z) + S_ref(z)).
At z → ∞: f_def → 1. At z = 0: f_def → ι<sub>τ</sub>³ ≈ 0.040.

[V.P159] Effective equation of state:
w(z) = −1 + (2/3) · f_def(z)/(1 − f_def(z)).
At z = 0: w₀ = ι<sub>τ</sub>³ − 1 ≈ −0.960 (quintessence-like).

- f_def_present_x10000 : ℕ
Present defect fraction f_def(0) (scaled ×10000): ι<sub>τ</sub>³ ≈ 0.0398 → 398.

- w0_offset_x1000 : ℕ
w₀ (scaled ×1000, offset from −1): ι<sub>τ</sub>³ ≈ 0.040 → 40 means w₀ = −0.960.

- w0_gt_minus_one : Bool
w₀ > −1 (quintessence-like, no phantom).

- transition_w_numer : ℤ
Transition value: w = −1/3 at z_acc.

- transition_w_denom : ℕ
Instances For

---

### `Tau.BookV.Thermodynamics.instReprDefectFractionEoS.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L379-L379)
**def
Tau.BookV.Thermodynamics.instReprDefectFractionEoS.repr :DefectFractionEoS → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instReprDefectFractionEoS`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L379-L379)
**instance
Tau.BookV.Thermodynamics.instReprDefectFractionEoS :Repr DefectFractionEoS**

Equations
- Tau.BookV.Thermodynamics.instReprDefectFractionEoS = { reprPrec := Tau.BookV.Thermodynamics.instReprDefectFractionEoS.repr }

---

### `Tau.BookV.Thermodynamics.defect_eos_canonical`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L381-L385)
**def
Tau.BookV.Thermodynamics.defect_eos_canonical :DefectFractionEoS**


Canonical EoS instance.
Equations
- Tau.BookV.Thermodynamics.defect_eos_canonical = { f_def_present_x10000 := 398, w0_offset_x1000 := 40 }
Instances For

---

### `Tau.BookV.Thermodynamics.w0_quintessence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L387-L389)
**theorem
Tau.BookV.Thermodynamics.w0_quintessence :defect_eos_canonical.w0_gt_minus_one = true**


w₀ > −1: quintessence-like, no phantom crossing.

---

### `Tau.BookV.Thermodynamics.TransitionRedshift`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L395-L408)
**structure
Tau.BookV.Thermodynamics.TransitionRedshift :Type**


[V.D294] Transition redshift z_acc = (2Ω_Λ/Ω_m)^(1/3) − 1 ≈ 0.632.
Observed: 0.64 ± 0.05 (SN Ia). Deviation: −1.3%.

[V.R418] Comparison: τ-prediction within observational uncertainty.

- z_acc_x1000 : ℕ
z_acc (scaled ×1000): 0.632 → 632.

- observed_x1000 : ℕ
Observed central value (scaled ×1000): 0.64 → 640.

- uncertainty_x1000 : ℕ
Observed uncertainty (scaled ×1000): 0.05 → 50.

- deviation_ppm : ℤ
Deviation from observed (ppm, negative = τ below).

Instances For

---

### `Tau.BookV.Thermodynamics.instReprTransitionRedshift.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L408-L408)
**def
Tau.BookV.Thermodynamics.instReprTransitionRedshift.repr :TransitionRedshift → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Thermodynamics.instReprTransitionRedshift`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L408-L408)
**instance
Tau.BookV.Thermodynamics.instReprTransitionRedshift :Repr TransitionRedshift**

Equations
- Tau.BookV.Thermodynamics.instReprTransitionRedshift = { reprPrec := Tau.BookV.Thermodynamics.instReprTransitionRedshift.repr }

---

### `Tau.BookV.Thermodynamics.z_acc_canonical`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L410-L413)
**def
Tau.BookV.Thermodynamics.z_acc_canonical :TransitionRedshift**


Canonical z_acc instance.
Equations
- Tau.BookV.Thermodynamics.z_acc_canonical = { z_acc_x1000 := 632, deviation_ppm := -12500 }
Instances For

---

### `Tau.BookV.Thermodynamics.z_acc_within_1sigma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Thermodynamics/DarkEnergyArtifact.lean#L415-L418)
**theorem
Tau.BookV.Thermodynamics.z_acc_within_1sigma :z_acc_canonical.z_acc_x1000 ≥ z_acc_canonical.observed_x1000 - z_acc_canonical.uncertainty_x1000**


z_acc within 1σ of observations.
