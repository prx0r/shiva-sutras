# 00 — INPUTS. What you need before anything runs.

## 1. Primary text (held, never committed if copyrighted)
- The complete teaching text in a reference file (here:
  `reference/aphorisms-of-siva-dyczkowski_clean.txt`, gitignored).
  Requirement that matters: it must supply exact SANSKRIT + TRANSLATION
  rows per verse/locus. Every card in every beat cites line refs.
- Sanskrit is never quoted from ASR/captions — card material comes from
  held e-texts only. If the lecturer voices a sūtra, quote her English
  and name the sūtra in context.

## 2. Voices (each lands in `audio/`, gitignored, with a SOURCES row)
- Primary archive: one file per session, same order as the teaching
  (here: 13 Baumer mp3s, ~1.4 GB). Single voice/room preferred.
- Second voice if the corpus has one (here: Dyczkowski intro, 1 file).
  Cross-voice pairs get marked in the unit files.
- Chant voice if Sanskrit must be heard (here: Sharma complete chant).
  Third voices where they fit (podcast, commentary) — never as card
  authority. Each source gets: file, provenance, rights, job
  (`audio/SOURCES.md`). Missing audio does NOT block text work (cut
  positions come from transcripts); it blocks only assembly. Track gaps.

## 3. Transcripts (the bridge between text and audio)
- Per session, stamped lines: `[HH:MM:SS] text` (here: `text/*.txt`,
  14 files, ~13.6k lines). YT rolling-cue dupes merged at build
  (extend-on-prefix, skip-on-contained); CF-whisper JSONs for sessions
  without captions (`cf/`, PID-unique temps, 600 s chunks).
- Word-level timing is REQUIRED, not optional (M40): line stamps lag or lead
  speech by seconds, and every downstream cut inherits the error. Transcribe
  (or re-align) with word timestamps from the start; interpolation is an
  estimate and never a cut point.
- IDs + transcript status per session in `MANIFEST.json`. Regenerating
  anything starts there.

## 4. Tooling present
- `tools/verify_units.py` (the gate), `validate_questions.py` (G0),
  `plain_filter.py` (plain integrity), `coverage_measure.py` +
  `gap_report.py` (coverage), `sync_counts.py` (count sync),
  `s2_cluster.py` (segmentation, REPORT ONLY post-pass-1),
  `build_manifests.py` (cut stamps), `make_l0.py` (audio prototype).
- `ffmpeg`/`ffprobe` + `python3` for render. `espeak` local fallback;
  network TTS needs a key (owner).

## Readiness checklist (all yes before stage 01)
- [ ] Every session has text + audio-or-gap-note + MANIFEST row
- [ ] Quotation vs explanation is field-distinguished in the schema
  (`layer: read` vs `explain` — if your source doesn't mark it, mark
  each unit at write time; everything downstream assumes it)
- [ ] Transliteration scheme fixed once (IAST text, ASCII fold matching)
- [ ] `audio/SOURCES.md` started (it WILL grow — rights per source)
