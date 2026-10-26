# FILES — process artifact map (repo-wide paths: `FILEMAP.md`).

| artifact | stage | produced by | consumed by |
|---|---|---|---|
| `excavations/ss*.md`, `dl1.md` | 01 | hand ✎ (schema `_SCHEMA.md`) | verify, coverage, cluster, manifests |
| `text/*.txt` (14), `MANIFEST.json` | 00 | `vtt2txt.py`, `cf_transcribe.py` | verify (source of truth for quotes) |
| `transcripts/`, `cf/` | 00 | pulls | `text/` provenance |
| `excavations/COVERAGE_LEDGER.tsv` | 02 | hand ✎ (asserted) | C-assembly, holes |
| `excavations/C-MARKS.md`, `COVERAGE.md` | 02 | hand ✎ + `coverage_measure.py` | 02 gate |
| `excavations/CATALOGUE.md` | 03 | hand ✎ (measured) | SPINE |
| `excavations/SPINE.md`, `SPINE_ASSIGN.tsv` | 03 | `s2_cluster.py` (report) + hand ✎ | essay-0, manifests |
| `excavations/ESSAY0.md` | 04 | hand ✎ (7-step run) | ESSAY0_OUTPUT (history) |
| `build/ESSAY0_OUTPUT.md`, `essay0_lock.json`, `t_essay0.txt`, `key_*.json`, `plain_essay0.json`, `loanwords_*.json` | 04 | hand ✎ + `plain_filter.py` | flow-read, beats, render |
| `build/ESSAY0_FLOW_READ.md` | 04 | hand ✎ (read aloud) | ear session |
| `build/SECTION_ARGUMENTS.md`, `JOIN_AUDIT.md` | 05 | hand ✎ (verified) | unfolding, manifests, beats |
| `build/UNFOLDING_AUDIT.md` | 06 | hand ✎ | collate, ear session |
| `build/HOLDUP_SHEET.md`, `B_SWEEP.md`, `holdup_verdicts.json` | 06 | sweep ✎ + units | manifests (B set) |
| `build/manifest_s{1..6}_{A,B,C}.json`, `C_WALK.md` | 07 | `build_manifests.py` | beats, render |
| `build/BEATS.md`, `SPEAKERS.md`, `EAR_CHECK.md` | 08 | hand ✎ | render |
| `audio/gen/`, `audio/cuts/` | 09 | `make_l0.py` / `make_audio.py` | masters (gitignored) |
| `build/TRACK_F_PRODUCTION.md` | 07/09 | `make_essence.py` (measured timecodes, asserts sheet==master) | essence assembly + ear session |
| `audio/SOURCES.md` | 00 | hand ✎ | voice rights/jobs |
| `process/verify.sh` | gates | runs the gates | every commit touching outputs |
| `tools/tts_scan.py` | no raw Sanskrit through TTS (stoplist + TTS_SAY) | after any TTS line/key change |
| `tools/deictic_check.py` | antecedent surfacing from transcript text | FLOW_REVIEW Q4 evidence, per cut |
| `tools/flow_lint.py` | machine half of flow review (runs, joints, longs, repetition, slots, pauses) | deterministic pre-ear check | every sheet, every re-cut |
| `process/FLOW_REVIEW.md` | 10-question evidence protocol | repeatable human pass | after validate_sheet, before ears |
| `build/FLOW_REVIEW_<cut>.md` | recorded findings (verdict + evidence) | the review artifact | filed per review |
| `process/ROLES.md` | roles abstract + shiva casting | casting, handover law, recast rule | beats, sheets, render |

Audio (`audio/*.mp3`, `audio/chant/`, `audio/third/`) is local-only,
gitignored, inventoried — never committed (M13).
