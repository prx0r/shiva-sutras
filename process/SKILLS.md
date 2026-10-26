# SKILLS — reusable techniques (ported, then adapted).

## Quote-locate (manifest-grade cut stamps)
Minimal contiguous transcript line-run covering the normalized quote
(punctuation/whitespace/`[HH:MM:SS]`/`[Music]` stripped both sides);
word-index → time at ~2.7 wps anchored to real stamps; completeness +
padding bounds (tin + W/3.6 + 0.4 ≤ tout ≤ tin + W/2.0 + 5.5). Skips
caption-lag dead zones by starting the search at the unit window −120 s.
Reference: `tools/build_manifests.py` `locate()`.

## Dual normalization (verifier must match the source's format)
YT/CF captions keep punctuation → strip it both sides. SRT-style
sources with clean text → whitespace-only. The norm matches the source,
never copied blindly (M6). Timestamps stripped before substring match;
start-stamp proximity checked separately (120 s tolerance).

## Keyword-score + fallback + verdict (segmentation without blobs)
Profiles per section from distinctive doctrine terms (pan-corpus glue
terms zero-counted and removed first — M9); score unit window + quote;
ties/zeroes/thin → session primary; content overrides logged with the
uid. Blind agglomerative clustering not run (produces blobs/dust).

## Hold-up test (one question per row)
"Does this deepen the locked seed answer beyond what A gives?" Verdict
KEEP / DEMOTE / LEDGER with a one-line reason. Budgets ≈ A×1.6–2.
Run against DRAFT only provisionally; re-run at LOCK.

## Flow-read (text gate before audio)
Read the whole chain aloud, no analysis. Record: does each answer plant
the next question? One hidden argument underneath? Weakest join named.
Text-level verdicts (bridges, levers, closure tests) become the audio
session's checklist.

## ASR ear-check harvest
Grep unit contexts for flagged forms + known suspect list (proper nouns,
mantra terms, I/eye, guru-words); each row: uid + window + heard-as +
expected. Verify at audio QA with mp3s, never from text.

## Count-sync disciplineOne tool owns every number-line (`sync_counts.py`); run after any
unit/grade change; templates fixed once must never regress (a re-broken
template is a pipeline bug). Scripted doc edits assert count == 1.

## PID-unique temps + chunked transcribe
Cloudflare whisper in 600 s chunks, one temp file per process (shared
temps crash parallel jobs — M8); base64 POST with retries; offsets added
back at merge. Patch scripts to files, never heredocs (OOM-killed
heredocs write partials — asserts saved us, M8).

## Sheet validation (the sheet is the product)
`tools/validate_sheet.py` works on ANY production sheet, standard or
custom: files exist, measured durations match the dur column, timecodes
accumulate without gaps, stated total matches, handover-audit + FX
sections present, FLAGs listed (open decisions, never failures).
A sheet that fails is not production-ready; a sheet that passes is
shippable for review with render still explicitly out of scope.

## Responsibility read (cold verdicts, not summaries)
When asked "does X work", do not describe X. Re-read X and verdict each
unit of it with a reason and, where it fails, a concrete alternative.
Procedure (as executed 2026-10-26 on essay-0 + Essay A):
1. Read the chain cold (flow-read artifact, then arguments, then joins).
2. Per cell/section: does the voice complete the question as asked?
   Name the exact sentence that carries or breaks it.
3. Per pause: what job does this silence do (think / land / reset)?
   Weight pauses to question-and-card difficulty, not to the template.
4. Per handover: parse the joint (tongue-switch? timbre-switch?
   deictic?); verdict OK / SOFT / FLAG with the mitigation.
5. End with decisions HANDED OVER, not taken: what needs ears, what
   needs the owner, what you recommend and why.
What it yielded here (the proof it beats assuming): the S1 fusion gap,
the S3 apophatic ruling, the S4 opaque-T ruling + pause prescription,
the S6 voice-swap audition, three differentiated silences, the L0→LA
restatement endorsed as doctrine-performed, the S5 bridge endorsed
without redesign, the G12 breach named with a keep-whole lean. None of
these existed in any artifact before the read; all of them changed the
build. Assuming would have shipped every one of these defects inside a
passing gate suite — gates check compliance, only the read checks sense.

## Model ears (audio QA): strong finder, weak verifier
An audio-capable model on the master is a good FIRST pass: it found the
TTS-Sanskrit offense, the c1 hard-concat seam, and the c2 "they"
comprehension failure (wrong antecedent inferred — the tell that the
card context did NOT carry it). It is a poor verifier: pass 3 returned
all-CLEAN with confabulated specifics (wrong labels, fake-precise
timecodes, "no long runs" beside a 42s clip). Rule: use model passes to
HUNT, never to CLEAR. Every fix must also hold structurally
(antecedent now adjacent in the cut plan, crossfade in the filter
graph, pronunciation by voice casting) — the build asserts what ears
cannot, and human ears still close the loop.
Excerpt probes confabulate worse than full passes (c3 excerpt invented
mantras and speakers): probe ISOLATED lines for pronunciation, run FULL
pieces for structure, never use excerpts as evidence for anything.
Single passes vary wildly run to run (one pass's all-CLEAN contradicts
the next pass's NO-FLOW on identical audio; orphan-syllable timestamps
shift between runs) — a finding only counts when corroborated by a
second pass or by structure (cut plan, transcript, measurement).
Uncorroborated model claims are logged as hints, never acted on.

## Deterministic flow checks (transcript-backed, no ears needed)
The sheet + transcripts already prove most of "flow": `tts_scan.py`
(Sanskrit never reaches TTS raw), `deictic_check.py` (every clip-opener
pronoun bound to transcript lines or flagged), repetition/order audits
from the sheet itself (flow_lint). Reserve ears strictly for acoustic
seam quality, drag feel, TTS naturalness, and confusion — everything
else asserts in code or text before any listening happens.
