#!/usr/bin/env python3
"""Build the Standard B1b line: Fish TTS of Dyczkowski's translation verbatim.
Spoken text = template translation with paren MARKS stripped (words kept),
"/" joins Cadenced to ". ", ".." collapsed; display/card text untouched.
Known book typos repaired ONLY against the book's own front-listing
(2.5 ofi->of fixed in template 2026-10-28; none remain here).
Sanskrit-voicing audit: every capitalized non-English token must resolve to
TTS_SAY or a probed-acceptable form (Maya, Siva), else the verse is DEFERRED.
Usage: python3 tools/build_b1b.py [verse ...]  (default: all 77)
Output: audio/gen/tts/b1b_<tag>.wav (-21dB via tts_line.py).
Voice: owner-locked Dyczkowski seat = voice THREE (tts_line.py header).
Manifest insertion is separate (insert_b1b step below)."""
import json, os, re, subprocess, sys

BASE = "/home/ubuntu/shiva-sutras"
THREE = "ef9c79b62ef34530bf452c0e50e3c260"  # owner-locked Dyczkowski voice (Fish)
os.chdir(BASE)
sys.path.insert(0, BASE + "/tools")
from tts_line import TTS_SAY  # noqa

import ast
import unicodedata


def fold(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower())
                   if unicodedata.category(c) != "Mn")


def sanskrit_tokens():
    """Every Sanskrit token TTS must never voice raw: tts_scan stoplist +
    folded book_sanskrit forms. Parsed (never imported) to avoid side effects."""
    src = open(BASE + "/tools/tts_scan.py").read()
    tree = ast.parse(src)
    toks = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "SANSKRIT":
            toks.update(e.value for e in node.value.elts)
    tpl = json.load(open(BASE + "/standard/template_77.json"))
    for t in tpl:
        toks.update(re.findall(r"[A-Za-z]{4,}", fold(t.get("book_sanskrit", ""))))
    return {fold(w) for w in toks}


def spoken(translation):
    s = re.sub(r"[()]", "", translation)
    s = s.replace(" / ", ". ")
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\.\.+", ".", s)
    s = re.sub(r"\bsiva\b", "Siva", s)
    return s


def audit(v, s, skt):
    """Flag any raw-Sanskrit token reaching TTS without a TTS_SAY spoken form."""
    covered = {fold(k) for k in TTS_SAY}
    # Audited loans: Fish voices these acceptably raw (carrier-probe +
    # whisper round-trip 2026-10-28: Maya->"Maya", Siva->"Siva", karma->"karma").
    loan = {fold(w) for w in ("Maya", "Siva", "karma")}
    bad = []
    for w in re.findall(r"[A-Za-z]{4,}", s):
        if fold(w) in skt and fold(w) not in covered and fold(w) not in loan:
            bad.append(w)
    return bad


def main():
    tpl = json.load(open(BASE + "/standard/template_77.json"))
    skt = sanskrit_tokens()
    want = sys.argv[1:] or [t["verse"] for t in tpl]
    deferred, done = [], 0
    for t in tpl:
        v = t["verse"]
        if v not in want:
            continue
        s = spoken(t["translation"])
        bad = audit(v, s, skt)
        if bad:
            deferred.append((v, bad, s))
            continue
        dst = BASE + "/audio/gen/tts/b1b_%s.wav" % v.replace(".", "_")
        r = subprocess.run(["python3", BASE + "/tools/tts_line.py", s, dst,
                            "1.0", THREE],
                           capture_output=True, text=True)
        if r.returncode != 0 or not os.path.exists(dst):
            deferred.append((v, ["TTS-FAIL"], s))
            continue
        done += 1
        print("b1b %s (%ds chars) ok" % (v, len(s)))
    print("rendered=%d deferred=%s" % (done, deferred))
    assert not deferred, deferred


if __name__ == "__main__":
    main()
