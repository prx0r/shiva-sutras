#!/usr/bin/env python3
"""DO NOT USE — non-convergent version kept for history (see M41).
This tool derives its whisper search region from the CURRENT manifest windows,
so every --apply moves the edges again (45 changed, then 18 more, never zero).
Use tools/recut_sentence.py instead (anchors to immutable unit windows +
transcript sentences, then measures; re-run converges to zero changes).
Kept so the failure mode stays visible; running it will silently drift every
cut in custom/manifests/manifest_s*_A.json."""

"""M40 implementation: set A-clip edges from MEASURED word times, never interpolated
transcript stamps. Per beat: whisper-transcribe source around the window with word
timestamps, fuzzy-locate the quote's first/last words, set head = first_word.start
- 0.4s, tail = last_word.end + 0.6s (trimmed back if next speech starts sooner).
Writes manifests in place. Reports per-beat old->new + flags (unlocated quotes
keep old windows UNTOUCHED for human verdict).
Usage: python3 tools/align_cuts.py [--apply]  (default: dry-run report)
Reference: unit quotes are verbatim; ASR garble on names/Sanskrit is expected —
fuzzy match (difflib) with a 0.6 floor; below that, FLAG, don't guess."""
import difflib
import glob
import json
import os
import re
import subprocess
import sys

BASE = "/home/ubuntu/shiva-sutras"
os.chdir(BASE)
sys.path.insert(0, BASE + "/tools")
from build_manifests import MP3, parse_units, norm  # noqa

SESS_TXT_IGNORED = True  # transcript text unused; quotes come from units


def wrds(s):
    return norm(s).split()


def ustamp(u):
    m = re.search(r"\[(\d+:\d+:\d+)\]-->\[(\d+:\d+:\d+)\]", u.get("timestamp", ""))
    if not m:
        return None, None
    def _t(t):
        h, mnt, s = t.split(":")
        return int(h) * 3600 + int(mnt) * 60 + float(s)
    return _t(m.group(1)), _t(m.group(2))


def locate(words, needle, floor=0.6):
    """Best fuzzy alignment of needle word-list inside words; returns (i,j,score)."""
    nw = [w["w"] for w in words]
    best, bi = None, 0.0
    n = len(needle)
    for i in range(max(1, len(nw) - n - 6)):
        for ln in (n, n + 1, n + 2, n - 1):
            if ln <= 0 or i + ln > len(nw):
                continue
            seg = nw[i:i + ln]
            r = difflib.SequenceMatcher(None, needle, seg).ratio()
            if r > bi:
                bi, best = r, (i, i + ln)
    return best + (bi,) if best and bi >= floor else (None, None, bi)


def main():
    from faster_whisper import WhisperModel  # noqa (lazy: heavy import)
    apply = "--apply" in sys.argv
    model = WhisperModel("base", device="cpu", compute_type="int8")
    units = parse_units()
    changed, flags, same = 0, [], 0
    for f in sorted(glob.glob(BASE + "/custom/manifests/manifest_s*_A.json")):
        d = json.load(open(f))
        dirty = False
        for b in d["beats"]:
            uid = b["uid"]
            q = wrds(units[uid]["quote"])
            if len(q) < 6:
                flags.append((uid, "quote-too-short"))
                continue
            src = os.path.join(BASE, b["mp3"])
            a, bb = b["t_in"], b["t_out"]
            # FIXED region from the UNIT window (immutable) — never from the
            # current manifest edges (M41 drift machine). Same input every run.
            u1, u2 = ustamp(units[uid])
            if u1 is None:
                flags.append((uid, "no-unit-span"))
                continue
            lo, hi = max(0, u1 - 15), u2 + 25
            tmp = "/tmp/opencode/align_%s.wav" % uid.replace("-", "_")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(lo), "-to", str(hi),
                            "-i", src, tmp], check=True)
            segs, _ = model.transcribe(tmp, beam_size=1, language="en", word_timestamps=True)
            words = [{"t": round(lo + w.start, 2), "e": round(lo + w.end, 2), "w": w.word.strip(".,!?\"' ").lower()}
                     for s in segs for w in (s.words or []) if w.word.strip()]
            words = [w for w in words if w["w"]]
            if not words:
                flags.append((uid, "no-words"))
                continue
            i0, _, s0 = locate(words, q[:8])
            i1, j1, s1 = locate(words, q[-8:])
            if i0 is None or i1 is None:
                flags.append((uid, "unlocated s=%.2f/%.2f" % (s0 or 0, s1 or 0)))
                continue
            nh = max(lo, round(words[i0]["t"] - 0.4, 1))
            # tail: last quote word end + decay, pulled back if next speech crowds
            end_t = words[j1 - 1]["e"] if j1 - 1 < len(words) else words[-1]["e"]
            nt = round(end_t + 0.6, 1)
            if j1 < len(words) and words[j1]["t"] < nt + 0.15:
                nt = round(max(end_t + 0.1, words[j1]["t"] - 0.15), 1)
                flags.append((uid, "crowded-tail %.1f" % nt))
            # M41b guard: stay in the unit's neighborhood (transcript lag is
            # seconds, not minutes). A tail far past the unit span means the
            # fuzzy match locked onto a repeat/chant — keep old, flag for hand.
            u1, u2 = ustamp(units[uid])
            if u1 is not None and (nt > u2 + 15 or nh < u1 - 15):
                flags.append((uid, "out-of-neighborhood [%.1f,%.1f] vs unit [%.0f,%.0f] — kept old" % (nh, nt, u1, u2)))
                continue
            if nt - nh < 2:
                flags.append((uid, "degenerate"))
                continue
            if abs(nh - a) > 0.05 or abs(nt - bb) > 0.05:
                print("%s %s [%.1f,%.1f] -> [%.1f,%.1f] s=%.2f/%.2f" %
                      (d["section"], uid, a, bb, nh, nt, s0, s1))
                if apply:
                    b["t_in"], b["t_out"] = nh, nt
                    b["dur"] = round(nt - nh, 1)
                    dirty = True
                    changed += 1
            else:
                same += 1
        if apply and dirty:
            json.dump(d, open(f, "w"), ensure_ascii=False, indent=1)
    print(("APPLIED " if apply else "DRY-RUN ") +
          "changed=%d unchanged=%d flags=%d" % (changed, same, len(flags)))
    for u, m in flags:
        print("  FLAG", u, m)


if __name__ == "__main__":
    main()
