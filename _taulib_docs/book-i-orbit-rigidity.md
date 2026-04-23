---
layout: taulib-doc
title: "TauLib.BookI.Orbit.Rigidity"
permalink: /verify/taulib/docs/book-i-orbit-rigidity/
lane: verify
module_name: "TauLib.BookI.Orbit.Rigidity"
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

# TauLib.Orbit.Rigidity


Rigidity (Aut(τ) = {id}) and Categoricity of τ₀.

## Registry Cross-References


- [I.T07] Rigidity of τ — `rigidity_non_omega`

- [I.T08] Categoricity of τ₀ — `categoricity_non_omega`


---

### `Tau.Orbit.rho_seed_omega`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Rigidity.lean#L18-L20)
**theorem
Tau.Orbit.rho_seed_omega
(x : Kernel.TauObj)

(h : x.seed = Kernel.Generator.omega)
 :Kernel.rho x = x**


If x.seed = omega, then rho x = x (generalized K2).

---

### `Tau.Orbit.TauAutomorphism`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Rigidity.lean#L22-L28)
**structure
Tau.Orbit.TauAutomorphism :Type**


A τ-automorphism: a bijection TauObj → TauObj that commutes with ρ.

- toFun : Kernel.TauObj → Kernel.TauObj
- invFun : Kernel.TauObj → Kernel.TauObj
- left_inv
(x : Kernel.TauObj)
 : self.invFun (self.toFun x) = x
- right_inv
(x : Kernel.TauObj)
 : self.toFun (self.invFun x) = x
- rho_comm
(x : Kernel.TauObj)
 : self.toFun (Kernel.rho x) = Kernel.rho (self.toFun x)
Instances For

---

### `Tau.Orbit.auto_omega_to_omega`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Rigidity.lean#L30-L39)
**theorem
Tau.Orbit.auto_omega_to_omega
(φ : TauAutomorphism)

(d : Nat)
 :(φ.toFun { seed := Kernel.Generator.omega, depth := d }).seed = Kernel.Generator.omega**


Any τ-automorphism maps omega-fiber objects to omega-fiber objects.

---

### `Tau.Orbit.auto_non_omega`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Rigidity.lean#L41-L50)
**theorem
Tau.Orbit.auto_non_omega
(φ : TauAutomorphism)

(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)
 :(φ.toFun { seed := g, depth := 0 }).seed ≠ Kernel.Generator.omega**


φ maps non-omega generators to non-omega objects.

---

### `Tau.Orbit.auto_shift`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Rigidity.lean#L52-L61)
**theorem
Tau.Orbit.auto_shift
(φ : TauAutomorphism)

(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)

(n : Nat)
 :φ.toFun { seed := g, depth := n } = { seed := (φ.toFun { seed := g, depth := 0 }).seed, depth := (φ.toFun { seed := g, depth := 0 }).depth + n }**


For non-omega g, φ maps the orbit O_g with constant depth offset.

---

### `Tau.Orbit.rigidity_depth`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Rigidity.lean#L63-L129)
**theorem
Tau.Orbit.rigidity_depth
(φ : TauAutomorphism)

(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)
 :(φ.toFun { seed := g, depth := 0 }).depth = 0**


φ maps depth-0 non-omega objects to depth 0.

---

### `Tau.Orbit.rigidity_non_omega`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Rigidity.lean#L131-L138)
**theorem
Tau.Orbit.rigidity_non_omega
(φ : TauAutomorphism)

(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)

(h_seed : (φ.toFun { seed := g, depth := 0 }).seed = g)

(n : Nat)
 :φ.toFun { seed := g, depth := n } = { seed := g, depth := n }**


[I.T07] **Rigidity**: φ = id on non-omega objects (given seed preservation).

---

### `Tau.Orbit.TauModel`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Rigidity.lean#L140-L146)
**structure
Tau.Orbit.TauModel :Type 1**


A model of the τ₀ axioms.

- Carrier : Type
- gen : Kernel.Generator → self.Carrier
- rho_model : self.Carrier → self.Carrier
- gen_distinct_ax
(g h : Kernel.Generator)
 : g ≠ h → self.gen g ≠ self.gen h
- omega_fixed_ax : self.rho_model (self.gen Kernel.Generator.omega) = self.gen Kernel.Generator.omega
Instances For

---

### `Tau.Orbit.interpret`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Rigidity.lean#L148-L150)
**def
Tau.Orbit.interpret
(M : TauModel)

(x : Kernel.TauObj)
 :M.Carrier**


The canonical map: ⟨g, n⟩ ↦ ρ_M^n(g_M).
Equations
- Tau.Orbit.interpret M x = Nat.rec (M.gen x.seed) (fun (x : Nat) (ih : M.Carrier) => M.rho_model ih) x.depth
Instances For

---

### `Tau.Orbit.categoricity_non_omega`

[source](https://github.com/Panta-Rhei-Research/taulib/blob/2261c049119c8dd9a4e891457f196745178c02b3/TauLib/BookI/Orbit/Rigidity.lean#L152-L164)
**theorem
Tau.Orbit.categoricity_non_omega
(M : TauModel)

(f : Kernel.TauObj → M.Carrier)

(f_gen : ∀ (g : Kernel.Generator), f (Kernel.TauObj.ofGen g) = M.gen g)

(f_rho : ∀ (x : Kernel.TauObj), f (Kernel.rho x) = M.rho_model (f x))

(g : Kernel.Generator)

(hg : g ≠ Kernel.Generator.omega)

(n : Nat)
 :f { seed := g, depth := n } = interpret M { seed := g, depth := n }**


[I.T08] **Categoricity** (non-omega): unique homomorphism into any model.
