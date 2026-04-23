---
layout: program-doc
title: "Problem Ledger"
lane: results
v2_lane: results
permalink: /results/problem-ledger/
type: "Result Index"
status: "Canonical"
summary_short: "A structured entry point into the program's problem-facing result claims."
summary_cards:
  - title: "Question first"
    body: "Each entry is read as an answer to a named problem or burden."
  - title: "Status visible"
    body: "Resolved, partial, qualitative, contradicted, not addressed, open, or deferred."
  - title: "Mirror surface"
    body: "This page mirrors Program > Research Agenda > Problem Ledger."
hero_ctas:
  - label: "Browse All Results"
    url: /results/browse/
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
{% assign status_groups = results | group_by: "status_code" | sort: "name" %}

## What the ledger does

The Problem Ledger organizes result pages by the questions they answer or partially address.

The current site already exposes a crawlable [Browse All Results]({{ '/results/browse/' | relative_url }}) catalogue. v2 adds this problem-ledger surface so readers can distinguish recognized external problems, internal structural readouts, quantitative predictions, and conditional consequences.

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

## Featured problem entries

<div class="dep-list">
  {% for result in results limit: 18 %}
  <a href="{{ result.url | relative_url }}" class="dep-link">
    <span class="dep-id">{{ result.id }}</span>
    <span class="dep-title">{{ result.title }}</span>
    <span class="chip" style="margin-left:auto">{{ result.status_code }}</span>
  </a>
  {% endfor %}
</div>
