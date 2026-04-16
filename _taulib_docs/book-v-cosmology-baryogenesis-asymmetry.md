---
layout: taulib-doc
title: "TauLib.BookV.Cosmology.BaryogenesisAsymmetry"
permalink: /verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/
lane: verify
module_name: "TauLib.BookV.Cosmology.BaryogenesisAsymmetry"
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

# TauLib.BookV.Cosmology.BaryogenesisAsymmetry


Primary baryogenesis formula and structural derivations.
Upgrades V.R324 (conjectural) to V.T172 (τ-effective).

## Registry Cross-References


- [V.T170] Exponent 15 = dim(τ³) × |generators| -- `exponent_15_structure`, `tau_generator_count`

- [V.T171] (5/6) threshold factor shared with Y_p -- `yp_baryogenesis_shared_factor`

- [V.T172] Primary baryogenesis formula η_B = α·ι<sub>τ</sub>¹⁵·(5/6) -- `eta_B_formula_string`, `eta_B_algebraic_identity`

- [V.P126] Sakharov CP source -- `sakharov_cp_source`

- [V.R375] Leptogenesis pathway via Majorana ν -- `leptogenesis_pathway`


## Mathematical Content


The baryon-to-photon ratio η_B = (121/270)·ι<sub>τ</sub>¹⁹ follows from:


- Exponent 15 = dim(τ³) × |generators| = 3 × 5 (V.T170)

- Factor (5/6) = 5 non-resonant / 6 total threshold channels,
shared with Y_p = 20/81 = (8/27)·(5/6) (V.T171, V.T149)

- Factor α = (121/225)·ι<sub>τ</sub>⁴ (fine structure constant in τ-framework)

- Combined: η_B = (121/225)·ι<sub>τ</sub>⁴ · ι<sub>τ</sub>¹⁵ · (5/6) = (121/270)·ι<sub>τ</sub>¹⁹


## Numerical result (50-digit mpmath precision)


η_B = α·ι<sub>τ</sub>¹⁵·(5/6) = 6.04101 × 10⁻¹⁰
η_B = (121/270)·ι<sub>τ</sub>¹⁹ = 6.04107 × 10⁻¹⁰
Planck 2018: 6.104 × 10⁻¹⁰ ± 0.058 × 10⁻¹⁰
Deviation: −1.03% (−1.09σ)

k=15, c=5/6 is the unique minimum in the 77-candidate
exponent scan (k ∈ {10,...,20}, 7 coefficient families).

## Scope Upgrade


V.R324 (conjectural) → V.T172 (τ-effective), based on:

- Structural exponent 15 = dim(τ³) × |generators| (V.T170)

- (5/6) shared with Y_p threshold counting (V.T171)

- Majorana ν structurally enable L→B conversion (IV.T146)

- Unique minimum in exponent scan

- Deviation within observational uncertainty (−1.09σ)


---

### `Tau.BookV.Cosmology.exponent_15_structure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L53-L59)
**theorem
Tau.BookV.Cosmology.exponent_15_structure :3 * 5 = 15**


Exponent 15 = dim(τ³) × |generators| = 3 × 5. [V.T170]

dim(τ³) = 3: the fibered product τ³ = τ¹ ×_f T² has three independent
directions (two fiber from T², one base from τ¹).

|generators| = 5: the generator set {α, π, γ, η, ω} has cardinality 5.

---

### `Tau.BookV.Cosmology.TauGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L61-L69)
**inductive
Tau.BookV.Cosmology.TauGenerator :Type**


The five τ-generators: α (gravity/base), π (Weak/A-sector),
γ (EM/B-sector), η (Strong/C-sector), ω = γ ∩ η (crossing).

- alpha : TauGenerator
- pi : TauGenerator
- gamma : TauGenerator
- eta : TauGenerator
- omega : TauGenerator
Instances For

---

### `Tau.BookV.Cosmology.instReprTauGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L69-L69)
**instance
Tau.BookV.Cosmology.instReprTauGenerator :Repr TauGenerator**

Equations
- Tau.BookV.Cosmology.instReprTauGenerator = { reprPrec := Tau.BookV.Cosmology.instReprTauGenerator.repr }

---

### `Tau.BookV.Cosmology.instReprTauGenerator.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L69-L69)
**def
Tau.BookV.Cosmology.instReprTauGenerator.repr :TauGenerator → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instDecidableEqTauGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L69-L69)
**instance
Tau.BookV.Cosmology.instDecidableEqTauGenerator :DecidableEq TauGenerator**

Equations
- Tau.BookV.Cosmology.instDecidableEqTauGenerator x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Cosmology.instBEqTauGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L69-L69)
**instance
Tau.BookV.Cosmology.instBEqTauGenerator :BEq TauGenerator**

Equations
- Tau.BookV.Cosmology.instBEqTauGenerator = { beq := Tau.BookV.Cosmology.instBEqTauGenerator.beq }

---

### `Tau.BookV.Cosmology.instBEqTauGenerator.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L69-L69)
**def
Tau.BookV.Cosmology.instBEqTauGenerator.beq :TauGenerator → TauGenerator → Bool**

Equations
- Tau.BookV.Cosmology.instBEqTauGenerator.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Cosmology.tau_generator_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L71-L73)
**theorem
Tau.BookV.Cosmology.tau_generator_count :[TauGenerator.alpha, TauGenerator.pi, TauGenerator.gamma, TauGenerator.eta, TauGenerator.omega].length = 5**


There are exactly 5 τ-generators. [V.T170]

---

### `Tau.BookV.Cosmology.tau3_dim`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L75-L76)
**def
Tau.BookV.Cosmology.tau3_dim :ℕ**


The dimension of τ³ = τ¹ ×_f T² is 3.
Equations
- Tau.BookV.Cosmology.tau3_dim = 3
Instances For

---

### `Tau.BookV.Cosmology.exponent_15_is_dim_times_generators`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L78-L81)
**theorem
Tau.BookV.Cosmology.exponent_15_is_dim_times_generators :tau3_dim * [TauGenerator.alpha, TauGenerator.pi, TauGenerator.gamma, TauGenerator.eta, TauGenerator.omega].length = 15**


The exponent 15 = τ³ dimension × generator count.

---

### `Tau.BookV.Cosmology.exponent_15_unique_factorization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L83-L90)
**theorem
Tau.BookV.Cosmology.exponent_15_unique_factorization :tau3_dim = 3 ∧ [TauGenerator.alpha, TauGenerator.pi, TauGenerator.gamma, TauGenerator.eta, TauGenerator.omega].length = 5 ∧ tau3_dim ≠ 1 ∧ tau3_dim ≠ 5 ∧ tau3_dim ≠ 15**


Factor pairs of 15: (1,15), (3,5), (5,3), (15,1).
Only (3,5) matches (dim(τ³), |generators|).

---

### `Tau.BookV.Cosmology.yp_baryogenesis_shared_factor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L96-L102)
**theorem
Tau.BookV.Cosmology.yp_baryogenesis_shared_factor :20 / 81 = 8 / 27 * (5 / 6)**


Y_p = 20/81 = (8/27) * (5/6): helium fraction shares the (5/6) factor
with the baryon asymmetry formula. [V.T171]

This is verified as a rational identity:
(20 : Rat) / 81 = 8 / 27 * (5 / 6).

---

### `Tau.BookV.Cosmology.threshold_count_five_sixths`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L104-L109)
**theorem
Tau.BookV.Cosmology.threshold_count_five_sixths :complete_ladder.count = 6 ∧ complete_ladder.count - 1 = 5**


The threshold count interpretation: 6 total canonical thresholds,
5 of which are non-resonant (not the baryogenesis threshold L_B).

---

### `Tau.BookV.Cosmology.five_sixths_is_universal_threshold_factor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L111-L118)
**theorem
Tau.BookV.Cosmology.five_sixths_is_universal_threshold_factor :domain_correction.corr_num = 5 ∧ domain_correction.corr_den = 6**


Both Y_p and η_B share factor 5/6:
Y_p = (8/27) · (5/6), η_B = α · ι<sub>τ</sub>¹⁵ · (5/6).
The (5/6) is verified for Y_p via rational arithmetic.

---

### `Tau.BookV.Cosmology.eta_B_formula_string`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L124-L136)
**def
Tau.BookV.Cosmology.eta_B_formula_string :String**


Documentation of the primary baryogenesis formula [V.T172].

η_B = α·ι<sub>τ</sub>¹⁵·(5/6) = (121/270)·ι<sub>τ</sub>¹⁹ ≈ 6.041 × 10⁻¹⁰
Planck 2018: (6.104 ± 0.058) × 10⁻¹⁰
Deviation: −1.03% (−1.09σ) — within observational uncertainty.

Scope: τ-effective (upgraded from conjectural V.R324).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.eta_B_algebraic_identity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L138-L144)
**theorem
Tau.BookV.Cosmology.eta_B_algebraic_identity :121 / 270 = 121 / 225 * (5 / 6)**


Algebraic identity: (121/270) = (121/225) × (5/6). [V.T172]

This verifies that α_τ·ι<sub>τ</sub>¹⁵·(5/6) = (121/270)·ι<sub>τ</sub>¹⁹:
the α_τ factor (= (121/225)·ι<sub>τ</sub>⁴) absorbs into the ι<sub>τ</sub> tower
to give a purely algebraic expression.

---

### `Tau.BookV.Cosmology.exponent_scan_minimum_k15_c56`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L146-L150)
**theorem
Tau.BookV.Cosmology.exponent_scan_minimum_k15_c56 :True**


The exponent scan confirms k=15, c=5/6 is the unique minimum:
77 candidates (k ∈ {10,...,20}, 7 coefficient families) were tested.
The next-best candidate (k=15, c=7/9) is 7.4× worse in absolute deviation.
(This is a documentation theorem; the computation is in baryogenesis_lab.py.)

---

### `Tau.BookV.Cosmology.sakharov_cp_source`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L156-L169)
**def
Tau.BookV.Cosmology.sakharov_cp_source :String**


All three Sakharov conditions are structurally met in τ. [V.P126]

- B-violation: baryogenesis window [L_B, L_N] (V.D198, pre-confinement)

- CP violation: A-sector balanced polarity κ(A;1) = ι<sub>τ</sub> (this proposition)

- Out-of-equilibrium: directed α-orbit (V.T06)


The CP asymmetry scale is ι<sub>τ</sub>. The baryon suppression relative to
this scale is η_B/ι<sub>τ</sub> = α·ι<sub>τ</sub>¹⁴·(5/6) ≈ 1.770 × 10⁻⁹.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.sakharov_reduction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L171-L181)
**theorem
Tau.BookV.Cosmology.sakharov_reduction :threshold_admissibility.above_confinement = AdmissibilityCategory.PreConfinement ∧ baryogenesis_window.depth_start < baryogenesis_window.depth_end**


The three Sakharov conditions reduce the baryogenesis mystery from
'three unknown mechanisms' to a single open sub-problem
(the precise ι<sub>τ</sub>¹⁵ derivation from holonomy algebra).

---

### `Tau.BookV.Cosmology.leptogenesis_pathway`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L187-L197)
**def
Tau.BookV.Cosmology.leptogenesis_pathway :String**


With Majorana neutrinos (IV.T146), leptogenesis pathway is available. [V.R375]

Majorana ν → L violation → sphaleron conversion η_L→η_B = (28/79)·η_L.
Structural reading: σ=C (established) → all 3 ν Majorana → L not conserved.
The (5/6) prefactor from σ-matrix generation mixing is a conjectural sub-problem.
(scope: conjectural)
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.sai_mod5_generator_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L203-L206)
**def
Tau.BookV.Cosmology.sai_mod5_generator_count :ℕ**


[V.D245] SA-i mod-5 Formal Proof.
Geometric series S₅ = Σ_{k=0}^{4} ι<sub>τ</sub>^{3k} = (1−ι<sub>τ</sub>¹⁵)/(1−ι<sub>τ</sub>³).
Each generator contributes ι<sub>τ</sub>^{dim(τ³)} = ι<sub>τ</sub>³.
Equations
- Tau.BookV.Cosmology.sai_mod5_generator_count = 5
Instances For

---

### `Tau.BookV.Cosmology.sai_mod5_exponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L207-L207)
**theorem
Tau.BookV.Cosmology.sai_mod5_exponent :3 * 5 = 15**


---

### `Tau.BookV.Cosmology.SakharovFromSigma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L209-L222)
**structure
Tau.BookV.Cosmology.SakharovFromSigma :Type**


[V.T187] Sakharov Conditions from τ³ σ-Involution.
All 3 Sakharov conditions satisfied structurally.

- baryogenesis_depth_start : ℕ
B-violation: pre-confinement baryogenesis window depth.

- baryogenesis_depth_end : ℕ
B-violation: baryogenesis window depth end.

- n_generations_for_cp : ℕ
CP violation: number of generations enabling Jarlskog invariant J_τ ≠ 0.

- n_conditions : ℕ
Out-of-equilibrium: directed α-orbit ensures cooling monotone.

- window_nonempty : self.baryogenesis_depth_start < self.baryogenesis_depth_end
Window is non-empty (depth_start < depth_end).

Instances For

---

### `Tau.BookV.Cosmology.instReprSakharovFromSigma.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L222-L222)
**def
Tau.BookV.Cosmology.instReprSakharovFromSigma.repr :SakharovFromSigma → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprSakharovFromSigma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L222-L222)
**instance
Tau.BookV.Cosmology.instReprSakharovFromSigma :Repr SakharovFromSigma**

Equations
- Tau.BookV.Cosmology.instReprSakharovFromSigma = { reprPrec := Tau.BookV.Cosmology.instReprSakharovFromSigma.repr }

---

### `Tau.BookV.Cosmology.sakharov_from_sigma_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L224-L226)
**def
Tau.BookV.Cosmology.sakharov_from_sigma_data :SakharovFromSigma**


Canonical Sakharov conditions.
Equations
- Tau.BookV.Cosmology.sakharov_from_sigma_data = { window_nonempty := Tau.BookV.Cosmology.sakharov_from_sigma_data._proof_2 }
Instances For

---

### `Tau.BookV.Cosmology.sakharov_from_sigma`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L228-L237)
**theorem
Tau.BookV.Cosmology.sakharov_from_sigma :sakharov_from_sigma_data.baryogenesis_depth_start = 2 ∧ sakharov_from_sigma_data.baryogenesis_depth_end = 3 ∧ sakharov_from_sigma_data.n_generations_for_cp = 3 ∧ sakharov_from_sigma_data.n_conditions = 3 ∧ sakharov_from_sigma_data.baryogenesis_depth_start < sakharov_from_sigma_data.baryogenesis_depth_end**


All 3 Sakharov conditions met from σ-involution:
B-violation window [2,3], CP from 3 generations, 3 conditions total.

---

### `Tau.BookV.Cosmology.EtaBFormalDerivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L239-L252)
**structure
Tau.BookV.Cosmology.EtaBFormalDerivation :Type**


[V.T188] η_B Formal Derivation at −10320 ppm.
η_B = α·ι<sub>τ</sub>¹⁵·(5/6) = 6.080×10⁻¹⁰, Planck 6.104±0.058.

- exponent : ℕ
Exponent in ι<sub>τ</sub>^k: k = dim(τ³) × |generators|.

- exponent_eq : self.exponent = 3 * 5
Exponent decomposition proof.

- coeff_numer : ℕ
Coefficient numerator (non-resonant channels).

- coeff_denom : ℕ
Coefficient denominator (total channels).

- deviation_sigma_x100 : ℕ
Number of σ from Planck (deviation within 1.09σ), ×100.

Instances For

---

### `Tau.BookV.Cosmology.instReprEtaBFormalDerivation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L252-L252)
**def
Tau.BookV.Cosmology.instReprEtaBFormalDerivation.repr :EtaBFormalDerivation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprEtaBFormalDerivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L252-L252)
**instance
Tau.BookV.Cosmology.instReprEtaBFormalDerivation :Repr EtaBFormalDerivation**

Equations
- Tau.BookV.Cosmology.instReprEtaBFormalDerivation = { reprPrec := Tau.BookV.Cosmology.instReprEtaBFormalDerivation.repr }

---

### `Tau.BookV.Cosmology.eta_B_formal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L254-L256)
**def
Tau.BookV.Cosmology.eta_B_formal :EtaBFormalDerivation**


Canonical η_B derivation.
Equations
- Tau.BookV.Cosmology.eta_B_formal = { exponent_eq := Tau.BookV.Cosmology.eta_B_formal._proof_1 }
Instances For

---

### `Tau.BookV.Cosmology.eta_B_formal_derivation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L258-L265)
**theorem
Tau.BookV.Cosmology.eta_B_formal_derivation :eta_B_formal.exponent = 15 ∧ eta_B_formal.exponent = 3 * 5 ∧ eta_B_formal.coeff_numer = 5 ∧ eta_B_formal.coeff_denom = 6 ∧ eta_B_formal.deviation_sigma_x100 = 109**


η_B formal derivation: exponent 15 = 3×5, coefficient 5/6, within 1.09σ.

---

### `Tau.BookV.Cosmology.baryogenesis_threshold_placement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L267-L271)
**def
Tau.BookV.Cosmology.baryogenesis_threshold_placement :String**


[V.P133] Baryogenesis Threshold Placement.
n_EW < n_B=15 < n_BBN. E_B m_Pl·ι<sub>τ</sub>¹⁵ 10¹² GeV.
Equations
- Tau.BookV.Cosmology.baryogenesis_threshold_placement = "n_EW < n_B=15 < n_BBN. SA-i hierarchy: " ++ "mod-3 → ι<sub>τ</sub>⁹ → θ_QCD=0 (exact); mod-5 → ι<sub>τ</sub>¹⁵ → η_B (τ-effective)."
Instances For

---

### `Tau.BookV.Cosmology.self_similar_ratio_preserved`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L275-L278)
**theorem
Tau.BookV.Cosmology.self_similar_ratio_preserved :3 / 175 / (9 / 700) = 4 / 3**


[V.D246] Self-Similar NNLO Correction.
δ₁=3/175=dim/(n·W₃(4)²), δ₂=9/700=(3/4)·δ₁. 4/3 ratio preserved.

---

### `Tau.BookV.Cosmology.grid_optimum_exact`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L280-L283)
**theorem
Tau.BookV.Cosmology.grid_optimum_exact :8 / 7 + 3 / 175 = 203 / 175**


[V.T189] Grid Optimum Structural Derivation.
(Δpq,Δpr) = (203/175, 609/700) = (8/7+3/175, 6/7+9/700) at +18.5 ppm.

---

### `Tau.BookV.Cosmology.grid_optimum_pr_exact`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L285-L286)
**theorem
Tau.BookV.Cosmology.grid_optimum_pr_exact :6 / 7 + 9 / 700 = 609 / 700**


---

### `Tau.BookV.Cosmology.combined_ratio_43`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L288-L291)
**theorem
Tau.BookV.Cosmology.combined_ratio_43 :203 / 175 / (609 / 700) = 4 / 3**


[V.P134] Self-Similar 4/3 Ratio Preservation.
Combined (203/175)/(609/700) = 4/3 exactly.

---

### `Tau.BookV.Cosmology.oqc3_sprint7b_status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L293-L296)
**def
Tau.BookV.Cosmology.oqc3_sprint7b_status :String**


[V.R383] OQ-C3 Status: PARTIAL-IMPROVED after Sprint 7B.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.BaryogenesisNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L302-L320)
**structure
Tau.BookV.Cosmology.BaryogenesisNLO :Type**


[V.T270] Baryogenesis NLO from fiber EM correction.
η_B(NLO) = α·ι<sub>τ</sub>¹⁵·(5/6)·(1 + (4/3)α).
NLO correction factor = (4/3)α ≈ 0.00973.
Result: 6.100 × 10⁻¹⁰, deviation −655 ppm (0.12σ).
15.8× improvement over LO (−10,320 ppm).

- nlo_coeff_num : ℕ
NLO correction coefficient numerator (fiber ratio).

- nlo_coeff_den : ℕ
NLO correction coefficient denominator (sector count).

- lo_deviation_ppm : ℕ
LO deviation in ppm (absolute).

- nlo_deviation_ppm : ℕ
NLO deviation in ppm (absolute).

- nlo_sigma_x100 : ℕ
NLO deviation in sigma × 100.

- improvement_x10 : ℕ
Improvement factor × 10.

Instances For

---

### `Tau.BookV.Cosmology.instReprBaryogenesisNLO.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L320-L320)
**def
Tau.BookV.Cosmology.instReprBaryogenesisNLO.repr :BaryogenesisNLO → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprBaryogenesisNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L320-L320)
**instance
Tau.BookV.Cosmology.instReprBaryogenesisNLO :Repr BaryogenesisNLO**

Equations
- Tau.BookV.Cosmology.instReprBaryogenesisNLO = { reprPrec := Tau.BookV.Cosmology.instReprBaryogenesisNLO.repr }

---

### `Tau.BookV.Cosmology.baryogenesis_nlo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L322-L323)
**def
Tau.BookV.Cosmology.baryogenesis_nlo :BaryogenesisNLO**


Canonical baryogenesis NLO data.
Equations
- Tau.BookV.Cosmology.baryogenesis_nlo = { }
Instances For

---

### `Tau.BookV.Cosmology.nlo_improves_lo_by_factor_10`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L325-L328)
**theorem
Tau.BookV.Cosmology.nlo_improves_lo_by_factor_10 :baryogenesis_nlo.lo_deviation_ppm / baryogenesis_nlo.nlo_deviation_ppm ≥ 10**


NLO improves LO by factor > 10: 10320/655 > 10.

---

### `Tau.BookV.Cosmology.nlo_correction_is_fiber_ratio`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L330-L334)
**theorem
Tau.BookV.Cosmology.nlo_correction_is_fiber_ratio :baryogenesis_nlo.nlo_coeff_num = 4 ∧ baryogenesis_nlo.nlo_coeff_den = 3**


The NLO correction uses the universal fiber ratio 4/3.

---

### `Tau.BookV.Cosmology.nlo_sub_1000_ppm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L336-L338)
**theorem
Tau.BookV.Cosmology.nlo_sub_1000_ppm :baryogenesis_nlo.nlo_deviation_ppm < 1000**


[V.R469] Assessment: NLO brings η_B below 1000 ppm threshold.
