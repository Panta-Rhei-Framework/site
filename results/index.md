---
layout: program-doc
title: "Results"
permalink: /results/
lane: results
v2_lane: results
type: "Lane Root"
status: "Canonical"
summary_short: "What the program currently derives from its research corpus."
summary_cards:
  - title: "World consequence"
    body: "Results is where the built Corpus becomes a world."
  - title: "Mirrors"
    body: "Problem Ledger Answers and Recovery Target Status mirror declared Agenda obligations."
  - title: "Status"
    body: "Every result surface separates internal stance, verification, and external acceptance."
hero_ctas:
  - label: "Landmark Results"
    url: /results/landmark-results/
    primary: true
  - label: "World Readout"
    url: /results/world-readout/
  - label: "Progress Against Agenda"
    url: /results/progress-against-agenda/
right_rail:
  related:
    - title: "Landmark Results"
      url: /results/landmark-results/
    - title: "Problem Ledger Answers"
      url: /results/problem-ledger-answers/
    - title: "Recovery Target Status"
      url: /results/recovery-target-status/
    - title: "Progress Against Agenda"
      url: /results/progress-against-agenda/
    - title: "Result Classifications"
      url: /results/classifications/
    - title: "Corpus Registry"
      url: /corpus/registry/
    - title: "Verify"
      url: /verify/
  meta:
    type: "Lane Root"
    scope: "All results"
    status: "Canonical"
    updated: "April 2026"
---

{% assign result_count = site.data.results.results | size %}
{% assign topic_groups = site.data.results.results | group_by: "topic" | sort: "name" %}
{% assign type_groups = site.data.results.results | group_by: "result_type" | sort: "name" %}

## Results is where the built Corpus becomes a world

The [Corpus]({{ '/corpus/' | relative_url }}) shows how the structure was built. Results shows what follows from that construction: landmark consequences, world readouts, current answers to the Problem Ledger, recovery-target status, and additional derived results.

Every result should be read with its status markers. An internally addressed result is not the same as external verification or scientific acceptance.

The intended reading order is simple:

<div class="v2-system-strip" aria-label="Results pipeline">
  <a href="{{ '/program/research-agenda/' | relative_url }}">Agenda</a>
  <span>-></span>
  <a href="{{ '/corpus/' | relative_url }}">Corpus</a>
  <span>-></span>
  <a href="{{ '/results/' | relative_url }}">Results</a>
  <span>-></span>
  <a href="{{ '/verify/' | relative_url }}">Verify</a>
</div>

The Agenda states the burden. The Corpus carries the build. Results shows the current answers and world-readouts. Verify exposes the inspection routes.

## Six ways to read Results

<ol class="v2-grid v2-card-list">
  <li>
    <a class="v2-tile" href="{{ '/results/landmark-results/' | relative_url }}">
      <strong>Landmark Results</strong>
      <span>Curated high-impact consequences, status-marked and not exhaustive.</span>
    </a>
  </li>
  <li>
    <a class="v2-tile" href="{{ '/results/world-readout/' | relative_url }}">
      <strong>World Readout</strong>
      <span>Domain-level pictures of mathematics, physics, life, and metaphysics.</span>
    </a>
  </li>
  <li>
    <a class="v2-tile" href="{{ '/results/problem-ledger-answers/' | relative_url }}">
      <strong>Problem Ledger Answers</strong>
      <span>Current stances against accepted public open-problem stress tests.</span>
    </a>
  </li>
  <li>
    <a class="v2-tile" href="{{ '/results/recovery-target-status/' | relative_url }}">
      <strong>Recovery Target Status</strong>
      <span>Current recovery status against declared recovery requirements.</span>
    </a>
  </li>
  <li>
    <a class="v2-tile" href="{{ '/results/additional-derived-results/' | relative_url }}">
      <strong>Additional Derived Results</strong>
      <span>Framework results not captured by the curated landmarks or ledger mirrors.</span>
    </a>
  </li>
  <li>
    <a class="v2-tile" href="{{ '/results/progress-against-agenda/' | relative_url }}">
      <strong>Progress Against Agenda</strong>
      <span>A dashboard over problem and recovery obligations.</span>
    </a>
  </li>
</ol>

## Current state snapshot

The older result catalogue still uses the historical topic labels `biology` and `philosophy` in data. In the v2.2 public lane language, those correspond to the broader **Life** and **Metaphysics / Philosophy** agenda domains unless a page states a narrower scope.

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/results/browse/' | relative_url }}">
    <strong>{{ result_count }} total result pages</strong>
    <span>The full crawlable catalogue with filters for domain, kind, importance, status, and book.</span>
  </a>
  {% for group in topic_groups %}
  <a class="v2-tile" href="{{ '/results/topic/' | append: group.name | append: '/' | relative_url }}">
    <strong>{{ group.size }} {{ group.name | capitalize }}</strong>
    <span>Problem-facing results currently grouped under {{ group.name }}.</span>
  </a>
  {% endfor %}
</div>

## Result families

<div class="v2-grid">
  {% for group in type_groups %}
  <a class="v2-tile" href="{{ '/results/classifications/' | relative_url }}#{{ group.name | slugify }}">
    <strong>{{ group.name | replace: "_", " " | capitalize }}</strong>
    <span>{{ group.size }} entries in the current catalogue.</span>
  </a>
  {% endfor %}
</div>

## Core routes

- [Progress Against Agenda]({{ '/results/progress-against-agenda/' | relative_url }}) mirrors Results back to the Program lane.
- [Problem Ledger Answers]({{ '/results/problem-ledger-answers/' | relative_url }}) organizes current stances against public problem obligations.
- [Recovery Target Status]({{ '/results/recovery-target-status/' | relative_url }}) reports current recovery status against declared recovery requirements.
- [Result Classifications]({{ '/results/classifications/' | relative_url }}) explains what kind of result each page claims to be.
- [World Readout]({{ '/results/world-readout/' | relative_url }}) gives the domain-level picture implied by the current results.
- [Browse All Results]({{ '/results/browse/' | relative_url }}) exposes the full catalogue.
- Related Verify surfaces carry the sharpest empirical pressure points: [Predictions]({{ '/results/predictions/browse/' | relative_url }}), [Falsification Paths]({{ '/results/falsifications/browse/' | relative_url }}), and [Prediction Timing]({{ '/results/predictions/timing/' | relative_url }}).
