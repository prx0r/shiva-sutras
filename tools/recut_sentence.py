#!/usr/bin/env python3
"""Re-cut A-clip windows to sentence-complete, silence-snapped bounds (M39).
Per beat: expand to enclosing sentence boundaries (terminal punctuation, caps:
back <=12s, fwd <=20s, never crossing neighbour windows), snap edges inside
silencedetect gaps (>=0.15s clear of words). Expansion-only: original windows
stay contained. Writes manifests in place; reports per-beat old->new + flags.
Usage: python3 tools/recut_sentence.py [--apply]  (default: dry-run report)
Rule: verify the report, then --apply, then rebuild + qa_std + listen sample."""
import glob, json, os, re, subprocess, sys

BASE = "/home/ubuntu/shiva-sutras"
os.chdir(BASE)

SESS_TXT = {'ss1': 'text/shiva_sutras_day_1_introduction_i.txt',
 'ss2': 'text/shiva_sutras_day_1_introduction_ii.txt',
 'ss3': 'text/shiva_sutras_day_2_introduction_iii.txt',
 'ss4': 'text/shiva_sutras_day_2_session_i.txt',
 'ss5': 'text/shiva_sutras_day_3_session_i.txt',
 'ss6': 'text/shiva_sutras_day_3_session_ii.txt',
 'ss7': 'text/shiva_sutras_day_4_session_i.txt',
 'ss8': 'text/shiva_sutras_day_4_session_ii_part_1.txt',
 'ss9': 'text/shiva_sutras_day_4_session_ii_part_ii.txt',
 'ss10': 'text/shiva_sutras_day_5_session_i.txt',
 'ss11': 'text/shiva_sutras_day_5_session_ii.txt',
 'ss12': 'text/shiva_sutras_day_6_session_i.txt',
 'ss13': 'text/shiva_sutras_day_6_session_ii.txt',
 'dl1': 'text/shiva_sutras_introduction_dl.txt'}
import sys as _s
_s.path.insert(0, BASE + "/tools")
from build_manifests import MP3, parse_units, norm  # noqa (sess->mp3 map, quotes)

MP3INV = {v: k for k, v in MP3.items()}


def ts(s):
    h, m, sec = s.split(":")
    return int(h) * 3600 + int(m) * 60 + float(sec)


def load(sess):
    out = []
    for raw in open(SESS_TXT[sess], encoding="utf-8"):
        m = re.match(r"\[(\d+:\d+:\d+)\] ?(.*)$", raw)
        if m:
            out.append((ts(m.group(1)), m.group(2).strip()))
    return out


GAPS = {}


def gaps(mp3):
    if mp3 not in GAPS:
        r = subprocess.run(["ffmpeg", "-v", "info", "-i", os.path.join(BASE, mp3),
                            "-af", "silencedetect=noise=-32dB:d=0.15",
                            "-f", "null", "-"], capture_output=True, text=True)
        gs = re.findall(r"silence_start: ([\d.]+)", r.stderr)
        ge = re.findall(r"silence_end: ([\d.]+)", r.stderr)
        GAPS[mp3] = [(float(a), float(b)) for a, b in zip(gs, ge)]
    return GAPS[mp3]


def snap(mp3, target, side):
    """Place edge inside a silence gap near target; else target (flagged)."""
    best, bd = None, 1.5
    for a, b in gaps(mp3):
        if b - a < 0.3:
            continue
        cand = min(max(target, a + 0.15), b - 0.15)
        d = abs(cand - target)
        if d < bd:
            best, bd = (cand, a, b), d
    if best:
        return round(best[0], 1), None
    return round(target, 1), "no-silence-near-%.1f" % target


WMODEL = None
WCACHE = {}


def _words(mp3, lo, hi):
    """Whisper word timestamps for [lo,hi] (cached per file+span)."""
    global WMODEL
    if WMODEL is None:
        from faster_whisper import WhisperModel  # noqa (lazy: heavy import)
        WMODEL = WhisperModel("base", device="cpu", compute_type="int8")
    key = (mp3, round(lo, 1), round(hi, 1))
    if key not in WCACHE:
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tf:
            tmp = tf.name
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(max(0, lo)),
                        "-to", str(hi), "-i", os.path.join(BASE, mp3), tmp], check=True)
        segs, _ = WMODEL.transcribe(tmp, beam_size=1, language="en", word_timestamps=True)
        out = []
        for s in segs:
            for w in (s.words or []):
                ww = norm(w.word.strip(".,!?\"' "))
                if ww:
                    out.append((round(lo + w.start, 2), round(lo + w.end, 2), ww))
        WCACHE[key] = out
        try:
            os.remove(tmp)
        except OSError:
            pass
    return WCACHE[key]


def main():
    apply = "--apply" in sys.argv
    units = parse_units()
    changed, flags = 0, []
    LINES = {}
    # global neighbour map (across sections: same mp3 may serve many sections)
    ALLB = []
    for _f in sorted(glob.glob(BASE + "/custom/manifests/manifest_s*_A.json")):
        _d = json.load(open(_f))
        for _b in _d["beats"]:
            ALLB.append(_b)
    for f in sorted(glob.glob(BASE + "/custom/manifests/manifest_s*_A.json")):
        d = json.load(open(f))
        for b in d["beats"]:
            mp3 = b["mp3"]
            sess = MP3INV.get(os.path.basename(mp3)[:-4], None)
            if sess is None:  # dl1
                sess = "dl1" if "Introduction" in mp3 else None
            assert sess, mp3
            if sess not in LINES:
                LINES[sess] = load(sess)
            lines = LINES[sess]
            a, bb = b["t_in"], b["t_out"]
            # quote-anchored run: candidates containing the quote; pick max
            # overlap with the original window (rolling-cue dupes) then shortest
            q = norm(units[b["uid"]]["quote"])
            cands = []
            for i in range(len(lines)):
                if lines[i][0] < a - 120:
                    continue
                if lines[i][0] > bb + 120:
                    break
                acc = ""
                for j in range(i, min(i + 60, len(lines))):
                    acc = (acc + " " + norm(lines[j][1])).strip() if j > i else norm(lines[j][1])
                    if q in acc:
                        cands.append((i, j))
                        break
            if not cands:
                flags.append((b["uid"], "quote-not-relocated"))
                continue
            def ovr(c):
                i, j = c
                return min(lines[j][0], bb) - max(lines[i][0], a), -(lines[j][0] - lines[i][0])
            i0, i1 = sorted(cands, key=ovr, reverse=True)[0]
            # expand back to sentence start (<=8s before run start)
            t0 = lines[i0][0]
            while i0 > 0:
                if re.search(r"[.!?]['\"]?\s*$", lines[i0 - 1][1]):
                    break
                if t0 - lines[i0 - 1][0] > 8:
                    break
                i0 -= 1
            # expand fwd to sentence end (<=12s past run end)
            t1 = lines[i1][0]
            while i1 < len(lines) - 1:
                if re.search(r"[.!?]['\"]?\s*$", lines[i1][1]):
                    break
                if lines[i1 + 1][0] - t1 > 12:
                    break
                i1 += 1
            # neighbour guard: never cross adjacent beat windows (same mp3, any section)
            sibs = sorted([x for x in ALLB if x["mp3"] == mp3 and x is not b],
                          key=lambda x: x["t_in"])
            pre = max([x["t_out"] for x in sibs if x["t_out"] <= a] or [0])
            nxt = min([x["t_in"] for x in sibs if x["t_in"] >= bb] or [9e9])
            # M41: anchor edges to MEASURED word times, not transcript stamps.
            # Transcript defines WHAT (sentence span i0..i1); whisper says WHEN.
            w_first = norm(lines[i0][1]).split()
            w_last = norm(lines[i1][1]).split()
            if not w_first or not w_last:
                flags.append((b["uid"], "empty-boundary-line"))
                continue
            wf, wl = w_first[0], w_last[-1]
            lo = max(0.0, lines[i0][0] - 5)
            hi = (lines[i1 + 1][0] if i1 + 1 < len(lines) else lines[i1][0] + 10) + 5
            try:
                wds = _words(os.path.join(BASE, mp3), lo, hi)
            except Exception as e:
                flags.append((b["uid"], "whisper-fail %s" % str(e)[:40]))
                continue
            fi = next((i for i, w in enumerate(wds) if w[2] == wf and w[0] - lo < 12), None)
            li = None
            for i in range(len(wds) - 1, -1, -1):
                if wds[i][2] == wl and hi - wds[i][0] < 20:
                    li = i
                    break
            if fi is None or li is None or li <= fi:
                flags.append((b["uid"], "boundary-not-found %s..%s" % (wf, wl)))
                continue
            nt_in = max(wds[fi][0] - 0.3, pre + 0.5)
            nt_out = min(wds[li][1] + 0.4, nxt - 0.5)
            if nt_out <= nt_in + 1:
                flags.append((b["uid"], "guard-collapse, kept"))
                continue
            st_in, f1 = snap(mp3, nt_in, "in")
            st_out, f2 = snap(mp3, nt_out, "out")
            if f1 or f2:
                flags.append((b["uid"], f1 or f2))
            if not (st_in <= a + 0.6 and st_out >= bb - 0.6):
                flags.append((b["uid"], "containment-fail [%.1f,%.1f]" % (st_in, st_out)))
                continue
            if st_out - st_in > 180:
                flags.append((b["uid"], "over-180s [%.1f,%.1f]" % (st_in, st_out)))
                continue
            if abs(st_in - a) > 0.05 or abs(st_out - bb) > 0.05:
                print("%s %s [%.1f,%.1f] -> [%.1f,%.1f]" % (d["section"], b["uid"], a, bb, st_in, st_out))
                if apply:
                    b["t_in"], b["t_out"] = st_in, st_out
                    b["dur"] = round(st_out - st_in, 1)
                    changed += 1
        if apply:
            json.dump(d, open(f, "w"), ensure_ascii=False, indent=1)
    print(("APPLIED " if apply else "DRY-RUN ") + "changed=%d flags=%d" % (changed, len(flags)))
    for u, f in flags[:20]:
        print("  FLAG", u, f)


if __name__ == "__main__":
    main()
