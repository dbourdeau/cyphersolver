#!/bin/sh
cd "$(dirname "$0")"
( for x in "R0001372 317" "R0001374 258" "R0001376 333" "R0001378 402" "R0001380 381"; do python3 dl.py $x; done ) &
( for x in "R0001373 289" "R0001375 295" "R0001377 328" "R0001379 397" "R0001381 393"; do python3 dl.py $x; done ) &
wait
