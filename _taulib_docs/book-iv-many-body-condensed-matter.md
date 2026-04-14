---
layout: taulib-doc
title: "TauLib.BookIV.ManyBody.CondensedMatter"
permalink: /verify/taulib/docs/book-iv-many-body-condensed-matter/
lane: verify
module_name: "TauLib.BookIV.ManyBody.CondensedMatter"
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

# TauLib.BookIV.ManyBody.CondensedMatter


Condensed matter from the defect lattice: monotone melting sequence,
topological branch of the defect spectrum, fiber-base factorization of
the universal defect functional, and fiber-level physics completeness.

## Registry Cross-References


- [IV.P143] Melting Sequence Monotone Mobility — `MeltingSequenceMobility`

- [IV.D240] Topological Branch — `TopologicalBranch`

- [IV.T94] Fiber-Base Factorization — `FiberBaseFactorization`

- [IV.R178] Why the separation is clean — comment-only

- [IV.P144] Fiber-Level Physics is Complete — `FiberLevelComplete`

- [IV.R179] The base is not the rest — comment-only


## Mathematical Content


This module synthesizes the many-body physics of Book IV Part VII by
establishing three structural results:

- 
**Melting sequence**: the six non-topological regimes are ordered by
monotonically increasing macroscopic mobility, from crystal (arrested)
to plasma (fully mobile).


- 
**Topological branch**: the superfluid and superconductor regimes form
a separate branch characterized by nonzero maximal mobility, zero bulk
vorticity, and quantized topological charge.


- 
**Fiber-base factorization**: the universal defect functional on
tau^3 = tau^1 x_f T^2 factorizes exactly as
delta[omega]*{tau^3} = delta[omega]*{T^2} tensor delta[omega]_{tau^1},
separating fiber (T^2, spatial) from base (tau^1, temporal) physics.


This factorization closes the fiber-level physics of Book IV and
exports a clean interface to Book V (base tau^1 = macrocosm).

## Ground Truth Sources


- Chapter 54 of Book IV (2nd Edition)

- fluid-condensed-matter.json: spectrum-complete-exports


---

### `Tau.BookIV.ManyBody.MeltingSequenceMobility`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L54-L74)
**structure
Tau.BookIV.ManyBody.MeltingSequenceMobility :Type**


[IV.P143] The six non-topological regimes are ordered by monotonically
increasing macroscopic mobility:

mu_crystal <= mu_quasi <= mu_glass < mu_Euler <= mu_NS < mu_MHD <= mu_plasma

This defines the **melting sequence**: each step increases the
degrees of freedom available to the many-body system.

The two topological regimes (superfluid, superconductor) lie on a
separate branch with maximal mobility but constrained theta.

- num_regimes : ℕ
Number of non-topological regimes.

- monotone : Bool
Ordering is monotone in mobility.

- sequence : List String
Regime labels in order.

- topological_separate : Bool
Topological branch separate.

Instances For

---

### `Tau.BookIV.ManyBody.instReprMeltingSequenceMobility`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L74-L74)
**instance
Tau.BookIV.ManyBody.instReprMeltingSequenceMobility :Repr MeltingSequenceMobility**

Equations
- Tau.BookIV.ManyBody.instReprMeltingSequenceMobility = { reprPrec := Tau.BookIV.ManyBody.instReprMeltingSequenceMobility.repr }

---

### `Tau.BookIV.ManyBody.instReprMeltingSequenceMobility.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L74-L74)
**def
Tau.BookIV.ManyBody.instReprMeltingSequenceMobility.repr :MeltingSequenceMobility → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.melting_sequence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L76-L76)
**def
Tau.BookIV.ManyBody.melting_sequence :MeltingSequenceMobility**

Equations
- Tau.BookIV.ManyBody.melting_sequence = { }
Instances For

---

### `Tau.BookIV.ManyBody.six_nontopo_regimes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L78-L79)
**theorem
Tau.BookIV.ManyBody.six_nontopo_regimes :melting_sequence.num_regimes = 6**


---

### `Tau.BookIV.ManyBody.melting_monotone`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L81-L82)
**theorem
Tau.BookIV.ManyBody.melting_monotone :melting_sequence.monotone = true**


---

### `Tau.BookIV.ManyBody.melting_sequence_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L84-L85)
**theorem
Tau.BookIV.ManyBody.melting_sequence_count :melting_sequence.sequence.length = 6**


---

### `Tau.BookIV.ManyBody.TopologicalBranch`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L91-L116)
**structure
Tau.BookIV.ManyBody.TopologicalBranch :Type**


[IV.D240] A topological branch of the defect spectrum is a regime with:

- Nonzero maximal mobility (free base-direction translation)

- Zero bulk vorticity nu_bulk = 0 (except at quantized cores)

- Quantized topological charge theta in Z


The two topological regimes are:


- Superfluid: theta quantized on fluid vortex cores

- Superconductor: theta quantized on magnetic flux tubes


They are distinguished by whether the B-sector (EM) is coupled.

- num_regimes : ℕ
Number of topological regimes.

- maximal_mobility : Bool
Common: maximal mobility.

- zero_bulk_vorticity : Bool
Common: zero bulk vorticity.

- quantized_theta : Bool
Common: quantized theta.

- superfluid_no_em : Bool
Superfluid: no EM coupling.

- superconductor_em : Bool
Superconductor: EM coupled.

- distinguished_by_em : Bool
Distinguished by B-sector coupling.

Instances For

---

### `Tau.BookIV.ManyBody.instReprTopologicalBranch`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L116-L116)
**instance
Tau.BookIV.ManyBody.instReprTopologicalBranch :Repr TopologicalBranch**

Equations
- Tau.BookIV.ManyBody.instReprTopologicalBranch = { reprPrec := Tau.BookIV.ManyBody.instReprTopologicalBranch.repr }

---

### `Tau.BookIV.ManyBody.instReprTopologicalBranch.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L116-L116)
**def
Tau.BookIV.ManyBody.instReprTopologicalBranch.repr :TopologicalBranch → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.topological_branch`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L118-L118)
**def
Tau.BookIV.ManyBody.topological_branch :TopologicalBranch**

Equations
- Tau.BookIV.ManyBody.topological_branch = { }
Instances For

---

### `Tau.BookIV.ManyBody.two_topological_regimes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L120-L121)
**theorem
Tau.BookIV.ManyBody.two_topological_regimes :topological_branch.num_regimes = 2**


---

### `Tau.BookIV.ManyBody.topological_distinguished_by_em`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L123-L124)
**theorem
Tau.BookIV.ManyBody.topological_distinguished_by_em :topological_branch.distinguished_by_em = true**


---

### `Tau.BookIV.ManyBody.FiberBaseFactorization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L130-L162)
**structure
Tau.BookIV.ManyBody.FiberBaseFactorization :Type**


[IV.T94] The universal defect functional on tau^3 = tau^1 x_f T^2
factorizes exactly:

delta[omega]*{tau^3} = delta[omega]*{T^2} tensor delta[omega]_{tau^1}

The fiber component delta[omega]_{T^2} contains all of:


- Quantum mechanics (Part III)

- Particle spectrum (Part VI)

- Electroweak and strong forces (Parts IV-V)

- Many-body and condensed matter (Part VII)


The base component delta[omega]_{tau^1} contains:


- Gravity (D-sector)

- Temporal structure

- Cosmological evolution


The factorization is exact by axiom K5 (fibered-product structure)
and the lemniscate L. The only fiber-base coupling passes through
the omega-sector (Kirchhoff junction).

- tensor_product : Bool
Factorizes as tensor product.

- fiber : String
Fiber: T^2 (spatial physics).

- base : String
Base: tau^1 (temporal physics).

- exact : Bool
Exact by K5 + lemniscate.

- coupling_omega_only : Bool
Only coupling: omega-sector.

- fiber_parts : ℕ
Number of fiber parts covered.

Instances For

---

### `Tau.BookIV.ManyBody.instReprFiberBaseFactorization.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L162-L162)
**def
Tau.BookIV.ManyBody.instReprFiberBaseFactorization.repr :FiberBaseFactorization → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprFiberBaseFactorization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L162-L162)
**instance
Tau.BookIV.ManyBody.instReprFiberBaseFactorization :Repr FiberBaseFactorization**

Equations
- Tau.BookIV.ManyBody.instReprFiberBaseFactorization = { reprPrec := Tau.BookIV.ManyBody.instReprFiberBaseFactorization.repr }

---

### `Tau.BookIV.ManyBody.fiber_base_factorization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L164-L164)
**def
Tau.BookIV.ManyBody.fiber_base_factorization :FiberBaseFactorization**

Equations
- Tau.BookIV.ManyBody.fiber_base_factorization = { }
Instances For

---

### `Tau.BookIV.ManyBody.factorization_exact`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L166-L167)
**theorem
Tau.BookIV.ManyBody.factorization_exact :fiber_base_factorization.exact = true**


---

### `Tau.BookIV.ManyBody.coupling_through_omega`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L169-L170)
**theorem
Tau.BookIV.ManyBody.coupling_through_omega :fiber_base_factorization.coupling_omega_only = true**


---

### `Tau.BookIV.ManyBody.FiberLevelComplete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L180-L203)
**structure
Tau.BookIV.ManyBody.FiberLevelComplete :Type**


[IV.P144] At the close of Part VII, every tau-admissible phenomenon
on the fiber T^2 is classified:


- Single particles (Part VI): quark/lepton spectrum, generations

- Quantum mechanics (Part III): uncertainty, measurement, energy/entropy

- Mass derivation (Part III): R = m_n/m_e, 10-link chain

- Electroweak forces (Part IV): EM, weak, Weinberg mixing, Higgs

- Strong force (Part V): confinement, mass gap, quarks/gluons

- Many-body (Part VII): 10 regimes, phase transitions, magnetism, NFL theorem


Nothing on the fiber T^2 remains unclassified. Book V addresses
the base tau^1 (gravity, cosmology, temporal structure).

- all_classified : Bool
All fiber phenomena classified.

- num_parts : ℕ
Number of Parts covering fiber.

- parts : List String
Parts: III (QM), IV (EW), V (Strong), VI (Particles), VII (Many-body).

- book_v_handles_base : Bool
Book V handles the base.

- export_to_book_v : Bool
Export contract to Book V.

Instances For

---

### `Tau.BookIV.ManyBody.instReprFiberLevelComplete.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L203-L203)
**def
Tau.BookIV.ManyBody.instReprFiberLevelComplete.repr :FiberLevelComplete → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprFiberLevelComplete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L203-L203)
**instance
Tau.BookIV.ManyBody.instReprFiberLevelComplete :Repr FiberLevelComplete**

Equations
- Tau.BookIV.ManyBody.instReprFiberLevelComplete = { reprPrec := Tau.BookIV.ManyBody.instReprFiberLevelComplete.repr }

---

### `Tau.BookIV.ManyBody.fiber_level_complete`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L205-L205)
**def
Tau.BookIV.ManyBody.fiber_level_complete :FiberLevelComplete**

Equations
- Tau.BookIV.ManyBody.fiber_level_complete = { }
Instances For

---

### `Tau.BookIV.ManyBody.fiber_all_classified`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L207-L208)
**theorem
Tau.BookIV.ManyBody.fiber_all_classified :fiber_level_complete.all_classified = true**


---

### `Tau.BookIV.ManyBody.fiber_five_parts`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L210-L211)
**theorem
Tau.BookIV.ManyBody.fiber_five_parts :fiber_level_complete.num_parts = 5**


---

### `Tau.BookIV.ManyBody.fiber_parts_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L213-L214)
**theorem
Tau.BookIV.ManyBody.fiber_parts_count :fiber_level_complete.parts.length = 5**


---

### `Tau.BookIV.ManyBody.RegimeSummary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L225-L233)
**structure
Tau.BookIV.ManyBody.RegimeSummary :Type**


Summary of the complete regime classification.

- name : String
Regime name.

- branch : String
Branch: non-topological or topological.

- discriminant : String
Key discriminant in defect tuple.

Instances For

---

### `Tau.BookIV.ManyBody.instReprRegimeSummary`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L233-L233)
**instance
Tau.BookIV.ManyBody.instReprRegimeSummary :Repr RegimeSummary**

Equations
- Tau.BookIV.ManyBody.instReprRegimeSummary = { reprPrec := Tau.BookIV.ManyBody.instReprRegimeSummary.repr }

---

### `Tau.BookIV.ManyBody.instReprRegimeSummary.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L233-L233)
**def
Tau.BookIV.ManyBody.instReprRegimeSummary.repr :RegimeSummary → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.regime_summary_table`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L235-L247)
**def
Tau.BookIV.ManyBody.regime_summary_table :List RegimeSummary**


The complete 10-regime classification.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.ten_regimes_total`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/ManyBody/CondensedMatter.lean#L249-L250)
**theorem
Tau.BookIV.ManyBody.ten_regimes_total :regime_summary_table.length = 10**
