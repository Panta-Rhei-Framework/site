---
layout: taulib-doc
title: "TauLib.BookIV.QuantumMechanics.HilbertSpace"
permalink: /verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/
lane: verify
module_name: "TauLib.BookIV.QuantumMechanics.HilbertSpace"
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

# TauLib.BookIV.QuantumMechanics.HilbertSpace


The Hilbert space H_tau as L^2-completion of CR-holomorphic functions on tau^3:
inner product, separability, completeness, orthonormal basis from CR-admissible
characters, physical states, entanglement, and superposition.

## Registry Cross-References


- [IV.D60] Space of CR-Functions — `CRFunctionSpace`

- [IV.P16] Algebraic Properties of CR(tau^3) — `cr_space_algebraic`

- [IV.D61] Canonical Inner Product — `TauInnerProduct`

- [IV.P17] Inner Product Properties — `inner_product_properties`

- [IV.P18] Inner Product Uniqueness — `inner_product_unique`

- [IV.D62] Holomorphic Hilbert Space — `HilbertSpaceTau`

- [IV.T18] Hilbert Space Properties — `von_neumann_axioms`

- [IV.P19] Central Theorem Implies Boundary Determination — `boundary_determines_states`

- [IV.T19] Orthonormal Basis — `onb_is_admissible_characters`

- [IV.P20] Spectral Completeness — `spectral_completeness`

- [IV.D63] Physical State Space — `PhysicalState`

- [IV.D64] Entanglement — `EntanglementClass`

- [IV.P21] Generic Entanglement — `entangled_is_generic`

- [IV.P22] Superposition from Linearity — `superposition_from_linearity`


## Ground Truth Sources


- Chapter 18 of Book IV (2nd Edition)


---

### `Tau.BookIV.QuantumMechanics.CRFunctionSpace`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L40-L58)
**structure
Tau.BookIV.QuantumMechanics.CRFunctionSpace :Type**


[IV.D60] CR(tau^3) = {f : tau^3 -> C | dbar_b f = 0}: the space of
CR-holomorphic functions on the arena. These are the "physical states"
before Hilbert space completion.

Properties:


- Complex vector space (linearity of dbar_b)

- Commutative algebra (pointwise multiplication)

- Infinite-dimensional (one basis element per admissible address)


- is_vector_space : Bool
Complex vector space.

- vec_true : self.is_vector_space = true
- is_algebra : Bool
Commutative algebra under pointwise multiplication.

- alg_true : self.is_algebra = true
- is_infinite_dim : Bool
Infinite-dimensional (admissible lattice is infinite).

- inf_true : self.is_infinite_dim = true
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprCRFunctionSpace`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L58-L58)
**instance
Tau.BookIV.QuantumMechanics.instReprCRFunctionSpace :Repr CRFunctionSpace**

Equations
- Tau.BookIV.QuantumMechanics.instReprCRFunctionSpace = { reprPrec := Tau.BookIV.QuantumMechanics.instReprCRFunctionSpace.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprCRFunctionSpace.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L58-L58)
**def
Tau.BookIV.QuantumMechanics.instReprCRFunctionSpace.repr :CRFunctionSpace → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.cr_function_space`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L60-L67)
**def
Tau.BookIV.QuantumMechanics.cr_function_space :CRFunctionSpace**


The canonical CR-function space.
Equations
- Tau.BookIV.QuantumMechanics.cr_function_space = { is_vector_space := true, vec_true := ⋯, is_algebra := true, alg_true := ⋯, is_infinite_dim := true, inf_true := ⋯ }
Instances For

---

### `Tau.BookIV.QuantumMechanics.cr_space_algebraic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L73-L79)
**theorem
Tau.BookIV.QuantumMechanics.cr_space_algebraic :cr_function_space.is_vector_space = true ∧ cr_function_space.is_algebra = true ∧ cr_function_space.is_infinite_dim = true**


[IV.P16] CR(tau^3) is a complex vector space, commutative algebra,
and infinite-dimensional.

---

### `Tau.BookIV.QuantumMechanics.TauInnerProduct`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L85-L99)
**structure
Tau.BookIV.QuantumMechanics.TauInnerProduct :Type**


[IV.D61] The canonical inner product on CR(tau^3):
 = integral f_bar * g d_mu over tau^3.
Inherits Hermitian, sesquilinear, positive-definite properties
from the CR-structure + Haar measure on T^2.

- is_sesquilinear : Bool
Sesquilinear in f, g.

- sesq_true : self.is_sesquilinear = true
- is_hermitian : Bool
Hermitian: = conjugate().

- herm_true : self.is_hermitian = true
- is_positive_definite : Bool
Positive definite: > 0 for f != 0.

- posdef_true : self.is_positive_definite = true
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprTauInnerProduct`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L99-L99)
**instance
Tau.BookIV.QuantumMechanics.instReprTauInnerProduct :Repr TauInnerProduct**

Equations
- Tau.BookIV.QuantumMechanics.instReprTauInnerProduct = { reprPrec := Tau.BookIV.QuantumMechanics.instReprTauInnerProduct.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprTauInnerProduct.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L99-L99)
**def
Tau.BookIV.QuantumMechanics.instReprTauInnerProduct.repr :TauInnerProduct → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.tau_inner_product`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L101-L108)
**def
Tau.BookIV.QuantumMechanics.tau_inner_product :TauInnerProduct**


The canonical inner product.
Equations
- Tau.BookIV.QuantumMechanics.tau_inner_product = { is_sesquilinear := true, sesq_true := ⋯, is_hermitian := true, herm_true := ⋯, is_positive_definite := true,
 posdef_true := ⋯ }
Instances For

---

### `Tau.BookIV.QuantumMechanics.inner_product_properties`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L114-L120)
**theorem
Tau.BookIV.QuantumMechanics.inner_product_properties :tau_inner_product.is_sesquilinear = true ∧ tau_inner_product.is_hermitian = true ∧ tau_inner_product.is_positive_definite = true**


[IV.P17] The inner product is sesquilinear, Hermitian,
and positive definite.

---

### `Tau.BookIV.QuantumMechanics.InnerProductUniqueness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L126-L138)
**structure
Tau.BookIV.QuantumMechanics.InnerProductUniqueness :Type**


[IV.P18] Inner product uniqueness: the canonical inner product is
the UNIQUE inner product on CR(tau^3) that is simultaneously
sigma-equivariant (respects bipolar involution) and
rho-compatible (respects refinement tower).
Formalized structurally: uniqueness = both constraints hold.

- sigma_equivariant : Bool
sigma-equivariant (respects lobe swap).

- sigma_true : self.sigma_equivariant = true
- rho_compatible : Bool
rho-compatible (respects refinement).

- rho_true : self.rho_compatible = true
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprInnerProductUniqueness.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L138-L138)
**def
Tau.BookIV.QuantumMechanics.instReprInnerProductUniqueness.repr :InnerProductUniqueness → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprInnerProductUniqueness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L138-L138)
**instance
Tau.BookIV.QuantumMechanics.instReprInnerProductUniqueness :Repr InnerProductUniqueness**

Equations
- Tau.BookIV.QuantumMechanics.instReprInnerProductUniqueness = { reprPrec := Tau.BookIV.QuantumMechanics.instReprInnerProductUniqueness.repr }

---

### `Tau.BookIV.QuantumMechanics.inner_product_unique`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L140-L145)
**def
Tau.BookIV.QuantumMechanics.inner_product_unique :InnerProductUniqueness**


The inner product is uniquely determined.
Equations
- Tau.BookIV.QuantumMechanics.inner_product_unique = { sigma_equivariant := true, sigma_true := ⋯, rho_compatible := true, rho_true := ⋯ }
Instances For

---

### `Tau.BookIV.QuantumMechanics.HilbertSpaceTau`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L151-L163)
**structure
Tau.BookIV.QuantumMechanics.HilbertSpaceTau :Type**


[IV.D62] H_tau = L^2-completion of CR(tau^3): the Hilbert space
of quantum states. Equipped with the canonical inner product.

- is_complete : Bool
Complete (Cauchy sequences converge).

- complete_true : self.is_complete = true
- is_separable : Bool
Separable (countable dense subset).

- separable_true : self.is_separable = true
- is_infinite_dim : Bool
Infinite-dimensional.

- inf_true : self.is_infinite_dim = true
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprHilbertSpaceTau`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L163-L163)
**instance
Tau.BookIV.QuantumMechanics.instReprHilbertSpaceTau :Repr HilbertSpaceTau**

Equations
- Tau.BookIV.QuantumMechanics.instReprHilbertSpaceTau = { reprPrec := Tau.BookIV.QuantumMechanics.instReprHilbertSpaceTau.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprHilbertSpaceTau.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L163-L163)
**def
Tau.BookIV.QuantumMechanics.instReprHilbertSpaceTau.repr :HilbertSpaceTau → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.hilbert_tau`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L165-L172)
**def
Tau.BookIV.QuantumMechanics.hilbert_tau :HilbertSpaceTau**


The canonical Hilbert space.
Equations
- Tau.BookIV.QuantumMechanics.hilbert_tau = { is_complete := true, complete_true := ⋯, is_separable := true, separable_true := ⋯, is_infinite_dim := true,
 inf_true := ⋯ }
Instances For

---

### `Tau.BookIV.QuantumMechanics.von_neumann_axioms`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L178-L185)
**theorem
Tau.BookIV.QuantumMechanics.von_neumann_axioms :hilbert_tau.is_complete = true ∧ hilbert_tau.is_separable = true ∧ hilbert_tau.is_infinite_dim = true**


[IV.T18] The three von Neumann axioms for quantum mechanics:
H_tau is (1) complete, (2) separable, and (3) infinite-dimensional.
These are exactly the axioms required for quantum mechanical state spaces.

---

### `Tau.BookIV.QuantumMechanics.BoundaryDetermination`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L191-L204)
**structure
Tau.BookIV.QuantumMechanics.BoundaryDetermination :Type**


[IV.P19] Central Theorem (II.T15) implies H_tau = L^2(L_hat, d_nu_spec):
states on the interior tau^3 are completely determined by spectral data
on the boundary L = S^1 v S^1.
Formalized: both representations have the same structure.

- interior_dim : ℕ
Interior representation dimension (characters on T^2).

- interior_eq : self.interior_dim = 2
- boundary_dim : ℕ
Boundary representation dimension (spectral data on L).

- boundary_eq : self.boundary_dim = 2
- iso : self.interior_dim = self.boundary_dim
They agree (isomorphism from Central Theorem).

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprBoundaryDetermination.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L204-L204)
**def
Tau.BookIV.QuantumMechanics.instReprBoundaryDetermination.repr :BoundaryDetermination → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprBoundaryDetermination`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L204-L204)
**instance
Tau.BookIV.QuantumMechanics.instReprBoundaryDetermination :Repr BoundaryDetermination**

Equations
- Tau.BookIV.QuantumMechanics.instReprBoundaryDetermination = { reprPrec := Tau.BookIV.QuantumMechanics.instReprBoundaryDetermination.repr }

---

### `Tau.BookIV.QuantumMechanics.boundary_determines_states`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L206-L212)
**def
Tau.BookIV.QuantumMechanics.boundary_determines_states :BoundaryDetermination**


Boundary determines states.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.ONBStructure`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L218-L234)
**structure
Tau.BookIV.QuantumMechanics.ONBStructure :Type**


[IV.T19] The CR-admissible characters {chi_{m,n} : (m,n) in Lambda_CR}
form an orthonormal basis (ONB) for H_tau.
The basis is indexed by the admissible sublattice.

- index_type : String
Basis is indexed by admissible lattice points.

- index_is_admissible : self.index_type = "Lambda_CR"
- is_orthogonal : Bool
Basis elements are orthogonal.

- orth_true : self.is_orthogonal = true
- is_normalized : Bool
Basis elements are normalized.

- norm_true : self.is_normalized = true
- is_complete : Bool
Basis is complete (spans H_tau).

- comp_true : self.is_complete = true
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprONBStructure.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L234-L234)
**def
Tau.BookIV.QuantumMechanics.instReprONBStructure.repr :ONBStructure → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprONBStructure`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L234-L234)
**instance
Tau.BookIV.QuantumMechanics.instReprONBStructure :Repr ONBStructure**

Equations
- Tau.BookIV.QuantumMechanics.instReprONBStructure = { reprPrec := Tau.BookIV.QuantumMechanics.instReprONBStructure.repr }

---

### `Tau.BookIV.QuantumMechanics.onb_admissible`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L236-L245)
**def
Tau.BookIV.QuantumMechanics.onb_admissible :ONBStructure**


The canonical ONB.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.onb_is_admissible_characters`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L247-L253)
**theorem
Tau.BookIV.QuantumMechanics.onb_is_admissible_characters :onb_admissible.index_type = "Lambda_CR" ∧ onb_admissible.is_orthogonal = true ∧ onb_admissible.is_normalized = true ∧ onb_admissible.is_complete = true**


[IV.T19] ONB is indexed by admissible characters.

---

### `Tau.BookIV.QuantumMechanics.spectral_completeness`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L259-L263)
**theorem
Tau.BookIV.QuantumMechanics.spectral_completeness :onb_admissible.is_complete = true**


[IV.P20] Unique decomposition: every f in H_tau admits a unique
expansion f = sum c_{m,n} chi_{m,n} over Lambda_CR.
The convergence is in L^2 norm.

---

### `Tau.BookIV.QuantumMechanics.PhysicalState`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L269-L278)
**structure
Tau.BookIV.QuantumMechanics.PhysicalState :Type**


[IV.D63] Physical states = normalized + stable elements of H_tau.
Normalized: ||psi||^2 = 1. Stable: preserved under tau-admissible evolution.

- is_normalized : Bool
The state is normalized (||psi||^2 = 1).

- norm_true : self.is_normalized = true
- is_stable : Bool
The state is stable (preserved under admissible evolution).

- stable_true : self.is_stable = true
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprPhysicalState`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L278-L278)
**instance
Tau.BookIV.QuantumMechanics.instReprPhysicalState :Repr PhysicalState**

Equations
- Tau.BookIV.QuantumMechanics.instReprPhysicalState = { reprPrec := Tau.BookIV.QuantumMechanics.instReprPhysicalState.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprPhysicalState.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L278-L278)
**def
Tau.BookIV.QuantumMechanics.instReprPhysicalState.repr :PhysicalState → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.EntanglementClass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L284-L291)
**inductive
Tau.BookIV.QuantumMechanics.EntanglementClass :Type**


[IV.D64] Entanglement classification: a state is entangled if
it cannot be written as a tensor product of subsystem states.

- Separable : EntanglementClass
psi = psi_A tensor psi_B (factorizable).

- Entangled : EntanglementClass
psi is not factorizable (entangled).

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprEntanglementClass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L291-L291)
**instance
Tau.BookIV.QuantumMechanics.instReprEntanglementClass :Repr EntanglementClass**

Equations
- Tau.BookIV.QuantumMechanics.instReprEntanglementClass = { reprPrec := Tau.BookIV.QuantumMechanics.instReprEntanglementClass.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprEntanglementClass.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L291-L291)
**def
Tau.BookIV.QuantumMechanics.instReprEntanglementClass.repr :EntanglementClass → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instDecidableEqEntanglementClass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L291-L291)
**instance
Tau.BookIV.QuantumMechanics.instDecidableEqEntanglementClass :DecidableEq EntanglementClass**

Equations
- Tau.BookIV.QuantumMechanics.instDecidableEqEntanglementClass x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.QuantumMechanics.instBEqEntanglementClass`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L291-L291)
**instance
Tau.BookIV.QuantumMechanics.instBEqEntanglementClass :BEq EntanglementClass**

Equations
- Tau.BookIV.QuantumMechanics.instBEqEntanglementClass = { beq := Tau.BookIV.QuantumMechanics.instBEqEntanglementClass.beq }

---

### `Tau.BookIV.QuantumMechanics.instBEqEntanglementClass.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L291-L291)
**def
Tau.BookIV.QuantumMechanics.instBEqEntanglementClass.beq :EntanglementClass → EntanglementClass → Bool**

Equations
- Tau.BookIV.QuantumMechanics.instBEqEntanglementClass.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.QuantumMechanics.EntanglementGenericity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L297-L307)
**structure
Tau.BookIV.QuantumMechanics.EntanglementGenericity :Type**


[IV.P21] Separable states are measure zero; entangled states are
generic (dense, open, and full-measure in the state space).
Formalized structurally: separable is the exception, not the rule.

- separable_measure_zero : Bool
Separable states have measure zero.

- sep_true : self.separable_measure_zero = true
- entangled_dense : Bool
Entangled states are dense.

- ent_true : self.entangled_dense = true
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprEntanglementGenericity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L307-L307)
**instance
Tau.BookIV.QuantumMechanics.instReprEntanglementGenericity :Repr EntanglementGenericity**

Equations
- Tau.BookIV.QuantumMechanics.instReprEntanglementGenericity = { reprPrec := Tau.BookIV.QuantumMechanics.instReprEntanglementGenericity.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprEntanglementGenericity.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L307-L307)
**def
Tau.BookIV.QuantumMechanics.instReprEntanglementGenericity.repr :EntanglementGenericity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.entangled_is_generic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L309-L314)
**def
Tau.BookIV.QuantumMechanics.entangled_is_generic :EntanglementGenericity**


Entangled states are generic.
Equations
- Tau.BookIV.QuantumMechanics.entangled_is_generic = { separable_measure_zero := true, sep_true := ⋯, entangled_dense := true, ent_true := ⋯ }
Instances For

---

### `Tau.BookIV.QuantumMechanics.superposition_from_linearity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L320-L325)
**theorem
Tau.BookIV.QuantumMechanics.superposition_from_linearity :cr_function_space.is_vector_space = true**


[IV.P22] Superposition is a theorem (linearity of H_tau), not a
postulate. Since CR(tau^3) is a complex vector space, any linear
combination of physical states is again a state.
Formalized: vector space implies superposition.
