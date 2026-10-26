#!/usr/bin/env python3
"""Build per-section A/B manifests with tight cut stamps (quote-located, not window edges).

Usage: python3 tools/build_manifests.py        (writes build/manifest_sN_{A,B}.json)
Order law: SECTION_ARGUMENTS order is canonical for its 71 A-clips (join-audited);
units missing from it (pass-1 A's) insert by (session, timestamp); B-keeps merge
by the same key. Asserts: every unit's grade/section matches SPINE_ASSIGN,
quote locates in its transcript, per-session order monotonic.
"""
import re, os, glob, json, sys, subprocess

SESS = {
 'ss1':'text/shiva_sutras_day_1_introduction_i.txt','ss2':'text/shiva_sutras_day_1_introduction_ii.txt',
 'ss3':'text/shiva_sutras_day_2_introduction_iii.txt','ss4':'text/shiva_sutras_day_2_session_i.txt',
 'ss5':'text/shiva_sutras_day_3_session_i.txt','ss6':'text/shiva_sutras_day_3_session_ii.txt',
 'ss7':'text/shiva_sutras_day_4_session_i.txt','ss8':'text/shiva_sutras_day_4_session_ii_part_1.txt',
 'ss9':'text/shiva_sutras_day_4_session_ii_part_ii.txt','ss10':'text/shiva_sutras_day_5_session_i.txt',
 'ss11':'text/shiva_sutras_day_5_session_ii.txt','ss12':'text/shiva_sutras_day_6_session_i.txt',
 'ss13':'text/shiva_sutras_day_6_session_ii.txt','dl1':'text/shiva_sutras_introduction_dl.txt'}
# session -> local mp3 (YouTube id / dl1 file); verified against MANIFEST titles
MP3 = {'ss1':'c1l1RgloZBs','ss2':'dyEQsbazQnM','ss3':'sLD0aeV1d3o','ss4':'KSpk4KO0JY4',
 'ss5':'ABQi35iUoyI','ss6':'Q-nwDCMripc','ss7':'s2cqHsBcsd4','ss8':'arJORd6eRXI',
 'ss9':'qRueQPC_wGc','ss10':'lfWQfoG23cY','ss11':'Xo9aR9GNOio','ss12':'r5wTwUNVYOo',
 'ss13':'xseTpOwSx9M','dl1':'Shiva_Sutra_Introduction'}
def mp3path(s): return f"audio/{MP3[s]}.mp3"

def norm(s):
    s = re.sub(r'\s+',' ',s).strip().lower()
    return re.sub(r'[^a-z0-9 ]','',s)
def strip_ts(s):
    s = re.sub(r'\[\d{2}:\d{2}:\d{2}\] ?', '', s)
    return re.sub(r'\[[^\]]*\] ?', '', s)
def ts2s(t):
    h,m,s = t.split(':'); return int(h)*3600+int(m)*60+int(s)
def s2ts(x):
    x = max(0, int(round(x))); h,r = divmod(x,3600); m,s = divmod(r,60); return f'{h:02d}:{m:02d}:{s:02d}'

def load_lines(sess):
    out = []
    for raw in open(SESS[sess], encoding='utf-8'):
        m = re.match(r'\[(\d{2}:\d{2}:\d{2})\] ?', raw)
        if not m: continue
        out.append((ts2s(m.group(1)), norm(strip_ts(raw[m.end():]))))
    return out

def locate(lines, quote, wstart, wend):
    """Minimal contiguous line-run covering norm(quote). Returns (in,out)."""
    q = norm(quote)
    best = None
    n = len(lines)
    for i in range(n):
        if wstart is not None and lines[i][0] < (wstart - 120): continue  # verify_units tolerance
        if wstart is not None and lines[i][0] > (max(wend or 0, wstart or 0) + 120): break
        acc = ''
        for j in range(i, min(i+60, n)):
            acc = (acc + ' ' + lines[j][1]).strip() if (j > i) else lines[j][1]
            if q in acc:
                width = (lines[j][0] - lines[i][0])
                if best is None or width < (best[2]-best[1]):
                    best = (i, lines[i][0], lines[j][0], j, acc)
                break
    if best is None: return None
    i, tin_l, tj, j, acc = best

    # word-index → time: interpolate inside a line at 2.7 wps, anchored to real stamps
    words_in = [len(lines[x][1].split()) for x in range(i, j+1)]
    total_w = sum(words_in)
    n_start = len(acc[:acc.find(q)].split()) if acc.find(q) >= 0 else 0
    n_end = n_start + len(q.split())

    def t_at(n):
        n = max(0, min(n, total_w))
        cum = 0
        for off, wc in enumerate(words_in):
            if n <= cum + wc or off == len(words_in) - 1:
                k = i + off
                t = lines[k][0] + (n - cum) / 2.7
                if k + 1 >= len(lines):
                    t = min(t, lines[k][0] + 12.0)
                return t
            cum += wc
        return lines[j][0] + 3.0

    tin, tout = t_at(n_start), t_at(n_end)
    # completeness + padding bounds at plausible speech rates (caption lag guard)
    W = max(1, len(q.split()))
    lo, hi = tin + W / 3.6 + 0.4, tin + W / 2.0 + 5.5
    if tout < lo: tout = lo
    if tout > hi: tout = hi
    if tout < tin + 0.5: tout = tin + 0.8
    if tout - tin > 300: return None
    return tin, tout

def parse_units():
    units = {}
    for path in sorted(glob.glob('excavations/ss*.md')+glob.glob('excavations/dl*.md')):
        sess = os.path.basename(path)[:-3]
        cur = None
        for line in open(path, encoding='utf-8'):
            m = re.match(r'### (ss\d+-\d+|dl\d+-\d+) — (.*)\[(A|B|C)\](?: \[text:[^\]]*\])?$', line)
            if m:
                if cur: units[cur['uid']] = cur
                cur = {'uid':m.group(1),'sess':sess,'title':m.group(2).strip(),'grade':m.group(3)}
            elif cur is not None and line.startswith('- '):
                k,_,v = line[2:].partition(':')
                if k in ('timestamp','quote'): cur[k] = v.strip()
        if cur: units[cur['uid']] = cur
    return units

def parse_assign():
    a = {}
    for l in open('excavations/SPINE_ASSIGN.tsv').read().splitlines()[1:]:
        if l.strip():
            f = l.split('\t'); a[f[0]] = {'grade':f[2],'sec':f[3]}
    return a

def sesskey(sess, tin):
    s = 0 if sess == 'dl1' else int(sess[2:])
    return (s, tin)

def sa_order():
    """SECTION_ARGUMENTS uid order per section (join-audited canonical)."""
    txt = open('build/SECTION_ARGUMENTS.md', encoding='utf-8').read()
    secs = {}
    cur = None
    for line in txt.splitlines():
        m = re.match(r'^# (\d) · ', line)
        if m: cur = int(m.group(1)); secs[cur] = []
        m2 = re.search(r'— (ss\d+-\d+|dl\d+-\d+)\s*$', line)
        if m2 and cur: secs[cur].append(m2.group(1))
    return secs

# essay-0 cell clips (M22: cell uids are A by law) — SEED-CAP: play at layer heads
# inside essay0 only, never in section lists (vatula G3 stacked-motto rule).
CELLS = {'ss3-10':1,'ss4-15':2,'ss12-16':3,'ss7-06':4,'ss11-05':5,'ss13-09':6}

def main():
    units = parse_units(); assign = parse_assign(); sa = sa_order()
    V = json.load(open('build/holdup_verdicts.json'))['verdicts']
    keeps = {u for u,v in V.items() if v == 'KEEP-B'}
    # grades/sections sanity vs TSV
    for u,d in units.items():
        assert u in assign, f'{u} missing in SPINE_ASSIGN'
        assert assign[u]['grade'] == d['grade'], f"grade mismatch {u}: {d['grade']} vs {assign[u]['grade']}"
    # mp3 durations
    dur = {}
    for s,vid in MP3.items():
        p = mp3path(s)
        assert os.path.exists(p), f'missing {p}'
        r = subprocess.run(['ffprobe','-v','error','-show_entries','format=duration',
                            '-of','csv=p=0',p], capture_output=True, text=True)
        dur[s] = float(r.stdout.strip())
    # cut stamps for every unit in play (all 307 for future C too — compute lazily per manifest set)
    cache = {}
    def stamp(u):
        if u in cache: return cache[u]
        d = units[u]
        w = re.search(r'\[(\d{2}:\d{2}:\d{2})\]-->\[(\d{2}:\d{2}:\d{2})\]', d.get('timestamp',''))
        ws, we = (ts2s(w.group(1)), ts2s(w.group(2))) if w else (None, None)
        res = locate(load_lines(d['sess']), d['quote'].strip('"'), ws, we)
        assert res, f'quote not located: {u}'
        tin, tout = res
        assert tout - tin < 300, f'suspicious span {u}: {tout-tin}s'
        assert tout <= dur[d['sess']] + 1, f'past EOF {u}'
        cache[u] = (tin, tout)
        return tin, tout

    CARD = {
     1:{'question':'What is consciousness?','sanskrit':'caitanyamatma','sutra':'1.1',
        'translation':'Consciousness is the Self.','plain':'consciousness is the self',
        'ref':'Aphorisms l.735/736 (word) · trans l.168'},
     2:{'question':'What keeps consciousness from being realised?','sanskrit':'jnanambandhah','sutra':'1.2',
        'translation':'Knowledge is bondage.','plain':'knowledge is bondage',
        'ref':'Aphorisms l.769/770 · trans l.169'},
     3:{'question':'How does realisation happen?','sanskrit':'udyamo bhairavah','sutra':'1.5',
        'translation':'Bhairava is upsurge.','plain':'bhairava is upsurge',
        'ref':'Aphorisms l.979/980 · trans l.173'},
     4:{'question':'What does realisation do to experience?','sanskrit':'tritayabhokta vtresah','sutra':'1.11',
        'translation':'The enjoyer of the three states is the Lord of the Heroes.',
        'plain':'the enjoyer of the three states is the lord of the heroes',
        'ref':'Aphorisms l.1401 (OCR-verify) · trans l.181'},
     5:{'question':'What does the mind have to do with consciousness?','sanskrit':'cittam mantrah','sutra':'2.1',
        'translation':'The mind is Mantra.','plain':'the mind is mantra',
        'ref':'Aphorisms l.2325/2326 · trans l.223'},
     6:{'question':'What happens after realisation?','sanskrit':'nartaka atma','sutra':'3.9',
        'translation':'The Self is the actor.','plain':'the self is the actor',
        'ref':'Aphorisms l.3763/3764 · trans l.265'},
    }

    def build(sec, layer):
        # C = all units in her order (demotes + original C play as texture);
        # ss4-22 skipped: nested duplicate of ss12-10 (M23b — keep the longer).
        SKIP = {'ss4-22'}
        sec_uids = [u for u,d in units.items() if assign[u]['sec'] == str(sec)
                    and u not in CELLS and u not in SKIP
                    and (d['grade'] in ('A','B') if layer=='B'
                         else True if layer=='C' else d['grade']=='A')]
        # restrict B to A + keeps; C keeps everything else too
        if layer == 'B':
            sec_uids = [u for u in sec_uids if units[u]['grade']=='A' or u in keeps]
        # canonical base = SA order ∩ this set, then insert the rest by (sess,t)
        stamps = {u: stamp(u) for u in sec_uids}
        base = [u for u in sa[sec] if u in sec_uids]
        missing = [u for u in sec_uids if u not in base]
        # SA order is canonical (join-audited) even where within-session time jumps;
        # require: session-blocks contiguous + ascending across the section.
        def blocks(seq):
            out = []
            for u in seq:
                s = units[u]['sess']
                if out and out[-1][0] == s: out[-1][1].append(u)
                else: out.append([s, [u]])
            return out
        bb = blocks(base)
        snums = [0 if s == 'dl1' else int(s[2:]) for s,_ in bb]
        assert snums == sorted(snums) and len(set(snums)) == len(snums), f'S{sec} blocks bad: {snums}'
        # insert missing: by session block (create if absent), by timestamp inside block
        for u in sorted(missing, key=lambda x: sesskey(units[x]['sess'], stamps[x][0])):
            s = units[u]['sess']; t = stamps[u][0]
            bi = next((i for i,(bs,_) in enumerate(bb) if bs == s), None)
            if bi is None:
                sn = 0 if s == 'dl1' else int(s[2:])
                bi = next((i for i,(bs,_) in enumerate(bb)
                           if (0 if bs=='dl1' else int(bs[2:])) > sn), len(bb))
                bb.insert(bi, [s, []])
            blk = bb[bi][1]
            pos = next((k for k,ub in enumerate(blk) if stamps[ub][0] > t), len(blk))
            blk.insert(pos, u)
        base = [u for _,us in bb for u in us]
        assert len(base) == len(sec_uids), (len(base), len(sec_uids))
        beats = []
        for i,u in enumerate(base, 1):
            d = units[u]; tin, tout = stamps[u]
            beats.append({'seq':i,'uid':u,'session':d['sess'],'mp3':mp3path(d['sess']),
                          't_in':round(tin,1),'t_out':round(tout,1),
                          'dur':round(tout-tin,1),'grade':d['grade'],'title':d['title']})
        total = sum(b['dur'] for b in beats)
        man = {'section':f'S{sec}','layer':layer,'question':CARD[sec]['question'],
               'card':CARD[sec],'source_order':'SECTION_ARGUMENTS (join-audited) + (sess,ts) inserts',
               'clip_count':len(beats),'window_seconds':round(total,1),
               'window_runtime':s2ts(total),'beats':beats}
        return man

    out = {}
    for sec in range(1,7):
        for layer in ('A','B','C'):
            m = build(sec, layer)
            p = f"build/manifest_s{sec}_{layer}.json"
            json.dump(m, open(p,'w'), indent=1, ensure_ascii=False)
            out[f'S{sec}{layer}'] = (m['clip_count'], m['window_runtime'])
    print(f"{'':6} {'clips':>6} {'window-rt':>10}")
    for layer in ('A','B','C'):
        ta = sum(json.load(open(f'build/manifest_s{s}_{layer}.json'))['window_seconds'] for s in range(1,7))
        n = sum(json.load(open(f'build/manifest_s{s}_{layer}.json'))['clip_count'] for s in range(1,7))
        print(f"LAYER {layer}: {n} clips, {ta/60:.1f}m windows")
    for sec in range(1,7):
        a = out[f'S{sec}A']; b = out[f'S{sec}B']; c = out[f'S{sec}C']
        print(f"S{sec}   A {a[0]:3d} {a[1]:>9}   B {b[0]:3d} {b[1]:>9}   C {c[0]:3d} {c[1]:>9}")

if __name__ == '__main__':
    main()
