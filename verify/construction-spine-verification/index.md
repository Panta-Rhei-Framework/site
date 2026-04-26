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

{% assign steps = site.data.construction_spine["construction-spine-data"] %}

> How each step of the Corpus Construction Spine can be inspected, checked, or challenged.

## Why construction-step verification matters

The Corpus shows how the structure was built. Verify shows how each construction step can be inspected. This is where the aligned spine becomes explicit:

Agenda -> Corpus -> Results -> Verify

Obligation -> Construction -> Consequence -> Inspection

## Step-by-step verification table

<div class="table-wrap">
  <table>
    <thead>
      <tr>
        <th scope="col">Step</th>
        <th scope="col">Construction step</th>
        <th scope="col">Primary verification modes</th>
      </tr>
    </thead>
    <tbody>
      {% for step in steps %}
      {% assign primary_modes = step.verification.primary_modes | default: empty %}
      <tr>
        <td>{{ step.sequence }}</td>
        <td><a href="{{ step.corpus_path | relative_url }}">{{ step.title }}</a></td>
        <td>
          {% if primary_modes.size > 0 %}
            {{ primary_modes | join: ", " }}
          {% else %}
            <span class="muted">Pending population</span>
          {% endif %}
        </td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>

## Verification-status legend

<table>
  <thead>
    <tr>
      <th scope="col">Status phrase</th>
      <th scope="col">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr><th scope="row">Available</th><td>A public inspection route exists for this step or mode.</td></tr>
    <tr><th scope="row">Partial</th><td>Some evidence is public, but the route is not complete enough to close the burden.</td></tr>
    <tr><th scope="row">Pending mapping</th><td>The public route is known to be needed but not yet mapped in this projection.</td></tr>
    <tr><th scope="row">Not applicable</th><td>The mode is not a relevant burden for this step.</td></tr>
  </tbody>
</table>

## Verification modes by step

{% for step in steps %}
{% assign step_anchor = step.sequence | prepend: '0' | slice: -2, 2 %}
{% assign build_status_label = step.build_status_label | default: step.build_status | replace: "_", " " | capitalize %}
{% assign primary_modes = step.verification.primary_modes | default: empty %}
{% assign bridge_checks = step.verification.bridge_checks | default: empty %}
{% assign empirical_checks = step.verification.empirical_checks | default: empty %}
{% assign unresolved_frontiers = step.verification.unresolved_frontiers | default: empty %}
{% assign related_verify_pages = step.verification.related_verify_pages | default: empty %}
<h3 id="step-{{ step_anchor }}">{{ step.sequence }}. {{ step.title }}</h3>

<ul>
  <li>Construction page: <a href="{{ step.corpus_path | relative_url }}">{{ step.title }}</a></li>
  <li>Current build status: <strong>{{ build_status_label }}</strong></li>
  <li>
    Primary verification modes:
    {% if primary_modes.size > 0 %}
      {{ primary_modes | join: ", " }}
    {% else %}
      Pending population.
    {% endif %}
  </li>
  <li>
    Bridge checks:
    {% if bridge_checks.size > 0 %}
      {{ bridge_checks | join: "; " }}
    {% else %}
      No dedicated bridge check declared yet.
    {% endif %}
  </li>
  <li>
    Empirical checks:
    {% if empirical_checks.size > 0 %}
      {{ empirical_checks | join: "; " }}
    {% elsif step.sequence == 1 %}
      Not applicable at this step. Empirical accountability begins after internal physical grammar and measurement bridges are constructed.
    {% elsif step.sequence == 2 %}
      Not applicable as a direct empirical check. This step supports later empirical accountability by recovering mathematical capacity under kernel discipline.
    {% elsif step.sequence == 3 %}
      Not applicable as a direct empirical check. This step concerns internal logic, categorical structure, and semantic self-containment.
    {% elsif step.sequence == 4 or step.sequence == 5 %}
      Downstream of this step. Measurement, calibration, and falsification burdens begin once empirical bridge surfaces are constructed.
    {% elsif step.sequence == 8 %}
      Downstream or domain-dependent at this step. Reflective-structure claims require separate life, semantic, and metaphysical verification routes.
    {% elsif step.sequence == 9 or step.sequence == 10 %}
      Not the primary burden at this step. This step is assessed through meta-verification, no-externalities review, and explicit boundary disclosure.
    {% else %}
      Not applicable at this step.
    {% endif %}
  </li>
  <li>
    Unresolved frontiers:
    {% if unresolved_frontiers.size > 0 %}
      {{ unresolved_frontiers | join: "; " }}
    {% else %}
      No unresolved frontier declared yet.
    {% endif %}
  </li>
</ul>

{% if related_verify_pages.size > 0 %}
Related Verify pages:

<div class="dep-list">
{% for related in related_verify_pages %}
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
