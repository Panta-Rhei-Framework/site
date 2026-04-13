---
layout: homepage
title: "Panta Rhei Research Program"
hero_line: "An independent open research program."
hero_body: "Exploring whether one constrained formal kernel can support a unified model of mathematics, physics, life, and metaphysics — with every claim typed, every derivation machine-checked, and every prediction publicly inspectable."
hero_ctas:
  - label: "Explore the Framework"
    url: /framework/about/
    primary: true
  - label: "Browse Key Results"
    url: /results/
    primary: true
  - label: "Verify It Yourself"
    url: /verify/
right_rail:
  related:
    - title: "About the Research"
      url: /research-program/about/
    - title: "Publications"
      url: /publications/
    - title: "Media Kit"
      url: /media/
  artifacts:
    - title: "TauLib"
      url: "https://github.com/Panta-Rhei-Framework/taulib"
      external: true
    - title: "Frozen Verification"
      url: "https://github.com/Panta-Rhei-Framework/formalization"
      external: true
  meta:
    type: "Landing"
    status: "Canonical"
    updated: "April 2026"
---

{% assign result_count = site.data.results.results | size %}{% assign registry_count = site.data.registry.objects | size %}{% assign book_count = site.data.publications.books | size %}{% assign chapter_count = site.data.publications.chapters | size %}
<div class="content-card homepage-section">
<h2>Why this program is built from a constrained kernel</h2>

The program binds itself to strong constraints. Every mathematical tool is *earned* from five generators, seven axioms, and one operator — not imported from existing mathematics. Every scope claim carries an explicit label: established, tau-effective, conjectural, or metaphorical. Every derivation chain is machine-checked in Lean 4.

The stronger the claimed scope, the stricter the foundation must be. This is not a design choice — it is a structural necessity. A framework that claims to derive both the Higgs mass and the Categorical Imperative from the same kernel must be maximally constrained, or it is merely telling stories.

<a href="{{ '/research-program/about/' | relative_url }}" class="btn-secondary">About the Research</a>
</div>

<div class="content-card homepage-section">
<h2>The Tau framework</h2>

Category tau begins below ordinary category theory. Five generators (alpha, pi, gamma, eta, omega) in strict total order, one progression operator (rho), and seven axioms (K0-K6) define a complete, rigid, countable universe. From this kernel, the framework earns its own arithmetic, geometry, analysis, topology, and category theory — then enriches itself through four layers:

- **E0 — Mathematics** (Books I-III): Kernel, holomorphy, spectral structure
- **E1 — Physics** (Books IV-V): Microcosm and macrocosm from one constant
- **E2 — Life** (Book VI): Life as self-decoding distinctions
- **E3 — Metaphysics** (Book VII): The final self-enrichment

The master constant iota_tau = 2/(pi+e) governs all quantitative predictions. Zero free parameters.

<div class="btn-group">
<a href="{{ '/framework/about/' | relative_url }}" class="btn-secondary">Framework Overview</a>
<a href="{{ '/verify/taulib/' | relative_url }}" class="btn-secondary">TauLib Documentation</a>
</div>
</div>

<div class="content-card homepage-section">
<h2>Current scope of the program's claims</h2>

The program currently presents **{{ result_count }} key results** across four domains, each with typed epistemic status. A small selection of flagship claims:

- **Dark sector closure** — dark matter and dark energy as structural artifacts of the boundary reading, not new particles
- **Hubble tension resolved** — h = 2/3 + iota_tau^2/17 at -120 ppm, zero free parameters
- **Genetic code optimality** — top 0.01% for error minimization, derived from BSD-motivic structure
- **Categorical Imperative** — Kant's CI derived as the unique j-closed fixed point, not postulated
- **Hierarchy problem** — the 10^32 gravity/EM ratio from structural sector separation
- **Gettier Problem dissolved** — knowledge as global section, Gettier cases as cover failures

Every claim carries a status: resolved, partial, qualitative, or contradicted. The typing is not optional — it is the program's principal epistemic commitment.

<div class="btn-group">
<a href="{{ '/results/' | relative_url }}" class="btn-secondary">Browse {{ result_count }} Results</a>
<a href="{{ '/results/why-so-many-results/' | relative_url }}" class="btn-secondary">Why So Many Results</a>
</div>
</div>

<div class="content-card homepage-section">
<h2>The program is public through verification surfaces</h2>

This is not a program that asks for trust. It is a program that provides inspection routes:

- **{{ book_count }} canonical books** — {{ chapter_count }} chapters in proof-order, available on Amazon KDP
- **TauLib** — 450 Lean 4 modules, 125,771 lines, 4,332 machine-checked theorems, 0 sorry in Books I-VI
- **{{ registry_count }} registry objects** — every definition, theorem, and proposition with dependency graphs
- **8 guided tours** — interactive Lean walkthroughs for skeptics, mathematicians, physicists, biologists, and philosophers
- **220+ quantitative predictions** — with explicit precision claims and falsification routes

The decisive empirical test: CMB-S4 will measure the tensor-to-scalar ratio *r*. If *r* is inconsistent with iota_tau^4, the framework's cosmological predictions fail.

<div class="btn-group">
<a href="{{ '/verify/' | relative_url }}" class="btn-secondary">Verify</a>
<a href="{{ '/registry/' | relative_url }}" class="btn-secondary">Registry</a>
<a href="{{ '/publications/guided-tours/' | relative_url }}" class="btn-secondary">Guided Tours</a>
</div>
</div>

<div class="content-card homepage-section">
<h2>Why this could matter if it holds</h2>

If the framework holds — or partially holds — consequences could propagate into public-good domains. The program's impact lane explores 11 conditional deployment portfolios across agriculture, climate, energy, ocean science, public health, and more, grounded in 44 companion papers.

The word *if* is load-bearing. These are scenario analyses, not predictions of social adoption. The framework must survive empirical testing before any downstream consequence becomes real.

<a href="{{ '/impact/' | relative_url }}" class="btn-secondary">Potential Impact</a>
</div>

<div class="content-card homepage-section">
<h2>Read, inspect, follow, and engage</h2>

The program can be entered through many routes:

- **[The Seven Books]({{ '/publications/books/' | relative_url }})** — the canonical monograph series with DOIs and Amazon links
- **[Key Results]({{ '/results/' | relative_url }})** — {{ result_count }} results with typed status across four domains
- **[Verify]({{ '/verify/' | relative_url }})** — clone TauLib, run `lake build`, step through the tours
- **[Media Kit]({{ '/media/' | relative_url }})** — for journalists, podcast hosts, reviewers, and institutions
- **[Follow the Research]({{ '/engage/follow-the-research/' | relative_url }})** — stay connected with the program's ongoing work

*Panta Rhei — Everything Flows.*
</div>
