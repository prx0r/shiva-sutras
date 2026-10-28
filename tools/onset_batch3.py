#!/usr/bin/env python3
"""Round-3 onset verification: file-opening B1s (filler risk)."""
import subprocess

S = "/home/ubuntu/shiva-study-set/"
JOBS = [
    ("1.7", "Shiva Sutras 1.7.mp3", 4), ("2.10", "Shiva Sutras 2.10.mp3", 4),
    ("2.2", "Shiva Sutras 2.2.mp3", 5), ("2.3", "Shiva Sutras 2.3.mp3", 4),
    ("2.5", "Shiva Sutras 2.5.mp3", 4), ("2.8", "Shiva Sutras 2.8.mp3", 6),
    ("3.1", "Shiva Sutras 3.1.mp3", 4), ("3.13", "Shiva Sutras 3.13.mp3", 5),
    ("3.18", "Shiva Sutras 3.18.mp3", 5), ("3.26", "Shiva Sutras 3.26.mp3", 4),
    ("3.31", "Shiva Sutras 3.31.mp3", 5), ("3.33", "Shiva Sutras 3.33.mp3", 5),
    ("3.35", "Shiva Sutras 3.35.mp3", 4), ("3.43", "Shiva Sutras 3.43.mp3", 5),
    ("3.44", "Shiva Sutras 3.44.mp3", 5), ("3.9", "Shiva Sutras 3.9.mp3", 30),
    ("3.17", "Shiva Sutras 3.17.mp3", 66),
]
OUT = "/tmp/opencode/onset_batch3.log"
open(OUT, "w").write("")


def log(s):
    print(s, flush=True)
    open(OUT, "a").write(s + "\n")


from faster_whisper import WhisperModel
m = WhisperModel("base", device="cpu", compute_type="int8")
for v, fn, c in JOBS:
    tmp = "/tmp/opencode/onset_b3.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss",
                    str(max(0, c - 8)), "-t", "16", "-i", S + fn,
                    "-ar", "16000", "-ac", "1", tmp], check=True)
    log("===== %s center %s =====" % (v, c))
    segs, _ = m.transcribe(tmp, beam_size=5, word_timestamps=True,
                           condition_on_previous_text=False)
    off = max(0, c - 8)
    for s in segs:
        for w in (s.words or []):
            log("%7.2f->%7.2f  %s" % (w.start + off, w.end + off, w.word))
log("ALLDONE-B3")
