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
