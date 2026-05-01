---
layout: corpus-monograph-chapter
title: "Chapter 44: Yoneda Embedding as Theorem"
permalink: /corpus/monographs/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-44-yoneda-embedding-as-theorem/
lane: corpus
v2_lane: corpus
type: "Corpus Monograph Chapter"
status: Canonical
updated: April 2026
publication_type: corpus_monograph_chapter
book_id: "II"
book_slug: "book-ii"
part_number: 8
part_display: "Part VIII"
part_slug: "part-08-self-enrichment-yoneda-and-higher-categories"
chapter_number: 44
chapter_slug: "chapter-44-yoneda-embedding-as-theorem"
page_in_book: 245
prev_chapter_url: "/corpus/monographs/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-43-tau-enriches-over-itself/"
prev_chapter_title: "Chapter 43: τ Enriches Over Itself"
next_chapter_url: "/corpus/monographs/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-45-2-categories-from-iterated-enrichment/"
next_chapter_title: "Chapter 45: 2-Categories from Iterated Enrichment"
summary_short: "The τ-Yoneda embedding y : τ ↪ [τ^op, τ] is a theorem, not abstract nonsense: it stays inside τ, preserves the bipolar splitting, and delivers computable fullness witnesses via the Code/Decode bijection."
canonical_book_url: /corpus/monographs/book-ii/
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: /corpus/monographs/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/
canonical_part_title: "Part VIII: Self-Enrichment, Yoneda, and Higher Categories"
publication_book_url: /publications/books/book-ii/
legacy_publication_url: /publications/books/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-44-yoneda-embedding-as-theorem/
right_rail:
  related:
  - title: "Book II: Categorical Holomorphy"
    url: /corpus/monographs/book-ii/
  - title: "Part VIII: Self-Enrichment, Yoneda, and Higher Categories"
    url: /corpus/monographs/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/
  - title: "Research Monograph artifact"
    url: /publications/books/book-ii/
  - title: "Registry"
    url: /registry/books/book-ii/
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part VIII"
    layer: "E₀ Mathematics"
    updated: "April 2026"
---

In classical category theory the Yoneda lemma is a purely formal result: it holds for any locally small category and requires nothing beyond the existence of composition and identities. In Category τ the Yoneda embedding y : τ ↪ [τ^op, τ] is a **theorem** (*II.T36*) with genuine content. Three features distinguish it from its classical cousin: (i) the target category [τ^op, τ] lives inside τ itself, not in an external universe — a consequence of self-enrichment (*II.D53*); (ii) the embedding preserves the bipolar structure of every morphism — a consequence of *II.P11*; and (iii) fullness is witnessed computably by the Code/Decode bijection (*II.T35*), not merely asserted to exist. The proof pivots on a single conceptual identification: **probe naturality** — the condition that characterized holomorphy in Part II (*II.R12*) — is *exactly* the Yoneda condition.

## What this chapter contributes

**Lemma *II.L11*** (Probe Naturality ⟺ Yoneda) establishes the triad at the chapter's heart: three conditions on a morphism φ : A → B are equivalent — (PN) postcomposition by φ is natural in the probe object P, (Hol) the natural transformation y(φ) preserves the bipolar sector structure of each Hom object, and (Yon) y(φ) is determined by its evaluation at id_A. The equivalence (PN) ↔ (Hol) uses the bipolar decomposition of [P,A] and [P,B]; (Hol) ↔ (Yon) is the enriched Yoneda bijection; (Yon) ↔ (PN) uses associativity of composition in τ, which is itself a theorem (*II.T28*) rather than an axiom.

**Theorem *II.T36*** assembles four properties of the Yoneda functor y. (1) *Well-definedness*: y(A) = [−,A] is a functor τ^op → τ because self-enrichment makes each [P,A] a τ-object. (2) *Faithfulness*: if y(φ) = y(ψ) then evaluation at id_A forces φ = ψ. (3) *Fullness*: every bipolar-preserving natural transformation η : y(A) ⇒ y(B) arises from a unique φ := η_A(id_A); the Code/Decode bijection provides the computable witness. (4) *Bipolar preservation*: y(e₊ · φ₊ + e₋ · φ₋) = e₊ · y(φ₊) + e₋ · y(φ₋), using the bilinearity of the program monoid over the e±-splitting.

The chapter also introduces the **tau-exponential** E_τ(A) := [A,A], the endofunctor that promotes E₀⁽⁰⁾-objects to E₀⁽¹⁾-objects. Every τ-object carries a canonical self-describing datum — the Code of its own identity morphism — as a distinguished element of its tau-exponential. The Code map (*II.D51*) and the Yoneda bijection are identified as the same isomorphism viewed from different perspectives: boundary coefficient streams are the stage-by-stage evaluations of the natural transformation y(φ).

The chapter explains why holomorphy is the most primitive structural condition in τ: the Yoneda embedding is the first feature of an enriched category, existing before continuity, topology, or geometry are defined. Holomorphy, as probe naturality at the enriched level, therefore precedes all derived structure — the inverted dependency chain (holomorphy → continuity → topology → geometry) is a consequence of enriched category theory applied to a self-enriched category.

## Lean coverage

Formalization is planned in `BookII.Enrichment.YonedaTheorem`. Targeted proof objects: `probe_yoneda_check` (*II.L11*), `yoneda_faithful_check` and `yoneda_full_check` (*II.T36*, using *II.T35* as constructive witness), `yoneda_bipolar_check` (bipolar preservation), and `probe_naturality_structural` (structural rather than computational character of PN). All proofs compile without `sorry` in Lean 4.

## Where this leads

The Yoneda embedding feeds directly into the Central Theorem of Part IX. Boundary characters on 𝕃 are natural transformations in [τ^op, τ]; Hartogs extension lifts each to an interior function; the ω-germ transformer identification follows; and *II.T36* is what converts ω-germ transformers into holomorphic functions — the categorical identification inside τ rather than a set-theoretic argument. Chapter 45 applies the Yoneda infrastructure to ask what happens when self-enrichment is iterated, yielding the 2-categorical structure of τ.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part08/ch43-yoneda-theorem.tex -->
