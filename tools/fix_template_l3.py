#!/usr/bin/env python3
"""Fix template Light-3 mapping: Academy 3.15-3.28 -> book 3/16-3/29.
(Book 3/15 is a visarga-sutra absent from Ksa/Acd numbering.)"""
import json
import re

BASE = "/home/ubuntu/shiva-sutras"
lines = open(BASE + "/reference/aphorisms-of-siva-dyczkowski_clean.txt",
             encoding="utf-8", errors="replace").readlines()
pat_eol = re.compile(r"[123]/\d{1,2}\s*$")
pat_num = re.compile(r"([123])/(\d{1,2})")
eol = sorted(i for i, l in enumerate(lines) if pat_eol.search(l.rstrip()))
eol = sorted(set(eol) | {819, 2696})
info = {}
for k, idx in enumerate(eol):
    nxt = eol[k + 1] if k + 1 < len(eol) else min(idx + 500, len(lines))
    m = pat_num.search(lines[idx])
    assert m, idx
    info[(m.group(1), int(m.group(2)))] = (idx, nxt)


def block(idx, nxt):
    mline = lines[idx].rstrip()
    trans = re.sub(r"\s*[123]/\d{1,2}\s*\.?\s*$", "", mline).strip()
    if not trans or not trans[0].isupper():
        j = idx - 1
        while j > 0 and not lines[j].strip():
            j -= 1
        trans = (lines[j].strip() + " " + trans).strip()
    sk = []
    j = idx - 1
    if j >= 0 and lines[j].strip() and lines[j].strip() in trans:
        j -= 1
    while j > 0 and len(sk) < 4:
        if lines[j].strip() == "":
            j -= 1
            continue
        sk.insert(0, lines[j].strip())
        if len(lines[j].strip()) > 70:
            break
        j -= 1
    body = "".join(lines[idx + 1:nxt - 6]).strip()
    return trans, sk, body


tpl = json.load(open(BASE + "/standard/template_77.json"))
byv = {t["verse"]: t for t in tpl}
for n in range(15, 29):
    idx, nxt = info[("3", n + 1)]
    trans, sk, body = block(idx, nxt)
    t = byv["3.%d" % n]
    t["book"] = ["3.%d" % (n + 1)]
    t["translation"] = trans
    t["sanskrit"] = sk
    t["body_chars"] = len(body)
    t["body"] = body
    print(t["verse"], t["book"], "|", trans[:60])
json.dump(tpl, open(BASE + "/standard/template_77.json", "w"), ensure_ascii=False,
          indent=1)
print("saved")
