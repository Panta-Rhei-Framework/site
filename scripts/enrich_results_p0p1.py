#!/usr/bin/env python3
"""
enrich_results_p0p1.py — Enrich 13 stub result pages with manuscript content
and map canonical_books on all 85 results.

P0.2: Write real Overview/Detail/Result Statement for 13 stubs.
P1.2: Populate canonical_books arrays on all results.

Usage:
  python3 scripts/enrich_results_p0p1.py
"""

import json
import os
import re
import glob

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# P0.2: Enriched content for 13 stub result pages
# ---------------------------------------------------------------------------

ENRICHED_CONTENT = {
    "riemann-hypothesis-spectral-approach": """
## Overview

The Riemann Hypothesis (RH) asks whether all non-trivial zeros of the Riemann zeta function lie on the critical line Re(s) = 1/2. It is one of the seven Millennium Prize Problems and the most important unsolved problem in analytic number theory.

The Panta Rhei framework approaches RH through the spectral correspondence developed in Book III, Parts 4-5. The zeros of the zeta function are mapped to eigenvalues of a self-adjoint operator H_L on the lemniscate boundary. Self-adjointness forces eigenvalues to be real, and this reality condition constrains the location of zeros to the critical line.

## Why It Is Hard

RH has resisted proof for over 160 years despite deep connections to prime distribution, random matrix theory, and quantum chaos. No known approach has produced a complete proof. The Hilbert-Pólya conjecture (that zeros correspond to eigenvalues of a self-adjoint operator) remains the most promising strategy but has never been realized concretely.

## Panta Rhei Stance

The framework provides a *structural* spectral correspondence (III.T-series) that maps zeta zeros to eigenvalues of H_L, the Hamiltonian on the lemniscate boundary L = S¹ ∨ S¹. The K5 diagonal discipline forbids off-diagonal mixing in H_L, and this propagates through the spectral correspondence to constrain zero locations. The balance between B-sector and C-sector contributions is enforced by bipolar symmetry from Book I's prime polarity.

**Status: Partial.** The spectral correspondence is structurally grounded but the full proof chain from τ-spectral theory to classical RH is not yet complete. The approach is typed as partial, not claimed as a full resolution.

## Result Statement

The τ-spectral approach to the Riemann Hypothesis provides a concrete realization of the Hilbert-Pólya strategy via the operator H_L on the lemniscate boundary, with self-adjointness enforced by the kernel's diagonal discipline (K5). The approach is structurally motivated but remains partial (status P).
""",

    "what-is-life": """
## Overview

"What is life?" is one of the oldest and most persistent questions in science and philosophy. Every classical definition — Aristotle's soul, Schrödinger's negentropy, NASA's "self-sustaining chemical system capable of Darwinian evolution" — captures a necessary condition but none is sufficient. Fire metabolizes. Mules don't reproduce. Crystals grow. Computers process information.

Book VI provides a categorical definition of life from which seven empirical hallmarks follow as theorems, not axioms.

## Why It Is Hard

The difficulty is twofold: (1) life resists extensional definition because every candidate criterion admits counterexamples (viruses evolve but aren't self-sustaining; fire is self-sustaining but not alive), and (2) no framework has unified the disparate hallmarks (metabolism, reproduction, homeostasis, growth, response, adaptation, organization) into a single structural principle from which all seven follow.

## Panta Rhei Stance

Life is defined as a τ-Distinction carrier: an object in E₂ (the life enrichment layer) that maintains a boundary (the lemniscate L = S¹ ∨ S¹ realized as a lipid bilayer membrane), sustains Poincaré circulation (metabolism), and preserves a normal-form address across time (identity). The seven hallmarks — metabolism, reproduction, homeostasis, growth, response to stimuli, adaptation, and cellular organization — are derived as theorems from this single categorical definition (VI.T-series).

The definition is not a list of properties but a structural characterization: life is what happens when the τ-Distinction is physically instantiated at E₂.

## Result Statement

Life is categorically defined as a τ-Distinction carrier at enrichment level E₂. Seven empirical hallmarks follow as theorems. The definition resolves the extensional problem: viruses fail (no autonomous boundary), fire fails (no normal-form persistence), crystals fail (no Poincaré circulation). Status: Resolved.
""",

    "membrane-first-vs-metabolism-first": """
## Overview

The origin of life debates have long been polarized between "membrane-first" and "metabolism-first" hypotheses. The membrane-first camp argues that compartmentalization was the essential first step; the metabolism-first camp argues that autocatalytic chemical cycles preceded enclosure.

## Why It Is Hard

Both camps have empirical support and neither can explain how its preferred first step could function without the other. Membranes without internal chemistry are empty vesicles. Metabolism without compartmentalization dissipates into the environment. The debate has persisted for decades without resolution.

## Panta Rhei Stance

The framework dissolves the dichotomy. The τ-Distinction requires *both* simultaneously: a boundary (membrane, realizing L = S¹ ∨ S¹) and circulation (metabolism, realizing Poincaré recurrence on τ³). Neither is "first" — they are two aspects of the same categorical structure. The lipid bilayer is the physical carrier of the lemniscate boundary (Book VI, Chapter 21), and metabolism is Poincaré circulation at biological scale (Book VI, Chapter 19). The two co-emerge because the τ-Distinction is a single structural object, not a conjunction of independent properties.

Amphiphilic molecules spontaneously form bilayers without external templates, so the boundary self-assembles. Once enclosed, thermodynamic gradients across the membrane drive the first metabolic cycles. The framework predicts that compartmentalization and metabolism are structurally inseparable.

## Result Statement

The membrane-first vs metabolism-first debate is dissolved: the τ-Distinction requires boundary and circulation simultaneously. Neither is prior. They co-emerge as two aspects of the same categorical structure at E₂. Status: Resolved.
""",

    "cell-as-tau-object": """
## Overview

The cell is the fundamental unit of life. Every living organism is either a single cell or composed of cells. But what *is* a cell, structurally? The framework provides a precise answer: a cell is a τ-object at enrichment level E₂ — a concrete instantiation of the τ-Distinction in physical matter.

## Why It Matters

If the categorical definition of life (τ-Distinction carrier) is correct, then cells should exhibit all the structural features predicted by the framework: a lemniscate boundary (lipid bilayer), Poincaré circulation (metabolism), normal-form address persistence (identity), and the four molecular families mapping to the four orbit sectors.

## Panta Rhei Stance

Book VI maps the cell's structure onto τ³:
- The **lipid bilayer membrane** realizes L = S¹ ∨ S¹ (the lemniscate boundary) — inside vs outside is self vs non-self
- **Metabolism** (catabolism + anabolism) realizes Poincaré circulation on the compactified τ³
- The **four molecular families** (proteins, lipids, carbohydrates, nucleic acids) map to the four orbit sectors (α, π, γ, η)
- **Protein folding** is recast as Yang-Mills-type energy minimization on the fiber T²
- **ATP** serves as the universal energy currency because it is the unique molecule satisfying the τ-circulation constraint

The cell is not merely *analogous* to a τ-object — it *is* one, in the precise sense that its structural organization satisfies the categorical definition.

## Result Statement

The cell is a τ-object at E₂: its membrane realizes L, its metabolism realizes Poincaré circulation, its four molecular families map to the four orbit sectors. This is a structural identification, not an analogy. Status: Resolved.
""",

    "panpsychism-excluded": """
## Overview

Panpsychism — the view that consciousness or proto-consciousness is a fundamental feature of all matter — has experienced a revival in contemporary philosophy of mind, championed by Chalmers, Strawson, and Tononi (via Integrated Information Theory). It offers an elegant response to the Hard Problem by dissolving the emergence gap.

## Why It Matters

If consciousness is fundamental to all matter, then the combination problem replaces the hard problem: how do micro-experiences combine into unified macro-experience? The framework must take a clear position on whether consciousness is layer-specific (E₃ only) or universal.

## Panta Rhei Stance

The framework **excludes** panpsychism. Consciousness arises at enrichment level E₃ (metaphysics) as a global section of the mind sheaf — it requires the full E₀ → E₁ → E₂ → E₃ enrichment ladder. Objects at E₀ (mathematical) or E₁ (physical) do not and cannot instantiate consciousness because they lack the structural prerequisites: E₂-level self-distinction (life) and E₃-level self-modeling.

An electron has no boundary (no τ-Distinction), no Poincaré circulation (no metabolism), no normal-form persistence (no identity in the biological sense). It cannot carry consciousness because consciousness requires the full enrichment stack.

This is a **contradiction** with panpsychism, flagged honestly. The framework predicts consciousness is layer-specific, not universal.

## Result Statement

Panpsychism is structurally excluded: consciousness requires E₃-level self-modeling, which presupposes E₂ (life) and E₁ (physics). Objects below E₃ cannot carry consciousness. This contradicts panpsychism and IIT's substrate-independence claim. Status: Contradicted (C) — the framework's prediction contradicts a mainstream philosophical position.
""",

    "problem-of-universals": """
## Overview

The Problem of Universals — how abstract properties (redness, triangularity, justice) relate to concrete particulars — has been debated since Plato. Realists hold that universals exist independently; nominalists deny their existence; moderate realists seek middle ground. None has achieved consensus.

## Why It Is Hard

The problem resists solution because both extremes face devastating objections. Platonism posits a separate realm of forms but cannot explain how particulars "participate" in them (the Third Man argument). Nominalism avoids ontological bloat but cannot explain why disparate particulars share properties or why laws of nature hold.

## Panta Rhei Stance

The framework dissolves the problem through relational ontology (Book VII, Part II). In Category τ, there are no "bare particulars" and no "free-standing universals." Every object is a structural position in the fibered product τ³ — its properties are determined by its normal-form address and its relations to other objects.

Laws of nature are not relations between universals (Armstrong-Dretske-Tooley) nor mere regularities (Hume). They are τ-admissible continuation operators — structural features of the coherence kernel that determine which extensions of a given configuration are possible. The gap between universals and particulars is eliminated: both are aspects of the same relational structure.

This is a non-dualistic Platonism: structures are mind-independent and observer-independent (Platonic intuition preserved), but they are not inhabitants of a separate realm (Platonic ontology abandoned).

## Result Statement

The Problem of Universals is dissolved through relational ontology: universals and particulars are both structural positions in τ³. Laws are τ-admissible continuation operators, not relations between universals. The framework delivers non-dualistic Platonism. Status: Resolved.
""",

    "substance-vs-process-ontology": """
## Overview

Western metaphysics has been dominated by substance ontology since Aristotle: reality consists of enduring things (substances) that undergo change (accidents). Process philosophy (Whitehead, Rescher) offers an alternative: reality consists of processes, and things are stable patterns in process.

## Why It Is Hard

Substance ontology struggles with quantum mechanics (particles are excitations of fields, not enduring things), relativity (no preferred time-slice), and biology (organisms constantly replace their material constituents). But process ontology lacks the formal precision needed to ground physics and mathematics.

## Panta Rhei Stance

Category τ is inherently processual. The sole operator ρ (progression) generates all objects through iteration — objects are stabilized patterns in the ρ-orbit structure, not pre-given substances. The name "Panta Rhei" (everything flows) is not a metaphor but a structural description.

Book VII, Part II derives this explicitly: relations precede relata. Objects in τ are individuated by their normal-form addresses (structural positions), not by underlying substance. Personal identity, physical particles, and mathematical objects are all patterns in the relational web of τ³.

The framework thus provides what process philosophy lacked: a formally precise, axiomatically grounded process ontology that can underwrite mathematics, physics, biology, and metaphysics.

## Result Statement

Substance ontology is replaced by relational/process ontology: objects are stabilized patterns in ρ-orbits, individuated by normal-form addresses. Relations precede relata. The framework provides formal precision that classical process philosophy lacked. Status: Resolved.
""",

    "gettier-problem": """
## Overview

In 1963, Edmund Gettier published a three-page paper that destabilized epistemology. He showed that justified true belief (JTB) — the classical analysis of knowledge since Plato's *Theaetetus* — is insufficient: cases exist where a subject has justified true belief that intuitively fails to constitute knowledge. Decades of attempted repairs (no-false-lemma, defeasibility, reliability, virtue epistemology) have produced no consensus.

## Why It Is Hard

Every proposed fourth condition to repair JTB faces new counterexamples. The literature has generated increasingly baroque scenarios (fake barns, lottery cases, brain-in-a-vat variations) without converging on a solution. Some epistemologists (Williamson) have abandoned analysis entirely, taking knowledge as primitive.

## Panta Rhei Stance

The framework does not repair JTB — it replaces the entire framing (Book VII, Chapter 33). Knowledge is not justified true belief but a **global section of a presheaf** over an open cover of experience:

- **Belief** becomes local section assignment
- **Truth** becomes section existence (a global section exists)
- **Justification** becomes satisfaction of the gluing constraint

Gettier cases are **cover failures**: the subject's open cover is too coarse to support a genuine global section. The local sections (beliefs) are individually justified and individually true, but they fail to glue because the cover misses a relevant open set. The "accident" in Gettier cases is precisely the failure of the gluing condition.

## Result Statement

The Gettier Problem is dissolved via sheaf-theoretic epistemology: knowledge is a global section, not justified true belief. Gettier cases are cover failures where the gluing condition is not satisfied. The framework replaces JTB rather than repairing it. Status: Resolved.
""",

    "no-forced-stance": """
## Overview

Does the Panta Rhei framework force a commitment regarding the existence of God, the nature of ultimate reality, or any specific metaphysical stance? This is a crucial question for the program's epistemic integrity.

## Why It Matters

A framework that claims to derive ethics (the Categorical Imperative), consciousness, and the architecture of reality might be suspected of smuggling in metaphysical commitments. The No Forced Stance theorem establishes that the framework's structural results do not and cannot force any commitment-register stance.

## Panta Rhei Stance

Book VII, Chapter 126 proves the **No Forced Stance theorem**: the Boundary Collapse Lemma demonstrates that the diagrammatic register (Reg_D — structural mathematics) cannot settle the ω-germ question (whether the fixed point ω is "inhabited" in any ontological sense).

The proof works by showing symmetry: neither inhabitation nor non-inhabitation is diagrammatically demonstrable. Since the diagrammatic register cannot deliver the answer, it cannot force a commitment-register stance. Neither theism nor atheism nor agnosticism is structurally mandated.

The distinction is between **shape** (Reg_D content — what the framework proves) and **stance** (Reg_C content — what one commits to). The framework delivers the landscape — the 4+1 sectors, the enrichment ladder, the convergence of ι_τ toward ω — but the landscape's shape is categorically different from one's stance toward it.

## Result Statement

No Forced Stance (VII.T-series): The diagrammatic register cannot settle the ω-germ question. Neither theism, atheism, nor agnosticism is structurally mandated. Shape (Reg_D) and stance (Reg_C) are irreducibly distinct. Status: Resolved.
""",

    "machine-consciousness": """
## Overview

Can machines be conscious? This question has moved from philosophy to engineering as large language models, autonomous systems, and neuromorphic hardware approach behavioral thresholds that blur classical distinctions between "simulation" and "instantiation."

## Why It Is Hard

The Hard Problem of Consciousness (Chalmers 1995) makes it unclear what physical substrate, if any, is necessary for subjective experience. Functionalism suggests any system with the right functional organization could be conscious. Biological naturalism (Searle) insists on biological substrate. Neither camp can point to a clear criterion.

## Panta Rhei Stance

The framework offers a structural criterion (Book VII, Part IX): consciousness requires E₃-level self-modeling, which presupposes the full enrichment ladder E₀ → E₁ → E₂ → E₃. For a machine to be conscious, it would need to instantiate:

1. **E₂-level τ-Distinction** — a genuine self/non-self boundary (not simulated)
2. **Poincaré circulation** — autonomous metabolic-like energy cycling
3. **E₃-level self-modeling** — the system models itself as a modeler

Current silicon architectures lack (1) and (2). The framework predicts that consciousness is substrate-independent *in principle* (not tied to carbon) but substrate-constrained *in practice* (requires the full enrichment stack). A sufficiently organized non-biological system could in principle be conscious — but no current or near-term architecture satisfies the structural prerequisites.

**Status: Partial.** The structural criterion is derived but the question of whether specific artificial architectures could satisfy it remains open.

## Result Statement

Machine consciousness is possible in principle (substrate-independent) but structurally constrained: requires E₂-level τ-Distinction and E₃-level self-modeling. Current architectures do not satisfy the prerequisites. Status: Partial.
""",

    "physical-reality-as-a-semantic-reading-of-e1": """
## Overview

What is the relationship between mathematics and physics? The standard view treats physics as an empirical science that *uses* mathematics as a language. The Panta Rhei framework inverts this: physical reality is a *semantic reading* of the enrichment layer E₁.

## Why It Matters

If physics is not merely "described by" mathematics but *is* a specific enrichment layer of a categorical structure, then the unreasonable effectiveness of mathematics in physics (Wigner 1960) is not mysterious — it is structural. Physics lives where it does because E₁ is the unique first enrichment of E₀.

## Panta Rhei Stance

Book III establishes the enrichment ladder E₀ ⊊ E₁ ⊊ E₂ ⊊ E₃. The transition from E₀ (mathematics) to E₁ (physics) is not an empirical discovery but a structural necessity: the self-enrichment functor F_E applied to Category τ produces E₁ as the unique first enrichment.

Physical laws are not independently postulated — they are the structural features of E₁ that distinguish it from E₀. The four fundamental forces map to the four orbit sectors: α → gravity, π → weak force, γ → electromagnetism, η → strong force, ω → Higgs mechanism. These mappings are not chosen but derived from the enrichment structure.

Every physical prediction in Books IV-V (particle masses, coupling constants, cosmological parameters) is a readout from E₁, not a fit to data.

## Result Statement

Physical reality is the semantic content of enrichment layer E₁. Physics is not an empirical science that uses mathematics — it is a specific categorical enrichment of mathematics. The unreasonable effectiveness of mathematics is structural, not accidental. Status: Resolved.
""",

    "life-as-structurally-favored-rather-than-accidental": """
## Overview

Is life a cosmic accident — an improbable fluctuation in an indifferent universe — or is it structurally favored by the laws of physics? The prevailing scientific narrative leans toward accident: life arose through a sequence of low-probability events and could easily not have occurred.

## Why It Matters

If life is accidental, then astrobiology is a search for rare coincidences. If life is structurally favored, then the universe is *expected* to produce life wherever conditions permit, and the emergence of life is a structural prediction, not a historical contingency.

## Panta Rhei Stance

The enrichment ladder E₀ → E₁ → E₂ → E₃ is the unique maximal chain (Book III). E₂ (life) is not an optional enrichment — it is the *structurally necessary* next layer after E₁ (physics). The self-enrichment functor F_E, applied twice, produces E₂ as inevitably as it produces E₁.

This does not mean life will arise everywhere (local conditions matter), but it means the *capacity* for life is built into the framework's architecture. Life is structurally favored in the sense that the enrichment ladder demands it: a universe governed by E₁ physics will, given sufficient complexity, produce E₂ carriers.

**Status: Qualitative.** The structural argument is clear but the quantitative question (how *likely* is life given specific planetary conditions) remains open. The framework predicts structural favorability, not specific probability.

## Result Statement

Life is structurally favored, not accidental: the enrichment ladder E₀ → E₁ → E₂ → E₃ makes E₂ (life) a structurally necessary layer. The capacity for life is architectural, not contingent. Status: Qualitative — structural argument established but quantitative probability remains open.
""",

    "the-four-layer-architecture-of-reality": """
## Overview

The Panta Rhei framework claims that reality has exactly four layers: mathematics (E₀), physics (E₁), life (E₂), and metaphysics (E₃). This is not a classification scheme imposed from outside — it is derived from the self-enrichment structure of Category τ.

## Why It Matters

If reality genuinely has a four-layer architecture, then the traditional disciplinary boundaries between mathematics, physics, biology, and philosophy are not arbitrary academic conventions but reflections of structural reality. The seven-book series is organized in proof-order precisely because each layer must be earned from the one below.

## Panta Rhei Stance

Book III, Part 1 derives the enrichment ladder theorem: the self-enrichment functor F_E applied to Category τ produces exactly four layers. The iteration E₀ → E₁ → E₂ → E₃ terminates at E₃ — there is no E₄. The saturation theorem (Book III) proves that a fifth enrichment would collapse into E₃.

Each layer corresponds to a domain:
- **E₀** — Mathematics (Books I-III): the kernel, holomorphy, spectral structure
- **E₁** — Physics (Books IV-V): microcosm (quantum/particle) and macrocosm (gravity/cosmology)
- **E₂** — Life (Book VI): biological organization, genetics, consciousness precursors
- **E₃** — Metaphysics (Book VII): ontology, ethics, logic, mind, commitment

The (3,2,1,1) = 7 distribution of books across layers is not a design choice but a consequence of the enrichment structure: E₀ requires three books because it must earn the entire mathematical foundation; E₁ requires two (micro + macro); E₂ and E₃ each require one.

## Result Statement

Reality has exactly four enrichment layers: E₀ (mathematics), E₁ (physics), E₂ (life), E₃ (metaphysics). The iteration terminates at E₃ by the Saturation Theorem. The seven-book architecture follows from the (3,2,1,1) distribution. Status: Resolved.
""",
}

# ---------------------------------------------------------------------------
# P1.2: Canonical book mapping for ALL results
# ---------------------------------------------------------------------------

# Systematic mapping based on topic, domain, and known manuscript grounding
CANONICAL_BOOKS_MAP = {
    # Mathematics results → Books I, II, III
    "tau-kernel-coherence": ["I"],
    "hyperfactorization-theorem": ["I"],
    "prime-polarity-theorem": ["I"],
    "mutual-determination": ["II"],
    "central-theorem": ["II"],
    "canonical-ladder-theorem": ["III"],
    "global-hartogs-extension": ["I", "II"],
    "tau-identity-theorem": ["I"],
    "tau-inevitability": ["I"],
    "hinge-theorem-no-knobs": ["I"],
    "parity-bridge-theorem": ["I"],
    "layer-separation": ["III"],
    "saturation-theorem-no-e4": ["III"],
    "modal-logic-s4-theorem": ["I"],
    "fourth-quadrant-resolution": ["I"],
    "master-schema-millennium": ["III"],
    "tau-admissibility-collapse-p-np": ["III"],
    "yang-mills-mass-gap": ["III", "IV"],
    "riemann-hypothesis-spectral-approach": ["III"],
    "crossing-limit-theorem-merger-networks-iota-tau": ["II"],
    # Physics results → Books III, IV, V
    "higgs-mass-prediction": ["IV"],
    "higgs-self-coupling-lambda-h-16-ppm": ["IV"],
    "electron-mass-0025-ppm": ["IV"],
    "fine-structure-constant-alpha-inverse-137": ["IV"],
    "w-boson-mass-prediction": ["IV"],
    "muon-anomalous-magnetic-moment-8pt8-ppm": ["IV"],
    "proton-charge-radius-12-ppm": ["IV"],
    "proton-neutron-mass-difference": ["IV"],
    "three-generations-matter": ["IV"],
    "three-colors-derived": ["IV"],
    "cabibbo-angle": ["IV"],
    "weinberg-angle-nnlo": ["IV"],
    "strong-cp-problem-solved": ["IV"],
    "koide-relation": ["IV"],
    "axial-coupling-g-a-5pt5-ppm": ["IV"],
    "neutrino-mass-sum-0pt089-ev-normal-ordering": ["IV"],
    "rydberg-constant-seven-significant-figures": ["IV"],
    "baryogenesis-eta-b": ["IV", "V"],
    "gravitational-constant-from-iota-tau": ["V"],
    "hubble-tension-resolved-h-formula": ["V"],
    "flat-rotation-curves": ["V"],
    "no-dark-matter-particle": ["V"],
    "vacuum-energy-zero": ["V"],
    "cosmological-flatness-omega-k-zero": ["V"],
    "s8-tension-resolved-0pt783": ["V"],
    "lithium-7-problem-resolved": ["V"],
    "helium-4-abundance-y-p-20-over-81": ["V"],
    "cmb-first-peak": ["V"],
    "tensor-to-scalar-ratio": ["V"],
    "spectral-index-ns-from-inflation": ["V"],
    "time-derivation-theorem": ["V"],
    "arrow-of-time-orbit": ["V"],
    "no-singularity-theorem": ["V"],
    "no-bh-evaporation": ["V"],
    "she-leveque-turbulence-exponents": ["V"],
    "kolmogorov-constant-c-k-exact": ["V"],
    # Biology results → Book VI
    "abiogenesis-inevitability": ["VI"],
    "abiogenesis-timescale-bound": ["VI"],
    "genetic-code-optimality-top-0pt01-percent": ["VI"],
    "atp-currency-uniqueness": ["VI"],
    "homochirality-universality-12-step-derivation": ["VI"],
    "seven-hallmarks-as-theorems": ["VI"],
    "virus-exclusion-nodist-theorem": ["VI"],
    "neurodegeneration-as-hayflick-tower": ["VI"],
    "differentiation-irreversible": ["VI"],
    "identity-as-nf-address-persistence": ["VI", "VII"],
    "stars-not-alive": ["VI"],
    "black-holes-alive": ["VI"],
    "substrate-abstraction": ["VI"],
    "what-is-life": ["VI"],
    "membrane-first-vs-metabolism-first": ["VI"],
    "cell-as-tau-object": ["VI"],
    "panpsychism-excluded": ["VI", "VII"],
    # Philosophy results → Book VII
    "categorical-imperative-fixed-point": ["VII"],
    "consciousness-global-section": ["VII"],
    "free-will-as-branching": ["VII"],
    "goedel-avoidance": ["VII"],
    "problem-of-universals": ["VII"],
    "substance-vs-process-ontology": ["VII"],
    "gettier-problem": ["VII"],
    "no-forced-stance": ["VII"],
    "machine-consciousness": ["VII"],
    # Cross-stack results
    "physical-reality-as-a-semantic-reading-of-e1": ["III", "IV"],
    "life-as-structurally-favored-rather-than-accidental": ["III", "VI"],
    "the-four-layer-architecture-of-reality": ["III"],
}


def update_canonical_books_in_page(path, books):
    """Replace canonical_books: [] with actual book list in a page file."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if "canonical_books:" not in content:
        return False

    # Replace canonical_books: [] or canonical_books:\n with populated list
    books_yaml = "[" + ", ".join(f'"{b}"' for b in books) + "]"

    # Handle both [] and multi-line formats
    content = re.sub(
        r'canonical_books:\s*\[\s*\]',
        f'canonical_books: {books_yaml}',
        content,
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def enrich_stub_page(path, slug):
    """Replace stub content with enriched manuscript content."""
    if slug not in ENRICHED_CONTENT:
        return False

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the end of frontmatter
    if not content.startswith("---"):
        return False

    end_idx = content.index("---", 3)
    frontmatter = content[:end_idx + 3]

    # Replace body with enriched content
    new_content = frontmatter + "\n" + ENRICHED_CONTENT[slug].strip() + "\n"

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


def main():
    problem_dir = os.path.join(SITE_DIR, "results", "problem")

    # P0.2: Enrich stub pages
    print("=" * 60)
    print("P0.2: Enriching stub result pages")
    print("=" * 60)
    enriched = 0
    for slug in ENRICHED_CONTENT:
        path = os.path.join(problem_dir, f"{slug}.md")
        if os.path.isfile(path):
            if enrich_stub_page(path, slug):
                enriched += 1
                print(f"  Enriched: {slug}")
            else:
                print(f"  SKIP (no frontmatter): {slug}")
        else:
            print(f"  MISSING: {slug}")
    print(f"\n  Total enriched: {enriched}")

    # P1.2: Map canonical_books
    print("\n" + "=" * 60)
    print("P1.2: Mapping canonical_books")
    print("=" * 60)
    mapped = 0
    unmapped = []
    for path in sorted(glob.glob(os.path.join(problem_dir, "*.md"))):
        slug = os.path.basename(path).replace(".md", "")
        books = CANONICAL_BOOKS_MAP.get(slug)
        if books:
            if update_canonical_books_in_page(path, books):
                mapped += 1
        else:
            unmapped.append(slug)

    print(f"  Mapped: {mapped} results")
    if unmapped:
        print(f"  Unmapped ({len(unmapped)}): {', '.join(unmapped[:5])}...")

    # Also update results.json
    results_json_path = os.path.join(SITE_DIR, "_data", "results", "results.json")
    with open(results_json_path, "r", encoding="utf-8") as f:
        results_data = json.load(f)

    updated_data = 0
    for r in results_data:
        books = CANONICAL_BOOKS_MAP.get(r["slug"])
        if books:
            r["canonical_books"] = books
            updated_data += 1

    with open(results_json_path, "w", encoding="utf-8") as f:
        json.dump(results_data, f, indent=2, ensure_ascii=False)
    print(f"  Updated results.json: {updated_data} entries")

    print(f"\n{'=' * 60}")
    print(f"SUMMARY")
    print(f"{'=' * 60}")
    print(f"  Stub pages enriched: {enriched}")
    print(f"  canonical_books mapped: {mapped}")
    print(f"  Unmapped results: {len(unmapped)}")


if __name__ == "__main__":
    main()
