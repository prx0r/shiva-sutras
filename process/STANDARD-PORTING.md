# STANDARD PORTING — the objective core + per-text config

The Standard method is text-independent. This file states the parts that
never change (the engine) and the parts each new text must supply (the
config). Porting = fill the config, run the engine, log the differences.

## PART 1 — The engine (invariant across texts)

**Roles (never people):**
- TEXT — the verses, in the tradition's order. Count fixed up front.
- EXACT — the exact Sanskrit wording reference (critical edition, GRETIL,
  or held print). Decides all B1 disputes; never quoted from ASR.
- TRUST — the trusted English translation (existing published rendering).
  Read verbatim by AI voice. Never paraphrased, never composed.
- VOICE — the archive voice that states each verse + explains it.
  Same voice for B1 and explanation wherever the corpus allows.
- Coda voice — the complete-text recitation that seals the Standard.
- BOOK — the per-verse exposition guide (what each verse's A must cover).

**Layer law (invariant):** 0 = verse + TRUST + VOICE gloss, nothing else.
A = 0 + one compressed explanation passage (~1 min/unit). B adds depth.
C adds everything + guests (guests never appear before B... in C only).
Coda closes C. Every layer contains every verse (completeness, never
selectivity — that is what makes it Standard and not Custom).

**Objective gates (pass/fail, no taste involved):**
1. B1 word-verified: onset/offset from word timestamps against EXACT;
   no filler words from adjacent speech (M27/M30/M31).
2. Every cut ends at a sentence boundary, verified against transcript (M29).
3. Per-piece level norm (gain = min(-21-mean, -1.5-max)); room beds cut
   from the same file's own pauses; afade bounds explicit (never bare).
4. Span-hashed cut filenames; sheet==master asserted every render (M24).
5. QA per proof with `listen.py` presets only (M26); findings need
   corroboration (second pass or measurement, M25); voice-ID claims need
   transcription corroboration (M33); cross-voice joints are doorways.
6. Provenance: every window traceable to file+timestamp; every doc edit
   count-asserted (M17); every fix logged with cause (M-log).

**Subjective parts (isolated, flagged, never decided by agent):**
A-curation (which passage = core), long-vs-tight calls, B1 voice choice
where two voicings exist, cross-voice treatment, final drag/pacing feel.
These go to owner ears as flagged decisions with evidence both sides.

## PART 2 — Per-text config (fill this for each new text)

1. Verse list: count, divisions, numbering authority + known traps
   (splits, merges, transpositions vs other editions — record each).
2. Corpus map: which files cover which verses (per-verse files OR
   session ranges with timestamps; review-heads and combined files noted).
3. Role fill: TEXT / EXACT / TRUST / VOICE / coda / BOOK with paths.
4. B1 fallback chain for unvoiced/garbled verses (re-pass → other voice
   exact slice → TTS, in that order).
5. Runtime bands per layer (from verse count × A-budget).
6. Rights + licensing per source (what may ship, what is cut-only).

## PART 3 — Worked port: Yoga Sutras (Patanjali)

Status: corpus present at `/home/ubuntu/yoga-sutras/` (14 Sharma sessions,
~20 h, WMA originals; chant + explanation with Vyasa + Vacaspati Misra).
Config sketch (to verify against the audio, not assumed):
- Verses: 196 (4 padas); numbering per standard edition; traps TBD at
  template build (compare GRETIL Yoga Sutras vs session coverage).
- Corpus map: sessions cover pada ranges (see yoga-sutras/README.md);
  per-verse cutting needed (sessions, not per-verse files) — locate pass
  is heavier here than Shiva; budget accordingly.
- Roles: VOICE = Sharma (states + explains — same voice, simpler than
  Shiva); TRUST = TBD (choose published translation; compare candidates
  against his glosses the way Dyczkowski was compared); EXACT = GRETIL
  Yoga Sutras text; BOOK = TBD (choose per-verse commentary guide);
  coda voice = Sharma complete recitation (exists? verify — else assemble
  per-verse chants into a full run).
- Expected shape: 0 ≈ 196 × ~30 s ≈ 100 min; A (≈1 min/verse) ≈ 3.5 h.
  Longer than Shiva — bands scale with verse count, law unchanged.
- First moves: transcribe sessions → verse list + numbering check →
  template_ys.json → locate B1s (dip-snapped + word-verified) →
  pilot one pada-1 verse end to end.
