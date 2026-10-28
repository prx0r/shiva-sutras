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

- **M10. Question bent to fit, not grown from the text (owner-caught).** S2 cell was
  "What hides consciousness?" + "Knowledge is bondage." — needed a bridge; the stack
  must read as ONE thought (formula step-6 stack-read). Root cause: I fixed the
  anchor-compliant question first and bent the answer to it, instead of letting the
  sūtra's answer shape the question (step-1 order: content-grounded from the TEXT).
  Fix: **"Why does knowledge bind consciousness?"** — 1.2 answers directly, and her
  ss4-15 line supplies the WHY (not-inherent-in-soul, incomplete knowledge).
  **Rule: run the completion test (does T read as the answer to Q, cold?) on every
  cell BEFORE locking any question.**

- **M11. Cell must meet the obvious counter (owner-caught).** After M10's fix the user
  still hit the wall: "isn't knowledge what frees?" A cell whose TRANSLATION invites the
  natural counter must meet it IN the cell (their step-1b: open-lean-in works both ways —
  the listener's counter is part of the enquiry). Fix: S2 resolution note with the three
  held loci (both-splits ss4-13 · 3.2 "(Empirical)" · 2.5 innate-arising).
  **Rule: before any cell ships, voice the strongest objection a cold listener has and
  check the cell answers it (or flag it for the section's B-depth).**

- **M12. Header-suffix broke two parsers.** Appending `[text:ss:direct]` after the
  `[A/B/C]` grade suffix made `verify_units` ("header missing grade" x5) and
  `s2_cluster` (grade read as C; then uid regex crashed on `### dl`) misparse.
  Fixed: both regexes accept the optional trailing text-tag; uid pattern covers
  `dl*`. **Rule: any header-format extension must be added to EVERY parser that
  reads headers, in the same commit.**
- **M13. mp3s swept into git + a deleted ref resurrected via packed-refs.** `git add -A`
  committed 242MB of audio (a 158MB file would have blocked any future push — GitHub
  100MB/file). Fix: `.gitignore` gains `audio/`, `git rm -r --cached`, then
  `filter-branch --index-filter` rewrite of the young unpushed history + aggressive gc.
  The loose `refs/original` deletion appeared to work but the ref had been *packed* by
  the intervening `git gc` — only `git update-ref -d refs/original/refs/heads/main`
  removed it from packed-refs (then .git: 243M → 1.3M, 0 reachable mp3s).
  **Rules: `audio/` is local-only forever (same as tantraessays); after filter-branch,
  verify with `git rev-list --objects --all | grep mp3` = 0, not with ls.**

- **M14. Category error in the S3 question object (owner-caught).** "Why can't
  CONSCIOUSNESS be forced?" — consciousness isn't the forceable thing (it just is);
  the event that can/can't be forced is the REALISATION of oneself as consciousness.
  Fixed: **"Why can't realisation of oneself as consciousness be forced?"** (9 words,
  G0 PASS) + new A-unit ss12-16 (the direct WHY-line "not made by any human effort")
  as the cell's audio; TEXT keeps udyama (WHAT), audio carries WHY.
  **Rule: interrogatives must name the right object — ask what the sūtra is actually
  about (the event), not the doctrine's subject (the ground).**

- **M15. Over-stuffed question object (owner review: "a bit wordy").** I maximally
  packed the S3 object ("realisation of oneself as consciousness", 9/9 gate words)
  when the owner's own sharpening-rule example already existed: **"Why can't you force
  realisation?"** — 6 words, speakable, object explicit, anchor carried by 'realisation'
  (now in G0 ANCHOR+CONTENT, justified: the corpus's S1-domain verb = realisation of
  consciousness). Also found in the same review: ss5-02 (guru-recognition story) was
  metric-filed under S2 but belongs to S5's guru-means cluster — moved (OVER).
  **Rule: gate-passing is not speakability; spoken questions ≤6-7 words, and prefer
  already-owner-tested forms over inventing longer ones.**

- **M16. Questions leaked their answers (owner, via the analayo Nibbāna set).** Mine
  confirmed ("Why does KNOWLEDGE bind…" pre-names the cause; "can't be FORCED"
  pre-states the verdict) where theirs WITHHOLD ("What perpetuates the process?").
  Opened all six: the thing → the obstacle → the arrival → the change → the mechanism
  → the after. Re-passed: G0 6/6, every completion-test still lands (TEXT answers what
  the question leaves open).
  **Rule: a spine question may name the ASK, never the answer's content-word — read it,
  then read the answer: if the question already contained the answer, re-ask.**
- **M17. Silent `.replace()` on doc edits.** The ESSAY0_OUTPUT enquiry-chain edit had no
  count-assert; the old string didn't match (wording had drifted) → stale chain survived
  TWO commits until the fresh-eyes read. Caught by manual read, not by any gate.
  **Rule: scripted doc edits assert `count == 1` (or print 0-miss) — a silent no-op is
  an unfixed file; and gates check tools, only eyes check prose.**

- **M18. Manual paste of quotes into SECTION_ARGUMENTS silently repaired two texts**
  (ss1-21: "they they…stand a rational" typed as "they…than a rational"; ss3-09: "of uh of"
  dropped without ellipsis). Caught 2026-10-25 by the 71/0 re-verify pass of the join audit.
  **Rule: after ANY quote is moved into a new document, re-run the verbatim verifier
  against transcripts — pass-verify protects the source file, not the copies.**
- **M19. Exact duplicate units ss5-06 / ss5-15** (identical quote, windows 30:29–30:46 vs
  30:31–30:50, grades B vs A) survived the original grading pass. Caught 2026-10-25 by the
  pass-1 window review of day3_session_i.
  **Rule: before appending a new unit, list the file's existing windows; and a
  duplicate-quote check belongs in verify_units (uid must be unique per quote).**
- **M20. Cross-file caption duplication: `day_2_session_i.txt` tail (L810-991, [49:54+])
  reproduces `day_6_session_i.txt` content with identical timestamps** (Jaideva-guru-run,
  Pañchastavī, vāktra). Either a caption-pipeline append-bug or genuine re-delivery;
  quotes verify in BOTH files (299/0) so no unit was harmed; units exist in parallel
  (ss4-21/22 vs ss12-09/10). Caught 2026-10-25 by the pass-1 read.
  **Rule: ledger such spans as cross-file-dup with pointer; NEVER create parallel units
  for the same claim twice (double-claim hazard).**
- **M21. C-grade used for a note, not a texture-clip (ss5-14 "archive pointer").**
  FORMULA rule: grades are ESSAY-LAYER membership — C = worth keeping as TEXTURE in the
  walk (anecdotes/asides/Q&A), not a storage-note. ss5-14's quote is pure logistics info
  (Lakshmanjoo SS audio-only, DVD) → demoted to ledger 2026-10-25; the other 8 C-units
  audited and retained (they play as texture). Caught by the structure review.
  **Rule: before grading C, ask "does this CLIP PLAY in the walk?" — if its reason to
  exist is a note, it belongs in C-MARKS/ledger, never in the units.**
- **M22. Essay-0 cell clip was grade B (ss4-15).** Grades = innermost essay-layer a clip
  enters (FORMULA) — essay-0 is innermost, so the six cell clips are A by law. Five were;
  ss4-15 sat at B and the HOLDUP sheet therefore listed it as a B-row while `ESSAY0_OUTPUT`
  labeled it "Grade A" — the sweep caught both claims disagreeing. **Promoted B→A**
  (2026-10-26, +1A → 82A). **Rule: when essay-0 cells are built or edited, assert every
  cell-uid's grade in the unit file == A; a cell clip at B/C is a structure bug, not a
  taste question.**
- **M23. Derived-file generator bugs surface at sweep time (4 found 2026-10-26).**
  (a) HOLDUP row for `ss4-03` rendered `?-?` + empty quote though the unit has a real
  window — repaired in-sheet. (b) Nested duplicate `ss4-22 ⊂ ss12-10` (same start-stamp,
  near-identical quote) survived grading — M19's duplicate-check still not in verify_units
  (owed); both demoted, C-walk must keep only the longer. (c) `dl1-05` zero-length window
  `[00:10:57]-->[00:10:57]` from a single-point srt cue — extend-to-next-cue if cut.
  (d) `ss12-11`'s header label describes its context, not its captured quote (label says
  Netra-limbs, quote is the fire/lake line) — judge demotes on the QUOTE, not the label.
  **Rule: derived sheets/manifests are regenerated from unit files, never trusted across
  sessions; and any duplicate/nested-window check belongs in verify_units (M19 follow-up).**
- **M24. Stale cut cache: span change, same filename.** `make_essence`'s
  cutter skipped existing files, so re-cutting c2's spans reused the old
  46s b0 under the new plan — acrossfade then rendered 46+30 = 75.6s of
  "cell" and every downstream gate still passed (files existed, durations
  matched the WRONG plan because the plan measured the same stale files).
  Caught only because the master grew 34s between passes. **Rule: derived
  cut filenames carry their spans (uid + t_in–t_out); bare indices are
  forbidden. Sheet and master assert equality every build so a cache bug
  can only fail loud, never ship.**

### M25 follow-up (2026-10-26, same day) — the model was right, the dismissal was wrong
After fixing the silence bug, Qwen's full pass diarized 4 voices and
transcribed the Sanskrit chants — and caught that c4's "dip-snapped"
window played sutra 1.12 instead of 1.11 (dips mark syllables, not sutra
boundaries; corrected to [312.5, 317.9], verified "tritaya bhokta
viresa" in-clip). Two corrections to the record: (1) the critic pass I
discounted as confabulation was reading a BROKEN file — near-silence plus
loud TTS explains every "orphan syllable" and "dead air" flag; (2) my
"single passes vary" rule stands, but it does not license dismissing
corroborated structure (three passes + transcript all pointed at real
defects while I blamed the judge). Rule amended: distrust single
passes, but when independent passes AND structure agree, the defect is
real — fix it, don't philosophize about it.

- M26. Custom prompts drop the guardrails. Two ad-hoc listen prompts
  (inline, not from listen.py presets) omitted the excerpt-edge rule and
  returned my own slice boundaries as defects. The presets exist for a
  reason — always extend listen.py, never improvise around it.
- M27. Transcript segment boundaries are not speech onsets. Two B1 windows
  cut at segment starts (1.1 @78.7, 1.2 @97.6) carried 0.4–2s of dead
  pre-speech pause; Qwen read the hole as static/jump. Fix: snap every
  window to speech onset with silencedetect (1.1 →79.0, 1.2 →99.6),
  re-cut, re-verify. Rule: segments locate the neighborhood, silence
  detection sets the in-point.
- M28. Wrong preset for partial proofs. A `verify` pass on a bare two-B1
  pilot confabulated a TTS narrator that doesn't exist (verify assumes
  full beats with card TTS). Discarded per the corroboration rule (model
  claims content absent from the plan = pass failure, not build failure).
  Rule: verify only full beats; scouting/pilots get qa.
- M29. Sentence completion beats silence. A 1.6s pause sat mid-sentence
  ("repeated | births") — cutting in it truncated the word. Rule: the
  in-point snaps to speech onset (M27), the OUT-point snaps to sentence
  completion; verify the last three words complete against the transcript
  before accepting any window.
- M30. 0-windows start on the sutra's frame word, word-verified. 1.1's B1
  opened with "And" (discourse filler from the previous thought) — caught by
  owner ear, not by me. Base word-timestamps put the boundary at 79.8
  ("Sutra"); segment starts are not word starts. Rule: every 0 in-point gets
  word-level verification; fillers ("and/so/now") belong to the previous
  thought and never open 0.
- M31. 0-B1 = the sutra's words only, book-verified. Framing ("Sutra is",
  sandhi demos, previous-sutra context) is explanation, not text — it lives
  in A, never in 0. Verify each B1 against the Aphorisms form before cutting.
- M32. xverse_scan.py mixes files in its report (hits shown under the wrong
  verse with another file's timestamps — e.g. 3.38's statement reported at
  3.3's 85.3s). **RESOLVED 2026-10-28, two compounding causes, both fixed:**
  (1) off-by-one slug slice `[4:-5]` truncated the last digit of every
  two-digit file (`lak_1_11.txt`→`1_1`, home `['1.1']`) — every 1_1X/2_X/3_XX
  file reported under the single-digit verse's home with its own correct
  timestamps, which reads exactly like a file mixup; fixed to `[4:-4]`
  (`locate_b1.py` already had it right). (2) exact-form anchors shared
  exposition headers (sivasutra/unmesa/prathama…) matching every file's own
  statement — fixed with HEADER_STOP. The 3.3→3.38 example evaporated on
  re-run; remaining hits are genuine cross-mentions (mostly 1.1/chaitanya
  references, expected). Rule stands: scout proposes, reading verdicts —
  no moves without a human read of the specific hit.
- M35. Template carried three silent integration breaks at once (found
  2026-10-28 auditing Standard consumers): (a) `sanskrit` field is build
  debris — `block()` grabs up-to-4 raw lines above the book anchor, only
  14/77 last-elements matching the curated `book_sanskrit`, the rest English
  fragments/partial/OCR-variant forms — and `b_match.py` anchored on it;
  (b) `sanskrit_exact`/`sanskrit_src` (added by `template_v2.py`) were lost
  when the template was rebuilt by `build_template.py`+`fix_template_l3.py`
  — two writers, last-write-wins, no assert; `xverse_scan.py` crashed
  (KeyError) and `locate_b1.py` silently matched nothing. Fixed: GRETIL
  forms vendored to `reference/gretil_sivasutra.json` (was /tmp-only),
  `template_v2.py` reads the vendored path + asserts 77/77 non-empty,
  re-ran (75 gretil + 2 ksa-voicing), `b_match.py` anchors on
  `book_sanskrit`. Rule: any tool reading a template field must use
  `.get()` with a loud fallback, and template rebuilds assert the full
  field set — silent field loss is a pipeline bug (M12 family).
- M33. Qwen hallucinates a "synthetic narrator"/TTS in TTS-free builds (1.19,
  2.7, 3.21 joints passes + 3.7/3.22 qa). Pattern: Lakshmanjoo's clipped
  English delivery + room change mislabeled as synthetic. Rule: any pass
  reporting synthetic speech where none exists is discounted on ALL voice
  claims; its structural findings (cut locations, joints) count only with
  a second corroborating pass.
- M33 (confirmed twice): Qwen hallucinates a "synthetic narrator"/TTS voice in
  builds with zero TTS, AND misreads natural pauses as cut-offs (3.17 A:
  claimed mid-word cut at a verified 5s pause; independent whisper
  transcription shows coherent continuous speech). Rule: model voice labels
  are never evidence on single-voice files; structural claims need
  transcript-or-measurement corroboration before any rebuild.
- M34. Wrong-audio-file cut (silent killer). Cut ss4-08's window from
  sLD0aeV1d3o.mp3 (ss3's file) by assuming MANIFEST order == ssN order.
  The cut "succeeded", levels passed, QA described wrong content. Rule:
  resolve every sess->mp3 through tools/build_manifests.py's MP3 map,
  never by position; spot-check each cut's first words against the unit
  quote before assembly.
- M33b (tooling twin of M33): invisible Unicode lookalikes in code (fullwidth
  chars mimicking `__main__`) pass every eyeball and grep-like review yet break
  execution — `grep -c` returned 0 while `tail` displayed the line. Rule: when
  a script behaves impossibly (clean exit, no output, valid-looking source),
  verify at byte level (`python -c` count on rb-read bytes); rewrite the file
  clean instead of patching it.
