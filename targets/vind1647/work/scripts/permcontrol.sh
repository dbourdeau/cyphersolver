#!/bin/sh
# Plan's second control: the solver on 20 random permutations of the cipher letters (word lengths kept); compare with the true solve.
cd "$(dirname "$0")"
for L in la da; do
  echo "== $L true"; VIND_LANG=$L python3 -I solve.py 1-12 2 12 | head -1 | python3 -c "import sys,json;print(json.loads(sys.stdin.read())['score_per_letter'])"
  for s in $(seq 101 120); do VIND_LANG=$L python3 -I solve.py 1-12 $s 12 perm | head -1 | python3 -c "import sys,json;print(json.loads(sys.stdin.read())['score_per_letter'])"; done | sort -n | tr '\n' ' '; echo
done
