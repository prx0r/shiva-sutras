# COVERAGE — how much of Baumer is missing, and how it gets included

Measured 2026-10-25 · tool: `tools/coverage_measure.py` (rerun after every grading pass)
· method: merged unit timestamp-spans vs timestamped transcript lines.

## The truth (updated numbers — supersedes §8b's 13%/5,824-word estimate)

| metric | covered | total | % |
|---|---|---|---|
| audio span | 106 min | 860 min | **12.3%** |
| transcript lines | 2,418 | 13,515 | 17.9% |
| words (on covered lines) | 12,418 | 73,296 | **16.9%** |

(Baumer's 13 files; dl1 separate: 17 min, 5/99 cues = 5%. Both voices together = 878 min.)

**Missing: ~754 minutes of Baumer audio, ~60,900 words (plus 15 min of dl1) — but it is NOT off-topic.** Spine-anchor
scan of uncovered lines: S1 421 · S2 238 · S3 135 · S4 148 · S5 491 · S6 149 uncovered
lines that speak directly to our six questions (anchor coverage 13–26% per section —
**S4 thinnest at 13%**, S3 best at 26%).

Worst-served files (work order): day5_session_ii 5.0% · day6_session_ii 7.2% ·
day3_session_i 8.4% · day4_session_i 9.7% · day4_ii_part_1 9.9% · day5_session_i 9.9%
· dl1 (Dyczkowski, 99 cues) only 5/99 = 5%.

## How "as much as possible" is included (without breaking any law)

Material can enter the project through exactly three channels:

1. **A/B promotion (selection-bias fix).** Current 71A were chosen from a 16% sample —
   the best clips of the other 84% may beat our weakest links. Rule holds: a new unit
   enters A/B only by beating the section's current weakest (B ≤ A×1.6–2; no superset
   ever ships). Ceiling ≈ ship ~50–75 min total, never 878.
2. **C-walk (the volume channel).** Everything else flows through the text-axis
   walkthrough in her order — inclusion without shipping clips. The ledger records why
   each span is A / B / C / C-mark.
3. **Ledger + anchors (the reach channel).** Every span dispositioned once; future
   builds (beats, full book) can pull any span by sūtra-range or anchor without
   re-walking.

## THE PASS (one pass serves all three §8e-1 options)

Read the transcripts session-by-session (TEXT, not audio — 75k words ≈ a long day),
in the worst-served-first order above, dispositioning EVERY uncovered line:
- **promote** → draft unit (grade honest, verify_units must stay 0-fail)
- **C-mark** → reason in `C-MARKS.md` (off-spine, repetitive, thin, wrong-register)
- **B/C ledger** → one-line disposition per span in `COVERAGE_LEDGER.tsv`

Done when: `coverage_measure.py` reports every file with a ledger row covering 100% of
lines (span% may stay ~12% — that is selection, not blindness), and anchors scanned.
This IS the coverage-standard decision's implementation for option (a)+(c); option (b)
full line-units would re-write this as dyczkowski-style per-line files — owner decides.
