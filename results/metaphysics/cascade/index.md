---
layout: program-doc
title: "Metaphysics Architecture — Reg_E/P/D/C + OR1–OR6"
permalink: /results/metaphysics/cascade/
lane: results
v2_lane: results
type: "Architecture Page"
status: "Canonical"
domain: metaphysics
summary_short: "Categorical-only architecture: four-register backbone (Empirical / Practical / Diagrammatic / Commitment) plus the six ontic-requirement narrowing rules. No empirical anchor — concepts instantiate as lived experience."
---

The metaphysics glossary has **no single empirical anchor** like physics's `PG-P01-neutron` or life's `LG-Y02`. Metaphysics is **categorical-only**: its concepts instantiate as lived-experience correlates, narrative examples, and ethical/proof-theoretic content rather than as numerical measurements.

What it has instead is an **architectural backbone**: the four canonical readout registers (Reg_E/P/D/C) plus the six original-rule narrowing principles (OR1–OR6). Every metaphysics glossary entry derives from this architecture.

## The four-register backbone

```
                            ╭────────────────╮
                            │  τ (kernel)    │
                            ╰────────┬───────╯
                                     │
              ┌──────────┬───────────┼──────────┬──────────┐
              ▼          ▼           ▼          ▼
         ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
         │ Reg_E   │ │ Reg_P   │ │ Reg_D   │ │ Reg_C   │
         │ → Obs   │ │ → Norm  │ │ → Proof │ │ → Stance│
         │ MG-R01  │ │ MG-R02  │ │ MG-R03  │ │ MG-R04  │
         └─────────┘ └─────────┘ └─────────┘ └─────────┘
              │          │           │          │
              ▼          ▼           ▼          ▼
        Empirical    Practical   Diagrammatic Commitment
        sector S_E   sector S_P  sector S_D   sector S_C
```

Each register reads a *different aspect* of τ-categorical reality:

- **Reg_E** (Empirical) → **Obs**: falsifiable observations (every physics measurement, every life biomarker)
- **Reg_P** (Practical) → **Norm**: normative content (ethical / legal / social judgments)
- **Reg_D** (Diagrammatic) → **Proof**: proof-theoretic content (mathematical theorems, logical inferences)
- **Reg_C** (Commitment) → **Stance**: stance-based content (promises, character, dignity)

## The OR1–OR6 narrowing principles

The Six Ontic Requirements (`VII.D37`) are the structural constraints that any candidate ontic reality must satisfy:

| # | Name | Constraint |
|---|---|---|
| OR1 | Self-coherence | No internal contradictions |
| OR2 | Completeness | Every required morphism is present |
| OR3 | Generativity | Structure can be extended consistently |
| OR4 | Independence | Each requirement is independently necessary (`VII.P08`) |
| OR5 | Continuity | Adjacent τ-states connect via valid morphisms |
| OR6 | Stability | The system tolerates perturbation |

The narrowing lemmas (`VII.L31`, `VII.L32`, `VII.L33`) prove that combinations of these requirements progressively constrain the space of possible ontic realities to the τ-categorical kernel.

## How the architecture replaces a calibration cascade

Physics's cascade traces *numerical* values from `ι_τ + m_n` to every constant. Metaphysics's architecture traces *categorical* claims through registers and narrowing rules:

```
τ-categorical claim
   ↓ (apply OR1–OR6 narrowing)
candidate-survival check
   ↓ (route to appropriate register)
Reg_E (empirical) | Reg_P (normative) | Reg_D (proof) | Reg_C (commitment)
   ↓ (rendered into the codomain)
Obs / Norm / Proof / Stance
   ↓ (instantiated phenomenologically)
lived experience, ethical practice, proof artifact, committed stance
```

Every metaphysics glossary entry's `phenomenological_correlate` field is the description of HOW that concept lands in lived experience after passing through this architecture.

## Glossary anchors

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/results/metaphysics/glossary/MG-R01-empirical-register/' | relative_url }}">
    <strong>MG-R01 · Empirical Register (Reg_E)</strong>
    <span>The empirical-bridge register. Image-codomain Obs. Anchors physics + life observations into the metaphysical architecture.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/metaphysics/glossary/MG-P01-or1-self-coherence/' | relative_url }}">
    <strong>MG-P01 · OR1 Self-Coherence</strong>
    <span>The first narrowing rule. No candidate ontic structure can carry an internal contradiction.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/metaphysics/glossary/MG-A01-ci-operator-graph/' | relative_url }}">
    <strong>MG-A01 · CI Operator Graph</strong>
    <span>The architecture connecting causal claims to their commitments across registers.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/metaphysics/glossary/MG-O01-being/' | relative_url }}">
    <strong>MG-O01 · Being</strong>
    <span>Being as cross-register categorical existence — the deepest ontological commitment.</span>
  </a>
</div>

## Why no calibration anchor?

The metaphysics glossary's contract is **categorical-only**: an entry has structure (`tau_definition`, `tau_derivation`) and lived-experience instantiation (`phenomenological_correlate`), but **no calibration anchor**. The validator (`scripts/validate_glossary.py`) enforces this — metaphysics entries that carry a `calibration_anchor` field fail validation.

This is by design. Metaphysical concepts (being, dignity, qualia, free-will) do not have numerical values. They have register codomains (where they live in the architecture) and instantiations (how they show up in lived experience).

## Read next

- [Metaphysics glossary]({{ '/results/metaphysics/glossary/' | relative_url }}) — all 68 entries across 6 categories
- [Physics cascade]({{ '/results/physics/cascade/' | relative_url }}) — for the linear numerical analog
- [Life cascade]({{ '/results/life/cascade/' | relative_url }}) — for the multi-branch tree analog

## Provenance

This is a Jekyll surface of the canonical corpus document at `corpus/metaphysics-glossary/architecture.md`. The corpus version is the source of truth; this page is a curated rendering for the public-facing site.
