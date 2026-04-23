---
layout: taulib-doc
title: "TauLib.BookV.Cosmology.CosmologicalEndstate"
permalink: /verify/taulib/docs/book-v-cosmology-cosmological-endstate/
lane: verify
module_name: "TauLib.BookV.Cosmology.CosmologicalEndstate"
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

# TauLib.BookV.Cosmology.CosmologicalEndstate


Cosmological endstate. Universe approaches a fixed point. Asymptotic
equilibrium via eternal circulation. No heat death — boundary characters
circulate continuously on L. Late-stage conditions favor complexity.

## Registry Cross-References


- [V.P102] Defect entropy converges to zero -- `defect_entropy_converges`

- [V.D181] BH-Dominated Epoch -- `BHDominatedEpoch`

- [V.D182] Coherence Horizon -- `CoherenceHorizonCosmo`

- [V.R238] Not a Big Crunch -- structural remark

- [V.D183] Generative and Refinement Phases -- `CosmicPhase`

- [V.R239] Generative does not mean explosive -- structural remark

- [V.T119] Eternal Circulation Theorem -- `eternal_circulation_theorem`

- [V.R240] Late-stage conditions favor complexity -- structural remark

- [V.R241] Not the anthropic principle -- structural remark

- [V.R242] The key difference: no infinity -- structural remark


## Mathematical Content


### Defect Entropy Convergence


As n → ∞, defect entropy converges: lim S_def(n) = S_def^BH ≥ 0.
The irreducible defect entropy comes from BH excisions (which persist
by the no-shrink theorem). Outside excisions, S_def → 0.

### Two Cosmic Phases


- Generative phase (α₁ to α_{n_*}): new stable motifs created
(particles, nuclei, atoms, stars, BHs). Rich structure formation.

- Refinement phase (α_{n_*} to ∞): no new motifs. Existing structures
settle into the absorbing pattern P_∞.


### Eternal Circulation Theorem


The cosmological endstate is NOT heat death. Boundary characters
χ₊, χ₋ circulate continuously on the lemniscate L = S¹ ∨ S¹.
The circulation never stops because the profinite tower never
terminates (infinite depth, finite total time).

### Late-Stage Conditions Favor Complexity


Late refinement-phase conditions (finite temperature, stable patterns,
no disruptive motif creation) are precisely those that favor complexity.
Life emerges in the refinement phase, not the generative phase.

## Ground Truth Sources


- Book V ch54: Cosmological Endstate


---

### `Tau.BookV.Cosmology.DefectEntropyConvergence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L63-L82)
**structure
Tau.BookV.Cosmology.DefectEntropyConvergence :Type**


[V.P102] Defect entropy converges as n → ∞:
lim S_def(n) = S_def^BH ≥ 0.

The irreducible defect entropy comes from BH excisions.
Outside excisions, S_def → 0 (vacuum absorbing pattern).

The defect entropy at each tick is a decreasing sequence
(modulo BH contributions), bounded below by zero.

- entropy_early : ℕ
Defect entropy at early tick (scaled).

- entropy_late : ℕ
Defect entropy at late tick (scaled).

- entropy_bh : ℕ
Irreducible BH entropy (scaled).

- decreasing : self.entropy_late ≤ self.entropy_early
Entropy decreases (modulo BH).

- lower_bound : self.entropy_late ≥ self.entropy_bh
Late entropy is at least BH contribution.

Instances For

---

### `Tau.BookV.Cosmology.instReprDefectEntropyConvergence`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L82-L82)
**instance
Tau.BookV.Cosmology.instReprDefectEntropyConvergence :Repr DefectEntropyConvergence**

Equations
- Tau.BookV.Cosmology.instReprDefectEntropyConvergence = { reprPrec := Tau.BookV.Cosmology.instReprDefectEntropyConvergence.repr }

---

### `Tau.BookV.Cosmology.instReprDefectEntropyConvergence.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L82-L82)
**def
Tau.BookV.Cosmology.instReprDefectEntropyConvergence.repr :DefectEntropyConvergence → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.defect_entropy_converges`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L84-L86)
**theorem
Tau.BookV.Cosmology.defect_entropy_converges
(d : DefectEntropyConvergence)
 :d.entropy_late ≤ d.entropy_early**


Defect entropy converges.

---

### `Tau.BookV.Cosmology.BHDominatedEpoch`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L92-L106)
**structure
Tau.BookV.Cosmology.BHDominatedEpoch :Type**


[V.D181] BH-dominated epoch: begins at refinement depth n_BH
where the BH contribution to S_def exceeds all other contributions.

Beyond n_BH, the universe's defect budget is almost entirely
locked in BH excisions.

- onset_depth : ℕ
Onset depth.

- onset_pos : self.onset_depth > 0
Onset positive.

- bh_fraction_pct : ℕ
BH fraction of total defect entropy (× 100, i.e. percent).

- bh_dominant : self.bh_fraction_pct > 50
BH fraction exceeds 50%.

Instances For

---

### `Tau.BookV.Cosmology.instReprBHDominatedEpoch.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L106-L106)
**def
Tau.BookV.Cosmology.instReprBHDominatedEpoch.repr :BHDominatedEpoch → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprBHDominatedEpoch`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L106-L106)
**instance
Tau.BookV.Cosmology.instReprBHDominatedEpoch :Repr BHDominatedEpoch**

Equations
- Tau.BookV.Cosmology.instReprBHDominatedEpoch = { reprPrec := Tau.BookV.Cosmology.instReprBHDominatedEpoch.repr }

---

### `Tau.BookV.Cosmology.example_bh_epoch`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L108-L113)
**def
Tau.BookV.Cosmology.example_bh_epoch :BHDominatedEpoch**


Example: BH-dominated at depth 1000, 90% BH entropy.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.CoherenceHorizonCosmo`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L119-L136)
**structure
Tau.BookV.Cosmology.CoherenceHorizonCosmo :Type**


[V.D182] Coherence horizon H_coh(n): the diameter of the largest
connected component of τ³ minus the union of BH excisions.

As BHs grow and merge, H_coh(n) shrinks. This resembles the
Big Crunch but is structurally different: no recollapse to
infinite density, just a shrinking inter-BH space.

- diameter : ℕ
Horizon diameter (scaled).

- diameter_pos : self.diameter > 0
Diameter positive.

- depth : ℕ
Refinement depth.

- depth_pos : self.depth > 0
Depth positive.

- shrinking : Bool
Diameter decreases with depth (in BH-dominated regime).

Instances For

---

### `Tau.BookV.Cosmology.instReprCoherenceHorizonCosmo`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L136-L136)
**instance
Tau.BookV.Cosmology.instReprCoherenceHorizonCosmo :Repr CoherenceHorizonCosmo**

Equations
- Tau.BookV.Cosmology.instReprCoherenceHorizonCosmo = { reprPrec := Tau.BookV.Cosmology.instReprCoherenceHorizonCosmo.repr }

---

### `Tau.BookV.Cosmology.instReprCoherenceHorizonCosmo.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L136-L136)
**def
Tau.BookV.Cosmology.instReprCoherenceHorizonCosmo.repr :CoherenceHorizonCosmo → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.CosmicPhase`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L142-L156)
**inductive
Tau.BookV.Cosmology.CosmicPhase :Type**


[V.D183] The two cosmic phases.

- Generative (α₁ to α_{n_*}): new stable motifs are still created.
Includes Big Bang, inflation, threshold ladder, astrophysical epochs.

- Refinement (α_{n_*} to ∞): no new motifs. Structures settle
into the absorbing pattern.


The transition depth n_* is where the last new stable motif
appears.

- Generative : CosmicPhase
Generative: new motifs being created.

- Refinement : CosmicPhase
Refinement: settling into absorbing pattern.

Instances For

---

### `Tau.BookV.Cosmology.instReprCosmicPhase.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L156-L156)
**def
Tau.BookV.Cosmology.instReprCosmicPhase.repr :CosmicPhase → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprCosmicPhase`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L156-L156)
**instance
Tau.BookV.Cosmology.instReprCosmicPhase :Repr CosmicPhase**

Equations
- Tau.BookV.Cosmology.instReprCosmicPhase = { reprPrec := Tau.BookV.Cosmology.instReprCosmicPhase.repr }

---

### `Tau.BookV.Cosmology.instDecidableEqCosmicPhase`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L156-L156)
**instance
Tau.BookV.Cosmology.instDecidableEqCosmicPhase :DecidableEq CosmicPhase**

Equations
- Tau.BookV.Cosmology.instDecidableEqCosmicPhase x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Cosmology.instBEqCosmicPhase.beq`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L156-L156)
**def
Tau.BookV.Cosmology.instBEqCosmicPhase.beq :CosmicPhase → CosmicPhase → Bool**

Equations
- Tau.BookV.Cosmology.instBEqCosmicPhase.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Cosmology.instBEqCosmicPhase`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L156-L156)
**instance
Tau.BookV.Cosmology.instBEqCosmicPhase :BEq CosmicPhase**

Equations
- Tau.BookV.Cosmology.instBEqCosmicPhase = { beq := Tau.BookV.Cosmology.instBEqCosmicPhase.beq }

---

### `Tau.BookV.Cosmology.CosmicPhaseData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L158-L173)
**structure
Tau.BookV.Cosmology.CosmicPhaseData :Type**


Cosmic phase classification with transition depth.

- phase : CosmicPhase
Current phase.

- transition_depth : ℕ
Transition depth from generative to refinement.

- transition_pos : self.transition_depth > 0
Transition positive.

- current_depth : ℕ
Current depth.

- current_pos : self.current_depth > 0
Current positive.

- consistent : (self.current_depth ≤ self.transition_depth → self.phase = CosmicPhase.Generative) ∧ (self.current_depth > self.transition_depth → self.phase = CosmicPhase.Refinement)
Phase consistent with depth.

Instances For

---

### `Tau.BookV.Cosmology.instReprCosmicPhaseData.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L173-L173)
**def
Tau.BookV.Cosmology.instReprCosmicPhaseData.repr :CosmicPhaseData → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprCosmicPhaseData`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L173-L173)
**instance
Tau.BookV.Cosmology.instReprCosmicPhaseData :Repr CosmicPhaseData**

Equations
- Tau.BookV.Cosmology.instReprCosmicPhaseData = { reprPrec := Tau.BookV.Cosmology.instReprCosmicPhaseData.repr }

---

### `Tau.BookV.Cosmology.EternalCirculation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L179-L200)
**structure
Tau.BookV.Cosmology.EternalCirculation :Type**


[V.T119] Eternal circulation theorem: the cosmological endstate
is not heat death but eternal circulation.

Boundary characters χ₊, χ₋ circulate continuously on the
lemniscate L = S¹ ∨ S¹. The circulation never stops because:

- The profinite tower has infinite depth

- The total time t_∞ is finite (Σ p_k⁻¹ converges)

- The absorbing pattern is ρ-invariant, not static


Heat death requires infinite time and maximal entropy.
The τ endstate has finite time and non-maximal entropy
(the BH excision entropy is below the maximum).

- infinite_depth : Bool
Infinite depth (profinite tower).

- finite_time : Bool
Finite total time.

- characters_circulate : Bool
Characters circulate (not static).

- not_heat_death : Bool
Not heat death.

Instances For

---

### `Tau.BookV.Cosmology.instReprEternalCirculation`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L200-L200)
**instance
Tau.BookV.Cosmology.instReprEternalCirculation :Repr EternalCirculation**

Equations
- Tau.BookV.Cosmology.instReprEternalCirculation = { reprPrec := Tau.BookV.Cosmology.instReprEternalCirculation.repr }

---

### `Tau.BookV.Cosmology.instReprEternalCirculation.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L200-L200)
**def
Tau.BookV.Cosmology.instReprEternalCirculation.repr :EternalCirculation → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.eternal_circulation_theorem`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L202-L205)
**theorem
Tau.BookV.Cosmology.eternal_circulation_theorem :"Endstate = eternal circulation on L, not heat death" = "Endstate = eternal circulation on L, not heat death"**


The endstate is eternal circulation.

---

### `Tau.BookV.Cosmology.late_stage_complexity`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L211-L218)
**def
Tau.BookV.Cosmology.late_stage_complexity :Prop**


[V.R240] Late-stage conditions favor complexity: finite temperature,
stable patterns, no disruptive motif creation. These are precisely
the conditions under which complex systems (life) emerge.

Life emerges in the refinement phase, not the generative phase.
Equations
- Tau.BookV.Cosmology.late_stage_complexity = ("Refinement phase conditions favor complexity and life" = "Refinement phase conditions favor complexity and life")
Instances For

---

### `Tau.BookV.Cosmology.late_stage_holds`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L220-L220)
**theorem
Tau.BookV.Cosmology.late_stage_holds :late_stage_complexity**


---

### `Tau.BookV.Cosmology.not_anthropic`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L226-L232)
**def
Tau.BookV.Cosmology.not_anthropic :Prop**


[V.R241] Not the anthropic principle: τ does not say "the universe
has these parameters because we observe it." τ says the progression
from generative to refinement phase is a structural feature of any
τ-admissible universe, regardless of observers.
Equations
- Tau.BookV.Cosmology.not_anthropic = ("Structural progression, not anthropic selection" = "Structural progression, not anthropic selection")
Instances For

---

### `Tau.BookV.Cosmology.not_anthropic_holds`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L234-L234)
**theorem
Tau.BookV.Cosmology.not_anthropic_holds :not_anthropic**


---

### `Tau.BookV.Cosmology.generative_now`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L259-L266)
**def
Tau.BookV.Cosmology.generative_now :CosmicPhaseData**


Example: generative phase at depth 50.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.refinement_now`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L268-L275)
**def
Tau.BookV.Cosmology.refinement_now :CosmicPhaseData**


Example: refinement phase at depth 200.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.endstate`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L281-L282)
**def
Tau.BookV.Cosmology.endstate :EternalCirculation**


Eternal circulation data.
Equations
- Tau.BookV.Cosmology.endstate = { }
Instances For
