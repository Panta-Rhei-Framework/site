---
layout: program-doc
title: "Progress Against Agenda"
lane: results
v2_lane: results
permalink: /results/progress-against-agenda/
type: "Result Index"
status: "Canonical"
summary_short: "How the program's result surfaces map back to the research agenda."
summary_cards:
  - title: "Agenda mirror"
    body: "Aggregates public Problem Ledger and Recovery Requirement status."
  - title: "52 public records"
    body: "Seven Problem seed items and forty-five Recovery/Refusal items."
  - title: "Status discipline"
    body: "Internal progress is separated from verification and external acceptance."
right_rail:
  related:
    - title: "Research Agenda"
      url: /program/research-agenda/
    - title: "Problem Ledger"
      url: /results/problem-ledger-answers/
    - title: "Verify"
      url: /verify/
  meta:
    type: "Result Index"
    scope: "Agenda mirror"
    status: "Canonical"
    updated: "April 2026"
---

{% assign progress = site.data.agenda_progress["agenda-progress"] %}
{% assign problem_records = progress | where: "item_kind", "problem" %}
{% assign recovery_records = progress | where_exp: "item", "item.item_kind != 'problem'" %}
{% assign domain_groups = progress | group_by: "domain" | sort: "name" %}
{% assign status_groups = progress | group_by: "display_status" | sort: "name" %}

## Status disclaimer

Status indicates the current internal state of the research program. Proposed answer, partial recovery, or internally addressed status does not mean external verification, scientific acceptance, or final settlement.

## Summary metrics

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/results/problem-ledger-answers/' | relative_url }}">
    <strong>{{ problem_records | size }} Problem Ledger item(s)</strong>
    <span>Current public answer mirror for selected stress-test problems.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/recovery-target-status/' | relative_url }}">
    <strong>{{ recovery_records | size }} Recovery/Refusal item(s)</strong>
    <span>Current public recovery-status mirror for declared requirements.</span>
  </a>
  <a class="v2-tile" href="{{ '/corpus/construction-spine/' | relative_url }}">
    <strong>10 construction steps</strong>
    <span>The Corpus build narrative that anchors future progress mappings.</span>
  </a>
</div>

## Filter by domain

<div class="v2-grid">
{% for group in domain_groups %}
  <div class="v2-tile">
    <strong>{{ group.name | replace: "_", " " | capitalize }}</strong>
    <span>{{ group.items | size }} public agenda record(s).</span>
  </div>
{% endfor %}
</div>

## Filter by status

<div class="v2-grid">
{% for group in status_groups %}
  <div class="v2-tile">
    <strong>{{ group.name | replace: "_", " " | capitalize }}</strong>
    <span>{{ group.items | size }} record(s).</span>
  </div>
{% endfor %}
</div>

## Public records

<div class="v2-grid">
{% for item in progress %}
  <a class="v2-tile" href="{{ item.canonical_program_url | relative_url }}">
    <strong>{{ item.title }}</strong>
    <span>{{ item.item_kind | replace: "_", " " | capitalize }} · {{ item.display_domain }} · {{ item.display_status | replace: "_", " " }}</span>
  </a>
{% endfor %}
</div>
