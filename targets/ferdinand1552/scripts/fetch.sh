#!/bin/bash
# one request at a time, 1s apart, honest UA
B='https://digitallibrary.unicatt.it/iiif/3/veneranda&SEPdata&SEPpublic&SEPcontents&SEP0b&SEP02&SEPda&SEP82&SEP80&SEP27&SEPc8&SEPd4&SEP'
for f in "$@"; do
 num=${f%[rv]}; s=${f: -1}
 n=$((2*(num-10)+21)); [ $s = v ] && n=$((n+1))
 id=$(printf "%04d" $n)
 code=$(curl -s -A WAINUT-research -o scans/c$f.jpg -w "%{http_code}" "${B}${id}_G275inf._c.${f}.jp2/full/max/0/default.jpg")
 echo "$f $id $code $(stat -c %s scans/c$f.jpg)"; [ "$code" = 429 ] && break; sleep 1
done
