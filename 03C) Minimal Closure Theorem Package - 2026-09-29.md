# GWXP — Minimal Closure Theorem Package

> **Freeze date:** 29 September 2026  
> This file isolates the smallest set of statements that would need to be proved, or convincingly replaced, for GWXP to move from a candidate programme to a closed emergent-gravity model.

---

## Theorem 1 — Autonomous three-dimensional phase

For an open region of microscopic couplings, the thermodynamic low-energy phase of the frozen parent exists and is a connected, statistically homogeneous and isotropic relational phase with finite-dimensional geometry satisfying appropriate three-dimensional scaling, including compatible spectral, volume-growth and gap diagnostics.

No external coordinates, dimension target, hard graph-distance cutoff, or geometric acceptance criterion may be used.

**Current status:** OPEN; finite numerical evidence exists at \(N=128,216,344\).

---

## Theorem 2 — Local kinetic isotropization

There exists a finite-range microscopic `H_mix` / schedule-frustration term, defined independently of the desired continuum tensor, whose low-energy measure produces

```math
K_{\rm eff}^{ijkl}
=
K_{\rm iso}^{ijkl}
+
o(1)
```

with a finite positive shear coefficient and

```math
c_4(N)\to0.
```

**Current status:** OPEN. Radius-four local move cones show feasibility; the selecting dynamics is not derived.

---

## Theorem 3 — First-class constraint phase

Within the same thermodynamic phase, there exist local low-energy scalar and spatial generators whose projected algebra closes without anomaly and whose normal-normal bracket uses the same emergent \(Q^{ij}\) that controls propagation.

Schematically,

```math
[H[N],H[M]]
\to
D[Q^{ij}(N\partial_jM-M\partial_jN)].
```

**Current status:** OPEN. Exact finite algebraic ancestors exist.

---

## Theorem 4 — Physical spectrum

The assembled low-energy phase contains exactly two healthy gapless tensor polarizations and no unwanted gapless scalar/vector geometric modes.

**Current status:** OPEN. Kinematic counting and quadratic compatibility tests exist.

---

## Theorem 5 — Shared matter/gravity cone

The matter and gravitational sectors share the same emergent clock and metric normalization in the interacting thermodynamic theory.

**Current status:** OPEN beyond finite coefficient-lock constructions.

---

## Theorem 6 — Nonlinear continuum universality

The long-wavelength limit exists and its two-derivative gravitational sector lies in the Einstein/TEGR universality class, with controlled corrections.

**Current status:** OPEN.

---

## Optional downstream theorem — black-hole response

Only after Theorems 1–6 are established should the black-hole branch be promoted.

A strong completion would show that the same parent generates the appropriate horizon stability Jacobian, equilibrium area/boost response and dynamical tidal response of the emergent gravitational theory.

**Current status:** speculative / structural only.

---

# Closure criterion

GWXP should be called *closed* only when the chain

```math
\mathrm{one autonomous finite parent}
\rightarrow
\mathrm{3D relational phase}
\rightarrow
\mathrm{local isotropic spin-2 kinetics}
\rightarrow
\mathrm{first-class constraints}
\rightarrow
\mathrm{two healthy tensor modes}
\rightarrow
\mathrm{shared matter/gravity metric}
\rightarrow
\mathrm{nonlinear Einstein/TEGR IR}
```

is realized without manually encoding the target continuum gravitational constraints.
