# 02 — COVERAGE. Full read pass; every gap dispositioned, nothing unseen.

## The truth step (`tools/coverage_measure.py`)
Measure merged unit timestamp-spans vs transcript lines: span %, line %,
word %, plus per-section anchor coverage. Rerun after every grading pass.
Report honestly — the number measures selection, not blindness.

## The pass (`tools/gap_report.py`, worst-served first)
Work-queue generator: uncovered spans per session, biggest gaps first.
Read each transcript line-by-line and disposition EVERY gap in
`excavations/COVERAGE_LEDGER.tsv`
(header: file, lines, t1, t2, words, disp, uid, note):
- **promote** → draft unit (honest grade; verify must stay 0-fail)
- **covered** → inside a unit window (record for audit)
- **C-mark** → reason from the closed vocabulary (off-spine ·
  logistics · repetitive · thin-aside · participant-QA · wrong-register ·
  duplicate-of-unit · audio-bad · overlap-covered) with the reason in
  `excavations/C-MARKS.md`
- **fix-window** → quote sits outside its unit's timestamps (audio would
  cut the wrong minute — fix immediately)
- **demoted-note** → a C that was a note, not a clip (M21)

Rules learned hard: a promote row can be swallowed by a C-row written
over its span — after writing rows, assert every new uid appears in the
ledger. Cross-file caption dups ledger once with a pointer, never create
parallel units (M20). New files' rows derive spans from the unit's own
timestamp lines, never typed seconds.

## Done when
`coverage_measure.py` reports every file with full ledger rows; every new
uid asserted in the ledger; verify still 0-fail. Remaining: only the
coverage-standard decision (span-ledger vs line-pass vs build-time
ingestion) — until it lands, no "full walk" claims.
