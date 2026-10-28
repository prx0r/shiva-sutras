#!/usr/bin/env python3
"""Build Academy-keyed 77-verse template from the held Aphorisms.
Academy 1.16 <-> book 1/16+1/17 (split); Academy 1.17-1.22 <-> book 1/18-1/23.
Lights 2,3 map directly."""
import re, json, collections

BASE = "/home/ubuntu/shiva-sutras"
lines = open(BASE + "/reference/aphorisms-of-siva-dyczkowski_clean.txt",
             encoding="utf-8", errors="replace").readlines()
eol = set(i for i, l in enumerate(lines)
          if re.search(r"[123]/\d{1,2}\s*$", l.rstrip()))
anchors = sorted(eol | {819, 2696})
info = {}
for pos, idx in enumerate(anchors):
    nxt = anchors[pos + 1] if pos + 1 < len(anchors) else min(idx + 500, len(lines))
    m = re.search(r"([123])/(\d{1,2})", lines[idx])
    assert m, idx
    info[idx] = {"book": m.group(1) + "." + m.group(2), "nxt": nxt}
bybook = {}
for k, v in info.items():
    bybook.setdefault(v["book"], []).append(k)


def block(a):
    i = a
    nxt = info[a]["nxt"]
    mline = lines[i].rstrip()
    trans = re.sub(r"\s*[123]/\d{1,2}\s*\.?\s*$", "", mline).strip()
    if not trans or not trans[0].isupper():
        j = i - 1
        while j > 0 and not lines[j].strip():
            j -= 1
        trans = (lines[j].strip() + " " + trans).strip()
    sk = []
    j = i - 1
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
    body = "".join(lines[i + 1:nxt - 6]).strip()
    return trans, sk, body


tpl = []


def add(acad, booknums):
    idxs = []
    for b in booknums:
        if "#" in b:
            base, nth = b.split("#")
            idxs.append(bybook[base][int(nth) - 1])
        else:
            if len(bybook[b]) > 1:
                raise ValueError("ambiguous book label %s (use #1/#2)" % b)
            idxs.append(bybook[b][0])
    parts = [block(a) for a in idxs]
    trans = " / ".join(p[0] for p in parts)
    sk = sum([p[1] for p in parts], [])
    body = ("\n\n[book %s]\n" % ",".join(booknums)) + "\n\n".join(p[2] for p in parts)
    tpl.append({"verse": acad, "book": booknums, "sanskrit": sk,
                "translation": trans, "body_chars": len(body), "body": body})


for n in range(1, 16):
    add("1.%d" % n, ["1.%d" % n])
add("1.16", ["1.16", "1.17"])
for n in range(17, 23):
    add("1.%d" % n, ["1.%d" % (n + 1)])
for n in range(1, 11):
    add("2.%d" % n, ["2.%d" % n])
for n in range(1, 29):
    add("3.%d" % n, ["3.%d" % n])
add("3.29", ["3.30"])
# book prints 3/32 twice: first = Acad 3.30 (svasakti), second = Acad 3.31 (sthiti)
add("3.30", ["3.32#1"])
add("3.31", ["3.32#2"])
for n in range(32, 36):
    add("3.%d" % n, ["3.%d" % (n + 1)])
# Acad 3.36 (bheda) has no own anchor — carried inside the 3/36 block; flagged
add("3.36", ["3.36"])
for n in range(37, 46):
    add("3.%d" % n, ["3.%d" % (n + 1)])
print(collections.Counter(t["verse"].split(".")[0] for t in tpl), len(tpl))
json.dump(tpl, open(BASE + "/standard/template_77.json", "w"),
          ensure_ascii=False, indent=1)
print("saved")
for t in tpl[15:18]:
    print(t["verse"], t["book"], "|", t["translation"][:80])
