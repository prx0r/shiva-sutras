# Śiva Sūtras — Baumer course (13 sessions) — process notes (living doc, 2026-10-25)

Endgame per owner: primary-text-first works. Method = analayo 33-sermons pipeline
(00 inputs → 01 transcribe/cut → 02 segment → 03 gold/core → 04 three-layer → render last,
verify at every gate) + vatulanatha ports (units-as-pool, measured questions,
BUILD ORDER LAW: essay 0 first, B = built x1.6–2 not superset) + tantraessays tagging
(direct/root/method/work/agn). AXIOMS hold: verbatim extracted never typed; grades
load-bearing; seams standalone; thin is honest; every fix logged here.

## 0. Inputs
- Audio/teacher: Bäumer Śiva Sūtras intensive, R2 `longform-audio/bettina-baumer-shiva-sutras/`
  (13 mp3s ~1.4GB) + `transcripts/` VTTs for 11 of 13.
- Pulled here: 11× VTT (6MB) → cleaned to `text/*.txt` (71,207 words, overlap-merge dedupe
  of YT rolling captions); 2 missing mp3s (Day2-S1 91MB, Day6-S1 150MB) pulled from R2;
  CF whisper-large-v3-turbo transcribed both (KSpk4 991 segs/57.6m; r5w 2222 segs/92.4m).
- Text held: Dyczkowski Aphorisms of Śiva + [V] SS 1.1/2.1/3.1 (tantraessays primary/texts);
  Kṣemarāja vārttika per vatulanatha INVENTORY (not yet on disk here).
- Mapping: ss1=Day1-introI … ss13=Day6-II (ss4=Day2-S1 [CF], ss12=Day6-S1 [CF]).

## 1. Grading pass (the whole corpus, first)
- 13/13 sessions read end-to-end (Days 1–6; ~100k words incl. CF transcripts).
- 180 excavation units, all quote-verified (`tools/verify_units.py`: normalize both sides,
  punctuation-stripped, [Music]-tolerant, start-stamp within 120s): **180 units, 0 fail**.
- Grade pyramid after tightening pass (87 A → 68 A; 104 B; 8 C):
  A = sharpest formulation per idea (duplicates demoted even when good);
  killers (~30) selected at clustering, not here.
- MISTAKES (logged, fixed):
  1. YT rolling-cue dupes ("X" / "X B" / "B" triples) — fixed with overlap-merge
     (extend-on-prefix, skip-on-contained); 85k → 71k words.
  2. CF temp collision: two jobs shared /tmp/opencode/cfseg_ss.mp3 → second crashed;
     fixed with PID-unique temp names; earlier crashed run left no partials (whole rerun).
  3. Verifier bugs (mine, 3x): norm dropped punctuation only on one side → 60 false fails;
     fixed by stripping punctuation + [Music] tokens both sides (note: dyczkowski's rule
     was whitespace-only because their srt had punctuation; YT/CF text needs the harder norm).
  4. Quoted-from-memory: 14 units failed because I wrote remembered phrasing (incl. dupes
     of other sessions' material: ss7-12/13 duplicated ss6, ss8-08 belonged to ss7,
     ss10-02 belonged to ss5). All rebuilt from grep-verified spans or deleted.
     RULE GOING FORWARD: never write a quote I haven't just re-read in the file;
     the verifier catches it, but prevention beats correction.
  5. Duplicate uid ss7-16 (two units) → renumbered second to ss7-17.
  6. `verify_units.py` lost its parse loop in an edit (0 units checked, exit 0 — silent pass
     is worse than a loud fail); loop restored; always eyeball the units count.

## 2. Convergence (measured, not assigned)
- Keyword spread (13 files): consciousness 13/13 · practice 13/13 · śakti 13/13 ·
  senses 13/13 · mind-mantra 12/13 (Day5-II spike = 2.1) · self-nature 12/13 ·
  realization 12/13 · freedom 7/13 (DIES after Day 4) · guru-grace 8/13 (patchy) ·
  recognition 4/13 (WRONG CORPUS — that's PH) · devotion 6/13 · heart 7/13 · kula 2/13.
- A-density: praxis 31 · doctrine 22 · mantra 16 · consciousness 11 · ritual 8 · …
  Both dissections agree: the course is consciousness-as-practiced-through-mantra/mind.
- KILLED as running questions: freedom (vanishes), recognition (PH's), grace (patchy).
- Essay-0 candidate: **"What is consciousness — and what does the mind have to do with it?"**
  Framing question it answers: "If everything is already consciousness, why aren't we
  liberated?" (the commentary's own engine: ss4-11, ss6-01, ss12-03/14).
- Details in `excavations/CATALOGUE.md` (topics→A-uids, per-session notes, pull-list).

## 3. Gaps / pull-list (from tagging needs)
- Netra Tantra (easy, high-level; Kṣemarāja leans on it in ss12–13) — pull text.
- Lakshmanjoo ŚS book (quoted throughout; pp.146-147 editor misattribution noted in-session:
  Netra quotes filed under Lakṣmīkaulārṇava — verify against print).
- Tantrasadbhava (khecari-mudrā source, unpublished — note as gap, don't invent).
- Parātrīśikā-vivaraṇa sessions (Baumer's other course, referenced in 2.1/mudrā units) — spoken-held in vatulanatha.
- Jaideva Singh (course text) + Dyczkowski Aphorisms (Bhāskara trans; [V] banked) — held.
- Kula-chūḍāmaṇi verse, Candrajñāna verse, Mālinīvijaya mantra-virya verse, Ambāstavī lines —
  locus-check against editions before any print use (flagged in units).

## 4. Repro
```bash
python3 tools/vtt2txt.py        # 11 YT VTT -> text/ (rerun-safe)
python3 tools/cf_transcribe.py audio/X.mp3 cf/X.json   # Cloudflare whisper-large-v3-turbo, 600s chunks
python3 tools/verify_units.py   # 180 units, 0 fail
grep -h "^### .*\[A\]" excavations/ss*.md | wc -l   # 68
```

## 5. Next (ordered)
1. Commit (local git; no remote assigned — tantraessays = Dyczkowski, vatulanatha = Baumer-series queue; decide home later).
2. Essay-0 build from CATALOGUE A-pool (question → pause → plain → her clip; Sanskrit-first card rule from vatulanatha §9b).
3. śākta/mantra deep-file (ss10–ss13 B-units hold the technical mantras deferred in-session).
4. Gateless-gate check: does any unit need the missing Day-6-I CF audio re-listen (ear-check flagged ASR spots: "rishikesh"=paratrishika-people, "Mitta City"=siddhi, "Dantoraja"=Tantrāloka)?

## 3. Essay-0 pick (ESSAY0-FORMULA run, 2026-10-25 evening)

Pulled vatulanatha's latest (`ESSAY0-FORMULA.md` 7 tests + UNFOLDING law + G0 gate
`validate_questions.py` + Step 5b flow test) and ran it on this corpus.

- G0 gate ported (`tools/validate_questions.py`, anchor = consciousness/self = 1.1's
  topic): 5/7 pass. The two generic drifts FAIL exactly as designed — including their
  own reject-case "What happens to the senses?" (no anchor).
- Master stays: "What is consciousness?" (clear, S1's word — their "clear, not verbose" rule).
- Sharpened pick: **"Why isn't consciousness something you do?"** (6 words; presupposes
  the course's doing/being distinction; thread present Days 1–6; opens "then what DO
  you do?" → mind → bondage → mantra → guru).
- Full stack in `excavations/ESSAY0.md`: S caitanyam ātmā → T1 her gloss (exact span,
  rolling-dup collapsed, print commas noted) + T2 Dyczkowski alternate → P mechanical
  (filter port + proposal key, hash 761da269094f96bb) → A ss3-10 [01:20:12]→[01:20:30]
  (18s, 100% in A-gold, completes the question).
- Lock = DRAFT (`build/essay0_lock.json`): no audio rendered, owner ear pending.
- Flow test passes: response seeds 0→A (sides) →B (mechanics) →C (source lines)
  without swapping the seed — the essay performs unfoldment (their UNFOLDING law).
- Alternates kept per their practice (A2 beyond-thought, A3 think-your-way, A1 master).
- Borrowed rules now local: BUILD ORDER (essay-0 first, B = built x1.6–2, no supersets
  ship); Sanskrit-first cards (source language on screen, English gloss beneath);
  beat grammar question→pause→plain→clip; human voice owns questions.

## 6. S2/S3 correction (2026-10-25) — the missed step, then done properly

Owner caught it: I ran essay-0 BEFORE segmentation. Analayo 02 ("every span gets
exactly one home") and vatula 17 (clustering → convergence → SPINE → then essay-0)
both put the partition first. A CATALOGUE of tags is not a partition; without
sections there is no enquiry to open, no A⊂B⊂C to collate under, and the essay-0
flow test had nothing real to seed.

**What was done (in order):**
1. Re-read the full process chain (analayo 00-08 + MISTAKES/SKILLS; vatula 12/17;
   their S2 attempt-log: blind agglomerative = blobs/dust — profiles-first is the method).
2. Preview spine: 6 sections as questions, from the sūtra arc + measured threads
   (SPINE_PREVIEW.md).
3. `tools/s2_cluster.py` — designed keyword profiles per section; scored every unit's
   ±5min transcript window + own quote; ties/zeroes/thin (margin≤2, score<12) → session
   primary; **48 content-verdict overrides** (human reading beats metric — their M6:
   "metric flags candidates, reading gives verdicts"). Glue-terms killed en route
   (tradition/means/word/will/body/sense/mantra-bare at pan-corpus counts = the
   vatula "nonduality glues → one blob" failure, caught early this time).
4. Totals reconcile: 180/180 units, one home each (`SPINE_ASSIGN.tsv`).
5. Convergence: unit distribution and independent A-buckets both rank S1 first,
   S5 second, S3 thinnest — two dissections, one elephant; mid-table S2/S4/S6
   disagreement logged as cosmetic.
6. Six section questions + essay-0 question: **7/7 G0 PASS**.
7. Essay-0 flow re-tested against the REAL sections (seed: consciousness-is-not-doing →
   S1 name → S2 hide → S3 unforceable → S4 does → S5 mind-engages → S6 free-to-do) — passes.
8. `excavations/SPINE.md` written: anchors are her words (not ours), journeys per
   cluster with her sūtra order inside, C-homes listed, build rules restated.

**Also fixed:** duplicate uid (bliss unit was second ss7-17 → ss7-19).
**State now:** grading ✓ · catalogue ✓ · segmentation ✓ · convergence ✓ · SPINE ✓ ·
essay-0 draft-lock ✓ (owner ear pending) → next = S5 collate A/B/C under the spine.

## 7. Second voice + main text reference (2026-10-25)

- **Dyczkowski's Śiva-Sūtra introduction imported as `dl1`** (owner): mp3 + srt copied
  from tantraessays repo, srt → stamped text (`text/shiva_sutras_introduction_dl.txt`,
  99 cues/1,982 words), 5 units adapted to our schema (uids dl1-01..05; their
  `[text:ss:…]` registry-tags preserved; grades re-derived: B/B/A/A/C — dl1-03 stakes-line
  and dl1-04 1.1-thesis are A). All 5 assigned S1 (revelation cluster + the 1.1 A/A
  cross-voice pair with Baumer ss3-10). Totals now **185 units (70A/106B/9C)**;
  verify_units 185/0 fails.
- **Aphorisms of Śiva = the main TEXT reference** (owner): held at
  `reference/aphorisms-of-siva-dyczkowski_clean.txt` (gitignored — copyright, never
  commit; same rule as tantraessays primary/texts). All six essay-0 SANSKRIT and
  TRANSLATION rows already source from it; per-sūtra card refs follow it.
- Both voices now serve one text: Baumer = interpretation archive (ss1–13),
  Dyczkowski = second archive voice (dl1), Aphorisms = the text on screen.

## 8. Session wrap (2026-10-25, continued) — questions, coverage truth, housekeeping

### 8a. Spine questions: opened per owner (analayo Nibbāna model)
Three owner corrections landed on the question set: (1) S2 object fixed (M10);
(2) S3 category error — consciousness isn't forceable, REALISATION is (M14);
(3) over-stuffed wordiness → owner's own rule-example "Why can't you force realisation?"
(M15); then the real upgrade: **open the questions** — name the ASK, withhold the
answer's content-word (M16). Final set (G0 7/7, role labels):
1 What is consciousness? (the thing) · 2 What keeps consciousness from being
realised? (the obstacle) · 3 How does realisation happen? (the arrival) ·
4 What does realisation do to experience? (the change) · 5 What does the mind have
to do with consciousness? (the mechanism) · 6 What happens after realisation? (the after).
Question↔content fit checked against actual A-pools (SPINE table): S2/S3 textbook,
S1/S5 strong, S4 (heart-lotus practice) and S6 (āsana/offering path-techniques) flagged
as wobbles — recorded, NOT patched (text-order homes stay; flow-read decides).

### 8b. COVERAGE TRUTH (owner question: "are we using all the content?")
Precise measurement (2026-10-25, `tools/coverage_measure.py` → `excavations/COVERAGE.md`):
**span-union 106m of 878m = 12.1%; words-on-covered-lines 12,418 of 75,278 = 16.5%**
(17.9% of lines). Uncovered spine-anchor lines: S1 421 · S2 238 · S3 135 · S4 148 ·
S5 491 · S6 149 — the missing 88% is materially ON-SPINE (anchor coverage 13–26%;
S4 thinnest). Inclusion plan = three channels + one read-pass in COVERAGE.md (worst-
served-first: day5-ii 5%, day6-ii 7.2%, dl1 5/99). 186→225 units (pass-1: day5_ii +18 ss11-09..26,
day6_ii +21 ss13-11..31 + 2 window fixes — see C-MARKS + LEDGER) = idea-dense extraction
(compare vatula 96 units);
**but there is NO coverage ledger for the remainder** — no C-MARKS equivalent, so we
cannot yet say what the un-unit'd 87% IS (logistics, participant Q&A, technical
stretches, her asides). Consequences:
- Essay A/B: fine (A⊂B pools are complete for their job).
- C-version "full walk": would have holes if built from units alone — vatula solved
  this with decompile-pools as the full-pool complement; dyczkowski solved it with
  100% line-coverage files. We have neither yet.
- Decision owed (open thread #1): which G1 standard for THIS corpus —
  (a) vatula-style span ledger (every span: unit'd or C-marked, ~73% realistic), or
  (b) dyczkowski-style full line-coverage pass (100%, multi-session), or
  (c) pragmatic C-build-time transcript ingestion (no ledger; verify at build).

### 8c. Housekeeping / organise
- M13: 242MB mp3s swept into git by `git add -A` → untracked, `audio/` gitignored,
  history rewritten (unpushed; .git 243M → 1.3M; packed-refs resurrection via
  `update-ref -d` documented). dl1 mp3 now local-only under audio/.
- Manifest complete: 13 sessions + dl1, all with transcripts (11 VTT-clean + 2 CF).
- CATALOGUE header refreshed (stale 180-unit counts → superseded pointer to
  SPINE_ASSIGN.tsv as authority) + dl1 addendum row.
- SPINE_PREVIEW.md banner: superseded by SPINE.md (kept as S2 design record).
- `tools/__pycache__` untracked; .gitignore += it.
- tantraessays-side: `/tmp/verify_cov.py` + `/tmp/verify_bc.py` (volatile /tmp — M12
  scar) copied to `dyczkowski/tools/`; its PROCESS_NOTES §14d repro-path note updated.

### 8d. STATE NOW (one screen)
- **Grading:** 186 units (71A/106B/9C), verify 186/0 → pass-1: 307 (82A/83B/142C), 307/0.
- **Segmentation:** 186/186 → pass-1 307/307 one-home (manual pass-1 rows in SPINE_ASSIGN), 48+ overrides in s2_cluster.
- **Convergence:** units × A-buckets agree (S1 top, S5 second, S3-thinnest-accepted).
- **SPINE:** 6 open questions, role labels, fit-check table, per-section anchors = her words.
- **Essay-0:** stack SANSKRIT→TRANSLATION→PLAIN→BÄUMER built (build/ESSAY0_OUTPUT.md),
  flow-read artifact written (weak join 4→5 flagged), lock = DRAFT (owner ear pending).
- **Voices:** Baumer ss1–13 + Dyczkowski dl1 (2A) · **TEXT law:** Aphorisms of Śiva (held, gitignored).
- **Gates:** verify_units ✓ · G0 7/7 ✓ · s2 totals ✓ · plain_filter hash ✓ · clean tree.

### 8e. OPEN THREADS (ordered)
1. **Coverage standard decision** (8b) — pick (a)/(b)/(c); blocks honest "full walk" claims.
2. **dl1 end-to-end read** — imported via units only; full pass of `text/shiva_sutras_introduction_dl.txt` pending (1,982w, ~20m).
3. **ASR ear-check list** — flagged forms (rishikesh=paratrishika-people, Mitta City=siddhi, Dantoraja=Tantrāloka, bhairava-name garbles…) — ear against mp3 at render; maintain list in MISTAKES/units.
4. **Audio flow-read** — question→pause→clip with real timing; stress joins 4→5 and S6 weight (levers: promote ss13-06 dancer to A, or re-ask).
5. **Owner ear on HEAD mp3** → essay0_lock.json LOCK (then G12-analog: window/sanskt/plain freeze).
6. **key_v2 sign-off** — proposal key (verily→truly) is one entry; plain rows are honest no-ops until signed; grows per section.
7. **Sanskrit OCR-verify** — tritayabhokta vtresah, nartaka atma (dl sūtra forms) vs print before any card render.
8. **Baumer mp3s local** — only KSpk4/r5w local; pull the other 11 from R2 at build/render time.
9. **S5 collate + B-selection + three-layer beats** (BUILD ORDER: essay0 → A → B hold-up → C walk) — the main build, not started.
   B-sweep instrument: `build/HOLDUP_SHEET.md` (219 B-rows, 114 provisional from pass-1 —
   verdict KEEP-B / DEMOTE-C / LEDGER per row at lock). Shapes per vatula `process/FORMULA.md`:
   **A ⊂ B ⊂ C, append-only** (A plays inside B unchanged; C = texture minus chant/mic/filler;
   grades = essay-layer membership — C-grade means texture-clip, never a note: M21).
   UNFOLDING law (vatula FORMULA §THE UNFOLDING): the same seed expands at every layer,
   essay0 recurs 4× (heads of 0/A/B/C), layer-bells 880Hz sections / 220Hz crossings.
10. **Cross-repo calls:** BHU-Tantraloka ownership (tantraessays vs vatulanatha CUTTING-FORMULA); CATALOGUE/dl1 rows re-audit if sections move; corpus.db "next loads" (essay-corpus wants PH/Spanda/SS units — ours qualify once locked).

## 8f. Four-layer gospel ratified (owner, "for all things")
Format confirmed canonical across the project: SANSKRIT → LITERAL TRANSLATION →
PLAIN ENGLISH → ARCHIVE VOICE (Baumer|Dyczkowski). Written as law in SPINE.md
("THE FOUR-LAYER GOSPEL"); beat = card(sanskrit+translation) → plain → voice;
essay-0 = the four rows spoken in order. Section sūtra-ranges now in SPINE headers;
unit→sūtra feed = section-default with explicit exceptions (see SPINE fit table).
Stale-question sweep: old Q strings exist ONLY in MISTAKES/PROCESS history (allowed)
and the gate's designated alternate.

## 8g. HANDOVER (supersedes 8d as the current-state screen) — 2026-10-25 end

**Read order for anyone picking this up:** `README.md` (front door) → this file §0–§8 →
`MISTAKES.md` (before touching tools) → `excavations/SPINE.md` → `build/ESSAY0_OUTPUT.md`
→ `build/ESSAY0_FLOW_READ.md` (read it aloud).

### What happened after 8d
- **Four-layer gospel ratified** (§8f) and enforced: sūtra-ranges in all six SPINE
  headers; unit→sūtra feed = section-default + explicit exceptions; every S/T row in
  ESSAY0_OUTPUT carries Aphorisms line-refs (12); voice-layer + plain-state rulings recorded.
- **Fresh-eyes read-through** (owner: "read through with fresh eyes") caught 3 defects,
  all fixed in 7f12c5d: (a) stale enquiry-chain in ESSAY0_OUTPUT (silent un-asserted
  string-replace had left the OLD closed-question chain across two commits) → now
  "the thing → the obstacle → the arrival → the change → the mechanism → the after";
  (b) FLOW_READ carried composed diacritic Sanskrit (caitanyamatmane, tṛtayabhoktā…)
  violating the never-compose rule → all five SANSKRIT lines now match held forms;
  (c) flow-analysis prose still described old questions + wrong recurrence claim →
  now 3+3 alternation (consciousness Q1/2/5, realisation Q3/4/6).
- **M17 logged:** silent `.replace()` without count-assert on doc edits lets stale
  content survive — assert-or-die on every scripted doc edit.

### FINAL STATE
- 307 units (82A/83B/142C) · verify 307/0 · segmentation 307/307 · G0 7/7 ·
  plain hash MATCH · manifest 14/14 · gates green · tree clean.
- Six open questions (fit-checked vs A-pools: S2/S3 textbook, S4/S6 wobbles recorded).
- Essay-0: four-layer cells + flow-read artifact — **text-level passes; lock DRAFT**.
- Text law: Aphorisms (held, reference/ gitignored) · voices: Baumer + dl1.
- Coverage: 13%-time in units, remainder unledgered (§8e-1 decision still owed).

### SECTION ARGUMENTS pass (owner: "textually make sense as a cohesive flow argument")
All 71 A-clips composed per section in her order → `build/SECTION_ARGUMENTS.md`.
Verdicts: S2 tightest (six-clip complete essay), S3/S1/S6 flow (S6 = strongest arc,
innermost-offering → stage), S4 one soft spot (ss7-16 icchā answers "drives" not "does"
— demote lever), S5 opener needs one bridge (MVUT-practice → mind). Two named bridges
total; everything else stands on her words alone. Assembly explicitly NOT needed for
this test (owner).

### JOIN AUDIT (owner: "manually check line by line that essays ARGUE, not random statements")
`build/JOIN_AUDIT.md`: every one of the 65 adjacent clip-pairs verdicted (55 OK / 9 SOFT /
0 WEAK) + cross-section joints + answer-test per section (closers all close; S5 closure
flagged: answer lives mid-section at mind-becomes-mantra, guru-grace is frame-closure).
Quote-integrity first: 71/0 re-verify caught 2 manual-paste repairs (M18). No reorderings,
no cuts proposed at text level. SECTION_ARGUMENTS gained 5 audit-notes (2 bridges already
known, 2 accept-deictics, 1 criteria-glue, 1 pivot, 1 closure-test) and its whole-doc
verdict now cites the audit numbers.

### PASS-1 COMPLETE (2026-10-25) — the full Baumer read-through
All 13 Baumer transcripts read line-by-line; every gap dispositioned in COVERAGE_LEDGER.tsv
(584 rows); +121 promotes → **306 units (81A/138B→216B/9C)**; A-pools unchanged at 75+6
(S5-3 + S3-1 + S6-3 from pass were A? NO — pass-1 promoted ALL-B except day4_i's 2A:
net A = 81). Six window-vs-quote fixes (ss13-03/05, ss7-05/16, ss9-02, ss6-18), M19
dup-removal, M20 cross-file-caption-dup. Coverage: span 12.3→15.9% (honest, one bogus
window removed), words 16.9→23.2%, anchors 13-26% → 26-35%. Files with 0 promotes
(ss2, ss4): original units already complete — pass CONFIRMED their coverage. dl1 (second
voice) same day: +3, 1 fix. Gates: 309/0 · G0 7/7 · plain MATCH. dl1 (non-Baumer) + coverage-standard decision remain.

### OPEN THREADS — final list (§8e items still live; closed ones noted)
1. Coverage-standard decision (ledger vs line-pass vs build-time ingestion) — **LIVE, blocks "full walk" claims**.
2. dl1 end-to-end read (imported via units only) — LIVE.
3. ASR ear-check list at render — LIVE (render-time).
4. Audio flow-read: joins 4→5 + S6 weight (levers: ss13-06 promote / re-ask) — **LIVE, next real gate**.
5. Owner ear on HEAD → essay0 LOCK — **LIVE, owner-blocked**.
6. key sign-off → plain regenerate + hash — LIVE (owner).
7. OCR/print-verify of Sanskrit forms (tritayabhokta vtresah, nartaka atma, caitanyamatma diacritics) — LIVE (card-build time).
8. Baumer mp3s: pull other 11 from R2 at render — LIVE (build-time).
9. **Main build** (essay0 → A → B hold-up → C walk → beats → render) — not started.
   Run `build/HOLDUP_SHEET.md` for the B-sweep; A⊂B⊂C append-only + 4× seed-recurrence
   per vatula FORMULA/UNFOLDING (M21: C = texture, not notes).
10. Cross-repo: BHU-Tantraloka ownership; essay-corpus corpus.db load — LIVE (external).

## 8i. V1 BUILD DAY (2026-10-26) — sweep + manifests + audio substrate

Owner: "just get a v1 ready... bell structure... not worried about visuals."
Executed in order:
1. **State-file fixes:** SPINE repro (180→308, `--apply` now REPORT-ONLY — it would
   erase 124 pass1-manual fallbacks), COVERAGE table (309→308, 584→678 ledger rows),
   676→678 ledger mentions, C-homes ghost (ss5-14→dl1-05), SPINE section headers
   (stale pre-pass-1 counts → live 76/30/40/43/71/47).
2. **All 11 missing Baumer mp3s pulled** from R2 bucket `longform-audio/`
   (boto3 path-style, STALLSHARK creds) → audio/ complete: 14/14 local.
3. **B-sweep RUN-1** (219 rows, HOLDUP): **83 KEEP-B · 134 DEMOTE-C · 1 LEDGER
   (ss3-08) · 1 PROMOTED-A (ss4-15, M22 cell-grade bug)** → 307 units
   (82A/83B/142C) · verdicts in build/holdup_verdicts.json + B_SWEEP.md (reasons) ·
   M22/M23 logged · gates re-run 307/0.
4. **Manifests** (`tools/build_manifests.py`): quote-located tight cuts (line-run +
   word-rate interpolation, completeness/padding bounds), SECTION_ARGUMENTS order
   canonical + (sess,ts) inserts, SEED-CAP cells excluded, ss4-22 skipped (M23b):
   A 76 clips/23.5m · B 159/53.2m · C 300/95.4m → 18 JSON + C_WALK.md.
5. **BEATS.md** (run-order: L0→LA→LB→LC, 880/220 bells, opener grammar, pipeline) +
   **SPEAKERS.md** (TTS placeholders for questions/cards) + **EAR_CHECK.md** (32 rows).
Open at day-end: audio generation (TTS→bells→cuts→layer concat→master), ear-session,
coverage-standard (#5), key sign-off. A=23.5m vs band 10–20m recorded honestly
(BEATS.md run-time honesties) — no A-clip cut for runtime.

CLOSED this session: format law, sūtra map, question set, stale strings, manifest/catalogue/pycache, /tmp-scripts (tantraessays).

## 8j. RESPONSIBILITY READ (2026-10-26) — agent takes verdicts, not summaries

Owner: "take responsibility now — does essay-0 and A make sense answering
the questions, what pausing, does the flow work." Agent re-read the six
cells + six arguments + joins cold and returned verdicts with reasons
(full text in session; decisions below). Codified the same day as
AXIOMS.md #13, SKILLS.md (Responsibility read), AGENTS.md (root).

Findings (each names its sentence; none existed in any artifact before):
- S1: clip never says "self" (card does) — fusion works, doing quiet work; don't widen the gap.
- S2: best cell, no action.
- S3: 70% apophatic — B carries the positive mechanism (dl1-07 in earshot if listeners ask "but what DOES it?"); kept consciously.
- S4: most opaque T of the six — fix is air (longest T-landing beat), not new words; seed blooms late, section repays the debt (recorded).
- S5: excellent, no action.
- S6: voice answers "stage" to an "actor" question — audition ss13-20 as cell voice at ear, keep ss13-09 as closer.
- Pauses differentiated by job: breath 2.5s after short Q (3s for S4/S5 long Q) = thinking; explicit ~1s beat after T = landing (S1/S2-shock/S4 especially); water = reset; 5s XL at 4→5, S5 Q does the bridging (no spoken bridge).
- L0→LA restatement endorsed as doctrine-performed; zoom bells load-bearing at master scale (recurrence must feel ritual).
- S5 opener bridge endorsed without redesign (planned glue stands; ear verifies).
- G12 breach named: ss4-15 runs 46s vs 25s rule — lean KEEP WHOLE with written exception (one thought); ear confirms or splits.
Decisions handed to owner/ears: S3 grace question, S6 voice audition, G12 exception.
Lesson recorded: gates check compliance, only the read checks sense —
a 6/6-cohere report without per-sentence verdicts would have shipped
every one of these defects green.

### §8j follow-up (2026-10-26, same day) — fixes applied, one flag overturned
- S1-19 filled: Sanskrit + translation verified vs held Aphorisms l.1923-24
  (Kṣemarāja 1.19; page + front-listing both skip it); chant window
  dip-snapped [361.2→366.5]; storyboard now 77 verse rows.
- Pauses differentiated in assembly: T-landing beat 1.0s after every
  translation; 3.0s breath behind the two long questions (S4, S5 cells).
  Essence re-rendered: 75 cues, 311s, sheet==master asserted in build.
- S6 audition DROPPED on re-read: ss13-09's delight-exhibiting-drama
  directly answers "what happens after" — the slide I flagged was mine,
  not the cell's. No swap; verdict recorded here instead.
- G12 exception recorded (not resolved): ss4-15 runs 46s vs the 25s rule —
  KEEP WHOLE stands (one thought; cutting loses the partial-vs-deep
  distinction). Ear confirms or splits; the flag rides the production
  sheet until then.
- S3 apophatic ruling stands with dl1-07 noted in earshot (storyboard S1-5).

## 8k. FLOW REVIEW + LINT (2026-10-26) — peer review made repeatable
- Built `tools/flow_lint.py`: deterministic pre-ear checks (voice runs,
  joint inventory, >25s clips, repetition, deictic slots, pause
  inventory). Same sheet → same findings, any agent.
- Wrote `process/FLOW_REVIEW.md`: 10-question evidence protocol (every
  answer cites cues/timecodes/quotes) + verdict format (PASS/SOFT/FLAG,
  FLOW/NO-FLOW). Filed `build/FLOW_REVIEW_essence_v1.md`: FLOW with
  3 ear FLAGs (c2 "they" antecedent +5s in-clip; c2/c4 split points;
  S1-head "22 sutras" trim — short alt cut banked:
  `audio/gen/l0_cuts/head_s1_intro_short.wav` [250→257s]).
- Read verdicts: Q-chain holds; landings ≤4s; c2's 46s is load-bearing
  (obstacle gets weight), not bloat; Light-head/spine-cell interleave
  checked — no conflict (c1–c4 are all Light-1 sutras); c1 two-span
  concat OK-text, ear-verify.
- Rule confirmed: lint gates the review, the protocol gates the render;
  disagreements land on FLAGs with evidence both sides. Machine
  enumerates, only the read judges.

### §8j follow-up 2 (2026-10-26) — Fish voice in, TTS_SAY map, L0 retired
- Alibaba key 401s at both regions; ears run on OpenRouter gpt-audio-mini instead (~$0.002/pass). Qwen-omni path stays open if a good key lands.
- Owner-supplied Fish key verified + stored (local env only, never echoed); all 24 TTS lines rebuilt in Fish s2.1-pro-free default voice. espeak retired everywhere.
- Bhairava fix verified by isolated probe (v2 "Bye-ruh-vuh" transcribed exactly; v1/v3 degraded) → `TTS_SAY` spoken-form map in both builders; display text untouched. Full-mix transcripts are unreliable for fine phonetics — isolated probes only.
- Excerpt probes confabulate worse than full passes (c3 excerpt invented mantras/speakers). Method: probe isolated lines, full pieces for structure, never excerpts as evidence.
- make_l0.py SUPERSEDED by make_essence.py (two assemblies = two truths); essence is the single build path. L0 mp3 kept as history.

### §8j follow-up 2 (2026-10-26) — ported vatulanatha's QA apparatus, fixed the repetition + room properly
- Compared process/19/20 + 18-SPACING + sfx kit. Adopted, with credit:
  room-tone beds (Baumer lecture-gap room, -63dB) replace digital-silence
  pads in place (same durations, zero sheet change); per-piece level norm
  (gain = min(-21-mean, -1.5-max), their formula) for every speech cut —
  measured now: chant -21.0, Baumer -23.2, TTS -21.0 exact, intros -21.0;
  listen.py excerpt-edge rule + verbatim-beats-verdict adjudication;
  their air/level numerics folded into validate_sheet + flow_lint.
- Answered the three charges: (1) bell = plain 880Hz sine, kept
  deliberately — bell grammar is locked design, their kit is first call
  at ship; (2) "consciousness is the self" repetition = gospel T+P —
  now DIFFERENTIATED (P at 1.12x summary delivery), model confirms
  differentiated not echo; residual dislike of the pairing itself is
  taste → ear call, not a defect; (3) Qwen ears: 6 passes, every fix
  verified — TTS-Sanskrit eliminated, c1 crossfade, c2 antecedent,
  S1-19 filled, c4 corrected to 1.11, afade silence bug caught by
  measurement the model pointed at.
- Quoting pressure test established: vague "hard cut" claims that cannot
  produce quoted locations on re-ask are discarded (two such claims
  dissolved this way). Verbatim beats verdict, again.
- S1 head shortened to the no-count intro (7s); G12 exception stands with
  mitigations in the build, not just in prose.

### §8j follow-up 3 (2026-10-26) — R2 + handover
- Essence master uploaded to R2 (`longform-audio/shiva-sutras/essence_v1.mp3`, verified by HEAD). Owner-supplied keys matched the stored set; nothing new written anywhere.
- HANDOVER-2026-10-26.md written: full session log for the next agent.

### §8j follow-up 4 (2026-10-26) — R2 packs
- Osho Hindi 10-talk zip built (stored, no recompression) + uploaded as
  `longform-audio/shiva-sutras/osho-hindi-10-talks.zip` (327 MB, HEAD-verified).

## 8l. STANDARD v2 — Lakshmanjoo voice swap (2026-10-27, Standard only; Custom frozen)
- Law recorded (BUILD_ENGINE + process/10 steps 3-6): B1 = his statements
  measured per-verse, B3 = his English verbatim excerpts, B2 = Dyczkowski T
  verbatim, coda = Sharma complete run ≈9 min. Baumer cells stay in
  essay-0/Custom; no verse dual-voiced in Standard.
- Transcription: tools/lak_transcribe.py (local faster-whisper base, stamped
  txt + segment JSON sidecars). Sanskrit-heavy openings garble in base
  (1.14, 1.19 heads) — large-model re-pass owed before locating those.
- Locate: 11/14 measured (table in storyboard v2); FLAGs = 1.14/1.19
  (re-pass), 1.20/1.21 (own statement later in file — heads review previous),
  1.22 (file↔verse map vs book). Pattern: file heads often review the
  previous sūtra — locate skips review.
- Pilot 1.1+1.2: windows snapped to speech onset (M27), room bed from his own
  pause, levels -21dB, Qwen qa = speech clean/natural; bare-B1 proof can't
  FLOW (needs full beats — B2+B3 next). M28 logged (verify on partials).
- Steals from vatulanatha (pulled, 5 commits): dual-reading manifest grammar
  [archive read → breath → translation]×N, sheet-driven build, done-by-rule.

### §8l follow-up (2026-10-27) — B2 corrected to his gloss (owner: "why Dyczkowski verbatim?")
- Dyczkowski-voiced readout was my leftover, not a decision: his own English
  gloss sits adjacent to every statement, same voice and breath. Standard B2
  = his gloss verbatim; Dyczkowski stays held TEXT (card + verify anchor),
  unvoiced. No TTS in the verse walk.

### §8l follow-up (2026-10-27) — Layer A definition (owner)
- A = highest-signal explanation per verse. Aphorisms of Siva is the source
  of truth for what each verse says (template hooks); audio is chosen for
  succinctness against those hooks. Fallback ladder: his excerpt first,
  then archive voices where they strike the verse, worst case Fish TTS of
  Dyczkowski's words verbatim (never paraphrased).

### §8l follow-up (2026-10-27) — Standard 0/A/B/C proof for 1.1 + 1.2 (tools/build_standard_verse.py + build/std_1_{1,2}.json)
- Durations: 1.1 0=24s A=80s B=405s C=806s; 1.2 0=50s A=114s B=444s C=663s.
  A in 1-3min band, B = A + 5-10min, C loose. Russian doll append-only.
- QA: A proofs fixed twice (M27 onset snap; sentence-complete ends — 1.2 B2
  extended to 146.2, A-core to 292.5 then 298.0). B joints 5/6 CLEAN, one
  RUBBED (anupaya entry) ear-flagged. C QA: no edit seams found; only source
  texture (pauses, overlap, stumbles) accepted as verbatim. Model limits hit:
  joints prompt bails on long single-voice; verify prompt confabulates on
  partials (M28); water-level room reads as "silence" to the model.
- Guests: C slots empty this round (his-loose only). Osho/Hareesh/dl1
  candidates unmapped — open for the C pass at scale.

### §8l follow-up — Cross-verse assignment sweep (Standard): NO MOVES
- Ran tools/xverse_scan.py (keyword scan for other verses' sutra forms in
  each file). Tool has a file-mixup bug (reports hits with wrong file's
  timestamps — DO NOT TRUST its locations; M-logged separately).
- Verdict on reading evidence: Lakshmanjoo files are per-verse by
  construction (one lecture per sutra), unlike Baumer's thematic sessions.
  Review-heads (1.20->1.19, 2.8->2.7, 3.2->3.1, 3.24->3.23, 3.38->3.37)
  STAY in their files (orientation, not movable depth). Cross-verse quotes
  (1.2 cites 1.3's formula @796.8) noted as seealso, never double-claimed
  (M20 rule). No unit moves. Assignment complete: everything home.

### §8l follow-up (2026-10-27) — Standard objective, generalized (owner)
- The Standard's 0, for ANY text: the source's own words, then the most
  precise available translation (clinical, exact — the trust anchor),
  then the master's rendering (the living meaning). Precision and
  interpretation are different jobs carried by different voices:
  Dyczkowski gives us precision; Lakshmanjoo gives us the meaning.
  Even with a master, both are needed — the master interprets, the
  scholar fixes the words. 0 = Sanskrit (him) -> precise English (AI,
  verbatim) -> his English (him). A adds one compressed explanation
  passage per verse (~1 min); whole of A ~= 1 hour.

### §8l follow-up (2026-10-27) — "he" = Siva (owner question, answered)
- In his lectures "he defines / he puts forth / he says" = Lord Siva
  speaking in the sutra (revealed through Vasugupta). Ksemaraja is named
  separately ("the commentator says") and never takes the bare "he".
- A-completion status: 27/77 with A built+QA-sampled; 0 verified for all
  located verses (B1 book-verified where Sanskrit is voiced; Sharma
  fallback + CF re-pass + ~10 deep-locates queued). Remaining A = read
  file, pick core passage against the book hooks, manifest, build, QA.

### Template text-critical notes (2026-10-27)
- Book (Dyczkowski) transposes prana/madhye vs Ksa+Gretil+files: book 3/24
  = Acad 3.22 (pranasamacare), book 3/23 = Acad 3.23 (madhye'vara). Mapped
  by content, never by number. Book also inserts an extra visarga-sutra at
  3/15 (no Ksa counterpart) and splits Ksa 1.16 into 1/16+1/17 (Acad 1.17-22
  = book 1/18-1/23). GRETIL Kaul text (75 sutras, no turya/hrdaye standalone)
  is the exact-Sanskrit reference; Lakshmanjoo voices the two Ksa-only
  sutras himself.

### §8l follow-up (2026-10-27) — A complete for all 77 (manifest level)
- Every verse: 0 (sutra+gloss) + A (one compressed excerpt) mapped, built
  via tools/build_standard_verse.py + build/std_*.json (77 files).
- B1 = his word-verified voicing; Sharma exact slices where he paraphrases
  or the tape garbles (1.4/1.6/3.22/3.41/3.42 + cf re-pass set).
- B2 = his adjacent gloss; book (Supreme Awakening) is the A-selection
  guide; GRETIL Kaustubha text is the Sanskrit reference (template_77.json).
- Numbering: Academy=Ksa (22/10/45); book inserts one visarga-sutra at 3/15
  and splits 1.16; Bhaskara order transposes prana/madhye vs Ksa.
- Remaining: full-build QA sweep (cross-voice joints first), B/C layers,
  TTS B1b line, Sharma coda assembly, owner ears.

### §8l QA ruling (2026-10-27) — cross-voice B1 joints are doorways, not seams
- 4 independent qa passes (1.4, 1.6, 3_7, 3.41) all flag the Sharma-chant →
  Lakshmanjoo-lecture handover as RUBBED (room/timbre discontinuity).
  Expected: different recordings, rooms, decades — no bed hides that, and
  hiding it would be dishonest. Ruling: cross-voice joints are DOORWAYS
  (2.5s room breath stands as the pause between movements), verdict SOFT
  by design, ear confirms intent. If owner wants formal punctuation, the
  approved alternative is a bell at cross-voice joints — NOT longer beds.
- Model failure mode logged (M33): Qwen repeatedly hallucinates a "synthetic
  narrator" in files containing zero TTS, mislabeling Lakshmanjoo's clipped
  English delivery. Any pass reporting synthetic speech in a TTS-free build
  is discounted on that claim; structural findings stand only with a second
  corroborating pass.

### §8l A-complete (2026-10-27) — all 77 verses have built 0 + A
- 77 manifests (build/std_*.json), all built via tools/build_standard_verse.py.
  B1 = his voicing word-verified, else Sharma exact slice (word-verified:
  1.4, 1.6, 3.17, 3.18, 3.22, 3.29, 3.32, 3.41, 3.42 + CF re-pass heads
  1.14/1.19/2.2/3.11/3.21/3.34/3.37 where his voicing is cleanest).
  Cross-voice joints = doorways (accepted RUBBED, mitigations in build).
- QA: ~20 proofs sampled; real defects fixed (mid-sentence cuts 1.2/1.5/2.3/
  3.32, dead-head onsets, B2 overruns); M33 hallucination (fake TTS) noted
  6+ times, rule logged — voice-ID claims need transcription corroboration.
- Runtime check: A proofs run ~1-2.5 min (over the 1-min target on several —
  compression pass owed before lock; pilot set first: 1.1, 1.2, 2.3).
- NEXT: B-layer (Baumer/dl1/Osho/Hareesh guests per verse) → C (full walk +
  stories) → B1b AI-translation line → coda assembly → owner ears.

### §8l Standard build method, as executed (2026-10-27, canonical)
1. SOURCE: per-verse lecture mp3s (79 files, 16h). Transcribe locally
   (faster-whisper base): stamped txt + float-timestamp segment JSON sidecars.
2. TEMPLATE: GRETIL Kaul text = exact Sanskrit per verse (Academy-keyed;
   Ksa-only turya/hrdaye from his voicing); Aphorisms = per-verse exposition
   hooks + translation check; Lakshmanjoo book = A-selection guide + his
   English. Numbering traps logged (book 3/15 extra, 1/16 split, 3/22-3/23
   transposition vs Ksa/Gretil/file order).
3. LOCATE B1 per verse, word-verified onset (M30: no filler; M31: book form;
   M27: snap to speech; Sharma exact slice where he paraphrases or tape is
   garbled; CF large-model re-pass for garbled heads). B2 = adjacent gloss,
   sentence-complete (M29). B1+B2 = Layer 0.
4. A = book's per-verse section mapped to timestamps (~1 min/verse);
   curated for highest signal, never padded, thin stays thin.
5. BUILD via tools/build_standard_verse.py from build/std_*.json (span-hashed
   cut names, per-piece norm to -21dB, own-room beds, 0.15s afades).
   QA: qa + joints per proof; cross-voice joints are doorways (accepted
   RUBBED); model voice-ID claims need transcription corroboration (M33).

### §8l B-layer method, proven on 1.1 (2026-10-27)
- B per verse = A + Baumer clips mapped 1:1 to book exposition hooks the A
  leaves open (here: knowledge+action union <- ss1-27; knower-known one <-
  ss4-08; anupaya <- ss1-29). Each clip word-verified, sentence-complete;
  wrong-file hazard logged (M34: verify sess<->mp3 map from build_manifests,
  never assume order).
- Assembly: A proof + breath + B clips in book order + water. 1.1 B =
  127.6s, QA FLOW, all joints CLEAN (cross-voice doorway holds).

### §8l QA close-out (2026-10-27) — A verified across the arc
- Sampled ~25/77 A proofs with Qwen qa/joints. Real defects fixed: mid-sentence
  cuts (1.2, 1.5, 2.3, 2.9, 3.32, 1.8 B1/B2/A-core bounds), dead pre-speech heads
  (M27 onsets: 1.1, 1.2, 2.1, 2.7, 3.9, 3.17, 3.21, 3.35, 3.44, 3.12...),
  wrong-file cut (M34: ss4-08), overlong B1s trimmed to the sutra (M30/M31).
- M33 confirmed 6+ times with a decisive test: faster-whisper transcription of
  the accused file shows coherent single-speaker lecture while Qwen reports
  "synthetic narrator" + "cut off mid-word" + "repeated fragments" for the
  same audio. No TTS exists anywhere in the std chain (verified: 0 synth
  files under audio/gen/std/). Voice-ID claims are now inadmissible without
  transcription corroboration; structural claims still require it too.
- Cross-voice (Sharma B1 -> his B2) joints ruled DOORWAYS (accepted RUBBED).
- Remaining for lock: full QA pass over all 77 (sampling done ~1/3), B-layer
  rollout (Baumer mapped per book hooks; 1.1 built FLOW 127s), C assembly,
  TTS B1b line, coda, owner ears.

### §8l close-out: A complete for 77, B method proven on 1.1 + 1.2 pilot
- All 77 verses: 0 + A built and gates green; ~30 proofs ear-checked, real
  defects fixed (mid-sentence cuts, dead heads, wrong-file B1, B1/B2 skips).
- M33 (synth hallucination) fired ~10x, always on single-voice files; twice
  corroborated by whisper transcription that the audio is clean continuous
  human speech. Standing rule: no rebuild on voice-ID claims, ever.
- B pattern locked: book hook -> Baumer unit, word-verified, sentence-closed,
  breath-joined, QA'd. C + TTS + coda + ears remain.

### §8l B architecture (canonical 2026-10-27): Lakshmanjoo mouth first, AI reads Dyczkowski verbatim
- Per verse: A + his continuation (deeper lecture cuts) + Baumer (book hooks
  his audio lacks) + Fish TTS of Dyczkowski's exact lines (Varttika verses,
  technical distinctions, variants, footnotes — only where no human voice
  carries the point). TTS convention: gloss parentheses dropped in voicing,
  full text lives on the card.

### §8l B status (2026-10-27): method proven on 1.1 + 1.2, rollout queued
- 1.1 B = A + his neti-neti + anupaya + her ss1-27/ss4-08/ss1-29 + 2x TTS
  (Varttika + microcosm verbatim). 266s. QA: joints CLEAN except
  cross-voice doorways (accepted); M33 hallucination noted again.
- 1.2 B = A + Baumer ss12-14 (devours both knowledges) 129s.
- B compositional law: his continuation FIRST (verbatim lecture), then her
  clips keyed to book hooks his audio lacks, then TTS of Dyczkowski exact
  lines only where no human voice carries the point.
- Qwen API down at session end (HTTP errors); final B QA pending ears.

### §8l Standard A/B definitions (canonical 2026-10-27, owner-locked)
- A = the "oh, that's it" cut: his sutra + his gloss + ONE sharpest
  explanation passage. ~1 min/verse. Nothing else.
- B = A + his continuation (deeper lecture cuts that expand the verse) +
  HER clips keyed 1:1 to book hooks the audio lacks + AI voice ONLY for
  GOLD insights no human voice carries (Dyczkowski verbatim, never composed).
  Order inside B: him first, her second, AI last — descending warmth, ascending
  precision. B ≈ A + 2-6 min depending on the verse's weight.
- The Aphorisms is the reference standard: its per-verse exposition is the
  checklist; every B element must answer a book point or be cut.
- C (later): full walk + stories + guests + coda. D (loose ends file).

### §8l joints doctrine (2026-10-26, stands unless ears overturn)
- Breath beds (2.5s own-room) between clips are the final answer to seams.
  Model flags them as "abrupt" about half the time; human ears hear a
  thinking pause. No crossfades, no music beds, no smoothing — the seams
  stay audible-by-design, like cuts in film. Only structural defects
  (mid-sentence cuts, wrong files, dead heads) trigger rebuilds.

### §8l TTS voice established (2026-10-27): Fish s2.1-pro-free + TTS_SAY
- TTS speaks ONLY verbatim book lines (never composed). Isolated-probe
  method: candidate spoken forms rendered alone, whisper round-trip decides
  (Mayiyamala -> "Mah-yee-ya-mah-lah" [whisper: Mahiyamaala]; Ksemaraja ->
  "Kshema-raja" [whisper: Keshma Rajas]; siddha kept inline with commas).
  TTS_SAY map in tools/tts_line.py. Varttika/microcosm/attribution lines
  rendered + round-trip verified; owner ear is final judge on proper nouns.
- B assembly: his-continuation -> Baumer (book hooks) -> TTS gold lines.
  1.1 B: 4.4 min FLOW (all cross-voice joints CLEAN); 1.2 B rebuilt with
  sentence-complete windows + probed TTS.

### §8l B-layer doctrine, final (2026-10-26, owner-ratified pattern)
B per verse, in order: (1) his continuation — deeper lecture cuts the A
did not fit; (2) HER voice, one clip per book hook A leaves uncovered
(matcher proposes via tools/b_match.py, human verdicts, word-verified
bounds, sentence-complete ends); (3) AI voice reading Dyczkowski VERBATIM,
only where neither human carries the point (Varttika lines, technical
distinctions, print-only variants). TTS rules: Fish s2.1-pro-free,
TTS_SAY spoken forms earned by isolated probe + whisper round-trip
(tools/tts_line.py), full text lives on the card, owner ear final on
proper nouns. Cross-voice joints are doorways (accepted RUBBED); never
blend, never smooth away.
A/B/C/D boundary law: A = the "oh that's it" cut (~1 min: sutra+gloss+
one core passage). B = A + depth (his + hers + book-gold). C = full walk
(stories, guests, coda). D = loose ends. Thin stays thin; never pad a B
to hit runtime, never cut audited membership for it either.

### §8l FROM SCRATCH — what this whole build taught (read before starting over)
If all artifacts vanished and only the process notes remained, here is the
order that would have saved ~40% of the work, and why each step exists:

1. TEMPLATE FIRST, cutting never. Build the verse map (book Sanskrit +
   translation + body bounds), the exact-Sanskrit reference (GRETIL or
   equivalent), and the numbering map with every recension trap WRITTEN
   DOWN (we burned turns re-deriving the 3/22-3/23 swap, the 3/15 extra
   sutra, the 1.16 split). No transcript is opened before this exists.
2. BATCH the mechanical verification. Word-onset every B1 in one background
   job (12s clips, base model, ~1 min each) instead of discovering mid-build
   that windows start mid-word. Same for sentence ends. The rule set that
   emerged — M27 (segments are not onsets), M29 (sentence-complete ends),
   M30 (no filler words open 0), M31 (book-verified forms) — is really one
   rule: never trust a boundary you have not seen with your own measurements.
3. CURATE WITH THE BOOK OPEN. A's core passage is whatever the book's
   per-verse section cannot do without; B fills what A leaves. Read the book
   section first, then cut. Doing it reversed (cut then check) produced every
   re-cut in this log.
4. MATCHER BEFORE VERDICTS. The keyword matcher (tools/b_match.py) proposes;
   the human disposes. Its scores are garbage-in-order only — metric proposes,
   reading verdicts. Never let it auto-assign.
5. TTS VOICE BEFORE TTS NEED. Establish Fish + TTS_SAY spoken forms by
   isolated probe + whisper round-trip BEFORE the first build that needs it.
   Every proper noun gets probed; owner ear is final. TTS speaks ONLY
   verbatim book lines, never composed text, never paraphrase.
6. MANIFESTS ARE CODE. Every window lives in build/std_N_N.json; the builder
   assembles from nothing else. Script ALL manifest mutations (assert counts
   after), never hand-edit, re-read before touching (two corruptions in this
   log came from blind in-place edits). Run tools/count + verify.sh after
   every batch. New artifact = FILEMAP row the same day.
7. QWEN PROTOCOL (what the model is actually for). Single passes are hints,
   never evidence. The model is RIGHT about: mid-sentence cuts, dead heads,
   wrong files, unclear antecedents, joints inventory. The model is WRONG
   about: who is speaking (M33 hallucinated TTS in clean single-voice builds
   6+ times), "dead air" (our room beds read as silence), taste ("draggy"
   natural speech). Standing procedure: qa for texture, joints for seams;
   corroborate every defect with transcript or energy measurement before any
   rebuild; log every fix with cause. When the API is down, fall back to
   structural verification (word timestamps + transcript), which catches
   90% of defects anyway.
8. WHAT BELONGS WHERE (the only taxonomy that survived contact):
   - 0 = sutra + gloss, nothing else. If a filler word ("and", "so", "now")
     opens it, the window is wrong, not the doctrine.
   - A = sutra + gloss + the single passage without which the verse is
     unrecognizable (~1 min). If you cannot name the core in one sentence,
     you have not read the verse yet.
   - B = A + his continuation (same lecture, deeper cut) + her clips nailed
     1:1 to book hooks + book-verbatim TTS gold ONLY where no human voice
     carries the point. Order inside B: him, then her, then the AI voice —
     warmth descending, precision ascending.
   - C = full walk (stories, guests, coda). D = loose ends, flagged, never
     silently dropped.
   - Cross-voice joints are doorways: room beds + fades, announced once,
     never "fixed" further. Bells are for section heads, not seams.
9. HOUSEKEEPING THAT IS LOAD-BEARING. Commit after every verse batch (we did
   not — the tree is dirty and that is a live risk). audio/gen/ is regenerable
   except masters; R2 mirrors every master; disk at 94% means clean
   intermediates aggressively. New tool = FILEMAP row + MISTAKES entry when
   it bites you.
10. THE ONE RULE ABOVE ALL: the text is the boss. When book, lecture, and
    transcript disagree, the sutra's own words win; when in doubt, cut less
    and flag more. Every flag in this log that was "fixed" by deleting words
    was a mistake corrected later; every flag fixed by moving a boundary was
    progress.

### §8l B-complete (2026-10-27) — all 77 verses have built 0 + A + B
- 77 manifests, all B built via tools/build_standard_verse.py.
  B composition: his-continuation (b-his, same file) + Baumer clips (uid,
  word-verified, sentence-complete) + TTS gold (book-verbatim Fish lines,
  probe-verified). Cross-voice joints = doorways (accepted RUBBED).
- QA: ~15 new B proofs sampled with joints; M33 hallucination (fake TTS)
  noted 8+ times on single-voice files; all RUBBED joints are cross-voice
  doorways by design. No structural defects found in B builds.
- B runtime: 77 files, 164.7 min total (~2 min/verse). 1.1 longest (316s
  with TTS gold). A runtime: 77 min. 0 runtime: 30 min.
- NEXT: TTS B1b line (all 77 Dyczkowski translations) + C layer + full
  assembly + owner ears.

### §8m AUTONOMOUS SESSION (2026-10-28) — push + 10-queue work-through
Pushed the 10-27 tree (7 commits: law+tools, template, ch1/ch2/ch3 manifests,
transcripts, handovers) — tree was 258 untracked + 15 modified, now clean.
Then worked TODO.md top-down, committing + pushing per item:

1. **Template truth (M35).** `sanskrit` field = build debris (14/77 last-elements
   match `book_sanskrit`); `sanskrit_exact` lost when template was rebuilt (two
   writers, last-write-wins) — `xverse_scan` crashed (KeyError), `locate_b1`
   silently matched nothing, `b_match` anchored on debris. Fixed: GRETIL vendored
   to `reference/gretil_sivasutra.json`, `template_v2.py` reads it + asserts
   77/77, `b_match` anchors on `book_sanskrit`.
2. **xverse M32 resolved.** Off-by-one slug `[4:-5]` misattributed every 2-digit
   file (`lak_1_11.txt`→home 1.1) + header-vocab false positives (sivasutra/
   unmesa) — fixed both; the 3.3→3.38 example evaporated. Scout works; no moves
   without a human read.
3. **b1_status enum closed (M36).** 7 spellings→5 states; builder asserts;
   4 uid-less M34-class Baumer clips verdict CORRECT (3 exact, 1 fix-window
   ss7-18 tail 4915→4930) + uid backfilled.
4. **B QA sweep (M37).** New `tools/qa_std.py`: 29 zero-overlap (hand-typed
   round-number) Baumer B windows found — built proofs played wrong audio
   inside green gates. All 29 re-located via `locate()`, 26 proofs rebuilt,
   transcription spot-check 25/29 + 4/4 via wider context, 3 sampled Qwen
   passes (M33 hallucinated TTS in all 3; zero corroborated defects). Sweep
   now zero FAIL / 41 FLAGs (F4 over-fires on long whisper segments — ear calls).
5. **B1b line (M38).** Cold read of all 77 spoken lines caught 7 template
   translation defects (2.3 wrong, 1.4/1.21/3.5 partial, 3.2 debris head,
   3.3 "May a", 2.5 "ofi") — fixed vs held front-listing/body. 77 Fish lines
   rendered (TTS_SAY +3 probed forms, Maya/Siva audited loans), inserted as
   0-layer b1b, all proofs rebuilt, qa zero FAIL, one joints pass CLEAN.
6. **Coverage per-corpus.** `--corpus baumer|lak|all`; Baumer truth re-baselined
   15.5%/22.6% (was diluted to 7.4% by lak files); Standard walk = 102/944 min
   (~11%, selective by design).
7. **Essence re-rendered.** `l0_cuts/` was gone; rebuilt → sheet==master,
   SHEET READY (276.8s, 3 FLAGs carried).
8. **Docs synced.** TODO 10-item rewrite, NEXT Standard-frontier, README state,
   FILEMAP rows for all new artifacts, this §8m entry.
Remaining: C layer → assembly → ears (TODO #4–6); owner message (TODO #10).

### §8n OWNER DOCTRINE (2026-10-28) — transcribe freeze + voiced-gold coverage
- Retranscription killed by owner: `text/` + `transcripts/` are frozen finding aids,
  never the verification path; garble zones verify by ear vs book/GRETIL. VERDICTS
  Action List item 1 struck and replaced; UNVERIFIED = ear task. (Pushed history not
  rewritten: the 51188f4 message over-claim — "retranscribe garbled lak files" with
  zero retranscribed files in the stat — stands corrected here, not in the log.)
- Coverage doctrine (book side, decided): every Aphorisms gold point VOICED in
  Standard by a human (Lakshmanjoo, Baumer, Hareesh) or TTS reading Dyczkowski
  verbatim where no human carries it. B1b (77/77 Fish lines) is the precedent;
  TTS_SAY probe discipline per line, verbatim-only. Completion rule for the VERDICTS
  B-expand queue: each point ends COVERED-by-human or COVERED-by-TTS; APPARATUS and
  thin-accept stand as declared. Thin stays thin — the doctrine voices gold, never pads.
- Scope note: this decides BOOK coverage in Standard. Baumer-walk standard (§8e-1:
  ledger vs line-pass vs build-time) stays open.

### §8o DISK CLEANUP (2026-10-28) — 95G→88G used, 1.8G→8.5G free
Deleted regenerable/renders only, primary untouched: custom WAV masters (mp3s
md5-matched to R2 v6/v5 first — 86a215fc / 2e380ac8), std cut wavs + concat txts
(proofs stay for assembly), tts_test stub, l0_essay0 superseded render, /tmp
Hareesh dup (byte-identical to audio/third primary). /home/ubuntu/analayo-nibbana
(3G) removed locally per owner (clean tree, in sync with origin, work lives in the
other repo — nothing pushed). npm cache cleaned. Left alone: huggingface weights
(B1 verification still needs whisper base), playwright/electron/chrome caches
(regenerable but slow — owner call), all other projects' dirs. Gates re-run green.

### §8p FULL WALKS ASSEMBLED (2026-10-28) — voiced-gold close-out
0/A/B walks concatenated verse-order, master==sum exact (0: 38min/18MB, A: 86min/41MB,
B: 184min/88MB), decode-clean, mirrored to R2 (walk_chall_{0,A,B}.mp3).
B-head qa: joints CLEAN; NO-FLOW verdict DISCOUNTED (essay criteria misapplied to a
fidelity walk — M28-class wrong-yardstick; no structural defect corroborated, no rebuild).
Deictic notes ride to the ear session. Full walks await owner ears (the only lock).

### §8p follow-up — cold read: 1.1 + 1.2 0/A/B (2026-10-28, full-proof transcripts)
1.1 FLOWS: 0 (sutra→translation→gloss, textbook) → A (independence-as-uniting-agency
+ one-in-many cap — the "oh that's it" cut, genuine) → B (sarvasamanya → neti-neti →
anupaya → her three seals → TTS Varttika+microcosm close). Each block answers the last
one's implicit question. One texture nit (kept, verbatim): bare "Complete Independence."
header mid-flow in A-core.
1.2 FLOWS: 0 (sutra→translation→two-readings gloss) → A (mala-not-dirt, samsara-sprout —
answers the obstacle question directly) → B (anavamala two ways → devours-both →
Matrka mechanism → attribution gold → stop-grasping release). Order law holds
(warmth→precision); 1.1-echo inside B2 ("Chaitanya Mahatma") self-resolves in 5s.
EAR FLAGS (not rebuilds): (a) 1.2's climax (release instruction) lands in synth voice —
does it land or deflate? (b) 1.1-echo moment for cold listeners.
Content-complete at 0/A/B; owner ears remain the only lock.

### §8p follow-up — public listen links (2026-10-28, voiced-gold walks)
- 0-walk (38min): https://d.uguu.se/RgfkWbOa.mp3 (R2 walk_chall_0.mp3, 18376839 B)
- A-walk (86min): https://h.uguu.se/mpanPjww.mp3 (R2 walk_chall_A.mp3, 41281000 B)
- B-walk (3h04): https://n.uguu.se/igaadhnX.mp3 (R2 walk_chall_B.mp3, 88429716 B)
Sizes match disk+R2 byte-for-byte. uguu links expire; R2 copies durable.

### §8p follow-up — voice doctrine (owner ears 2026-10-28)
Dyczkowski (B1b + TTS gold): voice THREE (Fish ef9c79b62e, deep/serious male) — owner
picked from 4-sample reel; default voice retired as too female. Sanskrit clarity line:
SEPARATE voice (round-trips prove Three mangles Sanskrit) — Adrian leads the shootout,
One backs up; owner ear decides. Intro+bells to be built on walks after voice lock.

### §8p follow-up — Sanskrit shootout round 2 (Qwen cast protocol, 2026-10-28)
9 voices tested, Qwen cast-ranked per sample + whisper cross-check. Kanha (Hindi male)
5+5 on both verses ("kaitanyam flawlessly separated"; "tritaya bhokta vire sa" nearest
to target) — RECOMMENDED. Pandit runner-up (5+4, only one to voice ch- correctly).
Sadhguru collapsed on the hard verse (5→3, muddy retroflexes). Conversational is
female (out on owner constraint). Slax/Three/Hindi/Gurudeep/Guruphilo out.
CALIBRATION: Qwen gave Alex 5/5 yet owner ears reject it as unclear — model clarity
scores OVERRATE; treat Qwen CAST as shortlist, owner ear as verdict. Verse-1 full-0
demo built in Kanha (provisional): bowls+bell+intro(voice3)+B1s+B1b+B2.

### §8p follow-up — Sanskrit long-read shootout (Qwen cast ×4, 2026-10-28)
Four verses per voice. Sadhguru 5/5 (full-transcript near-perfect, deep resonant
scholarly); Gurudeep 5/5 (every syllable distinct, recitative steadiness); Osho 4/5
(trail-off ending); Kanha 4/5 (shortened long vowels — drops from short-form 5).
Qwen cumulative: Sadhguru 5+5 most consistent; Gurudeep 4+5 close second with the
most chant-like delivery. RECOMMENDED: Sadhguru (owner already likes him), Gurudeep
backup. Owner ear decides.
