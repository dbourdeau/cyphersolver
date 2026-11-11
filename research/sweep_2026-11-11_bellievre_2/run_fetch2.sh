#!/bin/bash
# second resumable loop (other end of the queue, slower): bash run_fetch2.sh <scratch>. With run_fetch.sh the two together stay near one request per 2 s.
S=$1; cd "$(dirname "$0")"
for v in 15890 15898b 15898a; do
  until grep -q "DONE $v" $S/fetch.log $S/fetch2.log 2>/dev/null; do
    grep -q BLOCK $S/fetch.log $S/fetch2.log 2>/dev/null && exit
    FETCH_SLEEP=1.2 python3 fetch_all.py $S $v >> $S/fetch2.log 2>&1; sleep 5
  done
done
