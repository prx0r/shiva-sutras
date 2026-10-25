#!/usr/bin/env python3
"""Deterministic TEXT -> PLAIN filter (port of vatulanatha build/fish_filter_vatula.py).
Same algorithm, this project's key. Edit the KEY, never the output (07 ownership rule).
Usage: python3 tools/plain_filter.py            # writes build/plain_essay0.json + hash
       python3 tools/plain_filter.py --check    # rerun + verify hash
"""
import json, re, hashlib, sys, os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEY = json.load(open(f"{D}/build/key_ss1_proposal.json"))
LOAN = set(json.load(open(f"{D}/build/loanwords_ss1.json")))

def apply_dict(text):
    out = text
    for k in sorted(KEY, key=len, reverse=True):
        pat = re.compile(r'\b' + re.escape(k) + r'\b', re.I)
        def rep(m):
            v = KEY[k]
            if m.group(0)[0].isupper() and v:
                v = v[0].upper() + v[1:]
            return v
        out = pat.sub(rep, out)
    return out

def sanitize(text):
    t = text.replace('(', ' — ').replace(')', '')
    t = t.replace(':', ' —').replace(';', ',').replace('/', '.')
    t = re.sub(r'\s*—\s*', ' — ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    t = re.sub(r'\s+([.,])', r'\1', t)
    t = re.sub(r'—\.', '—', t)
    return t

def plain_of(text):
    return sanitize(apply_dict(text))

if __name__ == '__main__':
    import glob
    out = {}
    for p in sorted(glob.glob(f"{D}/build/t_*.txt")):
        t = open(p).read().strip()
        out[os.path.basename(p)] = {"text": t, "plain": plain_of(t)}
    h = hashlib.sha256(json.dumps(out, sort_keys=True).encode()).hexdigest()[:16]
    man = {"inputs": sorted(os.path.basename(p) for p in glob.glob(f"{D}/build/t_*.txt")),
           "outputs": out, "hash": h}
    if '--check' in sys.argv:
        old = json.load(open(f"{D}/build/plain_essay0.json"))
        print('MATCH' if old['hash'] == h else 'MISMATCH'); sys.exit(0 if old['hash'] == h else 1)
    json.dump(man, open(f"{D}/build/plain_essay0.json", 'w'), indent=1, ensure_ascii=False)
    print(f'wrote plain_essay0.json hash={h}')
