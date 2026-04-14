---
layout: taulib-doc
title: "TauLib.BookIV.Coda.CompleteLedger"
permalink: /verify/taulib/docs/book-iv-coda-complete-ledger/
lane: verify
module_name: "TauLib.BookIV.Coda.CompleteLedger"
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

# TauLib.BookIV.Coda.CompleteLedger


Complete Book IV ledger: full constants table with scope labels,
formalization frontier, open problems, export contracts to Books V-VII,
one-way flow of exports, and the tau-sphaleron question.

## Registry Cross-References


- [IV.R184] Why C1 is Conjectural — `remark_c1_conjectural` (conjectural)

- [IV.R185] Comparison with ch15 Ledger — `remark_ledger_comparison`

- [IV.R186] The Formalization Frontier — `remark_formalization_frontier`

- [IV.R187] Open vs Wrong Problems — `remark_open_vs_wrong`

- [IV.D242] tau-Sphaleron Question — `TauSphaleronQuestion` (conjectural)

- [IV.R188] Why Sphaleron is Deferred — comment-only (conjectural)

- [IV.D243] Book V Import List — `BookVImportList`

- [IV.D244] Book VI Import List — `BookVIImportList`

- [IV.D245] Book VII Import List — `BookVIIImportList`

- [IV.R189] One-Way Flow of Export Contracts — comment-only


## Mathematical Content


Chapter 56 provides the complete ledger of Book IV: every derived quantity,
prediction, scope label, and open problem. It also defines the export
contracts to subsequent books.

The ledger has 66 entries:


- 16 established (from axioms K0-K6 alone)

- 25 tau-effective (structural but requiring anchor)

- 18 conjectural (hypothesized, not derived)

- 7 metaphorical (suggestive analogies)


The tau-sphaleron question is explicitly deferred to Book V because
it requires base-fiber coupling not available on T^2 alone.

## Ground Truth Sources


- Chapter 56 of Book IV (2nd Edition)


---

### `Tau.BookIV.Coda.remark_c1_conjectural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L51-L61)
**def
Tau.BookIV.Coda.remark_c1_conjectural :String**


[IV.R184] (Conjectural) The electron mass prediction
m_e = 0.510998937 MeV (0.025 ppm) remains conjectural despite its
precision: the mass ratio formula R is tau-effective as an internal
structural identity, but the numerical calibration against SI units
requires the neutron mass anchor, which is an empirical input.

The prediction is as precise as CODATA but not a derivation from
axioms alone (which would require establishing m_n from K0-K6).
Equations
- Tau.BookIV.Coda.remark_c1_conjectural = "[conjectural] m_e = 0.510998937 MeV (0.025 ppm): R formula is " ++ "tau-effective, but SI calibration needs empirical m_n anchor"
Instances For

---

### `Tau.BookIV.Coda.LedgerComparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L67-L83)
**structure
Tau.BookIV.Coda.LedgerComparison :Type**


[IV.R185] The Full Constants Ledger contains 66 entries with scope labels:
16 established, 25 tau-effective, 18 conjectural, 7 metaphorical.
This is an improvement over the ch15 partial ledger (23 entries).

- total : ℕ
Total entries.

- established : ℕ
Established count.

- tau_effective : ℕ
Tau-effective count.

- conjectural : ℕ
Conjectural count.

- metaphorical : ℕ
Metaphorical count.

- ch15_count : ℕ
Ch15 partial ledger count.

Instances For

---

### `Tau.BookIV.Coda.instReprLedgerComparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L83-L83)
**instance
Tau.BookIV.Coda.instReprLedgerComparison :Repr LedgerComparison**

Equations
- Tau.BookIV.Coda.instReprLedgerComparison = { reprPrec := Tau.BookIV.Coda.instReprLedgerComparison.repr }

---

### `Tau.BookIV.Coda.instReprLedgerComparison.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L83-L83)
**def
Tau.BookIV.Coda.instReprLedgerComparison.repr :LedgerComparison → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.ledger_comparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L85-L85)
**def
Tau.BookIV.Coda.ledger_comparison :LedgerComparison**

Equations
- Tau.BookIV.Coda.ledger_comparison = { }
Instances For

---

### `Tau.BookIV.Coda.ledger_total`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L87-L88)
**theorem
Tau.BookIV.Coda.ledger_total :ledger_comparison.total = 66**


---

### `Tau.BookIV.Coda.ledger_sums_to_total`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L90-L93)
**theorem
Tau.BookIV.Coda.ledger_sums_to_total :ledger_comparison.established + ledger_comparison.tau_effective + ledger_comparison.conjectural + ledger_comparison.metaphorical = 66**


---

### `Tau.BookIV.Coda.remark_ledger_comparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L95-L96)
**def
Tau.BookIV.Coda.remark_ledger_comparison :String**

Equations
- Tau.BookIV.Coda.remark_ledger_comparison = "Full ledger: 66 entries (16E + 25T + 18C + 7M), up from ch15's 23"
Instances For

---

### `Tau.BookIV.Coda.FormalizationFrontier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L102-L114)
**structure
Tau.BookIV.Coda.FormalizationFrontier :Type**


[IV.R186] Fifteen of twenty-five tau-effective results await Lean
formalization. This reflects LaTeX exposition outpacing formal
verification; no tau-effective result contradicts existing Lean proofs.

- awaiting : ℕ
Tau-effective awaiting formalization.

- total_te : ℕ
Total tau-effective.

- formalized : ℕ
Formalized tau-effective.

- no_contradictions : Bool
No contradictions found.

Instances For

---

### `Tau.BookIV.Coda.instReprFormalizationFrontier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L114-L114)
**instance
Tau.BookIV.Coda.instReprFormalizationFrontier :Repr FormalizationFrontier**

Equations
- Tau.BookIV.Coda.instReprFormalizationFrontier = { reprPrec := Tau.BookIV.Coda.instReprFormalizationFrontier.repr }

---

### `Tau.BookIV.Coda.instReprFormalizationFrontier.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L114-L114)
**def
Tau.BookIV.Coda.instReprFormalizationFrontier.repr :FormalizationFrontier → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.formalization_frontier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L116-L116)
**def
Tau.BookIV.Coda.formalization_frontier :FormalizationFrontier**

Equations
- Tau.BookIV.Coda.formalization_frontier = { }
Instances For

---

### `Tau.BookIV.Coda.remark_formalization_frontier`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L118-L119)
**def
Tau.BookIV.Coda.remark_formalization_frontier :String**

Equations
- Tau.BookIV.Coda.remark_formalization_frontier = "15/25 tau-effective results await Lean formalization; 0 contradictions"
Instances For

---

### `Tau.BookIV.Coda.OpenProblems`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L125-L143)
**structure
Tau.BookIV.Coda.OpenProblems :Type**


[IV.R187] Five open problems are explicitly distinguished from
wrong claims. Open problems have well-defined resolution criteria;
wrong claims have been refuted or are inconsistent.

- num_open : ℕ
Number of open problems.

- problems : List String
Problem list.

- resolution_criteria : Bool
All have well-defined resolution criteria.

- not_wrong : Bool
None are wrong claims.

Instances For

---

### `Tau.BookIV.Coda.instReprOpenProblems`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L143-L143)
**instance
Tau.BookIV.Coda.instReprOpenProblems :Repr OpenProblems**

Equations
- Tau.BookIV.Coda.instReprOpenProblems = { reprPrec := Tau.BookIV.Coda.instReprOpenProblems.repr }

---

### `Tau.BookIV.Coda.instReprOpenProblems.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L143-L143)
**def
Tau.BookIV.Coda.instReprOpenProblems.repr :OpenProblems → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.open_problems`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L145-L145)
**def
Tau.BookIV.Coda.open_problems :OpenProblems**

Equations
- Tau.BookIV.Coda.open_problems = { }
Instances For

---

### `Tau.BookIV.Coda.five_open`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L147-L148)
**theorem
Tau.BookIV.Coda.five_open :open_problems.num_open = 5**


---

### `Tau.BookIV.Coda.open_problems_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L150-L151)
**theorem
Tau.BookIV.Coda.open_problems_count :open_problems.problems.length = 5**


---

### `Tau.BookIV.Coda.remark_open_vs_wrong`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L153-L154)
**def
Tau.BookIV.Coda.remark_open_vs_wrong :String**

Equations
- Tau.BookIV.Coda.remark_open_vs_wrong = "5 open problems with resolution criteria; 0 wrong claims"
Instances For

---

### `Tau.BookIV.Coda.TauSphaleronQuestion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L160-L182)
**structure
Tau.BookIV.Coda.TauSphaleronQuestion :Type**


[IV.D242] (Conjectural) The tau-sphaleron question: can a
non-perturbative process in Category tau change the topological
winding number theta by a nonzero integer while respecting all
tower compatibility conditions?

In orthodox electroweak theory, sphalerons mediate baryon-number
violation through tunneling over a potential barrier.

In Category tau, this requires base-fiber coupling (the transition
must pass through the omega-sector), which cannot be resolved on
the fiber T^2 alone. Deferred to Book V.

- question : String
Question: can theta change non-perturbatively?

- requires_base_fiber : Bool
Requires base-fiber coupling.

- fiber_insufficient : Bool
Cannot be resolved on T^2 alone.

- deferred : String
Deferred to Book V.

- scope : String
Scope: conjectural.

Instances For

---

### `Tau.BookIV.Coda.instReprTauSphaleronQuestion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L182-L182)
**instance
Tau.BookIV.Coda.instReprTauSphaleronQuestion :Repr TauSphaleronQuestion**

Equations
- Tau.BookIV.Coda.instReprTauSphaleronQuestion = { reprPrec := Tau.BookIV.Coda.instReprTauSphaleronQuestion.repr }

---

### `Tau.BookIV.Coda.instReprTauSphaleronQuestion.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L182-L182)
**def
Tau.BookIV.Coda.instReprTauSphaleronQuestion.repr :TauSphaleronQuestion → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.tau_sphaleron_question`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L184-L184)
**def
Tau.BookIV.Coda.tau_sphaleron_question :TauSphaleronQuestion**

Equations
- Tau.BookIV.Coda.tau_sphaleron_question = { }
Instances For

---

### `Tau.BookIV.Coda.BookVImportList`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L195-L220)
**structure
Tau.BookIV.Coda.BookVImportList :Type**


[IV.D243] Book V Import List: what Book IV exports to Book V.

Book V receives complete fiber T^2 physics:


- All 10 coupling constants as rational functions of iota_tau (Lean-verified)

- The defect functional on T^2 (all 9 regimes classified)

- Phase transition taxonomy

- Particle spectrum (quarks, leptons, bosons, generations)

- Fine structure constant alpha

- Mass ratio R = m_n/m_e

- UV finiteness guarantee


Book V adds: D-sector gravity, cosmology, temporal structure.

- couplings : ℕ
Coupling constants exported.

- couplings_verified : Bool
Coupling constants Lean-verified.

- regimes : ℕ
Regimes classified.

- spectrum_complete : Bool
Particle spectrum complete.

- mass_ratio : Bool
Mass ratio R available.

- uv_finite : Bool
UV finiteness guaranteed.

Instances For

---

### `Tau.BookIV.Coda.instReprBookVImportList`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L220-L220)
**instance
Tau.BookIV.Coda.instReprBookVImportList :Repr BookVImportList**

Equations
- Tau.BookIV.Coda.instReprBookVImportList = { reprPrec := Tau.BookIV.Coda.instReprBookVImportList.repr }

---

### `Tau.BookIV.Coda.instReprBookVImportList.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L220-L220)
**def
Tau.BookIV.Coda.instReprBookVImportList.repr :BookVImportList → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.book_v_imports`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L222-L222)
**def
Tau.BookIV.Coda.book_v_imports :BookVImportList**

Equations
- Tau.BookIV.Coda.book_v_imports = { }
Instances For

---

### `Tau.BookIV.Coda.ten_couplings_exported`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L224-L225)
**theorem
Tau.BookIV.Coda.ten_couplings_exported :book_v_imports.couplings = 10**


---

### `Tau.BookIV.Coda.BookVIImportList`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L231-L248)
**structure
Tau.BookIV.Coda.BookVIImportList :Type**


[IV.D244] Book VI Import List: what Book IV exports to Book VI.

Book VI (Categorical Life) receives:


- The 4-component defect tuple as substrate for biological dynamics

- The 8+1 fluid regimes as environmental classification

- Phase transition taxonomy (for biological phase transitions)

- Thermodynamic structure (entropy splitting, arrow of time)

- UV finiteness (life cannot exploit UV divergences)


- defect_tuple : Bool
Defect tuple as biological substrate.

- regimes : ℕ
Regimes as environment.

- thermodynamics : Bool
Thermodynamic structure.

- arrow_of_time : Bool
Arrow of time.

Instances For

---

### `Tau.BookIV.Coda.instReprBookVIImportList`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L248-L248)
**instance
Tau.BookIV.Coda.instReprBookVIImportList :Repr BookVIImportList**

Equations
- Tau.BookIV.Coda.instReprBookVIImportList = { reprPrec := Tau.BookIV.Coda.instReprBookVIImportList.repr }

---

### `Tau.BookIV.Coda.instReprBookVIImportList.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L248-L248)
**def
Tau.BookIV.Coda.instReprBookVIImportList.repr :BookVIImportList → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.book_vi_imports`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L250-L250)
**def
Tau.BookIV.Coda.book_vi_imports :BookVIImportList**

Equations
- Tau.BookIV.Coda.book_vi_imports = { }
Instances For

---

### `Tau.BookIV.Coda.BookVIIImportList`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L256-L275)
**structure
Tau.BookIV.Coda.BookVIIImportList :Type**


[IV.D245] Book VII Import List: what Book IV exports to Book VII.

Book VII (Categorical Metaphysics) receives:


- The ontic/non-ontic ontological framework

- The self-enrichment claim (tau^3 enriched over itself)

- The deterministic arrow of time (S_ref monotonicity)

- UV finiteness as metaphysical claim (no infinities in nature)

- The "laws as structure" thesis


- ontological_framework : Bool
Ontic/non-ontic framework.

- self_enrichment : Bool
Self-enrichment claim.

- arrow_of_time : Bool
Deterministic arrow of time.

- uv_finite : Bool
UV finiteness.

- laws_as_structure : Bool
Laws as structure thesis.

Instances For

---

### `Tau.BookIV.Coda.instReprBookVIIImportList`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L275-L275)
**instance
Tau.BookIV.Coda.instReprBookVIIImportList :Repr BookVIIImportList**

Equations
- Tau.BookIV.Coda.instReprBookVIIImportList = { reprPrec := Tau.BookIV.Coda.instReprBookVIIImportList.repr }

---

### `Tau.BookIV.Coda.instReprBookVIIImportList.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L275-L275)
**def
Tau.BookIV.Coda.instReprBookVIIImportList.repr :BookVIIImportList → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.book_vii_imports`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L277-L277)
**def
Tau.BookIV.Coda.book_vii_imports :BookVIIImportList**

Equations
- Tau.BookIV.Coda.book_vii_imports = { }
Instances For

---

### `Tau.BookIV.Coda.LedgerScope`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L289-L295)
**inductive
Tau.BookIV.Coda.LedgerScope :Type**


Scope label for a ledger entry.

- Established : LedgerScope
- TauEffective : LedgerScope
- Conjectural : LedgerScope
- Metaphorical : LedgerScope
Instances For

---

### `Tau.BookIV.Coda.instReprLedgerScope.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L295-L295)
**def
Tau.BookIV.Coda.instReprLedgerScope.repr :LedgerScope → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.instReprLedgerScope`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L295-L295)
**instance
Tau.BookIV.Coda.instReprLedgerScope :Repr LedgerScope**

Equations
- Tau.BookIV.Coda.instReprLedgerScope = { reprPrec := Tau.BookIV.Coda.instReprLedgerScope.repr }

---

### `Tau.BookIV.Coda.instDecidableEqLedgerScope`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L295-L295)
**instance
Tau.BookIV.Coda.instDecidableEqLedgerScope :DecidableEq LedgerScope**

Equations
- Tau.BookIV.Coda.instDecidableEqLedgerScope x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Coda.instBEqLedgerScope`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L295-L295)
**instance
Tau.BookIV.Coda.instBEqLedgerScope :BEq LedgerScope**

Equations
- Tau.BookIV.Coda.instBEqLedgerScope = { beq := Tau.BookIV.Coda.instBEqLedgerScope.beq }

---

### `Tau.BookIV.Coda.instBEqLedgerScope.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L295-L295)
**def
Tau.BookIV.Coda.instBEqLedgerScope.beq :LedgerScope → LedgerScope → Bool**

Equations
- Tau.BookIV.Coda.instBEqLedgerScope.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Coda.LedgerEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L297-L305)
**structure
Tau.BookIV.Coda.LedgerEntry :Type**


A ledger entry with scope and category.

- label : String
Entry label (e.g., "alpha", "M_W", "R").

- scope : LedgerScope
Scope.

- category : String
Category (coupling, mass, structural, etc.).

Instances For

---

### `Tau.BookIV.Coda.instReprLedgerEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L305-L305)
**instance
Tau.BookIV.Coda.instReprLedgerEntry :Repr LedgerEntry**

Equations
- Tau.BookIV.Coda.instReprLedgerEntry = { reprPrec := Tau.BookIV.Coda.instReprLedgerEntry.repr }

---

### `Tau.BookIV.Coda.instReprLedgerEntry.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L305-L305)
**def
Tau.BookIV.Coda.instReprLedgerEntry.repr :LedgerEntry → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.representative_entries`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L307-L319)
**def
Tau.BookIV.Coda.representative_entries :List LedgerEntry**


Representative ledger entries (10 of 66, illustrating scope distribution).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.representative_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/CompleteLedger.lean#L321-L322)
**theorem
Tau.BookIV.Coda.representative_count :representative_entries.length = 10**
