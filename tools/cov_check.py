#!/usr/bin/env python3
"""Coverage audit: every verse's book exposition vs A+B audio transcripts.
Output: per-verse term coverage + gap candidates for TTS-or-accept verdicts.
Usage: python3 tools/cov_check.py [verse ...] (default: all)"""
import glob
import json
import os
import re
import sys
import unicodedata
from collections import Counter

BASE = "/home/ubuntu/shiva-sutras"


def fold(s):
    out = []
    for c in unicodedata.normalize("NFD", s):
        if unicodedata.category(c) != "Mn":
            out.append(c.lower())
    return "".join(out).replace("h", "")


STOP = set("""the and his with from that this which have will what when
there their them then thus such every other these those into upon also
may might shall being been were are has have had not you your they them
then there here where while through before after about above below self
same own just like know reality state nature mind siva shiva sutra means
says said does make made much more very can could would should may might
will shall one two first also not but are was were been being have has
had does did done make makes made many much more most very can could
would should may might must shall will therefore thus hence however
although though since while whereas whereas also just even ever never
always often sometimes usually generally particularly especially mainly
mostly largely greatly highly apart alone along around among amongst
another any anyone anything anywhere become becomes became been before
behind being below beside besides between beyond both brief bring
brought build called came cause certain change claim clear come comes
conclude consider contain continue could course deal define describe
does done down during each early either else elsewhere end enough even
ever every everybody everything except exist exists experience
explain express fact far feel few find first follow found from
further gave general give given goes going good great group grow
half happen hard hear held hello help here high him himself his
history hold home however hundred idea identify imag imagine
important include including indeed indicate inside insofar instead
into inward issue its itself just keep kind knew know known knows
large last late later least leave left less like likely little
long look made main make makes many may maybe mean means meant
might mind minus minute miss most move much must myself name
near nearly need never next nobody none nor note nothing now
number oft often once one only onto open order other ought our
ours out over own part particular past pay people per perform
perhaps phenomen place please point poor possible power present
press pretty prior proof prove provide put quite rather reach read
ready real really reason receive recent regard remain remember
resolve respect rest return reveal right rise room round rule run
said same say says second see seem seen self sense sent series
set several shall shape share sharp shed shone short should show
shown side since single site situ slow small smooth soci sole
some somebody somehow someone something sometime sometimes soon
sort sought sound space spare speak special spend spoke spot
spread spring square stand start state still stood stop story
straight strange stretch strip strong stuck study stuff style
subject submit such sudden suffer suggest suit sum super suppose
sure surface system table take taken talk teach tell tend term
test than thank their theirs them themselves then thence there
these they thick thing think third those though thought thousand
threat three threw throat through throw thus tick time today
together told took total touch toward towards track trade
tradition traffic train trans treat trend trial tribe trick
tried tries triple trouble true truly trunk trust truth twice
twist type unable uncle under understand until unto upon upper
urban usage usual vain valid value various vast very video view
visit vital vivid vocabulary voice volume vote voyage wait wake
walk wall want war warm warn waste watch water wave weigh weird
welcome well went were west what whatever when whence whenever
where whereas wherever whether which while whilst white whole
whose why wide wife wild will wish with within without witness
woman wonder wood word work world worry worse worth would wound
write written wrong wrote yard year yell yellow yesterday yet
yield young youth zero zone""".split())


def terms(text):
    return [w for w in re.findall(r"[a-z]{5,}", fold(text)) if w not in STOP]


tpl = {t["verse"]: t for t in json.load(open(BASE + "/build/template_77.json"))}


def audio_text(v):
    man = json.load(open(BASE + "/build/std_%s.json" % v.replace(".", "_")))
    segsf = BASE + "/transcripts/lak_" + v.replace(".", "_") + ".segments.json"
    segs = json.load(open(segsf))["segments"] if os.path.exists(segsf) else []
    out = []
    for L in ("0", "A", "B"):
        for p in man.get("layers", {}).get(L, []):
            src = p.get("src", man["src"])
            if "sharma" in src:
                continue
            out.append(" ".join(s["text"] for s in segs
                                if s["end"] > p["t_in"] and s["t"] < p["t_out"]))
    return " ".join(out)


def audit(v, top=25):
    t = tpl[v]
    doc = t.get("body", "")[:8000]
    dc = Counter(terms(doc))
    au = Counter(terms(audio_text(v)))
    scored = []
    for w, c in dc.most_common(60):
        if len(w) < 5:
            continue
        cov = au.get(w, 0)
        status = "OK" if cov >= 2 or (cov >= 1 and c <= 2) else ("PART" if cov == 1 else "GAP")
        scored.append((w, c, cov, status))
    return scored


if __name__ == "__main__":
    verses = [a for a in sys.argv[1:] if not a.startswith("-")]
    if not verses:
        verses = [t["verse"] for t in json.load(open(BASE + "/build/template_77.json"))]
    for v in verses:
        print("=" * 10, v)
        gaps = []
        for w, c, cov, st in audit(v)[:25]:
            flag = " <<" if st == "GAP" else (" <" if st == "PART" else "")
            print("  %-12s book=%-3d audio=%-3d %s%s" % (w, c, cov, st, flag))
            if st == "GAP":
                gaps.append(w)
        print("  GAP-terms:", ", ".join(gaps[:12]) if gaps else "none")
