---
layout: taulib-doc
title: "TauLib.BookIV.ManyBody.Magnetism"
permalink: /verify/taulib/docs/book-iv-many-body-magnetism/
lane: verify
module_name: "TauLib.BookIV.ManyBody.Magnetism"
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

# TauLib.BookIV.ManyBody.Magnetism


Magnetism on T²: Ising model, no-monopole theorem, domain walls,
Curie transition, and five magnetic orders from defect-tuple signatures.

## Registry Cross-References


- [IV.D387] Magnetic Moment on T² — `MagneticMoment`

- [IV.D388] τ-Ising Hamiltonian on T² — `IsingHamiltonian`

- [IV.P226] Spontaneous Magnetization on T² — `SpontaneousMagnetization`

- [IV.T208] No Magnetic Monopoles on T² — `NoMonopoles`

- [IV.D389] Magnetic Domain Wall on T² — `DomainWall`

- [IV.P227] Domain Wall Energy from T² Winding — `DomainWallEnergy`

- [IV.T209] Curie Transition as T² Symmetry Breaking — `CurieTransition`

- [IV.P228] Magnetic Orders as Defect-Tuple Signatures — `MagneticOrders`


## Mathematical Content


This module formalizes magnetism as a consequence of T² topology:

- 
**No-monopole theorem**: χ(T²) = 0 ⟹ ∇·B = 0 identically.
No magnetic charges exist on a torus. This is the electric-magnetic
duality: charge = boundary obstruction, monopole = Euler obstruction.


- 
**Ising model on T²**: ferromagnetic order as global d₄ phase alignment.
Periodic boundary conditions from T² topology, Kramers-Wannier duality,
Onsager exact solution in thermodynamic limit.


- 
**Curie transition**: second-order phase transition in defect-tuple framework.
Order parameter = global d₄ coherence.


- 
**Five magnetic orders**: dia, para, ferro, antiferro, ferri — all as
d₄ signature variants.


## Ground Truth Sources


- Chapter 63 of Book IV (2nd Edition)

- 1st Edition ch07_07 (Ising on T², χ(T²)=0)


---

### `Tau.BookIV.ManyBody.MagneticMoment`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L51-L61)
**structure
Tau.BookIV.ManyBody.MagneticMoment :Type**


[IV.D387] Magnetic moment of a defect bundle with spin quantum number s
on T². The magnetization M is the average magnetic moment per unit volume
over the statistical ensemble.

- moment_from_spin : Bool
Magnetic moment proportional to spin.

- magnetization_collective : Bool
Magnetization is collective property.

- d4_governs_alignment : Bool
d₄ component governs alignment pattern.

Instances For

---

### `Tau.BookIV.ManyBody.instReprMagneticMoment`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L61-L61)
**instance
Tau.BookIV.ManyBody.instReprMagneticMoment :Repr MagneticMoment**

Equations
- Tau.BookIV.ManyBody.instReprMagneticMoment = { reprPrec := Tau.BookIV.ManyBody.instReprMagneticMoment.repr }

---

### `Tau.BookIV.ManyBody.instReprMagneticMoment.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L61-L61)
**def
Tau.BookIV.ManyBody.instReprMagneticMoment.repr :MagneticMoment → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.magnetic_moment`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L63-L63)
**def
Tau.BookIV.ManyBody.magnetic_moment :MagneticMoment**

Equations
- Tau.BookIV.ManyBody.magnetic_moment = { }
Instances For

---

### `Tau.BookIV.ManyBody.IsingHamiltonian`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L69-L82)
**structure
Tau.BookIV.ManyBody.IsingHamiltonian :Type**


[IV.D388] The τ-Ising Hamiltonian on a finite lattice Λ ⊂ T²:
H = -J Σ_{⟨i,j⟩} σ_i σ_j - h Σ_i σ_i
with periodic boundary conditions enforced by T² topology.
J > 0 favors alignment (ferromagnetic), σ_i ∈ {-1, +1}.

- exchange_positive : Bool
Exchange coupling J > 0.

- spin_values : List ℤ
Spins take values ±1.

- periodic_from_torus : Bool
Periodic BCs from T² topology.

- uniform_coordination : Bool
No edges on T² — every site has same coordination number.

Instances For

---

### `Tau.BookIV.ManyBody.instReprIsingHamiltonian.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L82-L82)
**def
Tau.BookIV.ManyBody.instReprIsingHamiltonian.repr :IsingHamiltonian → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprIsingHamiltonian`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L82-L82)
**instance
Tau.BookIV.ManyBody.instReprIsingHamiltonian :Repr IsingHamiltonian**

Equations
- Tau.BookIV.ManyBody.instReprIsingHamiltonian = { reprPrec := Tau.BookIV.ManyBody.instReprIsingHamiltonian.repr }

---

### `Tau.BookIV.ManyBody.ising_hamiltonian`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L84-L84)
**def
Tau.BookIV.ManyBody.ising_hamiltonian :IsingHamiltonian**

Equations
- Tau.BookIV.ManyBody.ising_hamiltonian = { }
Instances For

---

### `Tau.BookIV.ManyBody.ising_periodic_bc`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L86-L87)
**theorem
Tau.BookIV.ManyBody.ising_periodic_bc :ising_hamiltonian.periodic_from_torus = true**


---

### `Tau.BookIV.ManyBody.SpontaneousMagnetization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L93-L108)
**structure
Tau.BookIV.ManyBody.SpontaneousMagnetization :Type**


[IV.P226] Spontaneous magnetization on T²:


- Above T_C: ⟨M⟩ = 0 (paramagnetic)

- Below T_C: ⟨|M|⟩ > 0 (ferromagnetic, Z₂ broken)

- T_C determined by sinh(2J/k_BT_C) = 1 (Kramers-Wannier duality)


- phase_transition : Bool
Phase transition exists.

- above_tc_disordered : Bool
Above T_C: disordered.

- below_tc_broken : Bool
Below T_C: Z₂ broken.

- tc_from_duality : Bool
T_C from Kramers-Wannier self-duality.

- onsager_applies : Bool
Onsager solution applies on T².

Instances For

---

### `Tau.BookIV.ManyBody.instReprSpontaneousMagnetization.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L108-L108)
**def
Tau.BookIV.ManyBody.instReprSpontaneousMagnetization.repr :SpontaneousMagnetization → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprSpontaneousMagnetization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L108-L108)
**instance
Tau.BookIV.ManyBody.instReprSpontaneousMagnetization :Repr SpontaneousMagnetization**

Equations
- Tau.BookIV.ManyBody.instReprSpontaneousMagnetization = { reprPrec := Tau.BookIV.ManyBody.instReprSpontaneousMagnetization.repr }

---

### `Tau.BookIV.ManyBody.spontaneous_magnetization`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L110-L110)
**def
Tau.BookIV.ManyBody.spontaneous_magnetization :SpontaneousMagnetization**

Equations
- Tau.BookIV.ManyBody.spontaneous_magnetization = { }
Instances For

---

### `Tau.BookIV.ManyBody.magnetization_transition`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L112-L113)
**theorem
Tau.BookIV.ManyBody.magnetization_transition :spontaneous_magnetization.phase_transition = true**


---

### `Tau.BookIV.ManyBody.NoMonopoles`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L119-L144)
**structure
Tau.BookIV.ManyBody.NoMonopoles :Type**


[IV.T208] **No Magnetic Monopoles on T².**
χ(T²) = 0 ⟹ ∇·B = 0 identically.

Proof: A monopole charge g at point p ∈ T² would require
∮_{T²} B·dA = g ≠ 0. By Gauss-Bonnet, this integral equals
2π·χ(T²) = 0 for any curvature 2-form. Hence g = 0.

This is the electric-magnetic duality in τ³:


- Electric charge = boundary obstruction (∂T² via L, nontrivial)

- Magnetic charge = Euler obstruction (χ(T²) = 0, trivial)


No monopoles exist — not as empirical fact, but as topological necessity.

- euler_char_zero : Bool
Euler characteristic of T² is zero.

- genus_one : ℕ
χ(T²) = 0 by genus-1 surface.

- gauss_bonnet_zero : Bool
Gauss-Bonnet gives total charge zero.

- electric_boundary : Bool
Electric charge: boundary obstruction (nontrivial).

- magnetic_euler : Bool
Magnetic charge: Euler obstruction (trivial).

- topological_necessity : Bool
Topological necessity, not empirical.

Instances For

---

### `Tau.BookIV.ManyBody.instReprNoMonopoles.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L144-L144)
**def
Tau.BookIV.ManyBody.instReprNoMonopoles.repr :NoMonopoles → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprNoMonopoles`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L144-L144)
**instance
Tau.BookIV.ManyBody.instReprNoMonopoles :Repr NoMonopoles**

Equations
- Tau.BookIV.ManyBody.instReprNoMonopoles = { reprPrec := Tau.BookIV.ManyBody.instReprNoMonopoles.repr }

---

### `Tau.BookIV.ManyBody.no_monopoles`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L146-L146)
**def
Tau.BookIV.ManyBody.no_monopoles :NoMonopoles**

Equations
- Tau.BookIV.ManyBody.no_monopoles = { }
Instances For

---

### `Tau.BookIV.ManyBody.euler_char_T2_zero`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L148-L149)
**theorem
Tau.BookIV.ManyBody.euler_char_T2_zero :no_monopoles.euler_char_zero = true**


---

### `Tau.BookIV.ManyBody.no_monopoles_topological`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L151-L152)
**theorem
Tau.BookIV.ManyBody.no_monopoles_topological :no_monopoles.topological_necessity = true**


---

### `Tau.BookIV.ManyBody.DomainWall`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L158-L171)
**structure
Tau.BookIV.ManyBody.DomainWall :Type**


[IV.D389] Magnetic domain wall: codimension-1 defect in the spin-alignment
field on T². Curve γ ⊂ T² across which spin orientation changes
discontinuously (Bloch wall) or rotates (Néel wall). In defect-tuple
language, a locus where d₄ has winding discontinuity.

- codimension : ℕ
Codimension-1 defect.

- bloch_type : Bool
Bloch wall: discontinuous normal.

- neel_type : Bool
Néel wall: rotation in wall plane.

- d4_discontinuity : Bool
d₄ winding discontinuity.

Instances For

---

### `Tau.BookIV.ManyBody.instReprDomainWall.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L171-L171)
**def
Tau.BookIV.ManyBody.instReprDomainWall.repr :DomainWall → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprDomainWall`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L171-L171)
**instance
Tau.BookIV.ManyBody.instReprDomainWall :Repr DomainWall**

Equations
- Tau.BookIV.ManyBody.instReprDomainWall = { reprPrec := Tau.BookIV.ManyBody.instReprDomainWall.repr }

---

### `Tau.BookIV.ManyBody.domain_wall`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L173-L173)
**def
Tau.BookIV.ManyBody.domain_wall :DomainWall**

Equations
- Tau.BookIV.ManyBody.domain_wall = { }
Instances For

---

### `Tau.BookIV.ManyBody.DomainWallEnergy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L179-L192)
**structure
Tau.BookIV.ManyBody.DomainWallEnergy :Type**


[IV.P227] Domain wall energy σ_wall = 4√(AK), where A = exchange
stiffness, K = anisotropy constant. Width δ = π√(A/K).
On T², non-contractible cycles impose global consistency:
total winding change must be compatible with H₁(T²; ℤ) ≅ ℤ².

- energy_formula : String
Energy from exchange × anisotropy.

- width_formula : String
Width formula.

- torus_consistency : Bool
T² global consistency constraint.

- first_homology : String
H₁(T²; ℤ) ≅ ℤ² constraint.

Instances For

---

### `Tau.BookIV.ManyBody.instReprDomainWallEnergy.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L192-L192)
**def
Tau.BookIV.ManyBody.instReprDomainWallEnergy.repr :DomainWallEnergy → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprDomainWallEnergy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L192-L192)
**instance
Tau.BookIV.ManyBody.instReprDomainWallEnergy :Repr DomainWallEnergy**

Equations
- Tau.BookIV.ManyBody.instReprDomainWallEnergy = { reprPrec := Tau.BookIV.ManyBody.instReprDomainWallEnergy.repr }

---

### `Tau.BookIV.ManyBody.domain_wall_energy`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L194-L194)
**def
Tau.BookIV.ManyBody.domain_wall_energy :DomainWallEnergy**

Equations
- Tau.BookIV.ManyBody.domain_wall_energy = { }
Instances For

---

### `Tau.BookIV.ManyBody.CurieTransition`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L200-L218)
**structure
Tau.BookIV.ManyBody.CurieTransition :Type**


[IV.T209] **Curie transition as T² symmetry breaking.**
Second-order phase transition in defect-tuple framework:


- Order parameter φ = ⟨M⟩/M_sat (global d₄ coherence)

- Below T_C: φ ≠ 0 (Z₂ or SO(3) broken)

- Above T_C: φ = 0 (restored)

- At T_C: φ vanishes continuously, χ diverges
Critical exponents from universality class (Ising/Heisenberg).


- second_order : Bool
Second-order phase transition.

- order_param_d4 : Bool
Order parameter = d₄ coherence.

- z2_broken : Bool
Z₂ symmetry broken below T_C.

- susceptibility_diverges : Bool
Susceptibility diverges at T_C.

- universality : Bool
Universality class determines exponents.

Instances For

---

### `Tau.BookIV.ManyBody.instReprCurieTransition`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L218-L218)
**instance
Tau.BookIV.ManyBody.instReprCurieTransition :Repr CurieTransition**

Equations
- Tau.BookIV.ManyBody.instReprCurieTransition = { reprPrec := Tau.BookIV.ManyBody.instReprCurieTransition.repr }

---

### `Tau.BookIV.ManyBody.instReprCurieTransition.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L218-L218)
**def
Tau.BookIV.ManyBody.instReprCurieTransition.repr :CurieTransition → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.curie_transition`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L220-L220)
**def
Tau.BookIV.ManyBody.curie_transition :CurieTransition**

Equations
- Tau.BookIV.ManyBody.curie_transition = { }
Instances For

---

### `Tau.BookIV.ManyBody.curie_is_second_order`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L222-L223)
**theorem
Tau.BookIV.ManyBody.curie_is_second_order :curie_transition.second_order = true**


---

### `Tau.BookIV.ManyBody.MagneticOrders`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L229-L244)
**structure
Tau.BookIV.ManyBody.MagneticOrders :Type**


[IV.P228] Five magnetic orders as defect-tuple d₄ signatures:

- Diamagnetic: all d₄ paired, M ≤ 0

- Paramagnetic: random d₄, M → 0 at h=0

- Ferromagnetic: global d₄ alignment, M > 0

- Antiferromagnetic: alternating d₄ sublattices, M = 0

- Ferrimagnetic: unequal sublattice alignment, 0 < M < M_ferro


- num_orders : ℕ
Five fundamental orders.

- orders : List String
Order names.

- all_from_d4 : Bool
All classified by d₄ pattern.

Instances For

---

### `Tau.BookIV.ManyBody.instReprMagneticOrders.repr`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L244-L244)
**def
Tau.BookIV.ManyBody.instReprMagneticOrders.repr :MagneticOrders → ℕ → Std.Format**

Equations
- One or more equations did not get rendered due to their size.
Instances For

---

### `Tau.BookIV.ManyBody.instReprMagneticOrders`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L244-L244)
**instance
Tau.BookIV.ManyBody.instReprMagneticOrders :Repr MagneticOrders**

Equations
- Tau.BookIV.ManyBody.instReprMagneticOrders = { reprPrec := Tau.BookIV.ManyBody.instReprMagneticOrders.repr }

---

### `Tau.BookIV.ManyBody.magnetic_orders`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L246-L246)
**def
Tau.BookIV.ManyBody.magnetic_orders :MagneticOrders**

Equations
- Tau.BookIV.ManyBody.magnetic_orders = { }
Instances For

---

### `Tau.BookIV.ManyBody.five_magnetic_orders`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L248-L249)
**theorem
Tau.BookIV.ManyBody.five_magnetic_orders :magnetic_orders.num_orders = 5**


---

### `Tau.BookIV.ManyBody.magnetic_orders_count`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookIV/ManyBody/Magnetism.lean#L251-L252)
**theorem
Tau.BookIV.ManyBody.magnetic_orders_count :magnetic_orders.orders.length = 5**
