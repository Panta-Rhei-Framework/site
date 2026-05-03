---
layout: program-doc
title: "Core Semantics"
title_plain: "Core Semantics"
lane: agenda
v2_lane: agenda
section: research-agenda
type: "Agenda Surface"
status: "Canonical"
summary_short: "The language the theory must earn before it can answer."
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
    type: "Core Semantics"
    scope: "Research Agenda"
    status: "Canonical"
    updated: "April 2026"
---

{% assign recovery_items = site.recovery_requirements | sort: "canonical_recovery_id" %}
{% assign math_items = recovery_items | where: "domain", "mathematics" %}
{% assign physics_items = recovery_items | where: "domain", "physics" %}
{% assign life_items = recovery_items | where: "domain", "life" %}
{% assign metaphysics_items = recovery_items | where: "domain", "metaphysics" %}

## The language the theory must earn

Core Semantics names the semantic load a coherent theory of reality must be able to carry, preserve, refine, retype, replace, or explicitly mark as unresolved.

Core Semantics is not a promise to reproduce current semantics unchanged. It is the obligation to earn the language of the domains the theory addresses. Where established semantics works, the theory must carry it. Where established semantics breaks, the theory must retype, bridge, or replace it with reasons.

This surface was previously labeled Recovery Requirements. The URL and underlying Corpus projection remain stable so existing links, item IDs, and audit trails continue to work. Publicly, the surface now names the broader obligation: the theory must earn the language of mathematics, physics, life, metaphysics, and explicit refusal boundaries before its answers can be taken seriously.

The current canonical v0.1 public projection contains {{ recovery_items.size }} core semantic target and refusal items.

## Core semantic domains

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/program/research-agenda/recovery-requirements/mathematics/' | relative_url }}">
    <strong>Mathematics</strong>
    <span>{{ math_items.size }} target/refusal items covering formal checkability, finite syntax, arithmetic, geometry, ZFC as object theory, bridge adequacy, and mathematical refusals.</span>
  </a>
  <a class="v2-tile" href="{{ '/program/research-agenda/recovery-requirements/physics/' | relative_url }}">
    <strong>Physics</strong>
    <span>{{ physics_items.size }} target items covering quantity types, dimensional algebra, unit bridges, constants, laws, regimes, and measurement.</span>
  </a>
  <a class="v2-tile" href="{{ '/program/research-agenda/recovery-requirements/life/' | relative_url }}">
    <strong>Life</strong>
    <span>{{ life_items.size }} target items covering boundary, metabolism, heredity, evolution, development, ecology, and the life-mind bridge.</span>
  </a>
  <a class="v2-tile" href="{{ '/program/research-agenda/recovery-requirements/metaphysics/' | relative_url }}">
    <strong>Metaphysics</strong>
    <span>{{ metaphysics_items.size }} target items covering being, identity, relation, causality, modality, time, truth, mind, language, value, and ultimate boundary.</span>
  </a>
</div>

## Core Semantics vs problem solving

The Problem Ledger asks whether the kernel can express, classify, constrain, answer, defer, reclassify, or reject external stress-test problems with reasons.

Core Semantics asks whether the kernel can earn the language those problems presuppose: formal reasoning, measurement architecture, life-organization grammar, reflective meaning, and metaphysical intelligibility.

The point is not to preserve established theories as untouchable primitives. The point is to identify what the theory must carry, preserve, refine, retype, bridge, or explicitly challenge.

## Canonical v0.1 targets and refusals

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
