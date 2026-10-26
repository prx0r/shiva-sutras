# AGENTS.md — how to work in this repo (read this first, then FILEMAP).

## The one behaviour that matters
Take responsibility: read the thing cold and verdict it in your own
voice. Summarizing artifacts is not reviewing them. When asked whether
something works, re-read the words themselves and return verdicts with
reasons — the exact sentence that carries or breaks each unit, a
concrete alternative where it fails, decisions handed over (ears/owner)
not taken. See AXIOMS.md #13 and SKILLS.md (Responsibility read) for
the good behaviour with examples (S1 fusion gap, S3 apophatic ruling,
S4 opaque-T, S6 voice audition, differentiated pauses, named G12 breach)
and the bad behaviour it avoids (shipping defects inside passing gates).

## Operating rules
1. Read order: FILEMAP.md → the doc for the work at hand (BUILD_ENGINE.md
   for orientation, `process/` for execution). Never touch tools before
   MISTAKES.md (root).
2. Gates before and after every change to build outputs:
   `process/verify.sh` (units 307/0, G0 7/7, plain MATCH, totals, ledger).
   Red gate stops the line.
3. The sheet is the product; render is final-final (owner ears + signed
   sheet first). Validate sheets with `tools/validate_sheet.py`.
4. Two compilations, never blended: Standard (chant, sūtra order, four
   blocks per verse) first, Custom (spine edit) second. Details in
   BUILD_ENGINE.md.
5. Counts change → `tools/sync_counts.py`. Docs edited by script assert
   `count == 1`. Audio never commits (`audio/` gitignored except
   `audio/SOURCES.md`). New artifact → FILEMAP row the same day.
6. Log every fix with cause in MISTAKES.md. The engine only changes by
   adding checks, never relaxing them.
