---
layout: program-doc
title: "Metaphysics / Philosophy Problem Ledger"
lane: program
v2_lane: program
section: research-agenda
type: "Problem Ledger Domain"
status: "Canonical"
summary_short: "Philosophical problems as stress tests for ontology, knowledge, mind, meaning, and ethics."
right_rail:
  related:
    - title: "Problem Ledger"
      url: /program/research-agenda/problem-ledger/
    - title: "Source Policy"
      url: /program/research-agenda/problem-ledger-source-policy/
    - title: "Philosophy Results"
      url: /results/topic/philosophy/
  meta:
    type: "Domain Ledger"
    scope: "Metaphysics / Philosophy"
    status: "Canonical"
    updated: "April 2026"
---

{% assign items = site.problem_ledger | where: "domain", "metaphysics_philosophy" | sort: "title" %}

## Source rule

Metaphysics / Philosophy uses Wikipedia's list of philosophical problems. The site does not rename that source as an unsolved-problems-in-philosophy ledger, and v1.0 records the source warning about possible unverifiable material in the Corpus source manifest.

## Import Coverage

This domain is part of Problem Ledger v1.0. Every declared source entry for this domain has been mapped to a promoted public problem item or to an explicit merged record.

This domain uses Wikipedia's List of philosophical problems. It is not titled or treated as an "unsolved problems in philosophy" list.

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
    <tr><th scope="row">Metaphysics / Philosophy</th><td>27</td><td>27</td><td>0</td><td>0</td><td>0</td></tr>
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

_No Metaphysics / Philosophy source entries are merged in v1.0._

## Excluded Source Entries

_No Metaphysics / Philosophy source entries are excluded in v1.0._

## Deferred Source Entries

_No Metaphysics / Philosophy source entries are deferred in v1.0._

## Related Results Mirror

See [Problem Ledger Answers: Metaphysics / Philosophy]({{ '/results/problem-ledger-answers/metaphysics-philosophy/' | relative_url }}).
