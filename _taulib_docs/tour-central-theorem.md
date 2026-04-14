---
layout: taulib-doc
title: "TauLib.Tour.CentralTheorem"
permalink: /verify/taulib/docs/tour-central-theorem/
lane: verify
module_name: "TauLib.Tour.CentralTheorem"
book: "Tour"
book_label: "Tours"
right_rail:
  related:
  - title: TauLib Overview
    url: /verify/taulib/
  - title: Architecture
    url: /verify/taulib/architecture/
  artifacts:
  - title: Source on GitHub
    url: https://github.com/Panta-Rhei-Research/taulib
    external: true
  meta:
    type: "API Documentation"
    book: "Book Tour"
    status: "Frozen"
    updated: "April 2026"
---

# Tour 02: The Central Theorem


A guided walk through the climax of Book II:

**O(tau^3) = A_spec(L)**

The ring of tau-holomorphic functions on the fibered product tau^3 is
canonically isomorphic to the spectral algebra of the lemniscate L.

This tour covers:

- The split-complex boundary ring H = Z[j] and its sector decomposition

- The tau^3 fibered product: base tau^1, fiber T^2, and why it is NOT a product

- Boundary characters: idempotent-supported maps from the profinite boundary

- The Central Theorem itself: all four links of the isomorphism

- Spectral ring and holographic principle


**Prerequisites:** Tour/Foundations.lean (generators, axioms, iota_tau).
Step through this file in VS Code with the Lean 4 extension — hover over
`#check` and `#eval` to see types and computed values.
