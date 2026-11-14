#!/bin/sh
# Re-run the single pre-registered measurement of 14 Nov 2026 (1379,14-18 cipher image 06) and check it byte for byte.
# Usage, from this folder:  sh rerun.sh        (Python 3, standard library only; about one minute)
set -e
cd "$(dirname "$0")"
shasum -a 256 -c SHA256SUMS
python3 -I score_atlas.py K4.tsv img06_ARB.txt clear_1547_ref_img06.txt > rerun_out.txt
python3 -I score_k4.py K4.tsv img06_ARB.txt clear_1547_ref_img06.txt | head -n 3 >> rerun_out.txt
if cmp -s rerun_out.txt MESURE-P-ATLAS.txt; then
  echo "OK: rerun_out.txt is byte-identical to MESURE-P-ATLAS.txt"; grep '^score=\|^témoins\|^VERDICT' rerun_out.txt
else
  echo "DIFFERENT"; diff rerun_out.txt MESURE-P-ATLAS.txt | head; exit 1
fi
