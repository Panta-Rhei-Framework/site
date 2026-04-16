---
layout: taulib-doc
title: "TauLib.BookV.Temporal.MacroReadout"
permalink: /verify/taulib/docs/book-v-temporal-macro-readout/
lane: verify
module_name: "TauLib.BookV.Temporal.MacroReadout"
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

# TauLib.BookV.Temporal.MacroReadout


Macroscopic readouts: null intertwiners, operational distance, redshift,
expansion, and the Hubble parameter.

## Registry Cross-References


- [V.D27] Null Intertwiner — `NullIntertwiner`

- [V.T14] Boundary Supports Null — `boundary_supports_null`

- [V.P06] Null Selects EM — `null_selects_em`

- [V.D28] Operational Distance — `OperationalDistance`

- [V.T15] Distance-Time Duality — `distance_time_dual`

- [V.D29] Refinement Drift — `RefinementDrift`

- [V.T16] Refinement Drift Formula — `drift_formula_positive`

- [V.D30] Readout Expansion — `ReadoutExpansion`

- [V.D31] Hubble Readout Parameter — `HubbleReadout`


## Ground Truth Sources


- Book V Part II (2nd Edition): Temporal Foundation


---

### `Tau.BookV.Temporal.NullIntertwiner`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L36-L52)
**structure
Tau.BookV.Temporal.NullIntertwiner :Type**


[V.D27] Null intertwiner: massless morphism in boundary holonomy.
Null transport moves along base τ¹ at c_τ. Sector B (EM) is
uniquely selected by the null (zero fiber stiffness) condition.

- sector : BookIII.Sectors.Sector
The sector supporting this null intertwiner.

- null_is_em : self.sector = BookIII.Sectors.Sector.B
Null selects EM.

- carrier : BookIV.Physics.CarrierType
The carrier type (always Base for null transport).

- carrier_is_base : self.carrier = BookIV.Physics.CarrierType.Base
Null transport is base-only.

- massless : Bool
Massless flag.

- massless_true : self.massless = true
Must be massless.

Instances For

---

### `Tau.BookV.Temporal.instReprNullIntertwiner.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L52-L52)
**def
Tau.BookV.Temporal.instReprNullIntertwiner.repr :NullIntertwiner → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.instReprNullIntertwiner`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L52-L52)
**instance
Tau.BookV.Temporal.instReprNullIntertwiner :Repr NullIntertwiner**

Equations
- Tau.BookV.Temporal.instReprNullIntertwiner = { reprPrec := Tau.BookV.Temporal.instReprNullIntertwiner.repr }

---

### `Tau.BookV.Temporal.photon_null`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L54-L61)
**def
Tau.BookV.Temporal.photon_null :NullIntertwiner**


The photon as canonical null intertwiner.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.boundary_supports_null`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L67-L73)
**theorem
Tau.BookV.Temporal.boundary_supports_null :BookIV.Sectors.em_sector.generator = Kernel.Generator.gamma ∧ BookIV.Sectors.em_sector.depth = 2 ∧ photon_null.sector = BookIII.Sectors.Sector.B**


[V.T14] The boundary holonomy algebra supports null intertwiners.
EM generator gamma at depth 2 allows null transport on τ¹.

---

### `Tau.BookV.Temporal.null_selects_em`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L79-L83)
**theorem
Tau.BookV.Temporal.null_selects_em
(n : NullIntertwiner)
 :n.sector = BookIII.Sectors.Sector.B**


[V.P06] The null condition uniquely selects B-sector (EM).
Only B supports null transport: D/A are depth 1 temporal,
C is confined (χ₋), Omega is massive (crossing).

---

### `Tau.BookV.Temporal.em_unique_null`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L85-L91)
**theorem
Tau.BookV.Temporal.em_unique_null :BookIV.Sectors.em_sector.polarity = BookIV.Sectors.PolaritySign.ChiPlus ∧ BookIV.Sectors.em_sector.depth = 2 ∧ BookIV.Sectors.strong_sector.polarity = BookIV.Sectors.PolaritySign.ChiMinus ∧ BookIV.Sectors.higgs_sector.polarity = BookIV.Sectors.PolaritySign.Crossing**


EM is the unique null carrier among the 5 sectors.

---

### `Tau.BookV.Temporal.OperationalDistance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L97-L108)
**structure
Tau.BookV.Temporal.OperationalDistance :Type**


[V.D28] Operational distance: tick count of the null intertwiner
connecting two events at depth n₀. The τ-native spatial distance
is NOT a primitive metric but a counting readout of null transport.

- ref_depth : ℕ
Reference depth for the measurement.

- ref_depth_pos : self.ref_depth > 0
- dist_numer : ℕ
Distance numerator (tick count * scale).

- dist_denom : ℕ
- denom_pos : self.dist_denom > 0
Instances For

---

### `Tau.BookV.Temporal.instReprOperationalDistance`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L108-L108)
**instance
Tau.BookV.Temporal.instReprOperationalDistance :Repr OperationalDistance**

Equations
- Tau.BookV.Temporal.instReprOperationalDistance = { reprPrec := Tau.BookV.Temporal.instReprOperationalDistance.repr }

---

### `Tau.BookV.Temporal.instReprOperationalDistance.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L108-L108)
**def
Tau.BookV.Temporal.instReprOperationalDistance.repr :OperationalDistance → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.OperationalDistance.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L110-L112)
**def
Tau.BookV.Temporal.OperationalDistance.toFloat
(d : OperationalDistance)
 :Float**


Distance as Float.
Equations
- d.toFloat = Float.ofNat d.dist_numer / Float.ofNat d.dist_denom
Instances For

---

### `Tau.BookV.Temporal.distance_time_dual`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L118-L125)
**theorem
Tau.BookV.Temporal.distance_time_dual :canonical_base_circle.seed = Kernel.Generator.alpha ∧ photon_null.sector = BookIII.Sectors.Sector.B ∧ canonical_base_circle.profinite.seed = Kernel.Generator.alpha**


[V.T15] Distance and proper time are dual readouts.
Time counts α-ticks along base; distance counts null-intertwiner
ticks between events. Both derived from the refinement tower.

---

### `Tau.BookV.Temporal.RefinementDrift`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L131-L142)
**structure
Tau.BookV.Temporal.RefinementDrift :Type**


[V.D29] Refinement drift (cosmological redshift):
z(n_s, n_r) := Δt(n_s)/Δt(n_r) − 1. Since Δt(n) ~ ι<sub>τ</sub>^n
and ι<sub>τ</sub> < 1, source earlier (n_s < n_r) gives z > 0 (redshift).
The τ-framework predicts redshift WITHOUT metric expansion.

- n_source : ℕ
- n_receiver : ℕ
- source_pos : self.n_source > 0
- receiver_pos : self.n_receiver > 0
- source_earlier : self.n_source < self.n_receiver
Source precedes receiver (cosmological redshift).

Instances For

---

### `Tau.BookV.Temporal.instReprRefinementDrift`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L142-L142)
**instance
Tau.BookV.Temporal.instReprRefinementDrift :Repr RefinementDrift**

Equations
- Tau.BookV.Temporal.instReprRefinementDrift = { reprPrec := Tau.BookV.Temporal.instReprRefinementDrift.repr }

---

### `Tau.BookV.Temporal.instReprRefinementDrift.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L142-L142)
**def
Tau.BookV.Temporal.instReprRefinementDrift.repr :RefinementDrift → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.RefinementDrift.depth_diff`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L144-L146)
**def
Tau.BookV.Temporal.RefinementDrift.depth_diff
(d : RefinementDrift)
 :ℕ**


Depth difference (positive for redshift).
Equations
- d.depth_diff = d.n_receiver - d.n_source
Instances For

---

### `Tau.BookV.Temporal.drift_formula_positive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L152-L157)
**theorem
Tau.BookV.Temporal.drift_formula_positive
(d : RefinementDrift)
 :d.depth_diff > 0**


[V.T16] Drift depth difference is positive for cosmological
observations (source earlier than receiver).

---

### `Tau.BookV.Temporal.ReadoutExpansion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L163-L172)
**structure
Tau.BookV.Temporal.ReadoutExpansion :Type**


[V.D30] Readout expansion a(n) ~ ι<sub>τ</sub>^(-n): cumulative proper-time
scaling. The universe "expands" because the tower deepens and
proper-time increments shrink — not because space stretches.

- depth : ℕ
- depth_pos : self.depth > 0
- expansion_numer : ℕ
- expansion_denom : ℕ
- denom_pos : self.expansion_denom > 0
Instances For

---

### `Tau.BookV.Temporal.instReprReadoutExpansion.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L172-L172)
**def
Tau.BookV.Temporal.instReprReadoutExpansion.repr :ReadoutExpansion → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.instReprReadoutExpansion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L172-L172)
**instance
Tau.BookV.Temporal.instReprReadoutExpansion :Repr ReadoutExpansion**

Equations
- Tau.BookV.Temporal.instReprReadoutExpansion = { reprPrec := Tau.BookV.Temporal.instReprReadoutExpansion.repr }

---

### `Tau.BookV.Temporal.ReadoutExpansion.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L174-L176)
**def
Tau.BookV.Temporal.ReadoutExpansion.toFloat
(a : ReadoutExpansion)
 :Float**


Expansion as Float.
Equations
- a.toFloat = Float.ofNat a.expansion_numer / Float.ofNat a.expansion_denom
Instances For

---

### `Tau.BookV.Temporal.HubbleReadout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L182-L191)
**structure
Tau.BookV.Temporal.HubbleReadout :Type**


[V.D31] Hubble readout H(n) := Δa/a per tick. NOT constant: decays
with depth. Early (opening) H is large (inflation), late H is small.
H(n) ~ 1 − ι<sub>τ</sub> to leading order.

- depth : ℕ
- depth_pos : self.depth > 0
- hubble_numer : ℕ
- hubble_denom : ℕ
- denom_pos : self.hubble_denom > 0
Instances For

---

### `Tau.BookV.Temporal.instReprHubbleReadout.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L191-L191)
**def
Tau.BookV.Temporal.instReprHubbleReadout.repr :HubbleReadout → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Temporal.instReprHubbleReadout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L191-L191)
**instance
Tau.BookV.Temporal.instReprHubbleReadout :Repr HubbleReadout**

Equations
- Tau.BookV.Temporal.instReprHubbleReadout = { reprPrec := Tau.BookV.Temporal.instReprHubbleReadout.repr }

---

### `Tau.BookV.Temporal.HubbleReadout.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L193-L195)
**def
Tau.BookV.Temporal.HubbleReadout.toFloat
(h : HubbleReadout)
 :Float**


Hubble readout as Float.
Equations
- h.toFloat = Float.ofNat h.hubble_numer / Float.ofNat h.hubble_denom
Instances For

---

### `Tau.BookV.Temporal.null_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L201-L204)
**theorem
Tau.BookV.Temporal.null_structural
(n : NullIntertwiner)
 :n.massless = true ∧ n.carrier = BookIV.Physics.CarrierType.Base**


Null intertwiner is always massless and base-carried.

---

### `Tau.BookV.Temporal.null_transport_scale`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L206-L210)
**theorem
Tau.BookV.Temporal.null_transport_scale :BookIV.Sectors.em_sector.coupling_numer = BookIV.Sectors.iota_sq_numer ∧ BookIV.Sectors.em_sector.coupling_denom = BookIV.Sectors.iota_sq_denom**


The EM sector coupling ι<sub>τ</sub>² is the null-transport scale.

---

### `Tau.BookV.Temporal.redshift_requires_earlier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Temporal/MacroReadout.lean#L212-L214)
**theorem
Tau.BookV.Temporal.redshift_requires_earlier
(d : RefinementDrift)
 :d.n_source < d.n_receiver**


Redshift requires source < receiver.
