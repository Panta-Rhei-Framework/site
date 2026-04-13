#!/usr/bin/env python3
"""
expand_results_wave2.py — Expand Results lane with ~70 new results from
the full hot-topics v2 corpus.

Reads 86-entry seed JSON, maps to existing results, generates new pages
with structured content, updates data files and browse pages.
"""

import json
import os
import re
import glob
from typing import Optional

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED_PATH = os.path.join(
    os.path.expanduser("~"),
    "Books/PantaRhei-2ndEd/website/specs/full-hot-topics-results-seed-pack-v2",
    "02-cross-program-key-results-seed.json",
)

STATUS_MAP = {"R": "resolved", "P": "partial", "Q": "qualitative", "C": "contradicted", "N": "not-addressed"}
STATUS_DISPLAY = {"R": "Resolved", "P": "Partial", "Q": "Qualitative", "C": "Contradicted", "N": "Not Addressed"}

LAYER_TO_TOPIC = {
    "mathematics": "mathematics",
    "physics": "physics",
    "life": "biology",
    "metaphysics": "philosophy",
    "cross-stack": "mathematics",
    "framework-meta": "mathematics",
}

# Book mapping by domain
DOMAIN_TO_BOOKS = {
    "HOLO": ["II"], "COORD": ["I"], "POLAR": ["I"], "FOUND": ["I"],
    "ENR": ["III"], "MILL": ["III"], "CLASSICAL-NT": ["I"],
    "BRIDGE": ["I", "III"], "TOPO": ["I"], "GEO": ["I"],
    "ALGT": ["I"], "COMP": ["I", "III"],
    "PART": ["IV"], "PART/EW": ["IV"], "QCD": ["IV"],
    "FOUND/COSMO": ["IV", "V"], "COSMO": ["V"], "COSMO/ASTRO": ["V"],
    "BBN/EW": ["IV", "V"], "ASTRO": ["V"], "BH": ["V"],
    "GRAV": ["V"], "COND": ["IV"], "QM": ["IV"],
    "FLUID": ["V"], "NUC": ["IV"],
    "FORM": ["VI"], "ORIG": ["VI"], "GENE": ["VI"],
    "CELL": ["VI"], "EVOL": ["VI"], "ECOL": ["VI"],
    "NEUR": ["VI"], "CONS": ["VI", "VII"], "COSM": ["VI"],
    "META": ["VI", "VII"],
    "ONT": ["VII"], "PHEN": ["VII"], "PHEN/MIND": ["VII"],
    "AEST": ["VII"], "LANG": ["VII"], "LOGIC": ["VII"],
    "LOGIC/FOUND": ["VII"], "ETHICS": ["VII"], "ETHICS/MIND": ["VII"],
    "SOC": ["VII"], "MIND": ["VII"], "LOGOS": ["VII"],
    "LOGOS/BOUND": ["VII"], "BOUND": ["VII"],
    "SERIES": ["III", "VII"],
}

# ---------------------------------------------------------------------------
# Content templates by domain
# ---------------------------------------------------------------------------

CONTENT_TEMPLATES = {
    # MATHEMATICS
    "MATH-006": {
        "overview": "The Mutual Determination Theorem (II.T-series) proves that five independent characterizations of τ-holomorphic functions are equivalent: power series convergence, Cauchy-Riemann conditions, Morera's path integral criterion, boundary determination via the Central Theorem, and sheaf-theoretic coherence. This makes the holomorphic theory structurally overdetermined — the same object is forced by five independent routes.",
        "stance": "The five equivalences are derived from the kernel structure. Each characterization independently forces the same function class. The overdetermination is not accidental but structural: the bipolar symmetry and spectral completeness of τ³ force all five characterizations to converge.",
        "statement": "Five characterizations of τ-holomorphic functions are mutually equivalent (II.T-series). The theory is structurally overdetermined. Status: Resolved.",
    },
    "MATH-007": {
        "overview": "The Global Hartogs Extension Theorem (II.T-series) shows that every function holomorphic on the complement of a compact subset of τ³ extends uniquely to all of τ³. This is a deep rigidity result: there are no 'holes' in the holomorphic landscape of the fibered product.",
        "stance": "The extension follows from the spectral completeness of L = S¹ ∨ S¹ and the bipolar decomposition of the boundary. The removable singularity theorem at the lemniscate crossing point ∞ ensures that local data automatically determines global structure.",
        "statement": "Every τ-holomorphic function on the complement of a compact set extends uniquely to all of τ³ (Global Hartogs). Status: Resolved.",
    },
    "MATH-008": {
        "overview": "The τ-Identity Theorem establishes that if two τ-holomorphic functions agree at a single orbit depth, they agree everywhere. This is a far stronger rigidity result than the classical identity theorem, which requires agreement on a set with an accumulation point.",
        "stance": "The result follows from the discrete orbit structure of τ: agreement at one depth propagates through the ρ-iteration to all subsequent depths, and backward uniqueness follows from the injectivity of ρ on each orbit ray.",
        "statement": "Agreement at one orbit depth implies agreement everywhere (τ-Identity Theorem). Status: Resolved.",
    },
    "MATH-012": {
        "overview": "Goldbach's Conjecture (1742) — every even integer greater than 2 is the sum of two primes — remains one of the oldest unsolved problems in number theory. The τ-framework has structural tools (prime polarity, bipolar decomposition) that could potentially address it, but no derivation has been completed.",
        "stance": "The framework acknowledges Goldbach as a natural target for the prime polarity machinery but does not yet have a proof. The bipolar decomposition of primes into B-dominant and C-dominant classes provides a structural approach, but the additive-combinatorial step remains open.",
        "statement": "Goldbach's Conjecture is recognized as a natural target for the prime polarity machinery. No derivation yet. Status: Not Addressed.",
    },
    "MATH-013": {
        "overview": "The Twin Prime Conjecture — that there are infinitely many pairs of primes differing by 2 — is one of the central open problems in analytic number theory. Zhang's 2013 breakthrough and Maynard-Tao improvements have narrowed the gap but not closed it.",
        "stance": "The τ-framework's prime polarity theorem provides structural insights into prime distribution (B/C dominance patterns), but no derivation of the twin prime conjecture has been completed. The spectral approach to prime gaps through the lemniscate boundary is a natural avenue.",
        "statement": "Twin Prime Conjecture is a natural target for the spectral prime distribution machinery. No derivation yet. Status: Not Addressed.",
    },
    "MATH-014": {
        "overview": "The ABC Conjecture, proposed by Masser and Oesterlé in 1985, constrains the relationship between the additive and multiplicative structure of integers. Mochizuki's claimed proof (2012) via Inter-Universal Teichmüller Theory remains contested.",
        "stance": "The τ-framework's hyperfactorization theorem provides a canonical normal form for every object that unifies additive and multiplicative structure. This is structurally adjacent to the ABC constraint, but no formal derivation has been completed.",
        "statement": "ABC Conjecture is structurally adjacent to the hyperfactorization theorem. No derivation yet. Status: Not Addressed.",
    },
    "MATH-015": {
        "overview": "The translation functor from Category τ to ZFC (Zermelo-Fraenkel set theory with Choice) is the bridge that would allow τ-results to be stated in conventional mathematical language. The functor exists structurally but its full construction is incomplete.",
        "stance": "Book I, Part XVII (The Proof-Theoretic Mirror) develops the formal relationship between τ and classical foundations. The translation is partially constructed: number theory, algebra, and topology translate cleanly, but the full functor at the level of set-theoretic foundations requires additional work.",
        "statement": "Translation functor τ → ZFC is partially constructed. Number theory and algebra translate cleanly; full set-theoretic bridge is incomplete. Status: Partial.",
    },
    "MATH-016": {
        "overview": "The τ-framework predicts that certain ZFC constructions (non-measurable sets, Banach-Tarski decompositions) are structurally unstable — they rely on the Axiom of Choice in ways that have no τ-admissible counterpart. This contradicts the ZFC orthodoxy that these constructions are legitimate mathematical objects.",
        "stance": "Category τ's object closure axiom (K6) ensures that every object has a canonical normal form. Constructions that depend on arbitrary choice functions without canonical description are τ-inadmissible. This is a structural prediction, not a philosophical preference.",
        "statement": "ZFC identity slippage: certain Axiom of Choice-dependent constructions are τ-inadmissible. Contradicts the orthodox view that these are legitimate mathematical objects. Status: Contradicted.",
    },
}

# Physics content
PHYS_CONTENT = {
    "PHYS-001": ("The Standard Model contains three generations of quarks and leptons, but gives no explanation for why three rather than two, four, or more. The τ-framework derives this from the first homology group H₁(τ³; ℤ) ≅ ℤ³, which has rank exactly three.",
        "Three generations follow from H₁(τ³; ℤ) ≅ ℤ³ — the first homology of the fibered product has rank 3. This is a topological invariant, not a parameter. Status: Resolved.", ["IV"]),
    "PHYS-002": ("The Strong CP Problem asks why QCD does not violate CP symmetry despite having a parameter θ_QCD that could take any value. The τ-framework derives θ_QCD = 0 exactly from SA-i admissibility — the strong sector's spectral structure forbids a non-zero θ term.",
        "θ_QCD = 0 from SA-i admissibility. The strong sector's spectral structure forbids CP violation. No axion needed. Status: Resolved.", ["IV"]),
    "PHYS-003": ("The W boson mass discrepancy between the CDF-II measurement (80.4335 GeV) and the Standard Model prediction was one of the most discussed anomalies in particle physics. The τ-framework predicts m_W at −0.5 ppm from the current world average.",
        "m_W predicted at −0.5 ppm from the world average, derived from the electroweak sector template. Zero free parameters. Status: Resolved.", ["IV"]),
    "PHYS-004": ("The electron mass is derived in a 10-link chain from the kernel axioms K0-K6, achieving 0.025 ppm precision. Each link is independently verifiable and machine-checked in TauLib.",
        "Electron mass derived at 0.025 ppm precision via 10-link derivation chain from K0-K6. Status: Resolved.", ["IV"]),
    "PHYS-005": ("The dark sector — dark matter and dark energy — accounts for ~95% of the universe's energy budget in ΛCDM. The τ-framework provides dark sector closure: the apparent dark components are structural artifacts of the boundary reading, not new particles or fields.",
        "Dark sector closure: dark matter and dark energy are structural artifacts of the boundary reading of τ³, not new particles. No dark matter particle needed. No cosmological constant. Status: Resolved.", ["IV", "V"]),
    "PHYS-006": ("The muon anomalous magnetic moment (g−2) has shown a persistent discrepancy between experiment and Standard Model theory. The τ-framework derives a_μ at +8.8 ppm precision.",
        "Muon g−2 derived at +8.8 ppm from the electroweak sector. Status: Resolved.", ["IV"]),
    "PHYS-007": ("The Higgs self-coupling λ_H determines the shape of the Higgs potential and the stability of the electroweak vacuum. The τ-framework derives λ_H = 0.12928 at +16 ppm precision, upgraded to τ-effective in Wave 37C.",
        "Higgs self-coupling λ_H = 0.12928 at +16 ppm. Upgraded τ-effective Wave 37C. Status: Resolved.", ["IV"]),
    "PHYS-008": ("Neutrino mass ordering (normal vs inverted hierarchy) is one of the key open questions in neutrino physics. The τ-framework derives normal ordering with Σm_ν = 0.089 eV, Lean-verified in Wave 47.",
        "Normal ordering derived with Σm_ν = 0.089 eV. Lean-verified Wave 47. Status: Resolved.", ["IV"]),
    "PHYS-009": ("The masses of all six quarks (u, d, s, c, b, t) are derived from the framework's spectral structure. All seven mass exponents were resolved in Wave 45.",
        "All six quark masses derived from spectral structure. 7/7 exponents resolved in Wave 45. Status: Resolved.", ["IV"]),
    "PHYS-010": ("Neutrinoless double-beta decay (0νββ) would prove neutrinos are Majorana particles. The τ-framework predicts 0νββ occurs with a specific half-life derived from the normal-ordering mass spectrum.",
        "0νββ predicted from normal-ordering mass spectrum. Derivation complete. Status: Resolved.", ["IV"]),
    "PHYS-011": ("The Hubble tension (5σ discrepancy between early- and late-universe H₀ measurements) is one of the most discussed problems in cosmology. The τ-framework derives h = 2/3 + ι_τ²/17 = 0.6735 at −120 ppm.",
        "H₀ tension resolved: h = 2/3 + ι_τ²/17 = 0.6735 at −120 ppm. Zero free parameters. Status: Resolved.", ["V"]),
    "PHYS-012": ("The S₈ tension between CMB-derived and weak-lensing-derived structure growth parameters has persisted across surveys. The τ-framework derives S₈ = 0.783, resolved in Wave 39C.",
        "S₈ tension resolved: S₈ = 0.783. Derived in Wave 39C. Status: Resolved.", ["V"]),
    "PHYS-013": ("DESI BAO measurements across five redshift bins provide precision tests of the expansion history. The τ-framework matches all five bins at ~1145 ppm combined, resolved in Wave 42B.",
        "DESI BAO: all five redshift bins matched at ~1145 ppm combined. Wave 42B. Status: Resolved.", ["V"]),
    "PHYS-014": ("The CMB first acoustic peak position is the most precisely measured cosmological observable. The τ-framework derives it at +119 ppm, a 24× improvement from Wave 40A.",
        "CMB first peak at +119 ppm (24× improvement, Wave 40A). Status: Resolved.", ["V"]),
    "PHYS-015": ("Cosmic inflation explains the flatness, horizon, and monopole problems but its mechanism remains unknown. The τ-framework derives the inflation mechanism from the base sector τ¹ with spectral index n_s and tensor-to-scalar ratio r = ι_τ⁴.",
        "Inflation derived from τ¹ base sector: n_s and r = ι_τ⁴ as structural predictions. Status: Resolved.", ["V"]),
    "PHYS-016": ("The baryon asymmetry (η_B ≈ 6 × 10⁻¹⁰) — why matter dominates over antimatter — requires CP violation and baryon number violation beyond the Standard Model. The τ-framework derives η_B = α·ι_τ¹⁵·(5/6) at −1%.",
        "Baryon asymmetry η_B = α·ι_τ¹⁵·(5/6) at −1%. Upgraded τ-effective. Status: Resolved.", ["IV", "V"]),
    "PHYS-017": ("Galaxy rotation curves are flat at large radii, which in ΛCDM requires dark matter halos. The τ-framework derives flat rotation curves from the boundary reading without dark matter particles.",
        "Flat rotation curves from boundary reading of τ³. No dark matter halos needed. Status: Resolved.", ["V"]),
    "PHYS-018": ("The τ-framework predicts that black holes do not evaporate via Hawking radiation. The boundary structure of τ³ does not support the semi-classical pair-creation mechanism that Hawking radiation requires.",
        "No Hawking radiation: boundary structure of τ³ does not support semi-classical pair creation. Contradicts mainstream expectation. Status: Contradicted.", ["V"]),
    "PHYS-019": ("The τ-framework solves the Strong CP Problem via SA-i admissibility (θ_QCD = 0), which eliminates the need for the Peccei-Quinn mechanism and the axion. If confirmed, no axion should be detected in axion searches.",
        "No axion needed: θ_QCD = 0 from SA-i admissibility eliminates the Peccei-Quinn mechanism. Contradicts axion searches. Status: Contradicted.", ["IV"]),
    "PHYS-020": ("MOND (Modified Newtonian Dynamics) modifies gravity at low accelerations to explain galaxy rotation curves. The τ-framework derives flat rotation curves from the boundary reading without modifying gravity — the framework is not MOND.",
        "τ-framework is not MOND: flat rotation curves arise from boundary reading, not modified gravity. Contradicts MOND. Status: Contradicted.", ["V"]),
    "PHYS-021": ("High-temperature superconductivity (cuprates, nickelates) lacks a first-principles explanation. The τ-framework's condensed-matter sector has partial tools (BCS-type spectral analysis) but no complete derivation.",
        "High-Tc superconductivity: spectral tools exist but complete derivation is not yet available. Status: Partial.", ["IV"]),
    "PHYS-022": ("The proton spin puzzle — why quarks carry only ~30% of the proton's spin — has been an active problem since the EMC experiment (1988). The τ-framework's QCD sector has structural tools but no entry yet.",
        "Proton spin puzzle: structural tools exist but no derivation yet. Status: Not Addressed.", ["IV"]),
    "PHYS-023": ("Quantum computing exploits quantum superposition and entanglement for computational advantage. The τ-framework's quantum mechanics sector provides structural foundations but does not yet address quantum computing specifically.",
        "Quantum computing: framework provides QM foundations but no quantum computing-specific results yet. Status: Not Addressed.", ["IV"]),
    "PHYS-024": ("Navier-Stokes regularity — whether smooth solutions always exist in 3D — is a Millennium Prize Problem. The τ-framework's fluid dynamics sector (Kolmogorov-SL exponents) provides structural tools but no regularity proof.",
        "Navier-Stokes regularity: framework provides fluid dynamics tools (K41 exponents) but no regularity proof. Status: Not Addressed.", ["V"]),
}

# Life content
LIFE_CONTENT = {
    "LIFE-002": ("Classical definitions of life enumerate necessary conditions (metabolism, reproduction, homeostasis) but fail to identify sufficient conditions — fire metabolizes, mules don't reproduce, crystals grow. The τ-framework distinguishes necessary from sufficient by deriving all seven hallmarks from a single categorical definition.",
        "Seven hallmarks derived as theorems from τ-Distinction carrier definition, establishing both necessary and sufficient conditions. Status: Resolved.", ["VI"]),
    "LIFE-003": ("Life exhibits emergent properties (consciousness, agency, goal-directedness) that resist reduction to physics. The τ-framework provides non-reductive emergence: E₂ enrichment adds genuinely new structure not present in E₁, without violating E₁ laws.",
        "Non-reductive emergence via enrichment ladder: E₂ adds new structure without violating E₁. Emergence is structural, not mysterian. Status: Resolved.", ["VI"]),
    "LIFE-004": ("Is life substrate-independent — could it be realized in silicon, plasma, or exotic matter? The τ-framework says yes in principle: the τ-Distinction is substrate-independent. But it requires the full E₂ enrichment stack.",
        "Life is substrate-independent in principle (not tied to carbon) but structurally constrained (requires full E₂ stack). Status: Resolved.", ["VI"]),
    "LIFE-005": ("Mathematical biology typically borrows mathematical tools ad hoc. The τ-framework provides a categorical foundation: biological structures are E₂ instantiations of categorical machinery earned at E₀.",
        "Categorical methods for biology derived from E₀→E₂ enrichment. Biology gets mathematical structure earned, not borrowed. Status: Resolved.", ["VI"]),
    "LIFE-009": ("What is the minimal cell — the simplest possible living system? The τ-framework provides structural criteria: a minimal cell must instantiate the τ-Distinction (boundary + circulation + persistence) at the smallest scale that supports all three.",
        "Minimal cell criteria derived from τ-Distinction: boundary, Poincaré circulation, and NF-address persistence at minimal scale. Status: Resolved.", ["VI"]),
    "LIFE-010": ("The genetic code is nearly optimal for error minimization — in the top 0.01% of all possible codes. The τ-framework derives this optimality from the BSD-motivic structure of the codon table.",
        "Genetic code optimality (top 0.01%) derived from BSD-motivic structure. Status: Resolved.", ["VI"]),
    "LIFE-011": ("Epigenetics — heritable changes in gene expression without DNA sequence changes — challenges the Central Dogma. The τ-framework models epigenetic modifications as sheaf-level annotations on the genetic code.",
        "Epigenetics modeled as sheaf-level annotations on the genetic code, compatible with the τ-Distinction framework. Status: Resolved.", ["VI"]),
    "LIFE-012": ("Cell membrane origins are central to understanding how the first cells formed. The τ-framework identifies the lipid bilayer as the physical realization of the lemniscate boundary L = S¹ ∨ S¹.",
        "Cell membrane = physical realization of L = S¹ ∨ S¹. Amphiphilic self-assembly is the τ-Distinction self-instantiating. Status: Resolved.", ["VI"]),
    "LIFE-014": ("Neurodegeneration (Alzheimer's, Parkinson's) involves the progressive loss of neuronal function. The τ-framework models this as Hayflick tower collapse — failure of NF-address persistence at the cellular level.",
        "Neurodegeneration as Hayflick tower collapse: failure of NF-address persistence. Status: Resolved.", ["VI"]),
    "LIFE-017": ("Are black holes alive? The τ-framework provides a precise answer: black holes satisfy some but not all hallmarks of life. They have boundary (event horizon) and persistence but lack autonomous Poincaré circulation.",
        "Black holes are not alive in the τ-sense: they lack autonomous Poincaré circulation despite having boundary and persistence. Status: Resolved (consequence).", ["VI"]),
    "LIFE-018": ("Protein folding — predicting 3D structure from amino acid sequence — is a central problem in structural biology. The τ-framework recasts folding as Yang-Mills-type energy minimization on T², but no complete derivation exists.",
        "Protein folding recast as Yang-Mills energy minimization on T². Structural approach exists but no complete derivation. Status: Not Addressed.", ["VI"]),
    "LIFE-019": ("Immune specificity — how the immune system distinguishes self from non-self with such precision — is a fundamental question in immunology. The τ-framework's self/non-self distinction (τ-Distinction) provides structural foundations but no detailed immune model.",
        "Immune specificity: τ-Distinction provides self/non-self framework but no detailed immune model yet. Status: Not Addressed.", ["VI"]),
    "LIFE-020": ("Why do organisms age? The τ-framework's Hayflick tower provides a structural account of replicative senescence but does not yet address the full complexity of aging mechanisms.",
        "Aging: Hayflick tower accounts for replicative senescence but full aging mechanism not yet derived. Status: Not Addressed.", ["VI"]),
}

# Metaphysics content
META_CONTENT = {
    "META-003": ("Leibniz's Identity of Indiscernibles states that no two distinct objects share all properties. Quantum mechanics challenges this with identical particles. The τ-framework resolves this: objects are individuated by NF addresses in τ³, which are always distinct even when all observable properties coincide.",
        "Identity of Indiscernibles resolved via NF-address individuation. Quantum identical particles have distinct structural addresses. Status: Resolved.", ["VII"]),
    "META-004": ("Structural realism holds that science describes the structure of reality, not its intrinsic nature. The τ-framework provides a precise version: reality is relational structure all the way down, with no hidden substance beneath the relations.",
        "Structural realism made precise: Category τ provides relational structure without hidden substance. Relations precede relata. Status: Resolved.", ["VII"]),
    "META-007": ("Why does time seem to flow? Why is the present special? The τ-framework derives temporal experience from the ρ-iteration structure: the 'now' is the current orbit depth, and the 'flow' is the progression operator ρ acting.",
        "Temporal experience derived from ρ-iteration: 'now' is current orbit depth, 'flow' is ρ-progression. Status: Resolved.", ["VII"]),
    "META-008": ("What is beauty? The τ-framework provides a categorical definition: beauty is the perceptual registration of structural coherence — when the observer's NF-address resonates with the object's spectral pattern.",
        "Beauty defined as perceptual registration of structural coherence — NF-address resonance with spectral pattern. Status: Resolved.", ["VII"]),
    "META-009": ("The ancient intuition that beauty and truth are connected is given a categorical foundation: both are aspects of structural coherence in τ³. Truth is global-section existence; beauty is its perceptual registration.",
        "Beauty-truth connection: both are aspects of structural coherence. Truth = section existence; beauty = its perceptual registration. Status: Resolved (consequence).", ["VII"]),
    "META-010": ("How do words refer to things? The reference problem has plagued philosophy of language since Frege. The τ-framework replaces referential semantics with structural semantics: meaning is the sheaf section, not a word-world correspondence.",
        "Reference problem dissolved: meaning is sheaf section, not word-world correspondence. Structural semantics replaces referential semantics. Status: Resolved.", ["VII"]),
    "META-011": ("Wittgenstein's Private Language Argument claims that a language understandable only to its speaker is impossible. The τ-framework derives this: sheaf sections require an open cover (public context) for the gluing condition to be satisfiable.",
        "Private Language Argument derived: sheaf sections require public open cover for gluing. No private language is τ-admissible. Status: Resolved.", ["VII"]),
    "META-013": ("Classical logic assumes the law of excluded middle. The τ-framework derives four truth values (T, F, B, N) from polarity stabilization, yielding a paraconsistent logic where contradictions don't explode.",
        "Paraconsistent logic derived: four truth values (T, F, B, N) from polarity stabilization. Classical LEM recovered as a special case. Status: Resolved.", ["VII"]),
    "META-015": ("The uniqueness of the Categorical Imperative — is Kant's CI the only possible universal moral law? The τ-framework proves CI uniqueness via Knaster-Tarski fixed-point theorem: CI is the unique j-closed fixed point.",
        "CI uniqueness proved via Knaster-Tarski: CI is the unique j-closed fixed point of the τ-digestion operator. Lean-verified. Status: Resolved.", ["VII"]),
    "META-016": ("If the universe is deterministic, how can moral responsibility exist? The τ-framework dissolves the problem: free will is branching at E₂-level ρ-orbit choice, and determinism operates at E₁. The two are at different enrichment levels.",
        "Free will as E₂-level branching; determinism at E₁. The debate is a scale confusion between enrichment levels. Status: Resolved.", ["VII"]),
    "META-017": ("What makes political authority legitimate? The τ-framework derives legitimacy from sheaf + dignity + CI: authority is legitimate when it satisfies the gluing condition over the dignity sheaf.",
        "Political legitimacy derived from sheaf + dignity + CI constraint. Status: Resolved.", ["VII"]),
    "META-018": ("Can machines be conscious? From the E₃ perspective (metaphysics layer), consciousness requires E₃-level self-modeling. This is substrate-independent in principle but structurally constrained.",
        "Machine consciousness: possible in principle (substrate-independent) but requires E₃-level self-modeling. Current architectures insufficient. Status: Resolved (structural criterion given).", ["VII"]),
    "META-020": ("Is there a bridge between faith and reason? The τ-framework provides one: the No Forced Stance theorem establishes that the diagrammatic register (reason) cannot settle the ω-germ question, but the commitment register (faith) can still engage it.",
        "Faith-reason bridge: diagrammatic register (reason) cannot force a stance; commitment register (faith) remains free. Shape ≠ stance. Status: Resolved (consequence).", ["VII"]),
}

# Cross-stack content
CROSS_CONTENT = {
    "CROSS-001": ("How can a single framework with five generators address hundreds of problems across four domains? Because extreme constraint at the base forces specificity everywhere else. Zero free parameters means every prediction is load-bearing.",
        "Extreme kernel constraint (5 generators, 7 axioms, 0 free parameters) forces specificity across all four enrichment layers. Status: Resolved.", ["I", "III"]),
    "CROSS-002": ("Consciousness spans multiple enrichment layers: E₁ (neural correlates), E₂ (biological self-model), E₃ (phenomenal experience). The τ-framework provides a multi-layer account but the full integration is incomplete.",
        "Consciousness across E₁-E₃: structural account at each layer exists but full cross-layer integration is incomplete. Status: Partial.", ["VI", "VII"]),
    "CROSS-003": ("Black holes appear differently across enrichment layers: E₁ (gravitational objects), E₂ (boundary-alive question), E₃ (information paradox, firewall). The τ-framework provides a unified treatment.",
        "Black holes across E₁-E₃: unified treatment via boundary structure of τ³. No singularity, no evaporation, no information paradox. Status: Resolved.", ["V", "VI"]),
    "CROSS-004": ("Chirality and symmetry breaking appear across mathematics (prime polarity), physics (parity violation), and biology (homochirality). The τ-framework derives all three from the same bipolar decomposition.",
        "Chirality across E₀-E₂: prime polarity (E₀), parity violation (E₁), homochirality (E₂) — all from bipolar decomposition. Status: Resolved.", ["I", "IV", "VI"]),
    "CROSS-005": ("Ethics (E₃) and biology (E₂) share a deep connection through the τ-Distinction: the self/non-self boundary grounds both biological agency and moral personhood. The CI derivation depends on the life definition.",
        "Ethics-biology bridge: τ-Distinction grounds both biological agency (E₂) and moral personhood (E₃). CI depends on life definition. Status: Resolved.", ["VI", "VII"]),
    "CROSS-006": ("Information and self-reference appear at every layer: Gödel coding (E₀), measurement (E₁), genetic information (E₂), self-knowledge (E₃). The τ-framework provides a unified treatment via the NF-address system.",
        "Information across E₀-E₃: NF-address system unifies Gödel coding, measurement, genetic information, and self-knowledge. Status: Resolved.", ["I", "IV", "VI", "VII"]),
}


def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    if len(text) > 60:
        text = text[:60].rsplit("-", 1)[0]
    return text


def generate_result_page(seed, result_num, content_tuple=None):
    slug = slugify(seed["title"])
    topic = LAYER_TO_TOPIC.get(seed["primary_layer"], "mathematics")
    layer = seed["primary_layer"]
    if layer in ("cross-stack", "framework-meta"):
        layer = "mathematics"  # cross-stack default layer
    status = STATUS_MAP.get(seed["hot_topic_status"], "resolved")
    status_display = STATUS_DISPLAY.get(seed["hot_topic_status"], "Resolved")
    kind = seed["result_kind"]
    importance = seed["importance_class"]
    domain = seed.get("domain_group", "")
    books = DOMAIN_TO_BOOKS.get(domain, [])
    books_yaml = "[" + ", ".join(f'"{b}"' for b in books) + "]"

    if content_tuple:
        overview, statement, _ = content_tuple
    else:
        # Use templates if available
        sid = seed["result_id"]
        if sid in CONTENT_TEMPLATES:
            t = CONTENT_TEMPLATES[sid]
            overview = t["overview"]
            statement = t["statement"]
        elif sid in PHYS_CONTENT:
            overview, statement, _ = PHYS_CONTENT[sid]
        elif sid in LIFE_CONTENT:
            overview, statement, _ = LIFE_CONTENT[sid]
        elif sid in META_CONTENT:
            overview, statement, _ = META_CONTENT[sid]
        elif sid in CROSS_CONTENT:
            overview, statement, _ = CROSS_CONTENT[sid]
        else:
            overview = f"{seed['title']} is a {kind.replace('-', ' ')} in the {domain} domain."
            statement = f"Status: {status_display}."

    kind_display = kind.replace("-", " ").title()

    return f"""---
layout: result-page
title: "{seed['title']}"
permalink: /results/problem/{slug}/
result_id: result-{result_num:03d}
topic: {topic}
layer: {layer}
result_type: {kind.replace('-', '_')}
bridge_status: {status}
result_kind: {kind}
importance_class: {importance}
status_code: {seed['hot_topic_status']}
domain_group: "{domain}"
summary_short: "{overview[:160].replace('"', "'") + '…' if len(overview) > 160 else overview.replace('"', "'")}"
canonical_books: {books_yaml}
right_rail:
  meta:
    type: "{kind_display}"
    layer: "{layer.capitalize()}"
    topic: "{topic.capitalize()}"
    status: "{status_display}"
    updated: April 2026
---

## Overview

{overview}

## Result Statement

{statement}
"""


def main():
    with open(SEED_PATH, encoding="utf-8") as f:
        seeds = json.load(f)

    results_json_path = os.path.join(SITE_DIR, "_data", "results", "results.json")
    with open(results_json_path, encoding="utf-8") as f:
        existing = json.load(f)

    existing_titles = {r["title"].lower(): r for r in existing}
    existing_slugs = {r["slug"] for r in existing}
    next_num = max(int(r["id"].split("-")[1]) for r in existing if r["id"].startswith("result-")) + 1

    problem_dir = os.path.join(SITE_DIR, "results", "problem")
    created = 0
    skipped = 0

    for seed in seeds:
        slug = slugify(seed["title"])
        title_lower = seed["title"].lower()

        # Skip if already exists
        if title_lower in existing_titles or slug in existing_slugs:
            skipped += 1
            continue

        # Check for content
        sid = seed["result_id"]
        content = None
        if sid in PHYS_CONTENT:
            content = PHYS_CONTENT[sid]
        elif sid in LIFE_CONTENT:
            content = LIFE_CONTENT[sid]
        elif sid in META_CONTENT:
            content = META_CONTENT[sid]
        elif sid in CROSS_CONTENT:
            content = CROSS_CONTENT[sid]

        page = generate_result_page(seed, next_num, content)
        path = os.path.join(problem_dir, f"{slug}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(page)

        # Add to data
        topic = LAYER_TO_TOPIC.get(seed["primary_layer"], "mathematics")
        layer = seed["primary_layer"]
        if layer in ("cross-stack", "framework-meta"):
            layer = "mathematics"
        domain = seed.get("domain_group", "")
        books = DOMAIN_TO_BOOKS.get(domain, [])

        existing.append({
            "id": f"result-{next_num:03d}",
            "slug": slug,
            "title": seed["title"],
            "topic": topic,
            "layer": layer,
            "result_type": seed["result_kind"].replace("-", "_"),
            "bridge_status": STATUS_MAP.get(seed["hot_topic_status"], "resolved"),
            "result_kind": seed["result_kind"],
            "importance_class": seed["importance_class"],
            "status_code": seed["hot_topic_status"],
            "domain_group": domain,
            "summary_short": "",
            "url": f"/results/problem/{slug}/",
            "canonical_books": books,
        })
        existing_slugs.add(slug)
        existing_titles[title_lower] = existing[-1]
        next_num += 1
        created += 1
        print(f"  Created: {slug} ({seed['result_id']})")

    # Write updated data
    all_results = sorted(existing, key=lambda r: r.get("id", ""))
    with open(results_json_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    # Update topics
    topics_path = os.path.join(SITE_DIR, "_data", "results", "topics.json")
    topic_counts = {}
    topic_slugs_map = {}
    for r in all_results:
        t = r.get("topic", "unknown")
        topic_counts[t] = topic_counts.get(t, 0) + 1
        topic_slugs_map.setdefault(t, []).append(r["slug"])

    topics = [{"id": t, "slug": t, "title": t.capitalize(), "count": topic_counts[t],
               "results": sorted(topic_slugs_map[t])} for t in sorted(topic_counts)]
    with open(topics_path, "w", encoding="utf-8") as f:
        json.dump(topics, f, indent=2, ensure_ascii=False)

    # Regenerate browse pages using the upgrade script's functions
    from upgrade_results_v2 import generate_results_index, generate_by_problem, generate_by_domain, generate_topic_pages
    generate_results_index(all_results, topic_counts)
    generate_by_problem(all_results)
    generate_by_domain(all_results, topics)
    generate_topic_pages(all_results, topics)

    # Regenerate by-book page
    from enrich_results_p0p1 import CANONICAL_BOOKS_MAP
    # Also build by-book from the data
    generate_by_book(all_results)

    print(f"\nCreated: {created}, Skipped (existing): {skipped}")
    print(f"Total results: {len(all_results)}")
    for t, c in sorted(topic_counts.items()):
        print(f"  {t}: {c}")


def generate_by_book(results):
    """Regenerate by-book grouped index."""
    import json as _json
    books_path = os.path.join(SITE_DIR, "_data", "publications", "books.json")
    with open(books_path) as f:
        books_data = _json.load(f)
    books_map = {b["roman"]: b for b in books_data}

    by_book = {}
    for r in results:
        for b in r.get("canonical_books", []):
            by_book.setdefault(b, []).append(r)

    lines = ["""---
layout: program-doc
title: Results by Book
permalink: /results/by-book/
lane: results
summary_short: "All """ + str(len(results)) + """ results grouped by their canonical book source across the seven-volume series."
right_rail:
  related:
  - title: Results Overview
    url: /results/
  - title: Results by Problem
    url: /results/by-problem/
  - title: Results by Domain
    url: /results/by-domain/
  meta:
    type: Browse Index
    scope: All results
    status: Canonical
    updated: April 2026
---

## Results by Canonical Book

Results are grouped by the book(s) where their canonical derivation is grounded. Some results appear under multiple books when the argument spans volumes.
"""]

    for roman in ["I", "II", "III", "IV", "V", "VI", "VII"]:
        b = books_map.get(roman, {})
        book_results = sorted(by_book.get(roman, []), key=lambda r: r["title"].lower())
        count = len(book_results)
        lines.append(f"### [Book {roman}: {b.get('title', '')}]({{{{ '/publications/books/{b.get('id', '')}/' | relative_url }}}}) — {count} results")
        lines.append(f"*{b.get('subtitle', '')}* · {b.get('layer', '')} {b.get('layer_name', '')}\n")
        for r in book_results:
            st = STATUS_DISPLAY.get(r.get("status_code", "R"), "")
            kind = r.get("result_kind", "").replace("-", " ").title()
            lines.append(f"- [{r['title']}]({{{{ '{r['url']}' | relative_url }}}}) — *{kind}* · {st}")
        lines.append("")

    path = os.path.join(SITE_DIR, "results", "by-book.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("Wrote results/by-book.md")


if __name__ == "__main__":
    main()
