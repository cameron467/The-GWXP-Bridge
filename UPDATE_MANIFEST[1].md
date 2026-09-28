# GitHub Update Manifest

This package is designed to merge into the existing GWXP repository.

## Replace

Copy these over the existing root files:

```text
README.md
MASTER_EVIDENCE_LEDGER.md
```

The updated versions preserve the earlier full research history and append the September 2026 Natural Emergence results.

## Add

```text
CHANGELOG.md

docs/FULL_RESULTS_SUMMARY.md
docs/NATURAL_EMERGENCE_2026-09-28.md
docs/SCHEDULE_HDA_BRIDGE_2026-09-28.md
docs/CLAIMS_AND_LIMITATIONS.md
docs/OPEN_PROBLEMS_AND_FALSIFICATION.md
docs/REPRODUCIBILITY_2026-09-28.md
docs/PRIOR_ART_ADDENDUM.md

scripts/gwxp_natural_emergence_benchmark.py
scripts/gwxp_schedule_hda_bridge.py

requirements_natural_emergence.txt
run_new_benchmarks.py
```

## Keep

Do not delete the existing:

```text
CITATIONS.md
requirements.txt
run_all_tests.py
data/
archive/
older docs/
older scripts/
```

The point of this update is to extend the audit trail, not erase earlier work.

## Suggested GitHub landing order

A new reader should encounter:

1. `README.md`
2. `docs/FULL_RESULTS_SUMMARY.md`
3. `docs/CLAIMS_AND_LIMITATIONS.md`
4. `MASTER_EVIDENCE_LEDGER.md`
5. reproducibility docs/scripts

Someone evaluating only the new Natural Emergence result can jump directly to:

- `docs/NATURAL_EMERGENCE_2026-09-28.md`
- `docs/SCHEDULE_HDA_BRIDGE_2026-09-28.md`
