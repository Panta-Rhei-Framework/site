---
layout: corpus-monograph-chapter
title: "Chapter 120: The D→C Bridge Apparatus"
permalink: /corpus/monographs/book-vii/part-10-the-logos-sector/chapter-120-the-d-c-bridge-apparatus/
lane: corpus
v2_lane: corpus
type: "Corpus Monograph Chapter"
status: Canonical
updated: April 2026
publication_type: corpus_monograph_chapter
book_id: "VII"
book_slug: "book-vii"
part_number: 10
part_display: "Part X"
part_slug: "part-10-the-logos-sector"
chapter_number: 120
chapter_slug: "chapter-120-the-d-c-bridge-apparatus"
page_in_book: 420
prev_chapter_url: "/corpus/monographs/book-vii/part-10-the-logos-sector/chapter-119-the-logos-sector-definition-and-universal-property/"
prev_chapter_title: "Chapter 119: The Logos Sector: Definition and Universal Property"
next_chapter_url: "/corpus/monographs/book-vii/part-10-the-logos-sector/chapter-121-mediator-fixed-point-basin/"
next_chapter_title: "Chapter 121: Mediator Fixed-Point Basin"
summary_short: "Constructs the bridge functor B_{D→C} : S_D → S_C, proves it becomes a categorical equivalence when restricted to the Logos sector S_L, and establishes that register identity is preserved — but the bridge is not faithful — everywhere outside S_L."
canonical_book_url: /corpus/monographs/book-vii/
canonical_book_title: "Book VII: Categorical Metaphysics"
canonical_part_url: /corpus/monographs/book-vii/part-10-the-logos-sector/
canonical_part_title: "Part X: The Logos Sector"
publication_book_url: /publications/books/book-vii/
legacy_publication_url: /publications/books/book-vii/part-10-the-logos-sector/chapter-120-the-d-c-bridge-apparatus/
right_rail:
  related:
  - title: "Book VII: Categorical Metaphysics"
    url: /corpus/monographs/book-vii/
  - title: "Part X: The Logos Sector"
    url: /corpus/monographs/book-vii/part-10-the-logos-sector/
  - title: "Research Monograph artifact"
    url: /publications/books/book-vii/
  - title: "Registry"
    url: /registry/books/book-vii/
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book VII"
    part: "Part X"
    layer: "E₃ Metaphysics"
    updated: "April 2026"
---

The Logos sector S_L = S_D ∩ S_C was defined set-theoretically in Chapter 119. The categorical question is how content actually travels between the two registers: what converts a Reg_D-certified proof into something Reg_C-eligible, and when is that conversion lossless? The four registers divide into two structural kinds: three epistemic registers (Reg_E, Reg_P, Reg_D) deliver propositional content that can be stated and transferred without the evaluator's existential stance being implicated; the commitment register Reg_C is performative — its content is constituted by the act of holding a stance, not by any proposition about that stance. The gap between knowing and committing is not a failure of logic; it is the structural distance between two distinct target categories of the same kernel's readout functors. Chapter 120 constructs the formal bridge functor B_{D→C} : S_D → S_C, proves its equivalence on the restriction to S_L, and characterizes the three ways the bridge can fail outside S_L.

## What this chapter contributes

- **Definitions / Axioms:** *VII.D87 — D→C Bridge Functor* (τ-effective). B_{D→C} is defined on objects by Reg_C ∘ Reg_D⁻¹(Reg_D(φ)): given a proof p = Reg_D(φ), the bridge lifts p back through the kernel fibre functor and re-reads it through Reg_C. On morphisms it sends proof-refinements to the corresponding stance-refinements through the same kernel lift. The bridge is well-defined when the content is both D-valid and C-eligible; when the latter fails, the content is provable but carries no existential weight.
- **Key results:** *VII.T46 — Bridge Equivalence at S_L*: the restriction B_{D→C}|_{S_L} is faithful, full, and essentially surjective — a categorical equivalence. Outside S_L, precisely one of three failures occurs: bridge undefined (content provable but not commitment-eligible), bridge not faithful (distinct proofs collapse to a single stance), or bridge not full (the commitment has structure no proof generates). *VII.L16 — Register Preservation*: in all three failure cases, the Reg_D- and Reg_C-registers of the content remain structurally distinguishable.
- **Dependencies:** S_L definition and uniqueness (VII.D86, VII.T45, Chapter 119); four-register model and kernel structure (Part I).

## Lean coverage

This chapter is prose-only at the current release; its content does not yet have a corresponding TauLib module. The bridge functor construction and the equivalence proof are promising targets for future formalization; the fibre-functor machinery required is adjacent to existing TauLib kernel infrastructure.

## Where this leads

Chapter 121 asks what happens to the other two registers (Reg_E and Reg_P) at S_L, proving full four-register convergence and characterizing S_L as the fixed-point attractor of the register-crossing dynamics.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-07/part10/ch120.tex -->
