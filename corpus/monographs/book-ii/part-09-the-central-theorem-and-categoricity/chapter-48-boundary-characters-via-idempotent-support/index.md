---
layout: corpus-monograph-chapter
title: "Chapter 48: Boundary Characters via Idempotent Support"
permalink: /corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/chapter-48-boundary-characters-via-idempotent-support/
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
chapter_number: 48
chapter_slug: "chapter-48-boundary-characters-via-idempotent-support"
page_in_book: 279
prev_chapter_url: "/corpus/monographs/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-47-foundation-for-book-iii-s-self-enrichment-ladder/"
prev_chapter_title: "Chapter 47: Foundation for Book~III's Self-Enrichment Ladder"
next_chapter_url: "/corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/chapter-49-hartogs-extension-in-h-tau/"
next_chapter_title: "Chapter 49: Hartogs Extension in H_τ"
summary_short: "Every boundary character of the profinite ring ẑ_τ decomposes uniquely as χ = e₊·χ₊ + e₋·χ₋; the character algebra A_spec(𝕃) is precisely the algebra of idempotent-supported characters — no others exist."
canonical_book_url: /corpus/monographs/book-ii/
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: /corpus/monographs/book-ii/part-09-the-central-theorem-and-categoricity/
canonical_part_title: "Part IX: The Central Theorem and Categoricity"
publication_book_url: /publications/books/book-ii/
legacy_publication_url: /publications/books/book-ii/part-09-the-central-theorem-and-categoricity/chapter-48-boundary-characters-via-idempotent-support/
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

Part VII proved two decisive results: the Idempotent Decomposition Lemma (*II.L07*) splitting every holomorphic map f = e₊ · f₊ + e₋ · f₋ into independent B-channel and C-channel projections, and the Three-Lemma Chain (*II.T33*) establishing that holomorphy is *equivalent to* idempotent support. This chapter turns that equivalence inward. The boundary ring ẑ_τ = lim← ℤ/Pₙℤ and its canonical spectral characters χ₊ (*I.D22*) and χ₋ (*I.D23*) — defined in Book I as probes for the two lobes of the algebraic lemniscate 𝕃 — are restated in the language of idempotent decomposition. Every spectral character valued in the calibrated split-complex codomain H_τ (*II.D35*) admits a unique canonical decomposition χ = e₊ · χ₊ + e₋ · χ₋. The character algebra A_spec(𝕃) is *precisely* the algebra of idempotent-supported characters. This chapter organizes the input side of the Central Theorem: the boundary data, fully structured by idempotent support, ready for the Hartogs extension of Chapter 49.

## What this chapter contributes

**Definition *II.D59*** (Idempotent-Supported Character) specifies spectral characters χ : ẑ_τ → H_τ^cal as ring homomorphisms satisfying additivity, multiplicativity, unitality, and tower coherence (the restriction χₙ := χ mod Pₙ forms a compatible family under the primorial reduction maps). Tower coherence is automatic for any ring homomorphism from a profinite ring: the compatibility condition is simply the defining property of a profinite limit.

**Proposition *II.P14*** (Character Decomposition, also registered as *II.P13* for the preliminary form) proves that every spectral character decomposes canonically as χ = e₊ · χ₊ + e₋ · χ₋, where χ± = e± · χ. The proof uses the bipolar idempotent decomposition of H_τ^cal — since e₊ and e₋ are orthogonal ring idempotents (I.D21) and H_τ^cal ≅ A_τ^(B) × A_τ^(C), every character necessarily factors through this product structure. The two channel characters χ₊ and χ₋ are *independent*: modifying one does not constrain the other. The calibrated scalars ι_τ = 2/(π + e) carry quantitative spectral content that becomes essential when the full isomorphism is assembled in Chapter 52.

The chapter also shows that the *only* spectral characters in Spec(ẑ_τ, H_τ^cal) are idempotent-supported ones — there are no characters that fail to decompose bipolarl. This completeness statement, together with the decomposition, means that A_spec(𝕃) is fully characterized: it is the ring of pairs (χ₊, χ₋) with χ± : ẑ_τ → A_τ^(±), carrying pointwise addition and multiplication inherited from H_τ.

The characters χ₊ and χ₋ function as spectral probes for 𝕃 in exact analogy with Fourier characters on a Pontryagin-dual group: χ₊ detects B-sector spectral content, χ₋ detects C-sector content, and together they form a complete set — no spectral information escapes the pair.

## Lean coverage

Formalization is planned in `BookII.CentralTheorem.BoundaryCharacters`. Targeted proof objects: `idempotent_character_definition` (*II.D59*), `character_decomposition` (*II.P14*, the bipolar splitting), `character_algebra_complete` (no non-idempotent-supported characters exist), and `spectral_probe_completeness` (χ₊ and χ₋ together capture all information). All depend on `BookI.Boundary.SpectralCharacters` and `BookII.Idempotent.DecompositionLemma`.

## Where this leads

Chapter 49 takes each idempotent-supported character and extends it uniquely to the interior of τ³, producing a holomorphic function in H_τ. The extension is built channel-by-channel using the BndLift operator (*II.D36*) from Part VI, and uniqueness follows from Mutual Determination (*II.T27*). This chapter's decomposition χ = e₊ · χ₊ + e₋ · χ₋ is what makes the channel-by-channel extension possible: each channel extends independently.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-02/part09/ch47-boundary-characters-idempotent.tex -->
