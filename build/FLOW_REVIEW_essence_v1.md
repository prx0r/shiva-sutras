# FLOW REVIEW — essence v1 (75 cues, 311s) — 2026-10-26. Verdict: FLOW (3 ear FLAGs).

Machine half: `tools/flow_lint.py` clean (longest run c2 46s flagged,
6 joint types, repetition all structural, 2 XLs placed). Evidence below
is cue #s + timecodes from `build/TRACK_F_PRODUCTION.md`.

## Q1 completion (per beat)
- c1: Q "What is consciousness?" (cue 9) → "it means universal
  consciousness … not something you are doing, it is something which is
  there" (cue 16, 00:32). PASS (S1-fusion noted in §8j — quiet work, gap not widened).
- c2: Q "What keeps consciousness from being realised?" (cue 18) →
  "it is an incomplete knowledge" (cue 25, t=0080.71 + ~40s in-clip). PASS.
- c3: Q "How does realisation happen?" (cue 27) → "it is not made by any
  human effort" (cue 33). PASS with apophatic ruling (§8j: positive
  mechanism consciously in B).
- c4: Q "What does realisation do to experience?" (cue 36) → "he purifies
  and fills it with supreme bliss" (cue 43). PASS (T opaque — air, not words, is the fix; 3s breath + 1s beat applied).
- c5: Q "What does the mind have to do with consciousness?" (cue 51) →
  "thus becomes that mantra itself" (cue 57). PASS, strongest pair.
- c6: Q "What happens after realisation?" (cue 66) → "where the self takes
  delight with the intention of exhibiting the world drama" (cue 72).
  PASS (§8j follow-up: audition dropped, stage answers "what happens").

## Q2 chant→T landing
All six land ≤4 s after chant end (cues 12, 21, 30, 39, 54, 69). PASS.

## Q3 longest run
c2 Baumer 46.0s (cue 25) — structural justification recorded: the
obstacle gets weight; deepest point = longest dwell. c4 28.0s (cue 43)
— imagery-rich, holds. Both FLAGged for ear (split points unmarked
until heard). No unowned long runs. SOFT.

## Q4 deictics
- c2 "they are not inherent in the soul" (cue 25, t=0080.71 + ~5s in-clip): antecedent
  (mala/impurities) NOT in-clip — carried by card context ("Knowledge is
  bondage"). SOFT → FLAG: ear-check landing; fallback = extend cut head
  ~5s to the antecedent noun.
- c3 "That's why it is for bhavika, it is not made" (cue 33): "it" =
  the arising, card-primed ("upsurge"). SOFT, same fallback pattern.
- c1 "it means universal consciousness" (cue 16): bound in-sentence. OK.
- c4/c5/c6 openers self-contained ("this heroic yogi", "the mind of the
  devotee", "the place where the self"). OK.
- Sharma intros: "this section" anchored by preceding sentence. OK.
- TTS Q/T/P lines: pronoun-free. OK.

## Q5 joints
Sharma→TTS, TTS→TTS, TTS→Sharma, TTS→Baumer, Baumer→TTS,
Baumer→Sharma — all six typed. Mitigations: 2.5/3.0s breaths, 1.2s gap
+ 0.15s fades + room-tone-at-ship, motto bells. No unmitigated SOFT.
PASS (ear verifies the two robot→human joints).

## Q6 repetition
bell/gap/water/breath/tbeat recur at ritual intervals only. Q/T/P rows
each heard once. PASS — no accidental repetition.

## Q7 pauses
think (breath 2.5 / breath3 3.0 for long Qs), land (tbeat 1.0 after
every T), reset (gap 1.2, water 2.5), settle XL 5.0 open, terminal XL
6.0 close. XLs at weight points only. PASS.

## Q8 heads/tails
- S1 head frames 4 Light-1 seeds: OK. FLAG: intro claims "22 sutras",
  essence plays 4 — trim intro to the section name for the essence cut
  or accept as section framing (ear call).
- S2/S3 heads frame their seeds: OK. Closers: water + payoff; terminal
  stills 6s, no climax. PASS.

## Q9 G12
c2 (46s): exception recorded (§8j). c4 (28s): exception recorded.
No silent breaches. PASS.

## Q10 cold listener
"But what DOES it (realisation)?" after c3 → answered by c4's bliss
(cue 43). "Who is 'they'?" after c2 open → §Q4 FLAG. Otherwise asks
are met by next beats. SOFT (one FLAG carried).

## Whole-review verdict: FLOW — 3 ear FLAGs (c2 "they" antecedent,
c4/c2 split points, S1-head 22-count trim). NO-FLOW items: none.

## Pass log (machine ears, `tools/listen.py`)
- Pass 1 (qa): FLOW with issues — flagged TTS-Sanskrit heads (fixed:
  human chant cards), c1 hard-concat seam (fixed: 0.4s crossfades),
  c2 "they" (fixed: antecedent cut in), long-cell pacing (noted).
- Pass 2 (targeted): confirmed heads human+clean; re-fctched c1 seam
  (fixed as above) and c2 "they" (model inferred the WRONG antecedent —
  proof the card did not carry it; fixed as above); verdict NO-FLOW
  pending those two fixes.
- Pass 3 (qa, post-fix): all-CLEAN FLOW — discounted as verification
  (confabulated labels/timecodes; contradicts its own pass-2 specifics).
  Standing: fixes hold STRUCTURALLY (adjacent antecedent, crossfade
  graph, human chant); remaining items are human-ear calls (the 3 FLAGs).

## Pass 2 — deterministic (tools, no ears)
- `tools/tts_scan.py`: 24 TTS lines vs 74-token Sanskrit stoplist — CLEAN (only `bhairava`, covered by TTS_SAY spoken form).
- `tools/deictic_check.py` vs transcript text:
  - c1 "it" (cue 16): BOUND — antecedent "consciousness / not individual consciousness" 10–14s earlier in-clip breath + card priming on all four rows (Q/chant/T/P). Flag cleared structurally.
  - c2 "they" (cue 25): BOUND — "these Mala's" placed 1 cut earlier by the antecedent edit (was 30s away in source, now adjacent in the cut). Structural fix verified in plan, not by listening.
  - c3 "that/it" (cue 33): BOUND — grace neighborhood ([1200] will-of-God/grace lines) + card priming. Supports the apophatic ruling: the positive agent is adjacent, not absent.
  - c4 "this" (cue 43): BOUND in-sentence ("from the chandra gyana this is also a tantra" — antecedent named). Abrupt-open note remains (quotative frame cut) but it is completeness, not reference, that was at stake. G12 flag stands on length only.
  - c5/c6: no pronouns in openers. Clean.
  - c6 "what" is interrogative (self-contained Q&A). Clean.
- Repetition = T+P gospel pairs + bells/pads only (structural, intended). Order = Q precedes answer in every beat (sheet-verified); head cards state answers first BY DESIGN (seed planted, question re-opens — recorded, not a flaw).
- Remaining ear-only items: acoustic seam quality (c1/c2 crossfades), drag feel (c2 42s, c4 28s), TTS naturalness, confusion. Everything else is now asserted in code or text.
