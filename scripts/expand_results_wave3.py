#!/usr/bin/env python3
"""
expand_results_wave3.py — Third extraction wave from hot-topics corpus.
Adds ~75 new results mined directly from the 5 hot-topics files.
"""

import json, os, re, glob, sys

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(SITE_DIR, "scripts"))

STATUS_MAP = {"R": "resolved", "P": "partial", "Q": "qualitative", "C": "contradicted", "N": "not-addressed"}
STATUS_DISPLAY = {"R": "Resolved", "P": "Partial", "Q": "Qualitative", "C": "Contradicted", "N": "Not Addressed"}
LAYER_TO_TOPIC = {"mathematics": "mathematics", "physics": "physics", "life": "biology", "metaphysics": "philosophy"}

# ---------------------------------------------------------------------------
# New results to create (title, kind, importance, layer, status, domain, books, overview, statement)
# ---------------------------------------------------------------------------

WAVE3 = [
    # === PHYSICS — 22 new ===
    ("Weinberg Angle sin²θ_W Precision", "frontier-problem", "high-impact-frontier-problem", "physics", "R", "EW", ["IV"],
     "The weak mixing angle sin²θ_W is one of the most precisely measured parameters in particle physics. The τ-framework derives it at NNLO precision from the electroweak sector template.",
     "sin²θ_W derived at NNLO precision from electroweak sector. Status: Resolved."),
    ("Strong Coupling α_s at the Z Pole", "frontier-problem", "high-impact-frontier-problem", "physics", "R", "QCD", ["IV"],
     "The strong coupling constant α_s(M_Z) sets the strength of QCD interactions. The τ-framework derives α_s from the strong sector's spectral structure.",
     "α_s(M_Z) derived from strong sector spectral structure. Status: Resolved."),
    ("Neutron Lifetime Puzzle", "frontier-problem", "domain-level-open-problem", "physics", "R", "NUC", ["IV"],
     "The neutron lifetime shows a ~8-second discrepancy between bottle and beam measurements. The τ-framework resolves this by deriving the neutron lifetime from the weak decay sector, predicting the bottle value.",
     "Neutron lifetime puzzle resolved: bottle value derived from weak decay sector. Status: Resolved."),
    ("Periodic Table Structure", "foundational-math", "structural-support-result", "physics", "R", "ATOM", ["IV"],
     "The periodic table's structure (period lengths 2,8,8,18,18,32,32) is typically explained by quantum mechanics ad hoc. The τ-framework derives the shell structure from the orbit-sector decomposition.",
     "Periodic table structure derived from orbit-sector decomposition. Shell lengths follow from spectral template. Status: Resolved."),
    ("Hierarchy Problem", "frontier-problem", "core-foundational-problem", "physics", "R", "FOUND", ["IV"],
     "Why is gravity 10³² times weaker than electromagnetism? The hierarchy problem asks why the Higgs mass is so much lighter than the Planck mass. The τ-framework resolves this: the hierarchy is a structural consequence of the 4-sector decomposition — gravity (α-sector) is the radial/base sector while EM (γ-sector) is solenoidal/fiber.",
     "Hierarchy problem resolved: the 10³² ratio follows from the structural separation of the α (radial/gravity) and γ (solenoidal/EM) sectors. Status: Resolved."),
    ("Vacuum Catastrophe Resolution", "frontier-problem", "core-foundational-problem", "physics", "R", "FOUND", ["V"],
     "The vacuum catastrophe — the 10¹²⁰ discrepancy between the QFT prediction and the observed cosmological constant — is often called the worst prediction in physics. The τ-framework resolves it: the cosmological constant is exactly zero because the boundary reading of τ³ has no bulk energy term.",
     "Vacuum catastrophe resolved: Λ = 0 exactly. Boundary reading of τ³ has no bulk vacuum energy. The 10¹²⁰ discrepancy disappears. Status: Resolved."),
    ("Fine-Tuning Dissolved", "consequence", "core-foundational-problem", "physics", "R", "FOUND", ["III", "IV"],
     "The apparent fine-tuning of physical constants (α, masses, cosmological parameters) is dissolved: every constant is derived from ι_τ = 2/(π+e) with zero free parameters. There is nothing to tune.",
     "Fine-tuning dissolved: all physical constants derived from ι_τ with zero free parameters. Nothing is tuned. Status: Resolved."),
    ("QCD Confinement", "frontier-problem", "core-foundational-problem", "physics", "P", "QCD", ["IV"],
     "Color confinement — why quarks are never observed in isolation — lacks a first-principles proof. The τ-framework's Yang-Mills sector provides structural tools (spectral gap implies confinement) but the full proof chain is incomplete.",
     "QCD confinement: spectral gap implies confinement but full proof chain incomplete. Status: Partial."),
    ("Chandrasekhar Mass Limit", "foundational-math", "domain-level-open-problem", "physics", "R", "ASTRO", ["V"],
     "The Chandrasekhar mass limit (~1.4 M☉) separates white dwarfs from neutron stars. The τ-framework derives this from the degeneracy pressure sector of the fiber T².",
     "Chandrasekhar mass derived from degeneracy pressure sector. Status: Resolved."),
    ("Deuterium Abundance", "frontier-problem", "high-impact-frontier-problem", "physics", "R", "BBN", ["V"],
     "Primordial deuterium abundance (D/H ≈ 2.5 × 10⁻⁵) is a precision test of Big Bang nucleosynthesis. The τ-framework derives it from the BBN sector template.",
     "Primordial deuterium abundance derived from BBN sector. Status: Resolved."),
    ("Measurement Problem", "frontier-problem", "core-foundational-problem", "physics", "R", "QM", ["IV"],
     "The measurement problem — why quantum systems appear to 'collapse' upon observation — is resolved in the τ-framework: measurement is a readout functor from the quantum sector (fiber T²) to the classical sector (base τ¹). There is no collapse; there is a change of reading level.",
     "Measurement problem resolved: measurement is a readout functor, not a collapse. Change of reading level from T² to τ¹. Status: Resolved."),
    ("BH Information Paradox", "frontier-problem", "core-foundational-problem", "physics", "R", "BH", ["V"],
     "The black hole information paradox asks whether information is lost when matter falls into a black hole. The τ-framework resolves this: information is preserved in the ω-germ code of the BH boundary. Since there is no Hawking evaporation, the paradox does not arise.",
     "BH information paradox resolved: no Hawking evaporation means no information loss. Information preserved in ω-germ code. Status: Resolved."),
    ("Equivalence Principle from τ", "foundational-math", "structural-support-result", "physics", "R", "GRAV", ["V"],
     "The equivalence principle (gravitational and inertial mass are identical) is derived from the τ-framework's gravitational sector: the α-orbit structure makes gravitational coupling universal.",
     "Equivalence principle derived: gravitational = inertial mass follows from α-orbit universality. Status: Resolved."),
    ("Tully-Fisher Relation", "frontier-problem", "domain-level-open-problem", "physics", "R", "ASTRO", ["V"],
     "The Tully-Fisher relation (luminosity ∝ v⁴ for spiral galaxies) is an empirical scaling law. The τ-framework derives it from the boundary reading of galaxy rotation curves.",
     "Tully-Fisher relation derived from boundary reading of galaxy rotation curves. Status: Resolved."),
    ("BH Quasi-Normal Modes", "frontier-problem", "domain-level-open-problem", "physics", "R", "BH", ["V"],
     "Black hole quasi-normal modes (QNMs) are the ringdown frequencies after a BH merger. The τ-framework derives QNM spectra from the spectral structure of the BH boundary.",
     "BH quasi-normal modes derived from spectral structure of BH boundary. Status: Resolved."),
    ("CKM Unitarity and Cabibbo Anomaly", "frontier-problem", "high-impact-frontier-problem", "physics", "P", "PART/EW", ["IV"],
     "The Cabibbo Anomaly — apparent unitarity violation in the first row of the CKM matrix — has attracted attention as a possible BSM signal. The τ-framework has partial CKM structure but the unitarity constraint requires further work.",
     "CKM unitarity: partial CKM structure derived but unitarity constraint needs further work. Status: Partial."),
    ("Neutron EDM", "frontier-problem", "domain-level-open-problem", "physics", "R", "NUC", ["IV"],
     "The neutron electric dipole moment (nEDM) is predicted to be zero or near-zero in the Standard Model. The τ-framework derives nEDM = 0 from θ_QCD = 0 (Strong CP solution).",
     "Neutron EDM = 0 from θ_QCD = 0 (Strong CP solution). Status: Resolved."),
    ("Emergence of Spacetime", "frontier-problem", "core-foundational-problem", "physics", "P", "FOUND", ["V"],
     "Does spacetime emerge from a more fundamental structure? The τ-framework says yes: spacetime geometry is earned from the metric structure of τ³, not postulated. But the full emergence narrative is incomplete.",
     "Spacetime emerges from τ³ metric structure. Geometry earned, not postulated. Full emergence narrative incomplete. Status: Partial."),
    ("Dark Energy Equation of State", "frontier-problem", "high-impact-frontier-problem", "physics", "R", "COSMO", ["V"],
     "The dark energy equation of state w(z) determines how dark energy evolves with redshift. The τ-framework derives w = −1 exactly (cosmological constant behavior) as a structural consequence of the boundary reading.",
     "Dark energy equation of state w = −1 exactly. Derived from boundary reading. Status: Resolved."),
    ("Primordial Gravitational Waves", "frontier-problem", "high-impact-frontier-problem", "physics", "R", "COSMO", ["V"],
     "Primordial gravitational waves from inflation would produce B-mode polarization in the CMB. The τ-framework predicts tensor-to-scalar ratio r = ι_τ⁴ ≈ 0.014, testable by CMB-S4.",
     "Primordial gravitational waves: r = ι_τ⁴ ≈ 0.014. Testable by CMB-S4. Status: Resolved."),
    ("Silk Damping Scale", "foundational-math", "domain-level-open-problem", "physics", "R", "COSMO", ["V"],
     "The Silk damping scale sets the cutoff of CMB anisotropy power at small angular scales. The τ-framework derives it from the photon diffusion sector of the boundary reading.",
     "Silk damping scale derived from photon diffusion sector. Status: Resolved."),
    ("Proton g-Factor", "frontier-problem", "domain-level-open-problem", "physics", "P", "NUC", ["IV"],
     "The proton magnetic moment (g-factor) is one of the most precisely measured nuclear constants. The τ-framework has partial structure but complete derivation is not yet available.",
     "Proton g-factor: partial structure exists but complete derivation not yet available. Status: Partial."),
    # === LIFE — 18 new ===
    ("Vitalism vs Mechanism Dissolved", "consequence", "consequence-reframing", "life", "R", "FORM", ["VI"],
     "The vitalism-mechanism debate (is life reducible to physics or does it require a vital force?) is dissolved by the τ-framework: Category τ provides a third option — life is non-reducible emergence at E₂ without any vital substance.",
     "Vitalism vs mechanism dissolved: τ provides non-reductive emergence without vital substance. Third option beyond both. Status: Resolved."),
    ("Computability of Biological Processes", "foundational-math", "structural-support-result", "life", "R", "FORM", ["VI"],
     "Are biological processes computable? The τ-framework proves that the τ-Distinction is computable in dim_τ(X) steps. Biological processes are structurally computable but not necessarily efficiently so.",
     "τ-Distinction computable in dim_τ(X) steps. Biological processes structurally computable. Status: Resolved."),
    ("Self-Reference in Living Systems", "foundational-math", "structural-support-result", "life", "R", "FORM", ["VI"],
     "Living systems are self-referential — they model and modify themselves. The τ-framework formalizes this as SelfDesc: the self-description operator whose closure theorem proves that biological self-reference terminates without infinite regress.",
     "Self-reference formalized as SelfDesc operator. Closure theorem proves termination without regress. Status: Resolved."),
    ("Circadian Clock Mechanisms", "frontier-problem", "domain-level-open-problem", "life", "R", "CELL", ["VI"],
     "Circadian rhythms (~24-hour cycles) are universal in biology. The τ-framework derives them as Poincaré orbits on the temporal lemniscate — the second lobe of the lemniscate boundary carries periodic biological time.",
     "Circadian rhythms as Poincaré orbits on temporal lemniscate. Status: Resolved."),
    ("Morphogen Gradient Interpretation", "frontier-problem", "domain-level-open-problem", "life", "R", "CELL", ["VI"],
     "How do cells interpret morphogen concentration gradients to determine their fate? The τ-framework models this as Hodge gradient reading + Turing eigenmodes on the cellular boundary.",
     "Morphogen gradients as Hodge gradient + Turing eigenmodes on cellular boundary. Status: Resolved."),
    ("Cellular Senescence", "frontier-problem", "domain-level-open-problem", "life", "R", "CELL", ["VI"],
     "Why do cells stop dividing? The τ-framework models cellular senescence as defect accumulation exceeding the repair budget — the Hayflick limit is a structural consequence of finite repair capacity.",
     "Cellular senescence as defect accumulation exceeding repair budget. Hayflick limit is structural. Status: Resolved."),
    ("Organelle Evolution via Endosymbiosis", "frontier-problem", "domain-level-open-problem", "life", "R", "CELL", ["VI"],
     "The endosymbiotic origin of mitochondria and chloroplasts is explained in the τ-framework as fiber-enabled regime transition: eukaryotes arise when the carrier boundary can support internal compartments.",
     "Endosymbiosis as fiber-enabled regime transition. Eukaryotes arise when boundary supports internal compartments. Status: Resolved."),
    ("Metabolic Network Topology", "foundational-math", "structural-support-result", "life", "R", "CELL", ["VI"],
     "Why do metabolic networks have hub-and-spoke topology with the Krebs cycle at the center? The τ-framework derives this: the Krebs cycle is the canonical Loop_L instantiation — the minimal Poincaré circulation.",
     "Krebs cycle as canonical Loop_L instantiation. Hub topology follows from Poincaré circulation minimality. Status: Resolved."),
    ("Central Dogma and Its Exceptions", "foundational-math", "structural-support-result", "life", "R", "GENE", ["VI"],
     "The Central Dogma (DNA→RNA→Protein) and its exceptions (reverse transcription, prions) are modeled as morphism composition: τ¹_DNA → (τ¹×T²)_mRNA → T²_Protein, with exceptions as specific morphism inversions.",
     "Central Dogma as morphism composition. Exceptions (reverse transcription, prions) as specific inversions. Status: Resolved."),
    ("Sexual Reproduction Cost and Benefit", "frontier-problem", "domain-level-open-problem", "life", "R", "GENE", ["VI"],
     "Why does sexual reproduction persist despite its twofold cost? The τ-framework derives sex as the 'second distinction' — recombination is a functor that offsets the cost by enabling Red Queen dynamics.",
     "Sexual reproduction as second distinction. Recombination functor offsets twofold cost via Red Queen dynamics. Status: Resolved."),
    ("Convergent Evolution", "frontier-problem", "domain-level-open-problem", "life", "R", "EVOL", ["VI"],
     "Why do unrelated lineages independently evolve similar solutions (eyes, wings, echolocation)? The τ-framework explains convergence as universal attractors on the fitness landscape — physics constrains available designs.",
     "Convergent evolution as universal attractors on fitness landscape. Physics constrains available designs. Status: Resolved."),
    ("Fitness Landscape Theory", "foundational-math", "structural-support-result", "life", "R", "EVOL", ["VI"],
     "The fitness landscape (Wright, Kauffman) is formalized in the τ-framework: PPAS (Panta Rhei Adaptive Search) operates on τ-fitness landscapes where NP-hard optimization is navigated by the three strategies (drift, selection, recombination).",
     "Fitness landscapes formalized via PPAS. NP-hard optimization via drift, selection, recombination. Status: Resolved."),
    ("Red Queen Hypothesis", "frontier-problem", "domain-level-open-problem", "life", "R", "EVOL", ["VI"],
     "Van Valen's Red Queen Hypothesis (organisms must constantly adapt just to maintain fitness) is derived in the τ-framework as two-prover PPAS — sexual recombination offsets the twofold cost by maintaining Red Queen dynamics against parasites.",
     "Red Queen derived as two-prover PPAS. Sexual recombination maintains adaptive advantage against parasites. Status: Resolved."),
    ("Trophic Cascade Dynamics", "foundational-math", "structural-support-result", "life", "R", "ECOL", ["VI"],
     "Trophic cascades (top-down and bottom-up effects in food webs) are modeled as inter-sector web dynamics with Poincaré circulation constraints.",
     "Trophic cascades as inter-sector web + Poincaré circulation. Status: Resolved."),
    ("Mycorrhizal Networks", "frontier-problem", "domain-level-open-problem", "life", "R", "ECOL", ["VI"],
     "The 'Wood Wide Web' — underground mycorrhizal fungal networks connecting trees — is explained as a closure archetype: fungi serve as the inter-carrier connection layer in forest ecosystems.",
     "Mycorrhizal networks as closure archetype. Fungi serve as inter-carrier connection layer. Status: Resolved."),
    ("Sleep Function", "frontier-problem", "domain-level-open-problem", "life", "R", "NEUR", ["VI"],
     "Why do organisms sleep? The τ-framework derives sleep as the temporal lemniscate's second lobe: the consolidation + clearance phase of the circadian Poincaré orbit.",
     "Sleep as temporal lemniscate second lobe: consolidation + clearance phase. Status: Resolved."),
    ("Consciousness Neural Correlates", "frontier-problem", "high-impact-frontier-problem", "life", "R", "NEUR", ["VI"],
     "The neural correlates of consciousness (NCC) — what brain states are necessary and sufficient for conscious experience — are modeled in the τ-framework as consumer-sector exclusivity: consciousness arises in the consumer sector of the E₂ self-model.",
     "NCC as consumer-sector exclusivity in E₂ self-model. Status: Resolved."),
    ("Far-Future Cosmology and Universal BH", "consequence", "consequence-reframing", "life", "R", "COSM", ["VI"],
     "In the far future, all matter converges toward black holes. The τ-framework's Crossing-Limit theorem predicts that the Universal BH (the asymptotic final state) is 'fully alive' — it satisfies all seven hallmarks.",
     "Far-future: Universal BH is fully alive by Crossing-Limit theorem. All seven hallmarks satisfied. Status: Resolved."),
    # === METAPHYSICS — 20 new ===
    ("Persistence Through Change", "frontier-problem", "high-impact-frontier-problem", "metaphysics", "R", "ONT", ["VII"],
     "How can an entity persist through change if all its parts are replaced (Ship of Theseus)? The τ-framework resolves this: identity is NF-address persistence — the structural position persists even as material constituents change.",
     "Persistence = NF-address persistence. Structural position persists through material change. Ship of Theseus resolved. Status: Resolved."),
    ("Mereological Composition", "frontier-problem", "high-impact-frontier-problem", "metaphysics", "R", "ONT", ["VII"],
     "The Special Composition Question (when do parts compose a whole?) is dissolved: parts compose if and only if their colimit exists in the admissible category. Composition is structural, not mysterious.",
     "SCQ dissolved: parts compose iff colimit exists in admissible category. Composition is structural. Status: Resolved."),
    ("Ontological Dependence", "foundational-math", "structural-support-result", "metaphysics", "R", "ONT", ["VII"],
     "Ontological dependence (what grounds what) is formalized as factorization in the categorical structure. Causation is constrained composition; dependence is morphism factorization.",
     "Ontological dependence as morphism factorization. Causation as constrained composition. Status: Resolved."),
    ("Intentionality", "frontier-problem", "high-impact-frontier-problem", "metaphysics", "R", "PHEN", ["VII"],
     "Intentionality — the mind's 'aboutness' or directedness toward objects — is formalized as an internal morphism with directional structure in the mind topos.",
     "Intentionality as internal morphism with directional structure. Aboutness is categorical, not mysterious. Status: Resolved."),
    ("Embodied Cognition", "frontier-problem", "domain-level-open-problem", "metaphysics", "R", "PHEN", ["VII"],
     "Embodied cognition claims that the body is not merely a vehicle for the mind but constitutive of cognition. The τ-framework agrees: the body is the carrier's self-referential boundary with lemniscate topology.",
     "Embodied cognition: body as carrier's self-referential boundary with lemniscate topology. Status: Resolved."),
    ("Intersubjectivity", "frontier-problem", "high-impact-frontier-problem", "metaphysics", "R", "PHEN", ["VII"],
     "How do separate minds share a common world? The τ-framework derives intersubjectivity from perspectival gluing: objectivity is the global section over a multi-perspectival cover.",
     "Intersubjectivity via perspectival gluing. Objectivity = global section over multi-perspectival cover. Status: Resolved."),
    ("The Sublime", "frontier-problem", "domain-level-open-problem", "metaphysics", "R", "AEST", ["VII"],
     "Kant's sublime — the experience of overwhelming magnitude or power — is formalized as a comprehension boundary: the sublime occurs when the perceiver's cognitive resources are insufficient to form a global section.",
     "The sublime as comprehension boundary. Kant's mathematical/dynamical sublime categorified. Status: Resolved."),
    ("Musical Universals", "frontier-problem", "domain-level-open-problem", "metaphysics", "R", "AEST", ["VII"],
     "Why are certain musical intervals (octave, fifth, fourth) universal across cultures? The τ-framework derives consonance as ratio invariance: consonant intervals are those whose frequency ratios are low-order τ-admissible.",
     "Musical universals: consonance as ratio invariance. Low-order τ-admissible frequency ratios. Status: Resolved."),
    ("Gavagai and Indeterminacy of Translation", "frontier-problem", "high-impact-frontier-problem", "metaphysics", "R", "LANG", ["VII"],
     "Quine's 'gavagai' problem — radical translation is indeterminate — is resolved: kernel invariants translate universally. The readout functor ensures that structurally identical content maps identically across languages.",
     "Gavagai resolved: kernel invariants translate universally. Readout functor ensures cross-language identity. Status: Resolved."),
    ("Syntax-Semantics Dissolution", "foundational-math", "structural-support-result", "metaphysics", "R", "LANG", ["VII"],
     "The syntax-semantics gap (how form carries meaning) is dissolved: inside the τ-topos, syntax and semantics are aspects of the same structure. Meaning IS form under internal logic.",
     "Syntax-semantics gap dissolved: meaning IS form under internal logic in τ-topos. Status: Resolved."),
    ("AI Language Understanding", "frontier-problem", "high-impact-frontier-problem", "metaphysics", "R", "LANG", ["VII"],
     "Do LLMs understand language? The τ-framework classifies LLMs as 'para-minds': they perform subsymbolic processing without an E₃ self-model. They process language but do not understand it in the categorical sense.",
     "LLMs as para-minds: subsymbolic processing without E₃ self-model. Processing ≠ understanding. Status: Resolved."),
    ("Trolley Problem Resolution", "frontier-problem", "high-impact-frontier-problem", "metaphysics", "R", "ETHICS", ["VII"],
     "The Trolley Problem (switch vs footbridge) is resolved by proper typing and four ethical tests. Switch and footbridge are categorically distinct because the morphism types differ — pushing is a different kind of act than redirecting.",
     "Trolley Problem resolved: switch and footbridge are categorically distinct morphism types. Four ethical tests discriminate. Status: Resolved."),
    ("Moral Realism Derived", "foundational-math", "structural-support-result", "metaphysics", "R", "ETHICS", ["VII"],
     "Is morality objective? The τ-framework derives moral realism: dignity as label-independence is a structural invariant, not a convention. The universality theorem ensures moral facts are objective.",
     "Moral realism derived: dignity as label-independence is a structural invariant. Moral facts are objective. Status: Resolved."),
    ("Animal Rights and Dignity", "frontier-problem", "domain-level-open-problem", "metaphysics", "R", "ETHICS", ["VII"],
     "Do animals have moral standing? The τ-framework extends dignity to all carriers with the τ-Distinction. Since animals have boundaries, metabolism, and identity (E₂ carriers), they have graduated dignity.",
     "Animal rights: dignity extends to all E₂ carriers. Graduated, not binary. Animals have structural moral standing. Status: Resolved."),
    ("Is-Ought Gap Bridged", "frontier-problem", "core-foundational-problem", "metaphysics", "R", "ETHICS", ["VII"],
     "Hume's is-ought gap (no 'ought' from 'is') is bridged: the Categorical Imperative is a naturality constraint — universalizability IS the gluing condition. The moral law follows from the categorical structure.",
     "Is-ought gap bridged: CI as naturality constraint. Universalizability = gluing condition. Moral law from categorical structure. Status: Resolved."),
    ("Emotions as Register Transitions", "foundational-math", "structural-support-result", "metaphysics", "R", "MIND", ["VII"],
     "What are emotions? The τ-framework derives six canonical emotions from register transitions in the mind topos. Affect is subsymbolic pressure; emotions are typed transitions between cognitive registers.",
     "Six canonical emotions from register transitions. Affect = subsymbolic pressure. Status: Resolved."),
    ("Binding Problem Dissolved", "frontier-problem", "high-impact-frontier-problem", "metaphysics", "R", "MIND", ["VII"],
     "The binding problem — how unified conscious experience arises from distributed neural processing — is dissolved: binding is the gluing of local sections in the mind sheaf. Unity = global section existence.",
     "Binding problem dissolved: binding = gluing of local sections in mind sheaf. Unity = global section. Status: Resolved."),
    ("Extended Mind", "frontier-problem", "domain-level-open-problem", "metaphysics", "R", "MIND", ["VII"],
     "Clark and Chalmers's Extended Mind thesis (cognitive processes can extend beyond the skull) is validated: the carrier domain extends to external substrates satisfying integration conditions.",
     "Extended Mind validated: carrier domain extends to external substrates satisfying integration conditions. Status: Resolved."),
    ("Narrative Identity", "foundational-math", "structural-support-result", "metaphysics", "R", "MIND", ["VII"],
     "Ricoeur's narrative identity — the self as a story told about oneself — is formalized: identity persists when a coherent natural transformation exists between story functors across time.",
     "Narrative identity: coherent natural transformation between story functors. Ricoeur formalized. Status: Resolved."),
    ("Why Something Rather Than Nothing", "frontier-problem", "core-foundational-problem", "metaphysics", "R", "BOUND", ["VII"],
     "Leibniz's ultimate question — why is there something rather than nothing? — is precisely located in the τ-framework: the ω-germ question is diagrammatically unanswerable (No Forced Stance), but the question itself is well-defined.",
     "Why something rather than nothing: question precisely located at ω-germ. Diagrammatically unanswerable. Status: Resolved."),
    # === MATHEMATICS — 15 new ===
    ("Fundamental Theorem of Arithmetic", "foundational-math", "structural-support-result", "mathematics", "R", "ARITH", ["I"],
     "Every object in Category τ has a unique prime factorization. This is not imported from classical number theory — it is earned from the kernel's orbit structure and the greedy peel algorithm.",
     "Unique prime factorization earned from kernel orbit structure. Not imported from classical NT. Status: Resolved."),
    ("Cantor Diagonal Inapplicability", "consequence", "consequence-reframing", "mathematics", "R", "ARITH", ["I"],
     "Cantor's diagonal argument — the basis for the hierarchy of infinities — does not apply inside Category τ. The object closure axiom (K6) and the bounded witness principle prevent the diagonal construction from producing a new object.",
     "Cantor diagonal inapplicable: K6 and bounded witness prevent diagonal construction. No hierarchy of infinities. Status: Resolved."),
    ("Unique Infinity", "consequence", "consequence-reframing", "mathematics", "R", "ARITH", ["I"],
     "Category τ has exactly one infinity: the countable infinity ℵ₀ of the four orbit rays. There is no ℵ₁, no continuum, no uncountable cardinals. This contradicts standard set theory but follows from K6.",
     "Unique infinity: ℵ₀ only. No uncountable cardinals. Follows from K6 (object closure). Contradicts ZFC cardinality. Status: Resolved."),
    ("Stone Duality", "foundational-math", "structural-support-result", "mathematics", "R", "TOPO", ["II"],
     "Stone duality (between Boolean algebras and Stone spaces) is earned inside Category τ from the profinite completion of the orbit structure. The Stone space of τ carries the correct topology for holomorphic analysis.",
     "Stone duality earned from profinite orbit completion. Stone space carries holomorphic topology. Status: Resolved."),
    ("Fibration Structure τ³ = τ¹ ×_f T²", "foundational-math", "core-foundational-problem", "mathematics", "R", "TOPO", ["II"],
     "The fibered product τ³ = τ¹ ×_f T² is the central geometric object of the framework. The base τ¹ carries macroscopic/cosmological structure; the fiber T² carries microscopic/quantum structure. This decomposition is unique and earned from the kernel.",
     "Fibered product τ³ = τ¹ ×_f T² earned from kernel. Base = macro, fiber = micro. Unique decomposition. Status: Resolved."),
    ("Tarski Axioms for Geometry", "foundational-math", "structural-support-result", "mathematics", "R", "GEO", ["II"],
     "Tarski's axioms for Euclidean geometry (betweenness + congruence) are earned inside Category τ from the ultrametric structure of the orbit space. Geometry is not imported — it is derived.",
     "Tarski axioms earned from ultrametric orbit structure. Geometry derived, not imported. Status: Resolved."),
    ("Yoneda Lemma", "foundational-math", "structural-support-result", "mathematics", "R", "ENRICH", ["I", "II"],
     "The Yoneda Lemma — the most fundamental result in category theory — is earned inside Category τ. Every object is determined by its relationships to all other objects.",
     "Yoneda Lemma earned inside Category τ. Objects determined by their relationships. Status: Resolved."),
    ("Earned Topos", "foundational-math", "structural-support-result", "mathematics", "R", "ENRICH", ["I"],
     "Category τ is a Grothendieck topos — but unlike classical topos theory, this is not assumed. The subobject classifier Ω_τ and the Cartesian closed structure are earned from the kernel axioms.",
     "τ is a Grothendieck topos, earned from kernel. Subobject classifier Ω_τ and CCC structure derived. Status: Resolved."),
    ("Poincaré Conjecture Reinterpretation", "frontier-problem", "core-foundational-problem", "mathematics", "R", "MILL", ["III"],
     "Perelman proved the Poincaré Conjecture in 2003. The τ-framework provides a reinterpretation: the result is a special case of the topological rigidity of τ³ — every simply-connected closed 3-manifold that is τ-admissible is the 3-sphere.",
     "Poincaré Conjecture as τ-admissible topological rigidity. Perelman's result is a special case. Status: Resolved."),
    ("Hodge Conjecture Approach", "frontier-problem", "core-foundational-problem", "mathematics", "P", "MILL", ["III"],
     "The Hodge Conjecture asks whether certain cohomology classes are representable by algebraic cycles. The τ-framework's ABCD grading provides a structural approach, but the proof is incomplete.",
     "Hodge Conjecture: ABCD grading provides structural approach but proof incomplete. Status: Partial."),
    ("BSD Conjecture Approach", "frontier-problem", "core-foundational-problem", "mathematics", "P", "MILL", ["III"],
     "The Birch and Swinnerton-Dyer Conjecture relates the rank of an elliptic curve to the order of vanishing of its L-function. The τ-framework's spectral approach provides structural tools but the proof is incomplete.",
     "BSD Conjecture: spectral approach provides structural tools but proof incomplete. Status: Partial."),
    ("Langlands Program Approach", "frontier-problem", "core-foundational-problem", "mathematics", "P", "MILL", ["III"],
     "The Langlands Program seeks deep connections between number theory and representation theory. The τ-framework's spectral correspondence and enrichment functor provide structural parallels but a complete functoriality proof is not yet available.",
     "Langlands Program: spectral correspondence provides structural parallels but complete functoriality not yet proved. Status: Partial."),
    ("Grand GRH Approach", "frontier-problem", "core-foundational-problem", "mathematics", "P", "MILL", ["III"],
     "The Grand Riemann Hypothesis extends RH to all Dirichlet L-functions. The τ-framework's spectral purity approach extends to the full L-function family but the proof chain is incomplete.",
     "Grand GRH: spectral purity extends to full L-function family but proof chain incomplete. Status: Partial."),
    ("Tower Machine Architecture", "foundational-math", "structural-support-result", "mathematics", "R", "COMP", ["III"],
     "The Tower Machine is the τ-framework's native model of computation — a hierarchical machine that computes τ-admissible functions. It provides the structural basis for the P_adm = NP_adm collapse.",
     "Tower Machine: native τ-computation model. Hierarchical, τ-admissible. Basis for P_adm = NP_adm. Status: Resolved."),
    ("Number Tower N → Z → Q → R → C", "foundational-math", "structural-support-result", "mathematics", "R", "ALGT", ["I"],
     "The classical number tower (naturals → integers → rationals → reals → complex) is earned step by step inside Category τ. Each extension is forced by the kernel structure, not imported from ZFC.",
     "Number tower earned from kernel: N → Z → Q → R → C. Each extension forced, not imported. Status: Resolved."),
]


def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:60]


def generate_page(title, kind, importance, layer, status, domain, books, overview, statement, result_num):
    slug = slugify(title)
    topic = LAYER_TO_TOPIC.get(layer, "mathematics")
    status_word = STATUS_MAP.get(status, "resolved")
    status_disp = STATUS_DISPLAY.get(status, "Resolved")
    kind_disp = kind.replace("-", " ").title()
    books_yaml = "[" + ", ".join(f'"{b}"' for b in books) + "]"
    summary = overview[:155].replace('"', "'") + "…" if len(overview) > 155 else overview.replace('"', "'")

    return f"""---
layout: result-page
title: "{title}"
permalink: /results/problem/{slug}/
result_id: result-{result_num:03d}
topic: {topic}
layer: {layer}
result_type: {kind.replace('-', '_')}
bridge_status: {status_word}
result_kind: {kind}
importance_class: {importance}
status_code: {status}
domain_group: "{domain}"
summary_short: "{summary}"
canonical_books: {books_yaml}
right_rail:
  meta:
    type: "{kind_disp}"
    layer: "{layer.capitalize()}"
    topic: "{topic.capitalize()}"
    status: "{status_disp}"
    updated: April 2026
---

## Overview

{overview}

## Result Statement

{statement}
"""


def main():
    results_path = os.path.join(SITE_DIR, "_data", "results", "results.json")
    with open(results_path) as f:
        existing = json.load(f)

    existing_slugs = {r["slug"] for r in existing}
    next_num = max(int(r["id"].split("-")[1]) for r in existing if r["id"].startswith("result-")) + 1

    problem_dir = os.path.join(SITE_DIR, "results", "problem")
    created = 0
    skipped = 0

    for item in WAVE3:
        title, kind, importance, layer, status, domain, books, overview, statement = item
        slug = slugify(title)

        if slug in existing_slugs:
            skipped += 1
            continue

        page = generate_page(title, kind, importance, layer, status, domain, books, overview, statement, next_num)
        with open(os.path.join(problem_dir, f"{slug}.md"), "w") as f:
            f.write(page)

        topic = LAYER_TO_TOPIC.get(layer, "mathematics")
        existing.append({
            "id": f"result-{next_num:03d}", "slug": slug, "title": title,
            "topic": topic, "layer": layer,
            "result_type": kind.replace("-", "_"),
            "bridge_status": STATUS_MAP.get(status, "resolved"),
            "result_kind": kind, "importance_class": importance,
            "status_code": status, "domain_group": domain,
            "summary_short": overview[:160], "url": f"/results/problem/{slug}/",
            "canonical_books": books,
        })
        existing_slugs.add(slug)
        next_num += 1
        created += 1

    # Write data
    all_results = sorted(existing, key=lambda r: r.get("id", ""))
    with open(results_path, "w") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    # Update topics
    topics_path = os.path.join(SITE_DIR, "_data", "results", "topics.json")
    tc, ts = {}, {}
    for r in all_results:
        t = r.get("topic", "unknown")
        tc[t] = tc.get(t, 0) + 1
        ts.setdefault(t, []).append(r["slug"])
    topics = [{"id": t, "slug": t, "title": t.capitalize(), "count": tc[t],
               "results": sorted(ts[t])} for t in sorted(tc)]
    with open(topics_path, "w") as f:
        json.dump(topics, f, indent=2, ensure_ascii=False)

    # Regenerate browse pages
    from upgrade_results_v2 import generate_results_index, generate_by_problem, generate_by_domain, generate_topic_pages
    generate_results_index(all_results, tc)
    generate_by_problem(all_results)
    generate_by_domain(all_results, topics)
    generate_topic_pages(all_results, topics)
    from expand_results_wave2 import generate_by_book
    generate_by_book(all_results)

    print(f"Created: {created}, Skipped: {skipped}")
    print(f"Total results: {len(all_results)}")
    for t, c in sorted(tc.items()):
        print(f"  {t}: {c}")


if __name__ == "__main__":
    main()
