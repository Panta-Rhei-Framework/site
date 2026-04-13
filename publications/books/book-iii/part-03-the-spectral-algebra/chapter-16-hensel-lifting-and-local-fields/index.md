---
layout: publication-chapter
title: "Chapter 16: Hensel Lifting and Local Fields"
permalink: /publications/books/book-iii/part-03-the-spectral-algebra/chapter-16-hensel-lifting-and-local-fields/
lane: publications
publication_type: chapter
book_id: "III"
book_slug: "book-iii"
part_number: 3
part_slug: "part-03-the-spectral-algebra"
chapter_number: 16
chapter_slug: "chapter-16-hensel-lifting-and-local-fields"
page_in_book: 93
prev_chapter_url: "/publications/books/book-iii/part-03-the-spectral-algebra/chapter-15-the-crt-decomposition-theorem/"
prev_chapter_title: "Chapter 15: The CRT Decomposition Theorem"
next_chapter_url: "/publications/books/book-iii/part-03-the-spectral-algebra/chapter-17-the-adelic-embedding/"
next_chapter_title: "Chapter 17: The Adelic Embedding"
summary_short: "The CRT Decomposition Theorem (Chapter [ch:crt-decomposition-theorem]) split the primorial residue ring $ℤ / M_d ℤ$ into a product of prime-power components.…"
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


The CRT Decomposition Theorem
(Chapter [ch:crt-decomposition-theorem])
split the primorial residue ring
$ℤ / M_d ℤ$
into a product of prime-power components.
This chapter climbs those components vertically:
given a root modulo $p$,
we lift it constructively to a root modulo $p^2$,
then $p^3$, and so on without end.
The mechanism is **modular Newton iteration**—a
correction-by-divisibility procedure
that requires no signed arithmetic
and no convergence analysis.
The lifting is unique at each stage
(a $p$-adic contraction in the classical language;
a tower-coherent singleton in ours).
Assembling all stages produces
$ℤ_p^τ = \varprojlim ℤ / p^n ℤ$,
the **$τ$-native $p$-adic integers**—an
inverse limit that lives inside Category $τ$
with a canonical NF address.
The $p$-adic valuation $v_p$
is the D-coordinate restricted
to the $p$-primary component of the primorial tower.
We prove that $ℤ_p^τ$ is ``complete''
in the $τ$-sense:
every tower-coherent sequence has a unique limit.
This is not metric completeness
but Global Hartogs (I.T31) restricted
to the $p$-primary sub-tower—no
metric, no Cauchy sequences,
just tower coherence.
The chapter closes with the local-global bridge:
the $τ$-native local fields assemble via CRT
into the profinite completion $\widehatℤ_τ$,
laying the foundation for the adelic embedding
of Chapter 17.
