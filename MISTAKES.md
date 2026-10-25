# MISTAKES — everything we got wrong, with cause + fix. Read before touching the pipeline.

(Format inherited from analayo/process/MISTAKES.md — owner standing rule:
**add to this list as you go.**)

## Slop (writing things that aren't from the source)
- **M1. Misremembered quotes.** First draft of ss3–ss13 contained 14 audit fails
  written from memory instead of re-read (incl. wrong-session duplicates: ss7-12/13
  duplicated ss6 material, ss8-08 belonged to ss7, ss10-02 belonged to ss5 — the
  duplicates were deleted/moved, the rest rebuilt from grep-verified spans).
  Caught by `tools/verify_units.py`. **Rule: never type a quote I haven't just
  re-read in the file this session; grep it first, verifier second.**
- **M2. Duplicate uid.** Renumbering left the bliss unit as a second `ss7-17`
  (colliding with Kena-Umā). Fixed → `ss7-19`. **Rule: uid-uniqueness is asserted
  at write; count headers after any renumber.**
- **M3. Invented essay-0 stack format.** Owner-caught (2nd correction): I emitted a
  self-designed S/T/P/A stack, paired the sharpened question with a master-answering
  stack, and gave the six spine answers audio-only (no text, no plain).
  Correct cell, from vatula `build/essay0/MICRO-SESSION.md` + formula steps 2–4:
  **SANSKRIT (the source's own answer, sūtra-level) → TRANSLATION (existing exact
  rendering; lecturer > critical > gloss, never composed) → PLAIN (mechanical,
  key-vetted) → BÄUMER (her interpretation that completes the question)** — and EVERY
  spine question gets this cell, not just the opener. Fixed in `build/ESSAY0_OUTPUT.md`.
- **M4. Right answer, wrong order (process).** Essay-0 was built before segmentation;
  owner caught it. S2→S3 (cluster→convergence→SPINE) runs first; essay-0 is tested
  against the REAL sections afterwards. Logged in PROCESS_NOTES §6.

## Audit/check bugs (ours, not the data's)
- **M5. Silent pass.** An edit to `verify_units.py` deleted its parse loop →
  "units: 0 fails: 0" exit 0. A check that can't find failures is worse than one
  that finds too many. **Rule: always eyeball the units-count line.**
- **M6. One-sided normalization (family, now 4x across projects).** Quotes were
  unpunctuated while YT/CF transcripts keep punctuation → false "quote not found".
  Fix: strip whitespace+punctuation+`[HH:MM:SS]`+`[Music]` tokens on BOTH sides.
  (dyczkowski's verifier stayed whitespace-only because srt matched its quotes;
  the norm must match the source's format, never be copied blindly.)
- **M7. Stale gate input.** Committed a "G0 PASS" message while `validate_questions.py`
  still held the old 7-question set (2 designed fails) → next run printed 5/7 red.
  **Rule: the gate runs on the canonical set; update the set in the same commit.**
- **M8. CF temp collision + heredoc patchers.** Two Cloudflare jobs shared
  `/tmp/opencode/cfseg_ss.mp3` (second crashed mid-run → serial rerun with PID-unique
  temps); large heredoc patch scripts got OOM-killed mid-write by the harness
  (no partial writes — asserts saved us). **Rule: unique temp per process; write
  patchers to files, not heredocs; re-run the target after any failed patch.**

## Metric vs reading (their M6, reproduced then prevented)
- **M9. Glue terms in v1 profiles.** Pan-corpus counts (tradition 120, means 216,
  will 193, body 126, bare mantra 122…) reproduced vatula's documented failure
  ("nonduality glues → 1×51u blob") — caught early by a zero/pan-count audit of every
  profile term against the corpus, before the final assign. Profiles rewritten to
  distinctive doctrine terms; **48 content-verdict overrides** logged in
  `tools/s2_cluster.py` (metric flags candidates, reading gives the verdict).
