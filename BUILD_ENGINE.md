# BUILD ENGINE — front door (the law lives in `process/`)

Detailed, agent-executable pipeline: **`process/`** (stages 00–09, axioms,
skills, reproduce, verify) — same apparatus shape as
`analayo-nibbana/process/`. This file states only the two-compilation law and
the decode method. Stage detail lives in `process/`; if they ever
disagree, `process/` wins and this file gets fixed the same day. (Older
notes saying Track F/S mean Standard/Custom compilation.)

## Two compilations, in this order (do not blend them)

**STANDARD COMPILATION (chant).** The text's own structure, untouched:
all 77 sūtras in sūtra order, layered 0/A/B/C — 0 is statement + gloss
only, nothing added; A/B/C add explanation depth, every verse present
at every layer. No reordering, no selectivity, no argument imposed.
Fidelity object first.

**CUSTOM COMPILATION (spine).** Built AFTER the standard compilation,
from its findings: the six questions, the A-layer argument, our
clearest material only. Selection and order are ours; the text's order
is not binding here.

Law of the split: nothing composed for the custom compilation enters
the standard one; nothing in the standard is cut to flatter the custom.
The standard proves we heard the text; the custom proves we understood
it.

## Standard layers (canonical 2026-10-27 — Standard only, Custom untouched)

**Trust order: Dyczkowski's text first.** His Aphorisms is the trusted
wording; Lakshmanjoo's voice carries it. The book checks everything.
**0 = three voicings, nothing else.** Per verse, in order: (1) Lakshmanjoo
states the Sanskrit; (2) AI voice reads Dyczkowski's translation verbatim
("Consciousness is the Self"); (3) Lakshmanjoo reads his English rendering.
Then next verse. No explanation, no guests, no heads, no bells.
**A = 0 + one compressed explanation passage per verse** (his words),
~1 min/verse, whole of A ≈ 1 hour. B/C add depth; guests only in C.
Coda (Sharma complete run) seals C once.

## The decode method (why standard first, custom second)
Video 1 — the Standard Compilation — walks the text in the text's own structure, verse by verse, with
explanations attached logically per verse. It is complete and faithful by
construction — the viewer trusts it because nothing was skipped or
rearranged. Video 2 — the Custom Compilation — is the remix: shorter, punchier, ordered by
what is most interesting, carrying only the clearest findings the standard
surfaced. It earns its selectivity from the standard's completeness — the remix
is credible because the standard pass exists underneath it. Decode any text
this way: standard first, custom second, never the reverse.

## How an agent works here
1. Read `process/README.md` (pipeline + guarantees), then `process/AXIOMS.md`
   (violations fail the build), then the stage file for the work at hand.
2. Run `process/verify.sh` before and after every change to build outputs.
   Red gate stops the line.
3. Log every fix with cause in `MISTAKES.md` (root). The engine only changes
   by adding checks, never relaxing them.
