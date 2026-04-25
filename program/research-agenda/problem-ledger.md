---
layout: program-doc
title: "Problem Ledger"
lane: program
v2_lane: program
section: research-agenda
type: "Agenda Ledger"
status: "Canonical"
summary_short: "A typed ledger of the questions the program explicitly accepts as burdens of proof."
summary_cards:
  - title: "Source-pinned"
    body: "Problem items are generated from the versioned Corpus problem-ledger source."
  - title: "Domain-scoped"
    body: "Mathematics, physics, life, and metaphysics/philosophy each have explicit source rules."
  - title: "Mirror-ready"
    body: "Problem items link to Results where a current program stance already exists."
hero_ctas:
  - label: "Source Policy"
    url: /program/research-agenda/problem-ledger-source-policy/
    primary: true
  - label: "Physics Problem Ledger"
    url: /program/research-agenda/problem-ledger/physics/
  - label: "Results Mirror"
    url: /results/problem-ledger-answers/
right_rail:
  related:
    - title: "Problem Ledger Source Policy"
      url: /program/research-agenda/problem-ledger-source-policy/
    - title: "Mathematics Problem Ledger"
      url: /program/research-agenda/problem-ledger/mathematics/
    - title: "Physics Problem Ledger"
      url: /program/research-agenda/problem-ledger/physics/
    - title: "Life Problem Ledger"
      url: /program/research-agenda/problem-ledger/life/
    - title: "Metaphysics / Philosophy Problem Ledger"
      url: /program/research-agenda/problem-ledger/metaphysics-philosophy/
    - title: "Results Mirror"
      url: /results/problem-ledger-answers/
  meta:
    type: "Agenda Ledger"
    scope: "Program-wide"
    status: "Canonical"
    updated: "April 2026"
---

## Why this ledger exists

The program should not be judged only by the claims it prefers to highlight. It should also be judged by the questions it agrees to carry.

The Problem Ledger is the Program-side stress-test ledger. It imports or selects public problem spaces, records their source policy, and classifies whether the current framework can express, address, constrain, defer, reclassify, or reject each problem with reasons.

Import is not endorsement, solution, or priority. It is a commitment to visibility.

The source-policy architecture is now in place for all four agenda domains:

- Mathematics: Clay 7 + Langlands as selected foundational stress tests.
- Physics: full pinned Wikipedia physics ledger.
- Life: full biology + neuroscience ledgers.
- Metaphysics / Philosophy: full philosophical problems ledger.

The current public projection shows seed items while the wholesale import waves remain under Corpus review. These seed items prove the end-to-end projection path: source policy -> Corpus problem item -> public agenda page -> Results mirror.

## Start with the source policy

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/program/research-agenda/problem-ledger-source-policy/' | relative_url }}">
    <strong>Problem Ledger Source Policy</strong>
    <span>The method page for source selection, pinned revisions, import rules, and promotion into public projection.</span>
  </a>
  <a class="v2-tile" href="{{ '/program/research-agenda/problem-ledger/mathematics/' | relative_url }}">
    <strong>Mathematics Problem Ledger</strong>
    <span>Clay 7 + Langlands as selected foundational stress tests.</span>
  </a>
  <a class="v2-tile" href="{{ '/program/research-agenda/problem-ledger/physics/' | relative_url }}">
    <strong>Physics Problem Ledger</strong>
    <span>The pinned physics master ledger, currently represented publicly by seed items.</span>
  </a>
  <a class="v2-tile" href="{{ '/program/research-agenda/problem-ledger/life/' | relative_url }}">
    <strong>Life Problem Ledger</strong>
    <span>Biology and neuroscience master ledgers, with medicine excluded from the master ledger policy.</span>
  </a>
  <a class="v2-tile" href="{{ '/program/research-agenda/problem-ledger/metaphysics-philosophy/' | relative_url }}">
    <strong>Metaphysics / Philosophy Problem Ledger</strong>
    <span>The philosophical problems ledger for ontology, knowledge, mind, meaning, science, religion, and ethics.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/problem-ledger-answers/' | relative_url }}">
    <strong>Results Mirror</strong>
    <span>Where current program answers and partial answers are mirrored against the public problem burden.</span>
  </a>
</div>

## Domain Ledgers

{% assign problem_items = site.problem_ledger | sort: "title" %}

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/program/research-agenda/problem-ledger/mathematics/' | relative_url }}">
    <strong>Mathematics</strong>
    <span>Clay 7 + Langlands as selected foundational stress tests.</span>
  </a>
  <a class="v2-tile" href="{{ '/program/research-agenda/problem-ledger/physics/' | relative_url }}">
    <strong>Physics</strong>
    <span>Full pinned Wikipedia physics ledger, seeded here before wholesale import.</span>
  </a>
  <a class="v2-tile" href="{{ '/program/research-agenda/problem-ledger/life/' | relative_url }}">
    <strong>Life</strong>
    <span>Biology + neuroscience master ledgers, with medicine excluded from the core v2 ledger.</span>
  </a>
  <a class="v2-tile" href="{{ '/program/research-agenda/problem-ledger/metaphysics-philosophy/' | relative_url }}">
    <strong>Metaphysics / Philosophy</strong>
    <span>The philosophical problems ledger for ontology, knowledge, mind, meaning, science, religion, and ethics.</span>
  </a>
</div>

## Current Public Seed Items

These are not the full final ledgers. They are the current public v0.1 seed projection from the Corpus problem-ledger source. The full wholesale imports will be promoted after source capture, normalization, classification, and review.

<div class="dep-list">
  {% for problem in problem_items %}
  <a href="{{ problem.url | relative_url }}" class="dep-link">
    <span class="dep-id">{{ problem.canonical_problem_id }}</span>
    <span class="dep-title">{{ problem.title }}</span>
    <span class="chip" style="margin-left:auto">{{ problem.display_domain }}</span>
  </a>
  {% endfor %}
</div>

## Browse by Result Status

{% assign status_groups = problem_items | group_by: "program.result_status" | sort: "name" %}

<div class="v2-grid">
  {% for group in status_groups %}
  <div class="v2-tile">
    <strong>{{ group.name | replace: "_", " " | capitalize }}</strong>
    <span>{{ group.size }} seed item{% if group.size != 1 %}s{% endif %}.</span>
  </div>
  {% endfor %}
</div>

## Related Results Mirror

The [Results mirror]({{ '/results/problem-ledger-answers/' | relative_url }}) records current answers, partial answers, and open statuses. If no dedicated Result page exists yet, a Problem Ledger item remains visible as open or not yet classified rather than disappearing from the research agenda.
