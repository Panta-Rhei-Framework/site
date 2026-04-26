---
layout: "program-doc"
title: "Problem Ledger Answers"
permalink: "/results/problem-ledger-answers/"
lane: "results"
v2_lane: "results"
type: "Result Mirror"
status: "Canonical"
summary_short: "Current Results-side stances against public Problem Ledger items."
---

## Answer Mirror

> Current program stances against the open and foundational problems accepted in the Research Agenda.

This is the Results-side answer mirror of the Program-side Problem Ledger. It reports where the current public result surface has an answer, partial answer, structural constraint, or pending stance.

<div class="notice note"><strong>Status note.</strong> A program stance is not the same as external acceptance, scientific settlement, or final verification.</div>

## Browse by Domain

The Problem Ledger Answers mirror the Program-side Problem Ledger. Each domain page reports the current program stance against the imported or selected problem obligations.

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/results/problem-ledger-answers/mathematics/' | relative_url }}">
    <strong>Mathematics</strong>
    <span>8 public problem items.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/problem-ledger-answers/physics/' | relative_url }}">
    <strong>Physics</strong>
    <span>102 public problem items.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/problem-ledger-answers/life/' | relative_url }}">
    <strong>Life</strong>
    <span>102 public problem items.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/problem-ledger-answers/metaphysics-philosophy/' | relative_url }}">
    <strong>Metaphysics / Philosophy</strong>
    <span>27 public problem items.</span>
  </a>
</div>

## Current Status Summary

{% assign mirror_items = site.data.problem_ledger["problem-ledger"] %}
{% assign partial_answers = mirror_items | where_exp: "item", "item.program.result_status == 'partially_addressed'" %}
{% assign not_yet_classified = mirror_items | where_exp: "item", "item.program.result_status == 'not_yet_classified'" %}

<table>
  <thead>
    <tr>
      <th scope="col">Public status</th>
      <th scope="col">Count</th>
      <th scope="col">Meaning on this site</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Partially addressed</th>
      <td>{{ partial_answers | size }}</td>
      <td>The program has a visible Results-side stance, but not final settlement or external acceptance.</td>
    </tr>
    <tr>
      <th scope="row">Not yet touched</th>
      <td>{{ not_yet_classified | size }}</td>
      <td>The problem is publicly carried as an obligation without a current answer mirror.</td>
    </tr>
  </tbody>
</table>

## Source policy

Problem source policy remains owned by the Research Agenda: [Problem Ledger Source Policy](/program/research-agenda/problem-ledger-source-policy/). The mirror does not republish source prose; it reports the current program stance against pinned or institutionally selected source records.
