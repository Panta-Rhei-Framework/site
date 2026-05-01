---
layout: program-doc
title: "Mathematics Verification"
permalink: /verify/domain-verification/mathematics/
lane: verify
v2_lane: verify
type: "Verification Surface"
verify_type: domain_verification
domain: mathematics
status: "Canonical"
summary_short: "Verification for the mathematical layer of the τ-framework — Books I–III: kernel, holomorphy, central theorem, Yoneda enrichment, master constant ι_τ. Lean-formalized with the strongest formalization ratio of any domain."
plain_language_summary: |
  Mathematics is where the τ-framework's formalization is strongest. Books I–III are the foundational kernel: definitions, theorems, holomorphy results, the Yoneda-as-theorem under self-enrichment, and the central theorem that pins τ's categoricity. Verification here means checking that every load-bearing theorem actually compiles in Lean 4, that the registry's claim of "formalized" matches the source, and that bridges into standard mathematics (Mathlib) hold. Three load-bearing checks: the categoricity of τ (Book II), the Yoneda enrichment ladder (Book II), and the Hyperfactorization theorem (Book I). Anything claiming "formalized" status here should resolve to a Lean theorem you can read.
right_rail:
  related:
    - title: "Formal Verification Stack"
      url: /verify/formal-verification-stack/
    - title: "TauLib"
      url: /verify/taulib/
    - title: "Corpus Registry"
      url: /corpus/registry/
    - title: "Mathematics Results"
      url: /results/mathematics/
    - title: "How to Audit (Mathematician)"
      url: /verify/how-to-audit/mathematician/
  meta:
    type: "Domain Verification"
    domain: "Mathematics"
    status: "Canonical"
    updated: "April 2026"
glossary_term_ids:
  - MathG-D01-iota-tau
  - MathG-K01-universe-postulate
  - MathG-T04-central-theorem
  - MathG-D04-yoneda-as-theorem
  - MathG-T06-prime-polarity
  - MathG-D06-truth4-logic
  - MathG-T07-split-complex-forced
  - MathG-D07-4-plus-1-sector
---

{%- assign stats = site.data.verify.coverage_by_domain.by_domain.mathematics -%}

## At a glance

<div class="v2-grid verify-hub-stats">
  <div class="v2-tile v2-tile-mathematics">
    <span class="eyebrow">Books</span>
    <h3>I · II · III</h3>
    <p>Foundational kernel · holomorphy · enrichment + categoricity · spectral / Riemann.</p>
  </div>
  <div class="v2-tile v2-tile-mathematics">
    <span class="eyebrow">TauLib modules</span>
    <h3>{{ stats.module_count }}</h3>
    <p>{{ stats.line_count }} lines of Lean 4 across mathematics-domain modules.</p>
  </div>
  <div class="v2-tile v2-tile-mathematics">
    <span class="eyebrow">Lean coverage</span>
    <h3>{{ stats.formalized_count }} / {{ stats.declaration_count }}</h3>
    <p>Formalized declarations · {% assign pct = stats.formalized_count | times: 100 | divided_by: stats.declaration_count %}{{ pct }}% formal · 0 sorries.</p>
  </div>
  <div class="v2-tile v2-tile-mathematics">
    <span class="eyebrow">Custom axioms</span>
    <h3>{{ stats.axiom_count | default: 0 }}</h3>
    <p>Beyond Mathlib's standard base. All disclosed in the <a href="{{ '/verify/custom-axioms/' | relative_url }}">Custom Axiom Inventory</a>.</p>
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
  <a class="v2-tile v2-tile-mathematics" href="{{ '/verify/taulib/status/' | relative_url }}">
    <span class="eyebrow">Formalization</span>
    <h3>TauLib Status</h3>
    <p>Per-module formalization ratios, declaration counts, and source-line coverage for the mathematics layer.</p>
  </a>
  <a class="v2-tile v2-tile-mathematics" href="{{ '/verify/bridge-verification/' | relative_url }}">
    <span class="eyebrow">Bridge</span>
    <h3>Bridge Verification</h3>
    <p>How internal τ-categorical structure transfers to standard mathematics (Mathlib, classical results).</p>
  </a>
  <a class="v2-tile v2-tile-mathematics" href="{{ '/verify/custom-axioms/' | relative_url }}">
    <span class="eyebrow">Axioms</span>
    <h3>Custom Axiom Inventory</h3>
    <p>The {{ stats.axiom_count | default: 0 }} declared custom axioms, their finite-checked support, and what specialist review would close.</p>
  </a>
  <a class="v2-tile v2-tile-mathematics" href="{{ '/verify/tcb/' | relative_url }}">
    <span class="eyebrow">TCB</span>
    <h3>Trust Budget</h3>
    <p>What Lean's kernel trusts, where TauLib uses <code>native_decide</code>, and which theorems carry the extension.</p>
  </a>
  <a class="v2-tile v2-tile-mathematics" href="{{ '/verify/how-to-audit/mathematician/' | relative_url }}">
    <span class="eyebrow">Audit</span>
    <h3>How to Audit (Mathematician)</h3>
    <p>Reviewer route for category theorists, model theorists, complex analysts, and number theorists.</p>
  </a>
  <a class="v2-tile v2-tile-mathematics" href="{{ '/results/mathematics/' | relative_url }}">
    <span class="eyebrow">Results</span>
    <h3>Mathematics Results Hub</h3>
    <p>Landmark theorems, world readout, and recovery targets for the mathematics layer.</p>
  </a>
</div>

## Verification levels

### Kernel integrity
Does each Lean module compile cleanly relative to the stated formalization scope? Do theorem dependencies close, and does the registry's `formalized` flag match the source?

Surfaces: [TauLib]({{ '/verify/taulib/' | relative_url }}), [Formalization Status]({{ '/verify/taulib/status/' | relative_url }}), [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}).

### Standard-foundation alignment
Can selected hinge theorems be re-established in standard foundational settings (Mathlib, ZFC, classical category theory) by independent specialists?

Surfaces: hinge companion pages, [Formal Methods audit route]({{ '/verify/how-to-audit/formal-methods/' | relative_url }}), and selected corpus objects.

### Bridge adequacy
Do recovery and transfer claims into standard mathematics support the downstream use being made of them in physics, life, and metaphysics?

Surfaces: [Custom Axiom Inventory]({{ '/verify/custom-axioms/' | relative_url }}), [TCB Disclosure]({{ '/verify/tcb/' | relative_url }}), [Bridge Verification]({{ '/verify/bridge-verification/' | relative_url }}).

## Accountability statement

Any theorem claimed as formally certified is certified in the precise sense stated: relative to the relevant proof infrastructure, declared assumptions, and stated scope. Mathematical verification establishes internal proof discipline; it does not by itself settle bridge adequacy into every standard foundation, the program's downstream physics/life/metaphysics consequences, or external review.

{% include verify-glossary-terms.html %}

{% include verify-cross-domain-links.html %}

## See also

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/results/mathematics/' | relative_url }}">
    <strong>Results · Mathematics</strong>
    <span>Hub for mathematics-domain results, world readout, and recovery targets.</span>
  </a>
  <a class="v2-tile" href="{{ '/corpus/registry/' | relative_url }}">
    <strong>Corpus Registry</strong>
    <span>The 4,139 public registry items underpinning the formal layer.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/formal-verification-stack/' | relative_url }}">
    <strong>Formal Verification Stack</strong>
    <span>Cross-domain explanation of the four formal-verification layers.</span>
  </a>
  <a class="v2-tile" href="{{ '/verify/how-to-audit/' | relative_url }}">
    <strong>How to Audit (all roles)</strong>
    <span>Pick your reviewer route — formal methods, mathematician, physicist, philosopher, prior-art, or generalist.</span>
  </a>
</div>
