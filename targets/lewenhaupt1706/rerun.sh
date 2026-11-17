#!/bin/sh
# Reruns the single pre-registered measurement v2 (protocol/PREREG-v2.md) with the files as filed here.
# Expected output: protocol/MEASURE-v2.json (N_K2 0.6954, permuted-key controls max 0.2942).
cd "$(dirname "$0")/corpus" || exit 1
python3 -I ../tools/measure2.py ../key/key_K2_frozen.json calib_UR.json Lx.txt \
  ../transcription/L3_A_301.txt ../transcription/L3_A_302L.txt ../transcription/L3_A_302R.txt \
  ../transcription/L3_A_303L.txt ../transcription/L3_A_303R.txt
