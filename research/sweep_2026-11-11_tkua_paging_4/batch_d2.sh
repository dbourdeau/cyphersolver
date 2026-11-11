#!/bin/bash
# worker 2: 17th-century relation units no pass has sheeted (1 image in 4)
cd /home/user/cyphersolver/research/sweep_2026-11-11_tkua_paging_4
O=/tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a5d/sh
for b in 261193 261194 260775 260771 261083 260689 261037 262113 261417 260933 260687 261027 260895; do python3 ao.py sheet $b $O 4 400 4 5; done
