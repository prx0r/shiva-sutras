# Śiva Sūtras excavation schema (ported: vatulanatha/_SCHEMA.md ← analayo 01–06)

Each session -> one file `excavations/ss<N>.md` (`ss1` = Day 1 introduction I … `ss13` = Day 6 session II;
ss4 = Day 2 session I [CF], ss12 = Day 6 session I [CF]).

## Unit shape (all fields required)
- `uid`: `ss<N>-<nn>` stable, never reused (e.g. `ss5-03`)
- `timestamp`: `[HH:MM:SS]-->[HH:MM:SS]` from `text/*.txt` line stamps (same base as mp3)
- `topics`: 1–4 tags from the closed union list below
- `role`: claim | simile | refutation | story | lineage | method | practice | mantra-gloss | history | reading
- `quote`: Bäumer's words VERBATIM from `text/<session>.txt` (timestamps stripped for the audit)
- `context`: 1–2 lines — what she is answering / what comes before-after
- `grade`: A = clip/essay-ready · B = good with edit · C = do not use (namaskar tails, thank-yous, garble, head silence)
- `layer`: `read` = she is voicing a sūtra/commentary text · `explain` = her own words. No formal decompile pass in this project — layer is judged at write time from the read, and any locus she names goes in `context` with the source cited.
- `essay_use`: one line how this is reused (essay-0 / beat / B-depth / cross-link)

## Closed topics (union of vatulanatha 17 + tantraessays 9; add only with a note)
grace, sudden-enlightenment, madhya, speech, sound, senses, kula, guru, recognition,
nonduality, praxis, mantra-gloss, lineage, death-rebirth, ethics, ritual, cosmology, tattva,
doctrine, history, kundalini, mantra, initiation, devotion, tantra-comparative, shiva-sutras, tantraloka

## Rules (from analayo AXIOMS + vatulanatha MISTAKES)
- Quote must substring-verify in `text/<session>.txt` after `[HH:MM:SS] ` stamps are stripped. Timestamps must exist in the source file.
- Sanskrit is never quoted from ASR/Y-T captions: card material comes from held e-texts only (Dyczkowski Aphorisms, Kshemaraja). If she voices a sūtra, quote her English, name the sūtra in `context`.
- Grade pyramid target (global): A small, B larger, C honest. Never pad thin sessions to quota.
- Every file ends with `## Reuse clusters` + `## Cross-links` (session-internal clusters; poles to other sessions / Dyczkowski units / held texts).
- Every fix logged in PROCESS_NOTES; verify script `tools/verify_units.py` runs green before anything downstream consumes a quote.
