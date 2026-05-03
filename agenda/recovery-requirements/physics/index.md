---
layout: program-doc
title: "Physics Recovery Requirements"
lane: agenda
v2_lane: agenda
section: research-agenda
type: "Recovery Domain"
status: "Canonical"
summary_short: "What the tau-kernel must recover from established physics before it can claim to describe physical reality."
right_rail:
  related:
    - title: "Recovery Requirements"
      url: /agenda/recovery-requirements/
    - title: "Physics Problem Ledger"
      url: /agenda/problem-ledger/physics/
    - title: "Physics Results"
      url: /results/topic/physics/
  meta:
    type: "Recovery Domain"
    scope: "Physics"
    status: "Canonical"
    updated: "April 2026"
---

{% assign items = site.recovery_requirements | where: "domain", "physics" | sort: "canonical_recovery_id" %}

## Why physics recovery begins with measurement

Physics recovery is not just equation recovery. A candidate kernel must recover physical quantity types, dimensional algebra, internal units, empirical calibration bridges, constants, dynamical laws, regime transitions, and measurement conditions.

SI is a bridge target, not a primitive input. Dimensionful constants require unit bridges; dimensionless constants and ratios are sharper numerical targets.

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

## Relation to the Physics Problem Ledger

The Physics Problem Ledger tracks open questions. Physics Recovery tracks the baseline measurement-and-law architecture those questions presuppose.
