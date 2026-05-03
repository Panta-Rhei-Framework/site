---
layout: program-doc
title: "Metaphysics Core Semantics"
title_plain: "Metaphysics Core Semantics"
lane: agenda
v2_lane: agenda
section: research-agenda
type: "Core Semantic Domain"
status: "Canonical"
summary_short: "The metaphysical language the tau-kernel must earn at the level of ontology, intelligibility, mind, meaning, and value."
right_rail:
  related:
    - title: "Core Semantics"
      url: /program/research-agenda/recovery-requirements/
    - title: "Metaphysics / Philosophy Problem Ledger"
      url: /program/research-agenda/problem-ledger/metaphysics-philosophy/
    - title: "Metaphysics World Readout"
      url: /results/world-readout/metaphysics/
  meta:
    type: "Core Semantic Domain"
    scope: "Metaphysics"
    status: "Canonical"
    updated: "April 2026"
---

{% assign items = site.recovery_requirements | where: "domain", "metaphysics" | sort: "canonical_recovery_id" %}

## Conceptual grammar

Metaphysics Core Semantics is not the claim that the program has solved all philosophy. It is the requirement that the kernel carry the conceptual grammar by which reality becomes intelligible at all: being, identity, relation, grounding, causality, modality, time, truth, mind, language, value, and ultimate boundary.

Ultimate questions must not be invisible to the kernel, but this page does not claim final answers to all ultimate questions.

## Core semantic targets

<div class="dep-list">
  {% for item in items %}
  <a class="dep-link" href="{{ item.url | relative_url }}">
    <span class="dep-id">{{ item.canonical_recovery_id }}</span>
    <span class="dep-title">{{ item.title }}</span>
    <span class="badge badge-neutral" style="margin-left:auto">{{ item.verification_status | replace: "_", " " }}</span>
  </a>
  {% endfor %}
</div>

## Relation to Life Core Semantics

The life-mind bridge belongs to Life Core Semantics, while Metaphysics Core Semantics asks how mind, subjectivity, meaning, and value become intelligible in the larger architecture of reality-description.
