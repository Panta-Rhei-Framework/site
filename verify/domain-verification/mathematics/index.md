---
layout: program-doc
title: "Mathematics Verification"
permalink: /verify/domain-verification/mathematics/
lane: verify
v2_lane: verify
type: "Verification Surface"
verify_type: domain_verification
domain: mathematics
status: "Canonical"
summary_short: "Verification for the mathematical layer of the program."
right_rail:
  related:
    - title: "Formal Verification Stack"
      url: /verify/formal-verification-stack/
    - title: "TauLib"
      url: /verify/taulib/
    - title: "Corpus Registry"
      url: /corpus/registry/
    - title: "Mathematics Results"
      url: /results/topic/mathematics/
    - title: "Mathematics Recovery Requirements"
      url: /program/research-agenda/recovery-requirements/mathematics/
  meta:
    type: "Domain Verification"
    domain: "Mathematics"
    status: "Canonical"
    updated: "April 2026"
---

## Core Idea

At the mathematical level, verification focuses on internal formal consistency, mechanized proof validity, semantic alignment between Registry and Lean, selected theorem re-establishment in standard foundations, and adequacy of bridge claims into standard mathematics.

## Verification Levels

### Kernel Integrity Verification

Do the formal definitions and theorem dependencies close relative to the stated Lean formalization?

Evidence surfaces: [TauLib]({{ '/verify/taulib/' | relative_url }}), [Formalization Status]({{ '/verify/taulib/status/' | relative_url }}), [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}).

### Standard-Foundation Verification

Can selected hinge theorems be re-established in standard foundational settings or independently checked by specialists?

Evidence surfaces: hinge companion pages, formal-methods audit routes, and selected Corpus objects.

### Bridge Verification

Do recovery and transfer claims into standard mathematics support the use being made of them?

Evidence surfaces: [Custom Axiom Inventory]({{ '/verify/custom-axioms/' | relative_url }}), [TCB Disclosure]({{ '/verify/tcb/' | relative_url }}), Corpus dependencies, and bridge-specific review.

## Accountability Statement

Any theorem claimed as formally certified is certified only in the precise sense stated: relative to the relevant proof infrastructure, declared assumptions, and scope of formalization.

Mathematical verification can establish internal proof discipline. It does not by itself settle bridge adequacy into every standard foundation, external review, or the program's physics/life/metaphysics consequences.
