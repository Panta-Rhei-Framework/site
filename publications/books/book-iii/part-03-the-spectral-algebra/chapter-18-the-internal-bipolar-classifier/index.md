---
layout: publication-chapter
title: "Chapter 18: The Internal Bipolar Classifier"
permalink: /publications/books/book-iii/part-03-the-spectral-algebra/chapter-18-the-internal-bipolar-classifier/
lane: publications
publication_type: chapter
book_id: "III"
book_slug: "book-iii"
part_number: 3
part_display: "Part III"
part_slug: "part-03-the-spectral-algebra"
chapter_number: 18
chapter_slug: "chapter-18-the-internal-bipolar-classifier"
page_in_book: 105
prev_chapter_url: "/publications/books/book-iii/part-03-the-spectral-algebra/chapter-17-the-adelic-embedding/"
prev_chapter_title: "Chapter 17: The Adelic Embedding"
next_chapter_url: "/publications/books/book-iii/part-03-the-spectral-algebra/chapter-19-the-spectral-trichotomy/"
next_chapter_title: "Chapter 19: The Spectral Trichotomy"
summary_short: "The preceding chapters of Part III erected the spectral algebra in stages: the primorial ladder , the CRT decomposition (Chapter…"
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


The preceding chapters of Part III
erected the spectral algebra in stages:
the primorial ladder ,
the CRT decomposition ,
Hensel lifting ,
and the adelic embedding .
At every stage,
an informal vocabulary intruded—“$B$-lobe
dominant,” “$C$-lobe dominant,” “mixed”—to
describe the bipolar character
of individual primes.
Informal vocabulary is debt.
This chapter repays it.

The **internal bipolar classifier** $Label_n$
is a computable function
from primes $p ≤ p_n$
to the label set $\{B, C, X\}$,
defined entirely from the CRT idempotents
on $ℤ / Prim(n) ℤ$.
A prime receives label $B$
when its CRT idempotent projects dominantly
onto the $χ_+$-eigenspace
(the exponent stratum of the ABCD chart);
label $C$ when the projection is $χ_-$-dominant
(the tetration stratum);
and label $X$ when the two projections are balanced.
The classifier is computable at every finite depth:
one evaluates the CRT idempotent,
applies the split-complex projection,
and reads off the dominant component.

Two structural results close the chapter.
First, the classification *stabilises*:
for each prime $p$,
there exists a depth $n_0$ beyond which
$Label_n(p)$ is constant.
The limiting classifier $Label_∞$
is well defined.
Second, the label assignment is *compatible*
with the split-complex idempotents $e_+$ and $e_-$
of the boundary ring $H_τ$:
a $B$-type prime has $e_+$-dominant spectral coefficients,
a $C$-type prime has $e_-$-dominant coefficients,
and an $X$-type prime has balanced contributions.
A table of explicit computations
for the primes $2, 3, 5, 7, 11, 13$
at depths $n = 1, 2, 3, 4$
makes the stabilisation visible.

With the internal bipolar classifier in place,
every subsequent chapter
can replace informal lobe language
with a decidable predicate on primes.
The spectral algebra is closed.
