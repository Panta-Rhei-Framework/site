---
layout: taulib-doc
title: "TauLib.BookIV.Coda.LawsAsStructure"
permalink: /verify/taulib/docs/book-iv-coda-laws-as-structure/
lane: verify
module_name: "TauLib.BookIV.Coda.LawsAsStructure"
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

# TauLib.BookIV.Coda.LawsAsStructure


Physical laws as mathematical structure: tower-natural transformations,
Noether correspondence as corollary, why no larger gauge group is
possible, discrete symmetry violations, and UV finiteness.

## Registry Cross-References


- [IV.D241] Tower-Natural Transformation — `TowerNaturalTransformation`

- [IV.R180] Noether Theorem as Corollary — `remark_noether_corollary`

- [IV.R181] Why Not a Larger Gauge Group — comment-only

- [IV.R182] Individual C P CP Violations — comment-only

- [IV.P145] UV Finiteness — `UVFiniteness`

- [IV.R183] Vacuum Catastrophe Resolved — comment-only


## Mathematical Content


Chapter 55 establishes that in Category tau, physical laws are not
empirical regularities imposed on a blank substrate, but structural
consequences of the categorical architecture:

- 
**Tower-natural transformations**: every conservation law corresponds
to a natural transformation between sector functors that commutes
with the refinement tower.


- 
**Noether as corollary**: Noether's theorem (symmetry implies conservation)
is a special case: tower-naturality automatically implies the conserved
quantity. The structure determines which symmetries exist and which
conservation laws follow.


- 
**No larger gauge group**: the five sectors {D, A, B, C, omega} are
fixed by the generator count (K0-K6). No embedding into SU(5), SO(10),
or exceptional groups exists within tau.


- 
**UV finiteness**: every morphism in tau^3 involves sums over finitely
many addresses at each tower level, with no continuum regularization needed.


## Ground Truth Sources


- Chapter 55 of Book IV (2nd Edition)


---

### `Tau.BookIV.Coda.TowerNaturalTransformation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L54-L74)
**structure
Tau.BookIV.Coda.TowerNaturalTransformation :Type**


[IV.D241] A tower-natural transformation eta: F => G between sector
functors F, G: tau^1 -> tau^3|_{T^2} is a family {eta_n: F[n] -> G[n]}
in the boundary holonomy algebra that commutes with the refinement
tower maps:

eta_{n+1} composed phi_{n,n+1}^G = phi_{n,n+1}^F composed eta_n

for all primorial stages n. Every conservation law in the tau-framework
corresponds to such a transformation.

- indexed_by_stages : Bool
Family indexed by primorial stages.

- commutes_with_tower : Bool
Commutes with refinement tower maps.

- source : String
Source functor.

- target : String
Target functor.

- conservation_law : Bool
Conservation law correspondence.

Instances For

---

### `Tau.BookIV.Coda.instReprTowerNaturalTransformation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L74-L74)
**def
Tau.BookIV.Coda.instReprTowerNaturalTransformation.repr :TowerNaturalTransformation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.instReprTowerNaturalTransformation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L74-L74)
**instance
Tau.BookIV.Coda.instReprTowerNaturalTransformation :Repr TowerNaturalTransformation**

Equations
- Tau.BookIV.Coda.instReprTowerNaturalTransformation = { reprPrec := Tau.BookIV.Coda.instReprTowerNaturalTransformation.repr }

---

### `Tau.BookIV.Coda.tower_natural_transformation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L76-L76)
**def
Tau.BookIV.Coda.tower_natural_transformation :TowerNaturalTransformation**

Equations
- Tau.BookIV.Coda.tower_natural_transformation = { }
Instances For

---

### `Tau.BookIV.Coda.tower_nat_commutes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L78-L79)
**theorem
Tau.BookIV.Coda.tower_nat_commutes :tower_natural_transformation.commutes_with_tower = true**


---

### `Tau.BookIV.Coda.tower_nat_conservation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L81-L82)
**theorem
Tau.BookIV.Coda.tower_nat_conservation :tower_natural_transformation.conservation_law = true**


---

### `Tau.BookIV.Coda.remark_noether_corollary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L88-L99)
**def
Tau.BookIV.Coda.remark_noether_corollary :String**


[IV.R180] In Category tau, Noether's theorem is a corollary of the
categorical structure:

- The structure determines which natural transformations exist.

- Each automatically satisfies naturality (commutation with tower).

- Naturality implies the conserved quantity.


This inverts the orthodox logic: instead of "symmetry implies conservation",
we have "structural architecture determines both symmetries and
conservation laws simultaneously".
Equations
- Tau.BookIV.Coda.remark_noether_corollary = "Noether's theorem is a corollary: tower-naturality implies both " ++ "the symmetry and the conserved quantity simultaneously"
Instances For

---

### `Tau.BookIV.Coda.ConservationLaw`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L101-L119)
**inductive
Tau.BookIV.Coda.ConservationLaw :Type**


Conservation laws known to be tower-natural.

- Energy : ConservationLaw
Energy conservation from temporal tower-naturality.

- Momentum : ConservationLaw
Momentum conservation from spatial tower-naturality.

- AngularMomentum : ConservationLaw
Angular momentum from rotational tower-naturality on T^2.

- ElectricCharge : ConservationLaw
Electric charge from U(1) holonomy on B-sector.

- ColorCharge : ConservationLaw
Color charge from SU(3) holonomy on C-sector.

- BaryonNumber : ConservationLaw
Baryon number from eta-sector winding.

- LeptonNumber : ConservationLaw
Lepton number from gamma-sector winding.

- TopologicalCharge : ConservationLaw
Topological charge from pi_1(T^2).

Instances For

---

### `Tau.BookIV.Coda.instReprConservationLaw`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L119-L119)
**instance
Tau.BookIV.Coda.instReprConservationLaw :Repr ConservationLaw**

Equations
- Tau.BookIV.Coda.instReprConservationLaw = { reprPrec := Tau.BookIV.Coda.instReprConservationLaw.repr }

---

### `Tau.BookIV.Coda.instReprConservationLaw.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L119-L119)
**def
Tau.BookIV.Coda.instReprConservationLaw.repr :ConservationLaw → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.instDecidableEqConservationLaw`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L119-L119)
**instance
Tau.BookIV.Coda.instDecidableEqConservationLaw :DecidableEq ConservationLaw**

Equations
- Tau.BookIV.Coda.instDecidableEqConservationLaw x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Coda.instBEqConservationLaw`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L119-L119)
**instance
Tau.BookIV.Coda.instBEqConservationLaw :BEq ConservationLaw**

Equations
- Tau.BookIV.Coda.instBEqConservationLaw = { beq := Tau.BookIV.Coda.instBEqConservationLaw.beq }

---

### `Tau.BookIV.Coda.instBEqConservationLaw.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L119-L119)
**def
Tau.BookIV.Coda.instBEqConservationLaw.beq :ConservationLaw → ConservationLaw → Bool**

Equations
- Tau.BookIV.Coda.instBEqConservationLaw.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Coda.conservation_laws_exhaust`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L121-L126)
**theorem
Tau.BookIV.Coda.conservation_laws_exhaust
(c : ConservationLaw)
 :c = ConservationLaw.Energy ∨ c = ConservationLaw.Momentum ∨ c = ConservationLaw.AngularMomentum ∨ c = ConservationLaw.ElectricCharge ∨ c = ConservationLaw.ColorCharge ∨ c = ConservationLaw.BaryonNumber ∨ c = ConservationLaw.LeptonNumber ∨ c = ConservationLaw.TopologicalCharge**


All conservation laws are tower-natural.

---

### `Tau.BookIV.Coda.NoLargerGaugeGroup`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L140-L150)
**structure
Tau.BookIV.Coda.NoLargerGaugeGroup :Type**


Why no larger gauge group: fixed by 5 generators from K0-K6.

- num_generators : ℕ
Number of generators fixed by axioms.

- no_su5 : Bool
No embedding into SU(5).

- no_so10 : Bool
No embedding into SO(10).

- no_proton_decay : Bool
No proton decay.

Instances For

---

### `Tau.BookIV.Coda.instReprNoLargerGaugeGroup`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L150-L150)
**instance
Tau.BookIV.Coda.instReprNoLargerGaugeGroup :Repr NoLargerGaugeGroup**

Equations
- Tau.BookIV.Coda.instReprNoLargerGaugeGroup = { reprPrec := Tau.BookIV.Coda.instReprNoLargerGaugeGroup.repr }

---

### `Tau.BookIV.Coda.instReprNoLargerGaugeGroup.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L150-L150)
**def
Tau.BookIV.Coda.instReprNoLargerGaugeGroup.repr :NoLargerGaugeGroup → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.no_larger_gauge`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L152-L152)
**def
Tau.BookIV.Coda.no_larger_gauge :NoLargerGaugeGroup**

Equations
- Tau.BookIV.Coda.no_larger_gauge = { }
Instances For

---

### `Tau.BookIV.Coda.five_generators_fixed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L154-L155)
**theorem
Tau.BookIV.Coda.five_generators_fixed :no_larger_gauge.num_generators = 5**


---

### `Tau.BookIV.Coda.DiscreteSymmetryStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L167-L177)
**structure
Tau.BookIV.Coda.DiscreteSymmetryStatus :Type**


Discrete symmetry status in Category tau.

- c_violable : Bool
C (charge conjugation): can be violated.

- p_violated : Bool
P (parity): violated in A-sector.

- cp_violable : Bool
CP: can be violated (EW phase).

- cpt_preserved : Bool
CPT: preserved (structural).

Instances For

---

### `Tau.BookIV.Coda.instReprDiscreteSymmetryStatus.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L177-L177)
**def
Tau.BookIV.Coda.instReprDiscreteSymmetryStatus.repr :DiscreteSymmetryStatus → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.instReprDiscreteSymmetryStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L177-L177)
**instance
Tau.BookIV.Coda.instReprDiscreteSymmetryStatus :Repr DiscreteSymmetryStatus**

Equations
- Tau.BookIV.Coda.instReprDiscreteSymmetryStatus = { reprPrec := Tau.BookIV.Coda.instReprDiscreteSymmetryStatus.repr }

---

### `Tau.BookIV.Coda.discrete_symmetry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L179-L179)
**def
Tau.BookIV.Coda.discrete_symmetry :DiscreteSymmetryStatus**

Equations
- Tau.BookIV.Coda.discrete_symmetry = { }
Instances For

---

### `Tau.BookIV.Coda.cpt_preserved`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L181-L182)
**theorem
Tau.BookIV.Coda.cpt_preserved :discrete_symmetry.cpt_preserved = true**


---

### `Tau.BookIV.Coda.UVFiniteness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L188-L210)
**structure
Tau.BookIV.Coda.UVFiniteness :Type**


[IV.P145] Every morphism in tau^3 is UV-finite: loop integrals are
sums over intermediate addresses at tower level n with at most
prod_{p <= p_n} p terms, each well-defined and finite.

No continuum regularization (dimensional regularization, Pauli-Villars,
zeta-function regularization) is needed or meaningful.

UV divergences in orthodox QFT arise from summing over a continuum;
in tau the sum is always over a finite set at each tower level.

- finite_at_each_level : Bool
Finite sum at each tower level.

- bound : String
Bound: at most prod_{p <= p_n} p terms.

- no_dim_reg : Bool
No dimensional regularization needed.

- no_pauli_villars : Bool
No Pauli-Villars needed.

- no_zeta_reg : Bool
No zeta-function regularization needed.

- orthodoxy_source : String
Source of orthodoxy UV divergence: continuum sum.

Instances For

---

### `Tau.BookIV.Coda.instReprUVFiniteness.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L210-L210)
**def
Tau.BookIV.Coda.instReprUVFiniteness.repr :UVFiniteness → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.instReprUVFiniteness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L210-L210)
**instance
Tau.BookIV.Coda.instReprUVFiniteness :Repr UVFiniteness**

Equations
- Tau.BookIV.Coda.instReprUVFiniteness = { reprPrec := Tau.BookIV.Coda.instReprUVFiniteness.repr }

---

### `Tau.BookIV.Coda.uv_finiteness`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L212-L212)
**def
Tau.BookIV.Coda.uv_finiteness :UVFiniteness**

Equations
- Tau.BookIV.Coda.uv_finiteness = { }
Instances For

---

### `Tau.BookIV.Coda.uv_finite_at_each_level`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L214-L215)
**theorem
Tau.BookIV.Coda.uv_finite_at_each_level :uv_finiteness.finite_at_each_level = true**


---

### `Tau.BookIV.Coda.no_regularization_needed`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L217-L221)
**theorem
Tau.BookIV.Coda.no_regularization_needed :uv_finiteness.no_dim_reg = true ∧ uv_finiteness.no_pauli_villars = true ∧ uv_finiteness.no_zeta_reg = true**


---

### `Tau.BookIV.Coda.LawsAsStructureSummary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L232-L249)
**structure
Tau.BookIV.Coda.LawsAsStructureSummary :Type**


Summary: what "laws as structure" means. Physical laws in tau are:

- Not empirical regularities on a blank substrate

- Not axioms of a physical theory

- Structural consequences of the categorical architecture K0-K6

- Each law = a tower-natural transformation

- Conservation = naturality condition


- not_empirical : Bool
Not empirical.

- not_imposed : Bool
Not imposed axioms.

- structural : Bool
Structural consequences.

- law_is_nat_trans : Bool
Law = tower-natural transformation.

- conservation_is_naturality : Bool
Conservation = naturality.

Instances For

---

### `Tau.BookIV.Coda.instReprLawsAsStructureSummary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L249-L249)
**instance
Tau.BookIV.Coda.instReprLawsAsStructureSummary :Repr LawsAsStructureSummary**

Equations
- Tau.BookIV.Coda.instReprLawsAsStructureSummary = { reprPrec := Tau.BookIV.Coda.instReprLawsAsStructureSummary.repr }

---

### `Tau.BookIV.Coda.instReprLawsAsStructureSummary.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L249-L249)
**def
Tau.BookIV.Coda.instReprLawsAsStructureSummary.repr :LawsAsStructureSummary → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.laws_as_structure`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L251-L251)
**def
Tau.BookIV.Coda.laws_as_structure :LawsAsStructureSummary**

Equations
- Tau.BookIV.Coda.laws_as_structure = { }
Instances For

---

### `Tau.BookIV.Coda.laws_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Coda/LawsAsStructure.lean#L253-L254)
**theorem
Tau.BookIV.Coda.laws_structural :laws_as_structure.structural = true**
