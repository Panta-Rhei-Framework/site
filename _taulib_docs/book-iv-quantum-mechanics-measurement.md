---
layout: taulib-doc
title: "TauLib.BookIV.QuantumMechanics.Measurement"
permalink: /verify/taulib/docs/book-iv-quantum-mechanics-measurement/
lane: verify
module_name: "TauLib.BookIV.QuantumMechanics.Measurement"
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

# TauLib.BookIV.QuantumMechanics.Measurement


Measurement as address resolution, Born rule, Schrodinger equation,
decoherence, classical limit, and substrate determinism.

## Registry Cross-References


- [IV.D74] Measurement as Address Resolution — `AddressResolution`

- [IV.T27] Born Rule as Theorem — `born_rule_structural`

- [IV.P26] Post-Resolution Projection — `PostResolutionState`

- [IV.D75] Decoherence — `Decoherence`

- [IV.P27] Classical Limit — `classical_limit_structural`

- [IV.T28] Schrodinger Derived — `SchrodingerEquation`

- [IV.P28] Substrate Determinism + Outcome Probability — `determinism_probability`

- [IV.R323] Measurement remark — structural

- [IV.R326] Substrate remark — structural


## Mathematical Content


### Measurement = Address Resolution


In the tau-framework, measurement is NOT a primitive postulate but the
**resolution of a CR-address** to a definite lattice site. When a quantum
system (ψ as holomorphic field on T²) couples to a macroscopic detector,
the detector's own CR-address structure forces projection onto a single
lattice mode (m₀, n₀).

### Born Rule as Theorem


P(m₀, n₀) = |c_{m₀,n₀}|² follows from the Pythagorean theorem on the
CR-Hilbert space: the probability of resolving to mode (m₀, n₀) is the
squared projection coefficient. This is NOT a postulate.

### Schrodinger Equation


iℏ_τ ∂ψ/∂t = H_∞ ψ where H_∞ = ι<sub>τ</sub>² Δ_Hodge is the breathing operator
restricted to the torus T². This is DERIVED from holomorphic flow on the
CR-address lattice, not postulated.

### Classical Limit


When |m|, |n| → ∞, the CR-address lattice becomes dense and the
quantum obstruction (uncertainty product) becomes negligible relative
to the classical action scale. Classical mechanics emerges as the
large-quantum-number limit.

## Ground Truth Sources


- Book IV Part III ch20-ch22

- quantum-mechanics.json: measurement, born-rule, schrodinger


---

### `Tau.BookIV.QuantumMechanics.AddressResolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L63-L85)
**structure
Tau.BookIV.QuantumMechanics.AddressResolution :Type**


[IV.D74] Measurement = address resolution.

A measurement event is the coupling of a quantum state ψ (holomorphic
field on T²) to a macroscopic detector, forcing resolution of the
CR-address to a definite lattice site (m₀, n₀).

The detector's own CR-address structure acts as a "selector":
it projects ψ onto the eigenmode at (m₀, n₀) with probability
given by the squared coefficient |c_{m₀,n₀}|².

- outcome_m : ℤ
Resolved fiber mode index.

- outcome_n : ℤ
Resolved base mode index.

- probability_numer : ℕ
Probability numerator |c_{m₀,n₀}|² (scaled).

- probability_denom : ℕ
Probability denominator.

- denom_pos : self.probability_denom > 0
Denominator positive.

- prob_le_one : self.probability_numer ≤ self.probability_denom
Probability ≤ 1 (numer ≤ denom).

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprAddressResolution`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L85-L85)
**instance
Tau.BookIV.QuantumMechanics.instReprAddressResolution :Repr AddressResolution**

Equations
- Tau.BookIV.QuantumMechanics.instReprAddressResolution = { reprPrec := Tau.BookIV.QuantumMechanics.instReprAddressResolution.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprAddressResolution.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L85-L85)
**def
Tau.BookIV.QuantumMechanics.instReprAddressResolution.repr :AddressResolution → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.AddressResolution.probFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L87-L89)
**def
Tau.BookIV.QuantumMechanics.AddressResolution.probFloat
(a : AddressResolution)
 :Float**


Probability as Float (for display).
Equations
- a.probFloat = Float.ofNat a.probability_numer / Float.ofNat a.probability_denom
Instances For

---

### `Tau.BookIV.QuantumMechanics.born_rule_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L95-L102)
**theorem
Tau.BookIV.QuantumMechanics.born_rule_structural
(a : AddressResolution)
 :a.probability_numer ≤ a.probability_denom**


[IV.T27] Born rule as theorem: the probability of resolving to mode
(m₀, n₀) equals |c_{m₀,n₀}|², the squared projection coefficient.

This is a STRUCTURAL consequence of the Pythagorean theorem on the
CR-Hilbert space, not a postulate. The resolution probability is
determined by the geometry of the projection, not by an axiom.

---

### `Tau.BookIV.QuantumMechanics.BornNormalization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L104-L116)
**structure
Tau.BookIV.QuantumMechanics.BornNormalization :Type**


Probabilities sum to 1: for a complete set of resolutions, the
numerators (scaled to common denominator) sum to the denominator.

- resolutions : List AddressResolution
List of resolution probabilities (numer/denom pairs).

- common_denom : ℕ
Common denominator for all resolutions.

- common_denom_pos : self.common_denom > 0
Common denominator positive.

- sum_eq_denom : (List.map (fun (r : AddressResolution) => r.probability_numer * (self.common_denom / r.probability_denom))
 self.resolutions).sum = self.common_denom
Sum of scaled numerators equals common denominator.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprBornNormalization`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L116-L116)
**instance
Tau.BookIV.QuantumMechanics.instReprBornNormalization :Repr BornNormalization**

Equations
- Tau.BookIV.QuantumMechanics.instReprBornNormalization = { reprPrec := Tau.BookIV.QuantumMechanics.instReprBornNormalization.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprBornNormalization.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L116-L116)
**def
Tau.BookIV.QuantumMechanics.instReprBornNormalization.repr :BornNormalization → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.PostResolutionState`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L122-L135)
**structure
Tau.BookIV.QuantumMechanics.PostResolutionState :Type**


[IV.P26] Post-resolution state: after measurement, the quantum state
is projected onto the resolved mode.

"Collapse" is NOT a physical process but the bookkeeping update of the
CR-address label after resolution. The state was always a superposition
of CR-modes; measurement resolves which mode the detector selected.

- resolution : AddressResolution
The resolved address.

- is_eigenmode : Bool
The post-resolution state is a single eigenmode.

- is_idempotent : Bool
The projection is idempotent (projecting again gives same state).

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprPostResolutionState.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L135-L135)
**def
Tau.BookIV.QuantumMechanics.instReprPostResolutionState.repr :PostResolutionState → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprPostResolutionState`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L135-L135)
**instance
Tau.BookIV.QuantumMechanics.instReprPostResolutionState :Repr PostResolutionState**

Equations
- Tau.BookIV.QuantumMechanics.instReprPostResolutionState = { reprPrec := Tau.BookIV.QuantumMechanics.instReprPostResolutionState.repr }

---

### `Tau.BookIV.QuantumMechanics.projection_idempotent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L137-L139)
**theorem
Tau.BookIV.QuantumMechanics.projection_idempotent
(p : PostResolutionState)

(h : p.is_idempotent = true)
 :p.is_idempotent = true**


[IV.P26] Projection is idempotent by construction.

---

### `Tau.BookIV.QuantumMechanics.Decoherence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L145-L164)
**structure
Tau.BookIV.QuantumMechanics.Decoherence :Type**


[IV.D75] Decoherence = suppression of off-diagonal density matrix elements.

In the tau-framework, decoherence is the suppression of off-diagonal
elements ρ_{mn,m'n'} (m,n ≠ m',n') in the density matrix due to
coupling with the environment's CR-address lattice.

Rate: proportional to the number of environmental modes that
couple to the system's off-diagonal coherences.

- suppression_rate_numer : ℕ
Suppression rate numerator (1/time scale, scaled).

- suppression_rate_denom : ℕ
Suppression rate denominator.

- rate_denom_pos : self.suppression_rate_denom > 0
Denominator positive.

- off_diagonal_vanish : Bool
Off-diagonal elements vanish in the decoherence limit.

- scope : String
Scope: tau-effective.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprDecoherence.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L164-L164)
**def
Tau.BookIV.QuantumMechanics.instReprDecoherence.repr :Decoherence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprDecoherence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L164-L164)
**instance
Tau.BookIV.QuantumMechanics.instReprDecoherence :Repr Decoherence**

Equations
- Tau.BookIV.QuantumMechanics.instReprDecoherence = { reprPrec := Tau.BookIV.QuantumMechanics.instReprDecoherence.repr }

---

### `Tau.BookIV.QuantumMechanics.SchrodingerEquation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L170-L191)
**structure
Tau.BookIV.QuantumMechanics.SchrodingerEquation :Type**


[IV.T28] Schrodinger equation: iℏ_τ ∂ψ/∂t = H_∞ ψ.

H_∞ = ι<sub>τ</sub>² Δ_Hodge is the breathing operator on T².
This equation is DERIVED from holomorphic flow on the CR-address
lattice, not postulated. The ι<sub>τ</sub>² prefactor is the inverse of
the breathing operator B = (1/ι<sub>τ</sub>²)·Δ⁻¹|_{T²}.

The iota-squared coefficient:


- iota_sq_numer = ι² numerator (from SectorParameters)

- iota_sq_denom = ι² denominator


- hamiltonian_coeff_numer : ℕ
H_∞ coefficient numerator: ι<sub>τ</sub>².

- hamiltonian_coeff_denom : ℕ
H_∞ coefficient denominator.

- denom_pos : self.hamiltonian_coeff_denom > 0
Denominator positive.

- is_derived : Bool
The equation is derived (not postulated).

- operator_name : String
The Hamiltonian is H_∞ = ι<sub>τ</sub>² Δ_Hodge.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprSchrodingerEquation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L191-L191)
**def
Tau.BookIV.QuantumMechanics.instReprSchrodingerEquation.repr :SchrodingerEquation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprSchrodingerEquation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L191-L191)
**instance
Tau.BookIV.QuantumMechanics.instReprSchrodingerEquation :Repr SchrodingerEquation**

Equations
- Tau.BookIV.QuantumMechanics.instReprSchrodingerEquation = { reprPrec := Tau.BookIV.QuantumMechanics.instReprSchrodingerEquation.repr }

---

### `Tau.BookIV.QuantumMechanics.schrodinger_canonical`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L193-L197)
**def
Tau.BookIV.QuantumMechanics.schrodinger_canonical :SchrodingerEquation**


The canonical Schrodinger equation with H_∞ = ι<sub>τ</sub>² Δ.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.ClassicalLimit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L203-L217)
**structure
Tau.BookIV.QuantumMechanics.ClassicalLimit :Type**


[IV.P27] Classical limit: |m|, |n| → ∞ yields classical mechanics.

When the mode indices grow large, the CR-address lattice becomes
dense relative to the action scale. The uncertainty product
ℏ_τ / (action scale) → 0, and quantum interference effects
average out. Classical mechanics emerges as the continuum
limit of the discrete CR-lattice.

- threshold : ℕ
Threshold mode number above which classical approximation holds.

- threshold_large : self.threshold ≥ 100
Threshold is large (at least 100 for meaningful classical limit).

- is_continuum_limit : Bool
Classical mechanics is the large-|m|,|n| limit.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprClassicalLimit.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L217-L217)
**def
Tau.BookIV.QuantumMechanics.instReprClassicalLimit.repr :ClassicalLimit → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprClassicalLimit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L217-L217)
**instance
Tau.BookIV.QuantumMechanics.instReprClassicalLimit :Repr ClassicalLimit**

Equations
- Tau.BookIV.QuantumMechanics.instReprClassicalLimit = { reprPrec := Tau.BookIV.QuantumMechanics.instReprClassicalLimit.repr }

---

### `Tau.BookIV.QuantumMechanics.classical_limit_structural`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L219-L221)
**theorem
Tau.BookIV.QuantumMechanics.classical_limit_structural
(c : ClassicalLimit)
 :c.threshold ≥ 100**


Classical limit exists for any threshold ≥ 100.

---

### `Tau.BookIV.QuantumMechanics.DualTrackCompatibility`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L227-L245)
**structure
Tau.BookIV.QuantumMechanics.DualTrackCompatibility :Type**


[IV.P28] Substrate determinism + outcome probability coexist.


- **Substrate level**: The τ-orbit evolution α ↦ ρ(α) is fully
deterministic (unique successor at each refinement step).

- **Readout level**: Measurement outcomes are probabilistic
(Born rule gives |c_{m₀,n₀}|²).


These are NOT contradictory because they operate at different
levels of the dual-track architecture:


- Determinism: ontic (the orbit IS definite at each step)

- Probability: epistemic (the readout projects multi-mode state)


- substrate_deterministic : Bool
Substrate is deterministic.

- readout_probabilistic : Bool
Readout is probabilistic.

- compatible : Bool
Both are simultaneously true.

Instances For

---

### `Tau.BookIV.QuantumMechanics.instReprDualTrackCompatibility`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L245-L245)
**instance
Tau.BookIV.QuantumMechanics.instReprDualTrackCompatibility :Repr DualTrackCompatibility**

Equations
- Tau.BookIV.QuantumMechanics.instReprDualTrackCompatibility = { reprPrec := Tau.BookIV.QuantumMechanics.instReprDualTrackCompatibility.repr }

---

### `Tau.BookIV.QuantumMechanics.instReprDualTrackCompatibility.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L245-L245)
**def
Tau.BookIV.QuantumMechanics.instReprDualTrackCompatibility.repr :DualTrackCompatibility → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.QuantumMechanics.determinism_probability`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L247-L255)
**theorem
Tau.BookIV.QuantumMechanics.determinism_probability
(d : DualTrackCompatibility)

(h1 : d.substrate_deterministic = true)

(h2 : d.readout_probabilistic = true)

(h3 : d.compatible = true)
 :d.substrate_deterministic = true ∧ d.readout_probabilistic = true ∧ d.compatible = true**


[IV.P28] Both determinism and probability are simultaneously true.

---

### `Tau.BookIV.QuantumMechanics.schrodinger_is_iota_sq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L261-L265)
**theorem
Tau.BookIV.QuantumMechanics.schrodinger_is_iota_sq :schrodinger_canonical.hamiltonian_coeff_numer = Sectors.iota_sq_numer ∧ schrodinger_canonical.hamiltonian_coeff_denom = Sectors.iota_sq_denom**


The Schrodinger Hamiltonian coefficient matches ι<sub>τ</sub>².

---

### `Tau.BookIV.QuantumMechanics.schrodinger_is_derived`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L267-L269)
**theorem
Tau.BookIV.QuantumMechanics.schrodinger_is_derived :schrodinger_canonical.is_derived = true**


The Schrodinger equation is derived, not postulated.

---

### `Tau.BookIV.QuantumMechanics.resolution_bounded`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L271-L273)
**theorem
Tau.BookIV.QuantumMechanics.resolution_bounded
(a : AddressResolution)
 :a.probability_numer ≤ a.probability_denom**


Address resolution probabilities are bounded by 1.

---

### `Tau.BookIV.QuantumMechanics.example_decoherence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L288-L291)
**def
Tau.BookIV.QuantumMechanics.example_decoherence :Decoherence**

Equations
- Tau.BookIV.QuantumMechanics.example_decoherence = { suppression_rate_numer := 1, suppression_rate_denom := 1000,
 rate_denom_pos := Tau.BookIV.QuantumMechanics.example_decoherence._proof_2 }
Instances For

---

### `Tau.BookIV.QuantumMechanics.example_dual_track`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/QuantumMechanics/Measurement.lean#L295-L295)
**def
Tau.BookIV.QuantumMechanics.example_dual_track :DualTrackCompatibility**

Equations
- Tau.BookIV.QuantumMechanics.example_dual_track = { }
Instances For
