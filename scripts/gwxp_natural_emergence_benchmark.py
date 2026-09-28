#!/usr/bin/env python3
"""
GWXP Natural Emergence benchmark
Frozen benchmark used in the 28 Sep 2026 validation pass.

Parent (degree-six sector):
    H = H_degree + tau*T
        - Tr exp(g Atilde)
        + U sum_edges [exp(g Atilde)_ij]^2
        - kappa log det(eps I + Ltilde)

Atilde = D^{-1/2} A D^{-1/2}, Ltilde = I - Atilde.

The script reproduces:
  * cubic thermodynamic energy density,
  * finite cubic convergence,
  * lower-energy generalized-dihedral 3-D phase,
  * its spectral dimension by IDOS,
  * a deterministic rank-2 quotient sweep showing decompactification,
  * one representative rank-4 competitor.

Dependencies: numpy, scipy
Optional defect tests use networkx and are omitted from the default run.
"""

import itertools
import numpy as np
from scipy.special import iv

G = 6.0
U = 0.018
KAPPA = 0.01
EPS = 0.025
TAU = 5.0

# ---------- cubic Z^3 ----------

def cubic_det_density(n=80):
    th = 2*np.pi*np.arange(n)/n
    c = np.cos(th)
    total = 0.0
    for cx in c:
        vals = EPS + 1 - (cx + c[:, None] + c[None, :]) / 3.0
        total += np.log(vals).sum()
    return total / n**3

def cubic_infinite():
    i0, i1 = iv(0, 2.0), iv(1, 2.0)
    walk = -(i0**3)
    q = i1 * i0**2
    cap = U * 3.0 * q*q
    det = -KAPPA * cubic_det_density(80)
    return walk + cap + det

def cubic_finite_energy(L):
    # Exact periodic Fourier sum for C_L x C_L x C_L.
    th = 2*np.pi*np.arange(L)/L
    c = np.cos(th)
    total_walk = total_det = 0.0
    # exp(G*Atilde) = exp(Ax) x exp(Ay) x exp(Az) for degree 6, G=6.
    # q for one positive-direction edge is a 1D Fourier coefficient times two diagonals.
    e2c = np.exp(2*c)
    a0 = e2c.mean()
    a1 = (e2c*np.cos(th)).mean()
    trace_density = a0**3
    q = a1*a0*a0
    cap = U*3*q*q
    for cx in c:
        vals = EPS + 1 - (cx + c[:,None] + c[None,:])/3
        total_det += np.log(vals).sum()
    det = -KAPPA*total_det/(L**3)
    return -trace_density + cap + det

# ---------- mixed generalized-dihedral phase ----------
# Canonical degree-six generating set:
# one translation pair +/-a with a=(1,0,0)
# four reflections with offsets 0, 2a, b, c,
# b=(0,1,0), c=(0,0,1).

A3 = (1,0,0)
R3 = [(0,0,0),(0,1,0),(2,0,0),(0,0,1)]

def mixed_dihedral_energy_3d(n=56, u=U, return_spectrum=False):
    th = 2*np.pi*np.arange(n)/n
    count = n**3
    trace_sum = det_sum = m3_sum = 0.0
    qrot = 0.0 + 0.0j
    qrefs = np.zeros(4, dtype=np.complex128)
    lap_plus = [] if return_spectrum else None
    lap_minus = [] if return_spectrum else None

    for x in th:
        y,z = np.meshgrid(th, th, indexing="ij")
        pha = np.exp(1j*x)
        c = np.cos(x) * np.ones_like(y)
        phases = [
            np.ones_like(y, dtype=complex),
            np.exp(1j*y),
            np.exp(2j*x)*np.ones_like(y, dtype=complex),
            np.exp(1j*z),
        ]
        f = sum(phases)
        r = np.abs(f)

        e2c = np.exp(2*c)
        ch, sh = np.cosh(r), np.sinh(r)
        diag = e2c*ch
        trace_sum += diag.sum()

        vals1 = EPS + 1 - (2*c+r)/6
        vals2 = EPS + 1 - (2*c-r)/6
        det_sum += (0.5*(np.log(vals1)+np.log(vals2))).sum()

        m3_sum += ((2*c)**3 + 3*(2*c)*r*r).sum()

        qrot += np.sum(diag*np.conj(pha))
        h = np.zeros_like(f)
        mask = r > 1e-14
        h[mask] = e2c[mask]*sh[mask]*f[mask]/r[mask]
        for j,ph in enumerate(phases):
            qrefs[j] += np.sum(h*np.conj(ph))

        if return_spectrum:
            lap_plus.append((1-(2*c+r)/6).ravel())
            lap_minus.append((1-(2*c-r)/6).ravel())

    t = trace_sum/count
    qr = qrot.real/count
    qrs = qrefs.real/count
    cap = u*(qr*qr + 0.5*np.sum(qrs*qrs))
    det = -KAPPA*det_sum/count
    tri_density = (m3_sum/count)/6.0
    e = -t + cap + det + TAU*tri_density

    out = dict(e=e, walk=-t, cap=cap, det=det,
               tri_density=tri_density, qrot=qr, qrefs=qrs)
    if return_spectrum:
        out["lap"] = np.concatenate(lap_plus + lap_minus)
    return out

def idos_dimension(lap, lam_min=0.005, lam_max=0.05, npts=30):
    lap = np.asarray(lap)
    thresholds = np.geomspace(lam_min, lam_max, npts)
    frac = np.array([(lap <= x).mean() for x in thresholds])
    mask = frac > 0
    x, y = np.log(thresholds[mask]), np.log(frac[mask])
    slope, intercept = np.polyfit(x, y, 1)
    pred = slope*x + intercept
    r2 = 1 - np.sum((y-pred)**2)/np.sum((y-y.mean())**2)
    return 2*slope, r2

# ---------- rank-2 compactified quotients of the same phase ----------

def mixed_dihedral_energy_2d(m, ncoef, grid=128, u=U):
    # c = m*a + n*b; shortest explicit relation c-m a-n b = 0.
    th = 2*np.pi*np.arange(grid)/grid
    x,y = np.meshgrid(th, th, indexing="ij")
    c0 = np.cos(x)
    phases = [
        np.ones_like(x, dtype=complex),
        np.exp(1j*y),
        np.exp(2j*x),
        np.exp(1j*(m*x+ncoef*y)),
    ]
    if len({(0,0),(0,1),(2,0),(m,ncoef)}) < 4:
        return None
    f = sum(phases)
    r = np.abs(f)
    e2c = np.exp(2*c0)
    ch, sh = np.cosh(r), np.sinh(r)
    trace = np.mean(e2c*ch)

    vals1 = EPS + 1 - (2*c0+r)/6
    vals2 = EPS + 1 - (2*c0-r)/6
    det = -KAPPA*np.mean(0.5*(np.log(vals1)+np.log(vals2)))

    qr = np.mean(e2c*ch*np.exp(-1j*x)).real
    h = np.zeros_like(f)
    mask = r > 1e-14
    h[mask] = e2c[mask]*sh[mask]*f[mask]/r[mask]
    qrs = np.array([np.mean(h*np.conj(ph)).real for ph in phases])
    cap = u*(qr*qr + 0.5*np.sum(qrs*qrs))

    tri = np.mean((2*c0)**3 + 3*(2*c0)*r*r)/6
    if abs(tri) > 1e-8:
        return None

    e = -trace + cap + det
    relation_length = abs(m) + abs(ncoef) + 1
    return e, relation_length

# ---------- representative rank-4 non-Abelian competitor ----------

R4 = [(0,0,0,0),(0,-3,-3,-3),(-3,-2,-3,3),(-3,3,2,0)]
A4 = (1,0,0,0)

def mixed_dihedral_energy_4d(grid=18, u=U):
    vals = 2*np.pi*np.arange(grid)/grid
    meshes = np.meshgrid(vals,vals,vals,vals,indexing="ij")
    pts = np.stack([m.ravel() for m in meshes], axis=1)
    pa = pts@np.asarray(A4)
    pha = np.exp(1j*pa)
    c = pha.real

    phases=[]
    f=np.zeros(len(pts),complex)
    for rv in R4:
        ph=np.exp(1j*(pts@np.asarray(rv)))
        phases.append(ph); f += ph
    r=np.abs(f)

    e2c=np.exp(2*c); ch=np.cosh(r); sh=np.sinh(r)
    trace=np.mean(e2c*ch)
    det=-KAPPA*np.mean(0.5*(
        np.log(EPS+1-(2*c+r)/6) +
        np.log(EPS+1-(2*c-r)/6)
    ))
    qr=np.mean(e2c*ch*np.conj(pha)).real
    h=np.zeros_like(f); mask=r>1e-14
    h[mask]=e2c[mask]*sh[mask]*f[mask]/r[mask]
    qrs=np.array([np.mean(h*np.conj(ph)).real for ph in phases])
    cap=u*(qr*qr+0.5*np.sum(qrs*qrs))
    tri=np.mean((2*c)**3+3*(2*c)*r*r)/6
    return -trace+cap+det+TAU*tri

def main():
    e3 = mixed_dihedral_energy_3d(n=56, return_spectrum=True)
    d3, r23 = idos_dimension(e3["lap"])

    print("=== Frozen GWXP Natural Emergence benchmark ===")
    print(f"U/J = {U}, g = {G}, kappa = {KAPPA}, eps = {EPS}")
    print()
    print(f"Infinite cubic Z^3:              {cubic_infinite(): .12f}")
    print(f"Generalized-dihedral rank-3:    {e3['e']: .12f}")
    print(f"Rank-3 IDOS spectral dimension: {d3: .4f}  (R^2={r23:.5f})")
    print(f"Representative rank-4 phase:    {mixed_dihedral_energy_4d(): .12f}")
    print()

    print("Cubic finite-size convergence:")
    for L in range(4,11):
        print(f"  L={L:2d}, N={L**3:4d}: {cubic_finite_energy(L): .12f}")
    print()

    # Exhaustive deterministic quotient sweep in the displayed box.
    target = e3["e"]
    rows=[]
    for m in range(-12,13):
        for ncoef in range(-12,13):
            q = mixed_dihedral_energy_2d(m,ncoef)
            if q is None:
                continue
            e,R=q
            rows.append((e-target,R,m,ncoef,e))

    rows.sort()
    print("Best rank-2 quotient in |m|,|n|<=12:")
    gap,R,m,ncoef,e = rows[0]
    print(f"  c={m}a+{ncoef}b, relation length={R}")
    print(f"  energy={e:.12f}, excess above rank-3={gap:.3e}")
    print()
    print("Best rank-2 excess by relation length R:")
    byR={}
    for gap,R,m,ncoef,e in rows:
        if R not in byR or gap < byR[R][0]:
            byR[R]=(gap,m,ncoef)
    for R in sorted(byR):
        if 2 <= R <= 13:
            gap,m,ncoef=byR[R]
            print(f"  R={R:2d}: gap={gap:.6e}  (m,n)=({m},{ncoef})")

if __name__ == "__main__":
    main()
