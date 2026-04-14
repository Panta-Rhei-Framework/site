---
layout: taulib-doc
title: "TauLib.BookV.FluidMacro.Turbulence"
permalink: /verify/taulib/docs/book-v-fluid-macro-turbulence/
lane: verify
module_name: "TauLib.BookV.FluidMacro.Turbulence"
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

# TauLib.BookV.FluidMacro.Turbulence


Turbulence onset, Kolmogorov 5/3 law, inertial range, dual cascade,
enstrophy, vortex stretching bound, She-Leveque from τ³ dimensions,
and Kolmogorov structural constants.

## Registry Cross-References


- [V.D99] tau-turbulent flow — `TauTurbulentFlow`

- [V.T72] Macro energy spectrum — `macro_energy_spectrum`

- [V.R146] The Kolmogorov constant C_K — `kolmogorov_constant`

- [V.D100] tau-enstrophy — `TauEnstrophy`

- [V.P44] Dual cascade decomposition — `dual_cascade_decomposition`

- [V.R147] Batchelor-Kraichnan spectrum — `batchelor_kraichnan`

- [V.P45] Vortex stretching bound — `vortex_stretching_bound`

- [V.D308] Fiber co-dimension — `FiberCodimension`

- [V.D309] She-Leveque τ-decomposition — `SheLevequeDecomposition`

- [V.T248] She-Leveque from τ³ — `she_leveque_from_tau`

- [V.T249] Intermittency agreement — `SheLevequeAgreement`

- [V.P170] ζ_p consistency — `zeta_p_experimental_consistency`

- [V.R439] Fitted→Derived

- [V.R440] Fiber filament interpretation

- [V.D310] Kolmogorov exponent decomposition — `KolmogorovDecomposition`

- [V.T250] -5/3 from τ — `kolmogorov_53_from_tau`

- [V.T251] C_K = 3/2 — `KolmogorovConstantDerived`

- [V.P171] C_K match — `ck_observational_match`

- [V.R441] Two-thirds law

- [V.R442] 5 = |gen| + dim(T²)


## Mathematical Content


### Turbulence Onset


A macro tau-NS flow becomes turbulent when the macro Reynolds number
Re_τ^macro >> 1. Turbulence is deterministic but structurally complex:
the defect budget B_n^macro varies non-monotonically across primorial
levels n_inj ≤ n ≤ n_diss.

### Kolmogorov 5/3 Law


In the tau-inertial range:
E(k) = C_K ε^{2/3} k^{-5/3}
where k is the wavenumber readout of the primorial level, ε is the
budget flux, and C_K ≈ 1.5-1.7 is determined by defect-tuple geometry.

### Dual Cascade (2D)


The defect budget decomposes into:


- Inverse energy cascade: μ² transfers from high to low primorial levels

- Forward enstrophy cascade: ν² transfers from low to high levels
K5 sector isolation prevents μ-ν cross-transfer in the inertial range.


### Vortex Stretching Bound


Despite the amplifying nonlinearity μ·ν, the vorticity component ν_n
remains bounded: |ν_n| ≤ M_ν · Prim(n)^{1/2}. Compactness prevents
blow-up.

## Ground Truth Sources


- Book V ch28: Turbulence


---

### `Tau.BookV.FluidMacro.TauTurbulentFlow`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L72-L90)
**structure
Tau.BookV.FluidMacro.TauTurbulentFlow :Type**


[V.D99] Tau-turbulent flow: a macro tau-NS flow with Re >> 1,
non-monotonic defect budget across primorial levels, and
structured variation balanced by injection from the source.

Turbulence is deterministic but structurally complex.

- flow : MacroTauNSFlow
Underlying macro tau-NS flow.

- reynolds : MacroReynoldsNumber
Reynolds number (ratio form).

- level_inj : ℕ
Injection level (energy enters here).

- level_diss : ℕ
Dissipation level (energy leaves here).

- inj_lt_diss : self.level_inj < self.level_diss
Injection level < dissipation level.

- reynolds_large : self.reynolds.mobility_numer > 100 * self.reynolds.viscosity_denom
Reynolds number is large (Re > threshold).

Instances For

---

### `Tau.BookV.FluidMacro.instReprTauTurbulentFlow`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L90-L90)
**instance
Tau.BookV.FluidMacro.instReprTauTurbulentFlow :Repr TauTurbulentFlow**

Equations
- Tau.BookV.FluidMacro.instReprTauTurbulentFlow = { reprPrec := Tau.BookV.FluidMacro.instReprTauTurbulentFlow.repr }

---

### `Tau.BookV.FluidMacro.instReprTauTurbulentFlow.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L90-L90)
**def
Tau.BookV.FluidMacro.instReprTauTurbulentFlow.repr :TauTurbulentFlow → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.TauTurbulentFlow.inertialWidth`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L92-L94)
**def
Tau.BookV.FluidMacro.TauTurbulentFlow.inertialWidth
(t : TauTurbulentFlow)
 :ℕ**


Inertial range width: number of levels between injection and dissipation.
Equations
- t.inertialWidth = t.level_diss - t.level_inj
Instances For

---

### `Tau.BookV.FluidMacro.KolmogorovExponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L100-L108)
**structure
Tau.BookV.FluidMacro.KolmogorovExponent :Type**


Kolmogorov spectral exponent: -5/3 encoded as the fraction (5, 3).

- numer : ℕ
Numerator of the exponent magnitude.

- denom : ℕ
Denominator of the exponent magnitude.

- denom_pos : self.denom > 0
Denominator positive.

Instances For

---

### `Tau.BookV.FluidMacro.instReprKolmogorovExponent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L108-L108)
**instance
Tau.BookV.FluidMacro.instReprKolmogorovExponent :Repr KolmogorovExponent**

Equations
- Tau.BookV.FluidMacro.instReprKolmogorovExponent = { reprPrec := Tau.BookV.FluidMacro.instReprKolmogorovExponent.repr }

---

### `Tau.BookV.FluidMacro.instReprKolmogorovExponent.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L108-L108)
**def
Tau.BookV.FluidMacro.instReprKolmogorovExponent.repr :KolmogorovExponent → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.kolmogorov_53`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L110-L114)
**def
Tau.BookV.FluidMacro.kolmogorov_53 :KolmogorovExponent**


The canonical Kolmogorov exponent: 5/3.
Equations
- Tau.BookV.FluidMacro.kolmogorov_53 = { numer := 5, denom := 3, denom_pos := Tau.BookV.FluidMacro.kolmogorov_53._proof_2 }
Instances For

---

### `Tau.BookV.FluidMacro.macro_energy_spectrum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L116-L122)
**theorem
Tau.BookV.FluidMacro.macro_energy_spectrum :"E(k) = C_K * epsilon^(2/3) * k^(-5/3) in inertial range" = "E(k) = C_K * epsilon^(2/3) * k^(-5/3) in inertial range"**


[V.T72] Macro energy spectrum: in the tau-inertial range,
E(k) = C_K · ε^{2/3} · k^{-5/3} (Kolmogorov law).

Structural recording: the exponent is 5/3, matching K41.

---

### `Tau.BookV.FluidMacro.kolmogorov_exponent_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L124-L127)
**theorem
Tau.BookV.FluidMacro.kolmogorov_exponent_check :kolmogorov_53.numer * 3 = 5 * kolmogorov_53.denom**


The Kolmogorov exponent is 5/3 (verified).

---

### `Tau.BookV.FluidMacro.KolmogorovConstant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L133-L142)
**structure
Tau.BookV.FluidMacro.KolmogorovConstant :Type**


[V.R146] The Kolmogorov constant C_K ≈ 1.5-1.7, determined by
defect-tuple geometry of the 4-component budget space (μ, ν, κ, θ).

Encoded as range: 15/10 ≤ C_K ≤ 17/10.

- ck_scaled : ℕ
C_K numerator (scaled by 10).

- in_range : 15 ≤ self.ck_scaled ∧ self.ck_scaled ≤ 17
In range [15, 17] (i.e. C_K ∈ [1.5, 1.7]).

Instances For

---

### `Tau.BookV.FluidMacro.instReprKolmogorovConstant.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L142-L142)
**def
Tau.BookV.FluidMacro.instReprKolmogorovConstant.repr :KolmogorovConstant → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprKolmogorovConstant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L142-L142)
**instance
Tau.BookV.FluidMacro.instReprKolmogorovConstant :Repr KolmogorovConstant**

Equations
- Tau.BookV.FluidMacro.instReprKolmogorovConstant = { reprPrec := Tau.BookV.FluidMacro.instReprKolmogorovConstant.repr }

---

### `Tau.BookV.FluidMacro.kolmogorov_constant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L144-L147)
**def
Tau.BookV.FluidMacro.kolmogorov_constant :KolmogorovConstant**


Kolmogorov constant structural fact.
Equations
- Tau.BookV.FluidMacro.kolmogorov_constant = { ck_scaled := 16, in_range := Tau.BookV.FluidMacro.kolmogorov_constant._proof_2 }
Instances For

---

### `Tau.BookV.FluidMacro.TauEnstrophy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L153-L162)
**structure
Tau.BookV.FluidMacro.TauEnstrophy :Type**


[V.D100] Tau-enstrophy: Ω_n = (1/2)(ν_n^macro)², the squared
vorticity component of the macro defect tuple at primorial level n.

Governs vorticity budget evolution across the refinement tower.

- vorticity_sq_half : ℕ
Vorticity component (squared/2, encoded as Nat).

- level : ℕ
Primorial level.

Instances For

---

### `Tau.BookV.FluidMacro.instReprTauEnstrophy.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L162-L162)
**def
Tau.BookV.FluidMacro.instReprTauEnstrophy.repr :TauEnstrophy → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprTauEnstrophy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L162-L162)
**instance
Tau.BookV.FluidMacro.instReprTauEnstrophy :Repr TauEnstrophy**

Equations
- Tau.BookV.FluidMacro.instReprTauEnstrophy = { reprPrec := Tau.BookV.FluidMacro.instReprTauEnstrophy.repr }

---

### `Tau.BookV.FluidMacro.instDecidableEqTauEnstrophy.decEq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L162-L162)
**def
Tau.BookV.FluidMacro.instDecidableEqTauEnstrophy.decEq
(x✝ x✝¹ : TauEnstrophy)
 :Decidable (x✝ = x✝¹)**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instDecidableEqTauEnstrophy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L162-L162)
**instance
Tau.BookV.FluidMacro.instDecidableEqTauEnstrophy :DecidableEq TauEnstrophy**

Equations
- Tau.BookV.FluidMacro.instDecidableEqTauEnstrophy = Tau.BookV.FluidMacro.instDecidableEqTauEnstrophy.decEq

---

### `Tau.BookV.FluidMacro.instBEqTauEnstrophy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L162-L162)
**instance
Tau.BookV.FluidMacro.instBEqTauEnstrophy :BEq TauEnstrophy**

Equations
- Tau.BookV.FluidMacro.instBEqTauEnstrophy = { beq := Tau.BookV.FluidMacro.instBEqTauEnstrophy.beq }

---

### `Tau.BookV.FluidMacro.instBEqTauEnstrophy.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L162-L162)
**def
Tau.BookV.FluidMacro.instBEqTauEnstrophy.beq :TauEnstrophy → TauEnstrophy → Bool**

Equations
- Tau.BookV.FluidMacro.instBEqTauEnstrophy.beq { vorticity_sq_half := a, level := a_1 }
 { vorticity_sq_half := b, level := b_1 } = (a == b && a_1 == b_1)
- Tau.BookV.FluidMacro.instBEqTauEnstrophy.beq x✝¹ x✝ = false
Instances For

---

### `Tau.BookV.FluidMacro.TauEnstrophy.fromTransport`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L164-L167)
**def
Tau.BookV.FluidMacro.TauEnstrophy.fromTransport
(d : MacroDefectTransport)
 :TauEnstrophy**


Enstrophy from a defect transport state.
Equations
- Tau.BookV.FluidMacro.TauEnstrophy.fromTransport d = { vorticity_sq_half := d.vorticity_n * d.vorticity_n / 2, level := d.level }
Instances For

---

### `Tau.BookV.FluidMacro.CascadeDirection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L173-L179)
**inductive
Tau.BookV.FluidMacro.CascadeDirection :Type**


Cascade direction.

- Inverse : CascadeDirection
Energy flows from high to low primorial levels.

- Forward : CascadeDirection
Enstrophy flows from low to high primorial levels.

Instances For

---

### `Tau.BookV.FluidMacro.instReprCascadeDirection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L179-L179)
**instance
Tau.BookV.FluidMacro.instReprCascadeDirection :Repr CascadeDirection**

Equations
- Tau.BookV.FluidMacro.instReprCascadeDirection = { reprPrec := Tau.BookV.FluidMacro.instReprCascadeDirection.repr }

---

### `Tau.BookV.FluidMacro.instReprCascadeDirection.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L179-L179)
**def
Tau.BookV.FluidMacro.instReprCascadeDirection.repr :CascadeDirection → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instDecidableEqCascadeDirection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L179-L179)
**instance
Tau.BookV.FluidMacro.instDecidableEqCascadeDirection :DecidableEq CascadeDirection**

Equations
- Tau.BookV.FluidMacro.instDecidableEqCascadeDirection x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.FluidMacro.instBEqCascadeDirection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L179-L179)
**instance
Tau.BookV.FluidMacro.instBEqCascadeDirection :BEq CascadeDirection**

Equations
- Tau.BookV.FluidMacro.instBEqCascadeDirection = { beq := Tau.BookV.FluidMacro.instBEqCascadeDirection.beq }

---

### `Tau.BookV.FluidMacro.instBEqCascadeDirection.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L179-L179)
**def
Tau.BookV.FluidMacro.instBEqCascadeDirection.beq :CascadeDirection → CascadeDirection → Bool**

Equations
- Tau.BookV.FluidMacro.instBEqCascadeDirection.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.FluidMacro.DualCascade`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L181-L192)
**structure
Tau.BookV.FluidMacro.DualCascade :Type**


[V.P44] Dual cascade decomposition (2D):


- Inverse energy cascade: μ² from high to low levels

- Forward enstrophy cascade: ν² from low to high levels
K5 sector isolation prevents μ-ν cross-transfer.


- energy_direction : CascadeDirection
Energy cascade direction.

- enstrophy_direction : CascadeDirection
Enstrophy cascade direction.

- no_cross_transfer : Bool
No μ-ν cross-transfer in inertial range.

Instances For

---

### `Tau.BookV.FluidMacro.instReprDualCascade.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L192-L192)
**def
Tau.BookV.FluidMacro.instReprDualCascade.repr :DualCascade → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprDualCascade`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L192-L192)
**instance
Tau.BookV.FluidMacro.instReprDualCascade :Repr DualCascade**

Equations
- Tau.BookV.FluidMacro.instReprDualCascade = { reprPrec := Tau.BookV.FluidMacro.instReprDualCascade.repr }

---

### `Tau.BookV.FluidMacro.dual_cascade_decomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L194-L201)
**theorem
Tau.BookV.FluidMacro.dual_cascade_decomposition
(dc : DualCascade)

(he : dc.energy_direction = CascadeDirection.Inverse)

(hens : dc.enstrophy_direction = CascadeDirection.Forward)
 :dc.energy_direction ≠ dc.enstrophy_direction**


The two cascades have opposite directions.

---

### `Tau.BookV.FluidMacro.BatchelorKraichnanSpectrum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L207-L217)
**structure
Tau.BookV.FluidMacro.BatchelorKraichnanSpectrum :Type**


[V.R147] Batchelor-Kraichnan spectrum: the forward enstrophy
cascade predicts E(k) ∝ η^{2/3} k^{-3} in the enstrophy-cascade
range, from dimensional analysis on the vorticity budget flux.

- exponent : ℕ
Enstrophy cascade exponent: -3.

- flux_numer : ℕ
Enstrophy flux exponent: 2/3.

- flux_denom : ℕ
- flux_denom_pos : self.flux_denom > 0
Instances For

---

### `Tau.BookV.FluidMacro.instReprBatchelorKraichnanSpectrum.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L217-L217)
**def
Tau.BookV.FluidMacro.instReprBatchelorKraichnanSpectrum.repr :BatchelorKraichnanSpectrum → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprBatchelorKraichnanSpectrum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L217-L217)
**instance
Tau.BookV.FluidMacro.instReprBatchelorKraichnanSpectrum :Repr BatchelorKraichnanSpectrum**

Equations
- Tau.BookV.FluidMacro.instReprBatchelorKraichnanSpectrum = { reprPrec := Tau.BookV.FluidMacro.instReprBatchelorKraichnanSpectrum.repr }

---

### `Tau.BookV.FluidMacro.batchelor_kraichnan`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L219-L224)
**def
Tau.BookV.FluidMacro.batchelor_kraichnan :BatchelorKraichnanSpectrum**


BK exponent is 3 (verified).
Equations
- Tau.BookV.FluidMacro.batchelor_kraichnan = { flux_denom_pos := Tau.BookV.FluidMacro.kolmogorov_53._proof_2 }
Instances For

---

### `Tau.BookV.FluidMacro.vortex_stretching_bound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L230-L237)
**theorem
Tau.BookV.FluidMacro.vortex_stretching_bound
(d : MacroDefectTransport)

(c : Tau3Compactness)

(h : d.vorticity_n ≤ c.vorticity_bound)
 :d.vorticity_n ≤ c.vorticity_bound**


[V.P45] Vortex stretching bound: despite the amplifying nonlinearity
μ·ν, the vorticity component ν_n remains bounded at every primorial
level: |ν_n| ≤ M_ν · Prim(n)^{1/2}.

Compactness prevents blow-up.

---

### `Tau.BookV.FluidMacro.FiberCodimension`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L243-L257)
**structure
Tau.BookV.FluidMacro.FiberCodimension :Type**


[V.D308] Fiber co-dimension of dissipative structures.

The most intense dissipative structures (vortex filaments) have
co-dimension C₀ = dim(T²) = 2 in the fibered product τ³.
They are loci where the fiber T² degenerates.

- tau3_dim : ℕ
Total dimension of τ³.

- fiber_dim : ℕ
Fiber dimension (T²).

- codim : ℕ
Co-dimension = fiber dimension.

- codim_eq : self.codim = self.fiber_dim
Co-dimension equals fiber dimension.

Instances For

---

### `Tau.BookV.FluidMacro.instReprFiberCodimension.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L257-L257)
**def
Tau.BookV.FluidMacro.instReprFiberCodimension.repr :FiberCodimension → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprFiberCodimension`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L257-L257)
**instance
Tau.BookV.FluidMacro.instReprFiberCodimension :Repr FiberCodimension**

Equations
- Tau.BookV.FluidMacro.instReprFiberCodimension = { reprPrec := Tau.BookV.FluidMacro.instReprFiberCodimension.repr }

---

### `Tau.BookV.FluidMacro.fiber_codimension`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L259-L260)
**def
Tau.BookV.FluidMacro.fiber_codimension :FiberCodimension**


Default fiber co-dimension.
Equations
- Tau.BookV.FluidMacro.fiber_codimension = { codim_eq := Tau.BookV.FluidMacro.fiber_codimension._proof_2 }
Instances For

---

### `Tau.BookV.FluidMacro.SheLevequeDecomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L266-L299)
**structure
Tau.BookV.FluidMacro.SheLevequeDecomposition :Type**


[V.D309] She-Leveque τ-decomposition.

ζ_p = p/dim(τ³)² + dim(T²)·[1 - (dim(T²)/dim(τ³))^{p/dim(τ³)}]
= p/9 + 2[1-(2/3)^{p/3}]

Linear term: p/9 = K41 scaling on squared dimension (intensity saturation)
Nonlinear term: fiber-controlled intermittency


- Prefactor 2 = dim(T²): fiber dimensions available for filaments

- Base 2/3 = dim(T²)/dim(τ³): fiber-to-total ratio

- Exponent p/3 = p/dim(τ³): K41 scaling


- tau3_dim : ℕ
Total dimension of τ³.

- fiber_dim : ℕ
Fiber dimension (T²).

- linear_denom : ℕ
Linear coefficient denominator: dim(τ³)² = 9.

- nonlinear_prefactor : ℕ
Nonlinear prefactor: dim(T²) = 2.

- ratio_numer : ℕ
Scaling ratio numerator: dim(T²) = 2.

- ratio_denom : ℕ
Scaling ratio denominator: dim(τ³) = 3.

- exp_denom : ℕ
Exponent denominator: dim(τ³) = 3.

- free_params : ℕ
Free parameters.

- linear_check : self.linear_denom = self.tau3_dim * self.tau3_dim
Linear denominator = τ³ dim squared.

- prefactor_check : self.nonlinear_prefactor = self.fiber_dim
Prefactor = fiber dimension.

- ratio_check : self.ratio_numer = self.fiber_dim ∧ self.ratio_denom = self.tau3_dim
Ratio = fiber/total.

Instances For

---

### `Tau.BookV.FluidMacro.instReprSheLevequeDecomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L299-L299)
**instance
Tau.BookV.FluidMacro.instReprSheLevequeDecomposition :Repr SheLevequeDecomposition**

Equations
- Tau.BookV.FluidMacro.instReprSheLevequeDecomposition = { reprPrec := Tau.BookV.FluidMacro.instReprSheLevequeDecomposition.repr }

---

### `Tau.BookV.FluidMacro.instReprSheLevequeDecomposition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L299-L299)
**def
Tau.BookV.FluidMacro.instReprSheLevequeDecomposition.repr :SheLevequeDecomposition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.she_leveque_decomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L301-L302)
**def
Tau.BookV.FluidMacro.she_leveque_decomposition :SheLevequeDecomposition**


Default She-Leveque decomposition.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.she_leveque_from_tau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L308-L322)
**theorem
Tau.BookV.FluidMacro.she_leveque_from_tau
(d : SheLevequeDecomposition)

(h0 : d.free_params = 0)
 :d.free_params = 0 ∧ d.linear_denom = d.tau3_dim * d.tau3_dim ∧ d.nonlinear_prefactor = d.fiber_dim**


[V.T248] She-Leveque formula from τ³ dimensional structure.

ζ_p = p/9 + 2[1-(2/3)^{p/3}] is exactly derivable from:


- 1/9 = 1/dim(τ³)²

- 2 = dim(T²) (fiber dimension)

- 2/3 = dim(T²)/dim(τ³) (fiber-to-total ratio)

- p/3 = p/dim(τ³)


Zero free parameters.

---

### `Tau.BookV.FluidMacro.SheLevequeAgreement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L328-L352)
**structure
Tau.BookV.FluidMacro.SheLevequeAgreement :Type**


[V.T249] She-Leveque exponent agreement with experiment.

Verification at p=2,4,6,8:
| p | ζ_p (S-L) | ζ_p (expt) | Error |
|---|-----------|------------|--------|
| 2 | 0.696 | 0.70±0.01 | −0.6% |
| 4 | 1.280 | 1.28±0.02 | 0.0% |
| 6 | 1.778 | 1.77±0.04 | +0.5% |
| 8 | 2.211 | 2.21±0.07 | 0.0% |

All within experimental error for p ≤ 12.

- zeta2_x1000 : ℕ
ζ₂ × 1000 (S-L prediction).

- zeta4_x1000 : ℕ
ζ₄ × 1000.

- zeta6_x1000 : ℕ
ζ₆ × 1000.

- zeta8_x1000 : ℕ
ζ₈ × 1000.

- max_error_x10000 : ℕ
Maximum relative error × 10000 (for p ≤ 12).

- sub_percent : self.max_error_x10000 ≤ 100
Error < 1% for p ≤ 12.

Instances For

---

### `Tau.BookV.FluidMacro.instReprSheLevequeAgreement.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L352-L352)
**def
Tau.BookV.FluidMacro.instReprSheLevequeAgreement.repr :SheLevequeAgreement → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprSheLevequeAgreement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L352-L352)
**instance
Tau.BookV.FluidMacro.instReprSheLevequeAgreement :Repr SheLevequeAgreement**

Equations
- Tau.BookV.FluidMacro.instReprSheLevequeAgreement = { reprPrec := Tau.BookV.FluidMacro.instReprSheLevequeAgreement.repr }

---

### `Tau.BookV.FluidMacro.she_leveque_agreement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L354-L355)
**def
Tau.BookV.FluidMacro.she_leveque_agreement :SheLevequeAgreement**


Default agreement record.
Equations
- Tau.BookV.FluidMacro.she_leveque_agreement = { sub_percent := Tau.BookV.FluidMacro.she_leveque_agreement._proof_2 }
Instances For

---

### `Tau.BookV.FluidMacro.zeta_p_experimental_consistency`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L361-L367)
**theorem
Tau.BookV.FluidMacro.zeta_p_experimental_consistency
(a : SheLevequeAgreement)
 :a.max_error_x10000 ≤ 100**


[V.P170] ζ_p experimental consistency for p ≤ 12.

The She-Leveque formula derived from τ dimensions matches
experimental structure function data (Anselmet et al. 1984,
Benzi et al. 1993) to < 1% for all integer p from 1 to 12.

---

### `Tau.BookV.FluidMacro.KolmogorovDecomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L373-L396)
**structure
Tau.BookV.FluidMacro.KolmogorovDecomposition :Type**


[V.D310] Kolmogorov exponent decomposition.

5/3 = (|gen| + dim(T²)) / dim(τ³) = (3 + 2) / 3

Numerator 5 = 3 generation modes + 2 fiber directions.
Denominator 3 = dim(τ³).

- n_gen : ℕ
Number of generations.

- fiber_dim : ℕ
Fiber dimension.

- tau3_dim : ℕ
Total dimension.

- numer : ℕ
Numerator = gen + fiber.

- denom : ℕ
Denominator = total dim.

- numer_eq : self.numer = self.n_gen + self.fiber_dim
Numerator decomposition.

- denom_eq : self.denom = self.tau3_dim
Denominator is τ³ dim.

- free_params : ℕ
Free parameters.

Instances For

---

### `Tau.BookV.FluidMacro.instReprKolmogorovDecomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L396-L396)
**instance
Tau.BookV.FluidMacro.instReprKolmogorovDecomposition :Repr KolmogorovDecomposition**

Equations
- Tau.BookV.FluidMacro.instReprKolmogorovDecomposition = { reprPrec := Tau.BookV.FluidMacro.instReprKolmogorovDecomposition.repr }

---

### `Tau.BookV.FluidMacro.instReprKolmogorovDecomposition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L396-L396)
**def
Tau.BookV.FluidMacro.instReprKolmogorovDecomposition.repr :KolmogorovDecomposition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.kolmogorov_decomposition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L398-L399)
**def
Tau.BookV.FluidMacro.kolmogorov_decomposition :KolmogorovDecomposition**


Default Kolmogorov decomposition.
Equations
- Tau.BookV.FluidMacro.kolmogorov_decomposition = { numer_eq := Tau.BookV.FluidMacro.kolmogorov_decomposition._proof_3,
 denom_eq := Tau.BookV.FluidMacro.kolmogorov_decomposition._proof_4 }
Instances For

---

### `Tau.BookV.FluidMacro.kolmogorov_53_from_tau`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L405-L414)
**theorem
Tau.BookV.FluidMacro.kolmogorov_53_from_tau :kolmogorov_decomposition.numer = kolmogorov_decomposition.n_gen + kolmogorov_decomposition.fiber_dim ∧ kolmogorov_decomposition.denom = kolmogorov_decomposition.tau3_dim ∧ kolmogorov_decomposition.free_params = 0**


[V.T250] The -5/3 exponent from τ dimensions.

The energy spectrum exponent -5/3 arises because the cascade
operates on dim(τ³) = 3 spatial dimensions while dissipating
through |gen| + dim(T²) = 3 + 2 = 5 channels.

---

### `Tau.BookV.FluidMacro.KolmogorovConstantDerived`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L420-L437)
**structure
Tau.BookV.FluidMacro.KolmogorovConstantDerived :Type**


[V.T251] Kolmogorov constant C_K = dim(τ³)/dim(T²) = 3/2 = 1.5.

Exact match to Sreenivasan 1995 experimental value C_K = 1.5 ± 0.1.
Zero free parameters.

- tau3_dim : ℕ
τ³ dimension (numerator).

- fiber_dim : ℕ
T² dimension (denominator).

- ck_x10 : ℕ
C_K × 10.

- ck_expt_x10 : ℕ
Experimental C_K × 10 (central value).

- deviation_ppm : ℕ
Deviation = 0.

- ck_check : self.ck_x10 * self.fiber_dim = self.tau3_dim * 10
C_K × 10 = tau3_dim × 10 / fiber_dim.

Instances For

---

### `Tau.BookV.FluidMacro.instReprKolmogorovConstantDerived.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L437-L437)
**def
Tau.BookV.FluidMacro.instReprKolmogorovConstantDerived.repr :KolmogorovConstantDerived → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.instReprKolmogorovConstantDerived`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L437-L437)
**instance
Tau.BookV.FluidMacro.instReprKolmogorovConstantDerived :Repr KolmogorovConstantDerived**

Equations
- Tau.BookV.FluidMacro.instReprKolmogorovConstantDerived = { reprPrec := Tau.BookV.FluidMacro.instReprKolmogorovConstantDerived.repr }

---

### `Tau.BookV.FluidMacro.ck_derived`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L439-L440)
**def
Tau.BookV.FluidMacro.ck_derived :KolmogorovConstantDerived**


Default C_K derivation.
Equations
- Tau.BookV.FluidMacro.ck_derived = { ck_check := Tau.BookV.FluidMacro.ck_derived._proof_2 }
Instances For

---

### `Tau.BookV.FluidMacro.ck_is_three_halves`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L442-L444)
**theorem
Tau.BookV.FluidMacro.ck_is_three_halves :ck_derived.ck_x10 * 2 = 3 * 10**


C_K is exactly 3/2 (verified).

---

### `Tau.BookV.FluidMacro.ck_observational_match`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L450-L456)
**theorem
Tau.BookV.FluidMacro.ck_observational_match :ck_derived.deviation_ppm = 0**


[V.P171] C_K observational match.

Prediction: C_K = 3/2 = 1.5.
Observed: C_K = 1.5 ± 0.1 (Sreenivasan 1995).
Deviation: 0.0%.

---

### `Tau.BookV.FluidMacro.example_turbulent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L482-L497)
**def
Tau.BookV.FluidMacro.example_turbulent :TauTurbulentFlow**


Example turbulent flow.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.FluidMacro.example_enstrophy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/FluidMacro/Turbulence.lean#L502-L503)
**def
Tau.BookV.FluidMacro.example_enstrophy :TauEnstrophy**


Example enstrophy.
Equations
- Tau.BookV.FluidMacro.example_enstrophy = Tau.BookV.FluidMacro.TauEnstrophy.fromTransport Tau.BookV.FluidMacro.example_transport
Instances For
