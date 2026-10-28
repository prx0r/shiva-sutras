#!/usr/bin/env python3
"""L0 prototype: essay-0 as audio — chant -> card/TTS -> Baumer cell, x6.

Voice order per cell: QUESTION (TTS) -> 2-breath pause -> CHANT (Sharma cut)
-> TRANSLATION (TTS) -> PLAIN (TTS) -> 1.2s -> BAUMER cell cut.
Cells joined with 2.5s water; motto bell 880Hz opens.

Provisional stamp notes: Sharma seeds are proportional splits inside run-on
chant segments (ear-check at render). Baumer windows are the ESSAY0_OUTPUT
verified spans. TTS = edge-tts placeholder until Fish key (SPEAKERS.md).

Usage: python3 tools/make_l0.py   (writes audio/gen/l0_essay0.wav + .mp3)
"""
import os, subprocess, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GEN = os.path.join(BASE, "audio", "gen")
CUTS = os.path.join(GEN, "l0_cuts")
os.makedirs(CUTS, exist_ok=True)
os.makedirs(GEN, exist_ok=True)

def sh(cmd):
    print("+", " ".join(cmd), flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-2000:], flush=True)
        sys.exit(1)

def cut(src, t_in, t_out, dst):
    sh(["ffmpeg", "-v", "error", "-y", "-ss", str(t_in), "-to", str(t_out),
        "-i", src, "-af", ("afade=t=in:st=0:d=0.15,afade=t=out:st={ed:.2f}:d=0.15".format(ed=max(0.3, (t_out - t_in) - 0.15))),
        "-ar", "44100", "-ac", "1", dst])


def _fish_key():
    import re as _re
    for _f in [os.path.expanduser("~/.config/opencode/.env")]:
        try:
            _t = open(_f).read()
        except OSError:
            continue
        _m = _re.search(r"^FISH_API_KEY=(.*)$", _t, _re.M)
        if _m and _m.group(1).strip():
            return _m.group(1).strip()
    return None

# Spoken-form map: display text NEVER changes; only what TTS says.
# (Verified by probe 2026-10-26: model transcribes v2 as "Bhairava".)
TTS_SAY = {"Bhairava": "Bye-ruh-vuh", "bhairava": "bye-ruh-vuh"}

def _fish_tts(text, dst):
    # v1 voice = Fish s2.1-pro-free default voice (human-intelligible).
    # Returns True on success (wav 44.1k mono in place).
    import json as _json, urllib.request as _url
    key = _fish_key()
    if key is None:
        return False
    for _w, _s in TTS_SAY.items():
        text = text.replace(_w, _s)
    body = _json.dumps({"model": "fish-audio/s2.1-pro-free",
                        "input": text, "voice": "",
                        "response_format": "wav"}).encode()
    try:
        req = _url.Request("https://api.fish.audio/compat/v1/audio/speech",
            data=body, headers={"Authorization": f"Bearer {key}",
                                "Content-Type": "application/json"})
        data = _url.urlopen(req, timeout=120).read()
        open(dst + ".fish.wav", "wb").write(data)
        sh(["ffmpeg", "-v", "error", "-y", "-i", dst + ".fish.wav",
            "-af", "aresample=44100,aformat=channel_layouts=mono", dst])
        os.remove(dst + ".fish.wav")
        return True
    except Exception as e:
        print(f"fish tts failed ({str(e)[:100]}), espeak fallback", flush=True)
        return False

def tts(text, dst, voice="en"):
    # v1 placeholder voice: edge-tts is egress-blocked here, Fish needs a
    # key (owner). espeak proves the assembly; swap the engine later —
    # file layout stays identical (SPEAKERS.md: TTS is placeholder only).
    wav = dst + ".wav"
    sh(["espeak", "-v", voice, "-s", "150", "-w", wav, text])
    sh(["ffmpeg", "-v", "error", "-y", "-i", wav,
        "-af", "aresample=44100,aformat=channel_layouts=mono", dst])
    os.remove(wav)

def silence(dur, dst, sr=44100):
    sh(["ffmpeg", "-v", "error", "-y", "-f", "lavfi",
        "-i", f"anullsrc=r={sr}:cl=mono:d={dur}", "-ar", str(sr), "-ac", "1", dst])

def bell(freq, dur, dst):
    sh(["ffmpeg", "-v", "error", "-y", "-f", "lavfi",
        "-i", f"sine=frequency={freq}:duration={dur}",
        "-af", "afade=t=in:d=0.3,afade=t=out:d=0.8,volume=0.4",
        "-ar", "44100", "-ac", "1", dst])

SHARMA = os.path.join(BASE, "audio", "chant", "sharma_siva_sutras_2009.mp3")
MP3 = {"ss3": "sLD0aeV1d3o", "ss4": "KSpk4KO0JY4", "ss12": "r5wTwUNVYOo",
       "ss7": "s2cqHsBcsd4", "ss11": "Xo9aR9GNOio", "ss13": "xseTpOwSx9M"}

def hms(h, m, s):
    return h * 3600 + m * 60 + s

# Chant windows: dip-snapped (silencedetect -28dB/0.12s) near proportional
# splits inside Sharma section runs. Method-honest, ear-check at render.
CELLS = [
    (266.4, 270.4, "ss3", [(hms(1,19,45), hms(1,19,55)), (hms(1,20,26), hms(1,20,32))],
     "What is consciousness?",
     "Consciousness is the Self.", "consciousness is the self"),
    (270.4, 275.9, "ss4", [(hms(0,33,36), hms(0,34,22))],
     "What keeps consciousness from being realised?",
     "Knowledge is bondage.", "knowledge is bondage"),
    (282.7, 287.1, "ss12", [(hms(0,20,18), hms(0,20,30))],
     "How does realisation happen?",
     "Bhairava is upsurge.", "bhairava is upsurge"),
    (318.9, 322.9, "ss7", [(hms(0,22,32), hms(0,23,0))],
     "What does realisation do to experience?",
     "The enjoyer of the three states is the Lord of the Heroes.",
     "the enjoyer of the three states is the lord of the heroes"),
    (392.0, 396.2, "ss11", [(hms(0,50,23), hms(0,50,38))],
     "What does the mind have to do with consciousness?",
     "The mind is Mantra.", "the mind is mantra"),
    (492.5, 498.9, "ss13", [(hms(1,2,58), hms(1,3,9))],
     "What happens after realisation?",
     "The self is the actor.", "the self is the actor"),
]

def main():
    for f in ["SHARMA", *MP3.values()]:
        p = SHARMA if f == "SHARMA" else os.path.join(BASE, "audio", f + ".mp3")
        assert os.path.exists(p), f"missing {p}"
    bell(880, 2.5, os.path.join(CUTS, "bell880.wav"))
    silence(2.5, os.path.join(CUTS, "breath.wav"))
    silence(1.2, os.path.join(CUTS, "gap.wav"))
    silence(2.5, os.path.join(CUTS, "water.wav"))

    seq = [os.path.join(CUTS, "bell880.wav")]
    for i, (ci, co, sess, bspans, q, t, p) in enumerate(CELLS, 1):
        tag = f"c{i}"
        ch = os.path.join(CUTS, f"{tag}_chant.wav")
        cut(SHARMA, ci, co, ch)
        qq = os.path.join(CUTS, f'{tag}_q.wav'); tts(q, qq)
        tt = os.path.join(CUTS, f'{tag}_t.wav'); tts(t, tt)
        pp = os.path.join(CUTS, f'{tag}_p.wav'); tts(p, pp)
        parts = []
        for j, (bi, bo) in enumerate(bspans):
            bp = os.path.join(CUTS, f"{tag}_b{j}.wav")
            cut(os.path.join(BASE, "audio", MP3[sess] + ".mp3"), bi, bo, bp)
            parts.append(bp)
        if len(parts) == 1:
            cell = parts[0]
        else:
            cell = os.path.join(CUTS, f"{tag}_cell.wav")
            lst = os.path.join(CUTS, f"{tag}_cell.txt")
            open(lst, "w").write("".join(f"file '{x}'\n" for x in parts))
            sh(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0",
                "-i", lst, "-c", "copy", cell])
        seq += [os.path.join(CUTS, f'{tag}_q.wav'),
                os.path.join(CUTS, "breath.wav"), ch, tt, pp,
                os.path.join(CUTS, "gap.wav"), cell,
                os.path.join(CUTS, "water.wav")]
    lst = os.path.join(CUTS, "l0.txt")
    open(lst, "w").write("".join(f"file '{x}'\n" for x in seq))
    wav = os.path.join(GEN, "l0_essay0.wav")
    sh(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst,
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", wav])
    mp3 = os.path.join(GEN, "l0_essay0.mp3")
    sh(["ffmpeg", "-v", "error", "-y", "-i", wav, "-codec:a", "libmp3lame",
        "-q:a", "2", mp3])
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration", "-of", "csv=p=0", mp3],
                       capture_output=True, text=True)
    print(f"L0 DONE: {mp3}  {float(r.stdout.strip()):.1f}s", flush=True)

if __name__ == "__main__":
    main()
