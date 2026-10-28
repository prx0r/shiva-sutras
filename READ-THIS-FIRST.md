# READ THIS FIRST — or you will repeat 2026-10-28 (a full wasted day)

An agent burned an entire day here building the WRONG track with chant in the
WRONG place, shipped unlistened masters to the owner twice, and only found the
governing rules after being yelled at. Everything below is load-bearing. It is
deliberately insultingly explicit so no future agent has to be told twice.

## 0. Which track are you on? ASK. Do not infer it from file names.
- This repo builds TWO compilations that must never be blended (BUILD_ENGINE.md):
  **Standard** (fidelity: 77 sūtras in order, Lakshmanjoo's voice, 0/A/B/C layers,
  Sharma chant run as closing coda) and **Custom** (remix: six spine questions,
  essay-0 seed, Baumer's voice).
- "Essay 0" and "Essay A" are CUSTOM artifacts. "0/A/B layers" are STANDARD
  artifacts. If a request says "essay", confirm which track before touching anything.
- On 2026-10-28 the standing mandate became **STANDARD ONLY**. If no mandate file
  newer than this one exists, ASK THE OWNER which track before building anything.
  Building the wrong track for a day is worse than asking one question.

## 1. Chant placement law (the rule that was violated all day)
- **Standard:** per-verse Sanskrit is Lakshmanjoo's own voicing (B1). Sharma appears
  exactly twice: as B1 fallback where his tape garbles, and as the complete
  77-sūtra run AFTER THE LAST VERSE (coda). Source: `process/10-FORMAL-CHANT.md`
  §6 ("Sharma's complete run after the last verse"), `process/STANDARD.md` coda.
- **Custom/essays:** NO chant at all. Source: vatulanatha `FORMULA.md` rule 3
  ("chant runs ... stay in source, never in essay") — adopted as our rule.
- What the agent did wrong: put Sharma seed chants after every Custom question
  (Q → chant → T), because `custom/BEATS.md` + the existing `audio/gen/custom/l0_cuts/` intermediates
  already contained them and he never cross-checked the two chant rules above.
  The beat grammar is NOT the whole law. Content rules live across documents.
- Corollary (M39): no clip may promise what the build doesn't deliver within earshot
  ("So now I chant these sivsutras" followed by talk, not chant).

## 2. Never ship unlistened audio (AXIOM 10 already said this; it was ignored)
- 2026-10-28 v1 masters went to the owner with ZERO listen passes. Owner verdict:
  terrible — flat synth bell, chant-promise with no chant, ~20 mid-sentence cuts.
- Rule: no master leaves this repo without (a) sheet==master assert, (b) per-section
  joints pass, (c) qa sample, (d) chantcheck preset. The owner is the final ear,
  but NOTHING reaches the owner that the agent hasn't heard first.

## 3. Transcript timestamps are not speech times (M40)
- YT captions stamp appearance, not speech (±2–4s caption lag, varies by file).
  `locate()` interpolates at 2.7 wps — an estimate, never a cut point.
- Cut on MEASURED word boundaries (whisper word_timestamps) anchored to the
  transcript sentence (transcript says WHAT, audio says WHEN). Verify every
  window against audio before trusting it.

## 4. Your tools lie to you in specific, documented ways
- **Iterative tools must prove convergence.** `tools/align_cuts.py` re-derived its
  search region from its own output and drifted every run (M41) — 45 changed, then
  18 more, never settling. Fixed by anchoring to immutable inputs (unit windows).
  Rule: re-run any iterative tool immediately; if output moves, the tool is broken,
  not "refining". DO NOT USE `align_cuts.py` as-is (kept for history only).
- **One model verdict = one hint, not evidence.** The same clip got opposite
  verdicts (CLEAN then CUT) on identical bytes across runs. Corroborate every CUT
  with transcript + whisper before touching a window; a lone model claim changes
  nothing. When transcript and whisper agree a clip is complete, the model is
  overruled — record it and move on instead of re-running the model.
- **Stale artifacts ship as new.** `int()`-truncated cut filenames collide on
  sub-second edits: the builder skipped re-cutting and validated the OLD audio
  as new. After ANY sub-second manifest edit, delete the cut file to force a
  re-cut, then verify the file's mtime/content matches the edit.
- **Check the file before the theory.** Thirty minutes were spent "proving" a
  transcript-vs-audio mismatch using the WRONG mp3 (ss1 content probed in ss4's
  file). Verify sess→mp3 via the MP3 map FIRST; theorize second.

## 5. Stop conditions (against validation theater)
- Fixed verification budget per clip/section: structural gates → ONE model pass →
  owner ear. When rounds stop finding new defect CLASSES and only move edges by
  milliseconds, SHIP with the residuals logged as ear-checks. The owner listening
  once beats the agent listening ten times.
- Never re-run a full sweep "to be sure" after a no-change rebuild. Gates
  (`verify.sh`, `qa_std.py`, sheet asserts) are the repeatable check; model
  passes are hunts, not gates.

## 6. Where things stand (2026-10-28 evening)
- Standard: 77/77 0+A+B manifested + built, qa_std zero FAIL, B1b lines in,
  template repaired, coda cut, pilot ch1 + full B walk assemble. NOT DONE:
  C layer for 65 verses, full-walk QA + owner ear, print-verify, coverage decision.
- Custom masters on disk/R2 are DRAFTS built against violated rules. Do not ship,
  do not demo, do not build on them without the owner's explicit re-activation.
- Open flagged items live in the handover (HANDOVER-2026-10-28.md), not in chat.
