#!/bin/sh
# Re-run the two pre-registered measurements and check them byte for byte:
#   1. 14 Nov 2026, 1379,14-18 cipher image 06 (files in this folder, recorded in MESURE-P-ATLAS.txt);
#   2. 15 Nov 2026, 1379,14-18 cipher image 04 (files in img04/, recorded in img04/MESURE-312d-IMG04.txt).
# Usage, from this folder:  sh rerun.sh        (Python 3, standard library only; a few minutes)
set -e
cd "$(dirname "$0")"
echo "== image 06 (14 Nov)"
shasum -a 256 -c SHA256SUMS
python3 -I score_atlas.py K4.tsv img06_ARB.txt clear_1547_ref_img06.txt > rerun_out.txt
python3 -I score_k4.py K4.tsv img06_ARB.txt clear_1547_ref_img06.txt | head -n 3 >> rerun_out.txt
if cmp -s rerun_out.txt MESURE-P-ATLAS.txt; then
  echo "OK: rerun_out.txt is byte-identical to MESURE-P-ATLAS.txt"; grep '^score=\|^témoins\|^VERDICT' rerun_out.txt
else
  echo "DIFFERENT"; diff rerun_out.txt MESURE-P-ATLAS.txt | head; exit 1
fi
echo "== image 04 (15 Nov)"
cd img04
shasum -a 256 -c SHA256SUMS
T=img04_ARB.txt; C=clear_1547_ref_img04_joined.txt
{ echo "== score_atlas.py K5"; python3 -I score_atlas.py K5.tsv $T $C
  echo "== score_k4.py K5"; python3 -I score_k4.py K5.tsv $T $C | head -n 3
  echo "== score_atlas.py K4 (comparaison)"; python3 -I score_atlas.py K4.tsv $T $C | head -n 6; } > rerun_out.txt
# the recorded file = 4 comment lines (#) written at the time + this output
if grep -v '^#' MESURE-312d-IMG04.txt | cmp -s - rerun_out.txt; then
  echo "OK: rerun_out.txt is byte-identical to MESURE-312d-IMG04.txt (comment lines aside)"; grep '^==\|^score=\|^VERDICT' rerun_out.txt
else
  echo "DIFFERENT"; grep -v '^#' MESURE-312d-IMG04.txt | diff rerun_out.txt - | head; exit 1
fi
