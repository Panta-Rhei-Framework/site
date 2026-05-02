---
layout: program-doc
title: "TauLib Inspection Bridge"
permalink: /verify/taulib/
lane: verify
v2_lane: verify
type: "Verification Bridge"
status: "Canonical"
summary_short: "Verify-side bridge into the Corpus-native TauLib module and declaration projection."
og_image: /assets/images/plates/plate-06-verification-matrix-og.jpg
twitter_image: /assets/images/plates/plate-06-verification-matrix-og.jpg
og_image_alt: "Scientific plate showing the Verify lane as a verification matrix for obligations, construction steps, results, formal proof checking, bridge adequacy, empirical tests, external assessment, and explicit limits."
hero_ctas:
  - label: "Browse TauLib"
    url: /verify/taulib/docs/
    primary: true
  - label: "Formalization Status"
    url: /verify/taulib/status/
  - label: "Verify Framework"
    url: /verify/verification-framework/
right_rail:
  related:
    - title: "TauLib Browser"
      url: /verify/taulib/docs/
    - title: "Formalization Status"
      url: /verify/taulib/status/
    - title: "Verification Framework"
      url: /verify/verification-framework/
    - title: "Formal Verification Stack"
      url: /verify/formal-verification-stack/
    - title: "Release Manifest"
      url: /verify/release-manifest/
  meta:
    type: "Verification Bridge"
    status: "Canonical"
    updated: "April 2026"
---

{% assign summary = site.data.taulib_projections.summary %}

## What TauLib Verifies

TauLib is the Lean formalization layer of the program. The active Lean development source remains the public [TauLib repository](https://github.com/Panta-Rhei-Research/taulib); the Corpus owns a pinned snapshot and generates the public module/declaration browser from that source.

The current projection contains **{{ summary.module_count }} modules** and **{{ summary.declaration_count }} declarations/evals**, pinned to commit [`{{ summary.source_commit | slice: 0, 7 }}`](https://github.com/Panta-Rhei-Research/taulib/commit/{{ summary.source_commit }}).

## TauLib inside the verification matrix

{% include scientific-plate.html id="plate-06-verification-matrix" variant="thumb" loading="lazy" caption="TauLib is one formalization surface inside the broader verification matrix. Lean compilation checks formalized obligations; it does not by itself establish empirical truth." %}

TauLib is one formalization surface inside the broader verification matrix. Lean compilation checks formalized obligations; it does not by itself establish empirical truth.

## What Verify still owns

Verify does not stop at “the Lean code compiles.” It asks the higher-level inspection questions:

- What does the formalization cover?
- What do the formal terms mean relative to the surrounding Corpus?
- Which bridges connect formal objects to mathematical, physical, biological, or metaphysical claims?
- Which claims remain empirical, semantic, interpretive, or externally assessable?
- Where should a reviewer challenge the assumptions rather than merely re-run compilation?

## Inspection routes

<ul class="v2-grid v2-card-list">
  <li><article class="v2-tile"><h3><a href="{{ '/verify/taulib/docs/' | relative_url }}">TauLib Browser</a></h3><p>Corpus-native module and declaration pages generated directly from the pinned Lean snapshot.</p></article></li>
  <li><article class="v2-tile"><h3><a href="{{ '/verify/taulib/status/' | relative_url }}">Formalization Status</a></h3><p>Current counts, source commit, custom-axiom count, and projection boundary.</p></article></li>
  <li><article class="v2-tile"><h3><a href="{{ '/verify/formal-verification-stack/' | relative_url }}">Formal Verification Stack</a></h3><p>How formal proof checking fits into the broader review workflow.</p></article></li>
  <li><article class="v2-tile"><h3><a href="{{ '/verify/verification-framework/' | relative_url }}">Verification Framework</a></h3><p>How formal, bridge, empirical, and external-status checks remain distinct.</p></article></li>
  <li><article class="v2-tile"><h3><a href="{{ '/verify/release-manifest/' | relative_url }}">Release Manifest</a></h3><p>The pinned public release context and count reconciliation surface.</p></article></li>
</ul>
