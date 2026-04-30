---
layout: program-doc
title: "Results"
permalink: /results/
lane: results
v2_lane: results
type: "Lane Root"
status: "Canonical"
summary_short: "What the program currently derives — organized by domain. Mathematics, Physics, Life, Metaphysics."
og_image: /assets/images/plates/plate-05-results-world-readout-og.jpg
twitter_image: /assets/images/plates/plate-05-results-world-readout-og.jpg
og_image_alt: "Scientific plate showing the Results lane as a status-marked consequence layer with Landmark Results, World Readouts, Problem Answers, Recovery Target Status, Additional Derived Results, Progress Against Agenda, and inspection routes."
summary_cards:
  - title: "Four domains"
    body: "Mathematics, Physics, Life, Metaphysics — each its own per-domain hub."
  - title: "Calibration cascades"
    body: "Physics anchored at m_n; Life at K_χ; Metaphysics is categorical-only."
  - title: "Status grammar"
    body: "Every result surface separates internal stance, verification, and external acceptance."
hero_ctas:
  - label: "Physics"
    url: /results/physics/
    primary: true
  - label: "Life"
    url: /results/life/
  - label: "Mathematics"
    url: /results/mathematics/
  - label: "Metaphysics"
    url: /results/metaphysics/
right_rail:
  related:
    - title: "Landmark Results"
      url: /results/landmark-results/
    - title: "Problem Answers"
      url: /results/problem-ledger-answers/
    - title: "Recovery Target Status"
      url: /results/recovery-target-status/
    - title: "Progress Against Agenda"
      url: /results/progress-against-agenda/
    - title: "Result Classifications"
      url: /results/classifications/
    - title: "Corpus Registry"
      url: /corpus/registry/
    - title: "Verify"
      url: /verify/
  meta:
    type: "Lane Root"
    scope: "All results"
    status: "Canonical"
    updated: "April 2026"
---

{% assign result_count = site.data.results.results | size %}
{% assign mathematics_results = site.data.results.results | where: "layer", "mathematics" %}
{% assign physics_results = site.data.results.results | where: "layer", "physics" %}
{% assign life_results = site.data.results.results | where: "layer", "life" %}
{% assign metaphysics_results = site.data.results.results | where: "layer", "metaphysics" %}
{% assign glossary_summary = site.data.glossary.summary %}

## Four domains, one cascade

The τ-framework's results organize naturally into four domains, each with its own calibration cascade or categorical architecture:

<div class="v2-grid v2-grid-large">

  <a class="v2-tile v2-tile-domain v2-tile-mathematics" href="{{ '/results/mathematics/' | relative_url }}">
    <span class="eyebrow">Books I–III · Foundational Kernel</span>
    <h3>Mathematics</h3>
    <p>{{ mathematics_results | size }} results · the categorical kernel from which everything follows. Categoricity, holomorphy, the central theorem, Yoneda enrichment, the master constant ι_τ.</p>
    <span class="chip chip-cascade chip-cascade-kernel">Kernel</span>
  </a>

  <a class="v2-tile v2-tile-domain v2-tile-physics" href="{{ '/results/physics/' | relative_url }}">
    <span class="eyebrow">Books IV–V · Calibration Cascade</span>
    <h3>Physics</h3>
    <p>{{ physics_results | size }} results · 95 glossary entries · 67 numerical predictions. Every SI value derives from ι_τ + the neutron-mass anchor m_n. Tier-A precision down to 0.025 ppm.</p>
    <span class="chip chip-cascade chip-cascade-physics-cascade">Physics cascade</span>
  </a>

  <a class="v2-tile v2-tile-domain v2-tile-life" href="{{ '/results/life/' | relative_url }}">
    <span class="eyebrow">Book VI · K_χ Multi-Branch Tree</span>
    <h3>Life</h3>
    <p>{{ life_results | size }} results · 78 glossary entries. Every biological observable inherits from the Kinetic Pseudoscalar Channel (LG-Y02 / VI.L18). Five branches: chirality, energy, information, temporal, phenomenal.</p>
    <span class="chip chip-cascade chip-cascade-life-cascade">Life cascade</span>
  </a>

  <a class="v2-tile v2-tile-domain v2-tile-metaphysics" href="{{ '/results/metaphysics/' | relative_url }}">
    <span class="eyebrow">Book VII · Categorical Architecture</span>
    <h3>Metaphysics</h3>
    <p>{{ metaphysics_results | size }} results · 68 glossary entries. No empirical anchor — categorical-only. Four readout registers (Reg_E/P/D/C → Obs/Norm/Proof/Stance) plus six narrowing principles (OR1–OR6).</p>
    <span class="chip chip-cascade chip-cascade-metaphysics-architecture">Architecture</span>
  </a>

</div>

## Reading order

<div class="v2-system-strip" aria-label="Results pipeline">
  <a href="{{ '/program/research-agenda/' | relative_url }}">Agenda</a>
  <span>-></span>
  <a href="{{ '/corpus/' | relative_url }}">Corpus</a>
  <span>-></span>
  <a href="{{ '/results/' | relative_url }}">Results</a>
  <span>-></span>
  <a href="{{ '/verify/' | relative_url }}">Verify</a>
</div>

The Agenda states the burden. The Corpus carries the build. Results shows the current consequences and world-readouts. Verify exposes the inspection routes.

Every result should be read with its status markers. An internally addressed result is not the same as external verification or scientific acceptance.

## Cross-cutting surfaces

<div class="v2-grid">

  <a class="v2-tile" href="{{ '/results/landmark-results/' | relative_url }}">
    <strong>Landmark Results</strong>
    <span>The 18 highest-impact results curated across all four domains.</span>
  </a>

  <a class="v2-tile" href="{{ '/results/predictions/' | relative_url }}">
    <strong>Predictions</strong>
    <span>67 zero-parameter numerical predictions with precision tiers (sub-ppm to %).</span>
  </a>

  <a class="v2-tile" href="{{ '/results/falsifications/' | relative_url }}">
    <strong>Falsifications</strong>
    <span>30 sharp predictions (N1–N30) where named experiments adjudicate the framework on a 2025–2035 timeline.</span>
  </a>

  <a class="v2-tile" href="{{ '/results/problem-ledger-answers/' | relative_url }}">
    <strong>Problem Answers</strong>
    <span>One-to-one mirror of the public Problem Ledger — current answer or boundary for every problem.</span>
  </a>

  <a class="v2-tile" href="{{ '/results/recovery-target-status/' | relative_url }}">
    <strong>Recovery Target Status</strong>
    <span>Current recovery status against declared recovery requirements.</span>
  </a>

  <a class="v2-tile" href="{{ '/results/progress-against-agenda/' | relative_url }}">
    <strong>Progress Against Agenda</strong>
    <span>Dashboard over problem and recovery obligations.</span>
  </a>

  <a class="v2-tile" href="{{ '/results/browse/' | relative_url }}">
    <strong>Browse All</strong>
    <span>The full {{ result_count }}-page catalogue with filters for domain, kind, importance, status, book, and v3 badges.</span>
  </a>

  <a class="v2-tile" href="{{ '/results/classifications/' | relative_url }}">
    <strong>Classifications</strong>
    <span>What kind of result each page claims to be — derivation, structural, prediction, refusal, …</span>
  </a>

</div>

## Status legend

- **Internally addressed** — the current framework contains an internal answer, derivation, or structural stance.
- **Partial** — the framework has a partial result, recovery, or bridge, but further work remains.
- **Qualitative** — the result is conceptual or interpretive rather than quantitative or formal.
- **Contradicted** — the result is marked as conflicting with a target or requirement.
- **Not addressed** — no current public stance is available.

These labels report the program's internal status. They do not indicate external verification or scientific acceptance.

## Read next

- [Landmark Results]({{ '/results/landmark-results/' | relative_url }}) — top results across all four domains
- [Browse All Results]({{ '/results/browse/' | relative_url }}) — full filterable catalogue
- [How to read a result page]({{ '/results/how-to-read-a-result-page/' | relative_url }}) — the v3 4-section structure
- [Status & Claim Typing]({{ '/results/status-and-claim-typing/' | relative_url }}) — what each status marker means
