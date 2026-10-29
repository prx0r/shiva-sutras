# 12 — VOICE SEATS. Who speaks what, with IDs (owner-locked).

Seats, not voices-for-a-day. One seat = one job, one voice, every verse:

| seat | voice | Fish ID | carries |
|---|---|---|---|
| Dyczkowski (English) | voice THREE, deep male | `ef9c79b62ef34530bf452c0e50e3c260` | B1b translations + book-gold TTS lines, verbatim only |
| Sanskrit clarity | Osho, slow 0.85 | `06134e9a49cb4a36997b75402c8a0621` | B1s sutra line per verse (GRETIL-folded) |
| Sanskrit alternates (approved, unused) | Sadhguru / Gurudeep | `37a8fbc200e74961bee0597c3b4e4041` / `82926c3143bc4d259fa9834b96897fad` | fallback if the seat fails ears |

His voice carries A/B depth (the bulk) but never the first run (0 = Osho + Three
only, owner ruling: his levels are choppy). Archive owns source-language authority
(B1 windows stay recorded even where TTS carries the verse); TTS owns clarity and
book-verbatim overflow, never narration. No human guest speaks before B. Sharma is
banned everywhere (M47); `sharma` survives only as a dead enum value so old files
fail loud.

## Casting method (how seats get filled)

Qwen `cast` preset per sample + whisper cross-check + owner ears. Both model ears
must converge before a pick; owner ear overrules both (calibration on record: Qwen
5/5 clarity overrates — Alex rejected by owner ears; base-whisper garbles short
Sanskrit, Qwen hears it clean). New seat, same shootout; no seat changes without
re-rendering its lines, rebuilding proofs, and re-shipping walks. TTS_SAY grows per
line (probe log in comments); display text never changes for voicing.
