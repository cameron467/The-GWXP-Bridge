#!/usr/bin/env python3
"""Lightweight verification of the checked-in GWXP final-pass artifacts.

This intentionally does not rerun the expensive searches. It checks that the
saved state files are internally consistent and that the headline numerical
claims in README/STATUS agree with the checked-in raw outputs.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from scipy.sparse.csgraph import connected_components

ROOT = Path(__file__).resolve().parent
D = 6
G = 2.0
U = 0.1
KAPPA = 0.30
EPS = 0.025
TAU = 5.0


def load_json(rel):
    with open(ROOT / rel, "r", encoding="utf-8") as f:
        return json.load(f)


def triangles(A: np.ndarray) -> int:
    B = A.astype(np.int16)
    return int(np.trace(B @ B @ B) // 6)


def graph_energy(A: np.ndarray) -> float:
    """Energy density used in the corrected g=2,U=.1,kappa=.3 searches.

    The strong degree-sector constant is omitted because all authoritative
    states are exactly degree 6; this matches the stored search energies.
    """
    A = A.astype(float)
    X = A / D
    w, V = eigh(X, check_finite=False)
    ex = np.exp(G * w)
    comm = (V * ex) @ V.T
    edge_mask = np.triu(A > 0, 1)
    communicability = -float(np.mean(ex))
    capacity = U * float(np.sum(comm[edge_mask] ** 2)) / len(A)
    determinant = -KAPPA * float(np.mean(np.log(EPS + 1.0 - w)))
    triangle_term = TAU * triangles(A.astype(np.int8)) / len(A)
    return communicability + capacity + determinant + triangle_term


def check_state(path: Path, expected_energy: float):
    z = np.load(path, allow_pickle=True)
    A = z["A"].astype(np.int8)
    N = len(A)
    assert A.shape == (N, N)
    assert np.array_equal(A, A.T), f"{path.name}: adjacency not symmetric"
    assert np.all(np.diag(A) == 0), f"{path.name}: self loops"
    deg = A.sum(axis=1)
    assert np.all(deg == D), f"{path.name}: degree range {deg.min()}..{deg.max()}"
    assert triangles(A) == 0, f"{path.name}: authoritative state has triangles"
    nc, _ = connected_components(A, directed=False)
    assert nc == 1, f"{path.name}: disconnected ({nc} components)"
    E = graph_energy(A)
    assert abs(E - expected_energy) < 2e-9, (
        f"{path.name}: recomputed E={E:.12f}, expected={expected_energy:.12f}"
    )
    return N, E


def main():
    print("GWXP saved-result verification")
    print("=" * 36)

    metrics = load_json("results/three_size_metrics.json")
    byN = {int(x["N"]): x for x in metrics}
    assert set(byN) == {128, 216, 344}

    for N in (128, 216, 344):
        p = ROOT / f"data/states/autonomous_N{N}.npz"
        _, E = check_state(p, float(byN[N]["E"]))
        assert int(byN[N]["degree_min"]) == 6 and int(byN[N]["degree_max"]) == 6
        assert int(byN[N]["triangles"]) == 0
        print(f"[ok] N={N} authoritative state, E/N={E:.12f}")

    # Structured-adversary comparison used in the final status table.
    for N in (128, 216, 344):
        cj = load_json(f"results/cayley_scan_N{N}.json")
        best = min(float(v["energy"]) for v in cj["best_by_rank"].values())
        E = float(byN[N]["E"])
        assert E < best, f"N={N}: autonomous E={E} does not beat best scanned Cayley {best}"
        print(f"[ok] N={N} beats checked-in rank-1/2/3 Abelian/Cayley floor by {best-E:.3e}")

    # Rank-4 negative result must remain visible and numerically consistent.
    expected_spin4 = {128: 0.24936806799891656, 216: 0.3869, 344: 0.499}
    observed = {}
    for N in (128, 216, 344):
        r = load_json(f"results/rank4_N{N}.json")
        v = float(r["mediator"]["spin4_rms"])
        observed[N] = v
        assert v > 0.20, f"N={N}: rank-4 residual unexpectedly tiny; check provenance"
    assert abs(observed[128] - expected_spin4[128]) < 1e-10
    assert observed[216] > observed[128]
    assert observed[344] > observed[216]
    print("[ok] bare mediator-weighted spin-4 failure preserved:", ", ".join(f"N={N}:{observed[N]:.3f}" for N in (128,216,344)))

    # Global H_mix feasibility: exact isotropy residual small while shear retained.
    for N in (216, 344):
        h = load_json(f"results/hmix_global_N{N}.json")
        assert bool(h["feasible"])
        assert float(h["finalfeat"]) < 1e-6
        assert abs(float(h["shearratio"]) - 1.0) < 1e-5
        assert float(h["KL"]) < 1.0
        print(f"[ok] global H_mix feasibility N={N}, KL={float(h['KL']):.3f}")

    # Cycle span lengths and matter curl gaps.
    expected_span = {128: 7, 216: 7, 344: 8}
    for N in (128, 216, 344):
        c = load_json(f"results/cycle_rank_N{N}.json")
        assert int(c["span_L"]) == expected_span[N]
        assert int(c["ranks"][str(expected_span[N])]) == int(c["cycle_dim"])
        print(f"[ok] N={N} cycle space spans by ell={expected_span[N]}")

    s128 = load_json("results/softcurl_N128.json")
    s216 = load_json("results/softcurl_N216.json")
    s344 = load_json("results/softcurl_dense_N344.json")
    for N, s in ((128, s128), (216, s216), (344, s344)):
        g02 = float(s["gaps"]["0.2"])
        assert g02 > 0.02
        print(f"[ok] N={N} soft curl gap at rho_f=.2 = {g02:.6f}")

    # Exact finite combined quantum sectors: weak/moderate hopping remains heavily
    # concentrated on low-parent-energy states; large hopping delocalizes.
    for name in ("quantum_hypercube_N64_m10.npz", "quantum_hypercube_N128_m9.npz"):
        z = np.load(ROOT / "results" / name, allow_pickle=True)
        rows = [json.loads(str(x)) for x in z["results_json"]]
        byz = {float(x["zeta"]): x for x in rows}
        assert float(byz[0.3]["weight_lowest10pct"]) > 0.99
        assert float(byz[10.0]["weight_lowest10pct"]) < 0.5
        print(f"[ok] {name}: low-energy localization at zeta=.3, delocalization by zeta=10")

    print("=" * 36)
    print("All lightweight GWXP repository checks passed.")


if __name__ == "__main__":
    main()
