# GWXP / Cosmic Glue — Master Evidence Ledger

**Project:** The GWXP Bridge / Finite Causal Quantum Information  
**Scope:** full research history through V5, including opening assumptions, failed routes, derivations, numerical tests, finite constructions, strong-field tests, and the final unresolved theorem.  
**Status:** open research program — **not a proof of quantum gravity**.

> The purpose of this file is not to sell the hypothesis. It is to make the argument auditable. Every major route is labeled by evidence level, failed ideas are preserved, later corrections supersede earlier claims, and the final missing step is stated explicitly.

---

## 0. Executive verdict

The project began with a crude idea:

> Matter may consume a finite local information capacity, and the resulting shortage may appear macroscopically as gravity.

That hypothesis did **not** survive.

The surviving program is narrower:

> A fundamentally finite quantum process may possess a special nonlocally encoded phase in which a collective relational frame becomes geometry, local scheduling/embedding choices become gauge directions, exactly two massless tensor modes survive, the deformation algebra closes on the same emergent metric, and the two-derivative infrared completion is driven toward GR.

By the end of V5, the project has explicit or conditional mechanisms for most of the downstream architecture. It has **not** shown that one simple generic microscopic Hamiltonian naturally enters that full phase without the gravitational constraint structure being programmed into it.

### Current endpoint

```text
finite quantum substrate
        |
        v
nondegenerate relational frame phase
        |
        +--------------------------+
        |                          |
        v                          v
constraint / schedule code     moving protected code
        |                          |
        v                          +--------------------+
2 TT modes + HDA                    |                   |
        |                           v                   v
        v                    static Love = 0      horizon stability map
Fierz-Pauli / DeWitt / TEGR   dynamic response      / fold
        |
        v
Einstein GR in the two-derivative IR
```

**The last unresolved arrow is at the beginning, not the end:** does a simple autonomous finite Hamiltonian *spontaneously realize* the gravitational constraint/refoliation phase?

---

## 1. Evidence labels

The repository uses these labels strictly.

| Label | Meaning |
|---|---|
| **ESTABLISHED** | Result from existing mathematics/physics literature. |
| **DERIVED** | Algebra worked through in this project from stated assumptions. |
| **NUMERICAL** | Reproduced finite calculation with stored data/output. |
| **EXACT FINITE EXISTENCE** | An exact finite-dimensional construction showing that a proposed structure is algebraically possible. |
| **CONDITIONAL** | Follows if a stated microscopic/IR assumption is supplied. |
| **OPEN** | Still required for the natural-emergence claim. |
| **KILLED / DEMOTED** | Explicitly rejected or weakened by a test, correction, or counterexample. |
| **CAUTION** | Result remains true for the tested object, but a stronger interpretation was invalidated. |

No result should be promoted by changing labels rhetorically.

---

# PART I — OPENING ASSUMPTIONS AND THEIR DESTRUCTION

## 2. Opening hypothesis: finite local information is “cosmic glue”

### Initial assumption

The earliest picture treated spacetime as having a finite local information capacity. Matter/energy was imagined to occupy or consume that capacity, leaving less room for spacetime and thereby creating curvature.

Schematic intuition:

```text
finite local information capacity
        |
matter consumes capacity
        |
remaining capacity changes
        |
gravity / curvature
```

### Tests that killed it

1. **Hard-drive thought experiment:** logical information content cannot be an independent gravitational charge. Rearranging stored bits at fixed stress-energy should not create a new macroscopic gravitational field.
2. **Tensor-structure test:** a scalar “capacity fraction” cannot reproduce the full tensor content of relativistic gravity, light bending, gravitational waves and refoliation structure.
3. **Locality audit:** treating microscopic finite factors as literal Planck-sized spacetime cells conflicts with known obstructions to emergent nonlinear gravity from ordinary local kinematics.
4. **Area-bound audit:** a naive finite Hilbert space per spacetime cell produces a volume-extensive state count, not an automatic gravitational area bound.

### Verdict

**KILLED:** information content itself is not the gravitational source.

**Surviving primitive:** finite quantum information/rank may characterize the microscopic process substrate, but gravity must be a collective geometric phase rather than “used-up bits.”

---

## 3. Second primitive: finite causal cut capacity

The next formulation moved finite information from *sites* to *causal cuts/relations*.

If a microscopic cut crosses finite channels with total dimension

\[
D_\gamma=\prod_{e\in\gamma}\chi_e,
\]

then Schmidt rank implies

\[
S_\gamma\le \log D_\gamma=\sum_e\log\chi_e.
\]

Writing an effective transverse cut capacity \(C_{\rm cut}/a_*^2\),

\[
\frac{1}{4G}\le \frac{C_{\rm cut}}{a_*^2},
\]

or

\[
G\ge \frac{a_*^2}{4C_{\rm cut}}.
\]

This was the first precise remnant of the original finite-capacity intuition.

### Important correction

Finite capacity gives a **ceiling**, not the observed value of \(1/G\).

Define a dynamical usability fraction

\[
\frac{1}{4G}=f\,\frac{C_{\rm cut}}{a_*^2},\qquad 0\le f\le1.
\]

Nothing in gauge structure, QEC or HDA forces a universal nonzero \(f\).

### Verdict

**CONDITIONAL SURVIVOR:** finite cut capacity can constrain gravitational stiffness, but does not determine Newton’s constant.

---

## 4. Causal discreteness is not a finite-valency graph

A major correction came from causal-set reasoning.

A Lorentzian causal order can be discrete without selecting a preferred rest frame, but a Lorentz-covariant nearest-neighbour graph of fixed finite valency is not generally available.

Therefore:

```text
causal relation != independent finite channel
```

The replacement notion is **causal quasi-locality**:

- influence respects causal order;
- microscopic relational support may be broad;
- only finite independent channel rank/modes survive;
- the long-distance response becomes local.

### Verdict

**KILLED:** “one causal link = one finite information channel.”

---

# PART II — FROM FINITE INFORMATION TO A PURE SPIN-2 PHASE

## 5. Finite spin-2 kinematics

Take a symmetric spatial tensor \(h_{ij}\) and momentum \(\pi^{ij}\).

Linearized gravity has

\[
C_i=\partial_j\pi^{ij}=0,
\]

and

\[
C_0=\partial_i\partial_jh^{ij}-\nabla^2h=0.
\]

At generic nonzero momentum:

\[
6-3-1=2
\]

configuration degrees of freedom remain.

Finite-\(q\) CSS/stabilizer-like regulators were constructed with commuting discrete vector/scalar constraints.

### Verdict

**DERIVED:** finite local Hilbert spaces can carry the correct linearized two-tensor kinematic count.

**Not proved:** existence of a thermodynamic, interacting, gapless graviton phase.

---

## 6. First major failure: exact commuting-projector metric gravity

The obvious idea was to protect the GR constraints with exact local commuting projectors and generate dynamics perturbatively.

It failed for a structural reason.

Strictly local gauge-invariant metric operators begin at curvature order. Squaring them naturally produces

\[
k^4,\quad k^6
\]

stiffness rather than Einstein

\[
k^2.
\]

This mirrors the controlled higher-derivative side of known finite-spin emergent-graviton models.

### Pivot

Do not require every microscopic term to commute with every constraint.

Require only preservation of the constraint ideal:

\[
[H,\mathcal I]\subseteq\mathcal I.
\]

### Verdict

**KILLED:** rigid commuting-projector metric gravity as the primary \(z=1\) mechanism.

**SURVIVING DESIGN PRINCIPLE:** protect the physical subspace/ideal, not term-by-term microscopic gauge invariance.

---

## 7. Fierz–Pauli rigidity from constraint propagation

For the most general parity-even rotationally invariant two-derivative operator

\[
(Kh)_{ij}
=
a\nabla^2h_{ij}
+b(\partial_i v_j+\partial_jv_i)
+c\partial_i\partial_jh
+d\delta_{ij}s
+e\delta_{ij}\nabla^2h,
\]

constraint preservation gives

\[
a+b=0,\qquad b+d=0,\qquad c+e=0.
\]

Self-adjointness gives

\[
c=d.
\]

The operator collapses to the linearized Einstein/Fierz–Pauli form up to sign and normalization.

For the general ultralocal kinetic map

\[
(M\pi)_{ij}=\alpha\pi_{ij}+\beta\delta_{ij}\pi,
\]

scalar-constraint preservation requires

\[
\alpha+2\beta=0,
\]

hence

\[
(M\pi)_{ij}\propto\pi_{ij}-\frac12\delta_{ij}\pi.
\]

### Verdict

**DERIVED:** once the correct linear constraint ideal is present, minimal two-derivative propagation is highly rigid.

See `scripts/01_core_rigidity.py`.

---

## 8. QCA/process-map laboratory

A discrete update of the form

\[
\pi'=\pi-\epsilon Kh,\qquad
h'=h+\epsilon M\pi'
\]

can preserve the constraint ideal and give TT dispersion approaching

\[
\omega=ck+O(k^3a^2,k^3\epsilon^2).
\]

This showed that finite algebra, exact constraint preservation and \(z=1\) propagation are compatible at free level.

### Correction

A literal microscopic Floquet tick introduces a preferred clock/quasienergy structure. QCA was demoted from ontology to a **gauge-fixed laboratory**.

The covariant primitive shifted to a general-boundary/process language:

\[
M\mapsto Z[M]
\]

with composition by gluing, and time evolution emerging only after a relational slicing/clock choice.

---

# PART III — LOCALITY, FRAMES, HDA AND GR RIGIDITY

## 9. Microscopic factors are not spacetime points

Marolf-type kinematic nonlocality constraints forced an ontology change.

The microscopic tensor factorization should not be interpreted as Planck pixels embedded in emergent space.

### Surviving interpretation

```text
finite process degrees
    -> nonlocal protected encoding
    -> emergent local geometry
```

### Verdict

**KILLED:** literal microscopic sites = spacetime points.

---

## 10. Finite point lattices cannot carry exact continuum derivations

On a finite commutative algebra of functions on points, exact Leibniz derivations are trivial.

For an idempotent \(e_x^2=e_x\),

\[
D(e_x)=D(e_x^2)=2e_xD(e_x)
\]

forces \(D(e_x)=0\).

A finite matrix algebra is different:

\[
\delta_P(O)=i[P,O]
\]

obeys the Leibniz rule exactly.

### Design consequence

Do not discretize spacetime points first and then demand exact HDA.

Use finite noncommutative quantum algebra / rewrite structure and let approximately commuting geometry emerge.

### Verdict

**KILLED:** exact microscopic continuum HDA on an ordinary finite point lattice.

---

## 11. Frame/torsion pivot

A metric-only description pays a derivative-counting penalty. Frame variables offer a one-derivative field strength:

\[
T\sim \partial E.
\]

Therefore

\[
T^2\sim k^2
\]

can support relativistic stiffness.

A \(3\times3\) frame contains 9 components; internal rotations remove 3, leaving the 6 metric components.

\[
q_{ij}=E_i{}^aE_j{}^b\gamma_{ab}.
\]

Adding 3 spatial and 1 scalar gravitational constraints gives

\[
9-3-3-1=2.
\]

---

## 12. TEGR selection

For the parity-even torsion family

\[
L=c_1T^\rho{}_{\mu\nu}T_\rho{}^{\mu\nu}
+c_2T^\rho{}_{\mu\nu}T^{\nu\mu}{}_\rho
+c_3T^\rho{}_{\mu\rho}T^{\sigma\mu}{}_\sigma,
\]

unwanted vector and antisymmetric kinetic sectors have coefficients

\[
A_V=2c_1+c_2+c_3,\qquad
A_A=2c_1-c_2.
\]

Eliminating both gives

\[
c_2=2c_1,\qquad c_3=-4c_1,
\]

so

\[
(c_1,c_2,c_3)\propto(1,2,-4).
\]

### Verdict

**DERIVED under the stated DOF conditions:** the parity-even frame/torsion family collapses to the TEGR ray.

**ESTABLISHED:** TEGR is dynamically equivalent to GR up to a boundary term.

---

## 13. HDA target and why the same metric matters

Normal deformations of an embedded hypersurface obey

\[
[\delta_N,\delta_M]=\delta_\xi,
\]

with

\[
\xi^i=q^{ij}(M\partial_jN-N\partial_jM).
\]

The canonical target is

\[
[H[N],H[M]]
\rightarrow
D[q^{ij}(N\partial_jM-M\partial_jN)].
\]

The critical condition is not merely “some HDA-like algebra.” The **same** \(q^{ij}\) must control:

1. tensor propagation;
2. normal-normal deformation closure.

Once one healthy massless spin-2 field with the correct deformation/gauge algebra is obtained, established consistency results heavily constrain the two-derivative nonlinear completion toward Einstein gravity.

---

# PART IV — NEWTON COUPLING, CAPACITY AND COVARIANCE

## 14. Newton’s constant is a response coefficient, not raw Hilbert dimension

The project explicitly killed

\[
G\sim \frac{a_*^2}{\log d}
\]

as a universal formula.

Systems with identical local dimension \(d\) can have completely different long-wavelength response.

The appropriate object is a geometric susceptibility/spectral moment. Schematically,

\[
c_R\sim\int d^4x\,x^2\langle\Theta(x)\Theta(0)\rangle_c+\text{contacts},
\]

or

\[
c_R\sim\int_0^\infty ds\,\frac{\rho_\Theta(s)}{s^2}+\text{contacts}.
\]

The effective action contains

\[
I_{\rm eff}=c_R\int\sqrt g\,R+\cdots,
\qquad
c_R=\frac{1}{16\pi G}.
\]

### Sign

Microscopic spectral positivity alone does not guarantee \(c_R>0\), but a healthy physical TT graviton requires positive kinetic energy:

\[
c_R>0.
\]

### Verdict

**SURVIVING:** \(G\) is determined by long-wavelength geometric response, not “bits per site.”

---

## 15. Preferred-frame contamination

Condensed-matter analogues show that relativistic quasiparticles and induced geometric actions can emerge from nonrelativistic systems.

They also show the danger: the microscopic material may leave a timelike vector/foliation spurion in the IR.

The refined requirement is:

> no nonmetric preferred-frame spurion survives in the low-energy operator algebra.

A pure two-helicity spin-2 sector strongly restricts such contamination.

---

# PART V — ENTROPY, BOUNDARIES AND BLACK HOLES

## 16. The perturbative Hilbert space is not area-sized

A hoped-for unification failed.

If two genuine graviton modes survive per coarse bulk cell,

\[
\log\dim\mathcal H_{\rm graviton}(R)\propto V.
\]

Therefore GR constraints cannot simultaneously preserve local gravitons and make the entire perturbative Hilbert space scale with area.

Three notions must be separated:

1. vacuum entanglement can obey an area law;
2. perturbative physical/Fock space remains volume-extensive;
3. maximum entropy compatible with fixed semiclassical geometry is area-bounded because excessive energy/information backreacts.

### Verdict

**KILLED:** “holography means only area-many perturbative graviton states.”

---

## 17. Weak-gravity area bound

Relative entropy gives

\[
\Delta S\le\Delta\langle K\rangle.
\]

For a null/Rindler region,

\[
K=2\pi\int\lambda T_{kk}\,d\lambda\,dA.
\]

Einstein focusing converts the same energy moment into area change,

\[
2\pi\int\lambda T_{kk}
=
\frac{\Delta A}{4G},
\]

hence

\[
\Delta S\le\frac{\Delta A}{4G}.
\]

This is a downstream semiclassical relation once Einstein response is present; it is not a microscopic derivation of the number of black-hole states.

---

## 18. Boundary charges and the boost/area coefficient

The scalar constraint boundary term gives, with

\[
c_R=\frac{1}{16\pi G},
\]

a local boost charge variation

\[
\delta B_\Sigma=\frac{\delta A}{8\pi G}.
\]

For the modular boost generator

\[
K=2\pi B_\Sigma,
\]

\[
\delta K=\frac{\delta A}{4G}.
\]

The same \(c_R\) controlling bulk curvature response therefore fixes the semiclassical horizon boost/area response.

### Critical limitation

This does **not** count fundamental black-hole states.

The non-tautological strong-field test remains

\[
\lim_{A\gg a_*^2}\frac{\log\Omega_{\rm BH}(A)}{A}
\stackrel{?}{=}4\pi c_R.
\]

---

## 19. Moving-code theorem and zero static Love

For any smooth isolated projector family \(P(q)\),

\[
G_a=i[\partial_aP,P]
\]

generates local unitary motion:

\[
\partial_aP=-i[G_a,P].
\]

If a black-hole code orbit is isospectral,

\[
H(\lambda)=U(\lambda)H_0U^\dagger(\lambda),
\]

then spectral second-order response and the contact term cancel exactly at zero frequency:

\[
\chi(0)=0.
\]

Time-dependent motion still drives transitions, so finite-frequency absorption can remain.

### Verdict

**DERIVED structural mechanism:** zero static response is compatible with dynamical absorption in a finite moving-code system.

**OPEN:** reproduce the full physical Kerr/Schwarzschild response from one microscopic model.

---

## 20. MOTS correction: use a cross-Jacobian, not a symmetric susceptibility

The generic MOTS stability operator is non-self-adjoint because it contains normal-bundle drift.

A same-operator Hermitian equilibrium susceptibility is symmetric at \(\omega=0\) and cannot generically equal it.

The correct microscopic target is

\[
L^{\rm micro}_{xy}
=
\frac{\delta\Theta_x^+}{\delta b_y},
\]

where \(b_y\) is a normal-deformation variable and \(\Theta_x^+\) is an outgoing-expansion analogue.

For directed local couplings,

\[
L_{xy}=-w_{xy}e^{A_{xy}},\qquad A_{xy}=-A_{yx},
\]

and local normal-frame rescaling gives

\[
A_{xy}\rightarrow A_{xy}+f_x-f_y.
\]

This is the discrete connection transformation law. In the smooth limit it yields

\[
-(\nabla-X)^2+Q,
\]

the structural form of the generic MOTS stability operator.

### Verdict

**DERIVED structural bridge; OPEN microscopic origin.**

---

## 21. Horizon fold

For a nonlinear marginality equation

\[
\Theta[b,\mu]=0,
\]

with a simple zero mode at criticality, Lyapunov–Schmidt reduction gives

\[
a(\mu-\mu_c)+cA^2+\cdots=0.
\]

Hence

\[
A\sim|\mu-\mu_c|^{1/2},
\]

\[
s_{\min}(L)\sim|\mu-\mu_c|^{1/2},
\]

and

\[
\|L^{-1}\|\sim|\mu-\mu_c|^{-1/2}.
\]

### Verdict

**DERIVED generic normal-form result:** the \(1/2\) exponent should emerge from nonlinear marginality, not be fitted into a Kubo denominator.

---

# PART VI — V4 SU(2) NUMERICAL BRANCH

## 22. Test material

The V4 numerical model used finite even-rishon SU(2) quantum-link material on complete graphs.

The archived softness values are:

| Graph | \(\sigma_{\rm soft}\) |
|---|---:|
| K4 | 0.2500221817742957 |
| K5 | 0.2500067914741485 |
| K6 | 0.1890521106210234 |
| K7 | 0.1666732809348302 |
| K8 | 0.1389102561821202 |

See `data/K4_K8_SCALING.csv`.

### K7 mechanism diagnosis

The K7 detuning response was essentially

\[
\chi_{\rm uniform}(t)\propto t^{-0.9999998}.
\]

This is a conserved-sector \(k=0\leftrightarrow1\) Lehmann pole:

\[
\chi\sim\frac{1}{E_1-E_0}\sim\frac1t.
\]

It is **not** the nonlinear horizon fold.

### Verdict

**NUMERICAL:** the archived models soften and K7 has a clean \(1/t\) pole.

**KILLED:** interpreting that pole as the desired \(t^{-1/2}\) fold.

---

## 23. Late-V4 normalization audit

A later audit found a triangle/Wilson coefficient depending on global triangle enumeration/system size.

Therefore the K4–K8 decline cannot currently be used as clean homogeneous same-coupling finite-size scaling evidence.

### Important provenance rule

`data/BOUNDARY_VERDICT.json` is preserved as an earlier frozen boundary record, but its `homogeneous_across_sizes: true` metadata is **superseded** by the later normalization audit recorded in the V5 handoff.

The numerical values remain valid outputs of the archived Hamiltonians.

The strong scaling interpretation does not.

### Verdict

**DEMOTED / REQUIRES RERUN.**

---

## 24. V4 MOTS compatibility toy

The V4 reproducibility manifest records a deterministic compatibility toy with:

- near-zero baseline closure residual;
- injected controlled residual;
- critical eigenvalue near zero;
- fitted fold exponent \(\approx0.500004\).

See `data/v4_mots_bridge_manifest.json`.

The manifest itself explicitly states that this is a **compatibility/existence toy**. It does not derive the MOTS operator or fold from an independent microscopic Hamiltonian.

### Verdict

**VALIDATED TOY, NOT EMERGENCE EVIDENCE.**

---

# PART VII — V5: FINITE REFOLIATION AND THE SCALAR CONSTRAINT

## 25. Why V5 existed

At the V4→V5 boundary, most downstream structures had been reduced to known rigidity results or explicit finite constructions.

The sharp gap was:

\[
6-3=3
\]

instead of

\[
6-3-1=2.
\]

Where does the fourth, scalar/normal/refoliation redundancy come from **autonomously**?

---

## 26. Naive local clocks are insufficient

Putting one clock at every site does not automatically create refoliation gauge symmetry.

Different local update orders must describe the same physical history modulo spatial/frame gauge.

This turns the problem into a **diamond/path-independence** condition.

### Bare-diamond test

A completely free two-diamond amplitude model only constrains loop holonomies. It leaves local amplitudes underdetermined and does **not** select GR coefficients.

### Verdict

**KILLED:** bare path independence by itself as a GR selector.

See `scripts/02_minimal_diamond.py`.

---

## 27. Exact finite frame-dependent schedule holonomy

Finite update operators can satisfy exactly

\[
W_xW_yW_x^{-1}W_y^{-1}=G[Q],
\]

where \(G[Q]\) is a spatial-gauge move controlled by a finite frame variable.

This removes a basic algebraic obstruction: a finite-dimensional system can carry a field-dependent “normal-normal closes to spatial gauge” relation.

### Relational correction

A hand-made scalar \(Q\) is not enough. Replacing it with a rotational scalar such as

\[
Q_{12}=\mathbf S_1\cdot\mathbf S_2
\]

gives a relational spin-frame control variable with eigenvalues \(-2,-1,+1\).

### Verdict

**EXACT FINITE EXISTENCE.**

See `scripts/03_relational_spin_holonomy.py`.

---

## 28. The shear need not be a primitive many-body interaction

A static gapped mediator with simpler couplings produces at third order

\[
H_{\rm eff}^{(3)}
=
\frac{2g_1g_2g_3}{\Delta^2}\,Q\,n_cP_g.
\]

The explicit matrix test reproduces the term exactly in the perturbative expression.

### Verdict

**EXACT FINITE EXISTENCE:** no fundamental three-body locality obstruction.

**Not natural emergence:** the couplings are still designed.

See `scripts/04_static_mediator_gadget.py`.

---

## 29. The same frame supplies inverse-frame data

For three frame legs define

\[
C^i{}_a
=
\frac12\epsilon^{ijk}\epsilon_{abc}E_j{}^bE_k{}^c,
\]

and oriented volume

\[
v=
\frac16\epsilon^{ijk}\epsilon_{abc}
E_i{}^aE_j{}^bE_k{}^c.
\]

The exact symmetrized finite identity is

\[
\frac12\sum_a\{C^i{}_a,E_j{}^a\}
=
v\delta^i_j.
\]

Thus \(C^i{}_a\) is an exact finite densitized dual-frame object.

Classically,

\[
C^i{}_aC^j{}_a
=
\det(q)\,q^{ij}.
\]

### Verdict

**DERIVED / exact finite identity:** no independent inverse-metric register is required kinematically.

See `scripts/05_exact_cofactor_identity.py`.

---

## 30. Autonomous schedule frustration implies gauge invariance

A four-register finite model has schedule moves \(W_x,W_y\) with frame-dependent holonomy \(G_q\).

Use

\[
H_\diamond
=
J_x(I-W_x)+J_y(I-W_y),
\qquad J_x,J_y>0.
\]

Any zero-energy state satisfies

\[
W_x|\Psi\rangle=W_y|\Psi\rangle=|\Psi\rangle,
\]

hence automatically

\[
G_q|\Psi\rangle=|\Psi\rangle.
\]

For \(J_x=J_y=1\),

\[
\Delta=2-\sqrt2.
\]

More generally,

\[
\Delta(J_x,J_y)=J_x+J_y-\sqrt{J_x^2+J_y^2}>0
\]

throughout the positive quadrant.

### Verdict

**EXACT FINITE AUTONOMOUS MECHANISM:** schedule zero-frustration can force spatial-gauge invariance without a separate gauge projector.

See `scripts/06_autonomous_schedule_holonomy.py`.

---

## 31. Background-free inverse-metric uniqueness

Seek a local, derivative-free, parity-even \(M^{ij}(E)\) with two contravariant spatial indices, invariant under internal \(SO(3)\), using no background spatial metric.

At lowest polynomial order one needs two cofactor legs.

The possible internal \(\delta\)-pairings reduce to one nonzero symmetric tensor:

\[
M^{ij}\propto C^i{}_aC^j{}_a.
\]

Therefore

\[
M^{ij}\propto \det(q)\,q^{ij}.
\]

After density normalization the unique lowest-order map is

\[
M^{ij}\propto q^{ij}.
\]

### Verdict

**DERIVED rigidity statement:** once a nondegenerate relational frame is the only local geometry, the HDA tensor slot is not arbitrary.

See `scripts/07_inverse_metric_uniqueness.py`.

---

## 32. Nonbinary/general finite holonomy

The finite schedule construction is not restricted to a bit-valued geometry.

For any finite-dimensional frame/gauge unitary \(G(E)\) with a physical fixed subspace, controlled schedule moves give an exact frame-dependent diamond holonomy.

### Verdict

**EXACT FINITE EXISTENCE:** no binary-spectrum obstruction.

See `scripts/08_arbitrary_frame_holonomy.py`.

---

## 33. Nondegenerate frame = constant-rank gauge fiber

Let

\[
Q^{ij}\in{\rm Mat}_{3\times3}(\mathbb Z_p)
\]

control three spatial gauge translations.

The common fixed-space dimension is

\[
\dim\mathcal H_{\rm fixed}
=
p^{3-\operatorname{rank}Q}.
\]

For \(Q\in GL(3,p)\),

\[
\dim\mathcal H_{\rm fixed}=1.
\]

For degenerate \(Q\), extra invariant states appear.

The exhaustive \(p=3\) count gives:

| rank \(Q\) | number of matrices | fixed-space dimension |
|---:|---:|---:|
| 3 | 11232 | 1 |
| 2 | 8112 | 3 |
| 1 | 338 | 9 |
| 0 | 1 | 27 |

### Interpretation

Gapping degenerate frames keeps the protected physical fiber at constant rank.

### Verdict

**EXACT FINITE RESULT.**

See `scripts/09_nondegenerate_gauge_fiber.py`.

---

## 34. Exact finite lapse wedge

On one oriented edge, a finite group commutator gives exactly

\[
g_i\mapsto
g_i+
Q^{ij}(N_xM_y-M_xN_y).
\]

For \(y=x+a\hat e_j\),

\[
N_xM_y-M_xN_y
=
a(N\partial_jM-M\partial_jN)+O(a^2).
\]

Hence the finite law tends to

\[
\xi^i
=
q^{ij}(N\partial_jM-M\partial_jN).
\]

The included test exhausts all \(5^5=3125\) basis states and all \(25^2=625\) ordered lapse pairs per state for a nontrivial \(Q\).

### Verdict

**EXACT FINITE ALGEBRA:** the antisymmetric lapse wedge need not be inserted only at continuum level.

See `scripts/10_exact_lapse_wedge.py`.

---

## 35. Spatial covariance of the finite structure function

Under

\[
A\in GL(3,\mathbb Z_p),
\]

take

\[
Q\to AQA^T,\qquad
\alpha\to A^{-T}\alpha,\qquad
g\to Ag.
\]

Then exactly

\[
S_A G_Q(\alpha)S_A^{-1}
=
G_{AQA^T}(A^{-T}\alpha).
\]

### Verdict

**EXACT FINITE COVARIANCE:** the structure function transforms in the correct tensor slot.

See `scripts/11_finite_spatial_covariance.py`.

---

## 36. Associative finite HDA cocycle group

Define

\[
\omega_Q^i(N,M)
=
\sum_jQ^{ij}
(N_{j,0}M_{j,1}-M_{j,0}N_{j,1}).
\]

Because \(\omega\) is alternating and bilinear, it obeys the 2-cocycle identity.

For odd \(p\),

\[
(N,g)\star(M,h)
=
\left(
N+M,\,
g+h+\frac12\omega_Q(N,M)
\right)
\]

is an associative finite group with commutator

\[
[(N,0),(M,0)]
=
(0,\omega_Q(N,M)).
\]

### Verdict

**EXACT FINITE KINEMATIC EXISTENCE:** the discrete normal-normal law can be a bona-fide associative finite group structure, not just one hand-picked circuit identity.

See `scripts/12_finite_hda_cocycle.py`.

---

## 37. TT/refoliation coexistence

Let two soft TT modes mix derivatively with a gapped schedule/scalar/vector/defect sector:

\[
\mathcal H(k)
=
\begin{pmatrix}
c^2k^2I_2 & kB\\
kB^\dagger & M^2
\end{pmatrix}.
\]

Integrating out gapped modes gives

\[
\mathcal H_{\rm eff}^{TT}
=
k^2[c^2I_2-BM^{-2}B^\dagger]+O(k^4).
\]

A sufficient open-region condition is

\[
\|BM^{-1}\|_2^2<c^2.
\]

The deterministic included example preserves two positive \(k^2\) tensor eigenvalues while all hard modes remain gapped.

### Verdict

**DERIVED open-region compatibility:** adding a gapped schedule/refoliation sector does not generically reintroduce a soft scalar.

See `scripts/13_tt_schedule_coexistence.py`.

---

## 38. Exact finite canonical frame momentum and DeWitt selection

Finite dimension cannot realize the literal CCR \([q,p]=iI\), but it can realize the exponentiated finite Weyl/Clifford phase space.

On a three-site \(\mathbb Z_5\) regulator with six symmetric metric components/site, use the exact canonical shear

\[
h_{ij}\mapsto
h_{ij}
+
\pi_{ij}
-\lambda\delta_{ij}\pi,
\qquad
\pi^{ij}\mapsto\pi^{ij}.
\]

Every \(\lambda\) defines a finite canonical shear.

Now require scalar-constraint preservation inside the momentum-constraint ideal.

Exact rank test:

| \(\lambda\) mod 5 | augmented rank | preserves ideal? |
|---:|---:|---|
| 0 | 8 | no |
| 1 | 8 | no |
| 2 | 8 | no |
| 3 | 6 | **yes** |
| 4 | 8 | no |

Since

\[
2\cdot3=1\pmod5,
\]

\[
3=\frac12\pmod5.
\]

### Verdict

**EXACT FINITE REGULATOR:** the finite canonical theory uniquely selects the DeWitt trace coefficient within the tested family.

See `scripts/14_finite_dewitt_selection.py`.

---

## 39. Finite quantum stabilizer version

Exponentiate the finite scalar and momentum constraints into generalized-Pauli/Weyl stabilizers.

They form a commuting finite stabilizer code.

Under the finite Clifford DeWitt-family shear, the stabilizer row space is preserved only for

\[
\lambda=\frac12.
\]

Wrong trace coefficients add new independent stabilizer directions: the normal schedule step leaves the protected code.

### Verdict

**EXACT FINITE QUANTUM SELECTION:** within the prescribed gravitational constraint code, frustration-free schedule propagation selects DeWitt.

### Critical limitation

The constraint code itself was still prescribed.

This is **not** yet natural emergence.

See `scripts/15_stabilizer_dewitt_history.py`.

---

# PART VIII — ADVERSARIAL AUDIT

## 40. Obvious objection: “Spacetime as QEC is not new”

Correct.

Bulk locality as quantum error correction is established holographic territory (ADH, HaPPY and successors).

The project’s narrower target is a **dynamical, geometry-dependent code phase** in which the same collective frame appears in propagation and HDA and exactly two TT modes survive.

No originality claim should be made for the broad slogan.

---

## 41. Objection: Weinberg–Witten / emergent-gravity no-go results

The project does not assume an ordinary local relativistic microscopic QFT whose composite stress tensor produces gravity.

The intended escape route is:

- microscopic kinematics need not coincide with emergent spacetime locality;
- Lorentz/diffeomorphism structure is emergent;
- the gravitational Hamiltonian/boundary structure differs from ordinary local microscopic QFT.

This avoids a trivial contradiction, but it does **not** prove the desired phase exists.

---

## 42. Objection: exact finite HDA is impossible

On an ordinary finite commutative point lattice, exact continuum derivations are indeed obstructed.

V5 therefore does not claim an exact finite representation of the full nonlinear continuum HDA on fixed points.

What is claimed more narrowly is:

- exact finite schedule/gauge group relations exist;
- the discrete lapse wedge exists;
- the frame-dependent tensor map exists;
- their collective/continuum limit has the correct HDA slot;
- fully dynamical \(Q\) and natural phase emergence remain the final challenge.

---

## 43. Objection: “You inserted GR into the constraints”

This is currently the decisive objection.

V5.14/V5.15 show:

> **if** the scalar/momentum protected code exists, finite schedule propagation selects the DeWitt branch.

They do **not** show why the microscopic Hamiltonian naturally forms that code.

An exact parent Hamiltonian explicitly built from those stabilizers would merely compile GR into its ground space.

The project therefore stops short of calling that emergence.

---

## 44. Objection: numerical scaling was cherry-picked

The repository preserves the K4–K8 values **and** the later coupling-normalization flaw.

The old values are not erased.

The strong finite-size-scaling interpretation is demoted until a corrected homogeneous sequence is rerun.

This is deliberate falsification discipline.

---

## 45. Objection: the \(1/t\) singularity was called a black-hole fold

It was initially investigated as a possible critical response, then explicitly diagnosed as the wrong mechanism.

The K7 response is a conserved-sector Lehmann pole.

The desired fold requires a nonlinear marginal branch and simple zero mode.

The distinction is retained in the archive.

---

## 46. Objection: horizon area law was “derived” by assuming GR

The semiclassical boost/area coefficient follows from the Einstein curvature coefficient and is therefore not an independent microscopic state-counting result.

The project explicitly separates:

1. semiclassical area variation/edge charge;
2. microscopic black-hole state count.

Only the second would be a strong-field microscopic test.

---

# PART IX — WHAT IS ACTUALLY NEW INSIDE THIS PROJECT?

Novelty has **not** been professionally established. The following should be described as project-specific constructions/derivations pending literature audit, not as published discoveries:

1. the particular chain combining relational finite frame holonomy, schedule zero-frustration and finite gauge closure;
2. the explicit tiny finite schedule-holonomy models used here;
3. the project’s finite \(\mathbb Z_p\) lapse-wedge/cocycle realization tied to a frame matrix \(Q^{ij}\);
4. the constant-rank gauge-fiber interpretation of nondegenerate \(Q\);
5. the exact finite-regulator / finite-stabilizer DeWitt-selection tests in this specific form;
6. the attempt to unify those pieces with the earlier moving-code Love/MOTS branch.

The following are **not ours** in their broad form:

- holographic QEC / spacetime-as-code;
- path independence / HDA;
- HKT/Teitelboim rigidity;
- finite spin models with helicity-\(\pm2\) modes;
- causal-set discrete general covariance;
- perturbative Hamiltonian gadgets;
- densitized triad/cofactor inverse-metric geometry;
- TEGR equivalence to GR;
- generic saddle-node square-root scaling.

---

# PART X — FINAL CLAIM LEDGER

## 47. Safe claims

1. Finite-dimensional quantum systems can carry the kinematic ingredients for relational frames, moving protected subspaces and tensor collective variables.
2. A finite constraint system can leave exactly two tensor modes.
3. Once the GR-like linear constraint ideal is assumed, minimal two-derivative propagation is rigid toward Fierz–Pauli/DeWitt.
4. Under stated unwanted-mode conditions, the parity-even torsion family selects the TEGR ray.
5. Exact finite schedule/gauge algebras with frame-dependent holonomy exist.
6. The antisymmetric lapse wedge and inverse-metric tensor slot admit exact finite precursors.
7. Nondegenerate finite frame matrices naturally keep the gauge-fixed fiber at constant rank in the tested construction.
8. A finite Weyl/Clifford regulator can carry frame-momentum dynamics and select the DeWitt coefficient through code/constraint preservation.
9. A gapped schedule sector can coexist with two soft TT modes over an open quadratic coupling region.
10. The moving-code isospectral mechanism permits zero static response with nonzero finite-frequency response.
11. A generic nonlinear marginal branch with a simple zero mode gives the square-root fold.

---

## 48. Claims that must NOT be made

- “GWXP proves quantum gravity.”
- “Finite information causes gravity.”
- “The SU(2) rishon Hamiltonian derives GR.”
- “K4–K8 proves a thermodynamic critical point.”
- “The V4 MOTS compatibility toy proves microscopic horizon emergence.”
- “The finite cocycle group is the full nonlinear quantum HDA.”
- “The DeWitt stabilizer test proves the scalar constraint emerged naturally.”
- “The black-hole entropy state count has been derived.”
- “The Standard Model, \(3+1\) dimensions, cosmological constant or arrow of time follows from finite information.”
- “The remaining phase-emergence problem is merely technical.”

---

# PART XI — THE ONE REMAINING THEOREM

## 49. Natural-emergence GWXP

The final research question is:

> **Does one simple autonomous finite local Hamiltonian possess a stable phase in which the relational nondegenerate frame, scalar/refoliation constraint code, HDA structure and exactly two \(z=1\) tensor modes appear together without those gravitational constraints being inserted by hand?**

That is now a **phase-diagram problem**, not another missing algebra identity.

A meaningful next project would:

1. choose a small symmetry-allowed microscopic Hamiltonian family without explicit GR stabilizers;
2. locate its phases numerically/analytically;
3. test whether a nondegenerate relational frame condenses;
4. measure the low spectrum and demand only two \(z=1\) tensor modes;
5. test emergence of the scalar/momentum constraint ideal;
6. compute the deformation algebra on the protected sector;
7. verify that the same metric controls propagation and closure;
8. only then reconnect the black-hole response branch.

If the constraints must be hand-built into the parent Hamiltonian, **natural-emergence GWXP fails**, even though the mathematical-existence architecture remains coherent.

---

# PART XII — REPRODUCIBILITY MAP

## 50. Automated tests in this package

Run:

```bash
python run_all_tests.py
```

The runner executes:

| Script | What it checks |
|---|---|
| `00_archive_integrity.py` | V4 numerical files and provenance/cautions |
| `01_core_rigidity.py` | FP/DeWitt/TEGR algebra and DOF count |
| `02_minimal_diamond.py` | bare diamond underdetermination + finite holonomy existence |
| `03_relational_spin_holonomy.py` | rotationally invariant spin-frame-controlled holonomy |
| `04_static_mediator_gadget.py` | perturbative generation of the shear interaction |
| `05_exact_cofactor_identity.py` | exact densitized dual-frame identity |
| `06_autonomous_schedule_holonomy.py` | schedule frustration ⇒ gauge invariance + open gap |
| `07_inverse_metric_uniqueness.py` | lowest-order background-free inverse-metric tensor uniqueness |
| `08_arbitrary_frame_holonomy.py` | nonbinary arbitrary finite holonomy carrier |
| `09_nondegenerate_gauge_fiber.py` | fixed-space dimension vs rank \(Q\) |
| `10_exact_lapse_wedge.py` | exhaustive finite lapse-wedge identity |
| `11_finite_spatial_covariance.py` | \(GL(3,p)\) covariance |
| `12_finite_hda_cocycle.py` | cocycle identity, associativity and commutator |
| `13_tt_schedule_coexistence.py` | open-region TT/schedule stability |
| `14_finite_dewitt_selection.py` | exact finite canonical DeWitt selection |
| `15_stabilizer_dewitt_history.py` | finite quantum code preservation only at \(\lambda=1/2\) |

Requirements:

```text
numpy
sympy
```

---

## 51. Archive files

`archive/` contains the historical documents used to reconstruct the research path:

- `Cosmic_Glue_V3_Handoff_for_V4.docx`
- `cosmic_glue_conversation_part_2.docx`
- `GWXP_V5_Research_Handoff.docx`
- `GWXP_README_FULL_legacy.md`

`data/` contains preserved V4 numerical/provenance files:

- `K4_K8_SCALING.csv`
- `BOUNDARY_VERDICT.json`
- `v4_mots_bridge_manifest.json`
- `v4_mots_bridge_tables.tex`

`docs/v5/` contains the V5 stepwise verdict files.

---

# PART XIII — LITERATURE BOUNDARY

This is a minimal set of comparison points, not a complete bibliography.

1. A. Almheiri, X. Dong, D. Harlow, **Bulk Locality and Quantum Error Correction in AdS/CFT**, JHEP 2015, 163. DOI: 10.1007/JHEP04(2015)163.
2. F. Pastawski, B. Yoshida, D. Harlow, J. Preskill, **Holographic quantum error-correcting codes: toy models for the bulk/boundary correspondence**, JHEP 2015, 149. DOI: 10.1007/JHEP06(2015)149.
3. C. Teitelboim, **How commutators of constraints reflect the spacetime structure**, Ann. Phys. 79 (1973) 542–557. DOI: 10.1016/0003-4916(73)90096-1.
4. S. A. Hojman, K. Kuchař, C. Teitelboim, **Geometrodynamics Regained**, Ann. Phys. 96 (1976) 88–135. DOI: 10.1016/0003-4916(76)90112-3.
5. Z.-C. Gu, X.-G. Wen, **Emergence of helicity ±2 modes (gravitons) from qubit models**, Nucl. Phys. B 863 (2012) 90–129. DOI: 10.1016/j.nuclphysb.2012.05.010.
6. D. Marolf, **Emergent Gravity Requires Kinematic Nonlocality**, Phys. Rev. Lett. 114, 031104 (2015). DOI: 10.1103/PhysRevLett.114.031104.
7. D. P. Rideout, R. D. Sorkin, **Classical sequential growth dynamics for causal sets**, Phys. Rev. D 61, 024002. DOI: 10.1103/PhysRevD.61.024002.
8. T. Thiemann, **Non-degenerate metrics, hypersurface deformation algebra, non-anomalous representations and density weights in quantum gravity**, Gen. Relativ. Gravit. 56, 122 (2024). DOI: 10.1007/s10714-024-03313-w.
9. R. Srivastava, S. Surya, **Implementing Bell causality in Quantum Sequential Growth**, arXiv:2603.25503 (2026).
10. S. P. Jordan, E. Farhi, **Perturbative gadgets at arbitrary orders**, Phys. Rev. A 77, 062329 (2008). DOI: 10.1103/PhysRevA.77.062329.

Literature references are included to define prior art and constraints, not as evidence that GWXP itself is correct.

---

# 52. Final one-paragraph position

The research began with “finite information shortage causes gravity” and repeatedly tried to kill its own replacements. What survived is a much narrower proposition: finite quantum systems appear capable of carrying the **architecture** needed for an emergent gravitational code phase, and once the correct constraint/refoliation structure is present, multiple independent rigidity calculations push the low-energy theory strongly toward GR. V4 and V5 removed several apparent algebraic obstructions and found exact finite carriers for schedule/refoliation closure and DeWitt-compatible dynamics. The project still lacks the decisive result: a simple microscopic Hamiltonian that *naturally chooses* that complete phase rather than having the gravitational code inserted into it. Until that exists, GWXP is a structured, falsifiable research program—not a derivation of gravity.

---

# PART VII — V6 NATURAL EMERGENCE / AUTONOMOUS GEOMETRY UPDATE
## 28 September 2026

This part updates — but does not erase — the V5 endpoint.

At the end of V5, the dominant unresolved question was:

```text
Can one simple autonomous finite Hamiltonian naturally realize
the nondegenerate geometry + local scalar/refoliation phase,
rather than having the gravitational code inserted by hand?
```

The September 28 benchmark does **not** fully close that theorem. It does, however, replace a purely open placeholder with a concrete candidate phase and two deterministic reproducibility scripts.

The evidence labels below retain the discipline used throughout this ledger.

---

## 53. Natural Emergence pivot: from site order to dynamical relations

### Initial Natural Emergence test

A finite `Z_p` clock/shift system was first tested on complete graphs.

Naive site-frame condensation produced nonzero order parameters and low-lying multiplets, but the obvious triangle interactions could explicitly break the symmetry being diagnosed.

### Correction

The parent Hamiltonian was forced to preserve the relevant global clock symmetry.

The site model then showed genuine collective ordering, but its neutral pair correlations remained essentially complete-graph-like.

### Verdict

**KILLED / DEMOTED:** site-clock condensation alone is not emergent space.

**SURVIVING DESIGN PRINCIPLE:** the microscopic variable should be a **relation/link degree of freedom**, not merely a site order parameter.

---

## 54. Exact valence-selection mechanism

Introduce binary/clock-derived link occupation `n_ij`, edge number

```math
m=\sum_{i<j}n_{ij},
```

and degrees

```math
d_i=\sum_{j\neq i}n_{ij}.
```

For

```math
H_{\rm deg}
=
\mu m
+
\lambda\sum_i{d_i\choose2},
```

the preferred valence is `k` throughout the open interval

```math
-2k\lambda<\mu<-2(k-1)\lambda.
```

At the center,

```math
\mu=-(2k-1)\lambda,
```

the energy square-completes:

```math
H_{\rm deg}
=
\frac{\lambda}{2}
\sum_i(d_i-k)^2
+\text{constant}.
```

### Verdict

**DERIVED:** finite valence is selected over an open coupling interval rather than imposed as a hard graph constraint.

**Important interpretation:** valence does not uniquely determine dimension.

---

## 55. Why the first graph parents failed

Several successive graph-selection mechanisms were tested and rejected or demoted.

### Pure degree + triangle terms

For `k=2`, connected two-regular graphs are cycles, giving a clean one-dimensional toy geometry.

For higher valence, every `k`-regular graph is initially degenerate.

**DEMOTED:** valence selection is not dimension selection.

### Determinant / connectivity term alone

A term such as

```math
-\kappa\log\det(\epsilon I+L_G)
```

helps suppress fragmentation but, at sufficiently large size, can favor globally over-mixed / expander-like graphs.

**DEMOTED:** determinant pressure alone does not generate local finite-dimensional geometry.

### Fixed all-loop reward alone

A reward based on

```math
{\rm Tr}\,e^{g\widetilde A}
```

encourages local closed-walk structure but can be gamed by modular and loop-congested graphs.

**DEMOTED:** loop abundance alone is not manifold structure.

### One-body spectral uniqueness

Cospectral non-isomorphic graphs (e.g. rook vs. Shrikhande-type examples) cannot be distinguished by arbitrary functions of the one-body adjacency/Laplacian spectrum.

**KILLED:** one-body spectral invariants can uniquely identify the microscopic relational geometry.

---

## 56. Frozen resource/capacity graph functional

The surviving benchmark combines:

1. valence/resource pressure;
2. triangle frustration;
3. all-walk communicability reward;
4. convex link-capacity cost;
5. weak infrared connectedness pressure.

The frozen effective graph functional is

```math
H=
H_{\rm degree}
+\tau T
-J\,{\rm Tr}\,e^{g\widetilde A}
+U\sum_{\langle ij\rangle}
[e^{g\widetilde A}]_{ij}^{\,2}
-\kappa\log\det(\epsilon I+\widetilde L),
```

where

```math
\widetilde A=D^{-1/2}AD^{-1/2},
\qquad
\widetilde L=I-\widetilde A.
```

### Prior-art boundary

The broad programme “permutation-invariant dynamical graph -> emergent low-dimensional locality” predates GWXP (Quantum Graphity and related work).

The matrix exponential `exp(A)` is also standard graph communicability.

The potentially narrower GWXP-specific mechanism is the **competition between all-walk communicability and convex finite link capacity**, together with the later generalized-dihedral deformation-algebra bridge.

### Verdict

**NUMERICAL / PARTIAL ANALYTIC:** candidate Natural Emergence parent.

**NOT ESTABLISHED:** novelty or global thermodynamic uniqueness.

---

## 57. Three-dimensional spectral phase

At the frozen benchmark point near

```math
g=6,\qquad U/J=0.018,
```

the deterministic benchmark gives:

```math
e_{\mathbb Z^3}
=
-8.155619787129...
```

for ordinary cubic geometry.

A generalized-dihedral rank-three phase gives:

```math
e_{\rm 3D}
=
-8.173368935008...
```

and low-energy integrated-density-of-states fitting gives approximately

```math
d_{\rm spec}
=
2.98.
```

A representative rank-four non-Abelian competitor is higher:

```math
e_{\rm rank\,4}
\approx
-7.99084.
```

### Interpretation

The energy search does not simply select the cubic micrograph.

The present candidate is a **three-dimensional spectral phase class** with multiple microscopic realizations.

### Verdict

**NUMERICAL:** reproducible three-dimensional candidate phase.

**OPEN:** global minimization over all admissible infinite graphs.

---

## 58. Finite cubic convergence

The deterministic benchmark reproduces the cubic sequence:

| `L` | `N=L^3` | energy density |
|---:|---:|---:|
| 4 | 64 | -7.790663183943 |
| 5 | 125 | -8.080318990472 |
| 6 | 216 | -8.137762589083 |
| 7 | 343 | -8.152143946492 |
| 8 | 512 | -8.155063476958 |
| 9 | 729 | -8.155542936584 |
| 10 | 1000 | -8.155609770459 |

toward the thermodynamic cubic value.

### Verdict

**NUMERICAL / DETERMINISTIC:** small periodic boxes have strong wraparound artifacts; cubic thermodynamic comparison must use the converged sequence rather than tiny tori.

---

## 59. Lower-dimensional quotients and decompactification

Rank-two quotient families can become arbitrarily close in energy to the rank-three phase only when the shortest integer relation among the apparent three directions becomes very long.

Representative excess energies in the deterministic quotient sweep fall rapidly with relation scale.

This has a clean geometric interpretation:

```text
globally lower-dimensional quotient
+
compactification relation length -> infinity
=
locally indistinguishable from the rank-three covering geometry
on every fixed finite radius.
```

### Verdict

**PARTIAL ANALYTIC / NUMERICAL:** fixed-scale lower-dimensional quotients lose in the tested window; near-degeneracy arises through decompactification.

**OPEN:** arbitrary non-translational lower-dimensional infinite graph classes.

---

## 60. Adversarial graph families tested

The Natural Emergence search explicitly tested or compared against:

- random regular graphs / expanders;
- triangle-free bipartite expanders;
- finite-width strips and slabs;
- generalized infinite tubes;
- modular complete-bipartite constructions;
- circulant Cayley graphs;
- Abelian lower-rank quotients;
- generalized-dihedral lower-rank quotients;
- regular-tree products;
- higher-rank generalized-dihedral competitors;
- symmetric block-design incidence graphs;
- irregular annealed square-complex-like graphs;
- local edge addition, deletion and rewiring defects.

### Verdict

**CAUTION:** this is a strong adversary suite, not a proof over all graphs.

---

## 61. Generalized-dihedral schedule algebra

The lower-energy rank-three candidate naturally carries reflection-like involutions `R_s`.

Exactly:

```math
R_s^2=1,
```

and

```math
R_sR_t=T_{s-t}.
```

Therefore

```math
R_sR_tR_sR_t
=
T_{2(s-t)}.
```

At generator level,

```math
[R_s,R_t]
=
T_{s-t}-T_{t-s}.
```

This supplies an exact finite algebraic ancestor of:

```text
normal deformation × normal deformation -> spatial deformation.
```

### Verdict

**EXACT FINITE IDENTITY.**

This is stronger than the earlier hand-built V5 schedule circuit in one important respect: the involutions are native to an independently selected low-energy relational graph phase.

---

## 62. Same tensor in propagation and the deformation commutator

For six reflection offsets `s_alpha`, define

```math
Q^{ij}
=
\frac12\,{\rm Cov}(s)^{ij}.
```

Equivalently,

```math
Q^{ij}
=
\frac1{72}
\sum_{\alpha<\beta}
(s_\alpha-s_\beta)^i
(s_\alpha-s_\beta)^j.
```

The low-momentum graph Laplacian satisfies

```math
L(k)
=
Q^{ij}k_i k_j
+
O(k^4).
```

For smeared normal/schedule generators,

```math
[H[N],H[M]]
=
\sum_{\alpha<\beta}
(N_\alpha M_\beta-M_\alpha N_\beta)
[K_\alpha,K_\beta].
```

Using

```math
N_\alpha=N(x+s_\alpha),
```

the continuum expansion gives

```math
N_\alpha M_\beta-M_\alpha N_\beta
=
-(s_\alpha-s_\beta)^j
(N\partial_jM-M\partial_jN)
+O(a^2),
```

while

```math
T_{s_\alpha-s_\beta}
-
T_{s_\beta-s_\alpha}
=
2(s_\alpha-s_\beta)^i\partial_i
+O(a^3).
```

Thus, after the overall normal-generator normalization is fixed,

```math
[H[N],H[M]]
\longrightarrow
D\!\left[
Q^{ij}
(N\partial_jM-M\partial_jN)
\right].
```

### Verdict

**DERIVED CONTINUUM BRIDGE:** the same displacement covariance tensor controls propagation and the normal-normal structure function in the all-reflection phase.

---

## 63. Direct real-space continuum convergence

The bridge script tests the exact discrete commutator on smooth periodic fields against the Lie derivative on a half-density,

```math
{\cal L}^{(1/2)}_\xi\psi
=
\xi^i\partial_i\psi
+
\frac12(\partial_i\xi^i)\psi,
```

with

```math
\xi^i
=
\frac16\delta^{ij}
(N\partial_jM-M\partial_jN).
```

Results:

| `L` | fitted coefficient | relative residual |
|---:|---:|---:|
| 16 | 0.982606102 | 0.025700385 |
| 24 | 0.992187757 | 0.011312962 |
| 32 | 0.995589552 | 0.006341877 |
| 48 | 0.998034703 | 0.002811719 |
| 64 | 0.998893517 | 0.001580233 |

### Verdict

**NUMERICAL / DETERMINISTIC:** direct continuum convergence toward the predicted deformation action.

---

## 64. Autonomous local schedule/reconnection sector

Consider four vertices and six link qubits:

```math
H=
\frac12\sum_i(d_i-1)^2
-\Gamma\sum_eX_e.
```

At `Gamma=0`, the ground manifold contains exactly the three perfect matchings.

No matching-exchange gate is inserted.

The first matching-to-matching tunnelling occurs at fourth order.

Summing all virtual paths gives exactly

```math
t=20\Gamma^4.
```

The matching representation decomposes

```math
\mathbf3=\mathbf1\oplus\mathbf2,
```

with splitting

```math
\Delta_{\rm schedule}
=
60\Gamma^4
+
O(\Gamma^6).
```

Exact diagonalisation reproduces the perturbative coefficient.

### Verdict

**EXACT + NUMERICAL:** a local schedule/reconnection manifold can arise autonomously from generic link flips.

**OPEN:** extended gluing into the complete first-class gravitational constraint phase.

---

## 65. Soft spatial band and fiber-odd gap

The all-reflection bipartite structure has normalized adjacency bands

```math
\lambda_\pm(k)
=
\pm\frac{|f(k)|}{6},
```

and Laplacian bands

```math
\ell_\pm(k)
=
1\mp\frac{|f(k)|}{6}.
```

At `k=0`:

```math
\ell_+(0)=0.
```

The fiber-odd band remains finite under the benchmark normalization.

### Verdict

**EXACT FOR THE BENCHMARK GRAPH.**

### Critical interpretation warning

**DO NOT IDENTIFY THIS GAP DIRECTLY WITH THE HAMILTONIAN CONSTRAINT.**

A gapped physical fiber mode and a first-class gauge redundancy are not the same thing.

The significance is only that the geometric phase naturally provides a soft spatial branch plus a separated local fiber branch compatible with the qualitative architecture required by the earlier V5 programme.

---

## 66. Revised project-level status after Natural Emergence benchmark

### Previously

V5 ended with:

```text
finite HDA / frame / DeWitt architecture exists
BUT
natural emergence of the required phase is completely open.
```

### Now

The sharper status is:

```text
permutation-invariant dynamical graph
        |
        v
candidate stable 3D spectral phase
        |
        +--> native involutive local schedule algebra
        |       |
        |       v
        |   normal-normal -> spatial translation
        |       |
        |       v
        |   same Q^ij as IR propagation
        |
        +--> local schedule/reconnection tunnelling can arise
             autonomously from generic link flips

PLUS earlier V5 rigidity:
constraint phase
   -> Fierz-Pauli
   -> DeWitt lambda=1/2
   -> TEGR ray
   -> 2-TT-compatible IR
```

### Remaining decisive integration theorem

The project still must show, from **one microscopic parent Hamiltonian**, that the thermodynamic low-energy phase simultaneously contains:

1. autonomous nondegenerate relational geometry;
2. spatial and scalar first-class gravitational constraints;
3. local refoliation redundancy;
4. HDA closure on the same emergent metric;
5. exactly two healthy `z=1` tensor modes;
6. no extra scalar/vector/aether modes.

### Verdict

**MAJOR PROGRESS, NOT COMPLETION.**

Natural Emergence is no longer an empty missing box, but the final one-parent-Hamiltonian integration remains open.

---

## 67. New reproducibility files

The September 28 update adds:

```text
scripts/gwxp_natural_emergence_benchmark.py
scripts/gwxp_schedule_hda_bridge.py
```

The first deterministically reproduces:

- cubic thermodynamic energy;
- generalized-dihedral rank-three energy;
- spectral-dimension estimate;
- cubic finite-size convergence;
- lower-rank quotient / decompactification behaviour;
- representative higher-rank comparison.

The second deterministically reproduces:

- the three perfect matchings;
- exact fourth-order coefficient `20 Gamma^4`;
- schedule splitting `60 Gamma^4`;
- generalized-dihedral reflection commutator;
- equality between covariance and commutator metric tensors;
- Laplacian Hessian;
- soft/fiber-odd band separation;
- direct real-space HDA continuum convergence.

---

## 68. Updated final one-paragraph position

The project began with a vague “finite information shortage causes gravity” idea and repeatedly destroyed its own stronger interpretations. What survives is much narrower and more technical. Earlier work established finite carriers for two-tensor kinematics, frame geometry, inverse-metric structure, exact finite schedule holonomy, DeWitt-compatible canonical dynamics, Fierz–Pauli / TEGR rigidity, moving-code static-response cancellation and a corrected horizon-stability target. The September 2026 Natural Emergence benchmark now adds reproducible evidence that a permutation-invariant dynamical relation network can select a three-dimensional spectral phase and that a native generalized-dihedral involution algebra can reproduce the normal-normal-to-spatial deformation structure using the same tensor that controls long-wavelength propagation. The decisive theorem is still missing: all of those ingredients must arise together as one autonomous thermodynamic gravitational phase of a single microscopic Hamiltonian. Until that is demonstrated, GWXP remains a structured, falsifiable research programme rather than a proved theory of quantum gravity.
