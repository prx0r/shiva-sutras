#!/usr/bin/env python3
"""B-candidate retrieval: rank Baumer units per verse by distinctive-term
overlap with the book exposition. Human verdicts follow.
Usage: python3 tools/b_match.py 1.1 1.2 ...  (defaults to 1.1)"""
import glob
import json
import os
import re
import sys
import unicodedata
from collections import Counter

BASE = "/home/ubuntu/shiva-sutras"


def fold(s):
    out = []
    for c in unicodedata.normalize("NFD", s):
        if unicodedata.category(c) != "Mn":
            out.append(c.lower())
    return "".join(out).replace("h", "")


STOP = set(("the and his with from that this which have will what when "
"there their them then than thus such every other these those into upon "
"also may might must shall being been were are was had has have not no "
"yes you your our they them then there here where while through during "
"before after about above below self same own just like know reality "
"state nature consciousness mind siva shiva verse sutra means says said "
"does done made makes make many much more most very can cannot could "
"would should may might must will shall").split())

tpl = {t["verse"]: t for t in json.load(open(BASE + "/build/template_77.json"))}

units = []
for f in sorted(glob.glob(BASE + "/excavations/ss*.md") + [BASE + "/excavations/dl1.md"]):
    cur = None
    for line in open(f, encoding="utf-8", errors="replace"):
        m = re.match(r"###\s+(\S+)\s+", line)
        if m:
            if cur and cur.get("quote"):
                units.append(cur)
            cur = {"uid": m.group(1), "file": os.path.basename(f),
                   "head": line.rstrip()[:160], "quote": "", "ctx": []}
        elif cur is not None:
            if line.startswith("- quote:"):
                cur["quote"] = line[len("- quote:"):].strip()
            elif line.startswith("- context:") or line.startswith("- essay_use:"):
                cur["ctx"].append(line.strip()[:200])
    if cur and cur.get("quote"):
        units.append(cur)
print("units loaded: %d" % len(units), file=sys.stderr)


def terms(text):
    return [w for w in re.findall(r"[a-z]{5,}", fold(text)) if w not in STOP]


def candidates(v, top=8):
    t = tpl[v]
    anchor = " ".join([t.get("translation", "")] + t.get("sanskrit", []))
    doc = t.get("body", "")[:6000] + " " + anchor
    atext = ""
    mp = BASE + "/build/std_" + v.replace(".", "_") + ".json"
    segs = []
    sp = BASE + "/transcripts/lak_" + v.replace(".", "_") + ".segments.json"
    if os.path.exists(sp):
        segs = json.load(open(sp))["segments"]
    if os.path.exists(mp):
        man = json.load(open(mp))
        for L in ("0", "A"):
            for p in man.get("layers", {}).get(L, []):
                atext += " " + " ".join(
                    s["text"] for s in segs
                    if s["end"] > p["t_in"] and s["t"] < p["t_out"])
    dt = Counter(terms(doc))
    at = Counter(terms(atext))
    scored = []
    for u in units:
        ut = Counter(terms(u["quote"] + " " + " ".join(u["ctx"])))
        s = 0.0
        for w, c in ut.items():
            if w in dt:
                s += min(c, 3) * (1 + dt[w] ** 0.5) / (1 + at.get(w, 0))
        if s > 0:
            scored.append((s, u["uid"], u))
    scored.sort(key=lambda x: -x[0])
    return [(round(s, 1), uid, u["file"], u["head"][:100], u["quote"][:90])
            for s, uid, u in scored[:top]]


def main(argv):
    verses = [a for a in argv if not a.startswith("-")] or ["1.1"]
    for v in verses:
        print("=" * 12, v, flush=True)
        for s, uid, fn, head, q in candidates(v):
            print("  %.1f %s [%s] %s" % (s, uid, fn, head[:75]))
            print("      Q: %s" % q[:110])


if __name__ == "__main__":
    main(sys.argv[1:])
