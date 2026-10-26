# C-MARKS — why spans are NOT units (coverage pass)

One row per uncovered span dispositioned during the full read-pass (worst-served-first).
Schema: `file · lines · timespan · words · disposition · reason`
disposition = C-mark (excluded, reason) | B-pending | C-pending | promote→unit-uid
Reason vocabulary: off-spine · logistics · repetitive · thin-aside · participant-QA ·
wrong-register · duplicate-of-unit · audio-bad(unchecked) · overlap-covered.

Ledger: `excavations/COVERAGE_LEDGER.tsv` (header: file, lines, t1, t2, words, disp, uid, note).
Pass order & progress: see COVERAGE.md. verify_units must stay 0-fail after any promote.

## Pass-1: day5_session_ii (= ss11, worst file at 5.0% span) — DONE 2026-10-25
18 promotes (ss11-09..26; 4 A: autumn-clouds / 2.1-double-gloss / citta-organ / udyamo-gloss)
+ 33 C-dispositions. Session = the cittam-mantrah (2.1) exposition, previously at 8 units.
C-reasons used: logistics (music/walk/wrap), off-spine (Vāmā-devī cosmology, śabtarāśi
lexicon, Mālinīvijaya verse, shaktopaya structure, aham language-game), repetitive
(lake/identity/autumn reprises), dup-of-unit, thin lead-ins, ASR-garbled (EAR check),
noise. Full sub-span rows: COVERAGE_LEDGER.tsv (file=shiva_sutras_day_5_session_ii.txt).
Autumn-reprise C-note: the image recurs 3x by her own word ("comes again and again") —
recurrence recorded, unit kept single.

## Pass-1: day6_session_ii (= ss13, 7.2% span) — DONE 2026-10-25
21 promotes (ss13-11..31; 3 A: jīvanmukta-play / actor-being / līlā-closer) + 2 window fixes
(ss13-03, ss13-05 timestamps sat OUTSIDE their own quote lines — caught by gap-walk, fixed,
verify 225/0). Session = the 3.x drama exposition; previously 10 units at unit-markers only.
C-reasons: commentarial (section-structure, rasa-background), technical (prāṇa-anatomy,
drama-terms, karaṇa-temple, puryaṣṭaka), repetitive (samādhi/ranga/veil reprises), dup
(two-levels verse), thin lead-ins, logistics (time-over, temple pointer), noise.

## Pass-1: day3_session_i (= ss5, 8.4% span, biggest word-gap 7k) — DONE 2026-10-25
15 promotes (ss5-16..30; 1 A: freedom-is-challenging/armor-psychology) + 1 duplicate fix
(M19: ss5-06 was an EXACT re-entry of ss5-15 — removed, clusters/CATALOGUE re-pointed) +
1 heading dedup (double "## Reuse clusters"). Session = kañchūka/mala analysis + language-
mātṛkā half; C-reasons: commentarial (verses/catalogues), technical (tatwa/śakti-taxonomy),
dup (transform-law/mandala/four-levels reprises), thin leads, logistics (Q&A/walk/DVD).
Cross-session ledger note: mandala nothing-left-out here = ss13-12 (same teaching, 2 voices).

## Pass-1: day4_session_i (= ss7, 9.7% span) — DONE 2026-10-25
21 promotes (ss7-20..40; 2 A: turīyatīta-pervades-activity + full card-verse translation)
+ 2 window fixes (ss7-05 quote outside window; ss7-16 window sat in a caption DEAD-ZONE
while quote lived at 1:09:35 — audio would have cut the wrong minute at build). Session =
S4 home (tṛtayabhokta/States/Wonder/Icchā) + icchā-spontaneity block. C-reasons: dup
(vikalpa/moon/sambhava restatements), thin leads, technical (yogic-taxonomy, dream-runs,
will-translation), off-spine (Kālī-verse, mythology), logistics (notes/wrap).
Ledger note: Uma-Kālidāsa myth whole-block C (narration depth, off the six questions).

## Pass-1: day4_session_ii_part_1 (= ss8, 9.9% span) — DONE 2026-10-25
8 promotes (ss8-08..15, all B: compassion-descent, individual-void, identification-
hindrance, spontaneous-vs-practice, open-eyes samadhi, ananya-citta, senses-included,
god-to-universal transformation). Session = drik-sharira/heart-sutra block. C-reasons:
orientation-table (whole upaya-correspondence scheme), leads into covered units, dup
(heart-glosses/bhavanā), ASR-broken all-bodies list noted for EAR, logistics (walk-plan).

## Pass-1: day4_session_ii_part_ii (= ss9, 17.5% span) — DONE 2026-10-25
2 promotes (ss9-06 interconnectedness-consciousness, ss9-07 not-a-substance) + 1 micro-fix
(ss9-02 window ended 1s before its own quote-line "that a threshold"). Compassion-thesis
L14-20 logged dup-adjacent: inside ss9-01 window (window⊃quote). Q&A half (real-question)
C as question-half; Sarnath-survey/recaps C thin; covered rows recorded for audit.

## Pass-1: day2_introduction_iii (= ss3, 11.1% span, biggest word-file 10.8k) — DONE 2026-10-25
3 promotes (ss3-19..21, all B: Raja-manifesto quote, VB-100 conquer-becoming, nonduality-
applied-creed). Teaching-half was ALREADY well-unitd (18 units); audit caught several
"planned" clips as inside existing windows (silence, labels, is-not-doing, innermost,
freedom-distinctive, artificial) — recorded dup-adjacent in ledger, none force-overlapped.
Integration: intros-block (L134-1102, 4.3k+1.6k words of participant voices) = 2 giant
C-rows (participant-vote off-unit-policy); book-logistics/editions already covered ss3-08 (unit since removed to ledger — M21 rule, 2026-10-26).
Note: ss3-09 window extends past quote to the integrative-gloss — flagged for future
quote-extension, not overlapped.

## Pass-1: day1_introduction_i (= ss1, 11.7% span) — DONE 2026-10-25
5 promotes (ss1-27..31, all B: Sanderson-projects-plural-reality [flagged by her as the
first-sutra preview], need-a-guru-to-catch-essence, anupaya nothing-to-do already-given,
transcend-then-expand kula-model, fourth-state-must-pervade). 26 existing units covered
the doctrinal spine; C-run: institution-welcome, Kashmir-history surveys, Vasugupta/rock
LEGEND narrative (doctrine kept in ss1-16/17), lineage bios, Sanderson-77 scholarly,
brevity-implications catalogue, kārikā-form, upaya-caveats.

## Pass-1: day1_introduction_ii (= ss2, 14.9% span) — DONE 2026-10-25
0 promotes — every doctrinal clip already unit'd (ss2-01..06 = bhairavaita/turyatita/
brahman-shakti/maya-real/excludes-nothing/mutual-dep); ss2-07 = safety-net C-unit.
8 gaps ledgered: participant question-halves (Veda-comparison, dualistic-tools, safety-net),
dup-tails (multiplicity, abstract-to-experience = ss7-30-family), thin leads,
meditation-program logistics. PASS WITH NO UNITS ADDED — ledger-only file.

## Pass-1: day2_session_i (= ss4, 16.8% span) — DONE 2026-10-25
0 promotes — all 22 doctrinal clips already unitd (ss4-01..22 incl. imagination-real,
light, consumerism, flower, own-freedom-obstacle, guru-run). M20 logged: file TAIL
(L810-991) duplicates day6_i content (same stamps) — ledgered as cross-file-dup,
parallel units (ss4-21/22 vs ss12-09/10) kept, no double-claim created.

## Pass-1: day3_session_ii (= ss6, 31.7% span — best-covered file) — DONE 2026-10-25
7 promotes (ss6-20..26, all B: enlightenment-happens-yet-devotion, thoughts-enmesh,
horse-training-but-sudden, same-state-continues-outside, senses-divine-phases, not-even-
negations, fire-burns-multiplicity) + 1 window FIX: ss6-18 covered [47:54-1:01:04] of
UNRELATED content while its quote lived at 1:07:00 — corrected to [1:07:00-1:07:23]
(exposes the 13-min region honestly into the ledger). C-runs: bhairava-etymology,
ut/yam-roots, spatial-symbolism, MVUT-setup, krama-background, metaphors-recap,
devours-verse-dup (ss12-14), kala-devour.

## Pass-1: dl1 (Dyczkowski introduction, 19 min — NON-BAUMER second voice) — DONE 2026-10-25
3 promotes (dl1-06..08, all B: same-vision-of-Oneness, supreme-grace=that-insight,
one-consciousness-even-transgressive) + 1 window FIX (dl1-05 quote at [10:57] vs window
[11:53-17:50] — narrowed to the quote line). gap_report tool fixed to SESS-map (dl1.md
Source-line points at audio/, not text/ — tool silently skipped dl1 before).
NOTE: commit 0db32e7 landed with a premature message (script crash after gap_report-fix)
— the actual units/ledger landed in the follow-up commit. C-runs: legend-retelling,
sutra-thread dup, Sanskrit-verse walks, Spanda-relation, ASR-noise (L44-46/50-51/69-72),
logistics. 100% of 99 cues ledgered.
