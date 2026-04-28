---
layout: "corpus-monograph-chapter"
title: "Chapter 44: Yoneda Embedding as Theorem"
permalink: "/corpus/monographs/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-44-yoneda-embedding-as-theorem/"
lane: "corpus"
v2_lane: "corpus"
type: "Corpus Monograph Chapter"
status: "Canonical"
updated: "April 2026"
publication_type: "corpus_monograph_chapter"
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
summary_short: "In classical category theory, the Yoneda lemma holds for *any* locally small category — it is purely formal, requiring nothing about the objects or morphisms…"
canonical_book_url: "/corpus/monographs/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/corpus/monographs/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/"
canonical_part_title: "Part VIII: Self-Enrichment, Yoneda, and Higher Categories"
publication_book_url: "/publications/books/book-ii/"
legacy_publication_url: "/publications/books/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-44-yoneda-embedding-as-theorem/"
right_rail:
  related:
    -
      title: "Book II: Categorical Holomorphy"
      url: "/corpus/monographs/book-ii/"
    -
      title: "Part VIII: Self-Enrichment, Yoneda, and Higher Categories"
      url: "/corpus/monographs/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/"
    -
      title: "Research Monograph artifact"
      url: "/publications/books/book-ii/"
    -
      title: "Registry"
      url: "/registry/books/book-ii/"
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book II"
    part: "Part VIII"
    layer: "E₀ Mathematics"
    updated: "April 2026"
generated_from: "corpus/monograph-projections"
projection_version: "v0.1"
canonical_source: "corpus/monograph-projections"
do_not_edit: true
---

In classical category theory,
the Yoneda lemma holds for *any* locally small category —
it is purely formal, requiring nothing about
the objects or morphisms beyond their existence.
In Category τ, the Yoneda embedding
y : τ ↪ [τ^op, τ]
is a **theorem** (II.T36),
not an abstract generality.
Three features distinguish the τ-Yoneda
from its classical cousin:
(i) the target category [τ^op, τ]
lives inside τ itself (self-enrichment, II.D53),
not in an external universe of sets;
(ii) the embedding preserves the bipolar structure
(II.P11);
(iii) fullness is witnessed by the Code/Decode bijection
(II.T35), which provides computable, finite-stage certificates.
The proof rests on a single observation:
**probe naturality** — the condition
that characterized holomorphy in Part II
(Remark [rem:probe-naturality], II.R12) —
is *exactly* the Yoneda condition
(Lemma [lem:probe-yoneda], II.L11).
Holomorphy, probe naturality, and Yoneda representability
are three names for the same structural phenomenon.
This is the deep reason that holomorphy
is primitive in Category τ.
