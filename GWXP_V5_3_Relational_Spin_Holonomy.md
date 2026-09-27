# GWXP V5.3 — Relational Spin-Frame Holonomy

## 1. Remove the external-axis flaw

A single component such as \(S_z^2\) can control the finite shear, but it picks an external axis. Replace it by two spin-1 frame legs and define

\[
\hat Q_{12}=\mathbf S_1\cdot\mathbf S_2.
\]

Under a simultaneous rotation of both legs,

\[
[\hat Q_{12},\,\mathbf J_{\rm tot}]=0.
\]

Thus \(\hat Q_{12}\) is relational.

For two spin-1 systems,

\[
\mathbf S_1\cdot\mathbf S_2
=
\frac12\left[J_{12}(J_{12}+1)-4\right],
\]

so

\[
J_{12}=0,1,2
\quad\Rightarrow\quad
Q_{12}=-2,-1,+1.
\]

The multiplicities are \(1,3,5\).

## 2. Exact finite frame-dependent holonomy

Use a \(d\)-state schedule register \(c\) and a \(d\)-state spatial-label register \(g\). For \(d=5\), define

\[
T=
\sum_{r\in\{-2,-1,1\}}
P_r
\otimes
\sum_{c=0}^{d-1}|c\rangle\langle c|
\otimes X_g^{rc},
\]

where \(P_r\) projects onto the \(\hat Q_{12}=r\) sector, and let

\[
V=I\otimes X_c\otimes I.
\]

Then exactly,

\[
T V T^{-1}V^{-1}
=
\sum_r P_r\otimes I\otimes X_g^r
\equiv G_Q .
\]

Thus two schedule operations fail to commute only by a spatial-label gauge translation controlled by a **rotationally invariant relational frame observable**.

## 3. Collective finite frame and classical limit

Take each frame leg to be a block of \(N\) spin-1 systems locked into total spin \(J=N\). Define

\[
E_i^a=\frac{J_i^a}{N}.
\]

Then

\[
[E_i^a,E_j^b]
=
\frac{i}{N}\delta_{ij}\epsilon^{abc}E_i^c.
\]

So relational Gram operators

\[
q_{ij}=E_i\cdot E_j
\]

become approximately commuting classical variables as \(N\) grows, with noncommutativity suppressed by \(1/N\). Every finite \(N\) block still has finite Hilbert dimension.

Moreover,

\[
J_i\cdot J_j
=
\frac12\left[J_{ij}(J_{ij}+1)-J_i(J_i+1)-J_j(J_j+1)\right]
\]

has integer eigenvalues for integer spins. Therefore the unnormalised relational metric can control exact finite translations, while a physical translation lattice spacing proportional to \(1/N^2\) converts that integer shift into the normalised quantity \(q_{ij}\).

## Status

**DERIVED / exact finite existence:** a rotationally invariant spin-frame observable can act as an operator-valued structure function in an exact finite schedule holonomy.

**DERIVED / algebraic continuum bridge:** collective finite spin blocks provide a relational metric whose noncommutativity is suppressed as \(1/N\).

**OPEN:** the HDA uses \(q^{ij}\), not merely a Gram component \(q_{ij}\). The inverse/dual-frame structure must be produced consistently in the protected phase.

**OPEN:** the shear interaction is still constructed. We have not shown that one simple autonomous frame Hamiltonian naturally generates it.

**OPEN:** show simultaneously that arbitrary local schedule consistency removes the scalar mode and that the same collective frame controls the two TT propagation modes.
