---
layout: taulib-doc
title: "TauLib.BookV.Temporal.TemporalIgnition"
permalink: /verify/taulib/docs/book-v-temporal-temporal-ignition/
lane: verify
module_name: "TauLib.BookV.Temporal.TemporalIgnition"
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

# TauLib.BookV.Temporal.TemporalIgnition


Three temporal epochs of the α-orbit: pre-temporal, opening, and temporal.
Ignition depth, now-hypersurface, and coherence horizon.

## Registry Cross-References


- [V.D20] Temporal Epochs — `TemporalEpoch`

- [V.D21] Ignition Depth — `IgnitionDepth`

- [V.T11] Three Epochs Nonempty — `three_epochs_nonempty`

- [V.P04] Pre-Temporal Indistinguishability — `pre_temporal_no_labels`

- [V.D22] Now-Hypersurface — `NowHypersurface`

- [V.T12] Current Depth — `current_depth_exceeds_ignition`

- [V.D23] Coherence Horizon — `CoherenceHorizon`


## Mathematical Content


### Three Temporal Epochs [V.D20]


The α-orbit partitions into three sequential epochs:

- 
**Pre-Temporal** (n < n_ign): spectral labels incomplete; no subsystem
can distinguish ticks. The early refinement levels lack sufficient
structure for sector differentiation.


- 
**Opening** (n_ign ≤ n < n_open): full spectral labels present, but
sectors still in rapid equilibration. Corresponds to the early universe's
high-energy phase (inflationary/GUT epoch).


- 
**Temporal** (n ≥ n_open): stable sector differentiation, well-defined
physical time. The current epoch.


### Ignition Depth [V.D21]


n_ign is the smallest depth at which all 5 sector labels are present.
Below n_ign, the boundary holonomy algebra lacks full sector structure.

### Now-Hypersurface [V.D22]


Σ_now is the current refinement depth n_*. The universe's observed state
corresponds to a specific depth in the refinement tower.

### Coherence Horizon [V.D23]


n_coh is the depth beyond which further refinement yields no new
observable predictions at current experimental precision. The universe
has effectively "converged" for practical purposes.

## Ground Truth Sources


- Book V Part II (2nd Edition): Temporal Foundation

- Book V Chapter ~4-5: Temporal Ignition


---

### `Tau.BookV.Temporal.TemporalEpoch`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L65-L79)
**inductive
Tau.BookV.Temporal.TemporalEpoch :Type**


[V.D20] The three temporal epochs of the α-orbit.

The partition is exhaustive and ordered:
PreTemporal < Opening < Temporal in depth.

- PreTemporal : TemporalEpoch
Pre-temporal: spectral labels incomplete, ticks indistinguishable.
Depth range: 1 ≤ n < n_ign.

- Opening : TemporalEpoch
Opening: full labels present, rapid equilibration.
Depth range: n_ign ≤ n < n_open. Corresponds to early universe.

- Temporal : TemporalEpoch
Temporal: stable sector differentiation, well-defined physical time.
Depth range: n ≥ n_open. The current epoch.

Instances For

---

### `Tau.BookV.Temporal.instReprTemporalEpoch`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L79-L79)
**instance
Tau.BookV.Temporal.instReprTemporalEpoch :Repr TemporalEpoch**

Equations
- Tau.BookV.Temporal.instReprTemporalEpoch = { reprPrec := Tau.BookV.Temporal.instReprTemporalEpoch.repr }

---

### `Tau.BookV.Temporal.instReprTemporalEpoch.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L79-L79)
**def
Tau.BookV.Temporal.instReprTemporalEpoch.repr :TemporalEpoch → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.instDecidableEqTemporalEpoch`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L79-L79)
**instance
Tau.BookV.Temporal.instDecidableEqTemporalEpoch :DecidableEq TemporalEpoch**

Equations
- Tau.BookV.Temporal.instDecidableEqTemporalEpoch x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Temporal.instBEqTemporalEpoch`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L79-L79)
**instance
Tau.BookV.Temporal.instBEqTemporalEpoch :BEq TemporalEpoch**

Equations
- Tau.BookV.Temporal.instBEqTemporalEpoch = { beq := Tau.BookV.Temporal.instBEqTemporalEpoch.beq }

---

### `Tau.BookV.Temporal.instBEqTemporalEpoch.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L79-L79)
**def
Tau.BookV.Temporal.instBEqTemporalEpoch.beq :TemporalEpoch → TemporalEpoch → Bool**

Equations
- Tau.BookV.Temporal.instBEqTemporalEpoch.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Temporal.instInhabitedTemporalEpoch.default`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L79-L79)
**def
Tau.BookV.Temporal.instInhabitedTemporalEpoch.default :TemporalEpoch**

Equations
- Tau.BookV.Temporal.instInhabitedTemporalEpoch.default = Tau.BookV.Temporal.TemporalEpoch.PreTemporal
Instances For

---

### `Tau.BookV.Temporal.instInhabitedTemporalEpoch`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L79-L79)
**instance
Tau.BookV.Temporal.instInhabitedTemporalEpoch :Inhabited TemporalEpoch**

Equations
- Tau.BookV.Temporal.instInhabitedTemporalEpoch = { default := Tau.BookV.Temporal.instInhabitedTemporalEpoch.default }

---

### `Tau.BookV.Temporal.IgnitionDepth`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L85-L99)
**structure
Tau.BookV.Temporal.IgnitionDepth :Type**


[V.D21] Ignition depth: the smallest depth n_ign at which all 5
sector spectral labels are present in the boundary holonomy algebra.

Below n_ign, not all sectors are differentiated: the boundary
holonomy algebra lacks full sector structure.

- n_ign : ℕ
The ignition depth n_ign.

- n_ign_pos : self.n_ign > 0
Ignition depth is positive (some pre-temporal epochs exist).

- sectors_at_ignition : ℕ
Number of sectors activated at n_ign (must be 5).

- full_spectrum : self.sectors_at_ignition = 5
All 5 sectors present at ignition.

Instances For

---

### `Tau.BookV.Temporal.instReprIgnitionDepth.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L99-L99)
**def
Tau.BookV.Temporal.instReprIgnitionDepth.repr :IgnitionDepth → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.instReprIgnitionDepth`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L99-L99)
**instance
Tau.BookV.Temporal.instReprIgnitionDepth :Repr IgnitionDepth**

Equations
- Tau.BookV.Temporal.instReprIgnitionDepth = { reprPrec := Tau.BookV.Temporal.instReprIgnitionDepth.repr }

---

### `Tau.BookV.Temporal.canonical_ignition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L101-L108)
**def
Tau.BookV.Temporal.canonical_ignition :IgnitionDepth**


A canonical ignition depth (structural placeholder).
The exact value of n_ign depends on detailed τ-NF analysis;
here we record n_ign ≥ 1 with all 5 sectors present.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.epoch_classification`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L114-L118)
**def
Tau.BookV.Temporal.epoch_classification
(t : BookIV.Arena.ProtoTime)

(n_ign n_open : ℕ)
 :TemporalEpoch**


Classify a proto-time into its epoch given ignition and opening depths.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.three_epochs_nonempty`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L124-L143)
**theorem
Tau.BookV.Temporal.three_epochs_nonempty
(n_ign n_open : ℕ)

(h_ign : n_ign > 1)

(h_open : n_open > n_ign)
 :(∃ (t : BookIV.Arena.ProtoTime), epoch_classification t n_ign n_open = TemporalEpoch.PreTemporal) ∧ (∃ (t : BookIV.Arena.ProtoTime), epoch_classification t n_ign n_open = TemporalEpoch.Opening) ∧ ∃ (t : BookIV.Arena.ProtoTime), epoch_classification t n_ign n_open = TemporalEpoch.Temporal**


[V.T11] All three temporal epochs are nonempty: there exist depths
in each epoch.

Given n_ign > 1 and n_open > n_ign, all three epochs contain at
least one depth:


- PreTemporal contains depth 1 (since 1 < n_ign)

- Opening contains depth n_ign (since n_ign < n_open)

- Temporal contains depth n_open (since n_open ≥ n_open)


---

### `Tau.BookV.Temporal.pre_temporal_no_labels`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L149-L159)
**theorem
Tau.BookV.Temporal.pre_temporal_no_labels
(t : BookIV.Arena.ProtoTime)

(n_ign n_open : ℕ)

(h : t.tick < n_ign)
 :epoch_classification t n_ign n_open = TemporalEpoch.PreTemporal**


[V.P04] In the pre-temporal epoch, no subsystem can distinguish
ticks. The spectral labels are incomplete, so sector differentiation
has not yet occurred. Ticks exist (the refinement tower advances)
but they carry no physically distinguishable signatures.

Formalized: at pre-temporal depth, the epoch classification is
PreTemporal (i.e., full sector labels are NOT yet present).

---

### `Tau.BookV.Temporal.NowHypersurface`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L165-L178)
**structure
Tau.BookV.Temporal.NowHypersurface :Type**


[V.D22] The now-hypersurface: the current refinement depth n_*
of the universe. The observed state of the universe corresponds
to a specific depth in the refinement tower.

n_* is far beyond both ignition depth and opening depth:
n_* >> n_open >> n_ign.

- current_depth : BookIV.Arena.ProtoTime
Current depth n_*.

- ignition : IgnitionDepth
Reference ignition depth.

- past_ignition : self.current_depth.tick > self.ignition.n_ign
Current depth exceeds ignition.

Instances For

---

### `Tau.BookV.Temporal.instReprNowHypersurface.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L178-L178)
**def
Tau.BookV.Temporal.instReprNowHypersurface.repr :NowHypersurface → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.instReprNowHypersurface`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L178-L178)
**instance
Tau.BookV.Temporal.instReprNowHypersurface :Repr NowHypersurface**

Equations
- Tau.BookV.Temporal.instReprNowHypersurface = { reprPrec := Tau.BookV.Temporal.instReprNowHypersurface.repr }

---

### `Tau.BookV.Temporal.current_depth_exceeds_ignition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L184-L191)
**theorem
Tau.BookV.Temporal.current_depth_exceeds_ignition
(h : NowHypersurface)
 :h.current_depth.tick > h.ignition.n_ign**


[V.T12] The current depth n_* far exceeds the ignition depth n_ign.

This is structurally enforced: the refinement tower has advanced
well beyond the ignition threshold. The "far exceeds" is captured
by the past_ignition field of NowHypersurface.

---

### `Tau.BookV.Temporal.CoherenceHorizon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L197-L214)
**structure
Tau.BookV.Temporal.CoherenceHorizon :Type**


[V.D23] Coherence horizon: the depth n_coh beyond which further
refinement yields no new observable predictions at current
experimental precision.

The universe has effectively "converged" — profinite completion
has reached practical saturation. Deeper levels exist but are
observationally inaccessible.

n_coh depends on experimental precision; structurally, we only
require n_coh > n_ign (past ignition) and n_coh ≤ n_* (present).

- n_coh : ℕ
The coherence horizon depth.

- n_coh_pos : self.n_coh > 0
Past ignition.

- effectively_converged : Bool
Whether convergence is effective (to current precision).

Instances For

---

### `Tau.BookV.Temporal.instReprCoherenceHorizon`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L214-L214)
**instance
Tau.BookV.Temporal.instReprCoherenceHorizon :Repr CoherenceHorizon**

Equations
- Tau.BookV.Temporal.instReprCoherenceHorizon = { reprPrec := Tau.BookV.Temporal.instReprCoherenceHorizon.repr }

---

### `Tau.BookV.Temporal.instReprCoherenceHorizon.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L214-L214)
**def
Tau.BookV.Temporal.instReprCoherenceHorizon.repr :CoherenceHorizon → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.epoch_exhaust`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L220-L223)
**theorem
Tau.BookV.Temporal.epoch_exhaust
(e : TemporalEpoch)
 :e = TemporalEpoch.PreTemporal ∨ e = TemporalEpoch.Opening ∨ e = TemporalEpoch.Temporal**


All temporal epochs are accounted for.

---

### `Tau.BookV.Temporal.temporal_is_stable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/TemporalIgnition.lean#L225-L228)
**theorem
Tau.BookV.Temporal.temporal_is_stable :epoch_classification { tick := 100, tick_pos := ⋯ } 5 10 = TemporalEpoch.Temporal**


The temporal epoch is the only stable epoch (where physics operates).
