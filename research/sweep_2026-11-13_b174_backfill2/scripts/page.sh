#!/bin/bash
# page.sh filza maxpos : native 1272 px to scratch/nFFF via ASF IIIF (plain curl), then det4 -> scratch/dFFF.tsv
U="https://archiviodistatofirenze.cultura.gov.it/iipsrv/iipsrv.fcgi"
B=/home/claude/en/trackB/b174_backfill2
f=$(printf %03d $1); d=$B/scratch/n$f; mkdir -p $d
seq 1 $2 | xargs -P 3 -I{} bash -c 'n=$(printf %07d {}); o='$d'/q$n.jpg; [ -s $o ] || curl -sS -m 120 "'$U'?FIF=/data/iip-data/asfi/mediceo_avanti_principato/00100'$f'/A$n.ptif&QLT=85&WID=1272&CVT=jpeg" -o $o 2>/dev/null; s=$(stat -c%s $o 2>/dev/null||echo 0); [ $s -lt 5000 ] && rm -f $o; true'
echo "$f images: $(ls $d | wc -l) size: $(du -sh $d|cut -f1)"
python3 -I $B/scripts/det4.py $d > $B/scratch/d$f.tsv
echo "$f det done $(wc -l < $B/scratch/d$f.tsv)"
