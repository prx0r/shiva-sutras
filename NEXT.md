# NEXT — the complete work queue for whoever picks this up

State at handover: 309 units (81A/219B/9C) all verify-green (pass-1 in progress) · segmentation 225/225 ·
6 open spine questions G0 7/7 · essay-0 four-layer stack built + flow-read PASS ·
SECTION_ARGUMENTS (Essay A as text) verdicts: 5/6 flow on her words alone, 2 named
bridges, 2 soft spots · pushed to github.com/prx0r/shiva-sutras (main).
Read first: README → PROCESS_NOTES (esp. §8b coverage-truth + §8g) → MISTAKES (M1–M17).

## A. OWNER-BLOCKED (cannot be done by an agent — request and wait)
1. **HEAD ear-pass** — listen `build/essay0_lock.json`'s stack via a cut mp3; if yes →
   set status LOCKED. Until then nothing freezes.
2. **Key sign-off** — `build/key_ss1_proposal.json` (currently 1 entry, plain rows are
   honest no-ops). Propose section keys first (B7) for an informed decision.
3. **Coverage-standard decision** (PROCESS §8e-1): (a) span-ledger à la vatula,
   (b) full line-coverage à la dyczkowski, or (c) build-time ingestion. Agent may
   PROTOTYPE (a) on one session (B2) but must not claim "full walk" until decided.
4. **Question-set ratification** — six opened questions exist and pass G0; owner has
   seen them but no explicit "locked" statement on record.

## B. AGENT WORK — immediate (no owner input needed)
1. **dl1 end-to-end read** — `text/shiva_sutras_introduction_dl.txt` (99 cues, 1,982w)
   never read linearly (imported via 5 units). Read fully; add units for uncovered
   stretches or C-mark them; re-run verify_units (target stays 0-fail).
2. **EAR_CHECK.md** — harvest every flagged ASR form from units' context fields +
   known list (rishikesh→paratrishika-people, Mitta City→siddhi, Dantoraja→Tantrāloka,
   "swatan prevada", "ghoul"→guru, "naruto"→nirodha, "bharat waita"→Bhairavatattva? …)
   into one ear-check list with uid + window + expected word. Verification itself
   needs mp3s (audio) — do after B4.
3. **Span-ledger prototype (option a)** — pick the smallest session (ss2 or ss9,
   ~15 min), walk it minute-by-minute: every span → unit'd | B-note | C-mark reason
   (`excavations/C-MARKS.md` style). Output: coverage % for that session + effort
   estimate ×13. This is the data for decision A3.
4. **Pull the 11 Baumer mp3s** from R2 (`longform-audio/bettina-baumer-shiva-sutras/`,
   creds pattern: see PROCESS §0 / tantraessays §11f — STALLSHARK from ~/figgsite/.env,
   NEVER echo) into local `audio/` (gitignored). Then B2's ear-check can run.

## C. AGENT WORK — build sequence (BUILD ORDER LAW: essay0 first, outward)
5. **Audio flow-read** — cut the six cells' + essay-0 windows with ffmpeg (windows in
   ESSAY0_OUTPUT/SECTION_ARGUMENTS), assemble question→pause→plain→voice per beat
   (`build/flowread/`), READ/listen; stress join 4→5 and S6 weight; levers documented
   (demote ss7-16 icchā to B; promote ss13-06 dancer to A; re-ask). Output: verdict +
   any SPINE edits (asserted replaces!).
6. **HEAD mp3** build (question→2-breath→plain→her clip, target 20–25s) → owner ear (A1).
7. **Section plain-keys (proposal)** — for each spine sūtra, the terms appearing in
   its A/B quotes that need mapping (`build/key_sN_proposal.json`) → owner sign-off (A2);
   regenerate plain rows + hash after sign-off.
8. **Sanskrit print-verify** — forms: `tritayabhokta vtresah`, `nartaka atma`,
   `caitanyamatma`, `jnanambandhah`, `udyamo bhairavah`, `cittam mantrah` vs a print
   source (Muktabodha KSTS e-text / Jaideva Singh scan — check patala-checkpoints corpus
   `sources/sivasutra/` first, then vatulanatha INVENTORY paths). Diacritics restored
   ONLY here, then card rows frozen.
9. **A-collate manifests** — per section: ordered clip list (uid, mp3, in/out, question
   line, card rows, plain) → `build/manifest_sN_A.json` = "Essay A at speed" (~10–20m
   target total). Append-only verified: every quote re-checked against units.
10. **B-selection protocol** — for each section: B-pool raw minutes exist (71m total);
    select to B ≈ A×1.6–2 per hold-up test (*does this deepen essay-0's answer?*) with a
    one-line reason per kept clip; NO superset ever ships (M-record + vatula 86m lesson).
11. **C-walk** — definition depends on A3 (coverage decision): A+B in her order with
    C-homes excluded; holes = whatever the ledger says is uncovered.
12. **Beats** (four-layer, gospel order) + SPEAKERS.md (Baumer | Dyczkowski | HUMAN
    questions | TTS plain) → then render (last, always).

## D. EXTERNAL / CROSS-REPO
13. **BHU-Tantraloka ownership** — vatulanatha/CUTTING-FORMULA.md holds a BHU cut plan
    for Tantrāloka; tantraessays holds the 15-transcript coverage. Decide which repo
    builds it before either starts (one message to owner).
14. **essay-corpus import** — corpus.db wants units (schema: id `shivasutras:ss5-05`
    etc.); export `unit_tags`-equivalent with sections once A1-A2 lock (their §"next loads").
15. **vatulanatha FUTURE-TARGETS** — add note: Śiva Sūtras units now exist in
    prx0r/shiva-sutras (their row 3 said "pull R2 when wanted" — audio now partially local here).

## NEVER (MISTAKES invariants — read MISTAKES.md first)
Never type a quote not just re-read · never compose Sanskrit/plains · assert every
scripted doc edit (count==1) · update parsers when extending headers · mp3s/audio never
committed · gates run on canonical sets · thin sections stay thin · fix checks before data.
