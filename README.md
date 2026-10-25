# Śiva Sūtras — Bäumer course → essays (HANDOVER front door)

**What this is:** one primary text (Śivasūtras), covered completely, from two archive
voices: **Bettina Bäumer** (13-session Deer Park intensive, ss1–ss13) + **Dyczkowski**
(introduction lecture, dl1). Text on screen: **The Aphorisms of Śiva** (Dyczkowski, held).
Method = the house formula: *audio of a genius × tough text, voice as the excuse to
finish the text* — questions → pause → four-layer cell → her/his voice.

## Read in this order
1. `PROCESS_NOTES.md` — full session history (§0 inputs → §8g handover state).
2. `MISTAKES.md` — everything wrong, with cause+fix+rule (read BEFORE touching tools).
3. `excavations/SPINE.md` — the six sections-as-questions, gospel law, fit-check, build rules.
4. `build/ESSAY0_OUTPUT.md` — essay-0 + six spine cells (four-layer, verified).
5. `build/ESSAY0_FLOW_READ.md` — the spoken pass (read aloud before any build).
6. `build/SECTION_ARGUMENTS.md` — Essay A as text: all 71 A-clips in order per section
   with flow verdicts (read for argument coherence).
7. `build/JOIN_AUDIT.md` — line-by-line join audit: all 65 adjacent pairs verdicted
   (55 OK / 9 SOFT / 0 WEAK), quote-integrity 71/0, cross-section joints.

## State (handover snapshot)
- **Grading:** 186 units (71A/106B/9C) across 14 sessions — `tools/verify_units.py` = 186/0.
- **Segmentation:** 186/186 one section each — `excavations/SPINE_ASSIGN.tsv`
  (48+ content-verdict overrides logged in `tools/s2_cluster.py`).
- **Spine:** 6 open questions (G0 gate `tools/validate_questions.py` = 7/7 incl. alternate),
  sūtra-ranged, fit-checked vs actual A-pools.
- **Essay-0:** stack built + flow-read done (text-level) — lock = DRAFT, **owner ear pending**.
- **Four-layer gospel:** ratified as law (SPINE §GOSPEL); every S/T row carries
  Aphorisms line-refs; plain rows = proposal-key no-ops until sign-off.
- **Coverage:** units claim 13% of audio-time — **no ledger for the remainder yet**
  (decision owed, PROCESS §8e-1).

## Repo map
```
excavations/   ss1..ss13 + dl1 unit files · SPINE.md · SPINE_PREVIEW (superseded) ·
               CATALOGUE.md · SPINE_ASSIGN.tsv
build/         ESSAY0_OUTPUT.md · ESSAY0_FLOW_READ.md · SECTION_ARGUMENTS.md ·
               JOIN_AUDIT.md · essay0_lock.json (DRAFT) ·
               plain_essay0.json + key_ss1_proposal.json (PROPOSAL) · filters
reference/     aphorisms-of-siva (GITIGNORED — never commit, copyright)
audio/         mp3s (GITIGNORED — local only)     text/  stamped transcripts (14)
transcripts/   raw VTTs (11)   cf/  CF-whisper JSON (2)   tools/  verifiers & pipelines
MANIFEST.json  14/14 sessions with transcript sources
```

## Repro
```bash
python3 tools/verify_units.py      # 186/0
python3 tools/validate_questions.py  # 7/7 (6 spine + alternate)
python3 tools/s2_cluster.py --apply  # segmentation, totals reconcile 186
python3 tools/plain_filter.py --check  # hash MATCH
```

## What's next (owner-visible order)
1. Owner ear on HEAD mp3 → lock essay0.
2. Audio flow-read (real pauses; stress join 4→5, S6 weight) — levers: promote dancer
   ss13-06 or re-ask.
3. Coverage-standard decision (PROCESS §8e-1) before any "full walk" claim.
4. key sign-off → plain regenerate → Sanskrit print-verify (OCR forms).
5. Build: essay0 → A-collate per section → B hold-up selection → C walk → beats → render.
Audio on demand: pull the other 11 Baumer mp3s from R2 (`longform-audio/bettina-baumer-shiva-sutras/`).
