# neohive-coverage-scenario-e

Second fixture repo for HIVE-238 (F3 coverage), used for Scenario E (isolation): a hive that is deliberately different from `neohive-coverage-scenario-c` so the two hives are easy to tell apart in coverage output.

## Traits (intentionally different from scenario-c)

- Python instead of TypeScript (`app/`, `lib/`, `tests/`).
- Starts below 100 percent coverage: the `docs/` tree holds empty Markdown files that are indexable but produce no chunks, so they show up as ranked gaps.
- A compiled `.pyc` under `app/__pycache__/` confirms binary/compiled output is excluded from the denominator.
