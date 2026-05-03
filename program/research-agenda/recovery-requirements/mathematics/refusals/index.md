---
layout: program-doc
title: "Mathematical Refusals"
lane: agenda
v2_lane: agenda
section: research-agenda
type: "Core Semantic Boundary"
status: "Canonical"
summary_short: "What the tau-kernel refuses to import as primitive mathematical background."
right_rail:
  related:
    - title: "Mathematics Core Semantics"
      url: /program/research-agenda/recovery-requirements/mathematics/
    - title: "Core Semantics"
      url: /program/research-agenda/recovery-requirements/
    - title: "Formal Verification Stack"
      url: /verify/formal-verification-stack/
  meta:
    type: "Core Semantic Boundary"
    scope: "Mathematics"
    status: "Canonical"
    updated: "April 2026"
---

{% assign items = site.recovery_requirements | where: "item_type", "mathematical_refusal" | sort: "canonical_recovery_id" %}

## Why refusals matter

The mathematics agenda is not only defined by what language the kernel must earn. It is also defined by what the kernel refuses to import as primitive background: unrestricted power sets, unrestricted comprehension, unrestricted choice, arbitrary nonconstructive existence, completed uncountable totalities, silent contraction, impredicative large universes, and unqualified theorem transfer.

These refusals do not mean that classical mathematics is meaningless or invalid. They distinguish primitive ontology, object-language representation, constructive recovery, bridge transfer, and external classical proof.

## Refusal items

<div class="dep-list">
  {% for item in items %}
  <a class="dep-link" href="{{ item.url | relative_url }}">
    <span class="dep-id">{{ item.canonical_recovery_id }}</span>
    <span class="dep-title">{{ item.title }}</span>
    <span class="badge {% if item.verification_status == 'not_yet_verified' %}badge-muted{% else %}badge-neutral{% endif %}" style="margin-left:auto">{{ item.verification_status | replace: "_", " " }}</span>
  </a>
  {% endfor %}
</div>

## Foundational lineage

The tau-kernel stands near constructive mathematics, finitistic and ultrafinitistic discipline, and linear or substructural logic. It is not identical to any of those traditions. Its specific burden is to recover enough mathematics for reality-description under stricter coherence constraints and with explicit boundary behavior.
