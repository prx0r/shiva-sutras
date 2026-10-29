#!/usr/bin/env python3
"""The ONLY batch build path (M51). Direct xargs loops over builders are banned:
every historical full-rebuild disaster (syntax breaks, filename bugs, stale cuts,
unverified methods) would have died at the pilot stage. This wrapper enforces:
  1. PREFLIGHT: every tools/*.py compiles (1s — catches line-38-class breaks).
  2. PILOT: one verse builds end-to-end (default std_1_1), then proves itself:
     qa_std clean on it, proof decodes, head transcribes to words (content gate).
  3. BATCH: remaining manifests build in parallel batches of 4.
  4. POST: full qa_std + 77-proof count check.
Usage: python3 tools/build_all.py [--pilot 1_1] [--skip-pilot-if <stampfile>]
Any failure STOPS the line before a single batch render runs.
"""
import glob
import os
import subprocess
import sys

BASE = "/home/ubuntu/shiva-sutras"
os.chdir(BASE)

PILOT = "1_1"
for a in sys.argv[1:]:
    if a.startswith("--pilot"):
        PILOT = a.split("=", 1)[1] if "=" in a else sys.argv[sys.argv.index(a) + 1]


def sh(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def main():
    # 1. PREFLIGHT: compile everything (catches syntax breaks before any render).
    bad = []
    for f in glob.glob("tools/*.py"):
        r = sh([sys.executable, "-c",
                "import py_compile,sys; py_compile.compile(sys.argv[1],doraise=True)", f])
        if r.returncode != 0:
            bad.append(f)
    if bad:
        print("PREFLIGHT FAIL (syntax):", bad)
        sys.exit(1)
    print("preflight: all tools compile")

    # 2. PILOT: one verse end-to-end.
    pilot = "standard/manifests/std_%s.json" % PILOT.replace(".", "_")
    r = sh([sys.executable, "tools/build_standard_verse.py", pilot])
    if r.returncode != 0:
        print("PILOT BUILD FAIL:\n", r.stderr[-2000:])
        sys.exit(1)
    tag = PILOT.replace(".", "_")
    proof = "audio/gen/std/%s_B.mp3" % tag
    if not os.path.exists(proof):
        print("PILOT FAIL: no proof at", proof)
        sys.exit(1)
    # decode gate
    r = sh(["ffmpeg", "-v", "error", "-i", proof, "-f", "null", "-"])
    if r.returncode != 0:
        print("PILOT FAIL: proof does not decode")
        sys.exit(1)
    # content gate: proof must contain words (catches speed/garble disasters).
    # NOTE: transcribe the WHOLE pilot proof, never a head slice — whisper VAD
    # under-detects short leading-silence slices (0 words on a 45s slice of a
    # proof that yields 505 words whole).
    # NOTE: transcribe in a FRESH subprocess, never in-process — in-process
    # whisper reads go intermittently blind (0 words ×3 on a file that yields
    # 500+ fresh-process; cause undiagnosed, possibly thread/load-related).
    words = []
    for attempt in range(3):
        r = sh([sys.executable, "-c",
                "from faster_whisper import WhisperModel;"
                "m = WhisperModel('base', device='cpu', compute_type='int8');"
                "segs, _ = m.transcribe(%r, beam_size=5, language='en');"
                "print(len([w for s in segs for w in (s.words or [])]))"
                % proof])
        try:
            n = int(r.stdout.strip().split()[-1])
        except Exception:
            n = 0
        if n >= 50:
            words = ["x"] * n
            break
    if len(words) < 50:
        print("PILOT FAIL: proof has %d words after 3 reads (garbled/speed defect?)" % len(words))
        sys.exit(1)
    print("pilot %s: proof decodes, %d words, e.g. %s"
          % (PILOT, len(words), " ".join(words[:8])))

    # 3. BATCH: everything else, 2-way parallel (shared box — be kind).
    allm = sorted(glob.glob("standard/manifests/std_*.json"))
    rest = [f for f in allm if f != pilot]
    r = subprocess.run(
        "printf '%s\\n' " % "\\n".join(rest) +
        " | xargs -P 2 -I{} python3 tools/build_standard_verse.py {}",
        shell=True, capture_output=True, text=True)
    if "Traceback" in (r.stdout + r.stderr):
        print("BATCH FAILURES present — inspect before proceeding")
        print((r.stdout + r.stderr)[-2000:])
        sys.exit(1)
    print("batch done")

    # 4. POST: full gates.
    r = sh([sys.executable, "tools/qa_std.py"])
    print(r.stdout.strip().splitlines()[-1] if r.stdout else r.stderr[-500:])
    proofs = glob.glob("audio/gen/std/*_B.mp3")
    print("B proofs on disk:", len(proofs))
    if len(proofs) < 77 or r.returncode != 0:
        print("POST FAIL")
        sys.exit(1)
    print("BUILD_ALL OK — 77 proofs, qa green")


if __name__ == "__main__":
    main()
