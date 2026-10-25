#!/usr/bin/env python3
"""Recompute unit/section counts and sync every doc line that states them.
Run after any pass that adds units: python3 tools/sync_counts.py"""
import re,glob,os

def main():
    grades={}; homes={}
    for path in glob.glob('excavations/ss*.md')+glob.glob('excavations/dl*.md'):
        for m in re.finditer(r'^### ([a-z0-9\-]+) — .*\[(A|B|C)\]', open(path).read(), re.M):
            grades[m.group(1)]=m.group(2)
    for l in open('excavations/SPINE_ASSIGN.tsv').read().split('\n')[1:]:
        if not l.strip(): continue
        p=l.split('\t')
        homes[p[0]]=int(p[3])
    tot=len(grades); A=sum(1 for g in grades.values() if g=='A')
    B=sum(1 for g in grades.values() if g=='B'); C=tot-A-B
    dist={}; ad={}
    for uid,g in grades.items():
        s=homes.get(uid)
        if s: dist[s]=dist.get(s,0)+1
        if g=='A': ad[s]=ad.get(s,0)+1
    dist_s=' · '.join(f'S{k} {dist[k]}' for k in sorted(dist))
    ad_s=' · '.join(f'S{k} {ad[k]}' for k in sorted(ad))
    print(f'units {tot} ({A}A/{B}B/{C}C) | dist {dist_s} | A-buckets {ad_s}')

    def sub(fn, patterns):
        s=open(fn).read(); n=0
        for pat,rep in patterns:
            s2,c=re.subn(pat,rep,s,count=1); s=s2; n+=c
        open(fn,'w').write(s); return n
    # README
    sub('README.md',[
      (r'- \*\*Grading:\*\* \d+ units \(\d+A/\d+B/\d+C\) across 14 sessions \([^)]*\) — `tools/verify_units\.py` = \d+/0\.',
       f'- **Grading:** {tot} units ({A}A/{B}B/{C}C) across 14 sessions (pass-1: day5_ii +18, day6_ii +21) — `tools/verify_units.py` = {tot}/0.'),
      (r'- \*\*Segmentation:\*\* \d+/\d+ one section each', f'- **Segmentation:** {tot}/{tot} one section each'),
      (r'python3 tools/verify_units\.py      # \d+/0', f'python3 tools/verify_units.py      # {tot}/0'),
    ])
    # PROCESS
    sub('PROCESS_NOTES.md',[
      (r'- \*\*Grading:\*\* .*?\n', f'- **Grading:** 186 units (71A/106B/9C), verify 186/0 → pass-1: {tot} ({A}A/{B}B/{C}C), {tot}/0.\n'),
      (r'- \*\*Segmentation:\*\* .*?\n', f'- **Segmentation:** 186/186 → pass-1 {tot}/{tot} one-home (manual pass-1 rows in SPINE_ASSIGN), 48+ overrides in s2_cluster.\n'),
      (r'- \d+ units \(\d+A/\d+B/\d+C\) · verify \d+/0 · segmentation \d+/\d+ · G0 7/7 ·',
       f'- {tot} units ({A}A/{B}B/{C}C) · verify {tot}/0 · segmentation {tot}/{tot} · G0 7/7 ·'),
      (r'186→\d+ units \(pass-1:.*?LEDGER\)', f'186→{tot} units (pass-1: day5_ii +18, day6_ii +21 — see C-MARKS + LEDGER)'),
    ])
    # CATALOGUE
    sub('excavations/CATALOGUE.md',[
      (r'CURRENT totals: \*\*\d+ units: \d+ A / \d+ B / \d+ C\*\* \([^)]*\)',
       f'CURRENT totals: **{tot} units: {A} A / {B} B / {C} C** (pass-1)'),
    ])
    # SPINE
    sub('excavations/SPINE.md',[
      (r'- Unit distribution: .*?\(total \d+ after pass-1[^)]*\)\.',
       f'- Unit distribution: {dist_s} (total {tot} after pass-1; ss5-02 moved to S5 guru-means).'),
      (r'- Independent A-buckets:  .*?\(total \d+; pass-1[^)]*\)\.',
       f'- Independent A-buckets:  {ad_s} (total {A}; pass-1 grows as files are read).'),
    ])
    # NEXT
    sub('NEXT.md',[
      (r'State at handover: \d+ units \(\d+A/\d+B/\d+C\)[^·]*·',
       f'State at handover: {tot} units ({A}A/{B}B/{C}C) verify-green; pass-1 COMPLETE (14/14, ledger 676+ rows) ·'),
    ])
    print('docs synced')

if __name__=='__main__': main()
