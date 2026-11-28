#!/bin/sh
# After the plan: the solver on the whole text (lines 1-12 of transcription_frozen.txt) with each language model,
# seed 2, 12 restarts. Output: per language the JSON line (score per letter, key) and the decode.
cd "$(dirname "$0")"
for L in la da de nl; do echo "== $L"; VIND_LANG=$L python3 -I solve.py 1-12 2 12; done
