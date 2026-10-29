# 11 — VOICED GOLD. Every book point gets a voice (the completion method).

The Standard encapsulates the Aphorisms when every gold point is VOICED: by a
human (Lakshmanjoo, Baumer, Hareesh), by Fish TTS reading Dyczkowski verbatim
where no human carries it, or parked on a card (reference material, uncertainty
flags) where audio would bloat or invent. Thin stays thin — the doctrine voices
gold, never pads.

## The ladder (in order, per point)

1. **Human first.** Own lecture (grep the verse file, read the hit in context),
   then Baumer (`b_match.py` proposes, reading disposes), then Hareesh/dl1.
   Windows word-measured (SKILLS quote-locate + `word_onset.py`), sentence-complete
   (M29), no filler openings (M30), overlap-checked by `qa_std.py` F2 (M37).
2. **TTS second.** Book-verbatim sentences only (marks stripped per the B1b rule,
   never reworded; OCR debris dropped only with M38-class justification recorded).
3. **Card third.** Names, equations, terms no audio source carries — with
   UNCERTAINTY FLAG where held OCR is suspect; print-verify settles forms before
   any card renders. Never composed, never smoothed over.
4. **Accept fourth.** SOFT sub-points with per-verse reason recorded (implied-by-A,
   S-adjacent per M20, flavor-not-point, apparatus standing). A blanket accept
   without a reason is slop — each one names what carries it or admits thinness.

## TTS probe discipline (per line, fixed budget)

Isolated probe → carrier-context round-trip → full-line round-trip; stop after
fixed rounds, ship residuals as ear-FLAGs, never reword to fit the voice. Findings
that constrain the method: isolated probes do NOT predict flow rendering (Fish
mangles clusters in sentences that probe clean alone, and vice versa) — the
full-line round-trip is the real gate. Base-whisper round-trips are INVALID for
short Sanskrit (confabulates fluent English outros — M45); gate short clips by
duration-band + Qwen spots + owner ears. Mechanical wins that transfer:
compound-splitting ("Para Shiva"), hyphen pacing, TTS_SAY spoken-forms (display
untouched), owner ear final on proper nouns always.

## Completion gate

Machine-check: zero verse entries without COVERED / RESOLVED / ACCEPTED /
CARD-PARKED / CONFIRMED disposition (`BOOK_COVERAGE_VERDICTS.md`). The audit doc
is a working queue — resolutions land in it with windows, measurements, and qa
outcomes, not summaries.
