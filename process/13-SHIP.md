# 13 — SHIP. From proofs to public links without lying (post-M50).

Every master proves itself by CONTENT, never by headers. Duration metadata lies
on concats; model ears are blind to global defects (speed/pitch); whisper VAD
quits on long leading non-speech and confabulates on short clips. The chain:

## 1. Assemble (sample truth)

`assemble_standard.py`: decode → concat PCM → single encode (NEVER stream-copy
across files — M50). Asserts decoded SAMPLE counts, not header durations. Walk
masters only; intro bundle separate. Coda step struck with the Sharma ban.

## 2. Level (post-production chain, no re-renders)

Per-role gains baked at build (`build_standard_verse.py` role calibration);
walk stage: moment-leveling for mixed-voice evenness, then linear gain to the
house line (−19 LUFS mono). Bells are never leveled with speech (meter them
separately or leave them). Measure before and after; ears judge, meters report.

## 3. Verify (three gates, all content)

- **Samples:** decoded sample count == sum of parts (±1s).
- **Head:** transcribe past the intro (never open the window on bells — whisper
  VAD quits); expect words. Zero words = stop the line.
- **Seams:** joints inventory on ≤30min chunks (longer passes thin out to empty);
  structural flags only (CUT/mid-word/wrong-content). Doorway RUBBEDs are design.

## 4. Mirror + link (durable first)

R2 mirror with byte-match check, then public links (new key per version;
superseded links struck from PROCESS_NOTES the same day). uguu expires, R2
endures. Never link a master its gates haven't passed; never re-upload silently
after a rebuild.

## 5. Iterate (pilot-first, per M51)

No batch of 77 builds except through `build_all.py`. No full-length renders to
catch mistakes: pilot verse → samples → sheets → ears. A 22-second proof carries
every voice class and proves a voice swap in one minute.
