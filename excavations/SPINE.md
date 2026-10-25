# SPINE — six sections, each IS a question (S2+S3, 2026-10-25; preview→converged)

**Method (ported from vatulanatha 17 + analayo 02):** designed keyword profiles per
section → keyword-score every unit's ±5min transcript window (+ its own quote) →
ties/zeroes/thin(margin≤2 & score<12) fall back to the session's primary section →
**human verdict pass** for content>metric conflicts (48 overrides, all logged in
`tools/s2_cluster.py` OVER dict) → totals reconcile 180/180 (`excavations/SPINE_ASSIGN.tsv`).
Blind agglomerative clustering was NOT run (vatula attempt-log: it produces blobs/dust);
profiles-first is the method that works.

**Laws inherited:** sections are questions, never slot-labels (owner) · standalone-clarity
(no insider coinage, stranger parses cold) · question-chained as ONE enquiry ·
essay-0's response must OPEN the enquiry · her sūtra order = sort key INSIDE sections
(never reorders across) · thin sections stay thin · A ⊂ B ⊂ C collated under these.

## Convergence (two dissections, one elephant)
- Unit distribution: S1 71 · S2 30 · S3 36 · S4 39 · S5 68 · S6 43 (total 287 after pass-1; ss5-02 moved to S5 guru-means).
- Independent A-buckets:  S1 24 · S2 7 · S3 9 · S4 12 · S5 18 · S6 11 (total 81; pass-1 grows as files are read).
- Both rank S1 first and S5 second; S3 is thinnest in both — accepted, not padded.
  S6 vs S2/S4 swap mid-table is the only disagreement (cosmetic).

## The questions (all G0 PASS — tools/validate_questions.py, 7/7 incl. essay-0)

1. **What is consciousness?** — the thing (master — S1)
2. **What keeps consciousness from being realised?** — the obstacle (bondage — S2)
3. **How does realisation happen?** — the arrival (the upsurge — S3)
4. **What does realisation do to experience?** — the change (the yogi's states — S4)
5. **What does the mind have to do with consciousness?** — the mechanism (mantra — S5)
6. **What happens after realisation?** — the after (life-in-the-world — S6)

Fundamental progression (open questions, answers withheld): is → what keeps it from
being realised → how it happens → what it does to experience → how mind engages →
what happens after. Each question names the ASK, never the answer. Each follows the previous
answer-space; none closes the enquiry.

---

## S1. What is consciousness? — the thing · sūtras 1.1 (+intro/history) · 62 units (24A) · includes SECOND VOICE (dl1)
**Anchor (her words):** `ss3-10` — "consciousness is definitely not individual
consciousness … it means universal consciousness … consciousness is not something
you are doing it is something which is there"
**Journey:** program frame (ss1-01…09 — Day-1 units landed here as lead-in) →
the rock & revelation (ss1-16…19) → sūtra-form + the two real names (ss1-21, ss1-25/26) →
Vedānta-challenge Q&A (ss2-01…07) → Day-2 definitions (ss3-07…16 recognition/ātman/freedom) →
Day-2-session-I core (ss4-01…10: organ, mokṣa-unveiling, prakāśa, shadow-jump) →
fluidity closes (ss5-01, ss6-06, ss7-01, ss8-01, ss9-03…05).
**A-anchors:** ss3-10, ss4-05, ss1-16, ss1-25, ss9-03, ss4-08, ss4-09, ss5-01.
**Note:** ss12-02 (recognition-as-reading) and ss13-01 (ātman-per-level) are verdict-here;
recognition-thick material belongs to the PH project — keep only as reading-method here.

## S2. What keeps consciousness from being realised? — the obstacle · sūtras 1.2–1.4 (+kañcuka/mātṛkā exegesis) · 19 units (6A)
**Anchor:** `ss4-12` (the shock: "jñānam bandhaḥ") · definitional: ss4-14 · Q asks WHAT keeps, not why-it-binds — "Mala, it is said, is nothing but Vajjana or ignorance of one's real nature"
**Journey:** the bridge-question (ss4-11 "how come we are not all liberated") →
the shock (ss4-12 jñānam bandhaḥ) → two readings (ss4-13) → mala-map (ss4-14…17:
not-knowing, incomplete, consumerism, veiling=freedom) → five acts (ss4-18/19) →
kañcuka section (ss5-02…08, ss5-12, ss5-15: kalā-fragment, armor, removal-rule,
malas-speaking) → threshold as māyā (ss9-02) · siddhi-veil strays: ss13-03.
**A-anchors:** ss4-12, ss4-14, ss4-17, ss5-15, ss5-04.

## S3. How does realisation happen? — the arrival · sūtra 1.5 (+1.6-adjacent suddenness, 2.5-svābhāvika echo) · 20 units (8A)
**Anchor:** `ss6-04` — "ud + yam … it is not a gradual rising step by steps it is a sudden upsurge"
**Journey:** jīvanmukti-question (ss6-01) → Zen/sudden frame (ss6-02) → viśrānti (ss6-03) →
the sūtra itself (ss6-04/05 uplifting=divine) → union (ss6-07/08) → "not by any human
effort" (ss12-03/04 + ss10-05/06 easy-way & result-not-ticket) → thought-free outcome
(ss6-10…15, ss6-14 gap) → siddhi-rejection family (ss10-10, ss7-18, ss13-03).
**A-anchors:** ss6-04, ss6-05, ss6-08, ss6-14, ss12-04, **ss12-16 (the WHY-line: not made by any human effort)**, ss10-05.
**Note:** siddhi-rejection deliberately clustered here (means: not-by-powers), not in S6.

## S4. What does realisation do to experience? — the change · sūtras 1.7–1.15 (states/turya/heart) · 24 units (10A)
**Anchor:** `ss7-06` — "the moonlit vīra … with the rays of his knowledge he purifies
and fills it with supreme bliss right from hell to shiva"
**Journey:** turya/state-machinery (ss2-02, ss7-04…09: 3×3, sleep-entry, awakening-degrees) →
wonder-test & icchā (ss7-14, ss7-16) → bliss-first (ss7-19) → Somananda non-triad (ss7-01) →
body-reading (ss8-02…05 this-universe-my-body, peacock/banyan) → heart-practice
(ss8-06/07 lotus) → kṣobha/agitation (ss12-13) · program strays: ss3-01 invocation, ss6-19.
**A-anchors:** ss7-05, ss7-06, ss7-07, ss7-14, ss7-16, ss8-02, ss8-06, ss8-07.

## S5. What does the mind have to do with consciousness? — the mechanism · sūtra 2.1 (+2.3 mantra, 2.6 guru) · 36 units (15A)
**Anchor:** `ss11-05` — "the mind of the devotee … acquires identity with the deity and
thus becomes that mantra itself"
**Journey:** MVUT practice-freedom (ss1-10…15: fix awareness, adopt whatever enables) →
thought-has-a-level (ss1-07, ss4-20 agitation-ceases) → the mantra-essence block
(ss11-02…08: Parā, subjects, aham, identity, failure-law) → words/mātṛkā (ss5-09…13:
condense-to-source, nyāsa, pause-between-syllables) → attention-rule (ss6-09) →
**guru-cluster (verdict-kept together):** ss3-03/04, ss4-21/22, ss6-11/18, ss10-07,
ss12-08/09/10 → khecari/vitarka (ss12-05, ss10-07) · program: ss11-08 selection-note.
**A-anchors:** ss11-03/05/06, ss10-01, ss10-08, ss12-08, ss1-11, ss5-11.

## S6. What happens after realisation? — the after · sūtras 3.1–3.16 (āṇava yoga, jīvanmukti, actor/stage) · 25 units (8A)
**Anchor:** `ss3-17` — "they come at the end because you cannot practice any ethics or
any yama niyama unless you have already reached a certain stage of spiritual experience"
**Journey:** ethics-after (ss3-17/18) → supportlessness + āsana-redefined (ss10-03/04) →
radiance/fruit (ss10-09, ss9-01 compassion) → offering-the-body (ss12-12, ss6-16/17
vyutthāna/return) → kula-mārga totality (ss12-07) → devour-both + tripti (ss12-14/15) →
powers-hidden / siddhis-as-fruit (ss12-10) → Day-6-session-II: āṇava-yoga & drama
(ss13-02…10: prāṇāyāma, pratyāhāra, samādhi-sameness, dancer, stage, spectators) ·
misc: ss8-04 strays-in.
**A-anchors:** ss3-17, ss6-16, ss10-03, ss12-07, ss12-12, ss12-14, ss13-05, ss13-09.

---

## C-homes (8 C units, each lives where it fell; never build from them)
ss1-01 (program lead-in) · ss1-24 (supermarket joke → S1 note) · ss2-07 (Buddhist Q → S1) ·
ss3-05 (participant nuclear-bomb color → S1) · ss5-14 (edition availability → S2) ·
ss6-19 (translation-brevity shop-talk → S4) · ss7-10 (€4000-book anecdote → S4) ·
ss11-08 (selection-rule note → S5).

## Essay-0 flow re-test against the real sections (step 5b, passed)
Seed = "consciousness IS — not something you're doing, it's what you are."
S1 gives it a name → S2 explains what hides it (veiling = the doing-you-do) →
S3 says you can't force it → S4 shows what it does once present → S5 shows how
mind/mantra engages it → S6 shows what it is finally free to do. Same seed,
six widenings — the essay performs unfoldment; no layer swaps the idea.

## THE FOUR-LAYER GOSPEL (canonical for ALL content — owner law, 2026-10-25)

Every question-cell, every beat, every clip-slot:
1. **SANSKRIT** — the text's own answer, sūtra-level, form verified in the held
   Aphorisms (`reference/aphorisms-of-siva-dyczkowski_clean.txt`), never composed.
2. **LITERAL TRANSLATION** — existing exact rendering, priority lecturer > Dyczkowski >
   gloss; never repaired (weak line = re-pick, not edit).
3. **PLAIN ENGLISH** — mechanical output of the key filter over row 2 ONLY; regenerate
   at pick; edits go in the KEY, never the row.
4. **ARCHIVE VOICE** — Baumer (ss1–13) or Dyczkowski (dl1) explaining it: Grade A,
   ≤25s, window in gold, completes the question. Voice may read (commentary it voices)
   or explain — analayo precedent: the archive voice carries both; rows 1–2 remain the
   card, row 4 never substitutes for them.
On screen: rows 1–2 ride together as the card (Sanskrit on top, translation beneath),
plain under that; in essay-0 the four rows are spoken/scaffolded in order.
Order is fixed: no plain before translation, no voice before plain, ever.

## Build rules (next stages, unchanged from process docs)
Essay-0 lock (draft in build/essay0_lock.json, owner ear pending) → SPINE build:
A = sections at speed (10–20m) · B = A + depth (hold-up test: deepens the seed,
B ≈ A×1.6–2) · C = A+B+texture (her order within sections; C-homes stay out) ·
beats = [SANSKRIT+TRANSLATION card → PLAIN (key) → ARCHIVE VOICE] with question→2-breath-pause before,
HUMAN voice owns questions · Sanskrit-first cards · quotas never padded (thin is honest).

## Voices + TEXT law
- **Voice 1 (primary archive):** Bäumer, 13 sessions (ss1–ss13).
- **Voice 2:** Dyczkowski, Introduction to the Śiva Sūtras (`dl1`, imported from
  tantraessays: srt→stamped text, 5 units, 2A/2B/1C, all assigned S1). Cross-voice
  pairs marked in `excavations/dl1.md` (rock↔Terma, 1.1-thesis A/A with ss3-10).
- **TEXT reference (main, per owner):** *The Aphorisms of Śiva* (Dyczkowski) —
  held at `reference/aphorisms-of-siva-dyczkowski_clean.txt` (gitignored), canonical
  source for every SANSKRIT + TRANSLATION row; Baumer sessions provide the
  interpretation layer; srt-stamps provide windows.

## Repro
```bash
python3 tools/s2_cluster.py --apply     # reassign + totals reconcile (180/180)
python3 tools/validate_questions.py     # 6 spine + essay0 questions, G0 gate
python3 tools/verify_units.py           # 180 units, 0 fails
awk -F'\t' 'NR>1{c[$4]++} END{for(k in c) print k,c[k]}' excavations/SPINE_ASSIGN.tsv   # 62/20/19/24/35/25
```

## Question ↔ content fit (static check vs the actual A-pools, 2026-10-25)

| S | question | A-pool verdict |
|---|---|---|
| 1 | What is consciousness? | **strong** — every definition/what-it's-not/how-known clip answers it; only 2 frame units sit wide (ss1-21 text-mode, dl1-03 stakes) and both are section-frame by design |
| 2 | What keeps consciousness from being realised? | **textbook** — all 6 are obstacle-explanations (divided knowing, mala=not-knowing, veiling, māyā-threshold, reversal, removal-rule) |
| 3 | How does realisation happen? | **textbook** — all 9 answer HOW (upsurge, uplift, union, gap, easy way, unmade, not-manufactured, + pass-1 card-gloss ss11-23 "it just happens and takes hold of us without our doings") + 1 boundary (siddhis-hidden = what it's NOT) |
| 4 | What does realisation do to experience? | **strong, 8/10** — enjoyment/radiance/wonder/bliss/body-read = direct answers; wobble: ss8-06/07 (heart-light, lotus-merge) are practice HOW-units — kept, since the heart is where the yogi's experience occurs (domain reading); flag for audio flow-read |
| 5 | What does the mind have to do with consciousness? | **strong (deepened pass-1)** — mantra-core + the 2.1 exposition itself now in-pool: card double-gloss (ss11-16), autumn-clouds mind-needs-consciousness (ss11-14), citta = organ of consciousness (ss11-18), mind becomes mantra-origin (ss11-17/25/26); guru cluster via guru-vaktra + guru-word-as-pure-thought (ss11-24); MVUT = mind-practices of attention |
| 6 | What happens after realisation? | **good, 6/8** — ethics-after, vyutthāna-return, sameness, stage, devour-fruit = the life-question; wobble: ss10-03/12-12 (āsana, offering) are path-techniques parked here by TEXT-ORDER (3.x = her sūtra sequence) — fractal law says keep; flag for flow-read |

**Beat feed (unit→sūtra):** section sūtra-range is the default locator for every unit
inside it; explicit exceptions only where a unit's own sūtra differs (dl1-04 → 1.1,
ss12-16 → 2.5-commentary, ss6-14 → Spanda-echo). At beat build, each A-unit resolves:
unit quote (audio window) + Aphorisms rows 1–2 for the section's sūtra + key-plain.

Wobbles are recorded, not patched: units stay in their sūtra-order homes; if the audio
flow-read shows a section sagging, the levers are (a) promote a B (e.g. S6's dancer
ss13-06) or (b) re-ask — never move text-order homes to cosmetically fit a question.
