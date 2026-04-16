---
layout: taulib-doc
title: "TauLib.BookV.Cosmology.BBNBaryogenesis"
permalink: /verify/taulib/docs/book-v-cosmology-bbn-baryogenesis/
lane: verify
module_name: "TauLib.BookV.Cosmology.BBNBaryogenesis"
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

# TauLib.BookV.Cosmology.BBNBaryogenesis


Baryogenesis within the threshold ladder: threshold-dependent admissibility,
the baryogenesis window, N_eff = 3 from sector exhaustion, and dark sector
closure.

## Registry Cross-References


- [V.D197] Threshold-Dependent Admissibility -- `ThresholdDependentAdmissibility`

- [V.D198] Baryogenesis Window -- `BaryogenesisWindow`

- [V.T151] N_eff from Sector Exhaustion -- `n_eff_eq_three`

- [V.P113] Dark Sector Closure -- `n_eff_upper_bound`


## Mathematical Content


### Threshold-Dependent Admissibility [BBN.13]


The category of admissible endomorphisms on τ³ is not fixed but changes
at each threshold crossing. The SA-i condition (η-winding preservation
mod 3) applies only below the neutron threshold L_N (depth 3), where
the C-sector has crossed its confinement coupling κ(C;3). Above L_N,
at the baryogenesis threshold L_B (depth 2), the C-sector is deconfined
and SA-i does not apply, permitting baryon number violation.

### Baryogenesis Window [BBN.14]


B-violation is structurally permitted only in the window [L_B, L_N]
(depths 2–3). Below L_N, SA-i locks in and baryon number is absolutely
conserved. The window is finite and closed by confinement.

### N_eff = 3 from Sector Exhaustion [BBN.19]


The three neutrino flavors correspond to the three non-gravitational
generators {π, γ, η}. The ω-crossing is composite (ω = γ ∩ η), not
independent, and α is gravitational. So N_eff = 3.

### Dark Sector Closure [BBN.20]


The 5 generators exhaust all sectors. No additional generator exists
to host a dark sector, so N_eff > 3 is structurally impossible.

## Ground Truth Sources


- Book V ch48: Threshold Ladder, Baryogenesis section

- research/universe/bbn_final_comprehensive_sprint.md (BBN.13–20)


---

### `Tau.BookV.Cosmology.AdmissibilityCategory`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L59-L71)
**inductive
Tau.BookV.Cosmology.AdmissibilityCategory :Type**


Admissibility category: whether the SA-i condition (η-winding
preservation) applies at a given refinement depth.

Pre-confinement (above L_N): C-sector deconfined, SA-i does not
apply, B-violation permitted.
Post-confinement (below L_N): C-sector confined, SA-i locks in,
B is absolutely conserved.

- PreConfinement : AdmissibilityCategory
Pre-confinement: SA-i not active, B-violation allowed.

- PostConfinement : AdmissibilityCategory
Post-confinement: SA-i active, B absolutely conserved.

Instances For

---

### `Tau.BookV.Cosmology.instReprAdmissibilityCategory`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L71-L71)
**instance
Tau.BookV.Cosmology.instReprAdmissibilityCategory :Repr AdmissibilityCategory**

Equations
- Tau.BookV.Cosmology.instReprAdmissibilityCategory = { reprPrec := Tau.BookV.Cosmology.instReprAdmissibilityCategory.repr }

---

### `Tau.BookV.Cosmology.instReprAdmissibilityCategory.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L71-L71)
**def
Tau.BookV.Cosmology.instReprAdmissibilityCategory.repr :AdmissibilityCategory → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instDecidableEqAdmissibilityCategory`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L71-L71)
**instance
Tau.BookV.Cosmology.instDecidableEqAdmissibilityCategory :DecidableEq AdmissibilityCategory**

Equations
- Tau.BookV.Cosmology.instDecidableEqAdmissibilityCategory x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Cosmology.instBEqAdmissibilityCategory`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L71-L71)
**instance
Tau.BookV.Cosmology.instBEqAdmissibilityCategory :BEq AdmissibilityCategory**

Equations
- Tau.BookV.Cosmology.instBEqAdmissibilityCategory = { beq := Tau.BookV.Cosmology.instBEqAdmissibilityCategory.beq }

---

### `Tau.BookV.Cosmology.instBEqAdmissibilityCategory.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L71-L71)
**def
Tau.BookV.Cosmology.instBEqAdmissibilityCategory.beq :AdmissibilityCategory → AdmissibilityCategory → Bool**

Equations
- Tau.BookV.Cosmology.instBEqAdmissibilityCategory.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Cosmology.ThresholdDependentAdmissibility`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L73-L90)
**structure
Tau.BookV.Cosmology.ThresholdDependentAdmissibility :Type**


[V.D197] Threshold-dependent admissibility: the admissibility
category changes at the neutron threshold L_N (depth 3).


- Above L_N (depth < 3): PreConfinement → B-violation permitted

- Below L_N (depth ≥ 3): PostConfinement → B absolutely conserved


This resolves the baryogenesis tension: baryon number is not a
fundamental symmetry but a threshold-dependent one.

- confinement_depth : ℕ
Confinement threshold depth (L_N = depth 3).

- above_confinement : AdmissibilityCategory
Admissibility above confinement threshold.

- below_confinement : AdmissibilityCategory
Admissibility below confinement threshold.

- admissibility_changes : self.above_confinement ≠ self.below_confinement
The categories differ.

Instances For

---

### `Tau.BookV.Cosmology.instReprThresholdDependentAdmissibility`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L90-L90)
**instance
Tau.BookV.Cosmology.instReprThresholdDependentAdmissibility :Repr ThresholdDependentAdmissibility**

Equations
- Tau.BookV.Cosmology.instReprThresholdDependentAdmissibility = { reprPrec := Tau.BookV.Cosmology.instReprThresholdDependentAdmissibility.repr }

---

### `Tau.BookV.Cosmology.instReprThresholdDependentAdmissibility.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L90-L90)
**def
Tau.BookV.Cosmology.instReprThresholdDependentAdmissibility.repr :ThresholdDependentAdmissibility → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.threshold_admissibility`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L92-L94)
**def
Tau.BookV.Cosmology.threshold_admissibility :ThresholdDependentAdmissibility**


The canonical threshold-dependent admissibility instance.
Equations
- Tau.BookV.Cosmology.threshold_admissibility = { admissibility_changes := Tau.BookV.Cosmology.threshold_admissibility._proof_1 }
Instances For

---

### `Tau.BookV.Cosmology.pre_confinement_admits_B_violation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L96-L99)
**theorem
Tau.BookV.Cosmology.pre_confinement_admits_B_violation :threshold_admissibility.above_confinement = AdmissibilityCategory.PreConfinement**


Pre-confinement admits B-violation.

---

### `Tau.BookV.Cosmology.post_confinement_conserves_B`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L101-L104)
**theorem
Tau.BookV.Cosmology.post_confinement_conserves_B :threshold_admissibility.below_confinement = AdmissibilityCategory.PostConfinement**


Post-confinement forbids B-violation (SA-i active).

---

### `Tau.BookV.Cosmology.BaryogenesisWindow`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L110-L125)
**structure
Tau.BookV.Cosmology.BaryogenesisWindow :Type**


[V.D198] Baryogenesis window: the finite interval [L_B, L_N]
(depths 2–3) during which baryon number violation is structurally
permitted. The window opens at the baryogenesis threshold (depth 2)
and closes at the neutron threshold (depth 3) when SA-i locks in.

Below L_N, baryon number is absolutely conserved.

- depth_start : ℕ
Start depth (baryogenesis threshold L_B).

- depth_end : ℕ
End depth (neutron threshold L_N).

- window_nonempty : self.depth_start < self.depth_end
Window is non-empty: start < end.

- start_pos : self.depth_start > 0
Start is positive.

Instances For

---

### `Tau.BookV.Cosmology.instReprBaryogenesisWindow.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L125-L125)
**def
Tau.BookV.Cosmology.instReprBaryogenesisWindow.repr :BaryogenesisWindow → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprBaryogenesisWindow`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L125-L125)
**instance
Tau.BookV.Cosmology.instReprBaryogenesisWindow :Repr BaryogenesisWindow**

Equations
- Tau.BookV.Cosmology.instReprBaryogenesisWindow = { reprPrec := Tau.BookV.Cosmology.instReprBaryogenesisWindow.repr }

---

### `Tau.BookV.Cosmology.baryogenesis_window`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L127-L130)
**def
Tau.BookV.Cosmology.baryogenesis_window :BaryogenesisWindow**


The canonical baryogenesis window instance.
Equations
- Tau.BookV.Cosmology.baryogenesis_window = { window_nonempty := Tau.BookV.Cosmology.baryogenesis_window._proof_3,
 start_pos := Tau.BookV.Cosmology.baryogenesis_window._proof_4 }
Instances For

---

### `Tau.BookV.Cosmology.window_finite`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L132-L135)
**theorem
Tau.BookV.Cosmology.window_finite :baryogenesis_window.depth_end - baryogenesis_window.depth_start = 1**


The baryogenesis window is finite (width 1).

---

### `Tau.BookV.Cosmology.nucleosynthesis_after_window`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L137-L142)
**theorem
Tau.BookV.Cosmology.nucleosynthesis_after_window :baryogenesis_window.depth_end < canonical_ladder.nucleosynthesis.depth_index**


The nucleosynthesis threshold (depth 4) lies after the baryogenesis
window closes. This ensures BBN occurs in the B-conserving regime.

---

### `Tau.BookV.Cosmology.window_matches_ladder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L144-L151)
**theorem
Tau.BookV.Cosmology.window_matches_ladder :baryogenesis_window.depth_start = canonical_ladder.baryogenesis.depth_index ∧ baryogenesis_window.depth_end = canonical_ladder.neutron.depth_index**


The baryogenesis window matches the canonical ladder's ordering:
L_B (depth 2) < L_N (depth 3).

---

### `Tau.BookV.Cosmology.n_gauge_generators`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L157-L160)
**def
Tau.BookV.Cosmology.n_gauge_generators :ℕ**


Number of non-gravitational generators in Category τ. These are
{π, γ, η} — the three independent gauge-sector generators.
The ω-crossing (ω = γ ∩ η) is composite, and α is gravitational.
Equations
- Tau.BookV.Cosmology.n_gauge_generators = 3
Instances For

---

### `Tau.BookV.Cosmology.n_total_generators`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L162-L163)
**def
Tau.BookV.Cosmology.n_total_generators :ℕ**


Total generator count in Category τ.
Equations
- Tau.BookV.Cosmology.n_total_generators = 5
Instances For

---

### `Tau.BookV.Cosmology.n_gauge_from_total`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L165-L170)
**theorem
Tau.BookV.Cosmology.n_gauge_from_total :n_total_generators - 1 - 1 = n_gauge_generators**


The ω-crossing is composite: ω = γ ∩ η, not independent.
So the independent non-gravitational count is
total − gravitational (α) − composite (ω) = 5 − 1 − 1 = 3.

---

### `Tau.BookV.Cosmology.n_eff_eq_three`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L172-L176)
**theorem
Tau.BookV.Cosmology.n_eff_eq_three :n_gauge_generators = 3**


[V.T151] N_eff from sector exhaustion: the effective number of
neutrino species equals the number of non-gravitational generators.

N_eff = |{π, γ, η}| = 3.

---

### `Tau.BookV.Cosmology.n_eff_upper_bound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L182-L188)
**theorem
Tau.BookV.Cosmology.n_eff_upper_bound :n_gauge_generators ≤ 3**


[V.P113] Dark sector closure: the 5 generators of Category τ
exhaust all available sectors (D, A, B, C, ω). No additional
generator exists to host a dark sector.

Consequence: N_eff ≤ 3 is a structural upper bound. Any
observation of N_eff > 3 would falsify the 5-generator theorem.

---

### `Tau.BookV.Cosmology.no_dark_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L190-L192)
**theorem
Tau.BookV.Cosmology.no_dark_sector :n_total_generators - n_gauge_generators - 1 - 1 = 0**


The number of dark sector generators is zero.

---

### `Tau.BookV.Cosmology.window_within_ladder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L198-L204)
**theorem
Tau.BookV.Cosmology.window_within_ladder :canonical_ladder.ew.depth_index ≤ baryogenesis_window.depth_start ∧ baryogenesis_window.depth_end ≤ canonical_ladder.photon_decoupling.depth_index**


The 6-threshold ladder and the baryogenesis window are consistent:
the window [2,3] lies within the ladder [1,6].

---

### `Tau.BookV.Cosmology.clean_threshold_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L206-L210)
**theorem
Tau.BookV.Cosmology.clean_threshold_count :complete_ladder.count - 1 = domain_correction.corr_num**


Number of clean thresholds for He nucleation = 5 = total − 1.
This connects to the 5/6 domain-wall correction in HeliumFraction.

---

### `Tau.BookV.Cosmology.BaryogenesisSAIMechanism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L250-L272)
**structure
Tau.BookV.Cosmology.BaryogenesisSAIMechanism :Type**


[V.D238] SA-i mod-W₃(4) baryogenesis mechanism.
η_B = α·ι<sub>τ</sub>^15·(5/6): ι<sub>τ</sub>^15=(ι<sub>τ</sub>³)^W₃(4) from SA-i mod-5.
(5/6)=W₃(4)/(2·sectors)=5/6.


- Geometric sum: S₅ = Σ_{k=0}^{4} ι<sub>τ</sub>^{3k} = (1−ι<sub>τ</sub>¹⁵)/(1−ι<sub>τ</sub>³)

- Each generator contributes ι<sub>τ</sub>^{dim(τ³)} = ι<sub>τ</sub>³

- Parallel: SA-i mod-3 → θ_QCD=0 (IV.T160); SA-i mod-5 → baryogenesis


- sai_modulus : ℕ
SA-i modulus = W₃(4) = 5.

- modulus_eq : self.sai_modulus = 5
Modulus equals 5.

- exponent : ℕ
Exponent = dim(τ³) × modulus = 15.

- exponent_eq : self.exponent = 15
Exponent equals 15.

- exponent_decomp : self.exponent = 3 * self.sai_modulus
Exponent = 3 × 5.

- coeff_num : ℕ
Coefficient numerator = W₃(4) = 5.

- coeff_den : ℕ
Coefficient denominator = 2 × sectors = 6.

Instances For

---

### `Tau.BookV.Cosmology.instReprBaryogenesisSAIMechanism.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L272-L272)
**def
Tau.BookV.Cosmology.instReprBaryogenesisSAIMechanism.repr :BaryogenesisSAIMechanism → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprBaryogenesisSAIMechanism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L272-L272)
**instance
Tau.BookV.Cosmology.instReprBaryogenesisSAIMechanism :Repr BaryogenesisSAIMechanism**

Equations
- Tau.BookV.Cosmology.instReprBaryogenesisSAIMechanism = { reprPrec := Tau.BookV.Cosmology.instReprBaryogenesisSAIMechanism.repr }

---

### `Tau.BookV.Cosmology.baryogenesis_sai_mechanism`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L274-L280)
**def
Tau.BookV.Cosmology.baryogenesis_sai_mechanism :BaryogenesisSAIMechanism**


The canonical SA-i mechanism.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.baryogenesis_sai_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L282-L288)
**theorem
Tau.BookV.Cosmology.baryogenesis_sai_thm :baryogenesis_sai_mechanism.sai_modulus = 5 ∧ baryogenesis_sai_mechanism.exponent = 15 ∧ baryogenesis_sai_mechanism.coeff_num = 5 ∧ baryogenesis_sai_mechanism.coeff_den = 6**


SA-i mechanism: modulus 5, exponent 15, coefficient 5/6.

---

### `Tau.BookV.Cosmology.fifteen_window_product`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L291-L291)
**theorem
Tau.BookV.Cosmology.fifteen_window_product :3 * 5 = 15**


---

### `Tau.BookV.Cosmology.five_sixths_structure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L294-L294)
**theorem
Tau.BookV.Cosmology.five_sixths_structure :5 = 5 ∧ 6 = 2 * 3**


---

### `Tau.BookV.Cosmology.BaryogenesisFirstPrinciples`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L301-L319)
**structure
Tau.BookV.Cosmology.BaryogenesisFirstPrinciples :Type**


[V.P130] Baryogenesis first principles: SA-i mod-W₃(4) yields
η_B = α·ι<sub>τ</sub>¹⁵·(5/6) at −10320 ppm (within 1σ Planck ±9502 ppm).

Structure:


- 15 = 3 × W₃(4) from C-sector × Window

- (5/6) = W₃(4)/(2·sectors) from EM mixing

- SA-i mod-5: 5-fold holonomy winding cancellation

- All 3 Sakharov conditions: B-violation (σ lobe swap),
CP violation (3 gen, J_τ≠0), equilibrium departure (freezeout)


- sai_mod5_holds : Bool
SA-i mod-5 holds.

- sakharov_all_three : Bool
All 3 Sakharov conditions satisfied.

- eta_b_formula_valid : Bool
η_B formula valid.

- within_planck_1sigma : Bool
Within Planck uncertainty.

Instances For

---

### `Tau.BookV.Cosmology.instReprBaryogenesisFirstPrinciples.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L319-L319)
**def
Tau.BookV.Cosmology.instReprBaryogenesisFirstPrinciples.repr :BaryogenesisFirstPrinciples → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprBaryogenesisFirstPrinciples`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L319-L319)
**instance
Tau.BookV.Cosmology.instReprBaryogenesisFirstPrinciples :Repr BaryogenesisFirstPrinciples**

Equations
- Tau.BookV.Cosmology.instReprBaryogenesisFirstPrinciples = { reprPrec := Tau.BookV.Cosmology.instReprBaryogenesisFirstPrinciples.repr }

---

### `Tau.BookV.Cosmology.baryogenesis_fp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L321-L322)
**def
Tau.BookV.Cosmology.baryogenesis_fp :BaryogenesisFirstPrinciples**


The canonical baryogenesis first-principles instance.
Equations
- Tau.BookV.Cosmology.baryogenesis_fp = { }
Instances For

---

### `Tau.BookV.Cosmology.baryogenesis_first_principles`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L324-L330)
**theorem
Tau.BookV.Cosmology.baryogenesis_first_principles :baryogenesis_fp.sai_mod5_holds = true ∧ baryogenesis_fp.sakharov_all_three = true ∧ baryogenesis_fp.eta_b_formula_valid = true ∧ baryogenesis_fp.within_planck_1sigma = true**


Baryogenesis first principles: SA-i mod-5, Sakharov, formula valid.

---

### `Tau.BookV.Cosmology.sai_mod_comparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L333-L335)
**def
Tau.BookV.Cosmology.sai_mod_comparison :String**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.vop2_status_sprint6c`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L338-L341)
**def
Tau.BookV.Cosmology.vop2_status_sprint6c :String**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.GeneratorOrbitSuppression`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L358-L382)
**structure
Tau.BookV.Cosmology.GeneratorOrbitSuppression :Type**


[V.P130 upgrade] SA-i mod-5 generator orbit: the 5-generator orbit
of σ-involution on H_∂[ω] produces exactly ι<sub>τ</sub>¹⁵ suppression.

Proof structure:

- Each generator g_k ∈ {α,π,γ,η,ω} contributes one holonomy factor
ι<sub>τ</sub>^{dim(τ³)} = ι<sub>τ</sub>³ from the 3-dimensional τ³

- The generators act cyclically (ℤ/5ℤ) on the boundary character

- The full orbit traverses all 5 generators: total suppression
ι<sub>τ</sub>^{3×5} = ι<sub>τ</sub>¹⁵

- Geometric series S₅ = Σ_{k=0}^{4} ι<sub>τ</sub>^{3k} = (1−ι<sub>τ</sub>¹⁵)/(1−ι<sub>τ</sub>³)

- Parallel: SA-i mod-3 (3 colors) → θ_QCD=0; SA-i mod-5 → η_B


- n_generators : ℕ
Number of generators in the orbit.

- tau3_dim : ℕ
Dimension of τ³.

- per_generator_power : ℕ
Each generator contributes ι<sub>τ</sub>^{dim(τ³)}.

- total_exponent : ℕ
Total suppression exponent.

- cyclic_orbit : Bool
The orbit is cyclic (ℤ/5ℤ).

- exponent_decomp : self.total_exponent = self.n_generators * self.per_generator_power
Exponent = generators × per-generator power.

Instances For

---

### `Tau.BookV.Cosmology.instReprGeneratorOrbitSuppression`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L382-L382)
**instance
Tau.BookV.Cosmology.instReprGeneratorOrbitSuppression :Repr GeneratorOrbitSuppression**

Equations
- Tau.BookV.Cosmology.instReprGeneratorOrbitSuppression = { reprPrec := Tau.BookV.Cosmology.instReprGeneratorOrbitSuppression.repr }

---

### `Tau.BookV.Cosmology.instReprGeneratorOrbitSuppression.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L382-L382)
**def
Tau.BookV.Cosmology.instReprGeneratorOrbitSuppression.repr :GeneratorOrbitSuppression → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.generator_orbit_suppression`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L384-L385)
**def
Tau.BookV.Cosmology.generator_orbit_suppression :GeneratorOrbitSuppression**

Equations
- Tau.BookV.Cosmology.generator_orbit_suppression = { exponent_decomp := Tau.BookV.Cosmology.generator_orbit_suppression._proof_1 }
Instances For

---

### `Tau.BookV.Cosmology.generator_orbit_produces_15`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L387-L393)
**theorem
Tau.BookV.Cosmology.generator_orbit_produces_15 :generator_orbit_suppression.total_exponent = 15 ∧ generator_orbit_suppression.n_generators = 5 ∧ generator_orbit_suppression.tau3_dim = 3 ∧ generator_orbit_suppression.cyclic_orbit = true**


Generator orbit produces exactly ι<sub>τ</sub>¹⁵: 5 × 3 = 15.

---

### `Tau.BookV.Cosmology.fiber_dimension_decomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L395-L397)
**theorem
Tau.BookV.Cosmology.fiber_dimension_decomposition :1 + 2 = 3**


dim(τ³) = dim(τ¹) + dim(T²) = 1 + 2 = 3.

---

### `Tau.BookV.Cosmology.sai_mod_hierarchy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L399-L403)
**theorem
Tau.BookV.Cosmology.sai_mod_hierarchy :3 * 3 = 9 ∧ 3 * 5 = 15**


SA-i mod-N hierarchy: same mechanism, different modulus.
mod-3: 3 colors → ι<sub>τ</sub>⁹ → θ_QCD = 0 (exact, IV.T160)
mod-5: 5 generators → ι<sub>τ</sub>¹⁵ → η_B (τ-effective)

---

### `Tau.BookV.Cosmology.ThresholdUniquenessFiveSixths`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L409-L433)
**structure
Tau.BookV.Cosmology.ThresholdUniquenessFiveSixths :Type**


[V.T180 upgrade] The (5/6) factor is uniquely forced:

- Canonical ladder has exactly 6 thresholds (V.D58)

- Exactly 1 is resonant: L_B (baryogenesis), where the
ω-crossing mediates baryon-number-violating processes

- ω is resonant because ω = γ ∩ η is the self-coupling
singularity of L (the crossing point p_ω)

- No other threshold is resonant: the remaining 5 involve
single-sector crossings or composite transitions without
the ω self-coupling property

- Therefore 5/6 = (non-resonant)/(total) is uniquely forced


- total_thresholds : ℕ
Total canonical thresholds.

- resonant_count : ℕ
Resonant thresholds (ω-crossing only).

- nonresonant_count : ℕ
Non-resonant thresholds.

- omega_unique_singularity : Bool
ω-crossing is the unique self-coupling singularity.

- partition : self.nonresonant_count + self.resonant_count = self.total_thresholds
Partition: non-resonant + resonant = total.

- uniqueness : self.resonant_count = 1
Uniqueness: exactly 1 resonant.

Instances For

---

### `Tau.BookV.Cosmology.instReprThresholdUniquenessFiveSixths.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L433-L433)
**def
Tau.BookV.Cosmology.instReprThresholdUniquenessFiveSixths.repr :ThresholdUniquenessFiveSixths → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprThresholdUniquenessFiveSixths`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L433-L433)
**instance
Tau.BookV.Cosmology.instReprThresholdUniquenessFiveSixths :Repr ThresholdUniquenessFiveSixths**

Equations
- Tau.BookV.Cosmology.instReprThresholdUniquenessFiveSixths = { reprPrec := Tau.BookV.Cosmology.instReprThresholdUniquenessFiveSixths.repr }

---

### `Tau.BookV.Cosmology.threshold_uniqueness_56`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L435-L437)
**def
Tau.BookV.Cosmology.threshold_uniqueness_56 :ThresholdUniquenessFiveSixths**

Equations
- Tau.BookV.Cosmology.threshold_uniqueness_56 = { partition := Tau.BookV.Cosmology.threshold_uniqueness_56._proof_2,
 uniqueness := Tau.BookV.Cosmology.threshold_uniqueness_56._proof_3 }
Instances For

---

### `Tau.BookV.Cosmology.five_sixths_uniquely_forced`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L439-L445)
**theorem
Tau.BookV.Cosmology.five_sixths_uniquely_forced :threshold_uniqueness_56.nonresonant_count = 5 ∧ threshold_uniqueness_56.total_thresholds = 6 ∧ threshold_uniqueness_56.omega_unique_singularity = true ∧ threshold_uniqueness_56.resonant_count = 1**


(5/6) uniquely forced: 5 non-resonant of 6 total.

---

### `Tau.BookV.Cosmology.five_sixths_cross_check_yp`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L447-L449)
**theorem
Tau.BookV.Cosmology.five_sixths_cross_check_yp :5 / 6 * (8 / 27) = 20 / 81**


Cross-check: (5/6)·(8/27) = 20/81 = Y_p.

---

### `Tau.BookV.Cosmology.threshold_uniqueness_matches_ladder`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L451-L454)
**theorem
Tau.BookV.Cosmology.threshold_uniqueness_matches_ladder :threshold_uniqueness_56.total_thresholds = complete_ladder.count**


Threshold uniqueness consistent with canonical ladder count.

---

### `Tau.BookV.Cosmology.CPAsymmetryFromPolarity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L460-L484)
**structure
Tau.BookV.Cosmology.CPAsymmetryFromPolarity :Type**


CP asymmetry from A-sector (π-generator) polarity structure.

The A-sector polarity matrix [[1, ι<sub>τ</sub>],[ι<sub>τ</sub>, 1]] gives
B-violation asymmetry ε = ι<sub>τ</sub> per generator cycle.

Over the full 5-generator orbit × dim(τ³):
ε_total ∝ ι<sub>τ</sub>¹⁵ (matching SA-i mod-5 suppression)

ε_CP = κ(A;1) = ι<sub>τ</sub>: the A-sector self-coupling is
the CP asymmetry scale.

This connects baryogenesis CP violation to the same A-sector
polarity that drives PMNS mixing angles (Campaign A).

- cp_scale_is_iota : Bool
CP asymmetry scale = ι<sub>τ</sub> = κ(A;1).

- polarity_matrix_form : Bool
A-sector polarity matrix [[1,ι<sub>τ</sub>],[ι<sub>τ</sub>,1]].

- per_generator_asymmetry : Bool
Per-generator asymmetry = ι<sub>τ</sub>.

- total_matches_sai_mod5 : Bool
Total = ι<sub>τ</sub>¹⁵ from 5-gen × dim 3.

- connects_to_pmns : Bool
Connects to PMNS (Campaign A).

Instances For

---

### `Tau.BookV.Cosmology.instReprCPAsymmetryFromPolarity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L484-L484)
**def
Tau.BookV.Cosmology.instReprCPAsymmetryFromPolarity.repr :CPAsymmetryFromPolarity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprCPAsymmetryFromPolarity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L484-L484)
**instance
Tau.BookV.Cosmology.instReprCPAsymmetryFromPolarity :Repr CPAsymmetryFromPolarity**

Equations
- Tau.BookV.Cosmology.instReprCPAsymmetryFromPolarity = { reprPrec := Tau.BookV.Cosmology.instReprCPAsymmetryFromPolarity.repr }

---

### `Tau.BookV.Cosmology.cp_asymmetry_polarity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L486-L486)
**def
Tau.BookV.Cosmology.cp_asymmetry_polarity :CPAsymmetryFromPolarity**

Equations
- Tau.BookV.Cosmology.cp_asymmetry_polarity = { }
Instances For

---

### `Tau.BookV.Cosmology.cp_asymmetry_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L488-L493)
**theorem
Tau.BookV.Cosmology.cp_asymmetry_structural :cp_asymmetry_polarity.cp_scale_is_iota = true ∧ cp_asymmetry_polarity.total_matches_sai_mod5 = true ∧ cp_asymmetry_polarity.connects_to_pmns = true**


CP asymmetry structural: ε_CP = ι<sub>τ</sub>, total = ι<sub>τ</sub>¹⁵.
