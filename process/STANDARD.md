# STANDARD COMPILATION — the complete build manual (self-contained)

This document builds the Standard and nothing else. It does not reference
Custom artifacts except at the boundary (§10). If it ever conflicts with a
root doc, fix this file the same day.

## 0. What the Standard is

- **Fidelity object.** All 77 sūtras in sūtra order. Nothing skipped,
  nothing reordered, no argument imposed. Completeness is the product.
- **Layers (russian doll, append-only):**
  - **0** — verse + meaning only, per verse in order: (1) his Sanskrit
    reading, (2) AI voice reading Dyczkowski's translation verbatim (the
    trusted wording), (3) his English rendering. No explanation, no
    guests, no heads, no bells.
  - **A** — 0 + one compressed explanation passage per verse (~1 min/verse,
    whole of A ≈ 1 hour). The "oh, that's it" cut.
  - **B** — A + doctrine depth. Guest voices enter here, sparse and
    relevance-gated.
  - **C** — B + full lecture weight, stories, tangents, all guests.
  - **Coda** — Sharma's complete run after the last verse (mangala + 77
    sūtras + closing, ≈9 min). The text heard whole.
- **One-voice law:** 0 and A are Lakshmanjoo only (plus the AI translation
  line). No human guest speaks before B.
- **Source hierarchy:** (1) the sutras themselves; (2) GRETIL Kaul text =
  exact Sanskrit wording; (3) Dyczkowski = trusted English wording;
  (4) Lakshmanjoo book = what each verse's explanation must cover;
  (5) his lectures = the voice. Disputes resolve upward (text wins).

## 1. Inputs & provenance

| input | location | rule |
|---|---|---|
| Lakshmanjoo per-verse mp3s (79 files, ~16h) | `/home/ubuntu/shiva-study-set/` (OUTSIDE repo, never copy in) | read-only masters; never edit, never commit |
| Sharma complete chant (26:35) | `audio/chant/sharma_siva_sutras_2009.mp3` (+ whisper locate txt/json) | B1 fallback + coda source |
| Dyczkowski Aphorisms (held) | `reference/` (gitignored, copyright) | quote line-refs only, never the text |
| Lakshmanjoo book (Supreme Awakening) | `/tmp/opencode/lakshmanjoo_book.txt` (extracted) + `build/template_77.json` | A-selection guide, his English reference |
| GRETIL Kaul Sanskrit | patalacheckpoints corpus `sivasutra.txt` | exact Sanskrit forms |
| CF whisper (large) | `tools/cf_transcribe.py` (creds env-only) | garbled-head re-pass only |

## 2. Stage 1 — Transcribe

`python3 tools/lak_transcribe.py` (local faster-whisper base, idempotent —
reruns skip finished files). Output per file:
`text/lak_*.txt` (`[HH:MM:SS] segment` lines, the quote source-of-truth) +
`transcripts/lak_*.segments.json` (float timestamps for the locate pass).
ASR renders Sanskrit approximately — never quote Sanskrit from ASR; English
is reliable enough for finding, never for publishing.

## 3. Stage 2 — Template (the cornerstone)

`build/template_77.json`: one entry per verse — Academy key, GRETIL exact
Sanskrit (`sanskrit_exact`), Dyczkowski translation + book line-refs,
Lakshmanjoo's English (`lakshmanjoo_T`), book page, exposition body.
Built by `tools/build_template.py` + `tools/fix_template_l3.py`.
Numbering traps (recorded, do not re-derive):
- Book inserts an extra visarga-sutra at 3/15 (no Ksa counterpart):
  Academy 3.15+ maps to book 3/(N+1).
- Book splits Ksa 1.16 → 1/16+1/17 (Academy 1.17-22 ↔ book 1/18-1/23).
- Book transposes prana/madhye vs Ksa+GRETIL+lecture order: Academy 3.22
  ↔ book 3/24, Academy 3.23 ↔ book 3/23. Map by CONTENT, never by number.
- Two Ksa sutras absent from GRETIL (turya 1.7, hrdaye 1.15): his voicing
  IS the reference; verified against Dyczkowski's front-listing.

## 4. Stage 3 — Locate (B1 + B2 per verse)

B1 = the sutra voiced, nothing else (M31: book/GRETIL-verified form).
B2 = his adjacent English gloss, sentence-complete (M29).
Method, in order: (1) grep the transcript for folded Sanskrit keywords;
(2) confirm the candidate by reading surrounding lines; (3) snap onset to
the word with `tools/word_onset.py` (M27: transcript segments are not
speech onsets; M30: no filler words — and/so/now belong to the previous
thought, never open 0); (4) extend B2 to the sentence end.
Fallbacks, in order: his voicing (default) → Cloudflare large-model
re-pass for garbled heads → Sharma exact slice, word-verified (mark
`b1_status: sharma`). Record every window in `build/std_N_N.json`
(`src`, `room_t` from a measured pause ≥1.2s in the SAME file, `b1_status`).
`b1_status` is a CLOSED enum, asserted by the builder (M36): `his-verified`
(his statement, word-verified onset + book/GRETIL form) · `his-prov`
(located, verification pending) · `sharma` (Sharma exact-slice fallback) ·
`cf-done` (CF re-pass transcribed, his voicing cleanest there) · `cf-owed`
(garbled head, re-pass still owed).

## 5. Stage 4 — Curate (A, then B, then C)

A = one passage per verse covering the book's point for that verse (~1 min
total with 0; whole of A ≈ 1 h). Read the book section, find where he
speaks those points in the lecture, cut tight, never pad, thin stays thin.
B = +doctrine depth (citations, practice, +5–10 min/verse). C = +stories,
tangents, guest voices (only here). Guests: Baumer, dl1, Osho, Hareesh —
relevance sentence mandatory per insertion; rights per SOURCES.

## 6. Stage 5 — Build

`python3 tools/build_standard_verse.py build/std_X_Y.json` → per-layer
wav+mp3 in `audio/gen/std/`. Engine rules (violations fail the build):
span-hashed cut names (never bare indices, M24); explicit afade bounds
(st=, M25-silence lesson); per-piece level norm (gain = min(-21-mean,
-1.5-max)); room-tone beds cut from the verse's own pauses (never digital
silence, never brown noise); breath 2.5s / tbeat 1.0s / water 2.5s.
Cross-voice joints are DOORWAYS (accepted as heard seams; no bells in 0/A).

## 7. Stage 6 — QA (ears + measurement)

- `tools/listen.py <mp3> qa|joints` (Qwen omni default; presets only, M26).
- Every flaw needs corroboration: second pass OR transcript/energy
  measurement. Single-pass claims are hints (M25).
- Model failure modes on record (M33): hallucinates TTS voices on
  single-speaker files; misreads pauses as cut-offs. Voice-ID claims need
  transcription corroboration; never rebuild on uncorroborated verdicts.
- Fix classes: mid-sentence cuts (extend to sentence end), dead-head
  onsets (snap to word), B2 overruns (trim to gloss), cross-voice seams
  (accepted, doorway).
- Re-QA after every fix. Record verdicts per verse in the session log.

## 8. Stage 7 — Assemble 0, then A, then B, C, coda

Per-verse proofs concatenate in verse order (0/0A assessments first;
full-walk assembly only after every verse passes QA). Coda = Sharma run
cut 267–711 s (mangala + 77 + closing), lightly cleaned. Sheet asserts
sheet==master on every render (M24).

## 9. Stage 8 — Ship gates

`process/verify.sh` green · every A ≤ ~90 s (compression pass for
overruns; pilot set first) · B2 gloss present per verse · B1 forms
book/GRETIL-verified · rights cleared (Academy material) · R2 upload
HEAD-verified · owner ear on 0 + A. B/C ship after A locks.

## 10. Boundary with Custom (the only contact)

Nothing composed for Custom enters Standard; nothing in Standard is cut
to flatter Custom. Custom MAY reuse: located B1/B2 windows, the template,
the book hooks, QA verdicts (as evidence, not as structure). Standard
never imports: spine questions, essay-0 cells, A/B/C grades, clustering,
arguments, or reorderings. Shared tools live in `tools/`; shared law in
`process/AXIOMS.md`; everything else is separate.

## 11. Worked example — 1.1 (the shape every verse follows)

- B1 [78.7→82.4 minus filler → 79.8→82.4, word-verified]: "chaitanya-mātmāma"
- B2 [82.4→98.6]: "The supreme consciousness is the reality of everything..."
- A-core [167.3→199.0]: independence as the uniting agency, possessed by
  Paramashiva only. A-cap [826.9→847.6]: one universal being.
- 0 = 22 s, A = 80 s. QA: clean build, texture accepted, FLOW (1.3 twin).
