#!/usr/bin/env python3
"""Assemble Standard per-verse proofs into ordered walks.
Usage: python3 tools/assemble_standard.py <layer> [ch] [out]
  layer: 0|A|B|C  (proofs audio/gen/std/<tag>_<layer>.mp3, verse order)
  ch: 1|2|3|all (default all). out: default audio/gen/std/<walk>.mp3
Appends coda_sharma.mp3 for layer C walks. Asserts master == sum(parts)
within 2s (M24: sheet==master on every render). PILOT assemblies are
labeled pilot_ and are tooling validation, never ear candidates.
Full-walk assembly only after every verse passes QA (STANDARD.md stage 7)."""
import json, os, subprocess, sys

BASE = "/home/ubuntu/shiva-sutras"
os.chdir(BASE)

layer = sys.argv[1] if len(sys.argv) > 1 else "B"
ch = sys.argv[2] if len(sys.argv) > 2 else "all"
assert layer in ("0", "A", "B", "C"), layer

tpl = json.load(open(BASE + "/standard/template_77.json"))
verses = [t["verse"] for t in tpl]
if ch != "all":
    verses = [v for v in verses if v.split(".")[0] == ch]

parts, missing = [], []
for v in verses:
    p = "audio/gen/std/%s_%s.mp3" % (v.replace(".", "_"), layer)
    (parts if os.path.exists(p) else missing).append(p)
assert not missing, missing

lst = "/tmp/opencode/asm_%s_%s.txt" % (ch, layer)
open(lst, "w").write("".join("file '%s/%s'\n" % (BASE, p) for p in parts))
# (Coda step STRUCK with the Sharma ban — walks end at the last verse.)

out = sys.argv[3] if len(sys.argv) > 3 else \
    "audio/gen/std/%s_ch%s_%s.mp3" % ("pilot" if ch != "all" else "walk", ch, layer)


def dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration", "-of", "csv=p=0", p],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


def nsamples(p):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-ar", "44100",
                        "-ac", "1", "-f", "s16le", "-acodec", "pcm_s16le",
                        "-"], capture_output=True)
    return len(r.stdout) // 2


expect = sum(dur(p) for p in parts)
# M50: NEVER -c copy mp3 concats (mixed-encode frames corrupt joints; headers
# lie while playback fast-forwards). Decode everything, concat PCM, one encode.
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0",
                "-i", lst, "-ar", "44100", "-ac", "1",
                "-codec:a", "libmp3lame", "-q:a", "2", out], check=True)
# Ground-truth gate (headers lied under -c copy): decoded sample count must
# match the summed parts within 1s.
nsk = nsamples(out)
nexp = sum(nsamples(p) for p in parts)
print("samples: expect=%d got=%d diff=%.1fs" % (nexp, nsk, abs(nexp - nsk) / 44100))
assert abs(nexp - nsk) < 44100, "SAMPLE DRIFT — concat corrupt, do not ship"
print("ASSEMBLY OK")
