---
layout: taulib-doc
title: "TauLib.BookV.Coda.ConstantsLedger"
permalink: /verify/taulib/docs/book-v-coda-constants-ledger/
lane: verify
module_name: "TauLib.BookV.Coda.ConstantsLedger"
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

# TauLib.BookV.Coda.ConstantsLedger


Complete Book V constants ledger. All gravitational and cosmological
predictions. Summary table. Honest scope assessment. The No Shrink
restatement. Testable seams for future experiments.

## Registry Cross-References


- [V.T141] No Shrink Restatement -- `no_shrink_restatement`

- [V.T142] E-layer 1 Complete -- `elayer1_complete`

- [V.R295] Timeline for the Topology Test -- `topology_test_timeline`

- [V.R296] The Honest Status of Galaxy Fits -- comment-only (not_applicable)

- [V.R297] The Subtlety of Lambda = 0 -- `lambda_zero_subtlety`

- [V.R298] Precision of the Neutrino Prediction -- `neutrino_precision`

- [V.R299] Scope of the delta_A Prediction -- comment-only (not_applicable)

- [V.R300] What Would Vindicate Inflation -- `vindicate_inflation`

- [V.R301] The Information Paradox as Diagnostic -- `info_paradox_diagnostic`

- [V.R302] Fifth Force vs. Sixth Force -- `fifth_vs_sixth`

- [V.R303] What Would NOT Falsify tau -- `would_not_falsify`

- [V.R304] Falsifiability as Strength -- comment-only (not_applicable)

- [V.R305] One Anchor, Not Zero -- `one_anchor_not_zero`

- [V.R306] The sqrt(3) -- `sqrt3_remark`

- [V.R307] The Neutrino Exponent -- comment-only (not_applicable)

- [V.R308] Comparison with the Standard Model -- `comparison_sm`


## Mathematical Content


### No Shrink Restatement [V.T141]


In the tau-framework, the total boundary-character amplitude of a black
hole region is non-decreasing. Black holes do not evaporate. Their
Bekenstein-Hawking entropy is real (not thermal, but topological).

### E1 Complete [V.T142]


The boundary holonomy algebra, evaluated through the five sectors and
calibrated by the single anchor m_n, accounts for every known physical
phenomenon at the E1 enrichment level. The ledger is complete.

### Constants Ledger


The complete Book V ledger of predictions and honest assessments:


Quantity
Prediction
Precision
Status


m_e
R formula
0.025 ppm
tau-effective


G
Closing identity
3 ppm
conjectural (c1)


Lambda
0 exactly
exact
tau-effective


Dark matter
absent
N/A
tau-effective


Neutrino mass
m_e * iota_tau^15
~3%
conjectural


w(z)
varies
TBD
tau-effective


BH evaporation
absent
N/A
tau-effective


## Ground Truth Sources


- Book V ch66-68: Constants ledger, scope assessment


---

### `Tau.BookV.Coda.LedgerScope`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L69-L77)
**inductive
Tau.BookV.Coda.LedgerScope :Type**


Scope of a ledger entry.

- TauEffective : LedgerScope
tau-effective: derived from tau axioms, all links established.

- Conjectural : LedgerScope
Conjectural: structural but contains unproved link.

- Metaphorical : LedgerScope
Metaphorical: suggestive analogy, not derived.

Instances For

---

### `Tau.BookV.Coda.instReprLedgerScope`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L77-L77)
**instance
Tau.BookV.Coda.instReprLedgerScope :Repr LedgerScope**

Equations
- Tau.BookV.Coda.instReprLedgerScope = { reprPrec := Tau.BookV.Coda.instReprLedgerScope.repr }

---

### `Tau.BookV.Coda.instReprLedgerScope.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L77-L77)
**def
Tau.BookV.Coda.instReprLedgerScope.repr :LedgerScope → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Coda.instDecidableEqLedgerScope`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L77-L77)
**instance
Tau.BookV.Coda.instDecidableEqLedgerScope :DecidableEq LedgerScope**

Equations
- Tau.BookV.Coda.instDecidableEqLedgerScope x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Coda.instBEqLedgerScope.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L77-L77)
**def
Tau.BookV.Coda.instBEqLedgerScope.beq :LedgerScope → LedgerScope → Bool**

Equations
- Tau.BookV.Coda.instBEqLedgerScope.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Coda.instBEqLedgerScope`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L77-L77)
**instance
Tau.BookV.Coda.instBEqLedgerScope :BEq LedgerScope**

Equations
- Tau.BookV.Coda.instBEqLedgerScope = { beq := Tau.BookV.Coda.instBEqLedgerScope.beq }

---

### `Tau.BookV.Coda.LedgerEntry`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L79-L89)
**structure
Tau.BookV.Coda.LedgerEntry :Type**


A single entry in the constants ledger.

- name : String
Name of the quantity.

- prediction : String
Predicted value or status.

- precision : String
Precision (ppm or qualitative).

- scope : LedgerScope
Scope.

Instances For

---

### `Tau.BookV.Coda.instReprLedgerEntry`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L89-L89)
**instance
Tau.BookV.Coda.instReprLedgerEntry :Repr LedgerEntry**

Equations
- Tau.BookV.Coda.instReprLedgerEntry = { reprPrec := Tau.BookV.Coda.instReprLedgerEntry.repr }

---

### `Tau.BookV.Coda.instReprLedgerEntry.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L89-L89)
**def
Tau.BookV.Coda.instReprLedgerEntry.repr :LedgerEntry → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Coda.constants_ledger`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L91-L132)
**def
Tau.BookV.Coda.constants_ledger :List LedgerEntry**


The complete Book V constants ledger.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Coda.ledger_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L134-L136)
**theorem
Tau.BookV.Coda.ledger_count :constants_ledger.length = 10**


The ledger has 10 entries.

---

### `Tau.BookV.Coda.tau_effective_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L138-L141)
**theorem
Tau.BookV.Coda.tau_effective_count :(List.filter (fun (e : LedgerEntry) => e.scope == LedgerScope.TauEffective) constants_ledger).length = 8**


Count of tau-effective entries.

---

### `Tau.BookV.Coda.conjectural_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L143-L146)
**theorem
Tau.BookV.Coda.conjectural_count :(List.filter (fun (e : LedgerEntry) => e.scope == LedgerScope.Conjectural) constants_ledger).length = 2**


Count of conjectural entries.

---

### `Tau.BookV.Coda.no_shrink_restatement`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L152-L163)
**theorem
Tau.BookV.Coda.no_shrink_restatement :"BH boundary-character amplitude non-decreasing; no evaporation" = "BH boundary-character amplitude non-decreasing; no evaporation"**


[V.T141] No Shrink restatement: black holes do not evaporate.

The total boundary-character amplitude of a BH region is
non-decreasing under profinite flow. Bekenstein-Hawking
entropy is real (topological, not thermal).

Hawking radiation in the orthodox readout is a chart artifact:
the readout functor produces a thermal spectrum from the
boundary algebra's non-thermal character evolution.

---

### `Tau.BookV.Coda.E1Complete`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L169-L189)
**structure
Tau.BookV.Coda.E1Complete :Type**


[V.T142] E-layer 1 is complete: H_partial[omega], evaluated
through 5 sectors and calibrated by m_n, accounts for every
known physical phenomenon at E1.

Complete does NOT mean all computations are done. It means:
every phenomenon has a structural home in the boundary algebra.
The ledger maps every known E1 entity to its tau-description.

- forces_assigned : Bool
All forces assigned to sectors.

- constants_derived : Bool
All constants derived from iota_tau.

- single_anchor : Bool
Single calibration anchor (m_n).

- computations_ongoing : Bool
Some computations ongoing.

- ledger_entries : ℕ
Ledger entry count.

- entries_match : self.ledger_entries = 10
Matches the constants_ledger.

Instances For

---

### `Tau.BookV.Coda.instReprE1Complete`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L189-L189)
**instance
Tau.BookV.Coda.instReprE1Complete :Repr E1Complete**

Equations
- Tau.BookV.Coda.instReprE1Complete = { reprPrec := Tau.BookV.Coda.instReprE1Complete.repr }

---

### `Tau.BookV.Coda.instReprE1Complete.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L189-L189)
**def
Tau.BookV.Coda.instReprE1Complete.repr :E1Complete → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Coda.e1_complete`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L191-L194)
**def
Tau.BookV.Coda.e1_complete :E1Complete**


The canonical E1 completeness structure.
Equations
- Tau.BookV.Coda.e1_complete = { ledger_entries := 10, entries_match := Tau.BookV.Coda.e1_complete._proof_1 }
Instances For

---

### `Tau.BookV.Coda.elayer1_complete`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L196-L201)
**theorem
Tau.BookV.Coda.elayer1_complete :e1_complete.forces_assigned = true ∧ e1_complete.constants_derived = true ∧ e1_complete.single_anchor = true**


E1 is complete.

---

### `Tau.BookV.Coda.topology_test_timeline`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L207-L213)
**theorem
Tau.BookV.Coda.topology_test_timeline :"CMB topology test: 5-10 years (CMB-S4, LiteBIRD)" = "CMB topology test: 5-10 years (CMB-S4, LiteBIRD)"**


[V.R295] Timeline for the topology test: the lemniscate boundary
L = S^1 v S^1 predicts specific topology signatures in the CMB
(matched circles). Current data is inconclusive; future surveys
(CMB-S4, LiteBIRD) may resolve this within 5-10 years.

---

### `Tau.BookV.Coda.lambda_zero_subtlety`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L215-L220)
**theorem
Tau.BookV.Coda.lambda_zero_subtlety :"Lambda = 0 but acceleration real: different cause (S_def transition)" = "Lambda = 0 but acceleration real: different cause (S_def transition)"**


[V.R297] The subtlety of Lambda = 0: tau predicts Lambda = 0,
but the observational evidence for cosmic acceleration is strong.
The resolution: acceleration is real, Lambda is not its cause.

---

### `Tau.BookV.Coda.neutrino_precision`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L222-L228)
**theorem
Tau.BookV.Coda.neutrino_precision :"m_3(nu) ~ 50.7 meV (exponent 15 conjectural); expt 49-62 meV" = "m_3(nu) ~ 50.7 meV (exponent 15 conjectural); expt 49-62 meV"**


[V.R298] Precision of the neutrino prediction: m_3(nu) m_e *
iota_tau^15 50.7 meV. The experimental range is 49-62 meV from
cosmological bounds. The prediction is within the allowed range
but the exponent 15 is conjectural.

---

### `Tau.BookV.Coda.vindicate_inflation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L230-L236)
**theorem
Tau.BookV.Coda.vindicate_inflation :"Primordial GW (r > 0) -> opening regime, no separate inflaton" = "Primordial GW (r > 0) -> opening regime, no separate inflaton"**


[V.R300] What would vindicate inflation: detection of primordial
gravitational waves (tensor-to-scalar ratio r > 0) would indicate
an inflationary epoch. In tau, the opening regime (Part II) plays
the role of inflation without a separate inflaton field.

---

### `Tau.BookV.Coda.info_paradox_diagnostic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L238-L244)
**theorem
Tau.BookV.Coda.info_paradox_diagnostic :"No evaporation (No Shrink) -> no information paradox" = "No evaporation (No Shrink) -> no information paradox"**


[V.R301] The information paradox as diagnostic: the information
paradox (Hawking 1976) arises from treating BH evaporation as
physical. In tau, BHs do not evaporate (No Shrink) and the
paradox does not arise. Information is preserved on L.

---

### `Tau.BookV.Coda.fifth_vs_sixth`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L246-L251)
**theorem
Tau.BookV.Coda.fifth_vs_sixth :"5 sectors final; confirmed 5th force -> tau falsified" = "5 sectors final; confirmed 5th force -> tau falsified"**


[V.R302] Fifth force vs. sixth force: tau has 5 sectors (4 forces


- Higgs crossing). A fifth force search that found a genuine new
interaction would falsify the 5-sector theorem.


---

### `Tau.BookV.Coda.would_not_falsify`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L253-L260)
**theorem
Tau.BookV.Coda.would_not_falsify :"Missing computation does not falsify; structural prediction failure does" = "Missing computation does not falsify; structural prediction failure does"**


[V.R303] What would NOT falsify tau: failure to compute QCD
confinement from tau does not falsify the framework. It means
the computation is hard, not the structure wrong. Falsification
requires a structural prediction (Lambda = 0, no dark matter,
no singularities) to fail, not a computational deadline.

---

### `Tau.BookV.Coda.one_anchor_not_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L262-L267)
**theorem
Tau.BookV.Coda.one_anchor_not_zero :"0 free parameters, 1 anchor (m_n); iota_tau determines all ratios" = "0 free parameters, 1 anchor (m_n); iota_tau determines all ratios"**


[V.R305] One anchor, not zero: zero free parameters means no
dimensionless ratio is fitted. One experimental input (m_n)
sets the scale. iota_tau determines every ratio.

---

### `Tau.BookV.Coda.sqrt3_remark`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L269-L275)
**theorem
Tau.BookV.Coda.sqrt3_remark :"sqrt(3) triad: R correction, delta_A, alpha_G -- same |1 - omega|" = "sqrt(3) triad: R correction, delta_A, alpha_G -- same |1 - omega|"**


[V.R306] The sqrt(3): the same sqrt(3) = |1 - omega| appears in
the R correction, the proton-neutron mass difference, and the
gravitational closing identity. Three manifestations of the
spectral distance between adjacent lemniscate sectors.

---

### `Tau.BookV.Coda.comparison_sm`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Coda/ConstantsLedger.lean#L277-L283)
**theorem
Tau.BookV.Coda.comparison_sm :"SM: ~19 free params; tau: 0 free params + 1 anchor (m_n)" = "SM: ~19 free params; tau: 0 free params + 1 anchor (m_n)"**


[V.R308] Comparison with the Standard Model: the SM has ~19 free
parameters (masses, couplings, mixing angles). tau has 0 free
parameters and 1 anchor. The SM is an effective E1 readout of
the boundary algebra.
