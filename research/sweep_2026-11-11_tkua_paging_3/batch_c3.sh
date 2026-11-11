#!/bin/bash
# restart after the stop: what batch_c/batch_c2 had not sheeted
cd /home/user/cyphersolver/research/sweep_2026-11-11_tkua_paging_3
O=/tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a5c/sh
for b in 673416 261574 261490 262100 262105 262102; do python3 ao.py sheet $b $O 4 400 4 5; done
python3 ao.py sheet 261383 $O 4 400 4 5 192
