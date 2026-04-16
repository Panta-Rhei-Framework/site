---
layout: taulib-doc
title: "TauLib.BookIV"
permalink: /verify/taulib/docs/book-iv/
lane: verify
module_name: "TauLib.BookIV"
book: ""
book_label: ""
right_rail:
  related:
  - title: TauLib Overview
    url: /verify/taulib/
  - title: Architecture
    url: /verify/taulib/architecture/
  artifacts:
  - title: Source on GitHub
    url: https://github.com/Panta-Rhei-Research/taulib
    external: true
  meta:
    type: "API Documentation"
    book: "Book "
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookIV — Categorical Microcosm


Master import file for Book IV (Categorical Microcosm) Lean modules.

Book IV = fiber T² of τ³ = τ¹ ×_f T² = spatial physics:
quantum mechanics, particles, forces, atoms, chemistry, fluids.

## Module Organization


### Sectors (Part I: Sector Parameter Foundation)


- `SectorParameters`: 5 sector instantiations with 4 defining parameters each

- `CouplingFormulas`: 10 coupling formulas as rational functions of ι<sub>τ</sub>

- `FineStructure`: Fine structure constant α derivation


### Physics (Part II: Physical Quantity Core)


- `QuantityFramework`: 5 primary invariants, carrier types, particle ontology

- `PlanckCharacter`: ℏ_τ as sector lift of ι<sub>τ</sub>, uncertainty products

- `DefectFunctional`: 4-component defect tuple, 8 fluid regimes

- `MassEnergy`: Mass index, energy index, mass-energy relation

- `Thermodynamics`: Entropy splitting, defect budget, No-Running Principle


### Physics (Mass Ratio Derivation)


- `LemniscateCapacity`: √3 from lemniscate three-fold |1−ω|

- `HolonomyCorrection`: π³α² from triple U(1) holonomy

- `NucleonMassSplitting`: p-n mass difference, two-sector QCD−EM formula (33 ppm)


### Arena (Part I: Boundary Synthesis, ch02-ch07)


- `CoherenceKernel`: Coherence kernel, generator-sector assignment, uniqueness

- `RefinementTower`: Refinement tower, profinite limit, proto-time, NNO

- `Tau3Arena`: Base τ¹, fiber T², fibered product, master constant, 4 dimensions

- `BoundaryHolonomy`: Yoneda self-image, boundary characters, bipolar decomposition

- `FiveSectors`: Sector coupling atlas, temporal complement, power hierarchy

- `ActorsDynamics`: Defect bundles, radiation, virtual particles, primary invariants


### Calibration (Part II: Constants as Fixed-Point Readouts)


- `SIReference`: SI physical constants as exact Nat pairs (calibration targets)

- `DimensionlessNearMatch`: Weinberg, strong coupling range proofs

- `CalibrationAnchor`: Neutron mass anchor, 5→1 collapse

- `DimensionalBridge`: c, h, ε₀, μ₀, k_e derivation chain, Maxwell relation

- `ConstantsLedger`: Master synthesis table with scope labels


### Calibration (Part II: Extended modules)


- `SharedOntology`: Shared ontological layer between τ and SI

- `DimensionlessCouplings`: 5 self-couplings with numerical range proofs

- `DimensionlessCouplings2`: Cross-couplings, temporal complement, power hierarchy

- `DimensionlessAlpha`: Spectral and holonomy fine-structure formulas

- `RunningRegime`: Beta functions, readout functors, entropy at scale

- `ConstantsLedgerExt`: Coupling, scales, particle mass, structural constants tables


### Calibration (Mass Ratio & Epstein Zeta)


- `EpsteinZeta`: Epstein zeta function Z(s; iι<sub>τ</sub>) on T², Chowla-Selberg structure

- `MassRatioFormula`: R = m_n/m_e derivation, 10-link chain, range proofs


### QuantumMechanics (Part III: QM as Address Obstruction, ch16-ch22)


- `CRAddressSpace`: CR-manifold, CR-structure on τ³, character modes, admissible sublattice, spin-1/2

- `QuantumCharacters`: Characters on T², charge quantization, energy duality, sharp/spread states

- `HilbertSpace`: H_τ as L²-completion, inner product, ONB, entanglement, superposition

- `Quantization`: Holomorphic vector fields, quantization map, canonical commutation, observables

- `AddressObstruction`: Uncertainty as address obstruction, NoJointMin, Heisenberg bounds

- `Measurement`: Born rule, Schrödinger equation, decoherence, classical limit

- `EnergyEntropy`: Holomorphic tension, energy-entropy duality, arrow of time


### MassDerivation (Part III: Breathing Modes & Electron Mass, ch23-ch25)


- `BreathingModes`: Breathing operator on T², Epstein zeta, spectral distance, toroidal dominance

- `HolonomyDetail`: Triple holonomy H₃, π³α² correction, holonomy range proof

- `ElectronMass`: 10-link derivation chain, bulk term, Level 0 & Level 1+ formulas


### Electroweak (Part IV: EM + Weak + EW Mixing, ch26-ch35)


- `PhotonMode`: Photon as null transport mode, U(1) holonomy, electric charge quantization

- `GaugeInvariance`: EM principal bundle, gauge connections, field strength tensor

- `GaugeInvariance2`: Wilson loops, non-abelian gauge structure, Aharonov-Bohm phase

- `TauMaxwell`: Maxwell equations from boundary characters, Coulomb law, wave equation

- `AlphaDerivation`: Fine-structure constant derivation, spectral + holonomy formulas

- `WeakChirality`: Polarity as chirality, parity violation, W/Z boson structure

- `WeakChirality2`: Chirality selection rules, SU(2)_L assignment

- `WeakHolonomy`: SU(2) generators, W boson mass from holonomy

- `WeakHolonomy2`: Weinberg angle, Z boson mass, rho parameter

- `NeutrinoMode`: Neutrino flavors, PMNS matrix, mass hierarchy

- `MajoranaStructure`: σ = C_τ proof chain, Majorana theorem, 0νββ prediction

- `EWMixing`: Hypercharge, neutral boson mixing, EW unification

- `TauHiggs`: Higgs mechanism from crossing, physical vacuum

- `TauHiggs2`: Higgs mass prediction, Yukawa couplings, hierarchy problem

- `EWSynthesis`: 9 EW quantities, √3 triad, synthesis ledger


### Strong (Part V: Strong Sector, ch37-ch44)


- `StrongVacuum`: C-sector, strong defect functional, vacuum construction, truncation coherence

- `ColorHolonomy`: Color charge from eta-circle, ternary structure, SU(3), Wilson loops

- `Confinement`: Confinement theorem, color singlets, linear potential, proton stability

- `GapMetaTheorem`: Holonomy sector framework, kernel hypotheses, gap meta-theorem

- `YangMillsGap`: Plaquette defect, spectral gap, mass gap theorem, orthodox bridge conjecture

- `StrongCoupling`: Pi-lift construction, alpha_s^*, no ontic running, asymptotic freedom

- `QuarksGluons`: Quark modes, generations, gluon count, mesons, baryons

- `VacuumCatastrophe`: Boundary-first normalization, earned modes, no vacuum catastrophe


### Particles (Part VI: Particle Spectrum, ch45-ch51)


- `SectorAtlas`: Complete sector taxonomy, 9 canonical generators, generator adequacy

- `ThreeGenerations`: Three generations from lemniscate, Koide Q=2/3, mass exponents

- `BetaDecay`: Beta decay, hydrogen atom, Bohr radius, Rydberg constant, fine structure

- `HadronsNuclei`: Mesons, baryons, nucleon mass, nuclear shells, magic numbers, iron peak

- `PeriodicTable`: Periodic table, Madelung rule, bonding types, molecular geometry

- `SpectrumComplete`: Ontic entity criterion, ontic register, spectrum completeness

- `StrongCP`: θ_QCD = 0 from SA-i, neutron EDM = 0, no axion required (τ-native PQ)


### ManyBody (Part VII: Many-Body & Condensed Matter, ch52-ch54)


- `DefectFunctionalExt`: Macroscopic defect tuple, interaction corrections, tower compatibility, sector additivity

- `DefectFunctionalExt2`: Euler/NS/MHD/plasma/superfluid/superconductor regimes, temperature, phase transitions

- `FluidRegimes`: tau-Euler/NS flow, regularity, crystal/glass/quasicrystal, universal order parameter

- `CondensedMatter`: Melting sequence, topological branch, fiber-base factorization, fiber completeness


### Coda (Part VII: Closing Arc, ch55-ch57)


- `LawsAsStructure`: Tower-natural transformations, Noether corollary, UV finiteness, laws as structure

- `CompleteLedger`: 66-entry ledger, scope distribution, export contracts to Books V-VII, sphaleron question

- `SelfDescribing`: Neutron anchor rationale, self-enrichment, metaclosure, self-describing universe


### Physics (Ontological Architecture)


- `TickUnits`: 5 tick kinds as minimal endomorphisms, tick arithmetic, internal ratios

- `InternalEquations`: R₀, α, κ_D as internal identities with layer discipline

- `ReadoutFunctor`: R_μ with operational codomain, single anchor (m_n), 4 exact SI constants


## Current Count: 87 modules
