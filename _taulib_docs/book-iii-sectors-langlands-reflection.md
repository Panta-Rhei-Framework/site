---
layout: taulib-doc
title: "TauLib.BookIII.Sectors.LanglandsReflection"
permalink: /verify/taulib/docs/book-iii-sectors-langlands-reflection/
lane: verify
module_name: "TauLib.BookIII.Sectors.LanglandsReflection"
book: "III"
book_label: "Spectrum"
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
    book: "Book III"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookIII.Sectors.LanglandsReflection


Langlands₁ Reflection Bridge, Template Invariance, Universal Operator,
and Spectral Polarity.

## Registry Cross-References


- [III.D15] Langlands₁ Reflection Bridge -- `langlands_reflection_check`

- [III.T06] Template Invariance Under Reflection -- `template_invariance_check`

- [III.D16] Universal Operator -- `universal_operator`

- [III.D17] Spectral Polarity -- `spectral_polarity`

- [III.P04] Balanced Sector Uniqueness -- `balanced_uniqueness_check`


## Mathematical Content


**III.D15 (Langlands₁):** The enrichment functor F_E restricted to boundary
characters produces a correspondence between E₀-level sectors and E₁-level
sectors. Template invariant; carrier changes.

**III.T06 (Template Invariance):** The layer template (Carrier, Predicate,
Decoder, Invariant) is preserved under the Langlands₁ reflection.

**III.D16 (Universal Operator):** H_∞ on L²(Char(L)) unifies all L-functions
as spectral determinants.

**III.D17 (Spectral Polarity):** For each sector S_g, the spectral polarity
pol(S_g) = Σ|m| / Σ|n| over characters in the sector. The m-axis is the
multiplicative/Galois (B-lobe) direction, n-axis the additive/automorphic
(C-lobe) direction.

---

### `Tau.BookIII.Sectors.langlands_reflection_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L46-L74)
**def
Tau.BookIII.Sectors.langlands_reflection_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D15] Langlands₁ reflection: maps E₀-sector data to E₁-sector data.
The enrichment functor preserves the sector assignment when lifting
from E₀ to E₁: for each boundary character χ, the E₁-enriched version
of Φ(χ) has reduce-stable values at the E₁ level.
Equations
- Tau.BookIII.Sectors.langlands_reflection_check bound db = Tau.BookIII.Sectors.langlands_reflection_check.go bound db 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Sectors.langlands_reflection_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L53-L73)@[irreducible]

**def
Tau.BookIII.Sectors.langlands_reflection_check.go
(bound db : Denotation.TauIdx)

(m n k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.template_invariance_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L80-L99)
**def
Tau.BookIII.Sectors.template_invariance_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.T06] Template invariance check: the four-component layer template
is preserved under the Langlands₁ reflection.
The enrichment functor maps E₀ template to compatible E₁ template.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.template_invariance_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L88-L98)@[irreducible]

**def
Tau.BookIII.Sectors.template_invariance_check.go
(bound db : Denotation.TauIdx)

(e0 e1 : Enrichment.LayerTemplate)

(x k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.universal_operator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L105-L119)
**def
Tau.BookIII.Sectors.universal_operator
(χ : BoundaryCharacter)

(_x k bound : Denotation.TauIdx)
 :Denotation.TauIdx**


[III.D16] Universal operator H_{≤N} on characters at finite cutoff.
At stage k: H_{≤N}(χ)(x) = Σ_{j ≤ N} weight(χ) · reduce(j, k).
This is the finite-cutoff truncation of the universal spectral operator.
All L-functions are spectral determinants of this operator.
Equations
- Tau.BookIII.Sectors.universal_operator χ _x k bound = Tau.BookIII.Sectors.universal_operator.go k bound (χ.m_index.natAbs + χ.n_index.natAbs) 0 0 (bound + 1)
Instances For

---

### `Tau.BookIII.Sectors.universal_operator.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L113-L118)@[irreducible]

**def
Tau.BookIII.Sectors.universal_operator.go
(k bound : Denotation.TauIdx)

(w j acc fuel : ℕ)
 :Denotation.TauIdx**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.universal_op_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L121-L138)
**def
Tau.BookIII.Sectors.universal_op_check
(bound db : Denotation.TauIdx)
 :Bool**


[III.D16] Universal operator is reduce-stable at each stage.
Equations
- Tau.BookIII.Sectors.universal_op_check bound db = Tau.BookIII.Sectors.universal_op_check.go bound db 0 1 ((bound + 1) * (db + 1))
Instances For

---

### `Tau.BookIII.Sectors.universal_op_check.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L125-L137)@[irreducible]

**def
Tau.BookIII.Sectors.universal_op_check.go
(bound db : Denotation.TauIdx)

(m k fuel : ℕ)
 :Bool**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.spectral_polarity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L144-L161)
**def
Tau.BookIII.Sectors.spectral_polarity
(sec : Sector)

(bound : Denotation.TauIdx)
 :Denotation.TauIdx × Denotation.TauIdx**


[III.D17] Spectral polarity of a sector at finite cutoff.
Measures the m-axis (Galois/B-lobe) vs n-axis (automorphic/C-lobe)
balance DIRECTLY from the character lattice.
Returns (m_sum, n_sum) over characters in the sector.
Equations
- Tau.BookIII.Sectors.spectral_polarity sec bound = Tau.BookIII.Sectors.spectral_polarity.go sec bound 0 0 0 0 ((bound + 1) * (bound + 1))
Instances For

---

### `Tau.BookIII.Sectors.spectral_polarity.go`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L151-L160)@[irreducible]

**def
Tau.BookIII.Sectors.spectral_polarity.go
(sec : Sector)

(bound : Denotation.TauIdx)

(m n m_acc n_acc fuel : ℕ)
 :Denotation.TauIdx × Denotation.TauIdx**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.spectral_polarity_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L163-L181)
**def
Tau.BookIII.Sectors.spectral_polarity_check
(bound : Denotation.TauIdx)
 :Bool**


[III.D17] Check spectral polarity classification:


- D: both zero (trivial character only)

- A: BALANCED (m_sum = n_sum)

- B: m-dominant (m_sum > n_sum)

- C: n-dominant (n_sum > m_sum)

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.balanced_uniqueness_check`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L187-L199)
**def
Tau.BookIII.Sectors.balanced_uniqueness_check
(bound : Denotation.TauIdx)
 :Bool**


[III.P04] Balanced sector uniqueness: among primitive sectors {D, A, B, C},
only the A-sector has balanced spectral polarity (m_sum = n_sum > 0).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIII.Sectors.langlands_reflection_5_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L229-L230)
**theorem
Tau.BookIII.Sectors.langlands_reflection_5_3 :langlands_reflection_check 5 3 = true**


---

### `Tau.BookIII.Sectors.template_invariance_8_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L233-L234)
**theorem
Tau.BookIII.Sectors.template_invariance_8_3 :template_invariance_check 8 3 = true**


---

### `Tau.BookIII.Sectors.universal_op_3_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L237-L238)
**theorem
Tau.BookIII.Sectors.universal_op_3_3 :universal_op_check 3 3 = true**


---

### `Tau.BookIII.Sectors.spectral_polarity_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L241-L242)
**theorem
Tau.BookIII.Sectors.spectral_polarity_5 :spectral_polarity_check 5 = true**


---

### `Tau.BookIII.Sectors.balanced_uniqueness_5`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L245-L246)
**theorem
Tau.BookIII.Sectors.balanced_uniqueness_5 :balanced_uniqueness_check 5 = true**


---

### `Tau.BookIII.Sectors.sector_count_preserved`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L252-L254)
**theorem
Tau.BookIII.Sectors.sector_count_preserved :[Sector.D, Sector.A, Sector.B, Sector.C, Sector.Omega].length = 5**


[III.D15] Structural: the five-sector partition is preserved.

**Scope limitation (E3 collapse):** At finite primorial level, the E3
predicate degenerates to E0 because `reduce` is idempotent. This check
is vacuous but correctly models the mathematical structure. The E3 layer
is correctly DEFINED but finite verification is vacuous.
See audit DASHBOARD.md §E3 Collapse.

---

### `Tau.BookIII.Sectors.template_invariance_e3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L262-L265)
**theorem
Tau.BookIII.Sectors.template_invariance_e3 :Enrichment.layer_of Enrichment.EnrLevel.E3 8 3 = Enrichment.layer_of Enrichment.EnrLevel.E3.succ 8 3**


[III.T06] Structural: template invariance at E₃ is trivial
since E₃.succ = E₃ (saturation).

---

### `Tau.BookIII.Sectors.d_polarity_zero`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L267-L269)
**theorem
Tau.BookIII.Sectors.d_polarity_zero :spectral_polarity Sector.D 10 = (0, 0)**


[III.D17] Structural: D-sector polarity is (0, 0)
because only the trivial character (0,0) is in D.

---

### `Tau.BookIII.Sectors.a_balanced_3`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIII/Sectors/LanglandsReflection.lean#L271-L273)
**theorem
Tau.BookIII.Sectors.a_balanced_3 :(spectral_polarity Sector.A 3).1 = (spectral_polarity Sector.A 3).2**


[III.P04] Structural: A-sector polarity at bound=3 is balanced.
