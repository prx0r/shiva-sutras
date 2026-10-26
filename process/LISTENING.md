# LISTENING — what the ears are actually for (Qwen omni protocol).

The transcript is already perfect — every quote verified verbatim,
every cut from stamped spans. So the listen NEVER checks words. It
checks the four things text cannot see:

1. **Seams.** Hard concats, mid-word cuts, room jumps, clicks. The plan
   says where every joint is; ears say whether each one lands.
2. **Pacing feel.** Draggy stretches, stranded pauses, rushed landings.
   Durations are measured; only ears know if 46 seconds feels like
   depth or indulgence.
3. **Voice truth.** TTS naturalness, misreads, chant clarity. Spoken
   forms are probed isolated; delivery is judged in flow.
4. **Confusion.** Deictics that don't resolve, answers arriving before
   questions, anything a cold listener trips on. The model plays the
   cold listener better than any of us can — it has no memory of the
   plan.

## The critic format (every pass returns this shape)
Per section (S1-head, each cell, heads): FLOW 1–5 + one quoted reason.
Then: TOP 3 FLAWS (quoted location, what's wrong, suggested fix).
Then: ADVICE (one paragraph — if you were the director, what single
change improves this most?). Then VERDICT: FLOW / NO-FLOW with blocking
quotes. Ratings without quotes are ignored; quotes without timecues are
hints, not findings.

## Prompt modes (`tools/listen.py`)
- `qa` — full pass, transcript sketch + flaws + joints + deictics.
- `critic` — the format above (default for review passes).
- `joints` — handover inventory only.
- `deictics` — first-sentence pronouns + referents.
- `verify` — targeted re-check of fixed items + verdict.
Isolated-line probes (pronunciation) are separate: one word, three
candidate renderings, exact-transcription task. Never probe phonetics
in running audio.

## Interpretation rules (violations fail the review)
1. A finding counts only corroborated: second pass OR structure (cut
   plan, transcript, measurement). Single-pass claims are hints.
2. Full passes only. Excerpts confabulate (invented mantras, wrong
   speakers) — never evidence.
3.Transcript-sketch errors discount the pass, not the build: if the
   model mislabels voices, its flaw claims need structural backup.
4. "No flaws found" is the weakest result, not the strongest — it means
   run the targeted verify pass, not ship it.
5. Cost discipline: qwen3.8-omni-flash, thinking off, tight prompts
   (~$0.001 per 5-min pass). Log cost per pass in the review artifact.
   Never pay for what `flow_lint.py`, `tts_scan.py`, or
   `deictic_check.py` already assert.

## Worked example (essence v1, passes 1–6)
- Pass 1 (qa): found TTS-Sanskrit offense, c1 hard-concat seam, c2
  "they" with wrong antecedent inferred — all three verified
  structurally and fixed (human chant cards, 0.4s crossfades,
  antecedent cut in). Model: hunter, credited.
- Pass 2 (targeted): confirmed human chant, re-fetched c1 seam + c2
  "they" — corroborated both. Fixes proceeded on corroboration.
- Pass 3 (qa): all-CLEAN with confabulated specifics contradicting
  pass 2 on identical audio — DISCOUNTED as verification (rule 4
  inverse: clean bill without quotes is noise).
- Pass 5/6 (Fish voice era): confirmed human-sounding narrator;
  "Bhairava" anglicized → isolated probe → "Bye-ruh-vuh" wins,
  TTS_SAY map. Full-mix phonetic claims discounted; isolated probe
  trusted.
- Standing: every structural flaw fixed or flagged; remaining items
  are human-ear calls (the 3 FLAGs). No further model passes scheduled
  — marginal value exhausted until the next cut change.

## Full potential (what the model is actually good for)
qwen3.8-omni-flash (1M context, 113 languages, thinking/web-search/
function-calling, JSON Object mode, implicit caching, 2h video):
- **QA passes** (this doc) with `reasoning_effort: none` + tight caps —
  ~$0.001 per 5 min. Thinking left on multiplies cost 10x via reasoning
  tokens; never leave default for QA.
- **Structured audits** (`audit` prompt → JSON): machine-readable flaws
  with quotes — feeds review without prose parsing.
- **Diarization/voice mapping**: who speaks when (verify speaker law).
- **Transcription with timestamps**: independent transcript of the
  master — diff against the sheet as a compliance check.
- **1M-context structural reads**: whole transcripts + sheet in one
  prompt; section summaries; meeting-minute style beat logs.
- **Video understanding (2h)**: when the visual layer exists, the same
  QA loop reviews picture + sound together.
- **Web search + function calling**: research tasks (Sanskrit
  verification against print sources) with audio in context.
What it does NOT do: **make visuals** — omni-flash is text-output
only (understanding, not generation). Image/video generation is a
separate track (qwen-image / wan series) for the future visual phase.
Cost discipline stands: deterministic checks first, model only for
what text cannot see, every pass logged with engine + usage.

## Full potential (what the model is actually good for)
qwen3.8-omni-flash (1M context, 113 languages, thinking/web-search/
function-calling, JSON Object mode, implicit caching, 2h video):
- **QA passes** (this doc) with `reasoning_effort: none` + tight caps —
  ~$0.001 per 5-min pass. Thinking left on multiplies cost 10x via reasoning
  tokens; never leave default for QA.
- **Structured audits** (`audit` prompt → JSON): machine-readable flaws
  with quotes — feeds review without prose parsing.
- **Diarization/voice mapping**: who speaks when (verify speaker law).
- **Transcription with timestamps**: independent transcript of the
  master — diff against the sheet as a compliance check.
- **1M-context structural reads**: whole transcripts + sheet in one
  prompt; section summaries; meeting-minute style beat logs.
- **Video understanding (2h)**: when the visual layer exists, the same
  QA loop reviews picture + sound together.
- **Web search + function calling**: research tasks (Sanskrit
  verification against print sources) with audio in context.
What it does NOT do: **make visuals** — omni-flash is text-output
only (understanding, not generation). Image/video generation is a
separate track (qwen-image / wan series) for the future visual phase.
Cost discipline stands: deterministic checks first, model only for
what text cannot see, every pass logged with engine + usage.
