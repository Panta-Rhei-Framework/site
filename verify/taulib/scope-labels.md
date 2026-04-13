---
layout: program-doc
title: "Scope Labels"
permalink: /verify/taulib/scope-labels/
lane: verify
summary_short: "The 4-tier scope discipline classifying every mathematical claim in TauLib."
right_rail:
  related:
  - title: TauLib Overview
    url: /verify/taulib/
  - title: Formalization Status
    url: /verify/taulib/status/
  meta:
    type: "Documentation"
    status: "Frozen"
    updated: "April 2026"
---

## The Four Tiers

TauLib uses a 4-tier scope discipline to classify every mathematical claim. This system, introduced in Book III, ensures transparent epistemic status throughout the formalization.

### Established

Classical mathematics that is independently verified and widely accepted. These results do not depend on Category tau — they are standard theorems formalized within the tau framework.

**Example:** The Chinese Remainder Theorem (`BookI/Polarity/ChineseRemainder.lean`)

### tau-Effective

Quantitative predictions derived within the Category tau framework. These are the core results — formulas that produce specific numerical values from the master constant iota_tau and structural parameters, testable against experimental data.

**Example:** CMB first peak at l_1 = 220.6 with +69 ppm accuracy (`BookV/Cosmology/CMBSpectrum.lean`)

### Conjectural

Structural claims that are not yet derived from the axioms. Computationally verified at all tested finite bounds, but the infinite-limit assertion remains unproven. TauLib marks these with explicit `axiom` declarations.

**Example:** The bridge functor existence axiom (`BookIII/Bridge/BridgeAxiom.lean`) — all finite checks pass; the axiom asserts the infinite extension.

### Metaphorical

Philosophical or analogical extensions where formal mathematics meets lived experience. These mark the boundary between what can be formalized and what requires interpretation.

**Example:** The Categorical Imperative proof programme (`BookVII/Ethics/CIProof.lean`) — formalized as a j-closed fixed point, but its ethical content transcends the formalism.

## How Scope Labels Appear

- **Module docstrings** — each module header notes its dominant scope tier
- **Registry cross-references** — entries like `[IV.T140]` carry scope in the registry files
- **Axiom declarations** — the 3 conjectural axioms are explicitly labeled in their docstrings

## The Conjectural Boundary

The conjectural axioms follow a "compute-then-axiomatize" pattern: a decidable finite check function is verified computationally via `native_decide`, then an axiom asserts the property holds universally. This makes the conjectural boundary maximally transparent.
