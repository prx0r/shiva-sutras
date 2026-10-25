#!/usr/bin/env python3
"""Gap report: uncovered transcript spans per source file, worst-served first.
Run: python3 tools/gap_report.py [file-substring]"""
import re,glob,os,sys
from collections import defaultdict

def ts(s):
    h,m,sec=map(int,s.split(':')); return h*3600+m*60+sec
def hhmm(t): return f'{t//3600:02d}:{t%3600//60:02d}:{t%60:02d}'

def gaps(f, spans):
    tl=[]
    for i,L in enumerate(open(f),1):
        m=re.match(r'^\[(\d+:\d+:\d+)\]\s*(.+)$',L)
        if m: tl.append((i,ts(m.group(1)),m.group(2)))
    merged=[]
    for a,b in sorted(spans):
        if merged and a<=merged[-1][1]+1: merged[-1][1]=max(merged[-1][1],b)
        else: merged.append([a,b])
    out=[]; cur=None
    for i,t,x in tl:
        cov=any(a<=t<=b for a,b in merged)
        if not cov:
            if cur is None: cur=[i,i,t,t,len(x.split())]
            else: cur[1]=i; cur[3]=t; cur[4]+=len(x.split())
        else:
            if cur: out.append(cur); cur=None
    if cur: out.append(cur)
    return out

def main():
    srcunits=defaultdict(list)
    for ef in sorted(glob.glob('excavations/ss*.md')):
        txt=open(ef).read()
        m=re.search(r'^Source: `([^`]+)`',txt,re.M)
        for um in re.finditer(r'### ([a-z0-9\-]+) — .*\n- timestamp: \[(\d+:\d+:\d+)\]-->\[(\d+:\d+:\d+)\]',txt):
            srcunits[m.group(1)].append((ts(um.group(2)),ts(um.group(3))))
    files=sorted(glob.glob('text/*.txt'))
    if len(sys.argv)>1: files=[f for f in files if sys.argv[1] in f]
    for f in files:
        if f.endswith('dl1.txt') or not srcunits.get(f): continue
        g=gaps(f,srcunits[f])
        total=sum(x[4] for x in g)
        print(f'\n== {os.path.basename(f)} — {len(g)} gaps, {total} uncovered words')
        for a,b,t1,t2,w in g:
            print(f'  L{a}-{b}  [{hhmm(t1)}-{hhmm(t2)}]  {w}w')

if __name__=='__main__': main()
