#!/usr/bin/env python3
"""tts_scan.py — no raw Sanskrit through TTS, deterministically.
Every TTS-spoken line (make_essence HEADS + CELLS) is scanned for
Sanskrit tokens. A hit must EITHER have a TTS_SAY spoken-form entry
(display text unchanged) OR be re-voiced human. Loanwords that TTS
pronounces acceptably live in LOAN (audited, not assumed).

Usage: python3 tools/tts_scan.py
Exit 0 = clean. Violations name the line + token.
"""
import re, sys

sys.path.insert(0, "tools")
import make_essence as M

# Sanskrit tokens that may appear in card/plain text. Anything here
# reaching TTS raw is a fail (espeak mangled them; Fish would too).
SANSKRIT = {
    "caitanyamatma", "caitanya", "jnanam", "bandhah", "jnan", "yonivargah",
    "kalasariram", "jnanadhisthana", "matrka", "matrika", "udyamo",
    "bhairava", "bhairavah", "sakti", "cakra", "sandhane", "visvasamharah",
    "jagrat", "svapna", "susupta", "turya", "turiyatita", "turyabhoga",
    "sambhavah", "jnanam", "vikalpah", "avivekah", "mayasausuptam",
    "tritayabhokta", "tritayabhokta", "viresah", "vismayo", "yogabhumih",
    "iccha", "saktir", "kumari", "drsyam", "sariram", "hrdaye",
    "chittasanghatta", "drsyasvapadarsanam", "suddhatattva", "sandhanat",
    "apasusaktih", "vitarka", "atmajnanam", "lokanandah", "samadhisukham",
    "saktisandhane", "sarirotpattih", "bhutasandhana", "sudhavidyodayat",
    "cakresatvasiddhih", "mahahradanusandhanan", "mantraviryanubhavah",
    "cittam", "mantrah", "prayatnah", "sadhakah", "vidyasarirasatta",
    "mantrarahasyam", "garbhe", "cittavikaso", "vidyasvapnah",
    "vidyasamutthane", "svabhavike", "khecarisivavastha", "gurur",
    "upayah", "matrkacakrasambodhah", "havih", "jnanam", "annam",
    "vidyasamhara", "atmacittam", "vivekah", "mayam",
}
# Loanwords TTS says acceptably (audited once each, listed once).
LOAN = {"mantra", "sutra", "sutras", "guru", "shiva", "atman", "self",
        "consciousness", "knowledge", "bondage", "upsurge", "enjoyer"}

say = {w.lower(): s for w, s in getattr(M, "TTS_SAY", {}).items()}
lines = []
for sec, hi0, hi1, s, t, p in M.HEADS:
    lines += [(f"head-{sec.lower()}-t", t), (f"head-{sec.lower()}-p", p)]
for i, (ci, co, sess, bspans, q, t, p, note) in enumerate(M.CELLS, 1):
    lines += [(f"c{i}-q", q), (f"c{i}-t", t), (f"c{i}-p", p)]

fails = 0
for name, text in lines:
    for w in re.findall(r"[A-Za-z']+", text):
        wl = w.lower().strip("'")
        if wl in SANSKRIT and wl not in say:
            print(f"FAIL {name}: raw Sanskrit '{w}' reaches TTS (add TTS_SAY or re-voice human)")
            fails += 1
if fails:
    sys.exit(1)
print(f"TTS clean: {len(lines)} lines scanned, {len(SANSKRIT)}-token stoplist, TTS_SAY covers {sorted(say)}")
