#!/usr/bin/env python3
"""Batch word-onset verification. Loads model once, processes job list.
Jobs: (label, mp3path, center, window). Appends results to OUTFILE."""
import subprocess, sys, os

S = "/home/ubuntu/shiva-study-set"
JOBS = [
    ("1.3", "Shiva Sutras 1.3.mp3", 16, 6),
    ("1.5", "Shiva Sutras 1.5.mp3", 48, 6),
    ("1.7", "Shiva Sutras 1.7.mp3", 4, 6),
    ("1.8", "Shiva Sutras 1.8-10.mp3", 14, 6),
    ("1.9", "Shiva Sutras 1.8-10.mp3", 31, 6),
    ("1.10", "Shiva Sutras 1.8-10.mp3", 46, 6),
    ("1.13", "Shiva Sutras 1.13.mp3", 15, 6),
    ("1.15", "Shiva Sutras 1.15.mp3", 47, 8),
    ("1.16", "Shiva Sutras 1.16.mp3", 22, 6),
    ("1.17", "Shiva Sutras 1.17.mp3", 17, 6),
    ("1.18", "Shiva Sutras 1.18.mp3", 4, 6),
    ("2.1", "Shiva Sutras 2.1.mp3", 128, 10),
    ("2.3", "Shiva Sutras 2.3.mp3", 4, 6),
    ("2.4", "Shiva Sutras 2.4.mp3", 20, 6),
    ("2.5", "Shiva Sutras 2.5.mp3", 4, 6),
    ("2.6", "Shiva Sutras 2.6.mp3", 18, 6),
    ("2.8", "Shiva Sutras 2.8.mp3", 4, 6),
    ("2.9", "Shiva Sutras 2.9.mp3", 4, 6),
    ("2.10", "Shiva Sutras 2.10.mp3", 4, 6),
    ("3.1", "Shiva Sutras 3.1.mp3", 4, 6),
    ("3.4", "Shiva Sutras 3.4.mp3", 17, 6),
    ("3.5", "Shiva Sutras 3.5.mp3", 53, 6),
    ("3.9", "Shiva Sutras 3.9.mp3", 32, 8),
    ("3.10", "Shiva Sutras 3.10.mp3", 19, 6),
    ("3.12", "Shiva Sutras 3.12.mp3", 4, 6),
    ("3.13", "Shiva Sutras 3.13.mp3", 4, 6),
    ("3.15", "Shiva Sutras 3.15.mp3", 4, 6),
    ("3.16", "Shiva Sutras 3.16.mp3", 4, 6),
    ("3.23", "Shiva Sutras 3.23.mp3", 40, 8),
    ("3.25", "Shiva Sutras 3.25.mp3", 13, 6),
    ("3.26", "Shiva Sutras 3.26.mp3", 4, 6),
    ("3.27", "Shiva Sutras 3.27.mp3", 4, 6),
    ("3.28", "Shiva Sutras 3.28.mp3", 16, 6),
    ("3.30", "Shiva Sutras 3.30.mp3", 4, 6),
    ("3.31", "Shiva Sutras 3.31.mp3", 4, 6),
    ("3.32", "Shiva Sutras 3.32.mp3", 4, 6),
    ("3.35", "Shiva Sutras 3.35.mp3", 4, 6),
    ("3.36", "Shiva Sutras 3.36.mp3", 45, 6),
    ("3.39", "Shiva Sutras 3.39.mp3", 5, 6),
    ("3.41", "Shiva Sutras 3.41.mp3", 25, 8),
    ("3.43", "Shiva Sutras 3.43.mp3", 4, 6),
    ("3.44", "Shiva Sutras 3.44.mp3", 4, 6),
    ("3.45", "Shiva Sutras 3.45.mp3", 22, 6),
]
OUT = "/tmp/opencode/onset_batch.txt"
open(OUT, "w").write("")


def log(s):
    print(s, flush=True)
    open(OUT, "a").write(s + "\n")


from faster_whisper import WhisperModel
m = WhisperModel("base", device="cpu", compute_type="int8")
for label, fn, center, window in JOBS:
    tmp = "/tmp/opencode/onset_b.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss",
                    str(max(0, center - window)), "-t", str(2 * window),
                    "-i", os.path.join(S, fn), "-ar", "16000", "-ac", "1",
                    tmp], check=True)
    log(f"===== {label} center {center} =====")
    segs, _ = m.transcribe(tmp, beam_size=5, word_timestamps=True,
                           condition_on_previous_text=False)
    off = max(0, center - window)
    for s in segs:
        for w in (s.words or []):
            log(f"{w.start + off:7.2f}->{w.end + off:7.2f}  {w.word}")
log("ALL DONE")
