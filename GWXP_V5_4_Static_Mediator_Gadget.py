"""
GWXP V5.4 — Static mediator generation of the relational shear.

A qutrit mediator has |0> as its low state and |1>,|2> at energy Δ.
Let Q be the relational frame-cell observable S1.S2, n_c the clock
occupation projector, and P_g a Hermitian gauge-shift generator.

Use
  V1 = g1 Q   ⊗ (|1><0|+h.c.)
  V2 = g2 n_c ⊗ (|2><1|+h.c.)
  V3 = g3 P_g ⊗ (|0><2|+h.c.)

Then the connected virtual loops 0->1->2->0 and its reverse give
  H_eff^(3) = 2 g1 g2 g3 / Δ^2 * Q n_c P_g

(up to conventional signs from the chosen resolvent convention),
while second order produces only lower-body shifts that can be
absorbed/countered.

This is an existence construction, not natural emergence.
"""
