# Data

## `states/` — authoritative corrected states

- `autonomous_N128.npz` — unrestricted corrected autonomous `N=128` state used in the final three-size ledger.
- `autonomous_N216.npz` — corrected autonomous `N=216` state used in the final ledger.
- `autonomous_N344.npz` — unrestricted corrected autonomous `N=344` state used in the final ledger.
- `generic_initial_N344.npz` — generic coordinate-free degree-6 initial state before the old radius-filtered descent; included as a baseline.

Each state contains at minimum adjacency matrix `A`. Energy metadata fields vary historically (`E` or `energy`), so scripts handle both where necessary.

## `legacy/` — do not use as autonomous-emergence evidence

These states are preserved for comparison and provenance. They descend from the old radius-3-filtered proposal dynamics and are therefore not counted as proof that the parent discovers locality without a locality hint.

The filenames explicitly mark this status.
