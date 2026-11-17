#!/bin/sh
# MESURE UNIQUE D — ne lancer qu'une fois, après gel de PREREG-D2.
D=/Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/bellievre-matignon-1584
python3 -I $D/scripts/decode.py $D/key_D.tsv $D/transcription/f24_portion_final.txt > $D/mesure/f24D_decoded.txt
cd /private/tmp/claude-502/-Users-bdudout-Documents-CyberRisk-CyberRisk/48b5b555-43ba-4dab-b206-39e14df98bcc/scratchpad && python3 /Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/matignon-1584-f151/daniel_tools/targets/matignon1586c3/f276/scripts/measure.py $D/mesure/f24D_decoded.txt 200 > $D/mesure/RESULTAT.txt 2>&1
cat $D/mesure/RESULTAT.txt
