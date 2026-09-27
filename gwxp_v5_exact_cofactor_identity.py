"""
GWXP V5.5 — Exact finite quantum cofactor identity
27 Sep 2026

Three finite frame legs carry SU(2) vector operators E_i^a.
Different legs commute. Define

    C^i_a = 1/2 eps^{ijk} eps_{abc} E_j^b E_k^c
    v     = 1/6 eps^{ijk} eps_{abc} E_i^a E_j^b E_k^c

Then the symmetrically ordered identity

    1/2 sum_a { C^i_a , E_j^a } = v delta^i_j

holds exactly.

For i=j, C^i contains only the other two legs and commutes with E_i,
so the contraction is exactly the oriented volume.

For i!=j, the symmetrized product contains an epsilon contraction with
an anticommutator symmetric in the repeated internal indices, so it
vanishes identically.

This supplies an exact finite densitized inverse-frame object from the
same frame operators.  It does not by itself solve inverse-volume
ordering or natural emergence.
"""

import numpy as np

def spin1():
    Sz=np.diag([1,0,-1]).astype(complex)
    Sp=np.zeros((3,3),complex)
    Sp[0,1]=np.sqrt(2)
    Sp[1,2]=np.sqrt(2)
    Sm=Sp.conj().T
    return [(Sp+Sm)/2,(Sp-Sm)/(2j),Sz]

S=spin1()
I=np.eye(3,dtype=complex)

# Levi-Civita
eps=np.zeros((3,3,3),dtype=int)
eps[0,1,2]=eps[1,2,0]=eps[2,0,1]=1
eps[0,2,1]=eps[2,1,0]=eps[1,0,2]=-1

# E[i][a] on three spin-1 legs
E=[[None]*3 for _ in range(3)]
for i in range(3):
    for a in range(3):
        ops=[I,I,I]
        ops[i]=S[a]
        E[i][a]=np.kron(np.kron(ops[0],ops[1]),ops[2])

# oriented volume (equivalent to 1/6 eps^ijk eps_abc E_i^a E_j^b E_k^c)
v=np.zeros((27,27),complex)
for a in range(3):
    for b in range(3):
        for c in range(3):
            v += eps[a,b,c]*E[0][a]@E[1][b]@E[2][c]

# cofactors
C=[[np.zeros((27,27),complex) for _ in range(3)] for _ in range(3)]
for i in range(3):
    for a in range(3):
        for j in range(3):
            for k in range(3):
                for b in range(3):
                    for c in range(3):
                        C[i][a] += (
                            0.5*eps[i,j,k]*eps[a,b,c]
                            * E[j][b]@E[k][c]
                        )

print("GWXP V5.5 — exact cofactor test")
for i in range(3):
    for j in range(3):
        lhs=sum(
            0.5*(C[i][a]@E[j][a] + E[j][a]@C[i][a])
            for a in range(3)
        )
        rhs=v if i==j else np.zeros_like(v)
        err=np.linalg.norm(lhs-rhs)
        print(f"  (i,j)=({i+1},{j+1}) residual = {err:.3e}")
        assert err < 1e-12

print("\nVERDICT")
print("  1/2 Σ_a {C^i_a,E_j^a} = v δ^i_j exactly.")
print("  C^i_a is therefore an exact finite densitized dual-frame object.")
print("  The same finite frame supplies both metric and inverse-frame data;")
print("  no independent inverse metric register is required at the kinematic level.")
