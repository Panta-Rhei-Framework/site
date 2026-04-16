---
layout: taulib-doc
title: "TauLib.BookIV.Sectors.CouplingFormulas"
permalink: /verify/taulib/docs/book-iv-sectors-coupling-formulas/
lane: verify
module_name: "TauLib.BookIV.Sectors.CouplingFormulas"
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

# TauLib.BookIV.Sectors.CouplingFormulas


The 10-entry coupling ledger: all inter-sector couplings as rational functions
of ι<sub>τ</sub> = 2/(π+e), with structural theorems.

## Registry Cross-References


- [IV.D07] Coupling Formula Map — `coupling_formula`, `all_coupling_formulas`

- [IV.T01] Temporal Complement — `temporal_complement`

- [IV.T02] Temporal Multiplicative Closure — `temporal_multiplicative`

- [IV.P01] All Couplings Positive — `all_formulas_positive`

- [IV.P03] Power Hierarchy — `em_is_weak_squared`, `weak_strong_is_multiplicative`


## Mathematical Content


The No Knobs Principle (III.T08) determines all 10 inter-sector couplings
from ι<sub>τ</sub> alone. This module gives the explicit rational function formulas:

### Self-couplings (4)


Sector
Formula
Physical meaning


D (Gravity)
1 − ι<sub>τ</sub>
Temporal flow magnitude


A (Weak)
ι<sub>τ</sub>
Temporal arrow (= master constant)


B (EM)
ι<sub>τ</sub>²
Spatial distance scale


C (Strong)
ι<sub>τ</sub>³/(1−ι<sub>τ</sub>)
Confinement coupling


### Cross-couplings (6)


Pair
Formula
Physical meaning


(A,B)
ι<sub>τ</sub>³
Electroweak (multiplicative closure κ(A)·κ(B))


(A,C)
ι<sub>τ</sub>⁴/(1−ι<sub>τ</sub>)
Weak-Strong (multiplicative closure κ(A)·κ(C))


(A,D)
ι<sub>τ</sub>(1−ι<sub>τ</sub>)
Weak-Gravity (temporal consistency)


(B,C)
ι<sub>τ</sub>³/(1+ι<sub>τ</sub>)
EM-Strong = Higgs/mass crossing


(B,D)
ι<sub>τ</sub>²(1−ι<sub>τ</sub>)
EM-Gravity (lensing)


(C,D)
ι<sub>τ</sub>³(1−ι<sub>τ</sub>)
Strong-Gravity (mass curves time)


### Key structural relations


- κ(A;1) + κ(D;1) = 1 (temporal complement)

- κ(A,D) = κ(A;1) · κ(D;1) (temporal multiplicative closure)

- κ(B;2) = κ(A;1)² (EM = Weak squared)

- κ(A,C) = κ(A;1)·κ(C;3) (multiplicative closure)


## Ground Truth Sources


- temporal_spatial_decomposition.md §5: complete coupling reinterpretation

- Book III ch63 No Knobs Ledger: 10-entry inventory


---

### `Tau.BookIV.Sectors.CouplingFormula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L59-L72)
**structure
Tau.BookIV.Sectors.CouplingFormula :Type**


[IV.D07] A coupling formula: rational expression of ι<sub>τ</sub> between
two sectors, evaluated at the rational approximation.

- sector_i : BookIII.Sectors.Sector
First sector (ordered by Sector.toNat).

- sector_j : BookIII.Sectors.Sector
Second sector.

- numer : ℕ
Numerator of coupling (scaled).

- denom : ℕ
Denominator of coupling (scaled).

- denom_pos : self.denom > 0
Denominator is positive.

Instances For

---

### `Tau.BookIV.Sectors.instReprCouplingFormula.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L72-L72)
**def
Tau.BookIV.Sectors.instReprCouplingFormula.repr :CouplingFormula → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.instReprCouplingFormula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L72-L72)
**instance
Tau.BookIV.Sectors.instReprCouplingFormula :Repr CouplingFormula**

Equations
- Tau.BookIV.Sectors.instReprCouplingFormula = { reprPrec := Tau.BookIV.Sectors.instReprCouplingFormula.repr }

---

### `Tau.BookIV.Sectors.CouplingFormula.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L74-L76)
**def
Tau.BookIV.Sectors.CouplingFormula.toFloat
(c : CouplingFormula)
 :Float**


Coupling formula as Float.
Equations
- c.toFloat = Float.ofNat c.numer / Float.ofNat c.denom
Instances For

---

### `Tau.BookIV.Sectors.kappa_DD`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L103-L109)
**def
Tau.BookIV.Sectors.kappa_DD :CouplingFormula**


κ(D,D) = 1 − ι<sub>τ</sub>: Gravity self-coupling.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.kappa_AA`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L111-L117)
**def
Tau.BookIV.Sectors.kappa_AA :CouplingFormula**


κ(A,A) = ι<sub>τ</sub>: Weak self-coupling.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.kappa_BB`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L119-L125)
**def
Tau.BookIV.Sectors.kappa_BB :CouplingFormula**


κ(B,B) = ι<sub>τ</sub>²: EM self-coupling.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.kappa_CC`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L127-L133)
**def
Tau.BookIV.Sectors.kappa_CC :CouplingFormula**


κ(C,C) = ι<sub>τ</sub>³/(1−ι<sub>τ</sub>): Strong self-coupling (confinement).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.kappa_AB`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L135-L141)
**def
Tau.BookIV.Sectors.kappa_AB :CouplingFormula**


κ(A,B) = ι<sub>τ</sub>³: Electroweak coupling (multiplicative closure κ(A)·κ(B)).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.kappa_AC`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L143-L149)
**def
Tau.BookIV.Sectors.kappa_AC :CouplingFormula**


κ(A,C) = ι<sub>τ</sub>⁴/(1−ι<sub>τ</sub>): Weak-Strong coupling (multiplicative closure κ(A)·κ(C)).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.kappa_AD`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L151-L157)
**def
Tau.BookIV.Sectors.kappa_AD :CouplingFormula**


κ(A,D) = ι<sub>τ</sub>(1−ι<sub>τ</sub>): Weak-Gravity coupling (temporal consistency).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.kappa_BC`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L159-L165)
**def
Tau.BookIV.Sectors.kappa_BC :CouplingFormula**


κ(B,C) = ι<sub>τ</sub>³/(1+ι<sub>τ</sub>): EM-Strong = Higgs/mass crossing.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.kappa_BD`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L167-L173)
**def
Tau.BookIV.Sectors.kappa_BD :CouplingFormula**


κ(B,D) = ι<sub>τ</sub>²(1−ι<sub>τ</sub>): EM-Gravity (gravitational lensing).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.kappa_CD`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L175-L181)
**def
Tau.BookIV.Sectors.kappa_CD :CouplingFormula**


κ(C,D) = ι<sub>τ</sub>³(1−ι<sub>τ</sub>): Strong-Gravity (mass curves time).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.all_coupling_formulas`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L183-L187)
**def
Tau.BookIV.Sectors.all_coupling_formulas :List CouplingFormula**


The complete 10-entry coupling ledger.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.temporal_complement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L193-L200)
**theorem
Tau.BookIV.Sectors.temporal_complement :kappa_AA.numer + kappa_DD.numer = kappa_AA.denom**


[IV.T01] κ(A;1) + κ(D;1) = 1: the temporal pair exhausts the
depth-1 coupling budget. Gravity and Weak are complements.

Proof: ι + (D − ι) = D, so ι/D + (D−ι)/D = 1.

---

### `Tau.BookIV.Sectors.temporal_complement_denom`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L202-L205)
**theorem
Tau.BookIV.Sectors.temporal_complement_denom :kappa_AA.denom = kappa_DD.denom**


The shared denominator confirms they sum to exactly 1.

---

### `Tau.BookIV.Sectors.temporal_multiplicative`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L211-L220)
**theorem
Tau.BookIV.Sectors.temporal_multiplicative :kappa_AD.numer * (kappa_AA.denom * kappa_DD.denom) = kappa_AA.numer * kappa_DD.numer * kappa_AD.denom**


[IV.T02] κ(A,D) = κ(A;1) · κ(D;1): the temporal cross-coupling
is exactly the product of the two temporal self-couplings.
This means the temporal pair is "multiplicatively closed."

Proof: ι(D−ι)/D² = (ι/D)·((D−ι)/D).

---

### `Tau.BookIV.Sectors.em_is_weak_squared`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L226-L231)
**theorem
Tau.BookIV.Sectors.em_is_weak_squared :kappa_BB.numer * (kappa_AA.denom * kappa_AA.denom) = kappa_AA.numer * kappa_AA.numer * kappa_BB.denom**


[IV.P03a] κ(B;2) = κ(A;1)²: EM self-coupling equals Weak squared.
Proof: ι²/D² = (ι/D)².

---

### `Tau.BookIV.Sectors.weak_strong_is_multiplicative`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L233-L239)
**theorem
Tau.BookIV.Sectors.weak_strong_is_multiplicative :kappa_AC.numer * (kappa_AA.denom * kappa_CC.denom) = kappa_AA.numer * kappa_CC.numer * kappa_AC.denom**


[IV.P03b] κ(A,C) = κ(A;1)·κ(C;3): Weak-Strong = Weak × Strong (multiplicative closure).
Proof: (ι⁴·D)/(D⁴·(D−ι)) = (ι/D) · (ι³·D/(D³·(D−ι))).

---

### `Tau.BookIV.Sectors.all_formulas_positive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L245-L257)
**theorem
Tau.BookIV.Sectors.all_formulas_positive :kappa_DD.numer > 0 ∧ kappa_AA.numer > 0 ∧ kappa_BB.numer > 0 ∧ kappa_CC.numer > 0 ∧ kappa_AB.numer > 0 ∧ kappa_AC.numer > 0 ∧ kappa_AD.numer > 0 ∧ kappa_BC.numer > 0 ∧ kappa_BD.numer > 0 ∧ kappa_CD.numer > 0**


[IV.P01] All 10 coupling numerators are positive.
Since all denominators are positive by construction,
all coupling values are strictly positive.

---

### `Tau.BookIV.Sectors.coupling_ledger_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L259-L261)
**theorem
Tau.BookIV.Sectors.coupling_ledger_count :all_coupling_formulas.length = 10**


The ledger has exactly 10 entries.

---

### `Tau.BookIV.Sectors.coupling_formula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L267-L287)
**def
Tau.BookIV.Sectors.coupling_formula
(si sj : BookIII.Sectors.Sector)
 :CouplingFormula**


Retrieve the coupling formula for a sector pair.
Symmetric: coupling(i,j) = coupling(j,i).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.self_coupling_order`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/CouplingFormulas.lean#L293-L301)
**theorem
Tau.BookIV.Sectors.self_coupling_order :kappa_CC.toFloat < kappa_BB.toFloat ∧ kappa_BB.toFloat < kappa_AA.toFloat ∧ kappa_AA.toFloat < kappa_DD.toFloat**


Self-couplings are ordered: κ(C) < κ(B) < κ(A) < κ(D).
Strong < EM < Weak < Gravity in coupling strength.
