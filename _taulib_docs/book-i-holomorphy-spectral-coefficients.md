---
layout: taulib-doc
title: "TauLib.BookI.Holomorphy.SpectralCoefficients"
permalink: /verify/taulib/docs/book-i-holomorphy-spectral-coefficients/
lane: verify
module_name: "TauLib.BookI.Holomorphy.SpectralCoefficients"
book: "I"
book_label: "Foundations"
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
    book: "Book I"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.Holomorphy.SpectralCoefficients


Spectral coefficients and the restriction map for τ-holomorphic functions.

## Registry Cross-References


- [I.D65] Spectral Coefficients — `SpectralCoeff`

- [I.D66] Restriction Map — `restriction`

- [I.T29] Spectral Determination — `spectral_determines`


## Mathematical Content


Each τ-holomorphic function decomposes into spectral coefficients
via the character basis χ₊, χ₋ from Part X.
At each primorial stage k, the B-sector and C-sector outputs
provide two "Fourier coefficients".

The Spectral Determination Theorem: a τ-holomorphic function
is uniquely determined by its spectral coefficients.

---

### `Tau.Holomorphy.SpectralCoeff`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L34-L41)
**structure
Tau.Holomorphy.SpectralCoeff :Type**


[I.D65] Spectral coefficients of a StageFun at input n, stage k.
The B-sector coefficient is the B-output; the C-sector coefficient
is the C-output. Together they determine the function value at (n, k).

- b_coeff : Denotation.TauIdx
- c_coeff : Denotation.TauIdx
Instances For

---

### `Tau.Holomorphy.spectral_of`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L43-L45)
**def
Tau.Holomorphy.spectral_of
(f : StageFun)

(n k : Denotation.TauIdx)
 :SpectralCoeff**


Extract spectral coefficients from a StageFun.
Equations
- Tau.Holomorphy.spectral_of f n k = { b_coeff := f.b_fun n k, c_coeff := f.c_fun n k }
Instances For

---

### `Tau.Holomorphy.spectral_eq_implies_agree`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L47-L55)
**theorem
Tau.Holomorphy.spectral_eq_implies_agree
(f₁ f₂ : StageFun)

(n k : Denotation.TauIdx)

(h : spectral_of f₁ n k = spectral_of f₂ n k)
 :f₁.b_fun n k = f₂.b_fun n k ∧ f₁.c_fun n k = f₂.c_fun n k**


Two functions with the same spectral coefficients agree at that point.

---

### `Tau.Holomorphy.restriction`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L61-L66)
**def
Tau.Holomorphy.restriction
(f : StageFun)

(inK : Denotation.TauIdx → Bool)
 :StageFun**


[I.D66] The restriction map: restrict a StageFun to inputs
NOT in a given subset K (modeled as a predicate).
Returns 0 for inputs in K (the "deleted" set).
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.Holomorphy.restriction_outside`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L68-L73)
**theorem
Tau.Holomorphy.restriction_outside
(f : StageFun)

(inK : Denotation.TauIdx → Bool)

(n k : Denotation.TauIdx)

(hn : inK n = false)
 :(restriction f inK).b_fun n k = f.b_fun n k ∧ (restriction f inK).c_fun n k = f.c_fun n k**


Restriction agrees with original outside K.

---

### `Tau.Holomorphy.restriction_inside`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L75-L80)
**theorem
Tau.Holomorphy.restriction_inside
(f : StageFun)

(inK : Denotation.TauIdx → Bool)

(n k : Denotation.TauIdx)

(hn : inK n = true)
 :(restriction f inK).b_fun n k = 0 ∧ (restriction f inK).c_fun n k = 0**


Restriction is zero inside K.

---

### `Tau.Holomorphy.spectral_determines`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L86-L99)
**theorem
Tau.Holomorphy.spectral_determines
(f₁ f₂ : StageFun)

(h : ∀ (n k : Denotation.TauIdx), spectral_of f₁ n k = spectral_of f₂ n k)
 :f₁ = f₂**


[I.T29] Spectral Determination: if two tower-coherent StageFuns
have the same spectral coefficients at all inputs and stages,
they are equal.

This is essentially the content of the Identity Theorem (I.T21)
reformulated in spectral language.
