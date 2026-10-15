#!/bin/zsh
# Fetch openings of BnF fr. 3096 (ark btv1b9060015d) from Gallica's IIIF service.
# Each canvas is one microfilm frame of a double-page opening (9120 x 6250 px).
# usage: ./fetch.sh FIRST LAST [width|full]
ARK=btv1b9060015d
A=$1; B=$2; S=${3:-full}
mkdir -p img
if [ "$S" = "full" ]; then SZ=full; else SZ="$S,"; fi
for n in $(seq $A $B); do
  out=$(printf "img/f%04d_%s.jpg" $n $S)
  if [ -s "$out" ] && [ $(stat -f%z "$out") -gt 20000 ]; then continue; fi
  curl -sL -A 'Mozilla/5.0' --retry 4 --retry-delay 2 -m 180 \
    -o "$out" "https://gallica.bnf.fr/iiif/ark:/12148/$ARK/f$n/full/$SZ/0/native.jpg"
  echo "$out $(stat -f%z "$out" 2>/dev/null)"
  sleep 0.3
done
