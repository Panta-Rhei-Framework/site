---
layout: program-doc
title: "Mathematics Core Semantics"
title_plain: "Mathematics Core Semantics"
lane: agenda
v2_lane: agenda
section: research-agenda
type: "Core Semantic Domain"
status: "Canonical"
summary_short: "The mathematical language the tau-kernel must earn before it can function as a foundation for reality-description."
right_rail:
  related:
    - title: "Core Semantics"
      url: /program/research-agenda/recovery-requirements/
    - title: "Mathematical Refusals"
      url: /program/research-agenda/recovery-requirements/mathematics/refusals/
    - title: "Mathematics Problem Ledger"
      url: /program/research-agenda/problem-ledger/mathematics/
  meta:
    type: "Core Semantic Domain"
    scope: "Mathematics"
    status: "Canonical"
    updated: "April 2026"
---

{% assign items = site.recovery_requirements | where: "domain", "mathematics" | sort: "canonical_recovery_id" %}

## Why core semantics differs from open problems

The Mathematics Problem Ledger asks whether the kernel can express or re-ground Clay- and Langlands-scale stress tests. Mathematics Core Semantics asks which mathematical capacities must be earned before those stress tests can even be handled responsibly.

The semantic burden is not to import standard foundations wholesale. It is to carry formal checkability, finite syntax and proof objects, finite arithmetic and algebraic calculation, Euclidean geometry, representation of standard formal systems as object theories, and explicit bridge criteria into standard mathematics.

## Mathematical refusals

These core semantic targets must be read together with the [Mathematical Refusals]({{ '/program/research-agenda/recovery-requirements/mathematics/refusals/' | relative_url }}). The tau-kernel does not earn mathematical language by silently importing unrestricted classical background assumptions.

## Core semantic targets

<div class="dep-list">
  {% for item in items %}
  {% if item.item_type == "recovery_requirement" %}
  <a class="dep-link" href="{{ item.url | relative_url }}">
    <span class="dep-id">{{ item.canonical_recovery_id }}</span>
    <span class="dep-title">{{ item.title }}</span>
    <span class="badge {% if item.recovery_status == 'partial' %}badge-partial{% else %}badge-neutral{% endif %}" style="margin-left:auto">{{ item.recovery_status | replace: "_", " " }}</span>
  </a>
  {% endif %}
  {% endfor %}
</div>

## Relation to Verify

Mathematics Core Semantics connects directly to formal verification, bridge verification, TauLib, and the meta-verification frontier. The page fixes the public burden; the Verify lane records how much of that burden has actually been discharged.
