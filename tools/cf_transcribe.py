#!/usr/bin/env python3
"""Cloudflare whisper-large-v3-turbo transcription (port of analayo tools/cf_whisper.py,
creds from ~/figgsite/.env CF_ACCOUNT_ID/CF_API_TOKEN — never echo). Usage:
python3 cf_transcribe.py <audio> <out.json>"""
import base64, json, urllib.request, subprocess, math, sys, time, os
LECT, OUT = sys.argv[1], sys.argv[2]
env = {}
for line in open(os.path.expanduser('~/figgsite/.env')):
    line = line.strip()
    if line and not line.startswith('#') and '=' in line:
        k, v = line.split('=', 1); env[k] = v.strip().strip('"').strip("'")
KEY, ACCT = env['CF_API_TOKEN'], env['CF_ACCOUNT_ID']
URL = f'https://api.cloudflare.com/client/v4/accounts/{ACCT}/ai/run/@cf/openai/whisper-large-v3-turbo'
dur = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',LECT]).strip())
CH = 600
n = math.ceil(dur / CH)
segments = []
for i in range(n):
    seg = f'/tmp/opencode/cfseg_ss_{os.getpid()}.mp3'
    subprocess.run(['ffmpeg','-v','error','-ss',str(i*CH),'-t',str(CH),'-i',LECT,'-b:a','64k','-y',seg], check=True)
    audio = base64.b64encode(open(seg,'rb').read()).decode()
    body = json.dumps({'audio': audio, 'task': 'transcribe'}).encode()
    for attempt in range(5):
        try:
            req = urllib.request.Request(URL, data=body,
                headers={'Authorization': f'Bearer {KEY}','Content-Type':'application/json'})
            with urllib.request.urlopen(req, timeout=300) as r:
                d = json.load(r)
            if not d.get('success'): raise RuntimeError(str(d.get('errors'))[:200])
            break
        except Exception as e:
            if attempt == 4: raise
            print(f'  retry {attempt+1}: {str(e)[:120]}', flush=True)
            time.sleep(5 * (attempt + 1))
    res = d.get('result', {})
    off = i * CH
    for s in res.get('segments', []):
        segments.append({'t': round(off + float(s['start']), 2),
                         'end': round(off + float(s['end']), 2),
                         'text': s['text'].strip()})
    print(f'chunk {i+1}/{n} -> {len(res.get("segments",[]))} segments', flush=True)
    os.remove(seg)
json.dump({'source': LECT, 'duration': dur, 'engine': 'cf-whisper-large-v3-turbo',
           'sentences': segments}, open(OUT,'w'), ensure_ascii=False, indent=1)
print('SENTENCES:', len(segments), flush=True)
print('ALL DONE', flush=True)
