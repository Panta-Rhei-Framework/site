# Framework Lane Diagram Sprint — Phase 2 Review

**Status**: awaiting user approval before Phase 3 execution

## Executive Summary

All 60 framework modules audited against 98 TikZ diagrams in the 7-book LaTeX manuscripts. **59 diagrams selected** across **47 modules** (13 modules intentionally left without diagrams after editorial review).

| Book | Modules | Diagrams selected | With 2 | With 1 | With 0 |
|------|:-------:|:-----------------:|:------:|:------:|:------:|
| I | 11 | 6 | 1 | 4 | 6 |
| II | 6 | 6 | 1 | 4 | 1 |
| III | 6 | 7 | 1 | 5 | 0 |
| IV | 9 | 11 | 2 | 7 | 0 |
| V | 9 | 9 | 1 | 7 | 1 |
| VI | 8 | 10 | 3 | 4 | 1 |
| VII | 11 | 10 | 3 | 4 | 4 |
| **Total** | **60** | **59** | **12** | **35** | **13** |

Book I has `mathematics-coherence-kernel` already done in Phase 1 (the Five Generators Hasse diagram).

## Editorial principles applied

- **Thesis-aligned**: Every diagram directly illustrates the module's central thesis, not peripheral machinery
- **Canonical over comprehensive**: When a chapter has multiple figures, pick the one that IS the visual for the concept
- **Quality over coverage**: Modules without a genuinely illustrative diagram get `diagrams: []` — better empty than forced
- **Max 2 per module**: When a second diagram adds complementary visual insight, include it; otherwise stop at 1
- **Shared diagrams are fine**: A few diagrams serve multiple modules (e.g. the Master Schema in Book III, the Distinction matrix in Book VI) — each module gets the diagram that best serves its thesis

## Module-by-module review

### Book I — Categorical Foundations (11 modules → 6 diagrams)

| Module | Diagrams | Notes |
|--------|:--------:|-------|
| **mathematics-coherence-kernel** | 1 ✓ | **Already done in Phase 1** (Five generators Hasse) |
| mathematics-orbit-generation | 2 | Generative act + Ontic closure — complementary pair |
| mathematics-earning-arithmetic | 1 | Rank transfer bijections |
| mathematics-abcd-chart | 1 | Fibration coprojections (2+2 split) |
| mathematics-hyperfactorization | 0 | No TikZ diagram illustrates the No-Tie Lemma directly |
| mathematics-prime-polarity | 0 | Lemniscate illustrated in omega-germs module instead |
| mathematics-omega-germs | 1 | Algebraic lemniscate with B/C polarization |
| mathematics-internal-sets | 0 | Purely algebraic, no canonical visual |
| mathematics-split-complex-holomorphy | 0 | No dedicated visual in parts 12-13 |
| mathematics-earned-topos | 0 | Part 14-15 has only generic pullback diagrams |
| mathematics-global-hartogs | 0 | Part 16 has no TikZ figures |

### Book II — Categorical Holomorphy (6 modules → 6 diagrams)

| Module | Diagrams | Notes |
|--------|:--------:|-------|
| mathematics-omega-germ-construction | 2 | Fiber degeneration + τ³ fibration |
| mathematics-split-complex-shift | 1 | Function class containment hierarchy |
| mathematics-mutual-determination | 1 | Pentagonal 5-way equivalence cycle |
| mathematics-self-enrichment | 1 | Yoneda triad |
| mathematics-categoricity | 0 | Part 9 categoricity argument has no dedicated diagram |
| mathematics-central-theorem | 1 | O(τ³) ≅ A_spec(ℒ) isomorphism with bipolar splitting |

### Book III — Categorical Spectrum (6 modules → 7 diagrams)

| Module | Diagrams | Notes |
|--------|:--------:|-------|
| mathematics-canonical-ladder | 1 | Enrichment ladder E₀⊂E₁⊂E₂⊂E₃ |
| mathematics-sector-template | 1 | 4+1 sector decomposition |
| mathematics-spectral-algebra | 2 | Spectral trichotomy + Master Schema |
| mathematics-hinge-theorem | 1 | Master Schema reused (same diagram, different framing) |
| mathematics-computation-bridge | 1 | Computational bi-square at E₂ |
| mathematics-bridge-axiom | 1 | Architecture of reality grid |

Note: the Master Schema (ch63) serves both `mathematics-spectral-algebra` and `mathematics-hinge-theorem` because the Hinge Theorem IS the Master Schema interpretation — this is intentional reuse.

### Book IV — Categorical Microcosm (9 modules → 11 diagrams)

| Module | Diagrams | Notes |
|--------|:--------:|-------|
| physics-neutron-primacy | 2 | Defect bundle + T² torus arena |
| physics-beta-decay | 1 | Five sectors in concert (all 5 sectors in one process) |
| physics-fine-structure | 1 | Complete coupling ledger (from part 8) |
| physics-electron-mass | 1 | 10-link mass ratio chain (Epstein zeta) |
| physics-electroweak-synthesis | 2 | EW mixing triangle + Sector atlas |
| physics-nuclear-physics | 1 | SM–τ³ translation dictionary |
| physics-three-generations | 1 | H₁(τ³;ℤ) ≅ ℤ³ three winding classes |
| physics-atomic-ladder | 1 | Complexity hierarchy (P→NP through molecular structure) |
| physics-self-description | 1 | Self-describing closure loop |

Note: three modules share `IV.1` source part (neutron-primacy, beta-decay, fine-structure). Each gets a distinct thesis-aligned diagram.

### Book V — Categorical Macrocosm (9 modules → 9 diagrams)

| Module | Diagrams | Notes |
|--------|:--------:|-------|
| physics-hermetic-principle | 1 | Fiber-base split (microcosm T² / macrocosm τ¹) |
| physics-cmb-pipeline | 1 | Cosmic stack API pipeline |
| physics-gravity-earned | 1 | τ-Einstein equation as boundary identity |
| physics-gravitational-closing | 1 | τ-native ↔ orthodox correspondence |
| physics-no-dark-energy | 0 | Part 3 develops the thesis discursively without a canonical diagram |
| physics-thermodynamic-inversion | 1 | Entropy splitting (S_def vs S_ref) |
| physics-no-dark-matter | 2 | Capacity→rotation curves + Sector budget exhaustion |
| physics-black-holes | 1 | T² vs S² horizon topology |
| physics-falsification-predictions | 1 | Threshold ladder (energy scales from Planck to H₀) |

### Book VI — Categorical Life (8 modules → 10 diagrams)

| Module | Diagrams | Notes |
|--------|:--------:|-------|
| life-life-defined | 2 | Parity bridge + Homochirality cascade |
| life-layer-separation | 2 | Distinction/SelfDesc matrix + Enrichment regimes |
| life-seven-hallmarks | 1 | Bijection φ mapping hallmarks to categorical predicates |
| life-life-sectors | 1 | 4+1 sector template at E₂ |
| life-genetic-code | 1 | Central Dogma as morphism composition |
| life-evolution | 0 | Evolution chapters develop thesis textually |
| life-neural-architecture | 1 | Extended lemniscate with self-referential loop |
| life-crossing-limit | 2 | Distinction matrix (BH placement) + Enrichment regimes (BH-life) |

Note: `life-layer-separation` and `life-crossing-limit` share 2 diagrams (ch48-distinction-matrix + ch50-enrichment-regimes). Intentional reuse — the same diagrams support two distinct theses.

### Book VII — Categorical Metaphysics (11 modules → 10 diagrams)

| Module | Diagrams | Notes |
|--------|:--------:|-------|
| metaphysics-four-registers | 2 | Sector at E₃ + Enrichment tower |
| metaphysics-ontology | 1 | Five generators on the lemniscate |
| metaphysics-phenomenology | 1 | Knowledge as sheaf sections |
| metaphysics-aesthetics | 0 | Part 4 has no TikZ figures — aesthetic theory is discursive |
| metaphysics-language-meaning | 0 | Part 5 has no TikZ figures |
| metaphysics-logic-inference | 0 | Part 6 has no TikZ figures |
| metaphysics-categorical-ethics | 2 | CI sheaf + CI failure modes (both from ch77) |
| metaphysics-societies | 1 | Social ontology as recognition topology |
| metaphysics-mind-consciousness | 2 | Minds as topoi + Free will branching |
| metaphysics-logos-sector | 1 | S_L as S_D ∩ S_C unifying sector |
| metaphysics-no-forced-stance | 0 | Parts 11-12 develop the thesis discursively |

Note: four Book VII modules have no diagrams (aesthetics, language-meaning, logic-inference, no-forced-stance). These are philosophically discursive chapters where the thesis resists simple visualization. This is appropriate — not a gap.

## Modules without diagrams (13 total, intentional)

These modules were audited and no diagram was selected, either because no TikZ figure exists in the source chapters or because existing figures don't directly illustrate the module's central thesis:

- Book I: hyperfactorization, prime-polarity, internal-sets, split-complex-holomorphy, earned-topos, global-hartogs (6)
- Book II: categoricity (1)
- Book V: no-dark-energy (1)
- Book VI: evolution (1)
- Book VII: aesthetics, language-meaning, logic-inference, no-forced-stance (4)

## Review instructions

**To adjust the mapping**: edit `scripts/framework-diagrams-mapping.json` directly. You can:
- Remove a diagram by deleting its entry from the `diagrams` array
- Swap a diagram by replacing the object with one pointing to a different `tex_file` / `label`
- Add a diagram to a module currently at 0 (up to 2 per module)

**To approve as-is**: just tell me "approved" or "proceed with Phase 3" and I'll run the batch conversion book by book.

**Next step**: Phase 3 runs `scripts/tikz_to_svg.py` in batch mode, converts all 58 remaining diagrams (one already done in Phase 1), wires them into the corresponding module frontmatter, and ships them as one commit per book (7 commits total).
