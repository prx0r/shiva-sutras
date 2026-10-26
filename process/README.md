# The Process: teaching series → standard chant + custom spine

Turn a long recorded teaching series on a primary text into two
compilations without writing a single word of doctrine yourself:
the **Standard Compilation** (chant — the text in its own order,
complete) then the **Custom Compilation** (spine — our clearest
findings, selective). Standard first, custom second, never blended.

## What it is

Given a **primary text** (held, e.g. Dyczkowski's Aphorisms), **archive
voices** (e.g. Baumer's 13 sessions + Dyczkowski intro + Sharma chant),
and **stamped transcripts**, this process produces:

- **Standard Compilation** — all 77 sūtras in sūtra order, verse by verse,
  every verse the same four blocks: B1 chant → B2 readout → B3 explanation →
  B4 elaboration. The fidelity object. Nothing skipped, nothing reordered.
- **Custom Compilation, layer A** — the A-grade argument only (~20 min):
  sections as questions, clips in her order, join-audited. The clearest explanation.
- **Custom Compilation, layer B** — A + depth that passes the hold-up test
  (~2× A windows). The deep dive.
- **Custom Compilation, layer C** — A + B + texture in her order (the full walk).
- **Custom Compilation, layer 0** — essay-0: the seed stack (Q → S → T → P → voice),
  heard at every layer head, 4× across the master.

Each verse/beat is a fixed stack — chant (human Sanskrit), card
(Sanskrit + translation, held), plain (mechanical key output), archive
voice (verified clip). Plus bells + pauses per the flow grammar, human
questions at ship, TTS placeholders at v1.

## The pipeline (each step has its own doc)

```
00 INPUTS          primary text + voices + transcripts
01 EXCAVATE        units (quote/context/grade), verify-green from unit one
02 COVERAGE        full read pass, every gap dispositioned in the ledger
03 CONVERGE        measured threads × A-density → sections-as-questions
04 ESSAY0          seed cell stack, flow-read, DRAFT until owner ear
05 ARGUE           Essay A as text + per-join audit
06 AUDIT           UNFOLDING (no seed swapped) + hold-up sweep at lock
07 MANIFEST        quote-located cut stamps per layer/verse, C-walk doc
08 BEATS           run-order, bell grammar, speakers, ear-check list
09 RENDER          TTS placeholders → cuts → concat → loudnorm → listen
```

Track map: 00–04 serve both compilations. 05 argues the custom compilation
only (the standard's storyboard is the sūtra order itself). 06 audits
both. 07–09 run per compilation, standard first.

Supporting files: `AXIOMS.md` (binding rules), `ROLES.md` (the company:
roles abstract + our casting), `SKILLS.md` (reusable
techniques), `MISTAKES.md` at repo root (everything we got wrong + fixes —
read before touching tools), `REPRODUCE.md` (exact rerun), `FILES.md`
(artifact map; repo-wide paths live in `FILEMAP.md`), `verify.sh`
(one-command audit).

## What it guarantees

- No invented doctrine: every sacred word is an exact, provenanced slice
  of a transcript (substring-verified, re-verified after any move).
- No slop narration: TTS speaks mapped words and card rows only;
  plain lines are pure function of (translation, key). Deterministic —
  reruns are byte-identical (hash-recorded).
- Nothing lost: units + ledger hold 100% of the walked material; A/B/C
  are views. The standard compilation holds 100% of the text's order.
- Flow is read, not assumed: essay-0 read aloud, every join verdicted,
  every B-row hold-up tested, ears sign off before anything ships.
