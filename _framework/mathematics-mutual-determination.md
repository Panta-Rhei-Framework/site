---
title: Mutual Determination
module_id: E0-014
layer: E0
strand: interior
summary_short: Five descriptions of holomorphic structure are the same object — the
  5-way equivalence.
thesis: Refinement tails, spectral tails, omega-germs, boundary characters, and Hartogs
  continuations are mutually determining via bipolar decomposition.
canonical_books:
- II
source_parts:
- II.6
- II.7
key_registry:
- II.T27
- II.L02
- II.L03
- II.L04
- II.L05
depends_on:
- E0-012
- E0-013
unlocks:
- E0-015
right_rail:
  related:
  - title: The Split-Complex Shift
    url: /framework/mathematics-split-complex-shift/
  - title: Omega-Germ Construction & Profinite Tower
    url: /framework/mathematics-omega-germ-construction/
  - title: The Central Theorem
    url: /framework/mathematics-central-theorem/
  meta:
    type: Framework Module
    layer: E0 Mathematics
    strand: Interior
    status: Canonical
    updated: April 2026
---

## Overview

Five apparently different descriptions of holomorphic structure -- refinement tails, spectral tails, omega-germs, boundary characters, and Hartogs continuations -- turn out to be the *same thing*. The **Mutual Determination Theorem** (II.T27) proves that each description uniquely determines all four others via the bipolar idempotent decomposition. This is the central unification theorem of [Book II]({{ '/publications/books/book-ii/' | relative_url }}): it shows that the framework's holomorphic machinery is not an assemblage of loosely related tools but a single coherent structure seen from five angles.

## The Core Idea

The theorem rests on the **Idempotent Decomposition Lemma** (II.L07): every <math><mi>&tau;</mi></math>-holomorphic function <math><mi>f</mi></math> decomposes canonically as <math><mrow><mi>f</mi><mo>=</mo><msub><mi>e</mi><mo>+</mo></msub><mo>&sdot;</mo><msub><mi>f</mi><mo>+</mo></msub><mo>+</mo><msub><mi>e</mi><mo>&minus;</mo></msub><mo>&sdot;</mo><msub><mi>f</mi><mo>&minus;</mo></msub></mrow></math>. The decomposition is canonical (no choices), functorial (channels do not mix under composition), and complete (<math><msub><mi>f</mi><mo>+</mo></msub></math> and <math><msub><mi>f</mi><mo>&minus;</mo></msub></math> together determine <math><mi>f</mi></math> uniquely).

A three-lemma chain then establishes the equivalence:

1. **Branch Factorization** (II.L08): omega-germs factor through bipolar idempotents
2. **Prime-Split Support** (II.L09): the factorization is supported exactly on the B/C prime partition from [Prime Polarity]({{ '/framework/mathematics-prime-polarity/' | relative_url }})
3. **Polarity Symmetry** (II.L10): the two sectors are interchanged by the <math><mi>j</mi></math>-involution

Together these prove: **holomorphic <math><mo>&hArr;</mo></math> idempotent-supported** (II.T29). A function is <math><mi>&tau;</mi></math>-holomorphic if and only if it decomposes cleanly into two independent sector components. This collapses five descriptions into one:

- *Refinement tail* = a compatible tower on the primorial filtration
- *Spectral tail* = a sequence of spectral coefficients
- *Omega-germ* = a limit element in the profinite completion
- *Boundary character* = a character on the [lemniscate]({{ '/framework/mathematics-prime-polarity/' | relative_url }})
- *Hartogs continuation* = the unique [extension]({{ '/framework/mathematics-global-hartogs/' | relative_url }}) from boundary to interior

Each determines all others. The five-way equivalence is the mathematical reason the framework can read off physical constants from boundary data.

## Why This Matters

Mutual determination means the framework has *one* holomorphic concept, not five. A physicist working with boundary characters, a number theorist working with spectral tails, and an analyst working with Hartogs continuations are all manipulating the same object. This structural unity is what makes the [Central Theorem]({{ '/framework/mathematics-central-theorem/' | relative_url }}) possible -- it equates holomorphic functions on <math><msup><mi>&tau;</mi><mn>3</mn></msup></math> with the spectral algebra of <math><mi>L</mi></math>, and mutual determination is the engine that drives the isomorphism.

## Key Claims

1. **II.T27** -- Mutual Determination: five descriptions are equivalent *(established, machine-checked in [TauLib]({{ '/verify/taulib/' | relative_url }}))*
2. **II.L07** -- Idempotent Decomposition: canonical, functorial, complete *(established, machine-checked)*
3. **II.T29** -- Holomorphic = idempotent-supported *(established, machine-checked)*
4. **II.L08-L10** -- Three-lemma chain: branch factorization, prime-split support, polarity symmetry *(established, machine-checked)*

## Canonical Source

This module traces to **Book II**, Parts II.6, II.7.
