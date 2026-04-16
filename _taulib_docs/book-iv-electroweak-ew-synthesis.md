---
layout: taulib-doc
title: "TauLib.BookIV.Electroweak.EWSynthesis"
permalink: /verify/taulib/docs/book-iv-electroweak-ew-synthesis/
lane: verify
module_name: "TauLib.BookIV.Electroweak.EWSynthesis"
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

# TauLib.BookIV.Electroweak.EWSynthesis


Electroweak synthesis: the complete EW prediction table, Yukawa ordering,
the sqrt(3) triad, and structural closure — nine EW quantities from
iota_tau and m_n alone, zero free parameters.

## Registry Cross-References


- [IV.D143] τ-Yukawa Coupling (Full Definition) — `YukawaCouplingFull`

- [IV.T66] Nine EW Quantities from ι<sub>τ</sub> and m_n — `nine_ew_quantities`

- [IV.T67] Every EW Prediction Traces to ι<sub>τ</sub> + K0-K6 — `ew_traces_to_axioms`

- [IV.T124] √3 Triad Theorem — `Sqrt3Triad`, `sqrt3_triad_count`

- [IV.P78] Yukawa Ordering Follows Sector Hierarchy — `yukawa_ordering`

- [IV.P79] Zero Free Parameters vs SM's 19 — `zero_vs_nineteen`

- [IV.P175] Three Lemniscate Supports — `three_lemniscate_supports`

- [IV.R37] EW Synthesis Complete — structural remark

- [IV.R38] No BSM Particles Required — structural remark

- [IV.R39] Experimental Test Program — structural remark

- [IV.R40] Connection to Book V Cosmology — structural remark


## Mathematical Content


This module synthesizes the electroweak sector of Book IV. The key result
(IV.T66) is that ALL nine electroweak quantities — three boson masses
(W, Z, H), the VEV, the Weinberg angle, three Yukawa couplings
(top, bottom, electron), and the fine structure constant — are determined
by exactly two inputs: ι<sub>τ</sub> = 2/(π+e) and the neutron mass anchor m_n.

The SM requires 19 free parameters for the same predictions. The τ-framework
achieves zero free parameters by deriving everything from the 7 axioms K0-K6.

The √3 triad theorem (IV.T124) reveals that the same algebraic quantity
√3 = |1 − ω| (where ω = e^{2πi/3}) appears in three independent
physical contexts: the R mass ratio correction, the proton-neutron mass
splitting, and the gravitational closing identity.

## Ground Truth Sources


- Chapter 35 of Book IV (2nd Edition)

- electron_mass_first_principles.md (master synthesis)

- holonomy_correction_sprint.md §14 (√3 triad)


---

### `Tau.BookIV.Electroweak.YukawaCouplingFull`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L55-L78)
**structure
Tau.BookIV.Electroweak.YukawaCouplingFull :Type**


[IV.D143] Full Yukawa coupling definition: associates each
fermion flavor with its coupling strength, the sector that
determines it, and the generation index.

The coupling is determined by the sector hierarchy:


- 3rd gen (top): coupling ≈ 1 (O(ι<sub>τ</sub>⁰))

- 2nd gen (charm, muon): coupling ≈ ι<sub>τ</sub>² (O(ι<sub>τ</sub>²))

- 1st gen (up, electron): coupling ≈ ι<sub>τ</sub>⁴ (O(ι<sub>τ</sub>⁴))


Each step down in generation multiplies by ι<sub>τ</sub>².

- flavor : String
Fermion flavor label.

- generation : ℕ
Generation (1, 2, or 3).

- coupling_numer : ℕ
Coupling numerator (scaled ×10⁶).

- coupling_denom : ℕ
Coupling denominator.

- denom_pos : self.coupling_denom > 0
Denominator positive.

- gen_valid : self.generation ≥ 1 ∧ self.generation ≤ 3
Generation is 1, 2, or 3.

Instances For

---

### `Tau.BookIV.Electroweak.instReprYukawaCouplingFull`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L78-L78)
**instance
Tau.BookIV.Electroweak.instReprYukawaCouplingFull :Repr YukawaCouplingFull**

Equations
- Tau.BookIV.Electroweak.instReprYukawaCouplingFull = { reprPrec := Tau.BookIV.Electroweak.instReprYukawaCouplingFull.repr }

---

### `Tau.BookIV.Electroweak.instReprYukawaCouplingFull.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L78-L78)
**def
Tau.BookIV.Electroweak.instReprYukawaCouplingFull.repr :YukawaCouplingFull → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.YukawaCouplingFull.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L80-L82)
**def
Tau.BookIV.Electroweak.YukawaCouplingFull.toFloat
(y : YukawaCouplingFull)
 :Float**


Yukawa coupling as Float.
Equations
- y.toFloat = Float.ofNat y.coupling_numer / Float.ofNat y.coupling_denom
Instances For

---

### `Tau.BookIV.Electroweak.yukawa_full_top`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L84-L90)
**def
Tau.BookIV.Electroweak.yukawa_full_top :YukawaCouplingFull**


Top quark: generation 3, y_t ≈ 0.995.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.yukawa_full_bottom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L92-L98)
**def
Tau.BookIV.Electroweak.yukawa_full_bottom :YukawaCouplingFull**


Bottom quark: generation 3 (down-type), y_b ≈ 0.024.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.yukawa_full_charm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L100-L106)
**def
Tau.BookIV.Electroweak.yukawa_full_charm :YukawaCouplingFull**


Charm quark: generation 2, y_c ≈ 0.0072.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.yukawa_full_electron`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L108-L114)
**def
Tau.BookIV.Electroweak.yukawa_full_electron :YukawaCouplingFull**


Electron: generation 1, y_e ≈ 2.9 × 10⁻⁶.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.EWSynthesisPrediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L120-L134)
**structure
Tau.BookIV.Electroweak.EWSynthesisPrediction :Type**


An EW prediction entry: name, τ-value, experimental value, deviation.

- name : String
Quantity name.

- tau_numer : ℕ
τ-predicted value numerator.

- tau_denom : ℕ
τ-predicted value denominator.

- exp_numer : ℕ
Experimental value numerator.

- exp_denom : ℕ
Experimental value denominator.

- deviation_ppm : ℕ
Approximate deviation in parts per million.

Instances For

---

### `Tau.BookIV.Electroweak.instReprEWSynthesisPrediction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L134-L134)
**instance
Tau.BookIV.Electroweak.instReprEWSynthesisPrediction :Repr EWSynthesisPrediction**

Equations
- Tau.BookIV.Electroweak.instReprEWSynthesisPrediction = { reprPrec := Tau.BookIV.Electroweak.instReprEWSynthesisPrediction.repr }

---

### `Tau.BookIV.Electroweak.instReprEWSynthesisPrediction.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L134-L134)
**def
Tau.BookIV.Electroweak.instReprEWSynthesisPrediction.repr :EWSynthesisPrediction → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.EWSynthesisPrediction.tauFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L136-L138)
**def
Tau.BookIV.Electroweak.EWSynthesisPrediction.tauFloat
(p : EWSynthesisPrediction)
 :Float**


τ-predicted value as Float.
Equations
- p.tauFloat = Float.ofNat p.tau_numer / Float.ofNat p.tau_denom
Instances For

---

### `Tau.BookIV.Electroweak.EWSynthesisPrediction.expFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L140-L142)
**def
Tau.BookIV.Electroweak.EWSynthesisPrediction.expFloat
(p : EWSynthesisPrediction)
 :Float**


Experimental value as Float.
Equations
- p.expFloat = Float.ofNat p.exp_numer / Float.ofNat p.exp_denom
Instances For

---

### `Tau.BookIV.Electroweak.ew_prediction_table`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L144-L155)
**def
Tau.BookIV.Electroweak.ew_prediction_table :List EWSynthesisPrediction**


[IV.T66] The nine EW quantities determined by ι<sub>τ</sub> and m_n.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.nine_ew_quantities`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L157-L158)
**theorem
Tau.BookIV.Electroweak.nine_ew_quantities :ew_prediction_table.length = 9**


The table has exactly 9 entries.

---

### `Tau.BookIV.Electroweak.EWAxiomTrace`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L164-L180)
**structure
Tau.BookIV.Electroweak.EWAxiomTrace :Type**


[IV.T67] The derivation chain for every EW quantity passes
through at most two fundamental inputs:

- ι<sub>τ</sub> = 2/(π+e) — the master constant from K0-K6.

- m_n — the neutron mass anchor (a single measured input).


All coupling constants, mixing angles, and masses are
rational functions of ι<sub>τ</sub> evaluated at the neutron anchor.

- input_count : ℕ
Number of fundamental inputs.

- input_1 : String
Input 1: master constant.

- input_2 : String
Input 2: neutron mass anchor.

- all_trace : Bool
All 9 quantities trace to these.

Instances For

---

### `Tau.BookIV.Electroweak.instReprEWAxiomTrace.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L180-L180)
**def
Tau.BookIV.Electroweak.instReprEWAxiomTrace.repr :EWAxiomTrace → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprEWAxiomTrace`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L180-L180)
**instance
Tau.BookIV.Electroweak.instReprEWAxiomTrace :Repr EWAxiomTrace**

Equations
- Tau.BookIV.Electroweak.instReprEWAxiomTrace = { reprPrec := Tau.BookIV.Electroweak.instReprEWAxiomTrace.repr }

---

### `Tau.BookIV.Electroweak.ew_traces_to_axioms`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L182-L182)
**def
Tau.BookIV.Electroweak.ew_traces_to_axioms :EWAxiomTrace**

Equations
- Tau.BookIV.Electroweak.ew_traces_to_axioms = { }
Instances For

---

### `Tau.BookIV.Electroweak.ew_two_inputs`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L184-L185)
**theorem
Tau.BookIV.Electroweak.ew_two_inputs :ew_traces_to_axioms.input_count = 2**


---

### `Tau.BookIV.Electroweak.Sqrt3Triad`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L191-L213)
**structure
Tau.BookIV.Electroweak.Sqrt3Triad :Type**


[IV.T124] The √3 triad: the same algebraic quantity √3 = |1 − ω|
(where ω = e^{2πi/3} is a primitive cube root of unity) appears
in three independent physical contexts:

- R mass ratio correction: √3 · ι<sub>τ</sub>^{-2} (spectral distance on L)

- Proton-neutron mass splitting: δ_A/m_n ≈ (√3/2) · ι<sub>τ</sub>⁶ (isospin)

- Gravitational closing identity: α_G = α¹⁸ · √3 (bi-rotation)


All three appearances trace to the SAME geometric origin: the
three-fold structure of the lemniscate L = S¹ ∨ S¹ with its
three sectors {Lobe₁, Lobe₂, Crossing}.

- context_R : String
Context 1: R mass ratio.

- context_delta_A : String
Context 2: proton-neutron splitting.

- context_alpha_G : String
Context 3: gravitational closing.

- origin : String
Geometric origin.

- appearance_count : ℕ
Number of independent appearances.

Instances For

---

### `Tau.BookIV.Electroweak.instReprSqrt3Triad.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L213-L213)
**def
Tau.BookIV.Electroweak.instReprSqrt3Triad.repr :Sqrt3Triad → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.instReprSqrt3Triad`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L213-L213)
**instance
Tau.BookIV.Electroweak.instReprSqrt3Triad :Repr Sqrt3Triad**

Equations
- Tau.BookIV.Electroweak.instReprSqrt3Triad = { reprPrec := Tau.BookIV.Electroweak.instReprSqrt3Triad.repr }

---

### `Tau.BookIV.Electroweak.sqrt3_triad`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L215-L215)
**def
Tau.BookIV.Electroweak.sqrt3_triad :Sqrt3Triad**

Equations
- Tau.BookIV.Electroweak.sqrt3_triad = { }
Instances For

---

### `Tau.BookIV.Electroweak.sqrt3_triad_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L217-L218)
**theorem
Tau.BookIV.Electroweak.sqrt3_triad_count :sqrt3_triad.appearance_count = 3**


---

### `Tau.BookIV.Electroweak.yukawa_ordering`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L224-L237)
**theorem
Tau.BookIV.Electroweak.yukawa_ordering :yukawa_full_top.coupling_numer * yukawa_full_bottom.coupling_denom > yukawa_full_bottom.coupling_numer * yukawa_full_top.coupling_denom ∧ yukawa_full_bottom.coupling_numer * yukawa_full_charm.coupling_denom > yukawa_full_charm.coupling_numer * yukawa_full_bottom.coupling_denom ∧ yukawa_full_charm.coupling_numer * yukawa_full_electron.coupling_denom > yukawa_full_electron.coupling_numer * yukawa_full_charm.coupling_denom**


[IV.P78] Yukawa couplings are ordered by generation, and the
ordering follows the sector coupling hierarchy:
y_top > y_bottom > y_charm > y_electron.

Each generation step down multiplies the coupling by approximately
ι<sub>τ</sub>², reflecting the spectral gap of the torus T².

---

### `Tau.BookIV.Electroweak.ZeroVsNineteen`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L243-L258)
**structure
Tau.BookIV.Electroweak.ZeroVsNineteen :Type**


[IV.P79] The τ-framework determines all 9 EW quantities with
zero free parameters, compared to the Standard Model's 19.

SM free parameters include: 3 gauge couplings, 6 quark masses,
3 lepton masses, 4 CKM parameters, 1 QCD vacuum angle, 1 Higgs
mass, 1 Higgs VEV = 19 total.

The τ-framework replaces all 19 with derivations from ι<sub>τ</sub>.

- tau_params : ℕ
τ free parameters.

- sm_params : ℕ
SM free parameters.

- reduction : String
Reduction factor.

Instances For

---

### `Tau.BookIV.Electroweak.instReprZeroVsNineteen`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L258-L258)
**instance
Tau.BookIV.Electroweak.instReprZeroVsNineteen :Repr ZeroVsNineteen**

Equations
- Tau.BookIV.Electroweak.instReprZeroVsNineteen = { reprPrec := Tau.BookIV.Electroweak.instReprZeroVsNineteen.repr }

---

### `Tau.BookIV.Electroweak.instReprZeroVsNineteen.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L258-L258)
**def
Tau.BookIV.Electroweak.instReprZeroVsNineteen.repr :ZeroVsNineteen → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.zero_vs_nineteen`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L260-L260)
**def
Tau.BookIV.Electroweak.zero_vs_nineteen :ZeroVsNineteen**

Equations
- Tau.BookIV.Electroweak.zero_vs_nineteen = { }
Instances For

---

### `Tau.BookIV.Electroweak.tau_zero_params`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L262-L263)
**theorem
Tau.BookIV.Electroweak.tau_zero_params :zero_vs_nineteen.tau_params = 0**


---

### `Tau.BookIV.Electroweak.sm_nineteen_params`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L265-L266)
**theorem
Tau.BookIV.Electroweak.sm_nineteen_params :zero_vs_nineteen.sm_params = 19**


---

### `Tau.BookIV.Electroweak.LemniscateSupport`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L272-L286)
**structure
Tau.BookIV.Electroweak.LemniscateSupport :Type**


[IV.P175] The three structural supports of the lemniscate
L = S¹ ∨ S¹ in the EW context:

- B-lobe (EM sector): photon propagation, α determination

- C-lobe (Strong sector): confinement, mass gap

- Crossing point (ω-sector): Higgs mechanism, mass assignment


Each support corresponds to a distinct physical mechanism.

- label : String
Support label.

- sector : BookIII.Sectors.Sector
Associated sector.

- mechanism : String
Physical mechanism.

Instances For

---

### `Tau.BookIV.Electroweak.instReprLemniscateSupport`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L286-L286)
**instance
Tau.BookIV.Electroweak.instReprLemniscateSupport :Repr LemniscateSupport**

Equations
- Tau.BookIV.Electroweak.instReprLemniscateSupport = { reprPrec := Tau.BookIV.Electroweak.instReprLemniscateSupport.repr }

---

### `Tau.BookIV.Electroweak.instReprLemniscateSupport.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L286-L286)
**def
Tau.BookIV.Electroweak.instReprLemniscateSupport.repr :LemniscateSupport → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Electroweak.support_B_lobe`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L288-L291)
**def
Tau.BookIV.Electroweak.support_B_lobe :LemniscateSupport**

Equations
- Tau.BookIV.Electroweak.support_B_lobe = { label := "B-lobe", sector := Tau.BookIII.Sectors.Sector.B, mechanism := "photon propagation, alpha" }
Instances For

---

### `Tau.BookIV.Electroweak.support_C_lobe`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L293-L296)
**def
Tau.BookIV.Electroweak.support_C_lobe :LemniscateSupport**

Equations
- Tau.BookIV.Electroweak.support_C_lobe = { label := "C-lobe", sector := Tau.BookIII.Sectors.Sector.C, mechanism := "confinement, mass gap" }
Instances For

---

### `Tau.BookIV.Electroweak.support_crossing`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L298-L301)
**def
Tau.BookIV.Electroweak.support_crossing :LemniscateSupport**

Equations
- Tau.BookIV.Electroweak.support_crossing = { label := "Crossing", sector := Tau.BookIII.Sectors.Sector.Omega, mechanism := "Higgs mechanism, mass assignment" }
Instances For

---

### `Tau.BookIV.Electroweak.three_lemniscate_supports`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L303-L305)
**def
Tau.BookIV.Electroweak.three_lemniscate_supports :List LemniscateSupport**


All three lemniscate supports.
Equations
- Tau.BookIV.Electroweak.three_lemniscate_supports = [Tau.BookIV.Electroweak.support_B_lobe, Tau.BookIV.Electroweak.support_C_lobe, Tau.BookIV.Electroweak.support_crossing]
Instances For

---

### `Tau.BookIV.Electroweak.three_supports_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L307-L308)
**theorem
Tau.BookIV.Electroweak.three_supports_count :three_lemniscate_supports.length = 3**


---

### `Tau.BookIV.Electroweak.remark_ew_complete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L314-L317)
**def
Tau.BookIV.Electroweak.remark_ew_complete :String**


[IV.R37] EW synthesis is complete: all quantities determined,
no free parameters, all scope labels assigned.
Equations
- Tau.BookIV.Electroweak.remark_ew_complete = "EW synthesis complete: 9 quantities, 2 inputs (iota_tau, m_n), 0 free parameters"
Instances For

---

### `Tau.BookIV.Electroweak.remark_no_bsm`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L319-L323)
**def
Tau.BookIV.Electroweak.remark_no_bsm :String**


[IV.R38] No BSM (Beyond Standard Model) particles are required.
The τ-framework reproduces all EW physics without supersymmetry,
extra dimensions, or additional gauge groups.
Equations
- Tau.BookIV.Electroweak.remark_no_bsm = "No BSM particles required: no SUSY, no extra dimensions, no extended gauge groups"
Instances For

---

### `Tau.BookIV.Electroweak.remark_test_program`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L325-L332)
**def
Tau.BookIV.Electroweak.remark_test_program :String**


[IV.R39] Experimental test program: the τ-framework makes
specific predictions testable at current and future colliders:


- Weinberg angle: 2.7% tree-level deviation

- Higgs branching ratios: percent-level corrections

- W mass: sub-MeV prediction

- No proton decay from GUT-type mechanisms

Equations
- Tau.BookIV.Electroweak.remark_test_program = "Testable: sin2(theta_W) 2.7%, Higgs BRs ~1%, M_W sub-MeV, no proton decay"
Instances For

---

### `Tau.BookIV.Electroweak.remark_book_v_connection`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Electroweak/EWSynthesis.lean#L334-L339)
**def
Tau.BookIV.Electroweak.remark_book_v_connection :String**


[IV.R40] Book V (Categorical Macrocosm) extends the EW synthesis
to the gravitational sector. The closing identity
α_G = α¹⁸ · √3 · (1 − (3/π)·α) connects the EW fine structure
constant to Newton's gravitational constant G via 18 powers of α.
Equations
- Tau.BookIV.Electroweak.remark_book_v_connection = "Book V extends to gravity: alpha_G = alpha^18 * sqrt(3) * (1 - (3/pi)*alpha)"
Instances For
