# AI assistance and validation policy

GWXP was developed with extensive use of language-model tools for:

- algebraic exploration and derivation attempts;
- Python code generation and debugging;
- numerical falsification ideas;
- literature-search assistance;
- synthesis of research notes and evidence ledgers.

This is part of the provenance of the project and should be disclosed rather than hidden.

## What AI assistance does not establish

A language model agreeing with a derivation is not independent verification. A generated script producing an expected number is not peer review. The project therefore treats independent reproduction and specialist review as necessary before any result is presented as established physics.

## Internal safeguards used in this snapshot

- failed and superseded routes are retained in the archive;
- corrected states are separated from legacy radius-filtered states;
- the lightweight `run_all_tests.py` recomputes authoritative state energies and cross-checks saved headline results;
- the strongest negative result (bare rank-4 anisotropy) is prominently preserved rather than optimized away;
- assumptions, derived results, numerical evidence, interpretation, and open claims are separated in the master ledger.

## Recommended external validation

Reviewers should independently:

1. audit every exact derivation from the underlying definitions;
2. rerun the final-pass scripts from fresh environments and seeds;
3. broaden the graph adversary classes;
4. inspect stochastic proposal distributions for hidden bias;
5. challenge the physical interpretation of the finite schedule algebra;
6. derive or falsify the proposed local `H_mix` mechanism without fitted weights.
