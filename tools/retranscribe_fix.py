#!/usr/bin/env python3
"""One-shot: re-transcribe garbled Lakshmanjoo transcripts with language='en'.
The batch run (lak_transcribe.py, no language set) let whisper auto-detect per
file and produced wrong-script garbage (Arabic/Greek/CJK) on Sanskrit-heavy
openings — 6 files overlap B1/A windows (M39 follow-up). Same output format
(text/*.txt stamped lines + transcripts/*.segments.json); overwrites in place.
Usage: python3 tools/retranscribe_fix.py [slug ...]  (default: the 9 known-bad)
CAUTION: overwrites committed transcripts. Diff before committing.
"""
import glob
import json
import os
import re
import sys

BASE = "/home/ubuntu/shiva-sutras"
os.chdir(BASE)

BAD_DEFAULT = ["lak_1_14", "lak_2_2", "lak_3_11", "lak_3_21", "lak_3_34",
               "lak_3_37", "lak_1_19", "lak_1_8_10", "lak_3_17", "lak_3_9",
               "lak_3_42"]


def slug_to_mp3(slug):
    core = slug[len("lak_"):]
    table = {"1_8_10": "Shiva Sutras 1.8-10.mp3",
             "2_7_p1": "Shiva Sutras 2.7 part 1.mp3",
             "2_7_p2": "Shiva Sutras 2.7 part 2.mp3",
             "intro": "Shiva Sutras Introduction.mp3",
             "conclusion": "Shiva Sutras Conclusion.mp3",
             "3_intro": "Shiva Sutras 3. Introduction.mp3"}
    if core in table:
        return os.path.join("/home/ubuntu/shiva-study-set", table[core])
    m = re.match(r"(\d+)_(\d+)$", core)
    if m:
        return os.path.join("/home/ubuntu/shiva-study-set",
                             f"Shiva Sutras {m.group(1)}.{m.group(2)}.mp3")
    raise ValueError(slug)


def stamp(t):
    t = int(t)
    return f"[{t//3600:02d}:{(t%3600)//60:02d}:{t%60:02d}]"


def main():
    from faster_whisper import WhisperModel  # noqa (lazy: heavy import)
    want = sys.argv[1:] or BAD_DEFAULT
    model = WhisperModel("base", device="cpu", compute_type="int8")
    for slug in want:
        src = slug_to_mp3(slug)
        assert os.path.exists(src), src
        print(f"transcribing {slug} <- {os.path.basename(src)}", flush=True)
        segments, _ = model.transcribe(src, beam_size=5, vad_filter=True,
                                       language="en")
        segs = [{"t": round(s.start, 2), "end": round(s.end, 2),
                 "text": s.text.strip()} for s in segments if s.text.strip()]
        with open(BASE + f"/text/{slug}.txt", "w") as fh:
            for s in segs:
                fh.write(f"{stamp(s['t'])} {s['text']}\n")
        json.dump({"source": src, "engine": "faster-whisper-base+lang-en",
                   "segments": segs},
                  open(BASE + f"/transcripts/{slug}.segments.json", "w"),
                  ensure_ascii=False)
        print(f"  -> text/{slug}.txt ({len(segs)} segs)", flush=True)
    print("done — diff text/ + transcripts/ before committing", flush=True)


if __name__ == "__main__":
    main()
