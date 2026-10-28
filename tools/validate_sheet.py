#!/usr/bin/env python3
"""validate_sheet.py — the sheet is the product. Validates ANY production
sheet (Standard or Custom compilation) without rendering audio.

Checks:
 1. Every `cue` file exists (cuts dir) and its measured duration matches
    the sheet's dur column (±0.15s).
 2. Timecodes accumulate: each t_in == prev t_in + prev dur (±0.05s).
 3. Stated total runtime matches final timecode (±1s).
 4. Required sections present: handover audit + FX/pause vocabulary.
 5. Reports FLAGs (ear-session decisions) — listed, never failed.

Usage: python3 tools/validate_sheet.py custom/TRACK_F_PRODUCTION.md [cuts_dir]
Exit 0 = sheet is production-ready. Render is final-final and out of scope.
"""
import os, re, subprocess, sys

def dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration", "-of", "csv=p=0", p],
                       capture_output=True, text=True)
    return float(r.stdout.strip())

def maxvol(p):
    # M25: duration gates passed a silent master. Every cue file must
    # contain actual signal: max volume above -45 dBFS.
    r = subprocess.run(["ffmpeg", "-nostats", "-v", "info", "-i", p,
                        "-af", "volumedetect", "-f", "null", "-"],
                       capture_output=True, text=True)
    m = re.search(r"max_volume: ([\-\d.]+) dB", r.stderr)
    return float(m.group(1)) if m else -999.0

def main():
    sheet = sys.argv[1]
    cuts = sys.argv[2] if len(sys.argv) > 2 else "audio/gen/custom/l0_cuts"
    txt = open(sheet).read()
    rows = re.findall(r"^\|\s*(\d+)\s*\|\s*([\d.]+)\s*\|\s*([\d.\-—]+)\s*\|\s*`([^`]+)`\s*\|\s*([^|]*)\|\s*([^|]*)\|", txt, re.M)
    sil = re.findall(r"^\|\s*(\d+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|\s*`\(silence\)`\s*\|", txt, re.M)
    if not rows and not sil:
        print("FAIL: no cue rows parsed"); sys.exit(1)
    events = []
    for n, t, d, f, v, note in rows:
        if f in ("(silence)", "(plain row)"):
            continue  # text-only rows: silence beds (durations live in sil parse), unspoken plains (manifest/on-screen only)
        events.append((int(n), float(t), f, v.strip(), note.strip()))
    for n, t, d in sil:
        events.append((int(n), float(t), None, "", "silence"))
    # silence durations: re-parse (the silence regex above captured dur)
    sil_d = {int(n): float(d) for n, t, d in sil}
    fail = 0
    t_expect = 0.0
    for n, t, f, v, note in sorted(events):
        if f is None:
            d = sil_d[n]
        else:
            p = f if os.path.isabs(f) else os.path.join(cuts, f)
            if not os.path.exists(p):
                print(f"FAIL cue {n}: missing file {f}"); fail = 1; continue
            d = dur(p)
            # stated dur check
            m = re.search(r"^\|\s*%d\s*\|\s*[\d.]+\s*\|\s*([\d.]+)\s*\|" % n, txt, re.M)
            stated = float(m.group(1))
            if abs(d - stated) > 0.15:
                print(f"FAIL cue {n}: file {d:.2f}s vs sheet {stated:.2f}s"); fail = 1
        if abs(t - t_expect) > 0.05:
            print(f"FAIL cue {n}: t_in {t:.2f} vs accumulated {t_expect:.2f}"); fail = 1
        t_expect += d
    m = re.search(r"Total runtime: .*?\(([\d.]+)s\)", txt)
    if m and abs(float(m.group(1)) - t_expect) > 1.0:
        print(f"FAIL total: sheet states {m.group(1)}s, cues sum {t_expect:.1f}s"); fail = 1
    for section in ["Handover audit", "FX"]:
        if section not in txt:
            print(f"FAIL: missing section '{section}'"); fail = 1
    flags = re.findall(r"\[FLAG\][^|\n]*", txt)
    print(f"cues: {len(events)} · runtime: {t_expect:.1f}s · FLAGs open: {len(flags)}")
    for f in flags:
        print(f"  OPEN {f.strip()}")
    # audibility: every non-silence cue must carry signal (M25)
    _PADS = {"gap.wav", "water.wav", "breath.wav",
             "breath3.wav", "tbeat.wav", "xl5.wav", "xl6.wav"}
    for n, t, f, v, note in sorted(events):
        if f is None or f in _PADS:
            continue
        pth = f if os.path.isabs(f) else os.path.join(cuts, f)
        if not os.path.exists(pth):
            continue  # already failed above
        mv = maxvol(pth)
        if mv < -45.0:
            print(f"FAIL cue {n}: {f} is SILENT (max {mv:.1f} dB) — M25")
            fail = 1
    if fail:
        print("SHEET NOT READY — fix and re-render")
        sys.exit(1)
    print("SHEET READY ✓ (render is final-final — separate gate, owner ears)")

if __name__ == "__main__":
    main()
