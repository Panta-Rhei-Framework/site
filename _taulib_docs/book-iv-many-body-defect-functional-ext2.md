---
layout: taulib-doc
title: "TauLib.BookIV.ManyBody.DefectFunctionalExt2"
permalink: /verify/taulib/docs/book-iv-many-body-defect-functional-ext2/
lane: verify
module_name: "TauLib.BookIV.ManyBody.DefectFunctionalExt2"
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

# TauLib.BookIV.ManyBody.DefectFunctionalExt2


Continuation of the many-body defect functional extension: fluid regime
definitions (Euler, NS, MHD, plasma, superfluid, superconductor),
temperature as defect gradient, phase transitions as regime crossings,
and thermodynamic structure.

## Registry Cross-References


- [IV.D222] Euler Fluid Regime — `EulerFluidRegime`

- [IV.P136] tau-Euler Equation — `TauEulerEquation`

- [IV.D223] Navier-Stokes Regime — `NavierStokesRegime`

- [IV.R161] Turbulence question — comment-only (conjectural)

- [IV.D224] MHD Regime — `MHDRegime`

- [IV.R162] MHD frozen flux — comment-only

- [IV.D225] Plasma Regime — `PlasmaRegime`

- [IV.D226] Superfluid Regime — `SuperfluidRegime`

- [IV.P137] Superfluid Vortex Quantization — `SuperfluidVortexQuantization`

- [IV.R163] Helium-4 and beyond — `remark_helium4`

- [IV.D227] Superconductor Regime — `SuperconductorRegime`

- [IV.P138] Flux Quantization — `FluxQuantization`

- [IV.R164] Cooper pairing is topological — `remark_cooper_pairing`

- [IV.R165] Regime table recap — comment-only

- [IV.D228] Temperature as Defect Gradient — `TemperatureAsDefectGradient`

- [IV.R166] Boltzmann constant status — comment-only

- [IV.P139] Status of Boltzmann Constant — `BoltzmannConstantStatus`

- [IV.R167] No intrinsic temperature scale — comment-only

- [IV.T91] Second Law via Defect Functional — `SecondLawViaDefect`

- [IV.R168] Arrow of time recap — comment-only

- [IV.D229] First-order Phase Transition — `FirstOrderTransition`

- [IV.D230] Second-order Phase Transition — `SecondOrderTransition`

- [IV.T92] Phase Transition as Regime Crossing — `PhaseTransitionRegimeCrossing`

- [IV.R169] Universality and critical exponents — `remark_universality` (conjectural)


## Mathematical Content


This module completes ch52 by defining the fluid regimes as subsets of
the defect tuple space D = R_{>=0} x R x R x Z, and establishing the
thermodynamic structure: temperature as the defect gradient, the second
law as defect-entropy non-decrease, and phase transitions as inequality
crossings in the defect tuple.

## Ground Truth Sources


- Chapter 52 of Book IV (2nd Edition)

- fluid-condensed-matter.json: regime classification, tau-superfluidity


---

### `Tau.BookIV.ManyBody.EulerFluidRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L60-L75)
**structure
Tau.BookIV.ManyBody.EulerFluidRegime :Type**


[IV.D222] The Euler fluid regime: the subset of D where
0 < mu <= mu_crit and the Euler budget constraint holds:
mu + nu + kappa + theta = const (inviscid, no dissipation).

Distinguished from the single-bundle Euler regime by including
N-body interaction corrections in the budget law.

- mobility_bounded : Bool
Mobility bounded by critical threshold.

- budget_conserved : Bool
Budget conservation holds.

- inviscid : Bool
No dissipation (inviscid).

- kelvin_holds : Bool
Kelvin circulation theorem holds.

Instances For

---

### `Tau.BookIV.ManyBody.instReprEulerFluidRegime.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L75-L75)
**def
Tau.BookIV.ManyBody.instReprEulerFluidRegime.repr :EulerFluidRegime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprEulerFluidRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L75-L75)
**instance
Tau.BookIV.ManyBody.instReprEulerFluidRegime :Repr EulerFluidRegime**

Equations
- Tau.BookIV.ManyBody.instReprEulerFluidRegime = { reprPrec := Tau.BookIV.ManyBody.instReprEulerFluidRegime.repr }

---

### `Tau.BookIV.ManyBody.euler_fluid_regime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L77-L77)
**def
Tau.BookIV.ManyBody.euler_fluid_regime :EulerFluidRegime**

Equations
- Tau.BookIV.ManyBody.euler_fluid_regime = { }
Instances For

---

### `Tau.BookIV.ManyBody.TauEulerEquation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L83-L96)
**structure
Tau.BookIV.ManyBody.TauEulerEquation :Type**


[IV.P136] In the Euler fluid regime the macroscopic defect tuple evolves as
d/dn (mu_n, nu_n, kappa_n, theta_n) = (f_mu, f_nu, f_kappa, 0) subject to
the budget constraint. The theta component has zero derivative because
topological charge is a deformation invariant.

This is the tau-native formulation of the Euler equation.

- theta_derivative_zero : Bool
Theta derivative is zero.

- budget_constraint : Bool
Budget constraint enforced.

- tau_native : Bool
tau-native (no PDE imported).

Instances For

---

### `Tau.BookIV.ManyBody.instReprTauEulerEquation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L96-L96)
**def
Tau.BookIV.ManyBody.instReprTauEulerEquation.repr :TauEulerEquation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprTauEulerEquation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L96-L96)
**instance
Tau.BookIV.ManyBody.instReprTauEulerEquation :Repr TauEulerEquation**

Equations
- Tau.BookIV.ManyBody.instReprTauEulerEquation = { reprPrec := Tau.BookIV.ManyBody.instReprTauEulerEquation.repr }

---

### `Tau.BookIV.ManyBody.tau_euler_equation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L98-L98)
**def
Tau.BookIV.ManyBody.tau_euler_equation :TauEulerEquation**

Equations
- Tau.BookIV.ManyBody.tau_euler_equation = { }
Instances For

---

### `Tau.BookIV.ManyBody.euler_theta_invariant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L100-L101)
**theorem
Tau.BookIV.ManyBody.euler_theta_invariant :tau_euler_equation.theta_derivative_zero = true**


---

### `Tau.BookIV.ManyBody.NavierStokesRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L107-L121)
**structure
Tau.BookIV.ManyBody.NavierStokesRegime :Type**


[IV.D223] The Navier-Stokes regime: mu > mu_crit, where the Euler
budget is broken by viscous shear-defect dissipation. The budget
decays monotonically, encoding energy dissipation.

The tau-NS equation is the evolution law in this regime.

- above_threshold : Bool
Mobility above critical threshold.

- budget_broken : Bool
Euler budget broken.

- dissipative : Bool
Dissipation present.

- viscosity_derived : Bool
Viscosity from defect geometry (not free parameter).

Instances For

---

### `Tau.BookIV.ManyBody.instReprNavierStokesRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L121-L121)
**instance
Tau.BookIV.ManyBody.instReprNavierStokesRegime :Repr NavierStokesRegime**

Equations
- Tau.BookIV.ManyBody.instReprNavierStokesRegime = { reprPrec := Tau.BookIV.ManyBody.instReprNavierStokesRegime.repr }

---

### `Tau.BookIV.ManyBody.instReprNavierStokesRegime.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L121-L121)
**def
Tau.BookIV.ManyBody.instReprNavierStokesRegime.repr :NavierStokesRegime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.ns_regime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L123-L123)
**def
Tau.BookIV.ManyBody.ns_regime :NavierStokesRegime**

Equations
- Tau.BookIV.ManyBody.ns_regime = { }
Instances For

---

### `Tau.BookIV.ManyBody.MHDRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L134-L148)
**structure
Tau.BookIV.ManyBody.MHDRegime :Type**


[IV.D224] The MHD (magnetohydrodynamic) regime: nu >> mu and kappa is
coupled to the B-sector. The system exhibits frozen-flux behavior
(Alfven modes) where magnetic field lines move with the fluid.

EM holonomy is coupled to fluid transport.

- vorticity_dominant : Bool
Vorticity dominates mobility.

- em_coupled : Bool
B-sector coupled (EM holonomy).

- frozen_flux : Bool
Frozen-flux behavior.

- alfven_modes : Bool
Alfven modes present.

Instances For

---

### `Tau.BookIV.ManyBody.instReprMHDRegime.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L148-L148)
**def
Tau.BookIV.ManyBody.instReprMHDRegime.repr :MHDRegime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprMHDRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L148-L148)
**instance
Tau.BookIV.ManyBody.instReprMHDRegime :Repr MHDRegime**

Equations
- Tau.BookIV.ManyBody.instReprMHDRegime = { reprPrec := Tau.BookIV.ManyBody.instReprMHDRegime.repr }

---

### `Tau.BookIV.ManyBody.mhd_regime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L150-L150)
**def
Tau.BookIV.ManyBody.mhd_regime :MHDRegime**

Equations
- Tau.BookIV.ManyBody.mhd_regime = { }
Instances For

---

### `Tau.BookIV.ManyBody.PlasmaRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L160-L170)
**structure
Tau.BookIV.ManyBody.PlasmaRegime :Type**


[IV.D225] The plasma regime: mu, |nu|, |kappa| > mu_crit and theta
is fluctuating (not globally fixed). Topological charge can change
through defect pair creation/annihilation.

- all_above_threshold : Bool
All transport components above threshold.

- theta_fluctuating : Bool
Theta fluctuating.

- debye_screening : Bool
Debye screening present.

Instances For

---

### `Tau.BookIV.ManyBody.instReprPlasmaRegime.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L170-L170)
**def
Tau.BookIV.ManyBody.instReprPlasmaRegime.repr :PlasmaRegime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprPlasmaRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L170-L170)
**instance
Tau.BookIV.ManyBody.instReprPlasmaRegime :Repr PlasmaRegime**

Equations
- Tau.BookIV.ManyBody.instReprPlasmaRegime = { reprPrec := Tau.BookIV.ManyBody.instReprPlasmaRegime.repr }

---

### `Tau.BookIV.ManyBody.plasma_regime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L172-L172)
**def
Tau.BookIV.ManyBody.plasma_regime :PlasmaRegime**

Equations
- Tau.BookIV.ManyBody.plasma_regime = { }
Instances For

---

### `Tau.BookIV.ManyBody.SuperfluidRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L178-L193)
**structure
Tau.BookIV.ManyBody.SuperfluidRegime :Type**


[IV.D226] The superfluid regime: mu = mu_max (maximal mobility),
nu = 0 a.e. (vanishing vorticity except at isolated quantized vortex
cores), kappa = 0 (incompressible), theta quantized.

Transport is maximally free, rotation is suppressed except at
topological defects with integer winding number.

- maximal_mobility : Bool
Maximal mobility.

- vorticity_vanishes_ae : Bool
Vorticity vanishes (except at cores).

- incompressible : Bool
Incompressible.

- theta_quantized : Bool
Theta quantized at vortex cores.

Instances For

---

### `Tau.BookIV.ManyBody.instReprSuperfluidRegime.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L193-L193)
**def
Tau.BookIV.ManyBody.instReprSuperfluidRegime.repr :SuperfluidRegime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprSuperfluidRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L193-L193)
**instance
Tau.BookIV.ManyBody.instReprSuperfluidRegime :Repr SuperfluidRegime**

Equations
- Tau.BookIV.ManyBody.instReprSuperfluidRegime = { reprPrec := Tau.BookIV.ManyBody.instReprSuperfluidRegime.repr }

---

### `Tau.BookIV.ManyBody.superfluid_regime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L195-L195)
**def
Tau.BookIV.ManyBody.superfluid_regime :SuperfluidRegime**

Equations
- Tau.BookIV.ManyBody.superfluid_regime = { }
Instances For

---

### `Tau.BookIV.ManyBody.SuperfluidVortexQuantization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L201-L213)
**structure
Tau.BookIV.ManyBody.SuperfluidVortexQuantization :Type**


[IV.P137] In the superfluid regime every vortex core carries
theta_core in Z \ {0}, and the total circulation around any loop
enclosing k cores is 2*pi*hbar_tau/m times the sum of winding numbers.

Quantization is structural (from pi_1(T^2) = Z^2), not imposed.

- charge_nonzero_integer : Bool
Vortex charge is nonzero integer.

- circulation_quantized : Bool
Circulation quantized.

- structural_origin : String
Structural origin: pi_1(T^2).

Instances For

---

### `Tau.BookIV.ManyBody.instReprSuperfluidVortexQuantization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L213-L213)
**instance
Tau.BookIV.ManyBody.instReprSuperfluidVortexQuantization :Repr SuperfluidVortexQuantization**

Equations
- Tau.BookIV.ManyBody.instReprSuperfluidVortexQuantization = { reprPrec := Tau.BookIV.ManyBody.instReprSuperfluidVortexQuantization.repr }

---

### `Tau.BookIV.ManyBody.instReprSuperfluidVortexQuantization.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L213-L213)
**def
Tau.BookIV.ManyBody.instReprSuperfluidVortexQuantization.repr :SuperfluidVortexQuantization → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.superfluid_vortex_quant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L215-L215)
**def
Tau.BookIV.ManyBody.superfluid_vortex_quant :SuperfluidVortexQuantization**

Equations
- Tau.BookIV.ManyBody.superfluid_vortex_quant = { }
Instances For

---

### `Tau.BookIV.ManyBody.remark_helium4`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L217-L221)
**def
Tau.BookIV.ManyBody.remark_helium4 :String**


[IV.R163] In orthodox physics, superfluid He-4 has quantized
circulation h/m_{He}. In Category tau the quantization is structural:
it follows from the integer-valued topological charge on T^2.
Equations
- Tau.BookIV.ManyBody.remark_helium4 = "He-4: h/m_He quantization; in tau: structural from Z-valued theta on T^2"
Instances For

---

### `Tau.BookIV.ManyBody.SuperconductorRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L227-L240)
**structure
Tau.BookIV.ManyBody.SuperconductorRegime :Type**


[IV.D227] The superconductor regime: B-sector mobility mu_B = mu_max,
theta in Z (quantized), and magnetic flux is quantized in units
of Phi_0 = h/(2e). The Meissner effect (flux expulsion) follows
from the B-sector superfluid structure.

- b_sector_maximal : Bool
B-sector maximal mobility.

- theta_quantized : Bool
Topological charge quantized.

- flux_quantized : Bool
Magnetic flux quantized.

- meissner : Bool
Meissner effect from B-sector superfluid.

Instances For

---

### `Tau.BookIV.ManyBody.instReprSuperconductorRegime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L240-L240)
**instance
Tau.BookIV.ManyBody.instReprSuperconductorRegime :Repr SuperconductorRegime**

Equations
- Tau.BookIV.ManyBody.instReprSuperconductorRegime = { reprPrec := Tau.BookIV.ManyBody.instReprSuperconductorRegime.repr }

---

### `Tau.BookIV.ManyBody.instReprSuperconductorRegime.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L240-L240)
**def
Tau.BookIV.ManyBody.instReprSuperconductorRegime.repr :SuperconductorRegime → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.superconductor_regime`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L242-L242)
**def
Tau.BookIV.ManyBody.superconductor_regime :SuperconductorRegime**

Equations
- Tau.BookIV.ManyBody.superconductor_regime = { }
Instances For

---

### `Tau.BookIV.ManyBody.FluxQuantization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L248-L260)
**structure
Tau.BookIV.ManyBody.FluxQuantization :Type**


[IV.P138] Flux quantization from topological charge: in the superconductor
regime, the integrality of theta on T^2 implies magnetic flux through
any closed surface is quantized: Phi = n * Phi_0, n in Z.

This is the structural origin of the Abrikosov vortex lattice.

- quantized : Bool
Flux = n * Phi_0.

- origin : String
Origin: theta integrality on T^2.

- abrikosov : Bool
Consequence: Abrikosov vortex lattice.

Instances For

---

### `Tau.BookIV.ManyBody.instReprFluxQuantization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L260-L260)
**instance
Tau.BookIV.ManyBody.instReprFluxQuantization :Repr FluxQuantization**

Equations
- Tau.BookIV.ManyBody.instReprFluxQuantization = { reprPrec := Tau.BookIV.ManyBody.instReprFluxQuantization.repr }

---

### `Tau.BookIV.ManyBody.instReprFluxQuantization.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L260-L260)
**def
Tau.BookIV.ManyBody.instReprFluxQuantization.repr :FluxQuantization → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.flux_quantization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L262-L262)
**def
Tau.BookIV.ManyBody.flux_quantization :FluxQuantization**

Equations
- Tau.BookIV.ManyBody.flux_quantization = { }
Instances For

---

### `Tau.BookIV.ManyBody.remark_cooper_pairing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L264-L268)
**def
Tau.BookIV.ManyBody.remark_cooper_pairing :String**


[IV.R164] Cooper pairing is topological: two electron defect bundles
with opposite momentum share a combined T^2 character with even
winding number, forming a bosonic composite.
Equations
- Tau.BookIV.ManyBody.remark_cooper_pairing = "Cooper pairs: opposite momentum, combined even theta, bosonic composite"
Instances For

---

### `Tau.BookIV.ManyBody.TemperatureAsDefectGradient`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L278-L288)
**structure
Tau.BookIV.ManyBody.TemperatureAsDefectGradient :Type**


[IV.D228] The tau-temperature T_tau(C) = d deltaomega / d S_def(C)
is the gradient of the universal defect functional with respect to
defect entropy. It is a structural quantity, not an empirical postulate.

- definition : String
Definition: gradient of delta w.r.t. S_def.

- structural : Bool
Structural (not empirical).

- nonneg : Bool
Non-negative (mobility >= 0 implies T_tau >= 0).

Instances For

---

### `Tau.BookIV.ManyBody.instReprTemperatureAsDefectGradient`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L288-L288)
**instance
Tau.BookIV.ManyBody.instReprTemperatureAsDefectGradient :Repr TemperatureAsDefectGradient**

Equations
- Tau.BookIV.ManyBody.instReprTemperatureAsDefectGradient = { reprPrec := Tau.BookIV.ManyBody.instReprTemperatureAsDefectGradient.repr }

---

### `Tau.BookIV.ManyBody.instReprTemperatureAsDefectGradient.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L288-L288)
**def
Tau.BookIV.ManyBody.instReprTemperatureAsDefectGradient.repr :TemperatureAsDefectGradient → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.temperature_defect_gradient`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L290-L290)
**def
Tau.BookIV.ManyBody.temperature_defect_gradient :TemperatureAsDefectGradient**

Equations
- Tau.BookIV.ManyBody.temperature_defect_gradient = { }
Instances For

---

### `Tau.BookIV.ManyBody.BoltzmannConstantStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L299-L309)
**structure
Tau.BookIV.ManyBody.BoltzmannConstantStatus :Type**


[IV.P139] The Boltzmann constant k_B is an SI conversion factor,
not an ontic tau-constant. It converts dimensionless tau-temperature
to kelvin. In the tau-framework temperature is already dimensionless.

- is_conversion_factor : Bool
k_B is a conversion factor.

- not_ontic : Bool
Not an ontic constant.

- tau_temp_dimensionless : Bool
tau-temperature is dimensionless.

Instances For

---

### `Tau.BookIV.ManyBody.instReprBoltzmannConstantStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L309-L309)
**instance
Tau.BookIV.ManyBody.instReprBoltzmannConstantStatus :Repr BoltzmannConstantStatus**

Equations
- Tau.BookIV.ManyBody.instReprBoltzmannConstantStatus = { reprPrec := Tau.BookIV.ManyBody.instReprBoltzmannConstantStatus.repr }

---

### `Tau.BookIV.ManyBody.instReprBoltzmannConstantStatus.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L309-L309)
**def
Tau.BookIV.ManyBody.instReprBoltzmannConstantStatus.repr :BoltzmannConstantStatus → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.boltzmann_status`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L311-L311)
**def
Tau.BookIV.ManyBody.boltzmann_status :BoltzmannConstantStatus**

Equations
- Tau.BookIV.ManyBody.boltzmann_status = { }
Instances For

---

### `Tau.BookIV.ManyBody.boltzmann_is_conversion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L313-L314)
**theorem
Tau.BookIV.ManyBody.boltzmann_is_conversion :boltzmann_status.is_conversion_factor = true**


---

### `Tau.BookIV.ManyBody.SecondLawViaDefect`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L323-L338)
**structure
Tau.BookIV.ManyBody.SecondLawViaDefect :Type**


[IV.T91] Second law via defect functional: under propagation
Phi_{n,n+1}, defect entropy S_def is non-increasing, refinement
entropy S_ref is non-decreasing, and total entropy S = S_def + S_ref
is non-decreasing. This is the structural second law of thermodynamics.

The arrow of time is the direction of increasing S_ref.

- s_def_nonincreasing : Bool
S_def non-increasing.

- s_ref_nondecreasing : Bool
S_ref non-decreasing.

- s_total_nondecreasing : Bool
S_total = S_def + S_ref non-decreasing.

- arrow_of_time : String
Arrow of time: direction of increasing S_ref.

Instances For

---

### `Tau.BookIV.ManyBody.instReprSecondLawViaDefect.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L338-L338)
**def
Tau.BookIV.ManyBody.instReprSecondLawViaDefect.repr :SecondLawViaDefect → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprSecondLawViaDefect`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L338-L338)
**instance
Tau.BookIV.ManyBody.instReprSecondLawViaDefect :Repr SecondLawViaDefect**

Equations
- Tau.BookIV.ManyBody.instReprSecondLawViaDefect = { reprPrec := Tau.BookIV.ManyBody.instReprSecondLawViaDefect.repr }

---

### `Tau.BookIV.ManyBody.second_law_defect`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L340-L340)
**def
Tau.BookIV.ManyBody.second_law_defect :SecondLawViaDefect**

Equations
- Tau.BookIV.ManyBody.second_law_defect = { }
Instances For

---

### `Tau.BookIV.ManyBody.second_law_total_nondecreasing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L342-L343)
**theorem
Tau.BookIV.ManyBody.second_law_total_nondecreasing :second_law_defect.s_total_nondecreasing = true**


---

### `Tau.BookIV.ManyBody.FirstOrderTransition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L352-L363)
**structure
Tau.BookIV.ManyBody.FirstOrderTransition :Type**


[IV.D229] A first-order phase transition at defect entropy S_0 is a
discontinuity in the tau-temperature: lim_{S->S_0^-} T_tau(S) is
different from lim_{S->S_0^+} T_tau(S). The defect tuple jumps
discontinuously across a regime boundary.

- temp_discontinuous : Bool
Temperature discontinuity.

- tuple_jumps : Bool
Defect tuple jumps.

- has_latent_heat : Bool
Latent heat = jump magnitude.

Instances For

---

### `Tau.BookIV.ManyBody.instReprFirstOrderTransition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L363-L363)
**def
Tau.BookIV.ManyBody.instReprFirstOrderTransition.repr :FirstOrderTransition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprFirstOrderTransition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L363-L363)
**instance
Tau.BookIV.ManyBody.instReprFirstOrderTransition :Repr FirstOrderTransition**

Equations
- Tau.BookIV.ManyBody.instReprFirstOrderTransition = { reprPrec := Tau.BookIV.ManyBody.instReprFirstOrderTransition.repr }

---

### `Tau.BookIV.ManyBody.first_order_transition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L365-L365)
**def
Tau.BookIV.ManyBody.first_order_transition :FirstOrderTransition**

Equations
- Tau.BookIV.ManyBody.first_order_transition = { }
Instances For

---

### `Tau.BookIV.ManyBody.SecondOrderTransition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L367-L377)
**structure
Tau.BookIV.ManyBody.SecondOrderTransition :Type**


[IV.D230] A second-order (continuous) phase transition at S_0 is a
point where T_tau is continuous but dT_tau/dS_def is discontinuous.
The defect tuple is continuous but its derivative jumps.

- temp_continuous : Bool
Temperature continuous.

- deriv_discontinuous : Bool
Temperature derivative discontinuous.

- no_latent_heat : Bool
No latent heat.

Instances For

---

### `Tau.BookIV.ManyBody.instReprSecondOrderTransition.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L377-L377)
**def
Tau.BookIV.ManyBody.instReprSecondOrderTransition.repr :SecondOrderTransition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprSecondOrderTransition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L377-L377)
**instance
Tau.BookIV.ManyBody.instReprSecondOrderTransition :Repr SecondOrderTransition**

Equations
- Tau.BookIV.ManyBody.instReprSecondOrderTransition = { reprPrec := Tau.BookIV.ManyBody.instReprSecondOrderTransition.repr }

---

### `Tau.BookIV.ManyBody.second_order_transition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L379-L379)
**def
Tau.BookIV.ManyBody.second_order_transition :SecondOrderTransition**

Equations
- Tau.BookIV.ManyBody.second_order_transition = { }
Instances For

---

### `Tau.BookIV.ManyBody.PhaseTransitionRegimeCrossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L381-L396)
**structure
Tau.BookIV.ManyBody.PhaseTransitionRegimeCrossing :Type**


[IV.T92] Every phase transition is an inequality crossing in D:
first-order transitions correspond to the defect tuple jumping
discontinuously from one regime to another, second-order transitions
to the tuple arriving at a regime boundary continuously.

There are no "exotic" phase transitions outside this classification.

- first_order_discontinuous : Bool
First-order: discontinuous crossing.

- second_order_continuous : Bool
Second-order: continuous crossing.

- complete_classification : Bool
No exotic transitions outside classification.

- all_are_regime_crossings : Bool
All transitions are regime crossings in D.

Instances For

---

### `Tau.BookIV.ManyBody.instReprPhaseTransitionRegimeCrossing.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L396-L396)
**def
Tau.BookIV.ManyBody.instReprPhaseTransitionRegimeCrossing.repr :PhaseTransitionRegimeCrossing → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprPhaseTransitionRegimeCrossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L396-L396)
**instance
Tau.BookIV.ManyBody.instReprPhaseTransitionRegimeCrossing :Repr PhaseTransitionRegimeCrossing**

Equations
- Tau.BookIV.ManyBody.instReprPhaseTransitionRegimeCrossing = { reprPrec := Tau.BookIV.ManyBody.instReprPhaseTransitionRegimeCrossing.repr }

---

### `Tau.BookIV.ManyBody.phase_transition_crossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L398-L398)
**def
Tau.BookIV.ManyBody.phase_transition_crossing :PhaseTransitionRegimeCrossing**

Equations
- Tau.BookIV.ManyBody.phase_transition_crossing = { }
Instances For

---

### `Tau.BookIV.ManyBody.all_transitions_are_crossings`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L400-L401)
**theorem
Tau.BookIV.ManyBody.all_transitions_are_crossings :phase_transition_crossing.all_are_regime_crossings = true**


---

### `Tau.BookIV.ManyBody.remark_universality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L403-L409)
**def
Tau.BookIV.ManyBody.remark_universality :String**


[IV.R169] (Conjectural) Universality and critical exponents:
Critical exponents of Landau-Ginzburg/Wilson-Fisher theory are
readout-level quantities determined by the defect-tuple geometry
near the regime boundary. Scope: conjectural.
Equations
- Tau.BookIV.ManyBody.remark_universality = "[conjectural] Critical exponents from defect-tuple geometry near " ++ "regime boundaries; readout-level, not ontic"
Instances For
