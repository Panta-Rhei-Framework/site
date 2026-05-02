---
layout: program-doc
title: "TauLib Glossary"
permalink: /verify/taulib/glossary/
lane: verify
v2_lane: verify
type: "TauLib Reference"
status: "Canonical"
summary_short: "Key terms, symbols, constants, and structures used throughout TauLib."
right_rail:
  related:
  - title: TauLib Overview
    url: /verify/taulib/
  - title: Architecture
    url: /verify/taulib/architecture/
  meta:
    type: "Documentation"
    status: "Frozen"
    updated: "April 2026"
---

## Constants

| Symbol | Value | Lean Name | Description |
|--------|-------|-----------|-------------|
| iota_tau | 2/(pi + e) = 0.341304 | `iota_tau_float` | Master constant; governs all quantitative predictions |
| kappa_D | 1 - iota_tau = 0.658696 | — | Complementary constant (D-sector coupling) |
| kappa_omega | iota_tau/(1 + iota_tau) = 0.254485 | — | Omega coupling constant |
| W_3(4) | 5 | — | Continued-fraction window sum (3 partial quotients from index 4); governs NLO corrections |
| W_3(3) | 17 | — | Continued-fraction window sum (3 partial quotients from index 3) |
| W_4(3) | 18 | — | Continued-fraction window sum (4 partial quotients from index 3) |
| W_5(3) | 19 | — | Continued-fraction window sum (5 partial quotients from index 3); equals N_e/3 |

## Generators

| Generator | Symbol | Index | Role |
|-----------|--------|------:|------|
| `alpha` | alpha | 0 | Radial seed — its orbit becomes TauIdx (natural numbers) |
| `pi` | pi | 1 | Prime base / multiplicative spine |
| `gamma` | gamma | 2 | Exponent channel |
| `eta` | eta | 3 | Tetration channel |
| `omega` | omega | 4 | Fixed-point absorber / closure beacon |

## Core Structures

| Lean Type | Module | Description |
|-----------|--------|-------------|
| `Generator` | `BookI/Kernel/Signature` | The 5-element generator type |
| `TauObj` | `BookI/Kernel/Axioms` | Objects in Category τ (seed + depth) |
| `TauIdx` | `BookI/Denotation/TauIdx` | Internal natural numbers (= `Nat`, earned from O_alpha) |
| `SplitComplex` | `BookI/Boundary/SplitComplex` | Split-complex numbers (boundary ring) |

## Key Spaces

| Symbol | Description | Lean Module |
|--------|-------------|-------------|
| tau^3 | The tau-fibration: tau^1 x_f T^2 | `BookII/Interior/Tau3Fibration` |
| tau^1 | Base circle (macrocosm) | `BookV/Temporal/BaseCircle` |
| T^2 | Fiber torus (microcosm) | `BookIV/Arena/Tau3Arena` |
| L | Lemniscate boundary: S^1 v S^1 | `BookI/Polarity/Lemniscate` |

## Axioms (K0-K6)

| Axiom | Name | One-Line Description |
|-------|------|---------------------|
| K0 | Universe Postulate | tau exists as a universe of discourse |
| K1 | Strict Order | The 5 generators are strictly totally ordered: alpha < pi < gamma < eta < omega |
| K2 | Omega Fixed Point | rho(omega) = omega — omega is the unique fixed point |
| K3 | Orbit-Seeded | rho(g) is seeded by g for all non-omega generators |
| K4 | No-Jump (Cover) | rho advances depth by exactly 1 |
| K5 | Beacon Non-Successor | omega is never reached by iterating rho |
| K6 | Object Closure | Every TauObj is a generator or rho-generated |

## Registry ID Format

| Prefix | Meaning | Example |
|--------|---------|---------|
| `I.` - `VII.` | Book number | `IV.T140` = Book IV |
| `K` | Axiom | `I.K1` = Axiom K1 |
| `D` | Definition | `V.D317` |
| `T` | Theorem | `IV.T66` |
| `P` | Proposition | `V.P176` |
| `R` | Remark | `IV.R260` |
