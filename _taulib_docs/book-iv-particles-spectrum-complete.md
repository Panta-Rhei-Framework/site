---
layout: taulib-doc
title: "TauLib.BookIV.Particles.SpectrumComplete"
permalink: /verify/taulib/docs/book-iv-particles-spectrum-complete/
lane: verify
module_name: "TauLib.BookIV.Particles.SpectrumComplete"
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

# TauLib.BookIV.Particles.SpectrumComplete


Particle spectrum completeness: the ontic entity definition, complete
ontic register, non-ontic entities list, the ontological line, dictionary
limits, the parameter count summary, and temperature as derived readout.

## Registry Cross-References


- [IV.D209] Ontic Entity — `OnticEntity`, `OnticCriterion`

- [IV.R149] Parameter Count — `parameter_count`

- [IV.R150] Ontic Entities List — comment-only (not_applicable)

- [IV.R151] Non-ontic Entities List — `non_ontic_entities`

- [IV.R152] Where the Ontological Line Falls — `ontological_line`

- [IV.R153] Dictionary Limits — `dictionary_limits`

- [IV.R154] Temperature is not Fundamental — `temperature_not_fundamental`


## Mathematical Content


Chapter 51 closes Part VI with the spectrum completeness theorem:
every observed particle is accounted for by τ³ mode structure, no BSM
particles are predicted, and the complete ontic/non-ontic classification
is a mathematical consequence of the fibration τ³ = τ¹ ×_f T².

An entity is ontic iff it can be constructed as a mode, character, or
finite composite on τ³. Wave functions as independent objects, virtual
particles, path integral measures, renormalization group flow, and
gravitons as particles are non-ontic (computational devices, not things).

The entire Part VI uses only two inputs: ι<sub>τ</sub> = 2/(π+e) and m_n.

## Ground Truth Sources


- Chapter 51 of Book IV (2nd Edition)


---

### `Tau.BookIV.Particles.OnticCriterion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L46-L57)
**inductive
Tau.BookIV.Particles.OnticCriterion :Type**


[IV.D209] An entity is ontic in Category τ if it satisfies at least
one of four criteria.

- fiberMode : OnticCriterion
Well-defined mode on fiber T² (particle).

- baseMode : OnticCriterion
Well-defined mode on base τ¹ (temporal/gravitational).

- crossingMode : OnticCriterion
Well-defined crossing mode at ω = γ ∩ η (Higgs-type).

- finiteComposite : OnticCriterion
Finite composite of ontic modes (hadrons, nuclei, atoms).

Instances For

---

### `Tau.BookIV.Particles.instReprOnticCriterion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L57-L57)
**instance
Tau.BookIV.Particles.instReprOnticCriterion :Repr OnticCriterion**

Equations
- Tau.BookIV.Particles.instReprOnticCriterion = { reprPrec := Tau.BookIV.Particles.instReprOnticCriterion.repr }

---

### `Tau.BookIV.Particles.instReprOnticCriterion.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L57-L57)
**def
Tau.BookIV.Particles.instReprOnticCriterion.repr :OnticCriterion → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instDecidableEqOnticCriterion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L57-L57)
**instance
Tau.BookIV.Particles.instDecidableEqOnticCriterion :DecidableEq OnticCriterion**

Equations
- Tau.BookIV.Particles.instDecidableEqOnticCriterion x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Particles.instBEqOnticCriterion`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L57-L57)
**instance
Tau.BookIV.Particles.instBEqOnticCriterion :BEq OnticCriterion**

Equations
- Tau.BookIV.Particles.instBEqOnticCriterion = { beq := Tau.BookIV.Particles.instBEqOnticCriterion.beq }

---

### `Tau.BookIV.Particles.instBEqOnticCriterion.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L57-L57)
**def
Tau.BookIV.Particles.instBEqOnticCriterion.beq :OnticCriterion → OnticCriterion → Bool**

Equations
- Tau.BookIV.Particles.instBEqOnticCriterion.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Particles.OnticEntity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L59-L69)
**structure
Tau.BookIV.Particles.OnticEntity :Type**


[IV.D209] An ontic entity in Category τ.

- name : String
Entity name.

- criterion : OnticCriterion
Primary ontic criterion.

- sectors : List BookIII.Sectors.Sector
Sector(s).

- stable : Bool
Is stable?

Instances For

---

### `Tau.BookIV.Particles.instReprOnticEntity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L69-L69)
**def
Tau.BookIV.Particles.instReprOnticEntity.repr :OnticEntity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprOnticEntity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L69-L69)
**instance
Tau.BookIV.Particles.instReprOnticEntity :Repr OnticEntity**

Equations
- Tau.BookIV.Particles.instReprOnticEntity = { reprPrec := Tau.BookIV.Particles.instReprOnticEntity.repr }

---

### `Tau.BookIV.Particles.ontic_register`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L75-L92)
**def
Tau.BookIV.Particles.ontic_register :List OnticEntity**


The complete list of fundamental ontic entities constructed in Book IV.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.ontic_register_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L94-L94)
**theorem
Tau.BookIV.Particles.ontic_register_count :ontic_register.length = 15**


---

### `Tau.BookIV.Particles.ParameterCount`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L100-L115)
**structure
Tau.BookIV.Particles.ParameterCount :Type**


[IV.R149] Across all 25+ results of Part VI:


- 1 dimensionless constant: ι<sub>τ</sub> = 2/(π+e), derived from K0-K6

- 1 dimensional anchor: m_n = 939.565421 MeV

- 0 fitting parameters, effective couplings, or ad hoc mass ratios


- dimensionless : ℕ
Dimensionless constants.

- anchors : ℕ
Dimensional anchors.

- fitting : ℕ
Fitting parameters.

- effective : ℕ
Effective couplings.

- ad_hoc : ℕ
Ad hoc mass ratios.

Instances For

---

### `Tau.BookIV.Particles.instReprParameterCount.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L115-L115)
**def
Tau.BookIV.Particles.instReprParameterCount.repr :ParameterCount → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprParameterCount`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L115-L115)
**instance
Tau.BookIV.Particles.instReprParameterCount :Repr ParameterCount**

Equations
- Tau.BookIV.Particles.instReprParameterCount = { reprPrec := Tau.BookIV.Particles.instReprParameterCount.repr }

---

### `Tau.BookIV.Particles.parameter_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L117-L117)
**def
Tau.BookIV.Particles.parameter_count :ParameterCount**

Equations
- Tau.BookIV.Particles.parameter_count = { }
Instances For

---

### `Tau.BookIV.Particles.zero_fitting`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L119-L119)
**theorem
Tau.BookIV.Particles.zero_fitting :parameter_count.fitting = 0**


---

### `Tau.BookIV.Particles.zero_effective`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L120-L120)
**theorem
Tau.BookIV.Particles.zero_effective :parameter_count.effective = 0**


---

### `Tau.BookIV.Particles.zero_ad_hoc`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L121-L121)
**theorem
Tau.BookIV.Particles.zero_ad_hoc :parameter_count.ad_hoc = 0**


---

### `Tau.BookIV.Particles.total_inputs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L122-L123)
**theorem
Tau.BookIV.Particles.total_inputs :parameter_count.dimensionless + parameter_count.anchors = 2**


---

### `Tau.BookIV.Particles.NonOnticEntity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L129-L136)
**structure
Tau.BookIV.Particles.NonOnticEntity :Type**


[IV.R151] Non-ontic entities: computational devices useful in
orthodox calculations but NOT representing τ³ objects.

- name : String
Entity name.

- reason : String
Why non-ontic.

Instances For

---

### `Tau.BookIV.Particles.instReprNonOnticEntity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L136-L136)
**instance
Tau.BookIV.Particles.instReprNonOnticEntity :Repr NonOnticEntity**

Equations
- Tau.BookIV.Particles.instReprNonOnticEntity = { reprPrec := Tau.BookIV.Particles.instReprNonOnticEntity.repr }

---

### `Tau.BookIV.Particles.instReprNonOnticEntity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L136-L136)
**def
Tau.BookIV.Particles.instReprNonOnticEntity.repr :NonOnticEntity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.non_ontic_entities`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L138-L149)
**def
Tau.BookIV.Particles.non_ontic_entities :List NonOnticEntity**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.five_non_ontic`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L151-L151)
**theorem
Tau.BookIV.Particles.five_non_ontic :non_ontic_entities.length = 5**


---

### `Tau.BookIV.Particles.OntologicalLine`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L157-L172)
**structure
Tau.BookIV.Particles.OntologicalLine :Type**


[IV.R152] The ontic/non-ontic distinction is not philosophical
preference but a mathematical consequence of the τ³ fibration.
An entity is ontic iff it can be constructed as a mode, character,
or finite composite on τ³ = τ¹ ×_f T².

- mathematical : Bool
Mathematical, not philosophical.

- criterion : String
Criterion: constructible on τ³.

- resolves_wf : Bool
Resolves wave function reality.

- resolves_virtual : Bool
Resolves virtual particle reality.

- resolves_spacetime : Bool
Resolves spacetime reality.

Instances For

---

### `Tau.BookIV.Particles.instReprOntologicalLine`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L172-L172)
**instance
Tau.BookIV.Particles.instReprOntologicalLine :Repr OntologicalLine**

Equations
- Tau.BookIV.Particles.instReprOntologicalLine = { reprPrec := Tau.BookIV.Particles.instReprOntologicalLine.repr }

---

### `Tau.BookIV.Particles.instReprOntologicalLine.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L172-L172)
**def
Tau.BookIV.Particles.instReprOntologicalLine.repr :OntologicalLine → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.ontological_line`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L174-L174)
**def
Tau.BookIV.Particles.ontological_line :OntologicalLine**

Equations
- Tau.BookIV.Particles.ontological_line = { }
Instances For

---

### `Tau.BookIV.Particles.line_is_mathematical`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L176-L177)
**theorem
Tau.BookIV.Particles.line_is_mathematical :ontological_line.mathematical = true**


---

### `Tau.BookIV.Particles.DictionaryLimits`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L183-L195)
**structure
Tau.BookIV.Particles.DictionaryLimits :Type**


[IV.R153] The τ-to-SM translation dictionary covers sector decomposition,
coupling ledger, QM infrastructure, and particle content but has limits:

No SM counterpart for: H_∂[ω], breathing operator, defect functional.
No τ counterpart for: virtual particles, path integral, RG flow, gravitons.

- tau_only : List String
Tau concepts without SM counterpart.

- sm_only : List String
SM concepts without tau counterpart.

Instances For

---

### `Tau.BookIV.Particles.instReprDictionaryLimits.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L195-L195)
**def
Tau.BookIV.Particles.instReprDictionaryLimits.repr :DictionaryLimits → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprDictionaryLimits`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L195-L195)
**instance
Tau.BookIV.Particles.instReprDictionaryLimits :Repr DictionaryLimits**

Equations
- Tau.BookIV.Particles.instReprDictionaryLimits = { reprPrec := Tau.BookIV.Particles.instReprDictionaryLimits.repr }

---

### `Tau.BookIV.Particles.dictionary_limits`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L197-L197)
**def
Tau.BookIV.Particles.dictionary_limits :DictionaryLimits**

Equations
- Tau.BookIV.Particles.dictionary_limits = { }
Instances For

---

### `Tau.BookIV.Particles.three_tau_only`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L199-L199)
**theorem
Tau.BookIV.Particles.three_tau_only :dictionary_limits.tau_only.length = 3**


---

### `Tau.BookIV.Particles.four_sm_only`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L200-L200)
**theorem
Tau.BookIV.Particles.four_sm_only :dictionary_limits.sm_only.length = 4**


---

### `Tau.BookIV.Particles.TemperatureNotFundamental`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L206-L219)
**structure
Tau.BookIV.Particles.TemperatureNotFundamental :Type**


[IV.R154] Temperature is not fundamental in Category τ but a readout:
the gradient of the defect functional with respect to the entropy
component. Part VII will use the defect functional as organizing
variable with temperature as derived quantity.

- derived : Bool
Temperature is derived.

- derivation : String
Derivation: gradient of defect functional.

- fundamental : String
Fundamental variable: defect functional.

- used_in_part_vii : Bool
Part VII uses this.

Instances For

---

### `Tau.BookIV.Particles.instReprTemperatureNotFundamental.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L219-L219)
**def
Tau.BookIV.Particles.instReprTemperatureNotFundamental.repr :TemperatureNotFundamental → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprTemperatureNotFundamental`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L219-L219)
**instance
Tau.BookIV.Particles.instReprTemperatureNotFundamental :Repr TemperatureNotFundamental**

Equations
- Tau.BookIV.Particles.instReprTemperatureNotFundamental = { reprPrec := Tau.BookIV.Particles.instReprTemperatureNotFundamental.repr }

---

### `Tau.BookIV.Particles.temperature_not_fundamental`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L221-L221)
**def
Tau.BookIV.Particles.temperature_not_fundamental :TemperatureNotFundamental**

Equations
- Tau.BookIV.Particles.temperature_not_fundamental = { }
Instances For

---

### `Tau.BookIV.Particles.temp_is_derived`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L223-L224)
**theorem
Tau.BookIV.Particles.temp_is_derived :temperature_not_fundamental.derived = true**


---

### `Tau.BookIV.Particles.SpectrumSummary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L230-L246)
**structure
Tau.BookIV.Particles.SpectrumSummary :Type**


Summary of the complete particle spectrum:


- All observed SM particles accounted for

- No BSM particles predicted

- Two inputs only (ι<sub>τ</sub>, m_n)

- Ontic/non-ontic line is mathematical


- sm_complete : Bool
All SM particles accounted for.

- no_bsm : Bool
No BSM predicted.

- num_inputs : ℕ
Number of inputs.

- ontic_count : ℕ
Ontic entities in register.

- non_ontic_count : ℕ
Non-ontic entities identified.

Instances For

---

### `Tau.BookIV.Particles.instReprSpectrumSummary.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L246-L246)
**def
Tau.BookIV.Particles.instReprSpectrumSummary.repr :SpectrumSummary → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprSpectrumSummary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L246-L246)
**instance
Tau.BookIV.Particles.instReprSpectrumSummary :Repr SpectrumSummary**

Equations
- Tau.BookIV.Particles.instReprSpectrumSummary = { reprPrec := Tau.BookIV.Particles.instReprSpectrumSummary.repr }

---

### `Tau.BookIV.Particles.spectrum_summary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L248-L248)
**def
Tau.BookIV.Particles.spectrum_summary :SpectrumSummary**

Equations
- Tau.BookIV.Particles.spectrum_summary = { }
Instances For

---

### `Tau.BookIV.Particles.spectrum_complete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L250-L250)
**theorem
Tau.BookIV.Particles.spectrum_complete :spectrum_summary.sm_complete = true**


---

### `Tau.BookIV.Particles.spectrum_no_bsm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L251-L251)
**theorem
Tau.BookIV.Particles.spectrum_no_bsm :spectrum_summary.no_bsm = true**


---

### `Tau.BookIV.Particles.spectrum_two_inputs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L252-L252)
**theorem
Tau.BookIV.Particles.spectrum_two_inputs :spectrum_summary.num_inputs = 2**


---

### `Tau.BookIV.Particles.total_entities`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SpectrumComplete.lean#L254-L256)
**theorem
Tau.BookIV.Particles.total_entities :spectrum_summary.ontic_count + spectrum_summary.non_ontic_count = 20**


Ontic and non-ontic together account for all discussed entities.
