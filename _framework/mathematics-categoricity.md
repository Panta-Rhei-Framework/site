---
title: Categoricity & the Liouville Dodge
module_id: E0-016
layer: E0
strand: interior
summary_short: τ³ is unique up to isomorphism; Liouville's theorem does not apply.
thesis: Six axioms force τ³ uniquely; j² = +1 gives wave-type operators that avoid
  the maximum principle, allowing non-constant bounded holomorphic functions.
canonical_books:
- II
source_parts:
- II.9
key_registry:
- II.T41
- II.T42
- II.D61
depends_on:
- E0-015
- E0-012
unlocks: []
right_rail:
  related:
  - title: The Central Theorem
    url: /framework/mathematics-central-theorem/
  - title: The Split-Complex Shift
    url: /framework/mathematics-split-complex-shift/
  meta:
    type: Framework Module
    layer: E0 Mathematics
    strand: Interior
    status: Canonical
    updated: April 2026
---

## Overview

The [Central Theorem]({{ '/framework/mathematics-central-theorem/' | relative_url }}) proves that <math><mrow><mi>O</mi><mo>(</mo><msup><mi>&tau;</mi><mn>3</mn></msup><mo>)</mo><mo>&cong;</mo><msub><mi>A</mi><mtext>spec</mtext></msub><mo>(</mo><mi>L</mi><mo>)</mo></mrow></math>. But is this the *only* such isomorphism? Could a different set of axioms produce a different fibered product with the same boundary algebra? The Categoricity Theorem answers: no. The seven axioms K0-K6 force <math><msup><mi>&tau;</mi><mn>3</mn></msup></math> uniquely. There is exactly one model, and the split-complex signature <math><mrow><msup><mi>j</mi><mn>2</mn></msup><mo>=</mo><mo>+</mo><mn>1</mn></mrow></math> is what makes this possible.

## The Core Idea

The **Categoricity Theorem** (II.T42) proves that the moduli space of models satisfying K0-K6 is a single point: <math><mrow><mi>M</mi><mo>=</mo><mo>{</mo><mtext>pt</mtext><mo>}</mo></mrow></math>. No continuous parameters, no discrete choices, no alternative models. The fibered product <math><msup><mi>&tau;</mi><mn>3</mn></msup></math> is *discovered*, not constructed.

The proof has a crucial dependency on the [split-complex shift]({{ '/framework/mathematics-split-complex-shift/' | relative_url }}). In the elliptic regime (<math><mrow><msup><mi>i</mi><mn>2</mn></msup><mo>=</mo><mo>&minus;</mo><mn>1</mn></mrow></math>), the maximum principle forces every bounded entire function to be constant (Liouville's theorem). This means a classical-complex version of the Central Theorem would have trivial function spaces -- the isomorphism would be vacuous.

The split-complex regime avoids this. The **Liouville Escape** (II.T41) proves that wave-type differential operators (from <math><mrow><msup><mi>j</mi><mn>2</mn></msup><mo>=</mo><mo>+</mo><mn>1</mn></mrow></math>) do *not* satisfy the maximum principle. Non-constant bounded holomorphic functions exist. The function space <math><mrow><mi>O</mi><mo>(</mo><msup><mi>&tau;</mi><mn>3</mn></msup><mo>)</mo></mrow></math> is rich enough to carry the full spectral algebra.

The complete dependency chain (II.D62, verified in [Book II]({{ '/publications/books/book-ii/' | relative_url }}), Part X) traces every step from K0 through the Central Theorem and confirms that no external imports appear. The chain is a directed acyclic graph whose unique sources are the seven axioms and whose unique sink is the Central Theorem. This chapter-length audit is both a reference map and a proof of intellectual honesty.

## Why This Matters

Categoricity means the framework has zero free parameters at the mathematical level. There is nothing to tune, nothing to adjust, nothing to choose. When the [physics modules]({{ '/framework/physics-neutron-primacy/' | relative_url }}) derive physical constants, they do so from this unique structure -- and any deviation from observation falsifies the entire chain. This is the strongest possible [falsifiability posture]({{ '/verify/' | relative_url }}).

## Key Claims

1. **II.T42** -- Categoricity: K0-K6 force a unique model *(established, machine-checked in [TauLib]({{ '/verify/taulib/' | relative_url }}))*
2. **II.T41** -- Liouville Escape: non-constant bounded holomorphic functions exist in the split-complex regime *(established, machine-checked)*
3. **II.D62** -- Complete Dependency Chain: DAG from axioms to Central Theorem with no external imports *(established)*
4. Moduli space = {pt} -- zero free parameters at the mathematical level *(tau-effective)*
