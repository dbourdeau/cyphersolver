#!/bin/sh
# MESURE UNIQUE C — ne lancer qu'une fois, après gel de PREREG-C2.
D=/Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/matignon-1584-f151
python3 -I $D/scripts/decode.py $D/key_C.tsv $D/transcription/holdout_C_final.txt > $D/mesure_C/holdoutC_decoded.txt
cd /private/tmp/claude-502/-Users-bdudout-Documents-CyberRisk-CyberRisk/48b5b555-43ba-4dab-b206-39e14df98bcc/scratchpad && python3 $D/daniel_tools/targets/matignon1586c3/f276/scripts/measure.py $D/mesure_C/holdoutC_decoded.txt 200 > $D/mesure_C/RESULTAT.txt 2>&1
cat $D/mesure_C/RESULTAT.txt
