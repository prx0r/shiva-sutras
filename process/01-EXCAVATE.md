# 01 — EXCAVATE. Sessions → units, verify-green from the first unit.

## Unit shape (all fields required — see `excavations/_SCHEMA.md`)
- `uid`: stable, never reused (`ss5-03`). Duplicate uids/quotes are
  caught by listing a file's existing windows before appending (M19).
- `timestamp`: `[HH:MM:SS]-->[HH:MM:SS]` from `text/` stamps (same base
  as the mp3). Start stamp must sit within 120 s of a transcript stamp.
- `topics`: 1–4 tags from the closed union list (extend only with a note).
- `role`: claim | simile | refutation | story | lineage | method |
  practice | mantra-gloss | history | reading.
- `quote`: the voice's words VERBATIM from `text/<session>.txt`. Never
  write a quote not just re-read in the file this session; grep it first,
  verifier second (M1). Header format extensions update EVERY parser in
  the same commit (M12).
- `context`: 1–2 lines — what she is answering / what comes before-after;
  any locus she names goes here with the source cited.
- `layer`: `read` = voicing a sūtra/commentary text · `explain` = her own
  words. Judged at write time from the read.
- `grade`: A = clip/essay-ready · B = good with edit · C = texture or do
  not use. Grades are essay-layer membership (Axiom 3), never quality
  scores. Pyramid: A small, B larger, C honest.
- `essay_use`: one line — how this is reused (essay-0 / beat / B-depth /
  cross-link).
- Every file ends with `## Reuse clusters` + `## Cross-links`.

## Method
Read each session end to end. Mine every load-bearing formulation as a
unit; leave logistics, chant-only spans, mic checks, and garble out
(they were never units). Duplicates across sessions get deleted or moved
to their true home with a pointer — never kept twice (M1, M20).

## Gate
`python3 tools/verify_units.py` → `units: N fails: 0`. Eyeball the count
every run (a check that can't find failures is worse than one that finds
too many — M5). Fail the stage on any fail: fix data, never the checker.
