#!/usr/bin/env python3
"""
GWXP Natural Emergence -> Schedule/HDA bridge benchmark
28 Sep 2026

This script reproduces two independent pieces:

A) Autonomous local schedule sector
   Four vertices, six link qubits:
       V = 1/2 sum_i (d_i - 1)^2
       H = V - Gamma sum_e X_e
   The Gamma=0 ground manifold contains exactly the three perfect matchings.
   Uniform single-link flips generate matching-to-matching tunnelling only at
   fourth order.  The exact path sum is t = 20 Gamma^4, so the 1+2 splitting is
   3t = 60 Gamma^4 + O(Gamma^6).

B) Generalized-dihedral 3-D schedule/HDA seed
   For G = Z^3 semidirect Z_2, reflections R_s obey
       R_s R_t = T_{s-t}
       [R_s,R_t] = T_{s-t} - T_{t-s}
       R_s R_t R_s R_t = T_{2(s-t)}.
   A six-reflection presentation of the cubic lattice gives
       Q_IR = 1/2 Cov(s)
            = 1/72 sum_{s<t} (s-t)(s-t)^T,
   and the same Q_IR is the principal symbol of the normalized graph Laplacian.
   In physical cubic coordinates Q_IR = I/6.

Dependencies: numpy, scipy
"""

import itertools
import numpy as np
from scipy.linalg import eigh

# ---------------------------------------------------------------------
# A) Four-vertex link model
# ---------------------------------------------------------------------

vertices = range(4)
edges = list(itertools.combinations(vertices, 2))
edge_index = {e:i for i,e in enumerate(edges)}
dim = 1 << len(edges)

def degree_vector(mask):
    d = [0]*4
    for b,(i,j) in enumerate(edges):
        if (mask >> b) & 1:
            d[i] += 1
            d[j] += 1
    return d

V = np.zeros(dim)
for mask in range(dim):
    d = degree_vector(mask)
    V[mask] = 0.5 * sum((x-1)**2 for x in d)

matching_masks = [m for m in range(dim) if abs(V[m]) < 1e-14]

Xsum = np.zeros((dim,dim))
for m in range(dim):
    for b in range(len(edges)):
        Xsum[m ^ (1<<b), m] += 1.0

def fourth_order_path_sum(mi, mj):
    diff = [b for b in range(len(edges))
            if ((mi>>b)&1) != ((mj>>b)&1)]
    total = 0.0
    for order in itertools.permutations(diff):
        m = mi
        den = []
        good = True
        for b in order[:-1]:
            m ^= (1<<b)
            E = V[m]
            if E <= 1e-14:
                good = False
                break
            den.append(E)
        if good:
            total += 1.0/np.prod(den)
    return total

# ---------------------------------------------------------------------
# B) Generalized-dihedral algebra and metric tensor
# ---------------------------------------------------------------------

# Cubic lattice represented as an all-reflection Cayley graph of
# Dih(L), where L is the even-parity cubic sublattice written in a Z^3 basis.
S = np.array([
    [ 0, 0, 0],
    [-1,-1, 0],
    [ 0,-1, 0],
    [-1, 0, 0],
    [-1,-1, 1],
    [ 0, 0,-1],
], dtype=float)

# Physical basis of the even-parity sublattice.
Bphys = np.column_stack([
    np.array([1., 1., 0.]),
    np.array([1.,-1., 0.]),
    np.array([1., 0., 1.]),
])

meanS = S.mean(axis=0)
Cov = (S-meanS).T @ (S-meanS) / len(S)
Q_group = 0.5 * Cov
Q_from_commutators = sum(
    np.outer(S[i]-S[j], S[i]-S[j])
    for i,j in itertools.combinations(range(len(S)),2)
) / 72.0
Q_physical = Bphys @ Q_group @ Bphys.T

# generalized dihedral group element is (v, eps), eps in {0,1}
def gd_mul(g,h):
    v,e = g
    w,f = h
    v = np.asarray(v, dtype=int)
    w = np.asarray(w, dtype=int)
    return (tuple(v + ((-1)**e)*w), (e+f) % 2)

def reflection(s):
    return (tuple(np.asarray(s,dtype=int)), 1)

def translation(v):
    return (tuple(np.asarray(v,dtype=int)), 0)

def gd_commutator_reflections(s,t):
    rs, rt = reflection(s), reflection(t)
    x = gd_mul(gd_mul(gd_mul(rs,rt),rs),rt)
    return x

# Low-k band structure:
# normalized adjacency eigenvalues = +/- |sum_a exp(i k.s_a)|/6
def laplacian_bands(k):
    f = np.exp(1j*(S @ np.asarray(k))).sum()
    r = abs(f)/6.0
    return 1.0-r, 1.0+r

def numerical_hessian_Q(h=1e-5):
    def low(k):
        return laplacian_bands(k)[0]
    H = np.zeros((3,3))
    z = np.zeros(3)
    for i in range(3):
        ei=np.zeros(3); ei[i]=1
        H[i,i] = (low(h*ei)-2*low(z)+low(-h*ei))/h**2
    for i in range(3):
        for j in range(i+1,3):
            ei=np.zeros(3); ej=np.zeros(3)
            ei[i]=1; ej[j]=1
            H[i,j]=H[j,i]=(
                low(h*(ei+ej))-low(h*(ei-ej))
                -low(h*(-ei+ej))+low(-h*(ei+ej))
            )/(4*h*h)
    return H/2.0

def main():
    print("=== A. Autonomous local schedule sector ===")
    print("Number of Gamma=0 ground configurations:", len(matching_masks))
    print("Ground configurations are the three perfect matchings:")
    for m in matching_masks:
        print(" ", [edges[b] for b in range(len(edges)) if (m>>b)&1])

    tcoef = fourth_order_path_sum(matching_masks[0], matching_masks[1])
    print(f"\nExact fourth-order off-diagonal coefficient: t/Gamma^4 = {tcoef:.12g}")
    print(f"Predicted singlet-doublet splitting: 3t/Gamma^4 = {3*tcoef:.12g}")

    print("\nExact diagonalisation:")
    print("Gamma      triplet width       width/Gamma^4     gap above triplet")
    for gamma in (0.02,0.04,0.06,0.08,0.10):
        H = np.diag(V) - gamma*Xsum
        w = eigh(H, eigvals_only=True)
        width = w[2]-w[0]
        gap = w[3]-w[2]
        print(f"{gamma:5.2f}   {width:14.9e}   {width/gamma**4:14.8f}   {gap:14.8f}")

    print("\n=== B. Generalized-dihedral HDA seed ===")
    s = np.array([0,0,0])
    t = np.array([-1,0,0])
    c = gd_commutator_reflections(s,t)
    expected = translation(2*(s-t))
    print("Example reflection commutator:")
    print(" [R_s,R_t]_group =", c)
    print(" expected T_{2(s-t)} =", expected)
    print(" exact:", c == expected)

    print("\nIR metric tensor in group coordinates:")
    print(Q_group)
    print("\nSame tensor reconstructed from normal-normal commutator displacements:")
    print(Q_from_commutators)
    print("max |difference| =", np.max(np.abs(Q_group-Q_from_commutators)))

    print("\nIR metric tensor in physical cubic coordinates:")
    print(Q_physical)
    print("target I/6:")
    print(np.eye(3)/6.0)

    Qnum = numerical_hessian_Q()
    print("\nNumerical Hessian of the low Laplacian band:")
    print(Qnum)
    print("max |Q_numeric-Q_group| =", np.max(np.abs(Qnum-Q_group)))

    # Sample the two bands to verify the fiber-odd band is gapped.
    vals = 2*np.pi*np.arange(30)/30
    lowmin=1e9; uppermin=1e9
    for kx in vals:
        for ky in vals:
            for kz in vals:
                lo,up=laplacian_bands((kx,ky,kz))
                lowmin=min(lowmin,lo)
                uppermin=min(uppermin,up)
    print("\nBand minima on 30^3 Brillouin grid:")
    print(" soft/sheet-symmetric band min =", lowmin)
    print(" fiber-odd band min            =", uppermin)
    print(" analytic lower bound on fiber-odd band = 1")

    print("\nDiscrete HDA continuum identity:")
    print("  [R_s,R_t] = T_{s-t}-T_{t-s}")
    print("  N_s M_t-M_s N_t = -(s-t)^j (N d_j M-M d_j N)+O(a^2)")
    print("  T_{s-t}-T_{t-s} = 2(s-t)^i d_i+O(a^3)")
    print("  Sum_{s<t}(s-t)^i(s-t)^j/72 = Q_IR^{ij}")
    print("Therefore, after the overall lapse normalization is fixed,")
    print("  [H[N],H[M]] -> Q_IR^{ij}(N d_j M-M d_j N)d_i.")

if __name__ == "__main__":
    main()


# ---------------------------------------------------------------------
# C) Direct real-space continuum check on the cubic bipartite lattice
# ---------------------------------------------------------------------

DIRS = np.array([
    [ 1, 0, 0],[-1, 0, 0],
    [ 0, 1, 0],[ 0,-1, 0],
    [ 0, 0, 1],[ 0, 0,-1]
], dtype=int)

def _R_apply(field, s):
    plus = np.roll(field, shift=tuple(-s), axis=(0,1,2))
    minus = np.roll(field, shift=tuple(s), axis=(0,1,2))
    grid = np.indices(field.shape)
    parity = (grid[0]+grid[1]+grid[2]) % 2
    return np.where(parity==0, plus, minus)

def _H_apply(field, lapse):
    # c=1/sqrt(2), p_s=1/6
    avg = np.zeros_like(field, dtype=float)
    for s in DIRS:
        avg += _R_apply(field,s)/6.0
    return lapse*avg/np.sqrt(2.0)

def _dper(f, axis, h):
    return (np.roll(f,-1,axis=axis)-np.roll(f,1,axis=axis))/(2*h)

def real_space_convergence():
    print("\n=== C. Direct real-space HDA continuum convergence ===")
    print("The target action is the Lie derivative on a half-density:")
    print("  L_xi^(1/2) psi = xi^i d_i psi + 1/2 (d_i xi^i) psi")
    print("with xi^i=(delta^ij/6)(N d_j M-M d_j N).")
    print("L    fitted coefficient    relative residual")
    for L in (16,24,32,48,64):
        h=1.0/L
        x=np.arange(L)/L
        X,Y,Z=np.meshgrid(x,x,x,indexing="ij")
        N=1.1+0.2*np.sin(2*np.pi*X)+0.1*np.cos(2*np.pi*Y)
        M=0.9+0.15*np.sin(2*np.pi*Y)+0.08*np.cos(2*np.pi*Z)
        psi=np.sin(2*np.pi*X)+0.7*np.cos(2*np.pi*Y)+0.4*np.sin(2*np.pi*Z)

        comm=_H_apply(_H_apply(psi,M),N)-_H_apply(_H_apply(psi,N),M)

        dN=[_dper(N,a,h) for a in range(3)]
        dM=[_dper(M,a,h) for a in range(3)]
        dP=[_dper(psi,a,h) for a in range(3)]
        W=[N*dM[a]-M*dN[a] for a in range(3)]
        divW=sum(_dper(W[a],a,h) for a in range(3))
        target=(sum(W[a]*dP[a] for a in range(3)) + 0.5*divW*psi)/6.0

        scaled=comm/(h*h)
        coeff=np.vdot(target.ravel(),scaled.ravel()).real/np.vdot(target.ravel(),target.ravel()).real
        residual=np.linalg.norm(scaled-coeff*target)/np.linalg.norm(scaled)
        print(f"{L:2d}      {coeff: .9f}          {residual: .9f}")

if __name__ == "__main__":
    real_space_convergence()
