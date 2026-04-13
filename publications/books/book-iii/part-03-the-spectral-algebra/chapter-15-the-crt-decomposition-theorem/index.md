---
layout: publication-chapter
title: "Chapter 15: The CRT Decomposition Theorem"
permalink: /publications/books/book-iii/part-03-the-spectral-algebra/chapter-15-the-crt-decomposition-theorem/
lane: publications
publication_type: chapter
book_id: "III"
book_slug: "book-iii"
part_number: 3
part_slug: "part-03-the-spectral-algebra"
chapter_number: 15
chapter_slug: "chapter-15-the-crt-decomposition-theorem"
page_in_book: 87
prev_chapter_url: "/publications/books/book-iii/part-03-the-spectral-algebra/chapter-14-the-primorial-ladder/"
prev_chapter_title: "Chapter 14: The Primorial Ladder"
next_chapter_url: "/publications/books/book-iii/part-03-the-spectral-algebra/chapter-16-hensel-lifting-and-local-fields/"
next_chapter_title: "Chapter 16: Hensel Lifting and Local Fields"
summary_short: "Chapter [ch:primorial-ladder] established the primorial ladder $Prim(k) = p_1 ⋯ p_k$ as the canonical cofinal filtration of the $τ$ kernel. Every $τ$-effective…"
canonical_book_url: "/publications/books/book-iii/"
canonical_book_title: "Book III: Categorical Spectrum"
canonical_part_url: "/publications/books/book-iii/part-03-the-spectral-algebra/"
canonical_part_title: "Part III: The Spectral Algebra"
right_rail:
  related:
  - title: "Book III: Categorical Spectrum"
    url: /publications/books/book-iii/
  - title: "Part III: The Spectral Algebra"
    url: /publications/books/book-iii/part-03-the-spectral-algebra/
  - title: Registry
    url: /registry/books/book-iii/
  meta:
    type: Chapter
    book: "Book III"
    part: "Part III"
    layer: "E₀ Mathematics (Hinge)"
    updated: April 2026
---


Chapter [ch:primorial-ladder] established the primorial ladder
$Prim(k) = p_1 ⋯ p_k$
as the canonical cofinal filtration of the $τ$ kernel.
Every $τ$-effective property reduces to finitely many
primorial-level checks.
But a check at level $k$ is a computation
in the ring $ℤ / Prim(k)ℤ$,
whose order grows super-exponentially with $k$.
The **Chinese Remainder Theorem** (CRT)
decomposes this single large ring
into a product of small prime-level rings,
$$
 ℤ / Prim(k)ℤ
 ≅ 
 ∏_{i=1}^k ℤ / p_i ℤ,
$$
turning one hard computation into $k$ easy ones.
The classical CRT proof relies on the extended Euclidean algorithm,
which requires subtraction—a signed operation
that the $τ$ kernel does not import
($K3$ provides divisibility predicates,
not signed arithmetic).
This chapter proves the CRT constructively
using modular B\'ezout coefficients
obtained from divisibility alone.
We then read the CRT as the *algebraic Euler product*:
the endomorphism ring of the primorial presheaf decomposes
prime by prime.
The **Reconstruction Functor**
assembles local prime-level data into global primorial data
via an equivalence of module categories.
All Parts IV–VI arguments decompose through this functor.
