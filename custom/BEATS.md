# BEATS — the four-layer run order, bell grammar, assembly recipe (v1)

Owner-locked shape (HANDOVER box, vatula `FORMULA.md` VIDEO RUN-ORDER):
`[BELL] 0 → [BELL] A → [BELL] B → [BELL] C`, seed heard **4×**, A ⊂ B ⊂ C,
append-only, machinery (question/card/plain/bell) lives INSIDE the layers as
section openers. This doc is the build instrument for the audio master.

## Layer files (machine sources = `build/manifest_s{1..6}_{A,B,C}.json`)

| file | contents | clips | windows | + openers/essay0 ≈ |
|---|---|---|---|---|
| `L0` | essay-0 only (6 cells) | 6 cell-clips + 6 Q/S/T/P stacks | — | ~4.5m |
| `LA` | essay0 → S1..S6 A | 76 | 23.5m | ~36m |
| `LB` | essay0 → S1..S6 (A ∪ kept-B) | 159 | 53.2m | ~66m |
| `LC` | essay0 → S1..S6 (all, her order) | 300 | 95.4m | ~110m |

Master = L0 → [zoom] → LA → [zoom] → LB → [zoom] → LC ≈ **3.4h (v1, cumulative
canon)**. Delta-replay alternative (each clip once) is NOT the locked form — noted
as the single biggest ear-decision if v1 runs too long.

## The beat grammar (per section opener — every layer, every section)

```
[motto-bell 880 Hz / 2.5s]
QUESTION            (TTS v1 — HUMAN voice at ship; 6 questions, reused audio)
(2-breath pause ≈ 2.5s)
SANSKRIT + TRANSLATION   (card spoken: "caitanyamatma. Consciousness is the Self.")
PLAIN                   ("consciousness is the self")
(1.2s)
UNIT CLIPS in order     (her words — each clip afade 0.15, 1.2s gap)
(2.5s water)            → next section
```

essay-0 cell (the seed stack, plays at every layer head incl. L0):
`QUESTION → 2-breath → SANSKRIT → TRANSLATION → PLAIN → BÄUMER-CELL clip` — same
six cells, `ESSAY0_OUTPUT.md` is the text source. SEED-CAP: cell clips (ss3-10,
ss4-15, ss12-16, ss7-06, ss11-05, ss13-09) appear ONLY here, never in section lists.

## Bells (analayo 09-BELLS-ZOOM pattern, ported)

- **motto-bell 880 Hz / 2.5s** — opens every section (12-grammar slot = the question cue).
- **zoom-bell 220 Hz / 6.0s** — layer crossings only (L0→LA, LA→LB, LB→LC).
- Levels: standalone cues sit UNDER voice level (−20 dBFS-ish peak); never mask speech.
- Generate once (`tools/make_audio.py`), reuse: `audio/gen/bell_880.wav`, `bell_220.wav`.

## Levels & seams (analayo 05-RENDER)

- per-clip `afade t=in:d=0.15` / `afade t=out:d=0.15`
- full-mix `loudnorm I=-16:TP=-1.5:LRA=11` per layer file (then concat layers —
  re-encoded concat, never `-c copy`)
- pads v1 = digital silence (1.2s beat-gap / 2.5s group / 2.5s breaths);
  **at ship = room-tone breaths from lecture gaps** (analayo rule — flagged v1 placeholder)
- pause-snap (±0.3s to nearest silence) = audio-QA pass, not yet run

## Run-time honesties (recorded at build, 2026-10-26)

- A = 23.5m vs FORMULA band 10–20m: 76 clips at quote-tight cuts; band assumed
  fewer clips. Levers at ear: none taken (A = UNFOLDING-audited; no clip cut for
  runtime) — owner decides at the ear-session whether band or A-membership yields.
- B = 53.2m windows vs band 20–40m (cumulative-play semantics make bands
  per-artifact, as in vatula's G10 honesty).
- 16 clips have caption-lag padding (bounded ≤ words/2.0 + 5.5s) — ear-QA list.
- C = 95.4m windows = full unit-walk; holes (uncovered ledger spans) documented
  in `COVERAGE_LEDGER.tsv`, never silently bridged.

## Assembly pipeline (`tools/make_audio.py`)

1. **TTS** (once): 6 questions, 6 sanskrit lines, 6 translations, 6 plains →
   `audio/gen/tts_*.mp3` (Fish; voice in `SPEAKERS.md`).
2. **Bells** → sine 880/220 with fade (ffmpeg).
3. **Cuts**: per manifest beat → `audio/cuts/{uid}_{layer}.wav` re-encode ±0.15 handle.
4. **Section build**: opener stack + clips + pads → `sections/{L}_{Sn}.wav`.
5. **Layer build**: essay0 + sections + zoom-bell → `L{0,A,B,C}.wav`, loudnorm each.
6. **Master**: layer concat re-encode → `shiva_v1_master.wav` (+ mp3 -q:a 2).
7. **QA gates before ear**: verify_units 307/0 · every cut file exists · durations
   within bounds · no silent >8s (except pads) · loudnorm measured (ebur128 print).

## Levers held for the ear-session (flow-read notes, unchanged)

- S4: `ss7-16` icchā (A) demote→B if the section sags — NOW MOOT: it stays A until
  the ear says otherwise (A-demote at ear only).
- S6: `ss13-06` dancer promote A ← already judged KEEP-B this sweep; promote only
  if flow-read says S6 sags (held).
- S5 closure: answer mid-section vs guru-grace closer — re-test with audio.
- Joins: 4→5 (S4→S5 question chain) + the 2 named bridges (S1 thesis→speech,
  S5 question→means) — bridges are NOTE-lines in SA; in audio the opener
  (question→card) provides the bridge; listen whether it suffices.
