---
layout: program-doc
title: "Physics — Guided Tour"
permalink: /results/physics/guided-tour/
lane: results
v2_lane: results
type: "Guided Tour"
status: "Canonical"
domain: physics
hero_eyebrow: "Results · Physics · Guided Tour"
summary_short: "A 7-stop walk through the τ-framework's physics surface, in plain language. Start to finish in 10 minutes; click the 'next stop' link at the bottom of each stop to continue."
---

This is a **guided tour** through the τ-framework's physics domain. We'll walk from the foundational kernel out to specific numerical predictions, with each stop in plain language. Bring no physics background — every term that needs unpacking links to its glossary entry.

> **Reading time:** 10 minutes  ·  **Stops:** 7  ·  **Best read:** in order, top to bottom

## Stop 1 of 7 · Why physics has just two free numbers

The first thing to know about the τ-framework: it claims that **all of physics** — the electron mass, gravity, the speed of light, every constant — is determined by **two numbers**.

- **`ι_τ ≈ 0.341304`** — a pure mathematical number, equal to `2/(π+e)`. No measurement involved. ([PG-C02]({{ '/results/physics/glossary/PG-C02-iota-tau/' | relative_url }}))
- **`m_n = 1.6749275 × 10⁻²⁷ kg`** — the neutron's mass. The only empirical input. ([PG-P01]({{ '/results/physics/glossary/PG-P01-neutron/' | relative_url }}))

That's it. No 25 free parameters of the Standard Model. No fine-tuning.

→ **Next stop:** [Why neutron and not electron?](#stop-2)

## <span id="stop-2"></span>Stop 2 of 7 · Why neutron and not electron?

Most physicists pick the electron mass `m_e` as their "standard" because it's so well-measured. The τ-framework picks the neutron — and there's a structural reason.

The neutron is the **lightest stable T²-defect bundle** in the framework's topology. Every other particle (proton, electron, photon) can be derived *from* the neutron via a known structural operation (the β-decay differentiation tree). So the neutron is the structural parent.

If you tried to anchor at the electron, you'd lose information — the electron is downstream of the neutron in the τ structure.

→ **Next stop:** [The 5-layer cascade](#stop-3)

## <span id="stop-3"></span>Stop 3 of 7 · The 5-layer cascade

Once you have `ι_τ` and `m_n`, every dimensional constant in physics is built in 5 layers:

```
Layer 0:  τ-categorical kernel (I.K0)
Layer 1:  Master constant ι_τ ≈ 0.341304 (a pure number)
Layer 2:  τ³ topology + (M, L, ℏ) dimensional triple
Layer 3:  Derived dimensional constants (α, a₀, R_∞, c, ℏ, G, k_B)
Layer 4:  SI bridge — anchored at m_n
```

It's a deterministic pipeline: feed in `ι_τ` and `m_n`, every observable comes out the other end. ([Full diagram on the Calibration Cascade page]({{ '/results/physics/cascade/' | relative_url }}))

→ **Next stop:** [How precise is the framework?](#stop-4)

## <span id="stop-4"></span>Stop 4 of 7 · How precise is the framework?

The framework's flagship predictions hit **sub-ppm precision** against experiment:

- **Electron mass** `m_e`: agreement at **0.025 ppm** (one part per 40 million). Tier A.
- **Higgs boson mass** `m_H`: agreement at **+8.0 ppm**. Tier A.
- **Weak mixing angle** `sin²θ_W`: agreement at **−0.65 ppm**. Tier A.
- **Hubble constant** `H_0`: resolves the standing observational tension. Tier B.

Tier A means "best-in-class precision matching experiment". The full ledger has {% include release-metric.html id="predictions.records" %} numerical predictions across the precision tiers. ([Predictions page]({{ '/results/predictions/' | relative_url }}))

→ **Next stop:** [What if it's wrong? — Falsifications](#stop-5)

## <span id="stop-5"></span>Stop 5 of 7 · What if it's wrong? — Falsifications

A theory that "fits everything" is suspicious. The τ-framework has 30 specific **falsification points** (N1–N30) where named experiments adjudicate it on a 2025–2035 timeline.

If any of these comes back wrong, the framework is contradicted. Examples:
- **N1**: No fourth-generation matter (LHC searches)
- **N2**: No supersymmetric partners
- **N6**: Sum of neutrino masses < 0.089 eV (KATRIN, cosmology)
- **N15**: Helium-4 mass fraction Y_p ≈ 0.2481 (BBN observations)
- **N23**: No dark matter particle ever detected

These are sharp, dated, and experimentally accessible. ([Falsifications page]({{ '/results/falsifications/' | relative_url }}))

→ **Next stop:** [The connection to life](#stop-6)

## <span id="stop-6"></span>Stop 6 of 7 · The connection to life

Physics doesn't stay in the physics domain. The neutron-mass anchor [PG-P01]({{ '/results/physics/glossary/PG-P01-neutron/' | relative_url }}) propagates into biology via the K_χ channel ([LG-Y02]({{ '/results/life/glossary/LG-Y02-kinetic-pseudoscalar-channel/' | relative_url }})), which amplifies a weak-sector chirality seed (~10⁻¹⁷) into the biological homochirality (ee ≈ 1.0) we observe in every known living system.

This is one of 10 cross-domain edges currently mapped in the glossary. See [Cross-Domain Edges]({{ '/results/cross-domain/' | relative_url }}) for the full list.

→ **Next stop:** [Where to go next](#stop-7)

## <span id="stop-7"></span>Stop 7 of 7 · Where to go next

You've now seen the structure of the physics domain. To go deeper:

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/results/physics/glossary/' | relative_url }}">
    <strong>Browse the 95-entry physics glossary</strong>
    <span>Every constant, particle, law, and quantity with its full SI translation.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/predictions/' | relative_url }}">
    <strong>{% include release-metric.html id="predictions.records" %} numerical predictions</strong>
    <span>The Tier A / B / C precision ledger.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/physics/cascade/' | relative_url }}">
    <strong>The full calibration cascade</strong>
    <span>Layer 0 to Layer 4, with all registry anchors.</span>
  </a>
  <a class="v2-tile" href="{{ '/results/life/guided-tour/' | relative_url }}">
    <strong>Continue to the life tour</strong>
    <span>How K_χ amplifies physics into biology.</span>
  </a>
</div>

## You finished the tour

If you read all 7 stops, you have a working understanding of why the τ-framework's physics claims are sharp, structural, and falsifiable. The 78 individual physics result pages are now intelligible context-by-context.

The other three guided tours:
- [Mathematics — Guided Tour]({{ '/results/mathematics/guided-tour/' | relative_url }})
- [Life — Guided Tour]({{ '/results/life/guided-tour/' | relative_url }})
- [Metaphysics — Guided Tour]({{ '/results/metaphysics/guided-tour/' | relative_url }})

— or jump back to [the Physics Hub]({{ '/results/physics/' | relative_url }}).
