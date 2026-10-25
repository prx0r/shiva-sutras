#!/usr/bin/env python3
"""Coverage measurement: unit timestamp-spans vs original transcript lines/words.
Run: python3 tools/coverage_measure.py   (from repo root)"""
import re,glob,os,sys
from collections import defaultdict

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
        if f.endswith('introduction_dl.txt'): continue
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

if __name__=='__main__': main()
