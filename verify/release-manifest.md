---
layout: program-doc
title: "Release Manifest"
permalink: /verify/release-manifest/
lane: verify
v2_lane: verify
type: "Verification Surface"
verify_type: release_manifest
status: "Canonical"
summary_short: "Single authoritative snapshot of the current release — pinned TauLib commit, Lean/Mathlib versions, per-book formalization state, and an honest reconciliation of counts across the three public-facing surfaces (registry, dashboards, TauLib docs)."
og_image: /assets/images/plates/plate-06-verification-matrix-og.jpg
twitter_image: /assets/images/plates/plate-06-verification-matrix-og.jpg
og_image_alt: "Scientific plate showing the Verify lane as a verification matrix with obligations, construction steps, results, formal proof checking, bridge adequacy, predictions, falsification, and external assessment."
right_rail:
  related:
  - title: TauLib Overview
    url: /verify/taulib/
  - title: Formalization Status
    url: /verify/taulib/status/
  - title: Architecture
    url: /verify/taulib/architecture/
  - title: Registry
    url: /corpus/registry/
  meta:
    type: "Release Snapshot"
    status: "Canonical"
    updated: "April 2026"
---

This page is the **single authoritative snapshot** of the current release. Everything that is pinned, every count that is claimed, every known drift between surfaces is stated here in one view. If the registry, the per-book dashboards, and the TauLib docs appear to disagree on a number, this page explains why and which number is load-bearing for which purpose.

## Release state and trusted base

{% capture release_manifest_plate_caption %}The Release Manifest anchors the formalization surface inside the broader verification matrix: formal artifacts, filters, axioms, trusted base, and inspection boundaries.{% endcapture %}
{% include scientific-plate.html id="plate-06-verification-matrix" variant="thumb" class="scientific-plate--compact" caption=release_manifest_plate_caption loading="lazy" %}

The Release Manifest records the release state, trusted base, custom axioms, filters, and formalization boundaries. It tells a reviewer exactly which formal surface is being inspected.

## Release identity

{% assign build = site.data.verify.build %}

| Source | Revision | Reference |
|--------|----------|-----------|
| **TauLib** ({{ build.taulib.repo }}) | [`{{ build.taulib.commit_short }}`]({{ build.taulib.url }}/commit/{{ build.taulib.commit_sha }}) &middot; {{ build.taulib.commit_date }} | Apache&nbsp;2.0 &middot; [LICENSE]({{ build.taulib.license_url }}) |
| **Lean** | `{{ build.lean.version }}` | [lean-lang.org]({{ build.lean.url }}) |
| **Mathlib** | [`{{ build.mathlib.commit_short }}`]({{ build.mathlib.url }}/commit/{{ build.mathlib.commit_sha }}) | {{ build.mathlib.policy }} |

The TauLib browser under `/verify/taulib/docs/` is generated from the Corpus-native TauLib projection pinned to commit `{{ build.taulib.commit_short }}`. To reproduce locally, import the TauLib snapshot into `corpus/taulib-sources/project`, run `lake build`, then run the Corpus TauLib projection/export scripts and the site sync.

## Build status — summary

| Metric | Value |
|--------|------:|
| Total modules | **512** |
| Total lines | 142,406 |
| Theorems + lemmas | 4,863 |
| Definitions | 3,741 |
| Structures + inductive types | 1,700 |
| Computations (`#eval`) | 3,923 |
| Custom `axiom` declarations | **3** (all in Book III — spectral / number-theoretic bridges) |
| `sorry` (incomplete proofs) | **0** (across all 7 books) |

The 3 custom axioms sit outside Mathlib's trusted base and are specific to the τ-framework's internal construction; they are named and documented in the per-module TauLib browser. The prior v1 release pinned at commit `181a59e` shipped a fourth axiom `central_theorem_physical : True` in Book IV which was retired in `peer-review-fixes-v1` (2026-04-19) as a no-op — an axiom of type `True` is inhabited by `trivial` and added nothing to the theory.

Pre-peer-review-fixes-v1, Book VII shipped three `theorem X : True := sorry` declarations encoding methodological commitments. These were identified as performative (True is provable by `trivial`) and were retired in favor of inspectable `def : Commitment` values carrying `statement`/`warrant`/`registry_id` string data. TauLib now contains **zero sorry across all seven books**. See `TauLib/BookVII/Meta/Commitment.lean` and the three commitment defs in `BookVII/Logos/Sector.lean` and `BookVII/Final/Boundary.lean`.

## Per-book reconciliation

This is the table Assessment #3 asked for. It shows, for each book, what each of the three public surfaces claims — and where they differ. Registry objects and Lean modules are **different units of counting** (a single module hosts many definitions, theorems, and propositions, each of which is a registry object), so some spread is expected; the drift within the same unit (registry root vs per-book dashboard) is what the honest reader should track.

| Book | Registry root | Dashboard total | Dashboard formalized | TauLib modules | Sorry |
|------|-------------:|-----------------:|---------------------:|---------------:|------:|
| I — Foundations | 254 | 254 | 221 | 147 | 0 |
| II — Holomorphy | 230 | 219 | 184 | 66 | 0 |
| III — Spectrum | 289 | 289 | 231 | 71 | 0 |
| IV — Microcosm | 1864 | 1292 | 973 | 90 | 0 |
| V — Macrocosm | 1419 | 1253 | 884 | 81 | 0 |
| VI — Life | 217 | 168 | 0 | 31 | 0 |
| VII — Metaphysics | 274 | 273 | 182 | 9 | 0 |
| Meta / Tour / root modules | — | — | — | 17 | 0 |
| **Total** | **4,547** | **3,548** | **2,675** | **512** | **0** |

Each column applies a specific **filter rule** to the same canonical source. The filter rules are documented on the [Filter Rules manifest]({{ '/verify/filter-rules/' | relative_url }}) and summarized here:

| Column | Filter rule | What it counts |
|--------|-------------|----------------|
| Registry root | `registry_total` | All object types including axioms, constructions, corollaries (every entry in `book*_registry.jsonl`) |
| Dashboard total | `dashboard_display` | Display-filtered to 5 types (definition, lemma, proposition, remark, theorem) — the types that appear in dashboard enumeration |
| Dashboard formalized | `formalized_count` | `dashboard_display` restricted to `formalization_status == formalized` |
| TauLib modules | `taulib_modules` | Lean 4 module count — **different unit from registry objects** (one module hosts many objects) |
| Sorry | (direct count) | `sorry` declarations in pinned Lean source |

Sources: counts sourced from the canonical registry JSONL source, `book{1..7}_registry.jsonl`, and the pinned TauLib commit [`{{ build.taulib.commit_short }}`]({{ build.taulib.url }}/commit/{{ build.taulib.commit_sha }}). Filter-rule definitions, per-book current totals, and cross-surface invariants are on the [Filter Rules manifest]({{ '/verify/filter-rules/' | relative_url }}).

## How to read apparent "drift"

The `Registry root` and `Dashboard total` columns disagree for four of seven books (II +11, IV +572, V +166, VI +49). This is **not a data-integrity bug** — it is two different filter rules applied to the same authoritative source:

| Book | Difference | What it is |
|------|-----------:|-----------|
| II | +11 | 11 entries of type other than D/L/P/R/T (e.g., axioms, constructions) that `dashboard_display` omits |
| IV | +572 | Large number of Book IV corollaries/remarks/axioms that are tracked in the registry but not shown in dashboard enumeration |
| V | +166 | Same as IV |
| VI | +49 | Same as IV |

**Reconciliation protocol:** if a reader sees two different numbers for the same book on different pages, (1) identify which `filter_rule` each surface applies (visible on the [Filter Rules manifest]({{ '/verify/filter-rules/' | relative_url }})), (2) confirm both numbers match the `current_totals` table on that page. If they do, the apparent drift is the legitimate difference between two filters of the same canonical data. If either surface does NOT match the manifest, that IS a bug — `registry_verify.py` catches such regressions.

**Why this is acceptable:** a dashboard rendering every remark and axiom would be 2x longer and harder to scan. A registry that silently dropped "ancillary" object types would lose claim-ID stability. Two filter rules, documented explicitly and cross-checked, give both clarity and completeness.

A follow-up sprint to consolidate the generation pipeline end-to-end (one script, idempotent, with the prose-preservation safeguards already scaffolded) remains on the engineering backlog — but is no longer load-bearing for the drift narrative.

## What this release does NOT claim

- **Book VII is formalized at methodological depth.** The Lean corpus for Book VII contains 7 modules that include three `def : Commitment` values carrying structural-commitment data (statement, warrant, registry_id). Zero `sorry`. The Book VII formalization is scaffolded; the monograph's prose content is the primary substance.
- **The physics bridge is not proof-assistant-verified.** TauLib verifies the internal τ-framework mathematics; it does not verify that τ-internal statements correspond to the external physics they are interpreted as describing. The 67 predictions surfaced in [Predictions Browse]({{ '/results/predictions/browse/' | relative_url }}) and documented in the [Numerical Physics Ledger]({{ '/publications/monograph-supplements/numerical-physics-ledger/' | relative_url }}) are derived from the framework's algebraic structure; their agreement with experiment is empirical, not machine-checked.
- **Millennium resolutions are not Clay-valid formulations.** Only the Poincaré conjecture aligns with the Clay statement as solved (via Perelman's proof, re-read in τ-language). The other six Millennium claims are τ-internal formulations with explicit bridge-conjecture gaps; see the [Millennium & Langlands briefing]({{ '/results/fields/millennium-langlands/' | relative_url }}).

## Reproduction instructions

```bash
# Clone at the pinned commit
git clone https://github.com/{{ build.taulib.repo }}
cd taulib
git checkout {{ build.taulib.commit_sha }}

# Expected pins (already in lake-manifest.json / lean-toolchain)
# Lean: {{ build.lean.version }}
# Mathlib: {{ build.mathlib.commit_short }}

lake build          # Expect: 0 errors, ~8–12 min on 8-core laptop
rg "sorry" TauLib   # Expect: 0 matches across all 7 books
```

Continuous integration runs on every push and pull request and reports file count, line count, `sorry` count, and `axiom` count to the CI log. A failed build or a regression in `sorry` count is a merge blocker on `main`.

## Next release targets

- **Drift consolidation** — one source-of-truth for registry totals across all surfaces.
- **Book VI formalization uplift** — currently 0 of 168 dashboard objects formalized; Book VI ch22 (Three Domains) and ch31 (Ecosystems) have solid internal theorem structure and are the priority targets.
- **Book VII methodological `sorry` replacement with commitment tags — DONE** (landed in `peer-review-fixes-v1`, 2026-04-19). The three `theorem X : True := sorry` declarations were replaced with inspectable `def : Commitment` values in `TauLib/BookVII/Meta/Commitment.lean`.
