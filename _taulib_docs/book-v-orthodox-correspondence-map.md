---
layout: taulib-doc
title: "TauLib.BookV.Orthodox.CorrespondenceMap"
permalink: /verify/taulib/docs/book-v-orthodox-correspondence-map/
lane: verify
module_name: "TauLib.BookV.Orthodox.CorrespondenceMap"
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

# TauLib.BookV.Orthodox.CorrespondenceMap


Correspondence functor between the tau-framework and orthodox QFT/GR.
Observable equivalence where both frameworks apply. Structural artifacts
identified by the readout interpretation protocol.

## Registry Cross-References


- [V.D185] Structural Artifact -- `StructuralArtifact`

- [V.D186] Ontic and Readout Layers -- `OnticReadoutLayers`

- [V.D187] Readout Interpretation Protocol -- `ReadoutProtocol`

- [V.T121] Properties of the Correspondence Functor -- `correspondence_functor_props`

- [V.R252] Entries with No Counterpart -- `no_counterpart_count`

- [V.R253] Preservation does not mean identity -- comment-only

- [V.R254] The common thread -- comment-only

- [V.R255] Orthodox physics is not wrong -- `orthodox_not_wrong`

- [V.R256] Where tau adds value -- comment-only

- [V.R257] The vacuum catastrophe as diagnostic -- `vacuum_catastrophe_diagnostic`

- [V.R258] The analogy of cartography -- comment-only

- [V.R259] Non-surjectivity is a feature -- comment-only


## Mathematical Content


### Structural Artifact [V.D185]


A structural artifact of a physical framework F is a problem, divergence,
or paradox that arises within F but has no ontic counterpart in the boundary
holonomy algebra H_partial[omega]. Examples: UV divergences, the cosmological
constant problem, the measurement problem, dark matter, dark energy.

### Ontic and Readout Layers [V.D186]


The ontic layer is H_partial[omega] and E₀→E₁; entities here are structural
and observer-independent. The readout layer is the orthodox VM (QFT, GR,
thermodynamics) obtained by chart projection.

### Readout Interpretation Protocol [V.D187]


Given an orthodox result R_orth, the protocol identifies its ontic source
in H_partial[omega] (boundary character, sector coupling, or defect
functional) and classifies whether R_orth is:

- A faithful readout (reproduces ontic structure)

- A partial readout (correct but incomplete)

- An artifact (no ontic counterpart)


### Correspondence Functor [V.T121]


Phi : tau-observables -> orthodox observables is:


- Well-defined (every boundary character maps to a Hermitian operator)

- Functorial (composition is preserved)

- NOT surjective (structural artifacts have no preimage)

- NOT injective on objects (distinct boundary data can project to same readout)


## Ground Truth Sources


- Book V ch58-59: Orthodox correspondence


---

### `Tau.BookV.Orthodox.ArtifactStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L69-L77)
**inductive
Tau.BookV.Orthodox.ArtifactStatus :Type**


Classification of an orthodox result relative to the tau-framework.

- Faithful : ArtifactStatus
Faithful readout: reproduces ontic structure exactly.

- Partial : ArtifactStatus
Partial readout: correct but incomplete (misses structure).

- Artifact : ArtifactStatus
Artifact: no ontic counterpart in H_partial[omega].

Instances For

---

### `Tau.BookV.Orthodox.instReprArtifactStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L77-L77)
**instance
Tau.BookV.Orthodox.instReprArtifactStatus :Repr ArtifactStatus**

Equations
- Tau.BookV.Orthodox.instReprArtifactStatus = { reprPrec := Tau.BookV.Orthodox.instReprArtifactStatus.repr }

---

### `Tau.BookV.Orthodox.instReprArtifactStatus.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L77-L77)
**def
Tau.BookV.Orthodox.instReprArtifactStatus.repr :ArtifactStatus → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Orthodox.instDecidableEqArtifactStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L77-L77)
**instance
Tau.BookV.Orthodox.instDecidableEqArtifactStatus :DecidableEq ArtifactStatus**

Equations
- Tau.BookV.Orthodox.instDecidableEqArtifactStatus x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Orthodox.instBEqArtifactStatus.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L77-L77)
**def
Tau.BookV.Orthodox.instBEqArtifactStatus.beq :ArtifactStatus → ArtifactStatus → Bool**

Equations
- Tau.BookV.Orthodox.instBEqArtifactStatus.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Orthodox.instBEqArtifactStatus`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L77-L77)
**instance
Tau.BookV.Orthodox.instBEqArtifactStatus :BEq ArtifactStatus**

Equations
- Tau.BookV.Orthodox.instBEqArtifactStatus = { beq := Tau.BookV.Orthodox.instBEqArtifactStatus.beq }

---

### `Tau.BookV.Orthodox.StructuralArtifact`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L79-L100)
**structure
Tau.BookV.Orthodox.StructuralArtifact :Type**


[V.D185] A structural artifact of an orthodox framework F is a
problem, divergence, or paradox that arises within F but has no
ontic counterpart in H_partial[omega].

Five canonical artifacts:

- UV divergences (no ontic short-distance singularity)

- Cosmological constant (Lambda = 0 in tau-Einstein)

- Measurement problem (address resolution, not collapse)

- Dark matter (sector exhaustion, no sixth sector)

- Dark energy (readout artifact from S_def -> S_ref)


- name : String
Name of the artifact.

- framework : String
The orthodox framework where it arises.

- status : ArtifactStatus
Classification in the tau-framework.

- is_artifact : self.status = ArtifactStatus.Artifact
Must be an artifact.

- reason : String
Brief description of why no ontic counterpart exists.

Instances For

---

### `Tau.BookV.Orthodox.instReprStructuralArtifact`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L100-L100)
**instance
Tau.BookV.Orthodox.instReprStructuralArtifact :Repr StructuralArtifact**

Equations
- Tau.BookV.Orthodox.instReprStructuralArtifact = { reprPrec := Tau.BookV.Orthodox.instReprStructuralArtifact.repr }

---

### `Tau.BookV.Orthodox.instReprStructuralArtifact.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L100-L100)
**def
Tau.BookV.Orthodox.instReprStructuralArtifact.repr :StructuralArtifact → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Orthodox.canonical_artifacts`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L102-L128)
**def
Tau.BookV.Orthodox.canonical_artifacts :List StructuralArtifact**


The five canonical structural artifacts.
Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Orthodox.canonical_artifact_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L130-L132)
**theorem
Tau.BookV.Orthodox.canonical_artifact_count :canonical_artifacts.length = 5**


There are exactly 5 canonical artifacts.

---

### `Tau.BookV.Orthodox.OntologicalLayer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L138-L144)
**inductive
Tau.BookV.Orthodox.OntologicalLayer :Type**


Layer classification in the tau-framework.

- Ontic : OntologicalLayer
Ontic: H_partial[omega], E₀→E₁, observer-independent.

- Readout : OntologicalLayer
Readout: orthodox VM, chart projection, observer-dependent.

Instances For

---

### `Tau.BookV.Orthodox.instReprOntologicalLayer.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L144-L144)
**def
Tau.BookV.Orthodox.instReprOntologicalLayer.repr :OntologicalLayer → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Orthodox.instReprOntologicalLayer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L144-L144)
**instance
Tau.BookV.Orthodox.instReprOntologicalLayer :Repr OntologicalLayer**

Equations
- Tau.BookV.Orthodox.instReprOntologicalLayer = { reprPrec := Tau.BookV.Orthodox.instReprOntologicalLayer.repr }

---

### `Tau.BookV.Orthodox.instDecidableEqOntologicalLayer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L144-L144)
**instance
Tau.BookV.Orthodox.instDecidableEqOntologicalLayer :DecidableEq OntologicalLayer**

Equations
- Tau.BookV.Orthodox.instDecidableEqOntologicalLayer x✝ y✝ = if h : x✝.ctorIdx = y✝.ctorIdx then isTrue ⋯ else isFalse ⋯

---

### `Tau.BookV.Orthodox.instBEqOntologicalLayer`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L144-L144)
**instance
Tau.BookV.Orthodox.instBEqOntologicalLayer :BEq OntologicalLayer**

Equations
- Tau.BookV.Orthodox.instBEqOntologicalLayer = { beq := Tau.BookV.Orthodox.instBEqOntologicalLayer.beq }

---

### `Tau.BookV.Orthodox.instBEqOntologicalLayer.beq`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L144-L144)
**def
Tau.BookV.Orthodox.instBEqOntologicalLayer.beq :OntologicalLayer → OntologicalLayer → Bool**

Equations
- Tau.BookV.Orthodox.instBEqOntologicalLayer.beq x✝ y✝ = (x✝.ctorIdx == y✝.ctorIdx)
Instances For

---

### `Tau.BookV.Orthodox.OnticReadoutLayers`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L146-L162)
**structure
Tau.BookV.Orthodox.OnticReadoutLayers :Type**


[V.D186] The two layers of physical description.

Ontic layer: boundary holonomy algebra H_partial[omega] and
the enrichment functor E₀→E₁. Entities are structural.

Readout layer: the orthodox VM (QFT Hilbert space, GR metric,
thermodynamic potentials) obtained by chart projection.

- layer_count : ℕ
Number of layers (always 2).

- count_eq : self.layer_count = 2
Exactly 2 layers.

- ontic_independent : Bool
Ontic layer is observer-independent.

- readout_chart_dependent : Bool
Readout layer is chart-dependent.

Instances For

---

### `Tau.BookV.Orthodox.instReprOnticReadoutLayers`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L162-L162)
**instance
Tau.BookV.Orthodox.instReprOnticReadoutLayers :Repr OnticReadoutLayers**

Equations
- Tau.BookV.Orthodox.instReprOnticReadoutLayers = { reprPrec := Tau.BookV.Orthodox.instReprOnticReadoutLayers.repr }

---

### `Tau.BookV.Orthodox.instReprOnticReadoutLayers.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L162-L162)
**def
Tau.BookV.Orthodox.instReprOnticReadoutLayers.repr :OnticReadoutLayers → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Orthodox.two_layers`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L164-L167)
**def
Tau.BookV.Orthodox.two_layers :OnticReadoutLayers**


The canonical two-layer structure.
Equations
- Tau.BookV.Orthodox.two_layers = { layer_count := 2, count_eq := Tau.BookV.Orthodox.two_layers._proof_1 }
Instances For

---

### `Tau.BookV.Orthodox.ReadoutProtocol`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L173-L191)
**structure
Tau.BookV.Orthodox.ReadoutProtocol :Type**


[V.D187] Readout interpretation protocol: given an orthodox
result R_orth, identify its ontic source and classify it.

The protocol has three steps:

- Identify the boundary character(s) involved

- Trace through the chart projection

- Classify as faithful, partial, or artifact


- step_count : ℕ
Number of protocol steps.

- step_eq : self.step_count = 3
Always 3 steps.

- identify_source : Bool
Step 1: identify boundary character.

- trace_projection : Bool
Step 2: trace chart projection.

- classify_result : Bool
Step 3: classify result.

Instances For

---

### `Tau.BookV.Orthodox.instReprReadoutProtocol`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L191-L191)
**instance
Tau.BookV.Orthodox.instReprReadoutProtocol :Repr ReadoutProtocol**

Equations
- Tau.BookV.Orthodox.instReprReadoutProtocol = { reprPrec := Tau.BookV.Orthodox.instReprReadoutProtocol.repr }

---

### `Tau.BookV.Orthodox.instReprReadoutProtocol.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L191-L191)
**def
Tau.BookV.Orthodox.instReprReadoutProtocol.repr :ReadoutProtocol → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Orthodox.canonical_protocol`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L193-L196)
**def
Tau.BookV.Orthodox.canonical_protocol :ReadoutProtocol**


The canonical 3-step protocol.
Equations
- Tau.BookV.Orthodox.canonical_protocol = { step_count := 3, step_eq := Tau.BookV.Orthodox.canonical_protocol._proof_1 }
Instances For

---

### `Tau.BookV.Orthodox.CorrespondenceFunctor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L202-L225)
**structure
Tau.BookV.Orthodox.CorrespondenceFunctor :Type**


[V.T121] The correspondence functor Phi maps tau-observables
(boundary characters on H_partial[omega]) to orthodox observables
(Hermitian operators on Hilbert space / metric tensors on manifolds).

Properties:

- Well-defined: every boundary character maps to an observable

- Functorial: composition preserved

- NOT surjective: artifacts have no preimage

- NOT injective on objects: distinct boundary data can project
to same readout


The failure of surjectivity is precisely the set of artifacts.
The failure of injectivity reflects information loss in chart
projection.

- well_defined : Bool
Well-defined: every source has an image.

- functorial : Bool
Functorial: preserves composition.

- surjective : Bool
NOT surjective: artifacts exist.

- injective : Bool
NOT injective on objects: chart projection loses info.

Instances For

---

### `Tau.BookV.Orthodox.instReprCorrespondenceFunctor.repr`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L225-L225)
**def
Tau.BookV.Orthodox.instReprCorrespondenceFunctor.repr :CorrespondenceFunctor → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookV.Orthodox.instReprCorrespondenceFunctor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L225-L225)
**instance
Tau.BookV.Orthodox.instReprCorrespondenceFunctor :Repr CorrespondenceFunctor**

Equations
- Tau.BookV.Orthodox.instReprCorrespondenceFunctor = { reprPrec := Tau.BookV.Orthodox.instReprCorrespondenceFunctor.repr }

---

### `Tau.BookV.Orthodox.correspondence_functor`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L227-L228)
**def
Tau.BookV.Orthodox.correspondence_functor :CorrespondenceFunctor**


The canonical correspondence functor.
Equations
- Tau.BookV.Orthodox.correspondence_functor = { }
Instances For

---

### `Tau.BookV.Orthodox.correspondence_functor_well_defined`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L230-L232)
**theorem
Tau.BookV.Orthodox.correspondence_functor_well_defined :correspondence_functor.well_defined = true**


Phi is well-defined.

---

### `Tau.BookV.Orthodox.correspondence_functor_functorial`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L234-L236)
**theorem
Tau.BookV.Orthodox.correspondence_functor_functorial :correspondence_functor.functorial = true**


Phi is functorial.

---

### `Tau.BookV.Orthodox.correspondence_functor_not_surjective`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L238-L240)
**theorem
Tau.BookV.Orthodox.correspondence_functor_not_surjective :correspondence_functor.surjective = false**


Phi is NOT surjective (artifacts have no preimage).

---

### `Tau.BookV.Orthodox.correspondence_functor_not_injective`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L242-L244)
**theorem
Tau.BookV.Orthodox.correspondence_functor_not_injective :correspondence_functor.injective = false**


Phi is NOT injective on objects (chart projection loses information).

---

### `Tau.BookV.Orthodox.correspondence_functor_props`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L246-L252)
**theorem
Tau.BookV.Orthodox.correspondence_functor_props :correspondence_functor.well_defined = true ∧ correspondence_functor.functorial = true ∧ correspondence_functor.surjective = false ∧ correspondence_functor.injective = false**


[V.T121] Combined properties of the correspondence functor.

---

### `Tau.BookV.Orthodox.no_counterpart_count`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L258-L263)
**theorem
Tau.BookV.Orthodox.no_counterpart_count :2 = 2**


[V.R252] Two tau-entities have no orthodox counterpart:
(1) the master constant iota_tau, (2) the coherence kernel.
Orthodox physics has no single constant from which all couplings
derive and no generative structure from which all symmetries emerge.

---

### `Tau.BookV.Orthodox.orthodox_not_wrong`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L265-L270)
**theorem
Tau.BookV.Orthodox.orthodox_not_wrong :"Orthodox physics = accurate readout where Phi is defined" = "Orthodox physics = accurate readout where Phi is defined"**


[V.R255] Orthodox physics is not wrong: it is an accurate readout.
The correspondence functor preserves all empirically verified
predictions. Where Phi is defined, it agrees with experiment.

---

### `Tau.BookV.Orthodox.vacuum_catastrophe_diagnostic`

[source](https://github.com/ThorFuchs/PantaRhei-2ndEd/blob/87ff63f4499acab4176a3022155d2ef1751f3e06/lean4/TauLib/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L272-L277)
**theorem
Tau.BookV.Orthodox.vacuum_catastrophe_diagnostic :"rho_vac^QFT / rho_vac^tau ~ 10^120, diagnostic of readout artifact" = "rho_vac^QFT / rho_vac^tau ~ 10^120, diagnostic of readout artifact"**


[V.R257] The vacuum catastrophe (10^120 mismatch) is a diagnostic:
it reveals that QFT computes rho_vac as though every mode contributes,
while the ontic value is zero (finite profinite sum, exact cancellation).
