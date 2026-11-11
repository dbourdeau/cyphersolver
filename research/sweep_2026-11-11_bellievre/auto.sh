#!/bin/bash
# ranks each volume once its fetch is DONE; scale 0.5 / threshold 24 for colour single-page scans
S=$1; cd "$(dirname "$0")"
for v in 15903b 15903a 15902 15894 15897 15898a 15898b 15890; do
  until grep -q "DONE $v\|BLOCK" $S/fetch.log; do sleep 20; done
  grep -q "DONE $v" $S/fetch.log || exit
  mode=$(python3 -c "from PIL import Image;im=Image.open('$S/$v/c0050.jpg');print('C' if im.height>im.width else 'M')")
  if [ $mode = C ]; then python3 rank.py $S/$v 24 0.5 > $S/rank_$v.log 2>&1; else python3 rank.py $S/$v 20 > $S/rank_$v.log 2>&1; fi
done
