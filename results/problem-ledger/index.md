---
layout: program-doc
title: "Problem Ledger Results Mirror"
lane: results
v2_lane: results
permalink: /results/problem-ledger/
type: "Result Index"
status: "Canonical"
summary_short: "Compatibility bridge to the v2.1 Problem Ledger Answers surface."
summary_cards:
  - title: "Question first"
    body: "Each entry is read as an answer to a named problem or burden."
  - title: "Status visible"
    body: "Resolved, partial, qualitative, contradicted, not addressed, open, or deferred."
  - title: "Mirror surface"
    body: "This page mirrors generated Corpus Problem Ledger items where result links already exist."
hero_ctas:
  - label: "Problem Ledger Answers"
    url: /results/problem-ledger-answers/
    primary: true
  - label: "Agenda Ledger"
    url: /program/research-agenda/problem-ledger/
  - label: "Classifications"
    url: /results/classifications/
right_rail:
  related:
    - title: "Program Problem Ledger"
      url: /program/research-agenda/problem-ledger/
    - title: "Browse All Results"
      url: /results/browse/
    - title: "World Readout"
      url: /results/world-readout/
  meta:
    type: "Result Index"
    scope: "Problem-facing results"
    status: "Canonical"
    updated: "April 2026"
---

{% assign results = site.data.results.results %}
{% assign problem_items = site.problem_ledger | sort: "title" %}
{% assign status_groups = results | group_by: "status_code" | sort: "name" %}

## v2.1 route

This page is retained as a compatibility bridge. The v2.1 Results-side mirror now lives at [Problem Ledger Answers]({{ '/results/problem-ledger-answers/' | relative_url }}).

The Program-side [Problem Ledger]({{ '/program/research-agenda/problem-ledger/' | relative_url }}) names external stress-test problems and records source policy. The Results-side mirror shows where the current Results lane already has an answer, partial answer, structural constraint, or open stance.

The current site still exposes the full crawlable [Browse All Results]({{ '/results/browse/' | relative_url }}) catalogue. This page narrows the view to Problem Ledger seed items and their linked Result pages.

Recovery-facing burden tracking belongs to the Program-side [Recovery Requirements]({{ '/program/research-agenda/recovery-requirements/' | relative_url }}) ledger.

## Current status distribution

<div class="v2-grid">
  {% for group in status_groups %}
  <div class="v2-tile">
    <strong>
      {% case group.name %}
        {% when 'R' %}Resolved
        {% when 'P' %}Partial
        {% when 'Q' %}Qualitative
        {% when 'C' %}Contradicted
        {% when 'N' %}Not Addressed
        {% else %}{{ group.name }}
      {% endcase %}
    </strong>
    <span>{{ group.size }} entries in the current catalogue.</span>
  </div>
  {% endfor %}
</div>

## Status grammar

Use the shared result status vocabulary:

- Resolved
- Partial
- Qualitative
- Contradicted
- Not Addressed
- Open
- Deferred

## Current catalogue

The full v1/v2 result catalogue remains available at [Browse All Results]({{ '/results/browse/' | relative_url }}).

## Problem Ledger Seed Mirror

<div class="dep-list">
  {% for problem in problem_items %}
  <div class="dep-link">
    <span class="dep-id">{{ problem.canonical_problem_id }}</span>
    <span class="dep-title">{{ problem.title }}</span>
    <span class="chip" style="margin-left:auto">{{ problem.program.result_status | replace: "_", " " }}</span>
  </div>
  {% if problem.related.results.size > 0 %}
    {% for result_id in problem.related.results %}
    {% assign matches = results | where: "id", result_id %}
    {% assign result = matches | first %}
    {% if result %}
    <a href="{{ result.url | relative_url }}" class="dep-link">
      <span class="dep-id">{{ result.id }}</span>
      <span class="dep-title">{{ result.title }}</span>
      <span class="chip" style="margin-left:auto">{{ result.status_code }}</span>
    </a>
    {% endif %}
    {% endfor %}
  {% else %}
  <div class="dep-link"><span class="dep-id">Pending</span><span class="dep-title">No dedicated Result page yet</span></div>
  {% endif %}
  {% endfor %}
</div>
