---
layout: program-doc
title: "Guided Tours"
lane: publications
permalink: /publications/guided-tours/
summary_short: "Structural falsification guides and Lean verification companions — 56 pages of whitepapers plus 7 native Lean 4 tour modules."
summary_cards:
  - title: "7 whitepapers"
    body: "One per book, identifying 5-8 load-bearing hinges with exact attack vectors and survival analysis."
  - title: "7 Lean companions"
    body: "Native Lean 4 modules mapping 49 structural hinges to their machine-checked formalizations."
  - title: "8 interactive tours"
    body: "Step-through modules in TauLib for mathematicians, physicists, biologists, philosophers, and skeptics."
right_rail:
  related:
    - title: "Publications Overview"
      url: /publications/
    - title: "Verify"
      url: /verify/
  artifacts:
    - title: "TauLib Tours"
      url: "https://github.com/Panta-Rhei-Framework/taulib"
      external: true
  meta:
    type: "Family Root"
    status: "Published"
    updated: "April 2026"
---

## Guided Tour Whitepapers

Seven LaTeX whitepapers (56 pages total), each identifying the 5-8 structural hinges of one book:

| Book | Pages | Hinges | Key Attack Vectors |
|------|:-----:|:------:|-------------------|
| I | 6 | 7 | Axiom independence, Hyperfact counterexample |
| II | 7 | 7 | Ghost function, break Mutual Determination |
| III | 8 | 6 | Construct E₅, break sector template |
| IV | 7 | 7 | Falsify α formula, mass ratio wrong |
| V | 8 | 8 | CMB-S4 kills r=ι_τ⁴, direct DM detection |
| VI | 9 | 7 | Living system without SelfDesc |
| VII | 11 | 7 | Construct E₄, cross the boundary |

Available as PDF downloads at [panta-rhei.site](https://panta-rhei.site).

## Lean Verification Companions

7 native Lean 4 modules (`Tour/GuidedTour/BookI.lean` through `BookVII.lean`) that let you `#check` each hinge theorem directly. 49 structural hinges mapped to their exact formalization.

## Interactive Tours

8 audience-targeted tours in TauLib (`Tour/*.lean`):

- **VerifyItYourself** — the skeptic's tour (5 claims, verified live)
- **Foundations** — 5 generators, 7 axioms, rigidity
- **CentralTheorem** — O(τ³) ≅ A_spec(L)
- **Physics** — 9 electroweak predictions
- **OneConstant** — full constants ledger from ι_τ
- **MillenniumProblems** — GRH, BSD, Poincaré
- **LifeFromPhysics** — 4+1 life sectors, genetic code
- **MindAndEthics** — CI, consciousness, free will
