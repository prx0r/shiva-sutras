# SPEAKERS — who speaks what (v1 state)

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
