#!/bin/bash
# page.sh filza maxpos : native-ish 1272 px via ASF IIIF (plain curl, 4 parallel) -> scratch/nFFF, then det.py -> scratch/dFFF.tsv
U="https://archiviodistatofirenze.cultura.gov.it/iipsrv/iipsrv.fcgi"
B=/tmp/claude-0/-home-user-cyphersolver/6cad9ef2-f4c1-5b63-a0df-f48b5a524c6f/scratchpad/map
H=/home/user/cyphersolver/research/sweep_2026-11-13_map_paging/scripts
f=$(printf %03d $1); d=$B/n$f; mkdir -p $d
seq 1 $2 | xargs -P 4 -I{} bash -c 'n=$(printf %07d {}); o='$d'/q$n.jpg; [ -s $o ] || curl -sS -m 120 "'$U'?FIF=/data/iip-data/asfi/mediceo_avanti_principato/00100'$f'/A$n.ptif&QLT=80&WID=1272&CVT=jpeg" -o $o 2>/dev/null; s=$(stat -c%s $o 2>/dev/null||echo 0); [ $s -lt 5000 ] && rm -f $o; true'
echo "$f images: $(ls $d | wc -l) size: $(du -sh $d|cut -f1)"
python3 -I $H/det.py $d > $B/d$f.tsv
echo "$f det done $(wc -l < $B/d$f.tsv)"
