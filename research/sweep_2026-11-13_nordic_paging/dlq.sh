#!/bin/sh
# usage: dlq.sh "man n" ...   (sequential downloads)
cd "$(dirname "$0")"
export RIK_SP=/tmp/claude-0/-home-user-cyphersolver/6cad9ef2-f4c1-5b63-a0df-f48b5a524c6f/scratchpad/nordic
for x in "$@"; do python3 dl.py $x; done
