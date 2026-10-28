#!/usr/bin/env python3
"""Audit: for each verse, check if book body contains distinctive technical
terms (Bhaskara, Ksemaraja, specific mala names, etc.) that our B clips
don't cover. Output: per-verse gap list."""
import json

BASE = "/home/ubuntu/shiva-sutras"
tpl = {t["verse"]: t for t in json.load(open(BASE + "/standard/template_77.json"))}

def fold(s):
    return "".join(c for c in s if ord(c) < 128).lower()

# Distinctive terms per verse (from the book's scholarly apparatus)
gaps = {}
for v, t in tpl.items():
    body = fold(t.get("body", ""))
    d = json.load(open(BASE + "/build/std_%s.json" % v.replace(".", "_")))
    B = d["layers"].get("B", [])
    buids = " ".join([x.get("uid", "") + " " + x.get("why", "") for x in B]).lower()
    
    # Sharp technical points that Dyczkowski makes
    sharp = []
    if "bhaskara" in body and "bhaskara" not in buids:
        sharp.append("Bhaskara reading")
    if "ksemaraja" in body and "ksemaraja" not in buids:
        sharp.append("Ksemaraja reading")
    if "mayiyamala" in body and "mayiyamala" not in buids:
        sharp.append("mayiyamala")
    if "anavamala" in body and "anavamala" not in buids:
        sharp.append("anavamala")
    if "karmamala" in body and "karmamala" not in buids:
        sharp.append("karmamala")
    if "kancuka" in body and "kancuka" not in buids:
        sharp.append("kancuka")
    if "guha" in body and "guha" not in buids:
        sharp.append("guha")
    if "granthi" in body and "granthi" not in buids:
        sharp.append("granthi")
    if "jagadyoni" in body and "jagadyoni" not in buids:
        sharp.append("jagadyoni")
    if "timirodghatta" in body and "timirodghatta" not in buids:
        sharp.append("timirodghatta")
    if "malini" in body and "malini" not in buids:
        sharp.append("malini")
    if "svacchanda" in body and "svacchanda" not in buids:
        sharp.append("svacchanda")
    if "spanda" in body and "spanda" not in buids:
        sharp.append("spanda")
    if "svatantrya" in body and "svatantrya" not in buids:
        sharp.append("svatantrya")
    if "svaprakasa" in body and "svaprakasa" not in buids:
        sharp.append("svaprakasa")
    if "akalpita" in body and "akalpita" not in buids:
        sharp.append("akalpita")
    if "kundalini" in body and "kundalini" not in buids:
        sharp.append("kundalini")
    if "brahmarandhra" in body and "brahmarandhra" not in buids:
        sharp.append("brahmarandhra")
    if "pithesvari" in body and "pithesvari" not in buids:
        sharp.append("pithesvari")
    if "vacya" in body and "vacya" not in buids:
        sharp.append("vacya")
    if "vacaka" in body and "vacaka" not in buids:
        sharp.append("vacaka")
    if "vyoman" in body and "vyoman" not in buids:
        sharp.append("vyoman")
    if "samadhana" in body and "samadhana" not in buids:
        sharp.append("samadhana")
    if "sthiti" in body and "sthiti" not in buids:
        sharp.append("sthiti")
    if "vyutthana" in body and "vyutthana" not in buids:
        sharp.append("vyutthana")
    if "prasava" in body and "prasava" not in buids:
        sharp.append("prasava")
    if "madhye" in body and "madhye" not in buids:
        sharp.append("madhye")
    if "samyama" in body and "samyama" not in buids:
        sharp.append("samyama")
    if "visharga" in body and "visharga" not in buids:
        sharp.append("visharga")
    if "kalakala" in body and "kalakala" not in buids:
        sharp.append("kalakala")
    if "asuddhasrsti" in body and "asuddhasrsti" not in buids:
        sharp.append("asuddhasrsti")
    if "saksat" in body and "saksat" not in buids:
        sharp.append("saksat")
    
    if sharp:
        gaps[v] = sharp

for v, sharp in sorted(gaps.items()):
    print("%s: %s" % (v, ", ".join(sharp)))
print("\nTotal verses with gaps: %d / 77" % len(gaps))
