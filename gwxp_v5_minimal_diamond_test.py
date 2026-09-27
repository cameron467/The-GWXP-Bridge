"""
GWXP V5.2 — Minimal finite diamond tests
27 Sep 2026

Test A:
  Solve the completely free scalar-amplitude two-diamond strip.
  Verdict: diamond consistency alone is underdetermined and does NOT select GR.

Test B:
  Construct an exact finite Z_d operator model with frame-dependent
  diamond holonomy:
      T V T^{-1} V^{-1} = G_Q
  where
      T: (q,c,g) -> (q,c,g + q*c mod d)
      V: (q,c,g) -> (q,c+1,g)
      G_Q: (q,c,g) -> (q,c,g+q)
  This is an exact finite-dimensional analogue of an operator-valued
  structure function: the schedule commutator closes into a spatial-label
  gauge shift controlled by the frame register q.

This is an existence/consistency construction, NOT a derivation of GR.
"""

import numpy as np
import sympy as sp


def test_free_two_diamond_strip():
    # Vertices are (m,n), m=0,1,2 and n=0,1.
    # Horizontal scalar amplitudes:
    #   h00: (0,0)->(1,0)
    #   h01: (0,1)->(1,1)
    #   h10: (1,0)->(2,0)
    #   h11: (1,1)->(2,1)
    # Vertical amplitudes:
    #   v0, v1, v2 at m=0,1,2.
    # Gauge factors g0,g1 identify the two path endpoints of each diamond.
    h00,h01,h10,h11,v0,v1,v2,g0,g1 = sp.symbols(
        "h00 h01 h10 h11 v0 v1 v2 g0 g1", nonzero=True
    )

    eq1 = sp.expand(v1*h00 - g0*h01*v0)
    eq2 = sp.expand(v2*h10 - g1*h11*v1)

    sol = sp.solve([eq1,eq2],[h01,h11], dict=True)
    assert sol == [{
        h01: h00*v1/(g0*v0),
        h11: h10*v2/(g1*v1)
    }]

    print("TEST A — free two-diamond strip")
    print("Diamond equations:")
    print("  v1*h00 = g0*h01*v0")
    print("  v2*h10 = g1*h11*v1")
    print("General solution:")
    print("  h01 =", sol[0][h01])
    print("  h11 =", sol[0][h11])
    print("Verdict: only two loop products are constrained; local amplitudes remain free.")
    print("         Bare diamond consistency does NOT select a GR/DeWitt coefficient.")
    print()


def perm_matrix(d, mapfn):
    dim = d**3
    out = np.zeros((dim, dim), dtype=complex)

    def idx(q,c,g):
        return (q*d + c)*d + g

    for q in range(d):
        for c in range(d):
            for g in range(d):
                q2,c2,g2 = mapfn(q,c,g)
                out[idx(q2,c2,g2), idx(q,c,g)] = 1.0
    return out


def test_state_dependent_finite_holonomy(ds=(2,3,4,5,6,7)):
    print("TEST B — exact finite frame-dependent diamond holonomy")
    for d in ds:
        T = perm_matrix(
            d,
            lambda q,c,g,d=d: (q, c, (g + q*c) % d)
        )
        V = perm_matrix(
            d,
            lambda q,c,g,d=d: (q, (c + 1) % d, g)
        )
        GQ = perm_matrix(
            d,
            lambda q,c,g,d=d: (q, c, (g + q) % d)
        )

        Omega = T @ V @ T.conj().T @ V.conj().T
        ok = np.array_equal(Omega, GQ)
        assert ok

        print(f"  d={d}:  T V T^-1 V^-1 = G_Q   -> {ok}")

    print()
    print("Exact basis action:")
    print("  T : |q,c,g> -> |q,c,g+q*c mod d>")
    print("  V : |q,c,g> -> |q,c+1,g>")
    print("  Ω : |q,c,g> -> |q,c,g+q mod d>")
    print()
    print("Verdict: a finite-dimensional local rewrite algebra can close")
    print("         noncommuting schedule moves into a spatial-label gauge move")
    print("         whose action depends on the frame register q.")
    print("         This removes a finite-dimensional obstruction, but does not")
    print("         establish natural emergence or the full GR HDA.")


if __name__ == "__main__":
    test_free_two_diamond_strip()
    test_state_dependent_finite_holonomy()
