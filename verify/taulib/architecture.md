---
layout: program-doc
title: "TauLib Architecture"
permalink: /verify/taulib/architecture/
lane: verify
summary_short: "Module dependency graph, reading paths by audience, and per-book start files."
right_rail:
  related:
  - title: TauLib Overview
    url: /verify/taulib/
  - title: Formalization Status
    url: /verify/taulib/status/
  - title: Verify Overview
    url: /verify/
  artifacts:
  - title: TauLib Repository
    url: https://github.com/Panta-Rhei-Framework/taulib
    external: true
  meta:
    type: "Documentation"
    status: "Frozen"
    updated: "April 2026"
---

## Module Dependency Graph

TauLib's modules follow a strict dependency order. Each layer builds only on what came before.

```
Book I (Foundations)
  Kernel --> Orbit --> Denotation --> Coordinates
                                         |
                                    Polarity --> Boundary
                                         |          |
                                     Sets, Logic    Holomorphy
                                         |          |
                                       Topos -------+
                                         |
                                     MetaLogic
                                         |
                                        CF

Book II (Holomorphy)
  Interior --> Domains --> Topology --> Geometry
      |
  Transcendentals --> Enrichment --> CentralTheorem
      |
  Regularity --> Hartogs --> Closure --> Mirror

Book III (Spectrum)
  Enrichment --> Sectors --> Spectral --> Arithmetic
      |
  Bridge --> Computation --> Doors --> Hinge
      |
  Physics --> Mirror --> Spectrum (TTM)

Books IV-VII build on I-III
  BookIV (Microcosm) --> BookV (Macrocosm) --> BookVI (Life) --> BookVII (Metaphysics)
```

## Reading Paths by Audience

### For Skeptics / Reviewers

1. `Tour/VerifyItYourself.lean` — 5 extraordinary claims, verified live
2. `Tour/OneConstant.lean` — Full constants ledger from iota_tau alone
3. `BookIII/Bridge/BridgeAxiom.lean` — The scope ledger: what is proved vs. conjectured

### For Mathematicians

1. `BookI/Kernel/Signature.lean` — The 5 generators and rho operator
2. `BookI/Kernel/Axioms.lean` — Axioms K1-K6
3. `BookI/Orbit/Rigidity.lean` — Aut(tau) = {id} (categoricity)
4. `BookI/Boundary/Iota.lean` — The master constant iota_tau = 2/(pi+e)
5. `BookII/CentralTheorem/CentralTheorem.lean` — O(tau^3) = A_spec(L)
6. `BookIII/Bridge/BridgeAxiom.lean` — The one conjectural gap

### For Physicists

1. `Tour/Physics.lean` — Interactive overview of all key predictions
2. `Tour/OneConstant.lean` — alpha, h, l_1, omega_b, r — all from iota_tau
3. `BookIV/Electroweak/EWSynthesis.lean` — 9 EW quantities from iota_tau + m_n
4. `BookV/Cosmology/CMBSpectrum.lean` — CMB first peak at +69 ppm
5. `BookV/Astrophysics/RotationCurves.lean` — 20 galaxies, no dark matter

### For Biologists

1. `Tour/LifeFromPhysics.lean` — 4+1 life sectors, genetic code, neural arch
2. `BookVI/Source/GeneticCode.lean` — Codon degeneracy as error correction
3. `BookVI/Consumer/Neural.lean` — Neural architecture as tau^3 computer

### For Philosophers

1. `Tour/MindAndEthics.lean` — CI formalization, consciousness, free will, Logos
2. `BookVII/Ethics/CIProof.lean` — The Categorical Imperative as theorem
3. `BookVII/Logos/Sector.lean` — Consciousness as global section
4. `BookVII/Final/Boundary.lean` — The three methodological sorry

### For Lean Users

1. `Tour/Foundations.lean` — Interactive walkthrough of the axioms
2. `lakefile.lean` — Mathlib tactics-only dependency policy
3. `BookI/Kernel/Axioms.lean` — See how axioms become Lean theorems
4. Browse any module — all 450 files have 30+ line docstring headers

## Per-Book Start Files

| Book | Start Here | What You'll Find |
|------|-----------|-----------------|
| I | `BookI/Kernel/Signature.lean` | The 5 generators — where everything begins |
| II | `BookII/Interior/Tau3Fibration.lean` | The tau^3 = tau^1 x_f T^2 construction |
| III | `BookIII/Enrichment/CanonicalLadder.lean` | The E0-E1-E2-E3 ladder |
| IV | `BookIV/Sectors/SectorParameters.lean` | The 5 sector decomposition |
| V | `BookV/Gravity/GravitationalConstant.lean` | G from the torus vacuum |
| VI | `BookVI/LifeCore/Distinction.lean` | The 5-condition life predicate |
| VII | `BookVII/Meta/Saturation.lean` | Saturation theorem |

## Module Counts

| Book | Families | Files | Lines | Axioms | Sorry |
|------|:--------:|------:|------:|:------:|:-----:|
| I — Foundations | 12 | 94 | 20,554 | 0 | 0 |
| II — Holomorphy | 12 | 65 | 18,069 | 0 | 0 |
| III — Spectrum | 12 | 70 | 16,807 | 3 | 0 |
| IV — Microcosm | 11 | 89 | 29,730 | 1 | 0 |
| V — Macrocosm | 10 | 80 | 28,394 | 0 | 0 |
| VI — Life | 9 | 30 | 5,221 | 0 | 0 |
| VII — Metaphysics | 5 | 7 | 4,278 | 0 | 3 |
| Tour | — | 8 | ~1,850 | 0 | 0 |
| **Total** | **71** | **450** | **125,771** | **4** | **3** |
