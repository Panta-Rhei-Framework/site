---
layout: taulib-doc
title: "TauLib.BookI.Denotation.SolenoidPitch"
permalink: /verify/taulib/docs/book-i-denotation-solenoid-pitch/
lane: verify
module_name: "TauLib.BookI.Denotation.SolenoidPitch"
book: "I"
book_label: "Foundations"
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
    book: "Book I"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.Denotation.SolenoidPitch


The solenoid pitch theorem: c_τ = dπ/dα = 1.

## Registry Cross-References


- [IV.T34'] Solenoid Pitch — `c_tau_eq_one`

- [I.D08+] Depth Synchronization — `depth_sync`


## Mathematical Content


The solenoid pitch c_τ = dπ/dα measures the advance rate of π-orbits
relative to α-orbits along the base τ¹. This module proves c_τ = 1
from three already-established results:

- 
**RT_rho_comm** (RankTransfer.lean): For every non-ω generator g,
RT g (n+1) = ρ(RT g n). One ρ-step advances every orbit by exactly 1.


- 
**RT_sigma** (RankTransfer.lean): Cross-orbit transport σ_{g,h}
preserves depth: σ ∘ RT_g = RT_h. All orbits share the same
depth arithmetic.


- 
**rigidity_non_omega** (Rigidity.lean): Aut(τ) = {id} on non-ω
objects. No reparametrization freedom exists to rescale the
α-to-π advance ratio.


Together these force:

dπ/dρ = 1, dα/dρ = 1 ⟹ c_τ = dπ/dα = (dπ/dρ)/(dα/dρ) = 1/1 = 1.

The combinatorial advance ratio is 1 (this module). The bridge to
the physical wave equation uses j² = +1 (I.T10, BipolarAlgebra.lean):
the split-complex unit forces hyperbolic (wave-type) transport whose
null speed in these coordinates equals the solenoid pitch.

## Proof Chain (5 links)


Step
Content
Source


1
ρ sole iterator, successor
K4_no_jump


2
RT commutes with ρ
RT_rho_comm


3
σ preserves depth
RT_sigma


4
Aut(τ) = {id} (rigidity)
rigidity_non_omega


5
j² = +1 → wave eq → null = 1
split_complex_forced


Steps 1–4 are formalized in this module and its dependencies.
Step 5 is the physical bridge (see BipolarAlgebra.lean, PhotonMode.lean).

---

### `Tau.Denotation.depth_sync`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/SolenoidPitch.lean#L62-L69)
**theorem
Tau.Denotation.depth_sync
(g h : Kernel.Generator)

(n : TauIdx)
 :(RT g n).depth = (RT h n).depth**


**Depth synchronization**: For any two non-ω generators g and h,
RT_g(n) and RT_h(n) have the same depth. In other words, ρ advances
all orbit rays at exactly the same rate.

This is the structural content of "all clocks tick at the same rate."

---

### `Tau.Denotation.depth_sync_sigma`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/SolenoidPitch.lean#L71-L77)
**theorem
Tau.Denotation.depth_sync_sigma
(g h : Kernel.Generator)

(hgh : g ≠ h)

(n : TauIdx)
 :(sigma g h (RT g n)).depth = (RT g n).depth**


Depth synchronization via σ: cross-orbit transport σ_{g,h} maps
RT_g(n) to RT_h(n), preserving depth. Combines RT_sigma with the
observation that both rank transfers produce the same depth.

---

### `Tau.Denotation.pitch_ratio_one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/SolenoidPitch.lean#L83-L92)
**theorem
Tau.Denotation.pitch_ratio_one
(n : TauIdx)
 :(RT Kernel.Generator.alpha n).depth = (RT Kernel.Generator.pi n).depth**


**Pitch ratio one**: RT_α(n) and RT_π(n) have the same depth for all n.
This is the α-to-π advance ratio = 1:

dπ/dα = (dπ/dρ)/(dα/dρ) = 1/1 = 1.

Each ρ-step advances α by 1 (K4_no_jump for α) and π by 1
(K4_no_jump for π). The ratio is unity.

---

### `Tau.Denotation.alpha_advance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/SolenoidPitch.lean#L94-L97)
**theorem
Tau.Denotation.alpha_advance
(n : TauIdx)
 :(RT Kernel.Generator.alpha (n + 1)).depth = (RT Kernel.Generator.alpha n).depth + 1**


The advance of α under ρ is exactly 1.

---

### `Tau.Denotation.pi_advance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/SolenoidPitch.lean#L99-L102)
**theorem
Tau.Denotation.pi_advance
(n : TauIdx)
 :(RT Kernel.Generator.pi (n + 1)).depth = (RT Kernel.Generator.pi n).depth + 1**


The advance of π under ρ is exactly 1.

---

### `Tau.Denotation.advance_ratio_eq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/SolenoidPitch.lean#L104-L108)
**theorem
Tau.Denotation.advance_ratio_eq
(n : TauIdx)
 :(RT Kernel.Generator.alpha (n + 1)).depth - (RT Kernel.Generator.alpha n).depth = (RT Kernel.Generator.pi (n + 1)).depth - (RT Kernel.Generator.pi n).depth**


The advances are equal: α and π gain the same depth per ρ-step.

---

### `Tau.Denotation.c_tau_eq_one`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/SolenoidPitch.lean#L114-L140)
**theorem
Tau.Denotation.c_tau_eq_one :(∀ (n : TauIdx), (RT Kernel.Generator.alpha n).depth = (RT Kernel.Generator.pi n).depth) ∧ ∀ (φ : Orbit.TauAutomorphism) (g : Kernel.Generator),
 g ≠ Kernel.Generator.omega →
 (φ.toFun { seed := g, depth := 0 }).seed = g →
 ∀ (n : Nat), φ.toFun { seed := g, depth := n } = { seed := g, depth := n }**


**c_τ = 1 (Solenoid Pitch Theorem).**

The solenoid pitch c_τ = dπ/dα equals 1. Encoded as:
for all n, the depth of RT_α(n) equals the depth of RT_π(n),
AND neither orbit can be reparametrized (Aut(τ) = {id}).

**Proof:**


- depth_sync gives RT_α(n).depth = RT_π(n).depth = n for all n.

- rigidity_non_omega eliminates any automorphism that could
rescale one orbit relative to the other.

- Therefore the advance ratio dπ/dα = 1 is a structural invariant,
not a gauge artifact.


**Physical bridge (not formalized here):**
Step 5 of the proof chain uses j² = +1 (I.T10) to show that the
split-complex structure forces a hyperbolic (wave-type) transport
equation whose null speed in these coordinates equals the solenoid
pitch = 1. See BipolarAlgebra.lean for j² = +1.

---

### `Tau.Denotation.universal_depth_sync`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/SolenoidPitch.lean#L146-L151)
**theorem
Tau.Denotation.universal_depth_sync
(g h : Kernel.Generator)

(_hg : g ≠ Kernel.Generator.omega)

(_hh : h ≠ Kernel.Generator.omega)

(n : TauIdx)
 :(RT g n).depth = (RT h n).depth**


All four non-ω generators advance at the same rate under ρ.
This extends depth_sync to the full generator set.

---

### `Tau.Denotation.four_orbit_sync`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Denotation/SolenoidPitch.lean#L153-L160)
**theorem
Tau.Denotation.four_orbit_sync
(n : TauIdx)
 :(RT Kernel.Generator.alpha n).depth = n ∧ (RT Kernel.Generator.pi n).depth = n ∧ (RT Kernel.Generator.gamma n).depth = n ∧ (RT Kernel.Generator.eta n).depth = n**


All four non-ω orbits have the same depth at every stage.
Stated explicitly for α, π, γ, η.
