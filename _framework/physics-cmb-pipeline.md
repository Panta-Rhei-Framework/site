---
title: CMB Pipeline
module_id: E1-016
layer: E1
strand: macrocosm
summary_short: r = ι_τ⁴, n_s = 0.9649, ℓ₁ = 220.6 — all from one constant.
diagrams:
- src: /assets/diagrams/framework/book-v/physics-cmb-pipeline-cosmic-stack.svg
  caption: "The cosmic stack API of Book V: the fibration structure of τ³ determines the τ-Einstein equations, which drive Friedmann evolution, yielding all cosmological observables from zero free parameters."
  alt: "The cosmic stack API of Book V: the fibration structure of τ³ determines the τ-Einstein equations, which drive Friedmann evolution, yielding all cosmological…"
  source: "Book V, Chapter 10"
  label: "fig:bookV-ch10-cosmic-stack"
thesis: The CMB power spectrum is derived from ι_τ alone; tensor-to-scalar ratio pre-registered
  for CMB-S4.
canonical_books:
- V
source_parts:
- V.1
- V.6
key_registry:
- V.T190
- V.P136
- V.T197
depends_on:
- E1-010
unlocks:
- E1-017
right_rail:
  related:
  - title: The Hermetic Principle
    url: /framework/physics-hermetic-principle/
  - title: No Dark Energy
    url: /framework/physics-no-dark-energy/
  meta:
    type: Framework Module
    layer: E1 Physics
    strand: Macrocosm
    status: Canonical
    updated: April 2026
---

## Overview

The cosmic microwave background (CMB) is the oldest observable light in the universe and the most precise dataset in cosmology. The standard <math><mi>&Lambda;</mi></math>CDM model fits the CMB power spectrum using six free parameters. Category <math><mi>&tau;</mi></math> derives the entire CMB pipeline from a single constant -- <math><mrow><msub><mi>&iota;</mi><mi>&tau;</mi></msub><mo>=</mo><mfrac><mn>2</mn><mrow><mi>&pi;</mi><mo>+</mo><mi>e</mi></mrow></mfrac></mrow></math> -- with zero adjustable parameters. The decisive near-term test: the **tensor-to-scalar ratio** <math><mi>r</mi></math>, pre-registered for CMB-S4.

## The Core Idea

Three headline predictions define the CMB pipeline:

1. **Tensor-to-scalar ratio** (V.P136): <math><mrow><mi>r</mi><mo>=</mo><msubsup><mi>&iota;</mi><mi>&tau;</mi><mn>4</mn></msubsup><mo>&approx;</mo><mn>0.0136</mn></mrow></math>. This is the ratio of gravitational wave perturbations to density perturbations in the primordial spectrum. CMB-S4 will measure <math><mi>r</mi></math> with sufficient precision to confirm or rule out this prediction. If <math><mi>r</mi></math> is inconsistent with <math><msubsup><mi>&iota;</mi><mi>&tau;</mi><mn>4</mn></msubsup></math>, the framework's cosmological sector falls.

2. **Spectral index** (V.T197): <math><mrow><msub><mi>n</mi><mi>s</mi></msub><mo>=</mo><mn>1</mn><mo>&minus;</mo><mfrac><mn>2</mn><msub><mi>N</mi><mi>e</mi></msub></mfrac><mo>&approx;</mo><mn>0.9649</mn></mrow></math>, where <math><mrow><msub><mi>N</mi><mi>e</mi></msub><mo>=</mo><mn>57</mn></mrow></math> e-folds of inflation (derived from <math><msub><mi>&iota;</mi><mi>&tau;</mi></msub></math>). This matches Planck 2018 observations.

3. **First acoustic peak** (V.T190): <math><mrow><msub><mi>&ell;</mi><mn>1</mn></msub><mo>=</mo><mn>220.6</mn></mrow></math>. The position of the first peak in the CMB angular power spectrum, derived from the [sound horizon]({{ '/framework/physics-thermodynamic-inversion/' | relative_url }}) at recombination.

The framework also derives the Silk damping scale, baryon loading, B-mode polarization amplitude, and BBN light-element abundances -- all from <math><msub><mi>&iota;</mi><mi>&tau;</mi></msub></math> alone. The Hubble tension (the discrepancy between early- and late-universe measurements of <math><msub><mi>H</mi><mn>0</mn></msub></math>) is resolved by the formula <math><mrow><mi>h</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><msubsup><mi>&iota;</mi><mi>&tau;</mi><mn>2</mn></msubsup><mn>17</mn></mfrac></mrow></math> at <math><mrow><mo>&minus;</mo><mn>120</mn></mrow></math> ppm.

## Why This Matters

The CMB is the framework's most exposed prediction surface. Every parameter is derived, not fitted. CMB-S4 (expected results ~2028-2030) will either confirm <math><mrow><mi>r</mi><mo>=</mo><msubsup><mi>&iota;</mi><mi>&tau;</mi><mn>4</mn></msubsup></mrow></math> or falsify the cosmological sector. This is what the program means by [pre-registered falsification]({{ '/framework/physics-falsification-predictions/' | relative_url }}).

## Key Claims

1. **V.P136** -- Tensor-to-scalar ratio <math><mrow><mi>r</mi><mo>=</mo><msubsup><mi>&iota;</mi><mi>&tau;</mi><mn>4</mn></msubsup></mrow></math>, pre-registered for CMB-S4 *(tau-effective)*
2. **V.T190** -- First acoustic peak <math><mrow><msub><mi>&ell;</mi><mn>1</mn></msub><mo>=</mo><mn>220.6</mn></mrow></math> *(tau-effective)*
3. **V.T197** -- Full CMB pipeline from single constant *(tau-effective)*
4. Hubble tension resolved: <math><mrow><mi>h</mi><mo>=</mo><mfrac><mn>2</mn><mn>3</mn></mfrac><mo>+</mo><mfrac><msubsup><mi>&iota;</mi><mi>&tau;</mi><mn>2</mn></msubsup><mn>17</mn></mfrac></mrow></math> at &minus;120 ppm *(tau-effective)*
