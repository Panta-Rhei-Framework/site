---
layout: taulib-doc
title: "TauLib.BookIV.Sectors.SpectralPage"
permalink: /verify/taulib/docs/book-iv-sectors-spectral-page/
lane: verify
module_name: "TauLib.BookIV.Sectors.SpectralPage"
book: "IV"
book_label: "Microcosm"
right_rail:
  related:
  - title: TauLib Overview
    url: /verify/taulib/
  - title: Architecture
    url: /verify/taulib/architecture/
  artifacts:
  - title: Source on GitHub
    url: https://github.com/Panta-Rhei-Research/taulib
    external: true
  meta:
    type: "API Documentation"
    book: "Book IV"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookIV.Sectors.SpectralPage


Tensor-square derivation of 121/225 from the E₁ spectral page.

## Registry Cross-References


- [IV.D331] Tensor-Square Character Algebra — `tensorModes`

- [IV.T133] EM Tensor Density Theorem — `em_tensor_active_count`, `em_tensor_total`

- [IV.P179] E₁ Page Derivation of α-Coefficient — `tensor_equals_sieve_times_correction`

- [IV.R388] OQ-A1 Status Update — RESOLVED


## Mathematical Content


The boundary character algebra A_spec(L) has 15 modes (5 generators × 3 lobe
configurations). The tensor square A_spec(L)^{⊗2} has 225 = 15² mode pairs.
A mode pair (m₁, m₂) is jointly EM-active when both m₁ and m₂ are EM-active.

The EM-active count in the tensor square is 11² = 121 (since each factor
contributes independently). The density 121/225 = (11/15)² is the coefficient
in α = (121/225)·ι<sub>τ</sub>⁴.

**Physical interpretation:** α is a coupling constant for emission-absorption.
Each vertex (source, sink) contributes one factor of 11/15. The product
(11/15)² = 121/225 is the joint probability that both endpoints of the EM
propagator land on EM-active boundary modes.

**Unification:** The factorization (8/15)·(121/120) is a COROLLARY of the
tensor-square density, not the other way around.

## Ground Truth Sources


- spectral_page_121_225_sprint.md: mathematical derivation

- BoundaryFiltration.lean: structural EM-activity, twin prime residue

- ModeCensus.lean: mode enumeration, 11/15 census


---

### `Tau.BookIV.Sectors.SpectralPage.tensorModes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SpectralPage.lean#L49-L51)
**def
Tau.BookIV.Sectors.SpectralPage.tensorModes :List (ModeCensus.BoundaryMode × ModeCensus.BoundaryMode)**


[IV.D331] All mode pairs in A_spec(L)^{⊗2}.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.SpectralPage.emTensorActive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SpectralPage.lean#L53-L55)
**def
Tau.BookIV.Sectors.SpectralPage.emTensorActive :List (ModeCensus.BoundaryMode × ModeCensus.BoundaryMode)**


EM-active tensor modes: both endpoints EM-active.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.SpectralPage.emTensorSilent`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SpectralPage.lean#L57-L59)
**def
Tau.BookIV.Sectors.SpectralPage.emTensorSilent :List (ModeCensus.BoundaryMode × ModeCensus.BoundaryMode)**


EM-silent tensor modes: at least one endpoint silent.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Sectors.SpectralPage.em_tensor_total`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SpectralPage.lean#L65-L66)
**theorem
Tau.BookIV.Sectors.SpectralPage.em_tensor_total :tensorModes.length = 225**


[IV.T133] Total tensor-square modes = 225 = 15².

---

### `Tau.BookIV.Sectors.SpectralPage.em_tensor_active_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SpectralPage.lean#L68-L69)
**theorem
Tau.BookIV.Sectors.SpectralPage.em_tensor_active_count :emTensorActive.length = 121**


[IV.T133] EM-active tensor modes = 121 = 11².

---

### `Tau.BookIV.Sectors.SpectralPage.em_tensor_silent_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SpectralPage.lean#L71-L72)
**theorem
Tau.BookIV.Sectors.SpectralPage.em_tensor_silent_count :emTensorSilent.length = 104**


Silent tensor modes = 104.

---

### `Tau.BookIV.Sectors.SpectralPage.tensor_partition`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SpectralPage.lean#L74-L76)
**theorem
Tau.BookIV.Sectors.SpectralPage.tensor_partition :emTensorActive.length + emTensorSilent.length = tensorModes.length**


Active + silent = total (consistency).

---

### `Tau.BookIV.Sectors.SpectralPage.density_is_square`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SpectralPage.lean#L82-L83)
**theorem
Tau.BookIV.Sectors.SpectralPage.density_is_square :121 = 11 * 11 ∧ 225 = 15 * 15**


121 = 11² and 225 = 15²: the tensor density IS a perfect square ratio.

---

### `Tau.BookIV.Sectors.SpectralPage.density_equals_square`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SpectralPage.lean#L85-L87)
**theorem
Tau.BookIV.Sectors.SpectralPage.density_equals_square :121 * 15 * 15 = 11 * 11 * 225**


The density 121/225 = (11/15)². Cross-multiplied form.

---

### `Tau.BookIV.Sectors.SpectralPage.tensor_equals_sieve_times_correction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SpectralPage.lean#L89-L93)
**theorem
Tau.BookIV.Sectors.SpectralPage.tensor_equals_sieve_times_correction :8 * 121 * 225 = 15 * 121 * 120**


[IV.P179] Tensor square contains the sieve × correction factorization.
(8/15)·(121/120) = 121/225.
Cross-multiplied: 8 · 121 · 225 = 15 · 121 · 120.

---

### `Tau.BookIV.Sectors.SpectralPage.correction_cross_mult`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Sectors/SpectralPage.lean#L95-L98)
**theorem
Tau.BookIV.Sectors.SpectralPage.correction_cross_mult :121 * 15 * 120 = 8 * 225 * 121**


The correction 121/120 is recovered from the tensor density and sieve.
(121/225) / (8/15) = 121/120. Cross-multiplied (clearing denominators):
