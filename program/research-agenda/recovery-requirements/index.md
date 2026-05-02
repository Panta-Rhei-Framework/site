---
layout: program-doc
title: "Recovery Requirements"
lane: program
v2_lane: program
section: research-agenda
type: "Research Agenda Ledger"
status: "Canonical"
summary_short: "Known structures and conceptual grammars the program must recover without confusing them with open-problem stress tests."
hero_ctas:
  - label: "Mathematics"
    url: /program/research-agenda/recovery-requirements/mathematics/
    primary: true
  - label: "Physics"
    url: /program/research-agenda/recovery-requirements/physics/
  - label: "Life"
    url: /program/research-agenda/recovery-requirements/life/
  - label: "Metaphysics"
    url: /program/research-agenda/recovery-requirements/metaphysics/
right_rail:
  related:
    - title: "Problem Ledger"
      url: /program/research-agenda/problem-ledger/
    - title: "Result Criteria"
      url: /program/research-agenda/result-criteria/
    - title: "Verification Framework"
      url: /verify/verification-framework/
  meta:
    type: "Recovery Requirements"
    scope: "Research Agenda"
    status: "Canonical"
    updated: "April 2026"
---

{% assign recovery_items = site.recovery_requirements | sort: "canonical_recovery_id" %}
{% assign math_items = recovery_items | where: "domain", "mathematics" %}
{% assign physics_items = recovery_items | where: "domain", "physics" %}
{% assign life_items = recovery_items | where: "domain", "life" %}
{% assign metaphysics_items = recovery_items | where: "domain", "metaphysics" %}

## Why this is separate

Open problems test what the kernel can illuminate where current knowledge does not yet close. Recovery requirements test whether the kernel preserves and reconstructs structures that must not be broken.

The two burdens belong together, but they are not the same ledger. A kernel cannot credibly answer open problems if it cannot first recover the grammar those problems presuppose.

The current canonical v0.1 public projection contains {{ recovery_items.size }} recovery and refusal items.

## Recovery domains

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/program/research-agenda/recovery-requirements/mathematics/' | relative_url }}">
    <strong>Mathematics</strong>
    <span>{{ math_items.size }} recovery/refusal items covering formal checkability, finite syntax, arithmetic, geometry, ZFC as object theory, bridge adequacy, and mathematical refusals.</span>
  </a>
  <a class="v2-tile" href="{{ '/program/research-agenda/recovery-requirements/physics/' | relative_url }}">
    <strong>Physics</strong>
    <span>{{ physics_items.size }} recovery items covering quantity types, dimensional algebra, unit bridges, constants, laws, regimes, and measurement.</span>
  </a>
  <a class="v2-tile" href="{{ '/program/research-agenda/recovery-requirements/life/' | relative_url }}">
    <strong>Life</strong>
    <span>{{ life_items.size }} recovery items covering boundary, metabolism, heredity, evolution, development, ecology, and the life-mind bridge.</span>
  </a>
  <a class="v2-tile" href="{{ '/program/research-agenda/recovery-requirements/metaphysics/' | relative_url }}">
    <strong>Metaphysics</strong>
    <span>{{ metaphysics_items.size }} recovery items covering being, identity, relation, causality, modality, time, truth, mind, language, value, and ultimate boundary.</span>
  </a>
</div>

## Recovery vs problem solving

The Problem Ledger asks whether the kernel can express, classify, constrain, answer, defer, reclassify, or reject external stress-test problems with reasons.

The Recovery Requirements Ledger asks whether the kernel can recover baseline structures: formal reasoning, measurement architecture, life-organization grammar, and metaphysical intelligibility.

## Canonical v0.1 items

<div class="dep-list">
  {% for item in recovery_items %}
  <a class="dep-link" href="{{ item.url | relative_url }}">
    <span class="dep-id">{{ item.canonical_recovery_id }}</span>
    <span class="dep-title">{{ item.title }}</span>
    <span class="chip" style="margin-left:auto">{{ item.display_domain }}</span>
    <span class="badge {% if item.recovery_status == 'partial' %}badge-partial{% elsif item.recovery_status == 'not_applicable' %}badge-muted{% else %}badge-neutral{% endif %}">{{ item.recovery_status | replace: "_", " " }}</span>
  </a>
  {% endfor %}
</div>
