#!/usr/bin/env python3
"""YT rolling VTT -> readable timestamped txt.
Keep only plain cues (no <c>/<00: inline tags), strip, skip empty and
consecutive exact dupes. Output: [HH:MM:SS] text  per line."""
import re, sys, os, glob, json

def ts(hms):
    h,m,s = hms.split(':'); s=s.split('.')[0]
    return f'{int(h):02d}:{m}:{s}'

def convert(path):
    cues, block = [], []
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        if '-->' in line:
            if block: cues.append(block)
            block = [line]
        elif block is not None:
            if line.strip()=='' :
                if block: cues.append(block); block=[]
            else:
                block.append(line)
    if block: cues.append(block)
    out, prev = [], None
    for blk in cues:
        hdr = blk[0]
        m = re.match(r'(\d{2}:\d{2}:\d{2}\.\d{3}) -->', hdr)
        if not m: continue
        text = ' '.join(blk[1:]).replace('\n',' ').strip()
        if '<c>' in text or '<00:' in text or not text:
            continue
        text = re.sub(r'\s+',' ',text).strip()
        if text == prev: continue
        out.append(f'[{ts(m.group(1))}] {text}')
        prev = text
    return out

if __name__ == '__main__':
    manifest = {r['id']: r for r in json.load(open('/home/ubuntu/shiva-sutras/MANIFEST.json'))}
    os.makedirs('/home/ubuntu/shiva-sutras/text', exist_ok=True)
    for f in sorted(glob.glob('/home/ubuntu/shiva-sutras/transcripts/*.en.vtt')):
        vid = os.path.basename(f).split('.')[0]
        title = manifest[vid]['title'] if vid in manifest else vid
        slug = re.sub(r'[^a-z0-9]+','_', title.lower()).strip('_')
        lines = convert(f)
        dest = f'/home/ubuntu/shiva-sutras/text/{slug}.txt'
        open(dest,'w').write('\n'.join(lines)+'\n')
        words = sum(len(l.split())-1 for l in lines)
        print(f'{slug:40} {len(lines):5} lines  {words:6} words')
