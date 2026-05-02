---
layout: program-doc
title: "How to Audit — Mathematician Route"
permalink: /verify/how-to-audit/mathematician/
lane: verify
v2_lane: verify
type: "Inspection Route"
status: "Canonical"
summary_short: "For specialists in category theory, model theory, analytic number theory, operator theory, several complex variables, or algebraic geometry. Three load-bearing theorems in Books I–III are where the framework's internal mathematics either holds or fails."
plain_language_summary: "If you do mathematics professionally, three theorems in Books I–III carry the framework's mathematical weight: the Central Theorem (Book II) which establishes categoricity, the Yoneda-as-theorem result (Book II) which is the self-enrichment claim, and the Hyperfactorization Theorem (Book I) which is how all τ-objects are constructed. The page below routes you to those three, names what your specialization is best positioned to check, and tells you which Mathlib results the proofs depend on so you can verify the foundational moves use standard mathematics correctly."
right_rail:
  related:
    - title: "How to Audit (Hub)"
      url: /verify/how-to-audit/
    - title: "Foundational Hinges"
      url: /corpus/foundational-hinges/
    - title: "Prior-Art Comparisons"
      url: /program/research-agenda/kernel-model-reality/related-approaches/deep-comparison/
    - title: "Foundations briefing"
      url: /results/fields/foundations-logic/
    - title: "Millennium briefing"
      url: /results/fields/millennium-langlands/
  meta:
    type: "Inspection Route"
    scope: "Mathematical spine audit"
    status: "Canonical"
    updated: "April 2026"
---

This route is for mathematicians evaluating the framework's internal mathematical spine. It does not presuppose expertise in physics or philosophy of science — only rigor in the mathematical machinery of Books I–III.

The framework's mathematical content is not spread uniformly. Three theorem clusters carry the load; if any of them fail, the rest collapses because the physics, life, and metaphysics bridges all depend on them. This route walks you to those three clusters directly.

## First pass: foundational hinges

For the first mathematical pass, begin with the Foundational Hinge route. It is the compressed entry point for the first three construction burdens: kernel architecture, recovered mathematics, and self-enrichment.

- [Foundational Hinges]({{ '/corpus/foundational-hinges/' | relative_url }})
- [Step 1 — Build the τ-Kernel]({{ '/corpus/construction-spine/build-the-kernel/' | relative_url }})
- [Step 2 — Recover Core Mathematics]({{ '/corpus/construction-spine/recover-core-mathematics/' | relative_url }})
- [Step 3 — Internalize Self-Enrichment]({{ '/corpus/construction-spine/internalize-self-enrichment/' | relative_url }})

This route separates those construction burdens from later result claims. The hinge pages are not replacements for Books I-II or TauLib; they are the reviewer packet for finding the load-bearing paper, Registry, proof, and failure surface quickly.

## The three load-bearing clusters

### 1. Book I — Categoricity and rigidity of τ

**The claim:** Seven axioms K0–K6 on five generators (α, π, γ, η, ω) and one operator (ρ) determine the τ kernel **up to isomorphism**. Any two models satisfying K0–K6 are isomorphic; τ is rigid.

**Why it is load-bearing:** The entire framework rests on the claim that τ is *the* kernel, not *a* kernel. If K0–K6 admit multiple non-isomorphic models, the framework's "one coherence kernel" story fails and ι<sub>τ</sub> = 2/(π+e) is at best one of many possible calibrations.

**Where to look:**
- Claim page: [Categoricity of τ]({{ '/results/problem/categoricity-of-tau/' | relative_url }})
- Claim page: [τ-Kernel Coherence]({{ '/results/problem/tau-kernel-coherence/' | relative_url }})
- Book I canonical source + `TauLib/Book1/Kernel.lean` for the formalization
- Registry entry `I.T` for the formal statement with dependency chain

**What to check first:**
- In what logic is the categoricity claim stated? First-order? Second-order? An internal categorical-logic sense? The answer affects whether Löwenheim-Skolem is a problem.
- What is the precise definition of "rigid"? Is it functorial (Aut(τ) = trivial) or weaker?
- Are the axioms independent? A dependent axiom set may hide structure that looks rigid but factors through a smaller system.
- Is the argument constructive or does it use classical choice? The framework's architectural commitment to coherence-first derivation would be strained by heavy use of choice.

**Fail-fast:** If the categoricity theorem is stated in ordinary first-order logic and the argument relies on "up to isomorphism in ZFC", then Löwenheim-Skolem implies non-isomorphic models of any infinite cardinality exist and the claim is either in the wrong logic or wrong. Check this first.

### 2. Book II — Central Theorem 𝒪(τ³) ≅ A_spec(𝕃)

**The claim:** The ring of holomorphic functions on the fibered product τ³ = τ¹ ×_f T² is canonically isomorphic to the character algebra of the lemniscate boundary 𝕃 = S¹ ∨ S¹.

**Why it is load-bearing:** This is the bridge between the mathematical kernel and the physics readout. It is also the Holographic Principle claim (II.C01) that the framework advertises as a proved theorem rather than a conjectured duality (cf. AdS/CFT).

**Where to look:**
- Claim page: [Central Theorem]({{ '/results/problem/central-theorem/' | relative_url }})
- Claim page: [Holographic Principle]({{ '/results/problem/holographic-principle/' | relative_url }})
- Prior-art comparison: [τ-Holomorphy vs Fueter-Regular]({{ '/program/research-agenda/kernel-model-reality/related-approaches/deep-comparison/' | relative_url }})
- `TauLib/Book2/CentralTheorem.lean`

**What to check first:**
- What is the τ-Cauchy-Riemann operator, as a first-order differential system? How does it compare to Cauchy-Fueter in quaternionic analysis and to Moisil-Théodoresco in Clifford analysis?
- Is the isomorphism 𝒪(τ³) ≅ A_spec(𝕃) *canonical* in a functorial sense, or does it depend on auxiliary choices?
- What is the reproducing kernel, if any? Does it specialize to known kernels on slice restrictions?
- Are there side conditions (τ-admissibility, finite-window)? If so, how strong are they?

**Fail-fast:** If the "ring isomorphism" turns out to require side conditions that are equivalent to hand-picking compatible elements in both algebras, the theorem reduces to a tautology. Conversely, if there is a genuine unconditional isomorphism, this is non-trivial content that a specialist should be able to verify by matching generators and relations.

### 3. Book III — Critical Line Theorem III.T19

**The claim:** All non-trivial zeros of the τ-zeta function ζ<sub>τ</sub> lie on the critical line, via a spectral trichotomy argument (III.T14).

**Why it is load-bearing:** This is the τ-framework's analogue of the Riemann Hypothesis, explicitly labeled **τ-effective / finite-window**. It does not claim to resolve the Clay problem directly; the bridge is marked conjectural via the Master Schema (III.T27). But the τ-internal theorem is the most significant individual result in Book III and a natural target for specialist scrutiny.

**Where to look:**
- Claim page: [Riemann Hypothesis (τ-internal)]({{ '/results/problem/riemann-hypothesis/' | relative_url }})
- Claim page: [Riemann Hypothesis (Spectral Approach)]({{ '/results/problem/riemann-hypothesis-spectral-approach/' | relative_url }})
- Prior-art comparison: [Spectral ζ vs Hilbert-Pólya / Connes / Berry-Keating]({{ '/program/research-agenda/kernel-model-reality/related-approaches/deep-comparison/' | relative_url }})
- `TauLib/Book3/CriticalLine.lean`

**What to check first:**
- What is the τ spectral operator explicitly? On what Hilbert space does it act? Is it self-adjoint?
- Is the spectral trichotomy (III.T14) a genuine trichotomy (boundary / interior / critical line) with structural arguments excluding the first two, or is one of the cases vacuous?
- How does the τ-ζ function relate to the classical Riemann ζ? If not at all, what is the substance of the "Riemann-hypothesis-like" framing?
- Does the τ-zeros distribution satisfy Montgomery-Odlyzko pair-correlation (GUE)? If yes, strong consistency with classical ζ; if no, τ is making a different prediction.

**Fail-fast:** If the τ-ζ function is not coupled to classical ζ by any explicit functor (even a conjectural one named by the Master Schema), the spectral result is a statement about a different object and the RH-framing is rhetorical. The Master Schema is where the rhetoric-or-substance question is decided; inspect the Master Schema statement directly.

## Cross-cutting checks

Across all three clusters, the following specialist-level audits are high-signal:

- **Dependency chain integrity.** Each registry entry carries a dependency list. Trace the load-bearing theorems (I.T, II.T40, III.T19) back to the axioms. Are there gaps? Circular dependencies? Unstated premises?
- **"Earned from seven axioms" claim.** The framework states its mathematical content is earned from the kernel, not imported from Mathlib. Confirm this at the Lean level (see [Formal Methods route]({{ '/verify/how-to-audit/formal-methods/' | relative_url }})).
- **Scope-label discipline.** Book III explicitly labels each claim as **established / τ-effective / conjectural / metaphorical**. A mathematician's audit should verify that the labels match the actual formal status — no promoted-conjectural labels, no demoted-theorem labels.

## What to escalate

If a cluster audit returns specific technical objections (e.g., "the rigidity argument in I.T has a gap at step 4 because..."), this is exactly the kind of feedback the program can act on. [Contact]({{ '/engage/contact/' | relative_url }}) with concrete line references.

If the audit is positive — all three clusters survive specialist scrutiny — the next routes are:
- For physical interpretation of the mathematics: [Physicist route]({{ '/verify/how-to-audit/physicist/' | relative_url }})
- For prior-art overlap assessment: [Prior-Art Specialist route]({{ '/verify/how-to-audit/prior-art-specialist/' | relative_url }})

## Cross-links

- [Foundations, Logic & CS briefing]({{ '/results/fields/foundations-logic/' | relative_url }}) — full foundations claim set
- [Millennium & Langlands briefing]({{ '/results/fields/millennium-langlands/' | relative_url }}) — all seven Millennium problems + Grand GRH + Langlands
- [Prior-Art Comparisons]({{ '/program/research-agenda/kernel-model-reality/related-approaches/deep-comparison/' | relative_url }}) — specialist-level prior-art pages
- [Red-team FAQ]({{ '/program/about/red-team-faq/' | relative_url }}) — the 10 hardest first-contact questions
- [How to Audit (Hub)]({{ '/verify/how-to-audit/' | relative_url }}) — all six reviewer routes
