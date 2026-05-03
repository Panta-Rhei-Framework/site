---
layout: program-doc
title: "Life Problem Ledger"
lane: agenda
v2_lane: agenda
section: research-agenda
type: "Problem Ledger Domain"
status: "Canonical"
summary_short: "Biology and neuroscience as external stress tests for life and mind."
right_rail:
  related:
    - title: "Problem Ledger"
      url: /program/research-agenda/problem-ledger/
    - title: "Source Policy"
      url: /program/research-agenda/problem-ledger-source-policy/
    - title: "Life Results"
      url: /results/topic/biology/
  meta:
    type: "Domain Ledger"
    scope: "Life"
    status: "Canonical"
    updated: "April 2026"
---

{% assign items = site.problem_ledger | where: "domain", "life" | sort: "title" %}

## Source rule

Life uses the pinned biology and neuroscience master ledgers. Medicine is excluded as a v2 master ledger because it is primarily clinical and translational rather than the core life-system stress test.

## Import Coverage

This domain is part of Problem Ledger v1.0. Every declared source entry for this domain has been mapped to a promoted public problem item or to an explicit merged record.

Life uses the full pinned biology and neuroscience ledgers. Medicine is excluded from the v1.0 master ledger policy.

<table>
  <thead>
    <tr>
      <th scope="col">Domain</th>
      <th scope="col">Source scope</th>
      <th scope="col">Public items</th>
      <th scope="col">Merged</th>
      <th scope="col">Excluded</th>
      <th scope="col">Deferred</th>
    </tr>
  </thead>
  <tbody>
    <tr><th scope="row">Life</th><td>112</td><td>102</td><td>10</td><td>0</td><td>0</td></tr>
  </tbody>
</table>

## Public Problem Items

<div class="dep-list">
  {% for problem in items %}
  <a class="dep-link" href="{{ problem.url | relative_url }}">
    <span class="dep-id">{{ problem.canonical_problem_id }}</span>
    <span class="dep-title">{{ problem.title }}</span>
    <span class="chip" style="margin-left:auto">{{ problem.program.result_status | replace: "_", " " }}</span>
  </a>
  {% endfor %}
</div>

## Merged Source Entries

Ten biology/neuroscience overlaps are merged into canonical public items. The public pages retain the relevant source-entry IDs so the source accounting remains visible.

## Excluded Source Entries

_No Life source entries are excluded in v1.0. Medicine remains excluded as a master ledger source rather than as item-level exclusions._

## Deferred Source Entries

_No Life source entries are deferred in v1.0._

## Related Results Mirror

See [Problem Ledger Answers: Life]({{ '/results/problem-ledger-answers/life/' | relative_url }}).
