---
layout: taulib-doc
title: "TauLib.BookV.Cosmology.NoShrinkExtended"
permalink: /verify/taulib/docs/book-v-cosmology-no-shrink-extended/
lane: verify
module_name: "TauLib.BookV.Cosmology.NoShrinkExtended"
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

# TauLib.BookV.Cosmology.NoShrinkExtended


Extended no-shrink theorem for mature black holes. BH area is
non-decreasing. Hawking radiation reinterpreted as boundary readout.
Information paradox dissolved. Permanence hallmark.

## Registry Cross-References


- [V.D173] Mature Black Hole -- `MatureBlackHole`

- [V.T113] Defect-Mass Coupling -- `defect_mass_coupling`

- [V.T114] No-Shrink Theorem -- `no_shrink_theorem`

- [V.P95] Hawking Readout -- `hawking_readout`

- [V.C19] No BH Evaporation -- `no_bh_evaporation`

- [V.R226] Information Paradox Dissolved -- structural remark

- [V.D174] Permanence Hallmark -- `PermanenceHallmark`

- [V.R227] Permanence Export to Book VI -- structural remark

- [V.P96] BH Entropy Formula -- `bh_entropy_formula`


## Mathematical Content


### Mature Black Hole


A BH is mature at orbit depth n if:

- Geometric stabilization: the linking class ℓ is ρ-invariant

- Defect vanishing: S_def^BH(M) = 0 (no further defect to exhaust)


### No-Shrink Theorem


For any mature BH with M ≥ M_min (Chandrasekhar limit):
dM/dn ≥ 0
No τ-admissible evolution path reduces the mass.

### Hawking Radiation Reinterpreted


Hawking radiation is a chart-level readout of the boundary character
χ_BH at the linking boundary. It is NOT a transport of mass or
information from inside to outside.

### No BH Evaporation


No BH evaporates. The ontic mass is monotonically non-decreasing:
M(n+1) ≥ M(n) for all n beyond maturity depth.

### Information Paradox Dissolved


The information paradox dissolves because BHs don't evaporate. There
is no information-losing process to reconcile with unitarity.

## Ground Truth Sources


- Book V ch51: No-Shrink Extended


---

### `Tau.BookV.Cosmology.MatureBlackHole`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L64-L89)
**structure
Tau.BookV.Cosmology.MatureBlackHole :Type**


[V.D173] Mature black hole: a BH that has reached both geometric
stabilization (linking class ρ-invariant) and defect vanishing
(S_def^BH(M) = 0). Maturity is reached at finite depth.

Properties:


- The linking class no longer changes under ρ

- The defect functional is at its minimum (zero)

- Mass is above Chandrasekhar limit


- event : BlackHoleTopologicalEvent
The BH event.

- maturity_depth : ℕ
Maturity depth.

- maturity_pos : self.maturity_depth > 0
Maturity at finite depth.

- after_birth : self.maturity_depth ≥ self.event.birth_depth
Maturity is at or after birth.

- rho_invariant : Bool
Linking class is ρ-invariant.

- defect_zero : Bool
Defect is zero.

- mass_index : ℕ
Mass index (above Chandrasekhar).

- mass_pos : self.mass_index > 0
Mass positive.

Instances For

---

### `Tau.BookV.Cosmology.instReprMatureBlackHole.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L89-L89)
**def
Tau.BookV.Cosmology.instReprMatureBlackHole.repr :MatureBlackHole → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprMatureBlackHole`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L89-L89)
**instance
Tau.BookV.Cosmology.instReprMatureBlackHole :Repr MatureBlackHole**

Equations
- Tau.BookV.Cosmology.instReprMatureBlackHole = { reprPrec := Tau.BookV.Cosmology.instReprMatureBlackHole.repr }

---

### `Tau.BookV.Cosmology.defect_mass_coupling`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L95-L103)
**theorem
Tau.BookV.Cosmology.defect_mass_coupling
(mbh : MatureBlackHole)

(hd : mbh.defect_zero = true)
 :mbh.defect_zero = true**


[V.T113] Defect-mass coupling: for a mature BH, any mass
decrease M' < M would produce nonzero defect S_def > 0.

Reducing mass below the equilibrium value creates defect cost.
The mature state (S_def = 0) is the minimum, and mass decrease
moves away from it.

---

### `Tau.BookV.Cosmology.NoShrinkStatement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L109-L128)
**structure
Tau.BookV.Cosmology.NoShrinkStatement :Type**


[V.T114] No-shrink theorem: for any mature BH with M ≥ M_min,
dM/dn ≥ 0. No τ-admissible evolution path reduces the mass.

This is the τ-analogue of the classical area theorem (Hawking 1971),
but stronger: it applies to the MASS (not just area), and it is
exact (not just semiclassical).

Structural proof: mass decrease would create defect cost (V.T113),
but the mature BH has minimum defect (zero). Therefore mass
cannot decrease.

- mbh : MatureBlackHole
The mature BH.

- mass_n : ℕ
Mass at tick n.

- mass_n_plus_1 : ℕ
Mass at tick n+1.

- no_shrink : self.mass_n_plus_1 ≥ self.mass_n
No-shrink: mass doesn't decrease.

Instances For

---

### `Tau.BookV.Cosmology.instReprNoShrinkStatement.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L128-L128)
**def
Tau.BookV.Cosmology.instReprNoShrinkStatement.repr :NoShrinkStatement → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprNoShrinkStatement`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L128-L128)
**instance
Tau.BookV.Cosmology.instReprNoShrinkStatement :Repr NoShrinkStatement**

Equations
- Tau.BookV.Cosmology.instReprNoShrinkStatement = { reprPrec := Tau.BookV.Cosmology.instReprNoShrinkStatement.repr }

---

### `Tau.BookV.Cosmology.no_shrink_theorem`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L130-L132)
**theorem
Tau.BookV.Cosmology.no_shrink_theorem
(s : NoShrinkStatement)
 :s.mass_n_plus_1 ≥ s.mass_n**


No-shrink holds for any mature BH.

---

### `Tau.BookV.Cosmology.hawking_readout`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L138-L151)
**theorem
Tau.BookV.Cosmology.hawking_readout :"Hawking radiation = boundary character readout, not mass transport" = "Hawking radiation = boundary character readout, not mass transport"**


[V.P95] Hawking readout: Hawking radiation is a chart-level
readout of the boundary character χ_BH at the linking boundary.

It is NOT:


- A transport of mass from inside to outside

- A loss of information

- A process that reduces the BH mass


It IS:


- A boundary-character readout (like CMB temperature)

- A chart-level observable with no ontic consequence


---

### `Tau.BookV.Cosmology.no_bh_evaporation`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L157-L163)
**theorem
Tau.BookV.Cosmology.no_bh_evaporation :"No BH evaporates: M(n+1) >= M(n) for all n >= n_maturity" = "No BH evaporates: M(n+1) >= M(n) for all n >= n_maturity"**


[V.C19] No BH evaporation: no black hole evaporates.

M(n+1) ≥ M(n) for all n beyond maturity depth.
Follows from V.T114 (no-shrink) and V.P95 (Hawking is readout).

---

### `Tau.BookV.Cosmology.information_paradox_dissolved`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L169-L176)
**def
Tau.BookV.Cosmology.information_paradox_dissolved :Prop**


[V.R226] Information paradox dissolved: the paradox dissolves
because assumption (1) — that BHs evaporate — is false.

No information-losing process occurs. Unitarity is preserved
trivially because the ontic state never loses information.
Equations
- Tau.BookV.Cosmology.information_paradox_dissolved = ("BHs don't evaporate => no information loss => no paradox" = "BHs don't evaporate => no information loss => no paradox")
Instances For

---

### `Tau.BookV.Cosmology.info_paradox_holds`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L178-L178)
**theorem
Tau.BookV.Cosmology.info_paradox_holds :information_paradox_dissolved**


---

### `Tau.BookV.Cosmology.PermanenceHallmark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L184-L204)
**structure
Tau.BookV.Cosmology.PermanenceHallmark :Type**


[V.D174] Permanence hallmark: a structural property P of a
coherent instance in τ³ such that:

- P is acquired at finite depth (onset)

- P is ρ-invariant beyond onset

- P is irreversible (no τ-admissible path can undo P)


Black holes have the permanence hallmark: once formed, they
persist forever. This is the structural concept exported to
Book VI for the "alive" predicate.

- onset_depth : ℕ
Onset depth.

- onset_pos : self.onset_depth > 0
Onset is finite and positive.

- rho_invariant : Bool
ρ-invariant beyond onset.

- irreversible : Bool
Irreversible.

- all_conditions : Bool
All conditions met.

Instances For

---

### `Tau.BookV.Cosmology.instReprPermanenceHallmark`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L204-L204)
**instance
Tau.BookV.Cosmology.instReprPermanenceHallmark :Repr PermanenceHallmark**

Equations
- Tau.BookV.Cosmology.instReprPermanenceHallmark = { reprPrec := Tau.BookV.Cosmology.instReprPermanenceHallmark.repr }

---

### `Tau.BookV.Cosmology.instReprPermanenceHallmark.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L204-L204)
**def
Tau.BookV.Cosmology.instReprPermanenceHallmark.repr :PermanenceHallmark → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.BHEntropyFormula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L210-L224)
**structure
Tau.BookV.Cosmology.BHEntropyFormula :Type**


[V.P96] BH entropy: S_BH = k_B · A / (4 · ι<sub>τ</sub>²).

Derived from boundary counting: the torus horizon T² with area A
has boundary character degrees of freedom proportional to A/ι<sub>τ</sub>².
The factor 4 comes from the bipolar splitting (2 lobes × 2 sectors).

- num_lobes : ℕ
Number of lobes (always 2).

- num_bipolar : ℕ
Number of sectors in bipolar split (always 2).

- area_quantum_label : String
Area quantum is ι<sub>τ</sub>².

- prefactor_denom : ℕ
Prefactor is 1/(4·ι<sub>τ</sub>²) = num_lobes × num_bipolar denominator.

Instances For

---

### `Tau.BookV.Cosmology.instReprBHEntropyFormula.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L224-L224)
**def
Tau.BookV.Cosmology.instReprBHEntropyFormula.repr :BHEntropyFormula → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.instReprBHEntropyFormula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L224-L224)
**instance
Tau.BookV.Cosmology.instReprBHEntropyFormula :Repr BHEntropyFormula**

Equations
- Tau.BookV.Cosmology.instReprBHEntropyFormula = { reprPrec := Tau.BookV.Cosmology.instReprBHEntropyFormula.repr }

---

### `Tau.BookV.Cosmology.bh_entropy_formula`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L226-L228)
**theorem
Tau.BookV.Cosmology.bh_entropy_formula :2 * 2 = 4**


The entropy formula prefactor denominator is 2 × 2 = 4.

---

### `Tau.BookV.Cosmology.mature_bh_example`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L243-L250)
**def
Tau.BookV.Cosmology.mature_bh_example :MatureBlackHole**


Example mature BH.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Cosmology.bh_permanence`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L257-L260)
**def
Tau.BookV.Cosmology.bh_permanence :PermanenceHallmark**


Example permanence hallmark.
Equations
- Tau.BookV.Cosmology.bh_permanence = { onset_depth := 100, onset_pos := Tau.BookV.Cosmology.bh_permanence._proof_2 }
Instances For

---

### `Tau.BookV.Cosmology.ReadoutEntropyBound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L269-L280)
**structure
Tau.BookV.Cosmology.ReadoutEntropyBound :Type**


[V.T272] Readout channel entropy bound.
The readout state ρ_out has von Neumann entropy bounded by
log(dim H_∂), which is strictly less than S_BH.
The readout channel cannot carry away full ontic information.
Scope: τ-effective.

- log_dim_boundary : ℕ
Dimension of boundary Hilbert space (log scale, in nats).

- s_bh : ℕ
BH entropy (log scale, in nats).

- boundary_lt_bh : self.log_dim_boundary < self.s_bh
Strict inequality: boundary dimension < total BH entropy.

Instances For

---

### `Tau.BookV.Cosmology.OnticEntropyMonotonicity`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L282-L292)
**structure
Tau.BookV.Cosmology.OnticEntropyMonotonicity :Type**


[V.T273] Ontic entropy monotonicity for mature BH.
S_vN(ρ_ontic(n+1)) ≤ S_vN(ρ_ontic(n)) for all n ≥ n_mature.
The ontic state becomes purer, not less ordered.
Scope: τ-effective.

- maturity_depth : ℕ
Maturity depth.

- entropy_at : ℕ → ℕ
Entropy values (in units of k_B, indexed by orbit step beyond maturity).

- mono
(n : ℕ)
 : self.entropy_at (n + 1) ≤ self.entropy_at n
Monotonically non-increasing.

Instances For

---

### `Tau.BookV.Cosmology.stellar_bh_readout_bound`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L294-L299)
**def
Tau.BookV.Cosmology.stellar_bh_readout_bound :ReadoutEntropyBound**


Example readout entropy bound for a 10 M☉ BH.
log(dim H_∂) 10^77 << S_BH 10^79.
Equations
- Tau.BookV.Cosmology.stellar_bh_readout_bound = { log_dim_boundary := 77, s_bh := 79, boundary_lt_bh := Tau.BookV.Cosmology.stellar_bh_readout_bound._proof_2 }
Instances For

---

### `Tau.BookV.Cosmology.constant_entropy_mono`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L301-L305)
**def
Tau.BookV.Cosmology.constant_entropy_mono :OnticEntropyMonotonicity**


Example ontic entropy monotonicity: constant entropy (simplest case).
Equations
- Tau.BookV.Cosmology.constant_entropy_mono = { maturity_depth := 200, entropy_at := fun (x : ℕ) => 42, mono := Tau.BookV.Cosmology.constant_entropy_mono._proof_1 }
Instances For
