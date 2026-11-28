#!/bin/bash
# zoom.sh <canvas> <y0> <y1> <tag>: fetch left and right half-width full-resolution crops of rows y0..y1, scaled to 2000 px wide.
D=/home/claude/keyless/round40c/basel_anv9
n=$1; y0=$2; y1=$3; tag=$4
if [ $n -ge 199 ] && [ $n -le 206 ] && [ ! -f $D/FREEZE_KEY.txt ]; then echo "quarantined canvas $n"; exit 1; fi
pid=$(awk -F'\t' -v n=$n '$1==n{print $2}' $D/work/canvases.tsv)
W=$(awk -F'\t' -v n=$n '$1==n{split($5,a,"x");print a[1]}' $D/work/canvases.tsv)
h=$((y1-y0)); half=$((W/2))
mkdir -p $D/work/zoom
for side in L R; do
  if [ $side = L ]; then x=300; w=$((half-300+250)); else x=$((half-250)); w=$((W-x-150)); fi
  u="https://www.e-manuscripta.ch/i3f/v20/$pid/$x,$y0,$w,$h/2000,/0/default.jpg"
  out=$D/work/zoom/c$(printf %03d $n)_${tag}_$side.jpg
  [ -s $out ] || { r=$(curl -s -m 120 -A "Mozilla/5.0" -o $out -w "%{http_code} %{size_download}" "$u"); printf "%s\tcanvas %s region\t%s\t%s\n" "$(date -u +%FT%TZ)" $n "$u" "$r" >> $D/FETCH_LOG.txt; sleep 1; }
  echo $out
done
