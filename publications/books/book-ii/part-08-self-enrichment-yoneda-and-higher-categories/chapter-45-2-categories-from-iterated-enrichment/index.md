---
layout: publication-chapter
title: "Chapter 45: 2-Categories from Iterated Enrichment"
permalink: /publications/books/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-45-2-categories-from-iterated-enrichment/
lane: publications
publication_type: chapter
book_id: "II"
book_slug: "book-ii"
part_number: 8
part_display: "Part VIII"
part_slug: "part-08-self-enrichment-yoneda-and-higher-categories"
chapter_number: 45
chapter_slug: "chapter-45-2-categories-from-iterated-enrichment"
page_in_book: 253
prev_chapter_url: "/publications/books/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-44-yoneda-embedding-as-theorem/"
prev_chapter_title: "Chapter 44: Yoneda Embedding as Theorem"
next_chapter_url: "/publications/books/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-46-s-self-describing-structure/"
next_chapter_title: "Chapter 46: 's Self-Describing Structure"
summary_short: "the relevant chapter established that τ enriches over itself: the morphism space Hom(A,B) is itself an object of τ (II.D53), equipped with…"
canonical_book_url: "/publications/books/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/publications/books/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/"
canonical_part_title: "Part VIII: Self-Enrichment, Yoneda, and Higher Categories"
right_rail:
  related:
  - title: "Book II: Categorical Holomorphy"
    url: /publications/books/book-ii/
  - title: "Part VIII: Self-Enrichment, Yoneda, and Higher Categories"
    url: /publications/books/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/
  - title: Registry
    url: /registry/books/book-ii/
  meta:
    type: Chapter
    book: "Book II"
    part: "Part VIII"
    layer: "E₀ Mathematics"
    updated: April 2026
---


the relevant chapter
established that τ enriches over itself:
the morphism space Hom(A,B)
is itself an object of τ (II.D53),
equipped with bipolar decomposition
Hom(A,B) = e_+ · Hom_+(A,B)
+ e_- · Hom_-(A,B) (II.P11).
the relevant chapter
proved the Yoneda embedding τ ↪ [τ^op, τ]
as a *theorem* (II.T36).
This chapter asks:
what happens when we iterate?
Since Hom(A,B) is a τ-object,
and τ enriches over itself,
we can form
Hom(Hom(A,B), Hom(C,D))—morphisms
between morphisms.
These are **2-morphisms**,
and they organize into a **2-categorical structure**
on τ.
The key facts are:
(1) the 2-category τ₂ is well-defined
(the relevant definition, II.D55);
(2) 2-morphisms inherit bipolar decomposition
from the split-complex codomain
(the relevant definition, II.D56);
(3) the construction iterates to produce
n-morphisms for each finite n
(Proposition [prop:enrichment-iteration], II.P12);
(4) this is the concrete realization
of the E₀ → E₁ transition
in the enrichment frontier (I.D82, Book I).
The honest limitation:
we have earned the 2-categorical structure
and, in principle, the finite iteration to n-categories.
We have *not* earned
an ∞-categorical structure.
The passage from finite iteration
to a genuine ∞-category
requires coherence data at all levels simultaneously,
which belongs to the enrichment ladder's
E₁ → E₂ transition—the domain of Book III.
