---
layout: program-doc
title: "Additional Derived Results"
permalink: /results/additional-derived-results/
lane: results
v2_lane: results
type: "Result Index"
status: "Canonical"
summary_short: "Further framework results outside landmarks, Problem Ledger answers, and Recovery Target mappings."
hero_ctas:
  - label: "Browse All Results"
    url: /results/browse/
    primary: true
  - label: "Classifications"
    url: /results/classifications/
  - label: "World Readout"
    url: /results/world-readout/
right_rail:
  related:
    - title: "Results Overview"
      url: /results/
    - title: "Landmark Results"
      url: /results/landmark-results/
    - title: "Progress Against Agenda"
      url: /results/progress-against-agenda/
  meta:
    type: "Result Index"
    scope: "Additional derived results"
    status: "Canonical"
    updated: "April 2026"
---

{% assign results = site.data.results.results %}
{% assign domain_groups = results | group_by: "topic" | sort: "name" %}
{% assign type_groups = results | group_by: "result_type" | sort: "name" %}

## What belongs here

Additional Derived Results are results produced by the framework that are not direct entries in the external Problem Ledger, not simply Recovery Target mappings, and not selected as curated landmarks.

They include domain-specific derived results, explanatory results, bridge results, supporting results, and consequences that still belong to the program's output.

## Browse by domain

<div class="v2-grid">
{% for group in domain_groups %}
  <a class="v2-tile" href="{{ '/results/topic/' | append: group.name | append: '/' | relative_url }}">
    <strong>{{ group.name | capitalize }}</strong>
    <span>{{ group.items | size }} result page(s) in the current catalogue.</span>
  </a>
{% endfor %}
</div>

## Browse by result type

<div class="v2-grid">
{% for group in type_groups %}
  <a class="v2-tile" href="{{ '/results/classifications/' | relative_url }}#{{ group.name | slugify }}">
    <strong>{{ group.name | replace: "_", " " | capitalize }}</strong>
    <span>{{ group.items | size }} entries.</span>
  </a>
{% endfor %}
</div>

## Full catalogue

The complete crawlable catalogue remains available at [Browse All Results]({{ '/results/browse/' | relative_url }}).

