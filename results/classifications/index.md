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
    - title: "Problem Answers"
      url: /results/problem-ledger-answers/
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

The current Results surface makes those differences explicit through frontmatter, badges, right-rail metadata, and search filters.

## Classification families

{% assign type_descriptions = "consequence::Domain-facing consequences and answer surfaces that read from the constructed Corpus.;foundational_math::Mathematical spine results that carry kernel, self-enrichment, and formal-structure burdens.;frontier_problem::Problem-ledger answer routes that classify public stress-test problems without implying external settlement.;structural_readout::Interpretive world-readout or cross-domain consequences that depend on the Corpus architecture." | split: ";" %}

<ul class="v2-grid v2-card-list">
  {% for group in type_groups %}
  {% assign description = "" %}
  {% for entry in type_descriptions %}
    {% assign parts = entry | split: "::" %}
    {% if parts[0] == group.name %}
      {% assign description = parts[1] %}
    {% endif %}
  {% endfor %}
  <li>
    <article class="v2-tile" id="{{ group.name | slugify }}">
      <h3>{{ group.name | replace: "_", " " | capitalize }}</h3>
      <p>{{ description | default: "A typed result family in the current public catalogue." }}</p>
      <p class="hero-meta">{{ group.size }} result pages currently use this type.</p>
    </article>
  </li>
  {% endfor %}
</ul>

## Status grammar

<div class="v2-grid">
  {% for group in status_groups %}
  <div class="v2-tile">
    <strong>
      {% case group.name %}
        {% when 'R' %}Internally addressed
        {% when 'P' %}Partial
        {% when 'Q' %}Qualitative
        {% when 'C' %}Contradicted
        {% when 'N' %}Not addressed
        {% else %}{{ group.name }}
      {% endcase %}
    </strong>
    <span>{{ group.size }} entries in the current catalogue.</span>
  </div>
  {% endfor %}
</div>

## Why this matters

The same catalogue contains internal formal claims, bridge claims, empirical mappings, predictions, and interpretive readouts. A reader should not have to infer which burden a page carries. “Internally addressed” means the program currently has an internal answer route; it does not mean external verification or scientific acceptance. The classification layer names that burden explicitly and links back to the [Program result criteria]({{ '/program/research-agenda/result-criteria/' | relative_url }}).
