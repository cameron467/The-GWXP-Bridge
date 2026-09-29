# GWXP — Research Checkpoint — 29 September 2026

> **Status:** pre-handoff research checkpoint, not a final theory claim.  
> **Purpose:** freeze the current state after a major graph-phase / locality / kinetics audit so that later work cannot silently overwrite corrections, failed branches, or provenance.

---

## 1. Executive status

GWXP is now best described as a **finite relational emergent-gravity research programme with several exact finite constructions and a nontrivial graph-phase candidate**, but **not yet a derivation of GR from finite information**.

The strongest current result is that the graph-only parent has repeatedly shown an energetic drive away from generic expander-like degree-6 graphs toward a relation-rich, structurally disordered, approximately three-dimensional regime **without external coordinates or an explicit target dimension**. At the corrected working point

```text
degree k = 6
g        = 2.0
U        = 0.100
kappa    = 0.30
epsilon  = 0.025
tau      = 5
```

blind parent-energy descent at `N=216` crossed the tested rank-2 Cayley competitor while retaining approximately 3D heat-kernel behaviour. A fully unrestricted `N=344` blind trajectory, after removal of a hidden hard locality filter, also crossed the tested same-size rank-2 adversary.

The graph phase is therefore no longer merely an externally seeded existence result. However, **thermodynamic 3D selection is not proved**: the autonomous `N=344` trajectory has not yet been shown to settle into the mature local 3D basin with all scaling observables stabilized, and the broader one-parent integration theorem remains open.

---

## 2. Major results locked in at this checkpoint

### 2.1 Corrected graph-phase working point

The old `g=3, U=0.106, kappa=0.08` point is not a safe final point because a rank-2 Cayley competitor can beat it. The active graph-phase work has moved to the corrected `g=2, U=0.100, kappa=0.30, epsilon=0.025, tau=5` region.

### 2.2 Relation condensation has an analytic parent-energy driver

For a triangle-free degree-`d` regular graph, the leading `C4` reaction-coordinate contribution is

```text
Tr A^4 / N = d(2d-1) + 8 c4,
```

with `c4 = C4/N`.

At the corrected `g=2, U=.100, kappa=.30, epsilon=.025, d=6` point, the leading coefficient of `c4` is negative, so the parent itself rewards initial short-relation / 4-cycle condensation. This is a parent-energy statement, not a proposal heuristic.

### 2.3 N=216 autonomous accessibility — passed numerically

Starting from a generic triangle-free random 6-regular graph and using random legal 2-switches with **acceptance based only on the parent energy**, the trajectory moved from expander-like structure into a relation-rich low-dimensional state.

The corrected long run crossed the tested rank-2 control while retaining approximately 3D heat-kernel behaviour. The important qualitative result is:

```text
generic graph
  -> relation condensation
  -> spectral-gap reduction
  -> d_s approaches ~3
  -> energy below tested rank-2 competitor
```

without `C4`, dimension, curvature, gap, or isotropy steering.

### 2.4 N=344 unrestricted blind descent — rank-2 crossing survives removal of hard locality

A hidden issue was found in an earlier `N=344` proposal generator: candidate rewires were required to be local within a hard relational-radius condition. This was not acceptable as final emergence evidence.

The locality filter was removed completely. In the corrected unrestricted run:

- rewires were not filtered by graph distance;
- triangle-producing moves could be proposed and were rejected, when appropriate, by the actual `tau=5` parent energy;
- no geometric observable was used in acceptance.

The unrestricted trajectory subsequently crossed the tested same-size rank-2 adversary while remaining non-rank-2 in its spectral behaviour.

**Status:** strong numerical evidence that the hard `r<=3` cutoff is not required for the graph energy to defeat the tested rank-2 state. Arrival at the mature local 3D basin remains open.

### 2.5 Higher-order rewire correction

A prior `k=3` proposal routine allowed some nominal 3-edge events to re-add one removed edge. Two accepted events previously counted as genuine `k=3` moves were therefore only `k=2 + spectator` moves.

A stricter connected alternating-cycle generator fixed this.

Result: genuine `k=3` moves exist and can be downhill, but controlled comparisons did **not** show a special `k=3` un-jamming advantage over ordinary `k=2` rewires. The stronger claim that rare 3-switch tunnelling is the nucleation mechanism is therefore **demoted**.

### 2.6 Universal low-order 2-switch amplitude survives

The strong-valence perturbative result

```text
|t_switch| = 20 Gamma^4 / lambda^3
```

remains the established leading amplitude for a degree-preserving 2-switch. Higher-`k` amplitude formulas explored later are not promoted to the same status without an independent general proof.

---

## 3. Locality / mediator audit — major correction

### 3.1 Uniform all-edge driver remains unsuitable as the final metric driver

A uniform `-Gamma sum X_ij` driver has `O(N^2)` channels with no relational suppression. It therefore does not provide a physically satisfactory graph-local causal structure.

### 3.2 Hard `r=3` locality is not fundamental

The hard radius rule is retained only as a historical diagnostic. The intended final mechanism is soft relational locality generated by a gapped mediator.

### 3.3 Old multiplicative common-graph mediator — demoted

The previous symmetric common-graph amplitude

```text
t_GG' ~ sqrt[
  R_C(a,b) R_C(c,d) R_C(a,c) R_C(b,d)
]
```

is Hermitian, but a finite-size audit found a bootstrap/freezing problem: on generic graphs the absolute hopping strength falls rapidly with `N` because the removed-edge endpoints must also be connected through short alternate paths in the common graph.

This version is therefore **demoted as a thermodynamic nucleation driver**.

### 3.4 Heuristic square-root additive kernel — demoted

An additive source/target square-root kernel improved the scaling behaviour, but no comparably clean microscopic derivation was found. It should not be treated as fundamental.

### 3.5 Pair-mediator construction — exact finite constructive result

A cleaner microscopic realization uses a gapped pair mediator with

```text
h_G = I - rho A_G,
H_chi(G) = Delta (h_G tensor h_G),
0 < rho < 1/6.
```

Then

```text
H_chi(G)^(-1) = (1/Delta) R_G tensor R_G,
R_G = (I-rho A_G)^(-1).
```

Eliminating the mediator by a finite Schur/Feshbach reduction gives the Hermitian graph-to-graph hopping

```text
<G'|H_eff|G>
 = -(gamma^2 / 2 Delta) [
     R_G(a,c) R_G(b,d)
   + R_G'(a,b) R_G'(c,d)
   ].
```

The two terms exchange under `G <-> G'`, so Hermiticity is exact. A direct finite Hamiltonian check matched the analytic effective matrix element to machine precision.

**Status:** exact finite constructive realization of a soft relational `H_med` sector. It is not yet shown to be uniquely forced by the bare valence/link-flip parent; the existence of a gapped mediator sector remains a microscopic model choice.

---

## 4. Critical conceptual correction: annealing is not the final dynamics

The project has used zero-temperature parent-energy descent extensively because it is an efficient way to map the graph-energy landscape and test accessibility.

That should no longer be described as the literal microscopic dynamics.

The physical candidate is now schematically

```text
H_total = H_graph + H_med + H_sched + H_mix + matter/cell sector,
```

where:

- `H_graph` supplies the diagonal graph-energy landscape;
- `H_med` supplies Hermitian graph-configuration hopping amplitudes;
- `H_sched` and `H_mix` carry the schedule / closure sector;
- the matter sector is built from the same incidence complex.

The next physically meaningful graph-phase test is therefore a finite **combined quantum Hamiltonian** calculation, not another classical optimizer benchmark alone.

---

## 5. What is currently established / conditional / open

### ESTABLISHED / EXACT FINITE

- finite two-mode spin-2 kinematic constructions;
- Fierz–Pauli / linearized-Einstein rigidity under the stated constraint-preservation assumptions;
- DeWitt `-1/2` trace coefficient rigidity under the stated assumptions;
- TEGR coefficient ray under the stated degree-of-freedom conditions;
- finite schedule/refoliation and lapse-wedge constructions;
- incidence identity and the exact finite `z=1` matter carrier;
- universal leading 2-switch amplitude `20 Gamma^4/lambda^3`;
- exact finite pair-mediator realization of a Hermitian soft-local graph hopping kernel.

### STRONG NUMERICAL EVIDENCE

- parent-driven relation condensation from generic degree-6 graphs;
- autonomous `N=216` access to a low-dimensional basin below the tested rank-2 control;
- unrestricted `N=344` descent below the tested same-size rank-2 control;
- approximately 3D spectral / ball-growth behaviour in the mature amorphous candidate basin;
- structural disorder rather than a relabelled cubic crystal.

### OPEN / NOT YET PROVED

- an open thermodynamic coupling region whose global low-energy phase is uniquely the amorphous 3D phase against a sufficiently broad adversary family;
- autonomous `N=344` arrival at the mature local 3D basin under the corrected kinetics;
- the low-energy state of the **combined** `H_graph + H_med` quantum configuration-space Hamiltonian;
- actual downfolded `K_eff^{ijkl}` with vanishing rank-4 anisotropy in the corrected autonomous phase;
- local `H_mix` closure tests on the corrected phase;
- matter-cell curl-gap scaling on autonomous basins;
- one-parent extended first-class scalar/spatial constraint phase;
- absence of extra gapless scalar/vector modes after the full parent is assembled;
- nonlinear continuum closure / universality.

---

## 6. Final pre-handoff work programme

The project should now stop expanding sideways. The remaining solo / computational work is a bounded pre-handoff pass:

1. **Freeze one final candidate parent.** Mark every term as ASSUMED, DERIVED, EFFECTIVE, or INTERPRETATION.
2. **Combined quantum test.** Exactly diagonalize `H_graph + H_med` on the largest tractable finite configuration sector and determine whether low-energy weight concentrates on relation-rich / local states.
3. **Three-size geometry ledger.** Put `N=128,216,344` at the same corrected couplings/protocol and record energy, adversaries, `d_s`, gap, ball/Hausdorff growth, and disorder diagnostics.
4. **Actual rank-4 kinetic audit.** Compute the downfolded `K_eff^{ijkl}` on the corrected autonomous amorphous basin rather than relying only on statistical-isotropy arguments.
5. **Corrected closure and matter checks.** Re-run local `H_mix` feasibility and matter curl-gap diagnostics on the new graph phase.
6. **Stop and hand over.** The remaining integration theorem, many-body first-class phase, rigorous thermodynamic limit, extra-mode exclusion, and nonlinear continuum universality are the point where specialist external validation becomes more valuable than further ad-hoc numerical searching.

---

## 7. Handoff standard

The handoff should **not** claim that GWXP has proved emergent gravity.

The appropriate claim is:

> GWXP has produced one increasingly compact finite-relational candidate architecture, several exact finite algebraic constructions, a parent-energy mechanism for relation condensation, numerical evidence for autonomous approximately-3D graph formation, and a microscopically constructible soft-local graph hopping sector. The decisive unresolved question is whether these pieces form one stable thermodynamic quantum phase with the full first-class gravitational constraint structure and no extra low-energy modes.

That is the line between what this project has actually established and what an external expert still needs to prove or kill.

---

## 8. Provenance rule going forward

Do not silently overwrite failed or superseded branches.

Every future change should be marked as one of:

```text
CONFIRMED
CORRECTED
DEMOTED
KILLED
OPEN
```

In particular, retain the history of:

- the old `g=3` window;
- the rank-2 Cayley surprise;
- the contaminated old `N=512` scale;
- the reducible `k=3` proposal bug;
- the hidden hard-`r` proposal filter;
- the common-graph mediator freezing problem;
- the square-root mediator demotion;
- the distinction between classical annealing and quantum configuration-space dynamics.

Those corrections are part of the evidence record, not clutter to delete.
