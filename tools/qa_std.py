#!/usr/bin/env python3
"""Structural QA sweep for Standard manifests (no ears needed).
Per verse, per piece, asserts the fix classes from the session log:
  F1 wrong-audio-file (M34): uid piece src must equal the unit sess MP3 map
  F2 window-vs-unit: piece window must overlap the unit window (>=50% of the
     smaller, within 8s pad tolerance)
  F3 dead-head onset (M27): file-local piece starting within 1.0s of a segment
     start whose first word is filler (and/so/now/but/then/uh/um/well)
  F4 mid-sentence cut (M29): t_out strands >1.0s of a segment whose text does
     not end terminal (.?!), and the next segment continues lowercase-discourse
  F5 bounds: 0 < t_in < t_out, dur in [0.5, 900], t_out <= file duration
  F6 schema: b1_status in enum, roles non-empty, TTS pieces have real files
     (M28: verify-preset confabulation on partials — structural only here)
Usage: python3 tools/qa_std.py [verse ...]  (default: all 77)
Output: build/QA_SWEEP_<date>.json + summary lines. FAIL = rebuild, FLAG =
human verdict at the ear session. Transcript-backed only; ears decide the rest.
"""
import json, glob, os, re, subprocess, sys, datetime

BASE = "/home/ubuntu/shiva-sutras"
os.chdir(BASE)
sys.path.insert(0, BASE + "/tools")
from build_manifests import MP3, parse_units  # noqa

ENUM = {"his-verified", "his-prov", "sharma", "cf-done", "cf-owed"}
FILLER = {"and", "so", "now", "but", "then", "uh", "um", "well", "actually"}
TERMINAL = set(".?!\"'")


def ts2s(t):
    h, m, s = t.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def unit_span(u):
    m = re.search(r"\[(\d+:\d+:\d+)\]-->\[(\d+:\d+:\d+)\]", u.get("timestamp", ""))
    return (ts2s(m.group(1)), ts2s(m.group(2))) if m else (None, None)


DURCACHE = {}


def duration(src):
    if src not in DURCACHE:
        if not os.path.exists(src):
            DURCACHE[src] = None
        else:
            r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                "format=duration", "-of",
                                "default=noprint_wrappers=1:nokey=1", src],
                               capture_output=True, text=True)
            try:
                DURCACHE[src] = float(r.stdout.strip())
            except ValueError:
                DURCACHE[src] = None
    return DURCACHE[src]


SEGCACHE = {}


def segments_for(src):
    """Segments for a source mp3: lak via transcripts/lak_*.segments.json."""
    if src not in SEGCACHE:
        SEGCACHE[src] = None
        m = re.search(r"Shiva Sutras ([\d._]+)\.mp3", os.path.basename(src))
        if m:
            slug = m.group(1).replace(".", "_")
            sp = "transcripts/lak_%s.segments.json" % slug
            if os.path.exists(sp):
                SEGCACHE[src] = json.load(open(sp))["segments"]
    return SEGCACHE[src]


def overlap(a1, a2, b1, b2):
    return max(0, min(a2, b2) - max(a1, b1))


def check_verse(v, man, units):
    fails, flags = [], []
    tag = v.replace(".", "_")

    def F(code, msg):
        fails.append("%s %s" % (code, msg))

    def G(code, msg):
        flags.append("%s %s" % (code, msg))

    # F6 schema
    if man.get("b1_status") not in ENUM:
        F("F6", "b1_status %r not in enum" % man.get("b1_status"))
    for L, pcs in man.get("layers", {}).items():
        for i, p in enumerate(pcs):
            where = "%s/%s#%d(%s)" % (v, L, i, p.get("role"))
            if not p.get("role"):
                F("F6", "%s missing role" % where)
            a, b = p.get("t_in", -1), p.get("t_out", -1)
            # F5 bounds (prebuilt-copy TTS pieces carry [0,0] + file by design)
            if a == 0 and b == 0 and p.get("file", "").endswith(".wav"):
                fp0 = p["file"] if os.path.isabs(p["file"]) else os.path.join(BASE, p["file"])
                if not os.path.exists(fp0):
                    F("F6", "%s prebuilt TTS missing %s" % (where, p["file"]))
                continue
            if not (0 <= a < b):
                F("F5", "%s bad bounds [%s,%s]" % (where, a, b))
                continue
            if not (0.5 <= b - a <= 900):
                F("F5", "%s suspect dur %.1fs" % (where, b - a))
            src = p.get("src", man["src"]) if not p.get("file", "").endswith(".wav") else None
            if src is None:
                fp = p["file"] if os.path.isabs(p["file"]) else os.path.join(BASE, p["file"])
                if not os.path.exists(fp):
                    F("F6", "%s prebuilt TTS missing %s" % (where, p["file"]))
                continue
            if not os.path.exists(src):
                F("F5", "%s src missing %s" % (where, src))
                continue
            dur = duration(src)
            if dur and b > dur + 0.5:
                F("F5", "%s t_out %.1f past EOF %.1f" % (where, b, dur))
            # F1/F2 uid pieces (Baumer/dl1 clips in Standard B)
            uid = p.get("uid")
            if uid:
                u = units.get(uid)
                if not u:
                    F("F1", "%s uid %s not in units" % (where, uid))
                else:
                    expect = "audio/%s.mp3" % MP3.get(u["sess"], "?")
                    if os.path.basename(src) != os.path.basename(expect):
                        F("F1", "%s uid %s src %s != map %s (M34)" %
                          (where, uid, os.path.basename(src), os.path.basename(expect)))
                    u1, u2 = unit_span(u)
                    if u1 is not None:
                        ov = overlap(a, b, u1, u2)
                        need = 0.5 * min(b - a, u2 - u1)
                        if ov < need and not (a <= u1 + 8 and b >= u2 - 8):
                            F("F2", "%s window [%.0f,%.0f] vs unit %s [%.0f,%.0f]" %
                              (where, a, b, uid, u1, u2))
            # F3/F4 file-local pieces (his cuts: locate via lak segments)
            elif "sharma" not in os.path.basename(src).lower():
                segs = segments_for(src)
                if segs:
                    pre = [s for s in segs if s["t"] <= a + 1.0 <= s["end"] or
                           abs(s["t"] - a) <= 1.0]
                    if pre:
                        s0 = pre[0]
                        w0 = re.sub(r"[^a-z ]", "", s0["text"].lower().split(" ")[0] if s0["text"] else "")
                        first = (s0["text"].strip().split() or [""])[0].lower().strip(",.")
                        if abs(s0["t"] - a) <= 1.0 and first in FILLER:
                            G("F3", "%s opens on filler %r @%.1f (seg %.1f)" %
                              (where, first, a, s0["t"]))
                    cur = [s for s in segs if s["t"] <= b <= s["end"]]
                    if cur:
                        s1 = cur[0]
                        if s1["end"] - b > 1.0 and not (s1["text"].rstrip()[-1:] in TERMINAL):
                            G("F4", "%s ends mid-segment (%.1fs stranded): %r" %
                              (where, s1["end"] - b, s1["text"][-60:]))
    return fails, flags


def main():
    units = parse_units()
    want = sys.argv[1:] or [t["verse"] for t in
                             json.load(open(BASE + "/build/template_77.json"))]
    report = {}
    nf = ng = 0
    for v in want:
        f = BASE + "/build/std_%s.json" % v.replace(".", "_")
        if not os.path.exists(f):
            report[v] = {"fails": ["F6 manifest missing"], "flags": []}
            nf += 1
            continue
        man = json.load(open(f))
        fails, flags = check_verse(v, man, units)
        report[v] = {"status": man.get("b1_status"), "fails": fails, "flags": flags}
        nf += len(fails) > 0
        ng += len(flags) > 0
        if fails or flags:
            print("== %s [%s] FAIL=%d FLAG=%d" % (v, man.get("b1_status"), len(fails), len(flags)))
            for x in fails + flags:
                print("   ", x[:160])
    day = datetime.date.today().isoformat()
    out = BASE + "/build/QA_SWEEP_%s.json" % day
    json.dump(report, open(out, "w"), ensure_ascii=False, indent=1)
    print("verses=%d with-fails=%d with-flags=%d -> %s" % (len(want), nf, ng, out))


if __name__ == "__main__":
    main()
