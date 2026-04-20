---
layout: program-doc
title: "Verify"
lane: verify
permalink: /verify/
summary_short: "How to inspect, verify, and challenge the claims of the Panta Rhei Research Program — what can be checked, and what verification does not settle."
hero_ctas:
  - label: "Browse TauLib (Lean 4)"
    url: "https://taulib.site/docs/"
    variant: lean
  - label: "Release Manifest"
    url: /verify/release-manifest/
  - label: "Formalization Status"
    url: /verify/taulib/status/
hero_supporting_line: "445 Lean 4 modules · 127,440 lines · 4,332 machine-checked theorems · 0 sorry across all 7 books (TauLib Lean corpus; scope tiered — see [filter rules](/verify/filter-rules/)) · 3 conjectural axioms · Mathlib for tactics only."
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
    - title: "Claims"
      url: /results/
    - title: "Registry"
      url: /registry/
  artifacts:
    - title: "TauLib Docs"
      url: "https://taulib.site/"
      external: true
    - title: "TauLib Source (Apache-2.0)"
      url: "https://github.com/Panta-Rhei-Research/taulib"
      external: true
    - title: "License (Apache-2.0)"
      url: "https://github.com/Panta-Rhei-Research/taulib/blob/main/LICENSE"
      external: true
    - title: "TauLib (frozen)"
      url: "https://github.com/Panta-Rhei-Research/formalization"
      external: true
  meta:
    type: "Lane Root"
    scope: "All verification"
    status: "Canonical"
    updated: "April 2026"
---

## What Verification Means Here

The Panta Rhei Research Program distinguishes sharply between what can be formally verified and what remains open to scientific scrutiny.

**Licensing.** **TauLib**: Apache-2.0. **Site prose and predictions**: CC BY 4.0. Both licenses permit inspection and reuse with attribution.

### What can be checked now

- **Internal consistency**: Every theorem in TauLib compiles in Lean 4 with zero sorry across all 7 books. Clone the repo, run `lake build`, and confirm. — counted over the TauLib Lean source; Book VI has 30 Lean modules, none with `sorry`, but Book VI registry-level formalization is currently planned (0/168). See [filter rules]({{ '/verify/filter-rules/' | relative_url }}).
- **Quantitative predictions**: Every numerical claim (α, m_n/m_e, ℓ₁, r, n_s) has an explicit formula derivable from ι<sub>τ</sub> = 2/(π + e). Compute it yourself.
- **Scope labels**: Every claim carries one of four labels: established, τ-effective, conjectural, or metaphorical. The labels are enforced in the LaTeX source.
- **Dependency chains**: The registry tracks 4,547 objects with explicit dependency edges. Every theorem traces back to the seven axioms.

### What verification does not settle

- **Physical truth**: Compilation proves internal consistency. It does not prove the framework correctly describes reality. That requires empirical testing.
- **Bridge claims**: The identification between τ-internal results and classical mathematics is conjectural (via the Bridge Axiom). This is explicitly marked.
- **The decisive test**: CMB-S4 will measure the tensor-to-scalar ratio r. If r is inconsistent with ι<sub>τ</sub>⁴ ≈ 0.0136, the framework's cosmological predictions fail.

### Verification routes

| Route | What it checks | Where |
|-------|---------------|-------|
| **TauLib build** | All 4,332 theorems compile | [github.com/Panta-Rhei-Research/taulib](https://github.com/Panta-Rhei-Research/taulib) |
| **Guided tours** | 8 interactive walkthroughs | `Tour/*.lean` in TauLib |
| **Hinge companions** | 49 structural hinges mapped to Lean | `Tour/GuidedTour/Book*.lean` in TauLib |
| **Falsification pack** | 220+ quantitative predictions | Book V, Chapter 56 |
| **Registry** | 4,547 objects with dependency graph | [Registry lane]({{ '/registry/' | relative_url }}) |

## TauLib Documentation

The canonical documentation for TauLib is now integrated into this site:

- **[Release Manifest]({{ '/verify/release-manifest/' | relative_url }})** — Single authoritative snapshot: pinned commit, build status, axiom inventory, per-book reconciliation across registry / dashboards / TauLib docs
- **[Filter Rules]({{ '/verify/filter-rules/' | relative_url }})** — Authoritative manifest of which count means what across the site (registry root, dashboard display, TauLib modules) — makes apparent drift legible as a filter choice
- **[Custom Axiom Inventory]({{ '/verify/custom-axioms/' | relative_url }})** — Honest accounting of the 3 custom axiom declarations beyond Mathlib: what each axiom says, what finite computation motivates it, what universal step is axiomatized, what closes the gap
- **[Trust Budget and TCB Disclosure]({{ '/verify/tcb/' | relative_url }})** — What Lean's kernel trusts, and what TauLib extends it by via `native_decide` (`Lean.ofReduceBool`, `Lean.trustCompiler`) — including the Book II Central Theorem dependency chain
- **[TauLib Overview]({{ '/verify/taulib/' | relative_url }})** — What TauLib is, how to use it, entry routes
- **[Architecture]({{ '/verify/taulib/architecture/' | relative_url }})** — Module dependency graph and reading paths by audience
- **[Formalization Status]({{ '/verify/taulib/status/' | relative_url }})** — Per-book statistics, axiom inventory, sorry inventory
- **[Scope Labels]({{ '/verify/taulib/scope-labels/' | relative_url }})** — The 4-tier scope classification system
- **[Glossary]({{ '/verify/taulib/glossary/' | relative_url }})** — Constants, generators, structures, registry format

## AI-Assisted Assessment Protocols

For readers, critics, journalists, policymakers, and domain specialists who want a structured first signal before investing deeper human time, we provide a public assessment protocol:

- **[Assessment Overview]({{ '/verify/assessments/' | relative_url }})** — What the protocol is, who it is for, how to start
- **[Methodology]({{ '/verify/assessments/methodology/' | relative_url }})** — Why AI-assisted triage, what it can and cannot do
- **[Three-Gate Rubric]({{ '/verify/assessments/three-gate-rubric/' | relative_url }})** — 17 criteria across legitimacy, novelty, and impact
- **[Series-Level Prompt]({{ '/verify/assessments/series-assessment/' | relative_url }})** — Assess the entire 7-book architecture
- **[Book-Level Prompt]({{ '/verify/assessments/book-assessment/' | relative_url }})** — Assess a single book in depth
- **[Domain-Expert Prompt]({{ '/verify/assessments/domain-assessment/' | relative_url }})** — Assess from a specific disciplinary perspective
- **[Reviewer Workflow]({{ '/verify/assessments/reviewer-workflow/' | relative_url }})** — 8-step process from prompt to dossier
- **[Dossier Schema]({{ '/verify/assessments/dossier-schema/' | relative_url }})** — Structured output format
- **[Scorecard]({{ '/verify/assessments/scorecard/' | relative_url }})** — Downloadable scoring template

> **Note.** This protocol is a first-pass assessment method, not a substitute for peer review, expert adjudication, or formal proof checking. It is designed to answer: *"Is this worth serious human attention, and where should that attention go?"*

## The Right First Question

The right first question is not "should I already believe this?" The right first question is: **"is this a serious research program that has earned structured engagement?"**

To answer that, start here:
1. **Read** the [About the Research]({{ '/research-program/about/' | relative_url }}) overview
2. **Browse** the [Framework]({{ '/framework/about/' | relative_url }}) conceptual staircase
3. **Inspect** the [Registry]({{ '/registry/' | relative_url }}) for any theorem that interests you
4. **Run** `lake build` on TauLib to verify internal consistency
5. **Challenge** the [Results]({{ '/results/' | relative_url }}) with your domain expertise
6. **Assess** using the [AI-assisted protocol]({{ '/verify/assessments/' | relative_url }}) for a structured first signal

## Report Corrections

Found an error, a broken proof, a mis-stated numerical value, or a scope-label issue? We take corrections seriously and credit corrigendum contributors in the changelog.

**Email**: [errata@panta-rhei.site](mailto:errata@panta-rhei.site)

For formal peer-review coordination or institutional review inquiries: [review@panta-rhei.site](mailto:review@panta-rhei.site)
