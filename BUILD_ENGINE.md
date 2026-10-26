# BUILD ENGINE — front door (the law lives in `process/`)

Detailed, agent-executable pipeline: **`process/`** (stages 00–09, axioms,
skills, reproduce, verify) — same apparatus shape as
`analayo-nibbana/process/`. This file states only the two-track law and
the decode method. Stage detail lives in `process/`; if they ever
disagree, `process/` wins and this file gets fixed the same day.

## Two projects, in this order (do not blend them)

**TRACK F — the formal version (chant).** The text's own structure,
untouched: all 77 sūtras in sūtra order, verse by verse, every verse the
same four blocks (B1 chant → B2 readout → B3 explanation → B4 elaboration).
No reordering, no selectivity, no argument imposed. Fidelity object first.

**TRACK S — the spine (our edit).** Built AFTER the formal version, from
its findings: the six questions, the A-layer argument, our clearest
material only. Selection and order are ours; the text's order is not
binding here.

Law of the split: nothing composed for S enters F; nothing in F is cut to
flatter S. F proves we heard the text; S proves we understood it.

## The decode method (why two videos, in this order)
Video 1 walks the text in the text's own structure, verse by verse, with
explanations attached logically per verse. It is complete and faithful by
construction — the viewer trusts it because nothing was skipped or
rearranged. Video 2 is the custom remix: shorter, punchier, ordered by
what is most interesting, carrying only the clearest findings Video 1
surfaced. It earns its selectivity from Video 1's completeness — the remix
is credible because the formal pass exists underneath it. Decode any text
this way: formal pass first, remix second, never the reverse.

## How an agent works here
1. Read `process/README.md` (pipeline + guarantees), then `process/AXIOMS.md`
   (violations fail the build), then the stage file for the work at hand.
2. Run `process/verify.sh` before and after every change to build outputs.
   Red gate stops the line.
3. Log every fix with cause in `MISTAKES.md` (root). The engine only changes
   by adding checks, never relaxing them.
