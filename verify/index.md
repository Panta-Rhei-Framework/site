---
layout: program-doc
title: "Verify"
lane: verify
permalink: /verify/
summary_short: "How to inspect, verify, and challenge the claims of the Panta Rhei Research Program — what can be checked, and what verification does not settle."
summary_cards:
  - title: "What can be checked"
    body: "Every theorem in TauLib compiles in Lean 4. Every quantitative prediction has an explicit formula. Every scope claim carries its epistemic label."
  - title: "What verification does not settle"
    body: "Compilation proves internal consistency, not truth about the physical world. Bridge claims remain conjectural until independently validated."
  - title: "How to start"
    body: "Clone TauLib, run lake build, and step through the guided tours. Or read the falsification pack for the decisive empirical tests."
right_rail:
  related:
    - title: "About the Research"
      url: /research-program/about/
    - title: "Key Results"
      url: /results/
    - title: "Registry"
      url: /registry/
  artifacts:
    - title: "TauLib (active)"
      url: "https://github.com/Panta-Rhei-Framework/taulib"
      external: true
    - title: "TauLib (frozen)"
      url: "https://github.com/Panta-Rhei-Framework/formalization"
      external: true
  meta:
    type: "Lane Root"
    scope: "All verification"
    status: "Canonical"
    updated: "April 2026"
---

## What Verification Means Here

The Panta Rhei Research Program distinguishes sharply between what can be formally verified and what remains open to scientific scrutiny.

### What can be checked now

- **Internal consistency**: Every theorem in TauLib compiles in Lean 4 with zero sorry in Books I-VI. Clone the repo, run `lake build`, and confirm.
- **Quantitative predictions**: Every numerical claim (α, m_n/m_e, ℓ₁, r, n_s) has an explicit formula derivable from ι_τ = 2/(π + e). Compute it yourself.
- **Scope labels**: Every claim carries one of four labels: established, τ-effective, conjectural, or metaphorical. The labels are enforced in the LaTeX source.
- **Dependency chains**: The registry tracks 4,547 objects with explicit dependency edges. Every theorem traces back to the seven axioms.

### What verification does not settle

- **Physical truth**: Compilation proves internal consistency. It does not prove the framework correctly describes reality. That requires empirical testing.
- **Bridge claims**: The identification between τ-internal results and classical mathematics is conjectural (via the Bridge Axiom). This is explicitly marked.
- **The decisive test**: CMB-S4 will measure the tensor-to-scalar ratio r. If r is inconsistent with ι_τ⁴ ≈ 0.0136, the framework's cosmological predictions fail.

### Verification routes

| Route | What it checks | Where |
|-------|---------------|-------|
| **TauLib build** | All 4,332 theorems compile | [github.com/Panta-Rhei-Framework/taulib](https://github.com/Panta-Rhei-Framework/taulib) |
| **Guided tours** | 8 interactive walkthroughs | `Tour/*.lean` in TauLib |
| **Hinge companions** | 49 structural hinges mapped to Lean | `Tour/GuidedTour/Book*.lean` in TauLib |
| **Falsification pack** | 220+ quantitative predictions | Book V, Chapter 56 |
| **Registry** | 4,547 objects with dependency graph | [Registry lane](/registry/) |

## The Right First Question

The right first question is not "should I already believe this?" The right first question is: **"is this a serious research program that has earned structured engagement?"**

To answer that, start here:
1. **Read** the [About the Research](/research-program/about/) overview
2. **Browse** the [Framework](/framework/about/) conceptual staircase
3. **Inspect** the [Registry](/registry/) for any theorem that interests you
4. **Run** `lake build` on TauLib to verify internal consistency
5. **Challenge** the [Results](/results/) with your domain expertise
