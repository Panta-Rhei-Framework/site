---
layout: corpus-monograph-chapter
title: "Chapter 3: The Temporal Ignition: Why a ``Time Epoch'' Starts"
permalink: /corpus/monographs/book-v/part-01-the-base-itself-time-from-tau/chapter-03-the-temporal-ignition-why-a-time-epoch-starts/
lane: corpus
v2_lane: corpus
type: "Corpus Monograph Chapter"
status: Canonical
updated: April 2026
publication_type: corpus_monograph_chapter
book_id: "V"
book_slug: "book-v"
part_number: 1
part_display: "Part I"
part_slug: "part-01-the-base-itself-time-from-tau"
chapter_number: 3
chapter_slug: "chapter-03-the-temporal-ignition-why-a-time-epoch-starts"
page_in_book: 21
prev_chapter_url: "/corpus/monographs/book-v/part-01-the-base-itself-time-from-tau/chapter-02-proto-chronos-from-alpha-ticks-to-proper-time/"
prev_chapter_title: "Chapter 2: Proto-Chronos: From α-Ticks to Proper Time"
next_chapter_url: "/corpus/monographs/book-v/part-01-the-base-itself-time-from-tau/chapter-04-high-energy-and-high-entropy-at-the-beginning/"
next_chapter_title: "Chapter 4: High Energy and High Entropy at the Beginning"
summary_short: "The preceding chapter derived physical time as arc length along the base circle τ¹. But arc length is a mathematical construction — it exists at every…"
canonical_book_url: /corpus/monographs/book-v/
canonical_book_title: "Book V: Categorical Macrocosm"
canonical_part_url: /corpus/monographs/book-v/part-01-the-base-itself-time-from-tau/
canonical_part_title: "Part I: The Base Itself: Time from τ¹"
publication_book_url: /publications/books/book-v/
legacy_publication_url: /publications/books/book-v/part-01-the-base-itself-time-from-tau/chapter-03-the-temporal-ignition-why-a-time-epoch-starts/
right_rail:
  related:
  - title: "Book V: Categorical Macrocosm"
    url: /corpus/monographs/book-v/
  - title: "Part I: The Base Itself: Time from τ¹"
    url: /corpus/monographs/book-v/part-01-the-base-itself-time-from-tau/
  - title: "Research Monograph artifact"
    url: /publications/books/book-v/
  - title: "Registry"
    url: /registry/books/book-v/
  meta:
    type: "Corpus Monograph Chapter"
    book: "Book V"
    part: "Part I"
    layer: "E₁ Physics (Macrocosm)"
    updated: "April 2026"
---

Arc length exists as a mathematical quantity at every refinement depth — even at α₁. The prior chapter showed that time *is* this arc length, but not yet why proper time becomes *operationally readable*. This chapter bridges that gap. Temporal ignition depends on spectral purity (Book III, III.T19): the boundary holonomy algebra H_∂[ω] must support at least one pair of characters with a stable, resolvable frequency gap before any physical subsystem can function as a clock. Below the ignition depth n_ign the spectral structure is too coarse; there are no oscillating modes, no periodic processes, no measurement. Above the coherence horizon n_coh the remaining proper time t_∞ − t(n) falls below the smallest resolvable interval and time effectively freezes. The temporal epoch — the arena in which all observable physics takes place — lies between these two boundaries. The chapter proves that three epochs exist and are non-empty (V.T09), constructs the canonical "now" hypersurface Σ_now = {α_n*} × T²_n* (V.D19), establishes that simultaneity is structural rather than conventional (V.R05), and shows that the current universe sits deep within the temporal epoch (V.T10).

## What this chapter contributes

- **Definitions / Axioms:** *V.D17 — Three Temporal Epochs* (τ-effective); *V.D18 — Ignition Depth* (τ-effective); *V.D19 — Σ_now Hypersurface* (τ-effective); *V.D20 — Coherence Horizon* (τ-effective).
- **Key results:** *V.T09 — Epoch Existence Theorem* (τ-effective): the pre-temporal, temporal, and post-temporal epochs all exist and are non-empty. *V.T10 — Now-Within-Epoch Theorem* (τ-effective): n_ign ≪ n_* ≪ n_coh, placing the current universe firmly within the temporal epoch. *V.P04 — Pre-Temporal Indistinguishability* (τ-effective): no physical subsystem can distinguish adjacent ticks below n_ign. *V.R05 — Simultaneity Is Structural* (τ-effective): two events are simultaneous if and only if they share the same refinement depth, independent of any observer.
- **Notation introduced:** n_ign (ignition depth); n_coh (coherence horizon); Σ_now; three-epoch partition of the α-orbit.
- **Dependencies:** V.D12 (Base Circle), V.D14 (Proper Time), V.T06 (Time Derivation), V.T08 (Bounded Time), IV.D03 (Refinement Tower), IV.T01 (Structural Arrow), Book III III.T19 (Spectral Purity / RH).

## Lean coverage

`TauLib.BookV.Temporal.TemporalIgnition` — covers the ignition condition, epoch existence, and the Σ_now foliation.

## Where this leads

Chapter 4 characterises the physical conditions at the ignition depth (high energy, high entropy, maximal coupling); Chapter 5 uses the canonical foliation to define operational distance via the radar-time protocol.

<!-- chapter-abstract: regenerated 2026-04-29 from manuscript-sources/book-05/part01/ch05-temporal-ignition.tex -->
