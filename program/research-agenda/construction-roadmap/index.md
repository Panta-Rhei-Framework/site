---
layout: program-doc
title: "Construction Roadmap"
permalink: /program/research-agenda/construction-roadmap/
lane: program
v2_lane: program
section: research-agenda
type: "Agenda Page"
status: "Canonical"
summary_short: "The logical build-order required by the Research Agenda."
hero_ctas:
  - label: "Construction Spine"
    url: /corpus/construction-spine/
    primary: true
  - label: "Progress Against Agenda"
    url: /results/progress-against-agenda/
  - label: "Kernel, Model & Reality"
    url: /program/research-agenda/kernel-model-reality/
right_rail:
  related:
    - title: "Problem Ledger"
      url: /program/research-agenda/problem-ledger/
    - title: "Recovery Requirements"
      url: /program/research-agenda/recovery-requirements/
    - title: "Corpus Construction Spine"
      url: /corpus/construction-spine/
    - title: "Progress Against Agenda"
      url: /results/progress-against-agenda/
  meta:
    type: "Agenda Page"
    scope: "Logical construction order"
    status: "Canonical"
    updated: "April 2026"
---

{% assign steps = site.data.construction_spine["construction-spine"] %}

## This is not a timeline

The Construction Roadmap is not a calendar, sprint plan, or publication schedule. It is the logical build-order implied by the program's own burden of proof.

If the program seeks a no-externalities kernel of reality, it cannot begin by assuming mathematics, physics, life, mind, meaning, or lawfulness as finished inputs. These layers must be recovered in order.

## Why construction order matters

The other Research Agenda surfaces state what the program must face: open problems, recovery requirements, and the ontic-status burden. The Construction Roadmap explains how those burdens become a construction sequence.

<div class="v2-system-strip" aria-label="Construction sequence across lanes">
  <a href="{{ '/program/research-agenda/construction-roadmap/' | relative_url }}">Agenda obligation</a>
  <span>-></span>
  <a href="{{ '/corpus/construction-spine/' | relative_url }}">Corpus construction</a>
  <span>-></span>
  <a href="{{ '/results/progress-against-agenda/' | relative_url }}">Results status</a>
</div>

## The 10 construction steps

<div class="v2-grid">
{% for step in steps %}
  <a class="v2-tile" href="{{ step.corpus_path | relative_url }}">
    <strong>{{ step.sequence }}. {{ step.title }}</strong>
    <span>{{ step.required_to_do }}</span>
    <span class="chip">{{ step.build_status | replace: "_", " " }}</span>
  </a>
{% endfor %}
</div>

## How this roadmap appears in Corpus

In the Research Agenda, the sequence names obligations: what must be built and why. In the [Corpus Construction Spine]({{ '/corpus/construction-spine/' | relative_url }}), the same sequence becomes the public construction narrative: what has been built, where it appears in the Registry, how TauLib touches it, and which publications narrate it.

## How this roadmap appears in Results

In Results, the sequence is not the primary organizing principle. Results is where the built Corpus becomes a world: landmark consequences, world readouts, Problem Ledger answers, Recovery Target status, and the [Progress Against Agenda]({{ '/results/progress-against-agenda/' | relative_url }}) dashboard.

## Current status and next reading

Each step carries an internal build status. These statuses do not imply external acceptance or final verification. They are reading aids for tracing obligation, construction, result, and verification together.

