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
