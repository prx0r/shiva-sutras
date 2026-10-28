# SPEAKERS — who speaks what (v1 state + Standard v2 2026-10-27)

## Standard v2 (canonical — Custom rows below unchanged)

| role | voice | owns | v2 status |
|---|---|---|---|
| **LAKSHMANJOO** | archive (`/home/ubuntu/shiva-study-set/`, 79 files, outside repo) | Standard B1 (sūtra statements, measured per-verse) + B3 (English, verbatim excerpts) | locating (11/14 measured, pilot 1.1+1.2 verified) |
| **SHARMA** | archive (`audio/chant/sharma_siva_sutras_2009.mp3`) | Standard coda only (mangala + 77 sūtras + closing ≈ 9 min) | located, uncut |
| **READOUT** | his adjacent gloss, verbatim | Standard B2 per verse (same take as B1 where adjacent) | locating with B1 windows |

## Custom v1 (frozen — untouched by v2 work)

| role | voice | owns | v1 status |
|---|---|---|---|
| **BAUMER** | archive (`audio/ss*.mp3`) | all ss1–ss13 unit clips, essay-0 cell clips | final (the material) |
| **Dyczkowski** | archive (`audio/Shiva_Sutra_Introduction.mp3`) | dl1 clips (S1) | final |
| **HUMAN** | questions (6, per section × layers) + any bridges | opens every beat | **v1 = TTS placeholder** — owner re-records (~24 openers ≈ 2 min of speech) |
| **PLAIN/TEXT** | sanskrit words + translations + plains (card rows) | opener stacks | **v1 = Fish s2.1-pro-free default voice** (espeak retired 2026-10-26) · spoken-form map `TTS_SAY` in builders (display text never changes) · regenerate after key sign-off |

Rules carried (SPINE gospel / FORMULA / analayo 04):
- Order fixed: question → pause → card (S→T) → plain → archive voice. No plain
  before translation, no voice before plain.
- HUMAN owns questions at ship (TTS is placeholder only); archive never reads the
  card rows — the card is machinery, not her words.
- Sanskrit spoken by TTS at v1 = pronunciation unverified → **ear-check the six
  forms** (caitanyamatma · jnanambandhah · udyamo bhairavah · tritayabhokta vtresah
  · cittam mantrah · nartaka atma) — if bad, drop S-row from AUDIO (card stays
  visual-side at video build) rather than ship a mispronunciation.
- Plain rows are mechanical (`plain_filter` + key) — never hand-edited; TTS line =
  row-3 text verbatim from ESSAY0_OUTPUT.

TTS voice used (Fish): see `audio/gen/tts_meta.json` (written at generation).
