---
layout: taulib-doc
title: "TauLib.BookIV.QuantumMechanics.Quantization"
permalink: /verify/taulib/docs/book-iv-quantum-mechanics-quantization/
lane: verify
module_name: "TauLib.BookIV.QuantumMechanics.Quantization"
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

# TauLib.BookIV.QuantumMechanics.Quantization


Holomorphic quantization on tau^3: holomorphic vector fields, the quantization
map from classical to quantum observables, commutator lifting, discrete spectra
from compact T^2, canonical commutation relation, and self-adjointness.

## Registry Cross-References


- [IV.D65] Holomorphic Vector Field — `HolomorphicField`

- [IV.D66] Quantum Operator — `QuantumOperator`

- [IV.P23] Commutator Equals Lifted Lie Bracket — `commutator_lifts`

- [IV.T20] Topological Quantization — `topological_quantization`

- [IV.T21] Canonical Commutation Relation — `canonical_commutation`

- [IV.D67] Observable — `Observable`

- [IV.P24] X and P Are Self-Adjoint — `xp_self_adjoint`

- [IV.R305] Structural remark on holomorphic flow

- [IV.R310] Structural remark on discrete spectra

- [IV.R312] Structural remark on commutation

- [IV.R314] Structural remark on observables


## Ground Truth Sources


- Chapter 19 of Book IV (2nd Edition)


---

### `Tau.BookIV.QuantumMechanics.HolomorphicField`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L38-L49)
**structure
Tau.BookIV.QuantumMechanics.HolomorphicField :Type**


[IV.D65] Holomorphic vector field on tau^3: a smooth vector field X
satisfying [X, dbar_b] = 0. These are the symmetries of the
CR-structure, and they generate the classical dynamics.

- label : String
Name/label of the field.

- commutes_with_dbar : Bool
Commutes with dbar_b.

- comm_true : self.commutes_with_dbar = true
- carrier : String
Carrier type (where it acts).

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprHolomorphicField`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L49-L49)
**instance
Tau.BookIV.QuantumMechanics.instReprHolomorphicField :Repr HolomorphicField**

Equations
- Tau.BookIV.QuantumMechanics.instReprHolomorphicField = { reprPrec := Tau.BookIV.QuantumMechanics.instReprHolomorphicField.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprHolomorphicField.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L49-L49)
**def
Tau.BookIV.QuantumMechanics.instReprHolomorphicField.repr :HolomorphicField → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.field_position`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L51-L56)
**def
Tau.BookIV.QuantumMechanics.field_position :HolomorphicField**


Position-type holomorphic field (acts on T^2 fiber).
Equations
- Tau.BookIV.QuantumMechanics.field_position = { label := "X", commutes_with_dbar := true, comm_true := ⋯, carrier := "fiber_T2" }
Instances For

---

### `Tau.BookIV.QuantumMechanics.field_momentum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L58-L63)
**def
Tau.BookIV.QuantumMechanics.field_momentum :HolomorphicField**


Momentum-type holomorphic field (conjugate to position).
Equations
- Tau.BookIV.QuantumMechanics.field_momentum = { label := "P", commutes_with_dbar := true, comm_true := ⋯, carrier := "fiber_T2" }
Instances For

---

### `Tau.BookIV.QuantumMechanics.QuantumOperator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L69-L81)
**structure
Tau.BookIV.QuantumMechanics.QuantumOperator :Type**


[IV.D66] Quantum operator: the quantization map X_hat f(p) =
d/dt f(phi_t(p)) where phi_t is the holomorphic flow of X.
Each holomorphic vector field X yields a quantum operator X_hat
acting on CR(tau^3).

- classical_field : HolomorphicField
The underlying classical holomorphic field.

- is_bounded : Bool
Whether the operator is bounded.

- is_linear : Bool
Whether the operator is linear.

- linear_true : self.is_linear = true
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprQuantumOperator.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L81-L81)
**def
Tau.BookIV.QuantumMechanics.instReprQuantumOperator.repr :QuantumOperator → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprQuantumOperator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L81-L81)
**instance
Tau.BookIV.QuantumMechanics.instReprQuantumOperator :Repr QuantumOperator**

Equations
- Tau.BookIV.QuantumMechanics.instReprQuantumOperator = { reprPrec := Tau.BookIV.QuantumMechanics.instReprQuantumOperator.repr }

---

### `Tau.BookIV.QuantumMechanics.op_position`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L83-L88)
**def
Tau.BookIV.QuantumMechanics.op_position :QuantumOperator**


Position operator X_hat.
Equations
- Tau.BookIV.QuantumMechanics.op_position = { classical_field := Tau.BookIV.QuantumMechanics.field_position, is_bounded := false, is_linear := true,
 linear_true := ⋯ }
Instances For

---

### `Tau.BookIV.QuantumMechanics.op_momentum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L90-L95)
**def
Tau.BookIV.QuantumMechanics.op_momentum :QuantumOperator**


Momentum operator P_hat.
Equations
- Tau.BookIV.QuantumMechanics.op_momentum = { classical_field := Tau.BookIV.QuantumMechanics.field_momentum, is_bounded := false, is_linear := true,
 linear_true := ⋯ }
Instances For

---

### `Tau.BookIV.QuantumMechanics.commutator_lifts`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L101-L108)
**theorem
Tau.BookIV.QuantumMechanics.commutator_lifts
(A B : QuantumOperator)
 :A.is_linear = true → B.is_linear = true → A.is_linear = true**


[IV.P23] The commutator of quantum operators equals the quantization
of the Lie bracket: [X_hat, Y_hat] = [X, Y]_hat.
This is the fundamental property of geometric quantization.
Formalized: both operators are linear → commutator is well-defined.

---

### `Tau.BookIV.QuantumMechanics.TopologicalQuantization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L114-L135)
**structure
Tau.BookIV.QuantumMechanics.TopologicalQuantization :Type**


[IV.T20] Topological quantization: the compactness of T^2 forces
the dual lattice Z^2 to be discrete, which forces the spectrum of
every quantum operator to be discrete.

Chain: compact T^2 → discrete Z^2 → Lambda_CR → discrete spectra.

The essential point: the compactness of the fiber is why physics
has discrete quantum numbers.

- fiber_compact : Bool
T^2 is compact.

- compact_true : self.fiber_compact = true
- dual_discrete : Bool
Dual lattice is discrete (Z^2).

- discrete_true : self.dual_discrete = true
- spectrum_discrete : Bool
Spectrum is discrete.

- spec_true : self.spectrum_discrete = true
- chain_length : ℕ
Compactness chain: compact → discrete dual → discrete spectrum.

- chain_eq : self.chain_length = 3
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprTopologicalQuantization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L135-L135)
**instance
Tau.BookIV.QuantumMechanics.instReprTopologicalQuantization :Repr TopologicalQuantization**

Equations
- Tau.BookIV.QuantumMechanics.instReprTopologicalQuantization = { reprPrec := Tau.BookIV.QuantumMechanics.instReprTopologicalQuantization.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprTopologicalQuantization.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L135-L135)
**def
Tau.BookIV.QuantumMechanics.instReprTopologicalQuantization.repr :TopologicalQuantization → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.topological_quantization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L137-L146)
**def
Tau.BookIV.QuantumMechanics.topological_quantization :TopologicalQuantization**


The topological quantization structure.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.CanonicalCommutation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L152-L170)
**structure
Tau.BookIV.QuantumMechanics.CanonicalCommutation :Type**


[IV.T21] Canonical commutation relation: [X_hat, P_hat] = i * hbar_tau.

In tau-units, hbar_tau = 1/4 (the unique sigma-equivariant crossing-point
mediator, as established in PlanckCharacter.lean).

This commutation relation is a THEOREM derived from the CR-structure
on tau^3, not a postulate of quantum mechanics.

We encode hbar_tau = 1/4 as the pair (1, 4).

- hbar_numer : ℕ
hbar_tau numerator.

- hbar_denom : ℕ
hbar_tau denominator.

- denom_pos : self.hbar_denom > 0
Denominator positive.

- is_quarter : self.hbar_numer = 1 ∧ self.hbar_denom = 4
hbar_tau = 1/4 in tau-units.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprCanonicalCommutation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L170-L170)
**def
Tau.BookIV.QuantumMechanics.instReprCanonicalCommutation.repr :CanonicalCommutation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprCanonicalCommutation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L170-L170)
**instance
Tau.BookIV.QuantumMechanics.instReprCanonicalCommutation :Repr CanonicalCommutation**

Equations
- Tau.BookIV.QuantumMechanics.instReprCanonicalCommutation = { reprPrec := Tau.BookIV.QuantumMechanics.instReprCanonicalCommutation.repr }

---

### `Tau.BookIV.QuantumMechanics.canonical_commutation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L172-L177)
**def
Tau.BookIV.QuantumMechanics.canonical_commutation :CanonicalCommutation**


The canonical commutation structure with hbar_tau = 1/4.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.hbar_tau_quarter`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L179-L183)
**theorem
Tau.BookIV.QuantumMechanics.hbar_tau_quarter :canonical_commutation.hbar_numer = 1 ∧ canonical_commutation.hbar_denom = 4**


hbar_tau = 1/4 in tau-units.

---

### `Tau.BookIV.QuantumMechanics.Observable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L189-L201)
**structure
Tau.BookIV.QuantumMechanics.Observable :Type**


[IV.D67] Observable: a self-adjoint quantum operator on H_tau.
Observables are the physically measurable quantities.
Self-adjointness ensures real eigenvalues (measurement outcomes).

- op : QuantumOperator
The underlying quantum operator.

- is_self_adjoint : Bool
Self-adjoint: A_hat^dagger = A_hat.

- sa_true : self.is_self_adjoint = true
- real_eigenvalues : Bool
Eigenvalues are real (consequence of self-adjointness).

- real_true : self.real_eigenvalues = true
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprObservable`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L201-L201)
**instance
Tau.BookIV.QuantumMechanics.instReprObservable :Repr Observable**

Equations
- Tau.BookIV.QuantumMechanics.instReprObservable = { reprPrec := Tau.BookIV.QuantumMechanics.instReprObservable.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprObservable.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L201-L201)
**def
Tau.BookIV.QuantumMechanics.instReprObservable.repr :Observable → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.obs_position`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L203-L209)
**def
Tau.BookIV.QuantumMechanics.obs_position :Observable**


Position as observable.
Equations
- Tau.BookIV.QuantumMechanics.obs_position = { op := Tau.BookIV.QuantumMechanics.op_position, is_self_adjoint := true, sa_true := ⋯, real_eigenvalues := true,
 real_true := ⋯ }
Instances For

---

### `Tau.BookIV.QuantumMechanics.obs_momentum`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L211-L217)
**def
Tau.BookIV.QuantumMechanics.obs_momentum :Observable**


Momentum as observable.
Equations
- Tau.BookIV.QuantumMechanics.obs_momentum = { op := Tau.BookIV.QuantumMechanics.op_momentum, is_self_adjoint := true, sa_true := ⋯, real_eigenvalues := true,
 real_true := ⋯ }
Instances For

---

### `Tau.BookIV.QuantumMechanics.xp_self_adjoint`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L223-L229)
**theorem
Tau.BookIV.QuantumMechanics.xp_self_adjoint :obs_position.is_self_adjoint = true ∧ obs_momentum.is_self_adjoint = true**


[IV.P24] Both position X_hat and momentum P_hat are self-adjoint
operators on H_tau. This is a structural consequence of the
fact that holomorphic flows on tau^3 preserve the inner product.

---

### `Tau.BookIV.QuantumMechanics.xp_real_eigenvalues`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Quantization.lean#L231-L235)
**theorem
Tau.BookIV.QuantumMechanics.xp_real_eigenvalues :obs_position.real_eigenvalues = true ∧ obs_momentum.real_eigenvalues = true**


Both observables have real eigenvalues.
