#!/usr/bin/env python3
"""Standard-verse builder (russian doll): manifest -> cut -> assemble -> sheet.
Manifest: standard/manifests/std_<verse>.json {verse, src, room_src, room_t, layers:
  {\"0\": [...], \"A\": [...], \"B\": [...], \"C\": [...]}} pieces append-only
  (B lists A's pieces + more). Each piece {t_in, t_out, role}.
Pads from the verse's own room tone (never digital silence, never brown noise).
Usage: python3 tools/build_standard_verse.py standard/manifests/std_1_1.json"""
import json, os, re, subprocess, sys

BASE = "/home/ubuntu/shiva-sutras"
GEN = os.path.join(BASE, "audio", "gen", "std")

def sh(cmd):
    subprocess.run(cmd, check=True)

def levels(path):
    r = subprocess.run(["ffmpeg", "-nostats", "-v", "info", "-i", path,
                        "-af", "volumedetect", "-f", "null", "-"],
                       capture_output=True, text=True)
    me = re.search(r"mean_volume: ([\-\d.]+) dB", r.stderr)
    mx = re.search(r"max_volume: ([\-\d.]+) dB", r.stderr)
    return (float(me.group(1)), float(mx.group(1))) if me and mx else (None, None)

def cut(src, a, b, dst):
    if os.path.exists(dst):
        return
    ed = max(0.3, (b - a) - 0.15)
    sh(["ffmpeg", "-v", "error", "-y", "-ss", str(a), "-to", str(b), "-i", src,
        "-af", f"afade=t=in:st=0:d=0.15,afade=t=out:st={ed:.2f}:d=0.15",
        "-ar", "44100", "-ac", "1", dst])
    mean, mx = levels(dst)
    if mean is not None:
        g = max(-12.0, min(12.0, min(-21.0 - mean, -1.5 - mx)))
        sh(["ffmpeg", "-v", "error", "-y", "-i", dst, "-af", f"volume={g:.1f}dB",
            dst + ".n.wav"])
        os.replace(dst + ".n.wav", dst)

def room_bed(src, t, dur, dst):
    if os.path.exists(dst):
        return
    sh(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-t", "1.5", "-i", src,
        "-ar", "44100", "-ac", "1", dst + ".raw.wav"])
    sh(["ffmpeg", "-v", "error", "-y", "-i", dst + ".raw.wav", "-af",
        f"aloop=loop=-1:size=110250,atrim=0:{dur},"
        f"afade=t=in:st=0:d=0.15,afade=t=out:st={dur-0.15:.2f}:d=0.15", dst])
    os.remove(dst + ".raw.wav")

def main():
    man = json.load(open(sys.argv[1]))
    v, src = man["verse"], man["src"]
    # M36: closed b1_status enum — hand-set variance broke queries silently.
    # his-verified = his statement, word-verified onset + book/GRETIL form;
    # his-prov = located, verification pending; sharma = DEAD STATE (Sharma banned
    # by owner 2026-10-29 — no manifest may carry it; kept in enum so old files
    # fail loud, never silent); sadhguru = Sadhguru TTS carries the verse (his
    # tape unusable, GRETIL-exact folded); cf-done = CF re-pass transcribed
    # (his voicing cleanest there); cf-owed = garbled head, re-pass still owed.
    assert man.get("b1_status") in (
        "his-verified", "his-prov", "sharma", "sadhguru", "cf-done",
        "cf-owed"), \
        "%s: b1_status %r not in enum" % (v, man.get("b1_status"))
    if man.get("b1_status") == "sharma":
        raise SystemExit("%s: Sharma banned — reassign B1 (owner 2026-10-28)" % v)
    os.makedirs(GEN, exist_ok=True)
    tag = v.replace(".", "_")
    room = os.path.join(GEN, f"{tag}_room15.wav")
    room_bed(src, man["room_t"], 1.5, room)
    pads = {}
    for name, dur in [("breath", 2.5), ("tbeat", 1.0), ("water", 2.5)]:
        p = os.path.join(GEN, f"{tag}_{name}.wav")
        room_bed(src, man["room_t"], dur, p)
        pads[name] = p
    out = {}
    acc = []
    for layer in ["0", "A", "B", "C", "D"]:
        if layer not in man.get("layers", {}) or not man["layers"][layer]:
            continue
        acc = acc + man["layers"][layer]
        seq, Clo = [], acc
        for i, pc in enumerate(Clo):
            nm = f"{tag}_{layer}_{i}_{int(pc['t_in'])}-{int(pc['t_out'])}.wav"
            p = os.path.join(GEN, nm)
            if pc.get("file", "").endswith(".wav") and pc.get("t_in", 1) == 0 and pc.get("t_out", 0) == 0 and not os.path.exists(p):
                import shutil as _sh
                _sh.copy(os.path.join(BASE, pc["file"]) if not os.path.isabs(pc["file"]) else pc["file"], p)
                print("prebuilt:", os.path.basename(p))
            else:
                cut(pc.get("src", src), pc["t_in"], pc["t_out"], p)
            # Voice-evening calibration (per-role measured means 2026-10-29: his cuts
            # land ~5dB hot vs the -19 LUFS house line; TTS pre-leveled at file,
            # Baumer lifted at walk stage by dynaudnorm): his-lecture cuts -5dB here.
            if not pc.get("file") and not pc.get("uid"):
                sh(["ffmpeg", "-v", "error", "-y", "-i", p,
                    "-af", "volume=-5.0dB", p + ".g.wav"])
                os.replace(p + ".g.wav", p)
            if i > 0:
                seq.append(pads["tbeat"] if Clo[i-1].get("role") == "b2" else pads["breath"])
            seq.append(p)
        seq.append(pads["water"])
        lst = os.path.join(GEN, f"{tag}_{layer}.txt")
        open(lst, "w").write("".join(f"file '{f}'\n" for f in seq))
        wav = os.path.join(GEN, f"{tag}_{layer}.wav")
        sh(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0",
            "-i", lst, "-c", "copy", wav])
        r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                            "format=duration", "-of", "default=noprint_wrappers=1:nokey=1",
                            wav], capture_output=True, text=True)
        dur = float(r.stdout.strip())
        mp3 = wav.replace(".wav", ".mp3")
        sh(["ffmpeg", "-v", "error", "-y", "-i", wav, "-ar", "44100", "-ac", "1", mp3])
        n = len(Clo)
        print(f"{v} layer {layer}: {n} clips, {dur:.1f}s -> {os.path.basename(mp3)}", flush=True)
        out[layer] = {"clips": n, "dur": round(dur, 1), "mp3": mp3}
    print(json.dumps({v: out}, indent=1))

if __name__ == "__main__":
    main()
