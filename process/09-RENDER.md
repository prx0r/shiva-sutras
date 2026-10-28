# 09 — RENDER (final-final; the SHEET is the shippable product).

Render executes a validated sheet and nothing else. No render talk until
`validate_sheet.py` is green AND ears have signed the sheet — the sheet
is what ships for review, the master is what ships for ears. Same rule
both compilations. TTS placeholders → cuts → concat → loudnorm → listen.

## Preconditions (all verified before a single cut)
Text gates green (verify N/0, G0, plain MATCH, totals reconcile);
manifests cut with every stamp located; re-cut to sentence-complete,
silence-snapped bounds after ANY manifest touch (`tools/recut_sentence.py`,
M39); automated cut-verification green (cut edges transcribed, first/last
words == unit quote, M40); TTS lines scanned (no dead air, no orphaned
punctuation, English-first, traceable to card/key/bridge); every cut file
exists; pause-snap done; EAR_CHECK list ready. Fish-only TTS (no fallback
engine — outages fail loud, M39).

## Assembly (`tools/make_audio.py` pattern; prototype: `tools/make_l0.py`)
1. TTS once: questions, Sanskrit lines, translations, plains → `gen/`.
2. Bells → sine 880/220 with fades, generated once, reused.
3. Cuts per manifest beat → `cuts/{uid}_{layer}.wav`, re-encode ±0.15
   handle (mp3 `-c copy` concat throws warnings — re-encode for real).
4. Section build: opener stack + clips + pads.
5. Layer build: essay-0 + sections + zoom-bell, loudnorm each
   (`loudnorm I=-16:TP=-1.5:LRA=11`).
6. Master: layer concat re-encode → wav + mp3.
7. QA gates before ear: verify N/0 · durations in bounds · no silent >8 s
   outside pads · loudnorm measured (ebur128) · bells under voice ·
   cough/artifact hunt.

## The listen pass (ears — never automated away, never skipped)
Fixed layers played end to end. Checklist: join breaths, bell levels,
lever decisions (demote/promote/re-ask per the audit watch-lists),
closure tests (does each section land where its question expects?),
cough cover (micro-cut ±0.3 s or breath bed — hunt, don't sweep).
Ears sign off or it doesn't ship. TTS engine swaps (placeholder → Fish →
human) change files, never layout: block order is engine-independent.
No master uploads without a listen pass on the assembled audio (per-section
joints minimum; qa sample before any link goes out — M39). The surgery
preset (`tools/listen.py`: FIRST3/LAST3/HEAD/TAIL/VOICE/VERDICT) is the
standard per-clip protocol: corroborate every CUT against transcript +
waveform, fix, re-verify the fixed clip before rebuilding the master.
