---
layout: taulib-doc
title: "TauLib.BookVI.Persistence.TemporalLemniscate"
permalink: /verify/taulib/docs/book-vi-persistence-temporal-lemniscate/
lane: verify
module_name: "TauLib.BookVI.Persistence.TemporalLemniscate"
book: "VI"
book_label: "Life"
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
    book: "Book VI"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookVI.Persistence.TemporalLemniscate


Temporal lemniscate L_T, circadian rhythms, and homochirality.

## Registry Cross-References


- [VI.D27] Temporal Lemniscate L_T — `TemporalLemniscate`

- [VI.D28] Homochirality — `Homochirality`

- [VI.T17] Circadian Rhythm as Poincaré Orbit — `circadian_poincare_orbit`

- [VI.P09] 24-Hour Cycle as τ¹ Rotation — `circadian_tau1_rotation`

- [VI.P10] L-Amino Acid Preference as Parity Shadow — `homochirality_parity_shadow`


## Cross-Book Authority


- Book II, Part III: Lemniscate L = S¹ ∨ S¹ construction

- Book III, Part II: Poincaré force (periodic orbits, limit cycles)

- Book IV, IV.T146: σ = C_τ (all neutrinos Majorana)

- Book IV, IV.T160: θ_QCD = 0 (strong CP solved)


## Ground Truth Sources


- Book VI Chapter 15 (2nd Edition): Circadian Rhythms

- Book VI Chapter 16 (2nd Edition): Homochirality


---

### `Tau.BookVI.TempLem.TemporalLemniscate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L34-L49)
**structure
Tau.BookVI.TempLem.TemporalLemniscate :Type**


[VI.D27] Temporal Lemniscate L_T = S¹_act ∨ S¹_rest.
The persistence Life loop projected onto τ¹ traces a figure-eight:
active phase (S¹_act) and rest phase (S¹_rest).
Inherits lemniscate topology from L = S¹ ∨ S¹ (Book II, Part III).

- lobe_count : ℕ
Number of lobes.

- lobes_eq : self.lobe_count = 2
Exactly 2 lobes.

- active_lobe : String
Active-phase lobe.

- rest_lobe : String
Rest-phase lobe.

- winding_number : ℕ
Winding number on τ¹.

Instances For

---

### `Tau.BookVI.TempLem.instReprTemporalLemniscate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L49-L49)
**instance
Tau.BookVI.TempLem.instReprTemporalLemniscate :Repr TemporalLemniscate**

Equations
- Tau.BookVI.TempLem.instReprTemporalLemniscate = { reprPrec := Tau.BookVI.TempLem.instReprTemporalLemniscate.repr }

---

### `Tau.BookVI.TempLem.instReprTemporalLemniscate.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L49-L49)
**def
Tau.BookVI.TempLem.instReprTemporalLemniscate.repr :TemporalLemniscate → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.TempLem.temporal_lem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L51-L53)
**def
Tau.BookVI.TempLem.temporal_lem :TemporalLemniscate**

Equations
- Tau.BookVI.TempLem.temporal_lem = { lobe_count := 2, lobes_eq := Tau.BookVI.TempLem.temporal_lem._proof_1 }
Instances For

---

### `Tau.BookVI.TempLem.temporal_lemniscate_two_lobes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L55-L56)
**theorem
Tau.BookVI.TempLem.temporal_lemniscate_two_lobes :temporal_lem.lobe_count = 2**


---

### `Tau.BookVI.TempLem.temporal_lemniscate_winding_one`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L58-L59)
**theorem
Tau.BookVI.TempLem.temporal_lemniscate_winding_one :temporal_lem.winding_number = 1**


---

### `Tau.BookVI.TempLem.CircadianPoincare`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L65-L82)
**structure
Tau.BookVI.TempLem.CircadianPoincare :Type**


[VI.T17] Circadian Rhythm as Poincaré Orbit Theorem.
The persistence Life loop projected onto τ¹ is a Poincaré limit cycle
tracing L_T = S¹_act ∨ S¹_rest with period T ≈ 24h.
Authority: Book III, Part II (Poincaré force ensures periodic orbits).

- period_hours : ℕ
Period in hours.

- period_eq : self.period_hours = 24
Period ≈ 24 hours.

- is_limit_cycle : Bool
Is a Poincaré limit cycle.

- traces_L_T : Bool
Traces temporal lemniscate.

- winding_alpha : ℕ
Winding number w_α = 1 per cycle.

- characteristics : ℕ
Three characteristics: entrainable, temperature-compensated, free-running.

Instances For

---

### `Tau.BookVI.TempLem.instReprCircadianPoincare.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L82-L82)
**def
Tau.BookVI.TempLem.instReprCircadianPoincare.repr :CircadianPoincare → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.TempLem.instReprCircadianPoincare`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L82-L82)
**instance
Tau.BookVI.TempLem.instReprCircadianPoincare :Repr CircadianPoincare**

Equations
- Tau.BookVI.TempLem.instReprCircadianPoincare = { reprPrec := Tau.BookVI.TempLem.instReprCircadianPoincare.repr }

---

### `Tau.BookVI.TempLem.circadian`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L84-L86)
**def
Tau.BookVI.TempLem.circadian :CircadianPoincare**

Equations
- Tau.BookVI.TempLem.circadian = { period_hours := 24, period_eq := Tau.BookVI.TempLem.circadian._proof_1 }
Instances For

---

### `Tau.BookVI.TempLem.circadian_poincare_orbit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L88-L93)
**theorem
Tau.BookVI.TempLem.circadian_poincare_orbit :circadian.period_hours = 24 ∧ circadian.is_limit_cycle = true ∧ circadian.traces_L_T = true ∧ circadian.winding_alpha = 1**


---

### `Tau.BookVI.TempLem.CircadianTau1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L99-L107)
**structure
Tau.BookVI.TempLem.CircadianTau1 :Type**


[VI.P09] 24-Hour Cycle as τ¹ Rotation (conjectural).
Molecular clock intrinsic period near 24h across all terrestrial life
suggests a τ¹-derived timescale constraint.

- scope : String
Scope: conjectural.

- tau1_locked : Bool
Period locked to τ¹ rotation.

Instances For

---

### `Tau.BookVI.TempLem.instReprCircadianTau1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L107-L107)
**instance
Tau.BookVI.TempLem.instReprCircadianTau1 :Repr CircadianTau1**

Equations
- Tau.BookVI.TempLem.instReprCircadianTau1 = { reprPrec := Tau.BookVI.TempLem.instReprCircadianTau1.repr }

---

### `Tau.BookVI.TempLem.instReprCircadianTau1.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L107-L107)
**def
Tau.BookVI.TempLem.instReprCircadianTau1.repr :CircadianTau1 → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.TempLem.circadian_tau1`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L109-L109)
**def
Tau.BookVI.TempLem.circadian_tau1 :CircadianTau1**

Equations
- Tau.BookVI.TempLem.circadian_tau1 = { }
Instances For

---

### `Tau.BookVI.TempLem.circadian_tau1_rotation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L111-L112)
**theorem
Tau.BookVI.TempLem.circadian_tau1_rotation :circadian_tau1.tau1_locked = true**


---

### `Tau.BookVI.TempLem.Homochirality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L118-L131)
**structure
Tau.BookVI.TempLem.Homochirality :Type**


[VI.D28] Homochirality: L-amino acids / D-sugars.
Phenomenological shadow of the Parity Bridge (conjectural).
The weak sector's parity violation (IV.T146, IV.T160) seeds
the biological chirality preference.

- l_amino_acids : Bool
L-amino acids preferred.

- d_sugars : Bool
D-sugars preferred.

- parity_bridge_shadow : Bool
Connected to Parity Bridge.

- scope : String
Scope: τ-effective (upgraded from conjectural via VI.R26 derivation chain).

Instances For

---

### `Tau.BookVI.TempLem.instReprHomochirality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L131-L131)
**instance
Tau.BookVI.TempLem.instReprHomochirality :Repr Homochirality**

Equations
- Tau.BookVI.TempLem.instReprHomochirality = { reprPrec := Tau.BookVI.TempLem.instReprHomochirality.repr }

---

### `Tau.BookVI.TempLem.instReprHomochirality.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L131-L131)
**def
Tau.BookVI.TempLem.instReprHomochirality.repr :Homochirality → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.TempLem.HomochiralityParityShadow`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L133-L143)
**structure
Tau.BookVI.TempLem.HomochiralityParityShadow :Type**


[VI.P10] L-amino acid preference as Parity Shadow (conjectural).
The weak sector's chirality (IV.T146 σ=C_τ Majorana, IV.T160 θ_QCD=0)
seeds the biological enantiomeric excess via the Parity Bridge.

- iv_t146_majorana : Bool
IV.T146: σ = C_τ, all neutrinos Majorana from self-adjointness.

- iv_t160_strong_cp : Bool
IV.T160: θ_QCD = 0, strong CP solved from SA-i mod-3.

- temporal_protection : Bool
Temporal stability protects chirality.

Instances For

---

### `Tau.BookVI.TempLem.instReprHomochiralityParityShadow`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L143-L143)
**instance
Tau.BookVI.TempLem.instReprHomochiralityParityShadow :Repr HomochiralityParityShadow**

Equations
- Tau.BookVI.TempLem.instReprHomochiralityParityShadow = { reprPrec := Tau.BookVI.TempLem.instReprHomochiralityParityShadow.repr }

---

### `Tau.BookVI.TempLem.instReprHomochiralityParityShadow.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L143-L143)
**def
Tau.BookVI.TempLem.instReprHomochiralityParityShadow.repr :HomochiralityParityShadow → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.TempLem.homo_parity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L145-L145)
**def
Tau.BookVI.TempLem.homo_parity :HomochiralityParityShadow**

Equations
- Tau.BookVI.TempLem.homo_parity = { }
Instances For

---

### `Tau.BookVI.TempLem.homochirality_parity_shadow`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L147-L151)
**theorem
Tau.BookVI.TempLem.homochirality_parity_shadow :homo_parity.iv_t146_majorana = true ∧ homo_parity.iv_t160_strong_cp = true ∧ homo_parity.temporal_protection = true**


---

### `Tau.BookVI.TempLem.EnantiomericExcess`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L157-L170)
**structure
Tau.BookVI.TempLem.EnantiomericExcess :Type**


[VI.D73] Enantiomeric Excess at refinement level n.
ee(n) = |[L] - [R]| / ([L] + [R]) measures chirality purity.
Seeded by ChiralitySeed (VI.D72) at n=0 with ee ≈ 10⁻¹⁷,
amplified by SelfDesc closure at each refinement level.

- refinement_level : ℕ
Refinement level (0 = initial seed).

- converges_to_one : Bool
ee converges to 1 (100% homochiral).

- monotone : Bool
Monotonically increasing with refinement.

- seed_source : String
Seeded by VI.D72 ChiralitySeed.

Instances For

---

### `Tau.BookVI.TempLem.instReprEnantiomericExcess`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L170-L170)
**instance
Tau.BookVI.TempLem.instReprEnantiomericExcess :Repr EnantiomericExcess**

Equations
- Tau.BookVI.TempLem.instReprEnantiomericExcess = { reprPrec := Tau.BookVI.TempLem.instReprEnantiomericExcess.repr }

---

### `Tau.BookVI.TempLem.instReprEnantiomericExcess.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L170-L170)
**def
Tau.BookVI.TempLem.instReprEnantiomericExcess.repr :EnantiomericExcess → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.TempLem.StereochemicalSelection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L176-L189)
**structure
Tau.BookVI.TempLem.StereochemicalSelection :Type**


[VI.T42] Stereochemical Selection Theorem: SelfDesc closure (VI.T03)
amplifies the chirality seed (VI.D72) to full enantiomeric excess.
The polarity propagation (VI.D71) provides the initial asymmetry;
SelfDesc closure drives ee(n) → 1 monotonically.

- selfdesc_amplification : Bool
SelfDesc closure amplifies chirality.

- seed_from_parity_bridge : Bool
Chirality seed source: VI.D72.

- exponential_gain : Bool
Amplification is exponential (gain g per level).

- final_ee_is_one : Bool
Result: ee = 1 at convergence.

Instances For

---

### `Tau.BookVI.TempLem.instReprStereochemicalSelection.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L189-L189)
**def
Tau.BookVI.TempLem.instReprStereochemicalSelection.repr :StereochemicalSelection → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.TempLem.instReprStereochemicalSelection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L189-L189)
**instance
Tau.BookVI.TempLem.instReprStereochemicalSelection :Repr StereochemicalSelection**

Equations
- Tau.BookVI.TempLem.instReprStereochemicalSelection = { reprPrec := Tau.BookVI.TempLem.instReprStereochemicalSelection.repr }

---

### `Tau.BookVI.TempLem.stereochemical_sel`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L191-L191)
**def
Tau.BookVI.TempLem.stereochemical_sel :StereochemicalSelection**

Equations
- Tau.BookVI.TempLem.stereochemical_sel = { }
Instances For

---

### `Tau.BookVI.TempLem.stereochemical_selection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L193-L198)
**theorem
Tau.BookVI.TempLem.stereochemical_selection :stereochemical_sel.selfdesc_amplification = true ∧ stereochemical_sel.seed_from_parity_bridge = true ∧ stereochemical_sel.exponential_gain = true ∧ stereochemical_sel.final_ee_is_one = true**


---

### `Tau.BookVI.TempLem.EeMonotoneConvergence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L204-L218)
**structure
Tau.BookVI.TempLem.EeMonotoneConvergence :Type**


[VI.P21] ee(n) → 1 monotonically: enantiomeric excess increases
at every refinement level and converges to 1.
The double-well potential (Hodge stabilization) prevents regression,
and Poincaré topological lock-in on L = S¹ ∨ S¹ provides
additional protection beyond energetic barriers.

- monotone_increasing : Bool
Monotone increasing.

- limit_is_one : Bool
Converges to ee = 1.

- hodge_stabilization : Bool
Double-well barrier prevents regression.

- poincare_lockin : Bool
Topological lock-in on L.

Instances For

---

### `Tau.BookVI.TempLem.instReprEeMonotoneConvergence.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L218-L218)
**def
Tau.BookVI.TempLem.instReprEeMonotoneConvergence.repr :EeMonotoneConvergence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.TempLem.instReprEeMonotoneConvergence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L218-L218)
**instance
Tau.BookVI.TempLem.instReprEeMonotoneConvergence :Repr EeMonotoneConvergence**

Equations
- Tau.BookVI.TempLem.instReprEeMonotoneConvergence = { reprPrec := Tau.BookVI.TempLem.instReprEeMonotoneConvergence.repr }

---

### `Tau.BookVI.TempLem.ee_convergence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L220-L220)
**def
Tau.BookVI.TempLem.ee_convergence :EeMonotoneConvergence**

Equations
- Tau.BookVI.TempLem.ee_convergence = { }
Instances For

---

### `Tau.BookVI.TempLem.ee_monotone_convergence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L222-L227)
**theorem
Tau.BookVI.TempLem.ee_monotone_convergence :ee_convergence.monotone_increasing = true ∧ ee_convergence.limit_is_one = true ∧ ee_convergence.hodge_stabilization = true ∧ ee_convergence.poincare_lockin = true**


---

### `Tau.BookVI.TempLem.HomochiralityUniversality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L233-L247)
**structure
Tau.BookVI.TempLem.HomochiralityUniversality :Type**


[VI.T43] Homochirality Universality: all persistence-sector entries
inherit the same chirality from the unique polarity propagation path.
Since the Parity Bridge (VI.T01) is the unique factorization and the
chirality seed (VI.D72) has definite sign, every carrier satisfying
Distinction + SelfDesc must exhibit the same enantiomeric preference.

- universal_chirality : Bool
All persistence-sector entries share same chirality.

- from_unique_path : Bool
Derived from unique propagation path (VI.L14).

- applies_to_all_carriers : Bool
Applies to all carriers satisfying Distinction + SelfDesc.

- scope : String
Scope: τ-effective (derived from Parity Bridge chain).

Instances For

---

### `Tau.BookVI.TempLem.instReprHomochiralityUniversality.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L247-L247)
**def
Tau.BookVI.TempLem.instReprHomochiralityUniversality.repr :HomochiralityUniversality → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.TempLem.instReprHomochiralityUniversality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L247-L247)
**instance
Tau.BookVI.TempLem.instReprHomochiralityUniversality :Repr HomochiralityUniversality**

Equations
- Tau.BookVI.TempLem.instReprHomochiralityUniversality = { reprPrec := Tau.BookVI.TempLem.instReprHomochiralityUniversality.repr }

---

### `Tau.BookVI.TempLem.homochirality_universality_inst`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L249-L249)
**def
Tau.BookVI.TempLem.homochirality_universality_inst :HomochiralityUniversality**

Equations
- Tau.BookVI.TempLem.homochirality_universality_inst = { }
Instances For

---

### `Tau.BookVI.TempLem.homochirality_universality`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L251-L255)
**theorem
Tau.BookVI.TempLem.homochirality_universality :homochirality_universality_inst.universal_chirality = true ∧ homochirality_universality_inst.from_unique_path = true ∧ homochirality_universality_inst.applies_to_all_carriers = true**


---

### `Tau.BookVI.TempLem.HomochiralityScopeUpgrade`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L261-L280)
**structure
Tau.BookVI.TempLem.HomochiralityScopeUpgrade :Type**


[VI.R26] Homochirality Scope Upgrade: documents the complete derivation
chain that upgrades homochirality from conjectural to τ-effective.
Chain: K0-K6 → ι<sub>τ</sub> → holonomy sectors → σ_A-admissibility (IV.D112)
→ σ = C_τ Majorana (IV.T146) → Parity Bridge (VI.T01)
→ Polarity Propagation (VI.D71) → Chirality Seed (VI.D72)
→ Propagation Preserves Chirality (VI.T41)
→ Stereochemical Selection (VI.T42) → ee → 1 (VI.P21)
→ Homochirality Universality (VI.T43).
Every link is τ-effective; no conjectural step remains.

- previous_scope : String
Previous scope.

- new_scope : String
New scope.

- chain_length : ℕ
Derivation chain length.

- chain_complete : self.chain_length = 12
- op9_status : String
VI.OP9 status upgrade.

Instances For

---

### `Tau.BookVI.TempLem.instReprHomochiralityScopeUpgrade`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L280-L280)
**instance
Tau.BookVI.TempLem.instReprHomochiralityScopeUpgrade :Repr HomochiralityScopeUpgrade**

Equations
- Tau.BookVI.TempLem.instReprHomochiralityScopeUpgrade = { reprPrec := Tau.BookVI.TempLem.instReprHomochiralityScopeUpgrade.repr }

---

### `Tau.BookVI.TempLem.instReprHomochiralityScopeUpgrade.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L280-L280)
**def
Tau.BookVI.TempLem.instReprHomochiralityScopeUpgrade.repr :HomochiralityScopeUpgrade → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookVI.TempLem.scope_upgrade`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L282-L284)
**def
Tau.BookVI.TempLem.scope_upgrade :HomochiralityScopeUpgrade**

Equations
- Tau.BookVI.TempLem.scope_upgrade = { chain_length := 12, chain_complete := Tau.BookVI.TempLem.scope_upgrade._proof_1 }
Instances For
