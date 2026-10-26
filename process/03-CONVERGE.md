# 03 — CONVERGE. Measured threads × A-density → sections-as-questions.

## Two dissections, one elephant
1. Keyword spread per session (measured, not assigned): which threads run
   the whole corpus vs die halfway. A running question can't vanish
   mid-series — kill it early and log why.
2. A-density per topic (independent): what the best clips cluster around.
Both must land on the same shape. If they disagree, trust neither —
re-read, don't average.

## The questions (`excavations/SPINE.md`, `tools/validate_questions.py`)
Sections ARE questions, never slot-labels. Each must: be interrogative,
≤9 words, name an explicit content noun, carry the corpus anchor (here:
varies on 1.1's topic), hold no pronouns, and NEVER contain the answer's
content-word (read it, then read the answer — re-ask if the question
already gave it away, M16). Prefer speakable, owner-tested forms over
maximally packed ones (M15). Name the right object — the event, not the
ground (M14). Gate G0: all-pass on the canonical set (spine + essay-0
alternate); the gate runs on the set it ships, updated in the same commit
(M7). Questions chain as ONE enquiry (each follows the previous
answer-space); essay-0's response must OPEN it.

## Assign (`tools/s2_cluster.py` → `excavations/SPINE_ASSIGN.tsv`)
Keyword-score every unit's transcript window + quote; ties/zeroes/thin
fall back to the session primary; content-verdict overrides logged in
the tool (metric flags candidates, reading gives the verdict). Blind
clustering is NOT run (it produces blobs/dust); profiles-first is the
method that works. Thin sections stay thin — never padded.
**REPORT ONLY after pass-1 rows exist** — `--apply` rewrites the file
and erases manual fallbacks. Gate: totals reconcile (units == rows),
A-buckets recorded.

## Fit-check + gospel (in SPINE.md)
Per-section A-pool verdicts (strong / textbook / wobbles with levers),
unit→verse feed rules (section range is default, explicit exceptions
listed), the four-layer gospel (SANSKRIT → TRANSLATION → PLAIN → ARCHIVE
VOICE, order fixed, rows 1–2 ride as the card), and the build rules
(essay-0 lock → A → B hold-up → C walk → beats → render). Her order is
the sort key INSIDE sections, never across — wobbles flagged, homes
never moved to flatter a question (levers at ear: promote or re-ask).
