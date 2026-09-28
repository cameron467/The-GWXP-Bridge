# Natural Emergence — 28 Sep 2026 Benchmark

This document contains only the new autonomous-geometry branch. For the complete GWXP history, see [`FULL_RESULTS_SUMMARY.md`](FULL_RESULTS_SUMMARY.md) and the repository root `MASTER_EVIDENCE_LEDGER.md`.

## Frozen effective graph functional

```math
H=
H_{\rm degree}
+\tau T
-J\,{\rm Tr}\,e^{g\widetilde A}
+U\sum_{\langle ij\rangle}
[e^{g\widetilde A}]_{ij}^{\,2}
-\kappa\log\det(\epsilon I+\widetilde L),
```

with

```math
\widetilde A=D^{-1/2}AD^{-1/2},
\qquad
\widetilde L=I-\widetilde A.
```

The model contains no background coordinates or target spatial dimension.

### Resource/valence sector

At the centre of a valence-`k` phase,

```math
H_{\rm degree}
=
\frac{\lambda}{2}
\sum_i(d_i-k)^2+\mathrm{const}.
```

Valence is therefore selected energetically rather than imposed as a hard graph constraint.

## Deterministic three-dimensional benchmark

At

```math
g=6,\qquad U/J=0.018,
```

the supplied evaluator gives

```text
Infinite cubic Z^3              -8.155619787129
Generalized-dihedral rank-3    -8.173368935008
Rank-3 d_spec                   ~2.981
Representative rank-4          -7.990835619649
```

The lower-energy non-Abelian phase is still spectrally three-dimensional.

This supports the interpretation that **dimension is the macroscopic property**, not one exact microscopic lattice.

## Cubic convergence

```text
L=4   -7.790663183943
L=5   -8.080318990472
L=6   -8.137762589083
L=7   -8.152143946492
L=8   -8.155063476958
L=9   -8.155542936584
L=10  -8.155609770459
```

Small periodic cubic boxes are therefore poor thermodynamic representatives.

## Lower-dimensional quotients

The deterministic rank-two quotient sweep shows that finite relation-length compactifications remain above the rank-three phase.

The excess falls rapidly as the relation length grows, approaching degeneracy only through decompactification.

Interpretation:

```text
fixed-scale 2D quotient -> loses
compactification scale -> infinity -> locally approaches 3D covering graph
```

## Adversary classes tested during development

The exploratory programme tested:

- random regular expanders;
- bipartite expanders;
- strips / slabs / tubes;
- modular complete-bipartite graphs;
- circulant/Cayley families;
- tree products;
- Abelian and generalized-dihedral lower-rank quotients;
- higher-rank candidates;
- symmetric incidence-design graphs;
- irregular annealed graphs;
- local edge add/delete/rewire defects.

This list is intentionally adversarial but not mathematically exhaustive.

## What failed along the way

- site-clock condensation produced order, not space;
- determinant pressure eventually rewarded excessive global mixing;
- loop rewards produced modular/loop-congested cheats;
- one-body spectral invariants could not distinguish cospectral micrographs;
- `U/J=0.009` looked encouraging at small size but failed the thermodynamic slab test for the 3D branch;
- insufficient degree stiffness allowed valence collapse;
- cubic `Z^3` was beaten by a lower-energy non-Abelian 3D realization.

Those failures are why the current claim is “3D spectral phase”, not “cubic lattice vacuum”.

## Current status

**Supported:** autonomous finite-dimensional geometry with strong evidence for a degree-six 3D phase.

**Not proved:** global minimization over every infinite graph or complete gravitational dynamics.

## Reproduce

```bash
python scripts/gwxp_natural_emergence_benchmark.py
```
