# Scripts

These scripts are the compact final-pass numerical tools, not a polished Python package.

Run them from the repository root. Several scripts write directly into `results/`.

Core entry points:

- `blind_generic.py` — unrestricted parent-energy-only degree-preserving blind descent.
- `cayley_scan.py` — analytic Fourier-space scans of degree-6 Abelian/Cayley competitor families.
- `three_size_metrics.py` — common geometry diagnostics.
- `quantum_hypercube.py` / `quantum_hypercube_basin.py` — exact finite combined `H_graph + H_med` sectors.
- `rank4_keff_autonomous.py` — corrected mediator-weighted physical kinetic covariance audit.
- `hmix_global_corrected.py` — global corrected isotropization feasibility.
- `hmix_corrected_local.py`, `hmix_scalar_window.py`, `hmix_R4_*` — local corrected closure tests.
- `cycle_rank_autonomous.py` / `cycle_rank_incremental.py` — cycle-space spanning diagnostics.
- `softcurl_autonomous.py`, `softcurl_dense.py`, `softcurl_sparse.py` — local all-face Hodge/curl repair.

See `05) Reproducibility Guide.md` for command examples and caveats.
