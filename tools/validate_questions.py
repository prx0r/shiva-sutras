#!/usr/bin/env python3
"""G0 gate for the Siva Sutras project — port of vatulanatha validate_questions.py.
Same law, our anchor: every question varies on S1's topic (1.1 = consciousness/self),
not a generic. Standalone, <=9 words, explicit content noun, no unresolved pronouns.
Usage: python3 tools/validate_questions.py ["Q1?" "Q2?" ...]  (no args = check ESSAY0 set)
Exit 0 = all pass, 1 = failures (loud)."""
import re, sys

CONTENT = {  # explicit domain nouns — a question must name one
 'consciousness','conscious','self','atman','mind','mantra','bondage','knowledge',
 'thought','thinking','senses','sense','body','power','energy','awareness','guru',
 'practice','meditation','freedom','liberation','liberated','highest','supreme',
 'state','universe','world','experience','nature','essence','reality','real',
 'universal','individual','subject','object','duality','nonduality','means','way',
 'path','sudden','spontaneous','effort','silence','void','heart','breath','sutra',
 'yogi','shiva','grace','devotion','wisdom','ignorance','veiling',
 'realisation','realization','realised','realized','realise','realize',
}
PRONOUNS = {'it','this','that','these','those','them','they','he','she','his','her'}
ANCHOR = {'consciousness','conscious','self','atman','samvit','realisation','realization'}  # S1 (1.1) topic — realisation = realisation-of-consciousness, the corpus verb (their gate: realisation|self)
OBJLESS_HINT = re.compile(r'\b(happen|happens|do it|does it|make it|go|goes|end up|turn out)\b', re.I)

def words(q): return re.findall(r"[A-Za-z']+", q)

def check(q):
    fails = []
    ws = words(q); low = [w.lower().strip("'") for w in ws]
    if not q.strip().endswith('?'): fails.append("no '?'")
    if not low or low[0] not in {'what','why','how','where','which','who','when','is','are','was',
                                 'can','could','do','does','did','should','would','has','have','may'}:
        fails.append("not interrogative form")
    if len(ws) > 9: fails.append(f"verbose ({len(ws)} words > 9)")
    if not [w for w in low if w in ANCHOR]:
        fails.append("no consciousness-anchor (must vary on S1's topic, not drift generic)")
    if not [w for w in low if w in CONTENT or w.rstrip('s') in CONTENT]:
        fails.append("no explicit content noun (vague/context-dependent)")
    pron = [w for w in low if w in PRONOUNS]
    if pron: fails.append(f"unresolved pronoun(s): {','.join(sorted(set(pron)))}")
    if OBJLESS_HINT.search(q) and not [w for w in low if w in CONTENT]:
        fails.append("objectless verb (make what happen?)")
    return fails

ESSAY0_SET = [
 "What is consciousness?",
 "Why does knowledge bind consciousness?",
 "Why can't you force realisation?",
 "What does consciousness do to experience?",
 "How does the mind shape consciousness?",
 "What is consciousness free to do?",
 "Why isn't consciousness something you do?",
]

if __name__ == '__main__':
    qs = sys.argv[1:] or ESSAY0_SET
    bad = 0
    for q in qs:
        f = check(q)
        mark = 'FAIL' if f else 'PASS'
        if f: bad += 1
        print(f"  {mark}  {q}" + ("" if not f else "   -> " + "; ".join(f)))
    print(f"{len(qs)-bad}/{len(qs)} pass")
    sys.exit(1 if bad else 0)
