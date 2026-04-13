---
layout: publication-chapter
title: "Chapter 49: The Identity Theorem"
permalink: /publications/books/book-i/part-12-holomorphic-transformers/chapter-49-the-identity-theorem/
lane: publications
publication_type: chapter
book_id: "I"
book_slug: "book-i"
part_number: 12
part_slug: "part-12-holomorphic-transformers"
chapter_number: 49
chapter_slug: "chapter-49-the-identity-theorem"
page_in_book: 221
prev_chapter_url: "/publications/books/book-i/part-12-holomorphic-transformers/chapter-48-the-diagonal-free-protection-theorem/"
prev_chapter_title: "Chapter 48: The Diagonal-Free Protection Theorem"
next_chapter_url: "/publications/books/book-i/part-13-internal-set-theory-the-cantor-mirage/chapter-50-membership-from-divisibility/"
next_chapter_title: "Chapter 50: Membership from Divisibility"
summary_short: "In classical complex analysis, the identity theorem states: if two holomorphic functions agree on a set with an accumulation point, they agree everywhere. This…"
canonical_book_url: "/publications/books/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/publications/books/book-i/part-12-holomorphic-transformers/"
canonical_part_title: "Part XII: Holomorphic Transformers"
right_rail:
  related:
  - title: "Book I: Categorical Foundations"
    url: /publications/books/book-i/
  - title: "Part XII: Holomorphic Transformers"
    url: /publications/books/book-i/part-12-holomorphic-transformers/
  - title: Registry
    url: /registry/books/book-i/
  meta:
    type: Chapter
    book: "Book I"
    part: "Part XII"
    layer: "E₀ Mathematics"
    updated: April 2026
---


In classical complex analysis,
the identity theorem states:
if two holomorphic functions agree
on a set with an accumulation point,
they agree everywhere.
This rigidity —
the determination of a global function
by local data —
is the hallmark of holomorphy.
Does $τ$-holomorphy enjoy a similar rigidity?
This chapter proves that it does,
and in a stronger form.
The **$τ$-Identity Theorem**
(Theorem [thm:tau-identity], I.T21)
shows that agreement at a single primorial depth $d_0$
forces global equality on all omega-tails.
The proof uses tower coherence
(Definition [def:tower-coherence], I.D46)
and the CRT coherence structure
(Theorem [thm:crt-coherence], I.T18)
rather than Taylor series or analytic continuation.
The key intermediate result is
**Tail Agreement Propagation**
(Lemma [lem:tail-agreement-propagation], I.L07):
agreement at depth $d_0$ propagates *upward*
through the primorial tower to all depths.
This is the opposite direction from classical analysis,
where agreement propagates via analytic continuation.
In $τ$, the Chinese Remainder Theorem
forces upward propagation.
We also define the space $Hol(𝕃)$
(Definition [def:hol-L], I.D49)
of $τ$-holomorphic functions
on the algebraic lemniscate,
whose elements are uniquely determined
by finite-depth data —
a consequence that will be exploited
in the Global Hartogs Theorem
(Chapter [ch:global-hartogs]).
