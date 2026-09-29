# GWXP / COSMIC GLUE
## MASTER ROLLOVER HANDOFF
### 29 September 2026

**Purpose:** This is the new canonical handoff for the entire GWXP / Cosmic Glue programme. It supersedes the 28 September rollover while preserving it in full below. It combines the previous V3/V4/V5 handoffs, master evidence ledger, graph-only Natural Emergence work, the N=343 closure/isotropy campaign, the finite schedule/DeWitt/matter integration work, the moving-Q and incidence/Hodge results, and the cutoff-recovered N=344 nucleation/phase-mechanism calculations that were not posted before the previous chat hit its length limit.

**Use this document as the source of truth for the next ChatGPT instance.** Where later sections conflict with earlier sections, the later section is authoritative and the earlier statement remains as historical provenance. Killed, demoted, corrected, and conditional claims must remain labelled.

> **START THE NEXT CHAT HERE:** Upload this document and say: **“Continue GWXP from the 29 September master rollover. Read the entire handoff, preserve every killed/demoted/corrected branch, use short falsifiable computational passes, and begin with Section 43: Current Decisive Target. Do not re-derive settled algebra unless a new contradiction requires it.”**

**Rollover completeness note:** Sections 0-26 reproduce the 28 September canonical rollover that already consolidated the older V5 handoff/evidence ledger. Sections 27 onward contain all major work performed afterward, including recovered unposted calculations from the timeout boundary.

---

# 0. Research style and operating rules for the next instance

The user wants this treated as an adversarial research programme, not as a motivational exercise. The useful mode is: derive from first principles, attack the weakest link, run explicit finite benchmarks, preserve failed routes, and keep moving when the next test is clear.

Use the following epistemic labels consistently:

- **ESTABLISHED** - existing mathematics/physics, not a new project result.
- **EXACT / EXACT FINITE** - algebraic identity or finite construction verified exactly.
- **DERIVED** - worked through from stated assumptions inside GWXP.
- **NUMERICAL** - finite computation with saved code/output.
- **STRONG NUMERICAL EVIDENCE** - repeated finite computations with adversarial controls, but not a theorem/thermodynamic proof.
- **CONDITIONAL** - follows if a named microscopic or continuum assumption holds.
- **OPEN** - still required.
- **KILLED / DEMOTED / CORRECTED** - do not quietly resurrect the stronger claim.

Non-negotiable research discipline:

1. Do not call GWXP a Theory of Everything or solved quantum gravity yet.
2. Do not promote a finite-size plateau to a thermodynamic phase without scaling.
3. Distinguish algebraic closure from a genuine first-class Dirac constraint interpretation.
4. Distinguish a gapped unwanted mode from a gauge redundancy.
5. Distinguish a proxy tensor from the actual downfolded physical graviton kinetic tensor.
6. Search the literature before making novelty claims; broad ingredients such as graphity, communicability, heat-kernel actions, emergent gauge theories, and tensor-network gravity already have substantial prior art.
7. When a benchmark is contradicted by a later test, preserve both the result and the correction.
8. Prefer simple, falsifiable calculations over elaborate hand-built toy models.

The user's preferred working style is direct and technically serious. Avoid unnecessary caveat padding, but keep the epistemic boundary exact.

---

# 1. One-line hypothesis and one-line target

## 1.1 Surviving hypothesis

The original slogan "matter uses finite information capacity and the shortage is gravity" was killed. The surviving programme is:

> **A fundamentally finite relational quantum system may possess a protected low-energy phase in which geometry, gauge/refoliation redundancy, and gravity emerge together as collective properties of the relational state.**

A useful intuitive interpretation remains that spacetime can behave like an optimized finite-information relational ledger, but that is an interpretation, not a demonstrated microscopic law.

## 1.2 Current one-line target

```text
one autonomous finite relational parent
    -> spontaneous 3D relational geometry
    -> local schedule/refoliation + spatial gauge structure
    -> same emergent Q^{ij} in propagation and HDA
    -> exactly two healthy z=1 tensor modes
    -> isotropic physical rank-4 kinetic tensor
    -> nonlinear first-class closure
    -> Einstein/TEGR two-derivative IR
```

The gravity sector is not finished until that chain is realized by **one parent**, without compiling GR's constraints into the microscopic Hamiltonian by hand.

---

# 2. Executive verdict as of 28 September 2026

## 2.1 What is now unusually strong

The programme has accumulated several independent structures that all point toward the same gravitational IR target:

- finite spin-2 kinematic count: `6 - 3 - 1 = 2`;
- Fierz-Pauli / linearized Einstein rigidity from constraint preservation;
- DeWitt kinetic rigidity, selecting the `-1/2` trace coefficient;
- TEGR torsion coefficient ray `(1,2,-4)` under the required degree-of-freedom conditions;
- exact finite schedule/refoliation holonomies whose normal-normal commutator closes into spatial motion;
- generalized-dihedral reflection algebra producing the lapse wedge and the same inverse metric `Q^{ij}`;
- exact local smeared grading `[normal,normal] subset spatial`, `[spatial,normal] subset normal`, `[spatial,spatial] subset spatial` for arbitrary inhomogeneous matching maps;
- ordinary transverse link flips generating local schedule/reconnection tunnelling autonomously, including a full K6 microscopic confirmation;
- an emergent graph spectral term with a heat-kernel route to `sqrt(q) R`;
- an explicit frame map whose symmetric part spans all six spatial metric components and contains the TT plus/cross directions;
- an effective constrained linearized spectrum with exactly two physical TT modes and dispersion controlled by `Q^{ij} k_i k_j`;
- a universal leading metric-rewire hopping amplitude `20 Gamma^4 / lambda^3` from the valence penalty;
- a sharp identification of the rank-4 rotational-isotropy problem in crystalline degree-6 phases;
- a statistically isotropic / amorphous route in which rank-4 anisotropy self-averages as approximately `N^{-1/2}`;
- most recently, a **graph-only** candidate parameter region where the original graph functional supports low-energy, structurally disordered, approximately three-dimensional states without supplying external coordinates.

## 2.2 What is not proved

The missing theorem is still the integration theorem:

```text
one parent Hamiltonian
    -> stable thermodynamic 3D phase
    -> genuine local first-class scalar/spatial constraints
    -> shared-metric HDA
    -> actual downfolded K_eff^{ijkl} with no residual spin-4 anisotropy
    -> exactly two healthy massless tensor modes
    -> nonlinear closure and continuum universality
```

In particular, the newest amorphous graph results are **strong numerical evidence for a candidate basin**, not yet a thermodynamic proof.

## 2.3 Current strongest concise claim

A defensible current summary is:

> **GWXP has not derived gravity from finite information. It has constructed and numerically connected many of the required finite relational structures, and it now has evidence that the same graph-only parent can support a low-dimensional, approximately 3D, orientationally disordered basin. The decisive remaining tests are thermodynamic scaling, the actual downfolded rank-4 physical kinetic tensor, and one-parent first-class constraint integration.**

---

# 3. Core results that should not be casually reopened

## 3.1 Finite spin-2 counting - DERIVED

A symmetric spatial metric perturbation has 6 components. Three spatial gauge directions and one scalar/normal constraint leave:

```math
6 - 3 - 1 = 2
```

physical configuration modes.

Finite-q stabilizer-like regulators can realize this counting algebraically.

## 3.2 Fierz-Pauli rigidity - DERIVED

For the most general parity-even rotationally invariant two-derivative spatial operator

```math
\begin{aligned}
(Kh)_ij &= a nabla^{2} h_ij \\
&\quad + b (d_i v_j + d_j v_i) \\
&\quad + c d_i d_j h \\
&\quad + d \delta_{ij} s \\
&\quad + e \delta_{ij} nabla^{2} h,
\end{aligned}
```

constraint preservation gives

```math
\begin{aligned}
a + b &= 0 \\
b + d &= 0 \\
c + e &= 0
\end{aligned}
```

and self-adjointness gives

```math
c = d.
```

This collapses the operator to the linearized Einstein / Fierz-Pauli form up to sign and normalization.

## 3.3 DeWitt kinetic rigidity - DERIVED / EXACT FINITE SUPPORT

For

```math
(M \pi)_ij = \alpha \pi_{ij} + \beta \delta_{ij} \pi,
```

scalar-constraint preservation on the momentum-constraint surface forces

```math
\alpha + 2 \beta = 0,
```

hence

```math
(M \pi)_ij \propto \pi_{ij} - (1/02) \delta_{ij} \pi.
```

A separate finite Z5 canonical shear/stabilizer test independently selected `lambda = 1/2`. This is one of the strongest repeated rigidity results in the project.

## 3.4 TEGR coefficient selection - DERIVED under stated DOF conditions

For the parity-even torsion family

```math
\begin{aligned}
L &= c1 T^rho_{\mu \nu} T_rho^{\mu \nu} \\
&\quad + c2 T^rho_{\mu \nu} T^{\nu \mu}_rho \\
&\quad + c3 T^rho_{\mu \rho} T^{\sigma \mu}_sigma,
\end{aligned}
```

removing the unwanted vector and antisymmetric kinetic sectors gives

```math
(c1,c2,c03) \propto (1,2,-4).
```

That is the TEGR ray up to conventions. TEGR is established to be dynamically equivalent to GR up to a boundary term.

## 3.5 Moving-projector theorem - DERIVED

For any smooth isolated projector family `P(q)`:

```math
G_a = i [d_a P, P]
```

satisfies

```math
d_a P = -i [G_a, P].
```

So a moving protected band automatically carries a connection once it depends on collective coordinates.

## 3.6 Zero-static-response structural mechanism - DERIVED

For an isospectral orbit

```math
H(\lambda) = U(\lambda) H_0 U^{\dagger}(\lambda),
```

spectral second-order response cancels the contact/code-motion term at zero frequency, giving a structural

```math
\chi(0) = 0
```

while time-dependent motion can still produce transitions. This is a structural analogue of zero static Love plus absorption, not a derivation of the physical Kerr/Schwarzschild response.

## 3.7 Horizon/MOTS correction - CORRECTED

The generic MOTS stability operator is non-self-adjoint. Therefore it should not be identified with a same-operator Hermitian equilibrium susceptibility.

The correct microscopic target is a **cross-Jacobian**:

```math
L_{\mathrm{micro}},xy = \delta \Theta_{x}^+ / \delta b_y.
```

A directed finite Jacobian can carry the appropriate normal-bundle/covariant-Laplacian structure.

A simple zero mode of a nonlinear marginality equation generically gives the fold:

```text
A ~ |mu-mu_c|^(1/2)
||L^{-1}|| ~ |mu-mu_c|^(-1/2).
```

The old K7 `1/t` pole was a conserved-sector Lehmann pole, not this nonlinear horizon fold.

---

# 4. Historical routes that were killed, demoted, or corrected

These should remain dead unless genuinely new evidence changes them.

1. **KILLED:** logical information content itself is an independent gravitational source.
2. **KILLED:** a scalar "remaining information capacity" can reproduce full relativistic gravity.
3. **KILLED:** microscopic finite factors should be interpreted as literal Planck-sized spacetime points.
4. **KILLED:** a fixed ordinary finite point lattice can support exact continuum HDA derivations.
5. **KILLED:** exact commuting-projector metric gravity is the natural route to a `z=1` Einstein graviton; it naturally produces higher-derivative `k^4/k^6` structure.
6. **KILLED:** bare causal-diamond/path consistency by itself selects GR coefficients.
7. **KILLED:** the HHH Jacobi identity alone selects the DeWitt supermetric.
8. **KILLED:** one scalar `Q` register is sufficient evidence for a relational inverse metric.
9. **KILLED:** site-clock order is emergent geometry.
10. **KILLED:** the early site-clock/complete-graph model as the space mechanism; it produced ordinary clock order but not emergent locality/dimension.
11. **KILLED:** `U/J = 0.009` as an asymptotically 3D graph phase; slab/strip competitors collapse it.
12. **DEMOTED:** the old complete-graph K4-K8 softness sequence as homogeneous finite-size scaling evidence; a size-dependent triangle coupling was discovered.
13. **CORRECTED:** a gapped fiber/schedule band is not automatically a first-class scalar gauge constraint.
14. **CORRECTED:** exact finite group-derived operator closure is not automatically the complete physical Dirac constraint algebra of the extended parent.
15. **CORRECTED:** the shell-preserving "2-switch covariance" test for the 48-direction rank-4 shell was invalid as a physical simple-graph 2-switch calculation because those purported new shell edges were already occupied. The file is preserved with a warning.
16. **KILLED as final phase point:** the earlier `g=4, U=0.0374, kappa=0.01` graph-only `d~3` basin is not sufficient evidence for the thermodynamic 3D phase. A square-guided exact-energy search found a substantially lower square-rich state with heat-kernel `d_s ~ 2.2`, and exact product competitors independently show compactification/collapse pressure there.
17. **CAUTION:** a low-mode IDOS fit can be very misleading at small finite N because degeneracies and spectral gaps distort the slope. Heat-kernel spectral dimension, calibrated against known torus and random-regular controls, is now the preferred finite-size diagnostic.

---

# 5. Natural Emergence - graph sector

## 5.1 Exact valence selection - DERIVED

For edge occupations `n_ij`, edge count `m`, and degrees `d_i`:

```math
H_deg = \mu m + \lambda \sum_{i} C(d_i,2).
```

Target valence `k` is selected on

```math
-2 k \lambda < \mu < -2 (k-01) \lambda.
```

At the center

```math
\mu = -(2k-01) \lambda,
```

this becomes

```math
H_deg = (\lambda/02) \sum_{i} (d_i-k)^{2} + \mathrm{const}.
```

Valence is a resource constraint, not dimension.

## 5.2 Surviving graph functional

Using normalized adjacency and Laplacian

```math
\begin{aligned}
\widetilde A &= D^{-1/02} A D^{-1/2} \\
\widetilde L &= I - \widetilde A,
\end{aligned}
```

the current graph functional is

```math
\begin{aligned}
H_{\mathrm{eff}} &= H_{\mathrm{degree}} \\
&\quad + \tau T \\
&\quad - J \mathrm{Tr} \exp(g \widetilde A) \\
&\quad + U \sum_{edges} [\exp(g \widetilde A)_ij]^{2} \\
&\quad - \kappa \log \det(\epsilon I + \widetilde L).
\end{aligned}
```

Interpretation:

- degree/resource pressure selects finite valence;
- triangle frustration discourages overly clustered local structure;
- `Tr exp(g Atilde)` rewards all-walk communicability;
- the convex edge-capacity term penalizes overconcentrated communication channels;
- the determinant term weakly favors globally connected/spectrally useful structures.

No target coordinates or target dimension are supplied to the energy.

## 5.3 Early degree-6 / mixed-dihedral phase results - NUMERICAL

The frozen older benchmark was

```math
g=6, U=0.018, \lambda=4, \tau=5, \kappa=0.01, \epsilon=0.025.
```

For cubic `Z^3` the infinite energy was approximately

```text
-8.155619787129.
```

But a generalized-dihedral rank-3 phase beats ordinary cubic:

```text
D97   ~ -8.16275
D127  ~ -8.16814
D151  ~ -8.17012
thermodynamic estimate ~ -8.173368935008.
```

Its spectral dimension was approximately

```text
d_spec ~ 2.9814, R^2 ~ 0.9965.
```

Representative rank-4 non-Abelian competitors were much worse, approximately `-7.99`.

Lower-rank quotients can approach the rank-3 covering energy only through decompactification; fixed-scale lower dimension loses.

## 5.4 Clean all-reflection subphase

The all-reflection/cubic presentation used in the clean HDA derivations has its own narrow energetic subwindow. Examples located during the phase scan:

```text
g=4.0   U ~ 0.067757 - 0.070168
g=4.5   U ~ 0.050506 - 0.052089
g=5.0   U ~ 0.036974 - 0.037881
g=5.5   U ~ 0.026641 - 0.027065
g=6.0   U ~ 0.0189259 - 0.019045
g=6.25  U ~ 0.015875 - 0.015896
```

The window closes against tested boundaries above roughly `g ~ 6.5`.

A clean HDA-friendly point used later was

```math
g=5, U=0.0374, \lambda=4, \tau=5, \kappa=0.01, \epsilon=0.025.
```

This was useful as a clean periodic frame laboratory, but the rank-4 kinetic analysis later showed that a globally oriented cubic crystal is not enough for exact spin-2 isotropy.

---

# 6. Autonomous schedule/reconnection dynamics

## 6.1 K4 local matching model - DERIVED + NUMERICAL

For four vertices and six link qubits:

```math
\begin{aligned}
V &= (1/02) \sum_{i} (d_i-1)^{2} \\
H &= V - \Gamma \sum_{e} X_e.
\end{aligned}
```

At `Gamma=0` the zero manifold is the three perfect matchings.

Matching-to-matching tunnelling first appears at fourth order. Summing all 24 virtual paths gives

```math
t = 20 \Gamma^{4}.
```

The K3 schedule-orbit Laplacian then has gap

```math
\Delta_{\mathrm{schedule}} = 60 \Gamma^{4} + \mathcal{O}(\Gamma^{6}).
```

Sparse ED verified the coefficient over a range of Gamma.

## 6.2 Extensive matching orbit - EXACT / NUMERICAL

For all perfect matchings of `K_{2n}`, connect two schedules when one local two-pair rewire transforms one matching into the other.

Number of schedules:

```text
(2n-1)!!
```

The reconnection graph is connected by a constructive proof: repeatedly fix target matched pairs with a local swap.

For equal positive tunnelling, the schedule Hamiltonian

```math
H_{\mathrm{sched}} = t L_matching
```

is positive semidefinite with a unique kernel equal to the uniform schedule superposition.

Numerically, the first gap obeyed

```math
\Delta/t = 3,5,7,9,11
```

for `n=2..6`, strongly suggesting `2n-1`, though a full arbitrary-n smallest-gap proof was not supplied.

## 6.3 Full K6 microscopic confirmation - STRONG NUMERICAL

For all 15 link qubits of K6, with

```math
\begin{aligned}
H0 &= (1/02) \sum_{i} (d_i-1)^{2} \\
V &= -\Gamma \sum_{e} X_e,
\end{aligned}
```

there are 15 perfect-matching states at Gamma=0.

A local matching rewire has the same fourth-order coefficient

```math
t = 20 \Gamma^{4}.
```

The 15-state matching graph predicts relative bands

```math
\begin{aligned}
& 0, \\
& 100 \Gamma^{4}, \\
& 180 \Gamma^{4},
\end{aligned}
```

with multiplicities `1,9,5`.

Full sparse ED of the actual `2^15 = 32768` dimensional Hamiltonian reproduced those bands as Gamma -> 0.

This is important because the schedule-orbit Laplacian is not merely inserted after the fact; it is generated by ordinary link flips at low energy.

---

# 7. Generalized-dihedral schedule/HDA algebra

## 7.1 Native reflection algebra - EXACT

For

```math
G = Z^{3} semidirect Z_2,
```

with reflections `R_s`:

```math
\begin{aligned}
R_s^{2} &= 1 \\
R_s R_t &= T_{s-t} \\
R_s R_t R_s R_t &= T_{2(s-t)} \\
[R_s,R_t] &= T_{s-t} - T_{t-s}.
\end{aligned}
```

For smeared normal generators

```math
H[N] = \sum_{s} N_s K_s,
```

the commutator automatically carries the antisymmetric lapse wedge

```text
N_s M_t - M_s N_t.
```

That wedge is algebraic, not hand-inserted.

## 7.2 Same metric in propagation and HDA - EXACT

For six all-reflection offsets in group coordinates, the same covariance tensor appears in both the graph Laplacian and the normal-normal commutator displacements:

```math
\begin{aligned}
Q &= (1/702) sum_{\alpha<\beta} \\
& (s_alpha-s_beta)(s_alpha-s_beta)^{T} \\
 &= (1/02) Cov(s).
\end{aligned}
```

In the physical cubic basis:

```math
Q = I/6.
```

The low-k normalized Laplacian is

```math
L(k) = Q^{ij} k_i k_j + \mathcal{O}(k^{4}).
```

The continuum commutator gives

```text
[H[N],H[M]]
    -> D[Q^{ij}(N d_j M - M d_j N)].
```

So the same `Q` controls propagation and the HDA structure function.

## 7.3 Variable, sheared Q - NUMERICAL/DERIVED

Using a divergence-form operator

```math
\Delta_{Q} f = d_i(Q^{ij} d_j f),
```

with position-dependent positive non-diagonal `Q(x)`, the normal-normal commutator converged to the half-density Lie derivative with

```math
\xi^i = Q^{ij}(N d_j M - M d_j N).
```

The residual scaled approximately as `L^-2`. Derivative-of-Q terms appeared automatically.

## 7.4 Exact local smeared grading - EXACT

Let arbitrary bijections `phi_a : X -> X` define local matching channels with permutation matrices `P_a`. For arbitrary local weights `N_a(x)`, define a doubled-sheet normal operator

```math
\begin{aligned}
K[N] &= [[0, A_N^{\dagger}], [A_N, 0]], \\
A_N &= \sum_{a} P_a M[N_a].
\end{aligned}
```

Then exactly:

```text
[normal,normal]  subset spatial
[spatial,normal] subset normal
[spatial,spatial] subset spatial.
```

A deliberately sheared/inhomogeneous finite test gave exact block identities to machine precision and Jacobi residual around `4e-15`.

This is stronger than homogeneous closure, but still not by itself a proof that these are the complete local physical Dirac constraints of the full many-body parent.

## 7.5 Refoliation-as-gauge quotient - EXACT finite statement

If spatial relabellings act as `U(pi)` and relational observables are projected/averaged by

```math
P_{\mathrm{rel}} = (1/|G|) \sum_{pi} U(\pi),
```

then `P_rel U(pi)=P_rel`.

If schedule operations differ by a spatial relabelling,

```math
W_a W_b = U(\pi_{ab}) W_b W_a,
```

then after relational projection

```math
P_{\mathrm{rel}} W_a W_b = P_{\mathrm{rel}} W_b W_a.
```

Thus schedule orderings that close into pure spatial relabelling are physically equivalent in the finite quotient.

The remaining open issue is to derive the full local projector/constraint interpretation dynamically from the same extended parent rather than impose the quotient externally.

---

# 8. Finite constraint algebra consolidation

On a finite `Z_4^3 semidirect Z_2` regular representation, define

```math
\begin{aligned}
C_s &= R_s - I \\
D_v &= T_v - I.
\end{aligned}
```

Then exactly:

```math
\begin{aligned}
[C_s,C_t] &= D_{s-t} - D_{t-s} \\
[D_u,C_s] &= C_{u+s} - C_{s-u} \\
[D_u,D_v] &= 0
\end{aligned}
```

in the flat translation sector.

For the selected six reflections,

```math
L = (1/102) \sum_{s} C_s^{\dagger} C_s.
```

Also

```math
\widetilde A = I - L,
```

so the communicability term is literally

```math
-J e^g \mathrm{Tr} \exp(-g L).
```

This is a useful consolidation: graph selection, the propagation Laplacian, and a sum of squared finite group-derived operators become the same algebraic object in the homogeneous phase.

**Important status:** exact finite operator closure is proved; the complete physical first-class interpretation in the extended fluctuating many-body parent remains open.

---

# 9. Frame-to-metric bridge

## 9.1 Reflection-pair frame - EXACT

In the physical basis, the six offsets can be centered into

```text
{+e_x,-e_x,+e_y,-e_y,+e_z,-e_z}.
```

Define three frame vectors `E_a` from the opposite pairs. Then

```math
Q = (1/06) \sum_{a} E_a E_a^{T} = (1/06) E E^{T}.
```

At the cubic point `E=I`, so `Q=I/6`.

## 9.2 Full metric span - EXACT linear algebra

At `E=I`:

```math
\delta Q = (\delta E + \delta E^{T})/6.
```

The linear map from the 9 frame perturbations to symmetric `delta Q` has rank 6. Its kernel has dimension 3 and is exactly the antisymmetric local-frame rotations.

Thus the frame contains the full six-component spatial metric without bolting on a separate symmetric tensor register.

## 9.3 Explicit TT directions - DERIVED

For propagation along z:

```math
\begin{aligned}
plus  : \delta E &= diag(1,-1,0) \\
cross : \delta E_xy &= \delta E_yx = 1
\end{aligned}
```

produce the familiar trace-free, z-transverse plus and cross metric perturbations.

This only identifies TT directions kinematically; constraints are required to prove that only these propagate physically.

---

# 10. Spectral-action / curvature bridge

The graph term is

```math
H_J = -J \mathrm{Tr} \exp(g \widetilde A).
```

Since

```math
\widetilde A = I - \widetilde L,
```

```math
H_J = -J e^g \mathrm{Tr} \exp(-g \widetilde L).
```

If the long-wavelength phase is manifold-like and

```text
Ltilde -> (ell_*^2/6)(-Delta_q) + O(ell_*^4 d^4),
```

then with

```math
t = g ell_*^{2} / 6,
```

the 3D heat-kernel expansion gives

```math
\begin{aligned}
& \mathrm{Tr} \exp[-t(-\Delta_{q})] \\
& ~ (4 \pi t)^{-3/02} \int \sqrt{q} [1 + t R/6 + ...].
\end{aligned}
```

Therefore the same graph-selection term produces

```text
- Lambda int sqrt(q)
- c_R int sqrt(q) R
+ higher-curvature corrections.
```

For the older `g=6` normalization, the curvature coefficient from this term alone was

```text
c_R^(J) ~ 1.50939 J / ell_*.
```

Matching `B = 1/(16 pi G)` would give provisionally

```text
G_eff ~ 0.01318 ell_* / J,
```

or with `j=J ell_*`,

```text
G_eff / ell_*^2 ~ 0.01318 / j.
```

Do not treat this numerical coefficient as a precision prediction until the microscopic normalization of `q`, `pi`, lapse, and the other graph terms is fixed.

---

# 11. Linearized physical spectrum and HDA coefficient lock

These results were generated late and are important for rollover continuity.

## 11.1 Linearized physical-mode audit - DERIVED/NUMERICAL

Starting with:

- positive emergent inverse metric `Q^{ij}`;
- the scalar and momentum constraint structure;
- Fierz-Pauli curvature operator;
- DeWitt kinetic form;

for every nonzero momentum tested:

```math
\begin{aligned}
& 6 symmetric metric components \\
&\quad - 1 scalar constraint \\
&\quad - 3 spatial gauge directions \\
 &= 2 physical configuration modes.
\end{aligned}
```

An explicit TT gauge slice had nullity 2.

The Fierz-Pauli operator restricted to that slice had two equal positive eigenvalues proportional to

```math
p^{2} = Q^{ij} k_i k_j.
```

The DeWitt form was positive on TT, giving two degenerate healthy tensor modes

```math
\omega^{2} \propto Q^{ij} k_i k_j.
```

This is an IR/effective consistency test, not a microscopic derivation of the kinetic coefficient from Gamma.

File: `gwxp_linearized_physical_modes.py`.

## 11.2 HDA coefficient lock - DERIVED

Write the linearized scalar Hamiltonian as

```math
\begin{aligned}
H[N] &= A \int N (\pi_{ij} \pi_{ij} - 1/2 \pi^{2}) \\
&\quad - B \int N R^{1}[h] + ...
\end{aligned}
```

At the first nontrivial order, the scalar-scalar Poisson bracket gives

```math
\begin{aligned}
& {H[N],H[M]} \\
 &= A B D_i [N d^i M - M d^i N]
\end{aligned}
```

in the conventions used by the benchmark.

Canonical HDA normalization therefore requires

```math
A B = 1.
```

Consequences:

- the kinetic and curvature normalizations are not independent once the normal generator convention is fixed;
- if the graph spectral term determines `B`, HDA closure fixes `A` up to the time/lapse normalization;
- Gamma need only generate a positive nonzero kinetic operator in the correct constrained sector; its microscopic update scale can then be related to emergent proper time.

File: `gwxp_hda_coefficient_lock.py`.

---

# 12. Microscopic metric motion from link flips

## 12.1 Universal fourth-order 2-switch amplitude - DERIVED

For a generic target valence `k`, take

```math
\begin{aligned}
H_deg &= (\lambda/02) \sum_{i} (d_i-k)^{2} \\
V &= -\Gamma \sum_{e} X_e.
\end{aligned}
```

A genuine degree-preserving 2-switch changes only degree defects of four endpoints. The background valence `k` cancels out of the denominators.

Summing all 24 four-flip orders gives

```math
|t_{\mathrm{switch}}| = 20 \Gamma^{4} / \lambda^{3}
```

at leading order, before weaker graph terms renormalize the virtual denominators.

This was checked exactly for several lambda values.

File: `gwxp_microscopic_metric_kinetic_scale.py`.

## 12.2 Continuum configuration-space kinetic coefficient - DERIVED

For a coarse metric coordinate with step `delta_h`, a tight-binding hopping `t_switch` gives

```math
\begin{aligned}
& E(p_+,p_x) \\
 &= 2 t_{\mathrm{switch}} [2 - \cos(\delta_{h} p_+) - \cos(\delta_{h} p_x)] \\
& ~ t_{\mathrm{switch}} \delta_{h}^{2} (p_+^{2}+p_x^{2}).
\end{aligned}
```

Thus structurally

```math
A_TT = \rho_{\mathrm{move}} \delta_{h}^{2} (20 \Gamma^{4}/\lambda^{3}).
```

The unknown `rho_move delta_h^2` is a coarse-graining Jacobian, not a new microscopic coupling.

## 12.3 Local rewires span the full metric - NUMERICAL/LINEAR ALGEBRA

On the cubic representative, local degree-preserving rewires with new edge lengths up to face-diagonal scale were enumerated.

Results:

```math
\begin{aligned}
rank in Sym(03) &= 6 / 6 \\
rank of traceless projections &= 5 / 5 \\
rank onto TT(k||z) &= 2 / 2.
\end{aligned}
```

So the transverse-link dynamics has kinematic access to the full local metric, including both TT polarizations.

File: `gwxp_local_rewire_metric_span.py`.

---

# 13. The cubic rank-4 kinetic problem

This branch is central because it exposed a real obstruction rather than another supporting coincidence.

## 13.1 Rank-2 isotropy is not enough - EXACT observation

For the six cubic directions

```text
{+/-e_x, +/-e_y, +/-e_z},
```

the second moment is isotropic:

```math
<n_i n_j> = \delta_{ij}/3.
```

But the fourth moment is not:

```math
\begin{aligned}
<n_x^{4}> &= 1/3 \\
<n_x^{2} n_y^{2}> &= 0,
\end{aligned}
```

where rotational isotropy requires

```math
\begin{aligned}
<n_x^{4}> &= 1/5 \\
<n_x^{2} n_y^{2}> &= 1/15.
\end{aligned}
```

Thus a globally oriented cubic microstructure can look isotropic to rank-2 propagation while a spin-2 kinetic tensor still sees preferred axes.

## 13.2 Cubic kinetic rigidity - DERIVED

The most general cubic-symmetric kinetic map decomposes the symmetric momentum tensor into:

- trace;
- diagonal-traceless `E_g` sector;
- off-diagonal `T_2g` sector.

Let the corresponding coefficients be

```math
\lambda_{0}, \lambda_{E}, \lambda_{T}.
```

Impose the momentum constraint and require preservation of the linear scalar constraint for arbitrary momentum direction.

The unique solution up to normalization is

```math
\lambda_{0} : \lambda_{E} : \lambda_{T} = -1/2 : 1 : 1.
```

So exact first-class constraint preservation forbids the cubic TT split and recovers the DeWitt ray.

**Important limitation:** this proves what the exact IR theory must look like if the constraints are first-class. It does not by itself prove the microscopic cubic anisotropy is dynamically projected or renormalized away.

File: `gwxp_cubic_kinetic_rigidity.py`.

## 13.3 Full-parent cubic rewire calculations did not automatically fix it - NUMERICAL

Including full graph-energy corrections in representative local 2-switch denominators still left significant orientation dependence. Finite-size checks did not show a clean flow to unity.

Therefore the earlier escape route "the graph terms probably make the cubic shell isotropic anyway" is not currently supported.

---

# 14. Rank-4-isotropic shell searches

These were useful as mathematical laboratories, but the current direction has shifted toward amorphous statistical isotropy.

## 14.1 Icosahedral shell - EXACT design check

The 12 antipodal icosahedral directions satisfy both second- and fourth-moment isotropy to machine precision. This proved that finite local rank-4 isotropic shells are possible.

It was not accepted as a solution because inserting an icosahedron by hand would evade Natural Emergence.

File: `gwxp_icosahedral_isotropy.py`.

## 14.2 48-direction periodic integer shell - EXACT moment isotropy

A periodic `Z^3` Cayley shell made from the union of the full cubic orbits

```text
(2,1,1)
(5,2,2)
```

has 48 directions and exactly isotropic rank-2 and rank-4 raw generator moments.

It also admits an exactly isotropic TT quadratic form under equal channel weights.

Files:

- `gwxp_rank4_isotropic_natural_emergence.py`
- `gwxp_rank4_kinetic_protection.py`
- `gwxp_rank4_tt_kinetic.py`

## 14.3 Correction to shell-preserving 2-switch test - CORRECTED

A later test tried to enumerate "shell-preserving" simple-graph rewires whose new displacements also belonged to the occupied shell. In a homogeneous Cayley graph those edges are already present. Therefore that calculation was not a valid microscopic simple-graph 2-switch test.

The file `gwxp_rank4_shell_2switch_covariance.py` is preserved with an explicit warning and must not be cited as the physical parent kinetic tensor.

## 14.4 Better exact rank-4 shells - NUMERICAL search

Searches over cubic integer-orbit unions found shells with much smaller residual genuine-rewire anisotropy.

A three-orbit exact rank-4 shell

```text
O(4,3,0) union O(4,0,0) union O(5,3,0)
```

with total valence 54 gave a residual five-dimensional traceless rewire spread of only about

```text
0.918%.
```

This was an improvement, not exact closure.

File: `gwxp_rank4_three_orbit_rewire_search_fast.py`.

## 14.5 Strategic conclusion of the shell branch

The shell searches suggested that exact microscopic rank-4 isotropy is possible but increasingly artificial. This motivated the stronger physical question:

> Does the parent prefer a statistically isotropic, finite-correlation-length relational phase in which the spin-4 anisotropy vanishes under coarse graining, rather than a globally oriented crystal?

That is now the preferred route.

---

# 15. Statistical isotropy / fluctuating-frame route

## 15.1 IID isotropic local directions - NUMERICAL

For independent isotropically distributed local relational directions, the five-dimensional traceless kinetic anisotropy falls with the total number of samples approximately as

```text
epsilon_4 ~ N^(-1/2).
```

Measured fits were approximately

```text
alpha_local ~ -0.4987
alpha_block ~ -0.4985.
```

File: `gwxp_statistical_isotropy_scaling.py`.

## 15.2 Randomly oriented degree-6 cubic frames - NUMERICAL + EXACT rank-2 statement

Rotate the local triad independently from cell to cell.

For every individual cell:

```math
Q_ij = \delta_{ij}/3
```

exactly, independent of orientation.

The rank-4 cubic anisotropy is orientation-dependent and averages away under block coarse graining. The measured block exponent was approximately

```text
-0.4961.
```

Thus the problem is not degree 6 by itself; it is **long-range global orientational crystalline order**.

File: `gwxp_random_frame_amorphous.py`.

## 15.3 Finite orientational correlation length - NUMERICAL

Cells were grouped into orientation domains of fixed size. For every fixed finite correlation volume, the spin-4 anisotropy still scaled as approximately

```text
B^(-1/2).
```

Measured exponents for domain volumes 1, 4, 16, and 64 were all approximately `-0.50`.

If the entire observation volume shares one orientation, the anisotropy stays finite instead of decaying.

Therefore the sharp IR condition is:

```text
finite orientation correlation volume
    -> isotropic rank-4 IR

long-range crystal order
    -> persistent spin-4 anisotropy.
```

File: `gwxp_orientational_correlation_scaling.py`.

---

# 16. Externally generated amorphous graph adversaries

Before removing external coordinates completely, exactly degree-6 triangle-free amorphous graphs were constructed from random bipartite point clouds on a 3-torus. The Euclidean coordinates were used only to generate adversarial graphs; the GWXP energy was evaluated from adjacency alone.

At the old clean cubic point `g=5, U=0.0374`, cubic beat all generated amorphous competitors by a significant margin.

At lower g / lower effective capacity pressure, some amorphous graphs beat cubic. This showed that the same functional contains both crystalline and amorphous-friendly regimes.

Files:

- `gwxp_amorphous_degree6_energy.py`
- `gwxp_amorphous_crossing_scan.py`
- `gwxp_amorphous_size_scaling.py`

However this did **not** prove Natural Emergence because the candidate graphs were manufactured using a 3D point cloud. That motivated the graph-only work below.

---

# 17. Graph-only amorphous Natural Emergence - latest branch

This is the current frontier and the section the next instance should read most carefully.

## 17.1 First graph-only experiment - STRONG but later corrected in interpretation

Start from a random 6-regular graph. Use only:

- adjacency-based GWXP energy;
- degree-preserving simple-graph 2-switches;
- no external coordinates.

At an early point such as

```math
g=4, U=0.052, \tau=5, \kappa=0.01, \epsilon=0.025,
```

finite N=64 annealing reached lower-energy graphs with low-mode spectral fits near `d ~ 3`.

After deeper work, however, it became clear that plain low-mode IDOS fitting is fragile and that lower-energy square-rich states can exist. This result is evidence of low-dimensional self-organization, but not the final phase point.

Files:

- `gwxp_graph_only_amorphous_emergence.py`
- `gwxp_graph_only_multiseed.py`
- `gwxp_graph_only_deep_refinement.py`
- `gwxp_graph_only_deep_geometry.py`
- `gwxp_graph_only_size_scaling.py`

## 17.2 Spectral-dimension calibration - CRITICAL CORRECTION

The same first-k-eigenvalues IDOS estimator was calibrated on known 3D cubic tori and random 6-regular graphs.

Results:

- cubic tori do produce values around 3 for certain low-mode windows, but degeneracies distort other windows badly;
- random 6-regular graphs produce much larger effective dimensions at comparable N;
- therefore the old estimator can separate expanders from low-dimensional graphs, but a single fitted number is not robust enough to identify the continuum dimension.

Heat-kernel spectral dimension is now the preferred diagnostic:

```math
d_s(t) = 2 t [sum \lambda \exp(-t \lambda)] / [sum \exp(-t \lambda)].
```

File: `gwxp_spectral_dimension_calibration.py` and later `gwxp_heat_kernel_dimension.py`.

## 17.3 Old low-U 3D basin is metastable against square-rich collapse - KILLED as final point

At the old low-U point, a proposal heuristic favoring square-producing switches was used **only to find barriers more efficiently**. Every proposed state was still evaluated by the exact original energy.

This found a much lower-energy state with approximately

```text
C4/N ~ 6.45
```

and a heat-kernel plateau near

```text
d_s ~ 2.2.
```

Exact product competitors independently show the same collapse pressure. At `g=4, U=0.0374, kappa=0.01`:

```text
Z^3                e ~ -2.9655264
Z^2 x C4           e ~ -2.9815221
Z x C4 x C4        e ~ -2.9970386
```

so compactified lower-dimensional products beat the decompactified 3D product.

Files:

- `gwxp_square_guided_anneal.py`
- `gwxp_product_dimension_competitors.py`
- `gwxp_graph_phase_order_parameters.py`

This correction is important: the graph-only parent can find low-dimensional geometry, but the old parameter point did not cleanly select 3D.

## 17.4 Search for an amorphous-3D overlap window

The target is a coupling interval where:

1. 3D beats compactified lower-dimensional product competitors;
2. an amorphous/disordered graph still beats the ordered cubic crystal.

Define:

```math
\begin{aligned}
U_{\mathrm{collapse}} &= lower bound needed for Z^{3} to beat compactified products \\
U_{\mathrm{amorph}} &= upper bound below which an amorphous graph beats cubic.
\end{aligned}
```

We require

```text
U_collapse < U < U_amorph.
```

With `kappa=0.01`, a scan over g found no overlap; the miss was small but persistent.

Increasing **the already-existing determinant coupling** opened a narrow tested window.

At approximately

```math
\begin{aligned}
g &= 3.0 \\
\kappa &= 0.08 \\
\epsilon &= 0.025 \\
\tau &= 5
\end{aligned}
```

we found

```text
U_collapse ~ 0.105293
U_amorph   ~ 0.106651.
```

So the current candidate is

```math
U = 0.106.
```

No new operator was added; only existing couplings were moved.

File: `gwxp_amorphous_window_kappa_scan.py`.

## 17.5 Product-energy check at the candidate point

At

```math
g=3, U=0.106, \kappa=0.08, \epsilon=0.025,
```

representative infinite product energies are approximately:

```text
Z^3               -1.7617424011
Z^2 x C4          -1.7616853319
Z x C4 x C4       -1.7614118614
Z^2 x C6          -1.7616738265
Z x C6 x C6       -1.7615902536
```

So the tested decompactified 3D product beats those compactified products, but only by a narrow margin. This narrowness is exactly why finite-size and broader adversary scans are mandatory.

## 17.6 Graph-only N=128 candidate basin - STRONG NUMERICAL EVIDENCE

At the candidate point, a graph-only triangle-free seed followed by exact-energy annealing and a square-nucleation proposal heuristic produced

```text
N              = 128
e              = -1.7636898952
C4/N           = 4.734375
spectral gap   = 0.18314
```

Heat-kernel spectral dimension:

```text
d_s(t=03) ~ 3.174
d_s(t=04) ~ 3.291
d_s(t=05) ~ 3.235
d_s(t=06) ~ 3.123
```

The flattest intermediate region was approximately

```text
d_s ~ 3.292.
```

Intrinsic spectral-embedding orientation diagnostics:

```text
rank-2 spread  ~ 0.220
rank-4 spread  ~ 0.333.
```

For an IID isotropic finite sample with the same number of edge directions, the mean rank-4 spread was approximately

```text
0.334,
```

so the observed spin-4 anisotropy is consistent with finite-sample isotropic noise.

Saved state:

```text
gwxp_generic_N128_g3.0_U0.106_k0.08_seed128806.npz
```

## 17.7 Unrestricted random-regular N=128 seed - IMPORTANT CONTROL

To remove the triangle-free initialization loophole, the parent was started from an ordinary random 6-regular graph.

It began with 22 triangles. With the actual parent triangle penalty `tau=5`, annealing drove the best state to

```text
0 triangles.
```

After the same square-nucleation barrier was crossed, it independently landed in an almost identical basin:

```math
\begin{aligned}
e &= -1.7635476287 \\
C4/N &= 4.6953125
\end{aligned}
```

Heat-kernel values:

```text
d_s(03) ~ 3.1766
d_s(04) ~ 3.2958
d_s(05) ~ 3.2386
d_s(06) ~ 3.1237.
```

The flattest value was approximately

```text
3.2959.
```

This strongly suggests the phase is not an artifact of starting from a bipartite/triangle-free graph.

Saved state:

```text
gwxp_unrestricted_N128_g3.0_U0.106_k0.08_seed128909.npz
```

## 17.8 Graph-only N=216 candidate - STRONG NUMERICAL, not yet converged thermodynamic proof

At the same candidate couplings, a separate N=216 run with square-guided exact-energy basin search found

```math
\begin{aligned}
e &= -1.7629237021 \\
C4/N &= 4.074074 \\
spectral gap &= 0.129475.
\end{aligned}
```

Heat-kernel spectral dimension:

```text
d_s(03) ~ 3.235
d_s(04) ~ 3.419
d_s(05) ~ 3.435
d_s(06) ~ 3.392
d_s(08) ~ 3.280
d_s(10)~ 3.133.
```

The flattest intermediate region was around

```text
d_s ~ 3.44.
```

Intrinsic orientation diagnostics:

```text
rank-2 spread ~ 0.232
rank-4 spread ~ 0.276.
```

For an IID isotropic finite sample with the same edge count, the rank-4 mean was about `0.246` with a 5-95% interval of approximately `0.166-0.344`, so the observed rank-4 anisotropy remains compatible with finite-sample isotropic disorder.

The rank-2 spread was higher than the corresponding IID mean, so rank-2 isotropy still needs real scaling rather than rhetorical promotion.

Saved state:

```text
gwxp_generic_N216_g3.0_U0.106_k0.08_seed216806.npz
```

## 17.9 Structural disorder rather than a hidden crystal

For the N=128 and N=216 candidate graphs, square participation varies substantially from vertex to vertex.

Example coefficients of variation:

```math
\begin{aligned}
N &= 128  CV_square \sim 0.21 \\
N &= 216  CV_square \sim 0.27.
\end{aligned}
```

A perfect cubic crystal has zero square-participation variance.

Thus these states are structurally disordered, not merely relabeled cubic tori.

File: `gwxp_candidate_amorphous_order.py`.

## 17.10 Current interpretation of the graph-only branch

The strongest defensible statement is now:

> **The existing adjacency-only parent has a tested narrow coupling region supporting low-energy, structurally disordered graphs whose heat-kernel spectral dimension is near three and whose rank-4 orientation statistics are compatible with finite-sample isotropic noise.**

This is **strong numerical evidence for a candidate amorphous 3D basin**.

It is **not yet** evidence that:

- `d_s -> 3` in the thermodynamic limit;
- the anisotropic spin-4 coefficient really flows to zero;
- the basin is the global minimum against all graph competitors;
- ordinary local microscopic dynamics reaches the phase without a nucleation/barrier issue;
- the physical downfolded graviton kinetic tensor is exactly isotropic.

## 17.11 Square-guided proposals: what they do and do not mean

The square-guided search is a **proposal heuristic**, not a new Hamiltonian term.

It selects candidate 2-switches likely to cross the loop-condensation barrier, but every candidate is accepted/rejected using the exact original graph energy.

Therefore it is legitimate evidence about the energy landscape and possible low-energy basins.

It is not by itself evidence that the microscopic local dynamics rapidly thermalizes into that basin. Dynamical accessibility/nucleation remains a separate question.

---

# 18. Current status of the rank-4 objection

The strict adversarial standard is:

```math
\begin{aligned}
& K_{\mathrm{eff}}^{ijkl} \\
 &= K_iso^{ijkl} \\
&\quad + c_4(\ell) C_cubic^{ijkl} \\
&\quad + ...
\end{aligned}
```

The cubic objection is genuinely defeated only if the original parent gives

```text
c_4(ell) -> 0
```

at long scale, hence

```math
omega_+^{2} = \omega_{x}^{2}
```

for arbitrary propagation direction, without manually inserting an isotropic shell or counterterm.

What has changed:

- a globally oriented degree-6 crystal definitely has a rank-4 problem;
- constraint consistency says any exact first-class IR must satisfy `lambda_E=lambda_T`, but this is a target condition, not a microscopic proof;
- statistically isotropic finite-correlation frames suppress the spin-4 tensor as `N^-1/2`;
- the graph-only parent now appears capable of supporting structurally disordered, approximately 3D basins in a narrow parameter region;
- the parent-generated N=128/N=216 rank-4 orientation spreads are compatible with finite-sample isotropic noise.

Therefore the objection has moved from

```text
"degree-6 necessarily leaves a permanent cubic graviton split"
```

to

```text
"show that the actual parent-generated amorphous phase has c_4 -> 0 and that the physical downfolded K_eff, not just an orientation proxy, is isotropic."
```

Do **not** declare the objection dead until that scaling/downfolding is done.

---

# 19. Current decisive target - START NEXT RESEARCH PASS HERE

The next instance should not spend time inventing another local shell. The decisive tests are now thermodynamic and physical.

## 19.1 Primary finite-size scaling test

At the candidate couplings

```math
\begin{aligned}
k &= 6 \\
g &= 3.0 \\
U &= 0.106 \\
\kappa &= 0.08 \\
\epsilon &= 0.025 \\
\tau &= 5
\end{aligned}
```

run graph-only parent optimization for at least

```math
N = 128, 216, 343, 512, ...
```

with multiple independent random 6-regular seeds.

For each best basin record:

1. total energy density;
2. triangle density;
3. `C4/N` and distribution of square participation;
4. normalized-Laplacian gap;
5. heat-kernel spectral dimension `d_s(t)` over a broad intermediate diffusion-time range;
6. graph diameter and average graph distance;
7. intrinsic spectral-embedding rank-2 anisotropy `epsilon_2`;
8. intrinsic traceless rank-4 anisotropy `epsilon_4`;
9. local orientation correlation length if a stable intrinsic frame can be reconstructed;
10. comparison with cubic/product/random-regular competitors at the same N/couplings.

The desired scaling signatures are approximately:

```text
d_s -> 3
lambda_1 ~ N^(-2/03)              [if 3D diffusive continuum]
diameter ~ N^(1/03)               [up to disorder corrections]
epsilon_2 -> 0
epsilon_4 -> 0
```

and, for finite orientational correlation volume,

```text
epsilon_4 ~ N^(-1/2)
```

or faster.

## 19.2 Do not rely on one spectral-dimension estimator

Use at least:

- heat-kernel `d_s(t)` as the primary finite-size measure;
- IDOS/local slopes only as a secondary cross-check;
- gap scaling and diameter scaling as independent dimension diagnostics.

The finite cubic torus and random 6-regular controls should be rerun at every N to calibrate estimator bias.

## 19.3 Global-minimum/adversary test

The candidate overlap window is narrow. Expand the adversary set:

- compactified product geometries;
- random regular graphs;
- square-rich strips/slabs/tubes;
- generalized-dihedral and Cayley competitors;
- block-product/incidence constructions;
- graph states found by alternative annealing proposals.

The candidate basin must not only exist; it must remain competitive or selected as N grows.

## 19.4 Nucleation/dynamical-accessibility test

Separate two questions:

```text
Does the exact energy support the phase?
Does local microscopic dynamics naturally reach it?
```

Square-guided/basin-hopping proposals have established the first more strongly than the second.

Measure barrier heights and basin-to-basin transition rates under the actual link-flip/2-switch dynamics.

## 19.5 Actual physical rank-4 tensor - highest-priority gravity calculation

Do not identify raw edge-direction moments or raw rewire covariance with the physical graviton tensor by assumption.

Derive the downfolded physical kinetic action of the parent in the candidate amorphous phase:

```math
K_{\mathrm{eff}}^{ijkl}
```

and decompose

```math
K_{\mathrm{eff}} = K_iso + c_4 C_spin4 + ...
```

Track `c_4(N)` or `c_4(ell)` directly.

The rank-4 objection is defeated only if

```text
c_4 -> 0
```

and the TT modes have equal dispersion for arbitrary propagation direction.

Then independently verify that first-class scalar-constraint preservation supplies the DeWitt trace extension.

## 19.6 One-parent constraint integration

Even if the amorphous geometry and spin-4 problem close, the full gravity theorem still requires the same extended parent to produce genuine local first-class scalar/spatial constraints rather than only an algebraic schedule carrier.

The already derived arbitrary-bijection finite grading is encouraging because it does not require periodic order. Use it as the algebraic scaffold for the amorphous phase rather than returning to a crystal.

---

# 20. Concrete falsification criteria

The current parent should be considered to fail the gravity programme if robust large-N work shows any of the following:

1. the selected graph phase converges to `d != 3`;
2. the 3D-looking basin is always metastable above a lower-dimensional or expander phase;
3. `epsilon_4` approaches a nonzero constant;
4. the physical downfolded `K_eff` retains a finite cubic/spin-4 tensor even though raw orientation moments look isotropic;
5. schedule/refoliation operators remain gapped physical excitations rather than generating a gauge redundancy;
6. the extended many-body constraint algebra fails first-class closure on overlapping supports;
7. a scalar/vector/aether mode remains gapless alongside the two tensors;
8. tensor propagation and HDA closure use different effective metrics;
9. the required isotropic/constraint point only exists after adding a GR-shaped counterterm or manually imposing a special shell;
10. nonlinear closure produces anomalies that do not vanish in the continuum limit.

A clean kill is scientifically preferable to hiding one of these failures.

---

# 21. Broader physics/TOE boundary

Closing the gravity sector would still not be a Theory of Everything.

A true unification extension would need the same microscopic parent or a principled enlargement to generate, at minimum:

- Standard Model gauge group or an equivalent UV structure;
- chiral matter;
- fermion generations / flavor structure;
- Higgs or symmetry-breaking sector;
- anomaly cancellation;
- matter causal cone compatible with the graviton cone;
- realistic couplings and masses;
- quantum consistency across gravity + matter.

Do not work on this until the gravity parent is either closed or clearly dead. The current research priority remains gravity integration.

---

# 22. File and script inventory

All files below are included in the rollover package where available. The source headers are authoritative if a one-line description here is abbreviated.

## 22.1 Core Natural Emergence / HDA scripts

- `gwxp_natural_emergence_benchmark.py` - original static graph phase benchmark and adversaries.
- `gwxp_schedule_hda_bridge.py` - generalized-dihedral schedule algebra and real-space HDA convergence.
- `gwxp_dynamic_metric_hda.py` - frame-to-metric map and variable-Q HDA test.
- `gwxp_refoliation_gauge_bridge.py` - spatial-relabelling quotient and schedule-order equivalence.
- `gwxp_finite_constraint_algebra.py` - exact finite C/D group-derived operator algebra and Laplacian sum-of-squares identity.
- `gwxp_local_smeared_deformation_algebra.py` - exact local inhomogeneous smeared normal/spatial grading.
- `gwxp_extensive_schedule_orbits.py` - perfect-matching schedule-orbit connectivity and spectrum.
- `gwxp_k6_schedule_emergence.py` - full K6 microscopic ED confirmation of the schedule orbit.

## 22.2 Metric/kinetic/linearized-gravity scripts

- `gwxp_linearized_physical_modes.py` - explicit 2-mode constrained spectrum for generic positive Q.
- `gwxp_hda_coefficient_lock.py` - derivation of `A B = 1` from the scalar-scalar bracket.
- `gwxp_microscopic_metric_kinetic_scale.py` - universal `20 Gamma^4/lambda^3` switch amplitude and continuum kinetic scaling.
- `gwxp_local_rewire_metric_span.py` - local 2-switches span Sym(3), traceless 5D, and both TT directions.
- `gwxp_cubic_kinetic_rigidity.py` - cubic-symmetric kinetic map collapses to `-1/2:1:1` under scalar-constraint preservation.
- `gwxp_controlled_isotropic_kinetic_limit.py` - strong-valence/double-scaling argument for finite hopping with suppressed denominator anisotropy.

## 22.3 Rank-4 shell/design diagnostics

- `gwxp_icosahedral_isotropy.py` - exact rank-2/rank-4 isotropy of the icosahedral direction set.
- `gwxp_rank4_isotropic_natural_emergence.py` - 48-direction integer shell and static phase comparison.
- `gwxp_rank4_kinetic_protection.py` - orbit-weight sensitivity and strong-valence protection analysis.
- `gwxp_rank4_tt_kinetic.py` - exact equal-channel TT kinetic isotropy of the 48-direction shell.
- `gwxp_rank4_shell_2switch_covariance.py` - **corrected diagnostic; not a valid physical shell-preserving simple-graph rewire tensor.**
- `gwxp_rank4_three_orbit_rewire_search_fast.py` - exact rank-4 integer-shell search; best tested genuine-rewire residual split around 0.918%.
- `gwxp_low_energy_genuine_rewires.py` - local linear-response genuine-rewire diagnostic for a rank-4 shell.

## 22.4 Statistical/amorphous isotropy scripts

- `gwxp_statistical_isotropy_scaling.py` - IID isotropic direction scaling, approximately `N^-1/2`.
- `gwxp_random_frame_amorphous.py` - randomly oriented degree-6 triads; exact local rank-2 isotropy and block rank-4 self-averaging.
- `gwxp_orientational_correlation_scaling.py` - finite orientation-correlation-volume scaling.
- `gwxp_amorphous_degree6_energy.py` - externally generated 3D amorphous degree-6 adversary graphs.
- `gwxp_amorphous_crossing_scan.py` - cubic/amorphous energy crossing scan.
- `gwxp_amorphous_size_scaling.py` - finite-size tests of externally generated amorphous graphs.

## 22.5 Graph-only emergence and phase-search scripts

- `gwxp_graph_only_amorphous_emergence.py` - first coordinate-free graph-only anneal.
- `gwxp_graph_only_multiseed.py` - multiseed graph-only checks.
- `gwxp_graph_only_deep_refinement.py` - deep refinement of N=64 basin.
- `gwxp_graph_only_deep_geometry.py` - intrinsic spectral-embedding geometry diagnostics.
- `gwxp_graph_only_size_scaling.py` - reusable N-size graph-only benchmark.
- `gwxp_spectral_dimension_calibration.py` - IDOS estimator controls on cubic tori and random regular graphs.
- `gwxp_fast_trianglefree_anneal.py` - faster triangle-free graph-only search.
- `gwxp_resume_graphonly.py` - resume/refine saved graph-only states.
- `gwxp_graphonly_basin_hop.py` - multi-switch basin-hopping proposal search.
- `gwxp_graph_phase_order_parameters.py` - cycle/square and spectral order parameters.
- `gwxp_square_guided_anneal.py` - square-guided exact-energy proposal search at the old low-U point.
- `gwxp_product_dimension_competitors.py` - exact product-family dimension/collapse competitors.
- `gwxp_amorphous_3d_window.py` - overlap logic between anti-collapse and amorphous preference.
- `gwxp_amorphous_window_kappa_scan.py` - scan showing a narrow overlap after increasing existing kappa.
- `gwxp_fast_trianglefree_generic.py` - generic graph-only anneal at arbitrary g/U/kappa.
- `gwxp_square_guided_generic.py` - generic square-guided exact-energy basin search.
- `gwxp_unrestricted_generic_anneal.py` - unrestricted random 6-regular start including triangle penalty.
- `gwxp_heat_kernel_dimension.py` - heat-kernel dimension calibration on torus, random regular, collapsed and candidate phases.
- `gwxp_candidate_amorphous_order.py` - intrinsic rank-2/rank-4 and square-disorder audit for the candidate N=128/N=216 states.

## 22.6 Saved graph states / NPZ snapshots

Important current snapshots:

- `gwxp_generic_N128_g3.0_U0.106_k0.08_seed128806.npz` - triangle-free-seed candidate basin at the current overlap point.
- `gwxp_generic_N216_g3.0_U0.106_k0.08_seed216806.npz` - N=216 candidate basin at the same point.
- `gwxp_unrestricted_N128_g3.0_U0.106_k0.08_seed128909.npz` - unrestricted random-regular seed converging to an almost identical N=128 basin.

Historical / diagnostic snapshots:

- `gwxp_graphonly_N128_seed128303.npz`
- `gwxp_graphonly_N128_seed128374.npz`
- `gwxp_graphonly_N216_seed216303.npz`
- `gwxp_graphonly_N216_seed216374.npz`

Some historical files were subsequently overwritten by deeper/alternative searches. Use the source script and the handoff result table as the provenance record; do not assume every NPZ still corresponds to the earliest output mentioned in chat.

## 22.7 Repository/update packages

Existing packages:

- `GWXP_GITHUB_FULL_UPDATE.zip`
- `GWXP_UPLOAD_FROM_CURRENT_STATE.zip`

These predate much of the latest metric-kinetic/rank-4/amorphous branch. They should not be treated as the complete current archive until the new scripts and this handoff are folded in.

Repository name used previously:

```text
The-GWXP-Bridge
```

GitHub URL used in outreach:

```text
https://github.com/cameron467/The-GWXP-Bridge
```

---

# 23. Numeric ledger of the most important current values

## 23.1 Schedule/reconnection

```math
\begin{aligned}
& local 2-switch amplitude from valence term: \\
t_{\mathrm{switch}} &= 20 \Gamma^{4} / \lambda^{3} \\
& K4 matching-orbit gap: \\
& 60 \Gamma^{4} + \mathcal{O}(\Gamma^{6}) \\
& K6 effective matching bands: \\
& 0, 100 \Gamma^{4}, 180 \Gamma^{4} \\
& multiplicities 1, 9, 5
\end{aligned}
```

## 23.2 Older generalized-dihedral 3D phase

```math
\begin{aligned}
g &= 6, U=.018 mixed rank-3 generalized-dihedral: \\
& thermodynamic energy estimate \sim -8.173368935 \\
& d_{\mathrm{spec}} \sim 2.9814
\end{aligned}
```

## 23.3 Current candidate amorphous-3D overlap point

```math
\begin{aligned}
target degree k &= 6 \\
g &= 3.0 \\
U &= 0.106 \\
\kappa &= 0.08 \\
\epsilon &= 0.025 \\
\tau &= 5
\end{aligned}
```

Window estimate from tested adversaries:

```text
U_collapse ~ 0.105293
U_amorph   ~ 0.106651
```

Representative infinite product energies:

```text
Z^3            -1.7617424011
Z^2 x C4       -1.7616853319
Z x C4 x C4    -1.7614118614
Z^2 x C6       -1.7616738265
Z x C6 x C6    -1.7615902536
```

Candidate N=128 graph:

```text
e              -1.7636898952
C4/N            4.734375
heat d_s flat   ~3.292
rank-4 spread   ~0.333
```

Independent unrestricted N=128 graph:

```text
e              -1.7635476287
C4/N            4.6953125
heat d_s flat   ~3.296
triangles       0 after starting from 22
```

Candidate N=216 graph:

```text
e              -1.7629237021
C4/N            4.074074
heat d_s flat   ~3.44
rank-4 spread   ~0.276
```

These finite candidate energies being slightly below the infinite `Z^3` line is encouraging but not decisive; the advantage may shrink with N.

---

# 24. What the next instance should say if asked "where are we?"

Use something close to:

> We have not proved GWXP or quantum gravity. The algebraic gravity architecture is much further along than the phase-emergence theorem. The newest result is that the original adjacency-only graph functional appears to have a narrow parameter region where random 6-regular graphs can relax into structurally disordered, approximately three-dimensional low-energy basins, with rank-4 orientation statistics consistent with finite-sample isotropic noise. The make-or-break test is now large-N scaling of the heat-kernel dimension and the actual physical spin-4 coefficient, plus one-parent first-class constraint integration.

Do not answer with "we solved gravity" or "the model is dead"; neither is currently supported.

---

# 25. Exact starter prompt for the next rollover

Copy/paste this if useful:

```math
\begin{aligned}
& Continue the GWXP / Cosmic Glue research programme from the attached rollover handoff. \\
& Treat the handoff as the evidence ledger. Preserve every KILLED / DEMOTED / CORRECTED route. Do not reopen old derivations unless a new contradiction requires it. \\
& The immediate target is the candidate graph-only amorphous 3D phase at: \\
degree k &= 6 \\
g &= 3.0 \\
U &= 0.106 \\
\kappa &= 0.08 \\
\epsilon &= 0.025 \\
\tau &= 5 \\
& Current evidence: \\
- N &= 128 and N=216 graph-only low-energy basins are structurally disordered; \\
&\quad - heat-kernel spectral dimension is roughly 3.3-3.4 at intermediate scales; \\
&\quad - rank-4 orientation spread is compatible with finite-sample isotropic disorder; \\
&\quad - tested product competitors show a narrow anti-collapse/amorphous overlap window; \\
&\quad - ordinary annealing has nucleation barriers, so square-guided proposals have been used only as search accelerators while exact parent energy still decides acceptance. \\
& Attack this as hard as possible. \\
& First: \\
1. build a clean finite-size scaling benchmark for N &= 128,216,343,512+ with multiple random seeds; \\
& 2. use heat-kernel spectral dimension as primary dimension diagnostic, with IDOS/gap/diameter cross-checks; \\
& 3. fit gap scaling and \epsilon_{2}/\epsilon_{4} scaling; \\
& 4. broaden the global-energy adversary set; \\
& 5. distinguish existence of the basin from dynamical accessibility; \\
& 6. then derive the actual downfolded physical K_{\mathrm{eff}}^{ijkl} and track the spin-4 coefficient c4(\ell), rather than relying on raw orientation proxies. \\
The rank-4 objection is defeated only if c4 \to 0 and omega_+^{2} &= \omega_{x}^{2} for arbitrary propagation direction from the original parent. \\
The gravity programme is complete only if the same extended parent also yields genuine local first-class scalar/spatial constraints, shared-metric HDA, exactly two healthy z &= 1 tensors, and nonlinear closure without added GR-shaped counterterms. \\
& Use epistemic labels EXACT / DERIVED / NUMERICAL / CONDITIONAL / OPEN / KILLED. Keep drilling until the candidate either survives or breaks.
\end{aligned}
```

---

# 26. Final handoff sentence

The project has moved from "can finite systems imitate pieces of gravity?" to a much narrower and more falsifiable question:

```text
Can the existing finite relational graph parent possess a thermodynamically stable,
3D, orientationally disordered constraint phase whose actual physical low-energy
kinetic tensor is isotropic and whose schedule algebra becomes genuine refoliation gauge?
```

That is the frontier. Everything else in this document is scaffolding, evidence, or a constraint on how that question must be answered.


---

# 27. Research-strategy update after 28 September

The user explicitly prefers **sideways closure before premature depth**. Continue expanding across adjacent consistency loops until the architecture closes, then compress and deepen.

The preferred sequence is:

```text
1. Expand sideways across geometry, schedule/HDA, matter, clock, kinetic tensor,
   thermodynamics, and locality until the model closes a self-consistency loop.
2. Only after closure, ruthlessly compress the microscopic assumptions.
3. Separate ASSUMED vs DERIVED vs INTERPRETATION.
4. Remove redundant assumptions and treat every rescue term honestly as a model
   modification unless it can itself be derived.
5. Build a micro-to-macro dictionary from microscopic relational variables to:
   distance, proper time, metric/curvature, fields/particles, energy,
   momentum/charge, entropy, and macroscopic matter.
6. Cross-check the same emergent quantities independently in multiple sectors.
```

Operationally, use **small computation batches**. The previous conversation repeatedly hit runtime limits when too many eigensolves or candidate evaluations were bundled together. Report partial findings early, then extend only the informative branch.

The core cross-consistency loop is now:

```math
\begin{aligned}
& graph / incidence operator B \\
\to \widetilde L &= \widehat B \widehat B^{T} \\
& \to propagation Q \\
\to matter z &= 1 branch \\
& \to normal-normal lapse wedge \\
& \to moving graph \delta L \\
& \to metric move \delta h \\
& \to K_{\mathrm{eff}} covariance \\
& \to local schedule/H_{\mathrm{mix}} reweighting \\
& \to isotropic kinetic sector \\
& \to symmetry-derived scalar \\
\to DeWitt ray + AB &= 1 \\
& \to shared schedule clock with matter
\end{aligned}
```

The goal is no longer to collect compatible pieces; it is to prove that they are **the same pieces viewed in different representations**.

---

# 28. Cross-consistency matter result and shared metric

## 28.1 Old one-particle matter hopping - useful but z=2 limitation

A conserved internal matter excitation on a degree-6 graph can use

```math
H_m^{01} = \Delta I - t_B A.
```

For degree 6,

```math
6 I - A = 6 \widetilde L.
```

The archived N=128 check gave exact eigenvalue proportionality. Therefore, conditionally,

```math
Q_{\mathrm{matter}} \propto Q_propagation \propto Q_HDA.
```

This was already a strong same-spatial-metric result, but a simple one-particle tight-binding dispersion is naturally `z=2`, so it did not by itself provide relativistic matter.

## 28.2 Exact finite z=1 matter from the graph incidence operator - EXACT

Choose any orientation of the graph edges and let `B` be the vertex-edge incidence matrix. For a 6-regular graph,

```math
B B^{T} = 6 I - A = 6 \widetilde L.
```

Define

```math
\widehat B = B / \sqrt{6}
```

and the first-order graph Dirac operator

```math
\begin{aligned}
D_G &= [[0, \widehat B], \\
& [\widehat B^{T}, 0]].
\end{aligned}
```

Then exactly

```math
D_G^{2} vertex block = \widetilde L,
```

so the nonzero vertex-sector matter energies satisfy

```math
E_m^{2} = \lambda(\widetilde L).
```

This is an exact finite `z=1` spectrum using only the relational graph. Edge-orientation flips act by sign conjugation and vertex relabellings by permutation similarity, so the spectrum is independent of arbitrary labels/orientations.

**Status:** EXACT finite construction. This is a kinematic matter carrier, not yet Standard Model matter.

## 28.3 Same incidence operator generates normal-normal closure - EXACT on amorphous graph

Define a smeared normal carrier

```math
\begin{aligned}
K[N] &= [[0, M_N \widehat B], \\
& [\widehat B^{T} M_N, 0]].
\end{aligned}
```

Then on any 6-regular graph,

```math
\begin{aligned}
& [K[N], K[M]]_{\mathrm{vertex}} \\
 &= M_N \widetilde L M_M - M_M \widetilde L M_N,
\end{aligned}
```

while the edge block and off-diagonal blocks cancel.

On the actual parent-generated N=216 amorphous graph:

```math
\begin{aligned}
& ||\widehat B \widehat B^{T} - \widetilde L|| \sim 3.8e-15 \\
& normal-normal block identity error \sim 1.7e-15 \\
& edgewise lapse-wedge error \sim 4.4e-16 \\
& three-normal Jacobi residual \sim 1.7e-15
\end{aligned}
```

On each edge `(u,v)`, the commutator coefficient is exactly proportional to

```text
N_u M_v - M_u N_v.
```

Thus the **same incidence operator** supplies:

```math
\begin{aligned}
z &= 1 matter \\
& propagation Laplacian \\
& normal-normal schedule algebra.
\end{aligned}
```

This is currently one of the strongest same-Q consolidations in GWXP.

---

# 29. Uniform-driver no-go and the soft local rewrite replacement

## 29.1 Uniform all-edge flip driver - KILLED as final driver

The old

```math
V = -\Gamma sum_{i<j} X_ij
```

has `O(N^2)` channels and no geometry-local suppression. Far and local flips enter at the same microscopic order. The vacuum shift scales badly and the model lacks a graph-local Lieb-Robinson-like causal structure.

Therefore this driver is deprecated as the final metric dynamics.

## 29.2 Hard r=3 projector - useful intermediate, no longer fundamental

A Hermitian local projector driver was introduced:

```math
V_r = -\Gamma sum_{i<j} P_ij^{r} X_ij,
```

where the path test excludes the toggled edge. `r=3` was initially used explicitly.

Later work showed a cleaner reason for the appearance of 3:

- distance 1 is already occupied;
- adding a distance-2 edge to a triangle-free graph creates a triangle;
- therefore the **first legal local triangle-free rewrite appears at distance 3**.

So `r=3` can be demoted from a microscopic cutoff to the leading legal order.

## 29.3 Gapped graph mediator gives a soft Hermitian locality hierarchy - DERIVED/NUMERICAL

Let a gapped mediator propagate on occupied links:

```math
\begin{aligned}
R_rho &= (I - \rho A)^{-1} \\
 &= sum_{\ell\ge 0} \rho^\ell A^\ell,
\end{aligned}
```

with `rho < 1/6` for degree 6 stability.

For a 2-switch `G <-> G'`, define the common graph `C = G intersect G'` and use the symmetric amplitude

```math
\begin{aligned}
t_GG' &= \Gamma sqrt[ \\
& R_C(a,b) R_C(c,d) R_C(a,c) R_C(b,d) \\
& ].
\end{aligned}
```

Because the same common graph is used forward and backward, the amplitude is exactly Hermitian under switch reversal.

On N=216 the mediator amplitudes decrease sharply with relational distance. At `rho=0.1`, representative median two-edge weights fell roughly as:

```math
\begin{aligned}
d &= 3 : 1.6e-5 \\
d &= 4 : 1.35e-6 \\
d &= 5 : 3.3e-7 \\
d &= 6 : 8.5e-8.
\end{aligned}
```

Closure/H_mix reweighting still reached numerical isotropy over tested `rho` values roughly `0.05-0.15` with modest KL cost.

**Current interpretation:** no hard radius is required. Triangle-free geometry + ordinary propagator locality makes distance 3 the leading rewrite order while allowing suppressed longer processes.

## 29.4 Triangle frustration remains a genuine microscopic coupling - OPEN naturalness issue

The triangle-free phase is not a mathematical necessity of the rest of the parent. The non-triangle terms at `tau=0` can prefer triangle creation.

However, the triangle penalty is not knife-edge. On sampled unrestricted N=128 moves, triangle-removing/creating directions changed sign around only

```text
tau ~ 0.03-0.06,
```

while the working parent used `tau=5`.

Thus a broad positive triangle-frustration region exists, but `tau>0` remains an actual microscopic coupling unless a deeper derivation is found.

---

# 30. N=343 rank-4 campaign: what survived and what was corrected

This section records the long N=343 attack because several intermediate claims were later corrected.

## 30.1 Cubic crystal is not the end of the graph landscape

The perfect `7^3` cubic torus has the correct low-dimensional spectrum and was locally stable to simple isolated defects. However, an explicit sequence of relational-local, triangle-free 2-switches found a near-flat escape corridor and then crossed below the cubic parent energy.

Along the early corridor:

```text
E_343^cubic ~ -1.761650962
```

and a lower-energy noncrystalline state was found with

```math
\Delta E < 0
```

while a global rank-4 proxy decreased substantially from the cubic value ~0.72 toward ~0.39 and below.

This established that the N=343 crystal is not dynamically isolated under local rewrites.

## 30.2 Raw parent descent does not monotonically isotropize - CORRECTED

Some parent-downhill moves improved `c4`; others made it worse. Across candidate pools, `Corr(Delta E, Delta c4)` became close to zero at depth.

Therefore:

```math
bare parent energy descent != automatic isotropy descent.
```

A separate selector is needed if exact low-energy closure is to remove the spin-4 grain.

## 30.3 c4-penalty trajectories were useful diagnostics but not autonomous proof

A weak diagnostic functional

```math
F = E_parent + \kappa_{cl} c4^{2}
```

showed that `kappa_cl ~ 1e-4` could steer local moves that lowered both parent energy and anisotropy, whereas `1e-3` began trading bare parent energy for isotropy.

This demonstrated that the parent landscape contains nearby isotropizing directions, but `c4` itself cannot be inserted as the final microscopic selector.

## 30.4 Adjacency-only HDA residual is not the isotropy mechanism - KILLED shortcut

A schedule residual based only on the higher-derivative mismatch of the adjacency/Laplacian normal algebra was tested blindly. It did not reliably lower the physical TT kinetic splitting.

Therefore the shortcut

```text
adjacency HDA discretization residual -> isotropic graviton kinetics
```

is killed.

## 30.5 Real kinetic-closure anomaly and estimator-noise correction

The correct object is the kinetic constraint-preservation anomaly of the actual local rewire covariance. Initial per-candidate Monte Carlo reconstructions of `K_eff` were too noisy and produced false wins.

This was corrected using **common-channel before/after estimators**. Individual closure-improving rewires did not correlate strongly with TT improvement:

```math
Corr(\Delta eta_comp, \Delta \epsilon_{TT}) \sim 0
```

over the small robust move sample.

Thus closure and TT isotropy are not identical single-rewire objectives.

## 30.6 Multi-step blind closure trajectory - STRONG NUMERICAL but finite

A blind trajectory was then run using only:

```math
\begin{aligned}
& \Delta E_parent < 0 \\
& \Delta eta_comp < 0
\end{aligned}
```

with no TT/c4 selection.

Over an 8-step run, robust common-channel endpoint diagnostics showed approximately:

```text
eta_comp : 0.0668 -> 0.0219   (~67% reduction)
epsilon_TT : 28.1% -> 17.7%  (~37% reduction)
traceless isotropy residual : 0.2385 -> 0.1286
5D eigenvalue spread : 0.705 -> 0.330
trace-shear mixing : 0.106 -> 0.031
```

while bare parent energy also decreased.

The unguarded trajectory drifted upward in finite-size spectral-dimension estimates, so a hard `d_s` guard was imposed.

## 30.7 Hard-dimension guarded closure descent - PARTIAL SURVIVAL

Two robust guarded steps reduced closure anomaly while keeping approximately the same finite-size dimension window:

```text
eta_comp : 0.02732 -> 0.02086
mean TT split : 14.62% -> 13.46%
```

with negligible dimension drift. The TT tail/eigenvalue spread did not improve uniformly, and further single-rewire progress stalled.

Single-, pair-, and small triple-rewire searches at that point found a real graph-state bottleneck.

**Key interpretation:** the graph should not be forced to change geometry merely to repair the local kinetic tensor. That motivated the H_mix amplitude-reweighting route.

---

# 31. Fixed-graph H_mix: closure can reconstruct DeWitt kinetics without changing geometry

## 31.1 Positive local channel reweighting reaches exact rotational kinetic isotropy - STRONG NUMERICAL

On the stalled fixed N=343 graph, use hundreds of genuine local rewire channels with bare weights `w0_m` and permit only positive amplitude reweighting `w_m`.

The local kinetic covariance is built from the physical unnormalised metric-move tensors. The schedule/mix sector reweights the already available channels; the graph adjacency does not change.

For 600, 800, and 1000 independently sampled channels, exact closure-compatible reweightings exist with modest information cost:

```text
D_KL ~ 0.024-0.036.
```

Typical channel multipliers remain close to one.

After conformal/trace completion, the optimized kinetic map lands numerically on

```math
\begin{aligned}
& \lambda_{0} : \lambda_{1} : ... : \lambda_{5} \\
 &= -0.5 : 1 : 1 : 1 : 1 : 1
\end{aligned}
```

to numerical precision.

This is the DeWitt ray, not merely an isotropic shear block.

## 31.2 Exact isotropy is kinematically accessible with small reweighting

Earlier LP/SLSQP tests on N=128 and N=216 had already shown:

- full `Sym(3)` move span rank 6;
- traceless span rank 5;
- positive reweightings can make the five traceless directions exactly isotropic;
- full rotational mobility with vanishing trace-shear mixing is feasible;
- minimum-KL shifts were small.

The N=343 fixed-graph H_mix result turns that kinematic fact into a closure-selection mechanism.

## 31.3 Closure-anomaly rank and the 19-dimensional bad sector

A self-adjoint kinetic map on the 6-dimensional symmetric-tensor space has 21 components. Rotational invariance leaves exactly two scalar tensors: the trace projector and traceless identity.

Therefore the non-scalar sector has

```math
21 - 2 = 19
```

dimensions.

The real closure-anomaly map on the N=343 move ensemble has rank 19. Its null space coincides, to machine precision, with the two-dimensional SO(3)-scalar kinetic subspace. Principal-angle/projector comparisons were at ~`1e-15` level.

Thus the 19-component selector is not secretly a complicated GR tensor: it is exactly the removal of every non-scalar rotational irrep of the kinetic map.

Representation-theoretically,

```math
Sym^{2}(Sym^{2} R^{03}) = 2 l=0 + 2 l=2 + l=4,
```

so the bad sector is

```math
2 l=2 + l=4
```

with dimension `10+9=19`.

## 31.4 Symmetry-only token dynamics suppresses closure and TT anisotropy - STRONG NUMERICAL

The microscopic schedule-token model was rerun with an interaction defined only as distance from the SO(3)-scalar kinetic subspace, not with `SKZ` or TT/c4 inserted.

A representative result began at roughly

```math
\begin{aligned}
eta_SO3 &= 1 \\
eta_closure &= 1 \\
& \epsilon_{TT} \sim 16.4%
\end{aligned}
```

and evolved toward

```text
eta_SO3 ~ 0.047
eta_closure ~ 0.043
epsilon_TT ~ 0.5%
```

in the finite token simulation.

This removes most of the circularity in the isotropization mechanism.

---

# 32. Why the effective H_mix functional is not an arbitrary regularizer

## 32.1 History multiplicity gives the KL term - DERIVED / finite check

Suppose a coarse schedule block contains `R` microscopic update opportunities. Before closure acts, each token chooses local channel `m` with bare probability `w0_m`. A coarse block records only empirical frequencies `w_m`.

The number/weight of microscopic histories realizing `w` is multinomial. By the method of types,

```math
P_0(w) \sim \exp[-R D_KL(w || w0)].
```

Therefore the relative-entropy term arises from microscopic history multiplicity rather than being inserted as an optimization aesthetic.

A reduced finite history enumeration built from actual N=343 anomaly classes approached the continuum saddle predicted by the KL functional as the number of schedule tokens increased, with expected finite frequency quantization.

## 32.2 Schedule holonomy supplies the anomaly-square energy - DERIVED from existing autonomous schedule Hamiltonian

The old autonomous schedule diamond used

```math
H_diamond = J_x(I-W_x) + J_y(I-W_y),
```

with a finite positive gap and zero-frustration ground states invariant under the loop holonomy.

For a small loop

```math
G_loop = \exp[i \epsilon^{2} A + \mathcal{O}(\epsilon^{3})],
```

schedule frustration bounds the energy by a positive quadratic function of the holonomy mismatch. Thus the low-step effective cost contains

```text
~ epsilon^4 A^2.
```

Therefore the effective variational structure

```math
F[w] = D_KL(w||w0) + \kappa ||A(w)||^{2}
```

has identifiable microscopic origins:

```text
history multiplicity -> KL
schedule frustration -> anomaly square.
```

## 32.3 Optimized weights are low-dimensional collective tilts, not hundreds of knobs

For the real 800-channel N=343 ensemble,

```math
\log(w_m/w0_m) = c - \lambda dot g_m
```

fit the exact optimized weights with `R^2` numerically 1 and residual ~`1e-14`.

Thus the many channel-weight changes are generated by the small collective closure/anomaly coordinates, not by channel-by-channel tuning.

## 32.4 Microscopic token Monte Carlo reproduces the reweighting without an optimizer - NUMERICAL

With thousands of schedule tokens, equal bare channel fugacity, and only the collective schedule/closure interaction, the empirical channel frequencies spontaneously reweight.

Representative 10,000-token runs reduced closure anomaly from order one to ~`0.06` and TT splitting from ~`16%` to ~`3%`.

A coupling sweep showed a broad monotonic response rather than a knife-edge tuned point.

## 32.5 Quantum/Hartree variant - EXPLORATORY / cutoff-recovered

A later cutoff-era calculation replaced the classical KL form with a quantum amplitude/fidelity kinetic cost on a local N=216 ball. Minimizing

```text
1 - |<sqrt(w0)|psi>|^2 + kappa ||A(|psi|^2)||^2
```

converged from multiple initial states to the same Hartree stationary solutions.

Representative local results:

```math
\begin{aligned}
\kappa &= 0.1: eta/raw ~0.329, KL ~0.0226, shear spread ~1.08 \\
\kappa &= 1:   eta/raw ~0.119, KL ~0.0672, shear spread ~0.526 \\
\kappa &= 10:  eta/raw ~0.0266, KL ~0.140, shear spread ~0.136
\end{aligned}
```

This is not yet a preferred microscopic derivation; finite-token corrections can be large for small token populations. Preserve it as an exploratory quantum completion, not a core result.

---

# 33. Removing the prescribed scalar constraint: symmetry + schedule selects DeWitt

This branch is one of the most important post-rollover upgrades.

## 33.1 Spatial gauge symmetry uniquely fixes the two-derivative scalar - DERIVED / exhaustive finite support

For the most general rotational two-derivative scalar

```math
C = a d_i d_j h_ij + b nabla^{2} h,
```

spatial gauge invariance forces

```math
a + b = 0,
```

leaving, up to normalization,

```math
C \propto d_i d_j h_ij - nabla^{2} h,
```

i.e. the linearized spatial-curvature scalar.

In the three-site Z5 regulator, exhaustive enumeration of all `5^6 = 15625` coefficient vectors at `k || x`, with gauge and transverse little-group symmetry, left only

```text
0 and a(0,1,1,0,0,0)
```

for nonzero `a`.

Thus the finite scalar form was **recovered from symmetry**, not inserted as a gravitational stabilizer.

## 33.2 Normal-normal closure selects the DeWitt ray - EXACT FINITE

Use the generic isotropic kinetic update

```math
\delta h_ij = \alpha \pi_{ij} + \beta \delta_{ij} \pi.
```

On the three-site Z5 regulator, exhaustively test all 15,625 lapse pairs.

The only nonzero coefficient pairs that close for all lapse pairs are

```text
(1,2), (2,4), (3,1), (4,03) mod 5,
```

which are precisely the nonzero multiples of

```math
\alpha + 2 \beta = 0.
```

Wrong rays close only on the trivial/special lapse directions.

A separate all-momentum test over all 124 nonzero `k in Z5^3` again leaves the same ray; wrong choices pass only special finite-field null directions.

**Upgrade relative to V5.14/V5.15:** the scalar form is no longer assumed as a prescribed stabilizer in this derivation.

## 33.3 Exact finite lapse-wedge bridge

For the three-site ring, the coefficient generated by the normal-normal bracket satisfies exactly

```math
q = N (L M) - M (L N) = D^{T} \xi,
```

where

```math
\xi_{x} = N_x M_{x+1} - M_x N_{x+1}.
```

This is the same discrete lapse wedge previously generated by the autonomous schedule diamond.

The identity had zero failures over all 15,625 lapse pairs.

## 33.4 Wrong kinetic rays reduce the schedule-invariant physical fiber - EXACT FINITE

On the 18 finite metric registers of the three-site regulator:

```math
\begin{aligned}
spatial gauge rank &= 6 \\
spatial-gauge-invariant configuration exponent &= 18-6 = 12.
\end{aligned}
```

For wrong `alpha+2 beta`, schedule-loop holonomies introduce two additional non-gauge transverse translations, reducing the invariant fiber from

```text
5^12 -> 5^10.
```

That is a factor 25 loss of protected state capacity per regulator block, now derived from schedule holonomy + spatial gauge without separately inserting the scalar stabilizer.

## 33.5 Generic frame stiffness converts the capacity selection into zero-temperature energy selection - STRONG FINITE NUMERICAL

A minimal finite frame/schedule Hamiltonian was built with:

- a physical transverse frame register;
- a generic gapped frame Hamiltonian;
- two schedule registers whose loop shifts the physical frame coordinate by

```math
r = \alpha + 2 \beta.
```

At the DeWitt ray `r=0`, frame ground state and schedule zero-frustration coexist exactly at zero energy.

For wrong branches, the schedule loop translates a physical gapped frame coordinate, creating unavoidable frustration.

At equal couplings in the simplest toy:

```math
\begin{aligned}
E0(r &= 0)=0 \\
E0(r &= 1,04) ~0.8822 \\
E0(r &= 2,03) ~0.9268.
\end{aligned}
```

The selection persisted over a broad coupling sweep and across 30 randomized generic frame Hamiltonians (diagonal and dense Hermitian), producing 840/840 strictly positive wrong-branch tests.

**Status:** strong finite autonomous selection mechanism, still not a thermodynamic many-cell phase proof.

---

# 34. Finite coefficient lock and shared clock with matter

## 34.1 Gravity coefficient lock - EXACT FINITE

After selecting the DeWitt shape, write the normal Hamiltonian schematically as

```math
H[N] = A K[N] - B R[N].
```

Scanning all `(A,B) in Z5^2` over all 15,625 lapse pairs, the only nonzero fully matching pairs satisfy

```math
A B = 1 mod 5.
```

This is the finite version of the continuum HDA coefficient lock.

## 34.2 Matter bracket and shared schedule clock - EXACT FINITE

For a canonical finite scalar matter edge Hamiltonian with temporal coefficient `a` and gradient coefficient `b`, the exact bracket is

```math
\begin{aligned}
& {H_m[N],H_m[M]} \\
 &= a b (N_x M_y - M_x N_y) D_m,
\end{aligned}
```

where `D_m` is the discrete matter spatial-translation generator.

Exhausting all matter states, all lapse pairs, and all finite coefficient pairs selects

```math
a b = 1 mod 5.
```

Therefore one common schedule clock forces

```math
A B = a b = 1,
```

rather than allowing independent rescalings of gravity and matter time.

Combined with the same graph Laplacian/incidence operator, this is the strongest current common-cone result.

---

# 35. Local polygonal cell structure and Hodge repair of the matter edge kernel

## 35.1 Naive graph Dirac has an extensive edge-cycle kernel - real obstruction

For a connected graph, the raw incidence Dirac operator has an edge-cycle kernel of dimension

```text
E - N + 1.
```

For degree-6 N=343 this is 687 unwanted edge zero directions. They cannot simply be ignored.

## 35.2 Parent graphs contain enough short local cycles to act as 2-cells - NUMERICAL

On the independent parent states:

```math
\begin{aligned}
N &= 128: cycles of length \le 6 span 257/257 cycle directions. \\
N &= 216: rank progression \\
L &= 4:   338 \\
& L\le 5:  364 \\
& L\le 6:  417 \\
& L\le 7:  433/433.
\end{aligned}
```

On the torus-descended N=343 state, squares alone had rank 684 of 687, leaving the expected three toroidal global cycles, but this was correctly treated as ancestry-dependent rather than spontaneous topology evidence.

## 35.3 Local all-face curl penalty avoids global basis selection - DERIVED/NUMERICAL

Rather than selecting an independent global cycle basis, use every available local short cycle `c` as a curl penalty on the edge sector:

```math
\begin{aligned}
H_curl &= \sum_{c} \mu_{c} Q_c^{\dagger} Q_c, \\
& \mu_{c} > 0.
\end{aligned}
```

Because cycle boundaries lie in `ker B`, the curl term annihilates the vertex-gradient branch exactly and therefore leaves

```math
E_{\mathrm{vertex}}^{2} = \lambda(\widetilde L)
```

unchanged.

Its zero space depends only on the span of the local cycles, not on the individual positive weights.

This works dynamically if the face term is activated by the edge-occupation product for the loop, so the cell structure follows graph rewiring.

## 35.4 Fixed length <=7 was later demoted - CORRECTED

A fixed `ell<=7` face rule passed all archived N=128/216 states and many N=343 rewires, but one independently generated N=344 basin required length-8 loops to span its full cycle space.

Therefore:

```math
universal hard face cutoff \ell\le 7
```

is demoted.

The natural replacement is a soft local loop hierarchy, e.g.

```math
\mu_{\mathrm{ell}} \propto \rho_{f}^{\ell-\ell_{\mathrm{min}}}.
```

However, a rigorous basis lower-bound test showed that the curl gap can become extremely small when the shortest cycle basis drifts to longer loops. Representative lower bounds were as small as `~1e-7` for one N=344 state at `rho_f=0.1`.

**Current matter status:** finite-size z=1 matter construction is strong; a healthy thermodynamic curl gap is OPEN.

---

# 36. Dynamical Q survived increasingly hard tests

## 36.1 Classical moving-frame groupoid - EXACT FINITE toy

When a normal update also moves the frame variable, a midpoint-controlled schedule connection gives pairwise commutators with the expected leading `Q(q)` lapse-wedge term plus next-order frame-motion corrections.

The algebra becomes class-3 nilpotent rather than the fixed-Q class-2 central extension.

In a three-direction finite Z5 version, individual nested commutators are nonzero but the cyclic Jacobi sum cancels exactly. A finite test over 78,125 state/update combinations had zero Jacobi failures.

## 36.2 Noncommuting quantum relational frames close internally - DERIVED/NUMERICAL

For normalized frame legs `E=J/S`, define

```math
\begin{aligned}
q_12 &= E_1 dot E_2, \\
q_23 &= E_2 dot E_3, \\
q_31 &= E_3 dot E_1, \\
\chi &= E_1 dot (E_2 x E_3).
\end{aligned}
```

Then

```math
[q_12,q_23] = -(i/S) \chi.
```

Further commutators close quadratically inside the same rotational scalar frame algebra. For example,

```math
\begin{aligned}
& i[q_12,\chi] \\
 &= ((S+1)/S^{2})(q_31-q_23) \\
&\quad + (1/(2S)){q_12,q_31-q_23},
\end{aligned}
```

with cyclic analogues. Matrix-fit residuals were ~`1e-15` for several spins.

Thus operator-valued Q generates controlled internal frame/chirality corrections rather than uncontrolled new operators.

## 36.3 Classical limit and block classicality - DERIVED

The schedule-loop correction scales as

```text
~ epsilon^2/S.
```

For a block average of `n` independent local frames,

```math
[bar q_12, bar q_23] = -(i/(S n)) bar \chi.
```

So the effective quantum-frame parameter is

```text
hbar_frame_eff ~ 1/(S n).
```

No ferromagnetic global frame alignment is required. This is compatible with the amorphous/statistically isotropic route, and quantum frame noncommutativity decays faster (`~n^-1`) than ordinary orientation grain (`~n^-1/2`).

## 36.4 Moving actual graph sectors - EXACT finite operator check

For genuine N=216 local 2-switches:

```math
\begin{aligned}
& \Delta B has rank 1 or 2 and support on touched vertices. \\
& \Delta \widetilde L has rank 2.
\end{aligned}
```

In a two-geometry sector `G <-> G'`, the three moving-graph Jacobi terms were individually nonzero (norms about `0.380, 0.426, 0.579` in one test) yet cancelled to machine zero.

The variation of the spatial generator is exactly

```math
\begin{aligned}
& \delta D[N,M] \\
 &= M_N \delta \widetilde L M_M - M_M \delta \widetilde L M_N,
\end{aligned}
```

with local finite-rank support.

This is a concrete finite analogue of field-dependent structure functions whose Jacobi identity requires the metric to transform.

---

# 37. Exact identity fusing metric rewrites with propagation/HDA

For any three local coordinate/frame functions collected in `X`, the graph Dirichlet form is

```math
\begin{aligned}
& X^{T} \widetilde L X \\
 &= (1/06) \sum_{<uv>} (X_u-X_v)(X_u-X_v)^{T}.
\end{aligned}
```

For a genuine 2-switch `m`,

```math
6 X^{T} (\Delta \widetilde L_m) X = \delta h_m,
```

where `delta h_m` is exactly the physical unnormalised metric-move tensor used in the kinetic/DeWitt calculations.

This identity was verified on 30 N=216 rewires with maximum relative error ~`3e-16`.

Therefore the effective supermetric can be written as the covariance of local Laplacian fluctuations:

```math
\begin{aligned}
& K_{\mathrm{eff}} proportional to \\
& \sum_{m} w_m vec(X^{T} \Delta \widetilde L_m X) \\
& vec(X^{T} \Delta \widetilde L_m X)^{T}.
\end{aligned}
```

This is one of the deepest current consolidations:

```text
Delta B
  -> Delta Ltilde
  -> schedule/spatial-generator variation
  -> physical metric move delta h
  -> K_eff.
```

Gravity's kinetic tensor is the statistics of fluctuations of the same relational Laplacian that governs propagation.

---

# 38. Locality of the H_mix mechanism

The global H_mix reweighting could have cheated through cancellations between distant anisotropic regions. This was attacked with local graph balls.

Using purely local radius-R subgraph data and local diffusion frames:

```math
\begin{aligned}
R &= 2: local exact isotropization usually fails. \\
R &= 3: local positive reweighting succeeds robustly.
\end{aligned}
```

Representative exact LP checks:

```text
N=343: R=2 -> 0/20, R=3 -> 20/20
N=128: R=3 -> 8/8
N=216: R=3 -> 8/8
```

The local token Monte Carlo, with equal bare fugacity and no global optimizer, also reduced local rotational-frustration and local shear eigenvalue spread inside independent R=3 balls.

A global spectral embedding is not required: induced radius-3 subgraph diffusion frames also support the local isotropic move cone.

**Interpretation:** the DeWitt-compatible kinetic freedom exists neighborhood by neighborhood. The mechanism is not relying on distant cancellation.

The repeated appearance of the scale 3 is now understood primarily as the first legal local triangle-free rewrite order, not as a fundamental hard cutoff.

---

# 39. N=344 third-size basin evidence before the cutoff

## 39.1 Independent externally seeded amorphous basins - STRONG basin-existence evidence, not autonomous discovery

Two independent N=344 3D amorphous seeds were generated using coordinates only to propose the initial graphs; all parent energies were then evaluated from adjacency alone. Short parent-only relaxation lowered them to approximately:

```math
\begin{aligned}
E_344^{01} &= -1.76249817 \\
E_344^{02} &= -1.76246708
\end{aligned}
```

with 3D-like finite heat-kernel profiles.

The seeds prove that the parent contains a competitive N~344 amorphous 3D basin. They do not prove the parent can discover that basin from a generic graph because their initialization used external coordinates.

## 39.2 Three-size energy scaling - STRONG NUMERICAL diagnostic

Using the N=128, N=216, and mean N=344 basin energies, a fit

```math
E_N = E_inf + a/N
```

gave approximately

```text
E_inf ~ -1.761832
R^2 ~ 0.9983
```

with residuals at the few `1e-5` level.

Relative to the analytic infinite cubic `Z^3` energy at the old parameter point,

```math
E_Z3,inf = -1.7617424011,
```

the quantity

```text
N(E_N - E_Z3,inf)
```

was roughly

```text
-0.249, -0.255, -0.255
```

for N=128,216,344.

This is striking finite-size basin scaling, but later rank-2 adversaries change the interpretation of the old parameter point; see Section 40.

## 39.3 Random expander phase is much higher in energy

Generic triangle-free N=344 6-regular graphs sat near

```text
E/N ~ -1.750,
```

about `0.0125` per vertex above the low-dimensional basin. Random regular graphs with triangles were worse once the triangle penalty was included.

Thus failure to find the low-dimensional basin from a random start is primarily a **landscape/nucleation problem**, not evidence that the random phase is energetically competitive.

---

# 40. CUTOFF-RECOVERED RESULTS: relation condensation and the new phase correction

**Provenance:** the previous chat timed out immediately after the instruction to continue and to recheck existing research for clues to the nucleation mechanism. The runtime retained the scripts/snapshots. The following calculations were recovered and rerun after the cutoff; they were never posted in the previous chat.

This section supersedes any earlier statement that the old `g=3, U=0.106, kappa=0.08` point is already a secure 3D global phase.

## 40.1 Generic triangle-free N=344 starting state

A coordinate-free generic triangle-free 6-regular N=344 graph was constructed as the bipartite double cover of a random 6-regular graph:

```math
\begin{aligned}
E_start &= -1.7502717391 \\
C4/N &= 0.494186 \\
& heat d_s(05) \sim 4.52 \\
& heat d_s(10) \sim 4.33
\end{aligned}
```

This is an expander-like high-dimensional/disordered starting geometry.

## 40.2 The parent has a direct local energetic drive to create 4-cycles - STRONG NUMERICAL

At that generic state, a 120-move exact sample gave

```math
Corr(\Delta C4, \Delta E) = -0.99178.
```

Every sampled move with `Delta C4 > 0` was downhill in parent energy. Representative means:

```math
\begin{aligned}
\Delta C4 &= +1 \to mean \Delta E \sim -1.85e-5 \\
\Delta C4 &= +2 \to mean \Delta E \sim -3.33e-5 \\
\Delta C4 &= +3 \to mean \Delta E \sim -4.89e-5 \\
\Delta C4 &= +4 \to mean \Delta E \sim -6.46e-5.
\end{aligned}
```

Strongest sampled moves reached `Delta C4=+6` with

```math
\Delta E \sim -9.59e-5.
```

This is the first clear microscopic nucleation clue:

```text
communicability/spectral parent energy directly rewards local relation/4-cycle formation
inside a generic triangle-free expander.
```

## 40.3 Unbiased zero-temperature parent descent spontaneously condenses relations - MAJOR RECOVERED RESULT

Crucially, the effect does not require square-guided acceptance.

A blind zero-temperature walk accepted **only `Delta E_parent < 0`**, with no dimension, square, curvature, or isotropy term in the acceptance rule.

The trajectory evolved roughly:

```math
\begin{aligned}
start:        E &= -1.750272, C4/N=0.494 \\
200 attempts: E &= -1.753740, C4/N=1.108 \\
500 total:    E &= -1.756045, C4/N=1.570 \\
950 total:    E &= -1.757749, C4/N=1.974 \\
1250 total:   E &= -1.758523, C4/N=2.157 \\
2000 total:   E &= -1.759842, C4/N=2.497.
\end{aligned}
```

The heat-kernel dimension simultaneously drifted downward from strongly expander-like values:

```text
d_s(5): 4.52 -> 3.92 by the 2000-attempt state
d_s(10):4.33 -> 3.92.
```

This is not yet the mature `d~3` basin, but it demonstrates **autonomous relation condensation under the original parent energy** from a generic triangle-free graph.

This is currently the strongest clue to the missing “parent discovers locality” mechanism.

## 40.4 Relation-guided path shows a continuous energetic valley toward the 3D-like basin

A diagnostic path that screened candidate moves by largest `Delta C4` but accepted only if the exact parent energy fell produced:

```text
C4/N : 0.494 -> 0.936 -> 1.311 -> 1.686 -> 2.070 -> 2.477
       -> 2.823 -> 3.218 -> 3.532 -> 3.849 -> 4.183 -> 4.445 -> 4.596

E/N  : -1.75027 -> ... -> -1.762828.
```

At the `C4/N ~4.60` endpoint:

```text
gap ~0.1024
d_s(03) ~3.19
d_s(05) ~3.30
d_s(10)~3.17.
```

The path therefore exhibits a continuous relation-condensation valley from a generic expander toward a finite-dimensional 3D-like graph.

Because the candidate proposal screening used `Delta C4`, this path is a **mechanism diagnostic**, not autonomous-discovery proof. The unbiased walk above is the key autonomous evidence.

## 40.5 Local neighborhood growth contracts as relation density rises - mechanism clue

Independent N=128 and N=216 relation-condensation walks show the same qualitative trend: as `C4/N` increases and energy falls, radius-2/radius-3 balls contain fewer distinct vertices.

Examples:

```text
N=128:
C4/N 1.56 -> 2.65
mean |B_2| 31.38 -> 28.42
mean |B_3| 83.31 -> 75.64

N=216:
C4/N 0.741 -> 1.352
mean |B_2| 34.20 -> 32.29
mean |B_3| 112.95 -> 105.18.
```

Interpretation: short-cycle condensation creates repeated relational paths, reducing the exponential neighborhood growth of the random regular phase and driving the graph toward polynomial/local geometric growth.

## 40.6 Square growth is not simple local autocatalysis - CORRECTED mechanism detail

A test of whether new squares preferentially form where squares already exist found the opposite tendency.

At an early N=344 nucleation state:

```math
Corr(\Delta C4, local square participation) \sim -0.528.
```

Square-gaining moves occurred in **less square-rich** supports than square-losing moves.

Therefore the mechanism is not “squares seed more squares locally” in a naive autocatalytic sense. It looks more like **homogenizing relation condensation**: the parent preferentially fills locally under-looped regions.

## 40.7 Pairwise nucleation synergy is tiny - CORRECTED

For 89 pairs of individually downhill square-creating moves, the nonlinear pair synergy was extremely small:

```text
mean synergy ~ 2.1e-7
negative fraction ~0.45
range about -7.6e-7 to +1.68e-5.
```

At support separation 2-3 the mean synergy was approximately zero.

Thus the condensation is primarily an **additive local energetic drive**, not a strong two-move cooperative attraction.

## 40.8 Phenomenological Landau-like order parameter - NUMERICAL clue

Combining N=128, 216, and 344 relation-condensation histories, the old-parameter energy is remarkably well fit by

```math
E(N,c) \sim E0 + a/N + b c + q c^{2},
```

where `c = C4/N`.

Recovered fit:

```math
\begin{aligned}
& E0 \sim -1.7476669 \\
& a  \sim  0.0192003 \\
& b  \sim -0.0057279 \\
& q  \sim  0.0005175 \\
& R^{2} \sim 0.99724 \\
& RMSE ~2.26e-4 \\
c_star &= -b/(2q) ~5.53.
\end{aligned}
```

Allowing mild `1/N` corrections to the `c` coefficients improves `R^2` to ~`0.99918`.

Interpretation: at the old parameter point the parent behaves like a relation-condensation free-energy landscape with a preferred short-cycle density near `C4/N ~5.5`.

This immediately leads to the most important recovered correction below.

## 40.9 MAJOR CORRECTION: a rank-2 Cayley competitor beats the old 3D point

A broader adversary search constructed triangle-free degree-6 rank-2 Cayley graphs, not just simple compactified product tori.

For one generator choice, the large finite values are approximately:

```text
C4/N = 6
E/N ~ -1.76358
heat d_s(05) ~2.83
heat d_s(10)~2.19.
```

This is lower than the old N=128/216/344 3D-like candidates at

```math
g=3, U=0.106, \kappa=0.08.
```

Therefore the previous claim that this exact parameter point is a secure 3D global phase is **DEMOTED/KILLED**.

The older product-compactification checks were insufficient because this non-product rank-2 competitor was not in that adversary set.

This correction must not be lost.

## 40.10 Existing analytic product competitors are still useful but incomplete

At the old point, infinite `Z^3` beats simple `Z^2 x C_m` and `Z x C_m x C_n` product compactifications, with the gap closing as the compact cycles become very large. That result remains correct.

What changed is that a more general rank-2 Cayley geometry with a different local generator set can beat both those products and the 3D candidate.

So dimensional adversaries must include **general low-rank Cayley/periodic graphs**, not only orthogonal product geometries.

## 40.11 Capacity term provides the saturation pressure - NUMERICAL clue

Across N=344 relation-condensation trajectories, the capacity contribution is very accurately described by a convex function of short-cycle density.

A simple quadratic fit of the capacity term versus `c=C4/N` had

```text
R^2 ~0.99971.
```

Adding a variance measure of edge closed-walk participation improved the fit modestly (`R^2 ~0.99981`) with a positive variance coefficient.

This suggests a concrete mechanism:

```text
communicability term -> rewards short closed-walk/relation formation
capacity term         -> penalizes concentration/excess channel reuse
competition           -> finite preferred relation density.
```

At the old couplings the preferred density is too high and approaches the rank-2 competitor. Retuning the balance may place the minimum in the 3D amorphous range.

## 40.12 Reaction-coordinate scan: increasing U moves the preferred relation density downward

Re-evaluating the same N=344 condensation path at fixed `g=3,kappa=0.08` shows that as `U` rises, the energy minimum shifts from the most condensed endpoint toward intermediate `C4/N`.

For example:

```math
\begin{aligned}
& U \le ~0.110 : best among sampled path states remains C4/N ~4.596 \\
U &= 0.112 : best sampled path state moves to C4/N ~3.85.
\end{aligned}
```

This supports the Landau picture, but by itself does not establish a 3D global phase because rank-2 and cubic competitors must be reevaluated simultaneously.

## 40.13 New candidate parameter window where the amorphous relation-condensed state beats rank-2 and cubic controls - CONDITIONAL NUMERICAL

A scan at `g=3` re-evaluated the N=344 relation-condensed states against both:

- the rank-2 Cayley competitor;
- the cubic `Z^3` control.

A finite window appears at **larger determinant/spectral regularization kappa and slightly lower U**. Representative top scan points include:

```math
\begin{aligned}
\kappa &= 0.40, U=0.1020: \\
& amorphous C4/N~4.596 beats both controls by margin ~7.15e-4 \\
\kappa &= 0.35, U=0.1030: \\
& margin ~6.25e-4 \\
\kappa &= 0.30, U=0.1040: \\
& margin ~5.36e-4 \\
\kappa &= 0.25, U=0.1050: \\
& margin ~4.46e-4.
\end{aligned}
```

The scan found 155 tested parameter pairs where a relation-condensed amorphous state with `3 <= C4/N <=5` beat both rank-2 and cubic controls.

**Critical caveat:** these graphs were generated under the old couplings and merely re-evaluated at the new couplings. The new window is therefore a **candidate phase region**, not a demonstrated autonomously generated phase. It needs fresh parent-only annealing/nucleation from generic graphs at the new parameters.

This is now the highest-priority graph-phase experiment.

## 40.14 Ollivier-curvature proxy along the condensation path - NUMERICAL clue, convention-specific

A simple edge Ollivier-style transport proxy moved from strongly negative in the generic expander toward less negative values as relation density increased:

```text
generic start mean ~ -1.13
blind parent-only 2000 state ~ -0.70
relation-condensed C4/N~3.85 state ~ -0.56
relation-condensed C4/N~4.60 state ~ -0.50
externally seeded 3D state ~ -0.44
regular rank-2/cubic controls in this convention ~0.
```

Do not overinterpret the absolute values; the implementation uses a specific neighbor-measure convention. The qualitative trend supports the picture that relation condensation drives the random negative-curvature/expander geometry toward a flatter finite-dimensional phase.

---

# 41. Literature clue scan recovered at rollover boundary

The user explicitly requested that existing research be rechecked for clues to the nucleation mechanism. A focused scan after the timeout found strong prior-art parallels that must be acknowledged.

## 41.1 Quantum Graphity - established close analogue

Konopka, Markopoulou and Smolin/Severini developed background-independent dynamical graph models in which a highly connected/disordered graph can undergo a low-energy transition to an ordered, low-dimensional, local graph phase.

Key references:

- T. Konopka, F. Markopoulou, L. Smolin, **Quantum Graphity**, arXiv:hep-th/0611197.
- T. Konopka, F. Markopoulou, S. Severini, **Quantum Graphity: a model of emergent locality**, arXiv:0801.0861.
- F. Caravelli, F. Markopoulou, **Properties of Quantum Graphity at Low Temperature**, arXiv:1008.1340.

This means the broad idea “dynamical graph -> low-dimensional locality” is not novel to GWXP.

## 41.2 Combinatorial Quantum Gravity - especially relevant mechanism clue

Trugenberger and collaborators developed random-regular-graph models driven by combinatorial/Ollivier-Ricci curvature in which **short-cycle condensation** drives a transition from random graphs to geometric phases.

Key references:

- C. A. Trugenberger, **Combinatorial Quantum Gravity: Geometry from Random Bits**, arXiv:1610.05934.
- C. Kelly, C. A. Trugenberger, **Combinatorial Quantum Gravity: Emergence of Geometric Space from Random Graphs**, arXiv:1811.12905.
- C. A. Trugenberger, **Combinatorial quantum gravity and emergent 3D quantum behaviour**, arXiv:2311.17526.

This is extremely relevant to the recovered GWXP relation-condensation mechanism:

```text
random regular/expander-like graph
 -> condensation of short cycles
 -> reduced neighborhood growth / geometric phase.
```

GWXP's potentially distinctive question is not the existence of cycle condensation itself, but whether its **communicability + capacity + schedule/closure architecture** yields the required 3D relational phase and then ties the same Laplacian fluctuations to matter, HDA, DeWitt kinetics, and refoliation.

## 41.3 Ollivier curvature literature

Ollivier/Lin-Lu-Yau curvature on regular graphs is tightly related to short local cycle structure and transport between neighbor measures. Recent work gives explicit curvature formulae for regular graphs and girth-four cases.

Do not claim the GWXP Ollivier proxy or cycle-condensation observation as novel without a dedicated literature comparison.

## 41.4 Mechanism hypothesis suggested by both our numerics and prior art

The strongest present mechanism hypothesis is:

```text
1. Positive triangle frustration removes d=2 shortcut structure.
2. The communicability term strongly rewards creating local alternative paths /
   short even cycles in an expander-like graph.
3. Relation condensation reduces local exponential ball growth and moves the
   graph away from random negative-curvature/expander behavior.
4. The capacity term penalizes excessive/concentrated closed-walk traffic,
   producing a finite preferred relation density rather than total collapse.
5. The determinant/spectral term controls long-wavelength connectivity and can
   shift the competition against low-rank compactified/Cayley competitors.
6. In the correct coupling window the resulting disordered finite-correlation
   geometry may sit between the expander and crystalline/rank-2 phases.
```

This is the mechanism the next chat should attack directly.

---

# 42. Updated compact parent architecture and what is still hand-chosen

A cleaner minimal gravity-side family can now be organized schematically as

```math
\begin{aligned}
H_{\mathrm{total}} &= H_{\mathrm{graph}}[A] \\
&\quad + H_{\mathrm{med}}[A,\chi] \\
&\quad + H_{\mathrm{sched}}[B(A)] \\
&\quad + H_{\mathrm{mix}}[\Delta B, \Delta L].
\end{aligned}
```

with a matter/cell sector built from the same incidence complex.

Interpretation:

- `H_graph[A]` selects degree, triangle frustration, and the geometric graph phase through communicability/capacity/spectral competition.
- `H_med` is a gapped local graph mediator producing soft Hermitian rewrite amplitudes, replacing the hard radius cutoff.
- `H_sched[B(A)]` uses the incidence operator as the local normal/schedule carrier.
- `H_mix` penalizes non-scalar rotational charge of local `Delta L` fluctuation statistics through autonomous schedule frustration/history weighting.
- matter uses the same normalized incidence operator for an exact finite `z=1` branch.
- local cycle/curl terms remove the spurious edge-cycle kernel when the graph supplies sufficient local 2-cell structure.

No hard `r`, external coordinates, explicit `c4` target, `SKZ` tensor, DeWitt coefficient, or independent inverse-metric register is required in the current candidate architecture.

What remains genuinely microscopic/assumed:

1. degree-6 valence phase;
2. positive triangle frustration;
3. communicability/capacity/determinant graph-selection functional and its coupling region;
4. existence of a generic rotational schedule-frustration sector;
5. local finite quantum frame/process degrees from which the effective graph/incidence description descends.

The next compression phase should ask which of these can be derived from still fewer primitive rules.

---

# 43. CURRENT DECISIVE TARGET - START NEXT RESEARCH PASS HERE

The highest-priority problem changed at the cutoff.

The old `g=3,U=0.106,kappa=0.08` point is no longer a safe final phase because a rank-2 Cayley competitor beats it. At the same time, the cutoff recovery gave the first concrete autonomous nucleation mechanism: **blind parent descent spontaneously condenses short relations/4-cycles from a generic triangle-free graph and reduces effective neighborhood growth.**

The next pass should therefore attack the mechanism and the new parameter window, not return to N=343 closure tuning.

## 43.1 Primary experiment: fresh autonomous nucleation in the new rank-2-safe window

Choose representative candidate points from the recovered scan, e.g.

```math
\begin{aligned}
(g, \kappa, U) &= (3, 0.30, 0.104) \\
& (3, 0.35, 0.103) \\
& (3, 0.40, 0.102)
\end{aligned}
```

with the same degree/triangle structure.

For N=128, 216, and if feasible 344:

1. Start from **generic unrestricted or generic triangle-free random regular graphs**, not coordinate-generated 3D seeds.
2. Use only the parent energy for acceptance. No C4, dimension, curvature, or isotropy steering.
3. Track at short intervals:

```text
E/N
triangle count
C4/N and other short-cycle densities
ball growth B_r
heat-kernel d_s(t) against same-size lattice controls
spectral gap/IDOS
Ollivier-style curvature proxy
orientational/rank-4 diagnostics only after a low-dimensional basin appears.
```

4. Compare against explicit adversaries at the same couplings:

```text
rank-2 Cayley graphs
Z3 / cubic tori
compactified product graphs
random regular/expander graphs
square-rich/crystalline graphs
other low-rank Cayley generator sets.
```

**Success criterion:** unbiased parent dynamics repeatedly nucleates a disordered finite-dimensional basin that beats all known adversaries and whose finite-size observables stabilize across N.

**Kill criterion:** the dynamics converges to rank-2/crystalline/other lower-dimensional competitors, or the apparent amorphous minimum disappears when adversaries are broadened.

## 43.2 Derive the relation-condensation reaction coordinate from the parent terms

Do not merely observe `C4` correlation. Analytically/semianalytically expand the parent energy around a random triangle-free degree-6 graph in local 2-switch directions and identify why the leading coefficient of `Delta C4` is negative.

Target a decomposition like

```math
\begin{aligned}
& \Delta E \\
 &= -a \Delta C4 \\
&\quad + b \Delta(local closed-walk concentration) \\
&\quad + c \Delta(long-wave spectral term) \\
&\quad + higher motifs.
\end{aligned}
```

Then determine whether the capacity/determinant pieces generate a stable finite-density minimum analogous to the empirical Landau fit.

A particularly useful test is whether the coefficients predict the location of the new rank-2-safe amorphous window before annealing.

## 43.3 Broaden the low-dimensional adversary family

The rank-2 Cayley surprise proves the adversary set was too narrow.

Systematically scan degree-6 Abelian/Cayley graphs of ranks 1,2,3 with multiple generator choices and large finite periods. Also include non-Abelian/semidirect regular graph families if cheap.

The parent cannot claim 3D selection until the amorphous basin is below these structured low-rank phases.

## 43.4 Thermodynamic scaling after a genuinely autonomous third size

The coordinate-seeded N=344 basins are useful existence evidence but are not enough.

A fresh autonomously nucleated N~344 state in the new coupling window should be used for:

```text
energy-density scaling
heat-kernel spectral-dimension scaling
ball-growth/Hausdorff scaling
orientation-correlation scaling
rank-4 physical kinetic scaling
local H_mix feasibility
matter-cell curl-gap scaling.
```

Do not fit exponents from two sizes.

## 43.5 Matter thermodynamic curl gap remains open

The exact incidence z=1 matter branch survives. The unresolved issue is whether local polygonal face penalties remain uniformly gapped as N grows without a hand-set face-length cutoff.

Test local cycle-basis length distributions and weighted curl gaps on genuinely autonomous basins across sizes. If the required loop length grows with N and the gap collapses, the current Hodge matter completion fails.

## 43.6 One-parent locality of H_mix in the new graph phase

Once the new graph basin is found, rerun the local radius-ball isotropization/token tests there. The local closure mechanism must survive the corrected graph couplings and not rely on the old N=128/216 states.

## 43.7 Nonlinear/strong closure remains a final gravity target

The dynamic-Q, moving-graph Jacobi, symmetry-derived scalar, DeWitt ray, and finite coefficient lock are now unusually coherent. But a genuine extended many-body first-class constraint phase is still not proved.

The final gravity standard remains:

```text
one autonomous finite parent
 -> stable graph/frame phase
 -> local schedule redundancy
 -> first-class scalar/spatial constraints
 -> two TT modes
 -> shared metric/cone
 -> nonlinear continuum closure.
```

---

# 44. Current falsification criteria after the cutoff recovery

The project should be considered strongly damaged or killed if any of the following persist under fair tests:

1. **Dimensional phase failure:** after broad Cayley/product adversaries, no open coupling region has the amorphous 3D basin as a stable low-energy phase.
2. **Nucleation failure:** the low-dimensional basin exists only when seeded with external coordinates and cannot be reached by autonomous local/soft rewrite dynamics on increasing N.
3. **Thermodynamic drift:** heat-kernel/ball-growth/rank-4 observables do not stabilize toward a finite 3D phase with N.
4. **Local closure failure:** local H_mix isotropization ceases to be feasible in the corrected graph phase or requires nonlocal/global weight coordination.
5. **Matter cell failure:** the local curl gap collapses because the shortest required cycle basis length diverges with N.
6. **Shared-clock failure:** matter and gravity cannot maintain the same schedule normalization once a realistic interacting matter sector is used.
7. **Constraint failure:** the finite schedule symmetry does not become a genuine first-class local redundancy in the extended many-body low-energy space.
8. **Extra-mode failure:** additional scalar/vector modes remain gapless after the full coupled parent is assembled.
9. **Hidden-GR failure:** closure works only when the microscopic Hamiltonian is explicitly supplied with GR's scalar/momentum constraint tensors rather than symmetry/schedule data.

A clean kill is preferable to adding rescue terms without derivation.

---

# 45. Assumed / derived / interpretation ledger for the next compression phase

## 45.1 Still assumed / microscopic choices

- finite relational Hilbert space/process degrees;
- degree-6 target sector;
- positive triangle frustration;
- specific graph spectral/communicability/capacity/determinant competition;
- generic local schedule/frustration degrees;
- finite local frame/process algebra.

## 45.2 Derived or exact conditional on those ingredients

- valence selection from degree penalty;
- local rewrite/matching orbits;
- finite lapse wedge and schedule holonomy;
- incidence identity `Bhat Bhat^T=Ltilde`;
- same-Laplacian z=1 matter carrier;
- moving-graph finite-rank `Delta L`;
- metric-move identity `delta h = 6 X^T Delta L X`;
- SO(03) decomposition of the kinetic covariance;
- symmetry-derived two-derivative scalar;
- DeWitt ray from normal preservation/zero-frustration;
- `AB=1` and finite matter `ab=1` with a shared schedule clock;
- internal closure of quantum relational frame/chirality algebra;
- block classicality `~1/(Sn)`;
- exact finite/local Jacobi checks in several moving-Q representations.

## 45.3 Interpretation, not yet microscopic theorem

- “spacetime is an optimized finite-information ledger/compression display”;
- “cosmic glue” as an information-capacity explanation of gravity;
- any claim that the universe literally implements the tested graph functional;
- any claim of Standard Model emergence;
- any claim that black-hole response is fully derived from the parent.

Keep these categories explicit in future writing.

---

# 46. Micro-to-macro dictionary still to be completed after closure

Once the graph phase and one-parent constraint phase are secure, build a rigorous dictionary:

```text
microscopic edge/process variables
 -> graph adjacency / incidence
 -> graph distance and diffusion distance
 -> local frame / Gram matrix
 -> q_ij and q^ij
 -> proper spatial volume
 -> local schedule clock / proper time
 -> curvature and Einstein-Hilbert normalization
 -> matter field amplitudes
 -> particle/field momentum and energy
 -> conserved charges
 -> entropy / code capacity
 -> macroscopic stress-energy / matter
 -> horizon area / response.
```

Every dictionary entry should have at least one independent consistency check from a different sector.

Do not use an emergent metric to define a microscopic quantity and then claim the same quantity independently derived the metric.

---

# 47. Key post-28-Sep scripts and snapshots

The old sections already inventory the 28 September package. The following are the most important additions generated afterward.

## 47.1 N=343 closure / H_mix

```text
gwxp_N343_corridor_best3_full.npz
gwxp_N343_closure_steered_step2.npz
gwxp_N343_closure_steered_step4.npz
gwxp_N343_k1e-4_sweep_bestjoint.npz
gwxp_N343_k1e-4_exact_step7.npz
gwxp_N343_hda_parentdown_step3.npz
gwxp_N343_trueclosure_step8_measured.npz
gwxp_N343_dsguard_step1.npz
gwxp_N343_dsguard_step2.npz
gwxp_N343_dsguard_step3_try2.npz
gwxp_N343_fixedgraph_Hmix_reweight.npz
```

## 47.2 Schedule/DeWitt/shared-clock finite tests

```text
gwxp_z5_normal_closure_emergent_scalar.py
gwxp_z5_normal_closure_full_isotropic.py
gwxp_z5_allk_symmetry_scalar_dewitt.py
gwxp_z5_exact_normal_group_closure.py
gwxp_z5_normal_to_lapse_wedge.py
gwxp_z5_schedule_invariant_fiber.py
gwxp_z5_frame_schedule_frustration.py
gwxp_z5_generic_frame_selection.py
gwxp_z5_generic_frame_selection2.py
gwxp_z5_finite_AB_lock.py
gwxp_z5_matter_shared_clock.py
```

## 47.3 Matter / local cell complex

```text
gwxp_graph_dirac_N343.py
gwxp_shortcycle_rank.py
gwxp_hodge_dirac_N216_shortfaces.py
gwxp_allfaces_local_matter.py
gwxp_fixed_rule_L7.py
gwxp_L7_multiseed_test.py
gwxp_matter_gap_multiseed.py
gwxp_dynamic_face_robustness.py
gwxp_softcurl_gap.py
gwxp_softcurl_basis.py
```

## 47.4 Dynamic Q / moving graph / same-Q identities

```text
gwxp_dynamicQ_jacobi_z5.py
gwxp_quantum_frame_noncomm.py
gwxp_quantum_holonomy_scaling.py
gwxp_frame_quadratic_closure.py
gwxp_incidence_normal_sharedQ.py
gwxp_incidence_rewire_covariance.py
gwxp_movinggraph_jacobi.py
gwxp_move_laplacian_identity.py
```

## 47.5 Local H_mix / soft driver

```text
gwxp_local_hmix_balls.py
gwxp_local_hmix_lp.py
gwxp_local_token_mc.py
gwxp_local_frame_lp.py
gwxp_localframe_multisize_lp.py
gwxp_local_heat_hmix.py
gwxp_local_heat_token_mc.py
gwxp_radius_scan.py
gwxp_radius_channels.py
gwxp_radius_metricstep.py
gwxp_radius_multisize_counts.py
gwxp_soft_driver_compare.py
gwxp_softdistance_hmix.py
gwxp_resolvent_distance.py
gwxp_commoncore_softdriver.py
```

## 47.6 N=344 basin/nucleation/cutoff-recovered files

```text
gwxp_external_amorphous_N344_g3_U0.106_k0.08_seed344806.npz
gwxp_external_amorphous_N344_g3_U0.106_k0.08_seed344807.npz
gwxp_external_N344_parent_relaxed30.npz
gwxp_external_N344_parent_relaxed30_seed2.npz
gwxp_external_N344_parent_relaxed60_seed2.npz
gwxp_generic_tf_N344_doublecover_seed344123.npz
gwxp_N344_generic_parentonly_nucleation4.npz
gwxp_N344_generic_parentonly_nucleation8.npz
gwxp_N344_generic_parentonly_nucleation12.npz
gwxp_N344_unbiased200.npz ... gwxp_N344_unbiased950.npz
gwxp_N344_zeroT1250.npz ... gwxp_N344_zeroT2000.npz
gwxp_N344_relation_condense37.npz ... gwxp_N344_relation_condense312.npz
gwxp_nucleation_square_scan.py
gwxp_nucleation_square_energy.py
gwxp_nucleation_corr.py
gwxp_parentonly_nucleation_walk.py
gwxp_unbiased_zeroT_walk.py
gwxp_relation_condensation_walk.py
gwxp_square_autocatalysis.py
gwxp_pair_nucleation_synergy.py
gwxp_crosssize_relation_walk.py
gwxp_crosssize_orderparam.py
gwxp_universal_landau_fit.py
gwxp_capacity_variance_fit.py
gwxp_rank2_abelian_competitor.py
gwxp_rank2_window_scan.py
gwxp_reaction_Uscan.py
gwxp_path_phase_scan.py
gwxp_ollivier_path.py
```

## 47.7 Exploratory quantum H_mix

```text
gwxp_quantum_hartree_full.py
gwxp_quantum_hartree_iter.py
gwxp_quantum_hartree_riemann.py
gwxp_hartree_finiteR.py
```

---

# 48. Exact starter prompt for the next chat

Use this prompt with the uploaded master rollover:

> **Continue GWXP / Cosmic Glue from the 29 September 2026 MASTER ROLLOVER. Read the entire document before reasoning. Treat later corrections as authoritative, preserve all KILLED/DEMOTED/CORRECTED routes, and do not claim proof beyond the evidence labels. Work in short falsifiable batches to avoid tool timeouts. The current graph-phase issue is no longer the old N=343 isotropy test: the cutoff recovery found autonomous short-cycle/relation condensation from a generic triangle-free N=344 graph, but also found a rank-2 Cayley competitor that beats the old g=3,U=0.106,kappa=0.08 point. Start by attacking the new candidate rank-2-safe window around g=3, kappa~0.25-0.40, U~0.102-0.105 using fresh parent-only anneals from generic graphs, broad low-rank Cayley adversaries, and a first-principles decomposition of why the parent rewards relation condensation. Keep the same-Q incidence/Laplacian, local H_mix, symmetry-derived scalar, DeWitt, AB=ab=1, dynamic-Q, and matter/Hodge results intact unless a new test contradicts them. Also compare the observed short-cycle condensation mechanism with Quantum Graphity and combinatorial/Ollivier-curvature quantum-gravity literature before making novelty claims.**

---

# 49. Current honest status sentence

> **GWXP is still not a derivation of gravity from finite information. It has, however, compressed a large part of the desired architecture onto one relational graph/incidence structure: the same Laplacian now controls propagation, a finite z=1 matter carrier, normal-normal schedule algebra, moving metric fluctuations, and the kinetic covariance; symmetry plus autonomous schedule consistency can select the DeWitt ray and a shared clock normalization without inserting the old scalar stabilizer. The principal unresolved empirical problem is now whether the graph parent has an open, autonomously nucleating thermodynamic 3D amorphous phase once the newly discovered rank-2 Cayley competitors are included. The cutoff-recovered short-cycle/relation-condensation trajectory is the strongest clue to that mechanism, but the old parameter point is no longer defensible as the final phase.**
