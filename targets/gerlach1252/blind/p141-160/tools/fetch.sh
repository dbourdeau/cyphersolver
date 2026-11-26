#!/bin/bash
# usage: fetch.sh BATCH SCAN   -> gerlach_next/BATCH/img/scanSCAN.jpg, logged in gerlach_next/FETCH_LOG.txt
B=$1; S=$2; D=/home/claude/gerlach_next
u="https://iiif.wellcomecollection.org/image/b19695561_${S}.jp2/full/2000,/0/default.jpg"
code=$(curl -sS -o $D/$B/img/scan$S.jpg -w '%{http_code}' "$u")
echo "$(date -u +%FT%TZ) GET $u http=$code md5=$(md5sum $D/$B/img/scan$S.jpg|cut -c1-32) bytes=$(stat -c%s $D/$B/img/scan$S.jpg) -> $B/img/scan$S.jpg" >> $D/FETCH_LOG.txt
sleep 2
