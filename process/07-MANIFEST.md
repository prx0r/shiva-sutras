# 07 — MANIFEST. Quote-located cut stamps per layer; texture walk doc.

## Cut stamps (`tools/build_manifests.py` → `manifest_sN_{A,B,C}.json`)
Stamps locate the QUOTE (minimal contiguous line-run covering the
normalized quote, word-index → time interpolated at ~2.7 wps), never the
raw window edges. Completeness + padding bounds at plausible speech
rates guard caption lag; suspicious spans (>300 s) and past-EOF cuts
fail loudly. Order law: join-audited SECTION_ARGUMENTS order canonical,
missing units inserted by (session, timestamp); session blocks
contiguous and ascending per section (asserted). Every unit's grade and
section must match SPINE_ASSIGN (asserted).
SEED-CAP: essay-0 cell clips play at layer heads only, never in section
lists. Known duplicates resolve once by id with the reason logged (keep
the longer). Per-section beats carry uid, mp3, t_in/t_out, dur, grade,
title; headers carry clip counts + window runtimes.

## Layers
- A = sections at speed (append-only collate of the audited argument).
- B = A ∪ keeps (hold-up winners only).
- C = everything in her order (A + B + texture; chant/mic/logistics
  never unit'd; ledger-notes never appear).
`C_WALK.md` is the readable twin of the C manifests. Runtime honesties
recorded at build (band vs actual, caption-lag pads, holes documented,
never silently bridged). Thin sections stay thin — no clip cut for
runtime against audited membership (owner decides band vs membership at
the ear session).

## Gate
Every cut locates; durations within bounds; per-session monotonicity
holds; counts print per layer and per section. Re-run after any
grade/order change.
