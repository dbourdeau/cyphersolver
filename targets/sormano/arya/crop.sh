#!/bin/zsh
# Crop a horizontal band out of a fetched page image with sips.
# usage: ./crop.sh IMG Y H [X W] [outname]
img=$1; y=$2; h=$3; x=${4:-0}; w=${5:-0}
base=$(basename $img .jpg)
if [ "$w" -eq 0 ]; then w=$(sips -g pixelWidth "$img" | awk '/pixelWidth/{print $2}'); fi
out="crops/${base}_y${y}.jpg"
mkdir -p crops
sips -c $h $w --cropOffset $y $x "$img" --out "$out" >/dev/null 2>&1
echo "$out $(sips -g pixelWidth -g pixelHeight "$out" | awk '/pixel/{printf "%s ", $2}')"
