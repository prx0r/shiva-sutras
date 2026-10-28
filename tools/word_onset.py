#!/usr/bin/env python3
"""Word-onset verification for B1 candidates. Usage:
python3 tools/word_onset.py <mp3> <center1> [center2 ...] [--window N]
Cuts center±window per center, runs base word timestamps, prints words.
Model loads once for the whole batch."""
import subprocess, sys, os
args = [a for a in sys.argv[1:] if not a.startswith("--")]
window = 8
for a in sys.argv[1:]:
    if a.startswith("--window"):
        window = float(a.split("=")[1])
mp3, centers = args[0], [float(c) for c in args[1:]]
from faster_whisper import WhisperModel
m = WhisperModel("base", device="cpu", compute_type="int8")
for center in centers:
    tmp = "/tmp/opencode/onset.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss",
                    str(max(0, center - window)), "-t", str(2 * window),
                    "-i", mp3, "-ar", "16000", "-ac", "1", tmp], check=True)
    print(f"===== center {center} =====")
    segs, _ = m.transcribe(tmp, beam_size=5, word_timestamps=True,
                           condition_on_previous_text=False)
    off = max(0, center - window)
    for s in segs:
        for w in (s.words or []):
            print(f"{w.start + off:7.2f}->{w.end + off:7.2f}  {w.word}")
