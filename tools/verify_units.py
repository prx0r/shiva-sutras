#!/usr/bin/env python3
"""Verify excavation quotes against readable transcripts.
Usage: python3 tools/verify_units.py  (run from shiva-sutras/)
Checks: every unit has required fields; quote (whitespace-normalized,
lowercased, timestamps stripped) is a substring of its session text
(with [HH:MM:SS] stamps stripped); start timestamp line exists.
Exits 1 on any failure. Session map = lecture order."""
import re, glob, os, sys

SESS = {
 'ss1': 'text/shiva_sutras_day_1_introduction_i.txt',
 'ss2': 'text/shiva_sutras_day_1_introduction_ii.txt',
 'ss3': 'text/shiva_sutras_day_2_introduction_iii.txt',
 'ss4': 'text/shiva_sutras_day_2_session_i.txt',
 'ss5': 'text/shiva_sutras_day_3_session_i.txt',
 'ss6': 'text/shiva_sutras_day_3_session_ii.txt',
 'ss7': 'text/shiva_sutras_day_4_session_i.txt',
 'ss8': 'text/shiva_sutras_day_4_session_ii_part_1.txt',
 'ss9': 'text/shiva_sutras_day_4_session_ii_part_ii.txt',
 'ss10': 'text/shiva_sutras_day_5_session_i.txt',
 'ss11': 'text/shiva_sutras_day_5_session_ii.txt',
 'ss12': 'text/shiva_sutras_day_6_session_i.txt',
 'ss13': 'text/shiva_sutras_day_6_session_ii.txt',
}
def norm(s):
    s = re.sub(r'\s+',' ',s).strip().lower()
    return re.sub(r'[^a-z0-9 ]','',s)
def strip_ts(s):
    s = __import__('re').sub(r'\[\d{2}:\d{2}:\d{2}\] ?', '', s)
    return __import__('re').sub(r'\[[^\]]*\] ?', '', s)

REQ = ['timestamp','topics','role','layer','quote','context','essay_use']
GRADE_RE = __import__('re').compile(r'\[(A|B|C)\]\s*$')
fails, n_units = [], 0
for path in sorted(glob.glob('excavations/ss*.md')):
    lec = os.path.basename(path).removesuffix('.md')
    src = SESS.get(lec)
    if not src or not os.path.exists(src):
        print(f'SKIP {lec} (no transcript yet)'); continue
    stext = norm(strip_ts(open(src, encoding='utf-8').read()))
    stamps = set(re.findall(r'\[(\d{2}:\d{2}:\d{2})\]', open(src, encoding='utf-8').read()))
    cur, fields = None, {}
    def flush():
        global n_units
        if cur is None: return
        n_units += 1
        for r in REQ:
            if r not in fields: fails.append((lec, cur, f'missing field {r}')); return
        q = norm(fields['quote'].strip('"'))
        if q not in stext:
            fails.append((lec, cur, f'quote not found: {q[:80]}'))
        m = re.match(r'\[(\d{2}):(\d{2}):(\d{2})\]', fields['timestamp'])
        if m:
            t0 = int(m.group(1))*3600 + int(m.group(2))*60 + int(m.group(3))
            near = False
            for st in stamps:
                p = st.split(':')
                if len(p) != 3: continue
                if abs((int(p[0])*3600 + int(p[1])*60 + int(p[2])) - t0) <= 120:
                    near = True; break
            if not near:
                fails.append((lec, cur, f"no transcript stamp within 120s of {fields['timestamp']}"))
    for line in open(path, encoding='utf-8'):
        t = line.rstrip('\n')
        if t.startswith('### ss'):
            flush(); cur = t.split('\u2014')[0].strip().lstrip('### ').strip(); fields = {}
            if not GRADE_RE.search(t): fails.append((lec, cur, 'header missing [A/B/C] grade'))
        elif t.startswith('- ') and ':' in t and cur:
            k, v = t[2:].split(':', 1); fields[k.strip()] = v.strip()
    flush()
print(f'units: {n_units}  fails: {len(fails)}')
for lec,uid,msg in fails[:30]: print(f'  MISS {lec} {uid}: {msg}')
sys.exit(1 if fails else 0)
