---
layout: publication-chapter
title: "Chapter 73: The TauLib Linearity Audit"
permalink: /publications/books/book-i/part-17-the-proof-theoretic-mirror/chapter-73-the-taulib-linearity-audit/
lane: publications
publication_type: chapter
book_id: "I"
book_slug: "book-i"
part_number: 17
part_display: "Part XVII"
part_slug: "part-17-the-proof-theoretic-mirror"
chapter_number: 73
chapter_slug: "chapter-73-the-taulib-linearity-audit"
page_in_book: 333
prev_chapter_url: "/publications/books/book-i/part-17-the-proof-theoretic-mirror/chapter-72-diagonal-discipline-as-linear-logic/"
prev_chapter_title: "Chapter 72: Diagonal Discipline as Linear Logic"
next_chapter_url: "/publications/books/book-i/part-17-the-proof-theoretic-mirror/chapter-74-the-self-hosting-landscape/"
next_chapter_title: "Chapter 74: The Self-Hosting Landscape"
summary_short: "The Diagonal–Linear Correspondence (the relevant chapter, I.T37) identified a structural isomorphism between K5's diagonal discipline…"
canonical_book_url: "/publications/books/book-i/"
canonical_book_title: "Book I: Categorical Foundations"
canonical_part_url: "/publications/books/book-i/part-17-the-proof-theoretic-mirror/"
canonical_part_title: "Part XVII: The Proof-Theoretic Mirror"
right_rail:
  related:
  - title: "Book I: Categorical Foundations"
    url: /publications/books/book-i/
  - title: "Part XVII: The Proof-Theoretic Mirror"
    url: /publications/books/book-i/part-17-the-proof-theoretic-mirror/
  - title: Registry
    url: /registry/books/book-i/
  meta:
    type: Chapter
    book: "Book I"
    part: "Part XVII"
    layer: "E₀ Mathematics"
    updated: April 2026
---


The Diagonal–Linear Correspondence
(the relevant chapter, I.T37)
identified a structural isomorphism
between K5's diagonal discipline
and the !-free fragment of linear logic.
That correspondence operates at the level of design principles.
This chapter descends to the level of code.
TauLib — the Lean 4 formalization of Book I —
consists of 77 modules comprising approximately 15,900 lines.
The **Linearity Census Theorem**
(the relevant theorem, I.T38)
reports the empirical finding:
74 of 77 modules use zero classical axioms.
The remaining 3 sites —
2 uses of `Classical.em` in
`Coordinates/Primes.lean`
and 1 `funext` tactic call in
`Holomorphy/SpectralCoefficients.lean` —
are analyzed individually.
The `Classical.em` sites are eliminable
via decidable instances
(Proposition [prop:em-eliminable], I.P38).
The `funext` is a Lean kernel axiom
used tactically, not a classical commitment.
The chapter concludes with an honest
**Gap Declaration**
(Remark [rem:gap-declaration], I.R17):
what remains unearned,
and how Book III's self-enrichment program
will address it.
