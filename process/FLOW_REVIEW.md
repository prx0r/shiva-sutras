# FLOW REVIEW — peer-reviewing flow reliably, every time.

Deterministic checks catch compliance; they cannot hear. This protocol
makes the hearing repeatable: a fixed question series where every answer
must cite evidence (cue numbers, timecodes, quoted words). An answer
without a citation is an opinion and doesn't count. Run after
`validate_sheet.py` passes, before any ear session. Record findings in
`build/FLOW_REVIEW_<cut>.md`.

## The question series (all ten, every review)
1. **Completion test, per beat.** Does the voice complete the question as
   asked? Cite the Q text, the completing sentence (quote ≤20 words), and
   its timecode. Any beat whose answer lives a layer down gets a written
   apophatic ruling (kept consciously, with the layer named).
2. **Chant→translation landing.** Does the meaning land within 5 s of the
   chant ending? Cite the landing words + timecode. If the listener must
   hold untranslated Sanskrit longer, say so and shorten it or flag it.
3. **Longest voice run.** Measure it (flow_lint §1). Any single-voice run
   over 40 s needs a structural justification recorded (weight point) or
   a split point marked. No unowned long runs.
4. **Deictic sweep.** List every pronoun/demonstrative in TTS lines and
   in each archive clip's first sentence. Bind each to its antecedent +
   timecode, or FLAG it. Distant antecedents (>30 s back) count as
   unbound. Card context may carry a binding — write down that it does.
5. **Joint inventory.** Type every voice-to-voice handover (flow_lint §3
   enumerates them). Each SOFT joint states its mitigation (gap length,
   fade, room-tone, bell). Unmitigated SOFT joints fail the review.
6. **Repetition audit.** Same file recurring (flow_lint §5): ritual
   (bells, pads — intended) or accidental (a question/translation heard
   twice without a layer crossing to justify it)? Accidental repetition
   gets cut or re-voiced.
7. **Pause audit.** Every silence: state its job (think / land / reset /
   settle / still). Duration must match the job (XLs only at weight
   points: open, section crossings, terminal). Template-default pauses
   on non-template moments fail.
8. **Head/tail audit.** Each head: does it frame what actually follows
   (count claims — "22 sutras" before 4 clips fails)? Each closer: does
   it pay off, and does the terminal still rather than climax?
9. **G12 audit.** Every archive clip over 25 s: exception with reason
   recorded, or split point with timecode marked. No silent breaches.
10. **Cold-listener test.** One naive question per section ("but what
    DOES it?", "who is 'they'?"). Would they ask it? Does the next beat
    answer it, or does an answer live somewhere unflagged? Unasked-for
    answers are fine; unanswered asks fail.

## Verdict format (per question)
`PASS` | `SOFT` (mitigation + how verified) | `FLAG` (ear/owner decision
needed, with the exact alternatives). Whole-review verdict: FLOW or
NO-FLOW (list blocking FLAGs). NO-FLOW never renders.

## Why this is reliable
The machine half (`flow_lint.py`: runs, joints, longs, repetition,
deictic slots, pause inventory) is byte-deterministic — same sheet,
same findings, any agent, any time. The human half is constrained to
evidence: two reviewers answering Q1–Q10 on the same sheet must produce
the same citations even if their prose differs, because the questions
admit only checkable answers. Disagreements land on FLAGs, which is
where judgment belongs — enumerated, not vibed.
