---
layout: "program-doc"
title: "Problem Ledger Answers"
permalink: "/results/problem-ledger-answers/"
lane: "results"
v2_lane: "results"
type: "Result Mirror"
status: "Canonical"
summary_short: "Current Results-side stances against public Problem Ledger seed items."
---

# Problem Ledger Answers

> Current program stances against the open and foundational problems accepted in the Research Agenda.

This is the Results-side answer mirror of the Program-side Problem Ledger. It reports where the current public result surface has an answer, partial answer, structural constraint, or pending stance.

<div class="notice note"><strong>Status note.</strong> A program stance is not the same as external acceptance, scientific settlement, or final verification.</div>

## Browse by domain

<div class="v2-grid">
{% assign problem_domain_groups = site.data.problem_ledger["problem-ledger"] | group_by: "domain_slug" %}
{% for item in problem_domain_groups %}
  <a class="v2-tile" href="{{ '/results/problem-ledger-answers/' | append: item.name | append: '/' | relative_url }}">
    <strong>{{ item.name | replace: '-', ' ' | capitalize }}</strong>
    <span>{{ item.items | size }} public seed item(s).</span>
  </a>
{% endfor %}
</div>

## Source policy

Problem source policy remains owned by the Research Agenda: [Problem Ledger Source Policy](/program/research-agenda/problem-ledger-source-policy/).
