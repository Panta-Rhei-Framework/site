---
layout: homepage
title: "Panta Rhei Research Program"
hero_line: "An independent open research program."
hero_body: "A research program by Dr. Thorsten Fuchs and Anna-Sophie Fuchs, exploring whether one constrained formal kernel can support a unified model of mathematics, physics, life, and metaphysics — with every claim typed, every derivation machine-checked, and every prediction publicly inspectable."
hero_ctas:
  - label: "Get the Books"
    url: /publications/books/
    primary: true
  - label: "Explore the Lean Code"
    url: "https://github.com/Panta-Rhei-Research/taulib"
    variant: lean
  - label: "Explore the Framework"
    url: /framework/about/
  - label: "Browse Claims"
    url: /results/
  - label: "Verify It Yourself"
    url: /verify/
hero_supporting_line: "Fully constructive formal system (~125k lines of Lean 4, no Mathlib dependency)."
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
      url: "https://github.com/Panta-Rhei-Research/taulib"
      external: true
    - title: "Frozen Verification"
      url: "https://github.com/Panta-Rhei-Research/formalization"
      external: true
  meta:
    type: "Landing"
    status: "Canonical"
    updated: "April 2026"
---

{% assign result_count = site.data.results.results | size %}{% assign registry_count = site.data.registry.objects | size %}{% assign book_count = site.data.publications.books | size %}{% assign chapter_count = site.data.publications.chapters | size %}

<div class="content-card homepage-section">
  <svg class="section-icon-corner" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
  <h2>Why this program is built from a constrained kernel</h2>
  <p>The program binds itself to strong constraints. Every mathematical tool is <em>earned</em> from five generators, seven axioms, and one operator&mdash;not imported from existing mathematics. Every scope claim carries an explicit label: established, tau-effective, conjectural, or metaphorical. Every derivation chain is machine-checked in Lean 4.</p>
  <p>The stronger the claimed scope, the stricter the foundation must be. This is not a design choice&mdash;it is a structural necessity. A framework that claims to derive both the Higgs mass and the Categorical Imperative from the same kernel must be maximally constrained, or it is merely telling stories.</p>
  <div class="btn-group section-ctas">
    <a href="{{ '/research-program/about/' | relative_url }}" class="btn-secondary" {% include cta-attrs.html location="section" label="About the Research" href="/research-program/about/" %}>About the Research</a>
    <a href="{{ '/research-program/about/core-design-principles/' | relative_url }}" class="btn-ghost" {% include cta-attrs.html location="section" label="Core Design Principles" href="/research-program/about/core-design-principles/" %}>Core Design Principles</a>
  </div>
</div>

<div class="content-card homepage-section">
  <svg class="section-icon-corner" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
  <h2>The Tau framework</h2>
  <p>Category &tau; begins below ordinary category theory. Five generators (&alpha;, &pi;, &gamma;, &eta;, &omega;) in strict total order, one progression operator (&rho;), and seven axioms (K0&ndash;K6) define a complete, rigid, countable universe. From this kernel, the framework earns its own arithmetic, geometry, analysis, topology, and category theory&mdash;then enriches itself through four layers:</p>
  <ul>
    <li><strong>E<sub>0</sub>&mdash;Mathematics</strong> (Books I&ndash;III): Kernel, holomorphy, spectral structure</li>
    <li><strong>E<sub>1</sub>&mdash;Physics</strong> (Books IV&ndash;V): Microcosm and macrocosm from one constant</li>
    <li><strong>E<sub>2</sub>&mdash;Life</strong> (Book VI): Life as self-decoding distinctions</li>
    <li><strong>E<sub>3</sub>&mdash;Metaphysics</strong> (Book VII): The final self-enrichment</li>
  </ul>
  <p>The master constant &iota;<sub>&tau;</sub> = 2/(&pi;+e) governs all quantitative predictions. Zero free parameters.</p>
  <div class="btn-group section-ctas">
    <a href="{{ '/framework/about/' | relative_url }}" class="btn-secondary" {% include cta-attrs.html location="section" label="Framework Overview" href="/framework/about/" %}>Framework Overview</a>
    <a href="{{ '/verify/taulib/' | relative_url }}" class="btn-ghost" {% include cta-attrs.html location="section" label="TauLib Documentation" href="/verify/taulib/" %}>TauLib Documentation</a>
  </div>
</div>

<div class="content-card homepage-section">
  <svg class="section-icon-corner" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
  <h2>The Claims lane: two readings plus the Physics Ledger</h2>
  <p>The Claims lane presents <strong>250+ typed claims</strong> across four domains, each with explicit epistemic status, each linked to a canonical proof chain in the books and a formalization lane in TauLib. Four complementary inspection surfaces:</p>
  <ul>
    <li><strong>Reading 1 &middot; World Readouts</strong>&mdash;four pages (Mathematics, Physics, Life, Metaphysics) presenting what the framework says the world IS, layer by layer</li>
    <li><strong>Reading 2 &middot; Field Briefings</strong>&mdash;ten discipline-specific briefings, each cross-walked against canonical external lists (Wikipedia&rsquo;s per-discipline open-problems lists and the Clay Millennium Problems)</li>
    <li><strong>Physics Ledger</strong>&mdash;67 zero-parameter numerical predictions + 30 named falsifications, directly testable without accepting the framework&rsquo;s ontological claims</li>
    <li><strong>Browse All Claims</strong>&mdash;the raw catalogue with client-side filters for domain, layer, status, and book</li>
  </ul>
  <p>A selection of flagship claims:</p>
  <ul>
    <li><strong>Dark sector closure</strong> <span class="status-badge status-live">Resolved</span>&mdash;dark matter and dark energy as structural artifacts, not new particles</li>
    <li><strong>Hubble tension</strong> <span class="status-badge status-live">Resolved</span>&mdash;h = 2/3 + &iota;<sub>&tau;</sub>&sup2;/17 at &minus;120 ppm, zero free parameters</li>
    <li><strong>Sub-10 ppm precision</strong> <span class="status-badge status-live">15 predictions</span>&mdash;electron mass (0.025 ppm), sin&sup2;&theta;<sub>W</sub> (&minus;0.65 ppm), Higgs mass (+8.0 ppm)</li>
    <li><strong>Genetic code optimality</strong> <span class="status-badge status-live">Resolved</span>&mdash;top 0.01% for error minimization, derived from BSD-motivic structure</li>
    <li><strong>Categorical Imperative</strong> <span class="status-badge status-live">Resolved</span>&mdash;Kant&rsquo;s CI derived as the unique j-closed fixed point, not postulated</li>
    <li><strong>Panpsychism Excluded</strong> <span class="status-badge status-live">Contradicted</span>&mdash;framework explicitly rules out panpsychism and Orch-OR on structural grounds</li>
  </ul>
  <p>Every claim carries one of five statuses: <strong>Resolved &middot; Partial &middot; Qualitative &middot; Contradicted &middot; Not Addressed</strong>. The typing is not optional&mdash;it is the program&rsquo;s principal epistemic commitment. Three Contradicted stances (No Hawking Radiation, Panpsychism Excluded, ZFC Identity Slippage) show the framework takes falsifiable opposing positions where appropriate. The 67 numerical predictions are <strong>bridge-independent</strong>: they can be compared directly to experimental measurement without accepting deeper ontological claims.</p>
  <div class="btn-group section-ctas">
    <a href="{{ '/results/' | relative_url }}" class="btn-secondary" {% include cta-attrs.html location="section" label="Browse Claims Lane" href="/results/" %}>Browse Claims Lane</a>
    <a href="{{ '/results/predictions/browse/' | relative_url }}" class="btn-secondary" {% include cta-attrs.html location="section" label="67 Predictions" href="/results/predictions/browse/" %}>67 Predictions</a>
    <a href="{{ '/results/falsifications/browse/' | relative_url }}" class="btn-ghost" {% include cta-attrs.html location="section" label="Falsification Pack" href="/results/falsifications/browse/" %}>Falsification Pack</a>
  </div>
</div>

<div class="content-card homepage-section">
  <svg class="section-icon-corner" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
  <h2>The program is public through verification surfaces</h2>
  <p>This is not a program that asks for trust. It is a program that provides inspection routes:</p>
  <ul>
    <li><strong>{{ book_count }} canonical books</strong>&mdash;{{ chapter_count }} chapters in proof-order, available on Amazon KDP</li>
    <li><strong>TauLib</strong>&mdash;450 Lean 4 modules, 125,771 lines, 4,332 machine-checked theorems, 0 sorry in Books I&ndash;VI</li>
    <li><strong>{{ registry_count }} registry objects</strong>&mdash;every definition, theorem, and proposition with dependency graphs</li>
    <li><strong>67 quantitative predictions</strong>&mdash;from one constant, with 15 at sub-10 ppm precision, each filterable by domain, precision tier, and scope</li>
    <li><strong>30 falsification tests (N1&ndash;N30)</strong>&mdash;named experiments (CMB-S4, LZ, DESI, ngEHT), specific timelines, 5&sigma; threshold</li>
    <li><strong>Physics Ledger (free PDF)</strong>&mdash;the complete 156-page numerical scorecard with full derivations, available for download</li>
  </ul>
  <p>The decisive empirical test: CMB-S4 will measure the tensor-to-scalar ratio <em>r</em>. The &tau;-prediction is <em>r</em> = &iota;<sub>&tau;</sub><sup>4</sup> &asymp; 0.0136, testable at 14&sigma; significance. If <em>r</em> is inconsistent, the framework&rsquo;s cosmological predictions fail.</p>
  <div class="btn-group section-ctas">
    <a href="{{ '/publications/books/' | relative_url }}" class="btn-secondary" {% include cta-attrs.html location="section" label="Get the Books" href="/publications/books/" %}>Get the Books</a>
    <a href="{{ '/assets/downloads/physics-ledger.pdf' | relative_url }}" class="btn-secondary" download {% include cta-attrs.html location="section" label="Physics Ledger PDF" href="/assets/downloads/physics-ledger.pdf" %}>Physics Ledger (PDF)</a>
    <a href="{{ '/verify/' | relative_url }}" class="btn-ghost" {% include cta-attrs.html location="section" label="Verify" href="/verify/" %}>Verify</a>
    <a href="{{ '/registry/' | relative_url }}" class="btn-ghost" {% include cta-attrs.html location="section" label="Registry" href="/registry/" %}>Registry</a>
  </div>
</div>

<div class="content-card homepage-section">
  <svg class="section-icon-corner" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>
  <h2>Why this could matter if it holds</h2>
  <p>If the framework holds&mdash;or partially holds&mdash;consequences could propagate into public-good domains. The program&rsquo;s impact lane explores 11 conditional deployment portfolios grounded in 44 companion papers:</p>
  <ul>
    <li><strong>Climate and weather</strong>&mdash;causal-tree legibility for mitigation, adaptation, and resilience planning</li>
    <li><strong>Energy</strong>&mdash;grid optimization, fusion digital twins, renewable integration</li>
    <li><strong>Life sciences</strong>&mdash;precision agriculture, public health, biodiversity monitoring</li>
    <li><strong>Ocean and water</strong>&mdash;marine ecosystem modeling, water security, coastal resilience</li>
  </ul>
  <p>The word <em>if</em> is load-bearing. These are scenario analyses, not predictions of social adoption. The framework must survive empirical testing before any downstream consequence becomes real. The program is independent research&mdash;not yet peer-reviewed in traditional journals. All claims carry explicit scope labels.</p>
  <div class="btn-group section-ctas">
    <a href="{{ '/impact/' | relative_url }}" class="btn-secondary" {% include cta-attrs.html location="section" label="Potential Impact" href="/impact/" %}>Potential Impact</a>
  </div>
</div>

<div class="content-card homepage-section">
  <svg class="section-icon-corner" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
  <h2>Read, inspect, follow, and engage</h2>
  <p>The program can be entered through many routes:</p>
  <ul>
    <li><a href="{{ '/publications/books/' | relative_url }}"><strong>The Seven Books</strong></a>&mdash;the canonical monograph series with DOIs and Amazon links</li>
    <li><a href="{{ '/publications/physics-ledger/' | relative_url }}"><strong>Physics Ledger (free PDF)</strong></a>&mdash;67 predictions + 30 falsifications in one 156-page document</li>
    <li><a href="{{ '/results/' | relative_url }}"><strong>Claims</strong></a>&mdash;250+ typed claims across four domains, in two readings (World Readouts + 10 Field Briefings) plus the Physics Ledger</li>
    <li><a href="{{ '/verify/' | relative_url }}"><strong>Verify</strong></a>&mdash;clone TauLib, run <code>lake build</code>, step through the tours</li>
    <li><a href="{{ '/media/' | relative_url }}"><strong>Media Kit</strong></a>&mdash;for journalists, podcast hosts, reviewers, and institutions</li>
    <li><a href="{{ '/engage/follow-the-research/' | relative_url }}"><strong>Follow the Research</strong></a>&mdash;stay connected with the program&rsquo;s ongoing work</li>
  </ul>
  <p><strong>The enrichment ladder.</strong> For a guided reading path that follows the framework&rsquo;s own architecture, start with the <a href="{{ '/results/prologue/' | relative_url }}">Claims Introduction</a>, then continue through the four world readouts&mdash;<a href="{{ '/results/world-readout/mathematics/' | relative_url }}">Mathematics</a> (E<sub>0</sub>), <a href="{{ '/results/world-readout/physics/' | relative_url }}">Physics</a> (E<sub>1</sub>), <a href="{{ '/results/world-readout/life/' | relative_url }}">Life</a> (E<sub>2</sub>), <a href="{{ '/results/world-readout/metaphysics/' | relative_url }}">Metaphysics</a> (E<sub>3</sub>)&mdash;then the <a href="{{ '/results/fields/biology/' | relative_url }}">ten field briefings</a>, the <a href="{{ '/results/predictions/browse/' | relative_url }}">67 predictions</a>, the <a href="{{ '/results/falsifications/browse/' | relative_url }}">30 falsification tests</a>, and the <a href="{{ '/results/browse/' | relative_url }}">full claims catalogue</a>.</p>
  <p><em>Panta Rhei&mdash;Everything Flows.</em></p>
</div>
