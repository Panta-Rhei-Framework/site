---
layout: program-doc
title: "Legacy Problem Ledger Compatibility"
lane: results
v2_lane: results
permalink: /results/problem-ledger/
type: "Compatibility Bridge"
status: "Compatibility"
summary_short: "Legacy compatibility bridge to the canonical Problem Answers surface."
summary_cards:
  - title: "Question first"
    body: "Each entry is read as an answer to a named problem or burden."
  - title: "Status visible"
    body: "Internally addressed, partial, qualitative, contradicted, not addressed, open, or deferred."
  - title: "Mirror surface"
    body: "This page mirrors generated Corpus Problem Ledger items where result links already exist."
hero_ctas:
  - label: "Problem Answers"
    url: /results/problem-ledger-answers/
    primary: true
  - label: "Agenda Ledger"
    url: /agenda/problem-ledger/
  - label: "Classifications"
    url: /results/classifications/
right_rail:
  related:
    - title: "Program Problem Ledger"
      url: /agenda/problem-ledger/
    - title: "Browse All Results"
      url: /results/browse/
    - title: "World Readout"
      url: /results/world-readout/
  meta:
    type: "Compatibility Bridge"
    scope: "Problem-facing results"
    status: "Compatibility"
    updated: "April 2026"
---

{% assign results = site.data.results.results %}
{% assign problem_items = site.problem_ledger | sort: "title" %}
{% assign status_groups = results | group_by: "status_code" | sort: "name" %}

## v2.1 route

This page is retained as a compatibility bridge. The Results-side mirror now lives at [Problem Answers]({{ '/results/problem-ledger-answers/' | relative_url }}).

The Program-side [Problem Ledger]({{ '/agenda/problem-ledger/' | relative_url }}) names external stress-test problems and records source policy. The Results-side mirror shows where the current Results lane already has an answer, partial answer, structural constraint, or open stance.

The current site still exposes the full crawlable [Browse All Results]({{ '/results/browse/' | relative_url }}) catalogue. This page is now a compatibility bridge to the [Problem Answers]({{ '/results/problem-ledger-answers/' | relative_url }}) mirror.

Recovery-facing burden tracking belongs to the Program-side [Recovery Requirements]({{ '/agenda/core-semantics/' | relative_url }}) ledger.

## Current status distribution

<div class="v2-grid">
  {% for group in status_groups %}
  <div class="v2-tile">
    <strong>
      {% case group.name %}
        {% when 'R' %}Internally addressed
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

- Internally addressed
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
