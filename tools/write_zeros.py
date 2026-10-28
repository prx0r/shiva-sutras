#!/usr/bin/env python3
"""Write 0-layer manifests for all located verses. B1 = word-verified (or
provisional, marked), B2 = adjacent gloss from transcript segments.
Run: python3 tools/write_zeros.py. Writes build/std_<v>.json (0 only,
or preserves existing A/B/C and updates 0)."""
import json, os, re, unicodedata

BASE = "/home/ubuntu/shiva-sutras"
# verse: (mp3, b1_in, b1_out, b2_in, b2_out, room_t, status)
# status: ok (word-verified) | prov (segment-level, needs word check) | sharma (fallback) | repass (needs CF)
V = {
 "1.1": ("Shiva Sutras 1.1.mp3", 80.5, 81.8, 82.4, 98.3, 77.7, "ok"),
 "1.2": ("Shiva Sutras 1.2.mp3", 100.8, 102.0, 122.7, 146.2, 20.5, "ok"),
 "1.3": ("Shiva Sutras 1.3.mp3", 16.8, 19.0, 19.0, 24.0, 28.0, "prov"),
 "1.4": (None, None, None, None, None, None, "sharma"),
 "1.5": ("Shiva Sutras 1.5.mp3", 50.7, 51.7, 83.9, 96.9, 15.0, "ok"),
 "1.6": (None, None, None, None, None, None, "sharma"),
 "1.7": ("Shiva Sutras 1.7.mp3", 0.0, 4.0, 4.0, 14.7, 13.2, "prov"),
 "1.8": ("Shiva Sutras 1.8-10.mp3", 14.8, 16.5, 16.5, 21.0, 10.0, "prov"),
 "1.9": ("Shiva Sutras 1.8-10.mp3", 31.2, 33.0, 33.0, 38.0, 10.0, "prov"),
 "1.10": ("Shiva Sutras 1.8-10.mp3", 46.0, 49.0, 49.0, 56.0, 10.0, "prov"),
 "1.11": ("Shiva Sutras 1.11.mp3", 80.5, 82.5, 82.5, 98.6, 70.0, "prov"),
 "1.12": ("Shiva Sutras 1.12.mp3", 45.7, 63.4, 63.4, 78.4, 15.0, "prov"),
 "1.13": ("Shiva Sutras 1.13.mp3", 17.0, 20.5, 20.5, 26.5, 8.0, "prov"),
 "1.14": (None, None, None, None, None, None, "repass"),
 "1.15": ("Shiva Sutras 1.15.mp3", 47.1, 57.0, 57.0, 65.5, 40.0, "prov"),
 "1.16": ("Shiva Sutras 1.16.mp3", 22.1, 31.6, 31.6, 42.6, 16.0, "prov"),
 "1.17": ("Shiva Sutras 1.17.mp3", 16.8, 25.0, 25.0, 33.2, 8.0, "prov"),
 "1.18": ("Shiva Sutras 1.18.mp3", 6.7, 8.5, 8.5, 19.7, 30.0, "prov"),
 "1.19": (None, None, None, None, None, None, "repass"),
 "1.20": (None, None, None, None, None, None, "locate"),
 "1.21": (None, None, None, None, None, None, "locate"),
 "1.22": (None, None, None, None, None, None, "locate"),
 "2.1": ("Shiva Sutras 2.1.mp3", 128.4, 135.0, 135.0, 147.5, 120.0, "prov"),
 "2.2": (None, None, None, None, None, None, "locate"),
 "2.3": ("Shiva Sutras 2.3.mp3", 1.0, 4.0, 4.0, 11.3, 15.0, "prov"),
 "2.4": ("Shiva Sutras 2.4.mp3", 20.2, 30.0, 30.0, 41.0, 12.0, "prov"),
 "2.5": ("Shiva Sutras 2.5.mp3", 0.0, 4.1, 4.1, 11.0, 12.0, "prov"),
 "2.6": ("Shiva Sutras 2.6.mp3", 21.0, 21.9, 21.9, 30.0, 12.0, "prov"),
 "2.7": (None, None, None, None, None, None, "locate"),
 "2.8": ("Shiva Sutras 2.8.mp3", 1.4, 6.4, 6.4, 13.0, 40.0, "prov"),
 "2.9": ("Shiva Sutras 2.9.mp3", 3.4, 4.6, 4.6, 8.2, 10.0, "prov"),
 "2.10": ("Shiva Sutras 2.10.mp3", 0.0, 3.1, 3.1, 10.0, 12.0, "prov"),
 "3.1": ("Shiva Sutras 3.1.mp3", 0.0, 2.0, 2.0, 12.0, 15.0, "prov"),
 "3.2": (None, None, None, None, None, None, "locate"),
 "3.3": (None, None, None, None, None, None, "locate"),
 "3.4": ("Shiva Sutras 3.4.mp3", 17.0, 20.5, 20.5, 35.0, 10.0, "prov"),
 "3.5": ("Shiva Sutras 3.5.mp3", 53.5, 62.0, 62.0, 75.0, 45.0, "prov"),
 "3.6": (None, None, None, None, None, None, "locate"),
 "3.7": (None, None, None, None, None, None, "locate"),
 "3.8": (None, None, None, None, None, None, "locate"),
 "3.9": ("Shiva Sutras 3.9.mp3", 30.0, 33.0, 33.0, 45.0, 20.0, "prov"),
 "3.10": ("Shiva Sutras 3.10.mp3", 18.5, 21.0, 21.0, 35.0, 10.0, "prov"),
 "3.11": (None, None, None, None, None, None, "repass"),
 "3.12": ("Shiva Sutras 3.12.mp3", 2.1, 4.1, 4.1, 12.0, 15.0, "prov"),
 "3.13": ("Shiva Sutras 3.13.mp3", 1.0, 8.0, 8.0, 20.0, 25.0, "prov"),
 "3.14": (None, None, None, None, None, None, "locate"),
 "3.15": ("Shiva Sutras 3.15.mp3", 2.3, 9.0, 9.0, 16.0, 20.0, "prov"),
 "3.16": (None, None, None, None, None, None, "locate"),
 "3.17": (None, None, None, None, None, None, "locate"),
 "3.18": (None, None, None, None, None, None, "locate"),
 "3.19": (None, None, None, None, None, None, "locate"),
 "3.20": (None, None, None, None, None, None, "locate"),
 "3.21": (None, None, None, None, None, None, "repass"),
 "3.22": (None, None, None, None, None, None, "locate"),
 "3.23": ("Shiva Sutras 3.23.mp3", 40.9, 43.5, 43.5, 55.0, 30.0, "prov"),
 "3.24": (None, None, None, None, None, None, "locate"),
 "3.25": ("Shiva Sutras 3.25.mp3", 11.5, 14.0, 14.0, 25.0, 5.0, "prov"),
 "3.26": ("Shiva Sutras 3.26.mp3", 0.0, 2.1, 2.1, 9.0, 12.0, "prov"),
 "3.27": ("Shiva Sutras 3.27.mp3", 5.8, 7.1, 7.1, 15.0, 20.0, "prov"),
 "3.28": ("Shiva Sutras 3.28.mp3", 16.9, 18.0, 18.0, 30.0, 8.0, "prov"),
 "3.29": (None, None, None, None, None, None, "locate"),
 "3.30": ("Shiva Sutras 3.30.mp3", 7.0, 12.0, 12.0, 25.0, 30.0, "prov"),
 "3.31": ("Shiva Sutras 3.31.mp3", 0.0, 5.2, 5.2, 14.0, 20.0, "prov"),
 "3.32": ("Shiva Sutras 3.32.mp3", 0.0, 9.7, 9.7, 20.0, 25.0, "prov"),
 "3.33": ("Shiva Sutras 3.33.mp3", 0.0, 4.0, 4.0, 12.0, 15.0, "prov"),
 "3.34": (None, None, None, None, None, None, "repass"),
 "3.35": ("Shiva Sutras 3.35.mp3", 0.0, 4.0, 4.0, 16.0, 20.0, "prov"),
 "3.36": ("Shiva Sutras 3.36.mp3", 45.0, 50.0, 50.0, 62.0, 30.0, "prov"),
 "3.37": (None, None, None, None, None, None, "repass"),
 "3.38": (None, None, None, None, None, None, "locate"),
 "3.39": ("Shiva Sutras 3.39.mp3", 5.0, 10.0, 10.0, 22.0, 30.0, "prov"),
 "3.40": (None, None, None, None, None, None, "locate"),
 "3.41": ("Shiva Sutras 3.41.mp3", 17.0, 20.0, 20.0, 30.0, 10.0, "prov"),
 "3.42": (None, None, None, None, None, None, "locate"),
 "3.43": ("Shiva Sutras 3.43.mp3", 0.0, 5.0, 5.0, 14.0, 20.0, "prov"),
 "3.44": ("Shiva Sutras 3.44.mp3", 1.0, 7.0, 7.0, 16.0, 25.0, "prov"),
 "3.45": ("Shiva Sutras 3.45.mp3", 22.0, 28.0, 28.0, 40.0, 10.0, "prov"),
}
made, prov, other = 0, 0, []
for v, (fn, a, b, c, d, room, st) in V.items():
    if st in ("sharma", "repass", "locate"):
        other.append((v, st))
        continue
    tag = v.replace(".", "_")
    path = os.path.join(BASE, "build", "std_%s.json" % tag)
    man = {"verse": v, "src": "/home/ubuntu/shiva-study-set/" + fn,
           "room_t": room, "guests": [],
           "layers": {"0": [{"role": "b1", "t_in": a, "t_out": b},
                            {"role": "b2", "t_in": c, "t_out": d}],
                      "A": [], "B": [], "C": []}}
    if os.path.exists(path):
        old = json.load(open(path))
        for L in ("A", "B", "C"):
            if old.get("layers", {}).get(L):
                man["layers"][L] = old["layers"][L]
    man["b1_status"] = st
    json.dump(man, open(path, "w"), indent=1)
    made += 1
    if st == "prov":
        prov += 1
print("manifests: %d (prov %d)" % (made, prov))
print("deferred: %s" % other)
