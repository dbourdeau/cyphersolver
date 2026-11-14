#!/bin/bash
cd "$(dirname "$0")"
while kill -0 3491 2>/dev/null; do sleep 15; done
python3 na_run2.py > na_run2.log 2>&1
for e in 1.05.14 1.02.21.01 1.02.21.02 2.01.28.01 2.05.22 1.05.06 1.05.01.02 1.03.01 1.05.01.01; do python3 dump_ead.py $e dumps/ead_$e.jsonl; done > dump.log 2>&1
