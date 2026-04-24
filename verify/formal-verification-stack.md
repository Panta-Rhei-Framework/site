---
layout: program-doc
title: "Formal Verification Stack"
lane: verify
v2_lane: verify
type: "Verification Surface"
status: "Canonical"
permalink: /verify/formal-verification-stack/
summary_short: "The layered structure by which the formal core of the program is checked."
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

Formal verification in this program has multiple levels. They must not be collapsed into one confidence label.

<div class="v2-system-strip" aria-label="Formal verification stack">
  <a class="v2-system-node" href="{{ '/publications/books/' | relative_url }}">Publications</a>
  <a class="v2-system-node" href="{{ '/corpus/registry/' | relative_url }}">Corpus Registry</a>
  <a class="v2-system-node" href="{{ '/verify/taulib/' | relative_url }}">TauLib</a>
  <a class="v2-system-node" href="{{ '/verify/release-manifest/' | relative_url }}">Release Manifest</a>
  <a class="v2-system-node" href="{{ '/verify/how-to-audit/' | relative_url }}">Independent Audit</a>
</div>

## Level 1 — Kernel Integrity Verification

This asks whether the formal kernel holds together internally as a coherent formal system. It includes Lean modules compiling, proof chains closing, theorem dependencies connecting, and the public registry aligning with the corresponding formal objects where such alignment is claimed.

**Result:** formal certification relative to the Lean kernel and the stated formalization scope.

## Level 2 — Standard-Foundation Verification

This asks whether selected hinge theorems can also be re-established in standard foundations. The purpose is to reduce dependence on a custom system for especially load-bearing claims and to build overlap with standard formal mathematics.

**Result:** independent re-establishment of selected key theorems where such parallel work exists.

## Level 3 — Bridge Verification

This asks whether bridge constructions from the kernel into standard mathematics genuinely support the transfer claims being made. Internal analogues are not enough; the bridge must be adequate for the transfer burden.

**Result:** bridge-verified recovery and transfer claims where established.

## Current Surfaces

- **Publications** provide the narrative and mathematical exposition.
- **Corpus Registry** gives the structured spine: IDs, types, dependencies, and source locations.
- **TauLib** exposes the Lean 4 formalization and documentation surface.
- **Release Manifest** pins the inspected public state so counts and provenance can be reconciled.
- **Audit Pages** explain the remaining trust budget, bridge assumptions, and reviewer routes.

## Meta-Verification Boundary

The formal stack checks internal derivations where the formalization reaches. It does not automatically settle empirical adequacy, interpretive bridge claims, or the residual externality of the verifier itself. That last issue is treated in the [Meta-Verification Frontier]({{ '/verify/meta-verification-frontier/' | relative_url }}).
