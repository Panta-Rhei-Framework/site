---
layout: taulib-doc
title: "TauLib.BookIV.Strong.StrongCoupling"
permalink: /verify/taulib/docs/book-iv-strong-strong-coupling/
lane: verify
module_name: "TauLib.BookIV.Strong.StrongCoupling"
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

# TauLib.BookIV.Strong.StrongCoupling


Running coupling kappa(C;n), the pi-lift construction, strong coupling
constant alpha_s^*, uniqueness, no primitive mixing, ontic coupling,
regime selectors, no ontic running, and asymptotic freedom.

## Registry Cross-References


- [IV.D180] Lift at Stage n — `LiftAtStageN`

- [IV.D181] Lift Limit — `LiftLimit`

- [IV.D182] The Strong Coupling Constant — `StrongCouplingConstant`

- [IV.D183] Support Penalty — `SupportPenalty`

- [IV.D184] Ontic Coupling — `OnticCoupling`

- [IV.D185] Regime Selector — `RegimeSelector`

- [IV.D186] Regime Readout Map — `RegimeReadoutMap`

- [IV.T76] Uniqueness of the Strong Coupling — `uniqueness_strong_coupling`

- [IV.T77] No Ontic Running — `no_ontic_running`

- [IV.P109] No Primitive Mixing — `no_primitive_mixing`

- [IV.P110] The Argmin is the Lift — `argmin_is_lift`

- [IV.P111] QCD as Readout Saturation — `qcd_readout_saturation`

- [IV.P112] Asymptotic Freedom as Spectral Tightening — `asymptotic_freedom_spectral`

- [IV.R84-R91] Structural remarks (comment-only)


## Mathematical Content


The strong coupling constant alpha_s^* := NF(Lift_pi^omega) is the
unique element of Fix(s) obtained by the pi-lift construction. It
equals kappa(C;3) = iota_tau^3/(1-iota_tau) and is independent of all
regime selectors (no ontic running). Different readout functors give
different numerical values at different scales, explaining the apparent
running of alpha_s in QCD without any actual change in the ontic coupling.

## Ground Truth Sources


- Chapter 42 of Book IV (2nd Edition)


---

### `Tau.BookIV.Strong.LiftAtStageN`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L49-L61)
**structure
Tau.BookIV.Strong.LiftAtStageN :Type**


[IV.D180] The pi-lift at stage n: restriction of the canonical
strong lift Lift_{s,n} to pi-supported endomorphisms, selecting
the NF-minimal element. Deep inelastic scattering analogue.

- stage : ℕ
Stage n.

- pi_supported : Bool
Restricted to pi-supported endomorphisms.

- nf_minimal : Bool
NF-minimal among candidates.

- activation_depth : ℕ
Active from depth 3.

Instances For

---

### `Tau.BookIV.Strong.instReprLiftAtStageN`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L61-L61)
**instance
Tau.BookIV.Strong.instReprLiftAtStageN :Repr LiftAtStageN**

Equations
- Tau.BookIV.Strong.instReprLiftAtStageN = { reprPrec := Tau.BookIV.Strong.instReprLiftAtStageN.repr }

---

### `Tau.BookIV.Strong.instReprLiftAtStageN.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L61-L61)
**def
Tau.BookIV.Strong.instReprLiftAtStageN.repr :LiftAtStageN → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.LiftLimit`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L67-L78)
**structure
Tau.BookIV.Strong.LiftLimit :Type**


[IV.D181] Pi-lift omega-limit:
Lift_pi^omega := [(Lift_pi(n))*{n>=3}]*{~omega}
The tail equivalence class in H_partial representing the
profinite strong coupling as a well-defined boundary element.

- construction : String
Construction: tail equivalence class.

- lives_in : String
Lives in H_partial.

- well_defined : Bool
Well-defined by truncation coherence.

Instances For

---

### `Tau.BookIV.Strong.instReprLiftLimit.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L78-L78)
**def
Tau.BookIV.Strong.instReprLiftLimit.repr :LiftLimit → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprLiftLimit`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L78-L78)
**instance
Tau.BookIV.Strong.instReprLiftLimit :Repr LiftLimit**

Equations
- Tau.BookIV.Strong.instReprLiftLimit = { reprPrec := Tau.BookIV.Strong.instReprLiftLimit.repr }

---

### `Tau.BookIV.Strong.lift_limit`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L80-L80)
**def
Tau.BookIV.Strong.lift_limit :LiftLimit**

Equations
- Tau.BookIV.Strong.lift_limit = { }
Instances For

---

### `Tau.BookIV.Strong.StrongCouplingConstant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L86-L103)
**structure
Tau.BookIV.Strong.StrongCouplingConstant :Type**


[IV.D182] The tau-strong coupling constant:
alpha_s^* := NF(Lift_pi^omega) in Fix(s).
Normal-form selector applied to the pi-lift omega-limit.
Determined entirely by iota_tau and the boundary holonomy structure.

Numerical value: kappa(C;3) = iota_tau^3/(1-iota_tau) approx 0.0604.

- construction : String
NF selector applied to lift limit.

- lives_in : String
Lives in Fix(s).

- equals_kappa_C : Bool
Equals kappa(C;3).

- coupling_numer : ℕ
Coupling numerator (same as strong_sector).

- coupling_denom : ℕ
Coupling denominator (same as strong_sector).

Instances For

---

### `Tau.BookIV.Strong.instReprStrongCouplingConstant.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L103-L103)
**def
Tau.BookIV.Strong.instReprStrongCouplingConstant.repr :StrongCouplingConstant → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprStrongCouplingConstant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L103-L103)
**instance
Tau.BookIV.Strong.instReprStrongCouplingConstant :Repr StrongCouplingConstant**

Equations
- Tau.BookIV.Strong.instReprStrongCouplingConstant = { reprPrec := Tau.BookIV.Strong.instReprStrongCouplingConstant.repr }

---

### `Tau.BookIV.Strong.strong_coupling_constant`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L105-L105)
**def
Tau.BookIV.Strong.strong_coupling_constant :StrongCouplingConstant**

Equations
- Tau.BookIV.Strong.strong_coupling_constant = { }
Instances For

---

### `Tau.BookIV.Strong.alpha_s_matches_sector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L107-L111)
**theorem
Tau.BookIV.Strong.alpha_s_matches_sector :strong_coupling_constant.coupling_numer = Sectors.strong_sector.coupling_numer ∧ strong_coupling_constant.coupling_denom = Sectors.strong_sector.coupling_denom**


alpha_s^* matches strong_sector coupling.

---

### `Tau.BookIV.Strong.alpha_s_float`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L113-L116)
**def
Tau.BookIV.Strong.alpha_s_float :Float**


alpha_s^* as Float for display.
Equations
- Tau.BookIV.Strong.alpha_s_float = Float.ofNat Tau.BookIV.Strong.strong_coupling_constant.coupling_numer / Float.ofNat Tau.BookIV.Strong.strong_coupling_constant.coupling_denom
Instances For

---

### `Tau.BookIV.Strong.UniquenessStrongCoupling`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L122-L135)
**structure
Tau.BookIV.Strong.UniquenessStrongCoupling :Type**


[IV.T76] Uniqueness of the strong coupling: any tau-admissible
construction that preserves the strong vacuum, is pi-supported,
and yields a fixed point of HolEnd_tau(s) must equal alpha_s^*.
No alternative coupling is consistent with the tau-axioms.

- unique : Bool
Unique among admissible constructions.

- condition_vacuum : String
Conditions for uniqueness.

- condition_pi : String
- condition_fixed : String
- no_alternatives : Bool
No alternatives.

Instances For

---

### `Tau.BookIV.Strong.instReprUniquenessStrongCoupling.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L135-L135)
**def
Tau.BookIV.Strong.instReprUniquenessStrongCoupling.repr :UniquenessStrongCoupling → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprUniquenessStrongCoupling`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L135-L135)
**instance
Tau.BookIV.Strong.instReprUniquenessStrongCoupling :Repr UniquenessStrongCoupling**

Equations
- Tau.BookIV.Strong.instReprUniquenessStrongCoupling = { reprPrec := Tau.BookIV.Strong.instReprUniquenessStrongCoupling.repr }

---

### `Tau.BookIV.Strong.uniqueness_strong_coupling`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L137-L137)
**def
Tau.BookIV.Strong.uniqueness_strong_coupling :UniquenessStrongCoupling**

Equations
- Tau.BookIV.Strong.uniqueness_strong_coupling = { }
Instances For

---

### `Tau.BookIV.Strong.NoPrimitiveMixing`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L143-L155)
**structure
Tau.BookIV.Strong.NoPrimitiveMixing :Type**


[IV.P109] No primitive mixing: alpha_s^* is distinct from
alpha_em^* and alpha_wk^*. The fixed-point subalgebras
Fix(s), Fix(EM), Fix(wk) intersect only trivially.

- distinct_from_em : Bool
Strong distinct from EM.

- distinct_from_weak : Bool
Strong distinct from weak.

- trivial_intersection : Bool
Intersection is trivial.

- mechanism : String
Mechanism: different generators, different sectors.

Instances For

---

### `Tau.BookIV.Strong.instReprNoPrimitiveMixing`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L155-L155)
**instance
Tau.BookIV.Strong.instReprNoPrimitiveMixing :Repr NoPrimitiveMixing**

Equations
- Tau.BookIV.Strong.instReprNoPrimitiveMixing = { reprPrec := Tau.BookIV.Strong.instReprNoPrimitiveMixing.repr }

---

### `Tau.BookIV.Strong.instReprNoPrimitiveMixing.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L155-L155)
**def
Tau.BookIV.Strong.instReprNoPrimitiveMixing.repr :NoPrimitiveMixing → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.no_primitive_mixing`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L157-L157)
**def
Tau.BookIV.Strong.no_primitive_mixing :NoPrimitiveMixing**

Equations
- Tau.BookIV.Strong.no_primitive_mixing = { }
Instances For

---

### `Tau.BookIV.Strong.SupportPenalty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L163-L175)
**structure
Tau.BookIV.Strong.SupportPenalty :Type**


[IV.D183] Pi-support penalty Pen_pin:
measures how far an endomorphism deviates from pure pi-typed
action at stages beyond n. Penalizes non-pi-typed contributions.

- stage : ℕ
Stage n.

- penalty_range : String
Penalty range: stages n+1 to 2n.

- measures_deviation : Bool
Measures deviation from pi-typed action.

- nonneg : Bool
Non-negative valued.

Instances For

---

### `Tau.BookIV.Strong.instReprSupportPenalty.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L175-L175)
**def
Tau.BookIV.Strong.instReprSupportPenalty.repr :SupportPenalty → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprSupportPenalty`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L175-L175)
**instance
Tau.BookIV.Strong.instReprSupportPenalty :Repr SupportPenalty**

Equations
- Tau.BookIV.Strong.instReprSupportPenalty = { reprPrec := Tau.BookIV.Strong.instReprSupportPenalty.repr }

---

### `Tau.BookIV.Strong.ArgminIsLift`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L177-L184)
**structure
Tau.BookIV.Strong.ArgminIsLift :Type**


[IV.P110] The argmin of combined defect over A_pi[n]
equals the pi-lift Lift_pi(n).

- argmin_equals_lift : Bool
Argmin equals lift.

- canonical_equals_variational : Bool
Canonical construction coincides with variational.

Instances For

---

### `Tau.BookIV.Strong.instReprArgminIsLift.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L184-L184)
**def
Tau.BookIV.Strong.instReprArgminIsLift.repr :ArgminIsLift → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprArgminIsLift`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L184-L184)
**instance
Tau.BookIV.Strong.instReprArgminIsLift :Repr ArgminIsLift**

Equations
- Tau.BookIV.Strong.instReprArgminIsLift = { reprPrec := Tau.BookIV.Strong.instReprArgminIsLift.repr }

---

### `Tau.BookIV.Strong.argmin_is_lift`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L186-L186)
**def
Tau.BookIV.Strong.argmin_is_lift :ArgminIsLift**

Equations
- Tau.BookIV.Strong.argmin_is_lift = { }
Instances For

---

### `Tau.BookIV.Strong.QCDReadoutSaturation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L192-L203)
**structure
Tau.BookIV.Strong.QCDReadoutSaturation :Type**


[IV.P111] Lambda_QCD is the energy at which the readout functor
R_C(mu^2) ceases to be injective on the boundary algebra.
Below this scale, multiple boundary states project to the same
measured value: confinement at the readout level.

- saturation_point : Bool
Lambda_QCD is readout saturation point.

- non_injective_below : Bool
Below saturation: readout non-injective.

- interpretation : String
Interpretation: confinement at readout level.

Instances For

---

### `Tau.BookIV.Strong.instReprQCDReadoutSaturation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L203-L203)
**instance
Tau.BookIV.Strong.instReprQCDReadoutSaturation :Repr QCDReadoutSaturation**

Equations
- Tau.BookIV.Strong.instReprQCDReadoutSaturation = { reprPrec := Tau.BookIV.Strong.instReprQCDReadoutSaturation.repr }

---

### `Tau.BookIV.Strong.instReprQCDReadoutSaturation.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L203-L203)
**def
Tau.BookIV.Strong.instReprQCDReadoutSaturation.repr :QCDReadoutSaturation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.qcd_readout_saturation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L205-L205)
**def
Tau.BookIV.Strong.qcd_readout_saturation :QCDReadoutSaturation**

Equations
- Tau.BookIV.Strong.qcd_readout_saturation = { }
Instances For

---

### `Tau.BookIV.Strong.OnticCoupling`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L211-L226)
**structure
Tau.BookIV.Strong.OnticCoupling :Type**


[IV.D184] An ontic coupling: element of H_partial obtained by
finite-stage minimization, omega-tail stabilization, and
NF normalization. Belongs to Fix(S) for some sector S.
Scale-independent, unique, parameter-free.

- construction : String
Construction: minimize, stabilize, normalize.

- lives_in_fix : Bool
Lives in Fix(S) for some sector S.

- scale_independent : Bool
Scale-independent.

- unique : Bool
Unique.

- parameter_free : Bool
Parameter-free.

Instances For

---

### `Tau.BookIV.Strong.instReprOnticCoupling.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L226-L226)
**def
Tau.BookIV.Strong.instReprOnticCoupling.repr :OnticCoupling → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.instReprOnticCoupling`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L226-L226)
**instance
Tau.BookIV.Strong.instReprOnticCoupling :Repr OnticCoupling**

Equations
- Tau.BookIV.Strong.instReprOnticCoupling = { reprPrec := Tau.BookIV.Strong.instReprOnticCoupling.repr }

---

### `Tau.BookIV.Strong.RegimeSelector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L232-L243)
**structure
Tau.BookIV.Strong.RegimeSelector :Type**


[IV.D185] A regime selector: finite datum specifying truncation
depth, operational chart, sector carrier, and calibration bridge.

- truncation_depth : ℕ
Truncation depth n_0.

- chart : String
Operational chart (coordinate choice).

- carrier : BookIII.Sectors.Sector
Sector carrier.

- calibration : String
Calibration bridge from tau-units to SI.

Instances For

---

### `Tau.BookIV.Strong.instReprRegimeSelector`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L243-L243)
**instance
Tau.BookIV.Strong.instReprRegimeSelector :Repr RegimeSelector**

Equations
- Tau.BookIV.Strong.instReprRegimeSelector = { reprPrec := Tau.BookIV.Strong.instReprRegimeSelector.repr }

---

### `Tau.BookIV.Strong.instReprRegimeSelector.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L243-L243)
**def
Tau.BookIV.Strong.instReprRegimeSelector.repr :RegimeSelector → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.RegimeReadoutMap`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L249-L258)
**structure
Tau.BookIV.Strong.RegimeReadoutMap :Type**


[IV.D186] Read_S[R]: H_partial -> R_R, extracting the measured
value of an ontic coupling in a specific regime.

- source : String
Source: boundary algebra.

- target : String
Target: real numbers in regime metric.

- regime_dependent : Bool
Depends on regime selector.

Instances For

---

### `Tau.BookIV.Strong.instReprRegimeReadoutMap`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L258-L258)
**instance
Tau.BookIV.Strong.instReprRegimeReadoutMap :Repr RegimeReadoutMap**

Equations
- Tau.BookIV.Strong.instReprRegimeReadoutMap = { reprPrec := Tau.BookIV.Strong.instReprRegimeReadoutMap.repr }

---

### `Tau.BookIV.Strong.instReprRegimeReadoutMap.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L258-L258)
**def
Tau.BookIV.Strong.instReprRegimeReadoutMap.repr :RegimeReadoutMap → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.NoOnticRunning`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L264-L281)
**structure
Tau.BookIV.Strong.NoOnticRunning :Type**


[IV.T77] No ontic running in the strong sector:
alpha_s^* = kappa(C;3) is INDEPENDENT of all regime selectors.
It is the same element of H_partial regardless of scale, chart,
or calibration choice.

Different regime readouts CAN give different numerical values
(this is what experimentalists call "running"), but the ontic
coupling itself does not run. Running is a readout phenomenon.

- regime_independent : Bool
Coupling is regime-independent.

- same_element : Bool
Same boundary algebra element at all scales.

- running_is_readout : Bool
Apparent running is readout artifact.

- explanation : String
Experimental "running" = different readout charts.

Instances For

---

### `Tau.BookIV.Strong.instReprNoOnticRunning`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L281-L281)
**instance
Tau.BookIV.Strong.instReprNoOnticRunning :Repr NoOnticRunning**

Equations
- Tau.BookIV.Strong.instReprNoOnticRunning = { reprPrec := Tau.BookIV.Strong.instReprNoOnticRunning.repr }

---

### `Tau.BookIV.Strong.instReprNoOnticRunning.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L281-L281)
**def
Tau.BookIV.Strong.instReprNoOnticRunning.repr :NoOnticRunning → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.no_ontic_running`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L283-L283)
**def
Tau.BookIV.Strong.no_ontic_running :NoOnticRunning**

Equations
- Tau.BookIV.Strong.no_ontic_running = { }
Instances For

---

### `Tau.BookIV.Strong.AsymptoticFreedomSpectral`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L289-L310)
**structure
Tau.BookIV.Strong.AsymptoticFreedomSpectral :Type**


[IV.P112] Asymptotic freedom as spectral tightening:
at high energy (mu >> Lambda_QCD), the C-sector readout
R_C(mu^2) < 1 and decreases with increasing mu.
Chi_minus-dominant character modes become increasingly
tightly concentrated under spectral tightening.

The orthodox beta function coefficient b_0 = (11*N_c - 2*N_f)/(12*pi)
with N_c = 3, N_f = 6 gives b_0 = (33-12)/(12*pi) > 0.

- decreasing_at_high_E : Bool
Readout decreases at high energy.

- mechanism : String
Mechanism: spectral tightening.

- beta_positive : Bool
Beta function coefficient b_0 > 0 (from N_c = 3, N_f = 6).

- num_colors : ℕ
N_c = 3.

- num_flavors : ℕ
N_f = 6.

- beta_numerator : ℕ
11*N_c - 2*N_f = 21 > 0.

Instances For

---

### `Tau.BookIV.Strong.instReprAsymptoticFreedomSpectral`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L310-L310)
**instance
Tau.BookIV.Strong.instReprAsymptoticFreedomSpectral :Repr AsymptoticFreedomSpectral**

Equations
- Tau.BookIV.Strong.instReprAsymptoticFreedomSpectral = { reprPrec := Tau.BookIV.Strong.instReprAsymptoticFreedomSpectral.repr }

---

### `Tau.BookIV.Strong.instReprAsymptoticFreedomSpectral.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L310-L310)
**def
Tau.BookIV.Strong.instReprAsymptoticFreedomSpectral.repr :AsymptoticFreedomSpectral → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Strong.asymptotic_freedom_spectral`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L312-L312)
**def
Tau.BookIV.Strong.asymptotic_freedom_spectral :AsymptoticFreedomSpectral**

Equations
- Tau.BookIV.Strong.asymptotic_freedom_spectral = { }
Instances For

---

### `Tau.BookIV.Strong.asymptotic_freedom_condition`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L314-L318)
**theorem
Tau.BookIV.Strong.asymptotic_freedom_condition :11 * asymptotic_freedom_spectral.num_colors > 2 * asymptotic_freedom_spectral.num_flavors**


11*3 - 2*6 = 21 > 0 (asymptotic freedom condition).

---

### `Tau.BookIV.Strong.beta_numerator_correct`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Strong/StrongCoupling.lean#L320-L325)
**theorem
Tau.BookIV.Strong.beta_numerator_correct :11 * asymptotic_freedom_spectral.num_colors - 2 * asymptotic_freedom_spectral.num_flavors = asymptotic_freedom_spectral.beta_numerator**


The beta numerator matches 11*N_c - 2*N_f.
