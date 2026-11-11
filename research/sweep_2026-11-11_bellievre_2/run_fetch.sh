#!/bin/bash
# resumable fetch loop: bash run_fetch.sh <scratch> ; restarts fetch_all.py until every volume is DONE or a BLOCK is logged
S=$1; cd "$(dirname "$0")"
for v in 15894 15897 15898a 15898b 15890; do
  until grep -q "DONE $v" $S/fetch.log $S/fetch2.log 2>/dev/null; do
    grep -q BLOCK $S/fetch.log 2>/dev/null && exit
    python3 fetch_all.py $S $v >> $S/fetch.log 2>&1; sleep 5
  done
done
