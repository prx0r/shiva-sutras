# HANDOVER — Standard build, B-rollout in progress (2026-10-27)

## State in one paragraph
A is DONE for all 77 verses (built + QA-sampled, gates green). B is proven
on 1.1 (FLOW, 4.4 min) and 1.2, and built for 1.3-1.10 (QA sampled, defects
fixed as found). Everything after 1.10 needs the same treatment. C exists
only as sketches. TTS B1b line, coda assembly, and owner ears are pending.

## The B method (do not reinvent — copy it)
Per verse, in order: (1) HIS continuation — deeper lecture cuts A didn't fit
(b-his, same file, sentence-complete, word-verified onsets);
(2) HER (Baumer) clips nailed 1:1 to book hooks A leaves uncovered — pick via
`tools/b_match.py` (metric proposes) then HUMAN verdict (metric never decides);
(3) AI voice reading Dyczkowski VERBATIM only where neither human carries the
point (Varttika lines, technical distinctions, print variants).
Assemble with `tools/build_standard_verse.py` (manifest-driven, room beds,
afade, per-piece -21dB norm). QA with `tools/listen.py` (qa for texture,
joints for seams). Corroborate every defect before rebuilding (M25);
voice-ID claims are IGNORED without transcript corroboration (M33 hallucinated
TTS 6+ times — always check the build contains no TTS first).

## Key files (read in this order)
1. `build/template_77.json` — per-verse book Sanskrit + translation + exposition bodies + GRETIL exact forms (the A-checklist and B-hook source).
2. `build/std_N_M.json` (77 files) — per-verse manifests; layers 0/A/B/C/D append-only (builder concatenates in order).
3. `tools/b_match.py` — Baumer candidate ranker per verse (run: `python3 tools/b_match.py 3.12`).
4. `tools/cov_check.py` — book-vs-audio coverage audit (flags GAPs for verdict, not truth).
5. `tools/tts_line.py` + `TTS_SAY` map inside it — Fish TTS, isolated-probe verified forms only.
6. `process/STANDARD.md` (build law) + `process/STANDARD-PORTING.md` (porting) + this handover's predecessor notes in `PROCESS_NOTES.md` §8l/§8k.
7. `MISTAKES.md` M17-M33 — every load-bearing rule was paid for; read before touching tools.
8. Gates: `bash process/verify.sh` (units 307/0, G0 7/7, plain MATCH) + `python3 tools/count_a.py` (77/77 with 0+A).

## Open queue (in order)
1. B for 1.11–1.22 (matcher output in /tmp/opencode/bmatch_all.txt — re-run if stale; verify each window with word timestamps; build; QA sample).
2. B for ch2 (2.1–2.10), then ch3a/b/c in order.
3. TTS B1b line: Dyczkowski translation per verse (Fish; same probe discipline).
4. C layer: full walk per verse (A+B+stories + guests: Osho/Hareesh/dl1 mapped sparingly + Sharma coda already located 267–711s).
5. Full assembly → R2 → owner ears (ears are the ONLY lock; agents never sign off).

## Standing decisions (do not reopen without owner)
- 0 = B1 (his Sanskrit, word-verified) + B2 (his gloss) + TTS B1b (pending). No TTS elsewhere except book-verbatim gold.
- B1 = sutra ONLY (M18/M30/M31). B2 ends at sentence completion (M29).
- Cross-voice joints are DOORWAYS (accepted RUBBED); bells only at section heads.
- Verse order always; thin verses stay thin; never pad, never cut audited membership.
- Tree is dirty (uncommitted) — commit in verse batches with count-checked messages.
