---
layout: program-doc
title: "Formal Verification Stack"
lane: verify
v2_lane: verify
type: "Verification Surface"
status: "Canonical"
permalink: /verify/formal-verification-stack/
summary_short: "How TauLib, release manifests, filter rules, and audit pages fit together as the formal verification surface of the site."
summary_cards:
  - title: "Lean layer"
    body: "TauLib is the machine-checkable formalization surface."
  - title: "Manifest layer"
    body: "Release manifests pin the public snapshot, counts, and provenance."
  - title: "Audit layer"
    body: "Verifier and assessment pages explain what the formal layer does and does not establish."
right_rail:
  related:
    - title: "TauLib"
      url: /verify/taulib/
    - title: "TauLib Status"
      url: /verify/taulib/status/
    - title: "Release Manifest"
      url: /verify/release-manifest/
    - title: "Filter Rules"
      url: /verify/filter-rules/
  meta:
    type: "Verification Surface"
    status: "Canonical"
    updated: "April 2026"
---

## Stack Overview

The formal verification stack is the route from public claim to checkable artifact. It is deliberately static and reproducible: a reader can inspect the website, the release manifest, and TauLib without depending on hidden services.

<div class="v2-system-strip" aria-label="Formal verification stack">
  <a class="v2-system-node" href="{{ '/publications/books/' | relative_url }}">Publications</a>
  <a class="v2-system-node" href="{{ '/corpus/registry/' | relative_url }}">Corpus Registry</a>
  <a class="v2-system-node" href="{{ '/verify/taulib/' | relative_url }}">TauLib</a>
  <a class="v2-system-node" href="{{ '/verify/release-manifest/' | relative_url }}">Release Manifest</a>
  <a class="v2-system-node" href="{{ '/verify/how-to-audit/' | relative_url }}">Independent Audit</a>
</div>

## What Each Layer Does

- **Publications** provide the narrative and mathematical exposition.
- **Corpus Registry** gives the structured spine: IDs, types, dependencies, and source locations.
- **TauLib** exposes the Lean 4 formalization and documentation surface.
- **Release Manifest** pins the inspected public state so counts and provenance can be reconciled.
- **Audit Pages** explain the remaining trust budget, bridge assumptions, and reviewer routes.

## Boundary

The formal stack checks internal derivations where the formalization reaches. It does not automatically settle empirical adequacy, interpretive bridge claims, or downstream public-good consequences. Those remain routed through Results, Verify, and Impact.
