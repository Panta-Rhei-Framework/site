---
layout: program-doc
title: "Inspect & Verify"
lane: engage
v2_lane: engage
type: "Engagement Route"
status: "Canonical"
permalink: /engage/inspect-verify/
summary_short: "Inspection pathways for reviewers who want to trace claims through Results, Corpus, Verify, TauLib, and protocols."
summary_cards:
  - title: "Start from a result"
    body: "Choose a result page and follow its supporting surfaces."
  - title: "Trace to the corpus"
    body: "Use registry objects, identifiers, and dependency maps to inspect what is actually being claimed."
  - title: "Check verification"
    body: "Use TauLib, release manifests, assessment protocols, and falsification paths."
right_rail:
  related:
    - title: "Results"
      url: /results/
    - title: "Public Discussions"
      url: /engage/discussions/
    - title: "Corpus"
      url: /corpus/
    - title: "Verify"
      url: /verify/
    - title: "TauLib"
      url: /verify/taulib/
    - title: "Assessment Protocols"
      url: /verify/assessment-protocols/
  meta:
    type: "Engagement Route"
    scope: "Inspection"
    status: "Canonical"
    updated: "April 2026"
---

## Core Idea

Inspect & Verify is for readers who want to test the work structurally. The route begins with a visible claim, traces it into the corpus, and checks the relevant verification surface.

The program should not be evaluated only at the level of prose. Serious inspection follows identifiers, dependency structure, formalization status, empirical exposure, and stated scope.

## Inspection Paths

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/results/browse/' | relative_url }}">
    <h3>Start from Results</h3>
    <p>Choose a result, read its status, then inspect related corpus and verification references.</p>
  </a>
  <a class="v2-tile" href="{{ '/corpus/registry/' | relative_url }}">
    <h3>Trace to Corpus</h3>
    <p>Use registry identifiers, object types, aliases, and book provenance to locate the source object.</p>
  </a>
  <a class="v2-tile" href="{{ '/verify/' | relative_url }}">
    <h3>Check Verify</h3>
    <p>Use scientific rigor, verification framework, domain verification, and operational surfaces.</p>
  </a>
  <a class="v2-tile" href="{{ '/verify/taulib/' | relative_url }}">
    <h3>Inspect TauLib</h3>
    <p>Open the formalization surface and trace machine-checked parts back to public claims.</p>
  </a>
</div>

## Practical Workflow

1. Pick a claim in [Browse All Results]({{ '/results/browse/' | relative_url }}).
2. Note its type, status, domain, and related links.
3. Follow any registry or publication references into [Corpus]({{ '/corpus/' | relative_url }}) and [Publications]({{ '/publications/' | relative_url }}).
4. Use [Verify]({{ '/verify/' | relative_url }}) to select the relevant verification mode: formal, empirical, comparative, or protocol-based.
5. If the claim is formalized, inspect [TauLib]({{ '/verify/taulib/' | relative_url }}). If it is empirical, inspect [Predictions & Falsification]({{ '/verify/predictions-and-falsification/' | relative_url }}).

## What Good Inspection Produces

Good inspection names a specific object and a specific test. Examples include a broken dependency, a missing assumption, a mismatch between prose and registry source, a formalization gap, a prediction that should be reclassified, or a prior-art overlap that needs explicit treatment.

For structured public objections, continue to [Public Discussions]({{ '/engage/discussions/' | relative_url }}) or [Critique & Challenge]({{ '/engage/critique-challenge/' | relative_url }}). Use Issues for concrete defects and [Contact]({{ '/engage/contact/' | relative_url }}) for private or institutional routes.
