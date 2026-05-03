---
layout: program-doc
title: "Life Recovery Requirements"
lane: agenda
v2_lane: agenda
section: research-agenda
type: "Recovery Domain"
status: "Canonical"
summary_short: "What the tau-kernel must recover about living systems before it can claim to describe life."
right_rail:
  related:
    - title: "Recovery Requirements"
      url: /program/research-agenda/recovery-requirements/
    - title: "Life Problem Ledger"
      url: /program/research-agenda/problem-ledger/life/
    - title: "Life Results"
      url: /results/topic/biology/
  meta:
    type: "Recovery Domain"
    scope: "Life"
    status: "Canonical"
    updated: "April 2026"
---

{% assign items = site.recovery_requirements | where: "domain", "life" | sort: "canonical_recovery_id" %}

## Structural, not instance-level

The life recovery burden is not to derive the contingent inventory of Earth biology. It is to recover the structural grammar that makes life possible: boundary, energy throughput, encoding, heredity, reproduction, variation, evolution, development, classification, ecology, and the bridge from living regulation to cognition.

Earth life is the known calibration case, not the definition of life itself.

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

## Relation to the Life Problem Ledger

Biology and neuroscience remain external stress-test ledgers. Life Recovery names the structural preconditions that make those open problems addressable without assuming that life reduces to physics as an input premise.
