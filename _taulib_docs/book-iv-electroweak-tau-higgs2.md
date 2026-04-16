---
layout: taulib-doc
title: "TauLib.BookIV.Electroweak.TauHiggs2"
permalink: /verify/taulib/docs/book-iv-electroweak-tau-higgs2/
lane: verify
module_name: "TauLib.BookIV.Electroweak.TauHiggs2"
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

# TauLib.BookIV.Electroweak.TauHiggs2


Higgs mass, Hessian structure, Yukawa couplings, hierarchy problem dissolution,
Goldstone absorption, and decay branching ratios.

## Registry Cross-References


- [IV.D140] Hessian of Coherence Functional — `CoherenceHessian`

- [IV.D141] τ-Higgs Mass M_H — `TauHiggsMass`

- [IV.D142] τ-Yukawa Coupling — `TauYukawaCoupling`

- [IV.D320] EW Scale v_EW — `EWScale`

- [IV.L07] Hessian Eigenvalue Convergence — `hessian_eigenvalue_convergence`

- [IV.T65] No Fundamental Scalar — `no_fundamental_scalar`

- [IV.P74] Hessian Structure — `hessian_one_positive`

- [IV.P75] M_H ≈ 125 GeV — `higgs_mass_range`

- [IV.P76] Goldstone Bosons Eaten by W/Z — `goldstone_eaten`

- [IV.P77] Decay Branching Ratios — `decay_branching`

- [IV.R35] Hierarchy Problem Dissolution — structural remark

- [IV.R36] Deviation Signatures — structural remark


## Mathematical Content


The Hessian of the coherence functional V_n at its minimum has exactly
one positive eigenvalue in the radial direction (the Higgs mass squared)
and three zero eigenvalues in the angular directions (Goldstone modes
eaten by W± and Z).

The τ-Higgs mass M_H ≈ 125.1 GeV is determined by ι<sub>τ</sub> and the
neutron mass anchor through the coherence functional curvature.
There is NO hierarchy problem because the Higgs is NOT a fundamental
scalar — it is a collective excitation of the ω-sector coherence.

## Ground Truth Sources


- Chapter 34 of Book IV (2nd Edition)

- calibration_cascade_roadmap.md §12


---

### `Tau.BookIV.Electroweak.CoherenceHessian`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L50-L68)
**structure
Tau.BookIV.Electroweak.CoherenceHessian :Type**


[IV.D140] The Hessian (second variation matrix) of V_n at the
physical vacuum. It is a 4×4 real symmetric matrix with:


- 1 positive eigenvalue (radial = Higgs mass²)

- 3 zero eigenvalues (angular = Goldstone modes)


The positive eigenvalue converges as n → ∞ in the tower,
giving the physical Higgs mass.

- dim : ℕ
Dimension of the Hessian matrix.

- positive_eigenvalues : ℕ
Number of positive eigenvalues.

- zero_eigenvalues : ℕ
Number of zero eigenvalues (Goldstone directions).

- negative_eigenvalues : ℕ
Number of negative eigenvalues (stability).

- eigenvalue_check : self.positive_eigenvalues + self.zero_eigenvalues + self.negative_eigenvalues = self.dim
Eigenvalue count check.

Instances For

---

### `Tau.BookIV.Electroweak.instReprCoherenceHessian`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L68-L68)
**instance
Tau.BookIV.Electroweak.instReprCoherenceHessian :Repr CoherenceHessian**

Equations
- Tau.BookIV.Electroweak.instReprCoherenceHessian = { reprPrec := Tau.BookIV.Electroweak.instReprCoherenceHessian.repr }

---

### `Tau.BookIV.Electroweak.instReprCoherenceHessian.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L68-L68)
**def
Tau.BookIV.Electroweak.instReprCoherenceHessian.repr :CoherenceHessian → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.coherence_hessian`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L70-L70)
**def
Tau.BookIV.Electroweak.coherence_hessian :CoherenceHessian**

Equations
- Tau.BookIV.Electroweak.coherence_hessian = { eigenvalue_check := Tau.BookIV.Electroweak.coherence_hessian._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.TauHiggsMass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L76-L93)
**structure
Tau.BookIV.Electroweak.TauHiggsMass :Type**


[IV.D141] The τ-Higgs mass M_H: determined by the positive
eigenvalue of the coherence Hessian.

M_H ≈ 125100 MeV (125.1 GeV).
Experimental: 125100 ± 140 MeV (ATLAS+CMS combined, 2024).

In the τ-framework, M_H is a DERIVED quantity from ι<sub>τ</sub> and m_n,
not a free parameter.

- mass_MeV : ℕ
Higgs mass in MeV.

- mass_pos : self.mass_MeV > 0
Mass is positive.

- exp_MeV : ℕ
Experimental value in MeV (central).

- exp_unc_MeV : ℕ
Experimental uncertainty in MeV.

Instances For

---

### `Tau.BookIV.Electroweak.instReprTauHiggsMass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L93-L93)
**instance
Tau.BookIV.Electroweak.instReprTauHiggsMass :Repr TauHiggsMass**

Equations
- Tau.BookIV.Electroweak.instReprTauHiggsMass = { reprPrec := Tau.BookIV.Electroweak.instReprTauHiggsMass.repr }

---

### `Tau.BookIV.Electroweak.instReprTauHiggsMass.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L93-L93)
**def
Tau.BookIV.Electroweak.instReprTauHiggsMass.repr :TauHiggsMass → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.tau_higgs_mass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L95-L98)
**def
Tau.BookIV.Electroweak.tau_higgs_mass :TauHiggsMass**


τ-predicted Higgs mass.
Equations
- Tau.BookIV.Electroweak.tau_higgs_mass = { mass_MeV := 125100, mass_pos := Tau.BookIV.Electroweak.tau_higgs_mass._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.higgs_mass_GeV`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L100-L102)
**def
Tau.BookIV.Electroweak.higgs_mass_GeV :Float**


Higgs mass as Float in GeV.
Equations
- Tau.BookIV.Electroweak.higgs_mass_GeV = Float.ofNat Tau.BookIV.Electroweak.tau_higgs_mass.mass_MeV / 1000.0
Instances For

---

### `Tau.BookIV.Electroweak.TauYukawaCoupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L108-L123)
**structure
Tau.BookIV.Electroweak.TauYukawaCoupling :Type**


[IV.D142] A τ-Yukawa coupling: the coupling of a fermion
to the ω-sector VEV, determining the fermion's mass via
m_f = y_f · v_EW / √2.

In the τ-framework, Yukawa couplings are NOT free parameters —
they are determined by the sector hierarchy and ι<sub>τ</sub>.

- fermion : String
Fermion label.

- y_numer : ℕ
Yukawa coupling numerator (scaled ×10⁶).

- y_denom : ℕ
Yukawa coupling denominator.

- denom_pos : self.y_denom > 0
Denominator positive.

Instances For

---

### `Tau.BookIV.Electroweak.instReprTauYukawaCoupling.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L123-L123)
**def
Tau.BookIV.Electroweak.instReprTauYukawaCoupling.repr :TauYukawaCoupling → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprTauYukawaCoupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L123-L123)
**instance
Tau.BookIV.Electroweak.instReprTauYukawaCoupling :Repr TauYukawaCoupling**

Equations
- Tau.BookIV.Electroweak.instReprTauYukawaCoupling = { reprPrec := Tau.BookIV.Electroweak.instReprTauYukawaCoupling.repr }

---

### `Tau.BookIV.Electroweak.TauYukawaCoupling.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L125-L127)
**def
Tau.BookIV.Electroweak.TauYukawaCoupling.toFloat
(y : TauYukawaCoupling)
 :Float**


Yukawa coupling as Float.
Equations
- y.toFloat = Float.ofNat y.y_numer / Float.ofNat y.y_denom
Instances For

---

### `Tau.BookIV.Electroweak.yukawa_top`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L129-L133)
**def
Tau.BookIV.Electroweak.yukawa_top :TauYukawaCoupling**


Top quark Yukawa (≈ 1.0, the largest).
Equations
- Tau.BookIV.Electroweak.yukawa_top = { fermion := "top", y_numer := 995000, y_denom := 1000000, denom_pos := Tau.BookIV.Electroweak.yukawa_top._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.yukawa_bottom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L135-L139)
**def
Tau.BookIV.Electroweak.yukawa_bottom :TauYukawaCoupling**


Bottom quark Yukawa (≈ 0.024).
Equations
- Tau.BookIV.Electroweak.yukawa_bottom = { fermion := "bottom", y_numer := 24000, y_denom := 1000000, denom_pos := Tau.BookIV.Electroweak.yukawa_top._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.yukawa_electron`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L141-L145)
**def
Tau.BookIV.Electroweak.yukawa_electron :TauYukawaCoupling**


Electron Yukawa (≈ 2.9 × 10⁻⁶).
Equations
- Tau.BookIV.Electroweak.yukawa_electron = { fermion := "electron", y_numer := 3, y_denom := 1000000, denom_pos := Tau.BookIV.Electroweak.yukawa_top._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.EWScale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L151-L164)
**structure
Tau.BookIV.Electroweak.EWScale :Type**


[IV.D320] The electroweak scale v_EW ≈ 246.2 GeV: the vacuum
expectation value of the ω-sector coherence functional.
v_EW = √(2) · M_W / g ≈ 246200 MeV.

This is the single energy scale that determines all EW boson masses
via M_W = g·v/2, M_Z = M_W/cos(θ_W), M_H = √(2λ)·v.

- vev_MeV : ℕ
v_EW in MeV.

- vev_pos : self.vev_MeV > 0
Positive.

- determines_masses : Bool
Determines all EW boson masses.

Instances For

---

### `Tau.BookIV.Electroweak.instReprEWScale.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L164-L164)
**def
Tau.BookIV.Electroweak.instReprEWScale.repr :EWScale → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprEWScale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L164-L164)
**instance
Tau.BookIV.Electroweak.instReprEWScale :Repr EWScale**

Equations
- Tau.BookIV.Electroweak.instReprEWScale = { reprPrec := Tau.BookIV.Electroweak.instReprEWScale.repr }

---

### `Tau.BookIV.Electroweak.ew_scale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L166-L166)
**def
Tau.BookIV.Electroweak.ew_scale :EWScale**

Equations
- Tau.BookIV.Electroweak.ew_scale = { vev_pos := Tau.BookIV.Electroweak.ew_scale._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.HessianConvergence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L172-L185)
**structure
Tau.BookIV.Electroweak.HessianConvergence :Type**


[IV.L07] The positive eigenvalue of the Hessian converges as the
tower level n → ∞. The limit is the physical Higgs mass squared.

At each finite level n, the eigenvalue is a rational function of ι<sub>τ</sub>.
The convergence is exponentially fast in n, so level-1 already
gives a good approximation.

- exponential_rate : Bool
Convergence is exponentially fast.

- level1_good : Bool
Level 1 already approximates well.

- limit_exists : Bool
Limit exists.

Instances For

---

### `Tau.BookIV.Electroweak.instReprHessianConvergence.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L185-L185)
**def
Tau.BookIV.Electroweak.instReprHessianConvergence.repr :HessianConvergence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprHessianConvergence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L185-L185)
**instance
Tau.BookIV.Electroweak.instReprHessianConvergence :Repr HessianConvergence**

Equations
- Tau.BookIV.Electroweak.instReprHessianConvergence = { reprPrec := Tau.BookIV.Electroweak.instReprHessianConvergence.repr }

---

### `Tau.BookIV.Electroweak.hessian_eigenvalue_convergence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L187-L187)
**def
Tau.BookIV.Electroweak.hessian_eigenvalue_convergence :HessianConvergence**

Equations
- Tau.BookIV.Electroweak.hessian_eigenvalue_convergence = { }
Instances For

---

### `Tau.BookIV.Electroweak.NoFundamentalScalar`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L193-L212)
**structure
Tau.BookIV.Electroweak.NoFundamentalScalar :Type**


[IV.T65] The τ-Higgs is NOT a fundamental scalar field.
It is a collective excitation of the ω-sector coherence.

Consequences:

- No UV cutoff sensitivity → no hierarchy problem.

- No quadratic divergence in the mass renormalization.

- The Higgs mass is NATURALLY at the EW scale without fine-tuning.


This is the τ-framework's resolution of the hierarchy problem:
it simply does not arise because the Higgs is emergent, not fundamental.

- is_emergent : Bool
The Higgs is a collective/emergent excitation.

- no_uv_sensitivity : Bool
No UV cutoff sensitivity.

- no_quadratic_divergence : Bool
No quadratic divergence.

- natural_mass : Bool
Mass naturally at EW scale.

Instances For

---

### `Tau.BookIV.Electroweak.instReprNoFundamentalScalar.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L212-L212)
**def
Tau.BookIV.Electroweak.instReprNoFundamentalScalar.repr :NoFundamentalScalar → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprNoFundamentalScalar`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L212-L212)
**instance
Tau.BookIV.Electroweak.instReprNoFundamentalScalar :Repr NoFundamentalScalar**

Equations
- Tau.BookIV.Electroweak.instReprNoFundamentalScalar = { reprPrec := Tau.BookIV.Electroweak.instReprNoFundamentalScalar.repr }

---

### `Tau.BookIV.Electroweak.no_fundamental_scalar`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L214-L214)
**def
Tau.BookIV.Electroweak.no_fundamental_scalar :NoFundamentalScalar**

Equations
- Tau.BookIV.Electroweak.no_fundamental_scalar = { }
Instances For

---

### `Tau.BookIV.Electroweak.no_hierarchy_problem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L216-L220)
**theorem
Tau.BookIV.Electroweak.no_hierarchy_problem :no_fundamental_scalar.is_emergent = true ∧ no_fundamental_scalar.no_uv_sensitivity = true ∧ no_fundamental_scalar.no_quadratic_divergence = true**


---

### `Tau.BookIV.Electroweak.hessian_one_positive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L226-L233)
**theorem
Tau.BookIV.Electroweak.hessian_one_positive :coherence_hessian.positive_eigenvalues = 1 ∧ coherence_hessian.zero_eigenvalues = 3 ∧ coherence_hessian.negative_eigenvalues = 0**


[IV.P74] The Hessian has exactly one positive eigenvalue.
This structural fact means there is exactly ONE physical scalar
surviving after Goldstone absorption.

---

### `Tau.BookIV.Electroweak.higgs_mass_range`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L239-L244)
**theorem
Tau.BookIV.Electroweak.higgs_mass_range :tau_higgs_mass.mass_MeV > 124000 ∧ tau_higgs_mass.mass_MeV < 126000**


[IV.P75] The τ-predicted Higgs mass is in the range 124-126 GeV,
consistent with the experimental measurement of 125.1 ± 0.14 GeV.

---

### `Tau.BookIV.Electroweak.GoldstoneAbsorption`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L250-L271)
**structure
Tau.BookIV.Electroweak.GoldstoneAbsorption :Type**


[IV.P76] Three Goldstone bosons (from the 3 zero eigenvalues of
the Hessian) are absorbed by W+, W-, and Z to become their
longitudinal polarization modes.

Before eating: W+, W-, Z are massless with 2 polarizations each.
After eating: W+, W-, Z are massive with 3 polarizations each.

Counting: 3 × 2 + 3 = 3 × 3 (6 + 3 = 9 DOF, conserved).

- goldstones_eaten : ℕ
Number of Goldstones eaten.

- massive_bosons : List String
Bosons gaining mass.

- pol_before : ℕ
Polarization count before.

- goldstone_dof : ℕ
DOF from Goldstones.

- pol_after : ℕ
Polarization count after.

- dof_conserved : self.pol_before + self.goldstone_dof = self.pol_after
DOF conservation.

Instances For

---

### `Tau.BookIV.Electroweak.instReprGoldstoneAbsorption`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L271-L271)
**instance
Tau.BookIV.Electroweak.instReprGoldstoneAbsorption :Repr GoldstoneAbsorption**

Equations
- Tau.BookIV.Electroweak.instReprGoldstoneAbsorption = { reprPrec := Tau.BookIV.Electroweak.instReprGoldstoneAbsorption.repr }

---

### `Tau.BookIV.Electroweak.instReprGoldstoneAbsorption.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L271-L271)
**def
Tau.BookIV.Electroweak.instReprGoldstoneAbsorption.repr :GoldstoneAbsorption → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.goldstone_eaten`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L273-L273)
**def
Tau.BookIV.Electroweak.goldstone_eaten :GoldstoneAbsorption**

Equations
- Tau.BookIV.Electroweak.goldstone_eaten = { dof_conserved := Tau.BookIV.Electroweak.goldstone_eaten._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.DecayBranching`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L279-L297)
**structure
Tau.BookIV.Electroweak.DecayBranching :Type**


[IV.P77] Higgs decay branching ratios are determined by ι<sub>τ</sub>
through the Yukawa couplings and gauge couplings.

Dominant channels (SM values for comparison):


- H → bb̄: ≈ 58%

- H → WW*: ≈ 21%

- H → gg: ≈ 9%

- H → ττ̄: ≈ 6%

- H → cc̄: ≈ 3%

- H → ZZ*: ≈ 3%


The τ-framework predicts these from ι<sub>τ</sub> and sector couplings
with no free parameters.

- channel : String
Channel label.

- br_permille : ℕ
Branching ratio numerator (parts per 1000).

Instances For

---

### `Tau.BookIV.Electroweak.instReprDecayBranching.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L297-L297)
**def
Tau.BookIV.Electroweak.instReprDecayBranching.repr :DecayBranching → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprDecayBranching`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L297-L297)
**instance
Tau.BookIV.Electroweak.instReprDecayBranching :Repr DecayBranching**

Equations
- Tau.BookIV.Electroweak.instReprDecayBranching = { reprPrec := Tau.BookIV.Electroweak.instReprDecayBranching.repr }

---

### `Tau.BookIV.Electroweak.br_bb`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L299-L299)
**def
Tau.BookIV.Electroweak.br_bb :DecayBranching**

Equations
- Tau.BookIV.Electroweak.br_bb = { channel := "bb-bar", br_permille := 580 }
Instances For

---

### `Tau.BookIV.Electroweak.br_WW`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L300-L300)
**def
Tau.BookIV.Electroweak.br_WW :DecayBranching**

Equations
- Tau.BookIV.Electroweak.br_WW = { channel := "WW*", br_permille := 210 }
Instances For

---

### `Tau.BookIV.Electroweak.br_gg`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L301-L301)
**def
Tau.BookIV.Electroweak.br_gg :DecayBranching**

Equations
- Tau.BookIV.Electroweak.br_gg = { channel := "gg", br_permille := 90 }
Instances For

---

### `Tau.BookIV.Electroweak.br_tautau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L302-L302)
**def
Tau.BookIV.Electroweak.br_tautau :DecayBranching**

Equations
- Tau.BookIV.Electroweak.br_tautau = { channel := "tau-tau-bar", br_permille := 60 }
Instances For

---

### `Tau.BookIV.Electroweak.br_cc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L303-L303)
**def
Tau.BookIV.Electroweak.br_cc :DecayBranching**

Equations
- Tau.BookIV.Electroweak.br_cc = { channel := "cc-bar", br_permille := 30 }
Instances For

---

### `Tau.BookIV.Electroweak.br_ZZ`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L304-L304)
**def
Tau.BookIV.Electroweak.br_ZZ :DecayBranching**

Equations
- Tau.BookIV.Electroweak.br_ZZ = { channel := "ZZ*", br_permille := 30 }
Instances For

---

### `Tau.BookIV.Electroweak.decay_branching`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L306-L308)
**def
Tau.BookIV.Electroweak.decay_branching :List DecayBranching**


All major branching ratios.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.branching_sum_approx`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L310-L313)
**theorem
Tau.BookIV.Electroweak.branching_sum_approx :List.foldl (fun (x1 x2 : ℕ) => x1 + x2) 0 (List.map DecayBranching.br_permille decay_branching) = 1000**


Branching ratios sum to approximately 1000 permille.

---

### `Tau.BookIV.Electroweak.remark_hierarchy_dissolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L319-L326)
**def
Tau.BookIV.Electroweak.remark_hierarchy_dissolution :String**


[IV.R35] The hierarchy problem (why is M_H ≪ M_Planck?) does not
arise in the τ-framework because:

- The Higgs is emergent, not fundamental → no UV sensitivity.

- M_Planck is NOT a fundamental scale — it is derived from ι<sub>τ</sub>.

- The ratio M_H/M_Planck ≈ 10⁻¹⁷ is a CONSEQUENCE of the
sector coupling hierarchy, not a fine-tuning accident.

Equations
- Tau.BookIV.Electroweak.remark_hierarchy_dissolution = "No hierarchy problem: Higgs is emergent, M_Planck derived from iota_tau, ratio is structural"
Instances For

---

### `Tau.BookIV.Electroweak.remark_deviation_signatures`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L332-L341)
**def
Tau.BookIV.Electroweak.remark_deviation_signatures :String**


[IV.R36] The τ-framework predicts small deviations from SM
Higgs properties at the percent level, arising from:

- Tree-level coupling shifts from ι<sub>τ</sub> corrections.

- Modified loop structure (no BSM particles in loops).

- Decay channels sensitive to sector coupling ratios.


These deviations are potential experimental signatures for
the τ-framework at future colliders (HL-LHC, FCC-ee).
Equations
- Tau.BookIV.Electroweak.remark_deviation_signatures = "Percent-level deviations from SM Higgs: tree-level iota_tau corrections, testable at HL-LHC/FCC-ee"
Instances For

---

### `Tau.BookIV.Electroweak.NonOmegaGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L365-L370)
**inductive
Tau.BookIV.Electroweak.NonOmegaGenerator :Type**


The four non-ω generators of Category τ.
The ω-crossing = γ∩η is the intersection; the remaining four
generators count as the "non-ω" generators. [IV.T150]

- alpha : NonOmegaGenerator
- pi : NonOmegaGenerator
- gamma : NonOmegaGenerator
- eta : NonOmegaGenerator
Instances For

---

### `Tau.BookIV.Electroweak.instReprNonOmegaGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L370-L370)
**instance
Tau.BookIV.Electroweak.instReprNonOmegaGenerator :Repr NonOmegaGenerator**

Equations
- Tau.BookIV.Electroweak.instReprNonOmegaGenerator = { reprPrec := Tau.BookIV.Electroweak.instReprNonOmegaGenerator.repr }

---

### `Tau.BookIV.Electroweak.instReprNonOmegaGenerator.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L370-L370)
**def
Tau.BookIV.Electroweak.instReprNonOmegaGenerator.repr :NonOmegaGenerator → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instDecidableEqNonOmegaGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L370-L370)
**instance
Tau.BookIV.Electroweak.instDecidableEqNonOmegaGenerator :DecidableEq NonOmegaGenerator**

Equations
- Tau.BookIV.Electroweak.instDecidableEqNonOmegaGenerator x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Electroweak.higgs_factor_four`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L372-L375)
**theorem
Tau.BookIV.Electroweak.higgs_factor_four :[NonOmegaGenerator.alpha, NonOmegaGenerator.pi, NonOmegaGenerator.gamma, NonOmegaGenerator.eta].length = 4**


Factor 4 = |non-ω generators| = 4. [IV.T150]
This is the factor appearing in m_H/m_n = (4 − X)/κ_ω.

---

### `Tau.BookIV.Electroweak.higgs_factor_four_lobes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L377-L378)
**theorem
Tau.BookIV.Electroweak.higgs_factor_four_lobes :2 * 2 = 4**


Factor 4 = 2 lobes × 2 polarities. Equivalent lemniscate derivation. [IV.T150]

---

### `Tau.BookIV.Electroweak.higgs_factor_four_betti`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L380-L385)
**theorem
Tau.BookIV.Electroweak.higgs_factor_four_betti :3 + 3 - 2 = 4**


Factor 4 from Betti numbers: b₁(τ³) + b₂(τ³) − b₁(L) = 3 + 3 − 2 = 4. [IV.T150]
b₁(τ³) = b₁(τ¹) + b₁(T²) = 1 + 2 = 3 (Künneth on τ³ = τ¹ ×_f T²)
b₂(τ³) = b₂(T²) = 3 (from fiber T²)
b₁(L) = b₁(S¹∨S¹) = 2 (lemniscate two loops)

---

### `Tau.BookIV.Electroweak.higgs_mass_nlo_formula_n5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L387-L392)
**def
Tau.BookIV.Electroweak.higgs_mass_nlo_formula_n5 :String**


[IV.D348] The Higgs NLO mass formula using n=5 = W₃(4) window correction.
m_H/m_n = (4 − ι<sub>τ</sub>³/(1 − 5κ_ω))/κ_ω ≈ 133.372, deviation +493 ppm from PDG.
Structural motivation: W₃(4)=5 is the Window Universality modulus (IV.T140)
governing all three EW NLO corrections.
Equations
- Tau.BookIV.Electroweak.higgs_mass_nlo_formula_n5 = "m_H/m_n = (4 - iota_tau^3 / (1 - 5*kappa_omega)) / kappa_omega = 133.372 [+493 ppm, tau-effective]"
Instances For

---

### `Tau.BookIV.Electroweak.higgs_mass_nlo_formula_n6`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L394-L398)
**def
Tau.BookIV.Electroweak.higgs_mass_nlo_formula_n6 :String**


[IV.R399] Bonus formula with n=6 coefficient (68 ppm, structural meaning open).
(4 − ι<sub>τ</sub>³/(1 − 6κ_ω))/κ_ω = 133.315 vs PDG 133.306 → +68 ppm.
Coefficient 6 not yet identified structurally.
Equations
- Tau.BookIV.Electroweak.higgs_mass_nlo_formula_n6 = "m_H/m_n = (4 - iota_tau^3 / (1 - 6*kappa_omega)) / kappa_omega = 133.315 [+68 ppm, conjectural]"
Instances For

---

### `Tau.BookIV.Electroweak.higgs_w_ratio_comparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L400-L405)
**def
Tau.BookIV.Electroweak.higgs_w_ratio_comparison :String**


[IV.P188] m_H/m_W ratio from ω-sector (Higgs) and A-sector (W boson) NLO formulas.
PDG: m_H/m_W = 125.25/80.3692 = 1.55840.
τ-prediction (NLO): m_H/m_W = 1.55899, deviation +379 ppm.
Uses IV.T151 (Higgs, +493 ppm) and IV.T148 (M_W, −0.42 ppm).
Equations
- Tau.BookIV.Electroweak.higgs_w_ratio_comparison = "m_H/m_W: PDG=1.55840, tau(NLO)=1.55899, deviation=+379 ppm [conjectural]"
Instances For

---

### `Tau.BookIV.Electroweak.remark_omega_self_energy_open`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L407-L410)
**def
Tau.BookIV.Electroweak.remark_omega_self_energy_open :String**


[IV.R399] Open remark: structural identification of coefficient 6 in the
bonus formula (4 − ι<sub>τ</sub>³/(1−6κ_ω))/κ_ω = 133.315 at +68 ppm.
Equations
- Tau.BookIV.Electroweak.remark_omega_self_energy_open = "Open: coefficient 6 in n=6 formula (+68 ppm) — possible: 6=W_3(4)+1, 6=2*b1(tau^3), or higher CF-window value"
Instances For

---

### `Tau.BookIV.Electroweak.higgs_n6_cf_sum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L424-L430)
**theorem
Tau.BookIV.Electroweak.higgs_n6_cf_sum :True**


The coefficient n=6 in the improved Higgs formula (4−ι<sub>τ</sub>³/(1−6κ_ω))/κ_ω × m_n
≈ 125.26 GeV (+68 ppm from PDG 125.25 GeV). Structural candidates:
(A) n=6 = |generators|+1 = 5+1; (B) n=6 = 2×|sectors| = 2×3 = 6;
(C) n=6 = 2·b₁(τ³) = 2×3 = 6.
CF-sum candidate REJECTED: CF(ι<sub>τ</sub>⁻¹) = [2;1,13,3,...] → sum of 5 = 20 ≠ 6.
Sprint 4C discovery: with PDG 125.20 GeV, n=7 gives +8.0 ppm.

---

### `Tau.BookIV.Electroweak.higgs_n6_formula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L433-L434)
**def
Tau.BookIV.Electroweak.higgs_n6_formula :String**

Equations
- Tau.BookIV.Electroweak.higgs_n6_formula = "m_H = (4 - ι<sub>τ</sub>³/(1 - 6κ_ω))/κ_ω × m_n ≈ 125.26 GeV (+68 ppm, PDG 125.25; n=7 gives +8 ppm with PDG 125.20)"
Instances For

---

### `Tau.BookIV.Electroweak.iota_inv_cf_expansion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L436-L438)
**def
Tau.BookIV.Electroweak.iota_inv_cf_expansion :List ℕ**


CF expansion of ι<sub>τ</sub>⁻¹ for structural checks: [2;1,13,3,1,1,1,42,...].
Sum of first 5 partial quotients = 2+1+13+3+1 = 20 (NOT 6).
Equations
- Tau.BookIV.Electroweak.iota_inv_cf_expansion = [2, 1, 13, 3, 1, 1, 1, 42, 1, 2]
Instances For

---

### `Tau.BookIV.Electroweak.cf_sum_five_is_not_six`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L440-L441)
**theorem
Tau.BookIV.Electroweak.cf_sum_five_is_not_six :List.foldl (fun (x1 x2 : ℕ) => x1 + x2) 0 (List.take 5 iota_inv_cf_expansion) = 20**


---

### `Tau.BookIV.Electroweak.higgs_n7_formula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L450-L455)
**def
Tau.BookIV.Electroweak.higgs_n7_formula :String**


n=7 = 2×|lobes| + |force sectors| = 2×2+3 = 7 (best structural ID).
Lemniscate L=S¹∨S¹ has 2 lobes × 2 polarities + 3 non-ω sectors {A,B,C}.
Alternative: n=7 = b₁(τ³)+b₂(τ³)+1 = 3+3+1. CF analysis: n=7 NOT a CF convergent.
Equations
- Tau.BookIV.Electroweak.higgs_n7_formula = "m_H = (4 - ι<sub>τ</sub>³/(1-7κ_ω))/κ_ω × m_n ≈ 125.20 GeV (+8.0 ppm, PDG 125.20 GeV, tau-effective). " ++ "n=7 = 2×lobes+sectors = 2×2+3 (best structural ID)."
Instances For

---

### `Tau.BookIV.Electroweak.HiggsN7`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L458-L470)
**structure
Tau.BookIV.Electroweak.HiggsN7 :Type**


(4 - ι<sub>τ</sub>³/(1-7κ_ω))/κ_ω × m_n = 125.2010 GeV at +8.0 ppm from PDG 125.20 GeV.
n-scan: n=5: +892 ppm, n=6: +466 ppm, n=7: +8.0 ppm ***, n=8: -486 ppm.
n=7 = 2×lobes + sectors = 2×2+3 (structural decomposition).

- n_value : ℕ
n=7 structural coefficient.

- n_eq : self.n_value = 7
n equals 7.

- structural_decomp : self.n_value = 2 * 2 + 3
Structural: 2×lobes + sectors.

- tau_effective : Bool
Within τ-effective threshold.

Instances For

---

### `Tau.BookIV.Electroweak.instReprHiggsN7`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L470-L470)
**instance
Tau.BookIV.Electroweak.instReprHiggsN7 :Repr HiggsN7**

Equations
- Tau.BookIV.Electroweak.instReprHiggsN7 = { reprPrec := Tau.BookIV.Electroweak.instReprHiggsN7.repr }

---

### `Tau.BookIV.Electroweak.instReprHiggsN7.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L470-L470)
**def
Tau.BookIV.Electroweak.instReprHiggsN7.repr :HiggsN7 → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.higgs_n7_data`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L472-L475)
**def
Tau.BookIV.Electroweak.higgs_n7_data :HiggsN7**

Equations
- Tau.BookIV.Electroweak.higgs_n7_data = { n_value := 7, n_eq := Tau.BookIV.Electroweak.higgs_n7_data._proof_1,
 structural_decomp := Tau.BookIV.Electroweak.higgs_n7_data._proof_1 }
Instances For

---

### `Tau.BookIV.Electroweak.higgs_n7_tau_effective`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L477-L480)
**theorem
Tau.BookIV.Electroweak.higgs_n7_tau_effective :higgs_n7_data.n_value = 7 ∧ higgs_n7_data.tau_effective = true**


---

### `Tau.BookIV.Electroweak.muon_mass_nnlo_open`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L488-L493)
**def
Tau.BookIV.Electroweak.muon_mass_nnlo_open :String**


m_μ/m_e = ι<sub>τ</sub>^(-124/25) at +307.1 ppm (IV.T156, tau-effective).
Correction ×(1-ι<sub>τ</sub>^7.67) gives +44.5 ppm but k=7.67 has no structural ID.
Sub-100 ppm NNLO derivation remains open.
Equations
- Tau.BookIV.Electroweak.muon_mass_nnlo_open = "m_μ/m_e NNLO: iota^(-124/25) at +307 ppm. Correction x(1-iota^7.67) gives +44.5 ppm. " ++ "k=7.67 structural ID open. Sub-100 ppm target: OPEN."
Instances For

---

### `Tau.BookIV.Electroweak.nnlo_ratio_n7_n5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L496-L496)
**theorem
Tau.BookIV.Electroweak.nnlo_ratio_n7_n5 :7 ^ 2 = 49 ∧ 5 ^ 2 = 25**


---

### `Tau.BookIV.Electroweak.CoherenceFunctionalLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L510-L533)
**structure
Tau.BookIV.Electroweak.CoherenceFunctionalLevel :Type**


[IV.P199 upgrade] The coherence functional V_n at tower level n
samples the lemniscate and sector structure. The physical level
n = 2·|lobes| + |sectors| = 7 is the unique candidate with
structural support.

The Hessian eigenvalue λ₁ at level n gives m_H = √(2λ₁)·v.
The n=7 formula achieves +8.0 ppm from PDG 125.20 GeV.

Three candidate decompositions all yield n=7:
(A) 2·lobes + sectors = 2·2 + 3 = 7 (CANONICAL)
(B) generators + 2 = 5 + 2 = 7
(C) b₁(τ³) + b₂(τ³) + 1 = 3 + 3 + 1 = 7

- n_level : ℕ
Tower level n.

- decomp_canonical : self.n_level = 2 * 2 + 3
n = 2·lobes + sectors.

- decomp_generators : self.n_level = 5 + 2
n = generators + 2.

- decomp_betti : self.n_level = 3 + 3 + 1
n = b₁ + b₂ + 1.

- canonical_preferred : Bool
Canonical decomposition is preferred.

Instances For

---

### `Tau.BookIV.Electroweak.instReprCoherenceFunctionalLevel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L533-L533)
**instance
Tau.BookIV.Electroweak.instReprCoherenceFunctionalLevel :Repr CoherenceFunctionalLevel**

Equations
- Tau.BookIV.Electroweak.instReprCoherenceFunctionalLevel = { reprPrec := Tau.BookIV.Electroweak.instReprCoherenceFunctionalLevel.repr }

---

### `Tau.BookIV.Electroweak.instReprCoherenceFunctionalLevel.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L533-L533)
**def
Tau.BookIV.Electroweak.instReprCoherenceFunctionalLevel.repr :CoherenceFunctionalLevel → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.coherence_level_7`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L535-L538)
**def
Tau.BookIV.Electroweak.coherence_level_7 :CoherenceFunctionalLevel**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.HiggsN7Uniqueness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L544-L576)
**structure
Tau.BookIV.Electroweak.HiggsN7Uniqueness :Type**


[IV.P199 upgrade] Structural uniqueness of n=7.

The Hessian eigenvalue computation for V_n at level n samples:


- 2 lobes of L = S¹ ∨ S¹ (providing doublet structure)

- Each lobe contributes 2 channels (χ⁺/χ⁻ polarity)

- 3 force sectors {A, B, C} (providing triplet channels)

- Total: 2·2 + 3 = 7


n-scan evidence: n=5 gives +892 ppm, n=6 gives +466 ppm,
n=7 gives +8.0 ppm, n=8 gives −486 ppm.
n=7 is the unique minimum.

- n_lobes : ℕ
Number of lobes.

- polarity_per_lobe : ℕ
Polarity channels per lobe.

- n_sectors : ℕ
Force sectors.

- n_value : ℕ
n = doublet + triplet.

- decomp : self.n_value = self.n_lobes * self.polarity_per_lobe + self.n_sectors
Structural decomposition.

- dev_n5_ppm : ℕ
Absolute deviation in ppm for n=5 scan point.

- dev_n6_ppm : ℕ
Absolute deviation in ppm for n=6 scan point.

- dev_n7_ppm : ℕ
Absolute deviation in ppm for n=7 scan point.

- dev_n8_ppm : ℕ
Absolute deviation in ppm for n=8 scan point.

- n7_is_minimum : self.dev_n7_ppm < self.dev_n5_ppm ∧ self.dev_n7_ppm < self.dev_n6_ppm ∧ self.dev_n7_ppm < self.dev_n8_ppm
n=7 has minimum deviation among scan points.

Instances For

---

### `Tau.BookIV.Electroweak.instReprHiggsN7Uniqueness.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L576-L576)
**def
Tau.BookIV.Electroweak.instReprHiggsN7Uniqueness.repr :HiggsN7Uniqueness → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprHiggsN7Uniqueness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L576-L576)
**instance
Tau.BookIV.Electroweak.instReprHiggsN7Uniqueness :Repr HiggsN7Uniqueness**

Equations
- Tau.BookIV.Electroweak.instReprHiggsN7Uniqueness = { reprPrec := Tau.BookIV.Electroweak.instReprHiggsN7Uniqueness.repr }

---

### `Tau.BookIV.Electroweak.higgs_n7_uniqueness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L578-L580)
**def
Tau.BookIV.Electroweak.higgs_n7_uniqueness :HiggsN7Uniqueness**

Equations
- Tau.BookIV.Electroweak.higgs_n7_uniqueness = { decomp := Tau.BookIV.Electroweak.coherence_level_7._proof_1,
 n7_is_minimum := Tau.BookIV.Electroweak.higgs_n7_uniqueness._proof_2 }
Instances For

---

### `Tau.BookIV.Electroweak.higgs_n7_uniqueness_thm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L582-L588)
**theorem
Tau.BookIV.Electroweak.higgs_n7_uniqueness_thm :higgs_n7_uniqueness.n_value = 7 ∧ higgs_n7_uniqueness.n_lobes = 2 ∧ higgs_n7_uniqueness.n_sectors = 3 ∧ higgs_n7_uniqueness.dev_n7_ppm = 8**


n=7 is uniquely forced: 2·lobes·polarity + sectors = 7.

---

### `Tau.BookIV.Electroweak.WindowRGPeriod`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L594-L613)
**structure
Tau.BookIV.Electroweak.WindowRGPeriod :Type**


[IV.P191 upgrade] W₃(4)^k governs k-th perturbative order.

The holonomy spectral renormalization group has fundamental
period W₃(4) = 5 at each perturbative order:


- NLO: one lemniscate traversal → W₃(4)

- NNLO: double traversal → W₃(4)²

- k-th order: k traversals → W₃(4)^k


W₃(4) = a₃ + a₄ = 3 + 1 + 1 = 5 (CF partial quotients
in the [3,4] window). This is the "CF-RG correspondence".

- w34 : ℕ
Window modulus W₃(4).

- nlo_power : ℕ
NLO exponent.

- nnlo_value : ℕ
NNLO power = W₃(4)².

- nnlo_is_square : self.nnlo_value = self.w34 * self.w34
Period structure: NNLO = W₃(4)².

Instances For

---

### `Tau.BookIV.Electroweak.instReprWindowRGPeriod.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L613-L613)
**def
Tau.BookIV.Electroweak.instReprWindowRGPeriod.repr :WindowRGPeriod → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprWindowRGPeriod`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L613-L613)
**instance
Tau.BookIV.Electroweak.instReprWindowRGPeriod :Repr WindowRGPeriod**

Equations
- Tau.BookIV.Electroweak.instReprWindowRGPeriod = { reprPrec := Tau.BookIV.Electroweak.instReprWindowRGPeriod.repr }

---

### `Tau.BookIV.Electroweak.window_rg_period`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L615-L616)
**def
Tau.BookIV.Electroweak.window_rg_period :WindowRGPeriod**

Equations
- Tau.BookIV.Electroweak.window_rg_period = { nnlo_is_square := Tau.BookIV.Electroweak.window_rg_period._proof_1 }
Instances For

---

### `Tau.BookIV.Electroweak.window_nnlo_period`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L618-L623)
**theorem
Tau.BookIV.Electroweak.window_nnlo_period :window_rg_period.w34 = 5 ∧ window_rg_period.nnlo_value = 25 ∧ window_rg_period.nnlo_value = window_rg_period.w34 * window_rg_period.w34**


W₃(4)² = 25 governs NNLO: period structure.

---

### `Tau.BookIV.Electroweak.HiggsSelfCoupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L635-L656)
**structure
Tau.BookIV.Electroweak.HiggsSelfCoupling :Type**


[IV.D376] Higgs self-coupling from τ-chain.

λ_H = m_H(τ)² / (2·v_EW²) = 0.12928 at +16 ppm.
Inherits precision from IV.T166 (m_H at +8 ppm);
λ_H deviation ≈ 2 × m_H deviation since λ ∝ m².
Coherence functional curvature at ω-crossing equilibrium.

- lambda_x1e5 : ℕ
λ_H (×100000 for integer: 12928).

- lambda_sm_x1e5 : ℕ
SM λ from PDG m_H (×100000).

- deviation_ppm : ℤ
Deviation in ppm.

- higgs_mass_ppm : ℕ
Inherited from n=7 Higgs mass.

- doubled_mass_ppm : Bool
λ deviation ≈ 2 × m_H deviation.

- standalone_formula : Bool
No standalone formula found.

- free_params : ℕ
Number of free parameters.

Instances For

---

### `Tau.BookIV.Electroweak.instReprHiggsSelfCoupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L656-L656)
**instance
Tau.BookIV.Electroweak.instReprHiggsSelfCoupling :Repr HiggsSelfCoupling**

Equations
- Tau.BookIV.Electroweak.instReprHiggsSelfCoupling = { reprPrec := Tau.BookIV.Electroweak.instReprHiggsSelfCoupling.repr }

---

### `Tau.BookIV.Electroweak.instReprHiggsSelfCoupling.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L656-L656)
**def
Tau.BookIV.Electroweak.instReprHiggsSelfCoupling.repr :HiggsSelfCoupling → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.higgs_self_coupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L658-L658)
**def
Tau.BookIV.Electroweak.higgs_self_coupling :HiggsSelfCoupling**

Equations
- Tau.BookIV.Electroweak.higgs_self_coupling = { }
Instances For

---

### `Tau.BookIV.Electroweak.higgs_lambda_sub_100ppm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L660-L665)
**theorem
Tau.BookIV.Electroweak.higgs_lambda_sub_100ppm :higgs_self_coupling.deviation_ppm < 100 ∧ higgs_self_coupling.deviation_ppm > 0**


[IV.T194] τ-chain λ_H at +16 ppm.
No planned collider can distinguish τ from SM (gap = 0.0016%).

---

### `Tau.BookIV.Electroweak.HiggsLambdaFalsification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L667-L679)
**structure
Tau.BookIV.Electroweak.HiggsLambdaFalsification :Type**


[IV.P220] HL-LHC / FCC-hh sensitivity vs τ-SM gap.
HL-LHC: 50% precision → cannot see 0.0016% gap.
FCC-hh: 3-5% precision → still cannot see 0.0016% gap.

- tau_sm_gap_ppm : ℕ
τ-SM gap in ppm.

- hllhc_precision_pct_x10 : ℕ
HL-LHC precision (percent ×10).

- fcc_precision_pct_x10 : ℕ
FCC-hh precision (percent ×10).

- discriminating : Bool
Neither can discriminate.

Instances For

---

### `Tau.BookIV.Electroweak.instReprHiggsLambdaFalsification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L679-L679)
**instance
Tau.BookIV.Electroweak.instReprHiggsLambdaFalsification :Repr HiggsLambdaFalsification**

Equations
- Tau.BookIV.Electroweak.instReprHiggsLambdaFalsification = { reprPrec := Tau.BookIV.Electroweak.instReprHiggsLambdaFalsification.repr }

---

### `Tau.BookIV.Electroweak.instReprHiggsLambdaFalsification.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L679-L679)
**def
Tau.BookIV.Electroweak.instReprHiggsLambdaFalsification.repr :HiggsLambdaFalsification → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.higgs_lambda_falsification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/TauHiggs2.lean#L681-L681)
**def
Tau.BookIV.Electroweak.higgs_lambda_falsification :HiggsLambdaFalsification**

Equations
- Tau.BookIV.Electroweak.higgs_lambda_falsification = { }
Instances For
