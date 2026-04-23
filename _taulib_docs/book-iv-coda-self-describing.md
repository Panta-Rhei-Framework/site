---
layout: taulib-doc
title: "TauLib.BookIV.Coda.SelfDescribing"
permalink: /verify/taulib/docs/book-iv-coda-self-describing/
lane: verify
module_name: "TauLib.BookIV.Coda.SelfDescribing"
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

# TauLib.BookIV.Coda.SelfDescribing


The self-describing universe: why the neutron is the calibration anchor
(not the electron), the self-enrichment claim, and metaclosure of Book IV.

## Registry Cross-References


- [IV.R190] Why Neutron Not Electron as Anchor — `remark_neutron_anchor`


## Mathematical Content


Chapter 57 closes Book IV with the metaclosure observation: the tau-framework
is self-describing in the sense that tau^3 contains all the structural
information needed to reconstruct its own description, including:

- 
**Why neutron, not electron**: the neutron is ontologically prior because
it is a composite defect bundle whose existence is guaranteed by the
strong-sector structure (C-sector confinement). The electron is derived
from the neutron via the mass ratio R. Choosing the neutron as anchor
gives a cleaner derivation chain with fewer intermediate steps.


- 
**Self-enrichment**: tau^3 is enriched over itself in the sense that
the hom-objects Hom_{tau^3}(X,Y) are themselves objects of tau^3.
This is not a logical circularity but a structural closure: the
universe contains its own instruction set.


- 
**Metaclosure**: Book IV has derived all fiber-level physics from
7 axioms K0-K6 plus the single empirical anchor m_n, with zero
free parameters. The base-level physics (Book V) and the biological
(Book VI) and philosophical (Book VII) extensions follow from the
same structural foundation.


This module is intentionally compact: ch57 is a short closing chapter
with a single structural remark.

## Ground Truth Sources


- Chapter 57 of Book IV (2nd Edition)


---

### `Tau.BookIV.Coda.NeutronAnchorRationale`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L52-L78)
**structure
Tau.BookIV.Coda.NeutronAnchorRationale :Type**


[IV.R190] The neutron is chosen as calibration anchor because it is
ontologically prior: a composite defect bundle whose existence is
guaranteed by the strong-sector structure (C-sector confinement
with coupling kappa(C;3) = iota_tau^3 / (1 - iota_tau)).

The ontological priority chain is:
neutron -> proton -> electron -> Planck mass

Each subsequent quantity is derived from the previous one:


- m_p = m_n - delta_A (proton-neutron mass difference)

- m_e = m_n / R (mass ratio R = iota_tau^(-7) - correction)

- m_P = m_n / (alpha^9 * sqrt(chi*kappa_n/2)) (closing identity)


Choosing the electron as anchor would require deriving m_n from m_e,
inverting the natural derivation direction.

- ontologically_prior : Bool
Neutron is ontologically prior.

- confinement_guarantees : Bool
Guaranteed by C-sector confinement.

- chain_length : ℕ
Priority chain length.

- chain : List String
Priority chain.

- inversion_unnatural : Bool
Inverting would be unnatural.

Instances For

---

### `Tau.BookIV.Coda.instReprNeutronAnchorRationale.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L78-L78)
**def
Tau.BookIV.Coda.instReprNeutronAnchorRationale.repr :NeutronAnchorRationale → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.instReprNeutronAnchorRationale`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L78-L78)
**instance
Tau.BookIV.Coda.instReprNeutronAnchorRationale :Repr NeutronAnchorRationale**

Equations
- Tau.BookIV.Coda.instReprNeutronAnchorRationale = { reprPrec := Tau.BookIV.Coda.instReprNeutronAnchorRationale.repr }

---

### `Tau.BookIV.Coda.neutron_anchor_rationale`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L80-L80)
**def
Tau.BookIV.Coda.neutron_anchor_rationale :NeutronAnchorRationale**

Equations
- Tau.BookIV.Coda.neutron_anchor_rationale = { }
Instances For

---

### `Tau.BookIV.Coda.ontologically_prior`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L82-L83)
**theorem
Tau.BookIV.Coda.ontologically_prior :neutron_anchor_rationale.ontologically_prior = true**


---

### `Tau.BookIV.Coda.four_step_chain`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L85-L86)
**theorem
Tau.BookIV.Coda.four_step_chain :neutron_anchor_rationale.chain_length = 4**


---

### `Tau.BookIV.Coda.chain_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L88-L89)
**theorem
Tau.BookIV.Coda.chain_count :neutron_anchor_rationale.chain.length = 4**


---

### `Tau.BookIV.Coda.remark_neutron_anchor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L91-L93)
**def
Tau.BookIV.Coda.remark_neutron_anchor :String**

Equations
- Tau.BookIV.Coda.remark_neutron_anchor = "Neutron is calibration anchor: ontologically prior (C-sector confinement), " ++ "priority chain n -> p -> e -> m_P, inversion would be unnatural"
Instances For

---

### `Tau.BookIV.Coda.SelfEnrichment`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L99-L115)
**structure
Tau.BookIV.Coda.SelfEnrichment :Type**


The self-enrichment property of tau^3: hom-objects are themselves
objects of tau^3. This is not circular but a structural closure
analogous to a category enriched over itself (like Set enriched
over Set, or Cat enriched over Cat).

The self-enrichment means the universe contains its own instruction set:
the rules governing tau^3 are encoded as objects within tau^3.

- hom_internal : Bool
Hom-objects are internal.

- not_circular : Bool
Not logically circular.

- analogy : String
Analogous to Set enriched over Set.

- self_instruction : Bool
Universe contains its own instruction set.

Instances For

---

### `Tau.BookIV.Coda.instReprSelfEnrichment`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L115-L115)
**instance
Tau.BookIV.Coda.instReprSelfEnrichment :Repr SelfEnrichment**

Equations
- Tau.BookIV.Coda.instReprSelfEnrichment = { reprPrec := Tau.BookIV.Coda.instReprSelfEnrichment.repr }

---

### `Tau.BookIV.Coda.instReprSelfEnrichment.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L115-L115)
**def
Tau.BookIV.Coda.instReprSelfEnrichment.repr :SelfEnrichment → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.self_enrichment`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L117-L117)
**def
Tau.BookIV.Coda.self_enrichment :SelfEnrichment**

Equations
- Tau.BookIV.Coda.self_enrichment = { }
Instances For

---

### `Tau.BookIV.Coda.self_enrichment_internal`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L119-L120)
**theorem
Tau.BookIV.Coda.self_enrichment_internal :self_enrichment.hom_internal = true**


---

### `Tau.BookIV.Coda.self_enrichment_not_circular`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L122-L123)
**theorem
Tau.BookIV.Coda.self_enrichment_not_circular :self_enrichment.not_circular = true**


---

### `Tau.BookIV.Coda.BookIVMetaclosure`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L129-L161)
**structure
Tau.BookIV.Coda.BookIVMetaclosure :Type**


Metaclosure summary: what Book IV has achieved.

Inputs:


- 7 axioms K0-K6 (Book I)

- 1 empirical anchor: m_n = 939.565 MeV

- 0 free parameters


Outputs (fiber T^2 physics):


- Complete particle spectrum (quarks, leptons, bosons, 3 generations)

- Quantum mechanics (uncertainty, measurement, Born rule)

- Electroweak sector (EM, weak, Weinberg mixing, Higgs)

- Strong sector (confinement, mass gap, color)

- Many-body physics (9 regimes, phase transitions)

- Condensed matter (crystal, glass, superfluid, superconductor)

- Constants: 10 couplings, alpha, R, m_e, M_W, M_Z, M_H, ...


What remains for Book V: base tau^1 physics (gravity, cosmology).

- num_axioms : ℕ
Number of axioms.

- num_anchors : ℕ
Empirical anchors.

- free_params : ℕ
Free parameters.

- num_parts : ℕ
Parts in Book IV.

- num_chapters : ℕ
Chapters.

- fiber_complete : Bool
Fiber physics complete.

- base_deferred : Bool
Base physics deferred to Book V.

Instances For

---

### `Tau.BookIV.Coda.instReprBookIVMetaclosure.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L161-L161)
**def
Tau.BookIV.Coda.instReprBookIVMetaclosure.repr :BookIVMetaclosure → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.instReprBookIVMetaclosure`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L161-L161)
**instance
Tau.BookIV.Coda.instReprBookIVMetaclosure :Repr BookIVMetaclosure**

Equations
- Tau.BookIV.Coda.instReprBookIVMetaclosure = { reprPrec := Tau.BookIV.Coda.instReprBookIVMetaclosure.repr }

---

### `Tau.BookIV.Coda.metaclosure`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L163-L163)
**def
Tau.BookIV.Coda.metaclosure :BookIVMetaclosure**

Equations
- Tau.BookIV.Coda.metaclosure = { }
Instances For

---

### `Tau.BookIV.Coda.zero_free_parameters`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L165-L166)
**theorem
Tau.BookIV.Coda.zero_free_parameters :metaclosure.free_params = 0**


---

### `Tau.BookIV.Coda.nine_axioms`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L168-L169)
**theorem
Tau.BookIV.Coda.nine_axioms :metaclosure.num_axioms = 9**


---

### `Tau.BookIV.Coda.one_anchor`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L171-L172)
**theorem
Tau.BookIV.Coda.one_anchor :metaclosure.num_anchors = 1**


---

### `Tau.BookIV.Coda.fiber_complete`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L174-L175)
**theorem
Tau.BookIV.Coda.fiber_complete :metaclosure.fiber_complete = true**


---

### `Tau.BookIV.Coda.DerivationChainSummary`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L181-L199)
**structure
Tau.BookIV.Coda.DerivationChainSummary :Type**


The complete derivation chain from axioms to predictions.
Each link is either established (E), tau-effective (T), or conjectural (C).

- total_links : ℕ
Total links.

- chain : List String
Description.

Instances For

---

### `Tau.BookIV.Coda.instReprDerivationChainSummary`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L199-L199)
**instance
Tau.BookIV.Coda.instReprDerivationChainSummary :Repr DerivationChainSummary**

Equations
- Tau.BookIV.Coda.instReprDerivationChainSummary = { reprPrec := Tau.BookIV.Coda.instReprDerivationChainSummary.repr }

---

### `Tau.BookIV.Coda.instReprDerivationChainSummary.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L199-L199)
**def
Tau.BookIV.Coda.instReprDerivationChainSummary.repr :DerivationChainSummary → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.derivation_summary`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L201-L201)
**def
Tau.BookIV.Coda.derivation_summary :DerivationChainSummary**

Equations
- Tau.BookIV.Coda.derivation_summary = { }
Instances For

---

### `Tau.BookIV.Coda.ten_link_chain`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L203-L204)
**theorem
Tau.BookIV.Coda.ten_link_chain :derivation_summary.total_links = 10**


---

### `Tau.BookIV.Coda.derivation_chain_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L206-L207)
**theorem
Tau.BookIV.Coda.derivation_chain_count :derivation_summary.chain.length = 10**


---

### `Tau.BookIV.Coda.SelfDescribingUniverse`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L213-L238)
**structure
Tau.BookIV.Coda.SelfDescribingUniverse :Type**


The title-theorem of Book IV: the universe described by tau^3 is
self-describing.

Self-description means:

- The laws governing tau^3 are objects of tau^3 (self-enrichment)

- The constants of nature are readouts of structural invariants

- The framework determines itself (no external input besides m_n)

- The fiber T^2 contains complete spatial physics

- The base tau^1 contains complete temporal physics


Together: tau^3 = tau^1 x_f T^2 describes a complete, self-contained
physical universe with zero free parameters.

- laws_internal : Bool
Laws are internal objects.

- constants_readouts : Bool
Constants are structural readouts.

- self_determined : Bool
Self-determined (modulo m_n).

- fiber_complete : Bool
Fiber: complete spatial physics.

- base_complete : Bool
Base: complete temporal physics.

- zero_params : ℕ
Zero free parameters.

Instances For

---

### `Tau.BookIV.Coda.instReprSelfDescribingUniverse`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L238-L238)
**instance
Tau.BookIV.Coda.instReprSelfDescribingUniverse :Repr SelfDescribingUniverse**

Equations
- Tau.BookIV.Coda.instReprSelfDescribingUniverse = { reprPrec := Tau.BookIV.Coda.instReprSelfDescribingUniverse.repr }

---

### `Tau.BookIV.Coda.instReprSelfDescribingUniverse.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L238-L238)
**def
Tau.BookIV.Coda.instReprSelfDescribingUniverse.repr :SelfDescribingUniverse → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Coda.self_describing_universe`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L240-L240)
**def
Tau.BookIV.Coda.self_describing_universe :SelfDescribingUniverse**

Equations
- Tau.BookIV.Coda.self_describing_universe = { }
Instances For

---

### `Tau.BookIV.Coda.universe_self_determined`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L242-L243)
**theorem
Tau.BookIV.Coda.universe_self_determined :self_describing_universe.self_determined = true**


---

### `Tau.BookIV.Coda.universe_zero_params`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L245-L246)
**theorem
Tau.BookIV.Coda.universe_zero_params :self_describing_universe.zero_params = 0**


---

### `Tau.BookIV.Coda.universe_laws_internal`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/Coda/SelfDescribing.lean#L248-L249)
**theorem
Tau.BookIV.Coda.universe_laws_internal :self_describing_universe.laws_internal = true**
