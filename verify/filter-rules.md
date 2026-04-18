---
layout: program-doc
title: "Filter Rules — Which Count Means What"
permalink: /verify/filter-rules/
lane: verify
summary_short: "Authoritative manifest of the filter rules applied by every count claim on this site. When the registry root, the per-book dashboard, and the TauLib status page show different numbers for the same book, this page names the rule each surface applies and what it counts — so apparent drift becomes legible as a filter choice, not a data-integrity bug."
right_rail:
  related:
    - title: "Release Manifest"
      url: /verify/release-manifest/
    - title: "Formalization Status"
      url: /verify/taulib/status/
    - title: "Custom Axiom Inventory"
      url: /verify/custom-axioms/
    - title: "Registry"
      url: /registry/
  meta:
    type: "Filter-Rule Manifest"
    scope: "All count claims across the site"
    status: "Canonical"
    updated: "April 2026"
---

{% assign rules = site.data.registry.filter_rules.filter_rules %}
{% assign manifest = site.data.registry.filter_rules %}

A reader looking at three surfaces — the [Registry]({{ '/registry/' | relative_url }}), the per-book [Dashboards]({{ '/registry/dashboards/book-vi/' | relative_url }}), and the [TauLib Status]({{ '/verify/taulib/status/' | relative_url }}) — may see three different numbers for the same book. Book VI, for example, appears as **217**, **168**, and **30** across these three places.

This is not a data-integrity bug. It is three different **filter rules** applied to the same canonical source. This page names each rule, specifies what it includes, and pins down the current counts so a reader can always reconcile.

**Canonical source of truth.** All counts derive from `PantaRhei-2ndEd/registry/book{1..7}_registry.jsonl` — one JSONL line per registry object. Every number on this site descends from that file via one of the filter rules below.

## The five filter rules

| Rule | What it counts | Book VI example |
|------|----------------|----------------:|
| `registry_total` | All objects regardless of type or status — axioms, constructions, corollaries, definitions, lemmas, propositions, remarks, theorems | 217 |
| `dashboard_display` | Only the five display types (D + L + P + R + T) — the types per-book dashboards enumerate | 168 |
| `formalized_count` | `dashboard_display` restricted to `formalization_status == formalized` | 0 |
| `planned_count` | `dashboard_display` restricted to `formalization_status == planned` | 143 |
| `taulib_modules` | Lean 4 module count — **different unit** from registry objects (one module hosts many objects) | 30 |

**Why two registry filters, not one?** A dashboard that rendered every remark, axiom, and corollary would be 2× longer and harder to scan. A registry root that silently dropped "ancillary" object types would lose claim-ID stability across releases. The two rules — one complete, one display-filtered — give both clarity and completeness. The column-mapping in the [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}#per-book-reconciliation) makes the choice explicit at every surface.

**Why `taulib_modules` sits apart.** Lean modules and registry objects are **different units**. A single Lean module can host dozens of registry objects (definitions, theorems, propositions side by side). The module count (445 total) and the object count (4,547 total) are both correct for their respective units; they are not comparable quantities.

## Current totals — per book

Counts sourced from canonical `book{1..7}_registry.jsonl` ({{ manifest.updated }}) and the pinned TauLib commit at `/Users/thorfuchs/Books/PantaRhei-2ndEd/`.

{%- assign rt = rules.registry_total.current_totals -%}
{%- assign dd = rules.dashboard_display.current_totals -%}
{%- assign fc = rules.formalized_count.current_totals -%}
{%- assign pc = rules.planned_count.current_totals -%}
{%- assign nc = rules.not_applicable_count.current_totals -%}
{%- assign tm = rules.taulib_modules.current_totals -%}

| Book | `registry_total` | `dashboard_display` | `formalized_count` | `planned_count` | `not_applicable_count` | `taulib_modules` |
|------|----------------:|----------------:|----------------:|----------------:|----------------:|----------------:|
| I — Foundations | {{ rt.book_i }} | {{ dd.book_i }} | {{ fc.book_i }} | {{ pc.book_i }} | {{ nc.book_i }} | {{ tm.book_i }} |
| II — Holomorphy | {{ rt.book_ii }} | {{ dd.book_ii }} | {{ fc.book_ii }} | {{ pc.book_ii }} | {{ nc.book_ii }} | {{ tm.book_ii }} |
| III — Spectrum | {{ rt.book_iii }} | {{ dd.book_iii }} | {{ fc.book_iii }} | {{ pc.book_iii }} | {{ nc.book_iii }} | {{ tm.book_iii }} |
| IV — Microcosm | {{ rt.book_iv }} | {{ dd.book_iv }} | {{ fc.book_iv }} | {{ pc.book_iv }} | {{ nc.book_iv }} | {{ tm.book_iv }} |
| V — Macrocosm | {{ rt.book_v }} | {{ dd.book_v }} | {{ fc.book_v }} | {{ pc.book_v }} | {{ nc.book_v }} | {{ tm.book_v }} |
| VI — Life | {{ rt.book_vi }} | {{ dd.book_vi }} | {{ fc.book_vi }} | {{ pc.book_vi }} | {{ nc.book_vi }} | {{ tm.book_vi }} |
| VII — Metaphysics | {{ rt.book_vii }} | {{ dd.book_vii }} | {{ fc.book_vii }} | {{ pc.book_vii }} | {{ nc.book_vii }} | {{ tm.book_vii }} |
| Tour modules | — | — | — | — | — | {{ tm.tour_modules }} |
| **Total** | **{{ rt.grand_total }}** | — | **{{ fc.grand_total }}** | **{{ pc.grand_total }}** | **{{ nc.grand_total }}** | **{{ tm.grand_total }}** |

## Rule definitions — in detail

### `registry_total`

**What it counts.** {{ rules.registry_total.description | strip_newlines }}

- **Includes types:** {{ rules.registry_total.includes_types }}
- **Includes statuses:** {{ rules.registry_total.includes_statuses }}
- **Grand total:** {{ rt.grand_total }} objects

**Displayed on:**
{% for surface in rules.registry_total.displayed_on %}- `{{ surface }}`
{% endfor %}

### `dashboard_display`

**What it counts.** {{ rules.dashboard_display.description | strip_newlines }}

- **Includes types:** {{ rules.dashboard_display.includes_types }}
- **Includes statuses:** {{ rules.dashboard_display.includes_statuses }}

**Displayed on:**
{% for surface in rules.dashboard_display.displayed_on %}- `{{ surface }}`
{% endfor %}

### `taulib_modules`

**What it counts.** {{ rules.taulib_modules.description | strip_newlines }}

- **Unit:** {{ rules.taulib_modules.unit }}
- **Source:** {{ rules.taulib_modules.source }}
- **Grand total:** {{ tm.grand_total }} Lean 4 modules

**Displayed on:**
{% for surface in rules.taulib_modules.displayed_on %}- `{{ surface }}`
{% endfor %}

### `formalized_count`

**What it counts.** {{ rules.formalized_count.description | strip_newlines }}

- **Includes types:** {{ rules.formalized_count.includes_types }}
- **Grand total:** {{ fc.grand_total }} formalized objects

**Displayed on:**
{% for surface in rules.formalized_count.displayed_on %}- `{{ surface }}`
{% endfor %}

### `planned_count`

**What it counts.** {{ rules.planned_count.description | strip_newlines }}

- **Grand total:** {{ pc.grand_total }} planned objects

### `not_applicable_count`

**What it counts.** {{ rules.not_applicable_count.description | strip_newlines }}

- **Grand total:** {{ nc.grand_total }} not-applicable objects

## Cross-surface invariants

Every count on this site must satisfy these invariants, which `scripts/registry_verify.py` checks on every CI run:

{% for inv in site.data.registry.filter_rules.invariants %}- {{ inv }}
{% endfor %}

A violation of any invariant is a merge blocker on `main`. See [`scripts/registry_verify.py`](https://github.com/Panta-Rhei-Research/site/blob/main/scripts/registry_verify.py) for the implementation.

## Reconciliation protocol

{{ site.data.registry.filter_rules.reconciliation_protocol | strip_newlines }}

## Update protocol

{{ site.data.registry.filter_rules.update_protocol | strip_newlines }}

## What this page is NOT

- **Not a dashboard.** For per-book enumerations, see the [dashboards]({{ '/registry/dashboards/book-i/' | relative_url }}).
- **Not a registry browser.** For navigation to individual objects, see the [registry index]({{ '/registry/' | relative_url }}).
- **Not a TauLib map.** For Lean module architecture, see [Formalization Status]({{ '/verify/taulib/status/' | relative_url }}) and [Architecture]({{ '/verify/taulib/architecture/' | relative_url }}).

This page's single job is to make the filter rules legible and to let a reader reconcile any two count claims on the site without leaving the public surface.
