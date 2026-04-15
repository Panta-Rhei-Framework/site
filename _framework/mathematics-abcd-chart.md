---
title: The ABCD Coordinate Chart
module_id: E0-004
layer: E0
strand: coordinates
summary_short: Every object receives a canonical 4-dimensional address via the greedy
  peel algorithm.
diagrams:
- src: /assets/diagrams/framework/book-i/mathematics-abcd-chart-coprojections.svg
  caption: "The fibration coprojections from τ³ to its base τ¹ and fiber T². The two readout projections π_base and π_fiber realize the 2+2 split of the ABCD coordinate chart; their domains become the macrocosm and microcosm in Books IV–V."
  alt: "The fibration coprojections from τ³ to its base τ¹ and fiber T². The two readout projections π_base and π_fiber realize the 2+2 split of the ABCD coordinate…"
  source: "Book I, Chapter 20"
  label: "fig:bookI-ch20-coprojections"
thesis: The ABCD chart maps every tau-object to a unique quadruple (A, B, C, D) using
  tower atoms and greedy peel-off, forcing dim_tau = 4.
canonical_books:
- I
source_parts:
- I.4
key_registry:
- I.D16
- I.D17
- I.T09
depends_on:
- E0-003
unlocks:
- E0-005
right_rail:
  related:
  - title: Earning Arithmetic
    url: /framework/mathematics-earning-arithmetic/
  - title: Hyperfactorization Theorem
    url: /framework/mathematics-hyperfactorization/
  meta:
    type: Framework Module
    layer: E0 Mathematics
    strand: Coordinates
    status: Canonical
    updated: April 2026
---

## Overview

With [arithmetic earned]({{ '/framework/mathematics-earning-arithmetic/' | relative_url }}) from the kernel, the framework now asks: can every object be *addressed*? The ABCD Coordinate Chart provides a canonical map from objects to four-dimensional coordinates, using a greedy decomposition algorithm that peels off tower atoms in order of structural priority. The result is a forced dimensionality: every object in Category <math><mi>&tau;</mi></math> receives a unique quadruple <math><mrow><mo>(</mo><mi>A</mi><mo>,</mo><mi>B</mi><mo>,</mo><mi>C</mi><mo>,</mo><mi>D</mi><mo>)</mo></mrow></math>, and the dimension of the universe is exactly four. This is not postulated -- it is a theorem.

## The Core Idea

The ABCD chart begins with **internal primes**. Divisibility on <math><mrow><mi>&tau;</mi><mtext>-Idx</mtext></mrow></math> is defined from [earned multiplication]({{ '/framework/mathematics-earning-arithmetic/' | relative_url }}): <math><mrow><mi>a</mi><mo>|</mo><mi>b</mi></mrow></math> if and only if there exists <math><mi>k</mi></math> such that <math><mrow><mi>b</mi><mo>=</mo><mi>a</mi><mo>&times;</mo><mi>k</mi></mrow></math>. Internal primes are the irreducible elements under this relation, and the **Fundamental Theorem of Arithmetic** (I.T09) proves that every element of <math><mrow><mi>&tau;</mi><mtext>-Idx</mtext></mrow></math> has a unique prime factorization -- earned, not assumed from classical number theory.

From prime factorization, **tower atoms** are extracted by a greedy algorithm. Every integer <math><mrow><mi>X</mi><mo>&ge;</mo><mn>2</mn></mrow></math> decomposes into a canonical normal form:

<math display="block"><mrow><mi>X</mi><mo>=</mo><msup><mrow><mo>(</mo><msup><mi>A</mi><mi>C</mi></msup><mo>)</mo></mrow><mi>B</mi></msup><mo>&sdot;</mo><mi>D</mi></mrow></math>

where the four coordinates map to the four orbit channels:

- **A** (the <math><mi>&pi;</mi></math>-channel): the largest prime factor -- multiplicative spine
- **B** (the <math><mi>&gamma;</mi></math>-channel): the maximal exponent -- outer power
- **C** (the <math><mi>&eta;</mi></math>-channel): the maximal tetration height -- inner power
- **D** (the <math><mi>&alpha;</mi></math>-channel): the remainder after tower extraction -- counting scaffold

The ABCD Coordinate Chart (I.D17) is then the map <math><mrow><mi>&Phi;</mi><mo>:</mo><mtext>Obj</mtext><mo>(</mo><mi>&tau;</mi><mo>)</mo><mo>&rarr;</mo><msup><mrow><mi>&tau;</mi><mtext>-Idx</mtext></mrow><mn>4</mn></msup></mrow></math>, sending each object to its four-coordinate address. The map is total: every object has an address.

The four coordinates are not arbitrary labels -- they correspond one-to-one with the four orbit channels established by the [Coherence Kernel]({{ '/framework/mathematics-coherence-kernel/' | relative_url }}). This is why <math><mrow><msub><mtext>dim</mtext><mi>&tau;</mi></msub><mo>=</mo><mn>4</mn></mrow></math>: four orbit channels produce four independent coordinate axes. A fifth coordinate would require a fifth orbit channel, which the diagonal discipline forbids.

## Why This Matters

The ABCD chart transforms Category <math><mi>&tau;</mi></math> from an abstract orbit structure into a *coordinatized* universe where every object has a unique position. This is the foundation for all subsequent geometric and analytic constructions. The [fibered product]({{ '/framework/mathematics-split-complex-shift/' | relative_url }}) <math><mrow><msup><mi>&tau;</mi><mn>3</mn></msup><mo>=</mo><msup><mi>&tau;</mi><mn>1</mn></msup><msub><mo>&times;</mo><mi>f</mi></msub><msup><mi>T</mi><mn>2</mn></msup></mrow></math> that carries the framework's holomorphic geometry is built from these four coordinates.

The forced dimensionality <math><mrow><msub><mtext>dim</mtext><mi>&tau;</mi></msub><mo>=</mo><mn>4</mn></mrow></math> is structurally significant: it matches the dimension of spacetime, and this matching is not an input but a consequence. Whether this structural coincidence carries physical meaning is tested in the [physics modules]({{ '/framework/physics-neutron-primacy/' | relative_url }}).

The [Hyperfactorization Theorem]({{ '/framework/mathematics-hyperfactorization/' | relative_url }}) (next module) will prove that this chart is not merely total but *injective* -- distinct objects always receive distinct addresses.

## Key Claims

1. **I.T09** -- Fundamental Theorem of Arithmetic on <math><mrow><mi>&tau;</mi><mtext>-Idx</mtext></mrow></math>: unique prime factorization *(established, machine-checked in [TauLib]({{ '/verify/taulib/' | relative_url }}))*
2. **I.D17** -- ABCD Coordinate Chart: canonical four-coordinate address for every object *(established, machine-checked)*
3. **I.D16** -- Tower atoms and greedy peel algorithm *(established, machine-checked)*
4. <math><mrow><msub><mtext>dim</mtext><mi>&tau;</mi></msub><mo>=</mo><mn>4</mn></mrow></math> is forced by four orbit channels -- not postulated *(tau-effective)*
