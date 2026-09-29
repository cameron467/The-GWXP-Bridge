# Known issues, corrections, and non-results

This file is intentionally prominent. Several attractive intermediate interpretations did not survive harder checks.

## 1. Hard radius-3 accessibility evidence was contaminated

Early `N=344` descent code rejected rewires unless new edges were reachable within three graph hops after deleting the old edges. That was an implicit locality hint. Those runs are preserved under `data/legacy/` and `archive/` but are not counted as autonomous nucleation evidence.

The corrected unrestricted `N=344` state in `data/states/autonomous_N344.npz` is the authoritative state for the final pass.

## 2. Some nominal k=3 rewrites were reducible

An earlier multi-swap proposal generator admitted moves equivalent to a genuine 2-switch plus a spectator operation. Those results are not used to support a distinct k=3 tunnelling mechanism.

## 3. Uniform all-edge kinetic driver is not the final dynamics

A uniform flip driver has too many unsuppressed nonlocal channels and does not provide graph-local causal structure. It is retained only as historical scaffolding.

## 4. Multiplicative common-graph mediator freezes

The old Hermitian common-graph amplitude multiplies both forward- and reverse-local propagator support. On generic graphs its total transition-rate density falls sharply with system size. It is deprecated as the thermodynamic nucleation driver.

## 5. Square-root additive kernel is heuristic

An additive source/target square-root formula behaved numerically better, but a cleaner microscopic pair-mediator derivation produces products of Green-function entries instead. The square-root formula is therefore not part of the frozen candidate.

## 6. Classical downhill descent is not quantum dynamics

Zero-temperature graph descent was used to probe the diagonal energy landscape and accessibility. It must not be interpreted as the unitary evolution of the model. The final pass therefore included exact finite sectors of the combined `H_graph + H_med` Hamiltonian.

## 7. Bare rank-4 self-isotropization fails

This is the most important surviving weakness. After whitening the rank-2 metric and using corrected mediator-derived channel weights, the physical kinetic covariance remains strongly anisotropic. The measured residual increases across the tested autonomous states.

Therefore `H_mix` is required to do genuine dynamical work.

## 8. Radius-3 H_mix was overstated

Earlier local isotropization tests allowed exact anisotropy equations to be satisfied by driving the local shear power almost to zero. Once this loophole is excluded, radius 3 is not robust on the corrected phase.

Radius-4 move cones do contain nonzero exactly isotropic shear witnesses, but the Hamiltonian that naturally selects those weights is still open.

## 9. Hard face-length cutoff is false

The autonomous `N=344` cycle space requires length-8 loops for full local-cycle spanning. A universal rule keeping only faces of length <=7 is rejected. The surviving matter completion uses a soft positive loop hierarchy.

## 10. Thermodynamic claims remain open

Three finite sizes do not establish an asymptotic 3D phase, a nonzero matter curl gap at infinite size, or vanishing spin-4 grain. No thermodynamic exponent is claimed from the final `N=128,216,344` ledger.

## 11. One-parent first-class closure remains unproved

Finite exact schedule algebras and moving-graph Jacobi checks are not by themselves a proof that the full many-body low-energy subspace has genuine first-class scalar and spatial constraints.

## 12. AI-assisted research

The project used language models heavily for algebraic exploration, code generation, falsification suggestions, and synthesis. This increases the importance of independent verification. A result should not be treated as established solely because it survived internal AI-assisted checking.
