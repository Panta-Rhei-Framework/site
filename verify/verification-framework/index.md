---
layout: program-doc
title: "Verification Framework"
permalink: /verify/verification-framework/
lane: verify
v2_lane: verify
type: "Verification Surface"
verify_type: verification_framework
status: "Canonical"
summary_short: "What verification means in this program, and why it is not the same across all layers of the work."
plain_language_summary: "'Verified' means different things in different domains. A mathematical theorem is verified by a machine-checked proof. A physical prediction is verified when an experiment matches it. A biological claim is verified by a biomarker measurement. A metaphysical claim is verified by living-experience instantiation. This framework page names those four verification modes, explains why the program refuses to collapse them into a single criterion, and lays out the shared discipline (explicitness, traceability, derivability, domain-appropriate validation) that holds the whole structure together."
summary_cards:
  - title: "Many modes"
    body: "Formal proof, bridge adequacy, empirical accountability, and interpretive coherence are separate burdens."
  - title: "Shared discipline"
    body: "Every mode still requires explicitness, traceability, consistency, inspectability, and accountability."
  - title: "Layer-aware"
    body: "Mathematics, physics, life, and metaphysics require different validation standards."
right_rail:
  related:
    - title: "Scientific Rigor"
      url: /verify/scientific-rigor/
    - title: "Formal Verification Stack"
      url: /verify/formal-verification-stack/
    - title: "Domain Verification"
      url: /verify/domain-verification/
    - title: "Assessment Protocols"
      url: /verify/assessment-protocols/
  meta:
    type: "Verification Framework"
    status: "Canonical"
    updated: "April 2026"
---

## What Verification Means Here

This program does not flatten verification into a single notion of proof. A Lean theorem, a bridge statement, a numerical prediction, a life-science explanation, and a metaphysical analysis do not carry the same evidential burden.

## Shared Verification Principles

- **Explicitness:** the claim and its scope must be named.
- **Traceability:** the reader should be able to move from result to Corpus support and, where available, TauLib support.
- **Consistency:** public pages, manifests, and generated artifacts should not silently disagree.
- **Derivability:** formal and mathematical claims must expose their derivation burden.
- **Inspectability:** critical artifacts should be public and stable enough to audit.
- **Accountability:** standards and failure modes must be stated before the result is defended.
- **Domain-appropriate validation:** physics, life, and metaphysics cannot be verified by proof syntax alone.

## Why Verification Differs by Layer

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/verify/domain-verification/mathematics/' | relative_url }}">
    <strong>Mathematics</strong>
    <span>Formal consistency, mechanized proofs, standard-foundation robustness, and bridge adequacy.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/domain-verification/physics/' | relative_url }}">
    <strong>Physics</strong>
    <span>Structural derivation, empirical fit, prediction timing, falsification, and measurement bridges.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/domain-verification/life/' | relative_url }}">
    <strong>Life</strong>
    <span>Explanatory adequacy, biological constraints, structural necessity, and scope discipline.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/domain-verification/metaphysics/' | relative_url }}">
    <strong>Metaphysics</strong>
    <span>Ontological coherence, phenomenological adequacy, boundary conditions, and explicit commitment limits.</span>
  </a>
</div>

## Verification Stack Preview

Verification then routes into six concrete surfaces:

- [Formal Verification Stack]({{ '/verify/formal-verification-stack/' | relative_url }})
- [Construction Spine Verification]({{ '/verify/construction-spine-verification/' | relative_url }})
- [Domain Verification]({{ '/verify/domain-verification/' | relative_url }})
- [Predictions & Falsification]({{ '/verify/predictions-and-falsification/' | relative_url }})
- [Assessment Protocols]({{ '/verify/assessment-protocols/' | relative_url }})
- [How to Verify]({{ '/verify/how-to-verify/' | relative_url }})
