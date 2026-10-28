#!/usr/bin/env python3
"""Batch-transcribe the Lakshmanjoo study set (79 mp3s, ~16h) with local
faster-whisper base. Output matches the Baumer text/ shape:
  text/lak_*.txt  — [HH:MM:SS] segment lines (quote source-of-truth)
  transcripts/lak_*.segments.json — float-timestamp segments (locate pass)
Usage: nohup python3 tools/lak_transcribe.py >> /tmp/opencode/lak_transcribe.log 2>&1 &
Idempotent: skips files whose .txt already exists."""
import glob, json, os, re, sys

BASE = "/home/ubuntu/shiva-sutras"
SRC = "/home/ubuntu/shiva-study-set"

def slug(fn):
    s = fn.replace("Shiva Sutras ", "").replace(".mp3", "").strip()
    s = (s.replace(" part 1", "_p1").replace(" part 2", "_p2")
           .replace("Introduction", "intro").replace("Conclusion", "conclusion"))
    s = re.sub(r"[^0-9a-zA-Z]+", "_", s).strip("_").lower()
    return f"lak_{s}"

def stamp(t):
    t = int(t)
    return f"[{t//3600:02d}:{(t%3600)//60:02d}:{t%60:02d}]"

def main():
    from faster_whisper import WhisperModel
    model = WhisperModel("base", device="cpu", compute_type="int8")
    files = sorted(glob.glob(os.path.join(SRC, "*.mp3")))
    print(f"files: {len(files)}", flush=True)
    done, skipped = 0, 0
    for i, f in enumerate(files, 1):
        out_txt = os.path.join(BASE, "text", slug(os.path.basename(f)) + ".txt")
        out_json = os.path.join(BASE, "transcripts", slug(os.path.basename(f)) + ".segments.json")
        if os.path.exists(out_txt) and os.path.getsize(out_txt) > 0:
            skipped += 1
            continue
        print(f"[{i}/{len(files)}] {os.path.basename(f)}", flush=True)
        try:
            segments, _ = model.transcribe(f, beam_size=5, vad_filter=True)
            segs = [{"t": round(s.start, 2), "end": round(s.end, 2),
                     "text": s.text.strip()} for s in segments if s.text.strip()]
            with open(out_txt, "w") as fh:
                for s in segs:
                    fh.write(f"{stamp(s['t'])} {s['text']}\n")
            json.dump({"source": f, "engine": "faster-whisper-base",
                       "segments": segs}, open(out_json, "w"), ensure_ascii=False)
            done += 1
            print(f"  -> {os.path.basename(out_txt)} ({len(segs)} segs)", flush=True)
        except Exception as e:
            print(f"  ERROR: {e}", flush=True)
    print(f"DONE: {done} transcribed, {skipped} skipped", flush=True)

if __name__ == "__main__":
    main()
