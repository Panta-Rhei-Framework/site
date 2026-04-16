---
layout: taulib-doc
title: "TauLib.BookIV.Physics.InternalEquations"
permalink: /verify/taulib/docs/book-iv-physics-internal-equations/
lane: verify
module_name: "TauLib.BookIV.Physics.InternalEquations"
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

# TauLib.BookIV.Physics.InternalEquations


Physical equations as internal identities between categorical objects in
Layer 1 (internal physics). The numerical values are what the readout
functor R_μ reads out, not what the equations ARE.

## Registry Cross-References


- [IV.D323] Internal Identity — `InternalIdentity`

- [IV.D324] Equation Layer — `EquationLayer`

- [IV.T127] Mass Ratio as Internal Identity — `mass_ratio_internal`

- [IV.P176] Internal equations are dimensionless — `internal_identity_dimensionless`


## Mathematical Content


### Equations as Natural Transformation Identities


In Layer 1, a physical equation is a **morphism** (or natural transformation)
between internal categorical objects, not an equality between ℝ-numbers.

Example: The mass ratio R₀ = ι<sub>τ</sub>⁻⁷ − √3·ι<sub>τ</sub>⁻² is ontologically:

```
R₀ : Hom_C(m_n, m_e) → ℕ
```


i.e., an internal morphism that counts how many η-steps (strong sector
minimal endomorphisms) fit between the neutron and electron confinement
invariants. The number 1838.68 is what R_μ reads out.

### Layer Discipline


Every equation has a definite layer:


- Layer 0: Pure mathematical identities (category theory, no physics)

- Layer 1: Internal physics identities (tick counts, no SI units)

- Layer 2: Readout images (SI numbers, measurement procedures)


## Ground Truth Sources


- Book IV Part II ch10-ch11: Internal equations

- MassRatioFormula.lean: R₀ numerical derivation


---

### `Tau.BookIV.Physics.EquationLayer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L53-L69)
**inductive
Tau.BookIV.Physics.EquationLayer :Type**


[IV.D324] The ontological layer at which an equation lives.
Layer discipline: every equation belongs to exactly one layer.

- MathKernel : EquationLayer
Layer 0: Pure mathematics. Category theory, algebra, analysis.
No physics semantics, no units, no measurement concept.
Examples: axioms K0-K6, Central Theorem, Epstein zeta identity.

- InternalPhysics : EquationLayer
Layer 1: Internal physics. Sector-enriched H_∂[ω].
Quantities are tick counts, equations are morphisms.
ALL dimensionless. No SI, no measurement concept.
Examples: R₀ as η-step ratio, α as γ-oscillation self-coupling.

- SIBridge : EquationLayer
Layer 2: SI bridge. Readout functor R_μ images.
Domain: Layer 1 objects. Codomain: measurement procedures.
Examples: m_e = 9.109×10⁻³¹ kg, α⁻¹ ≈ 137.036.

Instances For

---

### `Tau.BookIV.Physics.instReprEquationLayer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L69-L69)
**instance
Tau.BookIV.Physics.instReprEquationLayer :Repr EquationLayer**

Equations
- Tau.BookIV.Physics.instReprEquationLayer = { reprPrec := Tau.BookIV.Physics.instReprEquationLayer.repr }

---

### `Tau.BookIV.Physics.instReprEquationLayer.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L69-L69)
**def
Tau.BookIV.Physics.instReprEquationLayer.repr :EquationLayer → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.instDecidableEqEquationLayer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L69-L69)
**instance
Tau.BookIV.Physics.instDecidableEqEquationLayer :DecidableEq EquationLayer**

Equations
- Tau.BookIV.Physics.instDecidableEqEquationLayer x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Physics.instBEqEquationLayer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L69-L69)
**instance
Tau.BookIV.Physics.instBEqEquationLayer :BEq EquationLayer**

Equations
- Tau.BookIV.Physics.instBEqEquationLayer = { beq := Tau.BookIV.Physics.instBEqEquationLayer.beq }

---

### `Tau.BookIV.Physics.instBEqEquationLayer.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L69-L69)
**def
Tau.BookIV.Physics.instBEqEquationLayer.beq :EquationLayer → EquationLayer → Bool**

Equations
- Tau.BookIV.Physics.instBEqEquationLayer.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Physics.instInhabitedEquationLayer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L69-L69)
**instance
Tau.BookIV.Physics.instInhabitedEquationLayer :Inhabited EquationLayer**

Equations
- Tau.BookIV.Physics.instInhabitedEquationLayer = { default := Tau.BookIV.Physics.instInhabitedEquationLayer.default }

---

### `Tau.BookIV.Physics.instInhabitedEquationLayer.default`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L69-L69)
**def
Tau.BookIV.Physics.instInhabitedEquationLayer.default :EquationLayer**

Equations
- Tau.BookIV.Physics.instInhabitedEquationLayer.default = Tau.BookIV.Physics.EquationLayer.MathKernel
Instances For

---

### `Tau.BookIV.Physics.InternalIdentity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L75-L95)
**structure
Tau.BookIV.Physics.InternalIdentity :Type**


[IV.D323] An internal identity: a named equation between categorical
objects at a specific ontological layer.

At Layer 1, the `source_sector` and `target_sector` identify which
sector subcategories the domain and codomain live in.
The `is_dimensionless` flag asserts the equation involves only
same-sector morphisms (a ratio, not a cross-sector bridge).

- name : String
Name of the identity (for documentation).

- layer : EquationLayer
Which ontological layer this identity belongs to.

- source_sector : BookIII.Sectors.Sector
Source sector (domain of the morphism).

- target_sector : BookIII.Sectors.Sector
Target sector (codomain of the morphism).

- is_dimensionless : Bool
Whether the identity is dimensionless (same-sector ratio).

- from_iota_alone : Bool
Whether this identity is derivable from ι<sub>τ</sub> alone (no free parameters).

Instances For

---

### `Tau.BookIV.Physics.instReprInternalIdentity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L95-L95)
**instance
Tau.BookIV.Physics.instReprInternalIdentity :Repr InternalIdentity**

Equations
- Tau.BookIV.Physics.instReprInternalIdentity = { reprPrec := Tau.BookIV.Physics.instReprInternalIdentity.repr }

---

### `Tau.BookIV.Physics.instReprInternalIdentity.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L95-L95)
**def
Tau.BookIV.Physics.instReprInternalIdentity.repr :InternalIdentity → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.mass_ratio_identity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L101-L110)
**def
Tau.BookIV.Physics.mass_ratio_identity :InternalIdentity**


The mass ratio R₀ = ι<sub>τ</sub>⁻⁷ − √3·ι<sub>τ</sub>⁻² as an internal identity.
Ontologically: a morphism in the C-sector (strong) that counts how many
η-steps separate the neutron and electron confinement invariants.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.alpha_identity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L112-L121)
**def
Tau.BookIV.Physics.alpha_identity :InternalIdentity**


The fine-structure constant α = (121/225)·ι<sub>τ</sub>⁴ as an internal identity.
Ontologically: the self-coupling strength of the B-sector (EM).
It is the γ-oscillation amplitude ratio for one full EM cycle.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.gravity_coupling_identity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L123-L133)
**def
Tau.BookIV.Physics.gravity_coupling_identity :InternalIdentity**


Gravitational coupling κ_D = 1 − ι<sub>τ</sub> as an internal identity.
Ontologically: the temporal self-coupling of the D-sector (gravity).
It is the α-tick deficit: the fraction of base-time NOT absorbed
by the master constant ι<sub>τ</sub>.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.temporal_complement_identity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L135-L144)
**def
Tau.BookIV.Physics.temporal_complement_identity :InternalIdentity**


The temporal complement κ_A + κ_D = 1 as an internal identity.
Ontologically: the weak and gravitational self-couplings exhaust
the base τ¹ — every α-tick is either weak or gravitational.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.confinement_identity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L146-L155)
**def
Tau.BookIV.Physics.confinement_identity :InternalIdentity**


The confinement coupling κ_C = ι<sub>τ</sub>³/(1−ι<sub>τ</sub>) as an internal identity.
Ontologically: the C-sector (strong) self-coupling, determined by
the ratio of third-order to first-order ι<sub>τ</sub> effects.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Physics.internal_identity_dimensionless`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L161-L169)
**theorem
Tau.BookIV.Physics.internal_identity_dimensionless :mass_ratio_identity.is_dimensionless = true ∧ alpha_identity.is_dimensionless = true ∧ gravity_coupling_identity.is_dimensionless = true ∧ temporal_complement_identity.is_dimensionless = true ∧ confinement_identity.is_dimensionless = true**


[IV.P176] All internal physics identities are dimensionless
(involve same-sector or sector-ratio morphisms, no SI dimensions).

---

### `Tau.BookIV.Physics.mass_ratio_internal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L171-L174)
**theorem
Tau.BookIV.Physics.mass_ratio_internal :mass_ratio_identity.layer = EquationLayer.InternalPhysics**


[IV.T127] The mass ratio identity lives at Layer 1 (internal physics),
not Layer 0 (math) or Layer 2 (SI bridge).

---

### `Tau.BookIV.Physics.all_from_iota`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L176-L183)
**theorem
Tau.BookIV.Physics.all_from_iota :mass_ratio_identity.from_iota_alone = true ∧ alpha_identity.from_iota_alone = true ∧ gravity_coupling_identity.from_iota_alone = true ∧ temporal_complement_identity.from_iota_alone = true ∧ confinement_identity.from_iota_alone = true**


All canonical internal identities are derivable from ι<sub>τ</sub> alone.

---

### `Tau.BookIV.Physics.mass_ratio_strong_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L185-L189)
**theorem
Tau.BookIV.Physics.mass_ratio_strong_sector :mass_ratio_identity.source_sector = BookIII.Sectors.Sector.C ∧ mass_ratio_identity.target_sector = BookIII.Sectors.Sector.C**


The mass ratio is a C-sector (strong) internal identity.

---

### `Tau.BookIV.Physics.alpha_em_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Physics/InternalEquations.lean#L191-L195)
**theorem
Tau.BookIV.Physics.alpha_em_sector :alpha_identity.source_sector = BookIII.Sectors.Sector.B ∧ alpha_identity.target_sector = BookIII.Sectors.Sector.B**


Fine-structure constant is a B-sector (EM) internal identity.
