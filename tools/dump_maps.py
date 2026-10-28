#!/usr/bin/env python3
"""Compact transcript maps for A-curation. Usage: dump_maps.py 3_31 3_32 ..."""
import json, sys

BASE = "/home/ubuntu/shiva-sutras"
for v in sys.argv[1:]:
    d = json.load(open(BASE + "/transcripts/lak_%s.segments.json" % v))
    print("=" * 12, "lak_" + v, round(d["segments"][-1]["end"] / 60, 1),
          "min;", len(d["segments"]), "segs")
    n = len(d["segments"])
    step = max(1, n // 18)
    for s in d["segments"][::step][:20]:
        print("[" + str(round(s["t"], 1)) + "] " + s["text"][:58])
