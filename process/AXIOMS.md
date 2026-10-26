# AXIOMS — binding rules. Violations fail the build.

1. **Verbatim is extracted, never typed.** Every quote carries
   {session file, timestamp window} provenance and must substring-verify
   in `text/` after normalization. Re-verify after ANY move into a
   derived doc (M18). Quoted-from-memory is the original sin (M1).
2. **Quotes are contiguous transcript spans.** No ellipsis in units — the
   verifier is substring-based; elision lives only in derived docs, which
   are re-verified with a split check (M18).
3. **Grades are essay-layer membership.** A enters innermost, B at depth,
   C = texture-clip that PLAYS in the walk. Notes live in C-MARKS/ledger,
   never as units (M21). Essay-0 cell clips are A by law (M22).
4. **One unit, one home.** Every unit belongs to exactly one section.
   Totals must reconcile: units == SPINE_ASSIGN rows. Overrides are
   logged in the tool, never silent.
5. **Seams read standalone.** No clip starts mid-sentence, ends
   mid-thought, or dangles. Blocks after a cut must parse cold.
   Deictics ("they", "this brahman") are flagged at audit, resolved by
   card/question context or glue at build — never ignored.
6. **Sanskrit and plains are never composed.** Cards come from held texts
   (never from ASR captions); plains come from the signed key via
   `plain_filter.py`. Fix the key, rerun, diff the blast radius — never
   hand-edit a row. TTS lines are traceable to (card row | key | marked
   human bridge) or they are slop.
7. **One voice per job.** Archive voices own ALL source-language spoken
   aloud (chant, verses). TTS owns questions/plains/cards at v1 only.
   Human owns questions at ship + rare marked bridges. Archive never
   reads cards; TTS never narrates; human never voices verses.
8. **Seeds open, never stack unmarked.** Essay-0 heads every layer (4×
   recurrence); cell clips play at layer heads ONLY, never inside
   section lists (SEED-CAP). Mottos/bells: 880 Hz sections, 220 Hz
   crossings — levels under voice, never masking.
9. **Slop is quarantined, not deleted.** Hand-written or failed artifacts
   move aside with a dated note, never ship, never silently fixed.
10. **Audit before render.** Verbatim 100%, flow-read complete, hold-up
    passed, TTS lines scanned, cuts located. Audio is always the LAST
    step; ears sign off or it doesn't ship.
11. **Thin is honest.** A thin section stays thin (no padding to quotas,
    no runtime-driven cuts of audited membership). Gaps declared with
    owners. Supersets never ship. Runtime honesties recorded at build.
12. **Every fix is logged with cause.** No silent edits. Scripted doc
    edits assert `count == 1` (M17). Any header-format extension updates
    EVERY parser in the same commit (M12). Derived files regenerate
    from units, never trusted across sessions (M23). The pipeline only
    changes by adding checks, never by relaxing them.
