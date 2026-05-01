---
layout: "program-doc"
title: "Mathematics Glossary — 41 entries, 7 categories"
permalink: "/results/mathematics/glossary/"
lane: "results"
v2_lane: "results"
type: "Glossary Index"
status: "Canonical"
domain: "mathematics"
summary_short: "Glossary for the τ-framework's mathematics domain — 41 canonical entries grouped by category."
generated_from: "corpus/mathematics-glossary"
projection_version: "v0.1"
do_not_edit: true
---

The 21-entry mathematics glossary covers the τ-framework's foundational kernel (Books I–III): postulates K0–K6, canonical definitions (ι_τ, τ-categorical, window-algebra, Yoneda-as-theorem, rank coordinates), Books I–II load-bearing theorems (Hyperfactorization, Rigidity, Categoricity, Central Theorem at rank (3, 15), Yoneda enrichment ladder), the three Book-III conjectural axioms (bridge functor, spectral correspondence O(3), Grand GRH adelic), structures (spectrum functor, holomorphy tower, self-enrichment), and the τ-object class. Each entry carries a mathematical-content section with the orthodox statement, Mathlib bridge, and the categoricity argument fixing the concept inside the kernel. Pilot sealed at v0.4.

<div class="notice note"><strong>Glossary contract.</strong> Every entry below carries a 4-section structure: τ-definition (categorical invariant + primary registry anchor), τ-derivation (chain of registry steps), domain-specific Section 3, and Lean coverage. The structure is uniform across all three domains so cross-references resolve unambiguously.</div>

## Browse by category

## Axiom <span class="muted">(3)</span>

<ul class="v2-grid v2-card-list">
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-A01-bridge-functor/' | relative_url }}">Bridge functor axiom <code>B</code></a></h3>
      <p>The Bridge functor axiom (III.D71) is the first of three custom axioms in TauLib beyond Mathlib's trusted base. It asserts the existence of a structure-preserving functor betwee…</p>
      <p class="muted"><code>MathG-A01-bridge-functor</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-A02-spectral-correspondence/' | relative_url }}">Spectral correspondence O(3) axiom <code>SC_{O(3)}</code></a></h3>
      <p>The Spectral correspondence O(3) axiom (III.T18, surfaced as A02 in this glossary) is the second custom axiom in TauLib. It asserts that the τ-spectral correspondence — the τ-in…</p>
      <p class="muted"><code>MathG-A02-spectral-correspondence</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-A03-grand-grh-adelic/' | relative_url }}">Grand GRH (adelic) axiom <code>GRH_{adelic}</code></a></h3>
      <p>The Grand GRH (adelic) axiom (III.D31) is the third custom axiom in TauLib. It asserts that the Prime Polarity Scaling Theorem (III.T20) extends to all automorphic L-functions i…</p>
      <p class="muted"><code>MathG-A03-grand-grh-adelic</code></p>
    </article>
  </li>
</ul>

## Definition <span class="muted">(16)</span>

<ul class="v2-grid v2-card-list">
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-D01-iota-tau/' | relative_url }}">Master constant ι_τ <code>ι_τ</code></a></h3>
      <p>ι_τ = 2/(π + e) is the structural fixed point of the boundary holonomy algebra H_∂[ω] over the categorical kernel τ. It is a theorem about τ, not a parameter — uniquely determin…</p>
      <p class="muted"><code>MathG-D01-iota-tau</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-D02-tau-categorical/' | relative_url }}">τ-categorical structure <code>τ-cat</code></a></h3>
      <p>The τ-categorical structure is the categorical content of the τ-kernel: τ as a category in its own right, equipped with the τ-site topology that turns it into an earned topos. T…</p>
      <p class="muted"><code>MathG-D02-tau-categorical</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-D03-window-algebra/' | relative_url }}">Window-algebra integers W_n(k) <code>W_n(k)</code></a></h3>
      <p>The window-algebra integers W_n(k) are the Book-II numerical invariants of the τ-categorical structure at rank coordinates (n, k). For load-bearing pairs (W₃(4) = 5, W₅(3) = 19,…</p>
      <p class="muted"><code>MathG-D03-window-algebra</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-D04-yoneda-as-theorem/' | relative_url }}">Yoneda-as-theorem under self-enrichment <code>Y</code></a></h3>
      <p>Yoneda-as-theorem (II.D50) is the τ-framework's distinctive treatment of the Yoneda lemma: rather than appearing as an external categorical fact applied to τ, the Yoneda embeddi…</p>
      <p class="muted"><code>MathG-D04-yoneda-as-theorem</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-D05-rank-coordinates/' | relative_url }}">Rank coordinates (n, k) <code>(n, k)</code></a></h3>
      <p>Rank coordinates (n, k) are the indexing scheme used throughout Books I–II to locate τ-categorical content along two structural axes: n is the prime-rank index (which prime-numb…</p>
      <p class="muted"><code>MathG-D05-rank-coordinates</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-D06-truth4-logic/' | relative_url }}">Truth4 Logic <code>T4</code></a></h3>
      <p>Truth4 Logic (I.D21) is the τ-internal four-valued logic — extending classical bivalence (true/false) with the structural truth values reflecting the kernel's bipolar polarity. …</p>
      <p class="muted"><code>MathG-D06-truth4-logic</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-D07-4-plus-1-sector/' | relative_url }}">4+1 Sector Decomposition <code>(D, A, B, C, ω)</code></a></h3>
      <p>The 4+1 Sector Decomposition (III.D13) decomposes τ-categorical content into five canonical sectors: four 'analytic' sectors (D, A, B, C) plus the closed 'ω' sector. The 4+1 str…</p>
      <p class="muted"><code>MathG-D07-4-plus-1-sector</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-D08-five-generators-def/' | relative_url }}">Five Generators (definition) <code>{g_1,…,g_5}</code></a></h3>
      <p>The Five Generators definition (I.D01) names the five canonical generators of the τ-kernel as a single bundled definition, complementing the K01–K06 axiomatization of MathG-K02.…</p>
      <p class="muted"><code>MathG-D08-five-generators-def</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-D09-calibrated-split-complex/' | relative_url }}">Calibrated Split-Complex Codomain <code>ℝ[j]_cal</code></a></h3>
      <p>The Calibrated Split-Complex Codomain (II.D35) is the split-complex algebra ℝ[j]/(j²−1) equipped with the τ-categorical calibration — a graded structure on real and j-imaginary …</p>
      <p class="muted"><code>MathG-D09-calibrated-split-complex</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-D10-split-complex-scalars/' | relative_url }}">Split-Complex Scalars <code>ℝ[j]</code></a></h3>
      <p>The Split-Complex Scalars (I.D20) are the elements of ℝ[j]/(j²−1) treated as the canonical scalar algebra of the τ-framework. Every τ-categorical scalar — including ι_τ, the ran…</p>
      <p class="muted"><code>MathG-D10-split-complex-scalars</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-D11-stage-k-cylinder/' | relative_url }}">Stage-k Cylinder <code>Cyl_k</code></a></h3>
      <p>The Stage-k Cylinder (II.D10) is the τ-categorical analogue of the cylinder construction at depth k along the K1 strict-order direction. It packages the rank-(n, k) data into a …</p>
      <p class="muted"><code>MathG-D11-stage-k-cylinder</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-D12-progression-operator/' | relative_url }}">Progression Operator ρ <code>ρ</code></a></h3>
      <p>The Progression Operator ρ (I.D02) is the τ-internal advancement operator on kernel atoms — the canonical step that lifts content from one K1 strict-order position to the next. …</p>
      <p class="muted"><code>MathG-D12-progression-operator</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-D13-diagonal-discipline/' | relative_url }}">Diagonal Discipline <code>Δ-disc</code></a></h3>
      <p>The Diagonal Discipline (I.D03) is the τ-internal coherence rule: every τ-categorical morphism that factors through the diagonal Δ : A → A × A must commute with K3 composition a…</p>
      <p class="muted"><code>MathG-D13-diagonal-discipline</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-D14-stone-space/' | relative_url }}">τ-Stone Space <code>Stone_τ</code></a></h3>
      <p>The τ-Stone Space (II.D14) is the τ-categorical analogue of the classical Stone space — the labelled topological space underlying the K2 boundary axiom. It is the structural env…</p>
      <p class="muted"><code>MathG-D14-stone-space</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-D15-boundary-ring/' | relative_url }}">Boundary Ring and Scalars <code>B_τ</code></a></h3>
      <p>The Boundary Ring (I.D19) is the τ-internal commutative ring on the K2 labelled boundary, with the split-complex scalars (D10) as its scalar algebra. The ring structure carries …</p>
      <p class="muted"><code>MathG-D15-boundary-ring</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-D16-ultrametric-distance/' | relative_url }}">τ-Ultrametric Distance <code>d_τ</code></a></h3>
      <p>The τ-Ultrametric Distance (II.D13) is the τ-categorical metric on the boundary, satisfying the strong triangle inequality d(x,z) ≤ max(d(x,y), d(y,z)) — the ultrametric propert…</p>
      <p class="muted"><code>MathG-D16-ultrametric-distance</code></p>
    </article>
  </li>
</ul>

## Lemma <span class="muted">(1)</span>

<ul class="v2-grid v2-card-list">
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-L01-idempotent-decomposition/' | relative_url }}">Idempotent Decomposition Lemma <code>Idem-decomp</code></a></h3>
      <p>The Idempotent Decomposition Lemma (II.L07) is the Book-II structural result that every τ-categorical content decomposes orthogonally into idempotent components. With 19 incomin…</p>
      <p class="muted"><code>MathG-L01-idempotent-decomposition</code></p>
    </article>
  </li>
</ul>

## Object <span class="muted">(2)</span>

<ul class="v2-grid v2-card-list">
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-O01-tau-object/' | relative_url }}">Generic τ-object <code>A ∈ τ</code></a></h3>
      <p>A generic τ-object is an inhabitant of the τ-categorical kernel — an object of the (∞, 1)-category τ that arises from finite K1–K5 composition (closed under K6). Each τ-object c…</p>
      <p class="muted"><code>MathG-O01-tau-object</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-O02-window-object/' | relative_url }}">Window-algebra object <code>W_n(k)-obj</code></a></h3>
      <p>A window-algebra object is the categorical presentation of a window in the ABCD coordinate chart at rank coordinate (n, k). It is a τ-object (O01) carrying the K1-iteration dept…</p>
      <p class="muted"><code>MathG-O02-window-object</code></p>
    </article>
  </li>
</ul>

## Postulate <span class="muted">(3)</span>

<ul class="v2-grid v2-card-list">
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-K01-universe-postulate/' | relative_url }}">The Universe Postulate (K0) <code>τ</code></a></h3>
      <p>The Universe Postulate (I.K0) is the foundational axiom of the τ-framework: there exists a small (∞, 1)-category τ — the categorical kernel — that supports the five canonical ge…</p>
      <p class="muted"><code>MathG-K01-universe-postulate</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-K02-five-generators/' | relative_url }}">The five canonical generators (K1–K5) <code>K1–K5</code></a></h3>
      <p>K1–K5 are the five canonical generators of the τ-kernel — strict order, labelled boundary, composition, boundary identification, and generator closure. They are the structural a…</p>
      <p class="muted"><code>MathG-K02-five-generators</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-K03-no-omega-axiom/' | relative_url }}">The no-ω axiom (K6) <code>K6</code></a></h3>
      <p>K6 is the closure axiom of the τ-kernel: there is no sixth generator. Any candidate sixth atom must reduce to a finite combination of K1–K5. K6 is what makes the τ-kernel finite…</p>
      <p class="muted"><code>MathG-K03-no-omega-axiom</code></p>
    </article>
  </li>
</ul>

## Structure <span class="muted">(3)</span>

<ul class="v2-grid v2-card-list">
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-S01-spectrum-functor/' | relative_url }}">Spectrum functor <code>Spec</code></a></h3>
      <p>The spectrum functor (III.D81) is the τ-internal functor sending each τ-categorical object to its associated spectral data — the analogue of the algebraic-geometric Spec functor…</p>
      <p class="muted"><code>MathG-S01-spectrum-functor</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-S02-holomorphy-tower/' | relative_url }}">Book I holomorphy tower <code>Hol_τ</code></a></h3>
      <p>The holomorphy tower (I.D96) is the Book-I structural ladder of holomorphy refinements on the τ-categorical kernel. It exhibits a graded sequence of τ-internal holomorphic objec…</p>
      <p class="muted"><code>MathG-S02-holomorphy-tower</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-S03-self-enrichment/' | relative_url }}">Self-enrichment construction <code>τ-enr</code></a></h3>
      <p>The self-enrichment construction (II.D53) equips τ with the structure of a category enriched over itself. Hom-sets in τ become τ-internal objects rather than external Set-elemen…</p>
      <p class="muted"><code>MathG-S03-self-enrichment</code></p>
    </article>
  </li>
</ul>

## Theorem <span class="muted">(13)</span>

<ul class="v2-grid v2-card-list">
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-T01-hyperfactorization/' | relative_url }}">Hyperfactorization theorem <code>Hyperfact</code></a></h3>
      <p>The Hyperfactorization theorem (I.T04) is the Book-I structural result that every τ-categorical morphism admits a unique hyperfactorization: a canonical decomposition through th…</p>
      <p class="muted"><code>MathG-T01-hyperfactorization</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-T02-rigidity-non-omega/' | relative_url }}">Rigidity of τ (non-ω) <code>Rigid_τ</code></a></h3>
      <p>The Rigidity theorem (I.T07) states that the τ-kernel admits no non-trivial automorphisms — every endomorphism of τ that fixes K0–K6 is the identity. Combined with the Categoric…</p>
      <p class="muted"><code>MathG-T02-rigidity-non-omega</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-T03-categoricity-non-omega/' | relative_url }}">Categoricity of τ (non-ω) <code>Cat_τ</code></a></h3>
      <p>The Categoricity theorem (I.T08) states that any two structures satisfying the τ-kernel axioms K0 + K1–K6 are canonically equivalent. Together with the Rigidity theorem (T02 / I…</p>
      <p class="muted"><code>MathG-T03-categoricity-non-omega</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-T04-central-theorem/' | relative_url }}">Central theorem at rank (3, 15) <code>T_{(3,15)}</code></a></h3>
      <p>The Central theorem at rank (3, 15) (II.T40) is the Book-II structural categoricity result that pins down the master constant ι_τ. The theorem asserts that the τ-categorical str…</p>
      <p class="muted"><code>MathG-T04-central-theorem</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-T05-yoneda-enrichment/' | relative_url }}">Yoneda enrichment ladder <code>Y_{enrich}</code></a></h3>
      <p>The Yoneda enrichment ladder (II.T36) is the Book-II theorem that lifts the pre-Yoneda embedding (D04 / II.D50) to a full self-enrichment of τ. The ladder exhibits a sequence of…</p>
      <p class="muted"><code>MathG-T05-yoneda-enrichment</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-T06-prime-polarity/' | relative_url }}">Prime Polarity Theorem <code>PP</code></a></h3>
      <p>The Prime Polarity Theorem (I.T05) is the most-referenced kernel result in Books I–III: it classifies every prime p with respect to the τ-categorical kernel into a polarity sect…</p>
      <p class="muted"><code>MathG-T06-prime-polarity</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-T07-split-complex-forced/' | relative_url }}">Split-Complex Forced <code>SCF</code></a></h3>
      <p>The Split-Complex Forced theorem (I.T10) proves that the τ-kernel forces the boundary algebra to be the split-complex numbers ℝ[j]/(j²−1) — not the complex numbers ℝ[i]/(i²+1), …</p>
      <p class="muted"><code>MathG-T07-split-complex-forced</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-T08-crt-coherence/' | relative_url }}">CRT Coherence Constraint <code>CRT-coh</code></a></h3>
      <p>The CRT Coherence Constraint (I.T18) is the τ-internal Chinese Remainder Theorem analogue: it asserts that the τ-categorical kernel decomposes coherently across coprime factor s…</p>
      <p class="muted"><code>MathG-T08-crt-coherence</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-T09-algebraic-lemniscate/' | relative_url }}">Algebraic Lemniscate <code>Lem</code></a></h3>
      <p>The Algebraic Lemniscate (I.D18) is the canonical 1-dimensional boundary structure on the τ-categorical kernel — a real-algebraic curve with two crossing branches (the lemniscat…</p>
      <p class="muted"><code>MathG-T09-algebraic-lemniscate</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-T10-crt-decomposition/' | relative_url }}">CRT Decomposition Theorem <code>CRT-decomp</code></a></h3>
      <p>The CRT Decomposition Theorem (III.T10) generalizes the Book I CRT Coherence Constraint (T08) to spectral data: τ-spectral content decomposes coherently across coprime adelic pl…</p>
      <p class="muted"><code>MathG-T10-crt-decomposition</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-T11-mutual-determination/' | relative_url }}">Mutual Determination (5-Way Equivalence) <code>5≡</code></a></h3>
      <p>The Mutual Determination theorem (II.T27) is the Book II equivalence statement: five distinct presentations of τ-categorical content — boundary, interior, spectrum, lemniscate, …</p>
      <p class="muted"><code>MathG-T11-mutual-determination</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-T12-global-hartogs/' | relative_url }}">Global Hartogs Extension <code>Hartogs</code></a></h3>
      <p>The Global Hartogs Extension theorem (I.T31) is the τ-categorical analogue of the classical Hartogs extension principle, lifted to the holomorphy tower (S02). It asserts that ev…</p>
      <p class="muted"><code>MathG-T12-global-hartogs</code></p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/results/mathematics/glossary/MathG-T13-spectral-trichotomy/' | relative_url }}">Spectral Trichotomy Lemma <code>(B,I,S)</code></a></h3>
      <p>The Spectral Trichotomy Lemma (III.T14) classifies every τ-spectral datum into one of exactly three sectors: B (boundary-type), I (interior-type), or S (singular-type). The tric…</p>
      <p class="muted"><code>MathG-T13-spectral-trichotomy</code></p>
    </article>
  </li>
</ul>
