---
layout: taulib-doc
title: "TauLib.BookIV.Particles.SectorAtlas"
permalink: /verify/taulib/docs/book-iv-particles-sector-atlas/
lane: verify
module_name: "TauLib.BookIV.Particles.SectorAtlas"
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

# TauLib.BookIV.Particles.SectorAtlas


Complete sector taxonomy: the map of all 5 sectors with associated particles,
force-carrier assignment, sector-particle correspondence table, 9-element
canonical generator set, generator adequacy, tau-Yukawa couplings, and the
parameter-count comparison (9 generators vs SM's 19 free parameters).

## Registry Cross-References


- [IV.T80] Exactly Four Primitive Forces (Physical Reading) — `exactly_four_primitive_forces`

- [IV.T81] Exactly One Derived Sector — `exactly_one_derived_sector`

- [IV.D194] 9-Element Canonical Generator Set — `CanonicalGeneratorSet`

- [IV.T82] Generator Adequacy and Minimality — `generator_adequacy`

- [IV.D195] τ-Yukawa Coupling — `TauYukawaCoupling`

- [IV.R106] Book III template vs Book IV instantiation — comment-only (not_applicable)

- [IV.R107] Topological rigidity — comment-only (not_applicable)

- [IV.R108] Yukawa as readout not parameter — `yukawa_is_readout`

- [IV.R109] SM parameter count comparison — `sm_parameter_comparison`

- [IV.R110] No BSM particles — `no_bsm_particles`


## Mathematical Content


Chapter 45 presents the complete sector atlas: a 13-row table mapping every
sector to its force carriers, matter content, and coupling constants. The
boundary holonomy algebra H_∂[ω] admits exactly 4 primitive sector characters
(D/Gravity, A/Weak, B/EM, C/Strong) and exactly 1 derived sector
(ω = B ∩ C = Higgs). The 9 canonical generators (4 vacuum idempotents +
4 gap quanta + 1 crossing generator ι<sub>τ</sub>) generate the entire algebra,
and no proper subset suffices. The τ-Yukawa couplings are readouts of
winding-mode geometry, not free parameters.

## Ground Truth Sources


- Chapter 45 of Book IV (2nd Edition)


---

### `Tau.BookIV.Particles.ExactlyFourPrimitive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L47-L65)
**structure
Tau.BookIV.Particles.ExactlyFourPrimitive :Type**


[IV.T80] The boundary holonomy algebra admits exactly four linearly
independent primitive sector characters, instantiating at E₁ as:

- D = Gravity (α-generator)

- A = Weak (π-generator)

- B = EM (γ-generator)

- C = Strong (η-generator)


No fifth primitive sector exists and no GUT unification reduces
this count. The four-ness is a topological invariant of L = S¹ ∨ S¹.

- count : ℕ
Number of primitive sectors.

- sectors : List BookIII.Sectors.Sector
Sectors are: D, A, B, C.

- independent : Bool
Each is linearly independent.

- no_fifth : Bool
No fifth sector.

Instances For

---

### `Tau.BookIV.Particles.instReprExactlyFourPrimitive`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L65-L65)
**instance
Tau.BookIV.Particles.instReprExactlyFourPrimitive :Repr ExactlyFourPrimitive**

Equations
- Tau.BookIV.Particles.instReprExactlyFourPrimitive = { reprPrec := Tau.BookIV.Particles.instReprExactlyFourPrimitive.repr }

---

### `Tau.BookIV.Particles.instReprExactlyFourPrimitive.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L65-L65)
**def
Tau.BookIV.Particles.instReprExactlyFourPrimitive.repr :ExactlyFourPrimitive → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.exactly_four_primitive_forces`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L67-L67)
**def
Tau.BookIV.Particles.exactly_four_primitive_forces :ExactlyFourPrimitive**

Equations
- Tau.BookIV.Particles.exactly_four_primitive_forces = { }
Instances For

---

### `Tau.BookIV.Particles.four_primitive_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L69-L70)
**theorem
Tau.BookIV.Particles.four_primitive_count :exactly_four_primitive_forces.count = 4**


---

### `Tau.BookIV.Particles.four_primitive_sectors`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L72-L73)
**theorem
Tau.BookIV.Particles.four_primitive_sectors :exactly_four_primitive_forces.sectors.length = 4**


---

### `Tau.BookIV.Particles.ExactlyOneDerived`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L79-L97)
**structure
Tau.BookIV.Particles.ExactlyOneDerived :Type**


[IV.T81] The lemniscate L = S¹ ∨ S¹ has exactly one self-intersection
point, so the sector decomposition admits exactly one derived sector:
ω = B ∩ C = γ ∩ η (Higgs/mass mechanism).

No other pair of primitive sectors produces a derived sector.
This is topologically rigid: any homeomorphism of L preserves the
unique wedge point, so the ω-sector cannot be removed.

- count : ℕ
Number of derived sectors.

- derived : BookIII.Sectors.Sector
The derived sector.

- parent_B : BookIII.Sectors.Sector
Parent sectors.

- parent_C : BookIII.Sectors.Sector
Parent sectors.

- rigid : Bool
Topologically rigid.

Instances For

---

### `Tau.BookIV.Particles.instReprExactlyOneDerived`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L97-L97)
**instance
Tau.BookIV.Particles.instReprExactlyOneDerived :Repr ExactlyOneDerived**

Equations
- Tau.BookIV.Particles.instReprExactlyOneDerived = { reprPrec := Tau.BookIV.Particles.instReprExactlyOneDerived.repr }

---

### `Tau.BookIV.Particles.instReprExactlyOneDerived.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L97-L97)
**def
Tau.BookIV.Particles.instReprExactlyOneDerived.repr :ExactlyOneDerived → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.exactly_one_derived_sector`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L99-L99)
**def
Tau.BookIV.Particles.exactly_one_derived_sector :ExactlyOneDerived**

Equations
- Tau.BookIV.Particles.exactly_one_derived_sector = { }
Instances For

---

### `Tau.BookIV.Particles.one_derived_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L101-L102)
**theorem
Tau.BookIV.Particles.one_derived_count :exactly_one_derived_sector.count = 1**


---

### `Tau.BookIV.Particles.total_sector_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L104-L107)
**theorem
Tau.BookIV.Particles.total_sector_count :exactly_four_primitive_forces.count + exactly_one_derived_sector.count = 5**


Total sector count: 4 primitive + 1 derived = 5.

---

### `Tau.BookIV.Particles.GeneratorGroup`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L113-L121)
**inductive
Tau.BookIV.Particles.GeneratorGroup :Type**


Generator group classification within H_∂[ω].

- vacuumIdempotent : GeneratorGroup
Vacuum idempotent (one per primitive sector).

- gapQuantum : GeneratorGroup
Gap quantum (one per primitive sector).

- crossingGenerator : GeneratorGroup
Crossing generator (unique, ι<sub>τ</sub>).

Instances For

---

### `Tau.BookIV.Particles.instReprGeneratorGroup.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L121-L121)
**def
Tau.BookIV.Particles.instReprGeneratorGroup.repr :GeneratorGroup → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprGeneratorGroup`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L121-L121)
**instance
Tau.BookIV.Particles.instReprGeneratorGroup :Repr GeneratorGroup**

Equations
- Tau.BookIV.Particles.instReprGeneratorGroup = { reprPrec := Tau.BookIV.Particles.instReprGeneratorGroup.repr }

---

### `Tau.BookIV.Particles.instDecidableEqGeneratorGroup`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L121-L121)
**instance
Tau.BookIV.Particles.instDecidableEqGeneratorGroup :DecidableEq GeneratorGroup**

Equations
- Tau.BookIV.Particles.instDecidableEqGeneratorGroup x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookIV.Particles.instBEqGeneratorGroup.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L121-L121)
**def
Tau.BookIV.Particles.instBEqGeneratorGroup.beq :GeneratorGroup → GeneratorGroup → Bool**

Equations
- Tau.BookIV.Particles.instBEqGeneratorGroup.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookIV.Particles.instBEqGeneratorGroup`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L121-L121)
**instance
Tau.BookIV.Particles.instBEqGeneratorGroup :BEq GeneratorGroup**

Equations
- Tau.BookIV.Particles.instBEqGeneratorGroup = { beq := Tau.BookIV.Particles.instBEqGeneratorGroup.beq }

---

### `Tau.BookIV.Particles.CanonicalGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L123-L135)
**structure
Tau.BookIV.Particles.CanonicalGenerator :Type**


[IV.D194] A canonical generator of the boundary holonomy algebra.
The 9 generators come in three groups:


- 4 sector vacuum idempotents

- 4 gap quanta (one per sector)

- 1 crossing generator ι<sub>τ</sub> coupling χ₊ and χ₋


- label : String
Generator label.

- group : GeneratorGroup
Group classification.

- sector : Option BookIII.Sectors.Sector
Associated sector (if applicable).

Instances For

---

### `Tau.BookIV.Particles.instReprCanonicalGenerator`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L135-L135)
**instance
Tau.BookIV.Particles.instReprCanonicalGenerator :Repr CanonicalGenerator**

Equations
- Tau.BookIV.Particles.instReprCanonicalGenerator = { reprPrec := Tau.BookIV.Particles.instReprCanonicalGenerator.repr }

---

### `Tau.BookIV.Particles.instReprCanonicalGenerator.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L135-L135)
**def
Tau.BookIV.Particles.instReprCanonicalGenerator.repr :CanonicalGenerator → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.canonical_generator_set`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L137-L151)
**def
Tau.BookIV.Particles.canonical_generator_set :List CanonicalGenerator**


[IV.D194] The 9-element canonical generator set.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.nine_generators`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L153-L153)
**theorem
Tau.BookIV.Particles.nine_generators :canonical_generator_set.length = 9**


---

### `Tau.BookIV.Particles.GeneratorAdequacy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L159-L172)
**structure
Tau.BookIV.Particles.GeneratorAdequacy :Type**


[IV.T82] The 9 canonical generators generate the entire boundary
holonomy algebra H_∂[ω], and no proper subset suffices.
Every polynomial expression in these 9 yields a physical observable.
Adequacy: span = H_∂[ω]. Minimality: removal of any one breaks span.

- total : ℕ
Total generators.

- adequate : Bool
Adequate: they generate H_∂[ω].

- minimal : Bool
Minimal: no proper subset suffices.

- all_observable : Bool
Every polynomial is a physical observable.

Instances For

---

### `Tau.BookIV.Particles.instReprGeneratorAdequacy.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L172-L172)
**def
Tau.BookIV.Particles.instReprGeneratorAdequacy.repr :GeneratorAdequacy → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprGeneratorAdequacy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L172-L172)
**instance
Tau.BookIV.Particles.instReprGeneratorAdequacy :Repr GeneratorAdequacy**

Equations
- Tau.BookIV.Particles.instReprGeneratorAdequacy = { reprPrec := Tau.BookIV.Particles.instReprGeneratorAdequacy.repr }

---

### `Tau.BookIV.Particles.generator_adequacy`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L174-L174)
**def
Tau.BookIV.Particles.generator_adequacy :GeneratorAdequacy**

Equations
- Tau.BookIV.Particles.generator_adequacy = { }
Instances For

---

### `Tau.BookIV.Particles.adequacy_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L176-L176)
**theorem
Tau.BookIV.Particles.adequacy_count :generator_adequacy.total = 9**


---

### `Tau.BookIV.Particles.is_adequate`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L177-L177)
**theorem
Tau.BookIV.Particles.is_adequate :generator_adequacy.adequate = true**


---

### `Tau.BookIV.Particles.is_minimal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L178-L178)
**theorem
Tau.BookIV.Particles.is_minimal :generator_adequacy.minimal = true**


---

### `Tau.BookIV.Particles.TauYukawaCoupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L184-L206)
**structure
Tau.BookIV.Particles.TauYukawaCoupling :Type**


[IV.D195] τ-Yukawa coupling: the coupling of a fermion mode χ_{m,n}
in sector X to the Higgs sector ω.

y_f = κ(ω) / √(m² + n²·ι<sub>τ</sub>²) × Γ_gen(f)

Determined by winding-mode overlap with the ω-sector crossing character.
NOT a free parameter — a readout of fiber geometry.

- fermion : String
Fermion name.

- sector : BookIII.Sectors.Sector
Sector.

- generation : ℕ
Generation (1, 2, or 3).

- coupling_numer : ℕ
Approximate coupling (numerator, scaled ×10⁶).

- coupling_denom : ℕ
Coupling denominator.

- denom_pos : self.coupling_denom > 0
Denominator positive.

- gen_valid : self.generation ≥ 1 ∧ self.generation ≤ 3
Valid generation.

Instances For

---

### `Tau.BookIV.Particles.instReprTauYukawaCoupling.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L206-L206)
**def
Tau.BookIV.Particles.instReprTauYukawaCoupling.repr :TauYukawaCoupling → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprTauYukawaCoupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L206-L206)
**instance
Tau.BookIV.Particles.instReprTauYukawaCoupling :Repr TauYukawaCoupling**

Equations
- Tau.BookIV.Particles.instReprTauYukawaCoupling = { reprPrec := Tau.BookIV.Particles.instReprTauYukawaCoupling.repr }

---

### `Tau.BookIV.Particles.YukawaReadout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L212-L225)
**structure
Tau.BookIV.Particles.YukawaReadout :Type**


[IV.R108] The Yukawa hierarchy spanning six orders of magnitude
(y_e ≈ 3×10⁻⁶ to y_t ≈ 1) is a readout of winding-mode geometry
on T², not a set of independent parameters. It arises from compounding
three geometric factors, each determined by ι<sub>τ</sub> alone.

- span_orders : ℕ
Orders of magnitude span.

- num_factors : ℕ
Number of geometric factors.

- iota_determined : Bool
All determined by ι<sub>τ</sub>.

- not_free : Bool
Not free parameters.

Instances For

---

### `Tau.BookIV.Particles.instReprYukawaReadout.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L225-L225)
**def
Tau.BookIV.Particles.instReprYukawaReadout.repr :YukawaReadout → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprYukawaReadout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L225-L225)
**instance
Tau.BookIV.Particles.instReprYukawaReadout :Repr YukawaReadout**

Equations
- Tau.BookIV.Particles.instReprYukawaReadout = { reprPrec := Tau.BookIV.Particles.instReprYukawaReadout.repr }

---

### `Tau.BookIV.Particles.yukawa_is_readout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L227-L227)
**def
Tau.BookIV.Particles.yukawa_is_readout :YukawaReadout**

Equations
- Tau.BookIV.Particles.yukawa_is_readout = { }
Instances For

---

### `Tau.BookIV.Particles.yukawa_span`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L229-L229)
**theorem
Tau.BookIV.Particles.yukawa_span :yukawa_is_readout.span_orders = 6**


---

### `Tau.BookIV.Particles.yukawa_not_free`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L230-L230)
**theorem
Tau.BookIV.Particles.yukawa_not_free :yukawa_is_readout.not_free = true**


---

### `Tau.BookIV.Particles.ParameterComparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L236-L252)
**structure
Tau.BookIV.Particles.ParameterComparison :Type**


[IV.R109] Parameter count comparison:


- Standard Model: ~19 free parameters

- Category τ: 9 canonical generators, of which only 1 (ι<sub>τ</sub>) is
a numerical constant; the remaining 8 are structural objects
uniquely determined by the boundary algebra.


Reduction: 19 free parameters → 1 master constant.

- sm_params : ℕ
SM free parameters.

- tau_generators : ℕ
τ canonical generators.

- tau_numerical : ℕ
Of which numerical constants.

- tau_structural : ℕ
Of which structural (determined by algebra).

Instances For

---

### `Tau.BookIV.Particles.instReprParameterComparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L252-L252)
**instance
Tau.BookIV.Particles.instReprParameterComparison :Repr ParameterComparison**

Equations
- Tau.BookIV.Particles.instReprParameterComparison = { reprPrec := Tau.BookIV.Particles.instReprParameterComparison.repr }

---

### `Tau.BookIV.Particles.instReprParameterComparison.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L252-L252)
**def
Tau.BookIV.Particles.instReprParameterComparison.repr :ParameterComparison → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.sm_parameter_comparison`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L254-L254)
**def
Tau.BookIV.Particles.sm_parameter_comparison :ParameterComparison**

Equations
- Tau.BookIV.Particles.sm_parameter_comparison = { }
Instances For

---

### `Tau.BookIV.Particles.sm_has_19`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L256-L256)
**theorem
Tau.BookIV.Particles.sm_has_19 :sm_parameter_comparison.sm_params = 19**


---

### `Tau.BookIV.Particles.tau_one_constant`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L257-L257)
**theorem
Tau.BookIV.Particles.tau_one_constant :sm_parameter_comparison.tau_numerical = 1**


---

### `Tau.BookIV.Particles.structural_plus_numerical`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L258-L261)
**theorem
Tau.BookIV.Particles.structural_plus_numerical :sm_parameter_comparison.tau_structural + sm_parameter_comparison.tau_numerical = sm_parameter_comparison.tau_generators**


---

### `Tau.BookIV.Particles.NoBSM`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L267-L283)
**structure
Tau.BookIV.Particles.NoBSM :Type**


[IV.R110] The periodic table of τ-particles contains no BSM particles:
no supersymmetric partners, no leptoquarks, no right-handed neutrinos,
no fourth generation, no dark matter candidates with new quantum numbers.
This is a structural consequence of the Exactly-Four Theorem and
lemniscate topology.

- no_susy : Bool
No supersymmetry.

- no_leptoquarks : Bool
No leptoquarks.

- no_rh_neutrinos : Bool
No right-handed neutrinos.

- no_fourth_gen : Bool
No fourth generation.

- no_new_dm : Bool
No new dark matter candidates.

Instances For

---

### `Tau.BookIV.Particles.instReprNoBSM.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L283-L283)
**def
Tau.BookIV.Particles.instReprNoBSM.repr :NoBSM → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprNoBSM`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L283-L283)
**instance
Tau.BookIV.Particles.instReprNoBSM :Repr NoBSM**

Equations
- Tau.BookIV.Particles.instReprNoBSM = { reprPrec := Tau.BookIV.Particles.instReprNoBSM.repr }

---

### `Tau.BookIV.Particles.no_bsm_particles`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L285-L285)
**def
Tau.BookIV.Particles.no_bsm_particles :NoBSM**

Equations
- Tau.BookIV.Particles.no_bsm_particles = { }
Instances For

---

### `Tau.BookIV.Particles.bsm_all_excluded`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L287-L292)
**theorem
Tau.BookIV.Particles.bsm_all_excluded :no_bsm_particles.no_susy = true ∧ no_bsm_particles.no_leptoquarks = true ∧ no_bsm_particles.no_rh_neutrinos = true ∧ no_bsm_particles.no_fourth_gen = true ∧ no_bsm_particles.no_new_dm = true**


---

### `Tau.BookIV.Particles.AtlasEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L298-L308)
**structure
Tau.BookIV.Particles.AtlasEntry :Type**


An entry in the 13-row sector atlas table.

- label : String
Row label.

- sector : BookIII.Sectors.Sector
Sector.

- carrier : String
Force carrier(s).

- matter : String
Matter content.

Instances For

---

### `Tau.BookIV.Particles.instReprAtlasEntry.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L308-L308)
**def
Tau.BookIV.Particles.instReprAtlasEntry.repr :AtlasEntry → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.instReprAtlasEntry`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L308-L308)
**instance
Tau.BookIV.Particles.instReprAtlasEntry :Repr AtlasEntry**

Equations
- Tau.BookIV.Particles.instReprAtlasEntry = { reprPrec := Tau.BookIV.Particles.instReprAtlasEntry.repr }

---

### `Tau.BookIV.Particles.sector_atlas`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L310-L318)
**def
Tau.BookIV.Particles.sector_atlas :List AtlasEntry**


The sector atlas: complete mapping from sectors to physical content.
This is the E₁ instantiation of Book III's abstract template.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.Particles.atlas_five_entries`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookIV/Particles/SectorAtlas.lean#L320-L320)
**theorem
Tau.BookIV.Particles.atlas_five_entries :sector_atlas.length = 5**
