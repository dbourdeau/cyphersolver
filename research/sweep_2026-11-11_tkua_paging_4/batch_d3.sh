#!/bin/bash
# worker 3: journal B tail again, then 1690s relations and envoy-archive units not yet sheeted (1 image in 4)
cd /home/user/cyphersolver/research/sweep_2026-11-11_tkua_paging_4
O=/tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a5d/sh
python3 ao.py sheet 673415 $O 4 400 4 5 880 936
for b in 262316 262315 262112 262317 261581 261582 261585 261586 261594 260777 260779 260781 260783 260786; do python3 ao.py sheet $b $O 4 400 4 5; done
