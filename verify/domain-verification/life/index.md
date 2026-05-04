---
layout: program-doc
title: "Life Verification"
permalink: /verify/domain-verification/life/
lane: verify
v2_lane: verify
type: "Verification Surface"
verify_type: domain_verification
domain: life
status: "Canonical"
summary_short: "Verification for the τ-framework's life layer (Book VI): explanatory adequacy, biological constraint checks, biomarker correlates anchored to the K_χ chirality channel, and empirical humility."
plain_language_summary: |
  Life verification asks whether the framework recovers biological constraint — organization, heredity, selection, development, agency — without quietly replacing empirical biology by formal analogy. Book VI's claim is that all of biology's universal regularities (homochirality, ATP universality, the genetic code, circadian timing, neural-defect asymmetry in consciousness) propagate from a single structural anchor: the Kinetic Pseudoscalar Channel K_χ (LG-Y02 / VI.L18) which amplifies a weak-sector chirality seed into biological-scale homochirality. Verification means checking each predicted biomarker against measurement, and asking whether the structural derivation chains hold. The 78 life-glossary entries each carry an empirical correlate (biomarker + measurable range + observation method).
right_rail:
  related:
    - title: "Life Results"
      url: /results/life/
    - title: "Life Recovery Requirements"
      url: /agenda/core-semantics/life/
    - title: "Origin of Life Problem Answer"
      url: /results/problem-ledger-answers/life/origin-of-life/
    - title: "Assessment Protocols"
      url: /verify/assessment-protocols/
    - title: "How to Audit (Philosopher)"
      url: /verify/how-to-audit/philosopher/
  meta:
    type: "Domain Verification"
    domain: "Life"
    status: "Canonical"
    updated: "April 2026"
glossary_term_ids:
  - LG-Y02-kinetic-pseudoscalar-channel
  - LG-E01-atp
  - LG-M01-consciousness
---

{%- assign stats = site.data.verify.coverage_by_domain.by_domain.life -%}

## At a glance

<div class="v2-grid verify-hub-stats">
  <div class="v2-tile v2-tile-life">
    <span class="eyebrow">Book</span>
    <h3>VI</h3>
    <p>Life sector · K_χ multi-branch tree (chirality / energy / information / temporal / phenomenal).</p>
  </div>
  <div class="v2-tile v2-tile-life">
    <span class="eyebrow">TauLib modules</span>
    <h3>{{ stats.module_count }}</h3>
    <p>{{ stats.line_count }} lines of Lean 4 across life-domain modules.</p>
  </div>
  <div class="v2-tile v2-tile-life">
    <span class="eyebrow">Lean coverage</span>
    <h3>{{ stats.formalized_count }} / {{ stats.declaration_count }}</h3>
    <p>Formalized declarations · {% assign pct = stats.formalized_count | times: 100 | divided_by: stats.declaration_count %}{{ pct }}% formal · 0 sorries.</p>
  </div>
  <div class="v2-tile v2-tile-life">
    <span class="eyebrow">Glossary entries</span>
    <h3>78</h3>
    <p>Each carries a biomarker + measurable range + observation method.</p>
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
  <a class="v2-tile v2-tile-life" href="{{ '/verify/taulib/status/' | relative_url }}">
    <span class="eyebrow">Formalization</span>
    <h3>TauLib Status</h3>
    <p>Per-module formalization for the life layer · {{ stats.formalized_count }} formalized declarations · 100% formal.</p>
  </a>
  <a class="v2-tile v2-tile-life" href="{{ '/verify/bridge-verification/' | relative_url }}">
    <span class="eyebrow">Bridge</span>
    <h3>Bridge Verification</h3>
    <p>How K_χ amplification of weak-sector chirality bridges to homochirality, ATP universality, and the genetic code.</p>
  </a>
  <a class="v2-tile v2-tile-life" href="{{ '/results/life/glossary/' | relative_url }}">
    <span class="eyebrow">Glossary</span>
    <h3>Life Glossary</h3>
    <p>78 sealed entries · biomarker correlates · 5 K_χ branches.</p>
  </a>
  <a class="v2-tile v2-tile-life" href="{{ '/agenda/core-semantics/life/' | relative_url }}">
    <span class="eyebrow">Recovery</span>
    <h3>Life Recovery Requirements</h3>
    <p>Known biological structures the kernel must rederive (recovery targets + status).</p>
  </a>
  <a class="v2-tile v2-tile-life" href="{{ '/verify/how-to-audit/philosopher/' | relative_url }}">
    <span class="eyebrow">Audit</span>
    <h3>How to Audit (Philosopher)</h3>
    <p>Reviewer route for philosophy of biology, autopoiesis / IIT / FEP comparison, and the derivation-vs-redefinition test.</p>
  </a>
  <a class="v2-tile v2-tile-life" href="{{ '/results/life/' | relative_url }}">
    <span class="eyebrow">Results</span>
    <h3>Life Results Hub</h3>
    <p>55 life results · K_χ multi-branch tree · landmark results · empirical correlates.</p>
  </a>
</div>

## Verification burden

Life verification asks whether a claim recovers biological constraint, organization, heredity, selection, development, and agency without replacing empirical biology by formal analogy. Explanatory adequacy is necessary here but is not the same as laboratory confirmation or external acceptance.

The framework's life-sector commitments anchor at the **Kinetic Pseudoscalar Channel** (`LG-Y02`, registry `VI.L18`), a parity-odd time-even operator that amplifies the weak-sector chirality seed (~10⁻¹⁷) into biological-scale homochirality (ee ≈ 1.0). Every life-sector empirical correlate inherits its observable signature from this anchor — see the [calibration tree]({{ '/results/life/cascade/' | relative_url }}) for the full multi-branch architecture.

The program may report a structural explanation or recovery route before a biological mechanism is externally accepted. That status must remain visible: internal adequacy, empirical support, and external review are separate questions.

{% include verify-glossary-terms.html %}

{% include verify-cross-domain-links.html %}

## See also

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/results/life/' | relative_url }}">
    <strong>Results · Life</strong>
    <span>55 life-domain results · 78 glossary entries · calibration tree · landmark results.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/life/cascade/' | relative_url }}">
    <strong>K_χ Calibration Tree</strong>
    <span>The 5-branch life architecture rooted at LG-Y02 (chirality / energy / information / temporal / phenomenal).</span>
  </a>
  <a class="v2-tile" href="{{ '/results/life/glossary/' | relative_url }}">
    <strong>Life Glossary</strong>
    <span>78 entries grouped by category, each with empirical correlate.</span>
  </a>
  <a class="v2-tile" href="{{ '/corpus/registry/' | relative_url }}">
    <strong>Corpus Registry (Book VI)</strong>
    <span>Public registry items underpinning the formal layer of life.</span>
  </a>
</div>
