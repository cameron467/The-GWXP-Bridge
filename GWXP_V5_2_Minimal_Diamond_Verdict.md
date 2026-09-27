# GWXP V5.2 — Minimal Diamond Verdict

## Question
Can the smallest finite two-diamond rewrite system, with all local amplitudes free, force a GR-like coefficient relation?

## Exact result 1 — No
For a two-plaquette strip with scalar edge amplitudes,

\[
v_1 h_{00}=g_0 h_{01}v_0,\qquad
v_2 h_{10}=g_1 h_{11}v_1 .
\]

The general solution is

\[
h_{01}=\frac{h_{00}v_1}{g_0v_0},\qquad
h_{11}=\frac{h_{10}v_2}{g_1v_1}.
\]

Thus the two diamonds constrain only the two independent loop products. The local update amplitudes remain highly underdetermined. Bare causal-diamond consistency therefore **does not select the DeWitt/TEGR/ADM coefficients**.

Equivalent graph statement: the strip has \(V=6\), \(E=7\), hence cycle rank \(E-V+1=2\). After fixing transport along a spanning tree, only two loop holonomies remain.

## Exact result 2 — Finite state-dependent closure exists
Take three finite \(Z_d\) registers:

- \(q\): frame/geometry register,
- \(c\): schedule register,
- \(g\): spatial-label gauge register.

Define

\[
T|q,c,g\rangle=|q,c,g+qc\rangle ,
\]

\[
V|q,c,g\rangle=|q,c+1,g\rangle ,
\]

with arithmetic mod \(d\).

Then exactly,

\[
T V T^{-1}V^{-1}=G_Q ,
\]

where

\[
G_Q|q,c,g\rangle=|q,c,g+q\rangle .
\]

So the mismatch between two local schedule orders is a spatial-label gauge transformation **controlled by the frame variable**.

For \(d=2\), \(T\) is a Toffoli gate, \(V=X_c\), and \(G_Q\) is CNOT from the frame bit to the gauge bit.

## Status
**DERIVED / EXACT FINITE EXISTENCE:** finite-dimensional rewrite systems can realize noncommuting local schedule moves whose commutator closes into a frame-dependent gauge transformation.

**KILLED:** the bare two-diamond condition by itself does not select GR coefficients.

**OPEN:** derive the shared local rewrite rule and its frame dependence from one simple autonomous Hamiltonian, and show that demanding arbitrary smooth schedule equivalence plus the two-TT phase forces the effective continuum rule onto the GR/TEGR branch without inserting that branch by hand.
