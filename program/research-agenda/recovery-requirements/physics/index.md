---
layout: program-doc
title: "Physics Core Semantics"
title_plain: "Physics Core Semantics"
lane: agenda
v2_lane: agenda
section: research-agenda
type: "Core Semantic Domain"
status: "Canonical"
summary_short: "The physical language the tau-kernel must earn before it can claim to describe physical reality."
right_rail:
  related:
    - title: "Core Semantics"
      url: /program/research-agenda/recovery-requirements/
    - title: "Physics Problem Ledger"
      url: /program/research-agenda/problem-ledger/physics/
    - title: "Physics Results"
      url: /results/topic/physics/
  meta:
    type: "Core Semantic Domain"
    scope: "Physics"
    status: "Canonical"
    updated: "April 2026"
---

{% assign items = site.recovery_requirements | where: "domain", "physics" | sort: "canonical_recovery_id" %}

## Why physics semantics begins with measurement

Physics Core Semantics is not just equation recovery. A candidate kernel must carry physical quantity types, dimensional algebra, internal units, empirical calibration bridges, constants, dynamical laws, regime transitions, and measurement conditions.

SI is a bridge target, not a primitive input. Dimensionful constants require unit bridges; dimensionless constants and ratios are sharper numerical targets.

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

## Relation to the Physics Problem Ledger

The Physics Problem Ledger tracks open questions. Physics Core Semantics tracks the baseline measurement-and-law architecture those questions presuppose.
