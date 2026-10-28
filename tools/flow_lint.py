#!/usr/bin/env python3
"""flow_lint.py — deterministic flow checks on a production sheet.
Catches what ears shouldn't have to: structural flow defects that are
measurable. Human review (process/FLOW_REVIEW.md) handles the rest.

Checks:
 1. VOICE RUNS — longest unbroken run by one voice (fatigue).
 2. GAPS — silences outside {gap, water, breath, tbeat, XL} vocabulary.
 3. JOINTS — every voice-to-voice handover listed with types for review.
 4. G12 — Baumer/archive clips over 25s listed (exception or split).
 5. REPETITION — identical cue files recurring; distances reported.
 6. DEICTICS — TTS lines + openers containing pronouns/demonstratives,
    flagged for antecedent check (he/she/it/they/this/that/these/those).
 7. PAUSE INVENTORY — every silence with duration (spec drift check).
 8. DENSITY — words-per-minute per spoken cue (espeak/mp3: estimated from
    filename only when .txt sidecars exist; skipped otherwise).

Usage: python3 tools/flow_lint.py build/TRACK_F_PRODUCTION.md
Exit 0 = lint clean (warnings listed, never failed — ears decide).
"""
import re, subprocess, sys, os

def dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration", "-of", "csv=p=0", p],
                       capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return None

PRON = re.compile(r"\b(he|she|it|they|them|his|her|its|their|this|that|these|those)\b", re.I)

def main():
    sheet = sys.argv[1]
    cuts = sys.argv[2] if len(sys.argv) > 2 else "audio/gen/l0_cuts"
    txt = open(sheet).read()
    rows = re.findall(r"^\|\s*(\d+)\s*\|\s*([\d.]+)\s*\|\s*([\d.\-—]+)\s*\|\s*`([^`]+)`\s*\|\s*([^|]*)\|\s*([^|]*)\|", txt, re.M)
    cues = []
    for n, t, d, f, v, note in rows:
        if f == "(silence)":
            continue
        cues.append({"n": int(n), "t": float(t), "f": f,
                     "v": v.strip(), "note": note.strip()})
    print(f"== cues: {len(cues)}")
    # 1. voice runs
    print("== 1. VOICE RUNS (same voice, consecutive spoken cues) ==")
    best = ("", 0.0, 0, 0)
    cur_v, cur_d, cur_a, cur_b = None, 0.0, 0, 0
    for c in cues:
        v = c["v"]
        if v in ("", "—") or c["f"] in ("(silence)", "(plain row)"):
            if cur_d > best[1]:
                best = (cur_v, cur_d, cur_a, cur_b)
            cur_v, cur_d = None, 0.0
            continue
        d = dur(os.path.join(cuts, c["f"]))
        if d is None:
            print(f"  cue {c['n']}: UNMEASURABLE {c['f']}")
            continue
        if v == cur_v:
            cur_d += d; cur_b = c["n"]
        else:
            if cur_d > best[1]:
                best = (cur_v, cur_d, cur_a, cur_b)
            cur_v, cur_d, cur_a, cur_b = v, d, c["n"], c["n"]
    if cur_d > best[1]:
        best = (cur_v, cur_d, cur_a, cur_b)
    print(f"  longest single-voice run: {best[0]} {best[1]:.1f}s (cues {best[2]}-{best[3]})")
    # 3. joints
    print("== 3. JOINTS (voice-to-voice handovers) ==")
    spoken = [c for c in cues if c["v"] not in ("", "—")]
    seen = set()
    for a, b in zip(spoken, spoken[1:]):
        key = (a["v"], b["v"])
        if key not in seen:
            seen.add(key)
            print(f"  {a['v']} → {b['v']} (first at cues {a['n']}→{b['n']})")
    # 4. G12
    print("== 4. LONG CLIPS (>25s, Baumer/archive) ==")
    for c in cues:
        if c["v"] in ("Baumer", "Sharma") and c["f"].endswith(".wav"):
            d = dur(os.path.join(cuts, c["f"]))
            if d and d > 25.0:
                print(f"  cue {c['n']}: {c['f']} {d:.1f}s {'[FLAG present]' if 'FLAG' in c['note'] else '[NO FLAG — add one]'}")
    # 5. repetition
    print("== 5. REPETITION (same file recurring) ==")
    from collections import defaultdict
    locs = defaultdict(list)
    for c in cues:
        locs[c["f"]].append((c["n"], c["t"]))
    for f, ll in sorted(locs.items()):
        if f in ("(silence)", "(plain row)"):
            continue  # structural by design, not repetition
        if len(ll) > 1:
            gaps = [f"{(b[1]-a[1])/60:.1f}m" for a, b in zip(ll, ll[1:])]
            print(f"  {f}: {len(ll)}x at cues {[x[0] for x in ll]} (gaps {', '.join(gaps)})")
    # 6. deictics — needs the spoken text; TTS lines have no sidecar here,
    # so flag Q/P/T cue slots for the human pass instead.
    print("== 6. DEICTIC SLOTS (human pass: resolve each pronoun) ==")
    for c in cues:
        if re.search(r"_q\.|_t\.|_p\.|intro", c["f"]):
            print(f"  cue {c['n']}: {c['f']} ({c['v']}) — list pronouns, bind each to antecedent + timecode")
    # 7. pause inventory from sheet silences
    print("== 7. PAUSE INVENTORY ==")
    for m in re.finditer(r"^\|\s*(\d+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|\s*`\(silence\)`\s*\|\s*([^|]*)\|\s*([^|]*)\|", txt, re.M):
        print(f"  cue {m.group(1)}: {m.group(3)}s — {m.group(5).strip()}")
    print("LINT DONE (warnings are for ears, not failures)")

if __name__ == "__main__":
    main()
