---
layout: "program-doc"
title: "Recovery Target Status"
permalink: "/results/recovery-target-status/"
lane: "results"
v2_lane: "results"
type: "Result Mirror"
status: "Canonical"
summary_short: "Current Results-side status against public Recovery Requirements."
---

# Recovery Target Status

> Current program status against the structures the kernel promised to recover.

This is the Results-side mirror of the Program-side Recovery Requirements ledger. Recovery requirements remain obligations; this surface reports their current public status.

<div class="notice note"><strong>Status note.</strong> Partial or internally addressed recovery is not the same as formal verification or external acceptance.</div>

## Browse by domain

<div class="v2-grid">
{% assign groups = site.data.recovery_requirements["recovery-requirements"] | group_by: "domain_slug" %}
{% for group in groups %}
  <a class="v2-tile" href="{{ '/results/recovery-target-status/' | append: group.name | append: '/' | relative_url }}">
    <strong>{{ group.name | replace: '-', ' ' | capitalize }}</strong>
    <span>{{ group.items | size }} recovery/refusal item(s).</span>
  </a>
{% endfor %}
</div>
