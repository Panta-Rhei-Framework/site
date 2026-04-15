---
title: Gravity Earned
module_id: E1-011
layer: E1
strand: macrocosm
summary_short: The τ-Einstein equation — gravity as an algebraic identity, not a nonlinear
  PDE.
diagrams:
- src: /assets/diagrams/framework/book-v/physics-gravity-earned-tau-einstein.svg
  caption: "The τ-Einstein equation as boundary identity: the lemniscate boundary condition, together with the kernel axioms, earns the metric g^(τ)_μν and forces the Einstein field equations G_μν = 8πG T_μν as a categorical consequence."
  alt: "The τ-Einstein equation as boundary identity: the lemniscate boundary condition, together with the kernel axioms, earns the metric g^(τ)_μν and forces the…"
  source: "Book V, Chapter 13"
  label: "fig:bookV-ch13-tau-einstein"
thesis: R^H = κ_τ · T^mat in the boundary holonomy algebra; chart shadow recovers
  Einstein's field equations.
canonical_books:
- V
source_parts:
- V.2
key_registry:
- V.D06
- V.T10
depends_on:
- E1-010
unlocks:
- E1-012
- E1-014
right_rail:
  related:
  - title: The Hermetic Principle
    url: /framework/physics-hermetic-principle/
  - title: Gravitational Closing Identity
    url: /framework/physics-gravitational-closing/
  - title: No Dark Matter
    url: /framework/physics-no-dark-matter/
  meta:
    type: Framework Module
    layer: E1 Physics
    strand: Macrocosm
    status: Canonical
    updated: April 2026
---

## Overview

Gravity is not a force that happens to exist -- it is the D-sector holonomy of the boundary algebra <math><mrow><msub><mi>H</mi><mo>&part;</mo></msub><mo>[</mo><mi>&omega;</mi><mo>]</mo></mrow></math>, canonically determined by generator <math><mi>&alpha;</mi></math> through the [sector template]({{ '/framework/mathematics-sector-template/' | relative_url }}). The **<math><mi>&tau;</mi></math>-Einstein equation** is not a nonlinear PDE on a background manifold -- it is a **boundary-character identity** in the holonomy algebra. Einstein's field equations are recovered as the "chart shadow" when this identity is projected onto coordinate charts.

## The Core Idea

The <math><mi>&tau;</mi></math>-Einstein equation (V.T10) reads:

<math display="block"><mrow><msup><mi>R</mi><mi>H</mi></msup><mo>=</mo><msub><mi>&kappa;</mi><mi>&tau;</mi></msub><mo>&sdot;</mo><msup><mi>T</mi><mtext>mat</mtext></msup></mrow></math>

where <math><msup><mi>R</mi><mi>H</mi></msup></math> is the holonomy curvature, <math><msup><mi>T</mi><mtext>mat</mtext></msup></math> is the matter tensor (both omega-germs in the same algebra), and <math><msub><mi>&kappa;</mi><mi>&tau;</mi></msub></math> is the gravitational coupling derived from the master constant. The gravitational constant <math><mi>G</mi></math> is not a fitted parameter -- it is a coherence conversion invariant: <math><mrow><mi>G</mi><mo>=</mo><mo>(</mo><msup><mi>c</mi><mn>3</mn></msup><mo>/</mo><mi>&hbar;</mi><mo>)</mo><mo>&sdot;</mo><msubsup><mi>&iota;</mi><mi>&tau;</mi><mn>2</mn></msubsup></mrow></math> (V.D06).

When projected onto coordinate charts, the <math><mi>&tau;</mi></math>-Einstein equation recovers the classical <math><mrow><msub><mi>G</mi><mrow><mi>&mu;</mi><mi>&nu;</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>8</mn><mi>&pi;</mi><mi>G</mi></mrow><msup><mi>c</mi><mn>4</mn></msup></mfrac><mo>&sdot;</mo><msub><mi>T</mi><mrow><mi>&mu;</mi><mi>&nu;</mi></mrow></msub></mrow></math> as its chart shadow. But the algebraic form is primary -- it is an *identity* in the holonomy algebra, not an equation to be solved on a manifold. Lorentz covariance is derived as a theorem about readouts (V.D06, Chapter 12), not assumed as an axiom about spacetime.

The weak-field regime derives Mercury's perihelion precession, gravitational light deflection, and the Shapiro time delay -- all from the same equation with no adjustable parameters. The strong-field regime produces the [gravitational closing identity]({{ '/framework/physics-gravitational-closing/' | relative_url }}) and the TOV equation for stellar structure.

## Why This Matters

Gravity is the bridge from the [microcosm]({{ '/framework/physics-self-description/' | relative_url }}) (fiber <math><msup><mi>T</mi><mn>2</mn></msup></math>) to the macrocosm (base <math><msup><mi>&tau;</mi><mn>1</mn></msup></math>). Without it, the framework would describe particles but not their large-scale behavior. The algebraic form of the <math><mi>&tau;</mi></math>-Einstein equation means gravity is not added to the framework -- it is *already there* as the D-sector of the [4+1 template]({{ '/framework/mathematics-sector-template/' | relative_url }}).

## Key Claims

1. **V.T10** -- <math><mi>&tau;</mi></math>-Einstein equation as boundary-character identity *(established, machine-checked in [TauLib]({{ '/verify/taulib/' | relative_url }}))*
2. **V.D06** -- Gravitational constant <math><mrow><mi>G</mi><mo>=</mo><mo>(</mo><msup><mi>c</mi><mn>3</mn></msup><mo>/</mo><mi>&hbar;</mi><mo>)</mo><mo>&sdot;</mo><msubsup><mi>&iota;</mi><mi>&tau;</mi><mn>2</mn></msubsup></mrow></math> *(tau-effective)*
3. Lorentz covariance derived as theorem, not axiom *(established, machine-checked)*
4. Einstein's <math><mrow><msub><mi>G</mi><mrow><mi>&mu;</mi><mi>&nu;</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>8</mn><mi>&pi;</mi><mi>G</mi></mrow><msup><mi>c</mi><mn>4</mn></msup></mfrac><msub><mi>T</mi><mrow><mi>&mu;</mi><mi>&nu;</mi></mrow></msub></mrow></math> is the chart shadow of the algebraic identity *(tau-effective)*
