# GWXP — Final Pre-Handoff Pass

**Date:** 29 September 2026  
**Purpose:** record the last bounded calculations performed before handing the remaining integration problem to specialist review.

## Executive status

The finite/numerical programme has reached the intended pre-handoff stopping line. The candidate is **not proved**, but several questions that could still be settled honestly in this environment have now been resolved or sharply isolated.

## 1. Combined quantum configuration-space Hamiltonian

Exact finite sectors were constructed by choosing commuting legal 2-switches, enumerating the resulting `2^m` graph configurations, putting the exact parent graph energy on the diagonal, and the derived pair-mediator hopping on configuration-space edges.

Across generic and mature-basin sectors at `N=64/128`, weak-to-moderate kinetic strength did not drive the ground state out of the low-parent-energy, relation-rich sector. Strong kinetic scales eventually delocalised it, as expected.

**Status:** PASSED as a finite quantum consistency test. Not a thermodynamic ground-state theorem.

## 2. Broadened structured adversaries and autonomous three-size ledger

At `(g,U,kappa)=(2,0.100,0.30)`, broadened Abelian/Cayley rank-1/2/3 scans found best tested structured energies approximately

```text
N=128 : -1.301602474
N=216 : -1.301972547
N=344 : -1.302071375
```

Corrected autonomous graph states reached

```text
N=128 : -1.301651700
N=216 : -1.302092376
N=344 : -1.302342902
```

and therefore beat those scanned structured floors at all three sizes.

Geometry diagnostics:

```text
N      C4/N     gap       d_s(05)   diameter
128    5.5313   0.15596   3.0365   6
216    4.9769   0.13505   3.2139   6
344    4.5436   0.13355   3.3669   7
```

The states are not equally relaxed, so no thermodynamic exponent is claimed.

**Status:** three-size autonomous phase evidence PASSED; thermodynamic stabilization remains OPEN.

## 3. Physical rank-4 kinetic audit

Using the exact metric-move identity, a whitened rank-2 frame, and corrected mediator channel weights, the bare physical `K_eff` has spin-4 residuals

```text
N=128 : 0.249
N=216 : 0.387
N=344 : 0.499
```

with large TT-direction splitting.

**Status:** bare self-isotropisation FAILED. The old claim that amorphous disorder alone removes rank-4 grain is DEMOTED.

## 4. Corrected H_mix locality audit

Global mediator-prior reweighting can exactly isotropise `K_eff` while preserving total shear strength, with finite KL costs:

```math
\begin{aligned}
N &= 216 : D_KL ~ 0.297 \\
N &= 344 : D_KL ~ 0.144.
\end{aligned}
```

The earlier radius-3 local success was found to contain a loophole: exact anisotropy constraints can be satisfied by collapsing local shear strength. After preventing that, radius 3 is not robust.

A physically better test allows the local scalar kinetic coefficient to renormalise but requires a finite nonzero isotropic shear tensor. At radius 4, random subsets of the full local move cone provide repeated constructive witnesses with order-one fractions of the bare shear scale.

Representative maximum-entropy subset tests reached exact isotropy with finite KL cost while retaining 25-100% of bare local shear strength.

**Status:** fixed-radius `R=4` local isotropic move cone is VIABLE; natural microscopic generation of the necessary reweighting is OPEN and is now a leading handoff problem.

## 5. Matter-cell / Hodge curl gap

Cycle-space dimensions and shortest spanning local loop lengths:

```text
N=128 : dim=257, ell_span=7
N=216 : dim=433, ell_span=7
N=344 : dim=689, ell_span=8
```

Thus a universal hard `ell<=7` rule is definitively rejected.

For the soft all-face hierarchy `mu_ell ~ rho_f^(ell-4)`, exact finite curl gaps using every cycle through the spanning length are

```text
rho_f   N=128       N=216       N=344
0.10    0.006735    0.003982    0.002791
0.20    0.034515    0.029971    0.039429
0.30    0.084391    0.095977    0.182344
```

Adding longer positive-weight faces can only raise these finite values.

**Status:** finite-size Hodge repair PASSED through N=344; thermodynamic gap remains OPEN.

## 6. Where to stop

Further brute-force work in this environment is unlikely to settle the remaining central theorem. The remaining targets require specialist many-body / mathematical-physics treatment:

1. prove or refute a stable thermodynamic approximately-3D phase;
2. derive a specific local `H_mix` / schedule-frustration Hamiltonian whose low-energy measure produces the required rank-4 isotropy without fitted weights;
3. establish genuine extended first-class scalar/spatial constraints in the same parent;
4. prove absence/gapping of extra scalar/vector modes in the assembled phase;
5. establish nonlinear continuum closure/universality and the GR/TEGR IR limit.

The handoff should therefore present GWXP as a sharply specified candidate plus exact finite constructions, corrected numerical evidence, failed routes, and explicit kill criteria — not as a solved theory.
