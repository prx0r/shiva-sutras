#!/usr/bin/env python3
"""S2 segmentation: keyword-score every unit's transcript window, assign exactly
one section (analayo 02 method). Deterministic; totals must reconcile (180/180).
Usage: python3 tools/s2_cluster.py [--apply]  (default: report only)
Writes excavations/SPINE_ASSIGN.tsv (uid, section, score, margin, fallback?)
"""
import re, glob, os, sys, collections

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESS = {'ss1':'text/shiva_sutras_day_1_introduction_i.txt','ss2':'text/shiva_sutras_day_1_introduction_ii.txt',
 'ss3':'text/shiva_sutras_day_2_introduction_iii.txt','ss4':'text/shiva_sutras_day_2_session_i.txt',
 'ss5':'text/shiva_sutras_day_3_session_i.txt','ss6':'text/shiva_sutras_day_3_session_ii.txt',
 'ss7':'text/shiva_sutras_day_4_session_i.txt','ss8':'text/shiva_sutras_day_4_session_ii_part_1.txt',
 'ss9':'text/shiva_sutras_day_4_session_ii_part_ii.txt','ss10':'text/shiva_sutras_day_5_session_i.txt',
 'ss11':'text/shiva_sutras_day_5_session_ii.txt','ss12':'text/shiva_sutras_day_6_session_i.txt',
 'ss13':'text/shiva_sutras_day_6_session_ii.txt','dl1':'text/shiva_sutras_introduction_dl.txt'}
PRIMARY = {'dl1':1,'ss1':1,'ss2':1,'ss3':1,'ss4':1,'ss5':2,'ss6':3,'ss7':4,'ss8':4,'ss9':4,'ss10':6,'ss11':5,'ss12':5,'ss13':6}

def norm(s):
    s = re.sub(r'\s+',' ',s).strip().lower(); return re.sub(r'[^a-z0-9 ]','',s)

ALIASES = {'chaitanya':'caitanya','sambit':'samvit','shambhava':'sambhava',
 'shambhavapaya':'sambhavopaya','swatantria':'svatantrya','vishranti':'visranti',
 'unmesha':'unmesa','nimajana':'nimajjana','cheetah':'citta',
 'kanchuka':'kancuka','kanchuga':'kancuka','utyama':'udyama','veera':'vira',
 'turia':'turya','toria':'turya','prabhuta':'prabuddha','suprabuta':'suprabuddha',
 'ichha':'iccha','jivanmukta':'jivan muk','jivanmukti':'jivan muk',
 'matrka':'matrka','matrika':'matrka'}

def alias(s):
    for a,b in sorted(ALIASES.items(), key=lambda x:-len(x[0])):
        s = re.sub(r'\b'+a+r'\b', b, s)
    return s

# section: [(term, weight)]
PROFILES = {
 1: [('caitanya',2),('samvit',2),('innermost nature',2),('light of consciousness',2),('rock',2),
     ('universal consciousness',1),('not individual',2),('freedom',1),('svatantrya',2),('consciousness is',1),
     ('absolute consciousness',1),('nothing is',1),('matter is',1),('shankapal',2),('stone',1),
     ('lineage',1),('commentator',1),('siddhanta',1),('history',1),('revelation',1),('vasugupta',2),
     ('agama',1),('darshana',1),('start from the',1)],
 2: [('bandha',2),('mala',2),('anava',2),('karma mala',2),('ignorance',2),('incomplete',2),
     ('apurna',2),('original sin',2),('impurity',1),('kancuka',2),('armor',1),('limitation',1),
     ('veil',2),('conceal',1),('samsara',1),('dualistic knowledge',2),('differentiated knowledge',2),
     ('yoni',2),('womb',2),('maya',1),('fragment',1),('threshold',1)],
 3: [('udyama',2),('upsurge',2),('sudden',2),('sambhava',2),('visranti',2),('anupaya',2),
     ('transmission',2),('shaktipata',2),('flash',2),('unmesa',2),('nimajjana',1),('sahaja',2),
     ('spontaneous',1),('thought free',1),('grace',1),('darshan',1),('elevated',2),
     ('no ladder',2),('no method',1),('from above',1)],
 4: [('turya',2),('waking',1),('dream',1),('sleep',1),('jagrat',1),('vira',2),('hero',1),
     ('iccha',2),('heart',2),('enjoy',1),('wonder',1),('prabuddha',2),('suprabuddha',2),
     ('dream yoga',2),('nine states',2),('fourth state',1),('chakra',1),('wheel of energies',2),('hub',1)],
 5: [('mantra is',2),('mind is',2),('reciter',2),('utter',1),('malini',2),
     ('pure thought',2),('jnana',1),('upaya',1),('initiation',2),('ritual',1),('puja',2),
     ('homa',1),('oblation',1),('worship',1),('deity',1),('letter',1),('alphabet',1),
     ('syllable',1),('citta',1)],
 6: [('jivan muk',2),('offering',2),('renunciation',1),('sacrifice',1),('fire',1),
     ('dancer',2),('actor',2),('ranga',2),('spectator',2),('samadhi',1),('sameness',2),
     ('compassion',2),('radiance',1),('siddhi',2),('powers',1),('temple',1),
     ('pranayama',1),('ethics',2),('nonviolent',2),('devotion',1),('liberation',1),
     ('moksha',1),('fruit',1)],
}
def score(text):
    out = {}
    for sec, terms in PROFILES.items():
        s = 0
        for t, w in terms:
            s += len(re.findall(r'\b'+re.escape(t)+r's?\b', text)) * w
        out[sec] = s
    return out

def load_transcripts():
    out = {}
    for k, p in SESS.items():
        lines = open(os.path.join(BASE, p), encoding='utf-8').read().splitlines()
        out[k] = lines
    return out

def ts_of(line):
    m = re.match(r'\[(\d{2}):(\d{2}):(\d{2})\]', line)
    return (int(m.group(1))*3600+int(m.group(2))*60+int(m.group(3))) if m else None

def parse_units():
    units = []
    for p in sorted(glob.glob(os.path.join(BASE, 'excavations/ss*.md')) + glob.glob(os.path.join(BASE, 'excavations/dl*.md'))):
        lec = os.path.basename(p).removesuffix('.md')
        if lec == 'ss_SCHEMA': continue
        cur = None
        for line in open(p, encoding='utf-8'):
            s = line.rstrip('\n')
            if s.startswith('### ss') or s.startswith('### dl'):
                m = re.match(r'### (ss\d+-\d+|dl\d+-\d+)', s)
                cur = {'uid': m.group(1), 'file': lec, 'grade': (__import__('re').search(r'\[(A|B|C)\](\s*\[text:|\s*$)', s).group(1) if __import__('re').search(r'\[(A|B|C)\](\s*\[text:|\s*$)', s) else 'C'), 'fields': {}}
                units.append(cur)
            elif cur is not None and s.startswith('- ') and ':' in s:
                k, v = s[2:].split(':', 1); cur['fields'][k.strip()] = v.strip()
    return units

def main():
    txt = load_transcripts()
    # transcript seconds per file for window lookup
    tss = {}
    for k, lines in txt.items():
        tss[k] = [ts_of(l) for l in lines]
    units = parse_units()
    rows, fallback = [], 0
    for u in units:
        lec = u['file']
        m = re.match(r'\[(\d{2}):(\d{2}):(\d{2})\]', u['fields'].get('timestamp',''))
        if m:
            t0 = int(m.group(1))*3600+int(m.group(2))*60+int(m.group(3))
            idx = [i for i,t in enumerate(tss[lec]) if t is not None and abs(t-t0) <= 300]
            lo, hi = (min(idx)-6, max(idx)+6) if idx else (0, 0)
            window = txt[lec][max(0,lo):hi+1]
        else:
            window = []
        span = alias(norm(' '.join(re.sub(r'\[\d{2}:\d{2}:\d{2}\] ?','',l) for l in window)))
        span += ' ' + alias(norm(u['fields'].get('quote','')))
        sc = score(span)
        best = max(sc, key=lambda k: sc[k])
        top = sorted(sc.values(), reverse=True)[:2]
        margin = top[0]-top[1]
        fb = ''
        if top[0] == 0 or margin == 0 or (margin <= 2 and top[0] < 12):
            best = PRIMARY[lec]; fb = 'primary' if top[0]==0 else ('tie-primary' if margin==0 else 'thin->primary')
            fallback += 1
        rows.append((u['uid'], lec, u['grade'], best, sc[best], margin, fb))
    OVER = {'ss1-08':1,'ss1-09':1,'ss1-25':1,'ss1-26':1,'ss2-01':1,'ss2-03':1,'ss2-04':1,
     'ss3-17':6,'ss4-19':2,'ss5-07':2,'ss5-12':2,'ss6-06':1,'ss6-09':5,'ss6-16':6,'ss6-17':6,
     'ss7-14':4,'ss7-16':4,'ss9-02':2,'ss10-01':5,'ss10-03':6,'ss10-05':3,'ss10-06':3,
     'ss10-09':6,'ss10-11':6,'ss11-01':5,'ss12-02':1,'ss12-11':6,'ss12-14':6,'ss12-15':6,'ss13-01':1,
     'ss9-03':1,'ss7-01':1,'ss6-18':5,'ss8-01':1,'ss12-16':3,
     'ss3-03':5,'ss3-04':5,'ss4-21':5,'ss4-22':5,'ss6-11':5,'ss12-09':5,'ss12-10':5,
     'ss10-07':5,'ss12-05':5,'ss5-09':5,'ss9-01':6,'ss7-18':3,'ss13-03':3,'ss8-04':4}
    rows = [(r[0],r[1],r[2],OVER.get(r[0],r[3]),r[4],r[5],'verdict' if r[0] in OVER else r[6]) for r in rows]
    print(f'units={len(rows)} fallback={fallback} verdict-overrides={len(OVER)}')
    by = collections.Counter(r[3] for r in rows)
    print('assignment:', dict(sorted(by.items())), 'total:', sum(by.values()))
    aga = collections.Counter((r[3]) for r in rows if r[2]=='A')
    print('A-density:', dict(sorted(aga.items())))
    if '--apply' in sys.argv:
        with open(os.path.join(BASE,'excavations/SPINE_ASSIGN.tsv'),'w') as f:
            f.write('uid\tfile\tgrade\tsection\tscore\tmargin\tfallback\n')
            for r in rows: f.write('\t'.join(map(str,r))+'\n')
        print('wrote SPINE_ASSIGN.tsv')

if __name__ == '__main__': main()
