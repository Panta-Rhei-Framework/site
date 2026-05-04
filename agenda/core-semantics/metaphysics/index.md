---
layout: program-doc
title: "Metaphysics Recovery Requirements"
lane: agenda
v2_lane: agenda
section: research-agenda
type: "Recovery Domain"
status: "Canonical"
summary_short: "What the tau-kernel must recover at the level of ontology, intelligibility, mind, meaning, and value."
right_rail:
  related:
    - title: "Recovery Requirements"
      url: /agenda/core-semantics/
    - title: "Metaphysics / Philosophy Problem Ledger"
      url: /agenda/problem-ledger/metaphysics-philosophy/
    - title: "Metaphysics World Readout"
      url: /results/world-readout/metaphysics/
  meta:
    type: "Recovery Domain"
    scope: "Metaphysics"
    status: "Canonical"
    updated: "April 2026"
---

{% assign items = site.core_semantics | where: "domain", "metaphysics" | sort: "canonical_recovery_id" %}

## Conceptual grammar recovery

Metaphysics recovery is not the claim that the program has solved all philosophy. It is the requirement that the kernel recover the conceptual grammar by which reality becomes intelligible at all: being, identity, relation, grounding, causality, modality, time, truth, mind, language, value, and ultimate boundary.

Ultimate questions must not be invisible to the kernel, but this page does not claim final answers to all ultimate questions.

## Recovery targets

<div class="dep-list">
  {% for item in items %}
  <a class="dep-link" href="{{ item.url | relative_url }}">
    <span class="dep-id">{{ item.canonical_recovery_id }}</span>
    <span class="dep-title">{{ item.title }}</span>
    <span class="badge badge-neutral" style="margin-left:auto">{{ item.verification_status | replace: "_", " " }}</span>
  </a>
  {% endfor %}
</div>

## Relation to Life Recovery

The life-mind bridge belongs to Life Recovery, while metaphysics recovery asks how mind, subjectivity, meaning, and value become intelligible in the larger architecture of reality-description.
