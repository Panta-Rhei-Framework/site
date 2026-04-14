---
title: Beta-Decay Rosetta Stone
module_id: E1-002
layer: E1
strand: microcosm
summary_short: All five sectors visible in one process — the single event that decodes
  the Standard Model.
thesis: n → p + e⁻ + ν̄ₑ is a torus reconfiguration displaying all five sectors simultaneously.
canonical_books:
- IV
source_parts:
- IV.1
key_registry:
- IV.T03
- IV.T04
depends_on:
- E1-001
unlocks:
- E1-003
- E1-004
right_rail:
  related:
  - title: Neutron Primacy
    url: /framework/physics-neutron-primacy/
  - title: Fine-Structure Constant & Calibration
    url: /framework/physics-fine-structure/
  - title: Electron Mass Prediction
    url: /framework/physics-electron-mass/
  meta:
    type: Framework Module
    layer: E1 Physics
    strand: Microcosm
    status: Canonical
    updated: April 2026
---

## Overview

Beta decay is the Rosetta Stone of the framework's physics. The transition <math><mrow><mi>n</mi><mo>&rarr;</mo><mi>p</mi><mo>+</mo><msup><mi>e</mi><mo>&minus;</mo></msup><mo>+</mo><msub><mover><mi>&nu;</mi><mo>&macr;</mo></mover><mi>e</mi></msub></mrow></math> is not merely a nuclear reaction -- it is a **torus reconfiguration** that displays all five sectors of the [4+1 template]({{ '/framework/mathematics-sector-template/' | relative_url }}) simultaneously. In a single process, the [neutron]({{ '/framework/physics-neutron-primacy/' | relative_url }}) transforms into a proton, an electron, and an antineutrino, revealing the electromagnetic, weak, strong, gravitational, and Higgs/mass sectors in concert. This one reaction is the decoder ring for the entire particle physics program.

## The Core Idea

The [neutron]({{ '/framework/physics-neutron-primacy/' | relative_url }}) is not the lowest-energy state in Category <math><mi>&tau;</mi></math>: <math><mrow><msub><mi>m</mi><mi>n</mi></msub><mo>&gt;</mo><msub><mi>m</mi><mi>p</mi></msub><mo>+</mo><msub><mi>m</mi><mi>e</mi></msub></mrow></math> by approximately 1.29 MeV. This energy difference triggers the reconfiguration. Beta decay (IV.T03) is defined as the fundamental <math><msup><mi>&tau;</mi><mn>3</mn></msup></math> mode transition:

<math display="block"><mrow><mi>n</mi><mo>&rarr;</mo><mi>p</mi><mo>+</mo><msup><mi>e</mi><mo>&minus;</mo></msup><mo>+</mo><msub><mover><mi>&nu;</mi><mo>&macr;</mo></mover><mi>e</mi></msub></mrow></math>

Each product maps to a specific sector: the proton carries the strong (<math><mi>&eta;</mi></math>) and electromagnetic (<math><mi>&gamma;</mi></math>) sectors, the electron carries the electromagnetic sector with the weak (<math><mi>&pi;</mi></math>) sector as catalyst, the antineutrino carries the weak sector alone, and the mass difference is accounted by the <math><mi>&omega;</mi></math>-coupling (Higgs mechanism). Gravity (<math><mi>&alpha;</mi></math>-sector) governs the base-direction propagation of all products.

The Rosetta Stone property (IV.T04) states that every Standard Model interaction can be decomposed into sector-labeled <math><msup><mi>T</mi><mn>2</mn></msup></math> mode transitions that are specializations of the beta-decay template. The particle zoo of the Standard Model is not a catalog to be memorized -- it is a set of variations on this single theme.

The framework treats particles as *dynamic patterns* on the torus, not static objects. In Heraclitean terms: what persists is not the particle but the transformation. The neutron is a pattern; beta decay is what the pattern does; the proton, electron, and neutrino are what the pattern becomes.

## Why This Matters

Beta decay is the entry point for the entire [force architecture]({{ '/framework/physics-electroweak-synthesis/' | relative_url }}). From this single process, the framework reads off the sector assignments (which force governs which particle), the coupling hierarchy (why electromagnetism is stronger than the weak force), and the mass relations (why <math><mrow><msub><mi>m</mi><mi>n</mi></msub><mo>&gt;</mo><msub><mi>m</mi><mi>p</mi></msub></mrow></math>). The [fine-structure constant]({{ '/framework/physics-fine-structure/' | relative_url }}) derivation (next module) uses the sector fractions established here.

## Key Claims

1. **IV.T03** -- Beta decay as the fundamental <math><msup><mi>&tau;</mi><mn>3</mn></msup></math> mode transition *(established, machine-checked in [TauLib]({{ '/verify/taulib/' | relative_url }}))*
2. **IV.T04** -- Rosetta Stone property: all Standard Model interactions are sector specializations of beta decay *(tau-effective)*
3. All five sectors of the 4+1 template are displayed simultaneously *(established, machine-checked)*
4. Particles are dynamic torus patterns, not static objects *(tau-effective)*
