---
layout: corpus-monograph-chapter
title: "Chapter 49: Hartogs Extension in H_τ"
permalink: /corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/chapter-49-hartogs-extension-in-h-tau/
lane: corpus
v2_lane: corpus
type: "Corpus Monograph Chapter"
status: Canonical
updated: April 2026
publication_type: corpus_monograph_chapter
book_id: "II"
book_slug: "book-ii"
part_number: 9
part_display: "Part IX"
part_slug: "part-09-the-central-theorem-and-categoricity"
chapter_number: 49
chapter_slug: "chapter-49-hartogs-extension-in-h-tau"
page_in_book: 287
prev_chapter_url: "/corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/chapter-48-boundary-characters-via-idempotent-support/"
prev_chapter_title: "Chapter 48: Boundary Characters via Idempotent Support"
next_chapter_url: "/corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/chapter-50-extensions-are-omega-germ-transformers/"
next_chapter_title: "Chapter 50: Extensions Are ω-Germ Transformers"
summary_short: "Every idempotent-supported boundary character extends uniquely to a τ-holomorphic function on τ³ valued in H_τ; uniqueness follows from bipolar channel independence via both Code/Decode and Mutual Determination."
canonical_book_url: /corpus/monographs/book-ii/
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: /corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/
canonical_part_title: "Part IX: The Central Theorem and Categoricity"
publication_book_url: /publications/books/book-ii/
legacy_publication_url: /publications/books/book-ii/part-09-the-central-theorem-and-categoricity/chapter-49-hartogs-extension-in-h-tau/
right_rail:
  related:
  - title: "Book II: Categorical Holomorphy"
    url: /corpus/monographs/book-ii/
  - title: "Part IX: The Central Theorem and Categoricity"
    url: /corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/
  - title: "Research Monograph artifact"
    url: /publications/books/book-ii/
  - title: "Registry"
    url: /registry/books/book-ii/
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part IX"
    layer: "E₀ Mathematics"
    updated: "April 2026"
---

Chapter 48 organized the boundary ring characters as idempotent-supported objects (*II.D59*): every character decomposes canonically as χ = e₊ · χ₊ + e₋ · χ₋ (*II.P13*). This chapter proves that each such character **extends uniquely** to a τ-holomorphic function on the interior of τ³, with the extension valued in the split-complex codomain H_τ rather than in classical ℂ. The mechanism is entirely internal to τ — no Cauchy integral, no ∂̄-equation, no classical several-complex-variables machinery is used. The construction has two stages: the Extension Lemma (*II.L12*) builds the extension channel-by-channel using the BndLift operator from Part VI; the Hartogs Extension Uniqueness Theorem (*II.T37*) proves that no other extension exists. Both the existence and uniqueness arguments exploit **bipolar channel independence**: each channel extends independently of the other, and independence leaves no room for alternatives.

## What this chapter contributes

**Lemma *II.L12*** (Extension in H_τ) constructs the Hartogs extension f_χ of a character χ = e₊ · χ₊ + e₋ · χ₋ by applying the BndLift_n operator (*II.D36*) to each channel separately. At stage n, BndLift_n carries boundary data at stage n to interior data at stage n+1. The channel-by-channel extension produces a tower-coherent family (f_χ^(n))_{n≥1} that converges, in the inverse limit, to a unique element of 𝒪(τ³). The H_τ-valued structure is inherited: each BndLift step preserves the split-complex codomain, so the full extension lives in H_τ^cal.

**Theorem *II.T37*** (Hartogs Extension Uniqueness) proves that f_χ is the *only* τ-holomorphic function on τ³ whose boundary restriction equals χ. Two independent arguments establish uniqueness. The first uses the Code/Decode bijection (*II.T35*): any two extensions with the same boundary data have the same boundary coefficient stream (Code is injective), and Decode reconstructs a unique interior function from that stream. The second, more illuminating argument uses Mutual Determination (*II.T27*): the five-way equivalence (refinement tail, spectral tail, ω-germ, boundary character, Hartogs continuation) shows that any holomorphic datum is completely determined by any one of its five representations. A boundary character *is* a holomorphic function, with no freedom left.

Both arguments exploit the same structural feature: **bipolar channel independence**. The B-channel extension f_χ₊ is determined entirely by χ₊ and is orthogonal to the C-channel — e₊ · f_χ₋ = 0. No cross-channel coupling exists. There is no room for an alternative extension.

This chapter establishes the **boundary → interior** direction of the Central Theorem. Every element of A_spec(𝕃) has a unique pre-image in 𝒪(τ³): the extension map χ ↦ f_χ is injective. Chapter 52 will prove that it is also surjective (every interior holomorphic function restricts to a boundary character), assembling the full isomorphism 𝒪(τ³) ≅ A_spec(𝕃).

## Lean coverage

Formalization is planned in `BookII.CentralTheorem.HartogsExtension`. Targeted proof objects: `extension_lemma` (*II.L12*, channel-by-channel BndLift construction), `hartogs_uniqueness` (*II.T37*, two independent proofs — one via Code/Decode, one via Mutual Determination), and `bipolar_independence_forces_uniqueness` (the structural explanation linking both proofs). All depend on `BookII.Part6.BndLift` and `BookII.Part7.MutualDetermination`.

## Where this leads

Chapter 50 identifies the extensions f_χ as ω-germ transformers — the algebraic objects from Book I Part XIII. This identification is the second link in the Central Theorem chain: boundary characters →^{II.T37} Hartogs extensions →^{II.T38} ω-germ transformers. Chapter 51 then closes the loop by applying the Yoneda theorem to prove that ω-germ transformers *are* τ-holomorphic functions, completing the four-bijection assembly that yields the Central Theorem.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part09/ch48-hartogs-extension-h-tau.tex -->
