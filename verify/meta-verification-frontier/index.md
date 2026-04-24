---
layout: program-doc
title: "Meta-Verification Frontier"
permalink: /verify/meta-verification-frontier/
lane: verify
v2_lane: verify
type: "Verification Surface"
verify_type: meta_frontier
status: "Canonical"
summary_short: "The remaining question of verifier externality, and the deeper closure ambitions of the program."
summary_cards:
  - title: "Current certification"
    body: "TauLib certification is meaningful relative to Lean and the stated release scope."
  - title: "Visible boundary"
    body: "The verifier itself remains external to the system being studied."
  - title: "Frontier, not excuse"
    body: "This page names a long-range frontier without weakening the current release's ordinary verification value."
right_rail:
  related:
    - title: "Formal Verification Stack"
      url: /verify/formal-verification-stack/
    - title: "TCB Disclosure"
      url: /verify/tcb/
    - title: "TauLib"
      url: /verify/taulib/
  meta:
    type: "Meta-Verification Frontier"
    status: "Canonical"
    updated: "April 2026"
---

## Core Issue

Current formal certification is relative to the Lean kernel. That is already meaningful and strong, but it remains formally external to the kernel being studied.

## Why This Is Not an Ordinary Defect

All externally hosted proof-assistant verification inherits verifier relativity. Lean, Coq, Isabelle, Agda, and similar systems all require trust in a proof kernel, toolchain, and computing environment. That is not unique to this program.

## Why It Matters More Here

The program makes stronger closure, categoricity, and self-grounding claims than an ordinary mathematical model. For that reason, the externality of the verifier becomes a visible meta-question rather than background infrastructure.

## Current Stance

- Lean-relative certification is fully meaningful within the current release state.
- No public page should imply that all external verifier dependence has already been eliminated.
- The remaining boundary is acknowledged explicitly through the trust-budget and formal-stack pages.

## Long-Range Frontier

Future work may explore richer internal proof-theoretic structure, deeper self-enrichment, internally hosted verification machinery, or compiler-equivalent structures realized inside the framework.

This is a frontier, not a present requirement for the work to count as serious.
