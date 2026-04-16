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
      url: "https://github.com/Panta-Rhei-Research/taulib"
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
| V | 8 | 8 | CMB-S4 kills r=ι<sub>τ</sub>⁴, direct DM detection |
| VI | 9 | 7 | Living system without SelfDesc |
| VII | 11 | 7 | Construct E₄, cross the boundary |

Available as PDF downloads at [panta-rhei.site](https://panta-rhei.site).

## Lean Verification Companions

7 native Lean 4 modules that let you `#check` each hinge theorem directly. 49 structural hinges mapped to their exact formalization:

- [BookI](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/GuidedTour/BookI.lean) · [BookII](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/GuidedTour/BookII.lean) · [BookIII](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/GuidedTour/BookIII.lean) · [BookIV](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/GuidedTour/BookIV.lean) · [BookV](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/GuidedTour/BookV.lean) · [BookVI](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/GuidedTour/BookVI.lean) · [BookVII](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/GuidedTour/BookVII.lean)

## Interactive Tours

8 audience-targeted tours in TauLib (`Tour/*.lean`), each a self-contained Lean 4 module you can run with `lake build`:

- **[VerifyItYourself](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/VerifyItYourself.lean)** — the skeptic's tour (5 claims, verified live)
- **[Foundations](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/Foundations.lean)** — 5 generators, 7 axioms, rigidity
- **[CentralTheorem](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/CentralTheorem.lean)** — O(τ³) ≅ A_spec(L)
- **[Physics](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/Physics.lean)** — 9 electroweak predictions
- **[OneConstant](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/OneConstant.lean)** — full constants ledger from ι<sub>τ</sub>
- **[MillenniumProblems](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/MillenniumProblems.lean)** — GRH, BSD, Poincaré
- **[LifeFromPhysics](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/LifeFromPhysics.lean)** — 4+1 life sectors, genetic code
- **[MindAndEthics](https://github.com/Panta-Rhei-Research/taulib/blob/main/TauLib/Tour/MindAndEthics.lean)** — CI, consciousness, free will
