#!/bin/bash
# $1 infile $2 tag $3 shuffle $4 iters $5 restarts $6 tol ; k1 15..30 in parallel
for k1 in $(seq 15 30); do ./kpw $1 $k1 $k1 15 32 $4 $5 $6 $((k1*7+$3)) $3 > g_$2_$k1.txt & 
  if (( k1 % 8 == 6 )); then wait; fi; done; wait; cat g_$2_*.txt > grid_$2.txt
