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

## Count-sync discipline
One tool owns every number-line (`sync_counts.py`); run after any
unit/grade change; templates fixed once must never regress (a re-broken
template is a pipeline bug). Scripted doc edits assert count == 1.

## PID-unique temps + chunked transcribe
Cloudflare whisper in 600 s chunks, one temp file per process (shared
temps crash parallel jobs — M8); base64 POST with retries; offsets added
back at merge. Patch scripts to files, never heredocs (OOM-killed
heredocs write partials — asserts saved us, M8).
