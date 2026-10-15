#!/bin/zsh
# Fetch a IIIF region of one opening of BnF fr. 3096 at full resolution.
# usage: ./region.sh CANVAS X,Y,W,H [outname] [size]
ARK=btv1b9060015d
n=$1; reg=$2; name=${3:-r}; sz=${4:-full}
mkdir -p img
out="img/f${n}_${name}.jpg"
curl -sL -A 'Mozilla/5.0' --retry 4 --retry-delay 2 -m 240 \
  -o "$out" "https://gallica.bnf.fr/iiif/ark:/12148/$ARK/f$n/$reg/$sz/0/native.jpg"
echo "$out $(stat -f%z "$out" 2>/dev/null)"
