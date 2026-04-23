---
layout: program-doc
title: "Result Classifications"
lane: results
v2_lane: results
permalink: /results/classifications/
type: "Result Guide"
status: "Canonical"
summary_short: "The status and type grammar used to classify Panta Rhei result pages."
right_rail:
  related:
    - title: "Program Result Criteria"
      url: /program/research-agenda/result-criteria/
    - title: "Problem Ledger"
      url: /results/problem-ledger/
    - title: "Status and Claim Typing"
      url: /results/status-and-claim-typing/
  meta:
    type: "Result Guide"
    status: "Canonical"
    updated: "April 2026"
---

{% assign results = site.data.results.results %}
{% assign type_groups = results | group_by: "result_type" | sort: "name" %}
{% assign status_groups = results | group_by: "status_code" | sort: "name" %}

## Why classification matters

Not all results make the same kind of claim. Some are formal results, some are bridge claims, some are numerical predictions, and some are interpretive world readouts.

v2 makes those differences explicit through frontmatter, badges, right-rail metadata, and search filters.

## Classification families

<div class="v2-grid">
  {% for group in type_groups %}
  <div class="v2-tile" id="{{ group.name | slugify }}">
    <strong>{{ group.name | replace: "_", " " | capitalize }}</strong>
    <span>{{ group.size }} result pages currently use this type.</span>
  </div>
  {% endfor %}
</div>

## Status grammar

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

## Why this matters

The same catalogue contains internal formal claims, bridge claims, empirical mappings, predictions, and interpretive readouts. A reader should not have to infer which burden a page carries. The classification layer names that burden explicitly and links back to the [Program result criteria]({{ '/program/research-agenda/result-criteria/' | relative_url }}).
