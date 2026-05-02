---
layout: homepage
shell: home
title: "Panta Rhei Research Program"
lane: discover
v2_lane: discover
type: "Homepage"
status: "Canonical"
summary_short: "A structured public interface to a living research system across mathematics, physics, life, and metaphysics."
hero_line: "A coherent formal system claiming to derive structure across mathematics, physics, life, and metaphysics."
hero_body: "An independent open research program by Thorsten Fuchs and Anna-Sophie Fuchs, exposing its public surfaces through Research Monographs, a structured Corpus, typed Results, verification routes, and empirical challenge commitments."
hero_ctas:
  - label: "Start with Discover"
    url: /discover/
    primary: true
  - label: "Explore the Corpus"
    url: /corpus/
  - label: "See the Results"
    url: /results/
  - label: "Verify It Yourself"
    url: /verify/
hero_supporting_line: "Static, inspectable, Pagefind-searchable, and organized around canonical public lanes."
og_image: /assets/images/plates/plate-01-public-research-observatory-og.jpg
twitter_image: /assets/images/plates/plate-01-public-research-observatory-og.jpg
og_image_alt: "Scientific plate mapping the Panta Rhei Research Program as a public research observatory with Research Agenda, Corpus, Results, Verify, Publications, Impact, and Engage."
---

{% assign result_count = site.data.results.results | size %}
{% assign registry_count = site.data.registry.objects | size %}
{% assign book_count = site.data.publications.books | size %}
{% assign chapter_count = site.data.publications.chapters | size %}

<section class="content-card homepage-section">
  <p class="v2-kicker">The research observatory at a glance</p>
  <h2>The public research observatory</h2>
  {% include scientific-plate.html id="plate-01-public-research-observatory" class="scientific-plate--hero" loading="eager" %}
  <div class="btn-group section-ctas">
    <a class="btn-secondary" href="{{ '/discover/' | relative_url }}">Start with Discover</a>
    <a class="btn-ghost" href="{{ '/corpus/' | relative_url }}">Explore the Corpus</a>
    <a class="btn-ghost" href="{{ '/results/' | relative_url }}">See the Results</a>
    <a class="btn-ghost" href="{{ '/verify/' | relative_url }}">Verify it yourself</a>
  </div>
</section>

<section class="content-card homepage-section">
  <p class="v2-kicker">Choose your entry</p>
  <h2>Different readers should not have to start in the same place</h2>
  <div class="v2-grid">
    <a class="v2-tile" href="{{ '/discover/' | relative_url }}">
      <h3>Discover</h3>
      <p>A guided first route for readers who want orientation before depth.</p>
    </a>
    <a class="v2-tile" href="{{ '/program/' | relative_url }}">
      <h3>Program</h3>
      <p>The aim, burden of proof, scope, constraints, and research contract.</p>
    </a>
    <a class="v2-tile" href="{{ '/corpus/' | relative_url }}">
      <h3>Corpus</h3>
      <p>The living research body: Construction Spine, Registry, TauLib projection, Research Monographs, and dependency graph.</p>
    </a>
    <a class="v2-tile" href="{{ '/results/' | relative_url }}">
      <h3>Results</h3>
      <p>Landmark Results, World Readouts, Problem Ledger Answers, Recovery Target Status, Additional Derived Results, and Progress Against Agenda.</p>
    </a>
    <a class="v2-tile" href="{{ '/verify/' | relative_url }}">
      <h3>Verify</h3>
      <p>Formalization, predictions, falsification, audit routes, and external challenge paths.</p>
    </a>
    <a class="v2-tile" href="{{ '/publications/' | relative_url }}">
      <h3>Publications</h3>
      <p>Research Monographs, Monograph Supplements, Research Papers, Research Notes, Research Briefings, White Papers, and Release Artifacts.</p>
    </a>
  </div>
</section>

<section class="content-card homepage-section">
  <p class="v2-kicker">Flagship results</p>
  <h2>Concrete claims before broad interpretation</h2>
  <p>The quantitative physics surface is organized around the master constant <strong>ι<sub>τ</sub> = 2/(π + e) ≈ 0.341304</strong>. The current public release treats this as a review target, not a rhetorical shortcut: the constant has a dedicated research paper, a Corpus foundational-hinge page (H3), a scalar-readout route through Construction Spine Step&nbsp;2, Registry anchors, and TauLib evidence. Downstream physics claims remain bridge and empirical-accountability claims, but the master-constant question now has a direct public review path.</p>
  <div class="btn-group section-ctas">
    <a class="btn-secondary" href="{{ '/corpus/foundational-hinges/master-constant-iota-tau/' | relative_url }}">Review the Master Constant</a>
    <a class="btn-ghost" href="{{ '/publications/research-papers/master-constant-iota-tau/' | relative_url }}">Read the paper</a>
    <a class="btn-ghost" href="{{ '/results/predictions/timing/' | relative_url }}">See prediction timing</a>
  </div>
  <p>The program presents {{ result_count }} typed result pages, 67 quantitative predictions, and 30 named falsification tests — with <a href="{{ '/results/predictions/timing/' | relative_url }}">full pre-registration accounting</a> distinguishing post-dictions, tension-side commitments, and forward forbiddances. These are not all equivalent in status; the site makes status, verification route, and external-acceptance boundaries visible at the page level.</p>
  <div class="v2-grid">
    <a class="v2-tile" href="{{ '/results/problem/hubble-tension-resolved-h-formula/' | relative_url }}">
      <h3>Hubble tension</h3>
      <p>A zero-continuous-parameter readout for the Hubble constant.</p>
      <div class="v2-badge-row"><span class="v2-badge">Physics</span><span class="v2-badge">Prediction</span></div>
    </a>
    <a class="v2-tile" href="{{ '/results/problem/no-dark-matter-particle/' | relative_url }}">
      <h3>No dark matter particle</h3>
      <p>A structural exhaustion claim rather than a new-particle hypothesis.</p>
      <div class="v2-badge-row"><span class="v2-badge">World Readout</span><span class="v2-badge">Falsifiable</span></div>
    </a>
    <a class="v2-tile" href="{{ '/results/problem/homochirality-universality-12-step-derivation/' | relative_url }}">
      <h3>Homochirality</h3>
      <p>A life-sector derivation path tied back to the formal corpus.</p>
      <div class="v2-badge-row"><span class="v2-badge">Life</span><span class="v2-badge">Corpus-linked</span></div>
    </a>
  </div>
  <div class="btn-group section-ctas">
    <a class="btn-secondary" href="{{ '/results/' | relative_url }}">Results Lane</a>
    <a class="btn-ghost" href="{{ '/results/predictions/browse/' | relative_url }}">Browse Predictions</a>
    <a class="btn-ghost" href="{{ '/results/falsifications/browse/' | relative_url }}">Browse Falsification Tests</a>
  </div>
</section>

<section class="content-card homepage-section">
  <p class="v2-kicker">How the system works</p>
  <h2>One Corpus, several public projections</h2>
  <p>Corpus truth lives in the Corpus and Registry. Publications crystallize the Corpus into citable artifacts. Results present current consequence surfaces. Verify exposes formal, empirical, and review routes. TauLib provides the Lean&nbsp;4 formalization projection.</p>
  <div class="v2-system-strip">
    <div class="v2-system-node"><strong>Kernel</strong>Five generators, one operator, and K0-K6 axioms, with the foundational-hinge route.</div>
    <div class="v2-system-node"><strong>Corpus</strong>{{ registry_count }} registry objects, monograph drilldowns, construction spine, foundational hinges, and dependency graph.</div>
    <div class="v2-system-node"><strong>TauLib</strong>Pinned Lean&nbsp;4 formalization with 522 modules, 0 sorry, and 3 custom axioms in Book&nbsp;III bridge territory.</div>
    <div class="v2-system-node"><strong>Results</strong>Landmark Results, World Readouts, Problem Ledger Answers, Recovery Target Status, and Progress Against Agenda.</div>
    <div class="v2-system-node"><strong>Verify</strong>Release Manifest, audit routes, prediction timing, falsification pack, and TCB disclosure.</div>
    <div class="v2-system-node"><strong>Publications</strong>Research Monographs, research papers, supplements, notes, briefings, white papers, release artifacts, and errata.</div>
  </div>
</section>

<section class="content-card homepage-section">
  <p class="v2-kicker">Public inspectability</p>
  <h2>The site asks to be checked, not simply believed</h2>
  <ul>
    <li><strong>TauLib</strong>: public Lean 4 formalization with a sharp axiom and sorry budget.</li>
    <li><strong>Registry</strong>: object-level IDs, dependencies, and status metadata.</li>
    <li><strong>Predictions</strong>: explicit values, observed comparators, and precision tiers.</li>
    <li><strong>Falsification pack</strong>: named experiments and timelines where the framework can fail.</li>
    <li><strong>Errata</strong>: public corrections with stable IDs and current status.</li>
  </ul>
  <div class="btn-group section-ctas">
    <a class="btn-secondary" href="{{ '/verify/' | relative_url }}">Verify</a>
    <a class="btn-ghost" href="{{ '/corpus/registry/' | relative_url }}">Registry</a>
    <a class="btn-ghost" href="{{ '/publications/errata/' | relative_url }}">Errata</a>
  </div>
</section>

<section class="content-card homepage-section">
  <p class="v2-kicker">World readout</p>
  <h2>What the framework says follows, domain by domain</h2>
  <div class="v2-grid">
    <a class="v2-tile" href="{{ '/results/world-readout/mathematics/' | relative_url }}"><h3>Mathematics</h3><p>Foundations, holomorphy, spectral structure, and problem surfaces.</p></a>
    <a class="v2-tile" href="{{ '/results/world-readout/physics/' | relative_url }}"><h3>Physics</h3><p>Microcosm, macrocosm, constants, predictions, and falsification seams.</p></a>
    <a class="v2-tile" href="{{ '/results/world-readout/life/' | relative_url }}"><h3>Life</h3><p>Self-decoding distinctions, biological structure, agency, and persistence.</p></a>
    <a class="v2-tile" href="{{ '/results/world-readout/metaphysics/' | relative_url }}"><h3>Metaphysics</h3><p>Ontology, ethics, consciousness, and the final enrichment layer.</p></a>
  </div>
</section>

<section class="content-card homepage-section">
  <p class="v2-kicker">Artifacts and continuation</p>
  <h2>Read, inspect, follow, and engage</h2>
  <p>The public release surface is not only the Research Monographs. It includes the Conspectus, Monograph Supplements such as the Numerical Physics Ledger, Research Notes, Research Briefings, White Papers, TauLib, assessment protocols, Release Artifacts, and errata. The site makes those surfaces easier to find without turning the homepage into a catalogue.</p>
  <div class="btn-group section-ctas">
    <a class="btn-secondary" href="{{ '/publications/' | relative_url }}">Publications</a>
    <a class="btn-secondary" href="{{ '/impact/' | relative_url }}">Impact</a>
    <a class="btn-ghost" href="{{ '/engage/' | relative_url }}">Engage</a>
  </div>
</section>
