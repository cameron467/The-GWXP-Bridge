# Reproducibility — 28 Sep 2026 Update

This guide covers the **new deterministic benchmarks**. The older repository may contain additional dependencies and scripts.

## Install

```bash
python -m pip install -r requirements_natural_emergence.txt
```

## Run

```bash
python run_new_benchmarks.py
```

or individually:

```bash
python scripts/gwxp_natural_emergence_benchmark.py
python scripts/gwxp_schedule_hda_bridge.py
```

## Expected Natural Emergence outputs

Approximately:

```text
Infinite cubic Z^3              -8.155619787
Generalized-dihedral rank-3    -8.173368935
Rank-3 d_spec                   2.98
Representative rank-4          -7.99084
```

The cubic finite-size sequence should converge rapidly toward the infinite cubic value.

The quotient sweep should show positive finite relation-length excess that approaches zero as the compactification relation becomes long.

## Expected Schedule/HDA outputs

Local four-vertex sector:

```text
Gamma=0 ground configurations = 3
t/Gamma^4 = 20
splitting/Gamma^4 -> 60
```

Generalized-dihedral bridge:

```text
reflection group commutator = T_{2(s-t)}
Q_covariance = Q_commutator
Q_physical = I/6
fiber-odd Laplacian branch remains finite
```

Real-space convergence:

```text
L=16  residual ~ 0.0257
L=24  residual ~ 0.0113
L=32  residual ~ 0.00634
L=48  residual ~ 0.00281
L=64  residual ~ 0.00158
```

The fitted normalization should tend toward one.

## Determinism

The supplied headline scripts are deterministic.

The exploratory phase search used many adversarial graph optimizations, but the GitHub benchmarks evaluate canonical representatives and exact/deterministic families so readers do not need to reproduce an optimizer trajectory to reproduce the headline values.

## Independent verification

For serious use:

1. rewrite the evaluators independently;
2. vary quadrature/grid sizes;
3. reproduce IDOS fits using an independent spectral routine;
4. test additional infinite graph families;
5. independently derive the generalized-dihedral covariance/HDA identity;
6. rerun the real-space convergence test with different smooth lapse/test fields.

## Scope warning

These scripts do not reproduce the entire historical project.

The root evidence ledger records the earlier rigidity, finite-code, SU(2), moving-code, black-hole and MOTS branches.
