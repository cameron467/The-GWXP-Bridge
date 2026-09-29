# GWXP — Mathematical Core

> **Freeze date:** 29 September 2026  
> **Purpose:** present GWXP with the narrative stripped away: definitions, exact identities, finite constructions, numerical claims, failed routes, and open propositions.  
> **Status:** pre-handoff formal core. This is not a proof of emergent general relativity.

---

## Evidence labels used here

- **EXACT IDENTITY** — follows algebraically from the stated definitions.
- **DERIVED** — analytic result obtained under stated assumptions.
- **FINITE CONSTRUCTION** — an explicit finite system realizing the claimed algebraic structure.
- **NUMERICAL** — finite-size computational evidence.
- **CONDITIONAL** — follows if specified structural assumptions hold.
- **FAILED / CORRECTED** — a previous claim or route weakened or rejected by a later audit.
- **CONJECTURE** — proposed mechanism not yet obtained from the frozen parent.
- **OPEN** — unresolved statement required for full closure.

---

# 1. Graph variables

Let

```math
G=(V,E), \qquad |V|=N,
```

with adjacency matrix \(A\), degree matrix \(D\),

```math
\widetilde A=D^{-1/2}AD^{-1/2},
```

and normalized Laplacian

```math
\widetilde L=I-\widetilde A.
```

The presently tested geometric phase is centered on degree

```math
d=6.
```

The frozen schematic parent is

```math
H_{\rm total}
=
H_{\rm graph}[A]
+
H_{\rm med}[A,\chi]
+
H_{\rm sched}[B(A)]
+
H_{\rm mix}
+
H_{\rm matter}.
```

The sectors have different evidentiary status. In particular, the existence of a mediator sector and a local schedule/frustration sector remains a microscopic model choice.

---

# 2. Degree selection

Take

```math
H_{\rm degree}
=
\mu m
+
\lambda\sum_i {d_i\choose 2}.
```

At

```math
\mu=-(2k-1)\lambda,
```

this becomes

```math
H_{\rm degree}
=
\frac{\lambda}{2}\sum_i(d_i-k)^2+\mathrm{constant}.
```

Hence the degree-\(k\) sector is selected at the center of an open chemical-potential interval.

**Status: DERIVED.**

For the current candidate,

```math
k=6.
```

---

# 3. Frozen graph functional

The tested graph-sector energy is

```math
H_{\rm graph}
=
H_{\rm degree}
+
\tau T[A]
-
J\,{\rm Tr}\,e^{g\widetilde A}
+
U\sum_{\langle ij\rangle}
[e^{g\widetilde A}]_{ij}^{2}
-
\kappa\log\det(\epsilon I+\widetilde L).
```

The finite phase-search benchmark uses

```math
d=6,\quad
J=1,\quad
g=2,\quad
U=0.100,\quad
\kappa=0.30,\quad
\epsilon=0.025,\quad
\tau=5.
```

Interpretively:

- \(H_{\rm degree}\) selects valence;
- \(T[A]\) frustrates triangles;
- \(-{\rm Tr}\,e^{g\widetilde A}\) rewards relational walk structure;
- the \(U\)-term penalizes concentrated communicability;
- the determinant term controls long-wavelength spectral connectivity.

**Status of the functional itself: ASSUMED MICROSCOPIC CHOICE.**

---

# 4. Four-cycle reaction coordinate

For a triangle-free \(d\)-regular graph,

```math
\frac{1}{N}{\rm Tr}\,A^4
=
d(2d-1)+8\,\frac{C_4}{N}.
```

Expanding the graph functional around this coordinate gives the leading four-cycle coefficient

```math
e(C_4/N)
=
e_0
+
\left[
\frac{g^4}{3}(4U-1)
+
\frac{2\kappa}{(1+\epsilon)^4}
\right]
\frac{C_4/N}{d^4}
+\cdots.
```

At the frozen benchmark the leading coefficient is negative.

**Status: DERIVED leading-order mechanism.**

This explains why short relations can condense without putting \(C_4\) explicitly into the Hamiltonian. It does not prove that the full nonlinear minimum is three-dimensional.

---

# 5. Degree-preserving graph rewrites

A legal 2-switch is

```math
(ab,cd)\longrightarrow(ac,bd),
```

with degree preserved.

In the strong-valence expansion, summing all \(4!\) virtual single-link-flip orderings gives

```math
|t_{\rm switch}|
=
\frac{20\Gamma^4}{\lambda^3}
```

at leading order.

**Status: DERIVED / EXACT at the stated perturbative order.**

Weaker graph terms and higher perturbative orders generate corrections.

---

# 6. Gapped pair mediator

Define

```math
h_G=I-\rho_m A_G,
\qquad 0<\rho_m<\frac16,
```

and

```math
H_\chi(G)
=
\Delta\,
(h_G\otimes h_G).
```

For degree six,

```math
\lambda_{\min}(h_G)\ge 1-6\rho_m,
```

so

```math
\Delta_\chi
\ge
\Delta(1-6\rho_m)^2>0.
```

Further,

```math
H_\chi^{-1}
=
\frac1\Delta
(R_G\otimes R_G),
\qquad
R_G=(I-\rho_m A_G)^{-1}.
```

A finite Schur/Feshbach elimination gives the Hermitian configuration-space hopping

```math
t_{GG'}
=
-\eta
\left[
R_G(a,c)R_G(b,d)
+
R_{G'}(a,b)R_{G'}(c,d)
\right],
```

with

```math
\eta=\frac{\gamma^2}{2\Delta}.
```

Under \(G\leftrightarrow G'\), the two terms exchange, hence

```math
t_{GG'}=t_{G'G}.
```

**Status: FINITE CONSTRUCTION / EXACT Hermitian kernel for the stated mediator.**

The old common-graph multiplicative mediator is **FAILED as a scalable nucleation driver**.  
The earlier square-root additive kernel is **DEMOTED**; it is not the kernel produced by this finite pair-mediator construction.

---

# 7. Combined configuration-space Hamiltonian

The physically relevant finite graph Hamiltonian is of the form

```math
H_{\rm conf}
=
\sum_G E_G |G\rangle\langle G|
+
\sum_{G\sim G'}
t_{GG'}
\left(
|G\rangle\langle G'|
+
|G'\rangle\langle G|
\right).
```

Finite exact subspaces built from commuting legal graph rewrites were diagonalized.

In the tested sectors, weak-to-moderate mediator hopping does not move the ground-state weight away from the relation-rich, low-parent-energy side.

**Status: NUMERICAL finite-sector evidence.**

This is not a thermodynamic ground-state theorem.

---

# 8. Incidence algebra

Let \(B\) be an oriented incidence matrix. In the degree-six sector,

```math
BB^T
=
6I-A
=
6\widetilde L.
```

Define

```math
\widehat B=\frac{B}{\sqrt6}.
```

Then

```math
\widehat B\widehat B^T
=
\widetilde L.
```

**Status: EXACT IDENTITY.**

A graph Dirac operator

```math
\mathcal D_G
=
\begin{pmatrix}
0 & \widehat B\\
\widehat B^T & 0
\end{pmatrix}
```

therefore satisfies

```math
(\mathcal D_G^2)_{\rm vertex}
=
\widetilde L.
```

This supplies an exact finite \(z=1\) vertex branch.

---

# 9. Finite normal/schedule carrier

For a diagonal lapse matrix \(M_N\), define

```math
K[N]
=
\begin{pmatrix}
0 & M_N\widehat B\\
\widehat B^T M_N & 0
\end{pmatrix}.
```

Then the vertex block of the normal-normal commutator is

```math
[K[N],K[M]]_{\rm vertex}
=
M_N\widetilde L M_M
-
M_M\widetilde L M_N.
```

**Status: EXACT FINITE CONSTRUCTION.**

This is a finite algebraic ancestor of the continuum normal-normal bracket. It is not yet a proof that the full many-body parent possesses local first-class Hamiltonian and momentum constraints.

---

# 10. Metric moves from graph moves

Let \(X\) collect three local frame/diffusion coordinates.

The graph Dirichlet form is

```math
X^T\widetilde L X
=
\frac16
\sum_{\langle uv\rangle}
(X_u-X_v)(X_u-X_v)^T.
```

For a legal 2-switch \(m\),

```math
6X^T(\Delta\widetilde L_m)X
=
\delta h_m.
```

**Status: EXACT IDENTITY.**

Thus graph rewrites, propagation, and metric fluctuations are linked through the same \(\Delta\widetilde L\).

---

# 11. Physical kinetic covariance

The effective metric kinetic covariance can be written schematically as

```math
K_{\rm eff}
\propto
\sum_m
w_m\,
{\rm vec}(\delta h_m)
{\rm vec}(\delta h_m)^T.
```

The corrected audit uses mediator-derived channel weights rather than arbitrary uniform move weights.

After whitening the rank-two metric, the bare spin-four residuals were approximately

```math
\epsilon_4(128)\approx0.249,
```

```math
\epsilon_4(216)\approx0.387,
```

```math
\epsilon_4(344)\approx0.499.
```

**Status: NUMERICAL NEGATIVE RESULT.**

Therefore

```math
\boxed{
\mathrm{amorphous graph disorder alone does not currently isotropize }K_{\rm eff}.
}
```

This is one of the most important corrections in the project.

---

# 12. Rotational closure / \(H_{\rm mix}\)

The proposed \(H_{\rm mix}\) sector penalizes non-scalar rotational charge in local metric-move statistics.

Global positive reweighting can make the tested \(K_{\rm eff}\) exactly isotropic with finite relative-entropy cost.

The old claim that radius-three neighborhoods robustly solve the problem is **CORRECTED**: some earlier exact solutions suppressed the shear kinetic strength instead of genuinely redistributing it.

At graph radius four, sampled local move cones contain positive finite-strength combinations with

```math
K_{\rm shear}\propto I_5.
```

Repeated constructive witnesses retain order-one fractions of the bare shear scale.

**Status: NUMERICAL EXISTENCE / CONVEX-CONE VIABILITY.**

The unresolved statement is stronger:

```math
\boxed{
\mathrm{derive a local microscopic Hamiltonian whose own low-energy measure selects those weights.}
}
```

That statement remains **OPEN**.

---

# 13. Fierz–Pauli rigidity

Take the most general parity-even rotationally invariant two-derivative spatial operator

```math
(Kh)_{ij}
=
a\nabla^2 h_{ij}
+
b(\partial_i v_j+\partial_j v_i)
+
c\,\partial_i\partial_j h
+
d\,\delta_{ij}s
+
e\,\delta_{ij}\nabla^2h.
```

Constraint preservation gives

```math
a+b=0,
\qquad
b+d=0,
\qquad
c+e=0,
```

and self-adjointness gives

```math
c=d.
```

This collapses the operator to the linearized Einstein / Fierz–Pauli form up to normalization and sign conventions.

**Status: DERIVED under the stated symmetry and constraint-preservation assumptions.**

---

# 14. DeWitt kinetic rigidity

For

```math
(M\pi)_{ij}
=
\alpha\pi_{ij}
+
\beta\delta_{ij}\pi,
```

normal/scalar-constraint preservation on the momentum-constraint surface gives

```math
\alpha+2\beta=0.
```

Hence

```math
(M\pi)_{ij}
\propto
\pi_{ij}
-\frac12\delta_{ij}\pi.
```

**Status: DERIVED.**

A separate finite stabilizer/shear construction selects the same trace coefficient.

This is a rigidity result conditional on having the gravitational constraint structure; it does not derive that structure from the full microscopic parent.

---

# 15. TEGR coefficient ray

For the parity-even torsion family

```math
\mathcal L
=
c_1T^\rho{}_{\mu\nu}T_\rho{}^{\mu\nu}
+
c_2T^\rho{}_{\mu\nu}T^{\nu\mu}{}_\rho
+
c_3T^\rho{}_{\mu\rho}T^{\sigma\mu}{}_\sigma,
```

eliminating the unwanted vector and antisymmetric kinetic sectors selects

```math
(c_1,c_2,c_3)
\propto
(1,2,-4),
```

up to conventions.

**Status: DERIVED under the stated degree-of-freedom conditions.**

This is the TEGR ray. The result is a conditional infrared rigidity statement, not a microscopic derivation of TEGR.

---

# 16. Two tensor modes

A symmetric spatial metric perturbation has six components.

Three spatial gauge directions plus one scalar/normal constraint give

```math
6-3-1=2.
```

Finite-\(q\) constructions realize this count algebraically.

**Status: FINITE KINEMATIC CONSTRUCTION.**

The full assembled parent has not yet been shown to gap all unwanted scalar/vector modes in the thermodynamic phase.

---

# 17. Matter and Hodge repair

The raw edge sector of an incidence Dirac operator has cycle-kernel dimension

```math
\dim\ker B|_{\rm edge}
=
E-N+1
```

for a connected graph.

Use local cycle boundaries \(Q_c\) and

```math
H_{\rm curl}
=
\sum_c
\mu_c Q_c^\dagger Q_c,
\qquad
\mu_c>0.
```

Because cycle boundaries lie in \(\ker B\), this term leaves the vertex-gradient branch unchanged while lifting edge-cycle zero modes.

**Status: DERIVED construction.**

A universal hard face-length cutoff \(\ell\le7\) is **FALSE**.

On corrected autonomous states,

```math
\ell_{\rm span}
=
7,\ 7,\ 8
```

for

```math
N=128,\ 216,\ 344.
```

For a soft hierarchy

```math
\mu_\ell\propto\rho_f^{\ell-4},
```

representative exact finite curl gaps are

| `rho_f` | `N=128` | `N=216` | `N=344` |
|---:|---:|---:|---:|
| 0.10 | 0.006735 | 0.003982 | 0.002791 |
| 0.20 | 0.034515 | 0.029971 | 0.039429 |
| 0.30 | 0.084391 | 0.095977 | 0.182344 |

using all local cycles through the spanning length.

**Status: NUMERICAL finite-size success.**

A uniform thermodynamic curl gap remains **OPEN**.

---

# 18. Autonomous phase evidence

At the frozen graph couplings, corrected coordinate-free autonomous states give

| `N` | autonomous `E/N` | best scanned Abelian/Cayley `E/N` |
|---:|---:|---:|
| 128 | -1.301651700 | -1.301602474 |
| 216 | -1.302092376 | -1.301972547 |
| 344 | -1.302342902 | -1.302071375 |

with finite spectral-dimension diagnostics around

```math
d_s(5)
\approx
3.04,\ 3.21,\ 3.37.
```

**Status: STRONG NUMERICAL EVIDENCE for a competitive low-dimensional amorphous basin.**

The three states are not equally equilibrated.

Therefore no asymptotic exponent or thermodynamic three-dimensionality theorem is claimed.

---

# 19. Shared-clock finite coefficient lock

In finite canonical gravity-like constructions, write

```math
H[N]
=
A K[N]-B R[N].
```

Finite exhaustive tests select

```math
AB=1
```

in the relevant finite arithmetic model.

For the finite matter edge Hamiltonian, the corresponding bracket selects

```math
ab=1.
```

A shared schedule normalization then gives

```math
AB=ab=1.
```

**Status: EXACT FINITE coefficient-lock construction.**

It is evidence that matter and geometry can share one schedule normalization. It is not yet a derivation of realistic interacting matter coupled to the final parent.

---

# 20. Black-hole branch: formal status only

The black-hole branch is downstream and should not be used as evidence that the core model is complete.

For an isospectral family

```math
H(\lambda)
=
U(\lambda)H_0U^\dagger(\lambda),
```

with

```math
U(\lambda)=e^{-i\lambda G},
```

the spectral second-order response and contact term cancel at zero frequency:

```math
\chi(0)=0.
```

**Status: DERIVED structural mechanism.**

Finite-frequency transitions need not vanish.

This is only a qualitative structural analogue of

```math
\mathrm{zero static Love}
+
\mathrm{nonzero dynamical absorption}.
```

It is not a Schwarzschild/Kerr response derivation.

The corrected microscopic horizon target is a cross-Jacobian

```math
L^{\rm micro}_{xy}
=
\frac{\delta\Theta_x^+}{\delta b_y},
```

not a symmetric same-operator equilibrium susceptibility.

**Status: STRUCTURAL TARGET / OPEN microscopic realization.**

---

# 21. Minimal theorem package required to close GWXP

The project is not mathematically closed unless the following propositions are proved, or replaced by stronger equivalents.

## Proposition A — thermodynamic geometry

There exists an open microscopic coupling region such that the thermodynamic low-energy phase of the autonomous parent has:

```math
d_s\to3,
```

appropriate finite-dimensional volume growth,

```math
\lambda_1\sim N^{-2/3}
```

up to finite-size/disorder corrections, and lower free/ground-state energy than all relevant competing phases.

**Status: OPEN.**

---

## Proposition B — autonomous kinetic isotropy

A finite-range microscopic \(H_{\rm mix}\) or equivalent schedule/frustration term, specified independently of the desired answer, produces in its low-energy phase

```math
K_{\rm eff}^{ijkl}
=
K_{\rm iso}^{ijkl}
+
o(1),
```

with the physical spin-four component satisfying

```math
c_4(N)\to0
```

while the shear coefficient remains finite and positive.

**Status: OPEN.**

---

## Proposition C — first-class many-body constraint phase

The same microscopic parent possesses a low-energy sector in which local scalar and spatial generators satisfy the appropriate first-class algebra, with the same emergent inverse metric \(Q^{ij}\) that controls propagation.

Schematically,

```math
[H[N],H[M]]
\longrightarrow
D\!\left[
Q^{ij}
(N\partial_jM-M\partial_jN)
\right],
```

with the other brackets closing consistently.

**Status: OPEN.**

---

## Proposition D — spectrum

In the same phase there are exactly two healthy gapless tensor polarizations and no additional unwanted gapless scalar or vector geometric modes.

**Status: OPEN.**

---

## Proposition E — nonlinear continuum universality

The continuum long-wavelength limit exists and lies in the Einstein/TEGR universality class at two derivatives, with controlled higher-derivative corrections.

**Status: OPEN.**

---

# 22. Clean failure conditions

GWXP should be considered falsified or substantially damaged if any of the following persists under fair large-\(N\) tests:

1. the autonomous graph phase flows to rank-one/rank-two, crystalline, expander, or other non-3D competitors;
2. the apparent \(d_s\sim3\) behavior is a finite-size transient;
3. physical spin-four anisotropy remains finite after the actual local microscopic \(H_{\rm mix}\) is specified;
4. isotropy requires nonlocal/global fitted weights;
5. the matter curl gap collapses as the required local cycle length grows;
6. the shared propagation/constraint metric cannot be maintained;
7. the schedule algebra never becomes a genuine first-class redundancy;
8. extra scalar/vector modes remain gapless;
9. the desired closure works only after explicitly inserting GR's constraint tensors by hand.

---
# 23. Formal bottom line

The strongest mathematically defensible summary is:

> **Formal bottom line**
>
> Many required finite algebraic structures exist;  
> a competitive autonomous low-dimensional graph basin exists numerically;  
> the corrected mediator is finite, Hermitian and relationally local;  
> but bare graviton kinetics remain spin-4 anisotropic;  
> and the one-parent first-class thermodynamic phase is unproved.

The remaining problem is an **integration theorem**, not the absence of candidate ingredients.
