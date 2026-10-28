#!/usr/bin/env python3
"""Coverage measurement: unit timestamp-spans vs original transcript lines/words.
Run: python3 tools/coverage_measure.py [--corpus baumer|lak|all]  (from repo root)
  baumer (default): Custom-compilation truth — Baumer/dl1 units vs Baumer
    transcripts (lak_* excluded; pre-Standard numbers restored).
  lak: Standard-compilation walk — per-verse manifest windows (0/A/B/C/D)
    vs Lakshmanjoo transcripts (no units exist there; windows are the claim).
  all: both tables side by side (denominators never mixed)."""
import re,glob,os,sys,json
from collections import defaultdict

CORPUS = sys.argv[sys.argv.index("--corpus")+1] if "--corpus" in sys.argv else "baumer"
assert CORPUS in ("baumer", "lak", "all"), CORPUS

def ts(s):
    h,m,sec=map(int,s.split(':')); return h*3600+m*60+sec

def main():
    srcunits=defaultdict(list)
    for f in sorted(glob.glob('excavations/ss*.md')):
        txt=open(f).read()
        m=re.search(r'^Source: `([^`]+)`',txt,re.M)
        if not m: print('NO SOURCE:',f,file=sys.stderr); continue
        for um in re.finditer(r'### ([a-z0-9\-]+) — .*\n- timestamp: \[(\d+:\d+:\d+)\]-->\[(\d+:\d+:\d+)\]',txt):
            srcunits[m.group(1)].append((ts(um.group(2)),ts(um.group(3)),um.group(1)))

    ANC={
     'S1':r'conscious|\bself\b|atman|samwit|samvit|chaitanya|recogni|realiz|realis',
     'S2':r'bondage|ignoran|mala|maya|veil|limit|imperf|anava|obstacle',
     'S3':r'upsurge|bhairava|spon[n]?taneous|effort|grace|sahaja|sudden|aris',
     'S4':r'bliss|wonder|heart|enjoy|ecstas|happi|delight|anand',
     'S5':r'\bmantra\b|\bmind\b|attention|awareness|guru|practice|meditat|concentr',
     'S6':r'\bethic\b|\bplay\b|\bstage\b|senses|sameness|after|drama|actor|household',
    }
    hit={k:[0,0] for k in ANC}
    rows=[]; T=C=W=CW=0
    for f in sorted(glob.glob('text/*.txt')):
        bn = os.path.basename(f)
        if bn.endswith('introduction_dl.txt'): continue
        if CORPUS == "baumer" and bn.startswith("lak_"): continue
        if CORPUS == "lak" and not bn.startswith("lak_"): continue
        tl=[]
        for L in open(f):
            m=re.match(r'^\[(\d+:\d+:\d+)\]\s*(.+)$',L)
            if m: tl.append((ts(m.group(1)),m.group(2)))
        if not tl: continue
        dur=max(t for t,_ in tl)
        spans=sorted((a,b) for a,b,_ in srcunits.get(f,[]))
        merged=[]
        for a,b in spans:
            if merged and a<=merged[-1][1]+1: merged[-1][1]=max(merged[-1][1],b)
            else: merged.append([a,b])
        cs=sum(b-a for a,b in merged)
        cl=[(t,x) for t,x in tl if any(a<=t<=b for a,b in merged)]
        for t,x in tl:
            cov=any(a<=t<=b for a,b in merged)
            for k,pat in ANC.items():
                if re.search(pat,x.lower()): hit[k][0 if cov else 1]+=1
        tw=sum(len(x.split()) for _,x in tl); cw=sum(len(x.split()) for _,x in cl)
        rows.append((os.path.basename(f),dur,len(srcunits.get(f,[])),cs,len(tl),len(cl),tw,cw))
        T+=dur; C+=cs; W+=tw; CW+=cw

    print(f'{"file":46s}{"dur":>6}{"unit":>5}{"span%":>7}{"line%":>7}{"word%":>7}')
    for f,dur,nu,cs,nl,cl,tw,cw in rows:
        print(f'{f:46s}{dur//60:>4}m{nu:>5}{100*cs/max(dur,1):>6.1f}%{100*cl/nl:>6.1f}%{100*cw/tw:>6.1f}%')
    print(f'\nTOTAL: {T//60}m audio · span {C//60}m = {100*C/T:.1f}% · words {CW}/{W} = {100*CW/W:.1f}%')
    print(f'\n{"section":9s}{"covered":>9}{"uncovered":>10}{"%":>5}')
    for k in ANC:
        c,u=hit[k]; tot=c+u
        print(f'{k:9s}{c:>9}{u:>10}{100*c/tot if tot else 0:>4.0f}%')

    if CORPUS in ("lak", "all"):
        # Standard walk: manifest windows (all layers) vs lak transcripts.
        # Slug match: manifest src "Shiva Sutras 1.11.mp3" <-> text/lak_1_11.txt
        # (plus the 1.8-10 / 2.7p1p2 / intro / conclusion / 3.intro specials).
        def slug_of(src):
            b = os.path.basename(src)
            if not b.startswith("Shiva Sutras"):
                return None
            core = b[len("Shiva Sutras "):-len(".mp3")]
            if core == "1.8-10": return "lak_1_8_10"
            if core in ("2.7", "2.7 part 1"): return "lak_2_7_p1"
            if core == "2.7 part 2": return "lak_2_7_p2"
            if core == "Introduction": return "lak_intro"
            if core == "Conclusion": return "lak_conclusion"
            if core == "3. Introduction": return "lak_3_intro"
            return "lak_" + core.replace(".", "_")
        byslug = defaultdict(list)
        for mf in glob.glob('build/std_*.json'):
            man = json.load(open(mf))
            for pcs in man.get("layers", {}).values():
                for p in pcs:
                    if p.get("file", "").endswith(".wav"):
                        continue  # prebuilt TTS, not lecture audio
                    src = p.get("src", man["src"])
                    if "sharma" in os.path.basename(src).lower():
                        continue  # chant fallback lives outside lak files
                    s = slug_of(src)
                    if s:
                        byslug[s].append((p["t_in"], p["t_out"]))
        # 2.7 lives in two files; slug_of already maps part 1/2 directly.
        print(f'\n{"=== LAK (Standard manifest windows)":60s}')
        print(f'{"file":46s}{"dur":>6}{"wins":>5}{"span%":>7}')
        LT = LC = 0
        for f in sorted(glob.glob('text/lak_*.txt')):
            tl = []
            for L in open(f):
                m = re.match(r'^\[(\d+:\d+:\d+)\]\s*(.+)$', L)
                if m: tl.append(ts(m.group(1)))
            if not tl: continue
            dur = max(tl)
            bn = os.path.basename(f)[:-4]
            merged = []
            for a, b in sorted(byslug.get(bn, [])):
                if merged and a <= merged[-1][1] + 1: merged[-1][1] = max(merged[-1][1], b)
                else: merged.append([a, b])
            cs = sum(b - a for a, b in merged)
            LT += dur; LC += cs
            print(f'{os.path.basename(f):46s}{dur//60:>4}m{len(byslug.get(bn, [])):>5}{100*cs/max(dur,1):>6.1f}%')
        print(f'\nLAK TOTAL: {LT//60}m audio · walked {LC//60}m = {100*LC/max(LT,1):.1f}%')


if __name__=='__main__': main()
