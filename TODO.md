# TODO — 20 actions for the next agent (2026-10-25)

> **STATUS 2026-10-26 (v1 push):** #7 sweep RUN-1 done (B_SWEEP.md) · #10 mp3s ALL local ·
> #12 EAR_CHECK built (listen-verify pending) · A/B/C manifests + BEATS.md + C_WALK built.
> Gates now: **307/0** (82A/83B/142C). Still owner-blocked: #3 ear · #4 keys · #5 coverage · #6 questions.

Context for each: `HANDOVER-2026-10-25.md` (narrative) · `NEXT.md` (full queue) ·
`FILEMAP.md` (paths + why) · `MISTAKES.md` M1–M21 (rules). Gates green at handover:
verify 307/0 · G0 7/7 · plain MATCH · tree clean · pushed.

**Legend:** 🔒 = blocked on owner (request once, in a single message; do the rest meanwhile)

### Read-first (before touching anything)
1. **Read in order:** HANDOVER → NEXT → MISTAKES → PROCESS §8. Acceptance: you can
   state M17 (assert count==1), M21 (C = texture-clip, not note), and the BUILD ORDER
   (essay0 → A → B-holdup → C → beats → render) from memory.
2. **Run the three gates cold** — `verify_units.py` (307/0), `validate_questions.py`
   (7/7), `plain_filter.py --check` (MATCH). If any fails, stop and fix before edits.

### Owner-gated (block once, then work around)
3. 🔒 **Request the ear-session**: play essay-0 HEAD+stack (`build/ESSAY0_*`); on yes
   flip `essay0_lock.json` status → LOCKED (single-field edit, count-asserted).
4. 🔒 **Request key sign-off**: regenerate `plain_essay0.json` with the signed key +
   rehash (`plain_filter`), never hand-edit rows; then Gospel plain-layer is final.
5. 🔒 **Request coverage-standard verdict** (PROCESS §8e-1): does the ledger stay this
   form or formalize (span-ledger rows / line-pass)? Until then no "full-walk" claims.
6. 🔒 **Request the one-line question ratification** (six spine questions locked) —
   G0 passes already; this closes the record.

### At lock (sequenced — each depends on #3)
7. **Run `build/HOLDUP_SHEET.md`**: 114 provisional-B first, then the rest —
   per row KEEP-B / DEMOTE-C / LEDGER; write verdicts into the sheet; re-run
   `sync_counts` + `verify_units` after any grade change.
8. **UNFOLDING audit run-2** against the LOCKED cells (`build/UNFOLDING_AUDIT.md`
   pattern): expect 0 N; re-judge the watch-list — ss4-02, ss8-06/07, ss10-03,
   S5-guru-cluster (the Q-decision lands HERE), ss7-16 lever.
9. **Collate Essay A per section** at FORMULA runtimes (10–20 min): windows from
   `SECTION_ARGUMENTS.md` **plus the 10 newer A's** it doesn't contain yet; every clip
   keeps source+timestamp (FORMULA rule 4).

### Audio track (independent of lock — start after #12)
10. **Pull the 11 remaining Baumer mp3s** from R2 (`longform-audio/…shiva-sutras/`,
    creds pattern in PROCESS §0 — `~/figgsite/.env` STALLSHARK_*, never echo) →
    `audio/` (gitignored).
11. **Build the section-A cut manifests** (uid → file → in/out from timestamps) →
    `build/manifest_s*_A.json`; **cut + listen** the six section runs; verdicts on the
    soft spots (S4 icchā lever, S6 offering/posture wobbles, S1/S5 bridges).
12. **Ear-check list**: grep contexts containing "EAR" (11 hits) + known ASR suspects
    (rishikesh, Mitta City, naruto, fairy/ferry, eye/I-consciousness) → `EAR_CHECK.md`
    with uid+window; verify against audio when #10 lands.
13. **Cut `essay0_1.mp3`** (HEAD: Q → 2 breaths → plain → her clip, ~20 s) — goes
    hand-in-hand with #3's ear-session.

### C-assembly & beats (after #7)
14. **C-walk doc per section**: texture = ledger rows marked promote-but-not-B after the
    sweep + the 8 surviving C-clips; ordered by her sūtra order; exclusions per FORMULA
    rule 3 (chant/mic/logistics already C-marked in ledger).
15. **Three-layer beats** (0→A→B→C) + bell spec (880 Hz section / 220 Hz layer) —
    port from vatula FORMULA §VIDEO RUN-ORDER; beats must re-land the seed each layer.

### Hygiene & cross-repo (anytime, small)
16. **After every unit/grade change**: `tools/sync_counts.py` then the three gates (#2).
    Keep `FILEMAP.md` current the same day you add anything.
17. **Export units to essay-corpus** (prx0r/essay-corpus `corpus.db`, id prefix
    `shivasutras:`) — only after #3–#5 lock the material (their §next-loads rule).
18. **BHU-Tantraloka ownership**: one owner line — vatula `CUTTING-FORMULA` holds the
    cut plan, tantraessays holds the 15-transcript coverage; only one repo may build it.
19. **Port `coverage_measure` + ledger to vatulanatha** if owner wants pass-1 parity
    there (it has C-MARKS but no ledger; FUTURE-TARGETS follow-up).
20. **analayo-nibbana loose ends** (separate repo): finish lectures 28/30/32/33
    (`ds-mp3/lec-*.mp3` → `tools/local_transcribe.py` → `gen_plan.py` → seam-audit),
    then close the `audio_ok` gaps in the 6 manifests; **no render without owner**.
