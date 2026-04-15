---
title: Categorical Societies
module_id: E3-008
layer: E3
strand: practical
summary_short: Social ontology as sheaf theory; power as morphism; legitimacy as recognition
  coherence.
diagrams:
- src: /assets/diagrams/framework/book-vii/metaphysics-societies-social-ontology.svg
  caption: "Social ontology as recognition-topology: a social group is constituted by a network of mutual recognition relations among agents. The category-theoretic structure is a directed graph whose cycles encode collective identity."
  alt: "Social ontology as recognition-topology: a social group is constituted by a network of mutual recognition relations among agents. The category-theoretic…"
  source: "Book VII, Chapter 0"
  label: "fig:bookVII-ch94-social-ontology"
thesis: Societies organize via recognition topology; dignity-bearing agents form the
  base space; spheres, Dunbar limits, and sovereignty as categorical structures.
canonical_books:
- VII
source_parts:
- VII.8
key_registry:
- VII.D76
- VII.D80
- VII.P25
depends_on:
- E3-007
unlocks: []
right_rail:
  related:
  - title: Categorical Ethics & the Kantian Bridge
    url: /framework/metaphysics-categorical-ethics/
  meta:
    type: Framework Module
    layer: E3 Metaphysics
    strand: Practical
    status: Canonical
    updated: April 2026
---

## Overview

Once [categorical ethics]({{ '/framework/metaphysics-categorical-ethics/' | relative_url }}) has established dignity-bearing agents as the base objects of the practical register, the question becomes: how do these agents organize? [Book VII]({{ '/publications/books/book-vii/' | relative_url }}) answers with a precise categorical apparatus -- social ontology as **sheaf theory**. The recognition relations between agents form a topology, and every social structure from intimate dyads to nation-states is a sheaf on that topology. This is not sociology dressed in mathematical language; it is a derivation of social architecture from the same [coherence kernel]({{ '/framework/mathematics-coherence-kernel/' | relative_url }}) that produced arithmetic, physics, and life.

## Spheres: Sloterdijk Meets Category Theory

Peter Sloterdijk's three-volume *Spheres* project described human social life through three spatial metaphors: bubbles (intimate spaces of co-presence), globes (totalizing cosmological enclosures), and foams (fragile, pluralistic, overlapping micro-environments). The framework gives these metaphors categorical teeth. A **bubble** is a connected component of the recognition sheaf with bounded diameter -- a small group within which every member has direct recognition relations with every other. A **globe** is a section over a larger open set that imposes coherence conditions on the bubbles it contains. A **foam** is the colimit of overlapping bubbles that share boundaries without merging into a single globe.

**Dunbar limits** emerge as connectivity bounds on the recognition topology. The empirical observation that human social groups cluster at characteristic sizes -- roughly 5, 15, 50, 150 -- is not an accident of primate neurology alone. These are the sizes at which the recognition sheaf can maintain global sections without collapsing under the combinatorial weight of mutual modeling. Beyond approximately 150, the topology fragments: global sections cease to exist, and social cohesion must be maintained by institutional structures rather than personal recognition.

## Cities, Power, and Sovereignty

Cities are the architectural response to this fragmentation. Urban design regulates the recognition topology through physical structure -- walls, streets, plazas, thresholds. Each architectural element modulates which recognition relations can form and at what density. The city is a built environment that shapes the sheaf.

**Power** is formalized as a morphism in the recognition category (VII.D76): an agent has power over another when the first agent's actions constrain the second agent's available morphisms. This is not a metaphor for power -- it is a definition that captures coercion, authority, influence, and persuasion as different types of constraint on the action category. **Sovereignty** is the special case of boundary control: the sovereign is the agent (or institution) that determines which recognition relations cross the boundary of a social unit. A state is sovereign when it controls who enters and exits its recognition topology. **Legitimacy** is recognition coherence -- a sovereign is legitimate when the boundary-control morphisms are compatible with the recognition sheaf of the governed population. When legitimacy fails, the sheaf has a gap: power operates but is not recognized, producing the characteristic instability of illegitimate rule.

## Capital and Religion

**Capital networks** (VII.D80) formalize economic structure as a second sheaf layered over the recognition topology. Capital flows along morphisms of exchange, and the accumulation of capital at a node corresponds to the concentration of exchange morphisms. The interplay between the recognition sheaf and the capital sheaf produces the familiar tensions between social solidarity and economic stratification.

**Religion** shapes the recognition topology through the **sacred-profane distinction**: certain objects, places, times, and actions are set apart from ordinary recognition relations and assigned a special status. This partitioning of the topology into sacred and profane regions is one of the oldest and most persistent social structures. The framework does not evaluate whether any particular sacred designation is correct -- that is a commitment-register question, outside the scope of diagrammatic derivation. What it does show is that the *structural role* of the sacred-profane distinction in organizing social life is a consequence of sheaf theory on the recognition topology (VII.P25).

## Key Claims

1. **VII.D76** -- Power as morphism; sovereignty as boundary control; legitimacy as recognition coherence *(established, machine-checked in [TauLib]({{ '/verify/taulib/' | relative_url }}))*
2. **VII.D80** -- Capital networks as exchange-sheaf over the recognition topology *(established, machine-checked)*
3. **VII.P25** -- Social organization derived from recognition-sheaf structure *(tau-effective)*
4. Dunbar limits as connectivity bounds on the recognition topology *(tau-effective)*
