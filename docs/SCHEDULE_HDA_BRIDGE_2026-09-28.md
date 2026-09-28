# Schedule / HDA Bridge — 28 Sep 2026

This update connects the new autonomous graph phase to the older V5 finite-refoliation programme.

## 1. Earlier V5 result

V5 already showed exact finite existence of schedule operators whose group commutator closes into a frame-dependent spatial gauge transformation.

That was a mathematical-existence result, but the update operators were deliberately constructed.

## 2. Native generalized-dihedral algebra

The new rank-three graph family naturally carries reflection-like involutions `R_s`:

```math
R_s^2=1,
```

and

```math
R_sR_t=T_{s-t}.
```

Therefore

```math
R_sR_tR_sR_t=T_{2(s-t)}
```

and

```math
[R_s,R_t]
=
T_{s-t}-T_{t-s}.
```

This is an exact finite

```text
normal-like × normal-like -> spatial
```

closure law native to the graph phase.

## 3. Smearing gives the antisymmetric lapse wedge

For

```math
H[N]=\sum_\alpha N_\alpha K_\alpha,
```

bilinearity gives

```math
[H[N],H[M]]
=
\sum_{\alpha<\beta}
(N_\alpha M_\beta-M_\alpha N_\beta)
[K_\alpha,K_\beta].
```

Sampling smooth lapses at the local offsets gives

```math
N_\alpha M_\beta-M_\alpha N_\beta
=
-(s_\alpha-s_\beta)^j
(N\partial_jM-M\partial_jN)
+O(a^2).
```

The spatial translation difference expands as

```math
T_{s_\alpha-s_\beta}
-
T_{s_\beta-s_\alpha}
=
2(s_\alpha-s_\beta)^i\partial_i
+O(a^3).
```

## 4. Same emergent metric tensor

For six equal-weight reflection channels,

```math
Q^{ij}
=
\frac12{\rm Cov}(s)^{ij}
=
\frac1{72}
\sum_{\alpha<\beta}
(s_\alpha-s_\beta)^i
(s_\alpha-s_\beta)^j.
```

The low-energy graph Laplacian satisfies

```math
L(k)=Q^{ij}k_i k_j+O(k^4).
```

The normal-normal commutator tends to

```math
[H[N],H[M]]
\longrightarrow
D\!\left[
Q^{ij}
(N\partial_jM-M\partial_jN)
\right].
```

So the propagation tensor and deformation-algebra tensor are the same covariance object.

## 5. Physical cubic coordinates

The benchmark's internal group basis gives a non-diagonal `Q`.

After transforming to the natural physical cubic basis,

```math
Q^{ij}=\frac16\delta^{ij}.
```

The benchmark confirms this using:

1. direct covariance;
2. pairwise commutator displacements;
3. the numerical Hessian of the soft Laplacian band.

## 6. Direct continuum test

The discrete commutator was tested on smooth periodic fields against the spatial Lie derivative on a half-density.

```text
L    coefficient       relative residual
16   0.982606102       0.025700385
24   0.992187757       0.011312962
32   0.995589552       0.006341877
48   0.998034703       0.002811719
64   0.998893517       0.001580233
```

## 7. Local schedule tunnelling from generic link flips

A four-vertex, six-link Hamiltonian

```math
H=
\frac12\sum_i(d_i-1)^2-\Gamma\sum_eX_e
```

has exactly three perfect matchings at `Gamma=0`.

Fourth-order virtual paths yield

```math
t=20\Gamma^4,
```

with schedule-manifold splitting

```math
\Delta=60\Gamma^4+O(\Gamma^6).
```

No explicit matching-exchange gate is inserted.

## 8. Fiber-odd gap

The all-reflection bipartite graph has Laplacian bands

```math
\ell_\pm(k)=1\mp\frac{|f(k)|}{6}.
```

The spatial/symmetric branch is soft at `k=0`; the odd branch is separated by a finite gap.

### Interpretation warning

This is **not yet the Hamiltonian constraint**.

A spectral gap for a physical fiber mode and a first-class gauge redundancy are different statements.

## 9. What this closes and what remains

This update closes a major conceptual bridge:

```text
autonomous graph phase
   -> native involutive schedule moves
   -> normal-normal commutator gives spatial motion
   -> same Q^ij governs propagation and closure
```

Still open:

```text
same microscopic parent
   -> exact first-class scalar/momentum constraints
   -> exactly two physical TT modes
   -> full thermodynamic gravitational phase
```

## Reproduce

```bash
python scripts/gwxp_schedule_hda_bridge.py
```
