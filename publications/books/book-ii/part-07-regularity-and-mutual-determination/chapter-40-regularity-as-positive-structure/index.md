---
layout: publication-chapter
title: "Chapter 40: Regularity as Positive Structure"
permalink: /publications/books/book-ii/part-07-regularity-and-mutual-determination/chapter-40-regularity-as-positive-structure/
lane: publications
publication_type: chapter
book_id: "II"
book_slug: "book-ii"
part_number: 7
part_slug: "part-07-regularity-and-mutual-determination"
chapter_number: 40
chapter_slug: "chapter-40-regularity-as-positive-structure"
page_in_book: 211
prev_chapter_url: "/publications/books/book-ii/part-07-regularity-and-mutual-determination/chapter-39-the-3-lemma-chain/"
prev_chapter_title: "Chapter 39: The 3-Lemma Chain"
next_chapter_url: "/publications/books/book-ii/part-07-regularity-and-mutual-determination/chapter-41-pre-yoneda-embedding/"
next_chapter_title: "Chapter 41: Pre-Yoneda Embedding"
summary_short: "What does it mean for a function to be regular at a point? In classical complex analysis, the answer is *negative*: a function is regular where it is *not*…"
canonical_book_url: "/publications/books/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/publications/books/book-ii/part-07-regularity-and-mutual-determination/"
canonical_part_title: "Part VII: Regularity and Mutual Determination"
right_rail:
  related:
  - title: "Book II: Categorical Holomorphy"
    url: /publications/books/book-ii/
  - title: "Part VII: Regularity and Mutual Determination"
    url: /publications/books/book-ii/part-07-regularity-and-mutual-determination/
  - title: Registry
    url: /registry/books/book-ii/
  meta:
    type: Chapter
    book: "Book II"
    part: "Part VII"
    layer: "E₀ Mathematics"
    updated: April 2026
---


What does it mean for a function to be regular at a point?
In classical complex analysis,
the answer is *negative*:
a function is regular where it is *not* singular.
Regularity is defined by the *absence* of pathology —
the absence of poles, branch points,
or essential singularities.
One first defines what can go wrong,
then declares regularity to be
the complement of wrongness.

In Category $τ$,
regularity is a *positive* condition:
the *existence* of a stabilized $ω$-germ.
A point $p ∈ τ^3$ is $τ$-regular for a function $f$
if the sequence of $ω$-germ restrictions
stabilizes at a finite primorial stage —
if finitely much boundary data suffices
to determine $f$ at $p$.
This chapter introduces
**$τ$-Regularity**
(Definition [def:tau-regularity], II.D49),
proves the
**Regularity Criterion**
(Theorem [thm:regularity-criterion], II.T34),
which establishes a sharp dichotomy —
every point is either $τ$-regular
(stabilization at finite stage)
or genuinely singular
(the germ sequence diverges) —
and explains in
**Remark [rem:positive-negative-regularity**] (II.R11)
why the classical notion of ``removable singularity''
has no $τ$-analogue.
The ultrametric topology
admits no epsilon-delta wiggle room:
cylinders are clopen,
so singularities cannot be ``approached'' and then ``removed.''
They are either present at a given stage or absent.

The key dependencies are:
the Global Hartogs Theorem
(I.T31, the Global Hartogs Extension (Book I, Chapter 62))
establishes that boundary data determines interior data;
the Idempotent Decomposition Lemma
(II.L07, Chapter [ch:idempotent-decomposition])
provides the canonical $e_±$-splitting;
the Holomorphic $⇔$ Idempotent-Supported
equivalence
(II.T33, Chapter [ch:three-lemma-chain])
characterizes holomorphic maps;
and the evolution operator
(II.D37, Chapter [ch:evolution-operator])
provides the propagation mechanism
through which stabilization occurs.
