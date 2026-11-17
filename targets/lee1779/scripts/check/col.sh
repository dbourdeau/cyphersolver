#!/bin/zsh
# col.sh page col [top bottom] -> crops 1776 page column into verify/tmp/col_<page><col>.jpg
V="${VERIFY_DIR:-.}"
P="${ENTICK_1776_PAGES:-sources/raw/entick_dictionary/bim_eighteenth-century_the-new-spelling-diction_entick-john_1776/pages}"
f=$(ls $P | grep "^p$(printf %03d $1)_")
t=${3:-0.07}; b=${4:-0.95}
if [ "$2" = a ]; then x0=0.0; x1=0.56; else x0=0.44; x1=1.0; fi
cd "$V/scripts"; python3 crop.py "$P/$f" "$V/tmp/col_$1$2.jpg" $x0 $t $x1 $b ${5:-850}
