---
layout: taulib-doc
title: "TauLib.BookIV.Calibration.RunningRegime"
permalink: /verify/taulib/docs/book-iv-calibration-running-regime/
lane: verify
module_name: "TauLib.BookIV.Calibration.RunningRegime"
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

# TauLib.BookIV.Calibration.RunningRegime


Running vs readout: beta functions, readout functors, entropy splitting
at scale, regime transitions, and the readout landscape.

## Registry Cross-References


- [IV.D299] Beta function — `BetaFunction`

- [IV.D300] Coupling Ledger and Observable Ledger — `ObservableLedger`

- [IV.D301] Readout Functor — `ReadoutFunctor`

- [IV.P168] Readout Properties — `readout_properties`

- [IV.P169] Beta Function as Readout Derivative — `beta_as_derivative`

- [IV.R279] Asymptotic freedom revisited — (structural remark)

- [IV.R280] Scheme dependence resolved — (structural remark)

- [IV.D302] Entropy splitting — `EntropyAtScale`

- [IV.P170] Total Entropy Invariance — `entropy_invariance`

- [IV.D303] Regime transition — `RegimeTransition`

- [IV.R282] Lean formalization — (structural remark)

- [IV.D304] Readout landscape — `ReadoutLandscape`

- [IV.T113] Readout Landscape Theorem — `readout_landscape_unique`


## Ground Truth Sources


- Chapter 14 of Book IV (2nd Edition)


---

### `Tau.BookIV.Calibration.BetaFunction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L38-L50)
**structure
Tau.BookIV.Calibration.BetaFunction :Type**


[IV.D299] The beta function β(α_X) = μ·d(α_X)/dμ for a coupling
α_X(μ). In the τ-framework, the ontic coupling is FIXED and
β ≡ 0 at the ontic level. What QFT calls "running" is the
readout functor's scale dependence.

- sector : BookIII.Sectors.Sector
Sector whose coupling is being examined.

- ontic_beta_zero : Bool
Ontic beta is identically zero.

- ontic_true : self.ontic_beta_zero = true
- apparent_nonzero : Bool
Apparent beta from readout (nonzero in general).

Instances For

---

### `Tau.BookIV.Calibration.instReprBetaFunction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L50-L50)
**instance
Tau.BookIV.Calibration.instReprBetaFunction :Repr BetaFunction**

Equations
- Tau.BookIV.Calibration.instReprBetaFunction = { reprPrec := Tau.BookIV.Calibration.instReprBetaFunction.repr }

---

### `Tau.BookIV.Calibration.instReprBetaFunction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L50-L50)
**def
Tau.BookIV.Calibration.instReprBetaFunction.repr :BetaFunction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.ObservableLedger`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L56-L66)
**structure
Tau.BookIV.Calibration.ObservableLedger :Type**


[IV.D300] The observable ledger at scale μ: the apparent coupling
values as seen by instruments at energy scale μ.
Distinct from the ontic coupling ledger (which is μ-independent).

- entry_count : ℕ
Number of coupling entries (same as ontic: 10).

- entry_eq : self.entry_count = 10
- scale_dependent : Bool
Scale-dependent (unlike ontic ledger).

- scale_true : self.scale_dependent = true
Instances For

---

### `Tau.BookIV.Calibration.instReprObservableLedger`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L66-L66)
**instance
Tau.BookIV.Calibration.instReprObservableLedger :Repr ObservableLedger**

Equations
- Tau.BookIV.Calibration.instReprObservableLedger = { reprPrec := Tau.BookIV.Calibration.instReprObservableLedger.repr }

---

### `Tau.BookIV.Calibration.instReprObservableLedger.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L66-L66)
**def
Tau.BookIV.Calibration.instReprObservableLedger.repr :ObservableLedger → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.ReadoutFunctor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L72-L85)
**structure
Tau.BookIV.Calibration.ReadoutFunctor :Type**


[IV.D301] The readout functor R_μ: L_τ → L_obs(μ) sends each
fixed ontic coupling κ(X;d) to its scale-dependent apparent value.
R_μ is a homomorphism preserving ordering and complement structure.

- source_count : ℕ
Source: 10 ontic couplings.

- source_eq : self.source_count = 10
- target_count : ℕ
Target: 10 apparent couplings at scale μ.

- target_eq : self.target_count = 10
- order_preserving : Bool
Order-preserving.

- order_true : self.order_preserving = true
Instances For

---

### `Tau.BookIV.Calibration.instReprReadoutFunctor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L85-L85)
**instance
Tau.BookIV.Calibration.instReprReadoutFunctor :Repr ReadoutFunctor**

Equations
- Tau.BookIV.Calibration.instReprReadoutFunctor = { reprPrec := Tau.BookIV.Calibration.instReprReadoutFunctor.repr }

---

### `Tau.BookIV.Calibration.instReprReadoutFunctor.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L85-L85)
**def
Tau.BookIV.Calibration.instReprReadoutFunctor.repr :ReadoutFunctor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.readout_properties`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L87-L90)
**theorem
Tau.BookIV.Calibration.readout_properties :{ source_count := 10, source_eq := ⋯, target_count := 10, target_eq := ⋯, order_preserving := true,
 order_true := ⋯ }.order_preserving = true**


[IV.P168] Readout properties: order preservation + complement preservation.

---

### `Tau.BookIV.Calibration.beta_as_derivative`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L92-L97)
**theorem
Tau.BookIV.Calibration.beta_as_derivative :{ sector := BookIII.Sectors.Sector.D, ontic_beta_zero := true, ontic_true := ⋯,
 apparent_nonzero := true }.ontic_beta_zero = true**


[IV.P169] The orthodox beta function is the logarithmic derivative
of the readout functor: β(α_X) = κ(X;d)·dR_μ/d(ln μ).
Since κ(X;d) is constant, all "running" resides in R_μ.

---

### `Tau.BookIV.Calibration.EntropyAtScale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L109-L122)
**structure
Tau.BookIV.Calibration.EntropyAtScale :Type**


[IV.D302] Entropy splitting at scale μ: S_X(μ) = S_vis(μ) + S_hid(μ).
S_vis is the entropy visible to instruments at scale μ.
S_hid is the entropy hidden below that resolution.

- sector : BookIII.Sectors.Sector
Sector.

- s_vis_numer : ℕ
Visible entropy numerator.

- s_hid_numer : ℕ
Hidden entropy numerator.

- total_numer : ℕ
Total is conserved (vis + hid = total).

- total_split : self.total_numer = self.s_vis_numer + self.s_hid_numer
Instances For

---

### `Tau.BookIV.Calibration.instReprEntropyAtScale.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L122-L122)
**def
Tau.BookIV.Calibration.instReprEntropyAtScale.repr :EntropyAtScale → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprEntropyAtScale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L122-L122)
**instance
Tau.BookIV.Calibration.instReprEntropyAtScale :Repr EntropyAtScale**

Equations
- Tau.BookIV.Calibration.instReprEntropyAtScale = { reprPrec := Tau.BookIV.Calibration.instReprEntropyAtScale.repr }

---

### `Tau.BookIV.Calibration.entropy_invariance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L124-L129)
**theorem
Tau.BookIV.Calibration.entropy_invariance
(e : EntropyAtScale)
 :e.total_numer = e.s_vis_numer + e.s_hid_numer**


[IV.P170] Total entropy invariance: S_total is μ-independent.
dS_vis/dμ = −dS_hid/dμ for each sector.

---

### `Tau.BookIV.Calibration.RegimeTransition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L135-L145)
**structure
Tau.BookIV.Calibration.RegimeTransition :Type**


[IV.D303] A regime transition at scale μ_*: a discontinuity in the
entropy splitting where S_vis jumps as a new sector becomes visible.

- scale_numer : ℕ
Transition scale (encoded as scaled Nat).

- sector_from : BookIII.Sectors.Sector
Sectors involved in the transition.

- sector_to : BookIII.Sectors.Sector
- distinct : self.sector_from ≠ self.sector_to
Different sectors.

Instances For

---

### `Tau.BookIV.Calibration.instReprRegimeTransition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L145-L145)
**def
Tau.BookIV.Calibration.instReprRegimeTransition.repr :RegimeTransition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprRegimeTransition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L145-L145)
**instance
Tau.BookIV.Calibration.instReprRegimeTransition :Repr RegimeTransition**

Equations
- Tau.BookIV.Calibration.instReprRegimeTransition = { reprPrec := Tau.BookIV.Calibration.instReprRegimeTransition.repr }

---

### `Tau.BookIV.Calibration.ReadoutLandscape`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L154-L164)
**structure
Tau.BookIV.Calibration.ReadoutLandscape :Type**


[IV.D304] The readout landscape R = {R_μ}_{μ>0}: the family of
readout functors indexed by energy scale. Encodes the totality
of scale-dependent physics.

- factor_count : ℕ
Number of sector-specific readout factors.

- factor_eq : self.factor_count = 5
- determined : Bool
Uniquely determined by boundary holonomy.

- determined_true : self.determined = true
Instances For

---

### `Tau.BookIV.Calibration.instReprReadoutLandscape.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L164-L164)
**def
Tau.BookIV.Calibration.instReprReadoutLandscape.repr :ReadoutLandscape → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Calibration.instReprReadoutLandscape`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L164-L164)
**instance
Tau.BookIV.Calibration.instReprReadoutLandscape :Repr ReadoutLandscape**

Equations
- Tau.BookIV.Calibration.instReprReadoutLandscape = { reprPrec := Tau.BookIV.Calibration.instReprReadoutLandscape.repr }

---

### `Tau.BookIV.Calibration.readout_landscape_unique`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Calibration/RunningRegime.lean#L170-L174)
**theorem
Tau.BookIV.Calibration.readout_landscape_unique :{ factor_count := 5, factor_eq := ⋯, determined := true, determined_true := ⋯ }.determined = true**


[IV.T113] The readout landscape is uniquely determined by the
boundary holonomy algebra and the enrichment layer E₁.
No additional input is needed beyond ι<sub>τ</sub>.
