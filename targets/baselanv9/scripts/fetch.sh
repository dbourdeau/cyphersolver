#!/bin/bash
# Plain-curl fetch of e-manuscripta IIIF images, 2000 px wide, sequential and polite.
# Usage: fetch.sh <first canvas> <last canvas>   (canvas numbers from work/canvases.tsv)
# Canvases 199-206 (ff. 97-99 area: the pasted key leaves per Steinmann) are QUARANTINED until FREEZE_KEY exists.
D=/home/claude/keyless/round40c/basel_anv9
LOG=$D/FETCH_LOG.txt
for n in $(seq $1 $2); do
  if [ $n -ge 199 ] && [ $n -le 206 ] && [ ! -f $D/FREEZE_KEY.txt ]; then echo "skip quarantined canvas $n"; continue; fi
  pid=$(awk -F'\t' -v n=$n '$1==n{print $2}' $D/work/canvases.tsv)
  out=$D/img/p2000/c$(printf %03d $n)_$pid.jpg
  [ -s "$out" ] && continue
  u="https://www.e-manuscripta.ch/i3f/v20/$pid/full/2000,/0/default.jpg"
  r=$(curl -s -m 120 -A "Mozilla/5.0" -o "$out" -w "%{http_code} %{content_type} %{size_download}" "$u")
  s=$(sha1sum "$out" | cut -c1-40)
  echo -e "$(date -u +%FT%TZ)\tcanvas $n\t$u\t$r\tsha1 $s" >> $LOG
  case "$r" in 200\ image/jpeg*) ;; *) echo "PROBLEM canvas $n: $r"; head -c 400 "$out"; echo;; esac
  sleep 1
done
