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
- **Grading:** 186 units (71A/106B/9C), verify 186/0 → pass-1: 306 (81A/216B/9C), 306/0.
- **Segmentation:** 186/186 → pass-1 306/306 one-home (manual pass-1 rows in SPINE_ASSIGN), 48+ overrides in s2_cluster.
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
- 306 units (81A/216B/9C) · verify 306/0 · segmentation 306/306 · G0 7/7 ·
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
(ss2, ss4): original units already complete — pass CONFIRMED their coverage. Gates:
306/0 · G0 7/7 · plain MATCH. dl1 (non-Baumer) + coverage-standard decision remain.

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
10. Cross-repo: BHU-Tantraloka ownership; essay-corpus corpus.db load — LIVE (external).
CLOSED this session: format law, sūtra map, question set, stale strings, manifest/catalogue/pycache, /tmp-scripts (tantraessays).
