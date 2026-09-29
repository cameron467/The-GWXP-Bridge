# GWXP — Frozen Candidate Parent for Pre-Handoff Review

**Date:** 29 September 2026  
**Status:** pre-handoff candidate, not a completed theory  
**Rule:** this file freezes the candidate architecture so external reviewers can attack one definite object. It does not promote OPEN components to DERIVED ones.

## 1. Graph sector

For adjacency `A`, define

```text
Atilde = D^(-1/2) A D^(-1/2)
Ltilde = I - Atilde
K_g     = exp(g Atilde)
```

and the graph energy

```text
H_graph = H_degree
        + tau T[A]
        - J Tr exp(g Atilde)
        + U sum_(ij in E) [K_g]_{ij}^2
        - kappa log det(epsilon I + Ltilde).
```
The degree term may be written

```text
H_degree = mu m + lambda sum_i C(d_i,2),
```

with the degree-6 sector centred by `mu=-(2k-1)lambda=-11lambda` for `k=6`.

Current finite phase-search point:

```text
d = 6
J = 1
g = 2.0
U = 0.100
kappa = 0.30
epsilon = 0.025
tau = 5
```

**Status:** candidate microscopic graph functional. The valence selection and several reaction-coordinate identities are derived conditional on this choice; the full functional itself remains a microscopic assumption.

## 2. Metric rewrite / soft-local kinetic sector

The old uniform all-edge driver and the old multiplicative common-graph mediator are deprecated.

For a graph `G`, define

```text
h_G = I - rho_m A_G,          0 < rho_m < 1/6,
H_chi(G) = Delta [h_G tensor h_G].
```

Then

```text
H_chi(G)^(-1) = (1/Delta) [R_G tensor R_G],
R_G = (I-rho_m A_G)^(-1).
```

For a legal degree-preserving switch

```text
(ab,cd) -> (ac,bd),
```

finite Schur/Feshbach elimination gives the Hermitian graph-configuration hopping

```text
t_GG' = - eta [
    R_G(a,c) R_G(b,d)
  + R_G'(a,b) R_G'(c,d)
],

eta = gamma^2/(2 Delta).
```

The two terms exchange under `G <-> G'`, so `t_GG'=t_G'G` exactly.

Separately, the strong valence Hamiltonian gives the leading degree-preserving 2-switch amplitude

```text
|t_switch| = 20 Gamma^4/lambda^3
```

before weaker graph-sector corrections.

**Status:** exact finite constructive mediator realization exists. The existence of the mediator sector is still a microscopic model choice; it has not been uniquely derived from the valence term alone.

## 3. Incidence / schedule sector

For oriented incidence `B` in the degree-6 sector,

```text
B B^T = 6 I - A = 6 Ltilde,
Bhat = B/sqrt(6).
```

The same incidence operator gives the finite matter propagation carrier and the normal/schedule carrier. A smeared normal operator is

```text
K[N] = [[0, M_N Bhat],
        [Bhat^T M_N, 0]].
```

Its vertex normal-normal commutator is exactly

```text
[K[N],K[M]]_vertex
 = M_N Ltilde M_M - M_M Ltilde M_N.
```

**Status:** EXACT finite algebraic construction. Promotion to a genuine extended many-body first-class constraint phase remains OPEN.

## 4. Physical metric moves and kinetic tensor

For a three-component local diffusion/frame map `X`, a genuine 2-switch obeys

```text
6 X^T (Delta Ltilde_m) X = delta h_m.
```

Thus the physical kinetic covariance is built from the same Laplacian fluctuations,

```text
K_eff proportional to
  sum_m w_m vec(delta h_m) vec(delta h_m)^T.
```

The corrected physical audit uses mediator-derived channel weights.

**Critical correction:** the bare mediator-weighted `K_eff` is not isotropic on the current autonomous states. Measured whitened spin-4 residuals are approximately

```text
N=128 : 0.249
N=216 : 0.387
N=344 : 0.499.
```

Therefore amorphous disorder alone is not currently an adequate rank-4 mechanism.

## 5. H_mix / rotational closure sector

`H_mix` is retained as the sector that penalizes non-scalar rotational charge in local metric-move statistics.

The old claim that radius-3 local reweighting robustly solved the problem is **CORRECTED**: when fake solutions that collapse the shear kinetic strength are excluded, `R=3` is not robust on the corrected phase.

At fixed graph radius `R=4`, sampled local move-cone witnesses at `N=344` do contain exactly isotropic nonzero shear tensors. On six corrected-autonomous neighborhoods, random subsets of the full local move cone retained roughly

```text
0.54, 0.92, 2.77, 1.45, 1.40, 1.64
```

times the physical bare-mediator shear scale at their maximum isotropic point. Three mature-basin neighborhoods gave about

```text
0.21, 0.85, 1.39.
```

Maximum-entropy tests on representative corrected-autonomous `R=4` subsets reached exact isotropy at finite KL cost while retaining 25-100% of the bare local shear scale, depending on neighborhood.

**Status:** fixed-radius local isotropic move cone is NUMERICALLY VIABLE at `R=4`; the microscopic schedule-frustration Hamiltonian that naturally generates the required reweighting remains OPEN. This is now a principal handoff target.

## 6. Matter / cell sector

The exact finite vertex branch obeys

```text
E_m^2 = lambda(Ltilde).
```

The extensive edge-cycle zero kernel is repaired by local curl faces,

```text
H_curl = sum_c mu_c Q_c^dagger Q_c,
mu_c > 0.
```

A universal hard face-length cutoff is deprecated. Use a soft local hierarchy, for example

```text
mu_ell proportional to rho_f^(ell-4).
```

On the corrected autonomous states the shortest cycle lengths required to span the full cycle space were

```text
N=128 : ell_span=7
N=216 : ell_span=7
N=344 : ell_span=8.
```

Using every local cycle through that spanning length, exact all-face curl gaps were

```text
rho_f   N=128       N=216       N=344
0.10    0.006735    0.003982    0.002791
0.20    0.034515    0.029971    0.039429
0.30    0.084391    0.095977    0.182344
```

Longer positive-weight faces can only increase these finite gaps.

**Status:** finite-size Hodge repair PASSED through `N=344` for a non-extreme soft hierarchy; a nonzero thermodynamic curl gap remains OPEN.

## 7. Current one-parent schematic

```text
H_total = H_graph[A]
        + H_med[A,chi]
        + H_sched[B(A)]
        + H_mix[local Delta L statistics / schedule frustration]
        + H_matter[B(A), local cells].
```

No external coordinates, hard graph radius, explicit target dimension, explicit `C4` target, or hand-inserted DeWitt tensor is part of the frozen candidate.

However `H_mix` is not yet microscopically closed, and the graph/schedule/frame sectors have not been proved to form one extended first-class phase.

## 8. Claims that are NOT licensed by this freeze

This checkpoint does **not** establish:

- a thermodynamic 3D phase theorem;
- a complete quantum theory of gravity;
- nonlinear first-class closure of the full many-body parent;
- absence of all extra scalar/vector modes in the assembled thermodynamic theory;
- Standard Model emergence;
- a microscopic derivation of every parent coupling;
- the literal information-ledger interpretation of spacetime.

Those remain external-review / next-stage problems.
