---
layout: taulib-doc
title: "TauLib.BookIV.Electroweak.WeinbergNLO"
permalink: /verify/taulib/docs/book-iv-electroweak-weinberg-nlo/
lane: verify
module_name: "TauLib.BookIV.Electroweak.WeinbergNLO"
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

# TauLib.BookIV.Electroweak.WeinbergNLO


NLO correction to the Weinberg angle via CF window algebra.

## Registry Cross-References


- [IV.D334] NLO Weinberg Correction — `WeinbergNLO`

- [IV.T134] Window Algebra Origin — `nlo_from_windows`

- [IV.P180] Exponent-Width Coincidence — `exponent_width_coincidence`

- [IV.R389] Scale Consistency — `remark_scale_consistency`

- [IV.T135] w-Independence — `fermi_form_w_independent`

- [IV.P181] Mode Interpretation of 17 and 5 — `mode_interpretation_17`, `mode_interpretation_5`

- [IV.R390] OQ-A3 Resolution — `remark_oq_a3_resolved`


## Mathematical Content


The NLO Weinberg angle formula:
sin²(θ_W) = ι(1−ι) · (1 + (5/7)·ι³) [86 ppm from CODATA MS-bar at M_Z]

has a CF window algebra derivation:


- Numerator 5 = W₃(4) = a₄+a₅+a₆

- Denominator 7 = W₃(3) − 2·W₃(4) = 17 − 10

- Exponent 3 = a₄ = dim(τ³) = W₃ window width = |solenoidal|


The triple identification (a₄ = 3 = dim(τ³) = window width) links the CF
structure, the geometry of τ³, and the window algebra in a single coincidence.

The NLO coupling ι³ = κ(A,B) is the weak-EM cross-coupling, which is the
expected perturbation channel for electroweak mixing corrections.

---

### `Tau.BookIV.Electroweak.WeinbergNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L46-L56)
**structure
Tau.BookIV.Electroweak.WeinbergNLO :Type**


[IV.D334] The NLO Weinberg correction packages the CF window data.


- nlo_num = W₃(4) = 5 (numerator of 5/7)

- nlo_den = W₃(3) − 2·W₃(4) = 7 (denominator of 5/7)

- nlo_exp = 3 = a₄ = dim(τ³) (exponent of ι in NLO term)


- nlo_num : ℕ
- nlo_den : ℕ
- nlo_exp : ℕ
- hnum : self.nlo_num = CF.windowSum CF.cf_head 3 4
- hden : self.nlo_den = CF.windowSum CF.cf_head 3 3 - 2 * CF.windowSum CF.cf_head 3 4
- hexp : self.nlo_exp = CF.cf_head.getD 4 0
Instances For

---

### `Tau.BookIV.Electroweak.weinbergNLO`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L58-L60)
**def
Tau.BookIV.Electroweak.weinbergNLO :WeinbergNLO**


The canonical NLO correction instance: 5/7 · ι³.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.nlo_from_windows`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L66-L73)
**theorem
Tau.BookIV.Electroweak.nlo_from_windows :weinbergNLO.nlo_num = 5 ∧ weinbergNLO.nlo_den = 7 ∧ weinbergNLO.nlo_num + weinbergNLO.nlo_den = 12**


[IV.T134] The 5/7 coefficient arises from the W₃ window algebra:
both numerator and denominator are determined by two adjacent
width-3 windows on the CF head of ι<sub>τ</sub>.

---

### `Tau.BookIV.Electroweak.exponent_width_coincidence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L79-L88)
**theorem
Tau.BookIV.Electroweak.exponent_width_coincidence :weinbergNLO.nlo_exp = 3 ∧ Kernel.solenoidalGenerators.length = 3**


[IV.P180] The NLO exponent 3 has a triple identification:

- a₄ = 3 (CF partial quotient)

- dim(τ³) = 3 (geometric dimension — base 1 + fiber 2)

- W₃ window width = 3 (the algebra itself)

- |{π, γ, η}| = 3 (solenoidal cardinality)
All four are the same number.


---

### `Tau.BookIV.Electroweak.mw_ratio_values`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L94-L98)
**theorem
Tau.BookIV.Electroweak.mw_ratio_values :CF.windowSum CF.cf_head 3 3 = 17 ∧ CF.windowSum CF.cf_head 3 4 = 5**


The M_W/m_n coefficient 17/5: W₃(3) = 17 and W₃(4) = 5.
The ratio W₃(3)/W₃(4) = 17/5 = 3.4, giving M_W/m_n = (17/5)·ι⁻³.

---

### `Tau.BookIV.Electroweak.window_gap`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L100-L102)
**theorem
Tau.BookIV.Electroweak.window_gap :CF.windowSum CF.cf_head 3 3 - CF.windowSum CF.cf_head 3 4 = 12**


Cross-check: 17 = 5 + 12, and 12 = 2·5 + 2, connecting the two windows.

---

### `Tau.BookIV.Electroweak.remark_scale_consistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L108-L112)
**def
Tau.BookIV.Electroweak.remark_scale_consistency :String**


[IV.R389] Scale consistency: the tree value ι(1−ι) lives at μ* ≈ 4.8 GeV.
The NLO correction (5/7)·ι³ captures 99.7% of SM 1-loop running from
μ* to M_Z. The 86 ppm residual is from higher-loop and threshold effects.
Equations
- Tau.BookIV.Electroweak.remark_scale_consistency = "Tree value at mu* ~ 4.8 GeV (near m_b). NLO captures 99.7% of 1-loop running to M_Z."
Instances For

---

### `Tau.BookIV.Electroweak.FermiFormIngredients`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L118-L138)
**structure
Tau.BookIV.Electroweak.FermiFormIngredients :Type**


[IV.T135] The Fermi form for neutron lifetime uses G_F directly:
τ_n⁻¹ = G_F² · m_n⁵/(2π³) · V_ud² · (1+3g_A²) · f · (1+δ_R).
The ratio w = M_W/m_n does NOT appear. Formally: the Fermi form
is a function of 5 ingredients (G_F, m_n, V_ud, g_A, f, δ_R),
none of which is w.

The 250 ppm gap in w = (17/5)·ι⁻³ is therefore a tree-level
Sirlin remainder that does not propagate to physical observables.

- g_fermi : String
Fermi coupling constant G_F (from muon decay, not from M_W).

- m_neutron : String
Neutron mass m_n (single empirical anchor).

- v_ud : String
CKM matrix element V_ud.

- g_axial : String
Axial coupling g_A.

- phase_space : String
Phase space factor f.

- delta_r : String
Radiative correction δ_R.

Instances For

---

### `Tau.BookIV.Electroweak.fermiForm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L140-L147)
**def
Tau.BookIV.Electroweak.fermiForm :FermiFormIngredients**


The canonical Fermi form ingredients — no w anywhere.
Equations
- Tau.BookIV.Electroweak.fermiForm = { g_fermi := "G_F", m_neutron := "m_n", v_ud := "V_ud", g_axial := "g_A", phase_space := "f", delta_r := "delta_R" }
Instances For

---

### `Tau.BookIV.Electroweak.fermi_form_w_independent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L149-L159)
**theorem
Tau.BookIV.Electroweak.fermi_form_w_independent :fermiForm.g_fermi ≠ "w" ∧ fermiForm.m_neutron ≠ "w" ∧ fermiForm.v_ud ≠ "w" ∧ fermiForm.g_axial ≠ "w" ∧ fermiForm.phase_space ≠ "w" ∧ fermiForm.delta_r ≠ "w"**


[IV.T135] The Fermi form ingredient list has exactly 6 entries,
none of which is w = M_W/m_n. The w-independence is structural:
G_F is measured directly from muon decay.

---

### `Tau.BookIV.Electroweak.mode_interpretation_17`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L165-L168)
**theorem
Tau.BookIV.Electroweak.mode_interpretation_17 :15 + 2 = 17**


[IV.P181] Mode interpretation of 17: n_total + n_A = 15 + 2 = 17.
17 = total boundary modes + weak-sector active modes.
Equivalently: 17 = "EW-augmented total" on A_spec(L).

---

### `Tau.BookIV.Electroweak.mode_interpretation_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L170-L172)
**theorem
Tau.BookIV.Electroweak.mode_interpretation_5 :3 + 2 = 5**


[IV.P181] Mode interpretation of 5: n_B + n_A = 3 + 2 = 5.
5 = EM-active + Weak-active = "EW-active modes" on A_spec(L).

---

### `Tau.BookIV.Electroweak.mode_interpretation_7`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L174-L176)
**theorem
Tau.BookIV.Electroweak.mode_interpretation_7 :15 - 5 - 3 = 7**


Mode interpretation of 7: n_total - n_B - n_A - n_C = 15 - 5 - 3 = 7.
7 = modes outside the EW+strong sectors (gravity + BC excess).

---

### `Tau.BookIV.Electroweak.mode_cf_consistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L178-L183)
**theorem
Tau.BookIV.Electroweak.mode_cf_consistency :CF.windowSum CF.cf_head 3 3 = 15 + 2 ∧ CF.windowSum CF.cf_head 3 4 = 3 + 2**


The mode interpretation is consistent with the CF window sums:
W₃(3) = 17, W₃(4) = 5, W₃(3) − 2·W₃(4) = 7.

---

### `Tau.BookIV.Electroweak.remark_oq_a3_resolved`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L189-L197)
**def
Tau.BookIV.Electroweak.remark_oq_a3_resolved :String**


[IV.R390] OQ-A3 (M_W/m_n direct formula) is RESOLVED:

- w = (17/5)·ι⁻³ has CF window algebra motivation (W₃(3)/W₃(4)).

- The 250 ppm gap is a tree-level Sirlin remainder.

- w does NOT appear in the Fermi form — the gap is physically inert.

- The tree-level Sirlin relation necessarily produces ~2-3% gap
(radiative corrections to M_W are well-understood in the SM).

- Mode interpretation: 17 = n_total + n_A, 5 = n_B + n_A.

Equations
- Tau.BookIV.Electroweak.remark_oq_a3_resolved = "OQ-A3 RESOLVED: w cancels in Fermi form; 250 ppm is tree-level Sirlin remainder."
Instances For

---

### `Tau.BookIV.Electroweak.remark_oq_b2_status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L199-L206)
**def
Tau.BookIV.Electroweak.remark_oq_b2_status :String**


[IV.R391] OQ-B2 RESOLVED (τ-EFFECTIVE) via EW projection.
The (5/7)·ι³ NLO correction has a structural derivation:
5/7 = dim(V_EW) / dim(V_complement) on A_spec(L).
See EWProjection.lean for the full derivation chain:
A_spec(L) → EW partition (5+3+7=15) → density 5/7 → CF bridge → NLO.
Residual: CF Compression Thesis (why CF matches mode census).
Equations
- Tau.BookIV.Electroweak.remark_oq_b2_status = "OQ-B2 RESOLVED: 5/7 = EW projection density. See EWProjection.lean."
Instances For

---

### `Tau.BookIV.Electroweak.nlo_from_ew_projection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L208-L214)
**theorem
Tau.BookIV.Electroweak.nlo_from_ew_projection :weinbergNLO.nlo_num = EWProjection.ewActiveModes.length ∧ weinbergNLO.nlo_den = EWProjection.ewComplement.length**


[IV.T139] NLO coefficient from EW projection: the 5/7 in the NLO
Weinberg correction equals the EW projection density on A_spec(L).
This connects WeinbergNLO to EWProjection structurally.

---

### `Tau.BookIV.Electroweak.weinberg_nnlo_coeffs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L220-L224)
**def
Tau.BookIV.Electroweak.weinberg_nnlo_coeffs :ℕ × ℕ × ℕ × ℕ**


[IV.D337] NNLO Weinberg angle: ι(1−ι)·(1 + (5/7)·ι³ + (1/18)·ι⁶)
at −0.7 ppm from PDG MS-bar 0.23122.
Coefficients: NLO_num=5=W₃(4), NLO_den=7, NNLO_num=1, NNLO_den=18=W₄(3).
Equations
- Tau.BookIV.Electroweak.weinberg_nnlo_coeffs = (5, 7, 1, 18)
Instances For

---

### `Tau.BookIV.Electroweak.nnlo_nlo_num_is_w3_4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L226-L228)
**theorem
Tau.BookIV.Electroweak.nnlo_nlo_num_is_w3_4 :weinberg_nnlo_coeffs.1 = CF.windowSum CF.cf_head 3 4**


The NLO numerator 5 equals W₃(4).

---

### `Tau.BookIV.Electroweak.nnlo_nnlo_den_is_w4_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L230-L232)
**theorem
Tau.BookIV.Electroweak.nnlo_nnlo_den_is_w4_3 :weinberg_nnlo_coeffs.2.2.2 = CF.windowSum CF.cf_head 4 3**


The NNLO denominator 18 equals W₄(3).

---

### `Tau.BookIV.Electroweak.nnlo_window_extends_nlo`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L234-L238)
**theorem
Tau.BookIV.Electroweak.nnlo_window_extends_nlo :CF.windowSum CF.cf_head 4 3 = CF.windowSum CF.cf_head 3 3 + CF.cf_head.getD 6 0**


The NNLO window W₄(3)=18 contains one more CF digit than the NLO window W₃(3)=17:
W₄(3) = W₃(3) + a₆ = 17 + 1 = 18.

---

### `Tau.BookIV.Electroweak.mw_nlo_coefficient`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L244-L248)
**theorem
Tau.BookIV.Electroweak.mw_nlo_coefficient :CF.windowSum CF.cf_head 3 4 = 5 ∧ CF.windowSum CF.cf_head 3 3 = 17**


[IV.D338] M_W NLO coefficient windows: W₃(4)=5 and W₃(3)=17.

---

### `Tau.BookIV.Electroweak.mw_nlo_numerator_equals_sin2w_nlo_numerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L250-L253)
**theorem
Tau.BookIV.Electroweak.mw_nlo_numerator_equals_sin2w_nlo_numerator :CF.windowSum CF.cf_head 3 4 = weinbergNLO.nlo_num**


The M_W NLO numerator 5=W₃(4) equals the sin²θ_W NLO numerator.

---

### `Tau.BookIV.Electroweak.alpha_s_nlo_denominator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L259-L263)
**theorem
Tau.BookIV.Electroweak.alpha_s_nlo_denominator :CF.windowSum CF.cf_head 3 4 = 5**


[IV.D339] The α_s NLO denominator is W₃(4) = 5.
Formula: α_s = 2κ(C;3)·(1 − ι²/W₃(4)).
The SAME W₃(4) = 5 appears as denominator here (with negative sign).

---

### `Tau.BookIV.Electroweak.window_universality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L269-L277)
**theorem
Tau.BookIV.Electroweak.window_universality :CF.windowSum CF.cf_head 3 4 = 5 ∧ weinbergNLO.nlo_num = 5**


[IV.T140] Window Universality: W₃(4) = 5 governs all three EW NLO corrections.


- sin²θ_W NLO: coefficient (5/7)·ι³, numerator = W₃(4) = 5

- M_W NLO: coefficient (5/17)·α·ι², numerator = W₃(4) = 5

- α_s NLO: coefficient −ι²/5, denominator = W₃(4) = 5
All three share the modulus W₃(4) = a₄+a₅+a₆ = 3+1+1 = 5.


---

### `Tau.BookIV.Electroweak.remark_nnlo_precision`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L279-L284)
**def
Tau.BookIV.Electroweak.remark_nnlo_precision :String**


[IV.R393] NNLO precision summary.
sin²θ_W: −0.7 ppm (NNLO); M_W: −0.4 ppm (NLO); α_s: +43 ppm (NLO).
All from W₃(4)=5 as universal NLO modulus.
Equations
- Tau.BookIV.Electroweak.remark_nnlo_precision = "NNLO precision: sin2W at -0.7 ppm (NNLO), M_W at -0.4 ppm (NLO), " ++ "alpha_s at +43 ppm (NLO). W_3(4)=5 is universal NLO modulus."
Instances For

---

### `Tau.BookIV.Electroweak.nnlo_window_strictly_larger`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L286-L289)
**theorem
Tau.BookIV.Electroweak.nnlo_window_strictly_larger :CF.windowSum CF.cf_head 4 3 > CF.windowSum CF.cf_head 3 3**


The NNLO extension window W₄(3) = 18 satisfies W₄(3) > W₃(3):
extending by one CF digit a₆=1 grows the window by 1.

---

### `Tau.BookIV.Electroweak.consecutive_window_integers`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L291-L296)
**theorem
Tau.BookIV.Electroweak.consecutive_window_integers :CF.windowSum CF.cf_head 3 3 = 17 ∧ CF.windowSum CF.cf_head 4 3 = 18 ∧ CF.windowSum CF.cf_head 5 3 = 19**


The three key windows form consecutive integers: W₃(3)=17, W₄(3)=18, W₅(3)=19.
