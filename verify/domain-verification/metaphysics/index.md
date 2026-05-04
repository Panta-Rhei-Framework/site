---
layout: program-doc
title: "Metaphysics Verification"
permalink: /verify/domain-verification/metaphysics/
lane: verify
v2_lane: verify
type: "Verification Surface"
verify_type: domain_verification
domain: metaphysics
status: "Canonical"
summary_short: "Verification for the τ-framework's metaphysics layer (Book VII): categorical-only architecture — Reg_E/P/D/C registers + OR1–OR6 narrowing principles. No empirical anchor; coherence + commitment-discipline are the verification modes."
plain_language_summary: |
  Unlike physics or life, the metaphysics layer has no single empirical anchor. It is purely categorical: concepts instantiate as lived-experience correlates, narrative examples, and ethical/proof-theoretic content rather than as numerical measurements. Verification here is the discipline of (1) keeping the four canonical readout registers (Reg_E/P/D/C → Obs/Norm/Proof/Stance) working coherently, (2) enforcing the OR1–OR6 narrowing principles (no internal contradictions, completeness, generativity, independence, continuity, stability), and (3) being honest about what diagrammatic access can and cannot establish. The framework's central limit-theorem here — No Forced Stance (VII.T47) — proves τ cannot force a stance on the ω-germ question, marking the categorical floor below which the framework explicitly does not commit.
right_rail:
  related:
    - title: "Philosophy Results"
      url: /results/metaphysics/
    - title: "Kernel, Model & Reality"
      url: /agenda/kernel-model-reality/
    - title: "Metaphysics Core Semantics"
      url: /agenda/core-semantics/metaphysics/
    - title: "Assessment Protocols"
      url: /verify/assessment-protocols/
    - title: "How to Verify (Philosopher)"
      url: /verify/how-to-verify-by-role/philosopher/
  meta:
    type: "Domain Verification"
    domain: "Metaphysics"
    status: "Canonical"
    updated: "May 2026"
glossary_term_ids:
  - MG-R01-empirical-register
  - MG-A01-ci-operator-graph
  - MG-H01-qualia
---

{%- assign stats = site.data.verify.coverage_by_domain.by_domain.metaphysics -%}

## At a glance

<div class="v2-grid verify-hub-stats">
  <div class="v2-tile v2-tile-metaphysics">
    <span class="eyebrow">Book</span>
    <h3>VII</h3>
    <p>Categorical architecture — registers, ontic requirements, commitments.</p>
  </div>
  <div class="v2-tile v2-tile-metaphysics">
    <span class="eyebrow">TauLib modules</span>
    <h3>{{ stats.module_count }}</h3>
    <p>{{ stats.line_count }} lines of Lean 4 across metaphysics-domain modules.</p>
  </div>
  <div class="v2-tile v2-tile-metaphysics">
    <span class="eyebrow">Lean coverage</span>
    <h3>{{ stats.formalized_count }} / {{ stats.declaration_count }}</h3>
    <p>Formalized declarations · {% assign pct = stats.formalized_count | times: 100 | divided_by: stats.declaration_count %}{{ pct }}% formal · 0 sorries.</p>
  </div>
  <div class="v2-tile v2-tile-metaphysics">
    <span class="eyebrow">Glossary entries</span>
    <h3>68</h3>
    <p>Each carries a phenomenological correlate (lived-experience instantiation; no empirical anchor).</p>
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
  <a class="v2-tile v2-tile-metaphysics" href="{{ '/agenda/kernel-model-reality/' | relative_url }}">
    <span class="eyebrow">Discipline</span>
    <h3>Kernel, Model &amp; Reality</h3>
    <p>The agenda's articulation of what diagrammatic access can and cannot establish.</p>
  </a>
  <a class="v2-tile v2-tile-metaphysics" href="{{ '/verify/taulib/status/' | relative_url }}">
    <span class="eyebrow">Formalization</span>
    <h3>TauLib Status</h3>
    <p>Per-module formalization for the metaphysics layer · {{ stats.formalized_count }} formalized declarations · 100% formal.</p>
  </a>
  <a class="v2-tile v2-tile-metaphysics" href="{{ '/results/metaphysics/glossary/' | relative_url }}">
    <span class="eyebrow">Glossary</span>
    <h3>Metaphysics Glossary</h3>
    <p>68 entries across registers / principles / architecture / ontology / commitment / phenomenology.</p>
  </a>
  <a class="v2-tile v2-tile-metaphysics" href="{{ '/agenda/core-semantics/metaphysics/' | relative_url }}">
    <span class="eyebrow">Recovery</span>
    <h3>Metaphysics Core Semantics</h3>
    <p>The language the theory must earn before it can answer metaphysical questions — categorical recovery targets and status.</p>
  </a>
  <a class="v2-tile v2-tile-metaphysics" href="{{ '/verify/how-to-verify-by-role/philosopher/' | relative_url }}">
    <span class="eyebrow">Audit</span>
    <h3>How to Verify (Philosopher)</h3>
    <p>Reviewer route for philosophers of mind, science, ethics, and metaphysics — the derivation-vs-redefinition test.</p>
  </a>
  <a class="v2-tile v2-tile-metaphysics" href="{{ '/results/metaphysics/' | relative_url }}">
    <span class="eyebrow">Results</span>
    <h3>Metaphysics Results Hub</h3>
    <p>45 metaphysics results · architecture page · landmark results · phenomenological correlates.</p>
  </a>
</div>

## Verification burden

Metaphysical verification is **not** laboratory proof and **not** Lean proof. It checks whether the program's ontic commitments are:

- **Explicit** — every commitment is named, not smuggled in
- **Coherent** with the construction — no contradictions among the four registers (Reg_E/P/D/C) or the six narrowing principles (OR1–OR6)
- **Disciplined by the no-externalities rule** — claims do not reach beyond τ-categorical structure
- **Honest about diagrammatic access** — what the kernel can show is not the same as what is

The Six Ontic Requirements (`VII.D37`) are the explicit narrowing rules: self-coherence, completeness, generativity, independence, continuity, stability. The No Forced Stance theorem (`VII.T47`) is the framework's structural floor — τ cannot force a stance on the ω-germ question, and any such stance belongs to the commitment register (Reg_C), not to proof.

A metaphysical page may argue for coherence, closure, or explanatory discipline. It must not imply direct noumenal access, final ontology, or external acceptance unless those stronger statuses are separately earned.

{% include verify-glossary-terms.html %}

{% include verify-cross-domain-links.html %}

## See also

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/results/metaphysics/' | relative_url }}">
    <strong>Results · Metaphysics</strong>
    <span>{% include release-metric.html id="results.metaphysics.records" %} metaphysics-domain results · {% include release-metric.html id="glossary.metaphysics.entries" %} glossary entries · architecture page · landmark results.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/metaphysics/cascade/' | relative_url }}">
    <strong>Categorical Architecture</strong>
    <span>Reg_E/P/D/C registers + OR1–OR6 narrowing principles. No empirical anchor — categorical-only.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/metaphysics/glossary/' | relative_url }}">
    <strong>Metaphysics Glossary</strong>
    <span>{% include release-metric.html id="glossary.metaphysics.entries" %} entries with phenomenological correlates and register codomains.</span>
  </a>
  <a class="v2-tile" href="{{ '/corpus/registry/' | relative_url }}">
    <strong>Corpus Registry (Book VII)</strong>
    <span>Public registry items underpinning the formal layer of metaphysics.</span>
  </a>
</div>
