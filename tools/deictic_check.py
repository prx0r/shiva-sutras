#!/usr/bin/env python3
"""deictic_check.py — antecedent surfacing from transcript text.
For each Baumer cell cut in the production sheet: prints the clip's
first sentence, flags pronouns/demonstratives, and shows the transcript
lines immediately before the cut so a human can bind or FLAG each one.
Machine surfaces, human verdicts (FLOW_REVIEW Q4 cites this output).

Usage: python3 tools/deictic_check.py
Reads custom/TRACK_F_PRODUCTION.md (Baumer cues) + excavations unit files
for quotes + text/ transcripts.
"""
import re, glob, os

PRON = re.compile(r"\b(he|she|it|they|them|his|her|its|their|this|that|these|those)\b", re.I)

def load_units():
    units = {}
    for path in sorted(glob.glob("excavations/ss*.md") + glob.glob("excavations/dl*.md")):
        sess = os.path.basename(path).removesuffix(".md")
        cur = None
        for line in open(path, encoding="utf-8"):
            m = re.match(r"### (ss\d+-\d+|dl\d+-\d+) —", line)
            if m:
                cur = {"uid": m.group(1), "sess": sess}
                units[cur["uid"]] = cur
            elif cur is not None and line.startswith("- quote:"):
                cur["quote"] = line.partition(":")[2].strip().strip('"')
            elif cur is not None and line.startswith("- timestamp:"):
                cur["ts"] = line.partition(":")[2].strip()
    return units

SESS = {"ss1": "text/shiva_sutras_day_1_introduction_i.txt",
        "ss2": "text/shiva_sutras_day_1_introduction_ii.txt",
        "ss3": "text/shiva_sutras_day_2_introduction_iii.txt",
        "ss4": "text/shiva_sutras_day_2_session_i.txt",
        "ss5": "text/shiva_sutras_day_3_session_i.txt",
        "ss6": "text/shiva_sutras_day_3_session_ii.txt",
        "ss7": "text/shiva_sutras_day_4_session_i.txt",
        "ss8": "text/shiva_sutras_day_4_session_ii_part_1.txt",
        "ss9": "text/shiva_sutras_day_4_session_ii_part_ii.txt",
        "ss10": "text/shiva_sutras_day_5_session_i.txt",
        "ss11": "text/shiva_sutras_day_5_session_ii.txt",
        "ss12": "text/shiva_sutras_day_6_session_i.txt",
        "ss13": "text/shiva_sutras_day_6_session_ii.txt",
        "dl1": "text/shiva_sutras_introduction_dl.txt"}

def ts2s(t):
    h, m, s = t.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)

def main():
    units = load_units()
    sheet = open("custom/TRACK_F_PRODUCTION.md").read()
    for m in re.finditer(r"`(c\d+)_b\d_\d+-\d+\.wav`", sheet):
        pass  # filenames carry spans; resolve via make_essence instead
    import sys
    sys.path.insert(0, "tools")
    import make_essence as ME
    for i, (ci, co, sess, bspans, q, t, p, note) in enumerate(ME.CELLS, 1):
        (bi, bo) = bspans[0]
        lines = open(SESS[sess], encoding="utf-8").read().splitlines()
        stamped = []
        for L in lines:
            mm = re.match(r"\[(\d+:\d+:\d+)\]\s*(.*)$", L)
            if mm:
                stamped.append((ts2s(mm.group(1)), mm.group(2)))
        before = [(sec, x) for sec, x in stamped if sec < bi][-4:]
        first = None
        for b in bspans:
            pass
        # first sentence of the clip ~ first transcript line in window
        inl = [x for sec, x in stamped if bi <= sec <= bo]
        first = inl[0] if inl else "(no transcript line in window)"
        print(f"--- c{i} ({sess} {bi:.0f}s→{bo:.0f}s): {note[:60]}")
        print(f"  FIRST: {first[:150]}")
        for w in set(PRON.findall(first)):
            print(f"  PRONOUN '{w}' — bind from context below or FLAG")
        for sec, x in before:
            print(f"    [{sec}] {x[:120]}")

if __name__ == "__main__":
    main()
