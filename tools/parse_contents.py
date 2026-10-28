#!/usr/bin/env python3
"""Parse the book's Expanded Contents into verse -> (sanskrit, translation, page).
Contents pattern: 'N.M. <sanskrit>  <page>' followed by translation lines."""
import json
import re

lines = open("/tmp/opencode/lakshmanjoo_book.txt", encoding="utf-8",
             errors="replace").readlines()
out = {}
i = 0
cur = None
pat = re.compile(r"^(\d\.\d{1,2})[.,]\s+(.*?)\s+(\d{1,3})\s*$")
while i < len(lines):
    m = pat.match(lines[i].rstrip())
    if m:
        if cur:
            out[cur["v"]] = cur
        v, sk, pg = m.group(1), m.group(2).strip(), int(m.group(3))
        cur = {"v": v, "sanskrit_book": sk, "page": pg, "trans": []}
        cur["_hyph"] = sk.endswith("-")
    elif cur:
        t = lines[i].strip()
        if cur.pop("_hyph", False) and t and not re.match(r"^\d\.\d", t):
            cur["sanskrit_book"] += t.split()[0]
            t = " ".join(t.split()[1:])
            if not t:
                continue
        if re.match(r"^\d\.\d{1,2}\.", t) or t in ("Contents", "x", "xi", "xii",
                                                     "xiii", "xiv", "FIRST AWAKENING",
                                                     "SECOND AWAKENING", "THIRD AWAKENING"):
            pass
        elif t:
            if len(cur["trans"]) < 6:
                cur["trans"].append(t)
        if len(cur["trans"]) >= 6:
            pass
    i += 1
if cur:
    out[cur["v"]] = cur
print(len(out), "verses")
# join translation lines
for v, d in out.items():
    d["translation_book"] = " ".join(d.pop("trans"))
json.dump(out, open("/tmp/opencode/book_contents.json", "w"),
          ensure_ascii=False, indent=1)
for v in ["1.1", "1.4", "1.7", "1.15", "2.7", "2.8", "3.19", "3.33"]:
    d = out.get(v, {})
    print(v, "|", d.get("sanskrit_book"), "|", d.get("translation_book", "")[:60])
