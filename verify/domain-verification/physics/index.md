---
layout: program-doc
title: "Physics Verification"
permalink: /verify/domain-verification/physics/
lane: verify
v2_lane: verify
type: "Verification Surface"
verify_type: domain_verification
domain: physics
status: "Canonical"
summary_short: "Verification for physics-facing claims: structural derivation, measurement bridges, prediction timing, falsification, and numerical accountability. Books IV–V — the calibration cascade from ι_τ + m_n to measurable observables."
plain_language_summary: |
  Physics verification is not just a Lean check. The framework's physics layer (Books IV–V) makes zero-parameter numerical predictions from a single algebraic constant ι_τ = 2/(π+e) and a single empirical anchor m_n (the neutron mass). Each prediction is testable. Verification means asking, separately: (1) does the derivation chain compile in Lean? (2) does the predicted number match measurement? (3) is ι_τ fitted or forced by the kernel structure? (4) are there genuine forward predictions on a fixed timeline? The Falsification Pack lists named experiments through 2035 whose outcomes would refute specific claims. None is currently contradicted.
right_rail:
  related:
    - title: "Predictions & Falsification"
      url: /verify/predictions-and-falsification/
    - title: "Numerical Physics Ledger"
      url: /publications/monograph-supplements/numerical-physics-ledger/
    - title: "Physics Recovery Requirements"
      url: /agenda/recovery-requirements/physics/
    - title: "Physics Results"
      url: /results/physics/
    - title: "How to Audit (Physicist)"
      url: /verify/how-to-audit/physicist/
  meta:
    type: "Domain Verification"
    domain: "Physics"
    status: "Canonical"
    updated: "April 2026"
glossary_term_ids:
  - PG-P01-neutron
  - PG-C02-iota-tau
  - PG-C01-newton-g
  - PG-C05-fine-structure-alpha
---

{%- assign stats = site.data.verify.coverage_by_domain.by_domain.physics -%}

## At a glance

<div class="v2-grid verify-hub-stats">
  <div class="v2-tile v2-tile-physics">
    <span class="eyebrow">Books</span>
    <h3>IV · V</h3>
    <p>Particle physics + cosmology + the calibration cascade.</p>
  </div>
  <div class="v2-tile v2-tile-physics">
    <span class="eyebrow">TauLib modules</span>
    <h3>{{ stats.module_count }}</h3>
    <p>{{ stats.line_count }} lines of Lean 4 across physics-domain modules.</p>
  </div>
  <div class="v2-tile v2-tile-physics">
    <span class="eyebrow">Lean coverage</span>
    <h3>{{ stats.formalized_count }} / {{ stats.declaration_count }}</h3>
    <p>Formalized declarations · {% assign pct = stats.formalized_count | times: 100 | divided_by: stats.declaration_count %}{{ pct }}% formal · 0 sorries.</p>
  </div>
  <div class="v2-tile v2-tile-physics">
    <span class="eyebrow">Predictions</span>
    <h3>{% include release-metric.html id="predictions.records" %}</h3>
    <p>Zero-parameter numerical predictions · {% include release-metric.html id="falsifications.records" %} falsification paths on a 2025–2035 timeline.</p>
  </div>
</div>

## Per-book Lean coverage

<div class="coverage-stats-table">

| Book | Modules | Lines |
|------|--------:|------:|
{% for pair in stats.books -%}
| {{ pair[0] | replace: "Book", "Book " }} | {{ pair[1].module_count }} | {{ pair[1].line_count }} |
{% endfor %}

</div>

## Inspection routes

<div class="v2-grid">
  <a class="v2-tile v2-tile-physics" href="{{ '/verify/predictions-and-falsification/' | relative_url }}">
    <span class="eyebrow">Empirical</span>
    <h3>Predictions &amp; Falsification</h3>
    <p>{% include release-metric.html id="predictions.records" %} numerical predictions · {% include release-metric.html id="falsifications.records" %} named-experiment falsification paths · prediction-timing ledger.</p>
  </a>
  <a class="v2-tile v2-tile-physics" href="{{ '/verify/taulib/status/' | relative_url }}">
    <span class="eyebrow">Formalization</span>
    <h3>TauLib Status</h3>
    <p>Per-module formalization for the physics layer · {{ stats.formalized_count }} formalized declarations.</p>
  </a>
  <a class="v2-tile v2-tile-physics" href="{{ '/verify/bridge-verification/' | relative_url }}">
    <span class="eyebrow">Bridge</span>
    <h3>Bridge Verification</h3>
    <p>How internal τ-categorical structure transfers to physical observables (m_n anchor → SI cascade).</p>
  </a>
  <a class="v2-tile v2-tile-physics" href="{{ '/verify/custom-axioms/' | relative_url }}">
    <span class="eyebrow">Axioms</span>
    <h3>Custom Axiom Inventory</h3>
    <p>The {{ stats.axiom_count | default: 0 }} custom axioms in this domain (none in physics; all 3 are in Book III).</p>
  </a>
  <a class="v2-tile v2-tile-physics" href="{{ '/verify/how-to-audit/physicist/' | relative_url }}">
    <span class="eyebrow">Audit</span>
    <h3>How to Audit (Physicist)</h3>
    <p>Reviewer route for particle physics, cosmology, quantum foundations, GR specialists.</p>
  </a>
  <a class="v2-tile v2-tile-physics" href="{{ '/results/physics/' | relative_url }}">
    <span class="eyebrow">Results</span>
    <h3>Physics Results Hub</h3>
    <p>{% include release-metric.html id="results.physics.records" %} physics result pages · {% include release-metric.html id="glossary.physics.entries" %} glossary entries · calibration cascade · landmark results.</p>
  </a>
</div>

## Verification burden

Physics verification is not established by formal derivation alone. A physics-facing result must separate:

- **Internal structural derivation** — does it compile in Lean and does the registry chain close?
- **Measurement interpretation** — what is the bridge from τ-construct to physical observable?
- **Numerical prediction** — what specific value follows from ι_τ + m_n?
- **Empirical comparison** — does the predicted value match published measurement?
- **External scientific review** — has the derivation chain survived independent specialist scrutiny?

The Numerical Physics Ledger is the artifact layer; Predictions & Falsification is the accountability layer; Results is the interpretation layer. None implies external acceptance on its own.

{% include verify-glossary-terms.html %}

{% include verify-cross-domain-links.html %}

## See also

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/results/physics/' | relative_url }}">
    <strong>Results · Physics</strong>
    <span>Physics-domain results hub: {% include release-metric.html id="results.physics.records" %} results, {% include release-metric.html id="glossary.physics.entries" %} glossary entries, predictions, falsifications.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/physics/cascade/' | relative_url }}">
    <strong>Calibration Cascade</strong>
    <span>The 5-layer architectural diagram: τ-kernel → ι_τ → (M, L, ℏ) → derived constants → SI bridge at m_n.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/physics/glossary/' | relative_url }}">
    <strong>Physics Glossary</strong>
    <span>{% include release-metric.html id="glossary.physics.entries" %} entries with full SI translations and τ-derivation chains.</span>
  </a>
  <a class="v2-tile" href="{{ '/corpus/registry/' | relative_url }}">
    <strong>Corpus Registry (Books IV–V)</strong>
    <span>Public registry items underpinning the formal layer of physics.</span>
  </a>
</div>
