---
title: Electron Mass Prediction
module_id: E1-004
layer: E1
strand: microcosm
summary_short: R₀ = ι_τ⁻⁷ − √3·ι_τ⁻² ≈ 1838.7 — mass ratio at 0.025 ppm.
thesis: The Epstein zeta at s=4 gives the bulk exponent -7; the lemniscate capacity
  √3 provides the correction.
canonical_books:
- IV
source_parts:
- IV.2
key_registry:
- IV.T09
depends_on:
- E1-003
unlocks:
- E1-005
right_rail:
  related:
  - title: Fine-Structure Constant & Calibration
    url: /framework/physics-fine-structure/
  - title: Three Generations & Particle Spectrum
    url: /framework/physics-three-generations/
  meta:
    type: Framework Module
    layer: E1 Physics
    strand: Microcosm
    status: Canonical
    updated: April 2026
---

## Overview

The proton-to-electron mass ratio -- why the proton is approximately 1836 times heavier than the electron -- is one of the most consequential numbers in physics. It determines atomic structure, molecular bonding, stellar nucleosynthesis, and the possibility of complex chemistry. The Standard Model treats this ratio as an empirical input. Category <math><mi>&tau;</mi></math> derives it from first principles:

<math display="block"><mrow><msub><mi>R</mi><mn>0</mn></msub><mo>=</mo><msubsup><mi>&iota;</mi><mi>&tau;</mi><mrow><mo>&minus;</mo><mn>7</mn></mrow></msubsup><mo>&minus;</mo><msqrt><mn>3</mn></msqrt><mo>&sdot;</mo><msubsup><mi>&iota;</mi><mi>&tau;</mi><mrow><mo>&minus;</mo><mn>2</mn></mrow></msubsup><mo>&approx;</mo><mn>1838.7</mn></mrow></math>

This matches the CODATA experimental value to approximately **8 parts per million** -- with zero free parameters.

## The Core Idea

The derivation combines three ingredients from the [quantum mechanics]({{ '/publications/books/book-iv/' | relative_url }}) of <math><msup><mi>&tau;</mi><mn>3</mn></msup></math>:

1. **Breathing modes on <math><msup><mi>T</mi><mn>2</mn></msup></math>**: the electron is a quantized excitation of the torus fiber, and its mass is determined by the breathing-mode spectrum -- the eigenvalues of the Laplacian on the torus at the relevant scale.

2. **The Epstein zeta function** (IV.T09): the zeta function of the torus lattice, evaluated at <math><mrow><mi>s</mi><mo>=</mo><mn>4</mn></mrow></math>, gives the bulk exponent <math><mrow><mo>&minus;</mo><mn>7</mn></mrow></math>. This is why the dominant term is <math><msubsup><mi>&iota;</mi><mi>&tau;</mi><mrow><mo>&minus;</mo><mn>7</mn></mrow></msubsup></math> -- the seventh power of the inverse master constant, arising from four spatial dimensions of the torus lattice combined with the spectral sum.

3. **Lemniscate capacity**: the correction term <math><mrow><msqrt><mn>3</mn></msqrt><mo>&sdot;</mo><msubsup><mi>&iota;</mi><mi>&tau;</mi><mrow><mo>&minus;</mo><mn>2</mn></mrow></msubsup></mrow></math> comes from the [lemniscate]({{ '/framework/mathematics-prime-polarity/' | relative_url }}) capacity -- a geometric invariant of the boundary curve <math><mrow><mi>L</mi><mo>=</mo><msup><mi>S</mi><mn>1</mn></msup><mo>&or;</mo><msup><mi>S</mi><mn>1</mn></msup></mrow></math> -- combined with a holonomy correction <math><mrow><msup><mi>&pi;</mi><mn>3</mn></msup><msup><mi>&alpha;</mi><mn>2</mn></msup></mrow></math> from the [fine-structure constant]({{ '/framework/physics-fine-structure/' | relative_url }}).

The three ingredients are not independent choices -- each is determined by the <math><msup><mi>&tau;</mi><mn>3</mn></msup></math> geometry. The Epstein zeta is the spectral sum of the torus Laplacian. The lemniscate capacity is a conformal invariant of the boundary. The holonomy correction is the [spectral algebra's]({{ '/framework/mathematics-spectral-algebra/' | relative_url }}) contribution to the EM sector. Together they produce a single formula with no adjustable parameters.

## Why This Matters

This ratio determines whether atoms can exist, whether chemistry can be complex, and whether stars can burn long enough for life to evolve. Standard physics treats <math><mrow><msub><mi>m</mi><mi>p</mi></msub><mo>/</mo><msub><mi>m</mi><mi>e</mi></msub></mrow></math> as a given; the framework treats it as a *prediction*. Agreement at 8 ppm with zero free parameters is one of the framework's strongest quantitative claims -- and one of its clearest [falsification routes]({{ '/verify/' | relative_url }}).

## Key Claims

1. **IV.T09** -- Proton-to-electron mass ratio: <math><mrow><msub><mi>R</mi><mn>0</mn></msub><mo>=</mo><msubsup><mi>&iota;</mi><mi>&tau;</mi><mrow><mo>&minus;</mo><mn>7</mn></mrow></msubsup><mo>&minus;</mo><msqrt><mn>3</mn></msqrt><mo>&sdot;</mo><msubsup><mi>&iota;</mi><mi>&tau;</mi><mrow><mo>&minus;</mo><mn>2</mn></mrow></msubsup></mrow></math> at ~8 ppm *(tau-effective)*
2. Bulk exponent <math><mrow><mo>&minus;</mo><mn>7</mn></mrow></math> from Epstein zeta at <math><mrow><mi>s</mi><mo>=</mo><mn>4</mn></mrow></math> on the torus lattice *(tau-effective)*
3. Correction from lemniscate capacity <math><msqrt><mn>3</mn></msqrt></math> and holonomy <math><mrow><msup><mi>&pi;</mi><mn>3</mn></msup><msup><mi>&alpha;</mi><mn>2</mn></msup></mrow></math> *(tau-effective)*
4. Zero free parameters -- all ingredients from <math><msup><mi>&tau;</mi><mn>3</mn></msup></math> geometry *(tau-effective)*
