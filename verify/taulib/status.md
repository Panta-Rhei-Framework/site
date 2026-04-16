---
layout: program-doc
title: "Formalization Status"
permalink: /verify/taulib/status/
lane: verify
summary_short: "Per-book statistics, axiom inventory, and sorry inventory for TauLib."
right_rail:
  related:
  - title: TauLib Overview
    url: /verify/taulib/
  - title: Architecture
    url: /verify/taulib/architecture/
  - title: Scope Labels
    url: /verify/taulib/scope-labels/
  meta:
    type: "Dashboard"
    status: "Frozen"
    updated: "April 2026"
---

## Build Pin

{% assign build = site.data.verify.build %}

| Source | Revision | Reference |
|--------|----------|-----------|
| **TauLib** ({{ build.taulib.repo }}) | [`{{ build.taulib.commit_short }}`]({{ build.taulib.url }}/commit/{{ build.taulib.commit_sha }}) &middot; {{ build.taulib.commit_date }} | Apache&nbsp;2.0 &middot; [LICENSE]({{ build.taulib.license_url }}) |
| **Lean** | `{{ build.lean.version }}` | [lean-lang.org]({{ build.lean.url }}) |
| **Mathlib** | [`{{ build.mathlib.commit_short }}`]({{ build.mathlib.url }}/commit/{{ build.mathlib.commit_sha }}) | {{ build.mathlib.policy }} |

The 445 API-doc pages in `/verify/taulib/docs/` were generated from TauLib commit `{{ build.taulib.commit_short }}` via `scripts/import_taulib_docs.py` + `scripts/convert_taulib_html_to_md.py`. To reproduce locally, clone the repo at that commit and run `lake build`.

---

## Summary

| Metric | Value |
|--------|------:|
| Total modules | 450 |
| Total lines | 125,771 |
| Theorems and lemmas | 4,332 |
| Definitions | 3,542 |
| Structures and types | 1,685 |
| Computations (`#eval`) | 3,721 |
| Examples | 350 |
| Axioms | 4 |
| Sorry | 3 |

## Per-Book Breakdown

| Book | Modules | Lines | Theorems | #eval | Axioms | Sorry |
|------|--------:|------:|---------:|------:|-------:|------:|
| I — Foundations | 94 | 20,554 | ~900 | ~700 | 0 | **0** |
| II — Holomorphy | 65 | 18,069 | ~700 | ~500 | 0 | **0** |
| III — Spectrum | 70 | 16,807 | ~600 | ~450 | 3 | **0** |
| IV — Microcosm | 89 | 29,730 | ~1,000 | ~900 | 1 | **0** |
| V — Macrocosm | 80 | 28,394 | ~900 | ~850 | 0 | **0** |
| VI — Life | 30 | 5,221 | ~200 | ~200 | 0 | **0** |
| VII — Metaphysics | 7 | 4,278 | ~120 | ~100 | 0 | 3 |
| Tour | 8 | ~1,850 | — | — | 0 | **0** |
| **Total** | **450** | **125,771** | **~4,332** | **~3,721** | **4** | **3** |

## Axiom Inventory

TauLib contains exactly **4 axioms**, each explicitly declared and documented.

### Conjectural Axioms (3)

These follow the "compute-then-axiomatize" pattern: a decidable check function is verified computationally via `native_decide` at all tested finite bounds. The axiom asserts the property holds universally.

| # | Axiom | Module | What It Asserts |
|---|-------|--------|-----------------|
| 1 | `bridge_functor_exists` | `BookIII.Bridge.BridgeAxiom` | The bridge functor from the canonical enrichment ladder to the spectral decomposition exists for all n |
| 2 | `spectral_correspondence_O3` | `BookIII.Doors.SpectralCorrespondence` | The O(3) spectral correspondence holds universally |
| 3 | `grand_grh_adelic` | `BookIII.Doors.GrandGRH` | The adelic Generalized Riemann Hypothesis (used for spectral completeness) |

### Structural Axiom (1)

| # | Axiom | Module | What It Asserts |
|---|-------|--------|-----------------|
| 4 | `central_theorem_physical` | `BookIV.Arena.BoundaryHolonomy` | The Central Theorem holds in the physical interpretation; references the algebraic proof in Book II |

## Sorry Inventory

TauLib contains exactly **3 sorry**, all in Book VII. Each is typed `True := sorry` — the goal is trivially `True`, and the sorry marks a philosophical boundary where formalization itself is the content under discussion.

| # | Theorem | Module | Why Sorry |
|---|---------|--------|-----------|
| 1 | `omega_point_theorem` | `BookVII.Logos.Sector` | Involves omega, which is non-diagrammatic by design. The theorem asserts convergence toward the omega-attractor. |
| 2 | `science_faith_boundary` | `BookVII.Logos.Sector` | Full convergence claim involves non-computable limits on omega-directed sequences. |
| 3 | `no_forced_stance` | `BookVII.Final.Boundary` | Asserts that the lemniscate closure does not force a metaphysical stance. Formalizing it fully would require the framework to step outside itself. |

**Key property:** All three sorry are reachable only through Book VII's philosophical modules. No mathematical or physical result in Books I-VI depends on any sorry.
