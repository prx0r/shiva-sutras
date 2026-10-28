# REPRODUCE — exact rerun, top to bottom.

Prerequisites: repo + `audio/` mp3s (14 local; 10 missing = audio-only
gap, text pipeline unaffected) + `text/` + `transcripts/`/`cf/`.

## Stage order (deterministic unless marked ✎ human)
1. Excavations exist (`excavations/ss*.md`, `dl1.md`); to extend, follow
   `process/01-EXCAVATE.md`, then seam-check by hand ✎.
2. Coverage: `python3 tools/gap_report.py [file]` for the work queue;
   disposition every gap into `COVERAGE_LEDGER.tsv`; assert new uids
   present. `python3 tools/coverage_measure.py` for the truth numbers.
3. Converge: `python3 tools/s2_cluster.py` (REPORT ONLY — never
   `--apply` post-pass-1) → check totals reconcile. Override list lives
   in the tool. `python3 tools/validate_questions.py` → all-pass.
4. Essay-0: cells in `custom/ESSAY0_OUTPUT.md`; flow-read artifact;
   lock stays DRAFT until ear. Plain: edit `key_*.json`, run
   `plain_filter.py`, `--check` must MATCH.
5. Argue: SECTION_ARGUMENTS order is canonical; JOIN_AUDIT re-verifies
   quotes (M18) then verdicts joins. Fixes are recorded notes, not
   silent reorderings.
6. Audit: UNFOLDING vs DRAFT cells, re-run vs LOCKED cells. HOLDUP at
   lock: verdicts → `holdup_verdicts.json`, reasons → `B_SWEEP.md`,
   sheet regenerates from units. Then `sync_counts.py` + all gates.
7. Manifests: `python3 tools/build_manifests.py` (asserts grades,
   sections, location, monotonicity). `C_WALK.md` regenerates with it.
8. Beats/speakers/ear-check: docs; TTS engine swappable, layout fixed.
9. `process/verify.sh` — ALL PASS or stop.
10. Render: `tools/make_l0.py` (L0 prototype) → full `make_audio.py`
    pattern per `process/09-RENDER.md`. Loudnorm, bells, pads.
11. QA listen (ears ✎, unskippable): levers, closures, coughs, signoff.

## What is NOT reproducible (human by design, marked ✎)
Verdict overrides, flow/join verdicts, hold-up reasons, bridges/intros,
bell choices, lock + sign-offs, coverage-standard decision, listen-pass
signoff. Everything else is scripted or it doesn't belong in the pipeline.
