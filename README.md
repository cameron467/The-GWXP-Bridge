The GWXP Bridge
Finite causal quantum information → dynamical code geometry → GR-like infrared structure → horizon stability
> **Status:** open research program. Several algebraic links are derived, several numerical results are reproducible, several continuum targets are established physics, and the central microscopic-to-continuum closure remains open.
The GWXP Bridge asks a narrower question than “is spacetime quantum information?”
The working hypothesis is that a fundamentally finite quantum system can possess a special many-body phase in which spacetime locality, geometry, gauge redundancy and gravity are emergent properties of a dynamical code subspace rather than properties of the microscopic factorization itself.
In that picture:
microscopic degrees of freedom are finite quantum process variables, not Planck-sized spacetime pixels;
emergent geometry is encoded in a state-dependent/code-dependent collective structure;
the low-energy sector contains exactly two gapless transverse-traceless tensor modes;
embedding/slicing changes become gauge directions;
the deformation algebra closes on the same emergent metric that controls propagation;
the two-derivative infrared theory is then strongly driven toward Einstein gravity;
black-hole formation is interpreted as a stability change of the geometric code, not as a universal local-density threshold;
zero static black-hole Love response may arise from isospectral code motion while time-dependent motion still permits absorption.
The project is intentionally organized as a falsification ledger. Ideas that fail are retained rather than silently removed.
---
Evidence labels used in this repository

To keep the speculative architecture separate from what has actually been shown, claims are tagged conceptually as:

ESTABLISHED — standard result from existing physics/mathematics literature.

DERIVED — algebra worked out within this project from stated assumptions.

NUMERICAL — reproduced by explicit finite-matrix / matrix-free calculations with stored outputs.

INFERRED — a structural connection suggested by the derived pieces but not yet generated autonomously by the microscopic model.

OPEN — a missing calculation or theorem required to close the program.

KILLED — a route explicitly falsified or demoted by algebra, numerics or a consistency check.

The central purpose of the repository is to shrink the OPEN category.
---
The complete hypothesis in one diagram
```text
FINITE QUANTUM PROCESS SUBSTRATE
(finite-dimensional microscopic factors; not spacetime sites)
                    |
                    v
DYNAMICAL / GEOMETRY-DEPENDENT CODE PHASE  P[q]
                    |
        +-----------+------------+
        |                        |
        v                        v
  CONSTRAINT / FRAME         MOVING-CODE RESPONSE
      STRUCTURE                    |
        |                          +----------------------+
        v                          |                      |
 exactly 2 TT modes               v                      v
 + one causal cone        isospectral code orbit   horizon/code stability
 + HDA/refoliation                |                      |
        |                         v                      v
        v                 static Love = 0        microscopic stability map
 FP / DeWitt / TEGR       dynamic absorption     L_micro = δTheta+/δb
        |                    can remain                  |
        v                                                v
 EINSTEIN GR (IR)                                  MOTS operator ?
                                                        |
                                                        v
                                             nonlinear fold / horizon birth
```
The ambitious claim is not that every arrow above has already been derived from one Hamiltonian.
The claim being tested is that these arrows may be different limits of one underlying finite quantum architecture.
---
1. Microscopic ontology
INFERRED: finite information is fundamental; spacetime points are not
The original “Cosmic Glue” idea began with a much cruder picture: matter consumes a finite local information capacity and the shortage appears as gravity.
That route was killed.
The surviving ontology is different:
> **The microscopic tensor factorization is a network of finite quantum process degrees of freedom. Emergent spacetime locality is a property of a protected low-energy code, not a literal map from microscopic factors to points in space.**
This matters because nonlinear gravity is incompatible with treating microscopic locality as ordinary spacetime locality in a naive way.
The preferred microscopic language is therefore finite noncommutative operator algebra / quantum-link / frame-like degrees of freedom, with continuum coordinates and derivatives emerging only in a protected infrared window.
A schematic full architecture is
```math
H_{\rm micro}
=
H_{\rm frame}
+
H_{\rm solder}
+
H_{\rm normal}
+
H_{\rm mix}
+
H_{\rm defect}.
```
Interpretation:
`H_frame`: collective frame / torsion-like degrees of freedom;
`H_solder`: locks relative frames/cones into one diagonal geometry;
`H_normal`: supplies the normal/schedule/refoliation sector;
`H_mix`: allows the protected sectors to communicate;
`H_defect`: gaps unwanted defects and non-geometric excitations.
The current SU(2) numerical model is a test material for part of this architecture, not yet the full autonomous Hamiltonian above.
---
2. Finite spin-2 kinematics
DERIVED: finite constraint counting can leave exactly two tensor modes
For a symmetric spatial tensor `h_ij`, there are six configuration components in three spatial dimensions.
Using three vector-gauge directions plus one scalar constraint gives
```math
6-3-1=2
```
logical configuration modes at generic nonzero momentum.
A finite-q CSS/stabilizer-like regulator can realize the chain condition between the discrete symmetric-gradient and scalar-curvature maps and reproduce this two-mode count.
This is an existence result for the kinematics.
It does not by itself establish a thermodynamic graviton phase.
---
3. Why the two-derivative infrared operator is highly constrained
DERIVED: preserving the constraint ideal selects the linearized Einstein structure
Take the linearized constraints
```math
C_i=\partial_j\pi^{ij}=0
```
and
```math
C_0
=
\partial_i\partial_jh^{ij}
-
\nabla^2h
=0.
```
For the most general parity-even, rotationally invariant, two-derivative spatial operator
```math
(Kh)_{ij}
=
a\nabla^2h_{ij}
+b(\partial_i v_j+\partial_jv_i)
+c\partial_i\partial_jh
+d\delta_{ij}s
+e\delta_{ij}\nabla^2h,
```
constraint preservation gives
```math
a+b=0,
\qquad
b+d=0,
\qquad
c+e=0.
```
Self-adjointness adds
```math
c=d.
```
These conditions collapse the operator to the linearized Einstein / Fierz-Pauli spatial structure up to normalization and sign.
For the most general ultralocal kinetic map
```math
(M\pi)_{ij}
=
\alpha\pi_{ij}
+
\beta\delta_{ij}\pi,
```
scalar-constraint preservation requires
```math
\alpha+2\beta=0,
```
which gives the DeWitt trace combination
```math
\pi_{ij}-\frac12\delta_{ij}\pi.
```
Interpretation
Once the correct protected constraint ideal exists, a healthy minimal two-derivative propagation law has very little freedom.
The hard problem is therefore not inventing an arbitrary graviton dispersion relation. It is making the finite microscopic phase autonomously realize the correct protected constraint structure.
---
4. Why exact commuting-projector gravity was abandoned
KILLED: rigid metric stabilizers are the wrong dynamical universality class
Exact local gauge-invariant metric observables begin at curvature order.
Squaring such objects naturally produces higher-derivative dispersion:
```text
curvature^2  ->  k^4
Cotton-like^2  ->  k^6
```
rather than the desired relativistic
```math
\omega^2\propto k^2.
```
The project therefore moved away from “every microscopic term must commute with every constraint” toward the weaker and more useful condition
```math
[H,\mathcal I]\subseteq\mathcal I,
```
where `I` is the constraint ideal.
The physical subspace is preserved even though individual microscopic terms need not be rigid stabilizers.
---
5. Frame/torsion route and TEGR
DERIVED: removing unwanted frame modes selects the TEGR ray
For the parity-even New General Relativity family
```math
L
=
c_1 T^\rho{}_{\mu\nu}T_\rho{}^{\mu\nu}
+c_2 T^\rho{}_{\mu\nu}T^{\nu\mu}{}_\rho
+c_3 T^\rho{}_{\mu\rho}T^{\sigma\mu}{}_\sigma,
```
the relevant kinetic combinations include
```math
A_V=2c_1+c_2+c_3,
\qquad
A_A=2c_1-c_2.
```
Demanding that the unwanted vector and antisymmetric frame modes disappear gives
```math
A_V=A_A=0,
```
hence
```math
(c_1,c_2,c_3)\propto(1,2,-4).
```
This is the TEGR ray, up to convention.
TEGR is dynamically equivalent to Einstein gravity up to a boundary term.
The same coefficient choice also reproduces the DeWitt kinetic trace ratio.
Status
The selection algebra is derived.
What is not yet shown is that the current finite SU(2) Hamiltonian autonomously flows to this frame/torsion theory in the infrared.
---
6. Hypersurface deformations and nonlinear GR
ESTABLISHED + DERIVED GEOMETRIC TARGET
For an embedded spatial surface, two normal deformations do not commute into another normal deformation. Their commutator becomes a tangential deformation with structure function given by the inverse spatial metric:
```math
[\delta_N,\delta_M]
=
\delta_\xi,
\qquad
\xi^j
=
q^{ij}(M\partial_iN-N\partial_iM).
```
The corresponding Hamiltonian target is the hypersurface-deformation algebra
```math
[H[N],H[M]]
\longrightarrow
D\!\left[q^{ij}(N\partial_jM-M\partial_jN)\right].
```
The important requirement is that the same emergent `q^{ij}` must control both propagation and the deformation algebra.
If the low-energy theory contains only one healthy massless spin-2 field with the correct deformation/gauge algebra and no additional light geometric fields, established consistency results strongly constrain the local two-derivative nonlinear completion toward Einstein gravity.
OPEN
The full HDA has not yet been generated from the finite SU(2) model itself.
This remains one of the central closure tests.
---
7. Horizon area / boost coefficient
DERIVED AT THE CONTINUUM EFFECTIVE LEVEL
With curvature coefficient
```math
c_R=\frac{1}{16\pi G},
```
the scalar constraint boundary term for a local boost gives
```math
\delta B_\Sigma=\frac{\delta A}{8\pi G}.
```
The modular boost generator is
```math
K=2\pi B_\Sigma,
```
so
```math
\delta K
=
\frac{\delta A}{4G}.
```
Together with the entanglement first law this gives
```math
\delta S
=
\frac{\delta A}{4G}.
```
This is important because the same infrared gravitational stiffness that fixes bulk propagation also fixes the horizon boost/area response coefficient.
What this does NOT prove
It does not count the fundamental black-hole microstates.
The strong-field state-counting problem remains open.
---
8. Black-hole static Love response from moving code geometry
DERIVED: exact static cancellation on an isospectral code orbit
Take a family of Hamiltonians related by
```math
H_{\rm BH}(\lambda)
=
U(\lambda)H_0U^\dagger(\lambda),
\qquad
U(\lambda)=e^{-i\lambda G}.
```
Then
```math
Q
=
\left.\frac{\partial H}{\partial\lambda}\right|_0
=
-i[G,H_0],
```
and
```math
C
=
\left.\frac{\partial^2H}{\partial\lambda^2}\right|_0
=
-[G,[G,H_0]].
```
Second-order perturbation theory forces the spectral polarizability and contact term to cancel in the static limit:
```math
\chi(0)=0.
```
A time-dependent deformation introduces the moving-basis connection and can still drive transitions, so structurally
```math
\chi(0)=0,
\qquad
\mathrm{Im}\,\chi(\omega>0)\neq0.
```
Interpretation
This is a candidate microscopic mechanism for the characteristic combination
> **zero static Love + nonzero dynamical absorption**.
OPEN
The full Schwarzschild/Kerr response function, including horizon absorption and exterior gravitational dressing, has not yet been derived from this microscopic construction.
---
9. Black-hole formation as code stability loss
INFERRED CENTRAL STRONG-FIELD HYPOTHESIS
The surviving strong-field idea is not that a local information density reaches a universal threshold.
That route fails immediately for macroscopic black holes.
The stronger proposal is:
> **A black-hole horizon appears when the geometric code reaches a marginal stability point in the channel that continuum GR describes with the MOTS stability operator.**
On the continuum side, the relevant object is schematically
```math
\mathcal L_{\rm MOTS}
=
-\Delta
+2X\cdot\nabla
+\left(Q+\nabla\cdot X-X^2\right)
=
-(\nabla-X)^2+Q.
```
A horizon bifurcation occurs when its principal mode becomes marginal.
The project originally tried to identify the inverse same-operator bridge susceptibility directly with this object.
That was too crude.
---
10. Corrected microscopic horizon bridge
DERIVED STRUCTURAL CORRECTION: MOTS is a Jacobian, not a same-operator susceptibility
The generic MOTS stability operator is non-self-adjoint because of its drift / normal-bundle connection term.
A static equilibrium `B-B` susceptibility of Hermitian operators is symmetric and therefore cannot generically equal the full MOTS operator.
The correct microscopic analogue should instead be a cross-Jacobian:
```math
L^{\rm micro}_{xy}
=
\frac{\delta\Theta_x^+}{\delta b_y},
```
where
`b_y` is a microscopic normal-deformation coordinate of the code/cut;
`Theta_x^+` is the microscopic analogue of outgoing null expansion.
A natural operational definition is that outgoing expansion is the fractional rate of change of the emergent area/corner charge under an outgoing deformation:
```math
\Theta_x^+
\sim
\frac{1}{a_x}
\,i\langle[H_+(x),a_x]\rangle,
```
with appropriate operator symmetrization in a complete implementation.
Why the non-self-adjoint structure is natural
For a local directed Jacobian, write the off-diagonal elements as
```math
L_{xy}=-w_{xy}e^{A_{xy}},
\qquad
A_{xy}=-A_{yx}.
```
Then
```math
(Lb)_x
=
Q_xb_x
+
\sum_{y\sim x}
w_{xy}\left(b_x-e^{A_{xy}}b_y\right).
```
Under a local rescaling of the normal frame
```math
b_x\rightarrow e^{f_x}b_x,
```
the directed connection transforms as
```math
A_{xy}\rightarrow A_{xy}+f_x-f_y.
```
That is the discrete transformation law expected of a normal-bundle connection.
In the smooth limit this gives
```math
D_a=\nabla_a-X_a
```
and therefore
```math
-D^2+Q
=
-\Delta
+2X\cdot\nabla
+\nabla\cdot X
-X^2
+Q,
```
which has exactly the structural form of the generic MOTS operator.
Status
This is a derived structural bridge.
It has not yet been extracted from the full finite SU(2) Hamiltonian.
---
11. Why the square-root horizon fold should come from nonlinearity, not a Kubo pole
DERIVED NORMAL-FORM CONSEQUENCE
Let the nonlinear microscopic marginality equation be
```math
\Theta[b,\mu]=0.
```
At a critical point assume a simple zero mode
```math
L\psi=0,
\qquad
\phi^\dagger L=0,
```
where
```math
L=\frac{\delta\Theta}{\delta b}.
```
Write
```math
b=b_c+A\psi+\cdots.
```
Projecting the nonlinear equation onto the left zero mode gives generically
```math
a(\mu-\mu_c)+cA^2+\cdots=0.
```
Therefore
```math
A\propto\sqrt{|\mu-\mu_c|}.
```
The restoring singular value then scales as
```math
s_{\min}(L)
\propto
\sqrt{|\mu-\mu_c|},
```
and the inverse response diverges as
```math
\|L^{-1}\|
\propto
|\mu-\mu_c|^{-1/2}.
```
Consequence
The desired `1/sqrt(t)` fold does not need to be inserted into a linear susceptibility by hand.
It should emerge automatically once the microscopic model contains the correct nonlinear marginality equation with a simple zero mode.
---
12. Current SU(2) quantum-link test material
The cleanest numerical test material developed so far uses:
two co-located SU(2) fundamental doublets on every link;
projection to the symmetric spin-1 triplet;
exact local Gauss/intertwiner sectors;
no compensating background charge in the even-rishon construction;
matrix-free Lanczos and Krylov/resolvent calculations.
The historical fixed-detuning softness sequence obtained from the archived Hamiltonians is:
Graph	`sigma_soft`
K4	0.2500221818
K5	0.2500067915
K6	0.1890521106
K7	0.1666732809
K8	0.1389102562
with
```math
\sigma_{\rm soft}
=
\frac{1}{s_{\max}(\chi)}.
```
The K7 principal mode is almost exactly the uniform bridge mode.
The detuning scan gives
```math
\chi_{\rm uniform}(t)
\approx
\frac{5.99972}{t},
```
with exponent approximately `-0.9999998`.
This is an isolated conserved-sector crossing pole, not a horizon fold.
---
13. Important new audit of the K4–K8 scaling sequence
ACTIVE NUMERICAL CORRECTION
The archived V4.4 builder contains the Wilson-triangle coefficient
```python
trinorm = 2.0/(N-2)
coeff = -(0.55 + 0.071*ti) * trinorm
```
where `ti` is the global triangle enumeration index.
That means the microscopic loop coefficient is not purely local and not actually size-independent across the `K_N` sequence.
Although `trinorm` was intended as a Kac normalization, the increasing number and index range of triangles causes the mean total incident loop strength per edge to grow with `N`.
For the archived sequence the mean incident triangle strength per edge is approximately:
N	Mean incident loop strength per edge
4	1.313
5	1.739
6	2.449
7	3.514
8	5.005
Consequence
The decreasing `sigma_soft` values remain valid outputs of the archived Hamiltonians, but they should no longer be described as a clean same-coupling finite-size scaling theorem until the sequence is rerun with genuinely size-independent local triangle couplings.
This is exactly the kind of artifact the project is intended to catch rather than hide.
---
14. Why the current `1/t` pole was structurally unavoidable
At `u = 0`, total H-flavor number `k` is exactly conserved and `Delta_B` acts as its chemical potential.
The current solver treats the `k=0` ground sector and `k=1` response sector separately.
Therefore the dominant linear response near the crossing is forced to have the Lehmann form
```math
\chi\sim\frac{1}{E_1-E_0}\sim\frac{1}{t}.
```
Consequence
The existing `k=0 <-> k=1` linear-response solver is not capable by construction of producing the nonlinear horizon fold.
To test the fold, the model must contain a gauge-compatible mechanism that mixes the relevant sectors and permits a nonlinear stationary branch `Theta[b,mu]=0` to be solved self-consistently.
This converts the old `t^-1` result from a mysterious failure into a precise diagnostic of the current truncation.
---
15. Complete graphs are a material test, not a geometry test
The current K4–K8 sequence uses fully connected graphs `K_N`.
Those graphs are useful for asking whether the microscopic material can develop a collective soft mode.
They are not a valid route to a local two-dimensional horizon geometry at large `N`.
The graph Laplacian of `K_N` has only
```text
0, N, N, N, ...
```
and therefore has no progressively resolved wavelength hierarchy analogous to spherical harmonics.
Next geometry family
The same SU(2) material should be moved onto genuine triangulated two-spheres.
For a triangulated sphere with `V` vertices,
```math
E=3V-6,
```
which grows much more slowly than
```math
E(K_V)=\frac{V(V-1)}{2}.
```
So the geometrically meaningful test may actually be computationally cheaper than the complete-graph sequence.
The full low spectrum of the microscopic stability map can then be tested against the spherical pattern
```math
-\Delta_{S^2}Y_{\ell m}
=
\ell(\ell+1)Y_{\ell m},
```
with multiplicities
```text
1, 3, 5, 7, ...
```
rather than tracking only one soft singular value.
---
16. The strongest version of the GWXP bridge
The project now has a much sharper target than the original slogan “quantum information becomes gravity.”
The desired chain is:
```text
finite quantum process algebra
        |
        v
geometry-dependent protected code P[q]
        |
        +-----------------------------+
        |                             |
        v                             v
constraint/frame sector         moving-code sector
        |                             |
        v                             +---------------------+
2 TT modes + HDA                       |                    |
        |                              v                    v
        v                       isospectrality       cut stability map
FP / DeWitt / TEGR                    |                    |
        |                              v                    v
        v                        static Love = 0      L_micro = δTheta+/δb
Einstein GR (IR)                 dynamic absorption         |
                                                          v
                                                 L_MOTS in continuum
                                                          |
                                                          v
                                                horizon fold / BH sector
```
If this closes autonomously in one microscopic theory, the conceptual result would be:
> **Graviton dynamics, black-hole static rigidity, dynamical absorption and horizon birth are different response limits of one finite quantum code architecture.**
That is the eureka target.
It is not yet a theorem.
---
17. What is actually established inside this project
DERIVED
finite constraint counting can leave exactly two tensor configuration modes;
preserving the linearized constraint ideal fixes the minimal two-derivative spatial operator to the Fierz-Pauli / linearized-Einstein structure;
scalar-constraint preservation fixes the DeWitt kinetic trace ratio;
rigid commuting-projector metric dynamics naturally falls into a higher-derivative universality class;
frame/torsion variables evade that derivative-counting obstruction;
eliminating vector and antisymmetric frame modes selects the TEGR coefficient ray `(1,2,-4)`;
the continuum geometric normal-deformation algebra has the required `q^{ij}` structure function;
the bulk curvature coefficient fixes the horizon boost/area variation coefficient;
an isospectral code orbit gives exact static spectral/contact cancellation;
a nonlinear marginal equation with a simple zero mode generically produces the square-root fold;
the generic MOTS target requires a cross-Jacobian rather than a symmetric same-operator static susceptibility;
a directed local Jacobian naturally carries a discrete normal-bundle connection and has the correct covariant-Laplacian continuum form.
NUMERICAL
exact finite Gauss/intertwiner sectors were constructed for the SU(2) quantum-link material;
matrix-free Lanczos / resolvent calculations were validated on the archived systems;
the archived complete-graph Hamiltonians exhibit decreasing softness through the reported K4–K8 sequence;
the K7 detuning response is an essentially exact `1/t` conserved-sector pole;
the K8 number corresponds to the lowest physical candidate verified in the targeted search, not an exhaustive global theorem.
IMPORTANT NUMERICAL CAVEAT
The K4–K8 sequence is currently under re-audit because the archived triangle coefficient depends on the global triangle index and therefore changes the effective local loop strength with system size.
---
18. What remains missing
These are the pieces that must still be supplied before the program can claim an autonomous microscopic derivation of gravity.
OPEN 1 — Autonomous full microscopic phase
A single fixed microscopic Hamiltonian must realize the required protected phase without having GR compiled into its couplings or constraints.
OPEN 2 — Same-model origin of the metric
The emergent metric `q_ij` must be extracted from the microscopic state/code itself and must be the same object controlling both propagation and the deformation algebra.
OPEN 3 — Full HDA closure
The finite model must reproduce the hypersurface-deformation algebra in its infrared code subspace with controlled finite-size / UV corrections.
OPEN 4 — Clean homogeneous scaling
The SU(2) sequence must be rerun with genuinely size-independent local couplings after removing the triangle-index normalization artifact.
OPEN 5 — Local spherical geometry
The model must be tested on a refining family of triangulated two-spheres, and the whole low response spectrum must approach the expected local differential-operator structure.
OPEN 6 — Microscopic outgoing expansion
An explicit operator definition of `Theta_micro` must be implemented from the moving code / area-corner sector rather than inserted as a continuum object.
OPEN 7 — Nonlinear sector mixing and fold
The relevant conserved-sector truncation must be relaxed in a gauge-compatible way so the nonlinear branch `Theta[b,mu]=0` can actually form and bifurcate.
OPEN 8 — Generic non-self-adjoint MOTS map
After the time-symmetric/self-adjoint limit is under control, the directed normal-bundle connection must emerge dynamically and reproduce the generic MOTS drift structure.
OPEN 9 — Full black-hole dynamical response
The code-orbit mechanism must reproduce the physical frequency dependence and normalization of the gravitational response, not only the structural static cancellation.
OPEN 10 — Strong-field state counting
The UV theory must explain why black-hole macrostate counting gives the Bekenstein-Hawking coefficient rather than merely reproducing the semiclassical area variation.
---
19. Falsification ledger
KILLED: matter consumes local information capacity
Information content is not gravitational charge. The idea did not produce the tensor structure of gravity and was abandoned.
KILLED: literal Planck pixels are spacetime points
Microscopic factorization and emergent gravitational locality cannot be identified so simply.
KILLED: scalar capacity fraction is the metric
A scalar can mimic a weak Newtonian acceleration but cannot reproduce full tensor gravity or relativistic light propagation.
KILLED: exact commuting-projector metric gravity as the main mechanism
It naturally produces higher-derivative `k^4` / `k^6` stiffness rather than the desired Einstein `k^2` structure.
KILLED: exact microscopic HDA on an ordinary finite point lattice
Finite commutative point algebras have trivial exact derivations. Continuum translation/differentiation must be emergent or encoded in a noncommutative matrix algebra.
KILLED: raw microscopic cut entropy equals `A/4G`
The relevant entropy belongs to the dressed/encoded gravitational algebra, not an arbitrary microscopic tensor-factor cut.
KILLED: the entire physical Hilbert space must scale with area
Local graviton excitations leave a volume-extensive perturbative state space. The gravitational area bound is a backreaction/maximum-entropy statement, not a statement that perturbative bulk degrees disappear.
KILLED: universal local density threshold for black-hole formation
Macroscopic black holes do not obey such a universal density criterion.
KILLED: hand-matched Hermitian bridge Hessian proves MOTS emergence
A compatibility toy can demonstrate mathematical consistency, but the generic MOTS operator is non-self-adjoint and the matching must arise from an independent microscopic response map.
KILLED: the current `1/t` pole is the horizon fold
It is an exact conserved-sector crossing pole.
DEMOTED: raw K4–K8 softness as clean thermodynamic scaling
The archived Hamiltonians contain a size-dependent triangle-index coupling. The values remain reproducible outputs of those Hamiltonians, but the sequence must be rerun before being used as clean same-material finite-size scaling evidence.
---
20. Immediate falsification program
The shortest path to either a real bridge or a clean failure is now:
Fix the microscopic loop normalization so every graph uses the same local couplings.
Rerun the homogeneous material test and see whether collective softening survives.
Move the same material onto triangulated spheres.
In the time-symmetric sector, test whether the microscopic stability map approaches
```math
L_{\rm micro}\approx qI+ZL_{\rm sphere}.
```
Test the whole low spectrum, not only one singular value.
Construct the microscopic outgoing-expansion observable `Theta_micro` from area/corner-charge flow.
Compute
```math
L^{\rm micro}_{xy}
=
\frac{\delta\Theta_x}{\delta b_y}.
```
Introduce gauge-compatible nonlinear sector mixing and solve the branch
```math
\Theta[b,\mu]=0.
```
Demand the simultaneous fold diagnostics
```math
s_{\min}(L)\to0,
```
```math
(\Delta b)^2\propto|\mu-\mu_c|,
```
and
```math
s_{\min}(L)^2\propto|\mu-\mu_c|,
```
with the same `mu_c`.
10. Turn on the directed connection and test convergence toward the full non-self-adjoint MOTS operator.
11. Independently test whether the same moving-code family retains the zero-static-Love cancellation and reproduces the physical dynamical absorption spectrum.
12. Finally test whether the same emergent `q^{ij}` closes the HDA and controls the TT propagation sector.
If these fail, the architecture should be rejected or substantially revised.
If they all work, the separate bridges close into one microscopic road.
---
21. Repository / reproducibility artifacts
The project has preserved code, output ledgers and checkpoints rather than relying only on narrative summaries.
Important archived artifacts include:
`cosmic_glue_v42_codebase.zip`
`cosmic_glue_v43_matrixfree.zip`
`cosmic_glue_v44_even_triplet.zip`
`cosmic_glue_v44_validated_boundary.zip`
`K4_K8_SCALING.csv`
`k8_final_checkpoint.zip`
V4 MOTS compatibility/audit files
raw CSV / JSON result ledgers
The older V4 MOTS compatibility toy is retained because it demonstrated that a bridge with a zero mode, fold and constraint protection can coexist in a finite matrix model.
It does not count as autonomous emergence because the MOTS matching and fold structure were supplied as inputs.
---
22. AI assistance
A substantial portion of the exploratory derivation, implementation, code generation, optimization, adversarial testing and documentation was performed with assistance from frontier language models, primarily OpenAI ChatGPT and Google AI.
The models are not treated as sources of numerical truth.
The working standard is:
explicit operators;
reproducible scripts;
stored numerical outputs;
convergence checks;
independent consistency attacks;
preservation of failed routes.
The project should be judged by the mathematics and reproducibility artifacts, not by the authority of the author or the language models used to accelerate the work.
---
23. Scientific context
This project sits near several established research programs without claiming ownership of their core ideas:
emergent gauge fields from finite-dimensional quantum systems;
Gu–Wen-style emergent helicity-2 lattice models;
quantum-link and rishon formulations of gauge theories;
holographic / operator-algebra quantum error correction;
hypersurface-deformation / geometrodynamic reconstruction;
spin-2 consistency and nonlinear completion;
teleparallel / New General Relativity;
black-hole Love numbers and dynamical response;
MOTS stability and horizon bifurcation;
gravitational edge modes, boosts and area charges.
The broad statement “spacetime is encoded like a quantum error-correcting code” is established territory.
The narrower GWXP question is whether the code itself can become a dynamical geometry and whether graviton dynamics, horizon formation and black-hole response can emerge as different limits of the same finite microscopic architecture.
---
Current bottom line
The project has not derived quantum gravity.
It has, however, reduced a broad speculative idea to a fairly specific set of mathematical bridges and falsification tests.
The strongest current architecture is:
```text
finite quantum substrate
        -> dynamical nonlocal code phase
        -> protected 2-TT / deformation structure
        -> FP / DeWitt / TEGR
        -> Einstein gravity in the IR
```
plus a strong-field branch
```text
same moving code
        -> isospectral static deformation -> zero static Love
        -> dynamical code motion          -> possible absorption
        -> geometric stability Jacobian   -> MOTS target
        -> nonlinear zero-mode fold       -> horizon birth
```
The missing eureka closure is:
> **Show that one autonomous microscopic Hamiltonian generates all of these structures rather than merely allowing them to be connected consistently.**
Or, in less respectable language:
> ## The quantum ledger has several entries that reconcile with Einstein.
> ## The final consolidation is still being audited.
Everything useful in this repository is intended to be taken, tested, modified or killed.
