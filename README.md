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
8. `excavations/COVERAGE.md` + `tools/coverage_measure.py` — coverage truth + the
   pass-1 ledger state (ledger = `excavations/COVERAGE_LEDGER.tsv`, 678 rows).
9. `HANDOVER-2026-10-25.md` — today's full log: pass-1, structure-pass, M19–M21,
   gotchas, and the exact next moves.
10. `TODO.md` — **the 20-action queue** (start here for work; NEXT = the longer why).
11. `FILEMAP.md` — every path: what it is and why (update it the day you add a file).
12. `BUILD_ENGINE.md` — front door (two-track law + decode method → `process/`) — what an agent executes to build or validate.
13. `process/` — the full engine: stages 00–09, axioms, skills, reproduce, `verify.sh` (same shape as analayo-nibbana/process).

## State (handover snapshot)
- **Grading:** 307 units (82A/83B/142C) across 14 sessions (pass-1: day5_ii +18, day6_ii +21) — `tools/verify_units.py` = 307/0.
- **Segmentation:** 307/307 one section each — `excavations/SPINE_ASSIGN.tsv`
  (48+ content-verdict overrides logged in `tools/s2_cluster.py`).
- **Spine:** 6 open questions (G0 gate `tools/validate_questions.py` = 7/7 incl. alternate),
  sūtra-ranged, fit-checked vs actual A-pools.
- **Essay-0:** stack built + flow-read done (text-level) — lock = DRAFT, **owner ear pending**.
- **Four-layer gospel:** ratified as law (SPINE §GOSPEL); every S/T row carries
  Aphorisms line-refs; plain rows = proposal-key no-ops until sign-off.
- **Coverage:** pass-1 COMPLETE — 678 ledger rows disposition every gap (14/14 files);
  15.5% span / 22.6% words quoted (`--corpus baumer`; re-baselined 2026-10-28);
  owner decision (§8e-1) now only formalizes the form.
- **Standard:** 0+A+B+B1b built 77/77 (77 Fish translation lines ride every
  0-layer); B proofs rebuilt after M37 relocation; `tools/qa_std.py` zero FAIL;
  essence SHEET READY (276.8s). Next: C layer → full assembly → ears.

## Repo map
```
excavations/   ss1..ss13 + dl1 unit files · SPINE.md · SPINE_PREVIEW (superseded) ·
               CATALOGUE.md · SPINE_ASSIGN.tsv
build/         ESSAY0_OUTPUT.md · ESSAY0_FLOW_READ.md · SECTION_ARGUMENTS.md ·
               JOIN_AUDIT.md · essay0_lock.json (DRAFT) ·
               plain_essay0.json + key_ss1_proposal.json (PROPOSAL) · filters ·
               std_*.json (77 Standard manifests) · template_77.json ·
               QA_SWEEP_2026-10-28.json · TRACK_F_PRODUCTION.md (SHEET READY)
reference/     aphorisms-of-siva (GITIGNORED — never commit, copyright) ·
               gretil_sivasutra.json (vendored exact-Sanskrit forms)
audio/         mp3s (GITIGNORED — local only)     text/  stamped transcripts (14 + 79 lak)
transcripts/   raw VTTs (11) + lak segment JSONs   cf/  CF-whisper JSON (2)
tools/         verifiers & pipelines (qa_std · build_b1b · b_match · builders · linters)
MANIFEST.json  14/14 sessions with transcript sources
FILEMAP.md     path inventory: what each file is + why (keep current)
TODO.md        10-action queue for the next agent
```

## Repro
```bash
python3 tools/verify_units.py      # 307/0
python3 tools/validate_questions.py  # 7/7 (6 spine + alternate)
python3 tools/s2_cluster.py --apply  # segmentation, totals reconcile (see SPINE_ASSIGN)
python3 tools/plain_filter.py --check  # hash MATCH
```

## What's next (owner-visible order)
Two compilations — **Standard chant** (77 sūtras, verse order, layered 0/A/B/C)
built and verifiable, **Custom spine edit** text-complete and frozen.
Never blended (see `BUILD_ENGINE.md`).
1. **Standard C layer** — stories + guests + Sharma coda per verse, then full
   assembly → R2 → owner ears (ears are the ONLY lock).
2. **Custom at lock** — HOLDUP + UNFOLDING re-run vs LOCKED cells; essay-corpus
   export; print-verify settles cards.
3. **Owner calls** (batched, one message): essay-0 ear/lock · key sign-off ·
   coverage-standard (§8e-1) · question ratification · B1b naturalness.
