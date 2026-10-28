#!/usr/bin/env python3
"""Template v2: exact GRETIL Sanskrit mapped to Academy verses + book bodies.
GRETIL Light-1 lacks Ksa 1.7 (turya) and 1.15 (hrdaye) as separate items
(its own 1.7/1.15 keys hold the NEXT sutra's text under GRETIL numbering).
Idempotent: re-running refreshes sanskrit_exact/sanskrit_src only.
Source: reference/gretil_sivasutra.json (vendored 2026-10-28 from
/tmp/opencode/gretil.json; GRETIL Kaul text, ancient, no rights issue)."""
import json

BASE = "/home/ubuntu/shiva-sutras"
g = json.load(open(BASE + "/reference/gretil_sivasutra.json"))
tpl = json.load(open(BASE + "/build/template_77.json"))

# Academy -> GRETIL key (None = Ksa-only, use his voicing)
amap = {}
for n in range(1, 7):
    amap["1.%d" % n] = "1.%d" % n
amap["1.7"] = None  # turya: jagrat-svapna-susupta-bhede turyabhoga-sambhavah
for acad, gre in [(8, 7), (9, 8), (10, 9), (11, 10), (12, 11), (13, 12), (14, 13)]:
    amap["1.%d" % acad] = "1.%d" % gre
amap["1.15"] = None  # hrdaye cittasanghattad drsyasvapadarsanam
for acad, gre in [(16, 14), (17, 15), (18, 16), (19, 17), (20, 18), (21, 19), (22, 20)]:
    amap["1.%d" % acad] = "1.%d" % gre
for n in range(1, 11):
    amap["2.%d" % n] = "2.%d" % n
for n in range(1, 46):
    amap["3.%d" % n] = "3.%d" % n

KSA_ONLY = {
    "1.7": "jagratsvapnasusuptabhede turyabhogasambhavah",
    "1.15": "hrdaye cittasanghattad drsyasvapadarsanam",
}
for t in tpl:
    v = t["verse"]
    gk = amap.get(v)
    if gk and gk in g:
        t["sanskrit_exact"] = g[gk]
        t["sanskrit_src"] = "gretil"
    elif v in KSA_ONLY:
        t["sanskrit_exact"] = KSA_ONLY[v]
        t["sanskrit_src"] = "ksa-voicing"
    else:
        t["sanskrit_exact"] = ""
        t["sanskrit_src"] = "missing"
missing = [t["verse"] for t in tpl if not t["sanskrit_exact"]]
assert len(tpl) == 77, "template must hold 77 verses, got %d" % len(tpl)
assert not missing, "sanskrit_exact missing for %s" % missing
print("entries:", len(tpl), "missing:", missing)
json.dump(tpl, open(BASE + "/build/template_77.json", "w"),
          ensure_ascii=False, indent=1)
print("saved")
