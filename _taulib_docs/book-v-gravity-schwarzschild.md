---
layout: taulib-doc
title: "TauLib.BookV.Gravity.Schwarzschild"
permalink: /verify/taulib/docs/book-v-gravity-schwarzschild/
lane: verify
module_name: "TauLib.BookV.Gravity.Schwarzschild"
book: "V"
book_label: "Macrocosm"
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
    book: "Book V"
    status: "Frozen"
    updated: "April 2026"
---

# TauLib.BookV.Gravity.Schwarzschild


Schwarzschild relation, black hole mass index, and the No-Shrink theorem.

## Registry Cross-References


- [V.D07] BH Mass Index — `BHMassIndex`

- [V.D08] Schwarzschild Relation — `SchwarzschildRelation`

- [V.T03] No-Shrink Theorem — `NoShrinkProperty`

- [V.D09] BH Evolution Mode — `BHEvolutionMode`

- [V.R02] Hawking evaporation forbidden — structural remark


## Mathematical Content


### Black Hole Mass Index


M_n(x) := MassIdx(NF_ω(x)) = α-Idx readout from normal-form
stabilized torus vacuum.

Properties:


- Not a primitive scalar but a resistance/scale index

- Comes with minimal carrier that can host it

- Monotone under admissible evolution (No-Shrink)


### Tau-Schwarzschild Theorem


For all mature BH states x:

```
R_n(x) = 2 · G_τ · M_n(x)
```


Both R and M are readouts of a **single surviving scale parameter**
on the stabilized torus vacuum. The linear coupling is the canonical
invariance structure from the τ-kernel.

### No-Shrink Theorem


For n ≥ n* (maturity horizon): no τ-admissible evolution step
decreases M_n(x).

Three admissible BH evolution modes (all monotone in M):

- **Ringdown**: Internal normalization (mass preserved)

- **Transport**: Boundary-induced holomorphic transport (mass preserved)

- **Fusion**: Merger/fission (mass strictly increases)


### Consequences


- **Hawking evaporation is forbidden**: The No-Shrink theorem directly
contradicts BH mass loss. Orthodox Hawking radiation exists as a
coarse-grain thermal READOUT but mass cannot decrease.

- **Bekenstein area-law entropy**: Emerges as readout, not implication
of mass loss.

- **Chandrasekhar limit** = first major radius where ι<sub>τ</sub> shape ratio
can be refinement-invariantly realized = minimal maturity scale.


## Ground Truth Sources


- gravity-einstein.json: schwarzschild-relation, no-shrink-theorem

- gravity-einstein.json: bh-mass-index, bh-evolution-modes

- gravity-einstein.json: hawking-bekenstein-reinterpretation


---

### `Tau.BookV.Gravity.BHMassIndex`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L72-L92)
**structure
Tau.BookV.Gravity.BHMassIndex :Type**


[V.D07] Black hole mass index: the α-Idx readout from a
normal-form stabilized torus vacuum.

M_n(x) := MassIdx(NF_ω(x))

Properties:


- Resistance/scale index of stabilized torus (not primitive scalar)

- Comes with minimal carrier that can host it

- Monotone under admissible evolution (No-Shrink)


- mass_numer : ℕ
Mass index numerator (scaled).

- mass_denom : ℕ
Mass index denominator.

- denom_pos : self.mass_denom > 0
Denominator positive.

- mass_positive : self.mass_numer > 0
Mass is positive for any physical BH.

- is_mature : Bool
Whether this state is beyond the maturity horizon n*.

Instances For

---

### `Tau.BookV.Gravity.instReprBHMassIndex`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L92-L92)
**instance
Tau.BookV.Gravity.instReprBHMassIndex :Repr BHMassIndex**

Equations
- Tau.BookV.Gravity.instReprBHMassIndex = { reprPrec := Tau.BookV.Gravity.instReprBHMassIndex.repr }

---

### `Tau.BookV.Gravity.instReprBHMassIndex.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L92-L92)
**def
Tau.BookV.Gravity.instReprBHMassIndex.repr :BHMassIndex → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.BHMassIndex.toFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L94-L96)
**def
Tau.BookV.Gravity.BHMassIndex.toFloat
(m : BHMassIndex)
 :Float**


Float display for BH mass.
Equations
- m.toFloat = Float.ofNat m.mass_numer / Float.ofNat m.mass_denom
Instances For

---

### `Tau.BookV.Gravity.SchwarzschildRelation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L102-L128)
**structure
Tau.BookV.Gravity.SchwarzschildRelation :Type**


[V.D08] Tau-Schwarzschild relation: R_n(x) = 2 · G_τ · M_n(x).

Linear coupling between major radius index and mass index,
arising from the single surviving scale degree of freedom
on the stabilized torus vacuum.

BH topology is T² (not S²) — only scale remains as free parameter.

Cross-multiplied form:
radius_numer · mass_denom · g_denom =
2 · g_numer · mass_numer · radius_denom

- radius_numer : ℕ
Major radius index numerator R_n(x).

- radius_denom : ℕ
Major radius index denominator.

- radius_denom_pos : self.radius_denom > 0
Radius denominator positive.

- mass : BHMassIndex
The BH mass index.

- g_tau : GravConstant
The gravitational constant.

- schwarzschild_identity : self.radius_numer * self.mass.mass_denom * self.g_tau.g_denom = 2 * self.g_tau.g_numer * self.mass.mass_numer * self.radius_denom
The Schwarzschild identity: R = 2 G_τ M (cross-multiplied).

Instances For

---

### `Tau.BookV.Gravity.instReprSchwarzschildRelation.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L128-L128)
**def
Tau.BookV.Gravity.instReprSchwarzschildRelation.repr :SchwarzschildRelation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.instReprSchwarzschildRelation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L128-L128)
**instance
Tau.BookV.Gravity.instReprSchwarzschildRelation :Repr SchwarzschildRelation**

Equations
- Tau.BookV.Gravity.instReprSchwarzschildRelation = { reprPrec := Tau.BookV.Gravity.instReprSchwarzschildRelation.repr }

---

### `Tau.BookV.Gravity.SchwarzschildRelation.radiusFloat`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L130-L132)
**def
Tau.BookV.Gravity.SchwarzschildRelation.radiusFloat
(s : SchwarzschildRelation)
 :Float**


Radius as Float.
Equations
- s.radiusFloat = Float.ofNat s.radius_numer / Float.ofNat s.radius_denom
Instances For

---

### `Tau.BookV.Gravity.NoShrinkProperty`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L138-L152)
**structure
Tau.BookV.Gravity.NoShrinkProperty :Type**


[V.T03] No-Shrink Theorem: beyond the maturity horizon n*,
no τ-admissible evolution step can decrease the BH mass index.

This is the τ-native mass monotonicity principle.

Consequences:


- Hawking evaporation is forbidden (mass cannot decrease)

- Bekenstein area-law entropy = readout, not mass loss implication

- BH is permanent ontic object (no information loss)


- mass : BHMassIndex
The BH mass that cannot shrink.

- mature_proof : self.mass.is_mature = true
The BH must be mature (beyond maturity horizon).

Instances For

---

### `Tau.BookV.Gravity.instReprNoShrinkProperty.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L152-L152)
**def
Tau.BookV.Gravity.instReprNoShrinkProperty.repr :NoShrinkProperty → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.instReprNoShrinkProperty`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L152-L152)
**instance
Tau.BookV.Gravity.instReprNoShrinkProperty :Repr NoShrinkProperty**

Equations
- Tau.BookV.Gravity.instReprNoShrinkProperty = { reprPrec := Tau.BookV.Gravity.instReprNoShrinkProperty.repr }

---

### `Tau.BookV.Gravity.BHEvolutionMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L158-L177)
**inductive
Tau.BookV.Gravity.BHEvolutionMode :Type**


[V.D09] The three admissible BH evolution modes.

All three are monotone in the mass index M_n(x):

- Ringdown preserves M

- Transport preserves M

- Fusion strictly increases M


No other τ-admissible evolution exists for mature BH states.

- Ringdown : BHEvolutionMode
Internal ringdown normalization.
Mass preserved; internal degrees of freedom settle.

- Transport : BHEvolutionMode
Boundary-induced holomorphic transport.
Mass preserved; BH moves or deforms within carrier bounds.

- Fusion : BHEvolutionMode
Merger/fusion of two BH states.
Mass strictly increases: M(result) > max(M₁, M₂).
Gen_ω(g₁, g₂) := Norm_ω(Fuse_ω(g₁, g₂)).

Instances For

---

### `Tau.BookV.Gravity.instReprBHEvolutionMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L177-L177)
**instance
Tau.BookV.Gravity.instReprBHEvolutionMode :Repr BHEvolutionMode**

Equations
- Tau.BookV.Gravity.instReprBHEvolutionMode = { reprPrec := Tau.BookV.Gravity.instReprBHEvolutionMode.repr }

---

### `Tau.BookV.Gravity.instReprBHEvolutionMode.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L177-L177)
**def
Tau.BookV.Gravity.instReprBHEvolutionMode.repr :BHEvolutionMode → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.instDecidableEqBHEvolutionMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L177-L177)
**instance
Tau.BookV.Gravity.instDecidableEqBHEvolutionMode :DecidableEq BHEvolutionMode**

Equations
- Tau.BookV.Gravity.instDecidableEqBHEvolutionMode x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Gravity.instBEqBHEvolutionMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L177-L177)
**instance
Tau.BookV.Gravity.instBEqBHEvolutionMode :BEq BHEvolutionMode**

Equations
- Tau.BookV.Gravity.instBEqBHEvolutionMode = { beq := Tau.BookV.Gravity.instBEqBHEvolutionMode.beq }

---

### `Tau.BookV.Gravity.instBEqBHEvolutionMode.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L177-L177)
**def
Tau.BookV.Gravity.instBEqBHEvolutionMode.beq :BHEvolutionMode → BHEvolutionMode → Bool**

Equations
- Tau.BookV.Gravity.instBEqBHEvolutionMode.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Gravity.instInhabitedBHEvolutionMode.default`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L177-L177)
**def
Tau.BookV.Gravity.instInhabitedBHEvolutionMode.default :BHEvolutionMode**

Equations
- Tau.BookV.Gravity.instInhabitedBHEvolutionMode.default = Tau.BookV.Gravity.BHEvolutionMode.Ringdown
Instances For

---

### `Tau.BookV.Gravity.instInhabitedBHEvolutionMode`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L177-L177)
**instance
Tau.BookV.Gravity.instInhabitedBHEvolutionMode :Inhabited BHEvolutionMode**

Equations
- Tau.BookV.Gravity.instInhabitedBHEvolutionMode = { default := Tau.BookV.Gravity.instInhabitedBHEvolutionMode.default }

---

### `Tau.BookV.Gravity.BHEvolutionMode.preserves_mass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L183-L187)
**def
Tau.BookV.Gravity.BHEvolutionMode.preserves_mass :BHEvolutionMode → Bool**


Whether an evolution mode preserves mass (vs. increases).
Equations
- Tau.BookV.Gravity.BHEvolutionMode.Ringdown.preserves_mass = true
- Tau.BookV.Gravity.BHEvolutionMode.Transport.preserves_mass = true
- Tau.BookV.Gravity.BHEvolutionMode.Fusion.preserves_mass = false
Instances For

---

### `Tau.BookV.Gravity.BHEvolutionMode.is_internal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L189-L193)
**def
Tau.BookV.Gravity.BHEvolutionMode.is_internal :BHEvolutionMode → Bool**


Whether an evolution mode is internal (vs. requires external input).
Equations
- Tau.BookV.Gravity.BHEvolutionMode.Ringdown.is_internal = true
- Tau.BookV.Gravity.BHEvolutionMode.Transport.is_internal = false
- Tau.BookV.Gravity.BHEvolutionMode.Fusion.is_internal = false
Instances For

---

### `Tau.BookV.Gravity.ChandrasekharLimit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L199-L217)
**structure
Tau.BookV.Gravity.ChandrasekharLimit :Type**


[V.R02] The Chandrasekhar limit reinterpreted in the τ-framework.

M_Chandrasekhar = first major radius where the ι<sub>τ</sub> shape ratio
can be refinement-invariantly realized = **minimal maturity scale**.

This is NOT a PDE equilibrium (TOV solution) but a threshold
where the torus vacuum first achieves ontic stability.

The Hawking-Bekenstein radiation exists as coarse-grain thermal
readout on the empirical layer, but evaporation is **forbidden**
by the No-Shrink theorem (mass monotonicity).

- minimal_mass : BHMassIndex
Minimal mature mass index.

- is_mature : self.minimal_mass.is_mature = true
Must be mature by definition.

- is_minimal : Bool
No smaller mature BH exists (minimality).

Instances For

---

### `Tau.BookV.Gravity.instReprChandrasekharLimit.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L217-L217)
**def
Tau.BookV.Gravity.instReprChandrasekharLimit.repr :ChandrasekharLimit → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Gravity.instReprChandrasekharLimit`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L217-L217)
**instance
Tau.BookV.Gravity.instReprChandrasekharLimit :Repr ChandrasekharLimit**

Equations
- Tau.BookV.Gravity.instReprChandrasekharLimit = { reprPrec := Tau.BookV.Gravity.instReprChandrasekharLimit.repr }

---

### `Tau.BookV.Gravity.three_evolution_modes`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L223-L226)
**theorem
Tau.BookV.Gravity.three_evolution_modes
(m : BHEvolutionMode)
 :m = BHEvolutionMode.Ringdown ∨ m = BHEvolutionMode.Transport ∨ m = BHEvolutionMode.Fusion**


Exactly 3 BH evolution modes.

---

### `Tau.BookV.Gravity.fusion_increases_mass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L228-L230)
**theorem
Tau.BookV.Gravity.fusion_increases_mass :BHEvolutionMode.Fusion.preserves_mass = false**


Fusion increases mass (does not preserve).

---

### `Tau.BookV.Gravity.ringdown_preserves_mass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L232-L234)
**theorem
Tau.BookV.Gravity.ringdown_preserves_mass :BHEvolutionMode.Ringdown.preserves_mass = true**


Ringdown preserves mass.

---

### `Tau.BookV.Gravity.transport_preserves_mass`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L236-L238)
**theorem
Tau.BookV.Gravity.transport_preserves_mass :BHEvolutionMode.Transport.preserves_mass = true**


Transport preserves mass.

---

### `Tau.BookV.Gravity.ringdown_internal`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L240-L242)
**theorem
Tau.BookV.Gravity.ringdown_internal :BHEvolutionMode.Ringdown.is_internal = true**


Ringdown is internal.

---

### `Tau.BookV.Gravity.no_shrink_requires_maturity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L244-L246)
**theorem
Tau.BookV.Gravity.no_shrink_requires_maturity
(p : NoShrinkProperty)
 :p.mass.is_mature = true**


No-Shrink requires maturity.

---

### `Tau.BookV.Gravity.schwarzschild_linear`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Gravity/Schwarzschild.lean#L248-L253)
**theorem
Tau.BookV.Gravity.schwarzschild_linear
(s : SchwarzschildRelation)
 :s.radius_numer * s.mass.mass_denom * s.g_tau.g_denom = 2 * s.g_tau.g_numer * s.mass.mass_numer * s.radius_denom**


Schwarzschild is linear: R is proportional to M
(the proportionality constant is 2G_τ).
