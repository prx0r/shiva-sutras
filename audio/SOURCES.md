# AUDIO SOURCES — chant + third voices (local only, gitignored)

Rule: `audio/` never commits. This file is the inventory so a fresh agent
knows what is here, where it came from, and what it is FOR. Order of the
voice stack (Video 1 → Video 2): **chant → card/TTS → Baumer → Dyczkowski +
podcast where it fits**.

## gen/sfx/ — signal kit (ported 2026-10-28 from vatulanatha/sfx/, royalty-free sources)
| file | what | use |
|---|---|---|
| `bowls_intro.wav` | singing-bowl swell→strike→decay 12.76s (mono re-encode of kit stereo) | program open |
| `long_break_bell.wav` | section bell, 4.7s strike+decay (mono) | section motto + close |
| `room_*.wav` | lecture-room tone pads (cut from Baumer lecture gaps, same durations as v1 digital) | breath/gap/tbeat/water/xl — no digital silence anywhere |
| kit spares (`bell_ding`, `block_*`) | copied, unused | future emphasis marks |

## chant/ — Sanskrit recitation sources
| file | what | provenance | rights | use |
|---|---|---|---|---|
| `sharma_siva_sutras_2009.mp3` (25M, 26:35) + `.txt`/`.json` whisper-locate | Ram Karan Sharma chants the complete Sanskrit text + English overview, recorded San Francisco 17 June 2009 | mywhatever.com RKS archive, direct mp3 | public page, scholar archive — attribute; cut-only, never redistribute | **Video 1 seed cuts.** All six seeds located: 1.1/1.2/1.5 @ ~04:27 run, 1.11 @ ~05:08, 2.1 `Chittang Mantraha` @ ~06:32, 3.9 nartaka @ ~08:03. Run-on chant = tight slicing needed. Transcript: whisper, for locating only — trust Sharma's voice, not the ASR. His handwritten Devanagari sheets (2 pp, 1700×2170) held at `reference/sharma/` (gitignored, read-along only) |
| Kumuda/Sharon Janis full recitation | Sanskrit + English, recorded 1982, Siddha Yoga lineage; YouTube `DwTTEEwDnG0` + spiritual-happiness.com streaming | Night Lotus | **NOT downloaded** — YouTube bot-blocked yt-dlp 2026-10-26; manual pull needed | Backup chant source if Sharma slicing proves too tight; has musical bedding — check before cutting |

## third/ — English commentary beyond Baumer + Dyczkowski
| file | what | provenance | rights | use |
|---|---|---|---|---|
| `hareesh_ep78_shiva-kaul-transmission.mp3` (61M, 1:05:33) + `.txt` (929 lines, stamped) | Hareesh + Ben Williams on Śiva Sūtra origins, commentaries, 65-manuscript Vimarśinī edition, Kaul lineage, ritual manuals | Acast public RSS enclosure, transcribed via cf_transcribe | podcast, fair-use excerpting — do not ship whole | Fits: S1 intro (origins/commentary circulation), print-verify note (await Williams edition before freezing cards). NOT Sanskrit recitation — no seed cuts here |

## Gated / manual (not yet local)
- **Lakshmanjoo Academy** — 15h50m original 1975 lectures, free with shop order (`lakshmanjooacademy.myshopify.com`, SHIVA_SUTRAS). Manual checkout step. Best-fit lineage voice for seed cuts if Sharma fails.
- **Pradipaka pronunciation 3/4/5** — per-aphorism MP3s behind JS player (sanskrit-trikashaivism.com). Manual save-as needed. Cleanest single-sutra enunciation if bulk pull works.
- **Dyczkowski 60-lecture course** (~100h, anuttaratrikakula.org, $50/section). Paid. Would expand dl1 second voice beyond the 20-min intro — v2 scope.
- **Hareesh Sutra Project First/Second/Third Light** (thinkific, paid). Per-sūtra audio + meditations. Paid. Candidate S5/S6 gloss at ear-session, not v1.
- **Sally Kempton Splendid Path** (14+h, $49). Paid practical commentary. Not pulled.
- **Osho 10 Hindi discourses** — DONE 2026-10-26, all ten local in `audio/third/osho_shiv_sutra_01..10.mp3` (~14h total, durations match OshoWorld listing). Track 3: Hindi-learning strand; English-TTTS-over-Hindi idea needs a TTS key (see below). **Transcripts: YES, free** — `audio/third/osho_transcripts/` holds all ten Hindi (`osho_hindi_01..10.txt`, ex OshoLive Library Archives) + all ten OshoLive English translations (`osho_english_01..10.txt`). The English script for the TTS-over-Hindi idea already exists — no translation work needed, only voicing.

## `audio/third/osho_*` — durations verified
01 1:41:03 · 02 1:37:39 · 03 1:34:15 · 04 1:32:33 · 05 1:22:48 · 06 1:35:25 · 07 1:24:27 · 08 1:14:45 · 09 1:23:14 · 10 1:20:37.

## `audio/gen/` — build outputs (regenerable, gitignored)
- `l0_essay0.wav/.mp3` — L0 prototype 3:15, built 2026-10-26 by `tools/make_l0.py`: Q(espeak) → breath → Sharma chant → T+P(espeak) → Baumer cell, ×6, bell-headed, loudnormed. **Placeholder voices**: espeak (edge-tts egress-blocked, Fish key outstanding) + proportional Sharma splits (ear-check). Swap engines, rerun.
- `l0_cuts/` — per-cell intermediates.

## TTS position (2026-10-26, updated same day)
Fish s2.1-pro-free default voice is live for all TTS (owner-supplied key, env-only). espeak retired to fallback-only. TTS_SAY map covers spoken-form fixes (Bhairava verified by isolated probe).

## Already in `audio/` root (the Baumer + dl1 corpus)
14 mp3s (~1.4G): 13 Baumer sessions + `Shiva_Sutra_Introduction.mp3` (dl1). See MANIFEST.json for id→session map.

## R2 packs (keys in ~/figgsite/.env, never in repo)
- `longform-audio/shiva-sutras/essence_v1.mp3` (3.2 MB) — the essence master, HEAD-verified on upload.
- `longform-audio/shiva-sutras/osho-hindi-10-talks.zip` (327 MB) — all 10 Osho Hindi discourses, HEAD-verified on upload.

## Third-party study set (verified 2026-10-26, other session's upload)
- `powpowpow-warehouse/shiva-sutras-study-set.zip` (447,966,762 bytes, exact) — archive as-is.
- `powpowpow-warehouse/shiva-sutras-study-set/` — 79 files extracted, 464,519,969 bytes total (uncompressed > zip, as expected).

## Lakshmanjoo study set (imported 2026-10-26, lives OUTSIDE repo)
- Local: `/home/ubuntu/shiva-study-set/` — 79 per-verse files ("Shiva Sutras 1.1.mp3" …), 464,519,969 bytes, byte-identical to R2 (`powpowpow-warehouse/shiva-sutras-study-set/`). Verified voice: Lakshmanjoo himself lecturing in English, states each Sanskrit sutra (spot-check 1.1: Nara-Ishvara-bheda refutation → "the sutra is Chaitanya Mahatma"). The missing second archive voice WITH sutra voicing — candidate for B1 Sanskrit + B3 explanation upgrades (rights: Academy material, attribute; check license before shipping cuts).
- Disk note: box at 94% — this set + audio/ = ~2.4 GB local. Do not duplicate into the repo.
