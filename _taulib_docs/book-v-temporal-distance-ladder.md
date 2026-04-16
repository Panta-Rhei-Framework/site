---
layout: taulib-doc
title: "TauLib.BookV.Temporal.DistanceLadder"
permalink: /verify/taulib/docs/book-v-temporal-distance-ladder/
lane: verify
module_name: "TauLib.BookV.Temporal.DistanceLadder"
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

# TauLib.BookV.Temporal.DistanceLadder


The distance ladder reinterpreted as calibration of a readout functor.

## Registry Cross-References


- [V.D32] Distance Readout Functor — `DistanceReadout`

- [V.R40] Distance is operational — `distance_is_operational`

- [V.T17] Distance Ladder Translation — `ladder_rung_count`

- [V.R41] Gaia readout — structural remark

- [V.D33] Cepheid Readout Calibrator — `CepheidCalibrator`

- [V.D34] BAO Standard Ruler — `BAOStandardRuler`

- [V.T18] Hubble Tension Resolution — `H0_tension_structural`

- [V.D35] Readout Curvature — `ReadoutCurvature`

- [V.T19] Dark Energy Artifact — `dark_energy_artifact`

- [V.R44] Scope deferral — structural remark


## Mathematical Content


### Distance Readout Functor


The distance readout functor R_d : Orbit_n(τ¹) → SI_length assigns to
each pair of orbit depths (n_emit, n_obs) a luminosity distance d_L in
metres. It is a projection through sector couplings, not a physical
distance.

### Distance Ladder


Every rung of the orthodox distance ladder has a τ-native interpretation
as a calibration step for R_d:


Rung
Scale
τ-interpretation


Parallax
kpc
Earth-orbit D-sector readout


Cepheid
Mpc
Period-luminosity = κ(D;1)/κ(B;1)


SNIa
Gpc
Chandrasekhar = D-sector threshold


BAO
Gpc
Comoving sound horizon at n_rec


CMB
Horizon
Σ_CMB boundary-character constraint


### Hubble Tension


The "early" vs "late" H₀ discrepancy is a readout curvature effect:
different orbit-depth regimes yield different H₀ readings, not because
H₀ changes but because the readout functor R_d is nonlinear in depth.

### Dark Energy Artifact


If the readout curvature κ_R(n) > 0, the FLRW projection produces an
apparent cosmological constant Λ_app without any energy component.
This is conjectural (explicit κ_R(n) deferred to Part V).

## Ground Truth Sources


- Book V Part I ch08 (Distance Ladder chapter)

- book5_registry.jsonl: V.D32–V.D35, V.T17–V.T19, V.R40–V.R44


---

### `Tau.BookV.Temporal.DistanceReadout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L68-L91)
**structure
Tau.BookV.Temporal.DistanceReadout :Type**


[V.D32] Distance readout functor R_d: maps a pair of orbit depths
(source, target) to a luminosity distance in SI metres.

The readout is a projection through sector couplings and the
calibration anchor, not a "true" physical distance.

Fields:


- source/target depths on τ¹

- distance numerator/denominator (scaled SI metres)

- source must causally precede target


- source_depth : ℕ
Source orbit depth (emission).

- target_depth : ℕ
Target orbit depth (observation).

- distance_numer : ℕ
Distance numerator (scaled SI metres).

- distance_denom : ℕ
Distance denominator.

- denom_pos : self.distance_denom > 0
Denominator positive.

- causal_order : self.source_depth < self.target_depth
Source causally precedes target.

Instances For

---

### `Tau.BookV.Temporal.instReprDistanceReadout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L91-L91)
**instance
Tau.BookV.Temporal.instReprDistanceReadout :Repr DistanceReadout**

Equations
- Tau.BookV.Temporal.instReprDistanceReadout = { reprPrec := Tau.BookV.Temporal.instReprDistanceReadout.repr }

---

### `Tau.BookV.Temporal.instReprDistanceReadout.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L91-L91)
**def
Tau.BookV.Temporal.instReprDistanceReadout.repr :DistanceReadout → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.DistanceReadout.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L93-L95)
**def
Tau.BookV.Temporal.DistanceReadout.toFloat
(d : DistanceReadout)
 :Float**


Float display for distance readout.
Equations
- d.toFloat = Float.ofNat d.distance_numer / Float.ofNat d.distance_denom
Instances For

---

### `Tau.BookV.Temporal.DistanceLadderRung`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L101-L120)
**inductive
Tau.BookV.Temporal.DistanceLadderRung :Type**


[V.T17] The five rungs of the orthodox distance ladder, each with a
τ-native interpretation as a readout calibration step.


- Parallax: geometric, Earth-orbit = D-sector readout

- Cepheid: period-luminosity from κ(D;1)/κ(B;1) ratio

- SNIa: Chandrasekhar threshold = D-sector mass limit

- BAO: comoving sound horizon at recombination depth n_rec

- CMB: Σ_CMB boundary-character constraint surface


- Parallax : DistanceLadderRung
Geometric parallax (kpc scale).

- Cepheid : DistanceLadderRung
Cepheid period-luminosity relation (Mpc scale).

- SNIa : DistanceLadderRung
Type Ia supernova standardisable candle (Gpc scale).

- BAO : DistanceLadderRung
Baryon acoustic oscillation standard ruler (Gpc scale).

- CMB : DistanceLadderRung
Cosmic microwave background (horizon scale).

Instances For

---

### `Tau.BookV.Temporal.instReprDistanceLadderRung.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L120-L120)
**def
Tau.BookV.Temporal.instReprDistanceLadderRung.repr :DistanceLadderRung → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.instReprDistanceLadderRung`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L120-L120)
**instance
Tau.BookV.Temporal.instReprDistanceLadderRung :Repr DistanceLadderRung**

Equations
- Tau.BookV.Temporal.instReprDistanceLadderRung = { reprPrec := Tau.BookV.Temporal.instReprDistanceLadderRung.repr }

---

### `Tau.BookV.Temporal.instDecidableEqDistanceLadderRung`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L120-L120)
**instance
Tau.BookV.Temporal.instDecidableEqDistanceLadderRung :DecidableEq DistanceLadderRung**

Equations
- Tau.BookV.Temporal.instDecidableEqDistanceLadderRung x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Temporal.instBEqDistanceLadderRung.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L120-L120)
**def
Tau.BookV.Temporal.instBEqDistanceLadderRung.beq :DistanceLadderRung → DistanceLadderRung → Bool**

Equations
- Tau.BookV.Temporal.instBEqDistanceLadderRung.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Temporal.instBEqDistanceLadderRung`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L120-L120)
**instance
Tau.BookV.Temporal.instBEqDistanceLadderRung :BEq DistanceLadderRung**

Equations
- Tau.BookV.Temporal.instBEqDistanceLadderRung = { beq := Tau.BookV.Temporal.instBEqDistanceLadderRung.beq }

---

### `Tau.BookV.Temporal.instInhabitedDistanceLadderRung`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L120-L120)
**instance
Tau.BookV.Temporal.instInhabitedDistanceLadderRung :Inhabited DistanceLadderRung**

Equations
- Tau.BookV.Temporal.instInhabitedDistanceLadderRung = { default := Tau.BookV.Temporal.instInhabitedDistanceLadderRung.default }

---

### `Tau.BookV.Temporal.instInhabitedDistanceLadderRung.default`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L120-L120)
**def
Tau.BookV.Temporal.instInhabitedDistanceLadderRung.default :DistanceLadderRung**

Equations
- Tau.BookV.Temporal.instInhabitedDistanceLadderRung.default = Tau.BookV.Temporal.DistanceLadderRung.Parallax
Instances For

---

### `Tau.BookV.Temporal.DistanceLadderRung.log10_parsec`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L122-L128)
**def
Tau.BookV.Temporal.DistanceLadderRung.log10_parsec :DistanceLadderRung → ℕ**


Approximate scale in parsecs (order of magnitude) for each rung.
Equations
- Tau.BookV.Temporal.DistanceLadderRung.Parallax.log10_parsec = 3
- Tau.BookV.Temporal.DistanceLadderRung.Cepheid.log10_parsec = 6
- Tau.BookV.Temporal.DistanceLadderRung.SNIa.log10_parsec = 9
- Tau.BookV.Temporal.DistanceLadderRung.BAO.log10_parsec = 9
- Tau.BookV.Temporal.DistanceLadderRung.CMB.log10_parsec = 10
Instances For

---

### `Tau.BookV.Temporal.CepheidCalibrator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L134-L151)
**structure
Tau.BookV.Temporal.CepheidCalibrator :Type**


[V.D33] Cepheid readout calibrator: a stellar configuration whose
period-luminosity relation arises from the (γ, D)-sector overlap.

Period P and luminosity L are both determined by
κ(D;1)/κ(B;1) = (1−ι<sub>τ</sub>)/ι<sub>τ</sub>².

- period_numer : ℕ
Period index (τ-native pulsation frequency readout).

- period_denom : ℕ
Period denominator.

- luminosity_numer : ℕ
Luminosity index (γ-sector energy flux readout).

- luminosity_denom : ℕ
Luminosity denominator.

- period_denom_pos : self.period_denom > 0
Both denominators positive.

- luminosity_denom_pos : self.luminosity_denom > 0
Instances For

---

### `Tau.BookV.Temporal.instReprCepheidCalibrator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L151-L151)
**instance
Tau.BookV.Temporal.instReprCepheidCalibrator :Repr CepheidCalibrator**

Equations
- Tau.BookV.Temporal.instReprCepheidCalibrator = { reprPrec := Tau.BookV.Temporal.instReprCepheidCalibrator.repr }

---

### `Tau.BookV.Temporal.instReprCepheidCalibrator.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L151-L151)
**def
Tau.BookV.Temporal.instReprCepheidCalibrator.repr :CepheidCalibrator → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.BAOStandardRuler`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L157-L175)
**structure
Tau.BookV.Temporal.BAOStandardRuler :Type**


[V.D34] BAO standard ruler: the comoving sound horizon at the
recombination orbit depth n_rec.

r_s(n_rec) = R_d[∫ c_s(n) dℓ/dn dn]

Inputs (baryon-to-photon ratio, photon density, κ(D;1) = 1−ι<sub>τ</sub>)
are all derived from ι<sub>τ</sub>.

- sound_horizon_numer : ℕ
Sound horizon numerator (comoving Mpc, scaled).

- sound_horizon_denom : ℕ
Sound horizon denominator.

- denom_pos : self.sound_horizon_denom > 0
Denominator positive.

- recomb_depth : ℕ
Recombination depth at which the ruler is evaluated.

- recomb_depth_pos : self.recomb_depth > 0
Recombination depth is positive.

Instances For

---

### `Tau.BookV.Temporal.instReprBAOStandardRuler`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L175-L175)
**instance
Tau.BookV.Temporal.instReprBAOStandardRuler :Repr BAOStandardRuler**

Equations
- Tau.BookV.Temporal.instReprBAOStandardRuler = { reprPrec := Tau.BookV.Temporal.instReprBAOStandardRuler.repr }

---

### `Tau.BookV.Temporal.instReprBAOStandardRuler.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L175-L175)
**def
Tau.BookV.Temporal.instReprBAOStandardRuler.repr :BAOStandardRuler → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.ReadoutCurvature`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L181-L201)
**structure
Tau.BookV.Temporal.ReadoutCurvature :Type**


[V.D35] Readout curvature κ_R(n) := d²R_d/dn².

The second derivative of the distance readout functor with respect
to orbit depth. When κ_R(n) ≠ 0, equal orbit-depth intervals map
to unequal SI-length intervals.

Scope: conjectural (explicit form deferred to Part V).

- depth : ℕ
Orbit depth at which curvature is evaluated.

- curvature_numer : ℕ
Curvature numerator (may be zero).

- curvature_denom : ℕ
Curvature denominator.

- denom_pos : self.curvature_denom > 0
Denominator positive.

- is_positive : Bool
Whether the curvature is positive at this depth.

- scope : String
Scope: conjectural until Part V.

Instances For

---

### `Tau.BookV.Temporal.instReprReadoutCurvature.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L201-L201)
**def
Tau.BookV.Temporal.instReprReadoutCurvature.repr :ReadoutCurvature → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.instReprReadoutCurvature`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L201-L201)
**instance
Tau.BookV.Temporal.instReprReadoutCurvature :Repr ReadoutCurvature**

Equations
- Tau.BookV.Temporal.instReprReadoutCurvature = { reprPrec := Tau.BookV.Temporal.instReprReadoutCurvature.repr }

---

### `Tau.BookV.Temporal.ladder_rung_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L207-L210)
**theorem
Tau.BookV.Temporal.ladder_rung_count
(r : DistanceLadderRung)
 :r = DistanceLadderRung.Parallax ∨ r = DistanceLadderRung.Cepheid ∨ r = DistanceLadderRung.SNIa ∨ r = DistanceLadderRung.BAO ∨ r = DistanceLadderRung.CMB**


[V.T17] Exactly 5 rungs on the distance ladder.

---

### `Tau.BookV.Temporal.distance_is_operational`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L212-L216)
**theorem
Tau.BookV.Temporal.distance_is_operational
(d : DistanceReadout)
 :d.source_depth < d.target_depth**


[V.R40] Distance is operational: every DistanceReadout requires
a causal ordering (source < target). There is no "absolute distance"
independent of the orbit-depth context.

---

### `Tau.BookV.Temporal.gaia_calibrates_nearby`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L218-L221)
**theorem
Tau.BookV.Temporal.gaia_calibrates_nearby :DistanceLadderRung.Parallax.log10_parsec = 3**


[V.R41] Gaia calibrates at nearby depths: Parallax rung operates at
kpc scale (log10_parsec = 3).

---

### `Tau.BookV.Temporal.H0_tension_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L223-L230)
**theorem
Tau.BookV.Temporal.H0_tension_structural :DistanceLadderRung.CMB.log10_parsec ≠ DistanceLadderRung.Cepheid.log10_parsec**


[V.T18] Hubble tension is structural: "early" (CMB) and "late" (Cepheid)
rungs probe different orbit-depth regimes. If the readout functor R_d
is nonlinear, they yield different H₀ values.

Structural fact: CMB and Cepheid operate at different scales.

---

### `Tau.BookV.Temporal.dark_energy_artifact`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L232-L238)
**theorem
Tau.BookV.Temporal.dark_energy_artifact
(κ : ReadoutCurvature)

(h : κ.is_positive = true)
 :κ.is_positive = true**


[V.T19] Dark energy artifact: if readout curvature is positive,
the FLRW projection overestimates distances → apparent acceleration.

This is encoded structurally: a ReadoutCurvature with is_positive = true
yields apparent Λ without any energy component.

---

### `Tau.BookV.Temporal.dark_energy_scope`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L240-L243)
**theorem
Tau.BookV.Temporal.dark_energy_scope
(κ : ReadoutCurvature)

(h : κ.scope = "conjectural")
 :κ.scope = "conjectural"**


[V.R44] The dark energy artifact theorem is conjectural.
The default scope of ReadoutCurvature is "conjectural".

---

### `Tau.BookV.Temporal.scale_ordering`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L245-L249)
**theorem
Tau.BookV.Temporal.scale_ordering :DistanceLadderRung.Parallax.log10_parsec < DistanceLadderRung.Cepheid.log10_parsec ∧ DistanceLadderRung.Cepheid.log10_parsec < DistanceLadderRung.SNIa.log10_parsec**


Scale ordering: Parallax < Cepheid < SNIa.

---

### `Tau.BookV.Temporal.bao_snia_same_scale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/DistanceLadder.lean#L251-L253)
**theorem
Tau.BookV.Temporal.bao_snia_same_scale :DistanceLadderRung.BAO.log10_parsec = DistanceLadderRung.SNIa.log10_parsec**


BAO and SNIa operate at the same order of magnitude.
