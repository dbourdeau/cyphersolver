#!/bin/sh
# MESURE UNIQUE — ne lancer qu'une fois, après gel de PREREG-B.
D=/Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/matignon-1584-f151
python3 -I $D/scripts/decode.py $D/key_frozen.tsv $D/transcription/holdout_final.txt > $D/mesure/holdout_decoded.txt
python3 $D/daniel_tools/targets/matignon1586c3/f276/scripts/measure.py $D/mesure/holdout_decoded.txt 200 > $D/mesure/RESULTAT.txt 2>&1
cat $D/mesure/RESULTAT.txt
