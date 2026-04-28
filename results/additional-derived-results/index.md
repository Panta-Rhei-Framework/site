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
{% assign mathematics_results = results | where: "topic", "mathematics" %}
{% assign physics_results = results | where: "topic", "physics" %}
{% assign biology_results = results | where: "topic", "biology" %}
{% assign philosophy_results = results | where: "topic", "philosophy" %}
{% assign type_groups = results | group_by: "result_type" | sort: "name" %}

## What belongs here

Additional Derived Results are results produced by the framework that are not direct entries in the external Problem Ledger, not simply Recovery Target mappings, and not selected as curated landmarks.

They include domain-specific derived results, explanatory results, bridge results, supporting results, and consequences that still belong to the program's output.

<div class="notice note"><strong>Boundary note.</strong> This page is not an accountability mirror. Declared open-problem obligations belong to [Problem Ledger Answers]({{ '/results/problem-ledger-answers/' | relative_url }}), and declared recovery obligations belong to [Recovery Target Status]({{ '/results/recovery-target-status/' | relative_url }}).</div>

## Browse by domain

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/results/topic/mathematics/' | relative_url }}">
    <strong>Mathematics</strong>
    <span>{{ mathematics_results | size }} result page(s) in the current catalogue.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/topic/physics/' | relative_url }}">
    <strong>Physics</strong>
    <span>{{ physics_results | size }} result page(s) in the current catalogue.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/topic/biology/' | relative_url }}">
    <strong>Life</strong>
    <span>{{ biology_results | size }} result page(s) in the current catalogue.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/topic/philosophy/' | relative_url }}">
    <strong>Metaphysics / Philosophy</strong>
    <span>{{ philosophy_results | size }} result page(s) in the current catalogue.</span>
  </a>
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
