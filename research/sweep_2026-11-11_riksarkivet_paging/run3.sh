#!/bin/sh
# Stedingk despatch drafts / Petersburg papers and Ericsberg autograph volumes: 24-image samples, after the 1133.08 downloads thin out
cd "$(dirname "$0")"
while pgrep -f "dl.py R000137[67]" >/dev/null; do sleep 10; done
for m in 90003434 90003435 90003441 90003446 90003391 90003530 A0040327 A0040331 A0040337 A0040345 A0040351 A0040360 90003536 90003397 A0040243 A0040123; do
  echo "$m" >> sheets3.log; python3 rik.py sheet $m 24 >> sheets3.log 2>&1
done
