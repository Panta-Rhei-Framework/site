---
layout: program-doc
title: "TauLib"
permalink: /verify/taulib/
lane: verify
summary_short: "The Lean 4 formalization library for Category τ — 445 modules, 127,440 lines, 0 sorry across all 7 books of TauLib Lean source (scope tiered — see filter rules)."
summary_cards:
- title: "445 modules"
  body: "Across 7 books, covering kernel axioms through metaphysical boundary theorems."
- title: "4,332 theorems"
  body: "Machine-checked in Lean 4 with 3,721 computational evaluations."
- title: "0 sorry"
  body: "Zero across all 7 books of TauLib Lean source. The three prior Book VII methodological markers were retired in peer-review-fixes-v1 in favor of inspectable `def : Commitment` values. Book VI is registry-planned, not yet Lean-formalized — see [filter rules](/verify/filter-rules/)."
right_rail:
  related:
  - title: Verify Overview
    url: /verify/
  - title: Architecture
    url: /verify/taulib/architecture/
  - title: Formalization Status
    url: /verify/taulib/status/
  artifacts:
  - title: TauLib (contributor)
    url: https://github.com/Panta-Rhei-Research/taulib
    external: true
  - title: Formalization (frozen)
    url: https://github.com/Panta-Rhei-Research/formalization
    external: true
  meta:
    type: "Documentation Root"
    status: "Frozen"
    updated: "April 2026"
---

## What TauLib Is

TauLib is the **Lean 4 formalization library** for the Panta Rhei Research Program. It machine-checks the mathematical claims of the seven-book monograph series, providing an independent verification layer that anyone can inspect and run.

**Clone and build:**
```bash
git clone https://github.com/Panta-Rhei-Research/taulib
cd taulib && lake build
```

Build completes with **0 errors** and **0 sorry across all 7 books** — counted over the TauLib Lean corpus. Book VI has 30 Lean modules, none with `sorry`; Book VI's registry-level formalization is currently planned (0/168) and tracked separately — see [filter rules]({{ '/verify/filter-rules/' | relative_url }}).

## What TauLib Verifies

Lean compilation verifies **internal consistency**: every theorem follows from the axioms, every definition type-checks, every computation evaluates. This is a strong guarantee — but it is not the same as empirical truth.

**What Lean checks**: The mathematical derivation chain from K0-K6 through to every claimed theorem.

**What Lean does not check**: Whether the framework's physical predictions match experiment. That requires empirical testing.

## How TauLib Relates to the Books

Each TauLib module corresponds to a specific chapter or section in the monograph series:

| Book | Modules | Key content |
|------|--------:|-------------|
| I — Foundations | 94 | Kernel axioms, orbit structure, coordinates, polarity, boundary |
| II — Holomorphy | 65 | Interior, topology, geometry, Central Theorem, Hartogs |
| III — Spectrum | 70 | Enrichment, sectors, spectral theory, computation, Millennium doors |
| IV — Microcosm | 89 | Particle physics, QM, electroweak, QCD, nuclear |
| V — Macrocosm | 80 | Gravity, cosmology, BBN, black holes, fluid dynamics |
| VI — Life | 30 | Life definition, genetics, cellular, ecology, consciousness |
| VII — Metaphysics | 7 | Ontology, ethics, Logos, final boundary |
| Tours | 8 | Interactive verification tours for different audiences |

## Entry Points

### Documentation
- [API Documentation]({{ '/verify/taulib/docs/' | relative_url }}) — 445 module pages generated from Lean 4 source
- [Architecture]({{ '/verify/taulib/architecture/' | relative_url }}) — Module dependency graph and reading paths
- [Formalization Status]({{ '/verify/taulib/status/' | relative_url }}) — Per-book statistics, axiom inventory, sorry inventory
- [Scope Labels]({{ '/verify/taulib/scope-labels/' | relative_url }}) — The 4-tier scope classification system
- [Glossary]({{ '/verify/taulib/glossary/' | relative_url }}) — Technical terms and conventions

### Interactive Tours
- [VerifyItYourself](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/VerifyItYourself.lean) — 5 claims, verified live
- [Foundations](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/Foundations.lean) — Axioms and rigidity
- [CentralTheorem](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/CentralTheorem.lean) — O(τ³) ≅ A_spec(L)
- [Physics](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/Physics.lean) — 9 electroweak predictions

### Repositories
- [TauLib (contributor)](https://github.com/Panta-Rhei-Research/taulib) — Active development
- [Formalization (frozen)](https://github.com/Panta-Rhei-Research/formalization) — Frozen verification snapshot
