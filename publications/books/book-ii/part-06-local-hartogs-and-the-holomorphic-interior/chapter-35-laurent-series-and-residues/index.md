---
layout: publication-chapter
title: "Chapter 35: Laurent Series and Residues"
permalink: /publications/books/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-35-laurent-series-and-residues/
lane: publications
publication_type: chapter
book_id: "II"
book_slug: "book-ii"
part_number: 6
part_slug: "part-06-local-hartogs-and-the-holomorphic-interior"
chapter_number: 35
chapter_slug: "chapter-35-laurent-series-and-residues"
page_in_book: 175
prev_chapter_url: "/publications/books/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-34-composition-identity-associativity/"
prev_chapter_title: "Chapter 34: Composition, Identity, Associativity"
next_chapter_url: "/publications/books/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/chapter-36-the-canonical-holomorphic-basis-b/"
next_chapter_title: "Chapter 36: The Canonical Holomorphic Basis B"
summary_short: "Classical Laurent theory expands a holomorphic function in an annulus $\\{r_1 < |z| < r_2\\}$ as a doubly-infinite power series $∑_{n=-∞}^∞ a_n z^n$, with the…"
canonical_book_url: "/publications/books/book-ii/"
canonical_book_title: "Book II: Categorical Holomorphy"
canonical_part_url: "/publications/books/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/"
canonical_part_title: "Part VI: Local Hartogs and the Holomorphic Interior"
right_rail:
  related:
  - title: "Book II: Categorical Holomorphy"
    url: /publications/books/book-ii/
  - title: "Part VI: Local Hartogs and the Holomorphic Interior"
    url: /publications/books/book-ii/part-06-local-hartogs-and-the-holomorphic-interior/
  - title: Registry
    url: /registry/books/book-ii/
  meta:
    type: Chapter
    book: "Book II"
    part: "Part VI"
    layer: "E₀ Mathematics"
    updated: April 2026
---


Classical Laurent theory
expands a holomorphic function
in an annulus $\{r_1 < |z| < r_2\}$
as a doubly-infinite power series
$∑_{n=-∞}^∞ a_n z^n$,
with the residue $a_{-1}$
computed by contour integration
around the singularity Ahlfors1979,Conway1978.
None of this machinery is available
in the split-complex setting:
there is no rotation group $SO(2)$,
no contour integration,
and no annular domains
in the sense of $ℂ$.
This chapter develops the
$τ$-analogue of Laurent expansion.
The key insight is that the bipolar spectral decomposition
(I.T10, I.D21, Book I)
replaces the circular Fourier decomposition.
A $τ$-holomorphic function
decomposes into two independent channel series:
$$
 f
 = 
 ∑_n a_n e_+ φ_n^{(+)}
 + 
 ∑_n b_n e_- φ_n^{(-)},
$$
where $φ_n^{(±)}$ are the sector basis functions.
**Residues** emerge as
spectral coefficients at distinguished frequencies
(Definition [def:residue], II.D43)—not
from contour integrals but from
the spectral projection operators
of Part V's calibration.
The **Residue Theorem**
(Theorem [thm:residue-theorem], II.T30)
shows that the sum of residues
equals the **spectral trace**,
a quantity computable from the
boundary character alone.
