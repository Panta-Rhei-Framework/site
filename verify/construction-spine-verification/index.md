---
layout: program-doc
title: "Verify the Construction Spine"
permalink: /verify/construction-spine-verification/
lane: verify
v2_lane: verify
section: construction-verification
type: "Verification Surface"
status: "Canonical"
summary_short: "Maps the ten Corpus Construction Spine steps to the relevant verification modes, including formal proof, bridge checks, empirical prediction, falsification, and answer-shape scrutiny."
right_rail:
  related:
    - title: "Construction Roadmap"
      url: /program/research-agenda/construction-roadmap/
    - title: "Corpus Construction Spine"
      url: /corpus/construction-spine/
    - title: "Formal Verification Stack"
      url: /verify/formal-verification-stack/
    - title: "Predictions & Falsification"
      url: /verify/predictions-and-falsification/
    - title: "Assessment Protocols"
      url: /verify/assessment-protocols/
    - title: "Progress Against Agenda"
      url: /results/progress-against-agenda/
  meta:
    type: "Verification Surface"
    scope: "Construction Spine"
    status: "Canonical"
    updated: "April 2026"
---

{% assign steps = site.data.construction_spine["construction-spine"] %}

# Verify the Construction Spine

> How each step of the Corpus Construction Spine can be inspected, checked, or challenged.

## Why construction-step verification matters

The Corpus shows how the structure was built. Verify shows how each construction step can be inspected. This is where the aligned spine becomes explicit:

Agenda -> Corpus -> Results -> Verify

Obligation -> Construction -> Consequence -> Inspection

## Step-by-step verification table

| Step | Construction step | Primary verification modes |
| --- | --- | --- |
{% for step in steps %}
| {{ step.sequence }} | [{{ step.title }}]({{ step.corpus_path | relative_url }}) | {{ step.verification.primary_modes | join: ", " }} |
{% endfor %}

## Verification modes by step

{% for step in steps %}
### {{ step.sequence }}. {{ step.title }} {#step-{{ step.sequence | prepend: '0' | slice: -2, 2 }}}

- Construction page: [{{ step.title }}]({{ step.corpus_path | relative_url }})
- Current build status: **{{ step.build_status_label }}**
- Primary verification modes: {{ step.verification.primary_modes | join: ", " }}
- Bridge checks: {% if step.verification.bridge_checks.size > 0 %}{{ step.verification.bridge_checks | join: "; " }}{% else %}No dedicated bridge check declared yet.{% endif %}
- Empirical checks: {% if step.verification.empirical_checks.size > 0 %}{{ step.verification.empirical_checks | join: "; " }}{% else %}No empirical check declared at this step.{% endif %}
- Unresolved frontiers: {% if step.verification.unresolved_frontiers.size > 0 %}{{ step.verification.unresolved_frontiers | join: "; " }}{% else %}No unresolved frontier declared yet.{% endif %}

{% if step.verification.related_verify_pages.size > 0 %}
Related Verify pages:

<div class="dep-list">
{% for related in step.verification.related_verify_pages %}
  {% if related.url %}
  <a class="dep-link" href="{{ related.url | relative_url }}">
    <span class="dep-id">Verify</span>
    <span class="dep-title">{{ related.title }}</span>
  </a>
  {% else %}
  <div class="dep-link"><span class="dep-id">Verify</span><span class="dep-title">{{ related }}</span></div>
  {% endif %}
{% endfor %}
</div>
{% endif %}
{% endfor %}

## Related Corpus Construction Spine

Use the [Corpus Construction Spine]({{ '/corpus/construction-spine/' | relative_url }}) when you want the build narrative rather than the verification matrix.

## Related Results and Progress Dashboard

Use [Progress Against Agenda]({{ '/results/progress-against-agenda/' | relative_url }}) to see how public problem and recovery obligations currently map to Results-side status surfaces.

## Related Assessment Protocols

Use [Assessment Protocols]({{ '/verify/assessment-protocols/' | relative_url }}) when you want a manual or LLM-assisted review route after identifying the relevant construction step.
