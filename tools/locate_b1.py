#!/usr/bin/env python3
"""Scan each lak transcript for its verse's Sanskrit statement.
Keywords from build/template_77.json Sanskrit forms (folded).
Output: candidate segments per verse with timestamps for human verdict."""
import json, re, unicodedata, glob, os

BASE = "/home/ubuntu/shiva-sutras"


def fold(s):
    s = "".join(c for c in unicodedata.normalize("NFD", s)
                if unicodedata.category(c) != "Mn").lower()
    return s.replace("h", "")  # chaitanya/caitanya, shiva/siva converge


tpl = {t["verse"]: t for t in json.load(open(BASE + "/build/template_77.json"))}

fmap = {"1_8_10": ["1.8", "1.9", "1.10"], "2_7_p1": ["2.7"], "2_7_p2": ["2.7"]}
for f in glob.glob(BASE + "/text/lak_*.txt"):
    slug = os.path.basename(f)[4:-4]
    if slug in ("intro", "conclusion"):
        continue
    verses = fmap.get(slug, [slug.replace("_", ".")])
    segs = json.load(open(BASE + "/transcripts/" + os.path.basename(f)[:-4]
                           + ".segments.json"))["segments"]
    for v in verses:
        t = tpl.get(v)
        if not t:
            print(f"== {v}: NO TEMPLATE"); continue
        # keywords: exact GRETIL/Ksa Sanskrit form, folded (h-dropped)
        form = fold(t.get("sanskrit_exact", ""))
        words = [w for w in re.findall(r"[^\W\d_]{4,}", form, flags=re.UNICODE)]
        stop = set()
        kws = [w[:7] for w in words][:8]
        # distinctive: drop ultra-common
        stop = {"which", "their", "there", "about", "that", "consciousness"}
        kws = [w[:7] for w in words if w not in stop][:6]
        hits = []
        for s in segs:
            f2 = fold(s["text"])
            n = sum(1 for k in kws if k in f2)
            if n >= 2 or (len(kws) == 1 and n >= 1):
                hits.append((s["t"], s["end"], n, s["text"][:90]))
        print(f"== {v} [{os.path.basename(f)}] kws={kws[:4]}")
        for h in hits[:8]:
            print(f"   [{h[0]:7.1f}->{h[1]:7.1f}] n={h[2]} {h[3]}")
