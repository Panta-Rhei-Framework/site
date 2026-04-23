---
layout: taulib-doc
title: "TauLib.BookI.MetaLogic.OnticInvariance"
permalink: /verify/taulib/docs/book-i-meta-logic-ontic-invariance/
lane: verify
module_name: "TauLib.BookI.MetaLogic.OnticInvariance"
book: "I"
book_label: "Foundations"
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
    book: "Book I"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.MetaLogic.OnticInvariance


Ontic Identity Invariance theorem, No Identity Decoherence corollary,
and the Slippage Breaks Unique Omega theorem.

## Registry Cross-References


- [I.T46] Ontic Identity Invariance — `ontic_identity_invariance`

- [I.C03] No Identity Decoherence — `no_identity_decoherence`

- [I.T47] Slippage Breaks Unique Omega — `slippage_breaks_omega`


## Mathematical Content


The Ontic Identity Invariance theorem shows that τ's coherence kernel
preserves ontic identity at every construction step. The corollary
establishes that diagonal resonance cannot occur. The conditional theorem
shows identity slippage prevents unique omega internalization.

---

### `Tau.MetaLogic.BlockingMechanism`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L29-L34)
**inductive
Tau.MetaLogic.BlockingMechanism :Type**


[I.T46] The three mechanisms that block diagonal resonance in τ.

- k5_diagonal_discipline : BlockingMechanism
- nf_confluence : BlockingMechanism
- star_autonomous_structure : BlockingMechanism
Instances For

---

### `Tau.MetaLogic.instDecidableEqBlockingMechanism`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L34-L34)
**instance
Tau.MetaLogic.instDecidableEqBlockingMechanism :DecidableEq BlockingMechanism**

Equations
- Tau.MetaLogic.instDecidableEqBlockingMechanism x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.MetaLogic.instReprBlockingMechanism`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L34-L34)
**instance
Tau.MetaLogic.instReprBlockingMechanism :Repr BlockingMechanism**

Equations
- Tau.MetaLogic.instReprBlockingMechanism = { reprPrec := Tau.MetaLogic.instReprBlockingMechanism.repr }

---

### `Tau.MetaLogic.instReprBlockingMechanism.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L34-L34)
**def
Tau.MetaLogic.instReprBlockingMechanism.repr :BlockingMechanism → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.blocking_targets`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L36-L40)
**def
Tau.MetaLogic.blocking_targets :BlockingMechanism → ResonanceComponent**


Each blocking mechanism targets a specific resonance component.
Equations
- Tau.MetaLogic.blocking_targets Tau.MetaLogic.BlockingMechanism.k5_diagonal_discipline = Tau.MetaLogic.ResonanceComponent.L
- Tau.MetaLogic.blocking_targets Tau.MetaLogic.BlockingMechanism.nf_confluence = Tau.MetaLogic.ResonanceComponent.E
- Tau.MetaLogic.blocking_targets Tau.MetaLogic.BlockingMechanism.star_autonomous_structure = Tau.MetaLogic.ResonanceComponent.P
Instances For

---

### `Tau.MetaLogic.blocking_targets_injective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L42-L45)
**theorem
Tau.MetaLogic.blocking_targets_injective
(m1 m2 : BlockingMechanism)

(h : blocking_targets m1 = blocking_targets m2)
 :m1 = m2**


The blocking map is injective: each mechanism targets a distinct component.

---

### `Tau.MetaLogic.blocking_targets_surjective`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L47-L53)
**theorem
Tau.MetaLogic.blocking_targets_surjective
(c : ResonanceComponent)
 :∃ (m : BlockingMechanism), blocking_targets m = c**


The blocking map is surjective: every component has a blocker.

---

### `Tau.MetaLogic.allBlockingMechanisms`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L55-L57)
**def
Tau.MetaLogic.allBlockingMechanisms :List BlockingMechanism**


All blocking mechanisms enumerated.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.blocking_mechanism_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L59-L60)
**theorem
Tau.MetaLogic.blocking_mechanism_count :allBlockingMechanisms.length = 3**


There are exactly 3 blocking mechanisms.

---

### `Tau.MetaLogic.OnticIdentityInvariance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L66-L86)
**structure
Tau.MetaLogic.OnticIdentityInvariance :Type**


[I.T46] Ontic Identity Invariance: in the coherence kernel, every admissible
construction preserves ontic identity. Formalized as: τ has a blocker for
each resonance component, and its resonance profile is clean.

The proof packages together:

- K5 blocks (L) — contraction_present = false

- NF-confluence blocks (E) — equality_congruence = false

- Star-autonomous blocks (P) — self_products = false


- profile : DiagonalResonance
τ's resonance profile

- is_tau : self.profile = tau_resonance
The profile matches τ

- l_blocked : self.profile.contraction_present = false
(L) is blocked

- e_blocked : self.profile.equality_congruence = false
(E) is blocked

- p_blocked : self.profile.self_products = false
(P) is blocked

- all_blocked
(c : ResonanceComponent)
 : ∃ (m : BlockingMechanism), blocking_targets m = c
All three blocking mechanisms exist

Instances For

---

### `Tau.MetaLogic.ontic_identity_invariance`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L88-L95)
**def
Tau.MetaLogic.ontic_identity_invariance :OnticIdentityInvariance**


The theorem witness: τ satisfies all conditions.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.identityCoherenceLevel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L101-L106)
**def
Tau.MetaLogic.identityCoherenceLevel
(dr : DiagonalResonance)
 :ℕ**


Identity coherence level: 100% means no component of diagonal resonance is present.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.MetaLogic.tau_identity_coherence_100`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L108-L109)
**theorem
Tau.MetaLogic.tau_identity_coherence_100 :identityCoherenceLevel tau_resonance = 100**


τ has 100% identity coherence.

---

### `Tau.MetaLogic.orthodox_identity_coherence_0`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L111-L114)
**theorem
Tau.MetaLogic.orthodox_identity_coherence_0
(f : OrthodoxFoundation)
 :identityCoherenceLevel (orthodox_resonance f) = 0**


Orthodox foundations have 0% identity coherence (all three components present).

---

### `Tau.MetaLogic.no_identity_decoherence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L120-L123)
**theorem
Tau.MetaLogic.no_identity_decoherence :tau_resonance.isFullResonance = false**


[I.C03] No Identity Decoherence: the diagonal resonance pattern (L+E+P)
cannot occur at the ontic level in τ. Direct consequence of I.T46.

---

### `Tau.MetaLogic.no_partial_decoherence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L125-L130)
**theorem
Tau.MetaLogic.no_partial_decoherence :tau_resonance.contraction_present = false ∧ tau_resonance.equality_congruence = false ∧ tau_resonance.self_products = false**


Stronger form: no subset of the resonance components is present.

---

### `Tau.MetaLogic.UniqueOmegaCapability`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L136-L140)
**structure
Tau.MetaLogic.UniqueOmegaCapability :Type**


A foundation can internalize unique omega only if it has no identity slippage.

- resonance : DiagonalResonance
- no_resonance : self.resonance.isFullResonance = false
No full resonance (prerequisite for unique omega)

Instances For

---

### `Tau.MetaLogic.slippage_breaks_omega`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L146-L158)
**theorem
Tau.MetaLogic.slippage_breaks_omega
(dr : DiagonalResonance)

(h : dr.isFullResonance = true)
 :¬∃ (u : UniqueOmegaCapability), u.resonance = dr**


[I.T47] Slippage Breaks Unique Omega: a foundation with full diagonal
resonance cannot internalize a unique absolute infinity omega.

If identity slippage is present (full resonance = true), then
UniqueOmegaCapability is impossible for that resonance profile.

---

### `Tau.MetaLogic.tau_omega_capability`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L160-L163)
**def
Tau.MetaLogic.tau_omega_capability :UniqueOmegaCapability**


τ CAN internalize unique omega (because it has no resonance).
Equations
- Tau.MetaLogic.tau_omega_capability = { resonance := Tau.MetaLogic.tau_resonance, no_resonance := Tau.MetaLogic.tau_no_full_resonance }
Instances For

---

### `Tau.MetaLogic.orthodox_no_omega`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/MetaLogic/OnticInvariance.lean#L165-L168)
**theorem
Tau.MetaLogic.orthodox_no_omega
(f : OrthodoxFoundation)
 :¬∃ (u : UniqueOmegaCapability), u.resonance = orthodox_resonance f**


All orthodox foundations CANNOT internalize unique omega (full resonance).
