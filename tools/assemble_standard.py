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

tpl = json.load(open(BASE + "/build/template_77.json"))
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
if layer == "C":
    open(lst, "a").write("file '%s/audio/gen/std/coda_sharma.mp3'\n" % BASE)
    parts = parts + ["audio/gen/std/coda_sharma.mp3"]

out = sys.argv[3] if len(sys.argv) > 3 else \
    "audio/gen/std/%s_ch%s_%s.mp3" % ("pilot" if ch != "all" else "walk", ch, layer)


def dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration", "-of", "csv=p=0", p],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


expect = sum(dur(p) for p in parts)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0",
                "-i", lst, "-c", "copy", out], check=True)
got = dur(out)
print("parts=%d expect=%.1f master=%.1f diff=%.2f -> %s"
      % (len(parts), expect, got, abs(expect - got), out))
assert abs(expect - got) < 2.0, "assembly drift"
print("ASSEMBLY OK")
