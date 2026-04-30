---
layout: program-doc
title: "Verify"
lane: verify
v2_lane: verify
permalink: /verify/
type: "Lane Root"
status: "Canonical"
summary_short: "How to inspect, verify, and challenge the claims of the Panta Rhei Research Program — what can be checked, and what verification does not settle."
og_image: /assets/images/plates/plate-06-verification-matrix-og.jpg
twitter_image: /assets/images/plates/plate-06-verification-matrix-og.jpg
og_image_alt: "Scientific plate showing the Verify lane as a verification matrix with obligations, construction steps, results, formal proof checking, bridge adequacy, predictions, falsification, and external assessment."
hero_ctas:
  - label: "Scientific Rigor"
    url: /verify/scientific-rigor/
    primary: true
  - label: "Verify the Construction Spine"
    url: /verify/construction-spine-verification/
  - label: "Formal Verification Stack"
    url: /verify/formal-verification-stack/
  - label: "How to Verify"
    url: /verify/how-to-verify/
hero_supporting_line: "522 Lean 4 modules · 142,406+ lines · 4,863 scanned theorem/lemma declarations · 0 active sorry assignments across all 7 books (TauLib Lean corpus at the current release SHA; scope tiered — see <a href=\"/verify/filter-rules/\">Filter Rules</a>) · 3 custom axioms · Mathlib for tactics only."
summary_cards:
  - title: "What can be checked"
    body: "Every theorem in TauLib compiles in Lean 4. Every quantitative prediction has an explicit formula. Every scope claim carries its epistemic label."
  - title: "What verification does not settle"
    body: "Compilation proves internal consistency, not truth about the physical world. Bridge claims remain conjectural until independently validated."
  - title: "How to start"
    body: "Start from an obligation, a construction step, or a result. Then trace it to Corpus support, Verify surfaces, and any available formalization."
right_rail:
  related:
    - title: "Verify the Construction Spine"
      url: /verify/construction-spine-verification/
    - title: "Verification Framework"
      url: /verify/verification-framework/
    - title: "Domain Verification"
      url: /verify/domain-verification/
    - title: "Construction Roadmap"
      url: /program/research-agenda/construction-roadmap/
    - title: "Corpus Construction Spine"
      url: /corpus/construction-spine/
    - title: "Results"
      url: /results/
    - title: "Corpus Registry"
      url: /corpus/registry/
  artifacts:
    - title: "Release Manifest"
      url: /verify/release-manifest/
    - title: "Filter Rules"
      url: /verify/filter-rules/
    - title: "Custom Axiom Inventory"
      url: /verify/custom-axioms/
    - title: "TCB Disclosure"
      url: /verify/tcb/
    - title: "TauLib Browser"
      url: /verify/taulib/docs/
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

## What Verify Means Here

> Verify is where every obligation, construction step, and result becomes inspectable.

Verification in this program is not one thing. It includes research-form legitimacy, source-policy inspection, construction-step verification, formal proof checking, semantic correspondence, bridge adequacy, domain-specific validation, prediction and falsification surfaces, and structured external assessment.

**Metrics context:** [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}) · [Filter Rules]({{ '/verify/filter-rules/' | relative_url }}) · [Custom Axiom Inventory]({{ '/verify/custom-axioms/' | relative_url }}) · [TCB Disclosure]({{ '/verify/tcb/' | relative_url }})

<p class="eyebrow">The inspection layer at a glance</p>

## The Verification Matrix

{% include scientific-plate.html id="plate-06-verification-matrix" class="scientific-plate--verification-matrix" loading="lazy" %}

Verification is not a single operation. It begins with traceability: what obligation is being answered, what construction supports it, what result follows, and how can it be challenged?

Formal checking is essential, but it is not empirical truth.

<div class="btn-group section-ctas">
  <a class="btn-secondary" href="{{ '/verify/construction-spine-verification/' | relative_url }}">Verify the Construction Spine</a>
  <a class="btn-ghost" href="{{ '/verify/taulib/' | relative_url }}">Inspect TauLib</a>
  <a class="btn-ghost" href="{{ '/verify/release-manifest/' | relative_url }}">Read the Release Manifest</a>
  <a class="btn-ghost" href="{{ '/verify/predictions-and-falsification/' | relative_url }}">Open Predictions & Falsification</a>
</div>

<div class="v2-system-strip" aria-label="Verify lane model">
  <a href="{{ '/verify/scientific-rigor/' | relative_url }}">Scientific Rigor</a>
  <span>-></span>
  <a href="{{ '/verify/verification-framework/' | relative_url }}">Verification Framework</a>
  <span>-></span>
  <a href="{{ '/verify/construction-spine-verification/' | relative_url }}">Construction Verification</a>
  <span>-></span>
  <a href="{{ '/verify/formal-verification-stack/' | relative_url }}">Formal Stack</a>
  <span>-></span>
  <a href="{{ '/verify/domain-verification/' | relative_url }}">Domain Verification</a>
  <span>-></span>
  <a href="{{ '/verify/how-to-verify/' | relative_url }}">Operational Routes</a>
</div>

## Core Routes

<ul class="v2-grid v2-card-list">
  <li>
    <article>
      <a class="v2-tile" href="{{ '/verify/scientific-rigor/' | relative_url }}">
        <strong>Scientific Rigor</strong>
        <span>Whether the program operates as a serious, inspectable research artifact.</span>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/verify/verification-framework/' | relative_url }}">
        <strong>Verification Framework</strong>
        <span>The shared standards: explicitness, traceability, derivability, and domain-appropriate validation.</span>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/verify/construction-spine-verification/' | relative_url }}">
        <strong>Verify the Construction Spine</strong>
        <span>How each of the ten construction steps can be inspected, checked, or challenged.</span>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/verify/formal-verification-stack/' | relative_url }}">
        <strong>Formal Verification Stack</strong>
        <span>Kernel integrity, standard-foundation checks, bridge verification, and current boundaries.</span>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/verify/domain-verification/' | relative_url }}">
        <strong>Domain Verification</strong>
        <span>How verification differs across mathematics, physics, life, and metaphysics.</span>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/verify/predictions-and-falsification/' | relative_url }}">
        <strong>Predictions & Falsification</strong>
        <span>Where results become accountable to computation, measurement, contradiction, or failure.</span>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/verify/assessment-protocols/' | relative_url }}">
        <strong>Assessment Protocols</strong>
        <span>Manual and LLM-assisted review pathways for structured external scrutiny.</span>
      </a>
    </article>
  </li>
</ul>

## Verification status legend

- **Formalized** — represented in TauLib or another formal artifact.
- **Formally checked** — compiles under the pinned formalization environment.
- **Bridge pending** — internal construction exists, but the bridge to standard mathematics, measurement, or domain interpretation remains open.
- **Empirical pending** — a prediction or comparison exists, but decisive external test or measurement remains open.
- **Externally reviewed** — discussed or reviewed outside the program.
- **Externally accepted** — accepted by an external scholarly process or community standard.

These labels describe inspection state. They are related to, but distinct from, Results status labels such as internally addressed, partial, qualitative, or not addressed.

## Operational Surfaces

- [TauLib]({{ '/verify/taulib/' | relative_url }}) is the Lean 4 formalization surface.
- [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}) pins the current public release state.
- [Filter Rules]({{ '/verify/filter-rules/' | relative_url }}) explain which count means what across site surfaces.
- [Custom Axiom Inventory]({{ '/verify/custom-axioms/' | relative_url }}) and [TCB Disclosure]({{ '/verify/tcb/' | relative_url }}) name the trust budget.
- [How to Verify]({{ '/verify/how-to-verify/' | relative_url }}) gives practical entry points for different reviewers.

## The Right First Question

The right first question is not "should I already believe this?" The right first question is: **is this a serious research program that has earned structured engagement?**

Start by checking the research form, then choose an obligation, a construction step, or a result, trace its Corpus support, inspect the available formalization, identify bridge assumptions, and test its domain-specific accountability route.

## Report Corrections

Found an error, a broken proof, a mis-stated numerical value, or a scope-label issue? We take corrections seriously and credit corrigendum contributors in the changelog.

**Email**: [errata@panta-rhei.site](mailto:errata@panta-rhei.site)

For formal peer-review coordination or institutional review inquiries: [review@panta-rhei.site](mailto:review@panta-rhei.site)
