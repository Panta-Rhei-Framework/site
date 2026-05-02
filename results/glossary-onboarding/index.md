---
layout: program-doc
title: "Glossary Onboarding"
permalink: /results/glossary-onboarding/
lane: results
v2_lane: results
type: "Onboarding Primer"
status: "Canonical"
hero_eyebrow: "Results · Glossary Primer"
summary_short: "A 5-minute primer on the τ-framework's vocabulary. Learn the words you'll see across the 241 glossary entries before you dive in."
---

The τ-framework introduces some vocabulary that may be unfamiliar even to mathematicians, physicists, biologists, or philosophers. This primer covers the core terms you'll encounter across the [physics]({{ '/results/physics/glossary/' | relative_url }}) (95), [life]({{ '/results/life/glossary/' | relative_url }}) (78), and [metaphysics]({{ '/results/metaphysics/glossary/' | relative_url }}) (68) glossary collections.

If you read these definitions you'll understand 90% of any glossary entry without further context. Each term links to its full glossary entry where applicable.

## The kernel-level terms

**τ (the kernel)**
The categorical universe of discourse. The framework's foundational object, defined by the Universe Postulate (`I.K0`). Everything else derives from τ.

**ι_τ (iota-tau, the master constant)**
A pure dimensionless number ι_τ ≈ 0.341304, equivalent to `2/(π+e)` algebraically. Every dimensional constant in physics emerges as an `ι_τ`-chain expression times a (M, L, ℏ)-dimensional factor. See [PG-C02-iota-tau]({{ '/results/physics/glossary/PG-C02-iota-tau/' | relative_url }}).

**τ-categorical**
Adjective. Means: derived from the τ-kernel's categorical structure, as opposed to derived from a specific model or experimental input. A τ-categorical claim is a structural fact about τ itself.

**Sector**
A τ-categorical sub-domain that emerges from the kernel as a coherent unit. Examples: the gravity sector (where Newton's G lives), the chirality sector (where homochirality emerges), the empirical sector S_E (where Reg_E reads).

## The reading-out terms

**Register (Reg_E, Reg_P, Reg_D, Reg_C)**
The four canonical "readout functors" — categorical functions from τ into observation/normative/proof/stance codomains. Each register reads a different aspect of τ-categorical reality:
- **Reg_E** → **Obs**: empirical observations ([MG-R01]({{ '/results/metaphysics/glossary/MG-R01-empirical-register/' | relative_url }}))
- **Reg_P** → **Norm**: ethical / normative content
- **Reg_D** → **Proof**: mathematical / logical content
- **Reg_C** → **Stance**: commitment / character / dignity

**Codomain**
The target category of a register functor. `Reg_E`'s codomain is `Obs`; `Reg_P`'s is `Norm`. Each glossary entry's "register codomain" field names where it lives.

## The physics-cascade terms

**SI translation**
The Section 3 of every physics glossary entry. The numerical SI value, uncertainty, and calibration anchor. Every physics SI value traces back through the cascade to one empirical input: m_n.

**Calibration anchor**
The single empirical input to a calibration cascade. In physics, [PG-P01-neutron]({{ '/results/physics/glossary/PG-P01-neutron/' | relative_url }}) (m_n = 1.6749275 × 10⁻²⁷ kg). In life, [LG-Y02-kinetic-pseudoscalar-channel]({{ '/results/life/glossary/LG-Y02-kinetic-pseudoscalar-channel/' | relative_url }}) (the K_χ channel). Metaphysics has **no anchor** — it's categorical-only.

**m_n (neutron mass)**
The single SI anchor of the entire physics cascade. Why neutron and not electron or proton? See [PG-P01-neutron]({{ '/results/physics/glossary/PG-P01-neutron/' | relative_url }}).

**(M, L, ℏ) triple**
The dimensional basis. Mass scale (anchored at m_n), length scale (Bohr-radius-related via ι_τ-chain), action quantum (via ι_τ-chain). Every physical constant is built from these three.

## The life-cascade terms

**K_χ (the Kinetic Pseudoscalar Channel)**
The single structural anchor of the life cascade ([LG-Y02]({{ '/results/life/glossary/LG-Y02-kinetic-pseudoscalar-channel/' | relative_url }}), registry `VI.L18`). A parity-odd, time-even operator that amplifies the weak-sector chirality seed (~10⁻¹⁷) into biological homochirality (ee ≈ 1.0).

**Empirical correlate**
The Section 3 of every life glossary entry. A biomarker, measurable range, observation method, and (for chirality-sensitive entries) anchor chain to LG-Y02 / VI.L18.

**Homochirality**
The dominance of one molecular handedness in living systems. L-amino acids in proteins; D-sugars in nucleic acids. ee ≈ 1.0 across all known terran biology.

## The metaphysics-architecture terms

**Phenomenological correlate**
The Section 3 of every metaphysics glossary entry. Lived-experience instantiation, narrative or ethical example, and the register codomain. **No calibration anchor** — metaphysics is categorical-only.

**OR1–OR6 (Six Ontic Requirements)**
The structural narrowing principles that any candidate ontic reality must satisfy: self-coherence (`OR1`, [MG-P01]({{ '/results/metaphysics/glossary/MG-P01-or1-self-coherence/' | relative_url }})), completeness (`OR2`), generativity (`OR3`), independence (`OR4`), continuity (`OR5`), stability (`OR6`).

**CI graph (Consequence-Intervention)**
The architectural structure connecting causal claims to their commitments across registers ([MG-A01]({{ '/results/metaphysics/glossary/MG-A01-ci-operator-graph/' | relative_url }})). Spans Reg_P / Reg_D / Reg_C.

## The 4-section glossary contract

Every glossary entry — across all three domains — carries the same 4-section structure:

1. **τ-Definition** — what the term *is* in the framework, with primary registry anchor.
2. **τ-Derivation** — chain of registry steps that derive the term from `I.K0`.
3. **Domain-specific Section 3** — `si_translation` / `empirical_correlate` / `phenomenological_correlate`.
4. **Lean coverage** — formal-verification status (`formalized` / `partial` / `planned` / etc.).

Plus: related glossary entries (cross-references) + referenced_by (reverse edges) + tags + version.

## Cross-domain edges

When a glossary entry's `related_glossary_entries` references a term in a different domain, that's a **cross-domain bridge**. See [Cross-Domain Edges]({{ '/results/cross-domain/' | relative_url }}) for the full list.

## How registry IDs work

Every τ-categorical commitment has a registry ID like `I.K0` (Book I, axiom K0) or `IV.D11` (Book IV, definition 11). Glossary entries' `primary_registry_id` field anchors them to a specific registry item. The full registry has {% include release-metric.html id="registry.registry_total.grand_total" %} objects across 7 books.

## Read next

- [Physics Glossary]({{ '/results/physics/glossary/' | relative_url }}) — start with [PG-P01-neutron]({{ '/results/physics/glossary/PG-P01-neutron/' | relative_url }}) (the SI anchor) or [PG-C02-iota-tau]({{ '/results/physics/glossary/PG-C02-iota-tau/' | relative_url }}) (the master constant)
- [Life Glossary]({{ '/results/life/glossary/' | relative_url }}) — start with [LG-Y02-kinetic-pseudoscalar-channel]({{ '/results/life/glossary/LG-Y02-kinetic-pseudoscalar-channel/' | relative_url }}) (the K_χ anchor)
- [Metaphysics Glossary]({{ '/results/metaphysics/glossary/' | relative_url }}) — start with [MG-R01-empirical-register]({{ '/results/metaphysics/glossary/MG-R01-empirical-register/' | relative_url }}) (Reg_E)
- [Cross-Domain Edges]({{ '/results/cross-domain/' | relative_url }}) — the structural bridges
- [How to read a result page]({{ '/results/how-to-read-a-result-page/' | relative_url }})
