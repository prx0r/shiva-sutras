# FILEMAP — where everything is and WHY (single source of truth for paths)

If you don't know what a file is, look here before opening it. Update this file the
day you add anything that a fresh agent would need. (Companion: `TODO.md` = the
20-action queue; `HANDOVER-2026-10-25.md` = the last day's narrative; `NEXT.md` =
the long-form queue with context.)

## ROOT — the law & state documents (read in this order)

| file | what | why it exists |
|---|---|---|
| `README.md` | front door: state snapshot, read-order, repro commands, repo map | first 5 minutes |
| `HANDOVER-2026-10-25.md` | the pass-1 day + structure-pass narrative, gotchas, M19–M21 | how we got to today, which errors repeat |
| `TODO.md` | **20 numbered actions for the next agent** | the executable subset of NEXT |
| `BUILD_ENGINE.md` | front door: two-track law + decode method → `process/` | how to run/validate/port — read before starting new work |

## `process/` — the objective engine (same apparatus shape as analayo-nibbana/process)

| file | what | why it exists |
|---|---|---|
| `process/README.md` | pipeline 00–09, compilation map, guarantees | the 5-minute orientation |
| `process/AXIOMS.md` | 12 binding rules | violations fail the build |
| `process/00-INPUTS.md` … `09-RENDER.md` | one doc per stage: inputs, method, gate | execute the stage, pass the gate |
| `process/SKILLS.md` | reusable techniques (locate, dual-norm, hold-up, flow-read, ear-harvest, count-sync, chunked transcribe) | port these, not vibes |
| `process/REPRODUCE.md` | exact rerun order + what stays human (✎) | byte-identical rebuilds |
| `process/FILES.md` | process artifact map (produced-by → consumed-by) | trace any file to its stage |
| `process/verify.sh` | one-command audit (units, G0, plain, totals, ledger, presence) | run before every commit touching outputs |
| `process/10-FORMAL-CHANT.md` | Standard Compilation method: tagging, spacing, what it never does | build the chant storyboard per corpus |
| `build/TRACK_F_STORYBOARD.md` | 76 verse rows (S1-19 flagged missing): B1 chant window + B2 readout + B3 slot + B4 slot | Standard Compilation assembly source (separate from custom manifests by law) |
| `NEXT.md` | full queue with context/threads (superset of TODO) | what & why, longer horizon |
| `PROCESS_NOTES.md` | §0–8h session history + pass-1-complete block + BUILD ORDER LAW | the project's memory — state claims live here |
| `MISTAKES.md` | M1–M21: mistake → cause → rule | **read BEFORE touching tools**; each rule is load-bearing (assert-count, contiguous quotes, C-semantics…) |
| `MANIFEST.json` | 14 YouTube ids + transcript status per session | provenance of `text/` — regenerating anything starts here |

## `excavations/` — the mined corpus (one file per source, append-only)

| file | what | why |
|---|---|---|
| `ss1..ss13.md`, `dl1.md` | **307 units** — uid/timestamp/quote/context/essay_use, graded A/B/C | the only place quotes live verbatim; grades = innermost essay-layer each clip enters (FORMULA) |
| `SPINE.md` | the 6 section-questions + gospel law + sūtra-ranges + fit-check | sections ARE questions; fit-check = A↔question measured evidence |
| `SPINE_ASSIGN.tsv` | uid → (grade, section, score, margin, fallback) | machine membership; `fallback=pass1-manual` marks the 124 provisional pass-1 rows |
| `_SCHEMA.md` | required unit fields | ported from vatula←analayo — breaks here break `verify_units` |
| `CATALOGUE.md` | topics → uids, A-density ranked | clustering/reshuffle layer |
| `COVERAGE.md` | coverage truth + pass-1 results + inclusion channels | answers "how much of Baumer are we using" |
| `COVERAGE_LEDGER.tsv` | **678 rows**: every gap span → disposition (promote / C-reason / covered / demoted) | the C-disposition substrate + audit trail; every pass-1 uid has a row (assert this after edits) |
| `C-MARKS.md` | why spans are NOT units, per file | the notes-layer (notes live HERE, never as units — M21) |
| `ESSAY0.md` | the essay-0 pick record (7-step run, sharpened-question audit) | why the question/seed is what it is |
| `SPINE_PREVIEW.md` | superseded S2 design record | kept deliberately as history — never edit, never cite as current |

## `build/` — outputs toward the essay (docs + machine-state)

| file | what | why |
|---|---|---|
| `ESSAY0_OUTPUT.md` | **the seed**: HEAD + six four-layer cells (S→T→plain→Bäumer), enquiry chain | essay-0 = the bīja everything expands from; DRAFT until `essay0_lock` flips |
| `essay0_lock.json` | lock machine-state | flip only on owner ear (then run TODO #6/#7) |
| `ESSAY0_FLOW_READ.md` | spoken pass of the seed/chain | read-aloud verification before any build |
| `SECTION_ARGUMENTS.md` | Essay A as text — 71 clips in order per section + flow verdicts | the A-collate draft; *missing the 10 newer A's (audit noted)* |
| `JOIN_AUDIT.md` | 65 clip-joins verdicted (55/9/0) | proof the arguments flow, not random statements |
| `UNFOLDING_AUDIT.md` | 81 A judged vs seeds (62E/11Q/5B/3W/**0N**) | proof no A swaps the seed; watch-list = ss4-02, ss8-06/07, ss10-03, S5-guru, ss7-16 |
| `HOLDUP_SHEET.md` | 219 B-rows, **RUN-1 verdicts written** (83 KEEP/134 DEMOTE/1 LEDGER/1 PROMOTED) | the B-membership sweep — run-1 done 2026-10-26 against DRAFT; re-run at lock |
| `B_SWEEP.md` + `holdup_verdicts.json` | sweep log (keep-reasons, budgets, defects M22/M23) + machine verdicts | what played at B and why — regenerate sheet from units, verdicts = single source |
| `manifest_s{1..6}_{A,B,C}.json` | 18 manifests: ordered clips w/ quote-located t_in/t_out, card+question | the cut lists for every layer — built by `tools/build_manifests.py` |
| `C_WALK.md` | the C layer as a doc (300 clips, her order) | readable texture walk; manifest_sc_C.json = machine source |
| `BEATS.md` | run-order, opener grammar, bell spec, assembly pipeline, runtimes | THE build instrument for audio (v1) |
| `SPEAKERS.md` | voice map (archive vs human vs TTS) + v1 placeholder rulings | who speaks what |
| `EAR_CHECK.md` | 32 ASR suspects (uid+window+expected) | verify at audio QA; `naruto` sits in an A-quote |
| `key_ss1_proposal.json`, `plain_essay0.json`, `loanwords_ss1.json`, `t_essay0.txt` | key/plain pipeline states (PROPOSAL) | plain rows are mechanical filter-output — regenerate+rehash at key sign-off, **never hand-edit** |
| `t_essay0.txt` | transcript-side text of essay-0 | input to filters |

## `tools/` — verifiers & pipelines (each gate has one)

| tool | what | why |
|---|---|---|
| `verify_units.py` | every unit quote ⊂ its transcript (substring, stamps near) | **the gate** — run after any unit/quote touch (expect 308/0) |
| `validate_questions.py` | G0: interrogative, ≤9 words, content-noun, no pronouns | spine-question gate (7/7) |
| `plain_filter.py --check` | plain rows hashed vs key | gospel plain-layer integrity |
| `coverage_measure.py` | span/line/word + per-section anchor coverage | "how much are we using" as a number |
| `gap_report.py` | uncovered spans per session (SESS map — handles dl1) | the pass's work-queue generator |
| `sync_counts.py` | recomputes counts → rewrites every doc line that states them | run after ANY unit add/demote; **its NEXT-state template was fixed 2026-10-25 — don't regress it** |
| `build_manifests.py` | A/B/C manifests: quote→line-run→word-rate cut stamps, SA-order | the cut lists (re-run after any grade/order change) |
| `make_l0.py` | SUPERSEDED by make_essence (history) | do not build from this |
| `make_essence.py` | essence build + production sheet from measured cuts (single source; asserts sheet==master) | standard-compilation essence + `TRACK_F_PRODUCTION.md` |
| `validate_sheet.py` | validates ANY production sheet (standard or custom): files exist, durations match, timecodes accumulate, total matches, audit+FX sections present | the sheet is the product — run before any render talk |
| `flow_lint.py` | deterministic flow checks (runs, joints, longs, repetition, deictic slots, pause inventory) | machine half of peer review — ears decide, never the linter |
| `s2_cluster.py` | section assignment + verdicts (REPORT ONLY post-pass-1) | historical (48+ overrides logged); new rows are manual now |
| `cf_transcribe.py`, `vtt2txt.py` | CF whisper + VTT→stamped-text | transcript acquisition (PID-unique temp, 600s chunks) |

## DATA (mostly gitignored on purpose)

| path | what | why / rule |
|---|---|---|
| `text/*.txt` (14) | stamped transcripts (the source-of-truth for quotes) | committed; all unit windows reference these stamps |
| `transcripts/` | raw VTTs (22 = 11×orig+compacted) | provenance for regenerating text/ |
| `cf/` | CF-whisper JSON+logs (2 sessions) | cf_transcribe outputs |
| `audio/` (14 mp3 = ALL Baumer+dl1, + `gen/` `cuts/` build-out) | local mp3s + generated audio | **GITIGNORED — never commit audio**; 2026-10-26: 11 pulled, corpus complete; `chant/` + `third/` hold non-Baumer voices, inventoried in `audio/SOURCES.md` |
| `reference/aphorisms-of-siva-dyczkowski_clean.txt` | held Sanskrit/translation source for cards | **GITIGNORED — copyright; held line-refs (l.735 etc.) are the only things quoted** |

## House rules that keep this map true

1. New artifact? Add it here the same day, with its **why**.
2. Note → `C-MARKS.md` + ledger, **never a unit** (M21). Quote → unit file only.
3. Counts change → `tools/sync_counts.py` (it owns the number lines).
4. Doc edit via script → `assert count == 1` (M17). Unit touched → `verify_units` (expect 308/0).
5. Superseded files stay, labeled at their top (`SPINE_PREVIEW` pattern) — history is evidence.
