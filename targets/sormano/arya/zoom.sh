#!/bin/zsh
# Fetch a IIIF region of one opening, upscaled, for reading glyphs by eye.
# usage: ./zoom.sh CANVAS X Y W H OUTNAME [OUTWIDTH]
ARK=btv1b9060015d
n=$1; x=$2; y=$3; w=$4; h=$5; name=$6; ow=${7:-3600}
mkdir -p crops
out="crops/z${n}_${name}.jpg"
curl -sL -A 'Mozilla/5.0' --retry 4 --retry-delay 2 -m 240 \
  -o "$out" "https://gallica.bnf.fr/iiif/ark:/12148/$ARK/f$n/$x,$y,$w,$h/$ow,/0/native.jpg"
echo "$out $(sips -g pixelWidth -g pixelHeight "$out" | awk '/pixel/{printf "%s ", $2}')"
