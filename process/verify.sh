#!/usr/bin/env bash
# verify.sh — one-command audit. ALL PASS or stop. Run before every commit
# touching build outputs, and after any unit/grade change.
set -u
cd "$(dirname "$0")/.."
fail=0

echo "== G1 units verify =="
python3 tools/verify_units.py || fail=1

echo "== G0 questions =="
python3 tools/validate_questions.py || fail=1

echo "== plain hash =="
python3 tools/plain_filter.py --check || fail=1

echo "== totals reconcile (units == SPINE_ASSIGN rows) =="
n_units=$(grep -h -c '^### \(ss\|dl\)' excavations/ss*.md excavations/dl*.md | paste -sd+ | bc)
n_assign=$(($(wc -l < excavations/SPINE_ASSIGN.tsv) - 1))
echo "units=$n_units assign=$n_assign"
[ "$n_units" = "$n_assign" ] || { echo "MISMATCH"; fail=1; }

echo "== ledger covers pass-1 uids (fallback=pass1-manual) =="
missing=$(python3 - <<'EOF'
import re
assign = {}
for l in open('excavations/SPINE_ASSIGN.tsv').read().splitlines()[1:]:
    if l.strip():
        f = l.split('\t')
        assign[f[0]] = f[6] if len(f) > 6 else ''
led = open('excavations/COVERAGE_LEDGER.tsv').read()
p1 = [u for u, f in assign.items() if f == 'pass1-manual']
miss = sorted(u for u in p1 if re.search(r'\b' + re.escape(u) + r'\b', led) is None)
print(len(p1), "pass1-manual;", len(miss), "missing:", " ".join(miss[:10]))
EOF
)
echo "$missing"
echo "$missing" | grep -q "; 0 missing" || fail=1

echo "== file presence (manifests, keys, sheets) =="
for f in build/manifest_s1_A.json build/manifest_s6_C.json build/holdup_verdicts.json \
         build/key_ss1_proposal.json build/plain_essay0.json excavations/SPINE_ASSIGN.tsv; do
  [ -f "$f" ] || { echo "ABSENT: $f"; fail=1; }
done

if [ "$fail" = 0 ]; then echo "ALL PASS"; else echo "FAIL — stop the line"; exit 1; fi
