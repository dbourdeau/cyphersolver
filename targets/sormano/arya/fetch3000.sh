#!/bin/zsh
# Fetch pages of BnF fr. 3000 (ark btv1b9060027m) from Gallica IIIF. usage: ./fetch3000.sh CANVAS [width] [region]
ARK=btv1b9060027m
n=$1; W=${2:-1600}; REG=${3:-full}
mkdir -p img3000
out="img3000/f${n}_${W}.jpg"
curl -sL -A 'Mozilla/5.0' --retry 4 -m 240 -o "$out" "https://gallica.bnf.fr/iiif/ark:/12148/$ARK/f$n/$REG/$W,/0/native.jpg"
echo "$out $(stat -f%z "$out" 2>/dev/null)"
