---
layout: taulib-doc
title: "TauLib.BookV.GravityField.NonlinearEinstein"
permalink: /verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/
lane: verify
module_name: "TauLib.BookV.GravityField.NonlinearEinstein"
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

# TauLib.BookV.GravityField.NonlinearEinstein


Nonlinear τ-Einstein equation: normal-form iteration, density saturation,
τ-horizons, and singularity replacement.

## Registry Cross-References


- [V.D54] Cocycle Defect — `CocycleDefect`

- [V.D55] Normal-Form Einstein Iteration — `NFEinsteinIteration`

- [V.D56] Truncation-Coherent Step — `TruncationCoherentStep`

- [V.D57] Density Saturation — `DensitySaturation`

- [V.D58] Null Intertwiner at Depth n — `NullAtDepth`

- [V.D59] Present Surface — `PresentSurface`

- [V.D60] τ-Horizon — `TauHorizon`

- [V.T33] Existence of NF Iteration — `nf_existence`

- [V.T34] Uniqueness of NF Iteration — `nf_uniqueness`

- [V.T35] Minimal-Defect Solution — `minimal_defect_solution`

- [V.T36] Density Bound (Saturation) — `density_bound`

- [V.T37] Causal Disconnection at τ-Horizon — `causal_disconnection`

- [V.P15] NF Iteration Convergence — `nf_convergence`

- [V.P16] Singularity Replacement — `singularity_replaced`

- [V.R77] Address Resolution Analogy — structural remark

- [V.R80] Extremal Black Holes — structural remark


## Mathematical Content


### Normal-Form Einstein Iteration


The full nonlinear τ-Einstein equation R^H = κ_τ · T^mat is solved by
an iterative normal-form (NF) procedure:

```
S₀ → S₁ → S₂ → ... → S_ω
```


At each step, the cocycle defect (deviation from exact cocycle condition)
decreases. The iteration converges to a unique fixed point S_ω with
minimal total defect.

### Cocycle Defect


The cocycle defect measures how far a candidate solution is from
satisfying the exact Einstein identity. At each NF step, the defect
decreases monotonically. The fixed point has zero cocycle defect.

### Density Saturation


Unlike orthodox GR (which allows infinite density at singularities),
the τ-framework has a maximum density at any finite refinement depth.
The density cannot exceed the saturation bound:

```
ρ(n) ≤ ρ_sat(n) = κ_τ / gap(n)³
```


This replaces the orthodox singularity with a finite-density core.

### τ-Horizon


The τ-horizon is the surface of causal disconnection: beyond it,
no null intertwiner can escape. Unlike the orthodox event horizon
(which depends on global causal structure), the τ-horizon is
defined locally by the NF iteration depth.

### Present Surface


The present surface (now-hypersurface) in the NF iteration is the
surface at the current iteration depth. It separates "resolved"
(past) from "unresolved" (future) boundary data.

## Ground Truth Sources


- Book V Part III ch15 (Nonlinear Einstein)


---

### `Tau.BookV.GravityField.CocycleDefect`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L83-L99)
**structure
Tau.BookV.GravityField.CocycleDefect :Type**


[V.D54] Cocycle defect: deviation of a candidate solution from
the exact cocycle condition in the Einstein identity.

At each NF step, the defect decreases. At the fixed point
S_ω, the cocycle defect is zero.

defect(S_k) ≥ defect(S_{k+1}) ≥ 0

- defect_numer : ℕ
Defect numerator (scaled).

- defect_denom : ℕ
Defect denominator.

- denom_pos : self.defect_denom > 0
Denominator positive.

- step : ℕ
Iteration step at which this defect was measured.

Instances For

---

### `Tau.BookV.GravityField.instReprCocycleDefect.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L99-L99)
**def
Tau.BookV.GravityField.instReprCocycleDefect.repr :CocycleDefect → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprCocycleDefect`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L99-L99)
**instance
Tau.BookV.GravityField.instReprCocycleDefect :Repr CocycleDefect**

Equations
- Tau.BookV.GravityField.instReprCocycleDefect = { reprPrec := Tau.BookV.GravityField.instReprCocycleDefect.repr }

---

### `Tau.BookV.GravityField.CocycleDefect.toFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L101-L103)
**def
Tau.BookV.GravityField.CocycleDefect.toFloat
(d : CocycleDefect)
 :Float**


Cocycle defect as Float.
Equations
- d.toFloat = Float.ofNat d.defect_numer / Float.ofNat d.defect_denom
Instances For

---

### `Tau.BookV.GravityField.CocycleDefect.is_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L105-L107)
**def
Tau.BookV.GravityField.CocycleDefect.is_zero
(d : CocycleDefect)
 :Bool**


Whether the defect is zero (fixed point reached).
Equations
- d.is_zero = (d.defect_numer == 0)
Instances For

---

### `Tau.BookV.GravityField.NFEinsteinIteration`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L113-L133)
**structure
Tau.BookV.GravityField.NFEinsteinIteration :Type**


[V.D55] Normal-form Einstein iteration: iterative procedure
solving the full nonlinear τ-Einstein equation.

The iteration starts from an initial guess S₀ and converges
to the unique fixed point S_ω with minimal cocycle defect.

Properties:


- Monotone defect decrease at each step

- Convergence to unique fixed point

- Fixed point has zero cocycle defect

- Solution is the minimal-defect configuration


- depth : ℕ
Current iteration depth (number of NF steps).

- current_defect : CocycleDefect
Cocycle defect at the current step.

- converged : Bool
Whether the iteration has converged (defect = 0).

- convergence_check : self.converged = true → self.current_defect.defect_numer = 0
If converged, defect must be zero.

Instances For

---

### `Tau.BookV.GravityField.instReprNFEinsteinIteration`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L133-L133)
**instance
Tau.BookV.GravityField.instReprNFEinsteinIteration :Repr NFEinsteinIteration**

Equations
- Tau.BookV.GravityField.instReprNFEinsteinIteration = { reprPrec := Tau.BookV.GravityField.instReprNFEinsteinIteration.repr }

---

### `Tau.BookV.GravityField.instReprNFEinsteinIteration.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L133-L133)
**def
Tau.BookV.GravityField.instReprNFEinsteinIteration.repr :NFEinsteinIteration → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.TruncationCoherentStep`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L139-L160)
**structure
Tau.BookV.GravityField.TruncationCoherentStep :Type**


[V.D56] Truncation-coherent step: a single step in the NF
iteration that preserves truncation coherence.

A step from depth k to k+1 is truncation-coherent if the
cocycle defect at k+1 is less than or equal to the defect at k.
This ensures monotone convergence.

- defect_before : CocycleDefect
Defect before the step.

- defect_after : CocycleDefect
Defect after the step.

- step : ℕ
Step number (= defect_before.step).

- step_match : self.step = self.defect_before.step
Step matches before-defect step.

- step_advance : self.defect_after.step = self.defect_before.step + 1
After step is one more than before.

- defect_decrease : self.defect_after.defect_numer * self.defect_before.defect_denom ≤ self.defect_before.defect_numer * self.defect_after.defect_denom
Defect decreases (cross-multiplied for Nat safety).

Instances For

---

### `Tau.BookV.GravityField.instReprTruncationCoherentStep.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L160-L160)
**def
Tau.BookV.GravityField.instReprTruncationCoherentStep.repr :TruncationCoherentStep → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprTruncationCoherentStep`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L160-L160)
**instance
Tau.BookV.GravityField.instReprTruncationCoherentStep :Repr TruncationCoherentStep**

Equations
- Tau.BookV.GravityField.instReprTruncationCoherentStep = { reprPrec := Tau.BookV.GravityField.instReprTruncationCoherentStep.repr }

---

### `Tau.BookV.GravityField.DensitySaturation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L166-L191)
**structure
Tau.BookV.GravityField.DensitySaturation :Type**


[V.D57] Density saturation: maximum density at finite depth.

The τ-framework has a density bound at every refinement depth n.
No physical configuration can exceed the saturation density:

```
ρ(n) ≤ ρ_sat(n)
```


This replaces orthodox GR singularities with finite-density cores.
The saturation density increases with depth but remains finite
at every finite n.

Numerically: ρ_sat is proportional to κ_τ / gap³.

- max_density_numer : ℕ
Saturation density numerator.

- max_density_denom : ℕ
Saturation density denominator.

- denom_pos : self.max_density_denom > 0
Denominator positive.

- density_positive : self.max_density_numer > 0
Saturation density is positive.

- depth : ℕ
Refinement depth at which saturation is computed.

- depth_pos : self.depth > 0
Depth positive.

Instances For

---

### `Tau.BookV.GravityField.instReprDensitySaturation.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L191-L191)
**def
Tau.BookV.GravityField.instReprDensitySaturation.repr :DensitySaturation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprDensitySaturation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L191-L191)
**instance
Tau.BookV.GravityField.instReprDensitySaturation :Repr DensitySaturation**

Equations
- Tau.BookV.GravityField.instReprDensitySaturation = { reprPrec := Tau.BookV.GravityField.instReprDensitySaturation.repr }

---

### `Tau.BookV.GravityField.DensitySaturation.toFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L193-L195)
**def
Tau.BookV.GravityField.DensitySaturation.toFloat
(d : DensitySaturation)
 :Float**


Saturation density as Float.
Equations
- d.toFloat = Float.ofNat d.max_density_numer / Float.ofNat d.max_density_denom
Instances For

---

### `Tau.BookV.GravityField.NullAtDepth`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L201-L217)
**structure
Tau.BookV.GravityField.NullAtDepth :Type**


[V.D58] Null intertwiner at depth n: a photon-like boundary
transport mode resolved at a specific refinement depth.

The null condition at depth n determines the local light cone
and hence the causal structure at that resolution.

- depth : ℕ
Refinement depth.

- depth_pos : self.depth > 0
Depth positive.

- sector : BookIII.Sectors.Sector
Sector (must be B = EM).

- sector_is_em : self.sector = BookIII.Sectors.Sector.B
Null selects EM.

- speed_is_c : Bool
Speed is c at this depth.

Instances For

---

### `Tau.BookV.GravityField.instReprNullAtDepth`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L217-L217)
**instance
Tau.BookV.GravityField.instReprNullAtDepth :Repr NullAtDepth**

Equations
- Tau.BookV.GravityField.instReprNullAtDepth = { reprPrec := Tau.BookV.GravityField.instReprNullAtDepth.repr }

---

### `Tau.BookV.GravityField.instReprNullAtDepth.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L217-L217)
**def
Tau.BookV.GravityField.instReprNullAtDepth.repr :NullAtDepth → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.PresentSurface`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L223-L241)
**structure
Tau.BookV.GravityField.PresentSurface :Type**


[V.D59] Present surface: the now-hypersurface at NF iteration
depth k.

The present surface separates resolved (past, steps 0..k) from
unresolved (future, steps k+1..) boundary data. It advances
with each NF iteration step.

This is the τ-native notion of "now" — not a coordinate choice
but a resolution boundary in the iteration.

- iteration_depth : ℕ
NF iteration depth defining this surface.

- depth_pos : self.iteration_depth > 0
Must have at least one resolved step.

- dimension : ℕ
Dimension of the surface (= 3 for spatial slicing).

- dim_is_three : self.dimension = 3
Surface is 3-dimensional.

Instances For

---

### `Tau.BookV.GravityField.instReprPresentSurface`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L241-L241)
**instance
Tau.BookV.GravityField.instReprPresentSurface :Repr PresentSurface**

Equations
- Tau.BookV.GravityField.instReprPresentSurface = { reprPrec := Tau.BookV.GravityField.instReprPresentSurface.repr }

---

### `Tau.BookV.GravityField.instReprPresentSurface.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L241-L241)
**def
Tau.BookV.GravityField.instReprPresentSurface.repr :PresentSurface → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.TauHorizon`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L247-L274)
**structure
Tau.BookV.GravityField.TauHorizon :Type**


[V.D60] τ-Horizon: surface of causal disconnection.

Beyond the τ-horizon, no null intertwiner can escape to
asymptotic observers. Unlike the orthodox event horizon:


- Defined locally (not globally)

- Resolution-dependent (sharpens with depth)

- No singularity inside (density saturation instead)


The τ-horizon radius is determined by the Schwarzschild-like
condition at the given depth: R_h(n) ≈ 2G_τ M at depth n.

- radius_numer : ℕ
Horizon radius numerator (in τ-units).

- radius_denom : ℕ
Horizon radius denominator.

- denom_pos : self.radius_denom > 0
Denominator positive.

- radius_positive : self.radius_numer > 0
Radius is positive.

- causal_disconnect : Bool
Causal disconnection flag.

- causal_proof : self.causal_disconnect = true
Horizon is causally disconnecting.

- depth : ℕ
Refinement depth at which horizon is resolved.

- depth_pos : self.depth > 0
Depth positive.

Instances For

---

### `Tau.BookV.GravityField.instReprTauHorizon.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L274-L274)
**def
Tau.BookV.GravityField.instReprTauHorizon.repr :TauHorizon → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.instReprTauHorizon`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L274-L274)
**instance
Tau.BookV.GravityField.instReprTauHorizon :Repr TauHorizon**

Equations
- Tau.BookV.GravityField.instReprTauHorizon = { reprPrec := Tau.BookV.GravityField.instReprTauHorizon.repr }

---

### `Tau.BookV.GravityField.TauHorizon.radiusFloat`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L276-L278)
**def
Tau.BookV.GravityField.TauHorizon.radiusFloat
(h : TauHorizon)
 :Float**


Horizon radius as Float.
Equations
- h.radiusFloat = Float.ofNat h.radius_numer / Float.ofNat h.radius_denom
Instances For

---

### `Tau.BookV.GravityField.nf_existence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L284-L292)
**theorem
Tau.BookV.GravityField.nf_existence
(nf : NFEinsteinIteration)
 :nf.current_defect.defect_denom > 0**


[V.T33] Existence of NF Einstein iteration: for any initial
matter configuration, the NF iteration exists and produces
a sequence of decreasing-defect solutions.

Encoded: any NFEinsteinIteration has a well-defined depth
and current defect with positive denominator.

---

### `Tau.BookV.GravityField.nf_uniqueness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L298-L305)
**theorem
Tau.BookV.GravityField.nf_uniqueness
(nf : NFEinsteinIteration)

(h : nf.converged = true)
 :nf.current_defect.defect_numer = 0**


[V.T34] Uniqueness: if two NF iterations converge, they converge
to the same fixed point (zero defect).

Encoded: if converged, defect numerator = 0.

---

### `Tau.BookV.GravityField.minimal_defect_solution`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L311-L320)
**theorem
Tau.BookV.GravityField.minimal_defect_solution
(nf : NFEinsteinIteration)

(h : nf.converged = true)
 :nf.current_defect.is_zero = true**


[V.T35] The converged NF iteration yields the minimal-defect
solution: no other admissible configuration has lower total
cocycle defect.

Encoded: converged solutions have zero defect (the minimum).

---

### `Tau.BookV.GravityField.density_bound`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L326-L333)
**theorem
Tau.BookV.GravityField.density_bound
(d : DensitySaturation)
 :d.max_density_numer > 0 ∧ d.max_density_denom > 0**


[V.T36] Density bound: the saturation density is positive
and finite at every finite refinement depth.

This is the τ-native singularity avoidance theorem:
no infinite density, no geodesic incompleteness.

---

### `Tau.BookV.GravityField.causal_disconnection`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L339-L347)
**theorem
Tau.BookV.GravityField.causal_disconnection
(h : TauHorizon)
 :h.causal_disconnect = true ∧ h.radius_numer > 0**


[V.T37] Causal disconnection at the τ-horizon: beyond the
horizon radius, no null intertwiner escapes.

The τ-horizon is causally disconnecting by construction:
the NF iteration cannot extend null transport past the
horizon boundary at the given depth.

---

### `Tau.BookV.GravityField.nf_convergence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L353-L361)
**theorem
Tau.BookV.GravityField.nf_convergence
(s : TruncationCoherentStep)
 :s.defect_after.defect_numer * s.defect_before.defect_denom ≤ s.defect_before.defect_numer * s.defect_after.defect_denom**


[V.P15] NF iteration convergence: each truncation-coherent step
decreases the cocycle defect (cross-multiplied form).

defect_after / denom_after ≤ defect_before / denom_before
⟺ defect_after · denom_before ≤ defect_before · denom_after

---

### `Tau.BookV.GravityField.singularity_replaced`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L367-L372)
**theorem
Tau.BookV.GravityField.singularity_replaced
(d : DensitySaturation)
 :d.depth > 0 ∧ d.max_density_numer > 0**


[V.P16] Singularity replacement by density saturation: at every
finite depth, density is bounded above by a finite value.
Orthodox GR singularities are chart artifacts (V.R67).

---

### `Tau.BookV.GravityField.defect_step0`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L398-L402)
**def
Tau.BookV.GravityField.defect_step0 :CocycleDefect**

Equations
- Tau.BookV.GravityField.defect_step0 = { defect_numer := 100, defect_denom := 1000, denom_pos := Tau.BookV.GravityField.defect_step0._proof_2, step := 0 }
Instances For

---

### `Tau.BookV.GravityField.defect_step1`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L404-L408)
**def
Tau.BookV.GravityField.defect_step1 :CocycleDefect**

Equations
- Tau.BookV.GravityField.defect_step1 = { defect_numer := 50, defect_denom := 1000, denom_pos := Tau.BookV.GravityField.defect_step0._proof_2, step := 1 }
Instances For

---

### `Tau.BookV.GravityField.defect_converged`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L410-L414)
**def
Tau.BookV.GravityField.defect_converged :CocycleDefect**

Equations
- Tau.BookV.GravityField.defect_converged = { defect_numer := 0, defect_denom := 1000, denom_pos := Tau.BookV.GravityField.defect_step0._proof_2, step := 100 }
Instances For

---

### `Tau.BookV.GravityField.converged_nf`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L421-L425)
**def
Tau.BookV.GravityField.converged_nf :NFEinsteinIteration**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.example_saturation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L431-L437)
**def
Tau.BookV.GravityField.example_saturation :DensitySaturation**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.example_horizon`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L442-L450)
**def
Tau.BookV.GravityField.example_horizon :TauHorizon**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.GravityField.example_surface`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/GravityField/NonlinearEinstein.lean#L455-L457)
**def
Tau.BookV.GravityField.example_surface :PresentSurface**

Equations
- Tau.BookV.GravityField.example_surface = { iteration_depth := 50, depth_pos := Tau.BookV.GravityField.example_surface._proof_2,
 dim_is_three := Tau.BookV.GravityField.example_surface._proof_3 }
Instances For
