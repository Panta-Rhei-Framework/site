---
layout: program-doc
title: "Physics Cascade — ι_τ + m_n calibration"
permalink: /results/physics/cascade/
lane: results
v2_lane: results
type: "Cascade Page"
status: "Canonical"
domain: physics
summary_short: "Single architectural diagram connecting τ-categorical kernel → ι_τ → (M, L, ℏ) → derived constants → SI bridge anchored at the neutron mass."
---

The **physics calibration cascade** is the single architectural diagram that connects every numerical value in the τ-framework's physics surface to the empirical world. Each numerical SI value traces back, through a deterministic chain of dimensionless ratios derived from `ι_τ`, to **one** empirical input: the neutron mass `m_n`.

This is the framework's most concrete claim about the relationship between **structure** and **measurement**: the entire physical-constants ecosystem (G, c, ℏ, k_B, α, e, R_∞, a₀, …) emerges from a master constant `ι_τ ≈ 0.341304` and a single SI anchor.

## The five layers

```
┌──────────────────────────────────────────────────────────────────────┐
│  Layer 0: τ-categorical kernel                                       │
│    I.K0 (Universe Postulate) — kernel τ exists                       │
└────────────────────────────────┬─────────────────────────────────────┘
                                 ▼
┌──────────────────────────────────────────────────────────────────────┐
│  Layer 1: master structural constant                                 │
│    ι_τ ≈ 0.341304 — emerges from kernel structure                   │
│    I.D34 / IV.D255 / V.D231                                          │
└────────────────────────────────┬─────────────────────────────────────┘
                                 ▼
┌──────────────────────────────────────────────────────────────────────┐
│  Layer 2: τ³ topology + dimensional triple (M, L, ℏ)                 │
│    Mass scale, length scale, action quantum                          │
└────────────────────────────────┬─────────────────────────────────────┘
                                 ▼
┌──────────────────────────────────────────────────────────────────────┐
│  Layer 3: derived physical constants (dimensional)                   │
│    α, a₀, R_∞, c, ℏ, G, k_B  ←  ι_τ-chain × (M, L, ℏ)               │
└────────────────────────────────┬─────────────────────────────────────┘
                                 ▼
┌──────────────────────────────────────────────────────────────────────┐
│  Layer 4: SI bridge — anchored to m_n (empirical input)              │
│    PG-P01-neutron: m_n = 1.6749275 × 10⁻²⁷ kg (CODATA-22)            │
└──────────────────────────────────────────────────────────────────────┘
```

## Why m_n and not m_e or m_p?

Per `IV.P331` (Neutron Superiority as Calibration Standard):

- **Directly measurable** — atomic mass spectrometry vs. unreachable Planck scale
- **Structurally minimal** — lightest stable T²-defect bundle
- **Universal constituent** — every nucleus contains neutrons
- **β-decay differentiation tree** (`IV.R121`) makes proton + electron + photon all derivable from neutron, so `m_n` is the structural parent

## Registry anchors

The cascade is fully manifested through a small set of canonical registry items:

- `I.K0` — Universe Postulate (Layer 0)
- `I.D34` / `IV.D255` / `V.D231` — Master constant ι_τ (Layer 1)
- `IV.D104` — Fine-structure constant α (Layer 3)
- `IV.P126`, `IV.T238` — Bohr radius a₀ (Layer 3)
- `V.D45`, `V.R69`, `V.P58` — Newton's gravitational constant G (Layer 3)
- `IV.P327` — τ-neutron defect bundle (Layer 4 anchor item)
- `IV.P331` — Neutron superiority as calibration standard

## Glossary anchors

Every numerical SI value lives as a glossary entry under `/results/physics/glossary/`. The cascade's anchor is:

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/results/physics/glossary/PG-P01-neutron/' | relative_url }}">
    <strong>PG-P01-neutron · The τ-neutron</strong>
    <span>The single SI anchor of the entire physics cascade. m_n = 1.6749275 × 10⁻²⁷ kg.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/physics/glossary/PG-C02-iota-tau/' | relative_url }}">
    <strong>PG-C02-iota-tau · Master constant ι_τ</strong>
    <span>The dimensionless invariant ι_τ ≈ 0.341304. The first dimensionless scalar of the framework.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/physics/glossary/PG-C01-newton-g/' | relative_url }}">
    <strong>PG-C01-newton-g · Newton's G</strong>
    <span>Gravitational constant — derived structural ratio from gravity-sector ι_τ embedding.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/physics/glossary/PG-C05-fine-structure-alpha/' | relative_url }}">
    <strong>PG-C05-fine-structure-alpha · α</strong>
    <span>Fine-structure constant — pure dimensionless ι_τ-chain.</span>
  </a>
</div>

## Lean formalization

The cascade has direct Lean formalizations:

- `TauLib.BookIV.Calibration.CalibrationAnchor` — the anchor itself
- `TauLib.BookV.Coda.CalibrationChain` — the chain assembly
- `TauLib.BookV.GravityField.CalibrationTriangle` — gravity-sector triangle inequality

## Read next

- [Physics glossary]({{ '/results/physics/glossary/' | relative_url }}) — 95 entries with full SI translations
- [Predictions]({{ '/results/predictions/' | relative_url }}) — 67 numerical predictions on top of this cascade
- [Falsifications]({{ '/results/falsifications/' | relative_url }}) — sharp tests of cascade-derived values
- [Life cascade]({{ '/results/life/cascade/' | relative_url }}) — analogous cascade for biological observables (VI.L18 anchor)

## Provenance

This is a Jekyll surface of the canonical corpus document at `corpus/physics-glossary/calibration-cascade.md`. The corpus version is the source of truth; this page is a curated rendering for the public-facing site.
