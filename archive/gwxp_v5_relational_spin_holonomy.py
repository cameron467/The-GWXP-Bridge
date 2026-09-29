"""
GWXP V5.3 — Relational spin-frame holonomy
27 Sep 2026

Purpose
-------
Replace the hand-made finite "metric register" by an actual rotationally
invariant spin-1 frame observable.

For two spin-1 frame legs define
    Q12 = S1 . S2.
This is invariant under simultaneous SU(2) rotations and has eigenvalues
    Jpair=0,1,2  ->  -2,-1,+1.
Those integer eigenvalues can control an exact Z_d gauge translation.

The script verifies:
  1. [Q12, J_total^a] = 0 exactly.
  2. spec(Q12) = {-2,-1,+1} with multiplicities 1,3,5.
  3. For d=5, a schedule-controlled shear T obeys exactly
         T V T^{-1} V^{-1} = G_Q
     where G_Q translates the gauge register by the eigenvalue of Q12.

Interpretation
--------------
This is an exact finite existence construction for a relational,
frame-dependent schedule holonomy. It is NOT yet a derivation of GR.
"""

import numpy as np


def spin1():
    s = 1.0
    m = np.array([1.0, 0.0, -1.0])
    Sz = np.diag(m).astype(complex)
    Sp = np.zeros((3,3), dtype=complex)
    # basis |1>,|0>,|-1>
    Sp[0,1] = np.sqrt(2.0)
    Sp[1,2] = np.sqrt(2.0)
    Sm = Sp.conj().T
    Sx = (Sp + Sm)/2
    Sy = (Sp - Sm)/(2j)
    return Sx, Sy, Sz


def shift(d, power=1):
    X = np.zeros((d,d), dtype=complex)
    for g in range(d):
        X[(g+power) % d, g] = 1
    return X


Sx,Sy,Sz = spin1()
I3 = np.eye(3, dtype=complex)

S1 = [np.kron(Sx,I3), np.kron(Sy,I3), np.kron(Sz,I3)]
S2 = [np.kron(I3,Sx), np.kron(I3,Sy), np.kron(I3,Sz)]

Q = sum(a@b for a,b in zip(S1,S2))
Jtot = [a+b for a,b in zip(S1,S2)]

print("TEST 1 — rotational invariance")
for name,J in zip("xyz",Jtot):
    err = np.linalg.norm(Q@J - J@Q)
    print(f"  ||[Q12,J_{name}]|| = {err:.3e}")
    assert err < 1e-12

evals, evecs = np.linalg.eigh(Q)
rounded = np.rint(evals).astype(int)
vals, counts = np.unique(rounded, return_counts=True)
print("\nTEST 2 — spectrum of Q12 = S1.S2")
for v,c in zip(vals,counts):
    print(f"  eigenvalue {v:+d}: multiplicity {c}")
assert list(vals) == [-2,-1,1]
assert list(counts) == [1,3,5]

# Spectral projectors of Q, grouped by exact integer eigenvalue.
projectors = {}
for r in (-2,-1,1):
    inds = np.where(rounded == r)[0]
    U = evecs[:,inds]
    projectors[r] = U @ U.conj().T

d = 5
Ic = np.eye(d, dtype=complex)
Ig = np.eye(d, dtype=complex)
Xc = shift(d,1)

# T = sum_r P_r \otimes sum_c |c><c| \otimes X_g^(r*c)
T = np.zeros((9*d*d, 9*d*d), dtype=complex)
for r,P in projectors.items():
    for c in range(d):
        Pc = np.zeros((d,d), dtype=complex)
        Pc[c,c] = 1
        T += np.kron(np.kron(P,Pc), shift(d,(r*c) % d))

V = np.kron(np.kron(np.eye(9), Xc), np.eye(d))

# G_Q = sum_r P_r \otimes I_clock \otimes X_g^r
GQ = np.zeros_like(T)
for r,P in projectors.items():
    GQ += np.kron(np.kron(P,Ic), shift(d,r % d))

Omega = T @ V @ T.conj().T @ V.conj().T
err = np.linalg.norm(Omega-GQ)

print("\nTEST 3 — exact relational finite holonomy")
print(f"  ||T V T^-1 V^-1 - G_Q|| = {err:.3e}")
assert err < 1e-10

print("\nVERDICT")
print("  Exact finite identity verified:")
print("      T V T^-1 V^-1 = G_Q")
print("  The gauge displacement is controlled by Q12=S1.S2,")
print("  which is rotationally invariant and therefore relational.")
print("  This is an existence result, not natural emergence of GR.")
