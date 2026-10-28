#!/usr/bin/env python3
"""Essence build: Track F production (3 Lights, 6 seeds) + production sheet.

Single source of truth: this script cuts nothing by hand — chant windows
are dip-snapped AND content-verified per window against the whisper
transcript (dips mark syllables, not sutra boundaries: c4 once landed on
1.12 instead of 1.11 — always confirm WHICH sutra the window holds),
Baumer windows from ESSAY0_OUTPUT,
and the sheet's timecodes are measured from the actual intermediates.
Re-run regenerates audio AND sheet together (never edit one without the other).

Cuts live in audio/gen/l0_cuts/ (all WAV — never concat heterogeneous
containers: espeak-derived mp3s drop silently). Master: essence_v1.wav/mp3.
Sheet: build/TRACK_F_PRODUCTION.md.
"""
import os, subprocess, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CUTS = os.path.join(BASE, "audio", "gen", "l0_cuts")
os.makedirs(CUTS, exist_ok=True)

def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-2000:], flush=True)
        sys.exit(1)

def dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration", "-of", "csv=p=0", p],
                       capture_output=True, text=True)
    return float(r.stdout.strip())

def _levels(path):
    import re as _re
    r = subprocess.run(["ffmpeg", "-nostats", "-v", "info", "-i", path,
                        "-af", "volumedetect", "-f", "null", "-"],
                       capture_output=True, text=True)
    me = _re.search(r"mean_volume: ([\-\d.]+) dB", r.stderr)
    ma = _re.search(r"max_volume: ([\-\d.]+) dB", r.stderr)
    return (float(me.group(1)), float(ma.group(1))) if me and ma else (None, None)

def cut(src, a, b, dst, norm=True):
    if os.path.exists(dst):
        return
    sh(["ffmpeg", "-v", "error", "-y", "-ss", str(a), "-to", str(b), "-i", src,
        "-af", ("afade=t=in:st=0:d=0.15,afade=t=out:st={ed:.2f}:d=0.15".format(ed=max(0.3, (b - a) - 0.15))),
        "-ar", "44100", "-ac", "1", dst])
    if norm:
        mean, mx = _levels(dst)
        if mean is not None:
            g = max(-12.0, min(12.0, min(-21.0 - mean, -1.5 - mx)))
            sh(["ffmpeg", "-v", "error", "-y", "-i", dst,
                "-af", f"volume={g:.1f}dB", dst + ".n.wav"])
            os.replace(dst + ".n.wav", dst)


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

def _fish_tts(text, dst, speed=1.0):
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
                        "response_format": "wav",
                       "speed": speed}).encode()
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

TTS_SAY_SPEED = 1.0  # default; P lines use 1.12 (brisker summary delivery)

def tts(text, dst, speed=1.0):
    if os.path.exists(dst):
        return
    if _fish_tts(text, dst, speed):
        mean, mx = _levels(dst)  # uniform -21dB mean on ALL speech (Fish speed shifts energy)
        if mean is not None:
            g = max(-12.0, min(12.0, min(-21.0 - mean, -1.5 - mx)))
            sh(["ffmpeg", "-v", "error", "-y", "-i", dst,
                "-af", f"volume={g:.1f}dB", dst + ".n.wav"])
            os.replace(dst + ".n.wav", dst)
        return
    raw = dst + ".raw.wav"
    sh(["espeak", "-v", "en", "-s", "150", "-w", raw, text])
    sh(["ffmpeg", "-v", "error", "-y", "-i", raw,
        "-af", "aresample=44100,aformat=channel_layouts=mono", dst])
    os.remove(raw)

def silence(d, dst):
    if os.path.exists(dst):
        return
    sh(["ffmpeg", "-v", "error", "-y", "-f", "lavfi",
        "-i", f"anullsrc=r=44100:cl=mono:d={d}", "-ar", "44100", "-ac", "1", dst])

def bell(f, d, dst):
    if os.path.exists(dst):
        return
    sh(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i",
        f"sine=frequency={f}:duration={d}",
        "-af", "afade=t=in:d=0.3,afade=t=out:d=0.8,volume=0.4",
        "-ar", "44100", "-ac", "1", dst])

SHARMA = os.path.join(BASE, "audio", "chant", "sharma_siva_sutras_2009.mp3")
MP3 = {"ss3": "sLD0aeV1d3o", "ss4": "KSpk4KO0JY4", "ss12": "r5wTwUNVYOo",
       "ss7": "s2cqHsBcsd4", "ss11": "Xo9aR9GNOio", "ss13": "xseTpOwSx9M"}


def _norm_say(text):
    import re as _re
    for _w, _s in TTS_SAY.items():
        text = text.replace(_w, _s)
    return _re.sub(r"[^a-z0-9 ]", "", text.lower()).strip()

# ANTI-ECHO RULE (2026-10-26, owner: "why would I hear it twice?").
# Gospel order is TEXTUAL (card rows S→T→P all exist in manifests, on
# screen, in hashes). The VOICE speaks P only when it says something new:
# if normalized P == normalized T, the P cue is dropped and the sheet
# records "P=T — single voicing". Never speak the same sentence twice.
def _plays_p(t_text, p_text):
    return _norm_say(t_text) != _norm_say(p_text)

def hms(h, m, s):
    return h * 3600 + m * 60 + s

# (chant_in, chant_out, baumer_sess, [(in,out)], Q, T, P, cell_note)
CELLS = [
    (266.4, 270.4, "ss3", [(hms(1,19,45), hms(1,19,55)), (hms(1,20,26), hms(1,20,32))],
     "What is consciousness?", "Consciousness is the Self.", "consciousness is the self",
     "universal/not-doing"),
    (270.4, 275.9, "ss4", [(hms(0,33,5), hms(0,33,18)), (hms(0,33,36), hms(0,34,6))],
     "What keeps consciousness from being realised?", "Knowledge is bondage.", "knowledge is bondage",
     "[FLAG] G12 exception STANDS (42s single clip): keep-whole words; antecedent adjacent; crossfaded; no-split decision 2026-10-26 — split would add water without shortening the part and widen dead-air surface; drag is ear-territory"),
    (282.7, 287.1, "ss12", [(hms(0,20,18), hms(0,20,30))],
     "How does realisation happen?", "Bhairava is upsurge.", "bhairava is upsurge",
     "not-made-by-effort WHY"),
    (312.5, 317.9, "ss7", [(hms(0,22,32), hms(0,23,0))],
     "What does realisation do to experience?",
     "The enjoyer of the three states is the Lord of the Heroes.",
     "the enjoyer of the three states is the lord of the heroes",
     "[FLAG] 28s exceeds G12 — ear-check"),
    (392.0, 396.2, "ss11", [(hms(0,50,23), hms(0,50,38))],
     "What does the mind have to do with consciousness?",
     "The mind is Mantra.", "the mind is mantra",
     "becomes-that-mantra"),
    (492.5, 498.9, "ss13", [(hms(1,2,58), hms(1,3,9))],
     "What happens after realisation?", "The self is the actor.", "the self is the actor",
     "stage/role delight"),
]

HEADS = [
    ("S1", 250.0, 257.0, None, "Consciousness is the Self.", "consciousness is the self"),
    ("S2", 382.0, 391.0, None, "The mind is Mantra.", "the mind is mantra"),
    ("S3", 444.0, 449.0, (452.5, 458.2), "The mind is the Self.", "the mind is the self"),
]
# S1 head uses the SHORT intro (no 22-count promise before 4 seeds).
# Decided 2026-10-26: the count line belongs to the full 77-walk, not the
# essence. Long version file retained; swap is one tuple.
# Head S cards are HUMAN chant, never TTS (QA pass 1: espeak Sanskrit is the
# worst sound in the build). S1/S2 reuse their seed chant cuts; S3 cuts 3.1.

def main():
    bell(880, 2.5, f"{CUTS}/bell880.wav")
    silence(2.5, f"{CUTS}/breath.wav")
    silence(3.0, f"{CUTS}/breath3.wav")
    silence(1.0, f"{CUTS}/tbeat.wav")
    silence(1.2, f"{CUTS}/gap.wav")
    silence(2.5, f"{CUTS}/water.wav")
    silence(5.0, f"{CUTS}/xl5.wav")
    silence(6.0, f"{CUTS}/xl6.wav")
    for si, (sec, hi0, hi1, s, t, p) in enumerate(HEADS, 1):
        # doorway only: intro is cut; T/P are text-only (anti-echo rule),
        # so no TTS is generated for heads at all.
        cut(SHARMA, hi0, hi1, f"{CUTS}/head_{sec.lower()}_intro.wav")
    cell_files = []
    for i, (ci, co, sess, bspans, q, t, p, note) in enumerate(CELLS, 1):
        tag = f"c{i}"
        cut(SHARMA, ci, co, f"{CUTS}/{tag}_chant.wav")
        tts(q, f"{CUTS}/{tag}_q.wav")
        tts(t, f"{CUTS}/{tag}_t.wav")
        tts(p, f"{CUTS}/{tag}_p.wav", speed=1.12)
        parts = []
        for j, (bi, bo) in enumerate(bspans):
            # span-hashed names: spans change across passes and cut() skips
            # existing files — bare indices silently reused a stale 46s cut
            # as a 30s one (M24). Never bare names.
            bp = f"{CUTS}/{tag}_b{j}_{int(bi)}-{int(bo)}.wav"
            cut(os.path.join(BASE, "audio", MP3[sess] + ".mp3"), bi, bo, bp)
            parts.append(bp)
        if len(parts) == 1:
            cell_files.append(parts[0])
        else:
            cp = f"{CUTS}/{tag}_cell.wav"
            if os.path.exists(cp):
                os.remove(cp)  # rebuild: spans change across passes
            ins = []
            for x in parts:
                ins += ["-i", x]
            # equal-power crossfades between spans (0.4s): hard concats of
            # lecture tape read as mid-word cuts (QA pass 2, c1 joint)
            filt = ""
            prev = "[0:a]"
            for j in range(1, len(parts)):
                filt += f"{prev}[{j}:a]acrossfade=d=0.4:c1=tri:c2=tri[a{j}];"
                prev = f"[a{j}]"
            filt += f"{prev}aresample=44100,aformat=channel_layouts=mono[aout]"
            sh(["ffmpeg", "-v", "error", "-y"] + ins +
                ["-filter_complex", filt, "-map", "[aout]", cp])
            cell_files.append(cp)

    # program order
    seq = ["bell880.wav", "xl5.wav"]
    order = [("S1", [0, 1, 2, 3]), ("S2", [4]), ("S3", [5])]
    for sec, idxs in order:
        s = sec.lower()
        # heads are DOORWAYS (bell + human frame + water) — never cards.
        # Card T/P live in cells where the question primes them; head cards
        # duplicated the cell cards ~15s later (Qwen pass: "same sentence
        # twice"). Seed chant plays once per verse, in its cell.
        seq += ["bell880.wav", f"head_{s}_intro.wav", "water.wav"]
        for k in idxs:
            tag = f"c{k+1}"
            br = "breath3.wav" if tag in ("c4", "c5") else "breath.wav"
            _ct, _cp = CELLS[k][5], CELLS[k][6]
            _pp = [f"{tag}_p.wav"] if _plays_p(_ct, _cp) else []
            seq += [f"{tag}_q.wav", br, f"{tag}_chant.wav",
                    f"{tag}_t.wav", "tbeat.wav"] + _pp + ["gap.wav",
                    os.path.basename(cell_files[k]), "water.wav"]
    seq += ["xl6.wav"]
    open(f"{CUTS}/essence.txt", "w").write("".join(f"file '{f}'\n" for f in seq))
    sh(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0",
        "-i", f"{CUTS}/essence.txt", "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
        f"{BASE}/audio/gen/essence_v1.wav"])
    sh(["ffmpeg", "-v", "error", "-y", "-i", f"{BASE}/audio/gen/essence_v1.wav",
        "-codec:a", "libmp3lame", "-q:a", "2", f"{BASE}/audio/gen/essence_v1.mp3"])

    # production sheet with MEASURED timecodes
    L = []
    L.append("# TRACK F — PRODUCTION SHEET (essence cut: 3 Lights, 6 seeds)")
    L.append("")
    L.append("Generated by `tools/make_essence.py` — timecodes measured from the actual intermediates. Re-run regenerates audio AND sheet together. [COM] = internal direction, [FX] = sound effect, [XL] = extra-long pause, [FLAG] = ear-session decision. G12: cells ≤25s.")
    L.append("")
    L.append("| # | t_in | dur | cue | voice | notes |")
    L.append("|---|---|---|---|---|---|")
    t = 0.0
    n = 0
    notes = {
        "bell880.wav": ("—", "motto"),
        "xl5.wav": ("—", "[XL] settle-in pause"),
        "xl6.wav": ("—", "[XL] terminal stilling, no climax"),
        "breath.wav": ("—", "2-breath 2.5s; SOFT joint after Q (tongue-switch) — do not lengthen"),
        "breath3.wav": ("—", "3-breath 3.0s for long Qs (c4 S4, c5 S5) — parse time before card"),
        "tbeat.wav": ("—", "1s T-landing beat; translation lands before plain"),
        "gap.wav": ("—", "1.2s; SOFT joint: robot→human next — fades + room-tone at ship"),
        "water.wav": ("—", "section water"),
    }
    def cue(f, voice=None, note=None):
        nonlocal t, n
        n += 1
        d = dur(os.path.join(CUTS, f))
        v, nn = notes.get(f, (voice or "", note or ""))
        if voice:
            v = voice
        if note:
            nn = note
        L.append(f"| {n} | {t:07.2f} | {d:5.2f} | `{f}` | {v} | {nn} |")
        t += d
    cnotes = [
        (None, None, "program open; [FX] downbeat TBD under tail"),
        (None, None, None),
    ]
    # open
    n += 1; d = dur(f"{CUTS}/bell880.wav")
    L.append(f"| {n} | {t:07.2f} | {d:5.2f} | `bell880.wav` | — | program open; [FX] downbeat TBD under tail |"); t += d
    n += 1; d = dur(f"{CUTS}/xl5.wav")
    L.append(f"| {n} | {t:07.2f} | {d:5.2f} | `(silence)` | — | [XL] settle-in pause |"); t += d
    sec_of = {0: "S1", 1: "S1", 2: "S1", 3: "S1", 4: "S2", 5: "S3"}
    order2 = [("S1", [0, 1, 2, 3]), ("S2", [4]), ("S3", [5])]
    for sec, idxs in order2:
        s = sec.lower()
        cue("bell880.wav", "—", f"{sec} head motto")
        cue(f"head_{s}_intro.wav", "Sharma", "section frame, human voice — the doorway (no card here; cards live in cells where Q primes them)")
        n += 1
        L.append(f"| {n} | {t:07.2f} | — | card rows S→T→P | text only | head carries no card audio — bell+intro+water only (anti-echo rule); full card lives in manifests + on screen + in each cell |")
        cue("water.wav", "—", "head water")
        for k in idxs:
            tag = f"c{k+1}"
            cue(f"{tag}_q.wav", "TTS", "spine question")
            cue("breath3.wav" if tag in ("c4", "c5") else "breath.wav")
            cue(f"{tag}_chant.wav", "Sharma", "[FX] downbeat TBD at start; chant")
            cue(f"{tag}_t.wav", "TTS", "comprehension landing — OK joint")
            cue("tbeat.wav", "—", "1s landing beat; translation lands before plain")
            _ct, _cp = CELLS[k][5], CELLS[k][6]
            if _plays_p(_ct, _cp):
                cue(f"{tag}_p.wav", "TTS", "plain ADDS meaning — spoken")
            else:
                n += 1
                L.append(f"| {n} | {t:07.2f} | — | `(plain row)` | text only | P=T verbatim — single voicing (anti-echo rule); row lives in manifest + on screen, never spoken |")
            cue("gap.wav")
            cue(os.path.basename(cell_files[k]), "Baumer", CELLS[k][7])
            cue("water.wav")
    n += 1; d = dur(f"{CUTS}/xl6.wav")
    L.append(f"| {n} | {t:07.2f} | {d:5.2f} | `(silence)` | — | [XL] terminal stilling, no climax |"); t += d
    L.append("")
    L.append(f"**Total runtime: {t/60:.1f} min ({t:.0f}s). Rendered master must match within 1s.**")
    L.append("")
    L.append("## Handover audit (voice-to-voice joints)")
    for line in [
        "- bell→Q/intro: OK (motto grammar).",
        "- Q→breath→chant: SOFT — English question answered in Sanskrit; breath 2.5s (3.0s for long Qs c4/c5), comprehension lands at T. Never lengthen beyond spec or the question strands.",
        "- chant→T: OK — same verse, two tongues; the translation moment.",
        "- T→P: OK — one card, one voice.",
        "- P→gap→Baumer: SOFT — timbre + room jump (espeak dry → lecture room); 1.2s gap + 0.15s fades now, room-tone beds at ship.",
        '- c1 internal two-span concat (31s source gap removed): OK-text (flow-read passed, ends on "is there"); ear-verify.',
        "- Baumer→water→next: OK except flagged long-cells.",
        "- Sharma intro→card: OK — human frames, TTS lands the card.",
    ]:
        L.append(line)
    L.append("")
    L.append("## FX + pause vocabulary (samples TBD — vatulanatha sfx kit first call)")
    for line in [
        "- motto-bell 880Hz/2.5s: program + Light heads (cut, in hand).",
        "- downbeat TBD: low wood-block under first Sanskrit word of each chant (6 placements).",
        "- breath 2.5s / breath3 3.0s / tbeat 1.0s / gap 1.2s / water 2.5s (cuts, in hand).",
        "- XL settle 5s (program open), XL terminal 6s (S3 tail).",
        "- zoom-bell 220Hz/6.0s: NOT in essence cut (single layer) — layers build only.",
    ]:
        L.append(line)
    open(f"{BASE}/build/TRACK_F_PRODUCTION.md", "w").write("\n".join(L) + "\n")

    master = dur(f"{BASE}/audio/gen/essence_v1.mp3")
    print(f"essence: {n} cues, sheet {t:.0f}s, master {master:.1f}s", flush=True)
    assert abs(t - master) < 1.0, f"SHEET/MASTER DIVERGED: {t:.1f} vs {master:.1f}"
    print("SHEET == MASTER ✓", flush=True)

if __name__ == "__main__":
    main()
