---
layout: "program-doc"
title: "Mathematics Glossary — 21 entries, 6 categories"
permalink: "/results/mathematics/glossary/"
lane: "results"
v2_lane: "results"
type: "Glossary Index"
status: "Canonical"
domain: "mathematics"
summary_short: "Glossary for the τ-framework's mathematics domain — 21 canonical entries grouped by category."
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

## Definition <span class="muted">(5)</span>

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

## Theorem <span class="muted">(5)</span>

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
</ul>
