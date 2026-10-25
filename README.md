# Śiva Sūtras project — transcript stash (pulled 2026-10-25)

Source: R2 `longform-audio` bucket (STALLSHARK creds, never echo).
- `transcripts/` — 22 files = 11 sessions × (en.vtt, en-orig.vtt); YT rolling-caption
  format with inline `<c>` word timings (en == en-orig, raw ASR, needs dedupe-cleanup
  before it counts as a readable transcript; ear-check rule applies).
- `MANIFEST.json` — 13 sessions, video-id → title, transcript: true/false.

MISSING transcripts (mp3 only on R2, need whisper if wanted):
- `KSpk4KO0JY4` Shiva Sutras (Day 2 - Session I)   [91MB]
- `r5wTwUNVYOo` Shiva Sutras (Day 6 Session I)     [150MB]

Not pulled (later): the 13 mp3s themselves (~1.4GB, same prefix).
Head start: vatulanatha/r2-prior/baumer-shiva-sutras-1..8 edit plans (block maps done).
Text side: primary/texts/aphorisms-of-siva-dyczkowski_clean.txt (held), Kṣemarāja vārttika
in corpus, [V] SS 1.1/2.1/3.1 banked in tantraessays.
