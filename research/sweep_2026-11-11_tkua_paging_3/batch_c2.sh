#!/bin/bash
# second worker for batch_c.sh: the same list from the far end (existing sheets are skipped)
cd /home/user/cyphersolver/research/sweep_2026-11-11_tkua_paging_3
O=/tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a5c/sh
for b in 261593 261584 673415 673416 261574 261490 262105 262102 262100 260651 260649 261377 261381; do python3 ao.py sheet $b $O 4 400 4 5; done
