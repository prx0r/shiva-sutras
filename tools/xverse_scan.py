#!/usr/bin/env python3
"""Cross-verse scan: for each lak file, find segments matching OTHER verses'
sutra keywords (template exact forms). Output candidate reassignments for
human verdict. Own-verse hits are expected (statements); report top 3 + all foreign hits."""
import json, glob, os, re, unicodedata
from collections import defaultdict

BASE = "/home/ubuntu/shiva-sutras"


def fold(s):
    s = "".join(c for c in unicodedata.normalize("NFD", s)
                if unicodedata.category(c) != "Mn").lower()
    return s.replace("h", "")


tpl = {t["verse"]: t for t in json.load(open(BASE + "/build/template_77.json"))}
keys = {}
# M32-isolated: exact forms all share exposition headers (sivasutra, unmesa,
# prathama/dvitiya/trtiya) — these match EVERY file's own statement and
# report as "foreign hits". Exclude them; only verse-distinctive roots count.
HEADER_STOP = {"sivasut", "pratama", "dvitiya", "trtiya", "unmesa"}
for v, t in tpl.items():
    words = [w for w in re.findall(r"[^\W\d_]{5,}", fold(t.get("sanskrit_exact", "")))]
    keys[v] = [w[:7] for w in words if len(w) > 4 and w[:7] not in HEADER_STOP][:4]

out = []
for f in sorted(glob.glob(BASE + "/text/lak_*.txt")):
    slug = os.path.basename(f)[4:-4]  # strip lak_ + .txt (M32: [4:-5] ate single-digit verse nos)
    if slug in ("intro", "conclusion"):
        continue
    home = {"1_8_10": ["1.8", "1.9", "1.10"],
            "2_7_p1": ["2.7"], "2_7_p2": ["2.7"]}.get(slug, [slug.replace("_", ".")])
    segs = json.load(open(BASE + "/transcripts/" + os.path.basename(f)[:-4]
                           + ".segments.json"))["segments"]
    foreign = defaultdict(list)
    for s in segs:
        f2 = fold(s["text"])
        for v, kws in keys.items():
            if v in home or not kws:
                continue
            n = sum(1 for k in kws if k in f2)
            if n >= 2 or (len(kws) == 1 and n >= 1 and len(kws[0]) > 6):
                foreign[v].append((round(s["t"], 1), s["text"][:70]))
    if foreign:
        out.append("== %s (home %s)" % (slug, home))
        for v, hits in sorted(foreign.items()):
            out.append("  -> %s: %d hits e.g. [%s] %s" %
                       (v, len(hits), hits[0][0], hits[0][1]))
open("/tmp/opencode/xverse.txt", "w").write("\n".join(out) + "\n")
print("%d files with foreign hits" % len(out))
print("\n".join(out[:60]))
