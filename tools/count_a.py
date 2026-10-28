#!/usr/bin/env python3
import glob
import json

noA = []
no0 = []
for f in sorted(glob.glob("/home/ubuntu/shiva-sutras/build/std_*.json")):
    d = json.load(open(f))
    if not d["layers"].get("A"):
        noA.append(d["verse"])
    if not d["layers"].get("0"):
        no0.append(d["verse"])
print("total:", len(glob.glob("/home/ubuntu/shiva-sutras/build/std_*.json")))
print("no-A:", len(noA), noA)
print("no-0:", no0)
