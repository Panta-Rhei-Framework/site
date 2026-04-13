---
title: "What Machine-Checked Verification Means for This Program"
date: 2026-04-08
summary_short: "Why TauLib exists and what 4,332 machine-checked theorems actually prove."
summary_medium: "The Lean 4 formalization of Category &tau; is not an afterthought. This note explains what TauLib verifies, what it cannot verify, and why the distinction matters for how the program should be read."
topics:
  - verification
  - foundations
  - methodology
related_results: []
related_framework_modules: []
related_publications: []
newsletter_ready: true
featured: true
right_rail:
  related:
    - title: "Research Notes"
      url: /research-notes/
    - title: "TauLib"
      url: /verify/taulib/
    - title: "Verify"
      url: /verify/
  meta:
    type: "Research Note"
    status: "Published"
    updated: "April 2026"
---

## The formalization

TauLib is the Lean 4 formalization library for Category &tau;. It currently comprises 450 modules, 125,771 lines of code, and 4,332 machine-checked theorems across six of the seven books (Books I through VI have 0 sorry; Book VII retains 3 intentional methodological sorry).

This is not a decorative badge. It is a structural commitment.

## What TauLib verifies

TauLib verifies the internal logical consistency of the derivation chains within the framework. When the framework says "Theorem X follows from Definitions A, B, and Axioms K0-K3," TauLib confirms that the proof is logically valid in constructive type theory.

This means:
- No hidden assumptions are smuggled into the proof
- No logical gaps exist between stated premises and conclusions
- The derivation is mechanically reproducible by anyone with a Lean 4 installation

## What TauLib does not verify

Machine-checked verification does not establish empirical truth. TauLib does not confirm that the framework's physical predictions match observation. It confirms only that *if* the axioms hold, *then* the theorems follow.

This is an important distinction. The framework could be internally consistent and empirically wrong. The formalization guards against one class of error (logical invalidity) but not another (empirical mismatch). Both matter.

## Why the distinction matters

A common misreading of formal verification is that it proves the theory is "correct." It does not. It proves that the theory is *coherent* &mdash; that its internal logic does not contradict itself. Whether the axioms capture reality is a separate question, answered by observation and experiment.

The program maintains this distinction explicitly. TauLib is the verification surface for logical structure. The falsification pack (220+ predictions with explicit precision bounds) is the verification surface for empirical adequacy. Both are public. Both are inspectable. Neither substitutes for the other.

## The 0-sorry discipline

The decision to maintain 0 sorry across Books I-VI is not a technical convenience. It is a research-program commitment: every theorem that the program publishes as "machine-checked" is genuinely machine-checked, without escape hatches.

The 3 sorry in Book VII are flagged as intentional and methodological &mdash; they mark points where the formalization of metaphysical concepts reaches the boundary of what current type theory can express. They are not bugs. They are honest scope markers.
