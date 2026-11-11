#!/bin/bash
# list sheets not yet marked viewed; "new.sh mark" marks all current as viewed
cd /tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a5d/sh; touch ../viewed.txt
if [ "$1" = mark ]; then shift; for f in "$@"; do echo $f >> ../viewed.txt; done; else ls | grep -v -x -F -f ../viewed.txt | sed 's/.jpg//' | tr '\n' ' '; fi
