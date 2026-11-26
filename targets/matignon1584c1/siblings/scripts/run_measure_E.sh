#!/bin/sh
# MESURE UNIQUE E (E1 puis E2) — ne lancer qu'une fois, après gel de PREREG-E2.
D=/Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/bellievre-matignon-1584
X=$D/sisters
M=/Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/matignon-1584-f151/daniel_tools/targets/matignon1586c3/f276/scripts/measure.py
for P in E1 E2; do
  python3 -I $D/scripts/decode.py $D/key_D.tsv $X/transcription/${P}_portion_final.txt > $X/mesure/${P}_decoded.txt
  (cd /private/tmp/claude-502/-Users-bdudout-Documents-CyberRisk-CyberRisk/48b5b555-43ba-4dab-b206-39e14df98bcc/scratchpad && python3 $M $X/mesure/${P}_decoded.txt 200 > $X/mesure/RESULTAT_${P}.txt 2>&1)
  echo "== $P"; cat $X/mesure/RESULTAT_${P}.txt
done
