---
layout: publication-chapter
title: "Chapter 43: τ Enriches Over Itself"
permalink: /publications/books/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-43-tau-enriches-over-itself/
lane: publications
publication_type: chapter
book_id: "II"
book_slug: "book-ii"
part_number: 8
part_slug: "part-08-self-enrichment-yoneda-and-higher-categories"
chapter_number: 43
chapter_slug: "chapter-43-tau-enriches-over-itself"
page_in_book: 237
prev_chapter_url: "/publications/books/book-ii/part-07-regularity-and-mutual-determination/chapter-42-code-decode-and-diagonal-protection/"
prev_chapter_title: "Chapter 42: Code/Decode and Diagonal Protection"
next_chapter_url: "/publications/books/book-ii/part-08-self-enrichment-yoneda-and-higher-categories/chapter-44-yoneda-embedding-as-theorem/"
next_chapter_title: "Chapter 44: Yoneda Embedding as Theorem"
summary_short: "In most categories, morphism spaces are **external**: $\\Hom(A,B)$ is a set, living in the ambient category $Set$ rather than in the category under study. An…"
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


In most categories, morphism spaces are **external**:
$\Hom(A,B)$ is a set,
living in the ambient category $Set$
rather than in the category under study.
An *enriched* category replaces these external sets
with **internal objects**—Hom
objects that are themselves objects of the category.
This chapter proves that Category $τ$ enriches over itself:
for any two objects $A, B ∈ Obj(τ)$,
the morphism space $\Hom_τ(A,B)$ is itself a $τ$-object,
with an NF-address, split-complex values,
and a tower-coherent structure
inherited from the primorial tower.

**Definition [def:self-enrichment**] (II.D53):
$τ$ is self-enriched—its
composition and identity maps are $τ$-morphisms.
**Definition [def:hom-object**] (II.D54):
the Hom object $[A,B]$ is the space of $τ$-holomorphic maps,
equipped with tower-coherent staging
$[A,B]_k = \Hom(A_k, B_k)$.
**Proposition [prop:hom-bipolar**] (II.P11):
every Hom object inherits the bipolar decomposition,
$[A,B] = e_+ · [A,B]_+ + e_- · [A,B]_-$,
because holomorphic maps between $τ$-objects
are themselves holomorphic objects,
and the Idempotent Decomposition Lemma (II.L07)
applies at the level of morphism spaces.

The argument rests on the Pre-Yoneda embedding
(Definition [def:pre-yoneda], II.D50,
Chapter [ch:pre-yoneda]):
holomorphic functions are objects,
so function *spaces* are objects,
so Hom spaces are objects.
Self-enrichment is the structural precondition
for the Yoneda embedding (Chapter [ch:yoneda-theorem]),
and it initiates the transition from $E₀⁽0⁾$
(Book I + Book II Parts I–VII)
to $E₀⁽1⁾$
(Book II Part VIII).
