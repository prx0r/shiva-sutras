# 00-ACQUIRE — how a new text's corpus gets found, vetted, and landed.
Companion to `00-INPUTS.md` (which states WHAT each stage needs): this states
HOW the corpus is hunted before any build exists. Written from the Yoga Sutras
and Paramarthasara hunts (2026-10-29).

## Search order (cheap truth first)

1. **EXACT (Sanskrit): GRETIL first.** Search, never guess paths (guessed GRETIL
   and Wikisource URLs both 404'd — D1/D2). Prefer an edition whose lineage
   matches the voice's commentary method (Maas/Vyasa-lineage for Sharma's
   Vyasa+Vacaspati exposition). Vendor to `reference/` with edition + licence
   in the commit message. Count verses on arrival (Yoga: reconcile 195/196).
2. **TRUST + BOOK (translation + commentary): public domain first.**
   archive.org full texts via `/download/` paths — `/stream/` returns page
   chrome (D7, twice). One source serving both jobs is ideal (Woods 1914 =
   translation + Vyasa + Vacaspati, matching the voice). Record the upgrade
   path (Bryant / Bansat-Boudon) for owner ratification; start PD so nothing
   blocks. OCR-clean before template extraction; verify rows against anchors.
3. **VOICE (audio): continuity preferred.** Same voice stating + explaining
   (Sharma pattern) beats multi-voice stacks (no doorways, no fallback ladders).
   Same tradition-voice across texts is worth real effort (Lakshmanjoo voices
   both Shiva and Paramarthasara). Check local disk first (`find` for prior
   pulls), then Academy/paid sources — cost and access are OWNER calls, never
   agent purchases. WMA/originals convert with ffmpeg at ingest (dts warnings
   are warnings — verify sizes against runtimes, D4).
4. **Bot walls stop the line, not the project.** amsi-style verification pages
   defeat fetching — note and route around (alternate source), never probe.

## Vetting (before anything lands in a repo)

- Verse count reconciled across EXACT/TRUST/sessions (numbering traps logged
  with the map-by-CONTENT rule, never bare numbers — D5).
- Commentary coverage vs sessions (a "selected" session threatens the
  every-verse law — flag in week one).
- Rights per source written down at discovery: PD-vendorable / held-gitignored /
  cut-only+attribute / paid-gated. No audio moves without its SOURCES row.
- OCR sampled (double-spacing, wrap-breaks, debris heads) before any row is trusted.

## Landing (stage-00 exit)

New text gets a repo skeleton (`text/ transcripts/ process/ tools/ build/
reference/ audio/`, audio gitignored), engine docs ported, scars inherited
(`MISTAKES-INHERITED.md`), GRETIL vendored, `PROCESS_NOTES.md` started with a
Difficulties section on day one. Exit gate = `00-INPUTS.md` readiness checklist
plus: verse count verified, commentary coverage checked, audio rights cleared,
cost calls batched to owner. Transcription starts with word timestamps (M40) or
not at all.
