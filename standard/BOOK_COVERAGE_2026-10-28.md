# BOOK COVERAGE — Dyczkowski cutting points vs Standard 0/A/B (2026-10-28)

Question: do our 0/A/B layers cover every cutting point of the Aphorisms exposition?
Method: per verse, book body → model proposes 3–7 major cutting points (v2 prompt,
book's joints, not 3-sentence chunks) → each point COVERED (clip+quote) or GAP.
Model output is PROPOSAL (`build/BOOK_GAPS_PROPOSAL.tsv`, 428 rows); every load-bearing
verdict below was hand-corroborated against transcript + book (M25/M33 discipline).

## Headline
- **0/A/B exist for all 77 verses** (0 = his Sanskrit + Fish translation + his gloss,
  A = core passage, B = his continuation + her clips + TTS gold). count_a 77/77.
- **Core-claim (P1) level, hand-verdict all 20 model-flagged verses:**
  COVERED 6 (2.1, 2.8, 3.7, 3.23, 3.31 overturned as model strictness —
  paraphrase counts; 1.22 fixed, see below) · SOFT 8 (core carried, specifics
  thin: 1.14, 1.20, 2.4, 2.10, 3.11, 3.33, 3.37, 3.44) · REAL GAP 6
  (1.19 five-powers listing · 3.4 forces-definition · 3.16 breath/Matsyavalana half ·
  3.19 sabdarasi/kala/bija-yoni structure · 3.41 perceiver-domain · 3.24 core +
  B1 defect, see below).
- **Model precision (measured):** lexical strictness costs real misses — "great ocean"
  vs "Great Lake" (same referent) flagged GAP; Paramesvara vs Siva flagged GAP;
  two direct-hit Baumer clips (ss12-12, ss1-14) missed on 2.8. Treat every model GAP
  as suspect until read. Conversely the model caught two genuine mis-locations no gate
  sees (1.22, 3.24 review-heads) — text gates cannot catch wrong-content audio.

## Defects fixed today (corroborated, rebuilt, qa clean)
1. **1.22 A-core was the previous verse's review** ([9,29.8] "reside peacefully" =
   1.21 tail). Re-located to the Great Lake/ocean passage [158,231]; rebuilt; qa zero FAIL.
2. **3.24 B1/B2 were review-heads** ([1,7] "he explains this in next sutra").
   Re-located to the statement+gloss [58,73]+[73,112]; rebuilt; qa clean, zero flags.
3. **1.9 B duplicate** (same 16s his-cut twice) removed; proof rebuilt.
4. **Audit-input blindness fixed:** `segments_for` slug regex missed combined files
   (1.8-10, 2.7 parts, intros) — audits AND qa F3/F4 were silently blind there.
   Fixed with exact slug map; 1.8/1.9/1.10/2.7 re-audited (coverage verdicts improved).

## Confirmed B-completion queue (real gaps, human-verdict)
- 1.19 (five powers + Body of Consciousness/Action), 3.4 (forces definition +
  progressive absorption), 3.16 (breath/Matsyavalana half), 3.19 (sabdarasi/kala/
  bija-yoni), 3.41 (perceiver-domain definition). Method: `b_match.py` + human
  verdict + `locate()` + rebuild + `qa_std.py` (the M37 loop). TTS gold where no
  human carries the point (book-verbatim only).
- Soft 8 → ear/C queue (core carried; specifics thin). No rebuild without ears.

## Known audit limits (do not over-claim)
- His Sanskrit-heavy windows transcribe as garble (base whisper) — the audit reads
  transcripts, not audio; Sanskrit-voiced content is under-counted, never over-counted.
- TTS gold content entered the audit as `why` summaries only (v1 blind spot, fixed v2).
- Non-P1 GAPs (~228) are un-triaged proposals: mix of real Level-2 depth, C-apparatus
  (commentator positions, lists, variants), and model strictness. Sample before acting.
- Osho guests have no timestamps (prose scripts) — unscoutable until whisper-located.

## Files
- `build/BOOK_GAPS_PROPOSAL.tsv` — 428 model rows (verse, verdict, line). Proposal, not verdict.
- `/tmp` scripts (not committed): `book_audit.py` (v1 chunks), `book_audit2.py` (v2 points).
  Promote to `tools/` if re-run; outputs here are the record.
