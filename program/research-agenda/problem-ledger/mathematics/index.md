---
layout: program-doc
title: "Mathematics Problem Ledger"
lane: agenda
v2_lane: agenda
section: research-agenda
type: "Problem Ledger Domain"
status: "Canonical"
summary_short: "Clay 7 + Langlands as selected foundational stress tests."
right_rail:
  related:
    - title: "Problem Ledger"
      url: /program/research-agenda/problem-ledger/
    - title: "Source Policy"
      url: /program/research-agenda/problem-ledger-source-policy/
    - title: "Mathematics Results"
      url: /results/topic/mathematics/
  meta:
    type: "Domain Ledger"
    scope: "Mathematics"
    status: "Canonical"
    updated: "April 2026"
---

{% assign items = site.problem_ledger | where: "domain", "mathematics" | sort: "title" %}

## Source rule

Mathematics uses selected foundational stress tests, not a wholesale open-math import. Problem Ledger v1.0 exposes all seven Clay Millennium Problems plus the Langlands Program.

## Import Coverage

This domain is part of Problem Ledger v1.0. Every declared source entry for this domain has been mapped to a promoted public problem item or to an explicit merged record.

Mathematics uses a selected foundational stress-test ledger: Clay 7 + Langlands.

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
    <tr><th scope="row">Mathematics</th><td>8</td><td>8</td><td>0</td><td>0</td><td>0</td></tr>
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

_No Mathematics source entries are merged in v1.0._

## Excluded Source Entries

_No Mathematics source entries are excluded in v1.0. GRH and Grand RH remain outside the initial standalone source policy._

## Deferred Source Entries

_No Mathematics source entries are deferred in v1.0._

## Related Results Mirror

See [Problem Ledger Answers: Mathematics]({{ '/results/problem-ledger-answers/mathematics/' | relative_url }}).
