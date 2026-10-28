# FILEMAP — where everything is and WHY (single source of truth for paths)

If you don't know what a file is, look here before opening it. Update this file the
day you add anything that a fresh agent would need. (Companion: `TODO.md` = the
10-action queue; `HANDOVER-STANDARD-2026-10-27.md` = the current-work doc; `NEXT.md` =
the long-form queue with context.)

## ROOT — the law & state documents (read in this order)

| file | what | why it exists |
|---|---|---|
| `README.md` | front door: state snapshot, read-order, repro commands, repo map | first 5 minutes |
| `READ-THIS-FIRST.md` | the 2026-10-28 failure log, written to be unmissable: wrong track, chant law, no unlistened masters, tool lies | read BEFORE AGENTS.md — it outranks everything for orientation |
| `HANDOVER-2026-10-28.md` | the Custom-audio day: what broke, what's verified, links (v4), Standard queue | current-state screen for whoever picks this up |
| `HANDOVER-2026-10-25.md` | the pass-1 day + structure-pass narrative, gotchas, M19–M21 | how Custom got text-complete, which errors repeat |
| `HANDOVER-2026-10-26.md` | ears + voice-build day (Qwen, Fish, anti-echo, silence bug M25) | voice/tooling decisions with causes |
| `HANDOVER-STANDARD-2026-10-27.md` | Standard B-rollout method + open queue | the current frontier doc |
| `TODO.md` | **10 actions for the next agent** | the executable subset of NEXT |
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
| `process/STANDARD.md` | Standard build manual (self-contained: inputs → locate → curate → build → QA → assemble → ship) | the Standard law; conflicts resolve here first |
| `process/STANDARD-PORTING.md` | text-independent engine + per-text config (worked Yoga Sūtras port) | start new texts here |
| `process/10-FORMAL-CHANT.md` | Standard Compilation method: tagging, spacing, what it never does | build the chant storyboard per corpus |
| `standard/TRACK_F_STORYBOARD.md` | 77 verse rows (S1-19 filled 2026-10-26): B1 chant window + B2 readout + B3 slot + B4 slot | Standard Compilation assembly source (separate from custom manifests by law) |
| `NEXT.md` | full queue with context/threads (superset of TODO) | what & why, longer horizon |
| `PROCESS_NOTES.md` | §0–8m session history + pass-1-complete block + BUILD ORDER LAW + FROM SCRATCH | the project's memory — state claims live here |
| `MISTAKES.md` | M1–M38: mistake → cause → rule | **read BEFORE touching tools**; each rule is load-bearing |
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

## `standard/` — the chant compilation (verse order, fidelity object)

| file | what | why |
|---|---|---|
| `manifests/std_*.json` (77) | Standard per-verse manifests (0/A/B/C, `b1_status` enum) | the cut lists — manifests are code; `qa_std.py` pre-commit |
| `template_77.json` | verse map: book bodies + translations + GRETIL exact + numbering traps | A-selection guide + B1b speech source + B-hook anchor |
| `TRACK_F_STORYBOARD.md` | 77 verse rows: B1 chant window + B2 readout + B3 slot + B4 slot | Standard assembly source (separate from custom manifests by law) |
| `QA_SWEEP_*.json` | structural sweep reports (FAIL/FLAG per verse) | evidence of verification, not verdicts |
| `BOOK_COVERAGE_2026-10-28.md` + `BOOK_COVERAGE_VERDICTS.md` + `BOOK_GAPS_PROPOSAL.tsv` | book-vs-Standard audit: 428 machine proposals, all 77 hand-verdict | the voiced-gold work queue (owner doctrine §8n) |

## `custom/` — the spine remix (selection + argument, never blended with Standard)

| file | what | why |
|---|---|---|
| `essay0/ESSAY0_OUTPUT.md` | **the seed**: HEAD + six four-layer cells (S→T→plain→Bäumer), enquiry chain | essay-0 = the bīja everything expands from; DRAFT until `essay0_lock` flips |
| `essay0/essay0_lock.json` | lock machine-state | flip only on owner ear (then run TODO #6/#7) |
| `essay0/ESSAY0_FLOW_READ.md` | spoken pass of the seed/chain | read-aloud verification before any build |
| `essay0/key_ss1_proposal.json`, `essay0/plain_essay0.json`, `essay0/loanwords_ss1.json`, `essay0/t_essay0.txt` | key/plain pipeline states (PROPOSAL) + transcript-side input | plain rows are mechanical filter-output — regenerate+rehash at key sign-off, **never hand-edit** |
| `manifests/manifest_s{1..6}_{A,B,C}.json` | 18 manifests: ordered clips w/ quote-located t_in/t_out, card+question | the cut lists for every layer — built by `tools/build_manifests.py` |
| `SECTION_ARGUMENTS.md` | Essay A as text — 71 clips in order per section + flow verdicts | the A-collate draft; *missing the 10 newer A's (audit noted)* |
| `JOIN_AUDIT.md` | 65 clip-joins verdicted (55/9/0) | proof the arguments flow, not random statements |
| `UNFOLDING_AUDIT.md` | 81 A judged vs seeds (62E/11Q/5B/3W/**0N**) | proof no A swaps the seed; watch-list = ss4-02, ss8-06/07, ss10-03, S5-guru, ss7-16 |
| `HOLDUP_SHEET.md` | 219 B-rows, **RUN-1 verdicts written** (83 KEEP/134 DEMOTE/1 LEDGER/1 PROMOTED) | the B-membership sweep — run-1 done 2026-10-26 against DRAFT; re-run at lock |
| `B_SWEEP.md` + `holdup_verdicts.json` | sweep log (keep-reasons, budgets, defects M22/M23) + machine verdicts | what played at B and why — regenerate sheet from units, verdicts = single source |
| `C_WALK.md` | the C layer as a doc (300 clips, her order) | readable texture walk; manifest_sc_C.json = machine source |
| `BEATS.md` | run-order, opener grammar, bell spec, assembly pipeline, runtimes | THE build instrument for audio (v1) |
| `SPEAKERS.md` | voice map (archive vs human vs TTS) + v1 placeholder rulings | who speaks what |
| `EAR_CHECK.md` | 32 ASR suspects (uid+window+expected) | verify at audio QA; `naruto` sits in an A-quote |
| `LA_PRODUCTION.md` | Essay-A production sheet (measured timecodes, asserts sheet==master) | SHEET READY; validate with BOTH cut dirs (l0 symlinks live in `custom_a_cuts/`) |
| `TRACK_F_PRODUCTION.md` | essence production sheet (measured timecodes, asserts sheet==master) | SHEET READY 2026-10-28; the sheet is the product (essence = Custom-side seeds) |
| `LISTEN_audit_essence_v1.json` + `FLOW_REVIEW_essence_v1.md` | machine audit + recorded flow verdicts | evidence, not verdicts |
| `VISUAL_ENGINE_SPEC.md` | left-2/3 timeline (verse/quote/diagram/question) + right-1/3 ambient deity loop + build recipe | the video spec (v1 prototypes rendered, templates/diagrams open) |

Shared inputs both compilations pull (paths frozen — never move without re-running every gate, M43): `text/` · `transcripts/` · `cf/` · `audio/` (sources + `gen/std/` + `gen/custom/` + shared `gen/tts/` + `gen/sfx/`) · `reference/` · `excavations/` · `tools/` · `process/` (law above both).

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
| `make_essence.py` | essence build + production sheet from measured cuts (single source; asserts sheet==master) | Custom-side seeds + `custom/TRACK_F_PRODUCTION.md` |
| `make_custom_a.py` | Essay-A master (essay-0 cells + section openers + 76 A clips; asserts sheet==master) | Custom LA + `custom/LA_PRODUCTION.md` (SHEET READY) |
| `validate_sheet.py` | validates ANY production sheet (standard or custom): files exist, durations match, timecodes accumulate, total matches, audit+FX sections present | the sheet is the product — run before any render talk |
| `flow_lint.py` | deterministic flow checks (runs, joints, longs, repetition, deictic slots, pause inventory) | machine half of peer review — ears decide, never the linter |
| `validate_sheet.py` | validates ANY production sheet | the sheet is the product — run before any render talk |
| `recut_sentence.py` | sentence-complete + silence-snapped re-cut of A windows (expansion-only, containment asserts) | run after ANY manifest touch, before rebuild (M39) |
| `align_cuts.py` | whisper word-timestamp re-edger — DO NOT RUN (non-convergent v1 kept for history, M41/M42) | superseded by recut_sentence's whisper-anchored edges |
| `listen.py` | Qwen omni ears (qa/critic/joints/deictic/verify/audit/surgery/chantcheck modes) | model QA per LISTENING.md — findings need corroboration |
| `tts_scan.py` | no raw Sanskrit through TTS (stoplist + spoken-form map) | run after any TTS line/key change |
| `deictic_check.py` | antecedent surfacing from transcript text | FLOW_REVIEW Q4 evidence, per cut |
| `visual_prototype_v0.py` | static split-screen prototype (S1-1 card left + 01-stages right, 1920×1080) | layout-lock reference (R2 `journey/shiva-s1-1-v0.mp4`) |
| `visual_prototype_v1.py` | switching-left (verse→quote→four-levels diagram) + ambient-right loop prototype | promote into visual_left/right at template lock (R2 `journey/shiva-v1-timeline.mp4`) |
| `s2_cluster.py` | section assignment + verdicts (REPORT ONLY post-pass-1) | historical (48+ overrides logged); new rows are manual now |
| `cf_transcribe.py`, `vtt2txt.py` | CF whisper + VTT→stamped-text | transcript acquisition (PID-unique temp, 600s chunks) |
| `qa_std.py` | structural sweep for Standard manifests (F1 file-map … F6 schema) | pre-commit on any manifest touch (M37); zero FAIL gate |
| `build_b1b.py` | Fish TTS of Dyczkowski translations verbatim (marks-stripped speech, Sanskrit audit, loan gate) | the B1b line; asserts no deferrals |
| `b_match.py` | Baumer candidate ranker per verse (anchors on `book_sanskrit`, M35) | metric proposes, human verdicts |
| `build_standard_verse.py` | manifest → cut → assemble → sheet per verse (asserts `b1_status` enum, M36) | the Standard builder; span-hashed cuts |
| `assemble_standard.py` | ordered concat of per-verse proofs (+ coda on C walks, master==sum assert) | pilot + full walks; pilots labeled `pilot_` |
| `build_template.py`, `fix_template_l3.py`, `template_v2.py` | template builders (Academy keying → L3 fix → GRETIL exact forms) | writers of `template_77.json`; v2 asserts 77/77 exact |
| `count_a.py` | 0/A presence per verse (77/77 with 0+A) | Standard completeness gate |
| `cov_check.py` | book-vs-audio term coverage per verse (flags GAPs for verdict) | B-hook audit, not truth |
| `tts_line.py` | Fish TTS + TTS_SAY spoken forms + -21dB norm | single voice path; isolated-probe discipline |
| `xverse_scan.py` | cross-verse keyword scout (header-stopped, slug-fixed M32) | hints only; human verdicts, no moves |
| `locate_b1.py`, `word_onset.py`, `onset_batch*.py` | B1 locate + word-level onset snapping | M27/M30: segments are not onsets |
| `lak_transcribe.py` | local faster-whisper base → stamped txt + segment JSONs | Standard transcript acquisition (idempotent) |
| `dump_maps.py`, `parse_contents.py`, `template_v2.py`, `write_zeros.py`, `xcheck.py` | one-shot maps/probes (history) | kept as evidence; not in the build path |
| `retranscribe_fix.py` | one-shot lang=en re-pass for garbled lak heads | FROZEN with the transcribe layer (owner §8n) — do not run; kept as evidence |

Reorg note (2026-10-28): `build/` is gone — split into `standard/` + `custom/` (essay-0 lives in
`custom/essay0/`, manifests in per-track `manifests/`, `audio/gen/` split into `std/` +
`custom/` with shared `tts/` + `sfx/`). Shared primary (`text/`, `transcripts/`, `audio/`
sources, `reference/`, `excavations/`, `tools/`) keeps frozen paths per M43. Handovers +
MISTAKES history intentionally still cite `build/` — they describe the past.

## DATA (mostly gitignored on purpose)

| path | what | why / rule |
|---|---|---|
| `text/*.txt` (14) | stamped transcripts (the source-of-truth for quotes) | committed; all unit windows reference these stamps |
| `text/lak_*.txt` (79) | Lakshmanjoo stamped transcripts (verse files + intros/conclusion) | committed 2026-10-26; Standard locate inputs + `lak` coverage scope |
| `transcripts/` | raw VTTs (22 = 11×orig+compacted) + `lak_*.segments.json` (79 float-timestamp sidecars) | provenance for regenerating text/; segments drive word-level locate |
| `cf/` | CF-whisper JSON+logs (2 sessions) | cf_transcribe outputs |
| `audio/` (14 mp3 = ALL Baumer+dl1, + `gen/` `cuts/` build-out) | local mp3s + generated audio | **GITIGNORED — never commit audio**; 2026-10-26: 11 pulled, corpus complete; `chant/` + `third/` hold non-Baumer voices, inventoried in `audio/SOURCES.md`; `gen/std/` proofs + `gen/tts/b1b_*` translation lines regenerable; `gen/custom/` holds LA/essence masters + cuts (`l0_cuts/` shared opener stacks; `custom_a_cuts/` carries 47 symlinks into `l0_cuts/` for single-dir sheet validation — M43) |
| `reference/aphorisms-of-siva-dyczkowski_clean.txt` | held Sanskrit/translation source for cards | **GITIGNORED — copyright; held line-refs (l.735 etc.) are the only things quoted** |
| `reference/gretil_sivasutra.json` | vendored GRETIL Kaul exact-Sanskrit forms (75 + 2 Ksa-only) | committed (ancient text, no rights issue); feeds `sanskrit_exact` |

## House rules that keep this map true

1. New artifact? Add it here the same day, with its **why**.
2. Note → `C-MARKS.md` + ledger, **never a unit** (M21). Quote → unit file only.
3. Counts change → `tools/sync_counts.py` (it owns the number lines).
4. Doc edit via script → `assert count == 1` (M17). Unit touched → `verify_units` (expect 307/0). Manifest touched → `qa_std.py` zero FAIL (M37).
5. Superseded files stay, labeled at their top (`SPINE_PREVIEW` pattern) — history is evidence.
