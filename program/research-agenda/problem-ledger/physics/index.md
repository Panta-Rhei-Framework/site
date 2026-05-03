---
layout: program-doc
title: "Physics Problem Ledger"
lane: agenda
v2_lane: agenda
section: research-agenda
type: "Problem Ledger Domain"
status: "Canonical"
summary_short: "The physics master ledger as an external stress test for formalized reality-description."
right_rail:
  related:
    - title: "Problem Ledger"
      url: /program/research-agenda/problem-ledger/
    - title: "Source Policy"
      url: /program/research-agenda/problem-ledger-source-policy/
    - title: "Physics Results"
      url: /results/topic/physics/
  meta:
    type: "Domain Ledger"
    scope: "Physics"
    status: "Canonical"
    updated: "April 2026"
---

{% assign items = site.problem_ledger | where: "domain", "physics" | sort: "title" %}

## Source rule

Physics uses the full pinned Wikipedia list of unsolved problems in physics as the master ledger. Problem Ledger v1.0 promotes the extracted named entries into public agenda items while keeping solution, verification, and external acceptance separate.

## Import Coverage

This domain is part of Problem Ledger v1.0. Every declared source entry for this domain has been mapped to a promoted public problem item or to an explicit merged record.

Physics uses the full pinned Wikipedia physics open-problem ledger.

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
    <tr><th scope="row">Physics</th><td>102</td><td>102</td><td>0</td><td>0</td><td>0</td></tr>
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

_No Physics source entries are merged in v1.0._

## Excluded Source Entries

_No Physics source entries are excluded in v1.0; historical solved sections and non-entry source sections were skipped during extraction rather than admitted as source entries._

## Deferred Source Entries

_No Physics source entries are deferred in v1.0._

## Related Results Mirror

See [Problem Ledger Answers: Physics]({{ '/results/problem-ledger-answers/physics/' | relative_url }}).
