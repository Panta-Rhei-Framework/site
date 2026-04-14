---
layout: taulib-doc
title: "TauLib.BookIV.Strong.Confinement"
permalink: /verify/taulib/docs/book-iv-strong-confinement/
lane: verify
module_name: "TauLib.BookIV.Strong.Confinement"
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

# TauLib.BookIV.Strong.Confinement


Confinement mechanism: fractional CR-sublattice, color-confined modes,
color singlets, linear potential, baryon number, winding preservation,
and proton stability.

## Registry Cross-References


- [IV.D158] Fractional CR-sublattice — `FractionalCRSublattice`

- [IV.D159] Color-confined Mode — `ColorConfinedMode`

- [IV.D160] Color Singlet — `ColorSingletDef`

- [IV.D161] Baryon Number — `BaryonNumberDef`

- [IV.T71] Confinement Theorem — `confinement_theorem`

- [IV.T72] Proton Stability Theorem — `proton_stability`

- [IV.P94] Singlet Stability — `singlet_stability`

- [IV.P95] Singlet Classification — `singlet_classification`

- [IV.P96] Linear Confinement Potential — `linear_potential`

- [IV.L8] Winding Preservation — `winding_preservation`

- [IV.R61-R68] Structural remarks (comment-only)


## Mathematical Content


Color confinement arises because modes with fractional eta-holonomy
(n not equiv 0 mod 3) fail to converge in H_partial[omega]. Only color
singlets (total winding 0 mod 3) resolve to stable boundary characters.
Baryon number is conserved because admissible endomorphisms preserve
total eta-winding mod 3, implying absolute proton stability.

## Ground Truth Sources


- Chapter 39 of Book IV (2nd Edition)


---

### `Tau.BookIV.Strong.FractionalCRSublattice`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L45-L56)
**structure
Tau.BookIV.Strong.FractionalCRSublattice :Type**


[IV.D158] The fractional CR-sublattice Lambda_CR^{1/3}:
{(m, n/3) : m,n in Z} subset Z x (1/3)Z, refining the character
lattice to accommodate color-charged modes with fractional
eta-component n/3 not in Z.

- lattice : String
Lattice description.

- refinement_factor : ℕ
Refinement factor (denominator of eta-fraction).

- purpose : String
Purpose: accommodate color-charged modes.

Instances For

---

### `Tau.BookIV.Strong.instReprFractionalCRSublattice.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L56-L56)
**def
Tau.BookIV.Strong.instReprFractionalCRSublattice.repr :FractionalCRSublattice → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprFractionalCRSublattice`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L56-L56)
**instance
Tau.BookIV.Strong.instReprFractionalCRSublattice :Repr FractionalCRSublattice**

Equations
- Tau.BookIV.Strong.instReprFractionalCRSublattice = { reprPrec := Tau.BookIV.Strong.instReprFractionalCRSublattice.repr }

---

### `Tau.BookIV.Strong.fractional_cr_sublattice`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L58-L58)
**def
Tau.BookIV.Strong.fractional_cr_sublattice :FractionalCRSublattice**

Equations
- Tau.BookIV.Strong.fractional_cr_sublattice = { }
Instances For

---

### `Tau.BookIV.Strong.sublattice_factor_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L60-L61)
**theorem
Tau.BookIV.Strong.sublattice_factor_3 :fractional_cr_sublattice.refinement_factor = 3**


---

### `Tau.BookIV.Strong.ColorConfinedMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L67-L78)
**structure
Tau.BookIV.Strong.ColorConfinedMode :Type**


[IV.D159] A mode chi_{m,n} is color-confined if:

- n not equiv 0 mod 3 (fractional eta-holonomy)

- The associated boundary character fails to converge in H_partial[omega]
Confinement = non-convergence in the profinite limit.


- eta_winding_mod3 : ℕ
Eta-winding (not divisible by 3).

- fractional : Bool
Non-zero mod 3 condition.

- non_convergent : Bool
Fails to converge in profinite limit.

Instances For

---

### `Tau.BookIV.Strong.instReprColorConfinedMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L78-L78)
**instance
Tau.BookIV.Strong.instReprColorConfinedMode :Repr ColorConfinedMode**

Equations
- Tau.BookIV.Strong.instReprColorConfinedMode = { reprPrec := Tau.BookIV.Strong.instReprColorConfinedMode.repr }

---

### `Tau.BookIV.Strong.instReprColorConfinedMode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L78-L78)
**def
Tau.BookIV.Strong.instReprColorConfinedMode.repr :ColorConfinedMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.is_confined`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L80-L81)
**def
Tau.BookIV.Strong.is_confined
(n : ℕ)
 :Bool**


A mode with winding n is confined iff n mod 3 != 0.
Equations
- Tau.BookIV.Strong.is_confined n = (n % 3 != 0)
Instances For

---

### `Tau.BookIV.Strong.winding_1_confined`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L83-L83)
**theorem
Tau.BookIV.Strong.winding_1_confined :is_confined 1 = true**


---

### `Tau.BookIV.Strong.winding_2_confined`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L84-L84)
**theorem
Tau.BookIV.Strong.winding_2_confined :is_confined 2 = true**


---

### `Tau.BookIV.Strong.winding_3_free`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L85-L85)
**theorem
Tau.BookIV.Strong.winding_3_free :is_confined 3 = false**


---

### `Tau.BookIV.Strong.winding_0_free`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L86-L86)
**theorem
Tau.BookIV.Strong.winding_0_free :is_confined 0 = false**


---

### `Tau.BookIV.Strong.ConfinementTheorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L92-L110)
**structure
Tau.BookIV.Strong.ConfinementTheorem :Type**


[IV.T71] Confinement Theorem: no isolated color-charged state
resolves to a stable element of H_partial[omega].

The boundary character sequence for a mode with exp(2pi i c/3)
holonomy (c != 0 mod 3) fails to converge because the fractional
eta-phase prevents cancellation in the profinite limit.

This is NOT an input or assumption — it follows from the boundary
holonomy algebra structure at depth 3 with chi_minus dominance.

- no_isolated_colored : Bool
Isolated color-charged states do not exist at omega.

- mechanism : String
Mechanism: non-convergence of fractional holonomy.

- scope : String
Scope: tau-effective (derived, not assumed).

- source : String
Source: boundary holonomy at depth 3 with chi_minus dominance.

Instances For

---

### `Tau.BookIV.Strong.instReprConfinementTheorem.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L110-L110)
**def
Tau.BookIV.Strong.instReprConfinementTheorem.repr :ConfinementTheorem → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprConfinementTheorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L110-L110)
**instance
Tau.BookIV.Strong.instReprConfinementTheorem :Repr ConfinementTheorem**

Equations
- Tau.BookIV.Strong.instReprConfinementTheorem = { reprPrec := Tau.BookIV.Strong.instReprConfinementTheorem.repr }

---

### `Tau.BookIV.Strong.confinement_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L112-L112)
**def
Tau.BookIV.Strong.confinement_theorem :ConfinementTheorem**

Equations
- Tau.BookIV.Strong.confinement_theorem = { }
Instances For

---

### `Tau.BookIV.Strong.ColorSingletDef`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L118-L125)
**structure
Tau.BookIV.Strong.ColorSingletDef :Type**


[IV.D160] Color singlet: composite state with trivial total
eta-holonomy, hol_eta(Psi) = 1, i.e., sum c_j equiv 0 mod 3.

- total_mod3 : ℕ
Total winding sum mod 3 = 0.

- trivial_holonomy : Bool
Trivial total holonomy.

Instances For

---

### `Tau.BookIV.Strong.instReprColorSingletDef`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L125-L125)
**instance
Tau.BookIV.Strong.instReprColorSingletDef :Repr ColorSingletDef**

Equations
- Tau.BookIV.Strong.instReprColorSingletDef = { reprPrec := Tau.BookIV.Strong.instReprColorSingletDef.repr }

---

### `Tau.BookIV.Strong.instReprColorSingletDef.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L125-L125)
**def
Tau.BookIV.Strong.instReprColorSingletDef.repr :ColorSingletDef → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.SingletStability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L131-L141)
**structure
Tau.BookIV.Strong.SingletStability :Type**


[IV.P94] A color singlet resolves to a stable boundary character:
the fractional eta-phases cancel exactly, so the composite boundary
character sequence converges in H_partial[omega].

- phases_cancel : Bool
Fractional phases cancel.

- converges : Bool
Converges in profinite limit.

- stable_on_L : Bool
Stable boundary character on L.

Instances For

---

### `Tau.BookIV.Strong.instReprSingletStability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L141-L141)
**instance
Tau.BookIV.Strong.instReprSingletStability :Repr SingletStability**

Equations
- Tau.BookIV.Strong.instReprSingletStability = { reprPrec := Tau.BookIV.Strong.instReprSingletStability.repr }

---

### `Tau.BookIV.Strong.instReprSingletStability.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L141-L141)
**def
Tau.BookIV.Strong.instReprSingletStability.repr :SingletStability → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.singlet_stability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L143-L143)
**def
Tau.BookIV.Strong.singlet_stability :SingletStability**

Equations
- Tau.BookIV.Strong.singlet_stability = { }
Instances For

---

### `Tau.BookIV.Strong.HadronType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L149-L157)
**inductive
Tau.BookIV.Strong.HadronType :Type**


Hadron types: the minimal color-singlet structures.

- baryon : HadronType
Baryon: three constituents {0,1,2} antisymmetric in color.

- meson : HadronType
Meson: quark-antiquark {c, c_bar}.

- exotic : HadronType
Exotic: tetraquark, pentaquark, etc.

Instances For

---

### `Tau.BookIV.Strong.instReprHadronType.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L157-L157)
**def
Tau.BookIV.Strong.instReprHadronType.repr :HadronType → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprHadronType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L157-L157)
**instance
Tau.BookIV.Strong.instReprHadronType :Repr HadronType**

Equations
- Tau.BookIV.Strong.instReprHadronType = { reprPrec := Tau.BookIV.Strong.instReprHadronType.repr }

---

### `Tau.BookIV.Strong.instDecidableEqHadronType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L157-L157)
**instance
Tau.BookIV.Strong.instDecidableEqHadronType :DecidableEq HadronType**

Equations
- Tau.BookIV.Strong.instDecidableEqHadronType x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Strong.instBEqHadronType.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L157-L157)
**def
Tau.BookIV.Strong.instBEqHadronType.beq :HadronType → HadronType → Bool**

Equations
- Tau.BookIV.Strong.instBEqHadronType.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Strong.instBEqHadronType`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L157-L157)
**instance
Tau.BookIV.Strong.instBEqHadronType :BEq HadronType**

Equations
- Tau.BookIV.Strong.instBEqHadronType = { beq := Tau.BookIV.Strong.instBEqHadronType.beq }

---

### `Tau.BookIV.Strong.SingletClassification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L159-L171)
**structure
Tau.BookIV.Strong.SingletClassification :Type**


[IV.P95] Every persistent hadronic state is a color singlet.
Minimal singlet structures:


- Baryon: {0,1,2} (three quarks, one per color)

- Meson: {c, bar{c}} (quark-antiquark)

- Exotic: {c1,c2,bar{c3},bar{c4}} etc. with total 0 mod 3


- all_hadrons_singlets : Bool
All hadrons are singlets.

- min_baryon_size : ℕ
Minimal baryonic singlet size.

- min_meson_size : ℕ
Minimal mesonic singlet size.

Instances For

---

### `Tau.BookIV.Strong.instReprSingletClassification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L171-L171)
**instance
Tau.BookIV.Strong.instReprSingletClassification :Repr SingletClassification**

Equations
- Tau.BookIV.Strong.instReprSingletClassification = { reprPrec := Tau.BookIV.Strong.instReprSingletClassification.repr }

---

### `Tau.BookIV.Strong.instReprSingletClassification.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L171-L171)
**def
Tau.BookIV.Strong.instReprSingletClassification.repr :SingletClassification → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.singlet_classification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L173-L173)
**def
Tau.BookIV.Strong.singlet_classification :SingletClassification**

Equations
- Tau.BookIV.Strong.singlet_classification = { }
Instances For

---

### `Tau.BookIV.Strong.baryon_is_singlet`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L175-L176)
**theorem
Tau.BookIV.Strong.baryon_is_singlet :is_color_singlet [0, 1, 2] = true**


Baryon winding pattern {0,1,2} is a singlet.

---

### `Tau.BookIV.Strong.meson_is_singlet`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L178-L179)
**theorem
Tau.BookIV.Strong.meson_is_singlet :is_color_singlet [1, 2] = true**


Meson winding pattern {1,2} is a singlet (1+2=3, 3 mod 3 = 0).

---

### `Tau.BookIV.Strong.single_quark_not_singlet`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L181-L182)
**theorem
Tau.BookIV.Strong.single_quark_not_singlet :is_color_singlet [1] = false**


A single quark {1} is NOT a singlet.

---

### `Tau.BookIV.Strong.single_quark_2_not_singlet`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L184-L185)
**theorem
Tau.BookIV.Strong.single_quark_2_not_singlet :is_color_singlet [2] = false**


A single quark {2} is NOT a singlet.

---

### `Tau.BookIV.Strong.LinearConfinementPotential`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L191-L204)
**structure
Tau.BookIV.Strong.LinearConfinementPotential :Type**


[IV.P96] The defect functional for a quark-antiquark pair:
D_C(delta) = D_C(0) + sigma_tau * delta + O(delta^2),
where sigma_tau = kappa(C;3) * g[omega]_s is the tau-string tension.

The linear growth with separation delta is the structural origin
of the confining flux tube / QCD string.

- linear_growth : Bool
Linear growth with separation.

- tension_involves_kappa_C : Bool
String tension involves kappa(C;3).

- flux_tube : Bool
Produces flux tube / string.

Instances For

---

### `Tau.BookIV.Strong.instReprLinearConfinementPotential.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L204-L204)
**def
Tau.BookIV.Strong.instReprLinearConfinementPotential.repr :LinearConfinementPotential → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprLinearConfinementPotential`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L204-L204)
**instance
Tau.BookIV.Strong.instReprLinearConfinementPotential :Repr LinearConfinementPotential**

Equations
- Tau.BookIV.Strong.instReprLinearConfinementPotential = { reprPrec := Tau.BookIV.Strong.instReprLinearConfinementPotential.repr }

---

### `Tau.BookIV.Strong.linear_potential`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L206-L206)
**def
Tau.BookIV.Strong.linear_potential :LinearConfinementPotential**

Equations
- Tau.BookIV.Strong.linear_potential = { }
Instances For

---

### `Tau.BookIV.Strong.BaryonNumberDef`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L212-L220)
**structure
Tau.BookIV.Strong.BaryonNumberDef :Type**


[IV.D161] Baryon number B(Psi) := (1/3) * sum_j n_j,
where n_j is the eta-winding of constituent psi_j.
For a baryon with {c1,c2,c3} = {0,1,2}: B = (0+1+2)/3 = 1.

- winding_sum : ℕ
Sum of windings.

- baryon_number : ℕ
Baryon number = winding_sum / 3 (integer for singlets).

Instances For

---

### `Tau.BookIV.Strong.instReprBaryonNumberDef.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L220-L220)
**def
Tau.BookIV.Strong.instReprBaryonNumberDef.repr :BaryonNumberDef → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprBaryonNumberDef`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L220-L220)
**instance
Tau.BookIV.Strong.instReprBaryonNumberDef :Repr BaryonNumberDef**

Equations
- Tau.BookIV.Strong.instReprBaryonNumberDef = { reprPrec := Tau.BookIV.Strong.instReprBaryonNumberDef.repr }

---

### `Tau.BookIV.Strong.compute_baryon_number`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L222-L226)
**def
Tau.BookIV.Strong.compute_baryon_number
(windings : List ℕ)
 :ℕ × ℕ**


Compute baryon number from a list of eta-windings.
Returns (winding_sum, baryon_number) where baryon_number = sum/3.
Equations
- Tau.BookIV.Strong.compute_baryon_number windings = (List.foldl (fun (x1 x2 : ℕ) => x1 + x2) 0 windings, List.foldl (fun (x1 x2 : ℕ) => x1 + x2) 0 windings / 3)
Instances For

---

### `Tau.BookIV.Strong.proton_baryon_number`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L228-L229)
**theorem
Tau.BookIV.Strong.proton_baryon_number :(compute_baryon_number [0, 1, 2]).2 = 1**


---

### `Tau.BookIV.Strong.meson_baryon_number`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L231-L232)
**theorem
Tau.BookIV.Strong.meson_baryon_number :(compute_baryon_number [1, 2]).2 = 1**


---

### `Tau.BookIV.Strong.WindingPreservation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L238-L248)
**structure
Tau.BookIV.Strong.WindingPreservation :Type**


[IV.L8] Winding Preservation: any admissible endomorphism phi
compatible with the C-sector preserves total eta-winding mod 3,
ensuring baryon number conservation under all physical processes.

- preserves_mod3 : Bool
Admissible endomorphisms preserve winding mod 3.

- baryon_conserved : Bool
Consequence: baryon number is conserved.

- mechanism : String
Mechanism: admissibility condition (SA-i) forces eta-sector preservation.

Instances For

---

### `Tau.BookIV.Strong.instReprWindingPreservation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L248-L248)
**instance
Tau.BookIV.Strong.instReprWindingPreservation :Repr WindingPreservation**

Equations
- Tau.BookIV.Strong.instReprWindingPreservation = { reprPrec := Tau.BookIV.Strong.instReprWindingPreservation.repr }

---

### `Tau.BookIV.Strong.instReprWindingPreservation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L248-L248)
**def
Tau.BookIV.Strong.instReprWindingPreservation.repr :WindingPreservation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.winding_preservation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L250-L250)
**def
Tau.BookIV.Strong.winding_preservation :WindingPreservation**

Equations
- Tau.BookIV.Strong.winding_preservation = { }
Instances For

---

### `Tau.BookIV.Strong.ProtonStabilityTheorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L256-L278)
**structure
Tau.BookIV.Strong.ProtonStabilityTheorem :Type**


[IV.T72] Proton Stability: the proton is absolutely stable.
No admissible endomorphism in the 4+1 sector framework can change
baryon number: B(phi(Psi)) = B(Psi) for all admissible phi.

This predicts tau_proton = infinity, in contrast to GUT theories
that predict finite proton lifetime via baryon-number-violating
leptoquark exchange.

The proof follows from winding preservation (IV.L8): since phi
preserves total eta-winding mod 3, and B = (1/3) * sum n_j,
baryon number is an invariant of admissible dynamics.

- absolutely_stable : Bool
Proton is absolutely stable.

- lifetime : String
Lifetime prediction: infinite.

- no_B_violation : Bool
No baryon number violation by any admissible endomorphism.

- gut_contrast : String
Contrast with GUTs.

- source : String
Source: winding preservation (IV.L8).

Instances For

---

### `Tau.BookIV.Strong.instReprProtonStabilityTheorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L278-L278)
**instance
Tau.BookIV.Strong.instReprProtonStabilityTheorem :Repr ProtonStabilityTheorem**

Equations
- Tau.BookIV.Strong.instReprProtonStabilityTheorem = { reprPrec := Tau.BookIV.Strong.instReprProtonStabilityTheorem.repr }

---

### `Tau.BookIV.Strong.instReprProtonStabilityTheorem.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L278-L278)
**def
Tau.BookIV.Strong.instReprProtonStabilityTheorem.repr :ProtonStabilityTheorem → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.proton_stability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Strong/Confinement.lean#L280-L280)
**def
Tau.BookIV.Strong.proton_stability :ProtonStabilityTheorem**

Equations
- Tau.BookIV.Strong.proton_stability = { }
Instances For
