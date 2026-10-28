#!/usr/bin/env python3
"""TTS a line verbatim via Fish (Dyczkowski exact wording only).
Usage: python3 tools/tts_line.py "<text>" out.wav [speed]
TTS_SAY spoken forms apply; display text never changes (we keep the book text
as the record; the wav is the rendering)."""
import json
import os
import re
import subprocess
import sys
import urllib.request

BASE = "/home/ubuntu/shiva-sutras"
TTS_SAY = {"Bhairava": "Bye-ruh-vuh", "bhairava": "bye-ruh-vuh", "Mayiyamala": "Mah-yee-ya-mah-lah", "Ksemaraja": "Kshema-raja", "Kṣemarāja": "Kshema-raja",
           "caitanya": "chaitanya", "jnanam": "gyanam",
           # B1b probes 2026-10-28 (carrier-sentence + whisper round-trip):
           # Matrka->"matricca", Kala->"Kala" exact, Susumna->"sushiumna".
           "Matrka": "Matrika", "Kala": "Kah-lah", "Susumna": "Sushumna",
           # 1.8-triad probes 2026-10-28: isolated probes non-discriminating (base ASR
           # garbles all short foreign tokens — M37 short-clip rule); carrier-context
           # round-trip, (a) wins over (b) on both slots; owner ear final on proper nouns.
           "cidatman": "chid-aht-mun", "sphurati": "sfoorati"}


def _fish_key():
    for f in [os.path.expanduser("~/.config/opencode/.env")]:
        try:
            m = re.search(r"^FISH_API_KEY=(.*)$", open(f).read(), re.M)
            if m and m.group(1).strip():
                return m.group(1).strip()
        except OSError:
            pass
    return None


def main():
    text, dst = sys.argv[1], sys.argv[2]
    speed = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
    for _w, _s in TTS_SAY.items():
        text = text.replace(_w, _s)
    key = _fish_key()
    assert key, "no FISH_API_KEY"
    body = json.dumps({"model": "fish-audio/s2.1-pro-free",
                       "input": text, "voice": "",
                       "response_format": "wav", "speed": speed}).encode()
    req = urllib.request.Request(
        "https://api.fish.audio/compat/v1/audio/speech", data=body,
        headers={"Authorization": f"Bearer {key}",
                 "Content-Type": "application/json"})
    out = urllib.request.urlopen(req, timeout=120)
    open(dst + ".tmp", "wb").write(out.read())
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", dst + ".tmp",
                    "-ar", "44100", "-ac", "1", dst], check=True)
    os.remove(dst + ".tmp")
    # level norm to -21dB mean (house standard)
    r = subprocess.run(["ffmpeg", "-nostats", "-v", "info", "-i", dst,
                        "-af", "volumedetect", "-f", "null", "-"],
                       capture_output=True, text=True)
    me = re.search(r"mean_volume: ([\-\d.]+) dB", r.stderr)
    mx = re.search(r"max_volume: ([\-\d.]+) dB", r.stderr)
    if me and mx:
        g = max(-12.0, min(12.0, min(-21.0 - float(me.group(1)),
                                       -1.5 - float(mx.group(1)))))
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", dst,
                        "-af", "volume={:.1f}dB".format(g),
                        dst + ".n.wav"], check=True)
        os.replace(dst + ".n.wav", dst)
    print("tts ok:", dst)


if __name__ == "__main__":
    main()
