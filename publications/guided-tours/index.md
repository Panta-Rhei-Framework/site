---
layout: program-doc
title: "Guided Tours"
lane: publications
permalink: /publications/guided-tours/
type: "Publication Family"
publication_type: "Guided Tours"
status: "Published"
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

## What This Family Does

Guided Tours are controlled entry points into the load-bearing parts of the program. They are shorter than the books and more technical than the homepage: each tour names the hinge, shows why it matters, and points to the place where a reader can attack it.

Use this family when you want to evaluate a book without first reading the full monograph, or when you want the Lean counterpart for a specific structural claim.

## Guided Tour Whitepapers

Seven PDF whitepapers (56 pages total), each identifying the 5-8 structural hinges of one book:

| Book | Pages | Hinges | Key attack vectors | Download |
|------|:-----:|:------:|--------------------|----------|
| I | 6 | 7 | Axiom independence, Hyperfact counterexample | [PDF]({{ '/assets/media/guided-tour-book-I.pdf' | relative_url }}) |
| II | 7 | 7 | Ghost function, break Mutual Determination | [PDF]({{ '/assets/media/guided-tour-book-II.pdf' | relative_url }}) |
| III | 8 | 6 | Construct E<sub>5</sub>, break sector template | [PDF]({{ '/assets/media/guided-tour-book-III.pdf' | relative_url }}) |
| IV | 7 | 7 | Falsify alpha formula, mass ratio wrong | [PDF]({{ '/assets/media/guided-tour-book-IV.pdf' | relative_url }}) |
| V | 8 | 8 | CMB-S4 kills r=iota<sub>tau</sub><sup>4</sup>, direct DM detection | [PDF]({{ '/assets/media/guided-tour-book-V.pdf' | relative_url }}) |
| VI | 9 | 7 | Living system without SelfDesc | [PDF]({{ '/assets/media/guided-tour-book-VI.pdf' | relative_url }}) |
| VII | 11 | 7 | Construct E<sub>4</sub>, cross the boundary | [PDF]({{ '/assets/media/guided-tour-book-VII.pdf' | relative_url }}) |

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

## Where to Go Next

If a tour raises a technical question, follow it into [TauLib]({{ '/verify/taulib/' | relative_url }}) or the relevant [Corpus registry]({{ '/corpus/registry/' | relative_url }}) object. If it raises an empirical question, follow the prediction or falsification target into [Results]({{ '/results/' | relative_url }}) and [Verify]({{ '/verify/predictions-and-falsification/' | relative_url }}).
